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
| [`platform.claude.com/`](platform.claude.com/), [`code.claude.com/`](code.claude.com/), [`support.claude.com/`](support.claude.com/), [`privacy.claude.com/`](privacy.claude.com/) | Developer/API docs, Cookbook, Claude Code docs, Help Center, and Privacy Center articles |
| [`alignment.anthropic.com/`](alignment.anthropic.com/), [`transformer-circuits.pub/`](transformer-circuits.pub/), [`trust.anthropic.com/`](trust.anthropic.com/) | Alignment, interpretability, security, and compliance |
| [`anthropic.skilljar.com/`](anthropic.skilljar.com/), [`anthropic-partners.skilljar.com/`](anthropic-partners.skilljar.com/) | Anthropic Academy lessons and caption transcripts |
| [`youtube.com/anthropic-ai/`](youtube.com/anthropic-ai/), [`youtube.com/claude/`](youtube.com/claude/) | One transcript or caption-status stub per official-channel video, Short, and stream |
| Anthropic-owned file hosts | PDFs linked from archived pages |

The tree follows source URLs as `<host>/<path>.md`. Crawled pages use a `<!-- source: <url> -->` header, Academy lessons use a source URL comment, and YouTube transcripts keep the source URL in YAML frontmatter. Mirrored PDFs store locally generated Apple Vision OCR as an invisible text layer inside the PDF. Bitmap images remain unchanged because PNG and JPEG do not support selectable text layers; no separate OCR Markdown is generated.

## Use

Browse on GitHub, search locally with `rg`, or clone the archive:

```bash
git clone https://github.com/ai-native-engineer/anthropic-mirror.git
cd anthropic-mirror
rg -i -n -C 2 --glob '*.md' 'harness|agent scaffold'
rg -l -i --glob '*.md' 'constitutional AI|alignment'
rg --files | rg -i 'harness|context-engineering'
```

The first command shows matching Markdown with line numbers and surrounding context. The second lists matching documents, and the third searches file paths. Most archived text is English, so start with English terms and synonyms.

`rg` cannot search compressed PDF contents directly. To search Markdown and every PDF text layer together, install `pdftotext` (Poppler; `brew install poppler` on macOS) and run:

```bash
./search-archive.sh 'constitutional AI|alignment'
```

PDF result line numbers refer to extracted text, not PDF page numbers.

## Coverage

The archive is regenerated in place and keeps only the latest crawl. Git preserves earlier revisions.

- JavaScript-only pages and content without extractable public text may be incomplete.
- Videos without accessible captions keep available page metadata and a caption-status stub.
- External publications and files over GitHub's size limit remain source links.
- The Claude product app and private or user-generated content are outside the archive scope.

## Updates and contributions

Archived pages are generated files. Report missing or broken pages with an issue instead of editing their contents. Maintainers should update [`.agents/skills/anthropic-mirror/`](.agents/skills/anthropic-mirror/) and regenerate the affected domains.

## Copyright

No license is granted for the archived material. Copyright holders may request removal by opening an issue.
