"""anthropic.com + claude.com + claude docs + support + 연구 블로그 공개 페이지 전체 크롤 (강의 제외).

sitemap.xml을 1차 소스로 쓴다 -- 사이트가 새 섹션을 추가해도 빠짐없이 따라간다(하드코딩 목록·See more 펼치기 폐기).
curl_cffi(impersonate="chrome")로 anthropic.com의 봇 차단을 우회한다 -- plain fetch는 본문 0이지만 chrome 지문이면 SSR 본문이 그대로 온다(브라우저·캡챠 불필요).
platform.claude.com/docs는 Mintlify SPA라 HTML엔 본문이 없지만 페이지별 <url>.md raw가 깨끗한 마크다운을 준다 -> .md로 받는다(브라우저 불필요).
trust.anthropic.com만 SafeBase SPA(curl도 .md도 본문 0)라 playwright innerText로 보강한다.

저장: <out>/<host>/<path>.md (academy의 anthropic.skilljar.com/과 같은 도메인 트리). 모든 URL을 검사하고 실제 마크다운이 달라진 파일만 갱신.
확정적 빈 페이지(404 또는 200이지만 본문<200자 -- 미발행 .md·redirect 셸)는 실패가 아니라 '본문없음 skip'으로 분류한다. 저장하지 않으므로 매 실행 재확인되고 업스트림이 발행하면 자동 수집된다.
crawl-mirror.py의 dest/save/find_boilerplate/strip_boilerplate를 재사용한다.

미해결 URL(404·redirect·login wall·thin·403·5xx·timeout)은 삭제하거나 성공으로 넘기지 않고
.anthropic-mirror-status.json에 분류와 함께 host별로 기록한다(coverage-audit·verify-publish가 읽는다).
--plan-json은 페이지 본문을 받지 않고 수집 대상 집합(C)만 JSON으로 쓴다.

실행: python3 crawl-site.py <out_dir> [--only <host>] [--force] [--limit N] [--concurrency N] [--plan-json FILE]
"""

import argparse, base64, hashlib, importlib.util, json, os, re
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
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)
_common_spec = importlib.util.spec_from_file_location(
    "mirror_common",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "mirror-common.py"),
)
mc = importlib.util.module_from_spec(_common_spec)
_common_spec.loader.exec_module(mc)

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
        "https://claude.dev/sitemap.xml",
        lambda u: True,
    ),  # Claude 공식 블로그/터미널 공개 표면
    (
        "https://claude.com/docs/sitemap.xml",
        lambda u: True,
    ),  # 실측 ~127 (태그형 help 문서, robots.txt가 선언하는 2번째 sitemap)
    # platform robots.txt가 docs sitemap과 별도로 선언한다. 홈 1-depth 탐색만으로는 목록 밖 레시피를 놓친다.
    (
        "https://platform.claude.com/cookbook/sitemap.xml",
        lambda u: "/cookbook" in urlsplit(u).path,
    ),
    (
        "https://support.claude.com/sitemap.xml",
        lambda u: "/en/" in u,
    ),  # 실측 영어 ~370 (Help Center)
    (
        "https://privacy.claude.com/sitemap.xml",
        lambda u: "/en/" in u,
    ),  # Privacy Center 영어 정본
    # Academy(구 anthropic.skilljar.com에서 이전). 실측 725: courses 438(코스 22 + 레슨 415),
    # use-cases 149, tutorials 120, products 8, collections 7. 전량 영어라 로케일 필터 불필요.
    # 레슨 본문까지 SSR로 오므로 브라우저가 필요 없다(curl_cffi impersonate로 3,800자+).
    # robots.txt가 막는 경로(/api/, /login, /dashboard, /badges/, /certificates/ 등)는
    # sitemap에 없지만, 나중에 섞여도 수집하지 않도록 예측자로 한 번 더 막는다.
    ("https://academy.claude.com/sitemap.xml", lambda u: not academy_blocked(u)),
]

# academy.claude.com/robots.txt의 Disallow 목록. 공개 sitemap만 따르더라도
# 사이트가 규칙을 바꿨을 때 조용히 넘어가지 않도록 수집기 쪽에서도 지킨다.
ACADEMY_DISALLOW = (
    "/api/",
    "/mcp",
    "/search-corpus.json",
    "/admin/",
    "/badges/",
    "/certificates/",
    "/dashboard",
    "/settings",
    "/garden",
    "/login",
    "/oauth/",
    "/start",
    "/welcome",
    "/goodbye",
    "/fluency-check-in",
)
# 본문 컨테이너를 <main>으로 고정하고 그 안의 nav/header를 보존할 호스트.
# academy는 코스 커리큘럼(레슨 목차)을 <main> 안 <nav>에, 코스 제목을 <header>에 둔다.
MAIN_ONLY_HOSTS = {"academy.claude.com"}


def academy_blocked(u):
    path = urlsplit(u).path
    return any(path == d.rstrip("/") or path.startswith(d) for d in ACADEMY_DISALLOW)


# Mintlify docs: sitemap의 각 URL + ".md"로 raw 마크다운을 받는다.
# platform = API/플랫폼 개발자 문서, code = Claude Code CLI 문서(hooks·subagents·settings·slash-commands·agent-sdk 등).
DOCS_SITEMAPS = [
    "https://platform.claude.com/sitemap.xml",  # 실측 영어 ~1755 (api 레퍼런스 포함)
    "https://code.claude.com/sitemap.xml",  # 실측 영어 ~154 (Claude Code CLI docs)
    "https://code.claude.com/docs/sitemap.xml",  # code robots.txt가 선언하는 docs 전용 sitemap
]


def is_docs_en(u):
    return "/docs/en/" in u


def docs_route(u):
    """docs host의 /docs/ 경로인가. 이 경로는 raw Markdown(fetch_docs_md)으로만 받고 영어 정본만 남긴다.
    HTML로 받으면 쿠키 배너·사이드바가 본문이 되고, 먼저 저장한 Markdown을 덮어쓴다."""
    parts = urlsplit(u)
    return parts.netloc in {
        urlsplit(d).netloc for d in DOCS_SITEMAPS
    } and parts.path.startswith("/docs/")


