<!-- source: https://claude.com/marketplace/plugins/opsera-devsecops -->

AI-powered DevSecOps agent that analyzes your codebase for security vulnerabilities, architectural risks, and compliance gaps. Connects to Opsera's cloud platform via MCP to deliver risk-focused architecture analysis, vulnerability scanning with secret detection, evidence-based compliance auditing across SOC2/HIPAA/PCI-DSS/ISO 27001 frameworks, and SQL injection detection with automated fixes. Includes a pre-commit security gate that automatically scans staged changes and blocks commits with critical or high-severity issues.

The plugin provides four core analysis tools — each producing detailed findings with severity ratings and actionable remediation steps. Architecture analysis examines auth routes, failure modes, and generates quantified architecture diagrams. Security scanning covers SAST, container security, infrastructure-as-code checks, and secret detection. Compliance auditing maps your codebase against regulatory frameworks and produces remediation roadmaps. SQL security discovers PII exposure, privilege escalation risks, and offers AI-powered auto-fix suggestions.

**How to use:** Run `/architecture-analyze` to perform a risk-focused review of your system design. Use `/security-scan` to scan for vulnerabilities and secrets across your codebase. Run `/compliance-audit` to assess alignment with SOC2, HIPAA, PCI-DSS, or ISO 27001 standards. Use `/sql-security` to detect SQL injection risks and PII exposure. You can also use natural language — try "analyze the architecture of this project for risks" or "audit this repo for HIPAA compliance." The pre-commit security gate runs automatically before git commits to catch issues early.

Requires an Opsera account (free trial available). No source code is transmitted — only anonymous usage metadata is reported to the Opsera analytics dashboard.

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
