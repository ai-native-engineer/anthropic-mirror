---
name: anthropic-mirror
description: "이 repo의 Anthropic/Claude 공개 표면 커버리지와 누락을 전수 감사하거나, 미러를 증분 갱신·재수집하고 생성물을 검증해 로컬 커밋한다. 공개 사이트, 개발자 문서, Academy, 공식 YouTube, 이미지·자막·PDF를 다룬다. Use when 'Anthropic 미러 전체 누락 조사', '커버리지 감사', '미러 갱신/재생성', '누락 페이지 복구', 'Academy/YouTube/PDF 재수집', 'anthropic-mirror'를 요청할 때. Do NOT use for Claude 제품 질문, 저장된 미러 검색, 단일 URL 크롤, OpenAI 미러."
---

# Anthropic Mirror

이 repo의 생성기와 발행 절차다. 생성물은 직접 수정하지 않고 수집기를 고쳐 다시 생성한다.

## 작업 라우팅

| 작업 | 먼저 읽을 것 |
|---|---|
| 전체 커버리지·누락 감사 | `references/coverage-audit.md` |
| 전체 갱신, 검증, commit, push | `references/publishing.md` |
| 부분 수집, 누락 복구, 수집기 수정 | `references/crawl-notes.md`와 대상 스크립트의 `--help` |
| Academy 로그인, 본문·영상 추출 | `references/academy-notes.md` |

일반 갱신은 `publishing.md`의 로컬 commit까지 완료한다. public push와 삭제 반영은 그 문서의 승인 게이트를 따른다.

## 불변 규칙

- 최신 상태만 제자리 갱신하고 이력은 git에 둔다.
- `_yt-cache/`와 `.anthropic-mirror-state.json`은 gitignored 작업 상태이며 발행하지 않는다.
- 모든 source와 Academy 레슨을 검사하되 정제된 본문이나 영상 ID가 달라진 파일만 쓴다.
- 외부 인용 PDF는 제외하고 Anthropic·Claude 소유 PDF만 원본으로 미러한다.
