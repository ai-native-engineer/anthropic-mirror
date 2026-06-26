<!-- source: https://claude.com/customers/asana-qa -->

Q&A | Claude Managed Agents

# How Asana built AI Teammates on Claude Opus 4.6

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3414e70a75001b66e8d27f_asana-black.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3414e7f48cd2308583c215_asana-light.svg)

Case Study: Asana

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c16e5688acc2af1a8c146c_og_case-study-asana%20(1).jpg)

Read more about how Asana supercharges work management with Claude.

Read more

[Read more](https://claude.com/customers/asana)Read more

Case Study: Asana

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Read more about how Asana supercharges work management with Claude.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Case Study: Asana

Read more about how Asana supercharges work management with Claude.

[Prev](#)Prev

[Next](#)Next

Asana recently launched [Asana AI Teammates](https://asana.com/product/ai/ai-teammates), powered by Claude Opus 4.6 **a**nd [Claude Managed Agents](https://claude.com/blog/claude-managed-agents). We sat down with Arnab Bose, Chief Product Officer at Asana, to discuss his thoughts on collaborative agents and why Asana chose Claude as their model layer.

## How does Asana think about the role of collaboration in AI agents?

**Bose:** The assumption in the market is that collaboration is a constraint on autonomy. We think that's backwards. We’ve seen autonomous agents struggle with work-related tasks they're given, not because the models aren't smart enough, but because the agents lack the context to execute well.

The industry defaulted to individual-first because it's the easiest problem to solve technically. What breaks at enterprise scale is coordination. AI actually increases the coordination tax. With an AI agent, a marketing manager can draft a brief in five minutes, but they still run into bottlenecks with rounds of reviews and syncing with a launch timeline that multiple teams depend on. When every person has their own AI assistant working independently, you create more fragmentation, not less. Collaboration is what makes real autonomy possible.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c1b3256b82290a188756af_Asana_QA_Image1small.png)

"We've been especially impressed by Claude's ability to handle multi-step workflows," said Arnab Bose, Chief Product Officer at Asana. "That level of synthesis and judgment is what sets Claude apart."

## How do AI Teammates actually work within Asana? Walk us through the experience.

**Bose:** It's designed to feel like adding a new team member, but one that's fully onboarded on Day 1. An AI Teammate has its own Asana account, just like any other colleague. You assign it a task, @mention it in a comment, or trigger it through a workflow rule, and it goes to work.

Take our Campaign Brief Writer. A marketer creates a request with the objective and target audience. The AI Teammate picks it up, pulls relevant context and drafts a structured brief the team can review. What used to take days of back-and-forth becomes a fifteen-minute review cycle. The key difference is that AI Teammates don't generate and disappear. They operate within the same project structure, permissions, and workflows your team already uses.

Building a custom AI Teammate doesn't require engineering resources or technical expertise. You describe the role, give it instructions, and point it at the right projects. A compliance team can stand one up to review submissions against regulatory checklists. An HR team can build one to triage employee requests.

## Why did Asana choose to build AI Teammates on Claude?

**Bose:** We evaluated available models carefully—AI Teammates uses a multi-agent architecture, and we use different models to accomplish different takes. The most important is the top-level agent responsible for coordinating a Teammate's efforts, and here Claude stood out for the quality of its reasoning, particularly when it comes to understanding nuanced, context-rich work scenarios. Work management isn't just about processing text. It requires interpreting goals, understanding dependencies between tasks, recognizing what's blocking progress, and communicating clearly with the humans in the loop. By using different Claude models in the various subagents, we're able to optimize for speed, reasoning power, or balance between the two—whatever it takes to move work forward.

We've been especially impressed by its ability to handle multi-step workflows, for instance, an AI Teammate that reviews an entire project's task history, identifies patterns in what's falling behind, and drafts a targeted status update with recommended next steps. That level of synthesis and judgment is what sets Claude apart. Claude Managed Agents removed a lot of the undifferentiated heavy lifting for AI Teammates. That let our product team stay focused on the things only we can build—enterprise-grade integration with how teams actually work in Asana.

## Your team has been building on Claude for a while now. Were there capabilities in Claude that changed something you couldn't have built a year ago?

**Bose:** We were early Claude adopters. In our experience, advancements in more recent models show that Claude excels at instruction following, with careful attention to detail that ensures our customer requests are followed to the letter and no further. This means that you can trust your AI Teammates won't surprise you by going beyond what you ask. Claude is also the best trained model at using Agent Skills, and we’ve used Skills to dramatically cut development time for core features like document editing in Microsoft Sharepoint & OneDrive. By combining Claude with the data in Asana Work Graph, AI Teammates are able to go from very basic customer requests to surprisingly complete pieces of work.

‍

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c1b120eb115620f2c01a08_Asana_QA_Image.png)

"Our principle is that AI Teammates should be autonomous on execution, but humans own the decisions." —Arnab Bose, Chief Product Officer at Asana

## Can you share a specific example of how an AI Teammate fits into a team's regular workflow?

**Bose:** Cross-functional launches are inherently complex. Marketing, product, engineering, and enablement are all working toward the same date. The coordination overhead is massive.

The Launch Planner AI Teammate takes on that coordination layer by living inside the workflow. It monitors progress across workstreams, flags dependencies, reports on status, and proactively surfaces what needs attention. Now the human program manager goes from spending hours stitching together spreadsheets to reviewing a structured summary and making decisions.

"By using different Claude models, we're able to optimize for speed, reasoning power, or balance between the two—whatever it takes to move work forward."

Arnab Bose

Chief Product Officer, Asana

**Anthropic: CIOs are worried about agent sprawl: too many bots, no visibility, unpredictable costs. How should enterprises be thinking about governance?**

**Bose:** That concern came up in nearly every early enterprise conversation. CIOs told us they had dozens of point-solution bots scattered across departments. There’s no single view of what the AI was doing, and nobody could answer "what happens if something goes wrong?"

Three principles shaped our approach. First, admins control whether users can access AI Teammates, and users control which ones are active, what they access, and what actions they take. Second, every action is recorded in task history, so it's visible and auditable. And finally, customer data is never used to train models, so you don't need new governance policies to use AI Teammates.

**Anthropic: Where should an agent act on its own, and where should it always come back to a human?**

**Bose:** Our principle is that AI Teammates should be autonomous on execution, but humans own the decisions. Drafting a brief, triaging requests, flagging compliance gaps — that's execution work the AI Teammate handles on its own. When there's a judgment call, it surfaces the decision to a human with the context they need. Teams can adjust how much autonomy an AI Teammate has based on the stakes involved.

**Anthropic: What's the vision for where AI Teammates go from here?**

**Bose:** Over time, we see AI Teammates becoming more capable across complex multi-step and multi-app workflows, learning from team patterns, and proactively identifying opportunities to move work forward by integrating with additional applications that Enterprises use. And we’re going to make them even smarter by using Agent Skills to extend and systematize the work that Teammates are able to do. The vision is that people spend their time on the creative, strategic, high-judgment work that drives the business. Not AI that replaces people, but AI that works alongside them as a true teammate.

Introducing Claude Opus 4.6

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698529955ffaa6de831ec14e_opus%201%20(4).jpg)

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Read more

[Read more](#)Read more

Introducing Claude Opus 4.6

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

"The vision is that people spend their time on the creative, strategic, high-judgment work that drives the business. Not AI that replaces people, but AI that works alongside them as a true teammate."

Arnab Bose

Chief Product Officer, Asana

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

## Related stories

[How Vercel built an ecosystem on the open skills standard](/customers/vercel-qa)How Vercel built an ecosystem on the open skills standard

How Vercel built an ecosystem on the open skills standard

Customer story

[Customer story](/customers/vercel-qa)Customer story

[Box builds document creation into its AI agent with Claude](/customers/box)Box builds document creation into its AI agent with Claude

Box builds document creation into its AI agent with Claude

Customer story

[Customer story](/customers/box)Customer story

[Juno helps people with chronic illness find patterns in their symptoms with Claude](/customers/juno)Juno helps people with chronic illness find patterns in their symptoms with Claude

Juno helps people with chronic illness find patterns in their symptoms with Claude

Customer story

[Customer story](/customers/juno)Customer story

[A conversation with Cursor on building coding agents for professional developers](/customers/cursor-qa)A conversation with Cursor on building coding agents for professional developers

A conversation with Cursor on building coding agents for professional developers

Customer story

[Customer story](/customers/cursor-qa)Customer story
