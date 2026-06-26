<!-- source: https://claude.com/plugins/nightvision -->

# NightVision

NightVision: DAST/API Discovery platform finding exploitable vulnerabilities in web applications and APIs

* Install in

  [Claude Code](#)

  [NightVision Engineering](https://www.nightvision.net)
* Installs

  1729

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

NightVision is a white-box-assisted DAST (Dynamic Application Security Testing) and API Discovery platform that finds exploitable vulnerabilities in web applications and REST APIs. This plugin brings NightVision's security scanning capabilities directly into your development workflow, letting you configure scans, triage findings, discover APIs, and set up CI/CD integrations through natural language.

The plugin provides four core skills. **Scan Configuration** helps you set up DAST scans by creating targets, configuring authentication (Playwright, headers, or cookies), managing projects, recording HTTP traffic for complex workflows, and defining scope exclusions. **Scan Triage** interprets scan results from ZAP and Nuclei engines in SARIF or CSV format, pinpoints vulnerable code using Code Traceback annotations, constructs curl commands for validation, and suggests remediations for issues like SQL injection, XSS, SSRF, and more. **API Discovery** extracts OpenAPI specifications from source code via static analysis across Python, Java, JavaScript, C#, Go, and Ruby frameworks — no running application required — and can diff specs to detect breaking API changes. **CI/CD Integration** generates pipeline configurations for GitHub Actions, GitLab CI, Azure DevOps, Jenkins, BitBucket, and JFrog.

**How to use:** Install the NightVision CLI and authenticate with your API token, then try prompts like: `"Set up a NightVision scan for my web app at https://myapp.com"`, `"Triage the results from my latest NightVision scan"`, `"Extract an OpenAPI spec from this codebase"`, or `"Add NightVision scanning to my GitHub Actions pipeline"`. You can also invoke skills directly with `/scan-configuration`, `/scan-triage`, `/api-discovery`, or `/ci-cd-integration`.

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