# sitemap 없는 정적 사이트: 같은 도메인의 공개 본문을 지정 depth까지 수집.
DISCOVER = [
    ("https://alignment.anthropic.com/", "alignment.anthropic.com", 2),
    ("https://transformer-circuits.pub/", "transformer-circuits.pub", 2),
    ("https://platform.claude.com/cookbook/", "platform.claude.com", 1),
    # 파트너 포털 루트는 로그인으로 가지만 디렉터리와 파트너 상세는 공개 SSR이다.
    ("https://partnerhub.claude.com/directory", "partnerhub.claude.com", 1),
]
# 루트가 다른 곳으로 redirect하거나 sitemap이 없는 공식 host. 보관 문서의 outbound link에서 URL을 찾는다.
# red.anthropic.com 글 대부분은 www.anthropic.com/research로 옮겨졌고, host에 남은 목록·부속 페이지만 이 경로로 잡힌다.
LINKED_HOSTS = {"resources.anthropic.com", "red.anthropic.com"}
NON_PAGE_SUFFIXES = (
    ".xml",
    ".pdf",
    ".json",
    ".jsonl",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".txt",
    ".md",
    ".csv",
    ".zip",
    ".mp4",
    ".mov",
    ".webm",
    ".docx",
    ".pptx",
    ".xlsx",
    ".ipynb",
)
# SafeBase SPA: curl·​.md 둘 다 본문 0 -> playwright innerText 보강.
SPA_PAGES = [
    "https://trust.anthropic.com/",
    "https://trust.anthropic.com/resources",
    "https://trust.anthropic.com/subprocessors",
    "https://trust.anthropic.com/faq",
    "https://trust.anthropic.com/updates",
]
STATE_FILE = ".anthropic-mirror-state.json"
NO_BOILERPLATE_STRIP = {"platform.claude.com", "code.claude.com", "trust.anthropic.com"}


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


def same_host(requested, final):
    return urlsplit(requested).netloc == urlsplit(final).netloc


def declared_sitemaps(host):
    """robots.txt가 선언한 sitemap. 사이트가 sitemap을 추가하면 설정 변경 없이 따라간다."""
    try:
        status, text, _ = get(f"https://{host}/robots.txt")
    except Exception as e:
        print(f"  robots ERR {host}: {str(e)[:80]}", flush=True)
        return []
    if status != 200:
        return []
    return [m.strip() for m in re.findall(r"(?im)^\s*sitemap:\s*(\S+)", text)]


def sitemap_urls(sm):
    """sitemap 또는 중첩된 sitemap index를 cycle-safe하게 끝까지 펼친다."""
    pending, seen, urls = [sm], set(), set()
    while pending:
        current = pending.pop()
        if current in seen:
            continue
        seen.add(current)
        try:
            _, text, _ = get(current)
        except Exception as e:
            print(f"  sitemap ERR {current}: {e}", flush=True)
            continue
        locs = [loc.strip() for loc in re.findall(r"<loc>(.*?)</loc>", text)]
        children = [loc for loc in locs if loc.lower().endswith(".xml")]
        if children and len(children) == len(locs):
            pending.extend(children)
        else:
            urls.update(locs)
    return urls


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


LAZY_SRC_ATTRS = ("data-src", "data-lazy-src", "data-original", "data-srcset", "srcset")


def image_source(img):
    """src가 비었으면 lazy-load 속성에서 실제 자산 URL을 찾는다."""
    src = (img.get("src") or "").strip()
    if src and not src.startswith(
        "data:image/gif;base64,R0lGOD"
    ):  # 1x1 투명 placeholder
        return src
    for attr in LAZY_SRC_ATTRS:
        value = (img.get(attr) or "").strip()
        if value:
            return value.split(",")[0].strip().split(" ")[0]
    return src


def missing_image_marker(label):
    """원본에 받을 자산이 없는 이미지는 깨진 참조 대신 명시 상태로 남긴다. 대체 텍스트도 없으면 장식 이미지다."""
    label = " ".join((label or "").split())
    return f"[미수집 이미지: {label}]" if label else ""


def absolutize_html(node, base):
    for img in node.find_all("img"):
        src = image_source(img)
        if not src:
            marker = missing_image_marker(img.get("alt", ""))
            if marker:
                img.replace_with(marker)
            else:
                img.decompose()
        elif src.startswith("attachment:"):
            label = img.get("alt", "attachment")
            img.replace_with(f"[미수집 첨부 이미지: {label}]")
        elif not src.startswith("data:"):
            img["src"] = absolute_url(base, src)
    for a in node.find_all("a", href=True):
        if not a["href"].startswith(("#", "mailto:", "tel:", "javascript:")):
            a["href"] = urljoin(base, a["href"])


_MD_IMAGE = re.compile(r"(!\[[^\]]*\]\()(<[^>]+>|[^)\s]+)")
_EMPTY_MD_IMAGE = re.compile(r"!\[([^\]]*)\]\(\s*\)")
_MD_ROOT_LINK = re.compile(r"(?<!!)(\[[^\]\n]*\]\()(/(?!/)[^)\s]*)")
# 확장자가 있거나 /로 끝나는 상대 링크(build.md, clip.mp4, sub/)만 원본 기준으로 푼다. 괄호 속 일반 텍스트는 두지 않는다.
_MD_REL_LINK = re.compile(
    r"(?<!!)(\[[^\]\n]*\]\()((?![a-zA-Z][a-zA-Z0-9+.-]*:|/|#)[^)\s]*(?:\.[A-Za-z0-9]{1,5}|/)(?:#[^)\s]*)?)(?=\))"
)
_FENCE = re.compile(r"^(```|~~~)")


def absolutize_markdown_images(text, base):
    def replace(m):
        wrapped = m.group(2).startswith("<")
        ref = m.group(2)[1:-1] if wrapped else m.group(2)
        if ref.startswith(("http://", "https://", "data:")):
            return m.group(0)
        fixed = absolute_url(base, ref)
        return m.group(1) + (f"<{fixed}>" if wrapped else fixed)

    # ![alt]()는 해석 가능한 자산이 아니다. 대체 텍스트가 있으면 미수집 상태로, 없으면 제거한다.
    text = _EMPTY_MD_IMAGE.sub(lambda m: missing_image_marker(m.group(1)), text)
    return _MD_IMAGE.sub(replace, text)


def absolutize_markdown_links(text, base):
    """root-relative·상대 링크는 미러 안에서 해석되지 않으므로 원본 페이지 기준 절대 URL로 바꾼다.

    코드 블록과 인라인 코드 안의 예시는 건드리지 않는다.
    """
    root = f"{urlsplit(base).scheme}://{urlsplit(base).netloc}"
    out, fenced = [], False
    for line in text.split("\n"):
        if _FENCE.match(line.lstrip()):
            fenced = not fenced
            out.append(line)
            continue
        if fenced or "](" not in line:
            out.append(line)
            continue
        # 인라인 코드를 같은 길이로 가려 위치를 보존한다. 코드 안의 예시 링크는 매칭되지 않고,
        # 링크 텍스트에 인라인 코드가 있는 [`/cmd`](/docs/x)는 매칭된다.
        masked = re.sub(
            r"`[^`]*`", lambda m: "`" + "x" * (len(m.group(0)) - 2) + "`", line
        )
        edits = []
        for pattern, absolute in (
            (_MD_ROOT_LINK, lambda ref: root + ref),
            (_MD_REL_LINK, lambda ref: urljoin(base, ref)),
        ):
            for m in pattern.finditer(masked):
                if not any(
                    start < m.end(2) and m.start(2) < end for start, end, _ in edits
                ):
                    edits.append(
                        (m.start(2), m.end(2), absolute(line[m.start(2) : m.end(2)]))
                    )
        for start, end, value in sorted(edits, reverse=True):
            line = line[:start] + value + line[end:]
        out.append(line)
    return "\n".join(out)


