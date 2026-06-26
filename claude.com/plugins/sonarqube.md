<!-- source: https://claude.com/plugins/sonarqube -->

# sonarqube

Automatically enforce SonarQube code quality and security in the agent coding loop.

* Install in

  [Claude Code](#)

  [SonarSource](#)
* Installs

  4444

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

**SonarQube uses multi-layered analysis, built on deterministic verification and complemented by AI-powered capabilities. This allows Sonar to enforce organizational standards consistently, repeatedly, and automatically. The SonarQube plugin applies the same quality standards already governing developer-written code to every line of code Claude produces — 7,500+ rules, secrets scanning, agentic analysis, and quality gates across 40+ languages. With Agentic Analysis enabled, PostToolUse hooks run SonarQube analysis after every file edit, catching issues the moment they're introduced — not after a CI pipeline or pull request. Every file Claude reads and every prompt you enter is automatically scanned for 450+ secrets patterns before content reaches the LLM context window, preventing secrets from ever leaking to the model. Slash commands give you on-demand access to quality gate status, open issues, coverage, duplication metrics, and dependency risks without leaving the terminal.**‍

‍**The Plugin includes: SonarQube CLI, MCP Server, skills, hooks, slash commands, and secrets scanning. Coverage spans code smells, duplication, complexity, SAST, and secrets detection across 40+ languages.**

**‍**‍**How to use:** Run /sonarqube:integrate after installation to walk through setup — CLI installation, authentication, and wiring up the MCP Server and hooks. From there, use slash commands like /sonarqube:quality-gate to check quality gates or interact naturally with prompts like "analyze my code for issues," "show open SonarQube findings," or "check my coverage." With Agentic Analysis enabled, verification happens automatically after each edit with no manual invocation required.**‍**

**Prerequisites:** Requires a SonarQube instance (Server, Cloud, or Community Build). Agentic Analysis requires SonarQube Cloud with those features enabled in your organization’s admin settings.

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
