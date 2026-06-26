<!-- source: https://claude.com/plugins/imessage -->

# iMessage

iMessage messaging bridge with built-in access control. Reads chat.db directly, sends via AppleScript. Manage pairing...

* Install in

  [Claude Code](#)

  [Anthropic](https://anthropic.com)
* Installs

  13780

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Bridge Claude Code to iMessage on macOS. This plugin reads your local `chat.db` directly and sends replies through AppleScript — no external servers, no tokens, fully local. With built-in access control, you decide exactly who can reach your assistant: allowlist specific contacts by phone number or Apple ID, use code-based pairing for approval, or restrict to self-chat only. Group chats are supported with configurable mention patterns so Claude only responds when addressed.

Security is a core design principle. Access control mutations can only happen through direct terminal invocation, never from incoming messages, preventing prompt-injection attacks. File sending blocks config directory paths, pairing codes expire after one hour, and a static mode locks down access at boot for unattended operation.

**How to use:** After installing, grant your terminal Full Disk Access in macOS System Settings, then run `/imessage:configure` for guided setup. Use `/imessage:access` to manage who can message your assistant — for example, `/imessage:access allow +15551234567` to allowlist a contact, or `/imessage:access policy allowlist` to set the access mode. Once configured, send yourself an iMessage to start chatting with Claude through Messages.app.

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
