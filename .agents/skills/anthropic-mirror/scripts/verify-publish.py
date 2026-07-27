#!/usr/bin/env python3
"""Anthropic 미러의 Git 변경분을 발행 전에 검증한다."""

import argparse
import hashlib
import os
import re
import subprocess
import sys
import tempfile


ALLOWED_ROOTS = {
    "alignment.anthropic.com",
    "alignment.anthropic.com.md",
    "anthropic-partners.skilljar.com",
    "anthropic.skilljar.com",
    "assets.anthropic.com",
    "claude.com",
    "claude.com.md",
    "code.claude.com",
    "platform.claude.com",
    "resources.anthropic.com",
    "support.claude.com",
    "transformer-circuits.pub",
    "transformer-circuits.pub.md",
    "trust.anthropic.com.md",
    "www-cdn.anthropic.com",
    "www.anthropic.com",
    "www.anthropic.com.md",
    "youtube.com",
}
MAX_FILE_BYTES = 100 * 1024 * 1024  # GitHub single-file push limit.
IMAGE_REF = re.compile(r"!\[[^\]]*\]\(\s*([^)]*?)\s*\)")


def image_ref_issues(fp, path):
    """이미지 참조가 로컬 경로면 대상이 실제로 있어야 한다.

    수집기가 페이지 URL(base)을 잃으면 상대 경로와 /_next/image 쿼리가 그대로 박혀
    미러 안에서 해석되지 않는 참조가 된다. 파일 수나 헤더로는 드러나지 않는 회귀라 여기서 잡는다.
    """
    with open(fp, encoding="utf-8", errors="replace") as f:
        text = f.read()
    bad = []
    for ref in IMAGE_REF.findall(text):
        if ref.startswith(("http://", "https://", "data:")):
            continue
        if not ref:
            bad.append("(빈 참조)")
            continue
        target = os.path.join(os.path.dirname(fp), ref.split("#")[0].split("?")[0])
        if not os.path.exists(target):
            bad.append(ref)
    if not bad:
        return []
    return [f"이미지 참조 대상 없음 {len(bad)}건: {path} [{bad[0][:60]}]"]


def _body_digest(fp):
    with open(fp, encoding="utf-8", errors="replace") as f:
        body = "".join(line for line in f if not line.startswith("<!--"))
    return hashlib.md5(body.encode("utf-8")).hexdigest()


def course_duplicate_issues(fp, path):
    """Academy 레슨이 같은 코스의 다른 레슨과 본문이 동일하면 추출 실패다.

    레슨 본문 대신 코스 소개 페이지가 반복 저장돼도 파일명과 source 헤더는 정상이라
    형식 검사만으로는 통과한다. 같은 디렉터리 안에서만 비교한다.
    """
    course = os.path.dirname(fp)
    mine = _body_digest(fp)
    for name in sorted(os.listdir(course)):
        sibling = os.path.join(course, name)
        if not name.endswith(".md") or os.path.abspath(sibling) == os.path.abspath(fp):
            continue
        if os.path.isfile(sibling) and _body_digest(sibling) == mine:
            return [f"같은 코스 레슨과 본문 동일: {path} == {name}"]
    return []


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", repo, *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    ).stdout


def worktree_changes(repo):
    out = git(repo, "status", "--porcelain=v1", "--untracked-files=all")
    return [(line[:2], line[3:]) for line in out.splitlines() if len(line) >= 4]


def staged_changes(repo):
    changes = []
    for line in git(repo, "diff", "--cached", "--name-status").splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            changes.append((parts[0], parts[-1]))
    return changes


def validate_change(repo, status, path, allow_deletes=False, strict_paths=False):
    root = path.split("/", 1)[0]
    if root not in ALLOWED_ROOTS:
        return [f"예상 도메인 밖 변경: {path}"] if strict_paths else []
    if status.startswith(("R", "C")) or "R" in status or "C" in status:
        return [f"rename/copy는 증분 발행 범위 밖: {path}"]
    if "D" in status:
        return [] if allow_deletes else [f"증분 발행에서 삭제 감지: {path}"]

    fp = os.path.join(repo, path)
    if not os.path.isfile(fp):
        return [f"파일을 찾을 수 없음: {path}"]

    issues = []
    if os.path.getsize(fp) > MAX_FILE_BYTES:
        issues.append(f"100MB 초과: {path}")

    with open(fp, "rb") as f:
        head = f.read(8)
    if path.endswith(".pdf"):
        if not head.startswith(b"%PDF-"):
            issues.append(f"PDF 매직바이트 불일치: {path}")
    elif path.endswith(".png"):
        if head != b"\x89PNG\r\n\x1a\n":
            issues.append(f"PNG 매직바이트 불일치: {path}")
    elif path.endswith((".jpg", ".jpeg")):
        if not head.startswith(b"\xff\xd8"):
            issues.append(f"JPEG 매직바이트 불일치: {path}")
    elif path.endswith(".md"):
        with open(fp, encoding="utf-8", errors="replace") as f:
            first = f.readline().rstrip("\n")
        if path in {"youtube.com/anthropic-ai.md", "youtube.com/claude.md"}:
            if not first.startswith("# "):
                issues.append(f"YouTube 인덱스 헤더 불일치: {path}")
        elif path.startswith(("youtube.com/anthropic-ai/", "youtube.com/claude/")):
            if first != "---":
                issues.append(f"YouTube frontmatter 누락: {path}")
        elif root.endswith(".skilljar.com"):
            if not first.startswith("<!-- https://"):
                issues.append(f"Academy source 헤더 누락: {path}")
            issues.extend(course_duplicate_issues(fp, path))
        elif not first.startswith("<!-- source: https://"):
            issues.append(f"source 헤더 누락: {path}")
        issues.extend(image_ref_issues(fp, path))
    else:
        issues.append(f"지원하지 않는 생성물 확장자: {path}")
    return issues


