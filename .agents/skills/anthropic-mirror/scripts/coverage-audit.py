"""공개 표면 전수 커버리지 감사: live 발견(D), 수집기 대상(C), 로컬 생성물(M)을 독립적으로 만들고 대조한다.

  D: robots.txt 선언 sitemap과 /sitemap.xml(중첩 index 재귀), 각 host 홈·내비게이션 링크(SPA는 렌더),
     보관본이 가리키는 공식 host outbound 링크, YouTube 채널 탭, Academy 인증 카탈로그.
     새 공식 host는 manifest(assets/mirror-manifest.json) 판정이 없으면 자동으로 structural_missing 후보가 된다.
  C: crawl-site.py --plan-json, academy-video.py --list-json, 채널 탭 ID, pdf-mirror 대상 PDF.
  M: 생성물의 source 주석, Academy source URL, YouTube frontmatter youtube_id, PDF 파일 경로.

D-C, C-M, M-D의 모든 URL을 mirror-common.CLASSES 중 하나로 분류한다. 규칙으로 못 정하면 live 응답으로 정하고,
그래도 못 정하면 unclassified로 남긴다. 결과: <repo>/.anthropic-mirror-audit/coverage.{json,md}.
종료 코드: 0 = 미분류·차단 분류 없음, 1 = 미분류 있음, 3 = 차단 분류(structural_missing 등) 있음.
생성물·git index는 바꾸지 않는다(감사 결과와 live 캐시만 .anthropic-mirror-audit/에 쓴다).

실행: <crawl4ai python> coverage-audit.py <repo> [--assets] [--concurrency N] [--cache-hours H]
"""

import argparse
import collections
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlsplit

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mc = load("mirror_common", os.path.join(HERE, "mirror-common.py"))
cs = load("crawl_site", os.path.join(HERE, "crawl-site.py"))
MANIFEST = mc.load_manifest()
ROOTS = {r for r in MANIFEST["archive_roots"] if not r.endswith(".md")}
ASSET_SUFFIXES = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    ".ico",
    ".css",
    ".js",
    ".woff",
    ".woff2",
    ".ttf",
    ".mp4",
    ".webm",
    ".mov",
    ".mp3",
    ".zip",
    ".json",
    ".xml",
    ".txt",
    ".csv",
    ".ipynb",
    ".jsonl",
    ".docx",
    ".pptx",
    ".xlsx",
    ".avif",
)
URL_IN_TEXT = re.compile(r"https?://[A-Za-z0-9.-]+[^\s<>)\]\"'`]*")
SOURCE_LINE = re.compile(r"^<!--\s*(?:source:\s*)?(https?://\S+?)\s*-->")


# ---------------------------------------------------------------- M
def mirrored(repo):
    """M: {norm_url: [path]} 와 youtube id, academy stub 목록."""
    pages, youtube, gated = collections.defaultdict(list), {}, []
    for root, dirs, files in os.walk(repo):
        rel_root = os.path.relpath(root, repo)
        top = rel_root.split(os.sep)[0]
        if rel_root != "." and top not in ROOTS:
            dirs[:] = []
            continue
        dirs[:] = [d for d in dirs if rel_root != "." or d in ROOTS]
        for name in files:
            rel = os.path.normpath(os.path.join(rel_root, name))
            if rel_root == "." and name.removesuffix(".md") not in ROOTS:
                continue
            fp = os.path.join(repo, rel)
            if name.endswith(".pdf"):
                pages[mc.norm_url("https://" + rel)].append(rel)
                continue
            if not name.endswith(".md") or ".parts" + os.sep in rel:
                continue
            with open(fp, encoding="utf-8", errors="replace") as f:
                head = f.read(4096)
            if rel.startswith("youtube.com" + os.sep):
                m = re.search(r"^youtube_id:\s*([A-Za-z0-9_-]{11})\s*$", head, re.M)
                if m:
                    youtube[m.group(1)] = rel
                continue
            m = SOURCE_LINE.match(head)
            if m:
                pages[mc.norm_url(m.group(1))].append(rel)
                if "_(등록 또는 권한이 필요한 레슨)_" in head:
                    gated.append((m.group(1), rel))
    return pages, youtube, gated


