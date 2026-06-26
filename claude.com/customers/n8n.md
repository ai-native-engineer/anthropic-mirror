<!-- source: https://claude.com/customers/n8n -->

Case study | Claude Platform

# n8n turns natural language into workflow automations with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/699f5640b0f641d11bbdf28d_logo_n8n-light-mode.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/699f56448e874b3e8f600712_logo_n8n-dark-mode.svg)

Industry:

Software

Company size:

Medium

Product:

Location:

EMEA

2 months

From concept to first production of the AI Workflow Builder, powered by Claude

Cuts 80% of the work

out of building a workflow, leaving engineers to handle the final refinements

Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525504b02eec936ac51b_68c469d41149ace562bfd24d_og-claude-product-claude-code.jpeg)

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Read more

[Read more](/product/claude-code)Read more

Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Developer Platform

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f5266ed232fd1354625a6_68c469d18f61fb5c21c81781_og-claude-api.jpeg)

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

Read more

[Read more](/platform/api)Read more

Developer Platform

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Developer Platform

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

[Prev](#)Prev

[Next](#)Next

[n8n](https://n8n.io) empowers technical teams to build, orchestrate, and deploy reliable AI workflows and agents, combining the speed of a visual builder with the flexibility of custom code. Their platform has earned more than 170,000 GitHub stars, putting it in the top 50 projects of all time, and customers span from solo founders to Fortune 100 companies.

**With Claude, n8n:**

* Built its AI Workflow Builder product on Claude in two months from concept to production, with the architecture since evolving into a multi-agent system with specialized agents managing different tasks
* Developed a chat-based workflow creator and debugger that replaces the two-tab workflow of switching between an LLM and the n8n interface
* Cuts 80% of the work out of building a workflow, leaving engineers to handle the final refinements
* Built reliable function calling for complex multi-step workflow assembly, with Claude performing best among other models for precise instruction following

## The challenge: Getting a model to generate a precise structured format

Before n8n built its AI Workflow Builder, many users had a familiar two-tab setup: n8n on one side, a chat-based LLM on the other. They'd describe what they wanted to automate, copy a suggested workflow, paste it into n8n, hit an error, and repeat. It worked, but the external model lacked context about what was actually happening inside the tool.

n8n had been shipping AI features since 2023. But the next step was more ambitious: what if building a workflow felt like having a conversation?

The challenge was structural. An n8n workflow is a precise object: nodes that need to be found, connected in a specific order, and configured with the right parameters. The team's first approach was to have the model generate the workflow's underlying JSON directly. "That turned out to be quite a big challenge for models," said JP van Oosten, Engineering Manager of n8n's AI team. Generating a complete workflow in one shot required the model to understand the full schema, all node definitions, and all connection logic simultaneously. "These models haven't seen more than maybe 10,000 n8n workflows, compared to millions of TypeScript code files," van Oosten said.

## Selecting Claude for precise instruction following

To solve the JSON generation problem, the team shifted to a tool-based architecture where Claude adds nodes one at a time, connects them, and configures them through discrete function calls. This played to the model's strengths and made the process, as van Oosten described it, "much more digestible for the model."

The team evaluated multiple models. Claude stood out in particular for instruction following. Other models either over-relied on function calls or ignored them entirely. Claude sat in what the team called a "sweet spot": consistently following instructions while using tools as intended.

"Latency and quality were really good,” said Oleg Ivaniv, Lead Engineer on the AI Workflow Builder. “Workflows can be a bit of a challenge to understand.”

Claude's documentation also helped with specifics like prompt caching, and Anthropic's team reviewed n8n's implementation to ensure the launch went smoothly from a rate-limiting perspective. The first iteration of the AI Workflow Builder took roughly two months from concept to production.

## The results: How n8n assembles workflows through conversation

The AI Workflow Builder gives n8n users something familiar, a chat interface, to do something that used to require understanding node types, connection logic, and configuration options. Users describe what they want to automate, and Claude figures out which pieces to assemble and how. The first generation of a workflow typically takes three minutes instead of the usual 10-30 minutes it takes to build one manually.

"Tool calling is top-notch in Claude, as well as its coding capabilities," van Oosten said. "These are essential to our approach in the AI Workflow Builder."

The clearest before-and-after is the two-tab experience. Users who previously moved back and forth between n8n and an external LLM now have that conversation inside the product. The AI Workflow Builder has context about what's actually happening in their workflow, which makes errors more diagnosable and suggestions more relevant. "Claude has enabled us to provide a familiar chat-based interface to go from idea to fully functional workflows," van Oosten said.

Since launch, the architecture has evolved into a multi-agent system where specialized agents manage different parts of the workflow creation process. The team's prompts are now heavily tailored to Claude Sonnet 4.5, and early experiments with a code-based approach, where Claude generates code rather than making tool calls, have shown promising results with more capable models.

For experienced users, the value is speed. The AI Workflow Builder delivers roughly 80% of a target workflow without manual assembly, so engineers can focus on refinement rather than construction. For first-time users, the value is different. n8n has thousands of templates, but its strength is flexibility, and many users choose the platform for unique use cases that templates don't cover. The AI Workflow Builder gives them a starting point. "It helps first-time users get over that initial mental hump of 'I don't know what I don't know,'" said Ophir Prusak, from the Product Marketing team.

The same interface also helps users debug: when a workflow breaks, they can describe the problem and get help fixing it, rather than relying purely on  documentation or community forums. The team recently saw this play out internally when the AI Workflow Builder assembled a complex workflow for tracking engineering progress. It correctly used multiple form nodes on the first attempt, a result van Oosten attributed to the team's ongoing work on optimizing prompts for specific node types.

## Future use cases

Looking ahead, the team is exploring whether building node-by-node or subgraph-by-subgraph, mirroring how experienced users actually construct automations, might offer a tighter feedback loop during the creation process. The current version presents a completed workflow at the end; a more incremental approach could let users shape it as it takes form.

n8n is continuing to expand the AI Workflow Builder's capabilities and deepen its work with Claude. The multi-agent architecture opens up new possibilities for handling increasingly complex automation requests, and the team's experiments with code-based generation suggest further quality improvements ahead.

"The AI Workflow Builder allows us to lower the bar to entry for users to start building with n8n,” van Oosten said, “but also allows more technical users to iterate faster on their ideas.”

‍

‍

‍

"Tool calling is top-notch in Claude, as well as its coding capabilities."

JP van Oosten

AI Engineering Manager, n8n

AI agents

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f5244ff22e3ab8e64404d_68c469d3872afd7941c5e6f2_og-claude-agents.jpeg)

Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

AI agents

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

AI agents

Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

[Prev](#)Prev

[Next](#)Next

## Related stories

[How Vercel built an ecosystem on the open skills standard](/customers/vercel-qa)How Vercel built an ecosystem on the open skills standard

How Vercel built an ecosystem on the open skills standard

Customer story

[Customer story](/customers/vercel-qa)Customer story

[Box builds document creation into its AI agent with Claude](/customers/box)Box builds document creation into its AI agent with Claude

Box builds document creation into its AI agent with Claude

Customer story

[Customer story](/customers/box)Customer story

[Juno helps people with chronic illness find patterns in their symptoms with Claude](/customers/juno)Juno helps people with chronic illness find patterns in their symptoms with Claude

Juno helps people with chronic illness find patterns in their symptoms with Claude

Customer story

[Customer story](/customers/juno)Customer story

[A conversation with Cursor on building coding agents for professional developers](/customers/cursor-qa)A conversation with Cursor on building coding agents for professional developers

A conversation with Cursor on building coding agents for professional developers

Customer story

[Customer story](/customers/cursor-qa)Customer story
