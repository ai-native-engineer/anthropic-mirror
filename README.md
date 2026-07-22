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
![repo size](https://img.shields.io/github/repo-size/ai-native-engineer/anthropic-mirror)

An unofficial, searchable Markdown archive of Anthropic and Claude public materials: articles, research, developer and help documentation, Academy lessons, YouTube transcripts, and Anthropic-hosted PDFs.

> [!WARNING]
> This repository is not created or operated by Anthropic. Anthropic retains the copyright to the archived material. Check the official source for current, authoritative information.

## Archive

| Path | Material |
|---|---|
| [`www.anthropic.com/`](www.anthropic.com/), [`claude.com/`](claude.com/) | News, research, engineering, policy, products, blog, customers, and resources |
| [`platform.claude.com/`](platform.claude.com/), [`code.claude.com/`](code.claude.com/), [`support.claude.com/`](support.claude.com/) | Developer/API docs, Claude Code docs, and Help Center articles |
| [`alignment.anthropic.com/`](alignment.anthropic.com/), [`transformer-circuits.pub/`](transformer-circuits.pub/), [`trust.anthropic.com.md`](trust.anthropic.com.md) | Alignment, interpretability, security, and compliance |
| [`anthropic.skilljar.com/`](anthropic.skilljar.com/), [`anthropic-partners.skilljar.com/`](anthropic-partners.skilljar.com/) | Anthropic Academy lessons and caption transcripts |
| [`youtube.com/anthropic-ai/`](youtube.com/anthropic-ai/), [`youtube.com/claude/`](youtube.com/claude/) | One transcript or caption-status stub per official-channel video |
| Anthropic-owned file hosts | PDFs linked from archived pages |

The tree follows source URLs as `<host>/<path>.md`. Crawled pages use a `<!-- source: <url> -->` header, Academy lessons use a source URL comment, and YouTube transcripts keep the source URL in YAML frontmatter.

## Use

Browse on GitHub, search locally with `rg`, or clone the archive:

```bash
git clone https://github.com/ai-native-engineer/anthropic-mirror.git
cd anthropic-mirror
rg "constitutional AI"
```

## Coverage

The archive is regenerated in place and keeps only the latest crawl. Git preserves earlier revisions.

- JavaScript-only pages and content without extractable public text may be incomplete.
- Videos without accessible captions keep available page metadata or are omitted.
- External publications and files over GitHub's size limit remain source links.
- The Claude product app and private or user-generated content are outside the archive scope.

## Updates and contributions

Archived pages are generated files. Report missing or broken pages with an issue instead of editing their contents. Maintainers should update [`.agents/skills/anthropic-mirror/`](.agents/skills/anthropic-mirror/) and regenerate the affected domains.

## Copyright

No license is granted for the archived material. Copyright holders may request removal by opening an issue.
