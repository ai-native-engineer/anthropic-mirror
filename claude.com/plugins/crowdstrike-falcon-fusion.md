<!-- source: https://claude.com/plugins/crowdstrike-falcon-fusion -->

# CrowdStrike Falcon Fusion

CrowdStrike Falcon Fusion skills for authoring, deploying, and executing Fusion workflows. Includes live action discovery, YAML authoring with schema validation, workflow import and release, execution monitoring, and Falcon Next-Gen SIEM lookup files.

* Install in

  [Claude Code](#)

  [CrowdStrike](https://www.crowdstrike.com)
* Installs

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Build CrowdStrike Falcon Fusion SOAR workflows directly from Claude Code. Six skills cover the full workflow lifecycle: discover available Fusion actions live from your CID's API, author workflow YAML validated against the Charlotte JSON schema, import and release workflow versions, trigger executions and monitor or debug them, and manage Falcon Next-Gen SIEM lookup files for CQL match() queries. A setup skill walks through Falcon API credential configuration on first run.

The plugin ships fifteen grounded use-case patterns the orchestrator matches your request against — enriching a detection's indicators with VirusTotal and tagging the case, gating device containment behind analyst approval on high-severity detections, paging through REST APIs inside a workflow, deduplicating Next-Gen SIEM detections, sending workflow notifications to a chat channel, and invoking a published Charlotte AI agent when a detection fires. Each pattern cites the CrowdStrike Tech Hub article or bundled example workflow it is grounded in.

**How to use:** Try prompts like "Create a Fusion workflow that enriches new detections with VirusTotal and comments the case", "Import this workflow into my CID and release it", "Run my containment workflow and tail the execution", or "Create a lookup file of known-bad domains for my CQL match() queries".

Requires a CrowdStrike Falcon subscription with API access; a companion plugin, crowdstrike-falcon-foundry, covers Falcon Foundry app development.

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
