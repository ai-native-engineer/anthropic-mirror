#!/usr/bin/env python3
"""Anthropic 미러 생성물을 발행 전에 검증한다.

모드:
  <repo>            worktree 변경분
  <repo> --staged   Git index 변경분
  <repo> --all      보관본 전체. 최상위 새 host·미추적 생성물·빈 디렉터리·기존 파일 오류까지 숨기지 않는다.
                    shared verify-mirror.py의 영상 자막·깨진 참조 검사, PDF text layer, coverage 감사 결과를 합친다.

문제(issue)는 발행을 막는 결함이고 exit 1이다. 상태(state)는 분류된 미해결 항목(auth_blocked 등)과 경고로,
문제 수에는 넣지 않지만 표와 JSON에 모두 남긴다. --all은 기본으로 .anthropic-mirror-audit/publish-all.{json,md}를 쓴다.
"""

import argparse
import collections
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from urllib.parse import urlsplit

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "mirror_common", os.path.join(HERE, "mirror-common.py")
)
mc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mc)

MANIFEST = mc.load_manifest()
ALLOWED_ROOTS = set(MANIFEST["archive_roots"])
NON_ARCHIVE_ROOTS = set(MANIFEST["non_archive_roots"])
MAX_FILE_BYTES = 100 * 1024 * 1024  # GitHub single-file push limit.
GENERATED_EXTS = {".md", ".pdf", ".png", ".jpg", ".jpeg", ".svg"}
IMAGE_REF = re.compile(r"!\[[^\]]*\]\(\s*(<[^>]*>|[^)\s]*)")
ATTACHMENT_REF = re.compile(r"!\[[^\]]*\]\(\s*<?attachment:[^)\s]*")
GATED_STUB = "_(등록 또는 권한이 필요한 레슨)_"
NO_BODY_LESSON = "_(본문 없는 레슨: 퀴즈·과제처럼 추출할 텍스트가 없음)_"
# 크롤러가 200자 미만 본문을 thin으로 버린다. 그보다 훨씬 짧은데 상태 마커도 없으면 저장 경로 결함이다.
MIN_BODY_CHARS = 50
CRAWL_SCRIPTS_DIR = os.environ.get(
    "CRAWL_SCRIPTS_DIR", os.path.expanduser("~/.agents/skills/shared/crawl/scripts")
)
VERIFY_MIRROR_EXCLUDES = [
    "*.skilljar.com/**",
    "platform.claude.com/**",
    "code.claude.com/**",
]


def issue(kind, path, detail=""):
    return {"kind": kind, "path": path, "detail": detail}


def read_text(fp):
    with open(fp, encoding="utf-8", errors="replace") as f:
        return f.read()


def image_ref_issues(text, fp, path):
    """이미지 참조는 원격 URL, data URI, 또는 실제로 있는 로컬 파일이어야 한다.

    수집기가 페이지 URL(base)을 잃으면 상대 경로와 /_next/image 쿼리가 그대로 박혀
    미러 안에서 해석되지 않는 참조가 된다. 파일 수나 헤더 검사로는 드러나지 않는다.
    """
    found = []
    for ref in IMAGE_REF.findall(text):
        if ref.startswith("<") and ref.endswith(">"):
            ref = ref[1:-1]
        ref = ref.strip()
        if ref.startswith(("http://", "https://", "data:")):
            continue
        if ref.startswith("attachment:"):
            continue  # attachment_ref_issues가 따로 센다
        if not ref:
            found.append(issue("빈 이미지 참조", path, "![]()"))
            continue
        target = os.path.join(os.path.dirname(fp), ref.split("#")[0].split("?")[0])
        if not os.path.exists(target):
            found.append(issue("로컬 이미지 참조 대상 없음", path, ref[:80]))
    return found


def attachment_ref_issues(text, path):
    """Jupyter attachment:는 미러에서 렌더되지 않는다. 수집기가 [미수집 첨부 이미지: ...]로 바꿔야 한다."""
    refs = ATTACHMENT_REF.findall(text)
    return [issue("미해결 attachment 이미지", path, f"{len(refs)}건")] if refs else []


def _body_digest(fp):
    with open(fp, encoding="utf-8", errors="replace") as f:
        body = "".join(line for line in f if not line.startswith("<!--"))
    return hashlib.md5(body.strip().encode("utf-8")).hexdigest()


