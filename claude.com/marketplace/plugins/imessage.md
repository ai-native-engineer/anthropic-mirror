<!-- source: https://claude.com/marketplace/plugins/imessage -->

Bridge Claude Code to iMessage on macOS. This plugin reads your local `chat.db` directly and sends replies through AppleScript — no external servers, no tokens, fully local. With built-in access control, you decide exactly who can reach your assistant: allowlist specific contacts by phone number or Apple ID, use code-based pairing for approval, or restrict to self-chat only. Group chats are supported with configurable mention patterns so Claude only responds when addressed.

Security is a core design principle. Access control mutations can only happen through direct terminal invocation, never from incoming messages, preventing prompt-injection attacks. File sending blocks config directory paths, pairing codes expire after one hour, and a static mode locks down access at boot for unattended operation.

**How to use:** After installing, grant your terminal Full Disk Access in macOS System Settings, then run `/imessage:configure` for guided setup. Use `/imessage:access` to manage who can message your assistant — for example, `/imessage:access allow +15551234567` to allowlist a contact, or `/imessage:access policy allowlist` to set the access mode. Once configured, send yourself an iMessage to start chatting with Claude through Messages.app.

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
