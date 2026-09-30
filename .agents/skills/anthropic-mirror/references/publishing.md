# 갱신과 발행

미러 갱신, 검증, commit, push 절차의 정본이다.

## 갱신

repo root에서 실행한다.

```bash
bash .agents/skills/anthropic-mirror/scripts/refresh.sh --check
bash .agents/skills/anthropic-mirror/scripts/refresh.sh
```

- `--check`는 도구, PDF text layer, 두 Academy 세션의 실제 로그인 여부를 확인한다. 세션이 만료되면 exit 3이다.
- entrypoint는 공개 사이트, Academy, 공식 YouTube, 이미지·인라인 자막·영상 reference·PDF를 갱신하고 coverage 감사와 전체 검증까지 실행한다.
- Academy 단계가 실패해도(세션 만료 3, 등록 필요 4, 무진행 5, 중복 본문 6) 레슨은 쓰지 않고 다른 표면 갱신은 계속한다. 대신 마지막에 exit 3으로 끝난다.
- coverage 감사에 미분류나 차단 분류가 남아도 exit 3이다. 다른 단계의 실패는 그 자리에서 멈춘다.
- exit 0이 아니면 갱신을 완료로 보고하지 않는다. `.anthropic-mirror-status.json`과 `.anthropic-mirror-audit/coverage.md`의 URL, 이유, 재시도 명령을 보고한다.
- Academy 세션 만료는 사람이 `login-academy.py`로 다시 로그인해야 풀린다(`academy-notes.md`). 그 뒤 Academy 단계와 검증만 다시 실행할 수 있다.

## 전체 보관본 검증

변경분 검증은 이번 실행이 건드린 파일만 본다. 기존 파일의 결함과 새 host는 `--all`로만 드러난다.

```bash
python3 .agents/skills/anthropic-mirror/scripts/verify-publish.py . --all
```

- 추적 파일과 ignore되지 않은 미추적 생성물 전체를 검사한다.
- 최상위 항목이 manifest `archive_roots`에 없으면 문제로, 파일 없는 디렉터리는 경고로 드러난다.
- 파일별로 source 헤더와 경로 일치, 본문 길이, 빈·로컬 이미지 참조, 미해결 attachment, PNG·JPEG·PDF의 형식과 잘림, PDF text layer(`pdftotext`, OCR marker)를 본다.
- shared `verify-mirror.py`의 자막 누락, 1MiB 초과, 깨진 로컬 참조를 합친다.
- 마지막 coverage 감사 결과를 읽어 미분류를 문제로, 차단 분류를 상태로 보인다.
- 결과는 `.anthropic-mirror-audit/publish-all.json`(전체 목록)과 `publish-all.md`(종류별 표)다. 문제가 하나라도 있으면 exit 1이다.
- `auth_blocked` stub, `[미수집 이미지: ...]`, 짧은 본문은 상태로 집계된다. 문제 수 0이어도 상태에 차단 분류가 있으면 완료가 아니다.

## 검토와 commit

1. 실행 전후 `git status --short`와 `git diff --stat`을 비교한다.
2. 변경된 생성물에 worktree 발행 검증을 실행한다.
3. 실제 갱신된 domain만 `git add -A -- <domain-root>...`로 stage한다.
4. staged 발행 검증과 통계를 확인한다.
5. diff가 있으면 그 회차의 변경 영역을 설명하는 commit 하나를 만든다.

```bash
python3 .agents/skills/anthropic-mirror/scripts/verify-publish.py .
python3 .agents/skills/anthropic-mirror/scripts/verify-publish.py . --staged
git diff --cached --check
git diff --cached --stat
git commit -m "Update mirror: <changed area> (YYYY-MM-DD)"
```

`README.md`, `README.ko.md`, `AGENTS.md`, `.agents/`, `.gitignore` 같은 source 변경은 생성물 갱신 commit과 분리한다. 생성물 diff가 없으면 빈 commit을 만들지 않는다.

## push와 완료 확인

이 스킬로 일반 갱신·재생성을 요청한 것은 현재 branch의 검증된 미전송 미러 관련 commit을 public repo에 push하는 승인까지 포함한다. 별도 확인을 위해 중단하지 않는다.

1. `git log --oneline @{upstream}..HEAD`와 `git diff --stat @{upstream}..HEAD`로 전송될 전체 범위를 확인한다.
2. 미러 갱신 관련 commit만 있으면 `git push`한다. 새 diff가 없어도 검증된 미전송 commit이 있으면 push한다.
3. `git rev-parse HEAD`와 `git rev-parse @{upstream}`이 같은지 확인한 뒤 완료를 보고한다.

예상 밖 commit, 불명확한 upstream, 검증 실패가 있으면 push하지 않고 정확한 범위를 보고한다. force push는 사용하지 않는다.

## 삭제 반영

갱신은 원본에서 사라진 페이지를 자동 삭제하지 않는다. 삭제를 반영할 때는 삭제 목록을 먼저 검토하고 다음 두 검증에만 `--allow-deletes`를 붙인다.

```bash
python3 .agents/skills/anthropic-mirror/scripts/verify-publish.py . --allow-deletes
python3 .agents/skills/anthropic-mirror/scripts/verify-publish.py . --staged --allow-deletes
```

예상하지 않은 rename/copy, 100MB 초과 파일, source metadata 누락, 허용 도메인 밖 변경은 발행하지 않는다.
