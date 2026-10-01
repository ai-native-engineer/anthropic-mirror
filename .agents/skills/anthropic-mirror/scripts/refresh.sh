#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: refresh.sh [--check|--self-test]"
}

case "${1:-}" in
  "") ;;
  --check) CHECK_ONLY=1 ;;
  --self-test) SELF_TEST=1 ;;
  --help|-h) usage; exit 0 ;;
  *) usage >&2; exit 2 ;;
esac

if [ "$#" -gt 1 ]; then
  usage >&2
  exit 2
fi

SKILL_DIR=$(cd "$(dirname "$0")/.." && pwd -P)
REPO_ROOT=$(git -C "$SKILL_DIR" rev-parse --show-toplevel)
CRAWL4AI_PYTHON=${CRAWL4AI_PYTHON:-"$HOME/.local/share/uv/tools/crawl4ai/bin/python"}
CRAWL_SCRIPTS_DIR=${CRAWL_SCRIPTS_DIR:-"$HOME/.agents/skills/shared/crawl/scripts"}
YOUTUBE_DIGEST_SCRIPTS_DIR=${YOUTUBE_DIGEST_SCRIPTS_DIR:-"$HOME/.agents/skills/shared/youtube/youtube-digest/scripts"}

require_file() {
  if [ ! -f "$1" ]; then
    echo "Missing required file: $1" >&2
    exit 1
  fi
}

for file in \
  "$SKILL_DIR/SKILL.md" \
  "$REPO_ROOT/AGENTS.md" \
  "$SKILL_DIR/assets/mirror-manifest.json" \
  "$SKILL_DIR/scripts/mirror-common.py" \
  "$SKILL_DIR/scripts/crawl-site.py" \
  "$SKILL_DIR/scripts/academy-video.py" \
  "$SKILL_DIR/scripts/coverage-audit.py" \
  "$SKILL_DIR/scripts/add-pdf-text-layer.py" \
  "$SKILL_DIR/scripts/verify-publish.py"; do
  require_file "$file"
done

if [ "${SELF_TEST:-0}" = 1 ]; then
  export PYTHONDONTWRITEBYTECODE=1
  "$CRAWL4AI_PYTHON" "$SKILL_DIR/scripts/crawl-site.py" "$REPO_ROOT" --self-test
  "$CRAWL4AI_PYTHON" "$SKILL_DIR/scripts/academy-video.py" --self-test
  python3 "$CRAWL_SCRIPTS_DIR/verify-mirror.py" --self-test
  python3 "$SKILL_DIR/scripts/add-pdf-text-layer.py" --self-test
  python3 "$SKILL_DIR/scripts/verify-publish.py" --self-test
  echo "self-test ok"
  exit 0
fi

if [ ! -x "$CRAWL4AI_PYTHON" ]; then
  echo "crawl4ai Python is not executable: $CRAWL4AI_PYTHON" >&2
  exit 1
fi

for file in \
  crawl-mirror.py \
  youtube-channels.py \
  extract-images.py \
  split-markdown.py \
  transcribe-ids.sh \
  youtube-transcripts.sh \
  inline-transcripts.py \
  render-video-refs.py \
  pdf-mirror.py \
  verify-mirror.py; do
  require_file "$CRAWL_SCRIPTS_DIR/$file"
done
require_file "$YOUTUBE_DIGEST_SCRIPTS_DIR/extract_transcript.sh"
require_file "$YOUTUBE_DIGEST_SCRIPTS_DIR/srt-to-md.sh"
require_file "$HOME/.crawl4ai/academy_state.json"
require_file "$HOME/.crawl4ai/skilljar-anthropic-partners.skilljar.com.json"

if ! command -v yt-dlp >/dev/null; then
  echo "Missing required command: yt-dlp" >&2
  exit 1
fi

for command in ocrmypdf pdftotext; do
  if ! command -v "$command" >/dev/null; then
    echo "Missing required command: $command" >&2
    exit 1
  fi
done

if ! "$CRAWL4AI_PYTHON" -c 'import bs4, curl_cffi, httpx, markdownify, playwright' 2>/dev/null; then
  echo "crawl4ai Python is missing required packages: bs4, curl_cffi, httpx, markdownify, or playwright" >&2
  exit 1
fi

export CRAWL_SCRIPTS_DIR YOUTUBE_DIGEST_SCRIPTS_DIR

