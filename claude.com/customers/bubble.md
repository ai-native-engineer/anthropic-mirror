<!-- source: https://claude.com/customers/bubble -->

Case study | Claude Platform

# How Bubble powers an AI agent that turns prompts into production apps with Claude

[Try Claude](https://claude.ai)

![Bubble logo](https://assets.claude.com/f0ab2e704f807b230788841d2f9fc01a3a0a4f62.svg)

Industry:
:   Software

Company size:
:   Startup

Product:
:   [Claude Platform](https://claude.com/platform/api)[Claude Code](https://claude.com/product/claude-code)

Location:
:   North America

~30% increase in user satisfaction

With the Claude-powered AI editing agent, compared to the previous model provider

2x first-week user activation rate

After launching the Claude-powered AI app generator

[Bubble](https://bubble.io/) is a no-code AI app development platform with more than six million users who've built more than seven million web and native mobile apps. Its Claude-powered AI agent builds in Bubble’s visual development language, so users can move between AI chat and visual editing to launch and scale applications.

## With Claude, Bubble:

* Doubled first-week activation rate and first-month retention after launching the Claude-powered AI app generator
* Increased user satisfaction with the AI editing agent by ~30% compared to the previous model provider, with positive feedback rates rising from ~70% to ~90%
* Adopted Claude Code across the majority of the engineering team, with all new hires now onboarded to it on day one
* Reduced inference costs while maintaining app generation quality
* Shipped backlog items previously not worth the effort, including a frontend migration from jQuery to SolidJS

## The challenge

## Closing the gap between first prompt and first app

Bubble has always believed that the best way for non-coders to build apps is to speak to a computer in their language, not in code. But before AI, visual development languages required a significant time investment to learn, and new users often churned before reaching the moment where things clicked.

"The #1 business challenge we solved was showing value to users faster," said Zachary Tessler, AI Engineering Lead at Bubble. The team started with a page generator, then built a Claude-powered AI app generator that created full working apps from prompts. The results were immediate: first-week activation doubled, and twice as many users were still active at the end of their first month. But generating a complete app in one pass wasn't enough: users needed to iterate on what the generator produced, to move past prototypes into real products. That's why the team built the Bubble AI Agent, a Claude-powered assistant that helps users refine and extend their apps from within the editor.

Claude Code

![Claude Code](https://assets.claude.com/38e8385d1c5f9c0f71c486994e22fc5861a4522d.jpg?w=2400&q=75&fm=webp&fit=max)

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](https://claude.com/product/claude-code)

## The solution

## Selecting Claude for reasoning quality

Bubble's team evaluated multiple model providers before choosing Claude, prioritizing reasoning quality, low latency, and user control. "Reasoning quality is a top consideration," Tessler explained. "It helps a user decompose complex and potentially ambiguous requests into discrete actions that address their query." Latency mattered because the agent needed to keep pace with users building apps in real time. And the team wanted users to stay in the driver's seat, with the agent surfacing its plan and letting users approve changes before anything was applied.

The experience also needed to feel native. "Not a separate AI tool bolted on, but a natural extension of the way people already build on Bubble," Tessler noted.

After switching from their previous provider to Claude, Bubble built an internal evaluation suite to benchmark each model upgrade. When they moved to Sonnet 4.6, it matched the output quality of larger models at lower cost and faster response times. "The resulting apps still have all the sophistication and visual quality we were previously seeing, but with much faster responses," Tessler said.

## From chat window to working app

The Bubble AI Agent is a chat window inside the editor. Users type what they want, whether that's a question about how Bubble works or a request to add a feature to their app. On the backend, Bubble enriches each message with context about the user's app: its elements, data schemas, and logic. Claude also receives extensive instructions about Bubble's visual development language and a set of Bubble-specific tools for modifying apps.

The agent proposes changes, the user approves them, and the edits are applied. Users move fluidly between chatting with the agent and editing their app with Bubble's point-and-click tools. The agent can access broad editor functionality, from the built-in issue checker (similar in spirit to a type-checker on source code) to the full range of Bubble components and workflows, so it can generate complete user interfaces, data schemas, and executable logic, all visually editable afterward.

"Our agent is built in langchain and langgraph, so migrating from other models over to the Claude API itself was a minimal amount of work," Tessler added. The bigger investment was the evaluation suite: testing each model swap against quality, latency, and cost to make sure nothing regressed.

Choosing the right Claude model

![Choosing the right Claude model](https://assets.claude.com/7388619b452db0af26c78442a275c86c5ebe3124.jpg?w=2400&q=75&fm=webp&fit=max)

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

> "It's less about things we couldn't do and more about things that weren't worth attempting before. The effort-to-reward ratio has shifted significantly."

Zoe LapommeEngineering Manager, Bubble

## The outcome

## Cleared backlogs and a growing builder ecosystem

After switching to Claude, user satisfaction with AI-driven edit requests increased by approximately 30%, with positive feedback rates climbing from roughly 70% to 90%. Latency improvements and better component and UI generation quality both contributed.

Internally, Claude Code has changed how Bubble's engineering team thinks about what's worth building. The majority of engineers use it, and all new hires are now onboarded to it on day one. "It's less about things we couldn't do and more about things that weren't worth attempting before," said Zoe Lapomme, Engineering Manager. "The effort-to-reward ratio has shifted significantly."

The Notes panel and style variables subtab in the Bubble editor, for instance, had been sitting on the backlog because the migration work wasn't justified. Using Claude Code to move the frontend from jQuery to SolidJS and implement new designs lowered the bar enough that the team actually shipped it. Onboarding has shifted too: bringing new engineers and contractors up to speed on an unfamiliar codebase is meaningfully faster. "Everyone's had Claude Code from the start, but it's hard to imagine doing it the old way now," Tessler said.

Beyond Bubble's own product, builders in the ecosystem are shipping Claude-powered apps through the platform: chatbots, content generation tools, document analysis workflows. Agency partners are building Claude-powered templates and plugins that other Bubble users can deploy, so the adoption compounds. Claude API integrations have trended upward over the past year, with Q1 2026 the strongest quarter to date.

Looking ahead, Bubble is integrating its app debugging tools with Claude so users can fix logic bugs directly, and adding multi-modal features like sharing app screenshots to iterate on generated UIs. "A Bubble user can connect to the Anthropic API, design a full conversational UI, and ship a Claude-powered product in hours rather than weeks," said Theo Goldberg, Partnerships Lead. "The compound effect across six million builders is what excites us most."

> "A Bubble user can connect to the Anthropic API, design a full conversational UI, and ship a Claude-powered product in hours rather than weeks."

Theo GoldbergPartnerships Lead, Bubble

[![Zendesk](https://assets.claude.com/eb4ae3eeaffc7fb16618696c1baa3ef6c6224977.svg)

### Zendesk built custom agents on Claude and reached 1 million agent executions in 7 weeks](https://claude.com/customers/zendesk)[![Supermetrics](https://assets.claude.com/3ac4171a81008be0340e5c3d8ccb46571c3edfb3.svg)

### Supermetrics lets marketers manage ad campaigns from a conversation with Claude](https://claude.com/customers/supermetrics)[![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

### How Atlassian builds AI agents teams can trust with Claude and Google Cloud](https://claude.com/customers/atlassian)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### Rocket Money on building agents that fix their own code](https://claude.com/customers/rocket-money-qa)
