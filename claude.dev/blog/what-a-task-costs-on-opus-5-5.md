<!-- source: https://claude.dev/blog/what-a-task-costs-on-opus-5-5/ -->

# What a task costs on Opus 5.5

Opus 5.5 costs less per token than Opus 5.

Addy Osmani

Sep 25, 2026

21 min

What a task costs on Opus 5.5

[└The cost of a task, and the cost of a retry](#the-cost-of-a-task-and-the-cost-of-a-retry)[└What does a task cost?](#what-does-a-task-cost)[└What changed in Opus 5.5](#what-changed-in-opus-55)[└The same tasks side-by-side](#the-same-tasks-side-by-side)[└Tips for maximizing the value of your session](#tips-for-maximizing-the-value-of-your-session)[└Measure it yourself](#measure-it-yourself)[└Keep in mind](#keep-in-mind)

[X.com](https://twitter.com/intent/tweet?text=What%20a%20task%20costs%20on%20Opus%205.5%20%2F%20claude.dev%20Blog&url=https%3A%2F%2Fclaude.dev%2Fblog%2Fwhat-a-task-costs-on-opus-5-5%2F)[LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fclaude.dev%2Fblog%2Fwhat-a-task-costs-on-opus-5-5%2F)[Email](mailto:?subject=What%20a%20task%20costs%20on%20Opus%205.5%20%2F%20claude.dev%20Blog&body=https%3A%2F%2Fclaude.dev%2Fblog%2Fwhat-a-task-costs-on-opus-5-5%2F)Copy URL[Copy markdown](https://claude.dev/blog/what-a-task-costs-on-opus-5-5.md)

## THE COST OF A TASK, AND THE COST OF A RETRY

You don't set out to buy millions of tokens. You set out to build a feature, finish a migration, or run a task. The token count is whatever the model needed to get there.

Two models with the same cost per token can cost very different amounts on the same task. One reads the code once. The other reads it, tries a fix, and reads it again. Each of those steps is a turn, and each turn resends the conversation so far. So the model that needs more turns costs more, even at the same price.

By the end of this post you should be able to answer three questions about your own work:

* What do my typical tasks cost me on Opus 5.5?
* Which settings change that, and by how much?
* How do I check my own session usage?

The tradeoff I want to share upfront is that every way to spend fewer tokens can also cost you a finished task. Lower effort, a smaller model, or less context can all certainly save tokens. A retry costs more than those savings. This post attempts to put a price on each tradeoff.

Some numbers here are list prices, and some are illustrations built from them. The figures are interactive, so change the inputs as you read. These are best effort illustrations, so be sure to check our docs and your own math.

## WHAT DOES A TASK COST?

A task in Claude Code is a loop. The model reads the conversation, calls a tool, reads the result, and goes round again until it's done. Each trip round the loop is one request. Four things set what the loop costs.

**Turns.** Every turn resends the conversation so far. Fewer turns means less input processed.

**Cache reads.** Most of what a turn resends is text the model saw on the previous turn. It's billed as a cache read, at a small fraction of the input price.

**Output token type.** The most expensive tokens, at five times the input price. [Thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) is billed as output, so a model that reasons less on the way to the answer costs less.

**Model.** Each model has its own prices, listed on the pricing page, so the model you pick sets the price of every token.

Our examples use Opus 5.5 API list prices: $4 per million input tokens, $20 per million output tokens and $0.20 per million cache reads. Like the calculator further down, the examples bill cached input at the read price and everything else at the input price, and leave out cache writes. The token counts are illustrations.

### Turns

Let’s say a task starts with 20K tokens of context and grows to 120K as the model reads files and tool results. At 40 turns, the average turn sends about 70K tokens. That's about 2.8M input tokens for the task, though the conversation never grew past 120K. With 90% read from cache, the input costs about $1.62. The same task in 25 turns processes about 1.75M tokens and costs about $1.02 in input.

A turn costs more than the tokens it adds, because it resends everything before it. So the cheapest turn is the one you don't need.

One habit that can cut turns is giving the model a way to check its work. For example, a test to run, a build, or a script that calls the endpoint. A model that can check its own work finds its mistakes earlier.

A model that gathers what it needs in one pass, and batches its tool calls, pays the resend fewer times too.

### Cache reads

The same 2.8M input tokens cost $11.20 if none come from cache. At a 90% hit rate they cost $1.62, and at 96% about $0.99. No other setting moves input cost this much. A steady session keeps a high hit rate on its own. I cover some actions to avoid breaking your cache later in this post.

### Output tokens

On Opus 5.5, an output token costs 100 times a cache read. The 60K output tokens of a typical task cost $1.20, the same as reading 6M tokens from cache. Output includes thinking. You pay for all of it, even when Claude Code only shows you a summary. That's why effort, which mostly changes how much the model thinks, moves the bill so much.

### Model

A model with cheaper cache reads mostly helps long sessions. One with cheaper output mostly helps tasks that need a lot of reasoning.

## WHAT CHANGED IN OPUS 5.5

Two things changed: the price, and how much work the model does.

**Every price line is lower.** Input and output tokens are 20% cheaper than on Opus 5. Cache reads are 60% cheaper. The input price falls, and the read rate falls with it, from a tenth of the input price to a twentieth. Fig A compares the two models per million tokens. These are API list prices. On a Pro, Max or Team plan, the lower Opus 5.5 price is passed on to your limits, including cached context, so they go about 25% further than on Opus 5. The extra cut on cache reads is an API price change.

Separately, five-hour limits went up on Pro, Max, Team and seat-based Enterprise plans, and eligible subscribers get a limit reset to use when they choose. You'll find it under Settings > Usage on the web or in Claude Desktop, not in Claude Code in your terminal. A reset applies across your account, Claude Code included.

![Bar chart of API list prices per million tokens, Opus 5 against Opus 5.5: input $5.00 and $4.00, output $25.00 and $20.00, cache reads $0.50 and $0.20, which is 20%, 20% and 60% lower.](https://claude.dev/media/b05e27f1d72e92adffee8d13608665be2af86db6133408b498199bc0f13e62d2.png)

**FIG A**API list price per million tokens.

On an API key, the cache-read price cut matters most for Claude Code. A long agentic session spends most of its input on cache reads. In the session priced in Fig B below, the cache line falls from $1.00 to $0.40, the largest drop on the receipt.

How much you save depends on the shape of your work. A session that is mostly cache reads can save up to 60% on input. A short question with no cache and a long answer can save up to 20%, because output dominates it. Most Claude Code tasks sit between the two. The calculator below shows where yours sits.

You may have seen that Opus 5.5 costs 40% less to run than Opus 5. That's our estimate for typical workloads billed by token, at default settings. It assumes Opus 5.5 uses fewer tokens per task at its medium default, on top of the lower prices, so it isn't a 40% cut to the price of a token. The token prices are the ones in Fig A, and Fig B shows what the price change does on its own.

Opus 5.5 can use more tokens on an answer, because it always thinks before it replies. We expect people to get more done on Opus 5.5, but it varies by task, so measure it on your own work. Fig C compares cost per task on the two models. This part depends on your work far more than the price does.

On a well-scoped task, both models finish in about the same number of turns, and the price cut is all you get. The gap should be biggest on open-ended tasks, where a model can spend many turns on the wrong idea. No single number holds for every codebase, so measure it (see the last section).

**Long runs end with a report.** Opus 5.5 closes a long run with what it changed, what it found, and what it needs from you. That can save money too, because you rerun a session less often when you can see what happened.

## THE SAME TASKS SIDE-BY-SIDE

Fig B prices one session on both models with the same token counts. So the difference is the price change and nothing else. Switch models to compare. The token counts are illustrative.

Same tokens on Opus 5On Opus 5.5

$3.50at Opus 5 API list prices

* Read from cache 2.0M$1.00
* Fresh input 200K$1.00
* Output 60K$1.50
* Total, Opus 5$3.50

**FIG B**Illustrative session with the same tokens on both models, so this is the price change alone.

The receipt has the three lines /usage shows for a session. Cache reads are the biggest line by tokens, at 2M. Output is the smallest by tokens and the biggest by cost. Fresh input sits between them. It covers the first read of each file and each new tool result.

Fig B gives both models the same token counts, so it shows the price change alone. Your own sessions can use more or fewer tokens on Opus 5.5. Priced that way, the session costs about 31% less.

A recorded run adds the second effect, the change in how much work the model does. On a task with a false start, the gap should widen.

### Try your own numbers

Set what one of your tasks uses, or start from a preset. The presets are pretty illustrative but I’d still recommend doing your own math. Cached input bills at the cache-read price and fresh input at the input price, so the cache slider shows how much of the gap comes from cache reads.

To fill the sliders from a real session, run /usage at the end of a task. The Session block gives input, output and cache figures. The last slider is your assumption about how much less work Opus 5.5 does on your tasks. Leave it at 0% for the price change alone. To set it from your own work, here's how: run the same task on Opus 5 and on Opus 5.5, and compare turns and output tokens. Measure it yourself walks through it, and Reading a session shows what to check in /usage.

Typical Claude Code sessionSmall editLarge refactorLong agentic run

Input tokens2.2M

Everything sent to the model across all turns, cached or not.

Read from cache91%

Output tokens60K

Includes thinking, which is billed as output.

Tasks per day10

Token change on Opus 5.5 (your assumption)0%

Leave at 0% for price alone. Opus 5.5 can use more or fewer tokens than Opus 5, so measure it on your own tasks.

Opus 5, these tokens**$3.50**$770 a month

Opus 5.5, these tokens**$2.40**$528 a month

Change at API list prices**−31%**$242 less a month, from price alone

Opus 5, these tokens: $3.50. Opus 5.5, these tokens: $2.40. Change at API list prices: −31%, $242 less a month, from price alone.

**FIG C**A month is 22 working days. API list prices. On a Pro, Max or Team plan, this is not a bill. No batch or volume discounts, and cache writes are not counted (see [caching](#caching-and-compaction)).

## TIPS FOR MAXIMIZING THE VALUE OF YOUR SESSION

Opus 5.5’s lower price makes each token cost less. How you run a session decides how many tokens you use, and these steps help.

### Raise effort before you change models

Effort sets a general disposition for how many tokens the model spends on each turn: its thinking, the text it writes, and its tool calls. At lower effort it makes fewer tool calls and keeps them shorter. Opus 5.5 has four levels (low, medium, high and xhigh), plus max for a single session. Pick a level below to see when to use it and the command that sets it.

lowmechanicalmediumeverydayhighif it stallsxhighhard problemsmaxone session

Medium: for well-scoped daily work

Day-to-day work with a clear scope. It thinks less per turn than high, so each turn costs less.

Start here when the task is well scoped.

* `/effort medium`Copy
* `/effort status`Copy
* `/model`Copy
* `/usage`Copy

**FIG D**Levels run from least to most thinking per turn.

Claude Code sets a default level for each model, and /effort status shows yours. Try **medium** for well-scoped, day-to-day work. When medium stalls, try **high**. It spends more per turn than medium, but less than moving to a bigger model. Use **low** for mechanical work, like renames or applying a known pattern across files.

On Opus 5.5 the default is medium, one level below Opus 5's default of high. Levels don't mean the same amount of thinking on every model. At a given level, Opus 5.5 thinks more per turn than Opus 5, most of all at xhigh and max. So don't carry over a level you chose for Opus 5. Start at medium, and keep xhigh and max for work where you've measured a gain.

A rough way to think about effort pricing: say high adds 20K thinking tokens across a task. On Opus 5.5 that's $0.40. A retry loop of ten turns at 100K of cached context, with 10K output tokens in total, costs about the same. So high pays for itself on a task where it saves one retry. On a task medium would have finished the first time, it's wasted.

#### When medium fixes one layer

The clearest sign you need more effort is a fix that stops at one layer.

Say a field is renamed in an API handler. At medium, the model updates the handler, the handler's tests pass, and the client still sends the old field. It did what it was asked. It just didn't read far enough to find the second caller. At high, it spends more turns reading call sites before it writes, and it changes both layers in one pass.

A check can catch the same bug. If the model can run a test that goes through the client, the old field fails that test on the turn it was written, at medium. So before you raise effort, check whether the model has a way to check its work. A test run costs one turn and its output. More effort adds thinking to every turn.

If upgrading effort levels and adding checks doesn’t work, then switch to a bigger model.

#### Changing effort mid-session

In Claude Code, run /effort with a level, for example /effort high. /effort status prints the current level. You can change it mid-task, and the new level applies to the next request.

On Opus 5.5 with an API key or a Claude subscription, changing effort keeps the cache. You can raise it for one hard step and lower it again without rewriting the conversation. On Amazon Bedrock, Google Cloud's Agent Platform or a Claude apps gateway, a change of effort still clears the cached conversation, and the next request pays the cache-write price on all of it. Thinking is always on for Opus 5.5, so there's no thinking setting to change.

### Choose the right model for your work

Model choice sets the price of every token in a session, so it moves the bill more than effort does. It also reaches further. Every subagent that inherits the main model inherits its price too. Most days need three models: a small one for lookups, Opus 5.5 for work you supervise closely, and a bigger one for the hardest tasks.

![Three models in order of cost, with bars that show order of cost only: Haiku or Sonnet for lookups and subagents, Opus 5.5 as the daily driver, and Fable 5.1 for the hardest work, each with the kinds of work it suits.](https://claude.dev/media/f08757b9a91bce794fda0b6e3cd0deacede7783ce9db0097a67a47606e6900a4.png)

#### Opus 5.5 as the daily driver

Use Opus 5.5 for work you supervise: feature work across a few files, debugging, and code review with follow-up edits. You read what it does and step in when it drifts, so the loop stays short.

#### Moving up to Fable 5.1

**Move up to Fable 5.1 when the result matters more than the token price.** For example long runs you won't supervise, problems with no existing pattern in the codebase, and large changes that coordinate many subagents. Don't wait for a third failure. If Opus 5.5 on xhigh hits the same problem twice, switch, and switch back once it's solved. For interactive work, Opus 5.5 is a better fit as it has lower latency and costs less.

Fable 5.1 lists at $10 per million input tokens and $50 per million output, two and a half times the Opus 5.5 price. Its cache reads cost $0.25 per million, only 1.25 times the Opus 5.5 rate, because they bill at 0.025 times its input price. So the gap is smallest on a long, cache-heavy run, and largest on a task that writes a lot.

Switch at a natural break. The cache belongs to the previous model, so expect the first turn on the new model to pay the write price on the whole conversation. Run /compact first, or start a fresh session with a short written plan, to make that turn smaller. Run [/model](https://code.claude.com/docs/en/model-config) with an alias or a model name to switch. /model also saves your choice as the default for new sessions, so switch back when the hard part is done.

#### Moving down for lookups

**Move down to Sonnet or Haiku for lookups, not for writing code:** subagents that search and summarize, reading logs and test output, and "where is this defined" questions. For a mechanical edit across many files, keep Opus 5.5 and set effort to low. The edit stays on the model that writes the rest of your code, at a lower cost per turn.

To put a [subagent](https://code.claude.com/docs/en/sub-agents) on a smaller model, set model: haiku or model: sonnet in its definition. To put every subagent on one model, set the CLAUDE\_CODE\_SUBAGENT\_MODEL environment variable. A model named in a subagent's definition overrides the variable. A subagent with no model setting runs on your main model, unless the variable is set.

Each subagent runs in its own context window and hands back a summary, so its file reads stay out of your main conversation. It still pays for its own tokens, so the model setting decides what that spend costs.

Agent teams, an experimental feature, multiply this. Each teammate is a separate Claude Code instance with its own context window, and it keeps using tokens until it exits. Our [costs docs](https://code.claude.com/docs/en/costs) put a team at about seven times the tokens of a standard session when teammates run in plan mode. Keep teams small, keep each task self-contained, and shut teammates down when their part is done.

The tradeoff: a small model that misreads a search result sends the main model after the wrong file, and the main model pays for the detour. Keep the small model on work where a mistake is cheap to spot, like finding files, running tests and reading logs.

Keep judgment calls on the main model. The opusplan alias splits the work a different way: Opus plans in plan mode, and Sonnet carries out the plan. That puts the code edits on Sonnet, the opposite of the advice above. Measure it on your own tasks before you make it a default.

### Check your prompts when you migrate

Instructions written for an older model can make Opus 5.5 write more and repeat tool calls. Run /claude-api prompt-audit in Claude Code to check your Claude Code setup, such as your skills and CLAUDE.md file, for these [prompting anti-patterns](https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform). It also checks the code of an app you build on the Claude Platform.

We tested this on a migration from Opus 4.8 to Opus 5.5, using an internal customer support benchmark of 44 tickets whose prompt had several of these patterns. The move to Opus 5.5, at low effort, cut the benchmark's cost by about 18%. Running prompt-audit cut it by a further 9%, to about 25% below the Opus 4.8 starting point. The audit removed ritual instructions that made the model write more and repeat tool calls: a mandatory six-step procedure, a scratchpad rule, a verify-twice rule, and instructions that contradicted each other.

That result comes from one benchmark, so treat it as an example rather than a number to expect. Run the audit, then compare /usage on a real task before and after (see Measure it yourself).

### Caching and compaction

Claude Code handles caching and compaction for you. How you run a session decides how much they save.

#### How the cache works

Claude Code caches the parts of a request that repeat, such as the system prompt, tool definitions, and the conversation so far.

On Opus 5.5 a cached read costs 5% of a fresh input token. Writing to the cache costs more than a fresh read, at 1.25 times the input price for a five-minute cache and twice the input price for a one-hour cache, on today's pricing. Each hit resets the lifetime at no charge.

In Claude Code the lifetime depends on how you pay. On a Claude subscription it's an hour. On an API key or a cloud provider it's five minutes by default, and a subscription drops to five minutes once it's drawing on usage credits.

At 120K tokens of context, a five-minute write on Opus 5.5 costs about $0.60 and a read about $0.02. One write costs as much as 25 reads. On an API key, a six-minute coffee break turns the next $0.02 read into a $0.60 write. A one-hour write at the same size costs about $0.96, and on the API you can pay that premium to cover the gaps in your day.

#### Session shape and hit rate

The cache stores a prefix, so it can reuse only the part of a request that matches the previous one from the start.

A steady session appends to the end of the conversation on every turn and keeps its hit rate high. Anything that changes an earlier part of the request lowers it. Changing the tool definitions clears the whole cache, and a change to the system prompt clears it from that point on, which is almost everything.

In practice, expect a cache write when:

* You pause longer than the cache lifetime;
* You change effort on Amazon Bedrock, Google Cloud's Agent Platform or a gateway, where the level is part of what the cache matches;
* You turn on fast mode for the first time in a conversation, which changes part of what the cache matches;
* You connect or disconnect an MCP server, which can change what loads at the start of each request;
* You switch models, since the new model starts from an empty cache; and
* The conversation is compacted, which rewrites the history the cache matched.

So set these up when the session starts, and leave them alone while it works.

#### Why long sessions cost more per turn

Every turn resends the whole context, so a turn costs more as the context grows, even with a warm cache. At 20K tokens of context a turn's cache read costs about $0.004 on Opus 5.5. At 150K it costs about $0.03, and 30 turns at that size spend $0.90 on reads alone. The same 30 turns at 20K cost about $0.12. On Claude 4.6 and later models a bigger context window doesn't change the price per token, so the cost comes entirely from resending the conversation.

Much of that context is left over from earlier work: a stack trace from an hour ago, a file you've finished with, the output of a test run you've since fixed. It's all still sent on every turn.

#### Compaction, /compact and /clear

When a session gets close to its context limit, Claude Code summarizes older history so later turns send less. Run /autocompact with a token count to change how full the context gets before that happens.

Two commands let you do this yourself. /clear empties the conversation and costs nothing, so use it when you move to unrelated work. /compact keeps continuity and costs one request. It reads the conversation it summarizes, and you can say what to keep, for example /compact keep the failing test names and the schema change.

A rough price for compacting at 150K tokens is about $0.25. That's the read, a summary of a few thousand output tokens, and a new cache write on the shorter context. Each later turn saves about $0.025 in reads, so the compaction pays for itself within about ten turns. A compaction just before you finish costs more than it saves.

That price assumes a warm cache. While the cache is warm, the summary request reads the conversation from it, so compact before a break, not after one. After a break longer than the cache lifetime, the same /compact reads the whole conversation again and writes it back to the cache. At 150K tokens on a five-minute cache, the input alone comes to about $0.75. If you've gone down a path you want to drop, /rewind to an earlier turn instead. While the cache is warm, that returns to a prefix that's already cached.

The summary also loses detail. A compaction in the middle of a debugging session can drop the one log line that mattered. Compact at a natural break, and when the next step depends on something specific, say so in the /compact instruction.

#### What loads before you type

Your [CLAUDE.md file](https://code.claude.com/docs/en/memory) loads into the context at the start of every session, so each line in it is part of what every turn resends. The [costs docs](https://code.claude.com/docs/en/costs) suggest keeping it under 200 lines. MCP tool definitions are deferred. Only tool names and server instructions load at the start, and a full definition loads when its tool is used. Run /mcp to see which servers are connected, and turn off the ones you aren't using.

#### The rest of the bill

The table lists the other billing rules that affect a Claude Code session, with a link to the docs where one exists.

Fast mode runs Opus 5.5 up to 2.5 times faster, at twice the standard price: $8 per million input tokens and $40 per million output. On a Claude subscription it's billed to usage credits, not your plan limits. The first request after you turn it on pays the fast-mode input price on the whole conversation, uncached. So turn it on at the start of a session, not deep into one.

| What the bill counts | How it works |
| --- | --- |
| Cache lifetime | In Claude Code, one hour on a subscription; five minutes on an API key or cloud provider, or once a subscription draws on usage credits. Each hit resets the lifetime. The API offers a one-hour cache at a higher write price. [Costs docs (Claude Code lifetime) and prompt caching docs](https://code.claude.com/docs/en/costs) |
| Cache writes | 1.25× the input price for a five-minute cache and 2× for a one-hour cache, on today's API pricing. [Pricing docs](https://platform.claude.com/docs/en/about-claude/pricing) |
| Thinking | Billed as output tokens, including thinking that isn't returned to you. [Extended thinking docs](https://platform.claude.com/docs/en/build-with-claude/thinking) |
| Effort | Applies to every output token: text, tool calls and thinking. [Effort docs](https://platform.claude.com/docs/en/build-with-claude/effort) |
| Auto-compaction | Runs as the context window nears its limit. /autocompact with a token count sets the threshold. [Context window docs](https://code.claude.com/docs/en/context-window) |
| Subagents and agent teams | A subagent works in its own context window and returns a summary. Agent teams in plan mode use about 7× the tokens of a standard session. [Context window and costs docs](https://code.claude.com/docs/en/costs) |
| Batch API | Half price on input and output tokens for requests sent through the Message Batches API. [Batch processing docs](https://platform.claude.com/docs/en/build-with-claude/batch-processing) |
| Typical spend today | Average: about $13 per developer per active day across enterprise deployments. For 90% of users, cost stays below $30 per active day. Both figures are for current models. [Public docs, costs page (enterprise average and 90% bound)](https://code.claude.com/docs/en/costs) |

## MEASURE IT YOURSELF

The figures in this post are illustrations. Your codebase, prompts and habits are different, so measure cost on your own tasks. Here's how to check.

1. **In a session, run [/usage](https://code.claude.com/docs/en/costs).** /cost does the same thing. The Session block shows token use and an estimated dollar cost at list price. A prompt-cache line shows how much of your input came from cache. On a Pro, Max, Team or Enterprise plan, the same screen shows your plan usage bars. The dollar figure is computed on your machine at list price, so on a subscription it is a guide to how much work you did, not a bill.
2. **Run the same task twice.** Opus 5.5 needs Claude Code v2.1.280 or later, so run `claude update` first. Pick something from your backlog, not a toy example. Use /model to switch between Opus 5 and Opus 5.5. Note turns, output tokens and cost for each run. Do three or four tasks before you draw a conclusion.
3. **For a team, use the usage and cost reports.** The [Claude Code Analytics API](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api) gives estimated cost per user. The [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api) breaks spend down by model and by cached versus uncached tokens.
4. **Try the effort ladder.** Run one hard task at medium and then at high. Run one mechanical task at low.

### Reading a session

Check three things in /usage at the end of a task.

* **Cache share.** For a long session it should be high. If it's low, look for a long pause, a model switch, an MCP server connected partway through or, on a cloud provider or gateway, a change of effort. The prompt cache line often names the likely cause of the last miss.
* **Output against input.** A lot of output on a small change usually means the effort level is too high for the task, or the model is retrying.
* **Total input against the size of the conversation.** If the total is many times the size of the conversation, the session took many turns, and the conversation is worth reading to find where the loop repeated.

For a baseline, the Claude Code costs docs give an average across enterprise deployments of about $13 per developer per active day, and under $30 per active day for 90% of users. A session that costs well above your own normal level is worth reviewing.

## KEEP IN MIND

* Use medium effort for well-scoped daily work.
* Give the model a way to check its work, and start changes that span files in plan mode.
* When medium stalls, raise effort to high. With an API key or a subscription the change keeps your cache. On a cloud provider or gateway, change it at a break.
* If xhigh hits the same problem twice, switch to Fable 5.1. Switch back once it's solved.
* Put search and log-reading subagents on Sonnet or Haiku. Keep code edits on Opus 5.5.
* Keep a long session moving, so its cache stays warm.
* Use /clear between unrelated tasks, and /compact at a break with a note on what to keep.
* **The one that matters most:** run one real task on each model and compare what /usage reports. Your own numbers are the ones to trust.

I hope this post was helpful. If your limits don’t go further on Opus 5.5 than on Opus 5, tell us with /feedback.

Further reading: [Manage costs effectively](https://code.claude.com/docs/en/costs) · [Model configuration](https://code.claude.com/docs/en/model-config) · [Choosing a Claude model and effort level in Claude Code](https://claude.com/blog/claude-model-and-effort-level-in-claude-code) · [Effort](https://platform.claude.com/docs/en/build-with-claude/effort) · [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) · [Maximizing the value of your Claude Code sessions](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions)

*With thanks to Michael Segner, Kacie Jenkins and Molly Vorwerck for their reviews.*

[Oct 01, 2026Getting started with Claude Code mods11 min](https://claude.dev/blog/getting-started-with-claude-code-mods/)[Sep 28, 2026Automating eval design and hillclimbing with Claude12 min](https://claude.dev/blog/automating-eval-design-and-hillclimbing/)[Sep 28, 2026Building with Claude Sonnet 5.59 min](https://claude.dev/blog/building-with-claude-sonnet-5-5/)[Sep 25, 2026Using Claude Code: Spending your effort8 min](https://claude.dev/blog/spending-your-effort/)[Sep 23, 2026How we made claude.ai 3x faster in two weeks15 min](https://claude.dev/blog/how-we-made-claude-ai-faster/)
