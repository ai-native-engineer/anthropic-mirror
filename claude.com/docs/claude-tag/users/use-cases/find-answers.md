<!-- source: https://claude.com/docs/claude-tag/users/use-cases/find-answers -->

##  How answer-finding prompts work

Each prompt below is a Slack message. You paste it in the channel where the question came up, Claude searches the connected docs or the channel history and posts progress in that thread, and the answer lands there too. The result is always an answer with the source it came from, so you can open what it read.

##  Check the channel’s connections

Check that the channel has the connections below. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

| Connection | Examples | Why it matters here |
| --- | --- | --- |
| Knowledge and docs | Google Drive, Notion, Confluence | Required to search those sources; channel-history-only answers need none. Searches the docs the answers live in |

##  Prompts to paste

###  Look up a policy

A customer asks about data retention and you need the policy, not a recollection. Ask where the question comes up.

@Claude what's our policy on data retention, and which doc says so?

Asking for the doc keeps the answer checkable, since you can open what it read.

###  Check a named document

Launch is close and you need to know whether the plan covers the EU rollout, without re-reading it. Point it at the document and the question.

@Claude does the launch plan cover the EU rollout? Quote the relevant section if it's there.

“Quote the relevant section” turns a yes/no into evidence.

###  Find the latest version

The pricing deck gets recreated every quarter, and the link you saved is two versions old. Ask for the current one.

@Claude find the latest pricing deck and post where it lives.

###  Answer from the channel alone

Without any connection, Claude can still answer from the channel’s own history.

@Claude what did this channel decide about the retention policy, and when?

Answers come from this channel’s history and [memory](/docs/claude-tag/users/memory).

## Catch up

The same mechanism pointed at “what did I miss”

## What Claude Tag remembers

How channel knowledge accumulates

[Answer data questions](/docs/claude-tag/users/use-cases/answer-data-questions)[Pull deal and account state](/docs/claude-tag/users/use-cases/pull-deal-state)
