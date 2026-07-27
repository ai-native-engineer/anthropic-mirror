"""anthropic.com + claude.com + claude docs + support + 연구 블로그 공개 페이지 전체 크롤 (강의 제외).

sitemap.xml을 1차 소스로 쓴다 -- 사이트가 새 섹션을 추가해도 빠짐없이 따라간다(하드코딩 목록·See more 펼치기 폐기).
curl_cffi(impersonate="chrome")로 anthropic.com의 봇 차단을 우회한다 -- plain fetch는 본문 0이지만 chrome 지문이면 SSR 본문이 그대로 온다(브라우저·캡챠 불필요).
platform.claude.com/docs는 Mintlify SPA라 HTML엔 본문이 없지만 페이지별 <url>.md raw가 깨끗한 마크다운을 준다 -> .md로 받는다(브라우저 불필요).
trust.anthropic.com만 SafeBase SPA(curl도 .md도 본문 0)라 playwright innerText로 보강한다.

저장: <out>/<host>/<path>.md (academy의 anthropic.skilljar.com/과 같은 도메인 트리). 모든 URL을 검사하고 실제 마크다운이 달라진 파일만 갱신.
확정적 빈 페이지(404 또는 200이지만 본문<200자 -- 미발행 .md·redirect 셸)는 실패가 아니라 '본문없음 skip'으로 분류한다. 저장하지 않으므로 매 실행 재확인되고 업스트림이 발행하면 자동 수집된다.
crawl-mirror.py의 dest/save/find_boilerplate/strip_boilerplate를 재사용한다.

실행: python3 crawl-site.py <out_dir> [--only <host>] [--force] [--limit N] [--concurrency N]
"""

import argparse, hashlib, importlib.util, json, os, re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlsplit, urljoin, parse_qs
from curl_cffi import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

CRAWL_SCRIPTS_DIR = os.environ.get(
    "CRAWL_SCRIPTS_DIR", os.path.expanduser("~/.agents/skills/shared/crawl/scripts")
)
CM_PATH = os.path.join(CRAWL_SCRIPTS_DIR, "crawl-mirror.py")
if not os.path.isfile(CM_PATH):
    raise SystemExit(f"crawl-mirror.py not found: {CM_PATH}. Set CRAWL_SCRIPTS_DIR.")
spec = importlib.util.spec_from_file_location("cm", CM_PATH)
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)

A = "https://www.anthropic.com"
IMPERSONATE = "chrome"  # anthropic.com은 일반 UA를 막는다 -> Chrome TLS/JA3 지문 위장
# claude.com sitemap은 첫 세그먼트로 로케일을 표기한다(ja/de/fr/ko/it ...). 영어 정본만 남긴다.
LOCALES = {
    "ja",
    "de",
    "fr",
    "ko",
    "it",
    "es",
    "pt",
    "zh",
    "nl",
    "pl",
    "ru",
    "id",
    "tr",
    "vi",
    "th",
    "ar",
    "hi",
    "ja-jp",
    "pt-br",
    "zh-cn",
    "zh-tw",
}


def first_seg(url):
    parts = [x for x in urlsplit(url).path.split("/") if x]
    return parts[0] if parts else ""


def is_claude_en(u):
    return first_seg(u) not in LOCALES


