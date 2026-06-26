<!-- source: https://claude.com/plugins/opsera-devsecops -->

# Opsera DevSecOps

Opsera DevSecOps Agent — AI-powered architecture analysis, security scanning, compliance auditing, and SQL security f...

* Install in

  [Claude Code](#)

  [Opsera](https://agent.opsera.ai)
* Installs

  1365

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

AI-powered DevSecOps agent that analyzes your codebase for security vulnerabilities, architectural risks, and compliance gaps. Connects to Opsera's cloud platform via MCP to deliver risk-focused architecture analysis, vulnerability scanning with secret detection, evidence-based compliance auditing across SOC2/HIPAA/PCI-DSS/ISO 27001 frameworks, and SQL injection detection with automated fixes. Includes a pre-commit security gate that automatically scans staged changes and blocks commits with critical or high-severity issues.

The plugin provides four core analysis tools — each producing detailed findings with severity ratings and actionable remediation steps. Architecture analysis examines auth routes, failure modes, and generates quantified architecture diagrams. Security scanning covers SAST, container security, infrastructure-as-code checks, and secret detection. Compliance auditing maps your codebase against regulatory frameworks and produces remediation roadmaps. SQL security discovers PII exposure, privilege escalation risks, and offers AI-powered auto-fix suggestions.

**How to use:** Run `/architecture-analyze` to perform a risk-focused review of your system design. Use `/security-scan` to scan for vulnerabilities and secrets across your codebase. Run `/compliance-audit` to assess alignment with SOC2, HIPAA, PCI-DSS, or ISO 27001 standards. Use `/sql-security` to detect SQL injection risks and PII exposure. You can also use natural language — try "analyze the architecture of this project for risks" or "audit this repo for HIPAA compliance." The pre-commit security gate runs automatically before git commits to catch issues early.

Requires an Opsera account (free trial available). No source code is transmitted — only anonymous usage metadata is reported to the Opsera analytics dashboard.

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
