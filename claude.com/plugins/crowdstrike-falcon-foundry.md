<!-- source: https://claude.com/plugins/crowdstrike-falcon-foundry -->

# CrowdStrike Falcon Foundry

CrowdStrike Falcon Foundry skills empower you to build apps that extend the Falcon platform.

* Install in

  [Claude Code](#)

  [CrowdStrike](https://www.crowdstrike.com)
* Installs

  684

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Build Falcon Foundry apps from a natural language prompt. Describe what you want, and Claude scaffolds the entire app with the Foundry CLI, imports OpenAPI specs for API integrations, creates Falcon Fusion SOAR workflows in YAML, writes serverless Go or Python functions, builds React or Vue UI pages with the Falcon Shoelace design system, and models collection schemas. Ten specialized skills cover the full app lifecycle from scaffolding through deployment and end-to-end testing.

The plugin enforces platform-specific patterns that are difficult to learn from documentation alone. A CLI guard hook validates commands to prevent common failures like missing --no-prompt flags or manually creating directories that bypass the manifest. A skill router detects Foundry-related intent and loads the right skill before Claude starts working.

**How to use:** Describe the app you want to build. For example: "Create a Falcon Foundry app with an Okta API integration. Share its listUsers endpoint with Falcon Fusion SOAR. Create a workflow to list users on demand, and a UI extension that displays the results." Claude breaks this into capabilities, scaffolds each one with the Foundry CLI, delegates implementation to the appropriate skill, validates the manifest, and deploys to the Falcon console. Each skill includes reference implementations from CrowdStrike's open-source sample apps.

The plugin also covers cross-cutting concerns: OAuth scope hardening and input validation via security patterns, systematic troubleshooting for deploy and manifest errors, and correct patterns for calling Falcon platform APIs from serverless functions using CrowdStrike's gofalcon and FalconPy SDKs.

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
