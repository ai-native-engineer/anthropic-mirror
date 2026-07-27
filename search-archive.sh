#!/usr/bin/env bash

set -u

if [[ $# -ne 1 || -z "$1" ]]; then
  echo "Usage: $0 '<term|synonym>'" >&2
  exit 2
fi

for dep in rg pdftotext; do
  command -v "$dep" >/dev/null 2>&1 || {
    echo "Missing dependency: $dep" >&2
    exit 2
  }
done

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd "$repo_root"

query=$1
found=0

if rg -i -n -C 2 --glob '*.md' -- "$query" .; then
  found=1
else
  status=$?
  [[ $status -eq 1 ]] || exit "$status"
fi

while IFS= read -r -d '' pdf; do
  while IFS= read -r hit; do
    printf '%s:%s\n' "$pdf" "$hit"
    found=1
  done < <(pdftotext "$pdf" - 2>/dev/null | rg -i -n -- "$query" -)
done < <(rg --files -g '*.pdf' -0)

[[ $found -eq 1 ]]
