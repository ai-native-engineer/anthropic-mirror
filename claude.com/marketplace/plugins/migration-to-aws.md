<!-- source: https://claude.com/marketplace/plugins/migration-to-aws -->

Provides a structured, five-phase workflow for migrating cloud infrastructure from Google Cloud Platform to Amazon Web Services. The plugin analyzes your existing Terraform-defined GCP resources, maps them to AWS equivalents using a re-platform strategy, estimates costs with live AWS pricing data, and produces a detailed execution plan with risk mitigation and rollback strategies.

The migration workflow progresses through five phases: **Discover** (parse Terraform files to inventory GCP resources), **Clarify** (gather migration requirements via a structured questionnaire), **Design** (map each GCP service to its AWS equivalent, e.g. Cloud Run to Fargate, Cloud SQL to RDS), **Estimate** (project monthly AWS costs with ROI analysis), and **Execute** (create an implementation timeline with risk register). Progress is tracked across sessions in timestamped migration directories so you can resume where you left off.

Connects to two MCP servers for enhanced accuracy: **AWS Pricing** for real-time cost data (with offline fallback) and **AWS Knowledge** for service documentation, regional availability, and architecture best practices.

**How to use:** Point the plugin at a project containing Terraform files (`.tf`) and use prompts like `"Migrate my GCP infrastructure to AWS"`, `"Move off Google Cloud"`, `"Migrate Cloud SQL to RDS"`, `"Migrate GKE to EKS"`, or `"Estimate the cost of moving our Google Cloud setup to AWS"`. The plugin will guide you through each phase interactively, asking clarifying questions about scope, compliance, and budget before producing architecture mappings and cost estimates.

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
