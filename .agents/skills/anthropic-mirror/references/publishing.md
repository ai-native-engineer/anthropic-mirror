# 갱신 결과 반영

전체 파이프라인은 repository 루트에서 다음 한 명령으로 실행한다.

```bash
bash .agents/skills/anthropic-mirror/scripts/update-mirror.sh
```

wrapper는 공개 페이지, Academy 전체 코스의 렌더 본문·영상, 공식 YouTube 채널, 이미지/인라인 자막/영상 reference/PDF 후처리, `verify-mirror.py`를 순서대로 실행한다. 중간 단계가 실패하면 즉시 멈추며 commit과 push는 하지 않는다.

## 결과 확인

1. 실행 전 기록한 `git status --short`와 실행 후 상태를 비교한다.
2. `git diff --stat`과 `git diff --name-only`로 변경된 domain을 확인한다.
3. `본문없음 skip`과 PDF의 `SKIP(비-PDF 응답)`은 저장하지 않는 upstream 상태이므로 실패로 재진단하지 않는다.
4. 채널 출력의 열거 영상 수와 발행 수가 같은지 확인한다.
5. `verify-mirror.py`가 exit 0인지 확인한다.

## Commit과 push

- 전체 crawl은 수천 파일을 건드릴 수 있으므로 `git add .`와 `git add -A`를 쓰지 않는다.
- 실행에서 실제로 갱신된 domain/path만 명시해 stage한다.
- commit 전 `git diff --cached --stat`으로 범위를 다시 확인한다.
- commit 메시지는 `Update mirror snapshot (YYYY-MM-DD)`를 쓴다.
- `git push` 전 commit과 변경 통계를 사용자에게 보여주고 명시 승인을 받는다.

이 repository는 최신 snapshot만 덮어쓴다. 날짜별 snapshot directory를 만들지 않으며 이력은 git이 보존한다.
