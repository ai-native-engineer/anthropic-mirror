<!-- https://anthropic-partners.skilljar.com/whats-new-with-opus-47/486151 -->

Lesson 1 of 5 · Course: What's New with Opus 4.7

# Three models. *One just got better.*

Anthropic ships three models for partner use: Opus, Sonnet, and Haiku. Opus 4.7 is the newest release, and the deltas matter for the customer conversations you're about to have. This lesson is the model family, the changes in 4.7, and how to recommend the right tier. Chris Donlan, an Applied AI Architect gives an overview of the model family.

The full family

## Three models, three jobs.

The first orientation customers need is which model to use where. The three tiers map to three distinct workloads. Get this part right and the rest of the conversation is easier.

Latest release

Opus 4.7

Peak intelligence

The frontier model. Long-horizon reasoning, agentic coding at scale, complex multi-step work. Use when the task needs careful thought across hours of execution.

Workhorse

Sonnet

Midsize, broadly applicable

The general-purpose model. Strong on most reasoning tasks, faster and cheaper than Opus, slower and more expensive than Haiku. The default starting point for most workloads.

Volume

Haiku

Speed and price

The fastest and most cost-efficient. Built for high-volume routine work where latency and per-call cost matter more than peak reasoning depth.

In his overview, Chris Donlan, highlights the best use-cases of each in more detail.

What changed in 4.7

## Four capability deltas worth knowing.

Customers will ask "what's actually new." These four are the answer. Each one shows up in a real workload that partners are already getting asked about.

01

Agentic coding at scale

Longer coding tasks with less hand-holding. The model stays on the work, follows the plan, and reaches stable end-states in cases where earlier versions would lose the thread.

02

Long-horizon projects

Multi-step work that holds together across hours of execution. Better at remembering what it was doing, prioritizing what matters, and finishing rather than drifting.

03

Improved multimodal reasoning

High-resolution vision now standard. Reads screenshots, text in images, diagrams, and complex document layouts with materially better accuracy than 4.6.

04

Improved memory capabilities

Better at retaining and applying context from prior conversations, so ongoing projects and user preferences carry forward more naturally across sessions.

How much better

## Significant gains on the coding benchmarks your customers care about.

Opus 4.7 posts material improvements on SWE-bench Pro and SWE-bench Verified compared with 4.6. These are the benchmarks most enterprise teams cite when evaluating coding models, and the gains here are what's making engineering leaders pay attention.

+6.8 pts

SWE-bench Verified, Opus 4.6 to 4.7

Opus 4.787.6%

Opus 4.680.8%

On SWE-bench Pro, Opus 4.7 scored 64.3% against Opus 4.6's 53.4% — a gain of 10.9 points. These are the two benchmarks engineering teams cite most when evaluating coding models.

SWE-bench Verified. Higher is better.

The honest version

Benchmarks are a starting point, not an answer. The line that closes most evaluations: **"Run your own evals to validate performance against your use case."** Customers who skip that step end up with the wrong model for their workload. The ones who do it end up trusting the deployment.

Activity · Model fit

## A customer is sizing a workload. Which model do you recommend?

The trap most partners fall into is recommending Opus 4.7 by default because it's the newest. Sometimes that's the right call. Sometimes it isn't. This scenario is one where it isn't.

Decision · Scenario

Customer is building a chatbot for high-volume customer support. Mostly routine queries, occasional escalation to a human. **Cost and latency matter.** Which model do you recommend for the bulk of the traffic?

A · Opus 4.7

"Peak intelligence on every query." Use the frontier model regardless of workload.

B · Sonnet

"Middle ground for everything." Default to the midsize workhorse.

C · Haiku

Speed and price for the routine traffic. Promote escalations to Sonnet or Opus only when needed.

**C is the answer.** High-volume routine work is where Haiku earns its place. Recommending Opus 4.7 for the bulk of customer-support queries means paying peak-intelligence prices for queries that don't need it; the customer will see latency and a bill that doesn't match the workload. Sonnet is overkill at this volume too. The right pattern is Haiku for the routine traffic and a promotion to a higher tier only when the conversation needs it. Lessons 3 and 4 cover exactly how that promotion is structured.

<!-- youtube: xRTZS5S9V2o -->

[![Three models. *One just got better.*](https://img.youtube.com/vi/xRTZS5S9V2o/hqdefault.jpg)](https://www.youtube.com/watch?v=xRTZS5S9V2o)

<details>
<summary>자막: Three models. *One just got better.*</summary>

Before we jump into what's new, let's take a look at the complete family of Claude models. On the left we have Opus, which is recommended for the hardest, most complex problems. Problems that require peak intelligence and sustained autonomy. In the middle we have Sonnet, which is our mid-size workhorse. It's great for things like coding as well as agents. And then when speed and price matter, we recommend Haiku, which is our most efficient model, delivering near frontier performance at accessible speed and price. Claude Opus 4.7 is our most capable generally available model, advancing in advancing areas like coding, enterprise workflows, and long running agent tasks. Opus 4.7 was built for agentic coding at scale, excelling at long horizon projects, complex implementations, and providing polished UIs. We've also improved multimodal reasoning with Opus 4.7, bringing a high resolution vision to the model itself. Capturing finer detail in charts, diagrams, as well as complex document layouts, along with its surrounding context. Claude Opus 4.7 also delivers increased performance for industry use cases such as those in legal and finance.

</details>
