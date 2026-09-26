<!-- source: https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context -->

Explore here

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225e31f7aa22c1f28cb_46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

# Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind.

Our latest Opus model is priced and trained to optimize costs for how developers code now.

* Category

  [Claude Code](https://claude.com/blog/category/claude-code)

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)
* Product

  [Claude Code](https://claude.com/product/claude-code)

  [Claude Enterprise](https://claude.com/solutions/enterprise)
* Date

  September 24, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context
* Author(s)

  Michael Segner

We estimate Claude Opus 5.5 [costs about 40% less](https://www.anthropic.com/claude-opus-5-5) to run than Opus 5 for typical workloads billed by token. For developers, exactly *how* those savings stack up matters.

If you pay by the token, you will see the greatest cost difference for longer-running, higher context sessions–the exact type of Claude Code sessions that have become more prevalent in the last six months.

This post will dive into the mechanics of what makes Opus 5.5 cost effective for how developers are coding today (and likely tomorrow).

## **Claude Code trends**

We've pulled aggregate data on how developers have been using Claude Code from March to September 2026. As model capabilities improve, developers have been deploying agents in increasingly sophisticated ways. The number of prompts per session has been steady, but we found some interesting behaviors:

* Claude works 3.3x longer on each prompt with more than 40% more model calls per prompt. There are 68% fewer interruptions.
* Developers are about twice as likely to have a tool server connected or use a skill and a third less likely to paste text into a prompt.
* Context per request has grown 2.6x. The input to output token ratio moved from 189:1 to 324:1.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6ab54d371474ec5e28cb0912_0dfedac7.png)

All of this points to developers aiming a harder working, better informed Claude toward bigger, more open-ended tasks. For these types of sessions, the economic impact of context engineering is compounded.

Simply put, Claude reads more tokens. You need to make sure [all the context you are providing is necessary](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models), and that [as much of that context as possible is reading from cache](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions).

## **What makes Opus 5.5 cost effective for long, context heavy sessions**

There are three changes that make long-running, context-heavy sessions more cost effective: changes to pricing, model behavior, and the Claude Code harness. Let’s look at each.

### **Cache is cheap**

For usage billed by the token, we reduced the cost of input and output tokens 20%, and *we dropped the price of reading a cached token 60%*. The latter reduction is significant because cache reads make up the majority of agentic and coding work costs.

And as we just discussed, context per request has increased roughly 2.6x in six months, which means savings are trending in the right direction. The same price change for those billed by token saves more on today's Claude Code traffic than it would have six months ago, because more of the bill is now re-read context.

As of the publication date, a cached token on Opus 5.5 costs a fifth of what it does compared to competing models while outperforming them.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6ab54d381474ec5e28cb0920_7df87a60.png)

### **Claude Code is better at using the cache**

This is less specific to Opus 5.5, and more the result of many of the Claude Code features we’ve added in the last six months. Given the coding session trends we just discussed, you would expect a higher rate of cache misses, but the opposite is true. **Input that misses the cache decreased by more than 50%.**

For example, we made it harder to unintentionally break your cache with smaller papercuts like refreshing a login. We also made it harder to break with larger actions, like adding instructions mid-conversation or loading tools on demand. For newer models like Opus 5.5 and Fable 5.1, you can now change effort levels during your sessions without resetting your cache.

We also made the cache more useful for longer-running and delegated sessions. Developers on API keys and cloud providers can now set a one-hour cache lifetime (which subscribers already had) and forked subagents start from the parent's cache instead of paying for the same context again.

### **The same task, but with fewer turns**

Opus 5.5 can need fewer turns than other models to accomplish the same task. Zeta Labs saw fewer turns and tool calls per task than Opus 5, but at nearly half the cost and twice as many of their hardest tasks completed.

This won't hold for every task. In [The cost of a task on Opus 5.5](https://claude.com/blog/what-a-task-costs-on-opus-5-5), Addy wrote, "On a well-scoped task, both models finish in about the same number of turns, and the price cut is all you get. The gap should be biggest on open-ended tasks, where a model can spend many turns on the wrong idea. No single number holds for every codebase, so measure it."

In other words, simple, short, and mechanical tasks will take the same amount of turns while longer, harder tasks have more potential for Opus 5.5 to avoid burning tokens on the wrong approach. A reduced turn is even more cost efficient than a cached token.

Also worth noting, especially as Claude works longer unattended or uninterrupted, is that Opus 5.5 generates output more than 30% faster than Opus 5. While this doesn’t increase cache hit rate or use less tokens, it means waiting less on long runs.

## **Protect your cached reads**

As agentic coding has matured, organizations have shifted from asking developers to scale at all costs to asking developers to scale efficiently. Run /usage in Claude Code to see how much of your usage is cached reads. Then protect that number:

* Pick your model at the start of a session rather than switching midway,
* Compact before you step away rather than after, and
* If you're on an API key or cloud provider, set the [one-hour cache lifetime](https://code.claude.com/docs/en/prompt-caching#choose-the-ttl-yourself) for long sessions.

Point Opus 5.5 at the open-ended, context-heavy work where those habits compound, and see [What a task costs on Opus 5.5](https://claude.com/blog/what-a-task-costs-on-opus-5-5) for the worked numbers.

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22deea97e4a5b5e5739_8d339ae8ecedecc1409db8f5bbb99c958db56946-1000x1000.svg)

Sep 24, 2026

### Claude Tag now supports personal connectors in channels

Product announcements

[Claude Tag now supports personal connectors in channels](#)Claude Tag now supports personal connectors in channels

[Claude Tag now supports personal connectors in channels](https://claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels)Claude Tag now supports personal connectors in channels

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2287f90c57df4c9dd97_c1ef4c0b6882dfe985555b52999d370ea88a3c50-1000x1000.svg)

Sep 23, 2026

### How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel on Claude Marketplace

Enterprise AI

[How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel on Claude Marketplace](#)How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel on Claude Marketplace

[How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel on Claude Marketplace](https://claude.com/blog/how-coderabbit-power-digital-and-thoughtspot-scale-with-snowflake-and-vercel-on-claude-marketplace)How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel on Claude Marketplace

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

Sep 23, 2026

### How to prepare for AI-driven code modernization projects

Enterprise AI

[How to prepare for AI-driven code modernization projects](#) How to prepare for AI-driven code modernization projects

[How to prepare for AI-driven code modernization projects](https://claude.com/blog/how-to-prepare-for-ai-driven-code-modernization-projects) How to prepare for AI-driven code modernization projects

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2287f90c57df4c9dd97_c1ef4c0b6882dfe985555b52999d370ea88a3c50-1000x1000.svg)

Sep 17, 2026

### Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5

Enterprise AI

[Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5](#)Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5

[Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5](https://claude.com/blog/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5)Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5

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

Claude Enterprise

Coding
