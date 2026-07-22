---
name: anthropic-mirror
description: "이 저장소의 Anthropic/Claude 공개 자료 미러를 전체·부분 갱신, 검증, 커밋한다. Use when 공개 사이트, 개발자 문서, Academy, 공식 YouTube, 이미지·자막·PDF를 동기화할 때. Do NOT use for 미러 내용 검색, 일반 웹 크롤, OpenAI 자료 수집."
---

# Anthropic Mirror

이 저장소의 생성 파이프라인을 운영한다. 도메인 디렉터리는 생성물이므로 직접 수정하거나 파일을 추가하지 않는다. 문제가 있으면 이 스킬의 스크립트를 고치고 다시 생성한다.

## 실행

1. `git status --short`로 기존 변경을 기록한다.
2. `bash .agents/skills/anthropic-mirror/scripts/update-mirror.sh --check`로 런타임과 공용 도구를 확인한다.
3. `bash .agents/skills/anthropic-mirror/scripts/update-mirror.sh`를 실행한다.
4. `references/publishing.md`를 읽고 실제 갱신된 경로만 stage·commit한다.

기본 실행은 전체 갱신이다. `--check`가 Academy 세션 문제를 보고하면 `references/academy-notes.md`의 로그인 절차를 따른다. wrapper는 commit과 push를 하지 않으며, push는 commit과 변경 통계를 보고한 뒤 명시 승인을 받아 실행한다.

## 작업별 reference

| 작업 | 먼저 읽을 파일 |
|---|---|
| 공개 사이트 대상, 부분 크롤, 수집 함정 | `references/news-sources.md` |
| Academy 로그인, 본문/영상 추출, Skilljar 함정 | `references/academy-notes.md` |
| 전체 갱신 결과 확인, commit, push | `references/publishing.md` |

## 완료 조건

- wrapper와 `references/publishing.md`의 결과 확인이 모두 통과한다.
- 기존 unrelated 변경은 그대로 남고 실제 갱신된 경로만 commit에 포함된다.
