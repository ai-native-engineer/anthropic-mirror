"""Anthropic Academy 영상 코스 전사 (자막).

영상 레슨은 텍스트 본문이 없어 academy-extract.py가 스킵한다. 이 스크립트는 레슨별 영상 자막을 전사한다.
영상 플레이어가 코스마다 다르다:
- youtube iframe (claude-code-101 등): yt-dlp로 자동자막(en) 추출.
- JWPlayer (MCP 코스 등): jwplayer().getPlaylistItem().tracks의 English captions(.srt, 수동 제작이라 고품질)를 다운로드.

함정:
- 레슨별 영상은 playwright로 렌더 후 잡아야 한다(httpx raw HTML엔 코스 전체 embed가 섞임).
  youtube는 "보이는 iframe"(width/height>50), JWPlayer는 재생 트리거 후 jwplayer API로 tracks 조회.
- 자막 .srt는 cdn.jwplayer.com에서 301 리다이렉트되므로 follow 필요(urllib 기본 follow).
- 쿠키 만료 시 비로그인 -> 레슨 ID가 안 잡힘 -> login-academy.py 재실행.

실행: <crawl4ai python> academy-video.py <out_dir> [course-slug ...]
  코스 슬러그 생략 시 카탈로그(/)에서 자동 수집.
  모든 레슨을 검사하고 실제 본문 변경·새 영상 ID만 저장/전사.
  출력: <out_dir>/anthropic.skilljar.com/<course>/<NN>-<title>.md (academy-extract와 같은 트리)
"""

import asyncio, hashlib, html, json, os, re, subprocess, sys, tempfile, time, urllib.request
from urllib.parse import urlsplit
import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from pathlib import Path
from playwright.async_api import async_playwright

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
BASE = os.environ.get("SKILLJAR_BASE", "https://anthropic.skilljar.com").rstrip("/")
_HOST = BASE.split("://")[-1]
STATE = os.path.expanduser(
    "~/.crawl4ai/academy_state.json"
    if _HOST == "anthropic.skilljar.com"
    else f"~/.crawl4ai/skilljar-{_HOST}.json"
)
# youtube 자막은 youtube-digest의 extract_transcript.sh를 재사용(크롬 쿠키로 429 회피 + 수동자막 우선). raw yt-dlp 직접 호출 금지.
YOUTUBE_DIGEST_SCRIPTS_DIR = os.environ.get(
    "YOUTUBE_DIGEST_SCRIPTS_DIR",
    os.path.expanduser("~/.agents/skills/shared/youtube/youtube-digest/scripts"),
)
EXTRACT = os.path.join(YOUTUBE_DIGEST_SCRIPTS_DIR, "extract_transcript.sh")
STATE_FILE = ".anthropic-mirror-state.json"


def expired_session(cookies, now=None):
    """저장된 sj_sessionid가 모두 만료됐는가. 만료 시각이 없는 세션 쿠키는 유효로 본다."""
    now = time.time() if now is None else now
    sess = [c for c in cookies if c.get("name") == "sj_sessionid"]
    if not sess:
        return True
    return all(0 < c.get("expires", -1) < now for c in sess)


def slug(t):
    t = re.sub(r"[^\w\s-]", "", t).strip().lower()
    return re.sub(r"\s+", "-", t)[:45] or "lesson"


def youtube_refs(srcs):
    refs = []
    for src in srcs:
        m = re.search(r"/embed/([\w-]{11})", src)
        ref = ("yt", m.group(1)) if m else None
        if ref and ref not in refs:
            refs.append(ref)
    return refs


def unseen_refs(existing, refs):
    return [
        ref
        for ref in refs
        if (
            f"<!-- youtube: {ref[1]} -->"
            if ref[0] == "yt"
            else f"<!-- jwplayer-srt: {ref[1]} -->"
        )
        not in existing
    ]


