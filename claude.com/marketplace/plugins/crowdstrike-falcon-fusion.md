<!-- source: https://claude.com/marketplace/plugins/crowdstrike-falcon-fusion -->

Build Falcon Fusion workflows from a natural language prompt. Describe what you want to automate, and Claude discovers real action IDs from the live API, authors workflow YAML with correct schema and CEL expressions, validates against the Charlotte JSON schema, imports the workflow to your CID, releases it, and triggers execution. Five specialized skills cover the full lifecycle: orchestration, authoring, deployment, execution, and lookup file management.

The plugin enforces discipline that prevents common failures. Action IDs are 32-character hex values only discoverable via live API search. The plugin never uses placeholders or guessed values. Every action gets a version constraint. YAML is validated locally before import, catching errors that would otherwise surface only at deploy time. A skill router hook detects workflow intent and loads the correct skill before Claude starts working.

**How to use:** Describe the workflow you want to build. For example: "Generate a Falcon Fusion workflow that will trigger from a Falcon Next-Gen SIEM detection. The workflow should hydrate the detection using an event query to get the full details of the detection. If a user, host, domain, url, file indicator, or ip indicator is found, enrich each in parallel using HTTP calls to VirusTotal or DomainTools. Summarize the enrichment across all the threat intelligence providers using an LLM completion action and then send an email formatted in HTML." Claude searches the action catalog for the right platform actions, resolves their IDs and parameters, authors the YAML with correct trigger configuration and CEL expressions, validates it, imports it to your CID, and releases it for execution. The plugin includes 25 production-grade example workflows from CrowdStrike's Content Library as reference implementations.

The plugin also handles adjacent concerns: HTTP actions that call external APIs (VirusTotal, Slack, PagerDuty) with credential config references, inline Python scripts that run directly in the workflow engine, schemaless event queries using CQL/FQL, loop and conditional patterns, and Falcon Next-Gen SIEM lookup files for threat hunting enrichment via CQL match() queries.

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
