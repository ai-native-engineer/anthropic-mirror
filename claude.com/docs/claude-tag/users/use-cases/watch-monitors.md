<!-- source: https://claude.com/docs/claude-tag/users/use-cases/watch-monitors -->

##  How monitor-watch prompts work

This page is for operations and on-call teams. A monitor is an automated check in a tool like Datadog or PagerDuty that fires an alert when a metric crosses a threshold. These prompts have Claude check those dashboards or investigate alerts as they arrive.
Each prompt below is a Slack message. You paste it in the channel that receives the alerts, Claude checks the connected dashboards or investigates the alert and posts progress in that thread, and the findings land there too. What comes back depends on the prompt, and each one below names it, like a scheduled one-line-per-service check, a single alert’s diagnosis, or a standing watch that posts only changes.

##  Check the channel’s connections

Check that the channel has the connections below. Ask `@Claude what can you access from this channel?` to check; an admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

| Connection | Examples | Why it matters here |
| --- | --- | --- |
| Monitoring | Datadog, Sentry, PagerDuty | Required. Reads dashboards and alert state |

##  Prompts to paste

###  Schedule a recurring dashboard check

One message sets up a standing check that posts every morning, one line per service.

@Claude every morning at 7, check the service dashboards and post one line per service: green, or what's off and since when.

Name the output format in the schedule, like “one line per service” above, so every post reads the same way. To list or cancel scheduled work later, see [Manage standing work](/docs/claude-tag/users/proactivity#manage-standing-work).

###  Investigate a single alert

Reply in the thread the alert landed in for a first pass at diagnosis. The prompt names what diagnosis means here and where to put the result.

@Claude investigate this alert: when it started, what changed around then, and what you'd look at first. Post findings here.

“When it started, what changed around then” points the work at diagnosis, and “post findings here” keeps the trail in the thread for whoever picks it up.

###  Start the diagnosis before anyone asks

Set this up as a routine to get both: a scheduled check against the last known state, and an investigation kicked off for any change. The routine posts only when something changed, not on every check.

@Claude every two hours, check the alerting dashboard against its last state. For anything new, post when it started, what changed around then, and what to look at first.

## Fix bugs

When the investigation should end in a pull request

## Set up routines

Schedules and event triggers

[Pull deal and account state](/docs/claude-tag/users/use-cases/pull-deal-state)[Fix bugs](/docs/claude-tag/users/use-cases/fix-bugs)