def write_state(path, state):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(
        json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    os.replace(tmp, path)


def cap_to_text(text):
    """vtt/srt 공용: 번호·타임스탬프·헤더 줄 제거, 인라인 태그·엔티티 정리, 연속 중복 제거.
    자막은 큐 단위(3~6 단어)로 끊겨 와 줄바꿈을 그대로 두면 33자 하드랩이 된다 -> 한 줄(flowing 문장)로 합친다(openai academy-extract와 동일)."""
    out = []
    for ln in text.splitlines():
        ln = ln.strip()
        if (
            not ln
            or "-->" in ln
            or ln.isdigit()
            or ln.startswith(("WEBVTT", "Kind:", "Language:"))
        ):
            continue
        ln = html.unescape(re.sub(r"<[^>]+>", "", ln))
        if not out or out[-1] != ln:
            out.append(ln)
    return " ".join(out)


def fetch_youtube(vid):
    if not os.path.isfile(EXTRACT):
        raise RuntimeError(
            f"extract_transcript.sh not found: {EXTRACT}. Set YOUTUBE_DIGEST_SCRIPTS_DIR."
        )
    with tempfile.TemporaryDirectory() as d:
        try:
            subprocess.run(
                ["bash", EXTRACT, f"https://www.youtube.com/watch?v={vid}", d],
                stdin=subprocess.DEVNULL,
                capture_output=True,
                timeout=180,
            )
        except subprocess.TimeoutExpired:
            return ""
        for lang in ("en-orig", "en", "ko"):  # 영어 원본 영상 기준 우선순위
            f = Path(d) / f"{vid}.{lang}.srt"
            if f.exists():
                return cap_to_text(f.read_text(encoding="utf-8", errors="ignore"))
        for f in Path(d).glob("*.srt"):
            return cap_to_text(f.read_text(encoding="utf-8", errors="ignore"))
    return ""


def fetch_srt(url):
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": UA}
        )  # urllib은 301 자동 follow
        with urllib.request.urlopen(req, timeout=30) as r:
            return cap_to_text(r.read().decode("utf-8", "ignore"))
    except Exception:
        return ""


async def rendered_body(pg):
    best = ""
    for sel in (
        ".course-text-content",
        ".clp__main-content",
        "#lesson-main-content",
        "article",
    ):
        loc = pg.locator(sel).first
        if not await loc.count():
            continue
        soup = BeautifulSoup(await loc.evaluate("e => e.outerHTML"), "html.parser")
        for tag in soup.select("script, style, nav, footer"):
            tag.decompose()
        text = md(str(soup), heading_style="ATX").strip()
        if len(text) > len(best):
            best = text
    if (
        len(best) < 50
        or "This video is still being processed" in best
        or "Skilljar is a learning management system that hosts our educational content"
        in best
    ):
        return ""
    return best


