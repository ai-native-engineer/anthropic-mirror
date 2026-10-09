<!-- source: https://claude.com/customers/warp -->

Case study | Claude Platform

# Warp rebuilds the terminal for AI coding with Claude

[Try Claude](https://claude.ai)

![Warp logo](https://assets.claude.com/399915ee2f0b3513a52ff63e61b1da17ed7eb078.svg)

Industry:
:   Software

Company size:
:   Startup

Product:
:   Claude Platform

Location:
:   North America

800K monthly developers

build software using Warp

10M Claude Code sessions

run inside Warp's terminal to date, including 400K+ each week

[Warp](https://www.warp.dev/) is building an agentic development environment: a workbench for running, managing, and scaling agents. Grounded in an open-source terminal with over 60k GitHub stars, developers using Warp run coding agents like Claude Code and Warp Agent locally or in the cloud. Users can start agents from any surface via CLI, API, or SDK, and manage all agents in a central control plane. Warp defaults to Claude models for advanced coding and provides a modern environment for running Claude Code locally.

## With Claude, Warp:

* Serves 800K monthly developers through its agentic terminal
* Has logged 40M Warp Agent conversations, with 65% of tokens routed to Claude models
* Processes 55 billion Claude tokens per day on its platform
* 10M Claude Code sessions run to date in its terminal, including 400K+ each week
* Can spawn Claude Code as a sub-agent for parallel work across a codebase
* Defaults its "auto-genius" mode to Claude for coding tasks when users want top intelligence

## The challenge

## A 40-year-old developer tool meets agentic coding

When Warp launched in 2021, the terminal hadn't seen meaningful investment in three or four decades. The team started by trying to improve the fundamental UI of the terminal, and added AI capability as language models became readily available: natural-language-to-shell-command translation, a chat assistant panel, then "agent mode," one of the first command-line agents with direct terminal access for running commands and reading files.

As agentic coding accelerated, teams trying to deploy autonomous coding agents into production started finding new problems. The terminal was the natural home for local development work, but wasn't built for it. And running agents in the cloud required stitching together a complex infrastructure: environments for agents to run, visibility into agent actions, tools to steer agents, and ways to continue work locally.

“Warp's mission has always been to help developers use great tools to ship great software, and that mission hasn't changed,” said Olivia Johnston, Senior Product Marketer at Warp. “What's changed is what supporting developers actually looks like today.”

Claude Code

![Claude Code](https://assets.claude.com/38e8385d1c5f9c0f71c486994e22fc5861a4522d.jpg?w=2400&q=75&fm=webp&fit=max)

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](https://claude.com/product/claude-code)

## The solution

## A Claude-powered agent harness, then a cloud platform around it

In 2024, Warp began evolving its flagship product from a terminal to an agentic development environment, optimizing the Warp Agent for complex coding tasks, and adding support for multi-agent workflows and code editing directly into the terminal.

When Claude Sonnet 4 arrived, Warp's team saw a step-change in coding capability. Up to that point, Warp's terminal agent had been strong at what the team called "shallow but broad" tasks: translating natural language commands, navigating CLIs, and helping developers find the right syntax. But with Sonnet 4, the agent could take on full software development lifecycle work: writing code, running tests, reviewing diffs, debugging across a codebase.

"There was an immediate, noticeable difference in what the agent was capable of, even as we were internally dogfooding,’" said Zach Bai, an Head of Product Engineering at Warp. "With Sonnet 4, the thing we built began working in a way it never had before."

For coding tasks, Warp's "auto" mode defaults to Claude. Most users who don't manually configure a model end up on Claude Opus, Sonnet, or Haiku, depending on the complexity of their task. “Most of our users believe Claude models are at the frontier of coding intelligence and are the right fit for the development tasks at hand," said Suraj Gupta, the engineer leading Agent Quality at Warp.

Warp's recently launched cloud agent orchestration platform, Oz, lets users start cloud runs of popular coding agents—including the Warp Agent and Claude Code—directly from the terminal. Runs can also be triggered through first-party integrations with Slack, Linear, and GitHub, or programmatically via API or SDK. Teammates can jump into an active session to see what an agent is doing and steer it, with the right permissions. Customers can self-host the platform, run it on Warp's infrastructure, or mix both.

Warp allows users to choose their preferred models and coding agents for tasks. Customers can use the Oz platform to start and steer Claude Code agents or Warp Agents in the cloud, can use the Warp code review feature to send comments directly to Claude Code in the terminal, and can select the model that best meets their needs.

"We want to provide the best place to build with agents, and for a lot of our customers that means giving them the flexibility to choose their favorite coding agent," Johnston said. "They've invested in tooling and want help building automations, but they want to keep using what they already have."

Choosing the right Claude model

![Choosing the right Claude model](https://assets.claude.com/7388619b452db0af26c78442a275c86c5ebe3124.jpg?w=2400&q=75&fm=webp&fit=max)

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

> "With Sonnet 4, the thing we built began working in a way it never had before."

Zach BaiHead of Product Engineering, Warp

## The outcome

## 800K developers, a new audience for the terminal

Warp now serves 800K monthly developers. The terminal has run 10 million Claude Code sessions to date, with over 400,000 each week. Warp Agent has logged 40 million conversations total, with 65% of those tokens routed to Claude. Users at 56% of the Fortune 500 are now on Warp, including leading engineering teams like Ramp, Peloton, and Docker.

Warp is also picking up an audience no one expected. "People who didn’t know what a terminal was two years ago are now seeking Warp out and downloading it," Bai said. Marketers and analysts use the terminal as a way into internal CLIs and data tools they otherwise couldn't reach, with an agent handling the parts they don't know. Johnston, a marketer herself, uses Warp's agent with Claude to query internal data directly, getting answers in minutes that previously meant filing a request and waiting on the data team's queue. "It can create dashboards and charts for me, then push them up onto our dashboard system so I can share them with everyone else," she said.

Warp's next focus is expanding on its support for teams using multiple agent harnesses with cross-agent memory. The team plans to add a persistent memory layer to the cloud platform so agents don't start every task from scratch. "We want it to be multi-harness," Gupta said. "Whether you're using Claude Code, our own harness, or another agent platform, your memories carry forward."

> "Whether you're using Claude Code, our own harness, or another agent platform, your memories carry forward."

Suraj GuptaEngineering Lead for Agent Quality, Warp

[![Zendesk](https://assets.claude.com/eb4ae3eeaffc7fb16618696c1baa3ef6c6224977.svg)

### Zendesk built custom agents on Claude and reached 1 million agent executions in 7 weeks](https://claude.com/customers/zendesk)[![Supermetrics](https://assets.claude.com/3ac4171a81008be0340e5c3d8ccb46571c3edfb3.svg)

### Supermetrics lets marketers manage ad campaigns from a conversation with Claude](https://claude.com/customers/supermetrics)[![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

### How Atlassian builds AI agents teams can trust with Claude and Google Cloud](https://claude.com/customers/atlassian)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### Rocket Money on building agents that fix their own code](https://claude.com/customers/rocket-money-qa)
