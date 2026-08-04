<!-- source: https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22c10cdf166eebe4c84_d4b15045df86e43e5b5dc7b25784321ce8b5dd88-1000x1000.svg)

# Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night

*Silas Alberti, SVP of Research at Cognition, has tested nearly every Claude model inside Devin, the company's AI software engineer. Claude Fable 5 is the first he'd trust to leave running overnight.*

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)
* Product

  No items found.
* Date

  July 10, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night

Cognition is young, even by Silicon Valley standards. It built Devin, its autonomous AI software engineer, in early 2024, at a time when the basic mechanics of an agent barely held together.

Devin takes on the work engineers never quite get to: codebase migrations, the backlog of bugs, the features that keep slipping. With customers ranging from high-growth startups to Fortune 500 companies, the bar is high. Code written by Devin has to be reliable and production-ready; a small bug introduced quietly can cause real problems downstream.

Alberti’s team trains and tests the models behind Devin and has run nearly every Claude generation since the start. He traces the first real jump to Claude 3.6 Sonnet in late 2024. It was the first model that could reliably chain tools and hold a multi-step task. When the team plugged it into Devin, internal usage tripled.

That history is what makes him hard to impress. Cognition has watched models ace a benchmark and then fall apart the moment its engineers tried to use them. "We've been burned like this a bunch of times," Alberti says. So the team trusts its own engineers over any score. Its highest-taste developers put each new model through a real day of work, and the bar is whether the code is something they’d actually keep.

As Alberti puts it, "we trust no eval."

## Where earlier models hit their limit

For all that progress, one ceiling remained: how long an agent could run before it lost the thread?

"Before Fable, you could delegate agents that could stay on-task for a couple of minutes, maybe an hour," Alberti says. After that, sessions drifted. Give an earlier model five ideas to weigh at once, and it would lose track and get confused. On one database migration, a prior Opus model technically finished the job but introduced a series of subtle bugs along the way.

Incident triage showed the same shape. Earlier models tended to stay at the surface of the logs instead of digging for the relevant line, and they were trained to give an answer no matter what—so they'd "confidently claim the first plausible thing they discover and then stop." Engineers learned to tune them out.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a4dd0c75a04f6ca41530255_C41-77690-D2-02-0006_VS_R1.jpeg)

Cognition evaluates frontier models against a series of benchmarks, including Frontier Code.

## Claude Fable 5 clears Cognition's own bar

Cognition grades models on Frontier Code, a benchmark it built because existing ones kept rewarding code that passed tests but wouldn't survive a real codebase. Alberti calls it an "anti-slop" standard. On its hardest subset, the prior Opus model scored around 10%. Claude Fable 5 scored about 30%.

The team's first reaction was suspicion. "Is there a bug? This can't be true." Usually a benchmark jump comes with engineers arguing for weeks over whether the model is actually better in practice. This time the dogfooding agreed with the numbers. "It was kind of a shocker, honestly," Alberti says.

"The biggest thing we noticed was the horizon, how long it can be self-sufficient," he says. "There have been tasks where I was about to go to bed and I was like, 'Okay, just please keep working on this and don't stop until I wake up.' And then I wake up, and it's been working for eight hours straight and actually making real progress. I hadn't seen that before."

The horizon held because Claude Fable 5 stayed clear-headed in messy context. It was the first model to properly use Cognition's internal debugging tools, paging through logs in the browser and drawing conclusions despite the noise. On a migration that had tripped up earlier models, it stated the invariants it would hold itself to, then executed against them. On triage, it pinned down the root cause and said what it didn't know, which Alberti says is what actually rebuilds trust.

He puts the jump in a small class of true step changes, the kind that come roughly once a year.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a4dd13a49316d41447995c4_C41-77690-D2-11-0026_VS_R1.jpeg)

Silas and his team are building Devin, powered by models like Claude, to tackle more complex, longer running workloads.

## What’s next

Cognition's founding bet was that agents should run in the cloud for hours at a time. For the company's first year, the models weren't there yet.

Alberti says Claude Fable 5 makes the full version of that bet viable, and some of it is already in the product. Devin can watch a Slack channel and jump into an issue without being tagged, or monitor production and triage a spike on its own. When it gets one of those right, he says, it feels "like a real engineer on the team."

He expects this to become the default for engineering teams. In a year or two, he says, 90% of agent sessions will be proactive ones that find a problem, scan the codebase, and message you with the fix.

"A lot of these things we've always wanted to build at the company are now possible," Alberti says.

Get started with [Claude Fable 5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5).

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d224f466b800c4a5a016_a7b8978859371a024139418f3366bb0600ee1675-1000x1000.svg)

Jul 24, 2026

### How the product designer who built Claude Design uses it to explore ideas before building them

Enterprise AI

[How the product designer who built Claude Design uses it to explore ideas before building them](#)How the product designer who built Claude Design uses it to explore ideas before building them

[How the product designer who built Claude Design uses it to explore ideas before building them](https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them)How the product designer who built Claude Design uses it to explore ideas before building them

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225e31f7aa22c1f28cb_46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

Jul 24, 2026

### Claude models explained: choosing the best model for your use case

Enterprise AI

[Claude models explained: choosing the best model for your use case](#)Claude models explained: choosing the best model for your use case

[Claude models explained: choosing the best model for your use case](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)Claude models explained: choosing the best model for your use case

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d23008bbc20c0ffaeb6f_43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)

Jun 18, 2026

### Centrally manage authorization for MCP connectors

Enterprise AI

[Centrally manage authorization for MCP connectors](#) Centrally manage authorization for MCP connectors

[Centrally manage authorization for MCP connectors](https://claude.com/blog/enterprise-managed-auth) Centrally manage authorization for MCP connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2279047e82efc257633_6c7219042e95bfef1a126ad5ee8b2c7def8b8b0a-1000x1000.svg)

May 22, 2026

### How Anthropic's finance team uses Claude to shape the narrative behind the numbers

Enterprise AI

[How Anthropic's finance team uses Claude to shape the narrative behind the numbers](#)How Anthropic's finance team uses Claude to shape the narrative behind the numbers

[How Anthropic's finance team uses Claude to shape the narrative behind the numbers](https://claude.com/blog/how-anthropics-finance-team-uses-claude-to-shape-the-narrative-behind-the-numbers)How Anthropic's finance team uses Claude to shape the narrative behind the numbers

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Coding
