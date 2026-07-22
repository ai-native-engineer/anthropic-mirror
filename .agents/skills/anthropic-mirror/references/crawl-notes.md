# 수집기 구조와 함정

부분 수집, 누락 복구, 생성기 수정에 필요한 비자명한 동작을 정리한다. 전체 갱신은 `scripts/refresh.sh`를 실행한다.

## 실행 환경

- `refresh.sh --check`는 Python, Academy 세션, shared `crawl`·YouTube 도구를 확인한다.
- 인터프리터는 `CRAWL4AI_PYTHON`, shared crawl 위치는 `CRAWL_SCRIPTS_DIR`, YouTube 도구 위치는 `YOUTUBE_DIGEST_SCRIPTS_DIR`로 바꿀 수 있다.
- 개별 수집기의 옵션은 해당 스크립트의 `--help`를 정본으로 삼는다.

## 커버리지

| 표면 | 수집기 | 발견 방식 |
|---|---|---|
| anthropic.com / claude.com | `crawl-site.py` | sitemap, 영어 정본 |
| platform.claude.com / code.claude.com | `crawl-site.py` | sitemap + Mintlify raw Markdown |
| support.claude.com | `crawl-site.py` | 영어 sitemap |
| alignment.anthropic.com / transformer-circuits.pub | `crawl-site.py` | 홈 링크 1-depth |
| trust.anthropic.com | `crawl-site.py` | SPA 렌더 |
| Anthropic Academy | `academy-video.py` | 인증 카탈로그 + 렌더된 레슨 |
| 공식 YouTube | shared `youtube-channels.py` | 채널 전 영상 + 자막 |
| Anthropic·Claude 소유 PDF | shared `pdf-mirror.py` | 허용 호스트의 원본 PDF |

## 공개 사이트와 문서

- sitemap을 URL 정본으로 쓰고 sitemap index는 한 단계 펼친다.
- `curl_cffi`의 Chrome 지문으로 SSR 본문을 받고 nav/footer boilerplate를 제거한다.
- platform·code 문서는 HTML 대신 페이지별 raw Markdown을 우선한다.
- claude.com과 support는 영어 정본만 저장한다.
- trust.anthropic.com만 SPA라 Playwright 렌더를 사용한다.
- thin, 404, network/extract 실패는 저장하지 않아 다음 실행에서 다시 확인한다.
- 한 host만 점검할 때는 `crawl-site.py . --only <host>`를 쓴다.

## 증분 상태

- 모든 source를 다시 확인하고 정제 본문의 SHA-256을 `.anthropic-mirror-state.json`과 비교한다.
- 첫 실행은 기존 archive를 다시 쓰지 않고 live hash를 기준선으로 등록한다.
- `--force`는 본문 hash와 무관하게 검사 결과를 다시 저장한다.
- 상태 파일은 로컬 cache이며 commit하지 않는다.

## Academy

- Skilljar는 인증 세션과 렌더가 필요하다. 로그인·레슨·영상 규칙은 `academy-notes.md`를 따른다.
- 기본 갱신은 `academy-video.py` 한 번으로 본문 hash와 YouTube/JWPlayer 영상 ID를 함께 검사한다.
- partner Academy도 같은 출력 계약을 쓰되 세션과 host는 분리한다.

## 후처리

- `extract-images.py`는 transformer-circuits의 인라인 base64 그림을 옆 `images/`의 PNG/JPG로 분리한다.
- `youtube-transcripts.sh`와 `inline-transcripts.py`는 페이지의 YouTube 링크 아래에 자막을 멱등 삽입한다.
- Academy와 docs는 자체 처리 또는 낮은 가치 때문에 wrapper의 인라인 자막 대상에서 제외한다.
- `youtube-channels.py`는 `_yt-cache/`를 재사용하고 채널별 transcript/stub을 발행한다.
- `pdf-mirror.py`는 Anthropic·Claude 소유 host만 허용하고 `%PDF-` 및 100MB 제한을 확인한다.
- `verify-mirror.py`는 자막 참조 누락과 렌더 불가능한 대형 Markdown을 마지막에 검사한다.

## 범위 밖

- Claude 제품 앱과 인증된 사용자 데이터는 수집하지 않는다.
- 외부 학회·정부·대학·arXiv PDF는 원문 링크만 유지한다.
- sitemap이나 발견 허브 어디에도 없는 페이지는 자동으로 찾을 수 없다.