def validate(repo, changes, allow_deletes=False, strict_paths=False):
    issues = []
    for status, path in changes:
        issues.extend(validate_change(repo, status, path, allow_deletes, strict_paths))
    return issues


def self_test():
    root = tempfile.mkdtemp()
    files = {
        "www.anthropic.com/x.md": b"<!-- source: https://www.anthropic.com/x -->\n",
        "anthropic.skilljar.com/course/x.md": b"<!-- https://anthropic.skilljar.com/course/x -->\n",
        "youtube.com/anthropic-ai.md": b"# anthropic-ai (YouTube)\n",
        "youtube.com/anthropic-ai/x.md": b"---\ntitle: x\n---\n",
        "assets.anthropic.com/x.pdf": b"%PDF-test",
        "transformer-circuits.pub/x/images/x.png": b"\x89PNG\r\n\x1a\n",
        "transformer-circuits.pub/x/images/x.jpg": b"\xff\xd8test",
    }
    for path, body in files.items():
        fp = os.path.join(root, path)
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp, "wb") as f:
            f.write(body)
    assert not validate(root, [("??", path) for path in files])
    assert not validate_change(root, "??", "README.md")
    assert validate_change(root, "??", "README.md", strict_paths=True)
    assert not validate_change(root, "D ", "README.md")
    assert validate_change(root, "D ", "README.md", strict_paths=True)
    assert validate_change(root, "D ", "www.anthropic.com/x.md")
    assert not validate_change(root, "D ", "www.anthropic.com/x.md", allow_deletes=True)

    extra = {
        # http 참조와 실재하는 로컬 참조는 통과, 상대·빈 참조는 실패
        "www.anthropic.com/img-ok.md": b"<!-- source: https://www.anthropic.com/i -->\n"
        b"![a](https://cdn/a.png)\n",
        "transformer-circuits.pub/x/ok.md": b"<!-- source: https://transformer-circuits.pub/x/ok -->\n"
        b"![a](images/x.png)\n",
        "www.anthropic.com/img-bad.md": b"<!-- source: https://www.anthropic.com/b -->\n"
        b"![a](/_next/image?url=%2Fa.png)\n",
        "www.anthropic.com/img-empty.md": b"<!-- source: https://www.anthropic.com/e -->\n"
        b"![a]()\n",
        # 같은 코스 안에서 본문이 겹치는 레슨 쌍
        "anthropic.skilljar.com/dup/a.md": b"<!-- https://anthropic.skilljar.com/dup/a -->\nAbout this course\n",
        "anthropic.skilljar.com/dup/b.md": b"<!-- https://anthropic.skilljar.com/dup/b -->\nAbout this course\n",
    }
    for path, body in extra.items():
        fp = os.path.join(root, path)
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp, "wb") as f:
            f.write(body)
    assert not validate_change(root, "??", "www.anthropic.com/img-ok.md")
    assert not validate_change(root, "??", "transformer-circuits.pub/x/ok.md")
    assert validate_change(root, "??", "www.anthropic.com/img-bad.md")
    assert validate_change(root, "??", "www.anthropic.com/img-empty.md")
    assert validate_change(root, "??", "anthropic.skilljar.com/dup/a.md")
    assert not validate_change(root, "??", "anthropic.skilljar.com/course/x.md")
    print("self-test ok")


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return 0
    parser = argparse.ArgumentParser()
    parser.add_argument("repo")
    parser.add_argument(
        "--staged", action="store_true", help="worktree 대신 Git index 검사"
    )
    parser.add_argument("--allow-deletes", action="store_true", help="검토한 삭제 허용")
    args = parser.parse_args()
    repo = os.path.abspath(args.repo)
    try:
        changes = staged_changes(repo) if args.staged else worktree_changes(repo)
    except subprocess.CalledProcessError as error:
        print(error.stderr.strip() or "Git 변경분을 읽지 못했습니다.", file=sys.stderr)
        return 2
    issues = validate(repo, changes, args.allow_deletes, strict_paths=args.staged)
    print(f"Git 변경 {len(changes)}개 검사: 문제 {len(issues)}개")
    for issue in issues[:30]:
        print(f"  {issue}")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
