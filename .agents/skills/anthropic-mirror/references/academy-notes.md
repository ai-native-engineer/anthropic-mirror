# Anthropic Academy(skilljar) 추출 구조·함정

`anthropic.skilljar.com`(Skilljar LMS). 로그인 뒤 코스의 텍스트 레슨을 추출한다. **다른 skilljar 인스턴스**(예: 파트너 전용 `anthropic-partners.skilljar.com`)는 `SKILLJAR_BASE` 환경변수로 지정한다 — 하단 "다른 skilljar 인스턴스" 참조.

## 환경

- crawl4ai 인터프리터: `~/.local/share/uv/tools/crawl4ai/bin/python` (playwright·httpx·bs4 포함)
- 본문 마크다운 변환용 `markdownify` 필요: `uv pip install --python <그 인터프리터> markdownify`
- 쿠키 저장 위치: `~/.crawl4ai/academy_state.json`. `SKILLJAR_BASE`가 기본 도메인이 아니면 `~/.crawl4ai/skilljar-<host>.json`으로 분리 저장(login-academy.py가 storage_state로 저장, 세 스크립트가 같은 규칙으로 읽음).

## 파이프라인

아래에서 `PY=~/.local/share/uv/tools/crawl4ai/bin/python`, `S=.agents/skills/anthropic-mirror/scripts`로 둔다.

1. `$PY $S/login-academy.py` (사람, 헤드풀): 로그인(academy는 이메일+비밀번호, 인스턴스마다 다를 수 있음) -> 루트 재확인 -> 쿠키 저장.
2. `$PY $S/academy-video.py <out_dir> [course-slug ...]` (AI): 모든 레슨을 렌더해 본문 hash와 모든 영상 ID를 검사 -> 달라진 본문과 새 clip만 저장·전사. 본문·자막이 없어도 catalog lesson ID마다 source stub을 남긴다.
3. `academy-extract.py`는 영상 검사가 필요 없는 부분 본문 점검용이다. 기본 전체 갱신에서는 같은 레슨을 두 번 읽지 않도록 실행하지 않는다.
4. 출력은 `<out_dir>/anthropic.skilljar.com/<course>/<NN>-<title>.md`로 저장한다(A 트랙과 같은 `<도메인>/<경로>` 트리).
5. 전체 `refresh.sh`는 public instance 뒤에 partner instance도 실행한다. public과 같은 slug는 건너뛰고 partner 전용 course만 갱신한다.

## 코스 유형 (미리 가르지 않는다)

코스는 세 종류다 — 순수 텍스트(claude-code-in-action·introduction-to-subagents), 순수 영상(api·bedrock·vertex·mcp 계열), **하이브리드**(텍스트 래퍼 + youtube 영상: ai-fluency 계열·claude-101·introduction-to-claude-cowork·introduction-to-agent-skills·ai-capabilities-and-limitations·teaching-ai-fluency·claude-code-101·platform-101·builders 등). 하이브리드가 다수다.

- **코스를 텍스트/영상으로 미리 분류해 academy-video를 일부 코스만 돌리는 짓 금지.** 과거 이 분류표가 하이브리드를 "텍스트 코스"로 묶어 ~10개 코스·63개+ 레슨의 youtube 자막이 통째로 빠졌다.
- 기본 워크플로는 **academy-video를 모든 코스에 돌린다.** 한 번의 렌더 순회에서 본문과 영상 ID를 함께 검사하며, 영상 없는 레슨과 기존 영상 ID는 no-op이다.
- 기본 실행은 모든 코스와 레슨을 검사한다. 중복 판단은 source URL이나 파일 존재가 아니라 정제된 본문 내용과 영상 ID로 한다. 기존 레슨에 새 클립이 붙으면 새 영상 ID만 전사한다.
- 코스 목록은 카탈로그(`/`) HTML의 단일 세그먼트 링크로 자동 수집된다. 미등록 코스는 레슨이 잠겨 0개로 나오니(`0 lessons listed`), 사용자가 등록 후 그 코스만 다시 추출한다.

## 함정