_PUA = re.compile(r"[\ue000-\uf8ff]")
_SENSITIVE_QUERY = re.compile(r"(?i)([?&]tracker=)[^&\s`)>\]]+")


def redact_sensitive_query(text):
    """Keep connector URLs useful without publishing provider tracking keys."""
    return _SENSITIVE_QUERY.sub(r"\1REDACTED", text)


def html_to_md(html, base_url=""):
    """본문 컨테이너(main/article/body 중 텍스트가 가장 많은 것)를 골라 nav/header/footer/form 제거 후 markdown.

    MAIN_ONLY_HOSTS는 예외다. academy.claude.com은 코스 커리큘럼을 <main> 안 <nav>에,
    코스 제목을 <header>에 두기 때문에 통상 제거 규칙이 제목과 레슨 목차를 통째로 지운다
    (실측: 코스 랜딩 22개 전부 H1 소실, claude-101 레슨 링크 16개 -> 0개).
    이 호스트는 사이트 크롬이 <main> 밖에 있으므로 컨테이너를 main으로 고정하는 것만으로 충분하다.
    고정 없이 제거만 풀면 텍스트 최대치 후보로 <body>가 뽑혀 상단 nav와 쿠키 배너가 유입된다.
    """
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script", "style", "noscript", "svg"]):
        t.decompose()
    main_only = urlsplit(base_url).netloc in MAIN_ONLY_HOSTS
    node = soup.find("main") if main_only else None
    if node is None:
        cands = [
            c
            for c in (soup.find("main"), soup.find("article"), soup.body)
            if c is not None
        ]
        # Distill 템플릿(alignment.anthropic.com 일부)은 <body> 없이 최상위에 <d-article>을 둔다 -> 문서 전체로 fallback
        node = max(cands, key=lambda c: len(c.get_text(strip=True))) if cands else soup
        for t in node(["nav", "header", "footer", "form"]):
            t.decompose()
    if base_url:
        absolutize_html(node, base_url)
    text = decode_cfemail(md(str(node), heading_style="ATX").strip())
    # 아이콘 폰트가 쓰는 사설 사용 영역(PUA) 코드포인트는 본문에서 깨진 글자로만 남는다.
    text = _PUA.sub("", text)
    text = "\n".join(line.rstrip() for line in text.splitlines())
    if base_url:
        text = absolutize_markdown_links(
            absolutize_markdown_images(text, base_url), base_url
        )
    return redact_sensitive_query(text)


_JS_REDIRECT = re.compile(r"(?i)you will be redirected|redirecting\b")
_META_REFRESH = re.compile(r"""(?i)<meta[^>]+http-equiv=["']?refresh[^>]+url=""")
_H1 = re.compile(r"^# \S", re.M)
# 제목이 있고 정적 본문이 100자 이상인 짧은 페이지(글 1개짜리 목록 hub 등)는 빈 셸이 아니라 완결된 페이지다.
MIN_SHORT_PAGE = 100


def content_node(soup):
    """사이트 크롬을 뺀 본문 후보(main > article > body)."""
    for t in soup(["script", "style", "noscript", "svg", "template"]):
        t.decompose()
    node = soup.find("main") or soup.find("article") or soup.body or soup
    for t in node(["nav", "header", "footer", "form"]):
        t.decompose()
    return node


def thin_reason(html, text):
    """정제 본문이 200자 미만일 때 이유를 가른다.

    JS 리다이렉트 셸은 redirect, 본문 영역이 SSR에서 비어 있으면 렌더가 필요한 js-shell,
    <main>조차 없이 정적 글자가 없으면 JS 전용(js-only), 짧지만 제목 있는 페이지는 정상(""),
    그 밖에는 추출 결함("thin")이다.
    """
    if _JS_REDIRECT.search(text) or _META_REFRESH.search(html):
        return "thin=redirect"
    soup = BeautifulSoup(html, "html.parser")
    has_main = soup.find("main") is not None or soup.find("article") is not None
    visible = content_node(soup).get_text(" ", strip=True)
    if len(visible) < 50:
        return "thin=js-shell" if has_main else "thin=js-only"
    if _H1.search(text) and len(text) >= MIN_SHORT_PAGE:
        return ""
    return "thin"


def fetch_html(url):
    try:
        s, h, final = get(url)
        if s != 200:
            return url, "", f"status={s}"
        canonical = final or url
        if mc.classify_http(200, canonical) == ("auth_blocked", "login wall"):
            return canonical, "", "auth=login"
        if urlsplit(canonical).path.lower().endswith(".pdf") or h.startswith("%PDF-"):
            return (
                canonical,
                "",
                "asset=pdf",
            )  # PDF는 pdf-mirror 몫이다. HTML로 파싱하면 재귀 한도를 넘는다.
        text = html_to_md(h, canonical)
        if len(text) >= 200:
            return canonical, text, ""
        reason = thin_reason(h, text)
        return canonical, (text if reason == "" else ""), reason
    except Exception as e:
        return url, "", str(e)[:80]


_DOCS_INDEX = re.compile(r"^(?:>[^\n]*\n)+", re.M)


def strip_docs_index(t):
    """code.claude.com .md는 매 페이지 상단에 llms.txt 안내 blockquote가 붙는다 -> 첫 'Documentation Index' 블록만 제거(H1 아래 페이지 설명 blockquote는 보존)."""
    if t.startswith("> ## Documentation Index"):
        m = _DOCS_INDEX.match(t)
        if m:
            return t[m.end() :].lstrip()
    return t


DOCS_MD_START = re.compile(r"---\s*\n|# ")


def fetch_docs_md(url):
    """Mintlify: <url>.md가 깨끗한 마크다운(브라우저로 렌더한 SPA 본문과 동일)."""
    try:
        s, t, final = get(url, ".md")
        if s != 200:
            return url, "", f"status={s}"
        canonical = final or url
        if canonical.endswith(".md"):
            canonical = canonical[:-3]
        if not same_host(url, canonical):
            return canonical, "", "stale=redirect"
        doc = strip_docs_index(t.strip())
        if not DOCS_MD_START.match(doc):
            # .md 엔드포인트가 간헐적으로 HTML 셸이나 HTML을 변환한 페이지(쿠키 배너부터 시작)를 준다.
            # 정상 문서는 docs 안내 블록을 걷어내면 frontmatter나 H1으로 시작한다. 그 밖의 응답을 저장하면 페이지 크롬이 본문이 된다.
            return canonical, "", "html=docs-md"
        text = redact_sensitive_query(
            absolutize_markdown_links(
                absolutize_markdown_images(doc, canonical), canonical
            )
        )
        if len(text) >= 200 or (_H1.search(text) and len(text) >= MIN_SHORT_PAGE):
            return canonical, text, ""
        return canonical, "", "thin"  # 미발행 .md·redirect 셸
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
            if (
                parsed.netloc == dom
                and "@" not in parsed.path
                and not parsed.path.lower().endswith(NON_PAGE_SUFFIXES)
            ):
                frontier.append((value, depth + 1))
    return out


