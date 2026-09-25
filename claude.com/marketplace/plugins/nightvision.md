<!-- source: https://claude.com/marketplace/plugins/nightvision -->

NightVision is a white-box-assisted DAST (Dynamic Application Security Testing) and API Discovery platform that finds exploitable vulnerabilities in web applications and REST APIs. This plugin brings NightVision's security scanning capabilities directly into your development workflow, letting you configure scans, triage findings, discover APIs, and set up CI/CD integrations through natural language.

The plugin provides four core skills. **Scan Configuration** helps you set up DAST scans by creating targets, configuring authentication (Playwright, headers, or cookies), managing projects, recording HTTP traffic for complex workflows, and defining scope exclusions. **Scan Triage** interprets scan results from ZAP and Nuclei engines in SARIF or CSV format, pinpoints vulnerable code using Code Traceback annotations, constructs curl commands for validation, and suggests remediations for issues like SQL injection, XSS, SSRF, and more. **API Discovery** extracts OpenAPI specifications from source code via static analysis across Python, Java, JavaScript, C#, Go, and Ruby frameworks — no running application required — and can diff specs to detect breaking API changes. **CI/CD Integration** generates pipeline configurations for GitHub Actions, GitLab CI, Azure DevOps, Jenkins, BitBucket, and JFrog.

**How to use:** Install the NightVision CLI and authenticate with your API token, then try prompts like: `"Set up a NightVision scan for my web app at https://myapp.com"`, `"Triage the results from my latest NightVision scan"`, `"Extract an OpenAPI spec from this codebase"`, or `"Add NightVision scanning to my GitHub Actions pipeline"`. You can also invoke skills directly with `/scan-configuration`, `/scan-triage`, `/api-discovery`, or `/ci-cd-integration`.

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
