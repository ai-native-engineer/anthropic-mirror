<!-- source: https://claude.com/plugins/remember -->

# Remember

Continuous memory for Claude Code: extracts, summarizes, compresses conversations into tiered daily logs.

* Install in

  [Claude Code](#)

  [Digital Process Tools](https://github.com/Digital-Process-Tools)
* Installs

  39792

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Continuous memory for Claude Code. This plugin automatically captures your sessions, compresses them through Claude Haiku into tiered daily logs, and reloads context when you start a new session. Claude remembers what you worked on yesterday — the files you changed, decisions you made, and where you left off — without any manual effort.

The memory pipeline works in layers: sessions are extracted and filtered, then summarized by Haiku into daily buffers. Hourly compression consolidates same-day entries, and daily consolidation organizes everything into 7-day "recent" and older "archive" files. On session start, relevant memory is automatically injected into Claude's context. You can also define a persistent identity file so Claude maintains consistent personality and conventions across sessions. Typical cost is less than $0.01 per session save.

The plugin installs SessionStart and PostToolUse hooks that run automatically in the background. It includes a Python-based processing pipeline for extraction, summarization, and consolidation, along with shell scripts for orchestration with built-in locking and cooldowns.

**How to use:** After installing, the plugin works automatically — sessions are saved and restored via hooks with no manual intervention needed. Use the `/remember` slash command to create a concise handoff document capturing your current project state, next steps, and important context for the next session. Example prompts: `/remember` to save a handoff before ending your session, or simply start a new session and Claude will already have context from your previous work.

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