# HTML 소스: (sitemap_url, keep_predicate). curl_cffi + bs4로 본문 추출.
HTML_SITEMAPS = [
    (
        f"{A}/sitemap.xml",
        lambda u: True,
    ),  # 실측 ~476 (news/research/engineering/events/legal/product/system-cards/economic 등 전량)
    (
        "https://claude.com/sitemap.xml",
        is_claude_en,
    ),  # 실측 영어 ~1591 (blog/customers/resources/connectors/plugins/solutions ...)
    (
        "https://claude.com/docs/sitemap.xml",
        lambda u: True,
    ),  # 실측 ~127 (태그형 help 문서, robots.txt가 선언하는 2번째 sitemap)
    (
        "https://support.claude.com/sitemap.xml",
        lambda u: "/en/" in u,
    ),  # 실측 영어 ~370 (Help Center)
]
# Mintlify docs: sitemap의 각 URL + ".md"로 raw 마크다운을 받는다.
# platform = API/플랫폼 개발자 문서, code = Claude Code CLI 문서(hooks·subagents·settings·slash-commands·agent-sdk 등).
DOCS_SITEMAPS = [
    "https://platform.claude.com/sitemap.xml",  # 실측 영어 ~1755 (api 레퍼런스 포함)
    "https://code.claude.com/sitemap.xml",  # 실측 영어 ~154 (Claude Code CLI docs)
]


def is_docs_en(u):
    return "/docs/en/" in u


# sitemap 없는 정적 연구 블로그: 홈에서 같은 도메인 링크 1-depth 수집.
DISCOVER = [
    (
        "https://alignment.anthropic.com/",
        "alignment.anthropic.com",
    ),  # Alignment Science Blog (Distill 정적)
    (
        "https://transformer-circuits.pub/",
        "transformer-circuits.pub",
    ),  # 해석가능성 연구 (정적 .html, sitemap 403)
]
# SafeBase SPA: curl·​.md 둘 다 본문 0 -> playwright innerText 보강.
SPA_PAGES = ["https://trust.anthropic.com/"]
STATE_FILE = ".anthropic-mirror-state.json"


def get(url, suffix=""):
    r = requests.get(url + suffix, impersonate=IMPERSONATE, timeout=40)
    return r.status_code, r.text, getattr(r, "url", "") or ""


def redirected(requested, final):
    """요청 URL과 최종 URL의 경로가 다른가(.md suffix와 trailing slash 차이는 무시)."""
    if not final:
        return False

    def norm(u):
        p = urlsplit(u).path
        if p.endswith(".md"):
            p = p[:-3]
        # 정적 사이트의 /foo/index.html은 /foo/와 같은 페이지다(alignment.anthropic.com)
        p = re.sub(r"/index\.html?$", "/", p)
        return p.rstrip("/")

    return norm(requested) != norm(final)


def sitemap_urls(sm):
    """sitemap(또는 sitemap 인덱스) -> URL 집합. 인덱스면 자식 sitemap을 한 단계 펼친다."""
    try:
        _, t, _ = get(sm)
    except Exception as e:
        print(f"  sitemap ERR {sm}: {e}", flush=True)
        return set()
    locs = re.findall(r"<loc>(.*?)</loc>", t)
    if locs and all(l.strip().endswith(".xml") for l in locs):
        urls = set()
        for c in locs:
            try:
                _, ct, _ = get(c.strip())
                urls.update(re.findall(r"<loc>(.*?)</loc>", ct))
            except Exception:
                pass
        return urls
    return set(l.strip() for l in locs)


_CFEMAIL = re.compile(
    r"\[([^\]]*)\]\((?:https?://[^)]*?)?/cdn-cgi/l/email-protection#([0-9a-fA-F]{8,})\)"
)


def _deob(h):
    """Cloudflare email obfuscation: 첫 바이트가 XOR 키, 나머지를 XOR해 ASCII 복원."""
    k = int(h[:2], 16)
    try:
        return "".join(chr(int(h[i : i + 2], 16) ^ k) for i in range(2, len(h), 2))
    except Exception:
        return None


def decode_cfemail(text):
    """[[email protected]](.../cdn-cgi/l/email-protection#HEX) -> [실제이메일](mailto:실제이메일)."""

    def r(m):
        e = _deob(m.group(2))
        return f"[{e}](mailto:{e})" if e and "@" in e else m.group(0)

    return _CFEMAIL.sub(r, text)


