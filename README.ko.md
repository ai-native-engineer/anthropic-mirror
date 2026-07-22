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

Anthropic과 Claude의 공개 자료를 검색하고 git으로 변경 이력을 확인할 수 있게 모은 비공식 아카이브입니다. 문서, 연구, Academy 코스, YouTube 자막, 링크된 PDF를 학습·참고용으로 미러합니다.

> [!WARNING]
> Anthropic이 만들거나 운영하는 저장소가 아닙니다. 저작권은 **Anthropic, PBC**에 있습니다. 최신 정본은 각 파일의 원문 링크에서 확인하세요.

## 포함 범위

| 경로 | 내용 |
|---|---|
| `www.anthropic.com/`, `claude.com/` | 소식, 연구, 엔지니어링, 정책, 제품, 블로그, 고객 사례, 리소스 |
| `platform.claude.com/`, `code.claude.com/`, `support.claude.com/` | 개발자/API 문서, Claude Code 문서, Help Center |
| `alignment.anthropic.com/`, `transformer-circuits.pub/`, `trust.anthropic.com.md` | 정렬, 해석가능성, 보안, 컴플라이언스 |
| `anthropic.skilljar.com/` | Anthropic Academy 레슨과 영상 자막 |
| `youtube.com/anthropic-ai/`, `youtube.com/claude/` | 공식 채널 자막, 영상 1편당 Markdown 1개 |
| `assets.anthropic.com/`, `www-cdn.anthropic.com/`, `resources.anthropic.com/` | 페이지에 링크된 PDF 원본 |

디렉터리는 원문 URL과 같은 `<host>/<path>.md` 구조입니다. 생성된 Markdown 첫 줄에는 `<!-- source: <url> -->`가 있습니다. 최신 스냅샷만 보관하고 변경 이력은 git에 남깁니다.

공개된 텍스트를 추출할 수 없는 페이지는 빠질 수 있습니다. Claude 앱(`claude.ai`)은 범위 밖입니다. 영상 파일 대신 자막 전사본을 보관합니다.

## 사용

GitHub에서 바로 읽거나 로컬로 클론해 검색합니다.

```bash
git clone https://github.com/ai-native-engineer/anthropic-mirror.git
cd anthropic-mirror
rg -n "constitutional AI"
```

## 갱신

저장소 로컬 `anthropic-mirror` 스킬이 재생성을 담당합니다. 유지보수자는 다음을 실행합니다.

```bash
bash .agents/skills/anthropic-mirror/scripts/update-mirror.sh --check
bash .agents/skills/anthropic-mirror/scripts/update-mirror.sh
```

도메인 아래 생성물은 읽기 전용입니다. 미러 본문을 직접 고치지 말고 스킬이나 크롤러를 수정한 뒤 다시 생성합니다.

## 오류·삭제 요청

- 빠졌거나 깨진 페이지는 이슈로 알려 주세요.
- 저작권자는 이슈를 열어 삭제를 요청할 수 있습니다.

## 저작권

미러 콘텐츠에는 오픈소스 라이선스를 부여하지 않습니다. 보관된 자료의 저작권은 Anthropic, PBC에 있습니다.
