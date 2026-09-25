<!-- source: https://claude.com/marketplace/plugins/remember -->

Continuous memory for Claude Code. This plugin automatically captures your sessions, compresses them through Claude Haiku into tiered daily logs, and reloads context when you start a new session. Claude remembers what you worked on yesterday — the files you changed, decisions you made, and where you left off — without any manual effort.

The memory pipeline works in layers: sessions are extracted and filtered, then summarized by Haiku into daily buffers. Hourly compression consolidates same-day entries, and daily consolidation organizes everything into 7-day "recent" and older "archive" files. On session start, relevant memory is automatically injected into Claude's context. You can also define a persistent identity file so Claude maintains consistent personality and conventions across sessions. Typical cost is less than $0.01 per session save.

The plugin installs SessionStart and PostToolUse hooks that run automatically in the background. It includes a Python-based processing pipeline for extraction, summarization, and consolidation, along with shell scripts for orchestration with built-in locking and cooldowns.

**How to use:** After installing, the plugin works automatically — sessions are saved and restored via hooks with no manual intervention needed. Use the `/remember` slash command to create a concise handoff document capturing your current project state, next steps, and important context for the next session. Example prompts: `/remember` to save a handoff before ending your session, or simply start a new session and Claude will already have context from your previous work.

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
