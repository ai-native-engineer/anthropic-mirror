# 공개 페이지 크롤 대상·명령

anthropic.com + claude.com + claude docs + support + 연구 블로그를 로컬 미러한다(강의는 academy-extract/academy-video).
**sitemap.xml을 1차 소스로 쓴다** -- 사이트가 새 섹션을 추가해도 빠짐없이 따라간다(옛 하드코딩 목록·See more 펼치기는 폐기). 주력은 `scripts/crawl-site.py` 한 방.

## 환경

- 인터프리터: `~/.local/share/uv/tools/crawl4ai/bin/python` (curl_cffi·bs4·markdownify·playwright 포함)
- crawler: `.agents/skills/anthropic-mirror/scripts/crawl-site.py`
- 공용 후처리: `~/.agents/skills/shared/crawl/scripts/`
- 출력: `<out>/<host>/<path>.md` 도메인 트리 (academy의 `anthropic.skilljar.com/`과 같은 루트에 공존)

## 주력: crawl-site.py

```bash
~/.local/share/uv/tools/crawl4ai/bin/python .agents/skills/anthropic-mirror/scripts/crawl-site.py <out_dir> [--only <host>] [--force] [--limit N] [--concurrency N]
```

- 기본은 **실제 데이터 기준 증분**: sitemap의 모든 URL을 검사하고 정제된 마크다운의 SHA-256을 로컬 `.anthropic-mirror-state.json`과 비교해 달라진 source만 저장한다. URL/파일 존재만으로 skip하지 않으며, 첫 실행은 기존 archive를 다시 쓰지 않고 live 본문 hash를 기준선으로 등록한다. 한 도메인만은 `--only <host substring>`(예: `--only claude.com`). `--limit`은 테스트용 상한, `--force`는 명시적 전체 재저장용이다.
- 한 실행으로 처리하는 소스(스크립트 상단 `HTML_SITEMAPS`/`DOCS_SITEMAPS`/`DISCOVER`/`SPA_PAGES`):

| 소스 | 방식 | 실측 규모 |
|---|---|---|
| www.anthropic.com (sitemap) | curl_cffi + bs4 | ~476 (news/research/engineering/events + legal/product/system-cards/economic 등 전량) |
| claude.com (sitemap, 영어 정본만) | curl_cffi + bs4 | ~1591 (blog/customers/resources/connectors/plugins/solutions ...) |
| claude.com/docs (robots 2번째 sitemap) | curl_cffi + bs4 | ~127 (태그형 help 문서) |
| support.claude.com (sitemap, /en/) | curl_cffi + bs4 | ~370 (Help Center) |
| platform.claude.com/docs (sitemap, /docs/en/) | curl_cffi + `.md` raw | ~1755 (api 레퍼런스 포함) |
| code.claude.com/docs (sitemap, /docs/en/) | curl_cffi + `.md` raw | ~154 (Claude Code CLI: hooks·subagents·settings·slash-commands·statusline·agent-sdk 등) |
| alignment.anthropic.com | 홈 링크 1-depth | ~52 (Alignment Science Blog) |
| transformer-circuits.pub | 홈 링크 1-depth | ~47 (해석가능성 연구) |
| trust.anthropic.com | playwright innerText | 1 (SafeBase SPA) |

## 후처리: 이미지 추출 + YouTube 자막 인라인 (크롤 다음 단계)

크롤은 텍스트만 받으므로 두 가지를 후처리한다. 둘 다 증분·멱등이라 재실행 안전. 후처리 스크립트는 **두 미러(anthropic·openai) 공용**이라 `~/.agents/skills/shared/crawl/scripts/`에 둔다(미러끼리 결합 없음).

### 인라인 base64 이미지 -> PNG (`extract-images.py`)

```bash
python3 ~/.agents/skills/shared/crawl/scripts/extract-images.py <out_dir>   # 또는 단일 .md 파일
```