if [ "${CHECK_ONLY:-0}" = 1 ]; then
  PYTHONDONTWRITEBYTECODE=1 python3 "$SKILL_DIR/scripts/add-pdf-text-layer.py" "$REPO_ROOT" --check
  # 세션 파일이 있어도 만료됐을 수 있다. 실제 /accounts/ 착지로 확인한다(만료면 exit 3).
  "$CRAWL4AI_PYTHON" "$SKILL_DIR/scripts/academy-video.py" "$REPO_ROOT" --check-auth
  SKILLJAR_BASE=https://anthropic-partners.skilljar.com \
    "$CRAWL4AI_PYTHON" "$SKILL_DIR/scripts/academy-video.py" "$REPO_ROOT" --check-auth
  echo "OK: repository $REPO_ROOT"
  echo "OK: skill $SKILL_DIR"
  echo "OK: crawl4ai Python $CRAWL4AI_PYTHON"
  echo "OK: shared crawl scripts $CRAWL_SCRIPTS_DIR"
  echo "OK: Academy session $HOME/.crawl4ai/academy_state.json"
  exit 0
fi

cd "$REPO_ROOT"
"$CRAWL4AI_PYTHON" "$SKILL_DIR/scripts/crawl-site.py" .
# Academy 실패(세션 만료 3, 등록 필요 4, 무진행 5, 중복 본문 6)는 레슨을 쓰지 않고 기록만 남긴다.
# 공개 표면 갱신은 계속하되 마지막에 non-zero로 끝내 성공으로 보고되지 않게 한다.
# SKILLJAR_EMAIL·SKILLJAR_PASSWORD가 repo 로컬 .env(gitignored)에 있으면 agents-env로 주입해 세션 만료 시 자동 재로그인한다.
skilljar_env=()
if command -v agents-env >/dev/null 2>&1 && agents-env ls --local 2>/dev/null | grep -q '^SKILLJAR_PASSWORD\b'; then
  skilljar_env=(agents-env run --local SKILLJAR_EMAIL SKILLJAR_PASSWORD --)
fi
academy_rc=0
${skilljar_env[@]+"${skilljar_env[@]}"} "$CRAWL4AI_PYTHON" "$SKILL_DIR/scripts/academy-video.py" . || academy_rc=$?
partner_rc=0
SKILLJAR_BASE=https://anthropic-partners.skilljar.com \
SKILLJAR_SKIP_HOST=anthropic.skilljar.com \
  "$CRAWL4AI_PYTHON" "$SKILL_DIR/scripts/academy-video.py" . || partner_rc=$?
python3 "$CRAWL_SCRIPTS_DIR/youtube-channels.py" . \
  anthropic-ai:UCrDwWp7EBBv4NwvScIpBDOA \
  claude:UCV03SRZXJEz-hchIAogeJOg \
  --tabs=videos,shorts,streams
python3 "$CRAWL_SCRIPTS_DIR/extract-images.py" .
python3 "$CRAWL_SCRIPTS_DIR/split-markdown.py" .
bash "$CRAWL_SCRIPTS_DIR/youtube-transcripts.sh" . \
  --exclude '*.skilljar.com/**' \
  --exclude 'platform.claude.com/**' \
  --exclude 'code.claude.com/**'
python3 "$CRAWL_SCRIPTS_DIR/inline-transcripts.py" .
python3 "$CRAWL_SCRIPTS_DIR/render-video-refs.py" .
python3 "$CRAWL_SCRIPTS_DIR/pdf-mirror.py" . --host anthropic.com --host claude.com
PYTHONDONTWRITEBYTECODE=1 python3 "$SKILL_DIR/scripts/add-pdf-text-layer.py" .
python3 "$CRAWL_SCRIPTS_DIR/verify-mirror.py" . \
  --exclude '*.skilljar.com/**' \
  --exclude 'platform.claude.com/**' \
  --exclude 'code.claude.com/**'
python3 "$SKILL_DIR/scripts/verify-publish.py" .
coverage_rc=0
"$CRAWL4AI_PYTHON" "$SKILL_DIR/scripts/coverage-audit.py" . || coverage_rc=$?
python3 "$SKILL_DIR/scripts/verify-publish.py" . --all

if [ "$academy_rc" != 0 ] || [ "$partner_rc" != 0 ] || [ "$coverage_rc" != 0 ]; then
  echo "Mirror refresh incomplete: academy=$academy_rc partner=$partner_rc coverage=$coverage_rc." >&2
  echo "See .anthropic-mirror-status.json and .anthropic-mirror-audit/coverage.md for exact URLs and retry targets." >&2
  exit 3
fi
echo "Mirror refresh and verification completed. Inspect git status before staging."