- **crwl profiles의 CDP 버그**: `crwl profiles create`가 `ECONNREFUSED ::1:9222`로 실패한다. macOS `/etc/hosts`의 `::1 localhost` + crawl4ai가 `http://localhost:9222`를 IPv6로 해석하는데 Chrome은 IPv4에만 바인드하기 때문. -> login-academy.py가 playwright persistent context로 직접 로그인해 우회.
- **쿠키 만료가 빠르다**: 만료되면 코스 페이지가 비로그인 미리보기를 반환하고 lesson ID가 `02`·`03` 같은 순번으로 나온다(실제는 287722 같은 6자리). academy-extract.py가 6자리+만 필터하고 로그인 여부(`auth/logout` 존재)를 먼저 확인한다. 비로그인이면 login-academy.py 재실행.
- **브라우저 크롤이 느리다**: skilljar 레슨 페이지가 1MB라 브라우저는 페이지당 12-18초. `text_mode=True`로 3초까지 줄지만, httpx 병렬(브라우저 없음)이 더 빠르고 안정적이다.
- **본문 셀렉터는 가장 긴 후보를 고른다(첫 매칭 금지)**: 영상 코스 레슨은 `.course-text-content`가 "Video" 5자뿐이고 실제 본문은 `article`/`#lesson-main-content`에 있다(claude-code-101 article 2562자). `or` 체인으로 첫 매칭만 쓰면 본문을 통째로 놓친다 -> `.course-text-content`/`.clp__main-content`/`#lesson-main-content`/`article` 중 **가장 긴 것**을 본문으로 쓴다.
- **영상 코스는 placeholder가 거짓 캡처된다**: 영상 레슨 본문 컨테이너에 `This video is still being processed`(약 218자) placeholder가 들어 50자 필터를 통과한다. academy-extract.py가 이 마커로 스킵하므로 captured에 안 잡힌다 -- captured 숫자만으로 텍스트 코스를 판단하지 말 것.
- **레슨 제목은 `<title>`에서 뽑는다**: 본문 첫 헤딩(`#`)은 대부분 "Learning Objectives"라 파일명이 떼창한다. 페이지 `<title>` 태그가 실제 레슨명(예: `What is Claude?`)이라 그걸 slug로 쓴다.

## 영상 코스 전사 (academy-video.py)

영상 코스는 **본문 + 자막을 한 파일에** 둔다(claude-code-101/platform/builders는 영상 + `article` 본문 = 자막보다 깨끗한 글). 워크플로: (1) academy-extract로 텍스트 본문 추출 -> (2) academy-video가 마커 + 전사를 붙인다(멱등: 마커가 이미 있으면 skip) -> (3) render-video-refs가 발행 형태(썸네일 + 접이식 `<details>` 자막)로 렌더. 본문이 없는 순수 영상 코스(MCP, bedrock/vertex/api)는 자막만 쓴다. 플레이어가 코스마다 다르다:

- **목차 레슨 ID는 httpx SSR로 잡는다** -- 일부 코스(ai-fluency-for-builders)는 playwright 렌더가 목차 링크를 비운다. 영상 ID/자막은 레슨별 playwright로.
- **youtube 코스/하이브리드**: 레슨별 youtube ID는 playwright로 렌더 후 "보이는 iframe"(width/height>50)에서 잡는다(httpx raw엔 코스 전체 embed가 섞임, `EAP_VIDEO_ID`는 공통 기본값이라 무시). **iframe 렌더가 1800ms보다 늦는 레슨이 있어** goto 직후 `wait_for_selector("iframe[src*=youtube], .jw-video, video", 7s)`로 플레이어 등장을 기다린 뒤 잡는다(고정 대기만 쓰면 하이브리드 레슨이 간헐 누락). 진짜 텍스트 레슨은 타임아웃 후 통과. 자막은 **youtube-digest의 `extract_transcript.sh`(크롬 쿠키로 429 회피 + 수동자막 우선 en-orig>en>ko)로 받는다 -- raw yt-dlp 직접 호출 금지**(youtube 자막 추출의 정본).
- **JWPlayer 코스**(MCP 등): youtube iframe이 없고 `<video src="blob:">`로 재생. 재생 트리거 후 `jwplayer().getPlaylistItem().tracks`의 English captions `.srt`(수동 제작, 고품질)를 다운로드한다(cdn.jwplayer.com, urllib이 301 follow).
- 실행: `$PY $S/academy-video.py <out_dir> [course-slug ...]` -> `<out_dir>/anthropic.skilljar.com/<course>/<NN>-<title>.md`(slug 생략 시 전체 코스, academy-extract와 같은 트리, `<!-- youtube: ID -->` 또는 `<!-- jwplayer-srt: URL -->` 주석).
- **전사는 flowing 문장** -- `cap_to_text`가 자막 큐(3~6 단어)를 줄바꿈 없이 공백으로 합쳐 OpenAI academy처럼 읽히는 문단을 만든다(33자 하드랩 금지). 자동자막(en) 원본의 ASR 오인식(예: "context"->"contacts")은 그대로 남는다 -- 미러 충실성을 위해 의미 재작성은 하지 않는다(수동자막이 있으면 extract_transcript.sh가 우선 사용).
- **발행 형태는 render-video-refs.py 단일 표준이다 — 추출 스크립트는 [마커 + 전사]만 남기고 썸네일·`<details>`를 직접 만들지 않는다.** 커스텀 포맷(예: `### [영상] 제목`, 펼친 전사, 직접 박은 `<details>`)을 쓰면 렌더러가 못 잡아 스타일이 어긋난다. 마커 + 펼친 전사만 두면 후처리 `~/.agents/skills/shared/crawl/scripts/render-video-refs.py`가 마커 아래에 [영상 임베드 + 접이식 `<details><summary>자막: 제목</summary>`]를 통일 생성한다(멱등: 이미 `<summary>자막`이면 skip, 옛 `## 자막 (영상 전사)`·펼친 포맷도 마이그레이션). 지원 마커:
  - `<!-- youtube: <11자ID> -->` -> YouTube 썸네일(`img.youtube.com/vi/ID/hqdefault.jpg`) + watch 링크
  - `<!-- vimeo: <숫자ID> -->` -> Vimeo watch 링크(썸네일 없음)
  - `<!-- jwplayer: <JW media ID> -->` -> JW 썸네일(`cdn.jwplayer.com/thumbs/ID.jpg`) + **재생 링크는 파일 첫 `<!-- source URL -->` 주석**(레슨 URL)에서 자동으로 가져온다 -> 파일 첫 줄에 source 주석을 반드시 남긴다
  - `<!-- jwplayer-srt: <URL> -->` -> 수동자막 코스, 공개 watch URL 없어 썸네일 생략·자막만 접는다