def abs_url(base, ref):
    """페이지 URL 기준 절대 URL. Next.js 이미지 최적화 경로(/_next/image?url=...)는 원본 CDN URL로 환원한다.
    스킴 없는 상대 경로를 그대로 두면 미러 파일 안에서 대상 없는 참조가 된다."""
    ref = (ref or "").strip()
    if not ref or ref.startswith(("data:", "blob:", "javascript:")):
        return ""
    if urlsplit(ref).path.endswith("/_next/image"):
        inner = parse_qs(urlsplit(ref).query).get("url", [""])[0].strip()
        if inner:
            ref = inner
    return urljoin(base, ref) if base else ref


def absolutize(node, base):
    """markdownify 전에 img/a를 절대 URL로 바꾼다. 해석 불가한 img는 빈 ![]()만 남기므로 제거."""
    for img in node.find_all("img"):
        raw = (img.get("src") or "").strip()
        if raw.startswith("data:"):
            # 인라인 base64는 extract-images.py가 뒤에서 images/ 파일로 뺀다 -> 건드리지 않는다
            continue
        src = abs_url(base, raw)
        if src.startswith(("http://", "https://")):
            img["src"] = src
        else:
            img.decompose()
    for a in node.find_all("a", href=True):
        href = a["href"].strip()
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        # cdn-cgi 난독화 링크는 decode_cfemail이 원형 그대로 매칭한다 -> 절대화에서 제외
        if "/cdn-cgi/l/email-protection" in href:
            continue
        a["href"] = urljoin(base, href)


def html_to_md(html, base_url=""):
    """본문 컨테이너(main/article/body 중 텍스트가 가장 많은 것)를 골라 nav/header/footer/form 제거 후 markdown."""
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script", "style", "noscript", "svg"]):
        t.decompose()
    cands = [
        c for c in (soup.find("main"), soup.find("article"), soup.body) if c is not None
    ]
    # Distill 템플릿(alignment.anthropic.com 일부)은 <body> 없이 최상위에 <d-article>을 둔다 -> 문서 전체로 fallback
    node = max(cands, key=lambda c: len(c.get_text(strip=True))) if cands else soup
    for t in node(["nav", "header", "footer", "form"]):
        t.decompose()
    if base_url:
        absolutize(node, base_url)
    return decode_cfemail(md(str(node), heading_style="ATX").strip())


def fetch_html(url):
    try:
        s, h, final = get(url)
        if s != 200:
            return url, "", f"status={s}"
        if redirected(url, final):
            # 다른 경로로 redirect된 URL. 최종 페이지 본문을 요청 경로에 저장하면
            # 옛 경로 파일이 다른 문서의 사본이 된다(whats-new-claude-4-6/4-7/4-8 사례).
            return url, "", f"redirect:{final}"
        return url, html_to_md(h, final or url), ""
    except Exception as e:
        return url, "", str(e)[:80]


_DOCS_INDEX = re.compile(r"^(?:>[^\n]*\n)+", re.M)
_MD_IMAGE = re.compile(r"(!\[[^\]]*\]\()\s*([^)\s]*)")


def absolutize_md_images(text, base):
    """Mintlify raw .md의 이미지 참조만 절대 URL로 바꾼다.

    업스트림 원문은 /docs/images/x.png처럼 사이트 절대경로를 쓰는데, 미러 파일 옆에는 그 경로가 없어
    대상 없는 참조가 된다. 링크는 원문 그대로 두고 이미지만 해석 가능하게 만든다.
    """

    def repl(m):
        ref = m.group(2)
        if not ref or ref.startswith(("http://", "https://", "data:", "<")):
            return m.group(0)
        return m.group(1) + urljoin(base, ref)

    return _MD_IMAGE.sub(repl, text)


def strip_docs_index(t):
    """code.claude.com .md는 매 페이지 상단에 llms.txt 안내 blockquote가 붙는다 -> 첫 'Documentation Index' 블록만 제거(H1 아래 페이지 설명 blockquote는 보존)."""
    if t.startswith("> ## Documentation Index"):
        m = _DOCS_INDEX.match(t)
        if m:
            return t[m.end() :].lstrip()
    return t


