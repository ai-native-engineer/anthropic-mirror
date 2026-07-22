<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/anthropic-logo-dark.svg">
    <img src="assets/anthropic-logo.svg" alt="Anthropic" height="30">
  </picture>
</p>

<p align="center"><b>English</b> | <a href="README.ko.md">한국어</a></p>

# anthropic-mirror

![status: unofficial mirror](https://img.shields.io/badge/status-unofficial%20mirror-orange)
![last commit](https://img.shields.io/github/last-commit/ai-native-engineer/anthropic-mirror)

An unofficial, searchable, git-versioned archive of public Anthropic and Claude materials. It mirrors documentation, research, Academy courses, YouTube transcripts, and linked PDFs for study and reference.

> [!WARNING]
> This repository is not created or operated by Anthropic. Copyright remains with **Anthropic, PBC**. Use the source link in each file for the latest and authoritative version.

## Coverage

| Path | Content |
|---|---|
| `www.anthropic.com/`, `claude.com/` | News, research, engineering, policy, products, blog, customers, and resources |
| `platform.claude.com/`, `code.claude.com/`, `support.claude.com/` | Developer/API docs, Claude Code docs, and Help Center articles |
| `alignment.anthropic.com/`, `transformer-circuits.pub/`, `trust.anthropic.com.md` | Alignment, interpretability, security, and compliance |
| `anthropic.skilljar.com/` | Anthropic Academy lessons and caption transcripts |
| `youtube.com/anthropic-ai/`, `youtube.com/claude/` | Official channel transcripts, one Markdown file per video |
| `assets.anthropic.com/`, `www-cdn.anthropic.com/`, `resources.anthropic.com/` | Linked PDFs in their original format |

The directory tree mirrors source URLs as `<host>/<path>.md`. Each generated Markdown file starts with `<!-- source: <url> -->`. The repository stores only the latest snapshot; git preserves change history.

Pages without extractable public text may be absent. The Claude app (`claude.ai`) is out of scope. Videos are stored as caption transcripts rather than media files.

## Use

Browse on GitHub or search a local clone:

```bash
git clone https://github.com/ai-native-engineer/anthropic-mirror.git
cd anthropic-mirror
rg -n "constitutional AI"
```

## Update

The repository-local `anthropic-mirror` skill owns regeneration. Maintainers run:

```bash
bash .agents/skills/anthropic-mirror/scripts/update-mirror.sh --check
bash .agents/skills/anthropic-mirror/scripts/update-mirror.sh
```

Generated domain files are read-only. Fix the skill or crawler and regenerate instead of editing mirrored content by hand.

## Issues and removal requests

- Open an issue for a missing or broken page.
- Copyright holders can open an issue to request removal.

## Copyright

No open-source license is granted for mirrored content. All archived material remains copyright Anthropic, PBC.
