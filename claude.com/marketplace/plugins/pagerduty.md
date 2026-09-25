<!-- source: https://claude.com/marketplace/plugins/pagerduty -->

Assess pre-commit risk by correlating PagerDuty incident history with your current code changes. The `/risk-score` command maps your repo to a PagerDuty service, checks for active incidents, analyzes 90 days of incident history, and identifies correlations between areas you're changing and areas that have caused past incidents.

Outputs a structured risk assessment with a 0-5 score, incident context, structural risk signals, and actionable recommendations. Requires a PagerDuty API key.

**How to use:**

Run `/risk-score` before committing changes to a production service. The plugin checks if there are active P1/P2 incidents on your service and warns you if your changes touch code related to the ongoing incident, helping you avoid making things worse during an outage.

Run `/risk-score` after modifying database migration files or authentication code. The plugin identifies structural risk signals in your diff and cross-references them with past incident patterns, surfacing whether similar changes have preceded incidents in the last 90 days.

Run `/risk-score` on a new repo. The plugin auto-detects your PagerDuty service by matching the repo name, or lets you pick from a list. It caches the mapping so subsequent checks are instant.

## Other plugins

### [Frontend Design](https://claude.com/marketplace/plugins/frontend-design)

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

### [Superpowers](https://claude.com/marketplace/plugins/superpowers)

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

### [Code Review](https://claude.com/marketplace/plugins/code-review)

AI code review with specialized agents and confidence-based filtering for pull requests

### [Context7](https://claude.com/marketplace/plugins/context7)

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

### [Code Simplifier](https://claude.com/marketplace/plugins/code-simplifier)

Code clarity agent: simplifies and refines recently modified code while preserving functionality and consistency.

### [Playwright](https://claude.com/marketplace/plugins/playwright)

Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, and automate testing workflows.
