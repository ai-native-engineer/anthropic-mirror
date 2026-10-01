# 수집기 구조와 함정

부분 수집, 누락 복구, 생성기 수정에 필요한 비자명한 동작을 정리한다. 전체 갱신은 `scripts/refresh.sh`를 실행한다.

## 목차

- 실행 환경과 스크립트 경로
- 커버리지
- 공개 사이트와 문서
- 미해결 상태 기록
- 증분 상태
- Academy 인증 실패 조건
- 후처리
- 범위 밖

## 실행 환경과 스크립트 경로

아래 경로는 repo root 기준이다. `S=.agents/skills/anthropic-mirror/scripts`, `CRAWL=~/.agents/skills/shared/crawl/scripts`, `PY=~/.local/share/uv/tools/crawl4ai/bin/python`로 둔다.

| 스크립트 | 인터프리터 | 역할 |
|---|---|---|
| `$S/refresh.sh` | bash | 전체 갱신·검증 진입점. `--check`는 도구·세션, `--self-test`는 스크립트 self-test |
| `$S/crawl-site.py` | `$PY` | 공개 사이트·docs 수집, `--plan-json`으로 수집 대상 집합 출력 |
| `$S/academy-video.py` | `$PY` | Skilljar 레슨 본문·영상 자막, `--check-auth`, `--list-json` |
| `$S/academy-extract.py` | `$PY` | 영상 검사 없는 부분 본문 점검 |
| `$S/login-academy.py` | `$PY` | 사람이 하는 헤드풀 로그인과 쿠키 저장 |
| `$S/coverage-audit.py` | `$PY` | D/C/M 전수 감사 |
| `$S/verify-publish.py` | `python3` | 변경분·staged·전체(`--all`) 발행 검증 |
| `$S/add-pdf-text-layer.py` | `python3` | PDF OCR text layer, `--check` |
| `$S/mirror-common.py` | import 전용 | manifest, URL 정규화, 상태 기록, 분류 상수 |
| `$CRAWL/verify-mirror.py` | `python3` | 자막 누락, 1MiB 초과, 빈 이미지, 깨진 로컬 참조 |
| `$CRAWL/youtube-channels.py`, `pdf-mirror.py`, `extract-images.py`, `split-markdown.py`, `render-video-refs.py` | `python3` | shared 후처리 |

- 인터프리터는 `CRAWL4AI_PYTHON`, shared crawl 위치는 `CRAWL_SCRIPTS_DIR`, YouTube 도구 위치는 `YOUTUBE_DIGEST_SCRIPTS_DIR`로 바꿀 수 있다.
- 개별 수집기의 옵션은 해당 스크립트의 `--help`를 정본으로 삼는다.

## 커버리지

| 표면 | 수집기 | 발견 방식 |
|---|---|---|
| anthropic.com / claude.com / claude.dev | `crawl-site.py` | sitemap, 영어 정본 |
| platform.claude.com / code.claude.com | `crawl-site.py` | docs sitemap + Mintlify raw Markdown, cookbook sitemap + 홈 1-depth |
| support.claude.com / privacy.claude.com | `crawl-site.py` | 영어 sitemap |
| academy.claude.com | `crawl-site.py` | sitemap, robots Disallow 제외 |
| alignment.anthropic.com / transformer-circuits.pub | `crawl-site.py` | same-host 링크 2-depth + canonical redirect |
| resources.anthropic.com / red.anthropic.com | `crawl-site.py` | 보관 문서의 공식 outbound link |
| trust.anthropic.com | `crawl-site.py` | 공개 SPA route별 렌더 |
| Anthropic Academy(Skilljar) | `academy-video.py` | 인증 카탈로그 + 렌더된 레슨 |
| 공식 YouTube | `$CRAWL/youtube-channels.py` | videos·shorts·streams ID 합집합 + 자막 |
| Anthropic·Claude 소유 PDF | `$CRAWL/pdf-mirror.py` | 허용 호스트의 원본 PDF |
| PDF 내부 image 텍스트 | `add-pdf-text-layer.py` | Apple Vision OCR을 원본 PDF의 투명 text layer로 추가 |

수집 host를 추가하면 `assets/mirror-manifest.json`의 `archive_roots`도 함께 고친다. `crawl-site.py --self-test`가 수집 host 전부가 manifest에 있는지 확인한다.