def fetch_docs_md(url):
    """Mintlify: <url>.md가 깨끗한 마크다운(브라우저로 렌더한 SPA 본문과 동일)."""
    try:
        s, t, final = get(url, ".md")
        if s != 200:
            return url, "", f"status={s}"
        if redirected(url, final):
            return url, "", f"redirect:{final}"
        return url, absolutize_md_images(strip_docs_index(t.strip()), url), ""
    except Exception as e:
        return url, "", str(e)[:80]


def rescue_article_views(pages):
    """짧은 터미널형 feature 페이지는 Article 토글을 클릭해 본문을 보강."""
    targets = [u for u, m in pages.items() if "Read as Article" in m and len(m) < 2000]
    if not targets:
        return 0
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print(f"  article fallback unavailable: {e}", flush=True)
        return 0

    rescued = 0
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        pg = b.new_page()
        for u in targets:
            try:
                pg.goto(u, wait_until="domcontentloaded", timeout=40000)
                pg.wait_for_timeout(3000)
                pg.get_by_text("Read as Article").click(timeout=5000)
                pg.wait_for_timeout(2000)
                # ponytail: current Anthropic feature article layout; broaden selectors if another client-only format appears.
                loc = pg.locator('[class*="editorialMain"]').first
                html = loc.inner_html() if loc.count() else pg.content()
                soup = BeautifulSoup(html, "html.parser")
                for t in soup.select('[class*="chapterHeadingPart"]'):
                    t.decompose()
                m = html_to_md(str(soup), u)
                if len(m) > len(pages[u]) * 2:
                    pages[u] = m
                    rescued += 1
            except Exception as e:
                print(f"  article fallback ERR {u}: {str(e)[:80]}", flush=True)
        b.close()
    return rescued


def discover(base, dom):
    """sitemap 없는 사이트: 홈에서 같은 도메인 링크 1-depth 수집."""
    try:
        s, h, _ = get(base)
        if s != 200:
            return set()
    except Exception:
        return set()
    soup = BeautifulSoup(h, "html.parser")
    out = {base}
    for a in soup.find_all("a", href=True):
        v = urljoin(base, a["href"]).split("#")[0].split("?")[0]
        if urlsplit(v).netloc == dom and not v.endswith(
            (".xml", ".pdf", ".json", ".png", ".jpg")
        ):
            out.add(v)
    return out


_SOURCE = re.compile(r"^<!--\s*(?:source:\s*)?(https://\S+?)\s*-->")


def known_urls(out):
    """미러에 이미 있는 파일의 source 헤더에서 host별 기존 URL을 모은다.

    sitemap이 축소돼도(platform.claude.com이 SDK 레퍼런스 1,196개를 sitemap에서 뺀 사례)
    이미 수집한 페이지를 계속 재확인해 미러가 특정 시점에 동결되지 않게 한다.
    사라진 URL은 crawl()이 '본문없음 skip'으로 분류하므로 저장되지 않는다.
    """
    by_host = {}
    for root, dirs, files in os.walk(out):
        dirs[:] = [
            d for d in dirs if d not in (".git", "_yt-cache", ".agents", ".claude")
        ]
        for fn in files:
            if not fn.endswith(".md"):
                continue
            try:
                with open(
                    os.path.join(root, fn), encoding="utf-8", errors="replace"
                ) as f:
                    first = f.readline().strip()
            except OSError:
                continue
            m = _SOURCE.match(first)
            if m:
                by_host.setdefault(urlsplit(m.group(1)).netloc, set()).add(m.group(1))
    return by_host


