<!-- source: https://claude.com/resources/guides/the-ai-investment-firm/the-claude-stack-on-the-buy-side -->

Chapter 164 min read

# The Claude stack on the buy side

4 min read

6 min remaining

Different teams or groups within a firm work with different Claude products: Claude Code for everyone who writes code, the Claude app and Claude for Microsoft 365 for investment and operations staff, Claude Enterprise with financial-data connectors for research, and the Claude Agent SDK (software development kit) for the agents the firm builds itself.

## Claude products

### Claude Code

Engineers work with Claude Code in the firm’s codebase from the terminal, a code editor, the browser, or Slack. They ask it to map a repository or modernize legacy code, and it can turn a ticket into a pull request with changes across many files.

### Claude and Claude Enterprise

In Claude Enterprise, teams ask questions across the firm’s research, data, and documents and get answers with citations. Analysts ask Claude to get them up to speed on a name or draft a first take. Claude can also take on longer tasks as an agent when someone gives it a goal, such as the overnight earnings run or a due-diligence questionnaire. It shows each step as it works across files and the browser, and it can run tasks on a schedule. On Enterprise plans, an owner turns on cloud sessions for the teams that need them, so scheduled tasks can run overnight with no one at a desk. Anthropic’s financial services plugins add finance skills and connectors for data providers such as FactSet, S&P Global, LSEG, Morningstar, PitchBook, and Moody’s, though each provider may require its own subscription. Other connectors link Claude to Snowflake, Databricks, and the firm’s own systems through the Model Context Protocol (MCP).

### Claude for Microsoft 365

Claude for Microsoft 365 works inside Excel, PowerPoint, and Word. It builds and edits models while keeping formula relationships intact, cites the cells behind its answers, and traces errors to their root cause. When an analyst moves from the model to a memo or a deck, Claude keeps the context.

### Claude Design and Claude Slides

From a person’s description, Claude Design builds a first draft of a one-pager or prototype on the firm’s design system. For presentations, Claude Slides drafts the deck from notes, reports, or earlier work in a conversation. Drafts from either can be exported to PowerPoint or PDF. Both are in beta, and Enterprise admins choose when to turn them on.

### Claude Agent SDK and Claude Managed Agents

The Claude Agent SDK packages the agent loop behind Claude Code as a library, so the firm’s developers can build their own agents for research, risk, reconciliation, or surveillance that work with the firm’s data and follow its methods. The firm can run those agents in its own environment or have Anthropic host them through Claude Managed Agents (beta).

### Claude Tag: @Claude in Slack

Claude Tag (beta) brings Claude into Slack threads, where several people can work with it at once. Engineers can tag in Claude and the principal engineers involved to triage a break, and an investment team can work through an idea together. Claude reads the thread, answers with the firm’s data, takes on longer tasks, and posts updates in the thread.

### Open-source plugins

Anthropic publishes plugins for financial services (equity research, financial analysis, private equity, and fund administration), for legal and finance teams, and for code modernization. Each one is a starting point that the firm can adapt to its house methods.