def archive_links(repo):
    """보관본 전체의 공식 host URL(outbound 링크 발견 수단)."""
    found = collections.Counter()
    for root, dirs, files in os.walk(repo):
        top = os.path.relpath(root, repo).split(os.sep)[0]
        if top != "." and top not in ROOTS:
            dirs[:] = []
            continue
        for name in files:
            if not name.endswith(".md"):
                continue
            with open(
                os.path.join(root, name), encoding="utf-8", errors="replace"
            ) as f:
                text = f.read()
            for url in URL_IN_TEXT.findall(text):
                url = url.rstrip(".,;:'\"")
                if mc.is_official_host(urlsplit(url).netloc, MANIFEST):
                    found[url] += 1
    return found


# ---------------------------------------------------------------- live
class Live:
    """curl_cffi GET 결과 캐시. 같은 감사 안에서 URL당 한 번만 요청한다."""

    def __init__(self, repo, hours, concurrency):
        self.path = os.path.join(repo, mc.AUDIT_DIR, "live-cache.json")
        self.ttl = hours * 3600
        self.concurrency = concurrency
        try:
            with open(self.path, encoding="utf-8") as f:
                self.cache = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.cache = {}

    def _get(self, url):
        hit = self.cache.get(url)
        if hit and time.time() - hit["at"] < self.ttl:
            return url, hit
        result = {
            "at": time.time(),
            "status": 0,
            "final": "",
            "len": 0,
            "ctype": "",
            "error": "",
        }
        for attempt in range(2):
            try:
                status, text, final = cs.get(url)
                result.update(status=status, final=final, len=len(text))
                result["error"] = ""
                break
            except Exception as e:  # 네트워크 오류는 재시도 1회 뒤 refresh_pending
                result["error"] = str(e)[:120]
                time.sleep(1 + attempt)
        return url, result

    def check(self, urls):
        todo = sorted(set(urls))
        with ThreadPoolExecutor(self.concurrency) as ex:
            for n, (url, result) in enumerate(ex.map(self._get, todo), 1):
                self.cache[url] = result
                if n % 200 == 0:
                    print(f"  live {n}/{len(todo)}", flush=True)
        self.save()
        return {u: self.cache[u] for u in todo}

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.cache, f)


# ---------------------------------------------------------------- D
def page_like(url):
    parts = urlsplit(url)
    path = parts.path.lower()
    if parts.scheme not in ("http", "https") or not parts.netloc:
        return False
    if any(seg in path for seg in ("/_next/", "/cdn-cgi/", "/wp-content/", "/static/")):
        return False
    path = path.rstrip("/")
    return not path.endswith(ASSET_SUFFIXES) and not path.endswith(".pdf")


def home_links(host, render=False):
    """host 홈의 same-host 공개 route와 공식 outbound host. SPA면 Playwright로 렌더한다."""
    base = f"https://{host}/"
    try:
        status, html, final = cs.get(base)
    except Exception as e:
        return {"status": 0, "final": "", "error": str(e)[:80], "links": set()}
    hrefs = re.findall(r'href="([^"#]+)', html)
    if render or len([h for h in hrefs if h.startswith("/") or host in h]) < 5:
        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto(base, wait_until="domcontentloaded", timeout=30000)
                page.wait_for_timeout(5000)
                hrefs += page.eval_on_selector_all(
                    "a[href]", "els => els.map(e => e.href)"
                )
                browser.close()
        except Exception as e:
            print(f"  render ERR {host}: {str(e)[:80]}", flush=True)
    links = {urljoin(final or base, h).split("#")[0] for h in hrefs}
    return {"status": status, "final": final, "error": "", "links": links}


