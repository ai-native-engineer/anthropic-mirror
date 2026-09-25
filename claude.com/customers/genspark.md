<!-- source: https://claude.com/customers/genspark -->

Case study | Claude Platform

# Genspark's Super Agent orchestrates 150+ tools with Claude

[Try Claude](https://claude.ai)

![Video thumbnail](https://assets.claude.com/363f972d0a4d291a65f4ea65358d9a0a9a8df32d.jpg)

Industry:
:   Software

Company size:
:   Startup

Product:
:   Claude Platform

Location:
:   North America

$250M ARR since pivoting to the Super Agent

in early 2025

150+ specialized tools orchestrated by Claude

inside a single agent

[Genspark](https://genspark.ai/) is an AI workspace where one prompt produces slides, spreadsheets, documents, design posters, or websites for non-technical knowledge workers. The product is built around the Super Agent, which uses Claude to coordinate more than 150 specialized tools in response to whatever a user asks for.

## With Claude, Genspark:

* Surpassed $250 million in annual recurring revenue after pivoting to the Super Agent in early 2025
* Orchestrates 150+ specialized tools end-to-end with its Super Agent architecture
* Creates AI slides, spreadsheets, and documents driven by Claude's coding capability
* Built an internal engineering culture where 100% of code is written by AI

## The challenge

![](https://assets.claude.com/6fe2411aee6587d0dc3532f08a30bcc7ec0e3271.jpg)

"Claude knew when to stop and knew which tools to call. When some tool returned an error message, it would know what alternative way to try." —Kay Zhu

## A rigid workflow that couldn't keep up

Genspark launched out of stealth in mid-2024 as an AI search product, then steadily expanded into parallel search and asynchronous deep research that would email users a finished analysis after running for several minutes. "If we positioned the product as search, it needed to return to the user in one second, or at most ten seconds," said Kay Zhu, co-founder and CTO at Genspark. "Ten seconds was too short for the system to do meaningful work."

The team kept expanding the runtime—first to parallel queries, then to background workflows running for minutes—because each expansion let them tackle harder problems for users. One paying user spent a week using a traditional search engine to compare credit cards against a long list of personal criteria, then handed the same question to Genspark's asynchronous agent and got the same conclusion in 15 minutes.

The architecture underneath, though, was a directed graph of predefined workflow nodes, and that design was hitting a ceiling. "It was too rigid," Zhu said. "It often broke on edge cases." Search satisfaction in the field has hovered around 80% for a decade, Zhu noted, no matter how much better the underlying systems get. Users adapt: as the system handles more, they ask harder questions, and the satisfaction rate stays flat. Genspark was seeing the same pattern. Simple questions ran through too many steps. Hard questions hit walls the workflow didn't know how to route around. The system that had taken Genspark to millions of users could no longer go where users wanted to go.

![Problem Solvers landing page](https://assets.claude.com/516bf8e49c81e551455b1e24a0fc3678725df957.jpg)

The most driven founders are problem solvers. Watch their unscripted conversations with the Anthropic engineers.

[Read more](https://claude.com/problem-solvers)

## The solution

## An agent loop that finally worked

The ReAct-style agentic loop, in which a model decides each next step rather than following a fixed plan, had been on Zhu’s mind since 2023. "The idea is very elegant," he said. "If the model is powerful enough, it should be able to know when to call which tool and when to stop." He tested it against every new frontier model that came out, roughly every three months, for two years. The failures were always the same: the model fell into infinite loops, hit the same error repeatedly, or failed to recognize when it had enough information to stop.

In early 2025, Zhu tried again at home with Claude Sonnet 3.7, the newest Claude release at the time. "To my surprise, it was very intelligent," he explained. "It knew when to stop and knew which tools to call. When some tool returned an error message, it would know what alternative way to try." That recovery behavior was the missing piece. Genspark rewrote the product around it.

The Super Agent that launched in early 2025 is model-agnostic by design, with different frontier models doing different jobs. Claude plays two central roles. The first is the agent loop itself: at each step in a task, Claude decides which of the 150+ available tools to call next, when to gather more information, when to backtrack, and when to summarize and return a result. For the most demanding planning problems, Genspark fans out to multiple frontier models in parallel and uses Claude to reconcile their plans into one. The second is code generation. Behind the AI slides, AI spreadsheets, and AI documents that users see, Claude generates the code that produces the final artifact.

"The old way was running on a rail," Zhu said of the original architecture. "If everything goes well, the train runs very fast. But if something goes wrong, the train gets flipped. The Super Agent is more like an experienced driver with a GPS and a goal in mind. It will try every means to reach the goal, and if there are detours or obstacles in between, it will find a way out."

That shift, from architecture as constraint to architecture as adaptive runtime, changes what a startup competes on. "Nobody really has a moat anymore," Zhu said. "The moat is execution speed." That belief shapes how Genspark operates internally. Roughly 50 engineers produce all of the company's code through AI tools. Some have built what they call a "lights-out factory" where issue creation, pull request composition, code review, merging, and testing all run automatically. Zhu personally writes code in Claude Code's plan mode. "It's like talking to a very experienced software engineer, someone who's super intelligent and knows the codebase really well," he said.

Claude Code

![Claude Code](https://assets.claude.com/38e8385d1c5f9c0f71c486994e22fc5861a4522d.jpg)

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](https://claude.com/product/claude-code)

> "Claude knew when to stop and knew which tools to call. When some tool returned an error message, it would know what alternative way to try."

Kay ZhuCo-founder and CTO, Genspark

## The outcome

![](https://assets.claude.com/6c8cf5cf12067719cc0355bff5404ea785da125c.jpg)

"We want to bring the Claude Code experience that software engineers have to all white-collar workers." —Kay Zhu

## From experiment to $250M ARR

The Super Agent helped Genspark grow past $200 million in annualized revenue. The feedback the team hears most from users, Zhu said, is from people who realize "other AI tools just chat. Genspark actually works." With a team of roughly 50 engineers, the company has been shipping major versions of AI Workspace on a roughly two-month cadence, with 3.0 the most recent release, and 4.0 already in planning.

Users invented use cases nobody at Genspark had planned for. A New York real estate analyst now produces investor pitch decks in hours, work that used to take weeks of multi-person research, and has started winning contracts away from larger firms. Japanese seafood industry CEOs use Genspark to analyze domestic demand and source new leads. One customer used Genspark’s agent to resign from a job he found too uncomfortable to quit in person.

Where Zhu sees model capability heading in 2026 shapes what Genspark is building next: effectively infinite context built through scaffolding around the model, long-horizon agents that can run for hours or days on complex tasks instead of minutes, and orchestration models capable of driving fleets of sub-agents in parallel. Genspark has internal experiments running against each.

Genspark spells out the bet on a billboard along US-101 in San Francisco: a three-day work week. The premise is that AI can handle the busywork, aligning slide bullets, building pivot tables, formatting documents, so people can spend their time on what they actually value. "We want to bring the Claude Code experience that software engineers have to all white-collar workers," Zhu said. "The model is so intelligent right now. The distribution is super uneven. Some people experience the latest capability and their lives change totally. A lot of people haven't experienced that yet. We want to accelerate that transition."

> "It's like talking to a very experienced software engineer, someone who's super intelligent and knows the codebase really well."

Kay ZhuCo-founder and CTO, Genspark

[![Supermetrics](https://assets.claude.com/3ac4171a81008be0340e5c3d8ccb46571c3edfb3.svg)

### Supermetrics lets marketers manage ad campaigns from a conversation with Claude](https://claude.com/customers/supermetrics)[![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

### How Atlassian builds AI agents teams can trust with Claude and Google Cloud](https://claude.com/customers/atlassian)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### Rocket Money on building agents that fix their own code](https://claude.com/customers/rocket-money-qa)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### How Rocket Money built its personal finance agent with Claude](https://claude.com/customers/rocket-money)