sitemap·BFS가 빠뜨린 공개 route는 `linked same-host` phase가 채운다. 보관본의 same-host 링크와 각 host 홈의 내비게이션 링크를 host별 keep 규칙(영어 정본, docs 경로 등)으로 거른다. manifest `path_decisions`·`host_decisions`로 판정된 URL은 모든 phase에서 받지 않는다.

## 공개 사이트와 문서

- sitemap을 URL 정본으로 쓰고 중첩된 sitemap index까지 재귀적으로 펼친다.
- robots.txt가 선언했지만 설정에 없는 sitemap은 매 실행 `structural_missing`으로 기록된다. 발견하면 `HTML_SITEMAPS`나 `DOCS_SITEMAPS`에 추가한다.
- `curl_cffi`의 Chrome 지문으로 SSR 본문을 받고 nav/footer boilerplate를 제거한다.
- platform·code의 `/docs/` 경로는 docs phase가 페이지별 raw Markdown으로만 받고 영어 정본만 남긴다. cookbook 탐색이나 linked phase가 같은 URL을 HTML로 받으면 쿠키 배너와 사이드바가 본문이 되고 먼저 저장한 Markdown을 덮어쓴다.
- 다른 host나 HTML 경로가 docs 경로로 리다이렉트하면(예: 옛 문서 링크) HTML 추출본을 저장하지 않고 `stale_or_redirect`로 남긴다. 저장하면 docs phase가 받은 파일을 덮어쓴다.
- `.md` 엔드포인트가 frontmatter나 H1으로 시작하지 않는 응답(HTML 셸, 쿠키 배너부터 시작하는 변환 페이지)을 주면 저장하지 않고 `refresh_pending`으로 남긴다.
- 반복 줄 제거(boilerplate)는 host마다 첫 묶음(sitemap·discover phase)에서 페이지 40% 이상에 반복되는 줄로 정하고 `.anthropic-mirror-state.json`의 `boilerplate:<host>`에 저장한다. linked phase와 `--url-file` 재시도는 그 판정을 재사용한다. 작은 묶음으로 새로 계산하면 논문 머리말(Authors, Published)이나 전사 모음의 공통 제목 같은 본문이 nav로 지워지고, 실행마다 결과가 흔들린다. 코드 펜스, 구분선, 표 구분자 같은 Markdown 구문 줄은 반복돼도 지우지 않는다.
- 대형 페이지 응답이 중간에 끊겨 인라인 base64 PNG가 IEND 없이 잘리면 저장하지 않고 `refresh_pending`으로 남긴다. 기존 파일이 온전한 그림을 지킨다.
- root-relative 링크와 확장자 있는 상대 링크는 원본 페이지 기준 절대 URL로 바꾼다. 미러 안에서는 해석되지 않는 경로이기 때문이다.
- 빈 `src` 이미지는 `data-src` 계열 lazy 속성에서 복원하고, 없으면 대체 텍스트로 `[미수집 이미지: ...]`를 남긴다. Jupyter `attachment:`는 `[미수집 첨부 이미지: ...]`가 된다.
- claude.com과 support는 영어 정본만 저장한다.
- trust.anthropic.com만 SPA라 Playwright 렌더를 사용한다.
- 한 host만 점검할 때는 `crawl-site.py . --only <host>`를 쓴다.
- 확정 누락이나 깨진 페이지만 복구할 때는 줄 단위 목록과 `--url-file <file> --force`를 쓴다.
- HTML 페이지가 PDF로 리다이렉트하면 파싱하지 않고 `PDF로 리다이렉트 -> <pdf>`로 기록한다. 대형 PDF를 HTML로 파싱하면 재귀 한도를 넘는다.
- crawl-site가 수집하지 않는 host(제품 앱, Skilljar)나 manifest 판정 URL로 리다이렉트된 본문은 저장하지 않고 `stale_or_redirect`로 남긴다. 저장하면 로그인 화면이나 비로그인 코스 랜딩이 원래 URL의 본문처럼 보관된다.
- 정제 본문이 200자 미만이면 이유를 가른다. JS 리다이렉트 셸은 `stale_or_redirect`, `<main>`이 SSR에서 빈 셸은 Playwright로 렌더해 다시 추출, 본문 영역 자체가 없는 JS 전용 페이지는 `intentional_exclusion`, 제목이 있고 100자 이상인 짧은 페이지는 정상 저장, 나머지는 `extract_failed`다.
- `--prune-stale`은 live 404·redirect가 확정된 source 파일을 지운다. 삭제는 publishing.md의 승인 게이트를 거친 뒤에만 쓴다.

## 미해결 상태 기록

