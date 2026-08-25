<!-- source: https://claude.com/blog/behind-model-launch-what-customers-discovered-testing-claude-opus-4-6-early -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22727482c9ba6a02e71_1576ae23eaf481f33bd36ab468171cc69d12361a-1000x1000.svg)

# Behind the model launch: What customers discovered testing Claude Opus 4.6 early

Inside the tight window between pre-production access and public launch, when customers race to test what a new Claude model can really do.

* Category

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)
* Product

  No items found.
* Date

  February 9, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/behind-model-launch-what-customers-discovered-testing-claude-opus-4-6-early

Before a [new Claude model goes live](https://www.anthropic.com/news/claude-opus-4-6), a small group of customers gets access days before the rest of the world. They work with pre-production research models, test them against real workloads to figure out what the model is great at, where it breaks, and whether it's ready to ship to their own users the moment  Anthropic launches it publicly. Their honest assessments — what works *and* what doesn't — directly shape the version of the model Anthropic ultimately ships.

The review window is tight. Teams clear their calendars, spin up war rooms, and start throwing their hardest problems at the model. Behind the scenes, it's late nights, many cups of coffee, and Slack channels lighting up at odd hours. What their customers eventually see is polished—but the process of getting there is a lot messier and a lot more fun.

For this piece, we wanted to pull the curtain on what this looks like. [Harvey](https://www.harvey.ai/), [bolt.new](https://bolt.new/), [Shopify](https://www.shopify.com/), and [Lovable](https://lovable.dev/) all gave us a look inside at their early access period with Claude Opus 4.6: the approaches they took, the breakthroughs they found, and what they learned before anyone else.

## **Getting ready for model testing**

How teams kick things off depends a lot on what they're building.

[bolt.new](https://claude.com/customers/stackblitz) spun up a dedicated Slack channel and deliberately avoided sharing impressions early so they wouldn't bias each other.

[Harvey](https://claude.com/customers/harvey)'s research team brought in experienced lawyers to test the model on legal tasks while running it through BigLaw Bench, their benchmark for real-world legal work.

[Shopify](https://claude.com/customers/shopify)'s engineers started feeding the model into iterative planning loops they'd already built around Claude.

At [Lovable](https://claude.com/customers/lovable), the team that manages models and evals kicked into gear immediately—running benchmarks while engineers booked time to do what they call "vibe checks," building apps with the new model to feel out where it's stronger. Alexandre Pesant, engineering lead at Lovable, said, "It's a bit like Christmas."

The approaches were different, but the instinct was the same: throw your hardest problems at the model first.

## **When the results start coming in**

Once testing is underway, teams are watching for two things: how the model scores on their benchmarks, and how it *feels* in practice. Both matter, and they don't always tell you the same thing.

Harvey's BigLaw Bench results came back at 90.2%—the first Anthropic model to break 90% on that benchmark, with 40% of tasks receiving perfect scores. But it was the qualitative reaction that stuck.

One of their internal lawyers ran a single query and came back saying the output felt "smart and analytical, like it's actually thinking." When your structured evals and your subject matter experts are both saying the same thing, that's a strong signal.

bolt.new.new combined their automated eval platform—which tests build quality, bug fixing, codebase understanding, and design aesthetics—with hands-on stress testing. By the end of the first day, they had a shared doc full of deployed test apps and specific observations.

One developer had a waterfall graph bug that had failed five-plus attempts with the previous model. Opus 4.6 diagnosed it on the first try, finding eight parallel HubSpot API searches firing simultaneously and additional queries bypassing rate-limit protection by using raw fetch instead of the project's rate-limited wrapper.

At Shopify, Paulo Arruda, a Staff Engineer, described a moment that flipped the usual dynamic: "I asked Opus 4.6 to move something from one page into another menu item — that's all I said. I didn't specify any details. It not only moved it but went above and beyond, creating a lot of details I didn't even know I wanted until I saw them. It anticipated my next ask and just did it. I found myself saying 'You're absolutely right' to the AI instead of the other way around, which had been the pattern before."

Ben Lafferty, a Staff Engineer on Shopify's Assistants team, pushed in a different direction. He had Opus 4.6 port a large library from TypeScript to Ruby for an internal prototype. "It created a shim to run against the existing test cases in the repo, then ported over almost the entire spec in one shot while validating against the original test set," he said. "Instruction following is significantly improved. This was one of the first early access periods where I haven't had substantial feedback to give."

At Lovable, the testing ran on two tracks.

The team ran design benchmarks and complex task evals to get the structured picture, but they also performed what they call "vibe checks"—engineers building apps with the new model to feel where it's stronger and where it breaks.

"It's always a bit of a race to discover the new rough edges," said Alexandre Pesant.

His own stress test was a side project involving complicated subway mapping and itinerary logic, something he'd tried with previous models and hit a wall on. With Opus 4.6 and max effort turned up, the model pushed past the point where he expected it to stall.

"I kind of know when things are not going to work or if we're hitting the limits," he said. "It went further than others." He also noticed a broader shift: with the model's ability to use the browser and test on its own inside Lovable, "you can feel a difference in autonomy."

## **What it's like on the other side**

By the time early access wraps up, teams have a clear picture of what they're working with. Every team we talked to kept coming back to the same point: the relationship with the model is changing.

“Opus 4.6 diagnosed bugs on the first try that we'd failed to fix across five-plus attempts with previous models. The jump in reasoning depth is real," said Garrett Serviss, VP of Marketing at bolt.new.

"For me, Opus 4.6 is the first model from Anthropic that feels like a true collaborator in my day-to-day work," said Ben Lafferty at Shopify. "The time horizon of tasks that I can hand off to the model continues to grow."

"Claude Opus 4.6 is an uplift in design quality," said Fabian Hedin, co-founder of Lovable. "It's more autonomous, which is core to Lovable's values. People should be creating things that matter, not micromanaging AI."

Of course not all of the feedback was glowing, and that's the point. Early testers directly inform what version of the model Anthropic ultimately ships. The whole process only works because teams are as candid about what's not working as they are about what is, and they know that candor actually goes somewhere.

"We get to shape the future of tools our engineering organization will use," said Paulo Arruda at Shopify. "We're not just passive testers — we're partners in development. When we identify issues or patterns, Anthropic listens and iterates."

‍

‍

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d23008bbc20c0ffaeb6f_43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)

Jun 18, 2026

### Centrally manage authorization for MCP connectors

Enterprise AI

[Centrally manage authorization for MCP connectors](#) Centrally manage authorization for MCP connectors

[Centrally manage authorization for MCP connectors](https://claude.com/blog/enterprise-managed-auth) Centrally manage authorization for MCP connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d222061abf091318fb82_423062049d4676b41d52b16068cbb5e21603190e-1000x1000.svg)

Aug 21, 2026

### The AI-Native SDLC playbook

Enterprise AI

[The AI-Native SDLC playbook](#)The AI-Native SDLC playbook

[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)The AI-Native SDLC playbook

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

Aug 13, 2026

### Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

Agents

[Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions](#)Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

[Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions](https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions)Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

Aug 20, 2026

### Build production agents with computer use, the Skills API, and the Files API

Product announcements

[Build production agents with computer use, the Skills API, and the Files API](#)Build production agents with computer use, the Skills API, and the Files API

[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api)Build production agents with computer use, the Skills API, and the Files API

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.
