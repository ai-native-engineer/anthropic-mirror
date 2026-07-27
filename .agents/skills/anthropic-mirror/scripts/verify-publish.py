#!/usr/bin/env python3
"""Anthropic 미러의 Git 변경분을 발행 전에 검증한다."""

import argparse
import os
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
    "privacy.claude.com",
    "resources.anthropic.com",
    "support.claude.com",
    "transformer-circuits.pub",
    "transformer-circuits.pub.md",
    "trust.anthropic.com",
    "trust.anthropic.com.md",
    "www-cdn.anthropic.com",
    "www.anthropic.com",
    "www.anthropic.com.md",
    "youtube.com",
}
MAX_FILE_BYTES = 100 * 1024 * 1024  # GitHub single-file push limit.


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", repo, *args], check=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=True,
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
        elif ".parts/" in path and not first.startswith("<!-- part of: https://"):
            issues.append(f"split part 헤더 누락: {path}")
        elif ".parts/" not in path and not first.startswith("<!-- source: https://"):
            issues.append(f"source 헤더 누락: {path}")
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
        "trust.anthropic.com/resources.md": b"<!-- source: https://trust.anthropic.com/resources -->\n",
        "platform.claude.com/docs/en/x.parts/part-001.md": b"<!-- part of: https://platform.claude.com/docs/en/x -->\n",
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
    print("self-test ok")


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return 0
    parser = argparse.ArgumentParser()
    parser.add_argument("repo")
    parser.add_argument("--staged", action="store_true", help="worktree 대신 Git index 검사")
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
