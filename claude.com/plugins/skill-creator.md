<!-- source: https://claude.com/plugins/skill-creator -->

# Skill Creator

Create, improve, and measure skills. Use for creating, updating, evaluating, and benchmarking performance.

* Anthropic Verified
* Install in

  [Claude Code](#)

  [Anthropic](https://anthropic.com)
* Installs

  324277

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Skill Creator is a comprehensive toolkit for developing, testing, and iterating on Claude Code skills. It provides four operating modes — Create, Eval, Improve, and Benchmark — that guide you through the full skill development lifecycle, from initial concept to optimized, production-ready skills.

Under the hood, four composable agents handle specialized tasks: an **Executor** that runs skills against eval prompts, a **Grader** that evaluates outputs against defined expectations, a **Comparator** that performs blind A/B comparisons between skill versions, and an **Analyzer** that suggests targeted improvements based on results. Together, these agents enable rigorous, data-driven skill refinement.

The plugin also includes utility scripts for initializing skills, validating configurations, preparing evaluations, and aggregating benchmark results with variance analysis — so you can measure performance with statistical confidence.

**How to use:** Invoke the skill with `/skill-creator` and choose a mode. Try prompts like: "Create a new skill that reviews PRs for security issues," "Run evals on my code-review skill," "Improve my deploy skill based on these test cases," or "Benchmark my skill across 10 runs and show variance." The interactive workflow will guide you through requirements gathering, test case creation, and iterative optimization.

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