def page_candidate(url):
    """링크로 발견한 URL이 수집할 페이지인가. 자산·깨진 링크·manifest 판정 URL은 뺀다."""
    parts = urlsplit(url)
    path = parts.path
    if parts.scheme not in ("http", "https") or not parts.netloc:
        return False
    if path.lower().rstrip("/").endswith(NON_PAGE_SUFFIXES) or re.search(
        r"[@{}\s]|%20", path
    ):
        return False
    if any(seg in path for seg in ("/_next/", "/cdn-cgi/", "/static/")):
        return False
    return mc.url_decision(url) is None


def home_links(host):
    """host 홈의 same-host 링크(내비게이션·hub). sitemap이 빠뜨린 공개 route의 발견 수단이다."""
    try:
        status, html, final = get(f"https://{host}/")
    except Exception:
        return set()
    if status != 200 or urlsplit(final or "").netloc not in ("", host):
        return set()
    soup = BeautifulSoup(html, "html.parser")
    links = {
        urljoin(final or f"https://{host}/", a["href"]).split("#")[0].split("?")[0]
        for a in soup.find_all("a", href=True)
    }
    return {u for u in links if urlsplit(u).netloc == host}


def spa_routes(base):
    """SPA 홈을 렌더해 same-host route를 모은다. 렌더 실패면 빈 집합(설정된 SPA_PAGES만 쓴다)."""
    host = urlsplit(base).netloc
    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(base, wait_until="domcontentloaded", timeout=30000)
            page.wait_for_timeout(6000)  # SafeBase는 내비게이션도 늦게 렌더
            hrefs = page.eval_on_selector_all("a[href]", "els => els.map(e => e.href)")
            browser.close()
    except Exception as e:
        print(f"  SPA route ERR {base}: {str(e)[:80]}", flush=True)
        return set()
    routes = {h.split("#")[0].split("?")[0].rstrip("/") for h in hrefs}
    return {u for u in routes if urlsplit(u).netloc == host and page_candidate(u)}


def linked_urls(out, hosts):
    """이미 보관한 공식 페이지가 가리키는 해당 host URL을 찾는다(outbound·same-host 링크 발견)."""
    found = set()
    pattern = re.compile(
        r"https://(?:" + "|".join(map(re.escape, hosts)) + r""")/[^\s<>)\]'\"]+"""
    )
    for root, dirs, files in os.walk(out):
        dirs[:] = [
            d for d in dirs if d not in (".git", ".claude", ".agents", "_yt-cache")
        ]
        for name in files:
            if not name.endswith(".md"):
                continue
            try:
                text = open(
                    os.path.join(root, name), encoding="utf-8", errors="replace"
                ).read()
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
        dirs[:] = [
            d for d in dirs if d not in (".git", ".claude", ".agents", "_yt-cache")
        ]
        for name in files:
            if not name.endswith(".md"):
                continue
            try:
                with open(
                    os.path.join(root, name), encoding="utf-8", errors="replace"
                ) as f:
                    first = f.readline().strip()
            except OSError:
                continue
            m = _SOURCE.match(first)
            if m:
                by_host.setdefault(urlsplit(m.group(1)).netloc, set()).add(m.group(1))
    return by_host


def unresolved(requested, url, err):
    """crawl 결과 하나를 미해결 항목으로 분류한다. 정상 저장이면 None."""
    if err == "stale=redirect":
        return {
            "url": requested,
            "class": "stale_or_redirect",
            "reason": f"cross-host redirect -> {url}",
        }
    if err == "auth=login":
        return {"url": requested, "class": "auth_blocked", "reason": "login wall"}
    if err.startswith("status="):
        code = int(err.split("=", 1)[1] or 0)
        cls, reason = mc.classify_http(code)
        return {"url": requested, "class": cls, "reason": reason}
    if err == "asset=pdf":
        return {
            "url": requested,
            "class": "stale_or_redirect",
            "reason": f"PDF로 리다이렉트 -> {url}",
        }
    if err == "thin=redirect":
        return {
            "url": requested,
            "class": "stale_or_redirect",
            "reason": "JS 리다이렉트 셸(본문 없음)",
        }
    if err == "thin=js-only":
        return {
            "url": requested,
            "class": "intentional_exclusion",
            "reason": "JS 전용 렌더(정적 HTML에 본문 영역 없음)",
        }
    if err == "thin=js-shell":
        return {
            "url": requested,
            "class": "extract_failed",
            "reason": "SSR 본문 영역이 비어 있고 렌더 보강도 실패",
        }
    if err in ("", "thin"):
        return {
            "url": requested,
            "class": "extract_failed",
            "reason": "thin: HTML 본문 영역에 글이 있으나 정제 본문 200자 미만",
        }
    if err == "html=docs-md":
        return {
            "url": requested,
            "class": "refresh_pending",
            "reason": "docs .md 엔드포인트가 Markdown 대신 HTML을 반환(재시도 대상)",
        }
    return {"url": requested, "class": "refresh_pending", "reason": f"network: {err}"}


def collected_hosts():
    """crawl-site가 스스로 발견·정제하는 host. 다른 host로 리다이렉트된 본문은 그 host의 수집기 몫이다."""
    hosts = {urlsplit(sm).netloc for sm, _ in HTML_SITEMAPS} | {
        urlsplit(sm).netloc for sm in DOCS_SITEMAPS
    }
    return (
        hosts
        | {dom for _, dom, _ in DISCOVER}
        | set(LINKED_HOSTS)
        | {urlsplit(u).netloc for u in SPA_PAGES}
    )


INLINE_PNG = re.compile(r"data:image/png;base64,([A-Za-z0-9+/=]+)")


def truncated_inline_png(text):
    """인라인 base64 PNG 중 IEND로 끝나지 않는 것이 있는가."""
    for m in INLINE_PNG.finditer(text):
        try:
            data = base64.b64decode(m.group(1) + "=" * (-len(m.group(1)) % 4))
        except ValueError:
            return True
        if b"IEND" not in data[-16:]:
            return True
    return False


def foreign_target(requested, url):
    """리다이렉트 대상이 이 수집기의 범위 밖(제품 앱·Skilljar 랜딩·manifest 제외)인가.
    docs 경로 목적지는 crawl()이 fetch 종류를 보고 따로 거른다."""
    host = urlsplit(url).netloc
    if host == urlsplit(requested).netloc:
        return mc.url_decision(url) is not None
    return host not in collected_hosts() or mc.url_decision(url) is not None