def discover_live(hosts):
    """D(web): host별 robots·sitemap(중첩 재귀)·홈 링크. 새 공식 host도 돌려준다."""
    D, meta, new_hosts = collections.defaultdict(set), {}, set()
    pending, seen = sorted(hosts), set()
    while pending:
        host = pending.pop()
        if host in seen:
            continue
        seen.add(host)
        if mc.host_decision(host, MANIFEST):
            continue
        sitemaps = set(cs.declared_sitemaps(host)) | {f"https://{host}/sitemap.xml"}
        for sm in sorted(sitemaps):
            for url in cs.sitemap_urls(sm):
                D[url].add(f"sitemap:{sm}")
        home = home_links(
            host, render=host in {urlsplit(u).netloc for u in cs.SPA_PAGES}
        )
        meta[host] = {
            "sitemaps": sorted(sitemaps),
            "home_status": home["status"],
            "home_final": home["final"],
            "home_error": home["error"],
        }
        for url in home["links"]:
            other = urlsplit(url).netloc.lower()
            if other == host:
                D[url].add("home")
            elif mc.is_official_host(other, MANIFEST) and other not in seen:
                new_hosts.add(other)
                pending.append(other)
        print(f"  D {host}: sitemaps {len(sitemaps)}, 누적 {len(D)}", flush=True)
    return D, meta, new_hosts


# ---------------------------------------------------------------- 규칙 분류
def rule_class(url):
    """live 확인 없이 정할 수 있는 분류. 없으면 None. manifest 판정이 정본이다."""
    parts = urlsplit(url)
    host, path = parts.netloc.lower(), parts.path
    decision = mc.url_decision(url, MANIFEST)
    if decision:
        return decision
    if not mc.is_official_host(host, MANIFEST):
        return "intentional_exclusion", "공식 host 아님"
    if re.search(r"[@{}\s]|%20", path):
        return "intentional_exclusion", "본문 속 잘못된 링크(이메일·중괄호·공백이 경로에 섞임)"
    if path.endswith(".md") and host not in ("platform.claude.com", "code.claude.com"):
        return "intentional_exclusion", "같은 페이지의 Markdown 대체 표현"
    if host == "claude.com" and not cs.is_claude_en(url):
        return "intentional_exclusion", "다국어 사본(영어 정본만 수집)"
    if host in ("support.claude.com", "privacy.claude.com") and "/en/" not in path and path not in ("", "/"):
        return "intentional_exclusion", "다국어 사본(영어 정본만 수집)"
    if host in ("platform.claude.com", "code.claude.com") and "/docs/" in path and "/docs/en/" not in path:
        return "intentional_exclusion", "다국어 사본(영어 정본만 수집)"
    if host == "academy.claude.com" and cs.academy_blocked(url):
        return "intentional_exclusion", "robots.txt Disallow 경로"
    return None


def live_class(url, res, which, collected_hosts):
    """live 응답으로 분류한다. None이면 crawler_probe로 넘기거나 미분류로 남긴다."""
    cls = mc.classify_http(res["status"], res["final"], url, res["error"])
    host = urlsplit(url).netloc.lower()
    if cls:
        cls_name, reason = cls
        if cls_name == "stale_or_redirect" and res["final"]:
            final_host = urlsplit(res["final"]).netloc.lower()
            reason += "" if final_host in collected_hosts else " (대상 host 미수집)"
        return cls_name, reason
    if res["status"] != 200:
        return None
    if which == "D-C" and host not in collected_hosts:
        return "structural_missing", "manifest에 없는 새 공식 host의 live 200 페이지"
    if which == "M-D":
        return "scope_decision", "live 200이지만 sitemap·홈·보관 링크 어디에도 없음(known_urls로 계속 갱신)"
    return None  # D-C·C-M은 crawler_probe가 수집기 fetch로 판정한다