- 큰 youtube 코스(bedrock 83·vertex 93·api 85)는 연속 호출이 많아 차단 위험 -> 코스를 나눠 배치로(extract_transcript.sh의 크롬 쿠키가 429를 완화).

## 다른 skilljar 인스턴스 (파트너 포털 등)

같은 Skilljar LMS라도 별도 인스턴스가 있다(예: 파트너 전용 `anthropic-partners.skilljar.com`). 세 스크립트(login/extract/video)에 `SKILLJAR_BASE=https://<host>`로 지정한다 — 기본값 `anthropic.skilljar.com`이라 기존 동작 불변, STATE·프로필은 도메인별로 분리돼 세션이 안 섞인다.

- **로그인 방식이 다를 수 있다**: 파트너 포털은 이메일+비번이 아니라 `partner-sso.anthropic.com` OAuth다. 헤드풀 브라우저(login-academy.py)로 사람이 로그인하면 `sj_` 쿠키는 동일하게 저장돼 방식 자체는 그대로 유효하다(CHECK URL은 코스 슬러그가 달라 루트로, 판정은 `sj_` 쿠키 존재).
- **중복부터 대조한다**: 파트너 포털은 공개 academy 코스를 다수 재호스팅한다. 미러 폴더 유무가 아니라 **공개 카탈로그(로그인 후 `/` + `/page/all-courses`)의 실제 슬러그 + 레슨 ID**와 대조해 가려낸다(슬러그+레슨ID 동일 = 같은 콘텐츠). 파트너 전용(공개에 없는 것)만 미러한다.
- **코스 목록은 목록 페이지까지 긁는다**: 루트(`/`)만으론 일부만 잡힌다 — `/page/all-courses` 등 목록 페이지의 단일 세그먼트 링크를 합친다.

### 콘텐츠 타입 (레슨마다 다름 — 미리 가르지 않는다)

한 코스 안에서도 레슨별로 렌더 방식이 다르다. academy-video가 `0 transcribed`면 아래를 의심한다:

- **직접 youtube embed**: academy-video가 정상 처리(레슨당 보이는 iframe 1개).
- **SCORM 패키지**: `#lesson-main-content`의 iframe(`scorm_content_frame`) src가 비고 JS로 로드된다. 실제 콘텐츠는 CloudFront 보호 중첩 프레임 `/content/wp/.../module-XX.html`이라 httpx 직접 요청은 403 — playwright 세션 내 `page.frames`에서 `/content/wp/` URL 프레임을 찾아 `frame.content()`로만 읽힌다. 텍스트/슬라이드가 많고 영상은 없을 수 있다.
- **JWPlayer 자체 비디오**: `<video src="blob:">`로 재생. JW media ID를 네트워크(`content.jwplayer.com/manifests/<ID>.m3u8`)에서 잡는다. **원본 자막 트랙이 없을 수 있다**(JW v2/media에 thumbnails만) -> `yt-dlp -x --audio-format m4a "https://cdn.jwplayer.com/manifests/<ID>.m3u8"`(토큰 불필요)로 오디오를 받아 STT 전사한다. 파일은 `[첫 줄 source(레슨) URL 주석 + <!-- jwplayer: <ID> --> 마커 + 제목 + 전사]`만 남기고 발행 형식은 render-video-refs가 통일 렌더한다(위 발행 형태 참조).
- **raw HTML의 youtube embed는 노이즈다**: 모든 레슨 페이지에 코스 전체(또는 홍보) 영상이 동일하게 프리로드된다. 여러 코스에서 같은 embed 목록이 나오면 레슨 영상이 아니라 curriculum 노이즈다 — 레슨 자막으로 쓰지 말 것(렌더된 `#lesson-main-content` 내부만 실제 콘텐츠).

### STT 함정 (JWPlayer 자막 없는 영상)

- **apple-stt는 영어 자료에 `-l en-US` 필수**: 로케일 기본이 한국어라 빼면 영어 웨비나가 통째로 깨진다(45분이 2787자로 축소·의미불명). `-l en-US`면 정상(5분에 ~4900자). 다화자·잡음이 심하면 whisper로.
- apple-stt는 진행 로그(`▶`·`·`로 시작)를 stdout에 섞으니 전사 본문만 추린다.
- 레슨 제목·파일명은 `html.unescape` 후 slug한다 — `<title>`의 `&#x27;` 같은 엔티티가 남으면 파일명이 `whatx27s`처럼 깨진다.