def render_shells(shells):
    """SSR에서 본문 영역이 빈 페이지를 렌더해 main/article 본문을 다시 추출한다. [(requested, url, markdown)]."""
    if not shells:
        return []
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print(f"  render fallback unavailable: {e}", flush=True)
        return [(r, u, "") for r, u in shells]
    out = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for requested, url in shells:
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=40000)
                page.wait_for_timeout(4000)  # 클라이언트 렌더 본문이 붙을 시간
                loc = page.locator("main, article").first
                html = loc.inner_html() if loc.count() else page.content()
                out.append((requested, url, html_to_md(f"<main>{html}</main>", url)))
            except Exception as e:
                print(f"  render fallback ERR {url}: {str(e)[:80]}", flush=True)
                out.append((requested, url, ""))
        browser.close()
    print(
        f"  render fallback: {sum(len(t) >= 200 for _, _, t in out)}/{len(shells)}개",
        flush=True,
    )
    return out


def crawl(urls, fetch, concurrency):
    pages, fails, empties, stale, items, shells = {}, [], [], [], [], []
    with ThreadPoolExecutor(max_workers=concurrency) as ex:
        futs = {ex.submit(fetch, u): u for u in urls}
        done = 0
        for f in as_completed(futs):
            requested = futs[f]
            url, mdtext, err = f.result()
            done += 1
            if done % 100 == 0:
                print(
                    f"  {done}/{len(urls)} (성공 {len(pages)}, 없음 {len(empties)}, 실패 {len(fails)})",
                    flush=True,
                )
            if redirected(requested, url):
                stale.append(requested)
                items.append(
                    {
                        "url": requested,
                        "class": "stale_or_redirect",
                        "reason": f"redirect -> {url}",
                    }
                )
            if mdtext and truncated_inline_png(mdtext):
                # 대형 페이지 응답이 중간에 끊기면 인라인 그림이 잘린 채 저장된다. 기존 파일을 지키고 다시 받는다.
                items.append({"url": requested, "class": "refresh_pending", "reason": "응답이 잘려 인라인 PNG가 불완전함"})
                fails.append((requested, "truncated inline png"))
                continue
            if mdtext and (foreign_target(requested, url) or (fetch is not fetch_docs_md and docs_route(url))):
                # docs 경로로 리다이렉트된 HTML은 docs phase가 raw Markdown으로 받은 파일을 쿠키 배너 본문으로 덮어쓴다.
                # 제품 앱 로그인 화면·비로그인 Academy 랜딩이 원래 URL의 본문으로 저장되지 않게 한다.
                if not any(i["url"] == requested for i in items):
                    items.append(
                        {
                            "url": requested,
                            "class": "stale_or_redirect",
                            "reason": f"수집 범위 밖으로 리다이렉트 -> {url}",
                        }
                    )
                stale.append(requested)
                continue
            if mdtext and (
                len(mdtext) >= 200 or err == ""
            ):  # 짧은 정상 페이지는 fetch가 err ""로 넘긴다
                pages[url] = mdtext
                continue
            if err == "thin=js-shell":
                shells.append(
                    (requested, url)
                )  # 스레드 밖에서 Playwright로 렌더해 보강한다
                continue
            # 저장하지 않은 URL은 삭제도 성공도 아니다. 분류해 기록하고 다음 실행에서 다시 확인한다.
            item = unresolved(requested, url, err)
            if not any(i["url"] == item["url"] for i in items):
                items.append(item)
            if err in ("status=404", "status=410", "stale=redirect", "thin=redirect"):
                stale.append(url)
            elif err in ("", "thin", "thin=js-only", "asset=pdf"):
                empties.append(url)
            else:
                fails.append((url, err))
    for requested, url, text in render_shells(shells):
        if len(text) >= 200:
            pages[url] = text
        else:
            items.append(unresolved(requested, url, "thin=js-shell"))
            empties.append(url)
    return pages, fails, empties, stale, items


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
    if not force and (
        previous == digest or (previous is None and os.path.exists(path))
    ):
        return False, previous is None
    cm.save(out, url, body, False)
    return True, False


MARKDOWN_SYNTAX = re.compile(r"^(?:```|~~~)|^[-*_=|:+\s]+$")


HOST_BOILERPLATE = {}


def load_boilerplate(state):
    """지난 전체 실행의 host별 판정을 불러온다. 크기 0으로 넣어 이번 실행의 sitemap·discover 묶음이 새 판정으로 덮는다."""
    for key, lines in state.items():
        if key.startswith("boilerplate:") and isinstance(lines, list):
            HOST_BOILERPLATE[key.split(":", 1)[1]] = (set(lines), 0)


def site_boilerplate(host, pages, reuse=False, owner=None, threshold=0.4):
    """host의 nav·footer 줄(묶음 페이지의 40% 이상에 반복되는 줄).

    sitemap·discover phase는 묶음마다 계산하고, 그 phase가 소유한 host의 가장 큰 묶음 결과를 기억한다.
    linked·target phase(reuse)는 작고 한 섹션에 쏠리기 쉬워, 새로 계산하면 전사 모음의 공통 제목 같은 본문이
    nav로 지워진다. 그래서 기억한 판정을 재사용하고, 기억이 없을 때만 묶음에서 계산한다.
    다른 host로 리다이렉트돼 섞인 소수 페이지 묶음은 그 host의 판정으로 기억하지 않는다."""
    if reuse and host in HOST_BOILERPLATE:
        return HOST_BOILERPLATE[host][0]
    # 코드 펜스·구분선·표 구분자는 어느 페이지에나 반복되는 Markdown 구문이지 nav가 아니다.
    bl = {
        line
        for line in cm.find_boilerplate(pages.values(), threshold)
        if not MARKDOWN_SYNTAX.match(line)
    }
    if (
        not reuse
        and host == owner
        and len(pages) > HOST_BOILERPLATE.get(host, (None, 0))[1]
    ):
        HOST_BOILERPLATE[host] = (bl, len(pages))
    return bl


def flush(pages, out, state, force=False, reuse=False):
    """호스트별 boilerplate 제거 후 즉시 저장(긴 실행이 끊겨도 phase 단위로 보존)."""
    rescued = rescue_article_views(pages)
    if rescued:
        print(f"  article fallback: {rescued}개", flush=True)
    by_host = {}
    for u in pages:
        by_host.setdefault(urlsplit(u).netloc, []).append(u)
    owner = max(by_host, key=lambda h: len(by_host[h])) if by_host else None
    for host, us in by_host.items():
        # Mintlify docs는 이미 깨끗하고, Trust Center는 route 간 공유 카드도 본문이다.
        if host not in NO_BOILERPLATE_STRIP and len(us) >= 5:
            bl = site_boilerplate(host, {u: pages[u] for u in us}, reuse, owner)
            if bl:
                for u in us:
                    pages[u] = cm.strip_boilerplate(pages[u], bl)
    changed = baselined = 0
    for url, body in pages.items():
        wrote, seeded = save_changed(out, url, body, state, force)
        changed += wrote
        baselined += seeded
    # 전체 실행의 판정을 남겨 --url-file 재시도도 같은 줄을 지운다. 묶음마다 다시 계산하면 결과가 흔들린다.
    for host, (bl, n) in HOST_BOILERPLATE.items():
        if n:
            state[f"boilerplate:{host}"] = sorted(bl)
    write_state(out, state)
    return len(pages), changed, baselined


