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
from urllib.parse import parse_qs, urljoin, urlsplit
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
cm = importlib.util.module_from_spec(spec); spec.loader.exec_module(cm)

A = "https://www.anthropic.com"
IMPERSONATE = "chrome"  # anthropic.com은 일반 UA를 막는다 -> Chrome TLS/JA3 지문 위장
# claude.com sitemap은 첫 세그먼트로 로케일을 표기한다(ja/de/fr/ko/it ...). 영어 정본만 남긴다.
LOCALES = {"ja", "de", "fr", "ko", "it", "es", "pt", "zh", "nl", "pl", "ru", "id",
           "tr", "vi", "th", "ar", "hi", "ja-jp", "pt-br", "zh-cn", "zh-tw"}


def first_seg(url):
    parts = [x for x in urlsplit(url).path.split("/") if x]
    return parts[0] if parts else ""


def is_claude_en(u):
    return first_seg(u) not in LOCALES


# HTML 소스: (sitemap_url, keep_predicate). curl_cffi + bs4로 본문 추출.
HTML_SITEMAPS = [
    (f"{A}/sitemap.xml", lambda u: True),                                 # 실측 ~476 (news/research/engineering/events/legal/product/system-cards/economic 등 전량)
    ("https://claude.com/sitemap.xml", is_claude_en),                     # 실측 영어 ~1591 (blog/customers/resources/connectors/plugins/solutions ...)
    ("https://claude.com/docs/sitemap.xml", lambda u: True),              # 실측 ~127 (태그형 help 문서, robots.txt가 선언하는 2번째 sitemap)
    ("https://support.claude.com/sitemap.xml", lambda u: "/en/" in u),    # 실측 영어 ~370 (Help Center)
    ("https://privacy.claude.com/sitemap.xml", lambda u: "/en/" in u),   # Privacy Center 영어 정본
]
# Mintlify docs: sitemap의 각 URL + ".md"로 raw 마크다운을 받는다.
# platform = API/플랫폼 개발자 문서, code = Claude Code CLI 문서(hooks·subagents·settings·slash-commands·agent-sdk 등).
DOCS_SITEMAPS = [
    "https://platform.claude.com/sitemap.xml",   # 실측 영어 ~1755 (api 레퍼런스 포함)
    "https://code.claude.com/sitemap.xml",        # 실측 영어 ~154 (Claude Code CLI docs)
]


def is_docs_en(u):
    return "/docs/en/" in u


# sitemap 없는 정적 연구 블로그: 같은 도메인의 공개 본문을 지정 depth까지 수집.
DISCOVER = [
    ("https://alignment.anthropic.com/", "alignment.anthropic.com", 2),
    ("https://transformer-circuits.pub/", "transformer-circuits.pub", 2),
    ("https://platform.claude.com/cookbook/", "platform.claude.com", 1),
]
LINKED_HOSTS = {"resources.anthropic.com"}
NON_PAGE_SUFFIXES = (".xml", ".pdf", ".json", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".txt")
# SafeBase SPA: curl·​.md 둘 다 본문 0 -> playwright innerText 보강.
SPA_PAGES = [
    "https://trust.anthropic.com/",
    "https://trust.anthropic.com/resources",
    "https://trust.anthropic.com/subprocessors",
    "https://trust.anthropic.com/faq",
    "https://trust.anthropic.com/updates",
]
STATE_FILE = ".anthropic-mirror-state.json"


def get(url, suffix=""):
    r = requests.get(url + suffix, impersonate=IMPERSONATE, timeout=40)
    return r.status_code, r.text, str(getattr(r, "url", "") or "")


def redirected(requested, final):
    if not final:
        return False

    def normalized(url):
        parsed = urlsplit(url)
        path = re.sub(r"/index\.html?$", "/", parsed.path)
        if path.endswith(".md"):
            path = path[:-3]
        return parsed.netloc, path.rstrip("/")

    return normalized(requested) != normalized(final)


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
                _, ct, _ = get(c.strip()); urls.update(re.findall(r"<loc>(.*?)</loc>", ct))
            except Exception:
                pass
        return urls
    return set(l.strip() for l in locs)


