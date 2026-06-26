<!-- source: https://claude.com/customers/box -->

Case study | Claude Platform

# Box builds document creation into its AI agent with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![Box logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8c287936531790c85c4_box_light.svg)![Box logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8bdc1ea299a1a768655_box_dark.svg)

Industry:

Software

Company size:

Large

Product:

Location:

North America

Concept to customer-facing capability in weeks using the Claude Skills API

instead of building document generation in-house

2-minute contract redline

when Box's team tested jurisdiction changes on a contract

[Box](https://www.box.com/) securely connects enterprise content to AI, enabling organizations to manage files and automate business processes. Its agent, the Box Agent, recently gained the ability to support document creation through Anthropic's Skills API.

## With Claude, Box:

* Saved months of development time by using the Skills API instead of building document generation in-house
* Went from concept to customer-facing document creation in weeks by using the Skills API instead of building in-house
* Redlined a contract in 2 minutes instead of an afternoon of manual review
* Generates multiple document formats from a single conversation: the same source material returned as a slide, a spreadsheet, or a written brief
* Creates PowerPoint, Excel, Word, and PDF files inside the Box agent without a separate code-execution environment
* Analyzes spreadsheets using their full structure rather than extracted text
* Maintains enterprise security through Box's existing LLM gateway, with only 2 new data paths added

## The challenge

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Redlined a contract vs. an afternoon of manual review

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Redlined a contract vs. an afternoon of manual review

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

2 minutes

Redlined a contract vs. an afternoon of manual review

## Bringing document creation inside Box

Box customers could already create, collaborate on, and sign documents inside the platform. Early customers of the new Box Agent consistently requested the ability to generate presentations, documents, and other file formats. Building that capability in-house didn’t make sense from a timing, effort, or focus standpoint. It would have meant standing up a distributed code-execution environment across Box's data centers and meeting the 5-nines reliability bar Box's customers expect. Box's team estimated the work for the in-house path would take months of engineering time.

“Box's strength is in how enterprise content is managed, governed, and put to work,” said Darryl Sladden, Staff Product Manager for AI at Box. “The intelligence to make a good slide is a different problem, and it's one Anthropic has already solved.”

## The solution

Choosing the right Claude model

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c2dd485d80024bc14f48c6_choosing%20model.jpeg)

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Choosing the right Claude model

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## Pre-built skills connected to the path Box already trusted

Box turned to Anthropic's Skills API for the generation itself. Anthropic's pre-built skills for PowerPoint, Excel, Word, and PDF deliver packaged expertise: they encode what makes a slide visually appealing, how to structure analytical spreadsheets, and how to handle complex Word edits cleanly.

“Using the API, we’re able to show the customers very early how they can save work and time, and start to change their processes very quickly,” Darryl says.

The integration principle was to change as little as possible. Box already routes all LLM requests through a production gateway that handles logging, request counting, and access control. Rather than create a separate path for document generation, the team added exactly two things: file upload on the way in, file download on the way out.

“We ran this through our main production path and added the file upload, file download capabilities,” Darryl says. “Everything else: the same file versioning, the same ownership. The only difference we have to talk about is those two paths.”

Inside the agent, Box routes work across Claude models by difficulty. Sonnet typically interprets the user's request, searches Box for relevant source files, and assembles context, while file generation often goes to the more capable Opus model. That flips the common pattern of using the larger model as planner and a smaller one as executor, but it matches where the difficulty sits: orchestrating over Box content is well-bounded, while producing a document that looks right demands more from the model.

The pre-built skills are also what made the speed possible. Spreadsheet analysis benefits from the full structure of a spreadsheet rather than just text extracted by RAG, and PowerPoint generation depends on judgment that's hard to specify, let alone replicate. “PowerPoint files have a lot of taste,” Darryl said. “It's really the designer's mind that I always find is most valuable, that it's actually been trained in.”

The capability runs under Box's existing Anthropic agreement, which contractually ensures customer data isn't used for training. Containers that execute skill code are short-lived, lasting only minutes. For Box's security team, the review was about two new data paths, not a new trust boundary.

How enterprises are building AI agents in 2026

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6938f1ba14ef8dffb304fae8_2026%20State%20of%20AI%20Agents%20Report%20-%20Blog%20-%201200%20x%20630%20E.png)

New research from 500+ technical leaders reveals how enterprises are deploying AI agents—and why 80% already report measurable ROI.

How enterprises are building AI agents in 2026

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

New research from 500+ technical leaders reveals how enterprises are deploying AI agents—and why 80% already report measurable ROI.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

How enterprises are building AI agents in 2026

New research from 500+ technical leaders reveals how enterprises are deploying AI agents—and why 80% already report measurable ROI.

## The outcome

## Redlining a contract in 2 minutes

Using the Skills API, Box went from concept to customer-facing capability in weeks. A member of Box's internal team tested the agent on a real contract, asking it to show redlines for changing the governing jurisdiction from New York to California. “We just waited two minutes, and it output the entire document,” Darryl said. “It was smart enough to change not only the state, but the city and all the additional clauses that talked about court.”

The financial summary flow works the same way: a user asks for a slide summarizing a company's financial position; the agent searches their Box folders, finds the previous quarterly report and recent monthly updates, pulls the relevant figures, and returns a formatted draft slide with the initial work done, ready for the team to add insights. A follow-up request for the same output as a spreadsheet reuses what the agent already found.

Box went from concept to customer-facing document creation capability in about a month, a timeline that wouldn't have been possible building from scratch. The time that didn't go into infrastructure went into making the agent actively useful inside the enterprise.

The principle that emerged: use pre-built skills where the expertise is general and already trained in; build your own where the knowledge is yours. “The trajectory of AI is really what we're betting on for this,” Darryl said. “Our advice is to look at each capability not only how it is now, but how it will be in six months.”

“Using the API, we’re able to show the customers very early how they can save work and time, and start to change their processes very quickly."

Darryl Sladden

Staff Product Manager for AI, Box

## Related stories

[How Vercel built an ecosystem on the open skills standard](/customers/vercel-qa)How Vercel built an ecosystem on the open skills standard

How Vercel built an ecosystem on the open skills standard

Customer story

[Customer story](/customers/vercel-qa)Customer story

[Juno helps people with chronic illness find patterns in their symptoms with Claude](/customers/juno)Juno helps people with chronic illness find patterns in their symptoms with Claude

Juno helps people with chronic illness find patterns in their symptoms with Claude

Customer story

[Customer story](/customers/juno)Customer story

[A conversation with Cursor on building coding agents for professional developers](/customers/cursor-qa)A conversation with Cursor on building coding agents for professional developers

A conversation with Cursor on building coding agents for professional developers

Customer story

[Customer story](/customers/cursor-qa)Customer story

[Inside Delight.ai’s AI/ML team: Building internal tools with Claude Code](/customers/delightai-qa)Inside Delight.ai’s AI/ML team: Building internal tools with Claude Code

Inside Delight.ai’s AI/ML team: Building internal tools with Claude Code

Customer story

[Customer story](/customers/delightai-qa)Customer story