def spa_rescue(urls):
    """SafeBase 등 SPA를 playwright innerText로 보강. 렌더 실패·thin route는 미해결 항목으로 돌려준다."""
    from playwright.sync_api import sync_playwright

    out, items = {}, []
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
                else:
                    items.append(
                        {
                            "url": u,
                            "class": "extract_failed",
                            "reason": "SPA 렌더 본문 200자 미만",
                        }
                    )
            except Exception as e:
                items.append(
                    {
                        "url": u,
                        "class": "refresh_pending",
                        "reason": f"render: {str(e)[:80]}",
                    }
                )
        b.close()
    return out, items


def plan(out, only=""):
    """수집 대상 phase 목록 [(label, urls, fetch)]을 만든다. fetch가 None이면 SPA 렌더 phase다.

    sitemap·BFS 발견만 네트워크를 쓰고 페이지 본문은 받지 않는다. --plan-json과 실제 수집이 같은 집합을 쓴다.
    robots.txt가 선언했지만 설정에 없는 sitemap은 구조적 누락으로 돌려준다.
    """
    known = known_urls(out)
    crawled, phases, gaps = set(), [], []

    def todo(urls, docs=False):
        # 같은 페이지의 표기 차이(끝 슬래시·fragment)는 한 번만 받는다.
        picked = []
        for u in sorted({u for u in urls if (not only) or (only in u)}):
            if mc.url_decision(u) is not None:
                continue  # manifest가 제외·별칭으로 판정한 URL은 어느 phase에서도 받지 않는다
            if docs_route(u) and not (docs and is_docs_en(u)):
                continue  # docs 경로는 docs phase의 영어 정본만 받는다
            key = mc.norm_url(u)
            if key not in crawled:
                crawled.add(key)
                picked.append(u)
        return picked

    configured = {sm for sm, _ in HTML_SITEMAPS} | set(DOCS_SITEMAPS)
    for host in sorted({urlsplit(sm).netloc for sm in configured}):
        if only and only not in host:
            continue
        for declared in declared_sitemaps(host):
            if declared not in configured:
                gaps.append(
                    {
                        "url": declared,
                        "class": "structural_missing",
                        "reason": f"{host} robots.txt가 선언했지만 수집기 설정에 없는 sitemap",
                    }
                )

    for sm, keep in HTML_SITEMAPS:
        if only and only not in urlsplit(sm).netloc:
            continue
        discovered = sitemap_urls(sm) | known.get(urlsplit(sm).netloc, set())
        phases.append(
            (
                urlsplit(sm).netloc + urlsplit(sm).path,
                todo([u for u in discovered if keep(u)]),
                fetch_html,
            )
        )
    for dsm in DOCS_SITEMAPS:
        if only and only not in urlsplit(dsm).netloc:
            continue
        discovered = sitemap_urls(dsm) | known.get(urlsplit(dsm).netloc, set())
        phases.append(
            (
                urlsplit(dsm).netloc + urlsplit(dsm).path,
                todo([u for u in discovered if is_docs_en(u)], docs=True),
                fetch_docs_md,
            )
        )
    for base, dom, depth in DISCOVER:
        if only and only not in dom:
            continue
        found = {u for u in discover(base, dom, depth) if page_candidate(u)}
        phases.append(
            (
                f"{base} (discover depth {depth})",
                todo(list(found | known.get(dom, set()))),
                fetch_html,
            )
        )
    linked_hosts = {h for h in LINKED_HOSTS if not only or only in h}
    if linked_hosts:
        linked = linked_urls(out, linked_hosts) | set().union(
            *(known.get(h, set()) for h in linked_hosts)
        )
        phases.append(
            ("linked hosts", todo(u for u in linked if page_candidate(u)), fetch_html)
        )

    # sitemap·BFS가 빠뜨린 공개 route: 보관본의 same-host 링크와 host 홈 내비게이션을 각 host의 keep 규칙으로 거른다.
    keeps = {}
    for sm, keep in HTML_SITEMAPS:
        keeps.setdefault(urlsplit(sm).netloc, []).append(keep)
    for dsm in DOCS_SITEMAPS:
        keeps.setdefault(urlsplit(dsm).netloc, []).append(is_docs_en)
    for _, dom, _ in DISCOVER:
        keeps.setdefault(dom, []).append(lambda u: True)
    keeps = {h: k for h, k in keeps.items() if not only or only in h}
    if keeps:
        candidates = linked_urls(out, set(keeps))
        for host in keeps:
            candidates |= home_links(host)
        candidates = {u.split("#")[0] for u in candidates}
        picked = [
            u
            for u in candidates
            if page_candidate(u)
            and any(k(u) for k in keeps.get(urlsplit(u).netloc, []))
        ]
        docs = [
            u
            for u in picked
            if is_docs_en(u)
            and urlsplit(u).netloc in {urlsplit(d).netloc for d in DOCS_SITEMAPS}
        ]
        phases.append(("linked same-host/docs", todo(docs, docs=True), fetch_docs_md))
        phases.append(("linked same-host", todo(set(picked) - set(docs)), fetch_html))
    if not only or only in "trust.anthropic.com":
        spa_host = urlsplit(SPA_PAGES[0]).netloc
        linked_spa = {
            u.split("#")[0].split("?")[0].rstrip("/")
            for u in linked_urls(out, {spa_host})
        }
        routes = (
            set(SPA_PAGES)
            | spa_routes(SPA_PAGES[0])
            | {u for u in linked_spa if page_candidate(u)}
        )
        phases.append(("SPA", todo(routes), None))
    return [phase for phase in phases if phase[1]], gaps


def record_unresolved(out, items, hosts, selected=None):
    """host별 status key를 교체한다. --url-file 실행은 고른 URL의 항목만 바꾸고 나머지는 보존한다."""
    by_host = {}
    for item in items:
        by_host.setdefault(urlsplit(item["url"]).netloc, []).append(item)
    previous = mc.load_status(out).get("surfaces", {})
    for host in sorted(set(hosts) | set(by_host)):
        key = f"crawl-site:{host}"
        kept = []
        if selected is not None:
            kept = [
                i
                for i in previous.get(key, {}).get("items", [])
                if i["url"] not in selected
            ]
        mc.record_status(out, key, kept + by_host.get(host, []))