def course_duplicate_issues(fp, path):
    """Academy 레슨이 같은 코스의 다른 레슨과 본문이 동일하면 추출이 실패한 것이다.

    세션이 만료되면 레슨이 코스 랜딩으로 튕겨 'About this course'가 모든 레슨에 저장되는데,
    파일명과 source 헤더는 정상이라 형식 검사만으로는 통과한다. 같은 디렉터리 안에서만 비교한다.
    """
    course = os.path.dirname(fp)
    mine = _body_digest(fp)
    for name in sorted(os.listdir(course)):
        sibling = os.path.join(course, name)
        if not name.endswith(".md") or os.path.abspath(sibling) == os.path.abspath(fp):
            continue
        if os.path.isfile(sibling) and _body_digest(sibling) == mine:
            return [issue("같은 코스 레슨과 본문 동일", path, name)]
    return []


def expected_path(url):
    """crawl-mirror dest 규칙: <host>/<path>.md, 루트는 <host>.md."""
    parts = urlsplit(url)
    rel = parts.path.strip("/")
    return f"{parts.netloc}/{rel}.md" if rel else f"{parts.netloc}.md"


def body_of(text):
    lines = text.splitlines()
    if lines and lines[0] == "---":
        end = next((i for i, line in enumerate(lines[1:], 1) if line == "---"), 0)
        lines = lines[end + 1 :]
    return "\n".join(line for line in lines if not line.startswith("<!--")).strip()


# 본문 대신 페이지 크롬이 저장된 신호. raw HTML 문서와 쿠키 동의 배너는 원문 본문에 나오지 않는다.
CHROME_LEAKS = (
    ("raw HTML이 본문으로 저장됨", re.compile(r"^\s*<(?:!doctype html|html[\s>])", re.I)),
    ("쿠키 동의 배너가 본문에 남음", re.compile(r"^#+ Cookie settings\s*$", re.M)),
)


def markdown_issues(fp, path, root, text):
    found, states = [], []
    first, second = (text.split("\n") + ["", ""])[:2]
    if path in {"youtube.com/anthropic-ai.md", "youtube.com/claude.md"}:
        if not first.startswith("# "):
            found.append(issue("YouTube 인덱스 헤더 불일치", path))
    elif path.startswith("youtube.com/"):
        if first != "---":
            found.append(issue("YouTube frontmatter 누락", path))
        else:
            for field in ("youtube_id", "url", "captions"):
                if not re.search(rf"^{field}:\s*\S", text, re.M):
                    found.append(issue("YouTube frontmatter 필드 누락", path, field))
    elif root.endswith(".skilljar.com"):
        m = re.match(r"<!-- (https://\S+) -->$", first)
        if not m:
            found.append(issue("Academy source 헤더 누락", path))
        else:
            parts = urlsplit(m.group(1))
            course = parts.path.strip("/").split("/")[0]
            if parts.netloc != root or path.split("/")[1] != course:
                found.append(issue("Academy source와 경로 불일치", path, m.group(1)))
        if GATED_STUB in text:
            states.append(
                issue(
                    "auth_blocked: 등록·권한 필요 레슨 stub",
                    path,
                    m.group(1) if m else "",
                )
            )
        found.extend(course_duplicate_issues(fp, path))
    elif ".parts/" in path:
        if not any(
            line.startswith("<!-- part of: https://") for line in (first, second)
        ):
            found.append(issue("split part 헤더 누락", path))
    else:
        m = re.match(r"<!-- source: (https://\S+?) -->$", first)
        if not m:
            found.append(issue("source 헤더 누락", path))
        elif expected_path(m.group(1)) != path:
            found.append(issue("source URL과 파일 경로 불일치", path, m.group(1)))
    body = body_of(text)
    for kind, pattern in CHROME_LEAKS:
        if pattern.search(body):
            found.append(issue(kind, path))
    if NO_BODY_LESSON in text:
        states.append(issue("본문 없는 레슨(퀴즈·과제) 표시", path))
    elif len(body) < MIN_BODY_CHARS and GATED_STUB not in text and ".parts/" not in path:
        found.append(issue("본문 없음·thin", path, f"{len(body)}자"))
    elif len(body) < 200 and GATED_STUB not in text:
        states.append(issue("경고: 짧은 본문(<200자)", path, f"{len(body)}자"))
    found.extend(image_ref_issues(text, fp, path))
    found.extend(attachment_ref_issues(text, path))
    missing = mc.ASSET_MISSING.findall(text)
    if missing:
        states.append(
            issue("asset_missing: 미수집 이미지 마커", path, f"{len(missing)}건")
        )
    return found, states


