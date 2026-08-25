<!-- source: https://claude.com/customers/deepgram -->

Case study | Claude

# Deepgram ships 4–10x more durable code with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a84c544207da56365de9165_logo_deepgram-light-mode.png)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a84c5496d5290209c339478_logo_deepgram-dark-mode.png)

Industry:

Software

Company size:

Startup

Product:

[Claude Code](https://claude.com/product/claude-code)

[Claude Enterprise](https://claude.com/solutions/enterprise)

Location:

North America

4–10x durable code output

from regular and power Claude users vs. non-users in an internal cohort study

Minutes to triage customer incidents

compared to multi-day back-and-forths, with agents that verify their own diagnoses

[Deepgram](https://deepgram.com/) builds the speech models that let software hear and talk: real-time speech-to-text, text-to-speech, and a Voice Agent API with Claude built in. It also rebuilt its own engineering on Claude, end to end.

## With Claude, Deepgram:

* Produces 4–10x more durable code output among regular and power Claude users than non-users, per an internal cohort analysis
* Cut customer incident triage from multi-day back-and-forth to minutes
* Runs roughly 95% Claude-written code on its most productive engineering team
* Documented 3–5x gains on team projects, with individuals reporting more than 2x on routine work
* Migrated the entire company to Claude Enterprise with SSO, centrally managed compliance, and organization-scoped MCP allowlists
* Replaced roughly 80% of its legacy research stack with a new agent-native environment

## The challenge

Claude for Statrtups

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0cb8c1f8c5c525e8c554b3_problem-solvers-padded-200kb.jpg)

Join the founders building on Claude. Access community and resources to accelerate your growth.

Read more

[Read more](https://claude.com/programs/startups)Read more

Claude for Statrtups

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Join the founders building on Claude. Access community and resources to accelerate your growth.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude for Statrtups

Join the founders building on Claude. Access community and resources to accelerate your growth.

## A product surface outgrowing human-speed workflows

Deepgram's engineering surface is enormous: inference, APIs, SDKs, billing, integrations, infrastructure, and apps. Traditional workflows couldn't cover it fast enough. "Our competitors and startups we haven't even heard of yet are building AI-native now, and the cost of code generation is approaching zero," said Kris Efland, Deepgram's VP of Engineering. "If we don't ship it, someone else does, and customers follow whoever ships."

Incident triage showed the cost most plainly. When a customer reported a spike in text-to-speech errors, a Deepgram engineer pulled logs and metrics by hand, pieced them together, and wrote a response, often over a multi-day back-and-forth. The data lived in five places, and the engineer fielding the report wasn't always the one who owned the affected service.

Claude adoption, meanwhile, was outrunning any official plan: engineers moved from personal API keys to out-of-pocket Claude Max subscriptions. "If your best people are paying out of pocket to get around your limits, you've already lost more than the license would've cost," Efland said.

## The solution

Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525504b02eec936ac51b_68c469d41149ace562bfd24d_og-claude-product-claude-code.jpeg)

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Read more

[Read more](https://claude.com/product/claude-code)Read more

Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

## A bake-off, a cohort study, and a hard cutover to Enterprise

The conclusion was to rebuild as an agentic company or get out-shipped, an effort Deepgram calls DG2. The rebuild started with data: a real-world bake-off of Claude Code against other coding agents. What mattered most was raw model quality on Deepgram's Rust, Python, and infrastructure-as-code codebases, fit with existing internal tools, ability to verify its own work, and zero-friction access for every engineer. “The model is just better, full stop," said one of Deepgram's power users after Claude Opus 4.6 arrived. “Everything else is moot.”

An internal analysis grouped developers by Claude usage and tracked how often code was later replaced; code that stayed in the codebase counted as durable. Regular and power Claude users produced durable code at roughly 4–10x the rate of non-users, while the heaviest use drove about 9x higher churn. So Deepgram set test-coverage standards for Claude-generated code higher, not lower.

Formalizing engineer access meant a hard cutover to Claude Enterprise in mid-2026. Deepgram handles customer data under HIPAA, SOC 2, GDPR, PCI-DSS, and CCPA, so it requires Enterprise licenses where training is off by default and not changeable by users. Retention, tool permissions, and MCP allowlists are centrally managed; new-hire accounts are auto-issued before day one.

The commitment outlasts any single release. "Claude is the only frontier model where the surrounding system is good enough that we've reshaped our own infrastructure around it," Efland said. Deepgram open-sourced a terminal API so agents could drive terminal I/O directly, changing its tooling to suit the agent rather than the reverse. Code review runs through Claude on rubrics that encode where each project sits in its lifecycle, with explicit instruction not to block on nits while staying alert to security issues. Claude also runs in Slack for ambient briefings and standup recall. "The differentiator is the ecosystem with Claude Code, Cowork, MCP, skills, and subagents,” Efland said. “These create so much more than value any single model's ceiling. That's a depth of integration we haven't reached with any other provider."

## Solve a problem once, ship it as a skill

The default engineering loop runs through Claude Code: start in plan mode, iterate until it's right, then let Claude execute and verify. Claude Code connects over the Model Context Protocol (MCP) to the systems engineers already live in, from Slack and Asana to GitHub and Grafana, and drives daily CLI work. All of it runs on a CLAUDE.md file and a few slash commands. "A tight setup beats elaborate configs all day long," Efland explained.

When a solution is reusable, it becomes a SKILL.md in the shared deepgram/agents repository for the whole company to use and improve. Non-coding work runs the same way: Slack messages become Asana tickets or incident investigations.

Underneath, Opus, better at tool use, handles heavy coding and reasoning, and Haiku covers high-volume automation. Claude shows up on the product side too: the Voice Agent API pairs Deepgram's own Nova, Flux, and Aura voice model with Sonnet on the Advanced tier and Haiku on Standard as its reasoning step, with end-to-end latency under about 700ms.

## Multi-agent support for customers

One engineer, Jake, built Deephive, an in-house multi-agent support system, using Claude Code. A central Opus-class agent reads a problem and spawns parallel, read-only Sonnet-class workers that pull context from Slack, DevRev, Notion, GitHub, and Asana, then synthesize a diagnosis and draft internal handoffs and customer replies. Anything sent or changed needs human approval. Deepgram supports its top accounts this way, Anthropic among them, moving from root cause to pull request in hours and to GPU-spec recommendations in minutes.

The clearest moment was a sustained text-to-speech degradation a customer reported. A Deepgram engineer pointed the incident-response skill, Claude Code with Loki and Prometheus access, at the problem. It came back with the correct diagnosis, a low-baseline server-side stream error, not an outage, and the exact client-side fix, reconnect-on-1011, correcting the engineer's earlier guess. The reply went out signed "Sent using Claude."

"Getting 'water through pipes' is easy now,” Efland said. “Getting all the bugs out still requires reading the code.” Every production change carries human sign-off; every deliverable has one responsible human.

"Claude is the only frontier model where the surrounding system is good enough that we've reshaped our own infrastructure around it."

Kris Efland

VP of Engineering, Deepgram

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## Shifting from writing to validating code

With Claude built into daily engineering, regular and power Claude users now produce 4–10x the durable code of non-users, and incident triage that once ran multi-day returns verified root causes in minutes.

Deepgram's restaurant and drive-thru team, its most productive group, runs roughly 95% Claude-written code; one new hire shipped 40+ substantial pull requests in six weeks. Company-wide, new hires onboard in hours and days, not weeks. The research team replaced roughly 80% of its legacy stack with an agent-native environment; porting models to new hardware is now routine. Non-engineers stand up tools too, from ops reconciliations to MVP apps in days, and recruiting uses Claude Code for its applicant surge. Together, these workflows run on the same skills and MCP infrastructure, expanding Deepgram's capacity to build and support its voice AI products across engineering, research, and customer support.

Cheap code generation moved the constraint to validation, so Deepgram writes more tests, not fewer, and engineering shifts from writing code to defining behavior and reviewing results. "The future is agents driving not just code authoring but infrastructure, deployment, testing, and support triage,” Efland said, “with humans in the loop to defend product integrity as non-negotiable.”

"The differentiator is the ecosystem with Claude Code, Cowork, MCP, skills, and subagents."

Kris Efland

VP of Engineering, Deepgram

## Related stories

[How Notion ships and scales agents with Claude Managed Agents](https://claude.com/customers/notion-qa)How Notion ships and scales agents with Claude Managed Agents

How Notion ships and scales agents with Claude Managed Agents

Customer story

[Customer story](https://claude.com/customers/notion-qa)Customer story

[Office Hours: Building the case for leaders who ship with DoorDash](https://claude.com/customers/doordash-boris-office-hours) Office Hours: Building the case for leaders who ship with DoorDash

Office Hours: Building the case for leaders who ship with DoorDash

Customer story

[Customer story](https://claude.com/customers/doordash-boris-office-hours)Customer story

[Office Hours: Asynchronous coding and the end of the IDE with Spotify](https://claude.com/customers/spotify-boris-office-hours) Office Hours: Asynchronous coding and the end of the IDE with Spotify

Office Hours: Asynchronous coding and the end of the IDE with Spotify

Customer story

[Customer story](https://claude.com/customers/spotify-boris-office-hours)Customer story

[Office Hours: Building for the model that doesn't exist yet](https://claude.com/customers/ramp-boris-office-hours)Office Hours: Building for the model that doesn't exist yet

Office Hours: Building for the model that doesn't exist yet

Customer story

[Customer story](https://claude.com/customers/ramp-boris-office-hours)Customer story
