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

SKILL_DIR=$(cd "$(dirname "$0")/.." && pwd)
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
  "$SKILL_DIR/scripts/crawl-site.py" \
  "$SKILL_DIR/scripts/academy-video.py" \
  "$SKILL_DIR/scripts/verify-publish.py"; do
  require_file "$file"
done

if [ "${SELF_TEST:-0}" = 1 ]; then
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

if ! command -v yt-dlp >/dev/null; then
  echo "Missing required command: yt-dlp" >&2
  exit 1
fi

if ! "$CRAWL4AI_PYTHON" -c 'import bs4, curl_cffi, httpx, markdownify, playwright' 2>/dev/null; then
  echo "crawl4ai Python is missing required packages: bs4, curl_cffi, httpx, markdownify, or playwright" >&2
  exit 1
fi

export CRAWL_SCRIPTS_DIR YOUTUBE_DIGEST_SCRIPTS_DIR

if [ "${CHECK_ONLY:-0}" = 1 ]; then
  echo "OK: repository $REPO_ROOT"
  echo "OK: skill $SKILL_DIR"
  echo "OK: crawl4ai Python $CRAWL4AI_PYTHON"
  echo "OK: shared crawl scripts $CRAWL_SCRIPTS_DIR"
  echo "OK: Academy session $HOME/.crawl4ai/academy_state.json"
  exit 0
fi

cd "$REPO_ROOT"
"$CRAWL4AI_PYTHON" "$SKILL_DIR/scripts/crawl-site.py" .
"$CRAWL4AI_PYTHON" "$SKILL_DIR/scripts/academy-video.py" .
python3 "$CRAWL_SCRIPTS_DIR/youtube-channels.py" . \
  anthropic-ai:UCrDwWp7EBBv4NwvScIpBDOA \
  claude:UCV03SRZXJEz-hchIAogeJOg
python3 "$CRAWL_SCRIPTS_DIR/extract-images.py" .
bash "$CRAWL_SCRIPTS_DIR/youtube-transcripts.sh" . \
  --exclude '*.skilljar.com/**' \
  --exclude 'platform.claude.com/**' \
  --exclude 'code.claude.com/**'
python3 "$CRAWL_SCRIPTS_DIR/inline-transcripts.py" .
python3 "$CRAWL_SCRIPTS_DIR/render-video-refs.py" .
python3 "$CRAWL_SCRIPTS_DIR/pdf-mirror.py" . --host anthropic.com --host claude.com
python3 "$CRAWL_SCRIPTS_DIR/verify-mirror.py" . \
  --exclude '*.skilljar.com/**' \
  --exclude 'platform.claude.com/**' \
  --exclude 'code.claude.com/**'
python3 "$SKILL_DIR/scripts/verify-publish.py" .

echo "Mirror refresh and verification completed. Inspect git status before staging."