def asset_issues(fp, path, head, tail):
    """확장자와 실제 형식이 맞고, 잘리지 않아 렌더 가능한지 본다(PNG IEND, JPEG EOI, SVG 루트)."""
    if path.endswith(".pdf"):
        if not head.startswith(b"%PDF-"):
            return [issue("PDF 매직바이트 불일치", path)]
        if b"%%EOF" not in tail:
            return [issue("PDF 끝(%%EOF) 없음, 잘린 파일", path)]
    elif path.endswith(".png"):
        if not head.startswith(b"\x89PNG\r\n\x1a\n"):
            return [issue("PNG 매직바이트 불일치", path)]
        if b"IEND" not in tail:
            return [issue("PNG IEND 없음, 잘린 이미지", path)]
    elif path.endswith((".jpg", ".jpeg")):
        if not head.startswith(b"\xff\xd8"):
            return [issue("JPEG 매직바이트 불일치", path)]
        if b"\xff\xd9" not in tail:
            return [issue("JPEG EOI 없음, 잘린 이미지", path)]
    elif path.endswith(".svg"):
        if b"<svg" not in head:
            return [issue("SVG 헤더 불일치", path)]
    return []


def validate_change(repo, status, path, allow_deletes=False, strict_paths=False):
    """호환 API: 문제 문자열 목록. validate_path가 정본이다."""
    return [
        f"{i['kind']}: {i['path']}" + (f" [{i['detail']}]" if i["detail"] else "")
        for i in validate_path(repo, status, path, allow_deletes, strict_paths)[0]
    ]


def validate_path(repo, status, path, allow_deletes=False, strict_paths=False):
    root = path.split("/", 1)[0]
    if root not in ALLOWED_ROOTS:
        return ([issue("예상 도메인 밖 변경", path)] if strict_paths else []), []
    if "R" in status or "C" in status:
        return [issue("rename/copy는 증분 발행 범위 밖", path)], []
    if "D" in status:
        return ([] if allow_deletes else [issue("증분 발행에서 삭제 감지", path)]), []

    fp = os.path.join(repo, path)
    if not os.path.isfile(fp):
        return [issue("파일을 찾을 수 없음", path)], []
    size = os.path.getsize(fp)
    if size == 0:
        return [issue("빈 파일", path)], []
    found, states = [], []
    if size > MAX_FILE_BYTES:
        found.append(issue("100MB 초과", path))
    ext = os.path.splitext(path)[1].lower()
    if ext not in GENERATED_EXTS:
        return found + [issue("지원하지 않는 생성물 확장자", path)], states
    with open(fp, "rb") as f:
        head = f.read(512)
        f.seek(max(0, size - 1024))
        tail = f.read()
    if ext == ".md":
        text = read_text(fp)
        md_found, md_states = markdown_issues(fp, path, root, text)
        found += md_found
        states += md_states
    else:
        found += asset_issues(fp, path, head, tail)
    return found, states


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", repo, *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    ).stdout


def worktree_changes(repo):
    """Null-terminated porcelain so paths with spaces/unicode stay intact."""
    fields = git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all").split(
        "\0"
    )
    changes = []
    i = 0
    while i < len(fields):
        entry = fields[i]
        i += 1
        if len(entry) < 4:
            continue
        status = entry[:2]
        changes.append((status, entry[3:]))
        if "R" in status or "C" in status:
            i += 1
    return changes


def staged_changes(repo):
    """Null-terminated name-status so staged paths with spaces stay intact."""
    fields = git(repo, "diff", "--cached", "--name-status", "-z").split("\0")
    changes = []
    i = 0
    while i + 1 < len(fields) and fields[i]:
        status = fields[i]
        if status[0] in ("R", "C") and i + 2 < len(fields):
            changes.append((status, fields[i + 2]))
            i += 3
        else:
            changes.append((status, fields[i + 1]))
            i += 2
    return changes


def all_changes(repo):
    """추적 파일과 ignore되지 않은 미추적 파일 전체. 비보관 루트만 뺀다."""
    paths = git(repo, "ls-files", "-z", "-co", "--exclude-standard").split("\0")
    return [
        ("??" if p in untracked_set(repo) else "  ", p)
        for p in paths
        if p and p.split("/", 1)[0] not in NON_ARCHIVE_ROOTS
    ]


