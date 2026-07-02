<!-- https://anthropic-partners.skilljar.com/whats-new-with-opus-47/486155 -->

Lesson 5 of 5 · Course: What's New with Opus 4.7

# Three smaller updates. *Easy to miss, worth knowing.*

The headline platform stories are Managed Agents, Advisor Strategy, and Task Budgets. There are three smaller updates underneath them that come up in customer conversations almost as often. This lesson is a quick tour of all three.

Feature one · Vision

## Higher-resolution image support.

Opus 4.7 now reads images at up to 2576 pixels on the long edge, up from 1568. The practical effect is in workflows your customers may already have running today.

01

What changed

Resolution ceiling raised to 2576px

The model can now process meaningfully more detail in screenshots, text in images, diagrams, and complex document layouts. This is where customers had been seeing the most quality loss in vision workflows.

From 1568px No API changes Works on existing calls

Feature two · Effort

## An extra-high effort level, when you need it.

The thinking-effort control gets a new level called `xhigh` that sits between `high` and `max`. For most customers it's a knob they won't reach for. For the workloads where it matters, it's worth knowing it's there.

02

What changed

Granular control over reasoning depth

A new `xhigh` level for explicit control over the token-cost-versus-performance trade-off. Adaptive thinking is on by default, so most workloads handle this automatically; `xhigh` is for the cases where you want to set the level explicitly rather than let the model choose.

New: xhigh Between high and max Adaptive thinking on by default

Feature three · Claude Code

## Ultrareview now runs from the CLI.

Claude Code's existing Code Review capability extends to the CLI with a new `/ultrareview` command. For partners and customers building inside the CLI workflow, this closes the gap between reviewing in the browser and reviewing in the terminal.

03

What changed

Code Review in the terminal, via `/ultrareview`

The same review capability that has been available in the browser is now invocable from the Claude CLI. First-party only; review still surfaces in the CLI or in Claude.ai. Useful for partners shipping CLI-based developer tooling for their customers.

Command: /ultrareview First-party only CLI or browser

Activity · Quick check

## Three statements. True or false on each.

A fast pass through the three features to lock them in. The traps are the misreadings partners are most likely to fall into when a customer asks.

Activity · Each statement is either true or false. Pick, see the explanation, then move on.

"Customers don't need to change their API calls to take advantage of higher-resolution image support."

True False

True. The vision improvement applies to existing calls automatically. If your customer is sending screenshots, diagrams, or document layouts today, they get the higher-resolution processing without code changes.

"You should default to xhigh effort to make sure customer workloads get the best reasoning."

True False

False. Adaptive thinking is on by default, and the model usually chooses the right effort level for the workload. Defaulting to xhigh pays for reasoning depth your customer's workload may not need. Use it deliberately, not as a default.

"Ultrareview is available to any third-party CLI tool that wraps the Claude API."

True False

False. Ultrareview is first-party only; review surfaces in the Claude CLI or in Claude.ai. Partners building their own CLI tools cannot embed it directly. Worth noting up front when scoping CLI-based offerings.

**The short version:** Vision is automatic on existing calls. Reach for xhigh deliberately; adaptive thinking handles the rest. Ultrareview surfaces in the Claude CLI and in Claude.ai. Three small updates, three precise framings to carry into customer conversations.
