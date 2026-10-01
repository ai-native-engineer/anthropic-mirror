<!-- source: https://claude.com/marketplace/plugins/agent-sdk-dev -->

A comprehensive development kit for building Claude Agent SDK applications in TypeScript and Python. This plugin streamlines the entire lifecycle of Agent SDK development, from initial project scaffolding to verification against best practices.

Key features include an interactive project creation command that guides you through setup, automatically installs the latest SDK version, configures environment files, and creates working examples tailored to your use case. The plugin also includes verification agents that thoroughly check your application for correct SDK usage patterns, type safety, security practices, and documentation completeness.

**How to use:** Run `/new-sdk-app` to create a new Agent SDK project with interactive prompts for language choice (TypeScript/Python), project name, agent type, and starting point. After development, ask Claude to "Verify my Agent SDK application" to run comprehensive checks and receive a detailed report with recommendations.

The verification agents check SDK installation, environment setup, correct usage patterns, type safety (TypeScript), import structures, error handling, and documentation — providing an overall status of PASS, PASS WITH WARNINGS, or FAIL along with specific recommendations referencing official SDK documentation.

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
