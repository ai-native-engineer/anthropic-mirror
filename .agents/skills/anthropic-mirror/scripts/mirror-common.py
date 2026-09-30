"""anthropic-mirror 수집기·검증기·감사기가 공유하는 manifest, URL 정규화, 상태 기록.

직접 실행하지 않는다. 각 스크립트가 importlib로 불러 쓴다(stdlib만 사용 -- 시스템 python3와
crawl4ai 인터프리터 양쪽에서 같은 모듈을 읽는다).
"""

import fnmatch
import json
import os
import re
import time
from urllib.parse import urlsplit, urlunsplit

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_PATH = os.path.join(SKILL_DIR, "assets", "mirror-manifest.json")
STATUS_FILE = ".anthropic-mirror-status.json"
AUDIT_DIR = ".anthropic-mirror-audit"

CLASSES = (
    "structural_missing",
    "refresh_pending",
    "extract_failed",
    "stale_or_redirect",
    "auth_blocked",
    "scope_decision",
    "intentional_exclusion",
)
# 수집이 끝나지 않았음을 뜻하는 분류. 분류 자체는 됐어도 완료 판정을 막는다.
BLOCKING_CLASSES = (
    "structural_missing",
    "refresh_pending",
    "extract_failed",
    "auth_blocked",
)

# 원본에 자산이 없거나 받을 수 없는 이미지를 깨진 참조 대신 남기는 명시 마커.
ASSET_MISSING = re.compile(r"\[미수집 (?:첨부 )?이미지: [^\]\n]*\]")


def load_manifest():
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        return json.load(f)


def archive_roots(manifest=None):
    return set((manifest or load_manifest())["archive_roots"])


def is_official_host(host, manifest=None):
    manifest = manifest or load_manifest()
    host = (host or "").lower().rstrip(".")
    if host in manifest["official_hosts"]:
        return True
    return any(
        host == d or host.endswith("." + d) for d in manifest["official_domains"]
    )


def host_decision(host, manifest=None):
    """manifest에 기록된 호스트 단위 판정 (class, reason) 또는 None."""
    decisions = (manifest or load_manifest())["host_decisions"]
    host = (host or "").lower()
    if host in decisions:
        return tuple(decisions[host])
    for pattern, value in decisions.items():
        if "*" in pattern and fnmatch.fnmatch(host, pattern):
            return tuple(value)
    return None


def url_decision(url, manifest=None):
    """URL 단위 판정 (class, reason) 또는 None. path_decisions가 host_decisions보다 먼저다.

    path_decisions는 순서대로 "host/path" fnmatch를 보고 첫 매칭에서 멈춘다. class가 null이면 수집 대상이라는 명시다.
    """
    manifest = manifest or load_manifest()
    parts = urlsplit(url)
    key = parts.netloc.lower() + (parts.path.rstrip("/") or "/")
    for pattern, cls, reason in manifest.get("path_decisions", []):
        if fnmatch.fnmatch(key, pattern):
            return (cls, reason) if cls else None
    return host_decision(parts.netloc, manifest)


def norm_url(url):
    """집합 대조용 정규화: https, 소문자 host, fragment·query 제거, index.html·끝 슬래시 제거."""
    url = (url or "").strip()
    if not url:
        return ""
    parts = urlsplit(url)
    path = re.sub(r"/index\.html?$", "/", parts.path)
    if len(path) > 1:
        path = path.rstrip("/")
    return urlunsplit(("https", parts.netloc.lower(), path or "/", "", ""))


def status_path(out):
    return os.path.join(out, STATUS_FILE)


def load_status(out):
    try:
        with open(status_path(out), encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def record_status(out, key, items, replace_prefix=None):
    """수집 단계의 미해결 항목을 surface key 단위로 교체 기록한다.

    items: [{"url", "class", "reason"}]. 성공한 항목은 넣지 않는다.
    replace_prefix를 주면 그 prefix로 시작하는 기존 key를 먼저 지운다(전체 재실행).
    """
    data = load_status(out)
    surfaces = data.setdefault("surfaces", {})
    if replace_prefix:
        for existing in [k for k in surfaces if k.startswith(replace_prefix)]:
            del surfaces[existing]
    surfaces[key] = {
        "at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "items": sorted(items, key=lambda item: item["url"]),
    }
    path = status_path(out)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    os.replace(tmp, path)


def status_items(out, prefix=""):
    items = []
    for key, value in load_status(out).get("surfaces", {}).items():
        if key.startswith(prefix):
            for item in value.get("items", []):
                items.append({**item, "surface": key})
    return items


def classify_http(status, final_url="", requested="", error=""):
    """HTTP 결과를 미해결 분류로 바꾼다. 정상 200 본문은 None."""
    final_path = urlsplit(final_url or "").path.lower()
    if re.search(
        r"/(?:login|signin|sign-in|auth/login|accounts/login)(?:/|$)", final_path
    ):
        return "auth_blocked", "login wall"
    if error:
        return "refresh_pending", f"network: {error[:80]}"
    if status in (404, 410):
        return "stale_or_redirect", f"HTTP {status}"
    if status == 401:
        return "auth_blocked", "HTTP 401"
    if status == 403:
        return "refresh_pending", "HTTP 403 (봇 차단 또는 권한), 재시도"
    if status and status >= 500:
        return "refresh_pending", f"HTTP {status}"
    if status and status != 200:
        return "refresh_pending", f"HTTP {status}"
    if requested and final_url and norm_url(requested) != norm_url(final_url):
        return "stale_or_redirect", f"redirect -> {final_url}"
    return None


def self_test():
    manifest = load_manifest()
    assert is_official_host("red.anthropic.com", manifest)
    assert is_official_host("anthropic.skilljar.com", manifest)
    assert not is_official_host("example.com", manifest)
    assert host_decision("x.mcp.claude.com", manifest)[0] == "intentional_exclusion"
    assert host_decision("brand-new.claude.com", manifest) is None
    assert url_decision("https://platform.claude.com/docs/en/x", manifest) is None
    assert url_decision("https://platform.claude.com/settings/keys", manifest)[0] == "intentional_exclusion"
    assert url_decision("https://platform.claude.com/", manifest)[0] == "intentional_exclusion"
    assert url_decision("https://claude.ai/new", manifest)[0] == "intentional_exclusion"
    for pattern, cls, _ in manifest.get("path_decisions", []):
        assert cls is None or cls in CLASSES, pattern
    for value in manifest["host_decisions"].values():
        assert value[0] in CLASSES, value
    assert norm_url("http://WWW.x.com/a/index.html#f") == "https://www.x.com/a"
    assert norm_url("https://x.com/a/?q=1") == "https://x.com/a"
    assert norm_url("https://x.com") == "https://x.com/"
    assert classify_http(404)[0] == "stale_or_redirect"
    assert (
        classify_http(200, "https://x.com/login", "https://x.com/a")[0]
        == "auth_blocked"
    )
    assert (
        classify_http(200, "https://x.com/b", "https://x.com/a")[0]
        == "stale_or_redirect"
    )
    assert classify_http(200, "https://x.com/a/", "https://x.com/a") is None
    assert classify_http(0, error="timeout")[0] == "refresh_pending"
    assert ASSET_MISSING.search("[미수집 첨부 이미지: image.png]")
    assert ASSET_MISSING.search("[미수집 이미지: Diagram]")
    assert set(BLOCKING_CLASSES) <= set(CLASSES)