def crawler_probe(url, which):
    """수집기와 같은 fetch로 저장 가능 여부를 본다. 저장 가능하면 D-C는 구조적 누락, C-M은 갱신 대기다."""
    docs = urlsplit(url).netloc in ("platform.claude.com", "code.claude.com") and "/docs/" in urlsplit(url).path
    final, text, err = (cs.fetch_docs_md if docs else cs.fetch_html)(url)
    if err or not text:
        item = cs.unresolved(url, final, err)
        return item["class"], item["reason"]
    if cs.redirected(url, final):
        return "stale_or_redirect", f"redirect -> {final}"
    if which == "D-C":
        return "structural_missing", f"수집 가능한 본문 {len(text)}자인데 수집기 발견 경로(sitemap·BFS·링크)에 없음"
    return "refresh_pending", f"수집 가능한 본문 {len(text)}자, 다음 refresh에서 저장"


# ---------------------------------------------------------------- YouTube / Academy / PDF
def youtube_live():
    yc = load("youtube_channels", os.path.join(cs.CRAWL_SCRIPTS_DIR, "youtube-channels.py"))
    ids = {}
    for handle, channel_id in MANIFEST["youtube_channels"].items():
        listed = yc.enumerate_channel(channel_id, tuple(MANIFEST["youtube_tabs"]))
        if listed is None:
            raise RuntimeError(f"{handle} 채널 탭 전부 조회 실패")
        for vid, _title in listed:
            ids[vid] = handle
    return ids


def youtube_oembed(vid):
    try:
        status, _, _ = cs.get(
            f"https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v={vid}"
        )
    except Exception as e:
        return "refresh_pending", f"oembed 오류 {str(e)[:60]}"
    if status == 200:
        return None
    if status in (401, 403):
        return "auth_blocked", f"oembed {status}: 비공개·멤버 전용"
    if status in (400, 404):
        return "stale_or_redirect", f"oembed {status}: 삭제된 영상"
    return "refresh_pending", f"oembed {status}"


