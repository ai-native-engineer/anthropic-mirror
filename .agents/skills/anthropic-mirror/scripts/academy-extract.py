"""Anthropic Academy 코스를 로그인 쿠키로 추출 (텍스트 본문).

skilljar 레슨 페이지는 1MB로 무거워 브라우저 크롤이 페이지당 12-18초로 느리다.
브라우저 없이 httpx 병렬 GET(동시 8)으로 받아 bs4 + markdownify로 본문만 뽑는다.

함정:
- lesson ID는 6자리+(287722)만 실제 레슨. 작은 숫자(02,03)는 진도 표시 노이즈라 코스로 리다이렉트된다.
- 본문 컨테이너는 .course-text-content / .clp__main-content (코스마다 다름, 폴백 체인).
- 영상 강의 코스(api/bedrock/vertex/mcp 등)는 텍스트 본문이 없고 영상이 보호된 JS player다.
  본문 컨테이너엔 "This video is still being processed" placeholder가 들어 50자 필터를 통과하므로
  그 마커로 스킵한다(자막도 불가, references 참고).
- Skilljar 공통 로그인 안내문도 본문이 아니므로 스킵한다.
- 쿠키는 만료되면 비로그인 미리보기 데이터를 받는다 -> 추출 전 로그인 확인, 만료면 login-academy.py 재실행.
- 레슨 제목은 코스 목차에서 뽑는다. 렌더 후 <title>은 코스명으로 바뀌어 파일명이 중복될 수 있다.
- 기존 파일의 영상 마커부터 끝까지는 보존한다. 본문 갱신이 academy-video가 붙인 자막을 지우면 안 된다.

실행: <crawl4ai python> academy-extract.py <out_dir> [course-slug ...]
  코스 슬러그 생략 시 카탈로그(/)에서 자동 수집.
  모든 레슨을 검사하고 실제 본문이 달라진 파일만 갱신.
  출력: <out_dir>/anthropic.skilljar.com/<course>/<NN>-<title>.md (레슨별, A 트랙과 같은 도메인 트리)
"""

import asyncio, json, os, re, sys, time
from pathlib import Path
from urllib.parse import urlsplit
import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE = os.environ.get("SKILLJAR_BASE", "https://anthropic.skilljar.com").rstrip("/")
_HOST = BASE.split("://")[-1]
STATE = os.path.expanduser(
    "~/.crawl4ai/academy_state.json"
    if _HOST == "anthropic.skilljar.com"
    else f"~/.crawl4ai/skilljar-{_HOST}.json"
)


def slug(t):
    t = re.sub(r"[^\w\s-]", "", t).strip().lower()
    return re.sub(r"\s+", "-", t)[:45] or "lesson"


def extract(html):
    soup = BeautifulSoup(html, "html.parser")
    title = (
        soup.title.get_text(strip=True) if soup.title else ""
    )  # 레슨명은 <title>이 정확(본문 첫 헤딩은 "Learning Objectives"류라 부정확)
    # 영상 레슨은 .course-text-content가 "Video" 몇 자뿐이라 첫 매칭만 쓰면 본문(article/#lesson-main-content)을 놓친다 -> 후보 중 가장 긴 본문을 고른다.
    best = ""
    for sel in (
        ".course-text-content",
        ".clp__main-content",
        "#lesson-main-content",
        "article",
    ):
        el = soup.select_one(sel)
        if not el:
            continue
        for t in el.select("script, style, nav, footer"):
            t.decompose()
        txt = md(str(el), heading_style="ATX").strip()
        if len(txt) > len(best):
            best = txt
    return title, best