def self_test():
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
        assert (
            absolute_url(url, "/_next/image?url=https%3A%2F%2Fcdn.example%2Fx.png&w=64")
            == "https://cdn.example/x.png"
        )
        assert "https://example.com/docs/x.png" in absolutize_markdown_images(
            "![](/docs/x.png)", url
        )
        assert absolutize_markdown_images("before ![]() after", url) == "before  after"
        assert (
            redact_sensitive_query("https://x.test/mcp?tracker=secret")
            == "https://x.test/mcp?tracker=REDACTED"
        )
        assert html_to_md("<main><p>x  </p></main>") == "x"
        assert (
            html_to_md("<main><img src=''><p>x</p></main>", "https://example.com/page")
            == "x"
        )
        # academy는 <main> 안 nav(레슨 목차)와 header(제목)를 보존해야 한다.
        academy_html = (
            "<body><nav>사이트메뉴</nav><main><header><h1>Claude 101</h1></header>"
            '<nav><a href="/courses/claude-101/what-is-claude">L1</a></nav></main>'
            "<footer>푸터</footer></body>"
        )
        academy_md = html_to_md(
            academy_html, "https://academy.claude.com/courses/claude-101"
        )
        assert "# Claude 101" in academy_md and "L1" in academy_md, academy_md
        assert "사이트메뉴" not in academy_md and "푸터" not in academy_md, academy_md
        # 다른 호스트는 기존대로 nav/header가 제거된다(동작 불변).
        other_md = html_to_md(academy_html, "https://www.anthropic.com/x")
        assert "L1" not in other_md and "Claude 101" not in other_md, other_md
        # 아이콘 폰트 PUA 코드포인트는 전 호스트에서 제거한다.
        assert html_to_md("<main><p>\ue02a본문</p></main>") == "본문"
        assert redirected(url, "https://example.com/other")
        assert not redirected(url, url + "/")
        assert same_host(url, url + "/other")
        assert not same_host(url, "https://other.example/page")
        assert "trust.anthropic.com" in NO_BOILERPLATE_STRIP
        assert docs_route("https://platform.claude.com/docs/ja/x") and docs_route(
            "https://code.claude.com/docs/en/x"
        )
        assert not docs_route("https://platform.claude.com/cookbook/x")
        assert unresolved("u", "u", "html=docs-md")["class"] == "refresh_pending"
        assert DOCS_MD_START.match("---\ntitle: x") and DOCS_MD_START.match("# T")
        assert not DOCS_MD_START.match(
            "### Cookie settings"
        ) and not DOCS_MD_START.match("<!DOCTYPE html>")
        main = {f"https://a.test/s{i}/p": "Nav\nx" + str(i) for i in range(6)}
        assert site_boilerplate("a.test", main, owner="a.test") == {"Nav"}
        skew = {
            f"https://a.test/t/{i}": "Nav\n### Metadata\nx" + str(i) for i in range(6)
        }
        assert site_boilerplate("a.test", skew, reuse=True) == {"Nav"}, (
            "linked phase는 기억한 판정을 재사용한다"
        )
        load_boilerplate({"boilerplate:d.test": ["Nav"]})
        assert site_boilerplate("d.test", skew, reuse=True) == {"Nav"}, "재시도는 저장된 판정을 쓴다"
        assert site_boilerplate("d.test", main, owner="d.test") == {"Nav"} and HOST_BOILERPLATE["d.test"][1] == 6
        stray = {f"https://c.test/t/{i}": "### Metadata\nx" + str(i) for i in range(6)}
        site_boilerplate("c.test", stray, owner="a.test")
        assert "c.test" not in HOST_BOILERPLATE, (
            "다른 host 묶음에 섞인 페이지로 판정을 기억하지 않는다"
        )
        fenced = {
            f"https://a.test/s{i}/p": "```\ncode\n```\n---\n| --- |\nx" + str(i)
            for i in range(6)
        }
        assert site_boilerplate("b.test", fenced) == {"code"}, (
            "Markdown 구문 줄은 boilerplate가 아니다"
        )
        assert (
            absolutize_markdown_images("![Diagram]()", "https://x.test/a")
            == "[미수집 이미지: Diagram]"
        )
        soup = BeautifulSoup(
            '<main><img alt="Chart" data-src="/c.png"><img alt="Gone"><img src=""></main>',
            "html.parser",
        )
        absolutize_html(soup, "https://x.test/p")
        assert soup.find("img")["src"] == "https://x.test/c.png", soup
        assert (
            "[미수집 이미지: Gone]" in soup.get_text()
            and len(soup.find_all("img")) == 1
        ), soup
        linked = absolutize_markdown_links(
            "[a](/docs/x) `[b](/y)`\n```\n[c](/z)\n```\n[d](//cdn/x) [e](#f)",
            "https://code.claude.com/docs/en/p",
        )
        assert (
            "[a](https://code.claude.com/docs/x)" in linked and "`[b](/y)`" in linked
        ), linked
        assert (
            "[c](/z)" in linked and "[d](//cdn/x)" in linked and "[e](#f)" in linked
        ), linked
        coded = absolutize_markdown_links(
            "Run [`/verify`](/docs/en/skills#run) and `see [x](/y)`",
            "https://code.claude.com/docs/en/p",
        )
        assert (
            coded
            == "Run [`/verify`](https://code.claude.com/docs/en/skills#run) and `see [x](/y)`"
        ), coded
        rel = absolutize_markdown_links(
            "[a](build.md) [v](clip.mp4#t) [u](URL) [s](sub/) [m](mailto:x@y.z) ![i](img.png)",
            "https://code.claude.com/docs/en/p",
        )
        assert (
            "[a](https://code.claude.com/docs/en/build.md)" in rel
            and "[v](https://code.claude.com/docs/en/clip.mp4#t)" in rel
        ), rel
        assert (
            "[u](URL)" in rel
            and "[s](https://code.claude.com/docs/en/sub/)" in rel
            and "[m](mailto:x@y.z)" in rel
            and "![i](img.png)" in rel
        ), rel
        assert unresolved("u", "u", "status=404")["class"] == "stale_or_redirect"
        assert unresolved("u", "u", "")["class"] == "extract_failed"
        assert unresolved("u", "u", "auth=login")["class"] == "auth_blocked"
        assert unresolved("u", "u", "timed out")["class"] == "refresh_pending"
        assert unresolved("u", "u", "thin=redirect")["class"] == "stale_or_redirect"
        assert unresolved("u", "u", "thin=js-only")["class"] == "intentional_exclusion"
        assert (
            thin_reason(
                "<body><p>You will be redirected in a few seconds</p></body>",
                "You will be redirected",
            )
            == "thin=redirect"
        )
        assert (
            thin_reason(
                "<body><div id=root></div><script>" + "x" * 500 + "</script></body>", ""
            )
            == "thin=js-only"
        )
        assert (
            thin_reason(
                "<body><header>" + "nav " * 100 + "</header><main></main></body>", ""
            )
            == "thin=js-shell"
        )
        assert (
            thin_reason(
                "<body><main><h1>Cookies</h1><p>" + "word " * 30 + "</p></main></body>",
                "# Cookies\n\n" + "w" * 120,
            )
            == ""
        )
        assert (
            thin_reason(
                "<body><main><p>" + "word " * 100 + "</p></main></body>", "short"
            )
            == "thin"
        )
        assert (
            unresolved("u", "https://cdn/x.pdf", "asset=pdf")["class"]
            == "stale_or_redirect"
        )
        moved = '<html><head><meta http-equiv="refresh" content="0;URL=\'/new/\'" /></head><body><p>This page has moved.</p></body></html>'
        assert thin_reason(moved, "This page has moved.") == "thin=redirect"
        assert not page_candidate("https://claude.com/form/apply")
        png = base64.b64encode(b"\x89PNG\r\n\x1a\nxxxx" + b"\x00\x00\x00\x00IEND\xaeB`\x82").decode()
        assert not truncated_inline_png(f"![](data:image/png;base64,{png})")
        assert truncated_inline_png(f"![](data:image/png;base64,{png[:-12]})"), "잘린 인라인 PNG는 저장하지 않는다"
        assert foreign_target("https://claude.com/x", "https://claude.ai/login")
        assert foreign_target(
            "https://www.anthropic.com/learn/x", "https://anthropic.skilljar.com/x"
        )
        assert not foreign_target(
            "https://www.anthropic.com/claude", "https://claude.com/product/overview"
        )
        assert not foreign_target("https://claude.com/a", "https://claude.com/b")
        assert page_candidate("https://www.anthropic.com/news/x")
        assert not page_candidate(
            "https://transformer-circuits.pub/2021/framework/name@example.test"
        )
        assert not page_candidate(
            "https://transformer-circuits.pub/2021/framework/index.html}"
        )
        assert not page_candidate("https://claude.dev/blog/x.md")
        assert not page_candidate("https://platform.claude.com/settings/keys")
        assert page_candidate("https://platform.claude.com/docs/en/x")
        record_unresolved(
            out,
            [{"url": "https://a.test/x", "class": "extract_failed", "reason": "thin"}],
            {"a.test"},
        )
        record_unresolved(out, [], {"a.test"}, selected={"https://a.test/y"})
        assert [i["url"] for i in mc.status_items(out, "crawl-site:a.test")] == [
            "https://a.test/x"
        ]
        record_unresolved(out, [], {"a.test"})
        assert not mc.status_items(out, "crawl-site:a.test")
        roots = mc.archive_roots()
        for host in (
            {urlsplit(sm).netloc for sm, _ in HTML_SITEMAPS}
            | {urlsplit(sm).netloc for sm in DOCS_SITEMAPS}
            | {d for _, d, _ in DISCOVER}
            | LINKED_HOSTS
        ):
            assert host in roots, f"수집 host가 manifest archive_roots에 없음: {host}"
    mc.self_test()
    print("self-test ok")


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
    ap.add_argument(
        "--prune-stale",
        action="store_true",
        help="live 404/canonical redirect source 파일 제거",
    )
    ap.add_argument(
        "--url-file", help="sitemap 발견 대신 줄 단위 URL 목록만 표적 재수집"
    )
    ap.add_argument(
        "--plan-json",
        help="본문을 받지 않고 수집 대상 URL 집합(C)을 이 JSON 파일로 쓴다",
    )
    ap.add_argument("--self-test", action="store_true", help=argparse.SUPPRESS)
    ap.add_argument("--limit", type=int, default=0, help="크롤 URL 상한(테스트용)")
    ap.add_argument("--concurrency", type=int, default=8)
    a = ap.parse_args()

    if a.self_test:
        self_test()
        return

    selected = None
    if a.url_file:
        with open(a.url_file, encoding="utf-8") as f:
            selected = sorted(
                {
                    line.strip()
                    for line in f
                    if line.strip() and not line.startswith("#")
                }
            )
        docs = [
            u
            for u in selected
            if urlsplit(u).netloc in ("platform.claude.com", "code.claude.com")
            and "/docs/" in urlsplit(u).path
        ]
        phases = [
            ("target/html", sorted(set(selected) - set(docs)), fetch_html),
            ("target/docs", docs, fetch_docs_md),
        ]
        phases, gaps = [p for p in phases if p[1]], []
    else:
        phases, gaps = plan(a.out, a.only)

    if a.plan_json:
        data = {"generated_by": "crawl-site.py --plan-json", "phases": {}, "gaps": gaps}
        for label, urls, fetch in phases:
            data["phases"][label] = {
                "fetch": fetch.__name__ if fetch else "spa_rescue",
                "urls": urls,
            }
        with open(a.plan_json, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(
            f"plan: {sum(len(p[1]) for p in phases)} URL / {len(phases)} phase -> {a.plan_json}",
            flush=True,
        )
        return

    state = load_state(a.out)
    load_boilerplate(state)
    scanned, changed, baselined, fails, empties, stale, items = (
        0,
        0,
        0,
        [],
        [],
        [],
        list(gaps),
    )
    budget = a.limit or 10**9
    hosts_run = set()
    for label, urls, fetch in phases:
        if scanned >= budget:
            break
        urls = urls[: max(0, budget - scanned)]
        hosts_run.update(urlsplit(u).netloc for u in urls)
        print(f"[{label}] {len(urls)} 크롤", flush=True)
        if fetch is None:
            pages, spa_items = spa_rescue(urls)
            items += spa_items
            n, c, b = flush(pages, a.out, state, a.force, reuse=True)
        else:
            p, f, e, s, i = crawl(urls, fetch, a.concurrency)
            items += i
            fails += f
            empties += e
            stale += s
            n, c, b = flush(
                p, a.out, state, a.force, reuse=label.startswith(("linked", "target"))
            )
        scanned += n
        changed += c
        baselined += b

    record_unresolved(
        a.out, items, hosts_run, set(selected) if selected is not None else None
    )
    removed = prune_stale(a.out, stale) if a.prune_stale else 0
    print(
        f"검사: {scanned} / 내용 변경 저장: {changed} / 기준선 등록: {baselined} / 본문없음 skip: {len(empties)} / stale: {len(stale)} / 제거: {removed} / 실패: {len(fails)}",
        flush=True,
    )
    if items:
        by = Counter(i["class"] for i in items)
        print(
            f"미해결 기록({mc.STATUS_FILE}): "
            + ", ".join(f"{k} {v}" for k, v in by.most_common()),
            flush=True,
        )
    if fails:
        print("실패(재실행 시 자동 재시도):", flush=True)
        for u, err in fails[:20]:
            print(f"  {u} [{err}]", flush=True)


if __name__ == "__main__":
    main()
