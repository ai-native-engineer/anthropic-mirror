<!-- https://anthropic-partners.skilljar.com/partner-basecamp/478260 -->
<!-- scorm-content: https://anthropic-partners.skilljar.com/content/wp/4hdejjwplbrm/37fr5vl5jyi3y/index.html -->

# Takeaways

[Intro](#top)
[Takeaways](#takeaways)
[Adoption Reality](#adoption)
[Where Claude Wins](#wins)
[Client Playbook](#playbook)
[Go Deeper](#deeper)

Your Takeaway Brief · April 2026

# Thank you for joining us at Partner Basecamp.

You covered a lot of ground over the last two days. This brief is yours to keep. It captures the frameworks, proof points, and conversation starters that came out of the sessions so you can put them to work with clients right away.

Get started →

## What You Now Know That Clients Need to Hear

These are positions you can take into a meeting. Client-ready arguments, not session summaries.

Foundations

### Most AI failures aren't model failures. They're implementation failures.

Your clients will say their AI "isn't working." The instinct is to swap models. Basecamp gave you a better diagnostic: separate scoping problems (wrong use case) from model behavior problems (bad prompts, broken context, poor tool design) from model selection problems (wrong tier). Different diagnoses, different fixes. Most of the time, the first artifact you should ask for isn't a benchmark. It's the system prompt.

Here's what makes this land with Anthropic behind it: 99% of organizations aren't using the full capability of the latest `Opus 4.7`. The bottleneck is never the model. It's the implementation layer around it. Claude's calibrated uncertainty makes this diagnosable. The model flags when it doesn't have enough information instead of confabulating. You can show this live in a client meeting. Give Claude a question outside its knowledge and watch it say "I don't know." No competitor does this as reliably.

From the Session

The diagnostic loop

Every AI system you'll debug — yours or your customer's — follows this same shape.

1
**Symptom**

What the customer reports. In their words, not yours.

2
**Hypothesis**

What you suspect before seeing internals. Email-only forces the discipline.

3
**Evidence**

Artifacts that confirm or kill your hypothesis.

4
**Recommendation**

Fix scoped to the actual root cause. Not "try a different model."

**The client move:** When a client says "our AI isn't performing," ask for the system prompt and the last ten failure cases before you touch the model. You'll find the root cause in the implementation 80% of the time.

Evaluation

### If you can't measure it, you can't deploy it. Evals are the product.

Anthropic's core position: evaluation is engineering, not a checkbox. You learned the full stack. Tasks with defined expectations. Graders (code-based, model-based, human-based). Eval suites. Trials for non-determinism. The Cera medical scribe case made it real: hallucination rates swung from 1% to 12% because the eval prompts were poorly designed, not because the model degraded.

Why this matters for your practice: most enterprises still don't have evals. They try new models and decide based on feel. As agents take on larger, more consequential tasks, evals become the load-bearing wall. This is probably the most durable consulting offering you can build. Help clients stand up an evaluation program that survives model upgrades and gives them real measurement instead of intuition.

From the Session

Every eval works the same way.

📝

**Input**
The test scenario you feed the model.

→

🤖

**Model**
The AI you're testing.

→

💬

**Output**
What the AI actually said.

→

✓

**Grader**
Judge if it's good.

→

📊

**Score**
The measurement.

Five parts. Same structure every time. The grader is where most of the design work lives — and where most eval programs fail.

From the Session

The Grader

The logic that decides whether the output was good enough. It's the hardest part of eval design — and the part most teams underinvest in.

Grader Type 01

Exact match.

Output must equal a specific expected string. Simple to build, but brittle — AI rarely produces identical text twice. Best for structured outputs: JSON fields, specific codes, numerical values.

Expected: "49.99"
Got:     "The jeans cost $49.99"
Result:   ✕ FAIL

Fast
Free
Very Brittle

Grader Type 02

Rule-based.

Checks specific conditions: does it contain keyword X? Is it under 200 words? Did it call the right tool? More flexible than exact match. Most of your early eval work lives here.

Check: response contains "49.99"  ✓ PASS
Check: called get\_product("jeans") ✓ PASS
Check: ≤ 2 tool calls             ✓ PASS

Fast
Cheap
Good for Constraints

Grader Type 03

LLM-as-judge.

Use a second AI call to evaluate the response. You prompt it: "Here's the task and the response — rate the quality." Flexible enough to handle nuance, tone, and reasoning.

**What do you sell?**
Many valid answers.

**Which is a better deal?**
Requires reasoning.

**I have $100, what should I buy?**
Subjective recommendation.

**Powerful but not free** — you're making an API call to grade every API call. And your judge needs its own prompt engineering.

Most enterprises default to LLM-as-judge because it feels the most flexible. But the cost adds up fast — you're doubling your API spend on every eval run. Start with exact match and rule-based graders where you can. Use LLM-as-judge for cases that genuinely need reasoning or subjective judgment. The discipline of choosing the right grader is what separates eval programs that scale from ones that quietly get abandoned.

**The client move:** For any client who's run a pilot, ask: "How do you know it's working?" If the answer is manual spot-checking or user surveys, you have an engagement.

Architecture

### Context engineering is a first-class design decision.

How an agent manages its context window determines whether it survives production. You learned the failure modes: context rot, token bloat from surfacing all tools at once, catastrophic compaction. The `Agent SDK` addresses each one. Auto-compaction. Progressive tool discovery. Surgical context editing.

In the mini-hack exercise, teams diagnosed a broken ticketing agent where sub-agents were claiming resolution on issues they hadn't actually fixed. The fix was structural: post-tool-use hooks that verify the agent solved the problem, not just said it did. That's the difference between a demo that works and a system that ships.

From the Session

The Agentic Loop

Your code orchestrates. Claude decides which tools to call and when to stop.

User Message
→
API Call
→
stop\_reason?
→
tool\_use
→
Execute Tool
→
Append Results
→
↺ Loop until end\_turn

**20 lines of Python.** Every framework — LangChain, Agents SDK, CrewAI — is abstraction on top of this pattern. Most agentic failures don't happen in the model call — they happen between tool execution and the next loop iteration, where results get appended incorrectly or verification is skipped. That's where post-tool-use hooks live, and why the ticketing agent in the mini-hack was claiming resolution on issues it hadn't actually fixed.

From the Session

Context Engineering

**Context Is a Finite Resource**

New tokens consume some portion of the model's attention budget. More is not always better.

**Implement Progressive Disclosure**

Surface the right information at the right moment. Agentic search, skills, and tool-engineering are your levers.

**Tune Agents to Find, Navigate, and Persist the Right Information**

Design agents that retrieve selectively, navigate efficiently, and retain only what's needed downstream.

These are design criteria, not abstract concepts. When reviewing a client's agent, run each one: is context being treated as finite? Is information being surfaced progressively? Is the agent retrieving selectively or pulling everything at once? The answer tells you exactly where the design is breaking.

Read the article: [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

From the Session

Prompt Engineering vs. Context Engineering

![Prompt engineering vs. context engineering diagram](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ffaa261102e46c7f090a2402a49000ffae18c5dd6-2292x1290.png&w=3840&q=75)

This distinction matters the moment a client's agent stops scaling. Prompt engineering runs out of headroom fast — adding more instructions doesn't fix an agent drowning in irrelevant context. Context engineering is the design discipline that takes over from there. If a client is still framing their agent problems as "we need a better prompt," they haven't made this shift yet.

**The client move:** When a client's agent prototype fails in production, the first question is "how are you managing context?" Bring progressive disclosure and compaction strategy into the design phase. Not as cleanup after launch.

A new option worth knowing: Claude Managed Agents (now in public beta) is a fully hosted agent harness — secure sandboxing, built-in tools, server-sent event streaming. For clients who don't want to manage orchestration infrastructure, it removes that layer entirely.

Competitive Positioning

### Lead with intelligence. Apply countermeasures for latency and cost.

When clients raise latency or cost objections, exhaust countermeasures before downgrading. Prompt caching eliminates up to 90% of repeated-context costs. Streaming solves perceived latency. You can route simple queries to `Haiku` and reserve `Opus` for complex reasoning. Effort control tunes thinking depth. Most partners haven't tried all four before switching models.

You saw the head-to-head: `GPT-5.0` with extended thinking versus `Claude Sonnet 4.5` with no optimization. Claude won on both latency and reasoning. `Opus 4.7` uses adaptive thinking that scales with task complexity — simpler queries stay lean, harder problems get full reasoning depth. For CodeRabbit's code review workloads, Opus 4.7 runs faster than GPT-5.4 xhigh with no sacrifice in output quality.

From the Session

What happens between send and response.

Understanding where latency lives lets you target the right countermeasure.

01

Prompt sent

→

02

API routing

→

03

Tokenization

→

04

Inference

→

05

Response

TTFTtime to first token

Totaltotal latency — every stage, every time

From the Session

The full countermeasure stack.

Exhaust these before recommending a model downgrade.

01

**Streaming**

Send tokens to the user as they're generated. Reduces perceived latency significantly.

02

**Model Selection & Routing**

Use Haiku for latency-sensitive tasks and route to larger models only when needed.

03

**Prompt Caching**

Cache repeated prompt content. Up to 50% faster on cache hits. Most effective over 30k tokens.

04

**Prompt Optimizations**

Reduce prompt length and output token size (OTOS) to lower processing time across the board.

05

**Parallel Tool Use**

Execute multiple tool calls simultaneously, reducing total round-trip time in agentic workflows.

06

**Context Window Management**

Cap input tokens for latency-sensitive applications. Customers commonly cap at 50k–100k tokens.

07

**Speculative Caching**

Pre-cache prompts likely to be used soon so cache hits are ready before the request arrives.

08

**Effort / Thinking Usage**

Lower the model's reasoning effort for tasks that don't require deep thinking. Cuts tokens and latency.

09

**Programmatic Tool Calling**

Handle deterministic or simple tool calls in code rather than sending them back to the model.

10

**Framework Overhead Reduction**

Test direct API calls versus abstraction layers like LangChain, which can introduce hidden latency.

11

**1P vs. 3P**

First-party versus third-party deployments may contribute to latency fluctuations — the gap has closed substantially as of late, but worth benchmarking.

**The client move:** Don't let a client downgrade before you've applied the countermeasure stack. Walk them through caching, routing, streaming, and effort control first. The performance objection resolves without sacrificing intelligence.

Strategy

### The cost of building is going to zero. The value is deciding what to build.

The old model: a small team decides what to build, then a large team spends months executing. Implementation cost dominated the pyramid. With AI coding tools driving that cost toward zero, the pyramid inverts. Deciding what to build becomes the bottleneck and the highest-value activity. That's the architect's job. The product designer's job. Your job as an advisor.

Sit with this for a second: deciding what to build hasn't been automated. It may be the last thing that gets automated. Pair this with the eval insight and two irreducibly human functions emerge. Defining what to build. Evaluating whether it's working. Everything in between is accelerating toward automation. Your value lives at both ends.

**The client move:** When a digital native client tries to implement your architecture on their own, don't compete on building speed. Compete on the decision layer: use case selection, eval design, architecture judgment. That's what doesn't get commoditized.

Trust

### The advisor who recommends against their own product earns the longer relationship.

Path 1 of the Solution Path Decision Framework is "Don't Use AI." That's not modesty. It's positioning. Anthropic teaches this deliberately. A partner who recommends simpler approaches or different models when the data says to earns trust. That trust gets you invited back for the projects where Claude is the answer.

This is where the Anthropic philosophy becomes a selling tool, not just a talking point. Helpful, honest, and harmless isn't just a training principle for the model. It's how the company operates with customers. Being transparent when a problem doesn't fit the platform builds long-term trust with technical decision makers. If clients sense you're optimizing for your own revenue instead of their outcome, the relationship is done.

**The client move:** In your next conversation, name one thing AI shouldn't be used for in their business. Then name three where Claude creates the most value. Honesty first, recommendation second. That sequence wins.

## The Adoption Reality: What's Actually Blocking Your Clients

Three things are slowing enterprise AI adoption, and none of them are the model. These are the objections you'll hear in your next client meeting, with the specific Anthropic answers that move the conversation forward.

Blocker 1

### Security and permissions processes haven't caught up to the technology.

Enterprise clients know the model is capable. What stops them is the question they keep asking: "How do I bring this into my enterprise securely?" The concerns are specific and they come up every time. Will you train on our data? Can anyone at your company access my proprietary code? What happens if the AI executes a destructive command on production infrastructure?

The answers are specific, not hand-wavy. Anthropic has an explicit policy: they never train on customer data. For conservative organizations, deploy through Bedrock or Vertex so data stays in the client's VPC. For standard deployment, there's zero data storage beyond the prompt-response cycle. Employee access is locked. Anthropic staff can't access customer data, with a narrow exception for safety-triggered review through a four-step process. `Claude Code`'s hooks provide deterministic guardrails. You can prevent destructive commands (like `rm -rf`) at the infrastructure level. Enterprise permission settings let you allow or disallow capabilities across the organization.

**The client move:** Lead the security conversation proactively. Don't wait for the CISO to raise objections. Walk them through: deployment options (VPC vs. standard), data handling policies, hooks for guardrails, and enterprise permissions. Addressing it in meeting one earns trust that lasts through procurement.

Blocker 2

### Organizations flip on AI without teaching anyone how to use it.

Too many enterprises roll out seats, turn on the tool, and call it transformation. Everyone becomes a chat user. Prompting back and forth, maybe getting 10% acceleration, but nobody is delegating large projects or building agentic workflows. The technology shipped. The organizational capability didn't.

Anthropic's recommendation is staged adoption, not spray-and-pray. Start with the dev team. They get it fastest. Pick an elite group who will push the organization forward. Once they see what `Claude Code` does for technical tasks, they naturally identify where else in the business it applies. Then transition to internal agentic workflows, then customer-facing products. Get teams into real workflows now so they already understand the uplift when new models and capabilities launch.

**The client move:** When a client wants to "roll out AI to the whole company," push back. Propose a 30-day sprint with 15 power users instead. Targeted adoption that demonstrates value beats broad deployment that demonstrates nothing.

Blocker 3

### Leadership alignment and team-level buy-in must happen simultaneously.

Two failure modes: top-down mandates that meet bottom-up resistance ("they're afraid it will replace their job"), or bottom-up shadow IT where developers use `Claude Code` on personal accounts without management awareness. You need both. Leadership alignment sets the direction. Team-level engagement proves the value. Either alone stalls out.

Cost predictability is a real part of this. Clients want to know what this will cost at scale. Anthropic provides general guidance (average and 90th-percentile usage benchmarks, up to roughly $200/month per user for code) and enterprise admins can set per-user monthly spend limits through role-based access controls. Transparent benchmarks plus configurable limits. That's what moves the budget conversation forward.

**The client move:** Map the client's AI readiness on both axes: leadership alignment and ground-level capability. If either is missing, the engagement starts there, not with architecture.

The model is not the bottleneck. Security processes, organizational readiness, and adoption strategy are. The partners who solve those three problems drive consumption and earn the long-term relationship.

## Where Claude Wins: Evidence to Cite

When the client asks "why Claude specifically?" these are the proof points. Each one is grounded in data or a real deployment.

Adaptive

Thinking that scales with task complexity — simpler queries stay lean, harder problems get full reasoning depth

87.6%

SWE-bench Verified, highest among production-deployed enterprise models

<4s

Time-to-first-token at max thinking depth on `Opus 4.7`

Enterprise-First Brand

### Every investment Anthropic makes is for enterprise.

This is a company building enterprise agent features with no distractions. No consumer play, no social features. Anthropic Labs products like Claude Design extend Claude into professional visual creation — designs, prototypes, slides — but the core investment remains governance, agentic platforms, and model intelligence for complex enterprise workflows. Clients see the contrast. And the brand alignment matters at the board level. Healthcare companies, financial institutions, regulated industries want to align with the AI company that leads on safety and enterprise commitment. That's where the conversation starts.

Cross-Cloud Flexibility

### The only model available on all three clouds.

Claude deploys across Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry with consistent behavior. `Claude Code` works across all three. `MCP`, co-founded by Anthropic under the Linux Foundation, provides the open integration standard. Codex has no equivalent enterprise integration path. For clients with data residency requirements, multi-cloud commitments, or security teams that require VPC deployment, this is the structural flexibility that closes deals.

From the Session

MCP or API. Six Questions.

|  |  |  |
| --- | --- | --- |
| 1 | Does the agent need multiple systems in a single turn? | MCP |
| 2 | Do multiple AI clients need access to the same system? | MCP |
| 3 | Will the tool set change or grow over time? | MCP |
| 4 | Is it always the same query, on a schedule? | API |
| 5 | Is it a batch job processing thousands of items? | API |
| 6 | Does the system owner want to control the tool interface? | MCP |

**The honest answer is often both.** MCP for live incident triage. API for the daily ticket summary. The question isn't MCP or API — it's which integration needs which protocol.

From the Session

MCP Architecture

An open standard built on JSON-RPC 2.0. Three roles: host, client, server. Dynamic tool discovery.

Host

Chat Application  
Code Assistant

MCP  
Architecture

Server

Database  
API Access  
Task Execution

Client

Communication  
Interface

MCP Host

**The user-facing app.** Claude Code, Claude Desktop, Cursor, or a custom app your client built. Embeds the client and runs the session.

MCP Client

**Claude** discovers tools at runtime and calls them autonomously. Reasons across multiple servers in one turn.

MCP Server

**External systems** expose tools and resources. Jira: `search_issues`, `get_ticket`. PagerDuty: `list_incidents`.

The key client insight: dynamic tool discovery means the tool set grows with the client's systems — no rebuild required. When a new system comes online, add an MCP server and Claude discovers it at runtime. That's what separates MCP from hardcoded integrations: the architecture scales with the business instead of requiring a new deployment every time something changes.

Governance

### Enterprise governance ships today, not on a roadmap.

`SCIM` provisioning, role-based access control, 180-day audit log retention, compliance API for `SIEM` integration, `HIPAA`/`FERPA`/`GDPR`/`FedRAMP` framework support. User-level spend limits. Hooks for deterministic guardrails. Enterprise permission settings for allow/deny across the organization. ChatGPT Enterprise has name recognition but thinner governance depth. Microsoft Copilot locks you into Azure. Claude Enterprise gives multi-cloud deployment with regulated-industry compliance. Ready now.

Platform

### The Claude Developer Platform: APIs, SDKs, and protocols your clients' teams will build on.

When you're in a technical conversation, this is the full stack. Know what's GA and what's in beta — it changes the deployment conversation.

From the Session

The Claude Developer Platform

APIs, SDKs, tools, and protocols for building with Claude.

APIs

**Messages API**

Core conversational API. Tool use, streaming, thinking, structured outputs, vision, PDFs, citations, caching — all composable in a single request.

Today's focus

**Batch API**

Async bulk processing — same Messages API shape, 50% cost reduction, up to 100K requests per batch.

GA

**Admin API**

Manage orgs, workspaces, members, API keys, and Claude Code analytics programmatically.

GA

**Files & Token Counting**

Upload files for reuse across calls. Count tokens before sending to manage costs.

GA

SDKs

**Client SDKs**

Python, TypeScript, Java, Go, C#, Ruby, PHP — type-safe, auto-retry, streaming helpers.

GA

**Agent SDK**

The harness powering Claude Code. Build autonomous agents with shell access, file editing, and tool orchestration.

GA

Protocols & Extensibility

**Model Context Protocol (MCP)**

Open standard for connecting Claude to external tools, data sources, and services. Server + client SDKs.

GA

**Skills API**

Extend Claude with reusable skill packages — pre-built (PPTX, XLSX, PDF) or custom. Progressive context disclosure.

Beta

**MCP Connector & Remote Servers**

Connect to remote MCP servers directly from the Messages API. No separate client needed.

Beta

Developer Tools

**Console & Workbench**

API key management, usage dashboards, spend controls, prompt playground with side-by-side model comparison.

You don't need to recite this stack. You need to know what's production-ready versus what carries beta risk. Messages API, Batch API, Agent SDK, MCP — those are deployment decisions you can make today. Skills API, MCP Connector, Managed Agents — set expectations accordingly. That distinction is what earns credibility with a technical buyer who's done their homework.

Case Study

### Insurance underwriting: 400 people, 6 systems, 3–5 hours per deal.

A major carrier's head of operations described the problem: 400 underwriters pulling data from 6 internal systems to build risk assessments. Claude's 200K+ context window ingests all six systems' data in a single pass. Calibrated uncertainty flags edge-case policies for human review instead of generating false confidence. The human owns the decision. Claude handles research and synthesis. That's the collaboration model clients actually want. And it's the one compliance will actually approve.

Case Study

### The latency benchmark: Claude won without trying.

A partner's client assumed Claude would be slower than GPT-5.0 for an agentic workflow requiring deep reasoning. The partner ran a direct benchmark: `GPT-5.0` with extended thinking versus `Claude Sonnet 4.5` with no optimization. Claude won on both latency and reasoning quality. Apply the countermeasure stack (caching, streaming, routing) and the gap widens further. Intelligence doesn't require the latency penalty clients assume.

## Client Playbook: Six Conversations to Start This Week

Specific openers for specific rooms. Each one leads with a problem the client already feels.

When the CTO says "We need an AI strategy"

"Let's separate three things: which problems shouldn't use AI at all, which ones need Claude in existing workflows, and which ones need custom-built agents. That decision tree matters more than which model you pick. Most companies skip it."

The Solution Path Decision Framework. Positions you as the advisor who asks the hard question first.

When the pilot "isn't working"

"Before we change models, I need to see the system prompt and the last ten failure cases. In my experience, 80% of AI underperformance is implementation, not model capability. Let me diagnose before I prescribe."

Diagnosis Before Recommendation. The fastest way to demonstrate you know what you're doing.

When security is blocking deployment

"Claude Enterprise ships with `SCIM`, `RBAC`, audit logs, and `FedRAMP` compliance today. Not on a roadmap. We also have three deployment options depending on how conservative your security team is. Let me walk your CISO through them in the first meeting, not the fifth."

Leading with governance removes the blocker that kills most vendor conversations. The three deployment options: client VPC (via Bedrock/Vertex/Foundry), zero-data-storage standard, and enterprise permission-controlled.

When they want to "roll out AI to everyone"

"Let's start with 15 power users for 30 days instead. Targeted adoption with your dev team first. They'll see the potential fastest and become internal advocates. Broad rollout without enablement creates chat users, not transformed workflows."

The Anthropic angle: staged adoption beats spray-and-pray. Start with developers. They see the potential fastest and become internal advocates. Prove value, then expand.

When the CFO asks about cost

"Claude Opus 4.7 uses adaptive thinking — it scales reasoning depth to task complexity, so simple queries stay cheap and hard problems get full attention. We also have user-level spend limits and tiered models. `Haiku` at $1/M tokens for volume, `Opus` for complex reasoning. The new Advisor tool pairs a fast executor with a higher-intelligence advisor mid-generation — another way to get Opus-level reasoning without Opus-level cost on every token. Let me model it against your actual workload."

Adaptive thinking plus spend controls. Offer to run the math on their volume. It converts.

When a digital native tries to build it themselves

"The cost of coding is going to zero. We both know that. Where you need a partner isn't in building. It's in deciding what to build, evaluating whether it's working, and designing the architecture that scales. That's the bottleneck now, and it's where we create the most value."

The paradigm shift: implementation is commoditizing, but use case selection, eval design, and architectural judgment are irreducibly human. That's your moat.

## Go Deeper

Client-shareable research. Each of these is something you could send to a CTO as a pre-read or attach to a follow-up email.

[Anthropic Economic Index: Learning Curves →

Empirical data on how AI adoption is actually progressing. Usage diversification, geographic patterns, and evidence that experienced users extract measurably more value.](https://www.anthropic.com/research/economic-index-march-2026-report)
[Labor Market Impacts of AI →

Real deployment data versus theoretical capability. Send to a CHRO or workforce strategy lead working through AI's impact on headcount planning.](https://www.anthropic.com/research/labor-market-impacts)
[Economic Futures Program →

Anthropic's initiative on AI's economic impacts, including policy proposals. For regulated industries and government-adjacent clients.](https://www.anthropic.com/economic-futures)
[Anthropic Research →

Alignment, interpretability, economic research, societal impacts. When a client asks "what makes Anthropic different?" the answer is that they publish the work.](https://www.anthropic.com/research)
[About Anthropic →

Public Benefit Corporation structure and governance design. For board-level conversations about why corporate structure determines AI safety outcomes.](https://www.anthropic.com/company)



← BackGet started →
