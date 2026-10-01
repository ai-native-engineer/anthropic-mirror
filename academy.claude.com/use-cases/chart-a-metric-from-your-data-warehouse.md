<!-- source: https://academy.claude.com/use-cases/chart-a-metric-from-your-data-warehouse -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Chart a metric from your data warehouse

Ask a data question in the thread where a number is being discussed, and Claude Tag queries the connected warehouse and replies with a chart and the query.

10 minResearchClaude Tag

![](https://academy.claude.com/assets/v1/thumbnail.light-mlmvli26.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-o1dom7ee.png)

A team discussing a metric in a channel can ask for the number in the thread and get it there, as a chart, while the discussion is still going. With Claude Tag connected to the data warehouse, anyone in the channel can ask, whether or not they write SQL. The query arrives with the chart, so the people who own the metric can see how it was counted.

Ask in the thread, and Claude runs the query and posts **[the chart and the query as artifacts(opens in new tab)](https://claude.com/docs/claude-tag/users/use-cases/create-artifacts)** there. In the thread, **[anyone on the team can reply to correct it(opens in new tab)](https://claude.com/docs/claude-tag/concepts/how-it-works#reply-in-the-thread-to-steer)**. Claude can save a correction for the channel, and post a number the team checks every week as a **[routine(opens in new tab)](https://claude.com/docs/claude-tag/users/proactivity#scheduled-jobs)**.

## Set up[](#set-up)

**Make sure Claude is in the channel:** `/invite @Claude`.

**Check what tools are connected:** `@Claude what can you access from this channel?`

For help, ask your admin or visit our [troubleshooting docs(opens in new tab)](https://claude.com/docs/claude-tag/users/troubleshooting).

## What to ask Claude, and what it does[](#what-to-ask-claude-and-what-it-does)

Ask in the thread where the discussion is happening, each time you need a number from the data warehouse. Name the metric and the time period. Claude reads the whole thread, so you can refer to something said earlier without describing it again.

Open the query to see what it counted and what it left out, and reply in the thread if your team counts the metric differently.

## Follow ups[](#follow-ups)

### Correct how the metric is counted, and have Claude remember it for the channel[](#correct-how-the-metric-is-counted-and-have-claude-remember-it-for-the-channel)

Claude redraws a chart from a correction in the thread. When the correction should apply from now on, for example that reactivated accounts should not count as signups, ask Claude to remember it for the channel ([channel memory(opens in new tab)](https://claude.com/docs/claude-tag/users/memory)):

### Get key metrics posted on a schedule[](#get-key-metrics-posted-on-a-schedule)

Claude can run a query and post the chart every morning ([routine(opens in new tab)](https://claude.com/docs/claude-tag/users/proactivity)). Name the format so each post stays short, and name the time zone.

### Ask Claude which routines are set up in this channel[](#ask-claude-which-routines-are-set-up-in-this-channel)

Claude lists a channel's routines when asked. Check before adding one, and stop one by naming it ([manage standing work(opens in new tab)](https://claude.com/docs/claude-tag/users/proactivity#manage-standing-work)).

### Chart numbers people posted in the channel, without a warehouse[](#chart-numbers-people-posted-in-the-channel-without-a-warehouse)

Without a warehouse connection, Claude can chart numbers people posted in the channel, such as request volume in a triage channel.

## Tips[](#tips)

### Keep each task in its own thread[](#keep-each-task-in-its-own-thread)

Claude treats a thread as one continuing conversation, so each reply builds on the last and follow-up questions can be short. A new message in the channel starts a fresh conversation, so include what Claude needs, such as the metric and the time period.

## Related resources[](#related-resources)

* Learn more in the [Introduction to Claude Tag(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-tag) course.
* [Get started with Claude Tag(opens in new tab)](https://claude.com/docs/claude-tag/users/getting-started): add @Claude to a channel and see what it can read there.
* [Answer data questions(opens in new tab)](https://claude.com/docs/claude-tag/users/use-cases/answer-data-questions): the Claude Tag docs page this use case is based on.

* [Set up](#set-up)
* [What to ask Claude, and what it does](#what-to-ask-claude-and-what-it-does)
* [Follow ups](#follow-ups)
* [Tips](#tips)
* [Related resources](#related-resources)
