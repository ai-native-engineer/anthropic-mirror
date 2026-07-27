# 공개 표면 커버리지 감사

미러가 이미 아는 URL만 검사하면 새 호스트·허브·탭을 놓친다. 전체 누락 조사는 live 발견 집합, 수집기 집합, 로컬 생성물 집합을 독립적으로 만든 뒤 대조한다.

## 감사 모드

- 감사 중에는 생성물·상태 파일·git index를 변경하지 않는다.
- 시작할 때 `git status --short`, `git diff --cached --name-only`, `git worktree list`로 다른 작업의 경계를 기록한다.
- 잠긴 작업트리와 기존 dirty 파일은 읽기 전용 증거로만 쓰고 현재 감사 결과와 섞지 않는다.
- 현재 시점의 URL·개수·응답은 live로 다시 확인한다. 이전 보고서의 숫자는 발견 힌트일 뿐이다.

## 세 집합

1. `D`(discovered): 공식 sitemap·robots·허브·내비게이션·공식 문서의 outbound link에서 발견한 live URL.
2. `C`(crawler): 현재 수집기가 실제로 열도록 구성한 URL.
3. `M`(mirrored): source 주석, Academy source URL, YouTube frontmatter로 확인한 로컬 생성물.

다음 차집합을 모두 분류한다.

- `D - C`: 수집기가 모르는 구조적 blind spot.
- `C - M`: 다음 refresh 대기, 추출 실패, thin shell, 인증 실패 중 하나.
- `M - D`: sitemap 축소, canonical redirect, 삭제·비공개 전환, 기존 URL 동결 중 하나.

파일 존재만으로 완료 처리하지 않는다. source URL, canonical 최종 URL, 본문 길이·형식, 링크·미디어 보존까지 확인한다.

## 발견 절차

1. 수집기·wrapper·검증기의 host, sitemap, filter, discovery depth, 제외 규칙을 인벤토리한다.
2. 알려진 공식 host의 `robots.txt`, 모든 선언 sitemap, sitemap index를 끝까지 펼친다.
3. sitemap 밖 landing page·문서 홈·내비게이션을 렌더해 같은 host의 공개 route를 수집한다.
4. 로컬 Markdown 전체의 공식 outbound host와 URL을 집계해 수집기 allowlist 밖 후보를 찾는다.
5. 공식 사이트 제한 검색은 보조 발견 수단으로만 쓰고, 검색 결과 개수를 coverage 분모로 쓰지 않는다.
6. 후보 URL의 status, final URL, content type, 렌더 본문을 확인해 정본·리다이렉트·로그인·폐기 URL을 구분한다.

## 표면별 대조

- `platform.claude.com`은 docs sitemap과 별도 공개 허브를 따로 검사한다. raw Markdown이 없는 route는 HTML 렌더 경로로 분리한다.
- SPA host는 루트 본문만 보지 말고 렌더된 내비게이션의 공개 route별 전문을 비교한다.
- sitemap 없는 연구 사이트는 홈 1-depth와 각 문서의 same-host deep link를 합친다.
- Claude·Anthropic Help/Privacy Center는 언어별 sitemap에서 영어 정본을 따로 센다.
- YouTube 채널은 `videos`, `shorts`, `streams` 탭의 ID 합집합과 로컬 `youtube_id`를 비교한다. 채널 외 embed는 transcript 또는 명시적 no-caption 상태까지 확인한다.
- Academy는 각 Skilljar instance의 루트와 전체 코스 목록을 합친다. 코스별 lesson ID와 로컬 source URL을 비교하고, 미등록·잠금으로 lesson ID가 0인 코스는 누락과 분리한다.
- PDF는 절대·상대 링크를 canonical URL로 만든 뒤 Anthropic·Claude 소유 host만 검사한다. 로컬 파일 존재, `%PDF-`, 크기 제한, stale redirect를 각각 기록한다.
- 이미지·다운로드 링크는 각 파일의 source URL을 기준으로 상대 URL을 절대화해 live 응답과 로컬 렌더를 함께 검사한다. 원문에서는 열리지만 미러에서 가리키는 로컬 파일이 없고 절대 URL로도 재작성되지 않은 참조는 추출 결함이다. `data:` 이미지는 base64와 percent-encoded 형식을 따로 센다.

## 판정과 종료 조건

모든 후보를 아래 중 하나로만 분류한다.

- `structural_missing`: 발견 경로 자체가 수집기에 없다.
- `refresh_pending`: 수집기는 알지만 아직 로컬에 반영되지 않았다.
- `extract_failed`: live 본문이 있는데 저장·정제·후처리가 실패했다.
- `stale_or_redirect`: 삭제됐거나 다른 canonical URL로 이동했다.
- `auth_blocked`: 등록·로그인·권한이 있어야 본문을 볼 수 있다.
- `scope_decision`: 공개이지만 상태 페이지·공식 GitHub·폼처럼 미러 목적 포함 여부가 정해지지 않았다.
- `intentional_exclusion`: 외부 PDF·다국어 사본·사용자 데이터처럼 기존 규칙상 제외다.

`미분류 0`이고 각 표면에서 `발견 수 = 미러 수 + 분류된 예외 수`일 때만 전수 감사를 완료한다. 구조적 누락을 찾은 뒤에는 생성물을 직접 만들지 말고 수집기 수정·재생성 범위를 먼저 제안한다.

## 보고 형식

다음 열을 유지한다.

| 표면 | 발견 | 미러 | 차이 | 판정 | 근거 | 다음 조치 |
|---|---:|---:|---:|---|---|---|

마지막에 `확정 누락`, `갱신 지연`, `인증·범위 결정`, `문제 없음`을 분리하고, 감사 중 변경한 파일이 없음을 명시한다.
