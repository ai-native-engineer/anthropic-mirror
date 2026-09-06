<!-- source: https://claude.com/customers/spellbook -->

Case study | Claude Platform

# Spellbook runs 530,000 contract reviews a month with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a90a99c672407237f462884_logo_spellbook-light-mode.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a91d95f81c53c648dd54bac_logo_spellbook-dark-mode-fixed.svg)

Industry:

Legal

Company size:

Medium

Product:

[Claude Platform](https://claude.com/platform/api)

[Claude Code](https://claude.com/product/claude-code)

Location:

North America

530,000 contract reviews per month

run by Spellbook's Claude-powered review agents

10x faster agreement turnaround time

for contracts, after cutting from 10 hours of lawyer time to one

By the time a lawyer opens a contract in [Spellbook](https://spellbook.com/), the AI has often already pulled it in from email, Slack, or Salesforce, flagged the risks, and drafted the redlines. Spellbook's Claude-powered agents draft and review contracts inside Microsoft Word and compare their terms against the market, and its new autonomous contract management moves agreements through a company before anyone opens them. Since launching in 2022, Spellbook has grown to 5,000 customers across 80 countries, from law firms to in-house legal teams at companies like LG, Dropbox, and eBay.

## **With Claude, Spellbook:**

* Runs its Claude-powered review agents across about 530,000 contracts every month
* Cuts the time to complete an agreement 10x, from roughly 10 hours of lawyer work to about one
* Handles more than 700,000 chat messages from practicing lawyers each month
* Applies each legal team's own review standards automatically, at a volume of thousands of contracts a year
* Orchestrates roughly 15 Claude agent configurations on its review surface alone, matched to the complexity of each subtask
* Grades production models against Claude Fable 5, the oracle model in its evaluation pipeline, with criteria vetted by legal experts
* Runs its own engineering fully on Claude Code, with Fable writing the plans and reviewing the results before a cheaper model executes

## The challenge

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## 10 hours of review per agreement

Before large language models, contract work meant reading every line by hand. "Lawyers would be  reviewing 50-page contracts in Microsoft Word, reading every line to find issues and mistakes, manually editing, copying and pasting between agreements," said Scott Stevenson, CEO and co-founder of Spellbook. A single agreement could absorb 10 hours of a lawyer's time, and at a top firm where a partner bills $1,000 an hour, that made it a $10,000 document.

The load never stops arriving: in-house legal teams see thousands of contracts flow through them every year, and, at that volume, the cost is more than time. "AI is really good at issue spotting, and humans are not very good at it," Stevenson noted. "These APIs are incredibly good at dealing with free-form text. No one could have built this before large language models."

## The solution

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## Selecting Fable as the domain expert

Spellbook selected Claude for the document editing at the center of the product, and runs a full suite of mostly Claude models on the Claude Platform. Roughly 15 agent configurations just for reviewing contracts, from Opus 5 on the most complex subtasks down to Opus 4.6 and Sonnet 4.6 where speed and conversational tone count for more. "For every suggestion we provide, we measure how many actually get accepted by a user," Stevenson explained. "We think that's better than an eval, because it measures the subjective preferences of the user and whether we're meeting them."

Successive releases kept that decision compounding. "Opus 4.6 last year was absolutely groundbreaking," said Jordan Weir, Senior Engineer at Spellbook. "There have been many times in the last three years that Anthropic was substantially ahead of anything anyone else was doing, so I pushed a lot of features into the Anthropic bucket."

To decide which model goes where, the team measures candidates against Fable. "We'll use Fable as an oracle model to generate a set of criteria, do manual review with our legal engineers and domain experts, and then see which other models come closest to achieving similar behaviors," Weir explained.

One check runs the same contract review, same prompt and contract ten times in a row and scores how consistently issues get flagged, because a lawyer only trusts a review they don't have to repeat. Earlier this year Spellbook moved the review surface from Sonnet 4.6 to Opus 4.6, after customers told the team, in effect, "I feel like I have to run it three or four times to find everything." Fable pulled further ahead. "Fable calls out more important issues, and for the issues it calls out, it calls them out far more consistently than any of the other Opus models," Weir said. "It has a lower time to first issue, and it's just generally a better result."

## Claude Code, but for contracts

One part of the product that lawyers see is a Word add-in that Stevenson describes as "kind of like Claude Code, but for contracts": Spellbook's agents spot issues, negotiate terms, and revise agreements directly in the document, so lawyers keep their file format, formatting, and habits.

Playbooks turn those reviews into enforced policy. An in-house team codifies how it reviews master service agreements and NDAs, what it negotiates and what it concedes, and Spellbook's agents apply that standard to every contract that follows. Around the add-in, a drafting tool retrieves language the team has used before, and chat answers questions with citations a lawyer can check. Spellbook Associate goes further, making complex edits across many documents at once, so one changed term ripples correctly through an entire deal. That scale is where the difficulty lives. "If you're editing five documents, it's easy," Weir explained. "If you're editing 20, it's harder. If you're editing 20 with a thousand other documents in context, it's harder still." The same logic runs through Spellbook's library and repository features, which index a firm's contracts and the questions it always asks of them, so a team holding 10,000 signed agreements can find exactly which ones to re-evaluate when the law changes.

None of that runs on a model of Spellbook's own. The team tried fine-tuning early and abandoned it, betting instead on the engineering around foundation models. "Most of the value we add is in the harness that goes around the models," Stevenson said, and much of that work goes to surviving Microsoft Word, whose formatting specification runs over 5,000 pages of comments, section numbering, and tables. "If you mess up a lawyer's document formatting at all, they just won't use the product," he added. Zero data retention applies across the product, and the agents' reach is deliberately narrow, with edits confined to specified paragraphs so a customer's contract can't leak.

## Fable writes the plan

Inside Spellbook, Claude runs well beyond what customers see. "We use it for everything," Stevenson said. “Our engineering team is all in on Claude Code. Opus 5 is good, but in practice Fable is even wiser."

The team mostly leans toward Fable for writing code. The economics work because Fable touches the steps where judgment deeply concentrates. "Fable is a large model, so we have it write the plan, then a smaller model, such as Sonnet, executes the plan,” Weir said. “After that, we have Fable review the results and flag the five or six things that need to change. The plans are far better than anything we would get before the Fable and Opus 5 era, and because you're only using it for those discrete steps, the additional cost is small. The end result is far better." The pattern has spread well past engineering: Spellbook's partnerships lead uses Fable to assemble project plans that keep a long list of potential partners moving.

"Fable calls out more important issues, and for the issues it calls out, it calls them out far more consistently."

Jordan Weir

Senior Engineer, Spellbook

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## 530,000 contracts assisted per month

Spellbook's Claude-powered agents now run hundreds of thousands of  contract reviews every month, and lawyers send the product more than 700,000 chat messages on top of them. "Every single one of those is a lawyer," Weir noted, "a high-value professional whose time is worth a lot of money."

Behind the volume, an agreement that took 10 hours of work now takes about one, what Stevenson calls "a true 10x efficiency improvement.” The recovered time allows lawyers to focus on why they got into law: judgment, negotiation, and strategy. "I think it's the best time ever to be a lawyer," Stevenson said. "A lot of my lawyer friends were really not that happy with their jobs before AI. They would spend 10 hours a day copying and pasting documents. Now they're like, ‘I actually love my job.’"

Spellbook has grown to 5,000 customers and 250 employees, with growth accelerating after the Claude-powered features launched. In-house legal teams are adopting fastest, because every contract they automate makes the businesses they support faster. "They were just waiting for something that actually worked," Stevenson noted.

Looking ahead, the team wants Claude to move from reviewing agreements to actually running them. Spellbook recently launched autonomous contract management, which moves agreements through an organization from the moment a salesperson requests one, through triage, review, and negotiation, to storage and long-term monitoring. Each new model has pushed the ceiling higher, and Spellbook is built to capture whatever comes next. "We've built an incredibly differentiated product by building on top of foundation models and capturing the gains of their continued improvement," Stevenson said.

"There have been many times in the last three years that Anthropic was substantially ahead of anything anyone else was doing."

Jordan Weir

Senior Engineer, Spellbook

## Related stories

[EvenUp cuts document drafting from 15 hours to 15 minutes with Claude](https://claude.com/customers/evenup)EvenUp cuts document drafting from 15 hours to 15 minutes with Claude

EvenUp cuts document drafting from 15 hours to 15 minutes with Claude

Customer story

[Customer story](https://claude.com/customers/evenup)Customer story

[Eve Legal helps plaintiff law firms settle cases 60 days faster with Claude](https://claude.com/customers/eve-legal)Eve Legal helps plaintiff law firms settle cases 60 days faster with Claude

Eve Legal helps plaintiff law firms settle cases 60 days faster with Claude

Customer story

[Customer story](https://claude.com/customers/eve-legal)Customer story

[GC AI powers legal workflows for 1,500 companies, saving lawyers 14 hours a week with Claude](https://claude.com/customers/gc-ai)GC AI powers legal workflows for 1,500 companies, saving lawyers 14 hours a week with Claude

GC AI powers legal workflows for 1,500 companies, saving lawyers 14 hours a week with Claude

Customer story

[Customer story](https://claude.com/customers/gc-ai)Customer story

[Thomson Reuters CTO on piloting Cowork with Claude Enterprise](https://claude.com/customers/thomson-reuters-qa)Thomson Reuters CTO on piloting Cowork with Claude Enterprise

Thomson Reuters CTO on piloting Cowork with Claude Enterprise

Customer story

[Customer story](https://claude.com/customers/thomson-reuters-qa)Customer story