def crawl(urls, fetch, concurrency):
    pages, fails, empties, moved = {}, [], [], []
    with ThreadPoolExecutor(max_workers=concurrency) as ex:
        futs = {ex.submit(fetch, u): u for u in urls}
        done = 0
        for f in as_completed(futs):
            url, mdtext, err = f.result()
            done += 1
            if mdtext and len(mdtext) >= 200:  # 200자 미만은 빈 SPA 셸·404 본문
                pages[url] = mdtext
            elif err.startswith("redirect:"):
                # 업스트림이 다른 경로로 옮긴 페이지. 옛 경로에 새 본문을 쓰지 않는다.
                # 이미 미러에 있는 옛 파일은 stale이 되므로 삭제 후보로 따로 보고한다.
                moved.append((url, err[len("redirect:") :]))
            elif err in ("", "status=404"):
                # 업스트림에 본문 자체가 없음(미발행 .md·sitemap의 404) -> 실패 아님.
                # 저장하지 않으므로 매 실행 재확인되고, 업스트림이 발행하면 자동 수집된다.
                empties.append(url)
            else:
                fails.append((url, err))
            if done % 100 == 0:
                print(
                    f"  {done}/{len(urls)} (성공 {len(pages)}, 없음 {len(empties)}, 이전 {len(moved)}, 실패 {len(fails)})",
                    flush=True,
                )
    return pages, fails, empties, moved


def fingerprint(text):
    return hashlib.sha256(cm.strip_chrome(text).strip().encode()).hexdigest()


def load_state(out):
    path = os.path.join(out, STATE_FILE)
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def write_state(out, state):
    path = os.path.join(out, STATE_FILE)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    os.replace(tmp, path)


def save_changed(out, url, body, state, force=False):
    """실제 정제 본문 해시가 바뀐 source만 쓴다. 기존 archive는 첫 실행에서 live hash로 기준선을 잡는다."""
    path, clean = cm.dest(out, url)
    digest = fingerprint(body)
    previous = state.get(clean)
    state[clean] = digest
    if not force and (
        previous == digest or (previous is None and os.path.exists(path))
    ):
        return False, previous is None
    cm.save(out, url, body, False)
    return True, False


def flush(pages, out, state, force=False):
    """호스트별 boilerplate 제거 후 즉시 저장(긴 실행이 끊겨도 phase 단위로 보존)."""
    rescued = rescue_article_views(pages)
    if rescued:
        print(f"  article fallback: {rescued}개", flush=True)
    by_host = {}
    for u in pages:
        by_host.setdefault(urlsplit(u).netloc, []).append(u)
    for host, us in by_host.items():
        # Mintlify docs .md는 이미 깨끗 -> boilerplate 스킵
        if host not in ("platform.claude.com", "code.claude.com") and len(us) >= 5:
            bl = cm.find_boilerplate([pages[u] for u in us], 0.4)
            if bl:
                for u in us:
                    pages[u] = cm.strip_boilerplate(pages[u], bl)
    changed = baselined = 0
    for url, body in pages.items():
        wrote, seeded = save_changed(out, url, body, state, force)
        changed += wrote
        baselined += seeded
    write_state(out, state)
    return len(pages), changed, baselined


