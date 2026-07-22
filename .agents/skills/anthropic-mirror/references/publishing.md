# 갱신과 발행

미러 갱신, 검증, commit, push 절차의 정본이다.

## 갱신

repo root에서 실행한다.

```bash
bash .agents/skills/anthropic-mirror/scripts/refresh.sh --check
bash .agents/skills/anthropic-mirror/scripts/refresh.sh
```

entrypoint는 공개 사이트, Academy, 공식 YouTube, 이미지·인라인 자막·영상 reference·PDF를 갱신하고 콘텐츠와 발행 변경을 검증한다. 중간 단계가 실패하면 즉시 멈춘다.

## 검토와 commit

1. 실행 전후 `git status --short`와 `git diff --stat`을 비교한다.
2. 변경된 생성물에 worktree 발행 검증을 실행한다.
3. 실제 갱신된 domain만 `git add -A -- <domain-root>...`로 stage한다.
4. staged 발행 검증과 통계를 확인한다.
5. diff가 있으면 그 회차의 변경 영역을 설명하는 commit 하나를 만든다.

```bash
python3 .agents/skills/anthropic-mirror/scripts/verify-publish.py .
python3 .agents/skills/anthropic-mirror/scripts/verify-publish.py . --staged
git diff --cached --stat
git commit -m "Update mirror: <changed area> (YYYY-MM-DD)"
```

`README.md`, `README.ko.md`, `AGENTS.md`, `.agents/` 같은 source 변경은 생성물 갱신 commit과 분리한다. 생성물 diff가 없으면 빈 commit을 만들지 않는다.

## push gate

`git push`는 public repo 발행이다. 로컬 commit SHA와 `git diff --stat HEAD~1`을 사용자에게 보여주고 명시 승인을 받은 뒤 push한다.

## 삭제 반영

갱신은 원본에서 사라진 페이지를 자동 삭제하지 않는다. 삭제를 반영할 때는 삭제 목록을 먼저 검토하고 다음 두 검증에만 `--allow-deletes`를 붙인다.

```bash
python3 .agents/skills/anthropic-mirror/scripts/verify-publish.py . --allow-deletes
python3 .agents/skills/anthropic-mirror/scripts/verify-publish.py . --staged --allow-deletes
```

예상하지 않은 rename/copy, 100MB 초과 파일, source metadata 누락, 허용 도메인 밖 변경은 발행하지 않는다.