- 저장하지 않은 URL은 `.anthropic-mirror-status.json`의 `crawl-site:<host>` key에 분류와 이유로 남는다.
- HTTP 분류는 `mirror-common.classify_http`, 본문 부족 분류는 `crawl-site.unresolved`가 정본이다. 404·410과 redirect는 `stale_or_redirect`, 401과 login wall은 `auth_blocked`, 403·5xx·timeout은 `refresh_pending`이다.
- 같은 host를 다시 돌리면 그 host의 기록이 교체된다. `--url-file` 실행은 고른 URL의 기록만 바꾼다.

## 증분 상태

- 모든 source를 다시 확인하고 정제 본문의 SHA-256을 `.anthropic-mirror-state.json`과 비교한다.
- 첫 실행은 기존 archive를 다시 쓰지 않고 live hash를 기준선으로 등록한다.
- `--force`는 본문 hash와 무관하게 검사 결과를 다시 저장한다.
- 정제 규칙(링크·이미지 처리)을 바꾸면 영향받는 페이지의 hash가 달라져 다음 실행에서 자동으로 다시 쓰인다.
- 상태 파일은 로컬 cache이며 commit하지 않는다.

## Academy 인증 실패 조건

- 세션 파일이 없거나 `/accounts/`가 로그인 페이지로 이동하면 `academy-video.py`와 `academy-extract.py`는 레슨을 쓰지 않고 exit 3으로 멈춘다.
- 실행 중 레슨이 다른 URL로 튕기면 세션을 다시 확인한다. 만료면 그 자리에서 exit 3이다. 코스 랜딩을 레슨 본문으로 저장하지 않기 위해서다.
- 세션은 유효한데 레슨만 막히면 등록·권한 문제다. `_(등록 또는 권한이 필요한 레슨)_` stub만 남기고 exit 4로 끝난다.
- 같은 코스의 서로 다른 레슨 본문이 같으면 저장을 거부하고 exit 6으로 끝난다.
- 무진행으로 강제 종료된 코스는 재시도 뒤 exit 5로 끝난다.
- 어느 경우든 `academy:<host>:<course>` key에 URL별 분류가 남는다. 로그인·영상 추출의 세부는 `academy-notes.md`를 따른다.

## 후처리

- `extract-images.py`는 transformer-circuits의 인라인 base64 그림을 옆 `images/`의 PNG/JPG로 분리한다.
- `split-markdown.py`는 1MiB를 넘는 생성 문서를 순서가 보존된 작은 Markdown 조각으로 나눈다.
- `youtube-transcripts.sh`와 `inline-transcripts.py`는 페이지의 YouTube 링크 아래에 자막을 멱등 삽입한다.
- Academy와 docs는 자체 처리 또는 낮은 가치 때문에 wrapper의 인라인 자막 대상에서 제외한다.
- `youtube-channels.py`는 `_yt-cache/`를 재사용하고 `videos`, `shorts`, `streams` 탭의 합집합을 채널별 transcript/stub으로 발행한다.
- `pdf-mirror.py`는 Anthropic·Claude 소유 host만 허용하고 `%PDF-` 및 100MB 제한을 확인한다.
- `add-pdf-text-layer.py`는 PDF의 visible text를 보존하면서 raster image를 다시 OCR하고, PDF metadata marker와 `--check`로 전수 커버리지를 확인한다. `--redo-ocr`가 초대형 raster 페이지에서 실패하면 기존 text layer를 둔 채 image-only 페이지만 OCR하는 `--skip-text`로 한 번 더 시도한다.
- PNG/JPEG 등 bitmap image에는 selectable text layer 규격이 없다. 별도 OCR 파일이나 PDF 변환을 명시적으로 요청하지 않는 한 원본만 보존한다.
- `$CRAWL/verify-mirror.py`는 자막 누락, 1MiB 초과, 빈 이미지, 깨진 로컬 참조, 미해결 attachment를 검사한다. root-relative 링크는 경고로만 센다. 점으로 시작하는 폴더(감사 결과 등 작업 상태)는 검사하지 않는다.

## 범위 밖

- Claude 제품 앱과 인증된 사용자 데이터는 수집하지 않는다.
- 외부 학회·정부·대학·arXiv PDF는 원문 링크만 유지한다.
- sitemap, 홈, 보관 링크 어디에도 없는 페이지는 자동으로 찾을 수 없다. coverage 감사의 `M-D`와 `D-C`가 그 경계를 드러낸다.
