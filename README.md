**English** | [한국어](README.ko.md)

# anthropic-mirror

![status: unofficial mirror](https://img.shields.io/badge/status-unofficial%20mirror-orange)
![last commit](https://img.shields.io/github/last-commit/ai-native-engineer/anthropic-mirror)
![repo size](https://img.shields.io/github/repo-size/ai-native-engineer/anthropic-mirror)
![docs ~4.5k](https://img.shields.io/badge/docs-~4.5k-blue)

> Unofficial markdown archive of **Anthropic & Claude public materials** - news, research, engineering, policy & legal, products, platform docs & API reference, Help Center, the Alignment Science and Interpretability blogs, and Anthropic Academy courses.

Collected as a reference source for talks and study, kept public so anyone can read.

> [!WARNING]
> **Unofficial archive. Not created or operated by Anthropic.** All content is copyright **Anthropic, PBC**; this repository only mirrors published text as markdown for personal reference. Always check the official sources below for the latest and most accurate information.

## Contents

About 4,500 markdown files, as of the latest crawl snapshot. The tree mirrors the source URLs (`<host>/<path>.md`), so a file's location maps directly to its original page. Each file keeps a `<!-- source: <url> -->` header linking back.

| Path | Content | Docs |
|---|---|---|
| `www.anthropic.com/` | News, research, engineering, events, company, careers, policy & legal, products, system cards, economic index | ~484 |
| `claude.com/` | Blog, customer stories, resources, use-cases, tutorials, connectors, plugins, help docs | ~1,717 |
| `platform.claude.com/` | Developer documentation and the full API reference | ~1,695 |
| `support.claude.com/` | Help Center articles | ~370 |
| `alignment.anthropic.com/` | Alignment Science blog | ~51 |
| `transformer-circuits.pub/` | Interpretability research (Transformer Circuits Thread), with figures saved as PNG | ~49 |
| `anthropic.skilljar.com/` | Anthropic Academy course lessons | ~158 |

Mostly text. Exceptions: interpretability papers keep their inline figures as extracted PNG files, and YouTube videos embedded in a page are transcribed and inlined below the embed inside a collapsible `<details>` block. Anthropic Academy video courses are transcribed from YouTube / JWPlayer captions.

## How it's generated

Crawled by an automated, sitemap-driven pipeline (no API keys, no login for public pages): every domain's `sitemap.xml` is the source of truth, fetched with a Chrome browser fingerprint so the server-rendered HTML comes through without a headless browser. `platform.claude.com` docs are pulled as Mintlify `.md` raw. See `AGENTS.md` for the regeneration details.

## Sources

- https://www.anthropic.com (news, research, engineering, policy, legal, products)
- https://claude.com (blog, customers, resources, connectors, help docs)
- https://platform.claude.com/docs (developer docs + API reference)
- https://support.claude.com (Help Center)
- https://alignment.anthropic.com (Alignment Science)
- https://transformer-circuits.pub (Interpretability)
- https://anthropic.skilljar.com (Anthropic Academy)

## Usage

Browse any folder on GitHub, or clone the full archive:

```bash
git clone https://github.com/ai-native-engineer/anthropic-mirror.git
```

## Out of scope

The Claude product app (claude.ai) is not included. Binary assets are excluded except interpretability figures (kept as PNG); video courses and embedded videos are kept as caption transcripts only.

## Updating

Re-crawled and overwritten by the `anthropic-mirror` skill. Only the latest mirror is kept; change history is preserved by git (`git log` / `git diff`). No dated snapshot folders are accumulated.

## Contributing

This archive is generated automatically, so files are not hand-edited - please don't open PRs that change document content (they'd be overwritten on the next sync). Instead:

- Found a broken or missing page? Open an issue.
- Are you the copyright holder requesting removal? Open an issue; the material will be taken down.

## License

No open-source license is granted - all archived text is copyright Anthropic, PBC. This repository is a study / reference mirror, and content is removed on the copyright holder's request.
