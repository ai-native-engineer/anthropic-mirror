<!-- source: https://claude.com/customers/zapier-cowork-qa -->

Q&A | Claude Cowork

# How Zapier's marketing and engineering teams use Claude Cowork to delegate real work

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![Zapier logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aedd1d4ccaa7aaecee72_zapier_light.svg)![Zapier logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aed89af0a9a659d820f0_zapier_dark.svg)

Industry:

Software

Company size:

Large

Product:

Claude Cowork

Claude Enterprise

Location:

North America

~15 minutes

from homepage concept from new positioning to shareable draft in.

15 SQL queries

synthesizing live data from 6 engineering systems in one Cowork session.

Cowork

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525604b02eec936ac521_696fc8952f473c6520149cfa_4f58536f1c08deac7a94811f4be57881_og-claude-cowork.jpeg)

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

Read more

[Read more](/product/cowork)Read more

Cowork

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Cowork

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

[Prev](#)Prev

[Next](#)Next

[Zapier](https://zapier.com/) connects nearly 8,000 apps for more than 3.4 million businesses, and internally, AI adoption runs deep: 97% of employees use AI in their daily work, with thousands of AI agents deployed across the company. Zapier was also one of Anthropic's earliest MCP partners.

When Claude Cowork launched, three teams picked it up quickly and pushed it in very different directions. We spoke with Head of Product Marketing Joe Stych, AI Automation Engineer Larisa Cavallaro, and Senior Manager of Influencer Marketing Matt Brown about what those workflows actually look like. The following conversation has been edited for length and clarity.

## How has Cowork changed the type of work you take on, as well as how you approach it?

**Joe Stych, Head of Product Marketing:** I can query our product database, write messaging docs, and build landing pages in the same session. That used to mean coordinating across three different teams. I delegate first-draft homepage concepting so I can share multiple positioning directions with leadership in minutes instead of days. That used to need design handoffs before anyone could even evaluate the direction.

**Matt Brown, Senior Manager of Influencer Marketing:** I delegate inbox triage: classification, drafts, archiving. I've extended that to multi-step stuff like validating YouTube descriptions and submitting creator forms. But the real shift is bigger than that. My advice to anyone starting out: stop using it for tasks you can already do in five minutes. Start bringing it the messy, technical problems you've been putting off because they felt like they needed an engineer.

**Larisa Cavallaro, AI Automation Engineer:** People treat Claude like a chatbot when it's closer to a capable teammate. The ceiling on what one person can ship has moved dramatically.

## Larisa, you pointed Cowork at Zapier's own operations. Walk us through what happened.

**Cavallaro:** I connected Cowork to our tech stack: the employee org database, Slack channels, team documentation, and Jira. Then I asked it to identify operational bottlenecks across engineering.

Claude ran 15 SQL queries synthesizing live data from six engineering systems: GitLab, Jira, Productboard, OpsLevel, Jellyfish, and incident tracking, all centralized in a Databricks warehouse that now connects 11 source systems across Zapier's entire org. It produced an interactive dashboard with a quantified breakdown of inefficiencies: team-by-team efficiency analyses, cross-functional friction points, and hidden productivity drains we hadn't surfaced on our own.

What made it especially powerful was the underlying data was rich enough to support increasingly granular follow-ups. In most AI chat tools, you'd query Slack, then query Databricks, then manually stitch the results together. Cowork can do all of that in a single pass. That's a fundamentally different kind of capability.

## Matt, you built a full influencer marketing dashboard with Cowork. How does the pipeline actually work?

**Brown:** I used Cowork to build a live influencer marketing dashboard on GitHub Pages that visualizes our reach, views, clicks, and conversions against quarterly goals.

The data architecture centers on a Zapier Table where every influencer investment is a row. Each row gets progressively enriched by multiple automated sources: a web scraper pulls current view counts, the Bitly API captures click-through data, and our Databricks warehouse supplies downstream conversion and product-upgrade metrics. A Zap transforms that table into a JSON feed consumed by the dashboard's front end.

Claude handled the end-to-end development: chart design, JavaScript and HTML code generation, layout decisions, and debugging. We worked inside a tight Cowork loop where I'd review outputs, request changes, and confirm each iteration before deployment. The result is a daily-updated, real-time visualization mapped against quarterly targets.

What started as a reporting gap is now the system guiding our investment decisions across the entire influencer program. This moves the team from retrospective reporting to forward-looking guidance, informing which channels to double down on, which content performs best, and where to reallocate budget.

## Joe, your workflow is less about building something from scratch and more about making a process repeatable. Walk us through how homepage concepting works in Cowork.

**Stych:** I connected Cowork to our homepage, a custom skill I built with our PMM guidelines, and our internal tools through Zapier MCP, so it could pull from Slack threads, Glean searches, whatever context it needed.

The workflow starts by giving Cowork two key inputs: the existing homepage as the baseline, and project-specific product marketing guidance that covers voice, positioning intent, and operating context. Those are loaded through custom skills: reusable instructions that encode how our team writes and thinks about positioning.

From there, Claude navigates to the live page in Chrome, identifies core page modules, and generates a revised homepage aligned to the new positioning. Instead of requiring a manual rewrite plus a handoff across tools, it produces an HTML mockup directly.

I can keep doing other things while it runs. In this case, the result was a shareable draft in about 15 minutes that I shared with our CMO and CEO for iteration, with enough fidelity to evaluate copy direction and page structure before deeper production work.

The skills layer is what makes this repeatable. Rather than re-prompting from scratch each time, the PMM context travels with the tool. The biggest mistake people make is treating Cowork as a conversation that ends. At the end of every working session, I ask: what should we remember from this? Claude captures it so everything compounds. Each session makes the next one smarter.

“The barrier between ‘having an idea’ and ‘shipping something’ has collapsed. I genuinely cannot remember doing my job without it.”

Larisa Cavallaro

AI Automation Engineer, Zapier

## How do you think about trusting Cowork's output? Is there a review loop, and has it changed over time?

**Cavallaro:** Trust is task-dependent. People relax the loop for familiar work but keep review for novel or high-stakes stuff. The second mistake people make, after underestimating scope, is being vague about the output. When you tell it exactly what you need to *do* with the result, not just what to produce, it will return something far more useful than you expected.

**Stych:** For homepage concepting, I'm looking at the output and giving directional edits, then letting Cowork regenerate. It's lightweight but deliberate. What's hard now is judgment: knowing when a line sounds wrong, catching a bad metric before it ships, noticing when messaging drifts from what the product actually does.

## Zapier's whole business is building integrations. How are you thinking about the Cowork plugin and skills architecture?

**Stych:** We're prioritizing interoperability. We use several AI platforms internally, so we've organized around Skills and MCP Tools as the core units. We store Skills in local files instead of on Cowork specifically, which allows for easy retrieval, modification, and headless use across the organization and across platforms. We also use Zapier MCP servers, which are client-agnostic and define custom tools we use often.

Examples of the skills we're building include a PMM homepage concepting skill covering voice, positioning, and page structure, daily Slack summary workflows, and Jira triage skills. We primarily use the Zapier MCP server. Zapier can connect to services like Slack, Glean, Drive, and Jira, among the thousands of other tools integrated into Zapier, so the Zapier MCP gives us one tool that lets us pass through to other services.

From our perspective, the architecture is maturing from "connect one app" to "install a workflow," bundling config, skills, and actions. That aligns well with how we think about integrations.

## Does Cowork change what it means to be good at your job?

**Brown:** The marketers who win will be the ones who know what to point the tools at, not the ones waiting for an engineer to build it for them.

**Stych:** Being good at the job looks different now. It's less about doing the reps and more about knowing which reps to do.

**Cavallaro:** The most obvious shift is speed and scale. But the deeper change is access. I can now interact with layered data in ways I couldn't before, build clear visual reports in minutes instead of waiting on someone else, and actually make the case for something with evidence.

Beyond analysis, it's opened doors I didn't expect. I've learned how to work with new file types, push code to GitLab, host projects on Vercel, and understand security standards at a level I didn't have after four years working in security.

The barrier between "having an idea" and "shipping something" has collapsed. The skill that matters now isn't knowing how to do every step. It's knowing clearly what you're trying to accomplish and being able to direct toward that outcome. Execution is still real work, but the ceiling on what one person can ship has moved dramatically. I genuinely cannot remember doing my job without it.

Claude Enterprise, now available self-serve

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690515bc9c9d273cbf764a30_og_amazon-bedrock-general-availability.jpg)

Any organization can now purchase Claude Enterprise directly—no sales conversation required. Set up SSO, invite team members, and start working in minutes.

Read more

[Read more](https://claude.com/blog/self-serve-enterprise)Read more

Claude Enterprise, now available self-serve

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Any organization can now purchase Claude Enterprise directly—no sales conversation required. Set up SSO, invite team members, and start working in minutes.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Enterprise, now available self-serve

Any organization can now purchase Claude Enterprise directly—no sales conversation required. Set up SSO, invite team members, and start working in minutes.

“The biggest mistake people make is treating Cowork as a conversation that ends. Claude captures it so everything compounds. Each session makes the next one smarter.”

Joe Stych

Head of Product Marketing, Zapier

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
