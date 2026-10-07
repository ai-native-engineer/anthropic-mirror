<!-- source: https://claude.com/resources/articles/introducing-dynamic-workflows-in-claude-code -->

**Update:** Dynamic workflows are now generally available.

Today we're introducing dynamic workflows in Claude Code, helping Claude take on the most challenging tasks end-to-end. Work you'd normally plan in quarters now finishes in days. Claude dynamically writes orchestration scripts that run tens to hundreds of parallel subagents in a single session, checking its work before anything reaches you.

Some problems are too big for one pass by a single agent, especially in complex, legacy codebases: a bug hunt across an entire service, a migration that touches hundreds of files, a plan you want stress-tested from every angle before you commit to it. Dynamic workflows can handle all of these end-to-end.

![](https://assets.claude.com/60506cfb5eb2692bedfbf445234d3958787966e5.png)

Dynamic workflows are generally available in the Claude Code CLI, Desktop, and the VS code extension for Pro, Max, Team, and Enterprise plans, as well as on the Claude API, on Amazon Bedrock, Vertex AI, and Microsoft Foundry.

Note: Dynamic workflows can consume substantially more tokens than a typical Claude Code session, so we recommend starting on a scoped task to get a feel for usage in your work.

For the best experience, turn on auto mode when using dynamic workflows. From there, you have two ways to start a workflow:

1. Ask Claude to create a dynamic workflow directly (e.g., “Create a workflow”), or
2. Switch on a new Claude Code-specific setting called `ultracode`. This is accessible through the effort menu and it sets the effort level to xhigh, while letting Claude decide automatically when to use a workflow to handle your task.

## **Dynamic workflows in action**

Early access users and teams inside Anthropic have been using dynamic workflows for a wide range of use cases, including:

* **Codebase-wide bug hunts, profiler-guided optimization audits, and security audits:** Claude searches a service or repo in parallel, then runs independent verification on every finding so the report surfaces real issues. The same shape works for hardening passes: auth checks, input validation, and unsafe patterns across an entire codebase.
* **Large migrations and modernization efforts:** Claude can handle framework swaps, API deprecations, language ports that span thousands of files end-to-end.**‍**
* **Critical work you need checked twice:** When the cost of a wrong answer is high, a workflow gives Claude independent attempts at the problem and adversarial agents working to break the result before you see it.

![Klarna](https://assets.claude.com/d2ca8f0751aef80edc79d0bba17fe65907838869.svg)

> “Dynamic workflows have been especially valuable for discovery and review tasks across large codebases. We’ve seen strong results using it to identify dead code and surface cleanup opportunities that traditional static analysis missed, helping our engineers move faster on maintenance and refactoring work.”

Alessio Vallero, Senior Engineering Manager

![CyberAgent](https://assets.claude.com/4a26eb3dd6223515011df7eacaa404d6af840d64.svg)

> “Dynamic workflows fill the gap between firing off a single subagent and building out a full agent team. Plan to implementation just flows, so we can trust longer runs without losing visibility.”

Ken Takao, Lead Systems Engineer

### **Rewriting Bun with dynamic workflows**

An example of what dynamic workflows can unlock at scale is the recent rewrite of Bun. Jarred Sumner used dynamic workflows to port Bun from Zig to Rust with 99.8% of the existing test suite passing, roughly 750,000 lines of Rust, and eleven days from first commit to merge. One workflow mapped the right Rust lifetime for every struct field in the Zig codebase. The next wrote every .rs file as a behavior-identical port of its .zig counterpart, hundreds of agents working in parallel with two reviewers on each file. A fix loop then drove the build and test suite until both ran clean. After the port landed, an overnight workflow addressed unnecessary data copies and opened a PR for each for final review. While not yet in production, all of this was handled by dynamic workflows. Jarred will be writing about this more in the future.

## **How it works**

When a workflow kicks off, Claude plans dynamically based on your prompt, breaks it into subtasks, and fans the work out across subagents running in parallel. Results are checked before they're folded in, and you come back to a single, coordinated answer. Agents address the problem from independent angles, other agents try to refute what they found, and the run keeps iterating until the answers converge—which is how a workflow reaches results a single pass can't.

Dynamic workflows are built for parallel and long-running work that can extend into hours and days, doing the most complex engineering work that previously would have taken weeks. Progress is saved as the run goes, so a job that's interrupted picks up where it left off instead of starting over. Because the coordination happens outside the conversation, the plan stays on track no matter how big the task gets.

It’s important to note that dynamic workflows consume meaningfully more usage than a typical Claude Code session. The first time a workflow triggers, Claude Code shows what's about to run and asks you to confirm. Organization admins can also optionally disable workflows through managed settings.

## **Getting started**

Dynamic workflows are on by default for Max, Team, and Enterprise plans, and when using Claude Code via the API. Pro plan users can enable them in `/config`. Ask Claude to create a workflow or turn on the Claude Code-specific setting `ultracode` to get started. Admins can manage availability in [settings](https://code.claude.com/docs/en/settings).

Read the [documentation](https://code.claude.com/docs/en/workflows) to learn more.

[ArticleOct 1, 2026

### Customize Claude Code with mods

Change how Claude Code behaves and looks with a few lines of TypeScript.

Claude Code](https://claude.com/resources/articles/claude-code-mods)[ArticleSep 30, 2026

### Claude for Government is now generally available

Claude Code CLI and Claude for Microsoft 365 also now available in early access.](https://claude.com/resources/articles/claude-for-government-is-now-generally-available)[ArticleSep 25, 2026

### Build plugins for Claude

You can now submit plugins to the Claude directory through a new developer portal, track them through review, and see usage analytics once they’re live.

Claude apps](https://claude.com/resources/articles/build-plugins-for-claude)[ArticleSep 24, 2026

### Claude Tag now supports personal connectors in channels

Claude Tag can now use your connectors for requests you make in a channel. Nobody else can use them, and you're in control of how to present the output.

Claude Tag](https://claude.com/resources/articles/claude-tag-now-supports-personal-connectors-in-channels)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