def academy_catalog(repo, base):
    """academy-video.py --list-json으로 live lesson URL 목록. 세션이 없으면 None."""
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        out = tmp.name
    env = {**os.environ, "SKILLJAR_BASE": base}
    env.pop("SKILLJAR_SKIP_HOST", None)
    result = subprocess.run(
        [
            sys.executable,
            os.path.join(HERE, "academy-video.py"),
            repo,
            "--list-json",
            out,
        ],
        env=env,
        capture_output=True,
        text=True,
    )
    try:
        if result.returncode != 0:
            return None, (result.stdout + result.stderr).strip().splitlines()[-1:] or [
                "exit %d" % result.returncode
            ]
        with open(out, encoding="utf-8") as f:
            return json.load(f)["courses"], []
    finally:
        os.unlink(out)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("repo")
    ap.add_argument(
        "--assets",
        action="store_true",
        help="보관본의 원격 이미지·YouTube 참조 전체를 live로 렌더 가능 여부 확인",
    )
    ap.add_argument("--concurrency", type=int, default=16)
    ap.add_argument(
        "--cache-hours",
        type=float,
        default=12,
        help="live 응답 캐시 유효 시간(재실행 비용 절감)",
    )
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    live = Live(repo, a.cache_hours, a.concurrency)
    items = []

    def add(url, surface, which, cls, reason, evidence=""):
        items.append(
            {
                "url": url,
                "surface": surface,
                "set": which,
                "class": cls,
                "reason": reason,
                "evidence": evidence,
            }
        )

    print("[M] 로컬 생성물", flush=True)
    M_pages, M_youtube, gated = mirrored(repo)

    print("[C] crawl-site.py --plan-json", flush=True)
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
        plan_path = tmp.name
    subprocess.run(
        [
            sys.executable,
            os.path.join(HERE, "crawl-site.py"),
            repo,
            "--plan-json",
            plan_path,
        ],
        check=True,
    )
    with open(plan_path, encoding="utf-8") as f:
        plan = json.load(f)
    os.unlink(plan_path)
    C_web = {
        mc.norm_url(u): u for phase in plan["phases"].values() for u in phase["urls"]
    }
    for gap in plan["gaps"]:
        add(
            gap["url"],
            urlsplit(gap["url"]).netloc,
            "D-C",
            gap["class"],
            gap["reason"],
            "robots.txt",
        )
    collected_hosts = {urlsplit(u).netloc for u in C_web.values()}

    print("[D] robots·sitemap·홈·보관 링크", flush=True)
    links = archive_links(repo)
    link_hosts = {urlsplit(u).netloc.lower() for u in links}
    seed = {
        r
        for r in ROOTS
        if "." in r and r not in ("youtube.com",) and not r.endswith(".skilljar.com")
    }
    D_raw, host_meta, new_hosts = discover_live(
        seed | {h for h in link_hosts if not h.endswith(".skilljar.com")}
    )
    for url in links:
        if page_like(url):
            D_raw[url].add("archive-link")
    D_web = {}
    for url, sources in D_raw.items():
        if page_like(url) and not urlsplit(url).netloc.endswith(".skilljar.com"):
            D_web.setdefault(mc.norm_url(url), (url, sources))
    M_web = {
        k: v
        for k, v in M_pages.items()
        if not k.endswith(".pdf") and not urlsplit(k).netloc.endswith(".skilljar.com")
    }

    # 새 공식 host: manifest 판정이 없고 보관 루트도 아니면 host 단위 후보를 먼저 남긴다.
    all_hosts = link_hosts | new_hosts | {urlsplit(u).netloc for u in D_web}
    for host in sorted(
        h
        for h in all_hosts
        if mc.is_official_host(h, MANIFEST)
        and h not in ROOTS
        and not mc.url_decision(f"https://{h}/", MANIFEST)
    ):
        res = live.check([f"https://{host}/"])[f"https://{host}/"]
        final_host = urlsplit(res["final"]).netloc.lower()
        if res["error"] or res["status"] >= 400:
            cls = mc.classify_http(
                res["status"], res["final"], f"https://{host}/", res["error"]
            ) or ("refresh_pending", "확인 실패")
            add(
                f"https://{host}/",
                host,
                "D-C",
                cls[0],
                f"새 공식 host 루트: {cls[1]}",
                "host",
            )
        elif final_host and final_host != host and final_host in ROOTS:
            add(
                f"https://{host}/",
                host,
                "D-C",
                "stale_or_redirect",
                f"새 host 루트가 {final_host}로 리다이렉트(별칭)",
                "host",
            )
        else:
            add(
                f"https://{host}/",
                host,
                "D-C",
                "structural_missing",
                "manifest·allowlist에 없는 새 공식 host",
                "host",
            )

    # 웹 페이지 차집합
    sets = {
        "D-C": sorted(set(D_web) - set(C_web)),
        "C-M": sorted(set(C_web) - set(M_web)),
        "M-D": sorted(set(M_web) - set(D_web)),
    }
    print({k: len(v) for k, v in sets.items()}, flush=True)
    need_live = collections.defaultdict(list)
    for which, keys in sets.items():
        for key in keys:
            url = {
                "D-C": lambda k: D_web[k][0],
                "C-M": lambda k: C_web[k],
                "M-D": lambda k: k,
            }[which](key)
            ruled = rule_class(url)
            if ruled:
                add(url, urlsplit(url).netloc, which, ruled[0], ruled[1])
            else:
                need_live[which].append(url)
    print(f"[live] {sum(len(v) for v in need_live.values())} URL 확인", flush=True)
    responses = live.check([u for urls in need_live.values() for u in urls])
    probe = []
    for which, urls in need_live.items():
        for url in urls:
            res = responses[url]
            cls = live_class(url, res, which, collected_hosts)
            evidence = (
                f"HTTP {res['status']} -> {res['final']}"
                if not res["error"]
                else res["error"]
            )
            if (
                which == "D-C"
                and cls
                and cls[0] == "stale_or_redirect"
                and mc.norm_url(res["final"]) in C_web
            ):
                cls = (
                    "stale_or_redirect",
                    f"수집 대상 정본으로 리다이렉트: {res['final']}",
                )
            if which in ("D-C", "C-M") and not cls and res["status"] == 200:
                probe.append((url, which))
                continue
            if cls:
                add(url, urlsplit(url).netloc, which, cls[0], cls[1], evidence)
            else:
                add(
                    url,
                    urlsplit(url).netloc,
                    which,
                    "unclassified",
                    "live 응답으로 분류 불가",
                    evidence,
                )
    with ThreadPoolExecutor(8) as ex:
        for (url, which), cls in zip(probe, ex.map(lambda p: crawler_probe(*p), probe)):
            add(url, urlsplit(url).netloc, which, cls[0], cls[1], "crawl-site fetch")

    # 수집 단계가 기록한 미해결 항목도 감사 결과에 합친다(분류는 수집기 판정을 따른다).
    for st in mc.status_items(repo):
        if not any(i["url"] == st["url"] for i in items):
            add(
                st["url"],
                st["surface"],
                "status",
                st["class"],
                st["reason"],
                mc.STATUS_FILE,
            )

    # YouTube
    print("[YouTube] 채널 탭", flush=True)
    surfaces = {}
    try:
        yt_live = youtube_live()
    except Exception as e:
        yt_live = None
        add(
            "https://www.youtube.com/",
            "youtube",
            "D-C",
            "refresh_pending",
            f"채널 목록 조회 실패 {str(e)[:80]}",
        )
    if yt_live is not None:
        missing = sorted(set(yt_live) - set(M_youtube))
        extra = sorted(set(M_youtube) - set(yt_live))
        for vid in missing:
            cls = youtube_oembed(vid) or (
                "refresh_pending",
                "채널 탭에 있으나 로컬 페이지 없음",
            )
            add(
                f"https://www.youtube.com/watch?v={vid}",
                "youtube",
                "C-M",
                cls[0],
                cls[1],
                yt_live[vid],
            )
        for vid in extra:
            cls = youtube_oembed(vid) or (
                "scope_decision",
                "공개 영상이지만 채널 탭 목록에서 빠짐",
            )
            add(
                f"https://www.youtube.com/watch?v={vid}",
                "youtube",
                "M-D",
                cls[0],
                cls[1],
                M_youtube[vid],
            )
        surfaces["youtube"] = {
            "D": len(yt_live),
            "C": len(yt_live),
            "M": len(M_youtube),
            "D-C": 0,
            "C-M": len(missing),
            "M-D": len(extra),
        }

    # Academy (Skilljar)
    for host in sorted(h for h in ROOTS if h.endswith(".skilljar.com")):
        print(f"[Academy] {host}", flush=True)
        local = {k: v for k, v in M_pages.items() if urlsplit(k).netloc == host}
        catalog, why = academy_catalog(repo, f"https://{host}")
        if catalog is None:
            add(
                f"https://{host}/accounts/",
                host,
                "D-C",
                "auth_blocked",
                f"세션 없음·만료로 live 카탈로그 조회 불가: {' '.join(why)}",
            )
            for key in sorted(local):
                add(
                    key,
                    host,
                    "M-D",
                    "auth_blocked",
                    "live lesson ID 대조 불가(세션 만료)",
                    local[key][0],
                )
            surfaces[host] = {
                "D": None,
                "C": None,
                "M": len(local),
                "D-C": None,
                "C-M": None,
                "M-D": len(local),
            }
            continue
        live_lessons = {
            mc.norm_url(u) for urls in catalog.values() if urls for u in urls
        }
        public = {k for k in M_pages if urlsplit(k).netloc == "anthropic.skilljar.com"}
        for course, urls in catalog.items():
            if urls is None:
                add(
                    f"https://{host}/{course}",
                    host,
                    "D-C",
                    "refresh_pending",
                    "코스 페이지 조회 실패",
                )
            elif not urls:
                add(
                    f"https://{host}/{course}",
                    host,
                    "D-C",
                    "auth_blocked",
                    "미등록·잠금으로 lesson ID 0개",
                )
        for key in sorted(live_lessons - set(local)):
            course = urlsplit(key).path.strip("/").split("/")[0]
            if host != "anthropic.skilljar.com" and any(
                urlsplit(p).path.strip("/").split("/")[0] == course for p in public
            ):
                add(
                    key,
                    host,
                    "C-M",
                    "intentional_exclusion",
                    "공개 Academy와 같은 코스(partner 중복)",
                )
            else:
                add(
                    key,
                    host,
                    "C-M",
                    "refresh_pending",
                    "live 카탈로그에 있으나 로컬 레슨 없음",
                )
        for key in sorted(set(local) - live_lessons):
            add(
                key,
                host,
                "M-D",
                "stale_or_redirect",
                "live 카탈로그에서 사라진 lesson ID",
                local[key][0],
            )
        surfaces[host] = {
            "D": len(live_lessons),
            "C": len(live_lessons),
            "M": len(local),
            "D-C": 0,
            "C-M": len(live_lessons - set(local)),
            "M-D": len(set(local) - live_lessons),
        }
    for url, rel in gated:
        add(
            url,
            urlsplit(url).netloc,
            "M(state)",
            "auth_blocked",
            "등록·권한 필요 레슨 stub(본문 미수집)",
            rel,
        )

    # PDF
    print("[PDF]", flush=True)
    pdf_mod = load("pdf_mirror", os.path.join(cs.CRAWL_SCRIPTS_DIR, "pdf-mirror.py"))
    C_pdf = {
        mc.norm_url(u): u
        for u in pdf_mod.scan(repo, MANIFEST["pdf_hosts"])
        if not pdf_mod.invalid_source_url(u)
    }
    D_pdf = dict(C_pdf)
    for url in D_raw:
        if urlsplit(url).path.lower().endswith(".pdf") and mc.is_official_host(
            urlsplit(url).netloc, MANIFEST
        ):
            D_pdf.setdefault(mc.norm_url(url), url)
    # 페이지 URL이 PDF로 리다이렉트한 경우(system card 등) 그 PDF도 발견 집합이다.
    for st in mc.status_items(repo, "crawl-site:"):
        if st["reason"].startswith("PDF로 리다이렉트 -> "):
            target = st["reason"].split(" -> ", 1)[1]
            if mc.is_official_host(urlsplit(target).netloc, MANIFEST):
                D_pdf.setdefault(mc.norm_url(target), target)
    M_pdf = {k for k in M_pages if k.endswith(".pdf")}
    pdf_sets = {
        "D-C": sorted(set(D_pdf) - set(C_pdf)),
        "C-M": sorted(set(C_pdf) - M_pdf),
        "M-D": sorted(M_pdf - set(D_pdf)),
    }
    pdf_res = live.check([D_pdf.get(k, k) for keys in pdf_sets.values() for k in keys])
    for which, keys in pdf_sets.items():
        for key in keys:
            url = D_pdf.get(key, key)
            res = pdf_res[url]
            cls = mc.classify_http(res["status"], res["final"], url, res["error"])
            if not cls and res["status"] == 200:
                if which == "C-M" and res["len"] > 100 * 1024 * 1024:
                    cls = ("intentional_exclusion", "100MB 초과 PDF(GitHub 한도)")
                elif which == "M-D":
                    cls = (
                        "scope_decision",
                        "live PDF이지만 보관 페이지에서 더 이상 링크되지 않음",
                    )
                else:
                    cls = ("refresh_pending", "다음 pdf-mirror 실행에서 저장")
            add(
                url,
                "pdf",
                which,
                *(cls or ("unclassified", "분류 불가")),
                f"HTTP {res['status']}",
            )
    surfaces["pdf"] = {
        "D": len(D_pdf),
        "C": len(C_pdf),
        "M": len(M_pdf),
        **{k: len(v) for k, v in pdf_sets.items()},
    }

    # 원격 이미지·영상 참조 렌더 가능 여부
    if a.assets:
        print("[assets] 원격 이미지 live 확인", flush=True)
        images = set()
        for root, dirs, files in os.walk(repo):
            top = os.path.relpath(root, repo).split(os.sep)[0]
            if top != "." and top not in ROOTS:
                dirs[:] = []
                continue
            for name in files:
                if name.endswith(".md"):
                    with open(
                        os.path.join(root, name), encoding="utf-8", errors="replace"
                    ) as f:
                        images.update(
                            re.findall(
                                r"!\[[^\]]*\]\(\s*<?(https?://[^)\s>]+)", f.read()
                            )
                        )
        for url, res in live.check(images).items():
            cls = mc.classify_http(res["status"], "", "", res["error"])
            if cls:
                add(url, "remote-image", "asset", cls[0], f"이미지 {cls[1]}", "")

    # 표면별 집계
    by_surface = collections.defaultdict(lambda: collections.Counter())
    for item in items:
        by_surface[item["surface"]][item["set"]] += 1
    for host in sorted(
        {urlsplit(k).netloc for k in set(D_web) | set(C_web) | set(M_web)}
    ):
        d = {k for k in D_web if urlsplit(k).netloc == host}
        c = {k for k in C_web if urlsplit(k).netloc == host}
        m = {k for k in M_web if urlsplit(k).netloc == host}
        surfaces[host] = {
            "D": len(d),
            "C": len(c),
            "M": len(m),
            "D-C": len(d - c),
            "C-M": len(c - m),
            "M-D": len(m - d),
        }

    unclassified = [i for i in items if i["class"] not in mc.CLASSES]
    blocking = [i for i in items if i["class"] in mc.BLOCKING_CLASSES]
    out_dir = os.path.join(repo, mc.AUDIT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    payload = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "surfaces": surfaces,
        "host_meta": host_meta,
        "class_counts": collections.Counter(i["class"] for i in items),
        "unclassified": len(unclassified),
        "blocking": len(blocking),
        "items": sorted(items, key=lambda i: (i["surface"], i["set"], i["url"])),
    }
    with open(os.path.join(out_dir, "coverage.json"), "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    with open(os.path.join(out_dir, "coverage.md"), "w", encoding="utf-8") as f:
        f.write(render(payload))
    live.save()
    print(render_summary(payload), flush=True)
    print(f"결과: {out_dir}/coverage.json / coverage.md", flush=True)
    return 1 if unclassified else 3 if blocking else 0


def render_summary(payload):
    counts = payload["class_counts"]
    return (
        f"미분류 {payload['unclassified']} / 차단 분류 {payload['blocking']} / "
        + ", ".join(f"{k} {counts.get(k, 0)}" for k in mc.CLASSES)
    )


def render(payload):
    lines = [
        f"# Coverage audit {payload['generated_at']}",
        "",
        render_summary(payload),
        "",
        "| 표면 | D | C | M | D-C | C-M | M-D | 분류 |",
        "|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    by_surface = collections.defaultdict(collections.Counter)
    for item in payload["items"]:
        by_surface[item["surface"]][item["class"]] += 1
    for name in sorted(set(payload["surfaces"]) | set(by_surface)):
        s = payload["surfaces"].get(name, {})
        cls = ", ".join(f"{k} {v}" for k, v in by_surface[name].most_common())
        cell = lambda k: "-" if s.get(k) is None else str(s[k])
        lines.append(
            f"| {name} | {cell('D')} | {cell('C')} | {cell('M')} | {cell('D-C')} | {cell('C-M')} | {cell('M-D')} | {cls} |"
        )
    lines += [
        "",
        "## 차단 분류와 미분류 항목",
        "",
        "| 분류 | 집합 | URL | 이유 |",
        "|---|---|---|---|",
    ]
    for item in payload["items"]:
        if item["class"] in mc.BLOCKING_CLASSES or item["class"] not in mc.CLASSES:
            lines.append(
                f"| {item['class']} | {item['set']} | {item['url']} | {item['reason']} |"
            )
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    sys.exit(main())
