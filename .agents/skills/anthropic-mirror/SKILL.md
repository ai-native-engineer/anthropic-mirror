---
name: anthropic-mirror
description: "Anthropic/Claude 공개 자료 미러를 이 repository에서 갱신, 검증, 커밋한다. 공개 사이트와 개발자 문서, Anthropic Academy, 공식 YouTube 채널, 인라인 이미지/자막, 링크된 PDF를 최신 상태로 동기화한다. Use when 사용자가 'anthropic-mirror', 'Anthropic 미러 갱신', 'Claude 자료 수집', 'Anthropic Academy 추출', 'Anthropic 전체 크롤'을 말할 때. Do NOT use for 미러 내용 검색만 하는 질문, 일반 웹 크롤, OpenAI 자료 수집."
---

# Anthropic Mirror

이 repository의 생성 파이프라인을 운영한다. 도메인 디렉터리는 생성물이다. 본문을 손으로 고치지 말고 이 스킬의 스크립트를 고친 뒤 다시 생성한다.

## 기본 계약

- 기본 갱신은 공개 페이지, Academy 본문/영상, 공식 YouTube 채널, 이미지/자막/PDF 후처리, 검증을 모두 실행한다.
- 모든 source URL과 레슨을 검사하되 정제된 본문과 영상 ID가 달라진 파일만 쓴다.
- 사용자가 만든 기존 변경을 보존하고, 생성물과 스킬 변경만 선택해 stage한다.
- `git push`는 public 발행이다. 로컬 commit과 diff 요약까지 만든 뒤 명시 승인을 받아 실행한다.

## 실행

1. `git status --short`로 기존 변경을 기록한다.
2. `bash .agents/skills/anthropic-mirror/scripts/update-mirror.sh --check`로 런타임과 공용 도구를 확인한다.
3. `bash .agents/skills/anthropic-mirror/scripts/update-mirror.sh`를 실행한다.
4. 검증이 통과하면 변경 범위를 확인하고 관련 도메인만 stage/commit한다. `git add .`와 `git add -A`는 쓰지 않는다.

`--check`가 Academy 세션 누락/만료를 지적하면 `references/academy-notes.md`의 로그인 절차를 실행한 뒤 다시 확인한다. wrapper는 crawl/후처리/검증까지만 수행하며 commit과 push는 하지 않는다.

## 작업별 reference

| 작업 | 먼저 읽을 파일 |
|---|---|
| 공개 사이트 대상, 부분 크롤, 수집 함정 | `references/news-sources.md` |
| Academy 로그인, 본문/영상 추출, Skilljar 함정 | `references/academy-notes.md` |
| 전체 갱신 결과 확인, commit, push | `references/publishing.md` |

## 완료 조건

- `verify-mirror.py`가 자막 누락과 1MB 초과 Markdown 없이 종료한다.
- 채널의 열거 영상 수와 발행 수가 일치한다.
- 관련 변경만 commit에 포함되고 기존 unrelated 변경은 그대로 남는다.
- push 전에는 변경 통계와 commit을 사용자에게 보고한다.