_CFEMAIL = re.compile(r'\[([^\]]*)\]\((?:https?://[^)]*?)?/cdn-cgi/l/email-protection#([0-9a-fA-F]{8,})\)')


def _deob(h):
    """Cloudflare email obfuscation: 첫 바이트가 XOR 키, 나머지를 XOR해 ASCII 복원."""
    k = int(h[:2], 16)
    try:
        return "".join(chr(int(h[i:i + 2], 16) ^ k) for i in range(2, len(h), 2))
    except Exception:
        return None


def decode_cfemail(text):
    """[[email protected]](.../cdn-cgi/l/email-protection#HEX) -> [실제이메일](mailto:실제이메일)."""
    def r(m):
        e = _deob(m.group(2))
        return f"[{e}](mailto:{e})" if e and "@" in e else m.group(0)
    return _CFEMAIL.sub(r, text)


def absolute_url(base, ref):
    """페이지 기준 URL. Next.js image proxy는 원본 URL로 환원한다."""
    ref = (ref or "").strip()
    if not ref or ref.startswith(("data:", "blob:", "javascript:")):
        return ref
    parsed = urlsplit(ref)
    if parsed.path.endswith("/_next/image"):
        inner = parse_qs(parsed.query).get("url", [""])[0].strip()
        if inner:
            ref = inner
    return urljoin(base, ref)


def absolutize_html(node, base):
    for img in node.find_all("img", src=True):
        if not img["src"].startswith("data:"):
            img["src"] = absolute_url(base, img["src"])
    for a in node.find_all("a", href=True):
        if not a["href"].startswith(("#", "mailto:", "tel:", "javascript:")):
            a["href"] = urljoin(base, a["href"])


_MD_IMAGE = re.compile(r"(!\[[^\]]*\]\()(<[^>]+>|[^)\s]+)")


def absolutize_markdown_images(text, base):
    def replace(m):
        wrapped = m.group(2).startswith("<")
        ref = m.group(2)[1:-1] if wrapped else m.group(2)
        if ref.startswith(("http://", "https://", "data:")):
            return m.group(0)
        fixed = absolute_url(base, ref)
        return m.group(1) + (f"<{fixed}>" if wrapped else fixed)
    return _MD_IMAGE.sub(replace, text)


def html_to_md(html, base_url=""):
    """본문 컨테이너(main/article/body 중 텍스트가 가장 많은 것)를 골라 nav/header/footer/form 제거 후 markdown."""
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script", "style", "noscript", "svg"]):
        t.decompose()
    cands = [c for c in (soup.find("main"), soup.find("article"), soup.body) if c is not None]
    # Distill 템플릿(alignment.anthropic.com 일부)은 <body> 없이 최상위에 <d-article>을 둔다 -> 문서 전체로 fallback
    node = max(cands, key=lambda c: len(c.get_text(strip=True))) if cands else soup
    for t in node(["nav", "header", "footer", "form"]):
        t.decompose()
    if base_url:
        absolutize_html(node, base_url)
    text = decode_cfemail(md(str(node), heading_style="ATX").strip())
    text = "\n".join(line.rstrip() for line in text.splitlines())
    return absolutize_markdown_images(text, base_url) if base_url else text


def fetch_html(url):
    try:
        s, h, final = get(url)
        if s != 200:
            return url, "", f"status={s}"
        if redirected(url, final):
            return url, "", "stale=redirect"
        return url, html_to_md(h, final or url), ""
    except Exception as e:
        return url, "", str(e)[:80]


_DOCS_INDEX = re.compile(r"^(?:>[^\n]*\n)+", re.M)


