<!-- source: https://claude.com/marketplace/plugins/launchdarkly -->

Take control of your code and agents at runtime, right from Claude. The LaunchDarkly plugin connects Claude to LaunchDarkly's hosted MCP server and adds skills for CodeControl and AgentControl, so you can control releases, experiments, and AI behavior in production without leaving your editor.

**CodeControl:** Claude creates feature flags that follow your codebase's existing patterns and wraps new code in them. It manages targeting, rules, and progressive rollouts in each environment. It audits your project for stale or fully launched flags and removes finished flags from your code, using LaunchDarkly as the source of truth so production behavior doesn't change. Metrics skills help you choose the right metric for an experiment or rollout, create it, and add the track() call to your code. The Release Autopilot skill turns on GitHub auto-flagging and auto-releasing, and explains why a pull request wasn't classified.

**AgentControl:** Claude creates and updates configs for your agents, tries different models and prompts as variations, attaches tools for function calling, and targets variations to the right users. It also adds online evals with custom LLM-as-a-judge evaluators so you can watch quality in production.

**How to use:** Install the plugin and sign in to LaunchDarkly when prompted. Then ask Claude what you need, for example "Create a flag for the new checkout flow and wrap the code in it," "Which flags are stale and safe to remove?", "Roll out new-checkout to 10% of users in production," or "Add an online eval to my support-bot agent config." Skills are also available directly as /launchdarkly:<skill-name>.

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
