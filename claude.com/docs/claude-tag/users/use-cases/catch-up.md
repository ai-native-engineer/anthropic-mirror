<!-- source: https://claude.com/docs/claude-tag/users/use-cases/catch-up -->

##  How catch-up prompts work

Each prompt below is a Slack message. You paste it in any channel Claude is in, Claude reads the channel or thread history and posts progress in that thread, and the recap lands there too. The result is always a summary of what was said, returned once or every morning depending on the prompt.

##  Check the channel’s connections

This use case needs no connections; it works on Slack history alone. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

##  Prompts to paste

###  Get a one-off recap

A thread ran to forty replies overnight, or you skipped a channel for a week. Ask for the catch-up you need.

@Claude catch me up on this channel since Monday.

@Claude what got decided in this thread, and what's still open?

@Claude summarize what I missed last week, grouped by topic.

Each of these bounds the work with a time window, one thread, or a grouping, so the summary comes back in a shape you can check.

###  Schedule a daily recap

If the first stretch of every morning goes to re-reading channels, schedule the recap instead. One message sets up a rollup that posts before you start the day.

@Claude every weekday at 9am, post a summary of open threads in this channel and anything that looks like it's waiting on someone.

“Waiting on someone” makes the rollup surface actions, not just a recap of yesterday. To list or cancel scheduled work later, see [Manage standing work](/docs/claude-tag/users/proactivity#manage-standing-work).

## Turn threads into docs and tickets

When the catch-up should become an artifact

## Set up routines

Scheduling and triggers

[Triage requests](/docs/claude-tag/users/use-cases/triage-requests)[Turn threads into docs and tickets](/docs/claude-tag/users/use-cases/create-artifacts)
