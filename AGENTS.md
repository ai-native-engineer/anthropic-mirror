# AGENTS.md

Guidance for AI agents (Claude Code, Codex, Cursor, etc.) working in this repository.

## What this repo is

A **generated** archive, not a hand-maintained one. Every Markdown file under a `<host>/` directory is crawled from a live Anthropic/Claude page and rewritten as Markdown. The first line of each file is a `<!-- source: <url> -->` pointer to the original.

## Do / Don't

- **Do not hand-edit content files.** They are overwritten on the next crawl, so edits are lost. Fix the generator (the `anthropic-mirror` skill), not the output.
- **Do not add files by hand** under the domain directories. New pages enter only through the crawl.
- Treat the archive as read-only when answering questions: browse and `rg`/grep across it freely.

## Layout

`<host>/<path>.md`, mirroring the original URL tree.

| Directory | Source |
|---|---|
| `www.anthropic.com/` | News, research, engineering, policy, legal, products, system cards |
| `claude.com/` | Blog, customer stories, resources, connectors, help docs |
| `platform.claude.com/` | Developer docs + API reference (Mintlify `.md` raw) |
| `support.claude.com/` | Help Center |
| `alignment.anthropic.com/` | Alignment Science blog |
| `transformer-circuits.pub/` | Interpretability research (figures extracted as PNG under `images/`) |
| `trust.anthropic.com.md` | Trust Center (security, compliance, certifications) - single page |
| `anthropic.skilljar.com/` | Anthropic Academy course lessons |
| `youtube.com/anthropic-ai/`, `youtube.com/claude/` | Official YouTube channel mirrors (one transcript per video, collapsible) |
| `assets.anthropic.com/`, `www-cdn.anthropic.com/`, `resources.anthropic.com/` | PDF documents linked from pages, kept as original `.pdf` files (system cards, research papers, eBooks, guides) |

## Conventions

- **YouTube has two forms.** The official channel mirrors live under `youtube.com/<handle>/` (committed, one transcript per video). Transcripts for videos embedded in a page are inlined below the embed in a `<details>` block. The raw transcript cache `_yt-cache/` is gitignored (extraction cache only, not committed).
- **Latest-only.** The newest crawl overwrites in place; there are no dated snapshot folders. History lives in git.
- **Commits:** one logical change per commit. Don't `git add .` blindly - a full crawl touches thousands of files, so stage the domains you actually regenerated. Never `git push --force` or `git reset --hard`.
- **README is bilingual** (`README.md` English, `README.ko.md` Korean). Keep both in sync when you change one.

## Regenerating

Owned by the `anthropic-mirror` skill (lives outside this repo). The crawl is sitemap-driven and uses a Chrome browser fingerprint (`curl_cffi`) so no headless browser is needed; `platform.claude.com` docs are fetched as Mintlify `.md` raw. Post-processing extracts inline base64 figures to PNG, inlines YouTube transcripts, mirrors the official YouTube channels under `youtube.com/<handle>/` (enumerated with `yt-dlp`), and mirrors PDF documents linked from pages as their original `.pdf` files (text-layer PDFs are kept as-is, not converted to markdown). Do not reimplement any of this inside the repo.
