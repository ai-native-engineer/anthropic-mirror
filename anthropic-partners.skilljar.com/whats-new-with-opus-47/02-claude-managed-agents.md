<!-- https://anthropic-partners.skilljar.com/whats-new-with-opus-47/486152 -->

Lesson 2 of 5 · Course: What's New with Opus 4.7

# What partners stop *having to build.*

Historically, the hard part of building agents wasn't the model. It was everything around it: sandboxing, memory, state management, tool execution. Anthropic now owns that layer. This is the headline platform release in 4.7, and it changes what partners build.

The historical shape

## Partners were the infrastructure team, not just the application team.

If a customer wanted an agentic workflow, the build looked like this. Spin up sandboxed execution environments. Wire in memory and state across long-running sessions. Implement tool execution. Coordinate retries and failure handling. The model was the easy part.

For most partners, that meant a real investment in infrastructure engineering before any customer-facing value was visible. The platform release flips that.

The new shape

## Anthropic runs the infrastructure. Partners focus on what the user sees.

Managed Agents is the name for the platform service that hosts the parts partners used to build themselves. Sandboxing, memory, state, tool orchestration. All managed. You bring the application logic and the end-user experience; Anthropic owns the part that used to take six months to stand up.

The line worth quoting

From Chris on the launch call: **"Headline platform release for me because it changes what partners have to build."** Whatever you were planning to invest in agent infrastructure this quarter is now available out of the box. The investment shifts to what the customer actually experiences.

Agent SDK and Managed Agents

## The two are different shapes, not competing options.

Customers will ask how this relates to the Agent SDK. The short answer is that one is the building blocks and the other is the managed service running on top of them. Choose based on how much of the stack you want to operate.

Agent SDK

The building blocks

Lower-level primitives for partners that want fine control over how agents are constructed, scheduled, and run. You own the operational surface. Use this when the customer's requirements diverge from the managed defaults, or when the workload needs custom infrastructure.

Managed Agents

The managed service on top of the blocks

Anthropic operates the agent runtime: sandboxing, memory, state, tool execution. You write the application; the infrastructure is hosted. Use this when the customer wants agentic capability without the operational burden, which is most of them.

The capability worth knowing

## Multi-agent coordination, out of the box.

The biggest delta on top of managed infrastructure is what comes next: agents can spawn other agents, parallelize work, and coordinate autonomously. This used to be the hardest part of the build. Anthropic now ships it as a platform feature.

Spawn

Agents create agents

An agent working on a complex task can break the problem up and delegate to sub-agents it spawns itself. No external orchestrator needed.

Parallelize

Work runs concurrently

Sub-agents run in parallel where the work allows it. The lead agent gathers their outputs and composes the final result.

Coordinate

No router to build

The coordination logic that partners used to write is part of the managed runtime. Inter-agent messaging, state, and synchronization come hosted.

Activity · Path selection

## A customer ask lands on your desk. Which path do you scope?

The wrong answer here is partners defaulting to the SDK because that's what they've always built on. Sometimes that's right. Often it's not.

Decision · Scenario

A mid-sized law firm wants an **internal compliance review agent** that spawns sub-agents for different jurisdictions, runs them in parallel, and produces a synthesized report. They have a small engineering team. Which do you scope?

A · Agent SDK build

Build the orchestration, sandboxing, and state management yourselves on top of the SDK primitives.

B · Managed Agents

Use the hosted runtime. Multi-agent coordination is already there. Your team builds the user-facing review experience.

C · Either; let engineering preference decide

Hedge. Let the team pick based on familiarity.

**B is the answer.** A small engineering team plus multi-agent coordination plus parallelization is exactly the shape Managed Agents was built for. Scoping the SDK build would put the firm's engineers on infrastructure work that's now hosted; the project would slip and the customer-facing review experience would suffer. C abdicates the partner's role; engineering preference is a fine tie-breaker but not a scoping decision. Lead with Managed Agents when the customer has the workload and not the infrastructure appetite.

<!-- youtube: MzhSDSY33bI -->

[![What partners stop *having to build.*](https://img.youtube.com/vi/MzhSDSY33bI/hqdefault.jpg)](https://www.youtube.com/watch?v=MzhSDSY33bI)

<details>
<summary>자막: What partners stop *having to build.*</summary>

So, Cloud Manager Agents is a headline platform release for me because it changes what partners have to build. Historically, if a customer wanted to run a production agent, they had to handle the infrastructure themselves. Sandboxing, memory, state management, tool execution, and that's a lot of work. With Cloud Manager Agents, we take care of that infrastructure for you. And I know you're probably asking yourself, well, we've already had the Agent SDK, and what's different about the Agent SDK and Cloud Manager Agents? And the easiest way to think of it is Agent SDK is the building blocks, and Manager Agents is the managed service to build built on those same blocks. So, again, we take care of the infrastructure for you. You don't have to worry about that piece of it.

</details>