def strip_docs_index(t):
    """code.claude.com .md는 매 페이지 상단에 llms.txt 안내 blockquote가 붙는다 -> 첫 'Documentation Index' 블록만 제거(H1 아래 페이지 설명 blockquote는 보존)."""
    if t.startswith("> ## Documentation Index"):
        m = _DOCS_INDEX.match(t)
        if m:
            return t[m.end():].lstrip()
    return t


def fetch_docs_md(url):
    """Mintlify: <url>.md가 깨끗한 마크다운(브라우저로 렌더한 SPA 본문과 동일)."""
    try:
        s, t, final = get(url, ".md")
        if s != 200:
            return url, "", f"status={s}"
        if redirected(url, final):
            return url, "", "stale=redirect"
        return url, absolutize_markdown_images(strip_docs_index(t.strip()), final or url), ""
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


def discover(base, dom, max_depth=1):
    """sitemap 없는 사이트를 same-host BFS하며 redirect 정본과 공개 본문만 반환."""
    out, seen, frontier = set(), set(), [(base, 0)]
    while frontier:
        requested, depth = frontier.pop(0)
        if requested in seen:
            continue
        seen.add(requested)
        try:
            status, html, final = get(requested)
        except Exception:
            continue
        if status != 200:
            continue
        canonical = (final or requested).split("#")[0].split("?")[0]
        if urlsplit(canonical).netloc != dom:
            continue
        if len(html_to_md(html, canonical)) >= 200:
            out.add(canonical)
        if depth >= max_depth:
            continue
        soup = BeautifulSoup(html, "html.parser")
        for anchor in soup.find_all("a", href=True):
            value = urljoin(canonical, anchor["href"]).split("#")[0].split("?")[0]
            parsed = urlsplit(value)
            if parsed.netloc == dom and "@" not in parsed.path and not parsed.path.lower().endswith(NON_PAGE_SUFFIXES):
                frontier.append((value, depth + 1))
    return out


