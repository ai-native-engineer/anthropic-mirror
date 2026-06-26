<!-- source: https://claude.com/plugins/pagerduty -->

# PagerDuty Pre-Commit Risk Score

Score pre-commit diffs against PagerDuty incident history and surface deployment risk before you ship.

* Install in

  [Claude Code](#)

  [PagerDuty](https://www.pagerduty.com)
* Installs

  4357

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Assess pre-commit risk by correlating PagerDuty incident history with your current code changes. The `/risk-score` command maps your repo to a PagerDuty service, checks for active incidents, analyzes 90 days of incident history, and identifies correlations between areas you're changing and areas that have caused past incidents.

Outputs a structured risk assessment with a 0-5 score, incident context, structural risk signals, and actionable recommendations. Requires a PagerDuty API key.

**How to use:**

Run `/risk-score` before committing changes to a production service. The plugin checks if there are active P1/P2 incidents on your service and warns you if your changes touch code related to the ongoing incident, helping you avoid making things worse during an outage.

Run `/risk-score` after modifying database migration files or authentication code. The plugin identifies structural risk signals in your diff and cross-references them with past incident patterns, surfacing whether similar changes have preceded incidents in the last 90 days.

Run `/risk-score` on a new repo. The plugin auto-detects your PagerDuty service by matching the repo name, or lets you pick from a list. It caches the mapping so subsequent checks are instant.

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

[### Code Review

AI code review with specialized agents and confidence-based filtering for pull requests

Anthropic verified

383892

installs](/plugins/code-review)

[### Context7

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

377529

installs](/plugins/context7)
