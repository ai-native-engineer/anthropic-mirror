<!-- source: https://claude.com/docs/claude-tag/users/use-cases/create-artifacts -->

##  How artifact prompts work

An artifact here is a generated document, page, chart, or file Claude posts in the thread for the team to use, as opposed to a chat reply.
Each prompt below is a Slack message. You paste it in the thread or channel you want turned into something, Claude reads the discussion and posts progress in that thread, and the draft lands there too. What the draft is depends on the prompt, and each one below names the artifact it returns, like a decision doc, a customer reply, a filed ticket, or a planning outline.

##  Check the channel’s connections

Check that the channel has the connections below. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

| Connection | Examples | Why it matters here |
| --- | --- | --- |
| None | — | Works on Slack content alone |
| Issue tracking | Linear, Jira, Asana | Optional. Files tickets from the draft |

##  Prompts to paste

###  Draft from one thread

The thread settled the question, and what’s missing is the doc, the customer reply, or the ticket. Name the artifact in the thread where the discussion happened.

@Claude turn this thread into a one-page decision doc: what we decided, the options we rejected, and why.

@Claude draft a reply I can send to the customer based on this discussion. Keep it under 150 words.

@Claude file this thread as a ticket, assign it to the owner we discussed above, and post the link here.

Name the format and the length; “a doc” gets you a guess, “a one-pager with a decision section” gets you the artifact.

###  Keep a capture channel

Planning inputs arrive over a month, not in one sitting. Forward messages and ideas to one channel as you find them, then ask for a synthesis when you need the artifact.

@Claude go through everything posted in this channel this month and synthesize it into an outline for the planning doc.

## Catch up

When you need the summary, not the artifact

## Good habits

How to specify outputs that come back right

[Catch up](/docs/claude-tag/users/use-cases/catch-up)[Track projects and chase approvals](/docs/claude-tag/users/use-cases/track-projects)