def linked_urls(out, hosts):
    """이미 보관한 공식 페이지가 가리키는 sitemap 없는 소유 host URL을 찾는다."""
    found = set()
    pattern = re.compile(r"https://(?:" + "|".join(map(re.escape, hosts)) + r''')/[^\s<>)\]'\"]+''')
    for root, dirs, files in os.walk(out):
        dirs[:] = [d for d in dirs if d not in (".git", ".claude", ".agents", "_yt-cache")]
        for name in files:
            if not name.endswith(".md"):
                continue
            try:
                text = open(os.path.join(root, name), encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            for value in pattern.findall(text):
                value = value.rstrip(".,;")
                if not urlsplit(value).path.lower().endswith(NON_PAGE_SUFFIXES):
                    found.add(value)
    return found


_SOURCE = re.compile(r"^<!--\s*(?:source:\s*)?(https://\S+?)\s*-->")


def known_urls(out):
    """sitemap 축소 뒤에도 기존 source URL을 계속 재확인한다."""
    by_host = {}
    for root, dirs, files in os.walk(out):
        dirs[:] = [d for d in dirs if d not in (".git", ".claude", ".agents", "_yt-cache")]
        for name in files:
            if not name.endswith(".md"):
                continue
            try:
                with open(os.path.join(root, name), encoding="utf-8", errors="replace") as f:
                    first = f.readline().strip()
            except OSError:
                continue
            m = _SOURCE.match(first)
            if m:
                by_host.setdefault(urlsplit(m.group(1)).netloc, set()).add(m.group(1))
    return by_host


def crawl(urls, fetch, concurrency):
    pages, fails, empties, stale = {}, [], [], []
    with ThreadPoolExecutor(max_workers=concurrency) as ex:
        futs = {ex.submit(fetch, u): u for u in urls}
        done = 0
        for f in as_completed(futs):
            url, mdtext, err = f.result()
            done += 1
            if mdtext and len(mdtext) >= 200:  # 200자 미만은 빈 SPA 셸·404 본문
                pages[url] = mdtext
            elif err in ("status=404", "stale=redirect"):
                stale.append(url)
            elif err == "":
                # 업스트림에 본문 자체가 없음(미발행 .md·redirect 셸·sitemap의 404) -> 실패 아님.
                # 저장하지 않으므로 매 실행 재확인되고, 업스트림이 발행하면 자동 수집된다.
                empties.append(url)
            else:
                fails.append((url, err))
            if done % 100 == 0:
                print(f"  {done}/{len(urls)} (성공 {len(pages)}, 없음 {len(empties)}, 실패 {len(fails)})", flush=True)
    return pages, fails, empties, stale


def prune_stale(out, urls):
    """404/redirect가 확정된 source 파일만 제거한다. git에서 복구 가능하다."""
    removed = 0
    for url in urls:
        path, _ = cm.dest(out, url)
        try:
            with open(path, encoding="utf-8", errors="replace") as f:
                first = f.readline().strip()
        except OSError:
            continue
        match = _SOURCE.match(first)
        if match and match.group(1) == url:
            os.remove(path)
            removed += 1
    return removed


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
    if not force and (previous == digest or (previous is None and os.path.exists(path))):
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
    ap.add_argument("--only", default="", help="이 host substring을 가진 URL만 크롤(예: claude.com)")
    ap.add_argument("--force", action="store_true", help="본문 해시와 무관하게 검사 결과를 다시 저장")
    ap.add_argument("--prune-stale", action="store_true", help="live 404/canonical redirect source 파일 제거")
    ap.add_argument("--url-file", help="sitemap 발견 대신 줄 단위 URL 목록만 표적 재수집")
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
            assert absolute_url(url, "fig.png") == "https://example.com/fig.png"
            assert absolute_url(url, "/_next/image?url=https%3A%2F%2Fcdn.example%2Fx.png&w=64") == "https://cdn.example/x.png"
            assert "https://example.com/docs/x.png" in absolutize_markdown_images("![](/docs/x.png)", url)
            assert html_to_md("<main><p>x  </p></main>") == "x"
            assert redirected(url, "https://example.com/other")
            assert not redirected(url, url + "/")
        print("self-test ok")
        return

    crawled = set()

    def todo(urls):
        urls = [u for u in urls if (not a.only) or (a.only in u)]
        picked = sorted(set(urls) - crawled)
        crawled.update(picked)
        return picked

    known = known_urls(a.out)
    state = load_state(a.out)
    scanned, changed, baselined, fails, empties, stale, budget = 0, 0, 0, [], [], [], (a.limit or 10 ** 9)

    if a.url_file:
        with open(a.url_file, encoding="utf-8") as f:
            selected = todo(line.strip() for line in f if line.strip() and not line.startswith("#"))
        docs = [u for u in selected if urlsplit(u).netloc in ("platform.claude.com", "code.claude.com") and "/docs/" in urlsplit(u).path]
        html = sorted(set(selected) - set(docs))
        for label, urls, fetch in (("target/html", html, fetch_html), ("target/docs", docs, fetch_docs_md)):
            if not urls:
                continue
            print(f"[{label}] {len(urls)} 크롤", flush=True)
            p, f, e, s = crawl(urls[:budget - scanned], fetch, a.concurrency)
            n, c, b = flush(p, a.out, state, a.force)
            scanned += n; changed += c; baselined += b; fails += f; empties += e; stale += s
        removed = prune_stale(a.out, stale) if a.prune_stale else 0
        print(f"검사: {scanned} / 내용 변경 저장: {changed} / 기준선 등록: {baselined} / 본문없음 skip: {len(empties)} / stale: {len(stale)} / 제거: {removed} / 실패: {len(fails)}", flush=True)
        return

    # 1) HTML sitemaps (curl_cffi + bs4)
    for sm, keep in HTML_SITEMAPS:
        if a.only and a.only not in urlsplit(sm).netloc:
            continue
        discovered = sitemap_urls(sm) | known.get(urlsplit(sm).netloc, set())
        urls = todo([u for u in discovered if keep(u)])[:max(0, budget - scanned)]
        if not urls:
            continue
        print(f"[{urlsplit(sm).netloc}] {len(urls)} 크롤", flush=True)
        p, f, e, s = crawl(urls, fetch_html, a.concurrency)
        n, c, b = flush(p, a.out, state, a.force); scanned += n; changed += c; baselined += b; fails += f; empties += e; stale += s

    # 2) Mintlify docs (.md raw): platform.claude.com(API) + code.claude.com(Claude Code CLI)
    for dsm in DOCS_SITEMAPS:
        if scanned >= budget:
            break
        if a.only and a.only not in urlsplit(dsm).netloc:
            continue
        discovered = sitemap_urls(dsm) | known.get(urlsplit(dsm).netloc, set())
        durls = todo([u for u in discovered if is_docs_en(u)])[:max(0, budget - scanned)]
        if not durls:
            continue
        print(f"[{urlsplit(dsm).netloc}/docs] {len(durls)} 크롤(.md)", flush=True)
        p, f, e, s = crawl(durls, fetch_docs_md, a.concurrency)
        n, c, b = flush(p, a.out, state, a.force); scanned += n; changed += c; baselined += b; fails += f; empties += e; stale += s

    # 3) sitemap 없는 연구 블로그 (홈 link discovery)
    for base, dom, depth in DISCOVER:
        if scanned >= budget:
            break
        if a.only and a.only not in dom:
            continue
        urls = todo(list(discover(base, dom, depth) | known.get(dom, set())))[:max(0, budget - scanned)]
        if not urls:
            continue
        print(f"[{dom}] {len(urls)} 크롤", flush=True)
        p, f, e, s = crawl(urls, fetch_html, a.concurrency)
        n, c, b = flush(p, a.out, state, a.force); scanned += n; changed += c; baselined += b; fails += f; empties += e; stale += s

    # 4) 루트가 다른 곳으로 redirect하는 공개 리소스 host는 보관 문서의 outbound link에서 발견한다.
    linked_hosts = {h for h in LINKED_HOSTS if not a.only or a.only in h}
    linked = todo(
        u for u in linked_urls(a.out, linked_hosts) | set().union(*(known.get(h, set()) for h in linked_hosts))
        if not urlsplit(u).path.lower().endswith(NON_PAGE_SUFFIXES)
    ) if linked_hosts else []
    if linked and scanned < budget:
        print(f"[linked hosts] {len(linked)} 크롤", flush=True)
        p, f, e, s = crawl(linked[:max(0, budget - scanned)], fetch_html, a.concurrency)
        n, c, b = flush(p, a.out, state, a.force); scanned += n; changed += c; baselined += b; fails += f; empties += e; stale += s

    # 5) SafeBase SPA (playwright 보강)
    spa = todo(SPA_PAGES) if not a.only or a.only in "trust.anthropic.com" else []
    if spa and scanned < budget:
        print(f"[SPA] {len(spa)} playwright 보강", flush=True)
        n, c, seeded = flush(spa_rescue(spa), a.out, state, a.force); scanned += n; changed += c; baselined += seeded

    removed = prune_stale(a.out, stale) if a.prune_stale else 0
    print(f"검사: {scanned} / 내용 변경 저장: {changed} / 기준선 등록: {baselined} / 본문없음 skip: {len(empties)} / stale: {len(stale)} / 제거: {removed} / 실패: {len(fails)}", flush=True)
    if empties:
        by = Counter(urlsplit(u).netloc for u in empties)
        print("본문없음(업스트림 미발행·redirect·404, 재실행 시 자동 재확인): "
              + ", ".join(f"{h} {n}" for h, n in by.most_common()), flush=True)
    if fails:
        print("실패(재실행 시 자동 재시도):", flush=True)
        for u, err in fails[:20]:
            print(f"  {u} [{err}]", flush=True)


if __name__ == "__main__":
    main()
