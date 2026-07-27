<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/anthropic-logo-dark.svg">
    <img src="assets/anthropic-logo.svg" alt="Anthropic" height="30">
  </picture>
</p>

<p align="center"><a href="README.md">English</a> | <b>한국어</b></p>

# anthropic-mirror

![status: unofficial mirror](https://img.shields.io/badge/status-unofficial%20mirror-orange)
![last commit](https://img.shields.io/github/last-commit/ai-native-engineer/anthropic-mirror)
![repo size](https://img.shields.io/github/repo-size/ai-native-engineer/anthropic-mirror)

Anthropic과 Claude 공개 자료를 검색하기 쉬운 마크다운으로 보관하는 비공식 아카이브입니다. 기사, 연구, 개발자·도움말 문서, Academy 레슨, YouTube 전사, Anthropic이 호스팅하는 PDF를 담습니다.

> [!WARNING]
> Anthropic이 만들거나 운영하는 저장소가 아닙니다. 보관된 자료의 저작권은 Anthropic에 있습니다. 최신 공식 정보는 반드시 원문에서 확인하세요.

## 아카이브

| 경로 | 자료 |
|---|---|
| [`www.anthropic.com/`](www.anthropic.com/), [`claude.com/`](claude.com/) | 뉴스, 연구, 엔지니어링, 정책, 제품, 블로그, 고객 사례, 리소스 |
| [`platform.claude.com/`](platform.claude.com/), [`code.claude.com/`](code.claude.com/), [`support.claude.com/`](support.claude.com/), [`privacy.claude.com/`](privacy.claude.com/) | 개발자/API 문서, Cookbook, Claude Code 문서, Help Center, Privacy Center |
| [`alignment.anthropic.com/`](alignment.anthropic.com/), [`transformer-circuits.pub/`](transformer-circuits.pub/), [`trust.anthropic.com/`](trust.anthropic.com/) | 정렬, 해석가능성, 보안, 컴플라이언스 |
| [`anthropic.skilljar.com/`](anthropic.skilljar.com/), [`anthropic-partners.skilljar.com/`](anthropic-partners.skilljar.com/) | Anthropic Academy 레슨과 영상 자막 |
| [`youtube.com/anthropic-ai/`](youtube.com/anthropic-ai/), [`youtube.com/claude/`](youtube.com/claude/) | 공식 채널의 일반 영상·Shorts·Streams별 전사 또는 자막 상태 stub |
| Anthropic 소유 파일 호스트 | 보관된 페이지가 링크한 PDF |

트리는 원문 URL을 `<host>/<path>.md` 형태로 따릅니다. 일반 페이지는 `<!-- source: <url> -->` 헤더, Academy 레슨은 원문 URL 주석, YouTube 전사는 YAML frontmatter에 원문 URL을 기록합니다. 미러링한 PDF는 로컬 Apple Vision OCR 결과를 PDF 내부의 투명 text layer로 저장합니다. PNG와 JPEG에는 selectable text layer 규격이 없어 bitmap image 원본은 변경하지 않으며, 별도 OCR Markdown도 생성하지 않습니다.

## 사용

GitHub에서 바로 읽거나, 로컬에서 `rg`로 검색하거나, 전체 아카이브를 클론할 수 있습니다.

```bash
git clone https://github.com/ai-native-engineer/anthropic-mirror.git
cd anthropic-mirror
rg -i -n -C 2 --glob '*.md' 'harness|agent scaffold'
rg -l -i --glob '*.md' 'constitutional AI|alignment'
rg --files | rg -i 'harness|context-engineering'
```

첫 번째 명령은 일치하는 Markdown 본문을 줄 번호와 앞뒤 문맥과 함께 보여줍니다. 두 번째는 일치한 문서 목록을, 세 번째는 파일 경로를 검색합니다. 보관된 텍스트는 대부분 영어이므로 영어 키워드와 동의어부터 검색하세요.

`rg`는 압축된 PDF 본문을 직접 검색하지 못합니다. Markdown과 모든 PDF 텍스트 레이어를 함께 검색하려면 `pdftotext`를 설치하고(macOS: `brew install poppler`) 다음 명령을 실행하세요.

```bash
./search-archive.sh 'constitutional AI|alignment'
```

PDF 결과의 줄 번호는 PDF 페이지가 아니라 추출된 텍스트의 줄 번호입니다.

## 수집 범위

아카이브는 같은 위치에 다시 생성하며 최신 크롤만 유지합니다. 이전 버전은 Git 이력으로 확인할 수 있습니다.

- JavaScript로만 표시되거나 공개 텍스트를 추출할 수 없는 내용은 일부 누락될 수 있습니다.
- 접근 가능한 자막이 없는 영상도 페이지 정보와 자막 상태 stub을 남깁니다.
- 외부 발행물과 GitHub 용량 제한을 넘는 파일은 원문 링크만 남깁니다.
- Claude 제품 앱과 비공개·사용자 생성 콘텐츠는 수집하지 않습니다.

## 갱신과 기여

보관된 페이지는 생성 파일입니다. 내용을 직접 고치지 말고 누락되거나 깨진 페이지를 이슈로 알려주세요. 관리자는 [`.agents/skills/anthropic-mirror/`](.agents/skills/anthropic-mirror/)를 수정한 뒤 해당 도메인을 다시 생성합니다.

## 저작권

보관된 자료에 별도 라이선스를 부여하지 않습니다. 저작권자는 이슈로 삭제를 요청할 수 있습니다.