_UNTRACKED = {}


def untracked_set(repo):
    if repo not in _UNTRACKED:
        _UNTRACKED[repo] = set(
            git(repo, "ls-files", "-z", "-o", "--exclude-standard").split("\0")
        )
    return _UNTRACKED[repo]


def top_level_issues(repo):
    """새 host 디렉터리, 비어 있어 Git에 안 보이는 디렉터리, 미추적 생성물을 드러낸다."""
    found, states = [], []
    ignored = set()
    names = sorted(os.listdir(repo))
    if names:
        result = subprocess.run(
            ["git", "-C", repo, "check-ignore", "--stdin", "-z"],
            input="\0".join(names),
            capture_output=True,
            text=True,
        )
        ignored = set(filter(None, result.stdout.split("\0")))
    for name in names:
        if name in NON_ARCHIVE_ROOTS or name in ignored or name.startswith("."):
            continue
        fp = os.path.join(repo, name)
        has_files = os.path.isfile(fp) or any(files for _, _, files in os.walk(fp))
        if name not in ALLOWED_ROOTS:
            if not has_files:
                states.append(
                    issue("경고: 파일 없는 최상위 디렉터리(Git 미추적)", name)
                )
            elif mc.is_official_host(name.removesuffix(".md"), MANIFEST):
                found.append(issue("manifest에 없는 새 공식 host 생성물", name))
            else:
                found.append(issue("예상 밖 최상위 항목", name))
    untracked = [
        p
        for p in untracked_set(repo)
        if p and p.split("/", 1)[0] not in NON_ARCHIVE_ROOTS
    ]
    for path in sorted(untracked):
        states.append(issue("미추적 생성물", path))
    return found, states


