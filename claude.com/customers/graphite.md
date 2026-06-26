<!-- source: https://claude.com/customers/graphite -->

Case study | Claude Platform

# Graphite speeds up code review by 40x with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![Graphite logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bb5f0cfaa84d1119a0c35b_Clip%20path%20group.svg)![Graphite logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bb5f1d05f1df7047ff2c0d_Graphite-dark-theme.svg)

Industry:

Software

Company size:

Small

Product:

Location:

North America

800x faster

35 minutes vs 3 weeks for analysis

Human-level

performance on biomedical benchmarks

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Read more

[Read more](#)Read more

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Read more

[Read more](#)Read more

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

Graphite, a modern end-to-end developer platform, uses Claude to power their AI code reviewer that catches bugs and suggests fixes, transforming how engineering teams at companies like Snowflake, Asana, and Ramp approach software development.

With Claude, Graphite achieves:

* 40x faster pull request feedback loop, from 1 hour to 90 seconds
* 96% positive feedback rate on AI-generated comments
* 67% implementation rate of suggested changes
* Support for hundreds of thousands of pull requests across their customer base

## The challenge of scaling modern code review

Code review is a critical bottleneck in modern software development. While big tech companies like Google and Facebook have sophisticated internal tools to manage this process, most engineering teams struggle with basic GitHub workflows. "The open secret in dev tools is that almost every company builds tooling on top of GitHub to improve it for teams," said Tomas Reimers, Co-founder at Graphite.

Without proper tools, developers face mounting delays. They wait hours or days for feedback, then start another time-consuming cycle of fixes and re-reviews. In early 2023, Graphite explored AI-powered code review after receiving repeated requests from forward-thinking development teams. However, early experiments proved disappointing. "The models would hallucinate and confidently claim problems in pull requests that didn't exist," said Reimers. "When the bot generated incorrect but specific statements, people were frustrated." The team needed something that could match human-level understanding of code while maintaining high accuracy.

## Choosing Claude for superior code comprehension

After testing leading AI models, Graphite found that only Claude met their standards for code review. The team's rigorous evaluation framework tested models against 500 pull requests, including synthetic and real-world examples with known bugs that even experienced engineers struggled to spot. "Claude was especially good at code understanding, which for code review is incredibly important," said Alyssa Baum, Lead AI Engineer at Graphite.

The release of Claude 3.5 Sonnet marked a decisive breakthrough. Baum said, "Not only did our eval performance skyrocket, but it identified bugs in our test dataset that we hadn't even realized were bugs." Through A/B testing, the team confirmed Claude's superior performance. "When Claude 3.5 came out, we plugged it into our system and the performance for our users was incredible."

The partnership with Anthropic amplified these technical advantages. Anthropic's team provided crucial guidance on evaluation frameworks and implementation strategies through a dedicated Slack channel. When Graphite's October 2024 launch faced unexpected demand, Anthropic quickly helped scale their rate limits to meet customer needs. "We've had great support from the Anthropic team," said Reimers. "We found it to be incredibly helpful just for getting advice on how we should structure our evals and our code in general."

## Transforming code review through advanced AI architecture

Graphite's implementation combines Claude's sophisticated reasoning capabilities with deep expertise in effective code review. Their architecture breaks complex code analysis into discrete steps, allowing Claude to excel at each specific task. The system employs multiple validation layers including voting, chain of reasoning, and self-critique to ensure only high-quality comments reach developers.

The platform focuses on objective bugs, not subjective suggestions. It addresses issues like:

* Function parameter ordering errors
* Copy-paste mistakes
* Security vulnerabilities
* Logic inconsistencies
* Best practice violations

When issues are identified, the system automatically generates fix suggestions for developers to implement with a single click, reducing the traditional fix-and-review cycle time.

![Graphite product screen ](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68baf058657d4f7b80396a99_0068517fa5822a805c478c7c933c6b29af2c1f65-2880x1620.png)

![Graphite product screen](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68baf058657d4f7b80396ac0_89b8c38542c938ea808b12f185b0a72e7ba58e28-2880x1620.png)

## Delivering measurable impact for development teams

Graphite's AI-powered approach has transformed the development workflow for their customers. Brian Michel from The Browser Company said, "Graphite Reviewer strikes a good balance between showing problems and not being annoying. It's different from other AI tools because it actually works. I'm able to iterate faster and produce something that is workable faster. This helps as a single developer because you're really not alone anymore."

The impact extends beyond individual developers to entire engineering organizations. "Graphite has been a game-changer for the team at Ramp," said Nik Koblov, Head of Engineering at Ramp. "The AI reviewer's automatic comments catch subtle errors before they become bugs, helping us maintain quality without slowing down. Overall, Graphite has made our workflow smoother and more productive."

This quality-at-speed advantage resonates across Graphite's customer base. "Graphite Reviewer is impressively high-signal: it has already caught several real bugs before they make it to customers, which is a valuable addition to our developer workflow," said Ben Kraft from Notion.

The system currently provides actionable feedback on one in five pull requests, nearing the industry standard of one in three receiving human comments. With 67% of AI suggestions leading to code changes and a 96% positive feedback rate, Graphite shows that AI can match human-level code review quality while operating at machine speed.

## Looking ahead to AI-augmented development

Graphite envisions a fundamental transformation in software development over the next decade. Reimers said, "Our belief here at Graphite is 10 years from now, individuals aren't going to write software. LLMs will write the majority of the code, and they'll be guided by or collaborate with humans who connect their product to the outside world."

Through their partnership with Anthropic, Graphite is leading this transformation. By automating time-consuming reviews, catching subtle bugs, and enabling one-click fixes, they're freeing developers to focus on what humans do best – making high-level architectural decisions that shape the future of software. Together, Graphite and Claude are transforming code review from a bottleneck into an accelerator of human creativity and engineering excellence.

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