async def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("./academy")
    courses = sys.argv[2:]
    out.mkdir(parents=True, exist_ok=True)
    state = json.load(open(STATE))
    ck = {
        c["name"]: c["value"]
        for c in state["cookies"]
        if "skilljar" in c.get("domain", "")
    }
    UA = {"User-Agent": "Mozilla/5.0"}
    async with httpx.AsyncClient(
        cookies=ck, headers=UA, timeout=45, follow_redirects=True
    ) as c:
        sem = asyncio.Semaphore(8)

        async def get(u):
            async with sem:
                try:
                    r = await c.get(u)
                    return u, r.text, str(r.url)
                except Exception:
                    return u, "", ""

        _, root, _ = await get(f"{BASE}/")
        if "auth/logout" not in root:
            print("[!] 비로그인 상태 - login-academy.py로 쿠키를 먼저 갱신하세요.")
            return
        if all(
            0 < ck_c.get("expires", -1) < time.time()
            for ck_c in state["cookies"]
            if ck_c.get("name") == "sj_sessionid"
        ):
            # 만료 세션은 레슨을 코스 랜딩으로 튕겨 소개글이 본문으로 저장된다(auth/logout 문자열은 남아 있어 판별 불가).
            print("[!] sj_sessionid 만료 - login-academy.py로 재로그인하세요.")
            return
        if not courses:
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
                    for m in re.findall(r'href="/([a-z0-9][a-z0-9-]+)/?"', root)
                    if m not in skip
                )
            )
        for course in courses:
            _, ch, _ = await get(f"{BASE}/{course}")
            ids = sorted(
                set(
                    i
                    for i in re.findall(rf"/{re.escape(course)}/(\d+)", ch)
                    if len(i) >= 5
                ),
                key=int,
            )
            titles = {}
            for item in BeautifulSoup(ch, "html.parser").select("li[data-url]"):
                m = re.fullmatch(
                    rf"/{re.escape(course)}/(\d{{5,}})", item.get("data-url", "")
                )
                label = item.select_one(".lesson-wrapper > div")
                if m and label:
                    titles[m.group(1)] = next(label.stripped_strings, "")
            cdir = out / urlsplit(BASE).netloc / course
            by_source = {}
            if cdir.exists():
                for path in cdir.glob("*.md"):
                    first = (
                        path.open(encoding="utf-8", errors="ignore").readline().strip()
                    )
                    m = re.fullmatch(r"<!-- (https?://\S+) -->", first)
                    if m:
                        by_source[m.group(1)] = path
            lres = await asyncio.gather(*[get(f"{BASE}/{course}/{lid}") for lid in ids])
            # 접근 불가 레슨은 코스 랜딩으로 redirect된다 -> 그 소개글을 본문으로 저장하지 않는다
            bodies = {
                u: extract(h)
                for u, h, fin in lres
                if not fin or urlsplit(fin).path.rstrip("/") == urlsplit(u).path.rstrip("/")
            }
            changed = 0
            for n, lid in enumerate(ids, 1):
                u = f"{BASE}/{course}/{lid}"
                ltitle, b = bodies.get(u, ("", ""))
                # 영상 레슨은 본문 컨테이너에 placeholder가 잡혀 50자 필터를 통과한다 -> 마커로 스킵
                if (
                    len(b) < 50
                    or "This video is still being processed" in b
                    or "Skilljar is a learning management system that hosts our educational content"
                    in b
                ):
                    continue
                title = (
                    slug(titles.get(lid) or ltitle)
                    if titles.get(lid) or ltitle
                    else lid
                )
                cdir.mkdir(parents=True, exist_ok=True)
                path = by_source.get(u, cdir / f"{n:02d}-{title}.md")
                existing = path.read_text(encoding="utf-8") if path.exists() else ""
                tail = re.search(
                    r"\n<!-- (?:youtube|vimeo|jwplayer(?:-srt)?): .*\Z", existing, re.S
                )
                preserved = tail.group(0).rstrip() if tail else ""
                content = f"<!-- {u} -->\n\n{b}"
                updated = f"{content}{preserved}\n" if preserved else f"{content}\n"
                if updated != existing:
                    path.write_text(updated, encoding="utf-8")
                    changed += 1
            print(
                f"{course}: {len(ids)} lessons inspected, {changed} bodies changed",
                flush=True,
            )


asyncio.run(main())