def spa_rescue(urls):
    """SafeBase 등 SPA를 playwright innerText로 보강."""
    from playwright.sync_api import sync_playwright

    out = {}
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        pg = b.new_page()
        for u in urls:
            try:
                pg.goto(u, wait_until="domcontentloaded", timeout=30000)
                pg.wait_for_timeout(6000)  # SafeBase는 본문을 늦게 렌더
                best = ""
                for sel in ["#trust-center-main-content", "main", "article", "body"]:
                    el = pg.locator(sel).first
                    if el.count():
                        t = el.inner_text()
                        if len(t) > len(best):
                            best = t
                if len(best) >= 200:
                    out[u] = best
            except Exception:
                pass
        b.close()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument(
        "--only", default="", help="이 host substring을 가진 URL만 크롤(예: claude.com)"
    )
    ap.add_argument(
        "--force",
        action="store_true",
        help="본문 해시와 무관하게 검사 결과를 다시 저장",
    )
    ap.add_argument("--self-test", action="store_true", help=argparse.SUPPRESS)
    ap.add_argument("--limit", type=int, default=0, help="크롤 URL 상한(테스트용)")
    ap.add_argument("--concurrency", type=int, default=8)
    a = ap.parse_args()

    if a.self_test:
        import tempfile

        with tempfile.TemporaryDirectory() as out:
            state = {}
            url = "https://example.com/page"
            path, _ = cm.dest(out, url)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w") as f:
                f.write("post-processed existing file\n")
            assert save_changed(out, url, "same live body", state) == (False, True)
            assert save_changed(out, url, "same live body", state) == (False, False)
            assert save_changed(out, url, "new live body", state) == (True, False)
            assert "new live body" in open(path).read()

            base = "https://www.anthropic.com/news/x"
            assert (
                abs_url(base, "/images/a.svg")
                == "https://www.anthropic.com/images/a.svg"
            )
            assert (
                abs_url(base, "fig1.png") == "https://www.anthropic.com/news/fig1.png"
            )
            assert (
                abs_url(base, "/_next/image?url=https%3A%2F%2Fcdn.x%2Fa.png&w=64")
                == "https://cdn.x/a.png"
            )
            assert abs_url(base, "/_next/image?url=%2Fstatic%2Fb.svg") == (
                "https://www.anthropic.com/static/b.svg"
            )
            assert abs_url(base, "data:image/png;base64,AAA") == ""
            body = html_to_md(
                '<body><p><img src="fig1.png"><img src="data:image/gif;base64,R0lGOD">'
                '<a href="/news/y">y</a></p></body>',
                base,
            )
            assert "![](https://www.anthropic.com/news/fig1.png)" in body
            assert "![]()" not in body
            assert "(https://www.anthropic.com/news/y)" in body
            # 인라인 base64는 extract-images.py가 처리하므로 크롤 단계에서 보존돼야 한다
            assert "data:image/gif;base64,R0lGOD" in body

            assert redirected(base, "https://www.anthropic.com/news/z")
            assert not redirected(base, "https://www.anthropic.com/news/x/")
            assert not redirected(base + ".md", "https://www.anthropic.com/news/x")
            assert not redirected(
                "https://alignment.anthropic.com/2024/rogue-eval/index.html",
                "https://alignment.anthropic.com/2024/rogue-eval/",
            )

            docs = "https://platform.claude.com/docs/en/build-with-claude/thinking"
            out_md = absolutize_md_images(
                "![d](/docs/images/a.svg) [keep](/docs/en/x) ![k](https://cdn/b.png)",
                docs,
            )
            assert "![d](https://platform.claude.com/docs/images/a.svg)" in out_md
            assert "[keep](/docs/en/x)" in out_md  # 링크는 원문 보존
            assert "![k](https://cdn/b.png)" in out_md

            with tempfile.TemporaryDirectory() as kout:
                d = os.path.join(kout, "platform.claude.com", "docs", "en")
                os.makedirs(d)
                with open(os.path.join(d, "a.md"), "w", encoding="utf-8") as f:
                    f.write("<!-- source: https://platform.claude.com/docs/en/a -->\n")
                with open(os.path.join(d, "b.md"), "w", encoding="utf-8") as f:
                    f.write("<!-- https://anthropic.skilljar.com/c/b -->\n")
                k = known_urls(kout)
                assert k["platform.claude.com"] == {
                    "https://platform.claude.com/docs/en/a"
                }
                assert k["anthropic.skilljar.com"] == {
                    "https://anthropic.skilljar.com/c/b"
                }
        print("self-test ok")
        return

    crawled = set()

    def todo(urls):
        urls = [u for u in urls if (not a.only) or (a.only in u)]
        picked = sorted(set(urls) - crawled)
        crawled.update(picked)
        return picked

    known = known_urls(a.out)

    def with_known(sitemap_url, urls):
        """sitemap URL에 미러가 이미 아는 같은 host의 URL을 더한다(sitemap 축소 대비)."""
        return set(urls) | known.get(urlsplit(sitemap_url).netloc, set())

    state = load_state(a.out)
    scanned, changed, baselined, fails, empties, moved, budget = (
        0,
        0,
        0,
        [],
        [],
        [],
        (a.limit or 10**9),
    )

    # 1) HTML sitemaps (curl_cffi + bs4)
    for sm, keep in HTML_SITEMAPS:
        urls = todo([u for u in with_known(sm, sitemap_urls(sm)) if keep(u)])[
            : max(0, budget - scanned)
        ]
        if not urls:
            continue
        print(f"[{urlsplit(sm).netloc}] {len(urls)} 크롤", flush=True)
        p, f, e, mv = crawl(urls, fetch_html, a.concurrency)
        n, c, b = flush(p, a.out, state, a.force)
        scanned += n
        changed += c
        baselined += b
        fails += f
        empties += e
        moved += mv

    # 2) Mintlify docs (.md raw): platform.claude.com(API) + code.claude.com(Claude Code CLI)
    for dsm in DOCS_SITEMAPS:
        if scanned >= budget:
            break
        durls = todo([u for u in with_known(dsm, sitemap_urls(dsm)) if is_docs_en(u)])[
            : max(0, budget - scanned)
        ]
        if not durls:
            continue
        print(f"[{urlsplit(dsm).netloc}/docs] {len(durls)} 크롤(.md)", flush=True)
        p, f, e, mv = crawl(durls, fetch_docs_md, a.concurrency)
        n, c, b = flush(p, a.out, state, a.force)
        scanned += n
        changed += c
        baselined += b
        fails += f
        empties += e
        moved += mv

    # 3) sitemap 없는 연구 블로그 (홈 link discovery)
    for base, dom in DISCOVER:
        if scanned >= budget:
            break
        urls = todo(list(discover(base, dom) | known.get(dom, set())))[
            : max(0, budget - scanned)
        ]
        if not urls:
            continue
        print(f"[{dom}] {len(urls)} 크롤", flush=True)
        p, f, e, mv = crawl(urls, fetch_html, a.concurrency)
        n, c, b = flush(p, a.out, state, a.force)
        scanned += n
        changed += c
        baselined += b
        fails += f
        empties += e
        moved += mv

    # 4) SafeBase SPA (playwright 보강)
    spa = todo(SPA_PAGES)
    if spa and scanned < budget:
        print(f"[SPA] {len(spa)} playwright 보강", flush=True)
        n, c, seeded = flush(spa_rescue(spa), a.out, state, a.force)
        scanned += n
        changed += c
        baselined += seeded

    print(
        f"검사: {scanned} / 내용 변경 저장: {changed} / 기준선 등록: {baselined} / "
        f"본문없음 skip: {len(empties)} / 이전(redirect) skip: {len(moved)} / 실패: {len(fails)}",
        flush=True,
    )
    if empties:
        by = Counter(urlsplit(u).netloc for u in empties)
        print(
            "본문없음(업스트림 미발행·404, 재실행 시 자동 재확인): "
            + ", ".join(f"{h} {n}" for h, n in by.most_common()),
            flush=True,
        )
    if moved:
        by = Counter(urlsplit(u).netloc for u, _ in moved)
        print(
            "이전(업스트림이 다른 경로로 옮김 - 옛 경로 파일은 stale, 삭제 검토 대상): "
            + ", ".join(f"{h} {n}" for h, n in by.most_common()),
            flush=True,
        )
        for u, final in sorted(moved)[:20]:
            print(f"  {u} -> {final}", flush=True)
        if len(moved) > 20:
            print(f"  ... 외 {len(moved) - 20}건", flush=True)
    if fails:
        print("실패(재실행 시 자동 재시도):", flush=True)
        for u, err in fails[:20]:
            print(f"  {u} [{err}]", flush=True)


if __name__ == "__main__":
    main()
