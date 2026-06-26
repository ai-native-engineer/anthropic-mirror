<!-- source: https://claude.com/customers/jamf-qa -->

Q&A | Claude Cowork

# How Jamf's engineering team turns structured workflows into interactive tools with Cowork

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![Jamf logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b45499ebd143bd2c52765a_logo_jamf-light.svg)![Jamf logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b454a6ceaa3ebddb228495_logo_jamf-dark.svg)

Industry:

Software

Company size:

Large

Product:

Claude Cowork

Location:

North America

45 minutes

to build a conversational UI in Cowork with branching logic, role-based filtering, Jira integration, progress tracking, and structured file export

16 departments

using Claude Enterprise

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

[Jamf](https://www.jamf.com/) manages and secures Apple devices for more than 70,000 customers worldwide. The company recently rolled out Claude Enterprise across all 16 departments. Then the engineering team found Cowork and started replacing spreadsheets and checklists with guided, reusable workflows. Nick Benyo, Software Engineer on Jamf's Enterprise AI and Automation team, sat down with Anthropic to discuss how the team is using Cowork, what surprised them about adoption, and where they see the most untapped potential. The following conversation has been edited for length and clarity.

## What made Cowork click for your team?

**Nick Benyo:** It stopped feeling like a chatbot and started feeling like a lightweight app framework. It changed how we thought about what we could build. We saw that a Claude skill could show a visible checklist tracking progress through a multi-step process, then use the ask-question feature to pause and wait for real input. And MCP integrations show up almost like a heads-up display. Each of those pieces on its own is useful, but together they give you structure, interactivity, and live context in one place. And anything you build is reusable by default. You're not writing a one-off script, you're building a tool anyone on the team can pick up and run.

## Has adoption spread beyond engineering?

**Nick Benyo:** The biggest surprise is that it's not engineers driving the broadest adoption. People across the org are using Cowork for data blending, analysis, and dashboard building. Bespoke dashboarding has been huge. Tasks that previously required a BI tool or an engineer's help, people are now doing themselves in minutes. Nobody had to teach them how to write a skill or explain what an MCP server is. The barrier to building isn't technical skill, it's just knowing what you want and making sense of what you're getting back. Once people realized that, adoption took care of itself.

## Walk us through a specific skill you've built.

**Nick Benyo:** Our engineering team has a performance review spreadsheet that covers seven areas across levels from Associate to Principal. Depending on your role, some competencies don't apply. Engineers doing self-evaluations had to navigate all of that on their own with limited guidance on what a good answer looks like. Many people found it intimidating.

We built a skill that turns that spreadsheet into a guided conversation. It asks your name, level, and role type, then builds a personalized checklist of competencies to cover. From there it works through each one: asks about a specific behavior, listens to your answer, then pushes for a concrete example. In the old process, someone might write "I do thorough code reviews" and call it done. The skill won't let you off the hook: what review, what feedback did you give, what changed because of it? If you get stuck, it can pull up your recently closed Jira tickets to jog your memory.

A typical session runs 60 to 90 minutes with a visible checklist tracking progress. At the end it generates a file you can review and paste back into the original spreadsheet and a summary report with a level assessment and development plan.

## How long did that take to build?

**Nick Benyo:** Under 45 minutes. At a previous employer, something comparable was a full team and three months of build time. You're talking about a conversational UI with branching logic, role-based filtering, Jira integration, progress tracking, and structured file export. Testing was just as fast. I told the skill to sample a few questions from each competency instead of running the full set and it adjusted on the fly. No code change, no redeployment. The test framework was up and running in a single prompt.

“The biggest surprise is that it's not engineers driving the broadest adoption. People across the org are using Cowork.”

Nick Benyo

Software Engineer, Jamf

## How does the quality compare to the old process?

**Nick Benyo:** Before this, engineers either rushed through it or were overwhelmed and avoided filling it out entirely. The results were inconsistent and managers had to work with whatever they got. When I went through the evaluation myself, the skill reframed something I said about my own work and I almost typed back "I feel so seen right now." The engineer walks away feeling like they had a real conversation instead of the painfully awkward self-promotion vibe of a self-evaluation.

## Are there other workflows you've brought into Cowork?

**Nick Benyo:** The software vendor review skill is another good example. It's a structured 12-question review with clear steps, but the startup cost of manually researching a vendor's capabilities meant reviews were often late. The skill researches the vendor, drafts answers, and walks the reviewer through each one for approval.

We're also looking at plugins as a way to put guardrails around how data gets queried. A plugin is a bundle of related skills and configurations that ships as a unit. When a skill needs data, it shouldn't have to know whether to hit a live API or a warehouse. Plugins can set those rules through the MCPs they include and the logic in their skills. A plugin might route to the data warehouse first for anything historical or aggregated, and only reach out to live sources when the request needs real-time data. That keeps API load down, keeps responses fast, and means the person using the skill never has to think about where the data came from.

The human is still making the decisions. Cowork just makes sure the process doesn't stall or come back with the wrong data.

## Where do you see the most untapped potential?

**Nick Benyo:** Structured workflows are the big opportunity. I've worked with teams that have full React webapps dedicated to provisioning resources and spinning up pipelines. There's usually an entire team building and maintaining those. That's a natural fit for Cowork, and a stronger case than the evaluation skill, because those React workflows are rigid. When something goes wrong or a step doesn't apply, they break. Cowork is adaptive by default.

The most exciting piece is shared read/write between users. So far, most of what we've done is read-heavy. But we're exploring a skill that gives engineers a guided template to workshop ideas, walk through feasibility, then write the output to a persistence layer and use similarity search to connect them with others working on something related. Right now, those connections happen by accident. Building discovery into the workflow itself is where we think the real leverage is.

## What advice would you give another team getting started with Cowork?

**Nick Benyo:** Lean into the interactive elements. The task list, the ask-question feature, the MCP calls visible on the side. Once you start thinking of Cowork as a canvas with interactive elements you can fill, the use cases become obvious. Look for high-value knowledge work that has structure: a checklist to get through, inputs to collect, data to pull in, outputs to produce.

Don't overthink the first skill. Pick a workflow that's annoying, structured, and repeatable, and build it. The engineering evaluation took 45 minutes. Once people saw what came out of that, they started finding their own use cases without being asked.

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

“The human is still making the decisions. Cowork just makes sure the process doesn't stall or come back with the wrong data.”

Nick Benyo

Software Engineer, Jamf

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