def pdf_layer_issues(repo, pdfs):
    """PDF가 text layer를 가져 pdftotext로 글자를 뽑을 수 있는지와 OCR marker를 확인한다."""
    found = []
    if not shutil.which("pdftotext"):
        return [issue("검사 도구 없음", "pdftotext")]
    for path in pdfs:
        result = subprocess.run(
            ["pdftotext", "-q", "-l", "3", os.path.join(repo, path), "-"],
            capture_output=True,
            text=True,
            errors="replace",
        )
        if result.returncode != 0:
            found.append(issue("pdftotext 실패", path, result.stderr.strip()[:80]))
        elif len(result.stdout.strip()) < 20:
            found.append(issue("PDF text layer 없음(pdftotext 20자 미만)", path))
    checker = os.path.join(HERE, "add-pdf-text-layer.py")
    result = subprocess.run(
        [sys.executable, checker, repo, "--check"],
        capture_output=True,
        text=True,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    if result.returncode != 0:
        missing = re.findall(r"missing text layer: (\S.*)", result.stdout)
        for path in missing or ["(unknown)"]:
            found.append(
                issue("OCR text layer marker 없음", path, result.stderr.strip()[:80])
            )
    return found


def verify_mirror_issues(repo):
    """shared verify-mirror.py의 자막 누락·1MiB 초과·빈 이미지·깨진 로컬 참조를 합친다. 경고 kind는 상태로 보낸다."""
    path = os.path.join(CRAWL_SCRIPTS_DIR, "verify-mirror.py")
    if not os.path.isfile(path):
        return [issue("검사 도구 없음", path)], []
    spec = importlib.util.spec_from_file_location("verify_mirror", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if not hasattr(module, "scan"):
        return [issue("verify-mirror.py가 scan()을 제공하지 않음", path)], []
    found, states = [], []
    for kind, rel, detail in module.scan(repo, VERIFY_MIRROR_EXCLUDES):
        if rel.split(os.sep, 1)[0] not in ALLOWED_ROOTS:
            continue  # 감사 결과·작업 폴더는 발행 트리가 아니다
        target = states if kind in getattr(module, "WARN_KINDS", ()) else found
        target.append(issue(f"verify-mirror: {kind}", rel, detail))
    return found, states


def coverage_state(repo):
    """마지막 coverage-audit 결과. 미분류가 있으면 문제, 차단 분류는 상태로 보인다."""
    path = os.path.join(repo, mc.AUDIT_DIR, "coverage.json")
    if not os.path.isfile(path):
        return [], [
            issue("경고: coverage 감사 결과 없음", path, "coverage-audit.py 실행 필요")
        ]
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    found, states = [], []
    for item in data.get("items", []):
        if item.get("class") not in mc.CLASSES:
            found.append(
                issue("coverage 미분류 URL", item.get("url", ""), item.get("set", ""))
            )
        elif item["class"] in mc.BLOCKING_CLASSES:
            states.append(
                issue(
                    f"{item['class']} ({item.get('set', '')})",
                    item.get("url", ""),
                    item.get("reason", ""),
                )
            )
    states.append(issue("coverage 감사 시각", path, data.get("generated_at", "")))
    return found, states


def validate(repo, changes, allow_deletes=False, strict_paths=False):
    found, states = [], []
    for status, path in changes:
        f, s = validate_path(repo, status, path, allow_deletes, strict_paths)
        found += f
        states += s
    return found, states


def render_report(mode, checked, found, states):
    lines = [
        f"# verify-publish {mode}",
        "",
        f"- 검사 파일: {checked}",
        f"- 문제: {len(found)}",
        f"- 상태·경고: {len(states)}",
        "",
    ]
    for title, rows in (("문제", found), ("상태·경고", states)):
        counts = collections.Counter(r["kind"] for r in rows)
        lines += [f"## {title}", "", "| 종류 | 건수 | 예시 |", "|---|---:|---|"]
        for kind, n in counts.most_common():
            sample = next(r for r in rows if r["kind"] == kind)
            lines.append(f"| {kind} | {n} | `{sample['path']}` {sample['detail']} |")
        lines.append("")
    return "\n".join(lines)


def self_test():
    root = tempfile.mkdtemp()
    files = {
        "www.anthropic.com/x.md": b"<!-- source: https://www.anthropic.com/x -->\n\n"
        + b"body " * 20
        + b"\n",
        "anthropic.skilljar.com/course/x.md": b"<!-- https://anthropic.skilljar.com/course/1 -->\n\n"
        + b"lesson " * 20
        + b"\n",
        "youtube.com/anthropic-ai.md": b"# anthropic-ai (YouTube)\n\n"
        + b"index " * 20
        + b"\n",
        "youtube.com/anthropic-ai/x.md": b"---\ntitle: x\nurl: https://youtu.be/x\nyoutube_id: ABCDEFGHIJK\ncaptions: none\n---\n\n"
        + b"t " * 40
        + b"\n",
        "anthropic.com/document/x.pdf": b"%PDF-test\n%%EOF\n",
        "assets.anthropic.com/x.pdf": b"%PDF-test\n%%EOF\n",
        "trust.anthropic.com/resources.md": b"<!-- source: https://trust.anthropic.com/resources -->\n\n"
        + b"r " * 40
        + b"\n",
        "platform.claude.com/docs/en/x.parts/part-001.md": (
            b"<!-- source: https://platform.claude.com/docs/en/x -->\n"
            b"<!-- part of: https://platform.claude.com/docs/en/x -->\n"
            + b"p " * 40
            + b"\n"
        ),
        "transformer-circuits.pub/x/images/x.png": b"\x89PNG\r\n\x1a\nIEND",
        "transformer-circuits.pub/x/images/x.jpg": b"\xff\xd8test\xff\xd9",
        "www.anthropic.com/events/images/x.svg": b"<svg xmlns='http://www.w3.org/2000/svg'></svg>",
    }
    for path, body in files.items():
        fp = os.path.join(root, path)
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp, "wb") as f:
            f.write(body)
    found, _ = validate(root, [("??", path) for path in files])
    assert not found, found
    assert not validate_change(root, "??", "README.md")
    assert validate_change(root, "??", "README.md", strict_paths=True)
    assert not validate_change(root, "D ", "README.md")
    assert validate_change(root, "D ", "README.md", strict_paths=True)
    assert validate_change(root, "D ", "www.anthropic.com/x.md")
    assert not validate_change(root, "D ", "www.anthropic.com/x.md", allow_deletes=True)

    body = b"x " * 120
    extra = {
        "www.anthropic.com/img-ok.md": b"<!-- source: https://www.anthropic.com/img-ok -->\n"
        + body
        + b"![a](https://cdn/a.png) ![b](<https://cdn/b c.png>) [\xeb\xaf\xb8\xec\x88\x98\xec\xa7\x91 \xec\x9d\xb4\xeb\xaf\xb8\xec\xa7\x80: Chart]\n",
        "www.anthropic.com/img-attach.md": b"<!-- source: https://www.anthropic.com/img-attach -->\n"
        + body
        + b"![c](attachment:image.png)\n",
        "transformer-circuits.pub/x/local-ok.md": b"<!-- source: https://transformer-circuits.pub/x/local-ok -->\n"
        + body
        + b"![a](images/x.png)\n",
        "www.anthropic.com/img-relative.md": b"<!-- source: https://www.anthropic.com/img-relative -->\n"
        + body
        + b"![a](/_next/image?url=%2Fa.png)\n",
        "www.anthropic.com/img-empty.md": b"<!-- source: https://www.anthropic.com/img-empty -->\n"
        + body
        + b"![a]()\n",
        "www.anthropic.com/moved.md": b"<!-- source: https://www.anthropic.com/elsewhere -->\n"
        + body,
        "www.anthropic.com/thin.md": b"<!-- source: https://www.anthropic.com/thin -->\n\n# T\n",
        "www.anthropic.com/raw.md": b"<!-- source: https://www.anthropic.com/raw -->\n\n<!DOCTYPE html><html>"
        + b"x" * 300
        + b"\n",
        "www.anthropic.com/banner.md": b"<!-- source: https://www.anthropic.com/banner -->\n\n### Cookie settings\n\n"
        + b"x" * 300
        + b"\n",
        "anthropic.skilljar.com/dup/a.md": b"<!-- https://anthropic.skilljar.com/dup/1 -->\n\n## About this course\n"
        + body,
        "anthropic.skilljar.com/dup/b.md": b"<!-- https://anthropic.skilljar.com/dup/2 -->\n\n## About this course\n"
        + body,
        "anthropic.skilljar.com/gate/a.md": (
            "<!-- https://anthropic.skilljar.com/gate/3 -->\n\n# L\n\n"
            + GATED_STUB
            + "\n"
        ).encode(),
        "anthropic.skilljar.com/wrong/a.md": b"<!-- https://anthropic.skilljar.com/other/4 -->\n\n"
        + body,
        "anthropic.skilljar.com/quiz/a.md": (
            "<!-- https://anthropic.skilljar.com/quiz/5 -->\n\n# Quiz\n\n" + NO_BODY_LESSON + "\n"
        ).encode(),
        "transformer-circuits.pub/x/images/cut.png": b"\x89PNG\r\n\x1a\nno-end",
        "anthropic.com/document/cut.pdf": b"%PDF-1.7 no end",
    }
    for path, content in extra.items():
        fp = os.path.join(root, path)
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp, "wb") as f:
            f.write(content)

    def kinds(path):
        found, states = validate_path(root, "??", path)
        return {i["kind"] for i in found}, {i["kind"] for i in states}

    assert kinds("www.anthropic.com/img-ok.md") == (
        set(),
        {"asset_missing: 미수집 이미지 마커"},
    ), kinds("www.anthropic.com/img-ok.md")
    assert kinds("www.anthropic.com/img-attach.md")[0] == {"미해결 attachment 이미지"}
    assert not kinds("transformer-circuits.pub/x/local-ok.md")[0]
    assert kinds("www.anthropic.com/img-relative.md")[0] == {
        "로컬 이미지 참조 대상 없음"
    }
    assert kinds("www.anthropic.com/img-empty.md")[0] == {"빈 이미지 참조"}
    assert kinds("www.anthropic.com/moved.md")[0] == {"source URL과 파일 경로 불일치"}
    assert kinds("www.anthropic.com/thin.md")[0] == {"본문 없음·thin"}
    assert kinds("www.anthropic.com/raw.md")[0] == {"raw HTML이 본문으로 저장됨"}
    assert kinds("www.anthropic.com/banner.md")[0] == {"쿠키 동의 배너가 본문에 남음"}
    assert kinds("anthropic.skilljar.com/dup/a.md")[0] == {"같은 코스 레슨과 본문 동일"}
    assert kinds("anthropic.skilljar.com/gate/a.md") == (
        set(),
        {"auth_blocked: 등록·권한 필요 레슨 stub"},
    )
    assert kinds("anthropic.skilljar.com/wrong/a.md")[0] == {
        "Academy source와 경로 불일치"
    }
    assert kinds("anthropic.skilljar.com/quiz/a.md") == (set(), {"본문 없는 레슨(퀴즈·과제) 표시"})
    assert kinds("transformer-circuits.pub/x/images/cut.png")[0] == {
        "PNG IEND 없음, 잘린 이미지"
    }
    assert kinds("anthropic.com/document/cut.pdf")[0] == {
        "PDF 끝(%%EOF) 없음, 잘린 파일"
    }
    assert expected_path("https://claude.com/") == "claude.com.md"
    assert (
        expected_path("https://transformer-circuits.pub/a/b.html")
        == "transformer-circuits.pub/a/b.html.md"
    )

    # --all 최상위 검사: 새 공식 host, 파일 없는 디렉터리, 미추적 생성물을 숨기지 않는다.
    git(root, "init", "-q")
    os.makedirs(os.path.join(root, "brand-new.anthropic.com"))
    with open(os.path.join(root, "brand-new.anthropic.com", "x.md"), "w") as f:
        f.write("x")
    os.makedirs(os.path.join(root, "empty.example", "deep"))
    found, states = top_level_issues(root)
    assert {"manifest에 없는 새 공식 host 생성물"} <= {i["kind"] for i in found}, found
    assert any(i["path"] == "empty.example" for i in states), states
    assert any(i["kind"] == "미추적 생성물" for i in states), states

    spaced = "www.anthropic.com/한글 문서.md"
    fp = os.path.join(root, spaced)
    with open(fp, "wb") as f:
        f.write(b"<!-- source: https://www.anthropic.com/x -->\n")
    assert spaced in {path for _, path in worktree_changes(root)}
    git(root, "add", "-A")
    assert spaced in {path for _, path in staged_changes(root)}
    report = render_report("--all", 1, [issue("빈 이미지 참조", "a.md")], [])
    assert "| 빈 이미지 참조 | 1 |" in report
    mc.self_test()
    print("self-test ok")


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return 0
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("repo")
    parser.add_argument(
        "--staged", action="store_true", help="worktree 대신 Git index 검사"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="보관본 전체 검사(최상위 항목·PDF text layer·verify-mirror·coverage 포함)",
    )
    parser.add_argument("--allow-deletes", action="store_true", help="검토한 삭제 허용")
    parser.add_argument(
        "--json",
        help="결과 JSON 경로(--all 기본: .anthropic-mirror-audit/publish-all.json)",
    )
    args = parser.parse_args()
    repo = os.path.abspath(args.repo)
    try:
        if args.all:
            changes = all_changes(repo)
        else:
            changes = staged_changes(repo) if args.staged else worktree_changes(repo)
    except subprocess.CalledProcessError as error:
        print(error.stderr.strip() or "Git 변경분을 읽지 못했습니다.", file=sys.stderr)
        return 2
    found, states = validate(
        repo, changes, args.allow_deletes, strict_paths=args.staged or args.all
    )
    mode = "--all" if args.all else ("--staged" if args.staged else "worktree")
    json_path = args.json
    if args.all:
        f, s = top_level_issues(repo)
        found += f
        states += s
        found += pdf_layer_issues(repo, [p for _, p in changes if p.endswith(".pdf")])
        f, s = verify_mirror_issues(repo)
        found += f
        states += s
        f, s = coverage_state(repo)
        found += f
        states += s
        json_path = json_path or os.path.join(repo, mc.AUDIT_DIR, "publish-all.json")

    print(
        f"{mode}: 파일 {len(changes)}개 검사, 문제 {len(found)}개, 상태·경고 {len(states)}개"
    )
    for title, rows, limit in (("문제", found, 50), ("상태·경고", states, 0)):
        counts = collections.Counter(r["kind"] for r in rows)
        if counts:
            print(f"[{title}]")
            for kind, n in counts.most_common():
                print(f"  {n:6d}  {kind}")
    for row in found[:50]:
        print(
            f"  - {row['kind']}: {row['path']}"
            + (f" [{row['detail']}]" if row["detail"] else "")
        )
    if len(found) > 50:
        print(f"  ... 나머지 {len(found) - 50}건은 JSON에 있음")
    if json_path:
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        payload = {
            "mode": mode,
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "checked": len(changes),
            "issues": found,
            "states": states,
        }
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        md_path = os.path.splitext(json_path)[0] + ".md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(render_report(mode, len(changes), found, states))
        print(f"결과: {json_path} / {md_path}")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
