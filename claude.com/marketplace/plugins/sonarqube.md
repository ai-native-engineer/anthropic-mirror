<!-- source: https://claude.com/marketplace/plugins/sonarqube -->

**SonarQube uses multi-layered analysis, built on deterministic verification and complemented by AI-powered capabilities. This allows Sonar to enforce organizational standards consistently, repeatedly, and automatically. The SonarQube plugin applies the same quality standards already governing developer-written code to every line of code Claude produces — 7,500+ rules, secrets scanning, agentic analysis, and quality gates across 40+ languages. With Agentic Analysis enabled, PostToolUse hooks run SonarQube analysis after every file edit, catching issues the moment they're introduced — not after a CI pipeline or pull request. Every file Claude reads and every prompt you enter is automatically scanned for 450+ secrets patterns before content reaches the LLM context window, preventing secrets from ever leaking to the model. Slash commands give you on-demand access to quality gate status, open issues, coverage, duplication metrics, and dependency risks without leaving the terminal.**‍

‍**The Plugin includes: SonarQube CLI, MCP Server, skills, hooks, slash commands, and secrets scanning. Coverage spans code smells, duplication, complexity, SAST, and secrets detection across 40+ languages.**

**‍**‍**How to use:** Run /sonarqube:integrate after installation to walk through setup — CLI installation, authentication, and wiring up the MCP Server and hooks. From there, use slash commands like /sonarqube:quality-gate to check quality gates or interact naturally with prompts like "analyze my code for issues," "show open SonarQube findings," or "check my coverage." With Agentic Analysis enabled, verification happens automatically after each edit with no manual invocation required.**‍**

**Prerequisites:** Requires a SonarQube instance (Server, Cloud, or Community Build). Agentic Analysis requires SonarQube Cloud with those features enabled in your organization’s admin settings.

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
