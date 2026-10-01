# 공개 표면 커버리지 감사

미러가 이미 아는 URL만 검사하면 새 호스트·허브·탭을 놓친다. 전수 감사는 live 발견 집합, 수집기 집합, 로컬 생성물 집합을 독립적으로 만든 뒤 대조한다. 집합 계산과 분류는 `scripts/coverage-audit.py`가 결정론으로 수행하고, 사람과 AI는 그 결과의 차단 분류를 해소한다.

## 목차

- 감사 모드
- 실행
- 세 집합
- 분류
- 표면별 규칙
- 새 호스트 처리
- 종료 조건과 보고

## 감사 모드

- 감사는 생성물과 git index를 바꾸지 않는다. 결과와 live 응답 캐시만 `.anthropic-mirror-audit/`에 쓴다.
- 시작할 때 `git status --short`, `git diff --cached --name-only`, `git worktree list`를 기록해 다른 작업의 경계를 남긴다.
- 기존 dirty 파일과 잠긴 작업트리는 읽기 전용 증거로만 쓰고 현재 감사 결과와 섞지 않는다.
- 이전 보고서의 숫자는 발견 힌트일 뿐이다. 현재 URL, 개수, 응답은 live로 다시 확인한다.

## 실행

repo root에서 crawl4ai 인터프리터로 실행한다(`curl_cffi`와 Playwright가 필요하다).

```bash
PY=~/.local/share/uv/tools/crawl4ai/bin/python
$PY .agents/skills/anthropic-mirror/scripts/coverage-audit.py .           # 페이지·YouTube·Academy·PDF
$PY .agents/skills/anthropic-mirror/scripts/coverage-audit.py . --assets  # 원격 이미지 렌더 가능 여부까지
```

- 결과는 `.anthropic-mirror-audit/coverage.json`(기계용 항목 전체)과 `coverage.md`(표면별 표와 차단 항목)다.
- 종료 코드는 0(미분류·차단 분류 없음), 1(미분류 있음), 3(차단 분류 있음)이다.
- live 응답은 `--cache-hours`(기본 12) 동안 재사용한다. 원본이 바뀌었다고 의심되면 `live-cache.json`을 지우고 다시 돈다.

## 세 집합

1. `D`(discovered): 각 host의 robots.txt가 선언한 sitemap과 `/sitemap.xml`을 중첩 sitemap index까지 재귀로 펼친 URL, host 홈의 same-host 링크(SPA는 렌더), 보관본 전체의 공식 host outbound 링크, YouTube 채널 탭, Academy 인증 카탈로그의 lesson URL.
2. `C`(crawler): `crawl-site.py --plan-json`이 계획한 URL, `academy-video.py --list-json`의 lesson URL, 채널 탭 ID, `pdf-mirror.py`가 받을 PDF.
3. `M`(mirrored): 생성물 첫 줄의 source 주석, Academy source URL, YouTube frontmatter `youtube_id`, PDF 파일 경로.

집합 비교는 `mirror-common.py`의 `norm_url`(https, 소문자 host, fragment·query·끝 슬래시·`index.html` 제거)로 한다.

- `D - C`: 수집기가 모르는 구조적 blind spot이다.
- `C - M`: 다음 refresh 대기, 추출 실패, thin shell, 인증 실패 중 하나다. 수집기와 같은 fetch 함수로 다시 받아 판정한다.
- `M - D`: sitemap 축소, canonical redirect, 삭제·비공개 전환, 기존 URL 동결 중 하나다.

## 분류

모든 후보를 아래 중 하나로만 분류한다. 정본은 `mirror-common.py`의 `CLASSES`다.

- `structural_missing`: 발견 경로 자체가 수집기에 없다(robots가 선언했지만 설정에 없는 sitemap 포함).
- `refresh_pending`: 수집기는 알지만 아직 로컬에 반영되지 않았거나 403·5xx·timeout으로 재시도가 필요하다.
- `extract_failed`: live 본문이 있는데 저장·정제·후처리가 실패했다(thin, 같은 코스 레슨과 동일한 본문).
- `stale_or_redirect`: 404·410이거나 다른 canonical URL로 이동했다.
- `auth_blocked`: 로그인 세션, 등록, 권한이 있어야 본문을 볼 수 있다.
- `scope_decision`: 공개이지만 미러 목적 포함 여부가 정해지지 않았다(상태 페이지, 발견 경로 밖에 남은 live 페이지).
- `intentional_exclusion`: 다국어 사본, robots Disallow, 외부 호스트, 서비스 endpoint처럼 규칙상 제외다.