- transformer-circuits.pub 연구글은 본문에 base64 이미지가 통째로 박혀 파일이 18~30MB가 된다 -> GitHub가 1MB 넘는 마크다운을 렌더 안 한다.
- 인라인 base64를 각 글 옆 `images/img-NNN.png`로 빼고 마크다운을 상대경로로 치환 -> 글이 수십 KB로 줄어 렌더되고 그림은 옆 폴더에서 로드.
- 두 래핑 방식 대응: literal 개행 줄바꿈 / URL 인코딩 `%0A` 줄바꿈(단일 라인). malformed 마크다운(닫는 `)` 누락)도 base64 청크 종료로 잡는다. data:image 없는 파일은 무변경.

### YouTube 자막 인라인 (`youtube-transcripts.sh` -> `inline-transcripts.py`)

페이지에 박힌 YouTube 링크는 텍스트만으론 영상 내용이 빠진다. 별도 트리에 두면 어느 글 영상인지 연관을 못 찾으니 영상이 인용된 위치 바로 아래에 자막을 붙인다.

```bash
bash ~/.agents/skills/shared/crawl/scripts/youtube-transcripts.sh <out_dir> [--exclude <glob>]...   # 1) 자막 추출 -> _yt-cache/<ID>.md 캐시
python3 ~/.agents/skills/shared/crawl/scripts/inline-transcripts.py <out_dir>    # 2) 캐시를 각 영상 링크 아래 인라인
```

- 1단계: 미러 전체에서 video ID를 모아 youtube-digest의 `extract_transcript.sh`+`srt-to-md.sh`(chrome 쿠키로 429 회피)로 전사. 순차+429 백오프(동시 호출은 차단 위험). raw yt-dlp 직접 호출 금지.
- `--exclude`로 자체 전사 파이프라인이 있는 트리를 뺀다 -- skilljar 전체는 `'*.skilljar.com/**'`(academy-video가 전사, 파트너 인스턴스 포함 -- 빼먹으면 이미 폴드가 붙은 영상을 쿼터만 쓰며 재전사한다), docs 트리는 저가치라 제외. `youtube.com/` 채널 발행 트리는 자동 제외.
- 2단계: `_yt-cache/<ID>.md` 캐시(frontmatter title/duration + 자막)를 읽어 각 영상 링크 아래에 `[썸네일 임베드](youtube)` + `<details>` 접이식 자막을 삽입. `<!-- yt-inline:ID -->` 마커로 멱등. 자막 없는 영상은 건너뜀(정상).
- **`_yt-cache/`는 gitignore** -- 발행되는 건 인라인뿐. 캐시는 로컬에 남겨 재실행 시 재추출을 피하고, 채널 미러(youtube-channels.py)와 같은 캐시를 공유해 자막 중복이 없다.

### PDF 원본 미러 (`pdf-mirror.py`)

페이지에 박힌 PDF 링크(eBook·가이드, 예 `assets.anthropic.com/m/<hash>/original/*.pdf`)는 크롤이 텍스트만 받아 본문이 통째로 빠진다. youtube와 같은 스캔 방식으로 원본을 받는다.

```bash
python3 ~/.agents/skills/shared/crawl/scripts/pdf-mirror.py <out_dir> --host anthropic.com --host claude.com [--force]
```

- 미러 전체 `.md`를 스캔해 지정 호스트의 PDF URL을 모아(youtube가 video ID 모으듯) 각 원본을 `<out>/<host>/<path>.pdf`로 받는다 -- 사이트 어디에 링크됐든 자동 발견(N개여도 전부).
- **PDF는 자체 텍스트 레이어가 있어 `.md`로 변환하지 않고 원본만 보존**(GitHub에서 다운로드/뷰어로 열림, 필요 시 `pdftotext`로 추출). 커밋 대상이라 gitignore하지 않는다.
- **`--host`는 필수**(반복 지정). 공용 도구라 미러 도메인을 하드코딩하지 않는다 -- Anthropic은 `anthropic.com`/`claude.com`(assets·www-cdn·resources·alignment 서브도메인까지 substring으로 커버). 외부 인용 PDF(arxiv 등)는 호스트 불일치로 자동 제외.
- 증분·멱등: 기존 파일 skip(`--force` 재다운로드), `urllib`로 받아 **`%PDF-` 매직바이트 검증**(HTML 에러페이지를 PDF로 오저장 방지). http 링크는 https로 승격 재시도(자산 CDN은 https 전용).
- **`--max-mb`(기본 100) 초과는 자동 skip** -- GitHub 파일 하드 리밋(100MB)이라 받아두면 `git push`가 통째로 거부된다(소스 링크는 .md에 남음). 이미지 전용(텍스트 레이어 없는) PDF는 검색 불가 -> `ocrmypdf <f> <f>`로 OCR 텍스트 레이어를 입히면 PDF 유지하며 검색 가능.

