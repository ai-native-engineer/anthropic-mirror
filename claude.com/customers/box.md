<!-- source: https://claude.com/customers/box -->

Case study | Claude Platform

# Box builds document creation into its AI agent with Claude

[Try Claude](https://claude.ai)

![Box logo](https://assets.claude.com/f7051ef3388f6fcd83051cffcba21499a021e446.svg)

Industry:
:   Software

Company size:
:   Large

Product:
:   [Claude Platform](https://claude.com/platform/api)

Location:
:   North America

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

## Bringing document creation inside Box

Box customers could already create, collaborate on, and sign documents inside the platform. Early customers of the new Box Agent consistently requested the ability to generate presentations, documents, and other file formats. Building that capability in-house didn’t make sense from a timing, effort, or focus standpoint. It would have meant standing up a distributed code-execution environment across Box's data centers and meeting the 5-nines reliability bar Box's customers expect. Box's team estimated the work for the in-house path would take months of engineering time.

“Box's strength is in how enterprise content is managed, governed, and put to work,” said Darryl Sladden, Staff Product Manager for AI at Box. “The intelligence to make a good slide is a different problem, and it's one Anthropic has already solved.”

2 minutes

Redlined a contract vs. an afternoon of manual review

## The solution

## Pre-built skills connected to the path Box already trusted

Box turned to Anthropic's Skills API for the generation itself. Anthropic's pre-built skills for PowerPoint, Excel, Word, and PDF deliver packaged expertise: they encode what makes a slide visually appealing, how to structure analytical spreadsheets, and how to handle complex Word edits cleanly.

“Using the API, we’re able to show the customers very early how they can save work and time, and start to change their processes very quickly,” Darryl says.

The integration principle was to change as little as possible. Box already routes all LLM requests through a production gateway that handles logging, request counting, and access control. Rather than create a separate path for document generation, the team added exactly two things: file upload on the way in, file download on the way out.

“We ran this through our main production path and added the file upload, file download capabilities,” Darryl says. “Everything else: the same file versioning, the same ownership. The only difference we have to talk about is those two paths.”

Inside the agent, Box routes work across Claude models by difficulty. Sonnet typically interprets the user's request, searches Box for relevant source files, and assembles context, while file generation often goes to the more capable Opus model. That flips the common pattern of using the larger model as planner and a smaller one as executor, but it matches where the difficulty sits: orchestrating over Box content is well-bounded, while producing a document that looks right demands more from the model.

The pre-built skills are also what made the speed possible. Spreadsheet analysis benefits from the full structure of a spreadsheet rather than just text extracted by RAG, and PowerPoint generation depends on judgment that's hard to specify, let alone replicate. “PowerPoint files have a lot of taste,” Darryl said. “It's really the designer's mind that I always find is most valuable, that it's actually been trained in.”

The capability runs under Box's existing Anthropic agreement, which contractually ensures customer data isn't used for training. Containers that execute skill code are short-lived, lasting only minutes. For Box's security team, the review was about two new data paths, not a new trust boundary.

Choosing the right Claude model

![Choosing the right Claude model](https://assets.claude.com/7388619b452db0af26c78442a275c86c5ebe3124.jpg?w=2400&q=75&fm=webp&fit=max)

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## The outcome

## Redlining a contract in 2 minutes

Using the Skills API, Box went from concept to customer-facing capability in weeks. A member of Box's internal team tested the agent on a real contract, asking it to show redlines for changing the governing jurisdiction from New York to California. “We just waited two minutes, and it output the entire document,” Darryl said. “It was smart enough to change not only the state, but the city and all the additional clauses that talked about court.”

The financial summary flow works the same way: a user asks for a slide summarizing a company's financial position; the agent searches their Box folders, finds the previous quarterly report and recent monthly updates, pulls the relevant figures, and returns a formatted draft slide with the initial work done, ready for the team to add insights. A follow-up request for the same output as a spreadsheet reuses what the agent already found.

Box went from concept to customer-facing document creation capability in about a month, a timeline that wouldn't have been possible building from scratch. The time that didn't go into infrastructure went into making the agent actively useful inside the enterprise.

The principle that emerged: use pre-built skills where the expertise is general and already trained in; build your own where the knowledge is yours. “The trajectory of AI is really what we're betting on for this,” Darryl said. “Our advice is to look at each capability not only how it is now, but how it will be in six months.”

How enterprises are building AI agents in 2026

![How enterprises are building AI agents in 2026](https://assets.claude.com/faaa398e4d7a94cfce273d40c67bf04482996e0d.png?w=2400&q=75&fm=webp&fit=max)

New research from 500+ technical leaders reveals how enterprises are deploying AI agents—and why 80% already report measurable ROI.

[Read more](https://claude.com/resources/articles/how-enterprises-are-building-ai-agents-in-2026)

> “Using the API, we’re able to show the customers very early how they can save work and time, and start to change their processes very quickly."

Darryl Sladden Staff Product Manager for AI, Box

[![Supermetrics](https://assets.claude.com/3ac4171a81008be0340e5c3d8ccb46571c3edfb3.svg)

### Supermetrics lets marketers manage ad campaigns from a conversation with Claude](https://claude.com/customers/supermetrics)[![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

### How Atlassian builds AI agents teams can trust with Claude and Google Cloud](https://claude.com/customers/atlassian)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### Rocket Money on building agents that fix their own code](https://claude.com/customers/rocket-money-qa)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### How Rocket Money built its personal finance agent with Claude](https://claude.com/customers/rocket-money)