`structural_missing`, `refresh_pending`, `extract_failed`, `auth_blocked`는 차단 분류다. 분류가 됐어도 전수 감사 완료를 막는다.

## 표면별 규칙

- sitemap이 없는 연구 사이트(alignment, transformer-circuits)는 홈 BFS와 보관본 deep link를 합쳐 `D`로 쓴다.
- `platform.claude.com`은 docs sitemap과 cookbook sitemap을 따로 선언한다. robots.txt의 모든 sitemap이 수집기 설정에 있어야 한다.
- SPA host(trust 등)는 홈을 렌더해 route를 모은다. 정적 HTML의 링크가 적으면 감사기가 자동으로 렌더한다.
- Claude·Anthropic Help/Privacy Center와 docs는 영어 정본만 센다. 다른 언어는 `intentional_exclusion`이다.
- YouTube는 `videos`, `shorts`, `streams` 탭 ID의 합집합과 로컬 `youtube_id`를 비교한다. 차이는 oEmbed 응답으로 비공개·삭제·공개를 가른다.
- Academy는 인스턴스마다 인증 카탈로그를 받는다. 세션이 없으면 그 인스턴스의 모든 로컬 레슨을 `auth_blocked`로 남긴다(대조 불가를 누락 없음으로 바꾸지 않는다).
- 등록·권한 stub 레슨은 차집합과 별도로 `M(state)` 집합에 `auth_blocked`로 남는다.
- PDF는 Anthropic·Claude 소유 host만 센다. 100MB 초과는 `intentional_exclusion`이다.
- `--assets`는 보관본의 원격 이미지 URL 전체를 live로 확인한다. 로컬 이미지·빈 참조·attachment는 `verify-publish.py --all`이 검사한다.

## 새 호스트 처리

1. 보관본 링크와 홈 outbound 링크에 나온 공식 도메인 host는 `assets/mirror-manifest.json`의 `archive_roots`나 `host_decisions`에 없으면 자동으로 `structural_missing` 후보가 된다.
2. 루트가 이미 수집하는 host로 리다이렉트하면 별칭이므로 `stale_or_redirect`로 분류한다.
3. 공개 본문이 있는 새 host는 수집기(`crawl-site.py`의 sitemap·BFS·`LINKED_HOSTS`)와 manifest `archive_roots`를 함께 고친 뒤 그 host만 재생성한다.
4. 수집하지 않기로 한 host는 이유와 함께 manifest `host_decisions`에 판정을 적는다.
5. host 안의 일부 경로(앱 route, 입력 폼, 개인 화면, 목록 hub)는 `path_decisions`에 `host/path` 글롭과 판정을 적는다. 순서대로 보고 첫 매칭에서 멈추며, class가 `null`이면 수집 대상이라는 명시다.
6. 판정은 개별 URL 목록이 아니라 경로 패턴 단위의 영속 사실만 적는다. 수집기도 같은 판정을 읽어 해당 URL을 받지 않는다.

## 종료 조건과 보고

`미분류 0`, 차단 분류 0, 각 표면에서 `발견 수 = 미러 수 + 분류된 예외 수`일 때만 전수 감사를 완료로 보고한다. 차단 분류가 남으면 완료라고 쓰지 않고 URL, 이유, 재시도 명령, 현재 로컬 상태를 보고한다.

`coverage.md`의 표를 그대로 쓴다.

| 표면 | D | C | M | D-C | C-M | M-D | 분류 |
|---|---:|---:|---:|---:|---:|---:|---|

마지막에 `확정 누락`, `갱신 지연`, `인증·범위 결정`, `문제 없음`을 분리하고, 감사 중 변경한 생성물이 없음을 명시한다.
