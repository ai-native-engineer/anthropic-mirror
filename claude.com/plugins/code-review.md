<!-- source: https://claude.com/plugins/code-review -->

# Code Review

AI code review with specialized agents and confidence-based filtering for pull requests

* Anthropic Verified
* Install in

  [Claude Code](#)

  [Anthropic](https://anthropic.com)
* Installs

  383892

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Automates pull request code review using multiple specialized agents working in parallel. Five independent reviewers analyze your changes from different angles: CLAUDE.md compliance checking, bug detection, git history context analysis, previous PR comment review, and code comment verification. Each finding is scored on a 0-100 confidence scale, and only high-confidence issues (default threshold: 80) are posted as comments, dramatically reducing false positives and review noise.

The plugin intelligently filters out PRs that don't need review—closed, draft, automated, or already-reviewed pull requests are automatically skipped. Comments include direct GitHub links with full SHA hashes and line number ranges for easy navigation to the exact code in question.

**How to use:** Run `/code-review` on any PR branch to launch the full automated review. The system will analyze your changes, score potential issues, and post actionable feedback directly to GitHub. You can customize the confidence threshold or focus areas (security, performance, accessibility) by editing the command configuration.

## Related plugins

[### Frontend Design

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

Anthropic verified

948012

installs](/plugins/frontend-design)

[### Superpowers

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

855112

installs](/plugins/superpowers)

[### Context7

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

377529

installs](/plugins/context7)

[### Skill Creator

Create, improve, and measure skills. Use for creating, updating, evaluating, and benchmarking performance.

Anthropic verified

324277

installs](/plugins/skill-creator)