async def lesson_videos(pg, course, ck, cdir, state):
    # 목차 레슨 ID는 httpx SSR로 잡는다(일부 코스는 playwright 렌더가 목차 링크를 비운다 - 예: ai-fluency-for-builders)
    cr = httpx.get(
        f"{BASE}/{course}",
        cookies=ck,
        headers={"User-Agent": UA},
        follow_redirects=True,
        timeout=30,
    )
    ids = sorted(
        set(int(x) for x in re.findall(rf"/{re.escape(course)}/(\d{{5,}})", cr.text))
    )
    titles = {}
    for item in BeautifulSoup(cr.text, "html.parser").select("li[data-url]"):
        m = re.fullmatch(rf"/{re.escape(course)}/(\d{{5,}})", item.get("data-url", ""))
        label = item.select_one(".lesson-wrapper > div")
        if m and label:
            titles[int(m.group(1))] = next(label.stripped_strings, "")
    by_source = {}
    if cdir.exists():
        for path in cdir.glob("*.md"):
            first = path.open(encoding="utf-8", errors="ignore").readline().strip()
            m = re.fullmatch(r"<!-- (https?://\S+) -->", first)
            if m:
                by_source[m.group(1)] = path
    out = []
    bodies = 0
    gated = 0
    for n, lid in enumerate(ids, 1):
        url = f"{BASE}/{course}/{lid}"
        if os.environ.get("SKILLJAR_MISSING_ONLY") == "1" and url in by_source:
            continue
        listed_title = titles.get(lid) or f"Lesson {lid}"
        listed_path = by_source.get(url, cdir / f"{n:02d}-{slug(listed_title)}.md")
        await pg.goto(url, wait_until="domcontentloaded")
        if urlsplit(pg.url).path.rstrip("/") != urlsplit(url).path.rstrip("/"):
            cdir.mkdir(parents=True, exist_ok=True)
            if not listed_path.exists():
                listed_path.write_text(
                    f"<!-- {url} -->\n\n# {listed_title}\n\n_(등록 또는 권한이 필요한 레슨)_\n",
                    encoding="utf-8",
                )
            by_source[url] = listed_path
            gated += 1
            continue
        # 영상 iframe/플레이어 렌더가 1800ms보다 늦는 레슨이 있다(하이브리드 코스 다수가 그래서 누락됐다).
        # 플레이어가 붙을 때까지 최대 7s 기다린 뒤 잡는다. 진짜 텍스트 레슨은 타임아웃 후 그대로 통과(영상 없음).
        try:
            player = await pg.wait_for_selector(
                "#lesson-main-content iframe[src*='youtube'], .clp__main-content iframe[src*='youtube'], #lesson-main-content .jw-video, .clp__main-content .jw-video, #lesson-main-content video, .clp__main-content video",
                timeout=7000,
                state="attached",
            )
        except Exception:
            player = None
        if player:
            await pg.wait_for_timeout(800)
        title = titles.get(lid) or (await pg.title()).strip()
        path = by_source.get(url, cdir / f"{n:02d}-{slug(title)}.md")
        body = await rendered_body(pg)
        if body:
            cdir.mkdir(parents=True, exist_ok=True)
            existing = path.read_text(encoding="utf-8") if path.exists() else ""
            key = f"academy-body:{url}"
            digest = hashlib.sha256(body.strip().encode()).hexdigest()
            previous = state.get(key)
            state[key] = digest
            if previous != digest and not (previous is None and existing):
                tail = re.search(
                    r"\n<!-- (?:youtube|vimeo|jwplayer(?:-srt)?): .*\Z", existing, re.S
                )
                preserved = tail.group(0).rstrip() if tail else ""
                content = f"<!-- {url} -->\n\n{body}"
                updated = f"{content}{preserved}\n" if preserved else f"{content}\n"
                path.write_text(updated, encoding="utf-8")
                bodies += 1
            by_source[url] = path
        # 1) youtube iframe (보이는 것만)
        vis = await pg.eval_on_selector_all(
            "#lesson-main-content iframe, .clp__main-content iframe",
            "els=>els.filter(e=>{const r=e.getBoundingClientRect();return r.width>50&&r.height>50})"
            ".map(e=>e.src).filter(s=>s&&s.includes('youtube')&&s.includes('/embed/'))",
        )
        refs = youtube_refs(vis)
        if refs:
            out.append((lid, title, path, refs))
            continue
        if not player:
            out.append((lid, title, path, []))
            continue
        # 2) JWPlayer: 재생 트리거 후 English captions .srt
        for sel in [
            "#lesson-main-content .jw-icon-display",
            ".clp__main-content .jw-icon-display",
            "#lesson-main-content .jw-video",
            ".clp__main-content .jw-video",
            "#lesson-main-content video",
            ".clp__main-content video",
        ]:
            try:
                el = pg.locator(sel).first
                if await el.count() and await el.is_visible():
                    await el.click()
                    break
            except Exception:
                pass
        await pg.wait_for_timeout(2500)
        srt = await pg.evaluate(
            "(()=>{try{const t=jwplayer().getPlaylistItem().tracks||[];"
            "const en=t.find(x=>x.kind==='captions'&&/english/i.test((x.label||x.name||'')));"
            "return en?en.file:null}catch(e){return null}})()"
        )
        out.append((lid, title, path, [("srt", srt)] if srt else []))
    return out, bodies, gated, len(ids)


