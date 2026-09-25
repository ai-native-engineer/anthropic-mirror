<!-- source: https://claude.com/blog/projects-redesigned -->

Explore here

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a42c9bc20d2072552ef256a_Node-EnterpriseAgents.svg)

# Projects redesigned: from folder to conversation

A new experience for Claude projects, now available in beta in Claude Code

* Category

  [Product announcements](https://claude.com/blog/category/announcements)

  [Claude Code](https://claude.com/blog/category/claude-code)
* Product

  [Claude Code](https://claude.com/product/claude-code)
* Date

  September 17, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/projects-redesigned

Managing multiple sessions across a build used to require you to divide the work, juggle handoffs, and stitch the results back together. Now in a Claude Code project, you describe what needs to get done and Claude manages the work.

Claude scopes the request, delegates the work, coordinates parallel threads, reviews the outputs, and assembles the finished result. You can steer progress throughout, even from your phone, and it keeps working after you step away from your computer.

For example, configure a project and set a goal to reduce your app's checkout p75 latency. Then ask Claude to profile each endpoint, test optimizations, and open PRs in parallel threads. Or connect your API, web, and mobile repos and set a goal to retire a deprecated v1 endpoint. Claude creates a thread per repo to migrate the callers, run the tests, open PRs, and then tells you which ones need to merge first.

Starting today, updated projects are available in beta to select Claude Pro and Max subscribers who use cloud sessions in Claude Code and don’t have any existing projects on the web or desktop.

Over the coming week, we'll expand access to more Claude Code users on those plans. Updated projects across all of Claude and Team and Enterprise plans come after that. If you're on Pro or Max and don't have access yet, you can join the [waitlist](https://claude.com/form/projects).

Existing projects on Pro and Max plans keep working as they do today. We'll upgrade them as the rollout expands to chat and Cowork.

## Threads do the work, Claude directs it

Projects have threads that do the work and a coordinator that directs them.

When you start a project, you select a goal as well as the repo or context. Claude starts by suggesting work it can pick up right away. You can configure the project’s cloud environment, connectors, plugins, instructions, and model.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6aac33beedd701b877e2516a_start-new-threads-card-ivory-2524w.png)

You can monitor and guide progress in the main project chat, or dive into each individual thread to examine and steer the details. Brief Claude in the project the way you'd brief a chief of staff and it routes work to new or pre-existing threads.

Claude also checks in and follows through on work. With repositories connected, a thread opens pull requests and runs your tests; with documents, it reads them and drafts.

Under the hood, each thread is a Claude Code cloud session working on its own branch and copy of the repo. The coordinator keeps work organized, but if any threads work on the same code, the overlap is resolved as a merge conflict just like any other PR.

Each thread can further split its delegated work into pieces using subagents, loops, and workflows when needed so large assignments finish faster.

## Context builds over time

Projects are designed for long-running or agentic workflows: work that takes longer than one reply and has more than one part.

Over time, Claude learns more about the project details and applies them to its work. Every thread now adds to and draws from a shared memory, reducing the need for complex prompt engineering.

For example, Claude can remember the release moved to Friday, why the export was dropped, or who to check in with before touching the billing service.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6aac17f18b4babdc667d967c_launch-readiness-under-4mb.gif)

*One project across a week. Each request opens a thread on the right; the memory, the decisions, and the results build underneath.*

Claude also remembers your working and communication style. You can ask it to adjust how often it checks in, how frequently it starts new threads, or how detailed to make each update.

Alongside memory, projects now include a library that collects the files you add and the artifacts produced by Claude. This makes it easier to find relevant materials and for new work to build on past efforts.

## What's next

Projects can run several threads at once, and each one is a full Claude Code session. Because of this, projects can reach usage limits faster. You can check project specific usage and select the model and effort levels used by the coordinator chat as well as the worker threads.

Threads run in the cloud today; running on your machine alongside your local tools and code and behind your network is coming very soon.

Start using [projects](https://claude.com/projects).

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2279047e82efc257633_6c7219042e95bfef1a126ad5ee8b2c7def8b8b0a-1000x1000.svg)

Sep 22, 2026

### What a task costs on Opus 5.5

Claude Code

[What a task costs on Opus 5.5](#)What a task costs on Opus 5.5

[What a task costs on Opus 5.5](https://claude.com/blog/what-a-task-costs-on-opus-5-5)What a task costs on Opus 5.5

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22deea97e4a5b5e5739_8d339ae8ecedecc1409db8f5bbb99c958db56946-1000x1000.svg)

Sep 24, 2026

### Claude Tag now supports personal connectors in channels

Product announcements

[Claude Tag now supports personal connectors in channels](#)Claude Tag now supports personal connectors in channels

[Claude Tag now supports personal connectors in channels](https://claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels)Claude Tag now supports personal connectors in channels

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225e31f7aa22c1f28cb_46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

Sep 24, 2026

### Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind.

Claude Code

[Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind.](#)Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind.

[Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind.](https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context)Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

Oct 20, 2025

### Claude Code on the web

Product announcements

[Claude Code on the web](#)Claude Code on the web

[Claude Code on the web](https://claude.com/blog/claude-code-on-the-web)Claude Code on the web

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Code

Coding
