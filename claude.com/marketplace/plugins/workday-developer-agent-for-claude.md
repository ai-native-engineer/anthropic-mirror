<!-- source: https://claude.com/marketplace/plugins/workday-developer-agent-for-claude -->

The Workday Developer Agent plugin lets developers use Workday Developer Agent from Claude Code. Workday Developer Agent is Workday’s purpose-built agent for developing Workday Extend apps. When you ask Claude to create, scaffold, edit or fix an Extend app in a project you have open in VS Code or Cursor, Claude hands the task to the Developer Agent, which does the file work.

The agent runs in the Developer Agent panel in your IDE, where you see the live session and approve or reject every gated edit. Claude then summarizes what changed. The plugin includes a skill that tells Claude when to delegate, a local MCP server started through the Workday CLI (wdcli), a session start hook that checks whether you opened Claude Code in an Extend project, and a /dev-agent-doctor command that checks your wdcli install, sign-in and IDE extension.

**How to use:**
You need a Workday Developer Platform account. Download and install the Workday Developer CLI (wdcli) from the Workday Developer Portal and sign in, install the Workday Developer Agent extension in VS Code or Cursor and sign in, then install this plugin in Claude Code. Open an Extend project in your IDE and ask Claude for the change you want. Try “Scaffold a new page in my Extend app”, “Add a business object”, or “Fix this WQL query”. If the agent isn’t reachable, run /dev-agent-doctor.

## Other plugins

### [Frontend Design](https://claude.com/marketplace/plugins/frontend-design)

Frontend design skill for UI/UX implementation

### [Superpowers](https://claude.com/marketplace/plugins/superpowers)

Core skills library for Claude Code: TDD, debugging, collaboration patterns, and proven techniques

### [Code Review](https://claude.com/marketplace/plugins/code-review)

Automated code review for pull requests using multiple specialized agents with confidence-based scoring

### [Context7](https://claude.com/marketplace/plugins/context7)

Upstash Context7 MCP server for up-to-date documentation lookup. Connects to Context7's hosted remote MCP server (https://mcp.context7.com/mcp) — no local Node.js or npx required — to pull version-specific documentation and code examples directly from source repositories into your LLM context. Authenticate with Context7 when prompted.

### [Code Simplifier](https://claude.com/marketplace/plugins/code-simplifier)

Agent that simplifies and refines code for clarity, consistency, and maintainability while preserving functionality

### [Playwright](https://claude.com/marketplace/plugins/playwright)

Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, click elements, and perform automated browser testing workflows.
