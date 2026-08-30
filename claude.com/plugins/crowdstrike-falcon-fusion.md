<!-- source: https://claude.com/plugins/crowdstrike-falcon-fusion -->

# CrowdStrike Falcon Fusion

CrowdStrike Falcon Fusion skills automate standalone SOAR workflow creation, from action discovery through deployment and execution. Search the live platform action catalog, author validated YAML with correct IDs and schema, import workflows to a CID, release them, trigger execution with payloads, and manage Falcon Next-Gen SIEM lookup files.

* Install in

  [Claude Code](#)

  [CrowdStrike](https://www.crowdstrike.com)
* Installs

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Build Falcon Fusion workflows from a natural language prompt. Describe what you want to automate, and Claude discovers real action IDs from the live API, authors workflow YAML with correct schema and CEL expressions, validates against the Charlotte JSON schema, imports the workflow to your CID, releases it, and triggers execution. Five specialized skills cover the full lifecycle: orchestration, authoring, deployment, execution, and lookup file management.

The plugin enforces discipline that prevents common failures. Action IDs are 32-character hex values only discoverable via live API search. The plugin never uses placeholders or guessed values. Every action gets a version constraint. YAML is validated locally before import, catching errors that would otherwise surface only at deploy time. A skill router hook detects workflow intent and loads the correct skill before Claude starts working.

**How to use:** Describe the workflow you want to build. For example: "Generate a Falcon Fusion workflow that will trigger from a Falcon Next-Gen SIEM detection. The workflow should hydrate the detection using an event query to get the full details of the detection. If a user, host, domain, url, file indicator, or ip indicator is found, enrich each in parallel using HTTP calls to VirusTotal or DomainTools. Summarize the enrichment across all the threat intelligence providers using an LLM completion action and then send an email formatted in HTML." Claude searches the action catalog for the right platform actions, resolves their IDs and parameters, authors the YAML with correct trigger configuration and CEL expressions, validates it, imports it to your CID, and releases it for execution. The plugin includes 25 production-grade example workflows from CrowdStrike's Content Library as reference implementations.

The plugin also handles adjacent concerns: HTTP actions that call external APIs (VirusTotal, Slack, PagerDuty) with credential config references, inline Python scripts that run directly in the workflow engine, schemaless event queries using CQL/FQL, loop and conditional patterns, and Falcon Next-Gen SIEM lookup files for threat hunting enrichment via CQL match() queries.

## Related plugins

[### Frontend Design

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

Anthropic verified

1134112

installs](https://claude.com/plugins/frontend-design)

[### Superpowers

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

1009371

installs](https://claude.com/plugins/superpowers)

[### Code Review

AI code review with specialized agents and confidence-based filtering for pull requests

Anthropic verified

438525

installs](https://claude.com/plugins/code-review)

[### Context7

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

417801

installs](https://claude.com/plugins/context7)
