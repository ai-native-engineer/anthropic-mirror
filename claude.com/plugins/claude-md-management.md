<!-- source: https://claude.com/plugins/claude-md-management -->

# CLAUDE.md Management

Tools to maintain CLAUDE.md - audit quality, capture learnings, and keep project memory current.

* Anthropic Verified
* Install in

  [Claude Code](#)

  [Anthropic](https://anthropic.com)
* Installs

  250441

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Keep your project memory fresh and effective. This plugin provides tools to audit CLAUDE.md file quality and capture session learnings, ensuring Claude always has the context it needs to work efficiently in your codebase.

The **claude-md-improver** skill scans your repository for all CLAUDE.md files, evaluates them against quality criteria (commands, architecture, gotchas, conciseness), and generates a detailed quality report with scores and grades. It then proposes targeted additions based on gaps it discovers.

The **/revise-claude-md** command helps you capture learnings at the end of a session—bash commands discovered, code patterns followed, environment quirks encountered—and suggests updates to the appropriate CLAUDE.md or .claude.local.md file.

**How to use:**

Say "audit my CLAUDE.md files" or "check if my CLAUDE.md is up to date" to trigger the audit skill. Run `/revise-claude-md` after a productive session to capture new insights. The plugin will show you proposed changes as diffs and only apply them with your approval.

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