## 핵심 원리

- **curl_cffi(impersonate="chrome")** -- anthropic.com은 일반 UA를 막아 plain fetch가 본문 0이지만, Chrome TLS/JA3 지문을 위장하면 SSR 본문이 그대로 온다(브라우저·캡챠 불필요). claude.com·support·alignment·transformer-circuits도 전부 SSR이라 같은 경로로 빠르게 받는다.
- **platform·code docs는 `.md` raw** -- Mintlify SPA라 HTML엔 본문이 없지만 페이지별 `<url>.md`가 깨끗한 마크다운을 준다(브라우저로 렌더한 결과와 동일). `DOCS_SITEMAPS`에 platform(API)·code(Claude Code CLI) 둘 다 등록. code.claude.com .md는 매 페이지 상단에 llms.txt 안내 blockquote가 붙어 `strip_docs_index`로 첫 'Documentation Index' 블록만 제거한다(H1 아래 페이지 설명 blockquote는 보존).
- **claude.com 로케일 필터** -- sitemap이 첫 세그먼트로 로케일을 표기한다(ja/de/fr/ko/it ...). `LOCALES` 집합으로 영어 정본만 남긴다.
- **boilerplate 제거** -- html_to_md 산출 호스트는 페이지별 nav/footer 제거 후, 호스트별 `find_boilerplate`로 공통 줄("Skip to main content" 등)을 한 번 더 제거한다. platform·code docs .md는 이미 깨끗해 스킵.

## 함정

- **trust.anthropic.com만 SPA** -- SafeBase는 curl도 .md도 본문 0이라 유일하게 playwright innerText(`#trust-center-main-content`/main/body, `domcontentloaded`+6s)로 보강한다.
- **sitemap 인덱스 자동 펼침** -- `sitemap_urls`는 `<loc>`가 전부 `.xml`이면 sitemap 인덱스로 보고 자식을 한 단계 더 펼친다.
- **새 surface가 생겨도 sitemap에 뜨면 자동 포함** -- 단, sitemap에 없는 사이트(alignment·transformer-circuits)는 홈 링크 1-depth라 홈에서 링크 안 된 글은 놓칠 수 있다. 누락 의심 시 해당 연도 인덱스를 `DISCOVER` base에 추가한다.
- **누락 검증** -- sitemap의 `<loc>` 집합과 저장된 `<host>/<path>.md`를 diff하면 빠진 URL이 바로 보인다(완전성 점검의 정본). 발행물 계약(자막 폴드 커버리지·1MB 렌더 리밋)은 update wrapper의 마지막 `verify-mirror.py`가 검사한다.
- **`본문없음 skip`은 재진단 금지** -- 업스트림에 본문 자체가 없는 페이지들이라 크롤러가 실패와 구분해 집계한다(수백 건이어도 정상). 실측 클래스: platform docs의 미발행 SDK 섹션(`.md` 404 또는 제목만 있는 stub -- terraform·tunnels 계열), claude.com `blog-product/`·`blog-usecases/`(JS redirect 셸, 본문은 blog 본편에 이미 있음), sitemap에 남은 404. 저장하지 않으므로 매 실행 재확인되고 업스트림이 발행하면 자동 수집된다.
