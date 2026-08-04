<!-- source: https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

# Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work

*Yoav Orlev, Head of Product at Base44, joined the vibe coding platform as its first employee and has seen his team build on every Claude model since Sonnet 4. Here's why he thinks Claude Fable 5 is the first model that reasons about software the way a senior engineer would, and what that frees the rest of his team to build.*

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)
* Product

  Claude Platform
* Date

  July 15, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work

Base44 is a vibe-coding platform that allows anyone, regardless of technical ability, to build full stack applications and websites. Its customers range from small businesses with no developers to companies using it to build full SaaS products.

Yoav Orlev, who joined Base44 as its first employee and now runs product, says one of the most satisfying parts of his work is seeing what small businesses can do with the platform for which they otherwise lacked the time, budget, or knowhow, whether that’s building a digital storefront or a shift-management application for restaurant staff. His team’s mission is to keep widening their product’s capabilities while keeping it usable for everyone.

The Base44 product and engineering teams have always moved quickly, especially when shipping small or medium-scope features. But any changes to the platform’s core that touch multiple interdependent parts could only be entrusted to the most senior engineers.

One such bottleneck was Base44's system prompt and its hundreds of permutations, which vary by whether someone is on their first app or their fifth, a free user or a subscriber, and by the category and features of the app being built. Another was changing the native mobile infrastructure, which only engineers with mobile expertise could do.

Earlier Claude models, which have powered Base44’s app generation engine since it launched in early 2025, couldn't be trusted with that work, Orlev suggests. When a model got stuck on an error, for example, it would keep working the spot in front of it instead of recognizing the fix probably already existed elsewhere in the code and searching for it.

“The decision on what to do next is a crucial one and most of the time [earlier] models would take, I would say, a naive approach,” he says.

Claude Fable 5 was the first model the team tested that could reason as if it had an understanding of how software is built, Orlev says.

## Trusting Fable 5 with the most complex product and engineering jobs

Base44 runs each new Claude model through evals across different app types, measuring latency, cost, and build errors. The team also runs tests like building a Minecraft clone to see how a model handles game physics and mechanics.

With Claude Fable 5, two things stood out: it finished tasks in far fewer turns, and it built more complete apps from the first prompt, including the edge cases that earlier models skipped.

So the team pointed it at a task they had previously reserved only for the most senior engineers: rebuilding the Base44 system prompt. After about an hour of back-and-forth questions, Claude Fable 5 ran on its own for four hours and returned 90% to 95% of what they needed. Using its A/B testing infrastructure, the team was then able to measure and ship these changes that afternoon. And while Claude Fable 5 worked, it even flagged a gap in Base44's own evals: the team wasn't testing for cache hits, even though a prompt change can break the cache, and at the scale of millions of users that drives up cost. The model raised a blind spot and corrected it.

When Claude Fable 5 got stuck on a change to the harness behind Base44's in-app agent, it reasoned that the same problem had probably been solved elsewhere in the codebase, went to investigate that part, and came back with the fix. "This reasoning of 'this probably has been solved somewhere else, so I should go there to investigate' is something we haven't seen so often in other models," Orlev says.

Orlev compares working with Claude Fable 5 to working with a senior engineer. While a junior engineer needs every step specified and constant checking, you only need to brief a senior one on the goal and the why.

This type of work extends beyond the engineering team, too. When a product manager wanted to bring native mobile app building inside Base44, he pointed Claude Fable 5 at the job and after roughly two and a half hours had a working environment that was about 90% of what the team needed to move to production.

Before Claude Fable 5, this type of work had to wait for Base44's top three engineers or a specialist to free up. Now, the model executes tasks while Orlev's team reviews, tests, and approves the code before shipping it.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a57c73e324085779c230b3d_000262380003_VS_R1.jpeg)

Claude Fable 5 gives Base44's product, engineering, and design teams confidence to build more ambitious parts of their Sugeragents platform.

## What’s next

As Claude model capabilities advance, so do the Base44 team’s goals for the platform. The team aims to turn Base44 from a tool that builds apps into one that also helps people manage and grow what they've built. Base44 Superagents, now public, run workflows around those apps.

Knowing that they can trust Fable 5 with complex tasks, Orlev now encourages product managers and designers to build in parts of the platform they were previously not willing to touch for fear of breaking anything.

“Fable has given us the confidence to make bolder moves with the business,” Orlev says. “It’s bringing the product to a whole new area and possibilities that before that we were, I would say, scared to do.”

***Get started with*** [***Claude Fable 5***](https://www.anthropic.com/claude/fable)***.***

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

Claude Platform
