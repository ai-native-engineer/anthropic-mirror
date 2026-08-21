<!-- source: https://claude.com/blog/introducing-routines-in-claude-code -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f783c784823d48ad84175_Object-CodeChatText.svg)

# Introducing routines in Claude Code

Define repeatable routines that work your backlog, review your PRs, and respond to events in the cloud.

* Category

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  [Claude Code](https://claude.com/product/claude-code)
* Date

  April 14, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/introducing-routines-in-claude-code

Today, we're introducing routines in Claude Code in research preview. A routine is a Claude Code automation you configure once — including a prompt, repo, and connectors — and then run on a schedule, from an API call, or in response to an event. Routines run on [Claude Code’s web infrastructure](https://code.claude.com/docs/en/claude-code-on-the-web), so nothing depends on your laptop being open.

Developers already use Claude Code to automate the software development cycle, but until now, they've managed cron jobs, infrastructure, and additional tooling like MCP servers themselves. Routines ship with access to your repos and your [connectors](https://claude.com/connectors), so you can package up automations and set them to run on a schedule or trigger.

## How it works

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69de678887f94fb639698fa7_dd878b86.png)

### Scheduled routines

Give Claude Code a prompt and a cadence (hourly, nightly, or weekly) and it runs on that schedule:

```
Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR.
```

If you're using [/schedule](https://code.claude.com/docs/en/scheduled-tasks#compare-scheduling-options) in the CLI, those tasks are now scheduled routines.

### API routines

You can also configure routines to be triggered by API calls. Every routine gets its own endpoint and auth token. POST a message, get back a session URL. Wire Claude Code into your alerting, your deploy hooks, your internal tools—anywhere you can make an HTTP request:

```
Read the alert payload, find the owning service, and post a triage summary to #oncall with a proposed first step.
```

If you're building cloud-hosted agents on the Claude Platform rather than automating Claude Code, [scheduled deployments in Claude Managed Agents](https://claude.com/blog/whats-new-in-claude-managed-agents) give your own agents the same run-on-a-schedule behavior.

### Webhook routines, starting with GitHub

Subscribe a routine to automatically kick off in response to GitHub repository events. Claude will create a new session for every PR matching your filters and run your routine.

```
Please flag PRs that touch the /auth-provider module. Any changes to this module need to be summarized and posted to #auth-changes.
```

Claude opens one session per PR and will continue to feed updates from that PR to the session, so it can address follow-ups like comments and CI failures.

We plan to expand webhook-based routines to trigger from more event sources in the future.

## What teams are building

A few common patterns have emerged for early users creating routines:

### Scheduled routines

* Backlog management: triage new issues nightly, label, assign, and post a summary to Slack
* Docs drift: scan merged PRs weekly, flag docs that reference changed APIs, and open update PRs

### API routines

* Deploy verification: your CD pipeline posts after each deploy, Claude runs smoke checks against the new build, scans error logs for regressions, and posts a go/no-go to the release channel
* Alert triage: point Datadog at the routine's endpoint, Claude pulls the trace, correlates it with recent deployments, and has a draft fix waiting before on-call opens the page
* Feedback resolution: a docs feedback widget or internal dashboard posts the report, Claude opens a session against the repo with the issue in context, and drafts the change

### GitHub routines

* Library port: every PR merged to a Python SDK triggers a routine that ports the change to the parallel Go SDK, and opens a matching PR
* Bespoke code review: on PR opened, run your team's own checklist across security and performance, leaving inline comments before a human reviewer looks

## Getting started

Routines are available today for Claude Code users on Pro, Max, Team, and Enterprise plans with [Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web#who-can-use-claude-code-on-the-web) enabled. Head to [claude.ai/code](http://claude.ai/code) to create your first routine, or type /schedule in the CLI.

Routines draw down subscription usage limits in the same way as interactive sessions. In addition, routines have daily limits: Pro users can run up to 5 routines per day, Max users can run up to 15 routines per day, and Team and Enterprise users can run up to 25 routines per day. You can run extra routines beyond these limits with extra usage. [See the docs](http://code.claude.com/docs/en/routines) for more information.

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

Get Claude Code

curl -fsSL https://claude.ai/install.sh | bash

Copy command to clipboard

irm https://claude.ai/install.ps1 | iex

Copy command to clipboard

Or read the [documentation](https://code.claude.com/docs/en/overview)

Try Claude Code

[Try Claude Code](https://claude.ai/code)Try Claude Code

Developer docs

[Developer docs](https://code.claude.com/docs/en/overview)Developer docs

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

Aug 20, 2026

### Build production agents with computer use, the Skills API, and the Files API

Product announcements

[Build production agents with computer use, the Skills API, and the Files API](#)Build production agents with computer use, the Skills API, and the Files API

[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api)Build production agents with computer use, the Skills API, and the Files API

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

Aug 20, 2026

### Anthropic’s approach to teaching and learning AI

Product announcements

[Anthropic’s approach to teaching and learning AI](#)Anthropic’s approach to teaching and learning AI

[Anthropic’s approach to teaching and learning AI](https://claude.com/blog/anthropics-approach-to-teaching-and-learning-ai)Anthropic’s approach to teaching and learning AI

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22bed4b18b6703cd710_e750c875fbd7f08ffb6495efa180a8ed60de3611-1000x1000.svg)

May 19, 2026

### New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

Product announcements

[New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](#)New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

[New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](https://claude.com/blog/claude-managed-agents-updates)New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2260bfc90348429f9c3_cd9cf56a7f049285b7c1c8786c0a600cf3d7f317-1000x1000.svg)

Aug 13, 2026

### Claude Tag now reads even more of the room

Product announcements

[Claude Tag now reads even more of the room](#)Claude Tag now reads even more of the room

[Claude Tag now reads even more of the room](https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room)Claude Tag now reads even more of the room

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

Work

Productivity

Agents
