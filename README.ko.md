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
![docs ~4.7k](https://img.shields.io/badge/docs-~4.7k-blue)

> **Anthropic / Claude 공개 자료**(소식, 연구, 엔지니어링, 정책/법무, 제품, 플랫폼 문서/API 레퍼런스, Claude Code CLI 문서, Help Center, Trust Center, Alignment Science/해석가능성 블로그, Anthropic Academy 코스)를 마크다운으로 정리한 비공식 아카이브.

강의/자료 제작 시 참고 소스로 모았고, 누구나 읽어볼 수 있게 공개해 둡니다.

> [!WARNING]
> **비공식 아카이브입니다. Anthropic이 만들거나 운영하지 않습니다.** 모든 콘텐츠의 저작권은 **Anthropic, PBC**에 있으며, 이 저장소는 원문을 마크다운으로 변환해 보관한 개인 참고용 미러입니다. 최신/정확한 내용은 항상 아래 공식 출처를 확인하세요.

## 무엇이 담겨 있나

최신 크롤 스냅샷 기준 약 4,700개 마크다운 파일. 트리는 원문 URL 구조(`<host>/<path>.md`)를 그대로 따라가므로 파일 위치가 곧 원문 페이지 위치입니다. 각 파일 상단에 원문 링크 `<!-- source: <url> -->`가 붙어 있습니다.

| 경로 | 내용 | 문서 수 |
|---|---|---|
| `www.anthropic.com/` | 소식, 연구, 엔지니어링, 이벤트, 회사, 채용, 정책/법무, 제품, system cards, economic index | 약 484 |
| `claude.com/` | 블로그, 고객 사례, 리소스, use-case, 튜토리얼, connectors, plugins, help 문서 | 약 1,717 |
| `platform.claude.com/` | 개발자 문서 + 전체 API 레퍼런스 | 약 1,695 |
| `code.claude.com/` | Claude Code CLI 문서(hooks, sub-agents, settings, slash commands, statusline, output styles, checkpointing, Agent SDK) | 약 154 |
| `support.claude.com/` | Help Center article | 약 370 |
| `alignment.anthropic.com/` | Alignment Science 블로그 | 약 51 |
| `transformer-circuits.pub/` | 해석가능성 연구(Transformer Circuits Thread), 그림은 PNG로 추출 | 약 49 |
| `trust.anthropic.com` | Trust Center(보안, 컴플라이언스, 인증) | 1 |
| `anthropic.skilljar.com/` | Anthropic Academy 코스 레슨 | 약 158 |

대부분 텍스트입니다. 예외: 해석가능성 논문은 본문 그림을 PNG 파일로 추출해 함께 보관하고, 페이지에 임베드된 YouTube 영상은 자막으로 전사해 영상 바로 아래 접이식 `<details>` 블록으로 인라인합니다. Anthropic Academy 영상 코스는 YouTube / JWPlayer 자막을 텍스트로 전사합니다.

**알려진 커버리지 갭** (각 sitemap 대조 측정, 표면별 약 96~99%). 못 담은 것: `platform.claude.com/docs/en/api/` 하위 자동생성 API SDK 레퍼런스 약 150개(terraform/php/csharp 엔드포인트, 원본 `.md`가 404), 그리고 서버측 텍스트가 없는 JS 렌더 페이지 소수. 이들을 담으려면 헤드리스 브라우저가 필요한데, 이 미러는 의도적으로 쓰지 않습니다.

## 어떻게 만들어지나

sitemap 기반 자동 크롤 파이프라인으로 수집합니다(API 키 없음, 공개 페이지는 로그인 없음): 각 도메인의 `sitemap.xml`을 1차 소스로 삼고, Chrome 브라우저 지문(`curl_cffi`)으로 가져와 헤드리스 브라우저 없이 SSR HTML을 받습니다. `platform.claude.com`·`code.claude.com` 문서는 Mintlify `.md` raw로 받습니다. 재생성 절차는 `AGENTS.md` 참조.

## 출처 (Sources)

- https://www.anthropic.com (소식, 연구, 엔지니어링, 정책, 법무, 제품)
- https://claude.com (블로그, 고객 사례, 리소스, connectors, help)
- https://platform.claude.com/docs (개발자 문서 + API 레퍼런스)
- https://code.claude.com/docs (Claude Code CLI)
- https://support.claude.com (Help Center)
- https://alignment.anthropic.com (Alignment Science)
- https://transformer-circuits.pub (해석가능성)
- https://trust.anthropic.com (Trust Center)
- https://anthropic.skilljar.com (Anthropic Academy)

## 사용법

GitHub에서 폴더별로 바로 읽거나, 전체를 클론하세요:

```bash
git clone https://github.com/ai-native-engineer/anthropic-mirror.git
```

## 범위 밖

Claude 제품 앱(claude.ai)은 포함하지 않습니다. 바이너리 자산은 해석가능성 그림(PNG)을 제외하고 담지 않으며, 영상 코스와 임베드 영상은 자막 전사본으로만 보관합니다.

## 갱신

`anthropic-mirror` 스킬로 다시 크롤해 최신 미러만 덮어씁니다. 변경 이력은 git이 보존하므로 `git log` / `git diff`로 추적합니다(날짜별 디렉토리를 누적하지 않습니다).

## 기여

이 아카이브는 자동 생성되므로 파일을 손으로 고치지 않습니다 - 문서 내용을 바꾸는 PR은 다음 동기화 때 덮어써지니 보내지 마세요. 대신:

- 깨졌거나 빠진 페이지를 찾으셨나요? 이슈를 열어 주세요.
- 저작권자로서 자료 삭제를 원하시나요? 이슈를 열어 주시면 해당 자료를 내립니다.

## 라이선스 / 저작권

오픈소스 라이선스를 부여하지 않습니다 - 보관된 텍스트의 저작권은 전부 Anthropic, PBC에 있습니다. 학습 / 참고 목적의 미러이며, 저작권자의 요청이 있으면 해당 자료를 내립니다.
