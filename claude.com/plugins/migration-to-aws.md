<!-- source: https://claude.com/plugins/migration-to-aws -->

# Migration to AWS

Assess cloud usage/billing, compare AWS services/pricing, recommend migration or continued use of current provider.

* Install in

  [Claude Code](#)

  [Amazon Web Services](https://aws.amazon.com)
* Installs

  1938

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Provides a structured, five-phase workflow for migrating cloud infrastructure from Google Cloud Platform to Amazon Web Services. The plugin analyzes your existing Terraform-defined GCP resources, maps them to AWS equivalents using a re-platform strategy, estimates costs with live AWS pricing data, and produces a detailed execution plan with risk mitigation and rollback strategies.

The migration workflow progresses through five phases: **Discover** (parse Terraform files to inventory GCP resources), **Clarify** (gather migration requirements via a structured questionnaire), **Design** (map each GCP service to its AWS equivalent, e.g. Cloud Run to Fargate, Cloud SQL to RDS), **Estimate** (project monthly AWS costs with ROI analysis), and **Execute** (create an implementation timeline with risk register). Progress is tracked across sessions in timestamped migration directories so you can resume where you left off.

Connects to two MCP servers for enhanced accuracy: **AWS Pricing** for real-time cost data (with offline fallback) and **AWS Knowledge** for service documentation, regional availability, and architecture best practices.

**How to use:** Point the plugin at a project containing Terraform files (`.tf`) and use prompts like `"Migrate my GCP infrastructure to AWS"`, `"Move off Google Cloud"`, `"Migrate Cloud SQL to RDS"`, `"Migrate GKE to EKS"`, or `"Estimate the cost of moving our Google Cloud setup to AWS"`. The plugin will guide you through each phase interactively, asking clarifying questions about scope, compliance, and budget before producing architecture mappings and cost estimates.

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