async def main():
    if sys.argv[1:] == ["--self-test"]:
        refs = youtube_refs(
            [
                "https://youtube.com/embed/ABCDEFGHIJK",
                "https://youtube.com/embed/1234567890_",
                "https://youtube.com/embed/ABCDEFGHIJK",
            ]
        )
        assert refs == [("yt", "ABCDEFGHIJK"), ("yt", "1234567890_")]
        assert unseen_refs("<!-- youtube: ABCDEFGHIJK -->", refs) == [
            ("yt", "1234567890_")
        ]
        assert expired_session([{"name": "sj_sessionid", "expires": 1000}], now=2000)
        assert not expired_session(
            [{"name": "sj_sessionid", "expires": 3000}], now=2000
        )
        assert not expired_session([{"name": "sj_sessionid", "expires": -1}], now=2000)
        assert expired_session([{"name": "sj_csrftoken", "expires": 3000}], now=2000)
        assert urlsplit("https://x/course/123").path.rstrip("/") == urlsplit(
            "https://x/course/123/"
        ).path.rstrip("/")
        print("self-test ok")
        return
    if len(sys.argv) < 2:
        print("사용법: academy-video.py <out_dir> [course-slug ...]")
        return
    out_root = Path(sys.argv[1])
    state_path = out_root / STATE_FILE
    try:
        mirror_state = json.loads(state_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        mirror_state = {}
    courses = sys.argv[2:]
    auth_state = json.load(open(STATE))
    ck = {
        c["name"]: c["value"]
        for c in auth_state["cookies"]
        if "skilljar" in c.get("domain", "")
    }
    if expired_session(auth_state["cookies"]):
        # 만료 세션에서는 모든 레슨이 코스 랜딩으로 튕겨 전 코스가 gated로만 기록된다.
        # 루트의 'auth/logout' 문자열은 만료 뒤에도 남아 있어 로그인 판정에 쓸 수 없다.
        print("[!] sj_sessionid 만료 - login-academy.py로 재로그인하세요.", flush=True)
        return
    if not courses:
        catalogs = [
            httpx.get(
                f"{BASE}{path}",
                cookies=ck,
                headers={"User-Agent": UA},
                follow_redirects=True,
                timeout=30,
            ).text
            for path in ("/", "/page/all-courses")
        ]
        if "auth/logout" not in catalogs[0]:
            print("[!] 비로그인 상태 - login-academy.py로 쿠키를 먼저 갱신하세요.")
            return
        skip = {
            "auth",
            "accounts",
            "page",
            "catalog",
            "paths",
            "plans",
            "courses",
            "lessons",
        }
        courses = sorted(
            set(
                m
                for text in catalogs
                for m in re.findall(r'href="/([a-z0-9][a-z0-9-]+)/?"', text)
                if m not in skip
            )
        )
        skip_host = os.environ.get("SKILLJAR_SKIP_HOST", "")
        if skip_host:
            courses = [c for c in courses if not (out_root / skip_host / c).exists()]
    async with async_playwright() as p:
        b = await p.chromium.launch(headless=True)
        ctx = await b.new_context(storage_state=STATE, user_agent=UA)
        pg = await ctx.new_page()
        for course in courses:
            cdir = out_root / _HOST / course
            lv, bodies, gated, listed = await lesson_videos(
                pg, course, ck, cdir, mirror_state
            )
            got = 0
            for n, (lid, title, fpath, refs) in enumerate(lv, 1):
                cdir.mkdir(parents=True, exist_ok=True)
                existing = (
                    fpath.read_text(encoding="utf-8").rstrip() if fpath.exists() else ""
                )
                if not existing:
                    existing = f"<!-- {BASE}/{course}/{lid} -->\n\n# {title}"
                    fpath.write_text(f"{existing}\n", encoding="utf-8")
                if not refs:
                    continue
                added = 0
                for kind, ref in unseen_refs(existing, refs):
                    tag = (
                        f"<!-- youtube: {ref} -->"
                        if kind == "yt"
                        else f"<!-- jwplayer-srt: {ref} -->"
                    )
                    tx = fetch_youtube(ref) if kind == "yt" else fetch_srt(ref)
                    if len(tx) >= 50:
                        pending = f"<!-- {kind}-pending: {ref} -->"
                        existing = existing.replace(
                            f"\n\n{pending}\n\n_(영상 자막 없음 또는 추출 실패)_", ""
                        )
                        existing = f"{existing}\n\n{tag}\n\n## 자막 (영상 전사)\n\n{tx}"
                        got += 1
                    else:
                        pending = f"<!-- {kind}-pending: {ref} -->"
                        if pending in existing:
                            continue
                        existing = f"{existing}\n\n{pending}\n\n_(영상 자막 없음 또는 추출 실패)_"
                    added += 1
                if added:
                    fpath.write_text(f"{existing}\n", encoding="utf-8")
            write_state(state_path, mirror_state)
            note = f", {gated}/{listed} gated(skipped)" if gated else ""
            print(
                f"{course}: {len(lv)} lessons inspected, {bodies} bodies changed, {got} clips added{note}",
                flush=True,
            )
        await b.close()


if __name__ == "__main__":
    asyncio.run(main())
