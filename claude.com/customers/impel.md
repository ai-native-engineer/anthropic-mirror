<!-- source: https://claude.com/customers/impel -->

Case study | Claude

# How Impel is building an agent for every job with Claude

[Try Claude](https://claude.ai)

![Impel AI logo](https://assets.claude.com/39d44e8971441c5dc5bafc4aeba0054a6c547c89.svg)

Industry:
:   Automotive

Company size:
:   Medium

Product:
:   [Claude Platform](https://claude.com/platform/api)[Claude Enterprise](https://claude.com/solutions/enterprise)[Claude Code](https://claude.com/product/claude-code)

Location:
:   North America

Ramp time cut to 1 month

down from the 3 to 6 months reps once needed per new product

85% less prep time

per dealer business review

[Impel](https://impel.ai/) builds vertical AI solutions for automotive dealers and OEMs, including digital voice assistants that field dealership calls. Inside the company, AI adoption starts from a stack-rank of its biggest business problems, funded like investments and built on Claude. One agent workflow is built from Claude's analysis of more than 150 thousand recorded dealer calls so that 150+ customer-facing reps can practice hard conversations in advance.

## With Claude, Impel:

* Cut new-product ramp time from 3 to 6 months to an average of 1 month of roleplay and certification
* Reduced monthly business review prep from 3 to 4 hours to about 30 minutes with Claude-drafted briefs from Snowflake
* Handles 20% more support cases, with reclaimed time going to migrations and strategic projects
* Saw roughly 25% of go-to-market staff practicing voluntarily in the past month, beyond any certification requirement
* Built the flagship roleplay agent in about 3 weeks
* Maps 30 to 40 agent opportunities into six root-cause problem clusters, funded in priority order

## The challenge

## A product engine that outran its own training

Impel's training problem started with its own success: once its product and engineering teams adopted Claude Code and became, in the team's words, "10x engineers," features shipped faster than its 150-plus customer-facing reps, out of nearly 500 employees, could learn to sell and support.

Presentations and FAQ documents were never going to close that gap. "People only really learn when they go and do the thing," said Britt DeJohn, SVP of Operations at Impel. "We didn't want our team to stumble in the market and practice for the first time with actual dealers." The audience includes dealership staff with 20-plus years of expertise. Small-group roleplay with colleagues felt inauthentic, and practicing on live dealers risked real relationships.

Reps needed 3 to 6 months, sometimes more, to get comfortable with a new product, pulling solutions engineers and sales leaders into conversations they could not yet carry. Account reps hand-assembled every monthly business review, spending 3 to 4 hours each, and each quarter brought strategic projects nobody was free to run.

Claude Fable

![Claude Fable](https://assets.claude.com/c4cccb47d2ee2cf151f52b084554003b801e6a75.jpg)

Next generation of intelligence for the hardest knowledge work and coding problems.

[Read more](https://www.anthropic.com/claude/fable)

## The solution

## The first model trusted to carry the work

Impel selected Opus for the multi-step work needed across engineering and product. "The tipping point was Opus 4.5: it felt like the first truly agentic model we had used," said Benjy Kest, Chief of Staff at Impel. "We could hand off multistep workflows across MCPs and trust it to carry the work through without hardcoding every step. It felt like learning how to work effectively with a coworker."

The push beyond engineering started when engineers shared what they had been building with Claude Code: "We realized that these powerful capabilities had applications far beyond just product development,” Kest said. "As a company trusted by thousands of automotive dealers, we needed powerful models without compromising company or customer data, and our InfoSec and Legal teams were particularly impressed with Anthropic.” Impel now runs 400-plus Claude Enterprise seats across knowledge work and engineering.

Impel runs a mix of foundation models alongside its own verticalized models, and what settles on Claude is the complex, reasoning-intensive work spanning large datasets and multiple systems. "We use frontier models like Opus 5 and Fable 5.1 where stronger reasoning matters most: designing new agents, navigating messy context, solving workflows we haven't mapped before," Kest explained. "Once a flow is proven, we test lighter models like Sonnet and routinely find they deliver sufficient results as executor agents."

## Fable for the unmapped work, Sonnet for the proven

Roughly 70 to 80% of Fable usage sits with engineering for code generation; the rest is knowledge work where reasoning is the bottleneck. "We found Fable to be much more opinionated than the other models, in a good way," said Kest. "It's more willing to make decisions instead of taking a neutral path or referring back to the user. It absorbs the context and acts on what it thinks is the best path forward, which is really helpful because it's usually right." Depending on how much users want to stay in the loop, he added, "the smarter models need less babysitting and are more likely to get to the right output on a first attempt, even with less context."

For example, Kest pointed Fable at Salesforce to map every object, field, and relationship into a reusable skill for lighter models. "Now if I have a quick question about Salesforce, I'm using Sonnet because it's a lightweight one-off task," he explained. "It references the skill Fable made and performs almost five times better, and the reliability is almost 100% at this point. When it comes to documenting business processes and mapping out our internal systems, we’ve found Fable to do that in a way that the other models haven't been able to.”

Claude Code

![Claude Code](https://assets.claude.com/38e8385d1c5f9c0f71c486994e22fc5861a4522d.jpg)

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](https://claude.com/product/claude-code)

> "We found Fable to be much more opinionated than the other models, in a good way."

Benjy KestChief of Staff Impel

## The outcome

## One-month certifications, thousand-review weeks

With Claude in 400-plus hands, leadership collected close to 100 agent candidates and culled the list to less than 40. "We started asking: what are the biggest business problems?" DeJohn said. Each candidate mapped to one of six root-cause clusters, from revenue leak & retention risk to talent performance & ramp speed. Each cluster was then scored on impact and build complexity, then landed in buckets labeled fund-now, back-half, or next-year.

Training ranked near the top of that first stack-rank on the strength of one question: "How do you encode in-the-room judgment that veteran reps have developed through years of experience?" DeJohn said. The dealer roleplay agent is Impel's answer. Every dealer-facing call at the company is recorded, and Claude worked through that archive to build the training, "digging through more than 150 thousand Gong calls and our entire Salesforce instance," in Kest's words, "analyzing an amount of data that no team of even 20 humans could reasonably get through in two months." "Standing it up with Claude was the easy part," DeJohn noted: about 3 weeks, against the 1 to 2 months spent aligning go-to-market leaders on scenarios and rubrics. The agent runs custom tracks from sales through support, speaks via speech-to-text and text-to-speech, opens in character ("I've got about 30 minutes before I need to jump into a floor meeting, so let's make this count. I'm Derek"), and scores each session on objection handling, rapport, product knowledge, and next steps, DMing the scorecard in Slack.

Ramp time on new products, which used to run 3 to 6 months, now averages 1 month of structured roleplay and certification, and escalations fell with it. Reps who once had to tap in a solutions engineer or the VP of sales now carry the conversation themselves. "With this method, there's up to 20% fewer escalations in the first two months of a new product or feature rollout, because they're feeling more comfortable in that knowledge themselves," DeJohn explained. In the past month, roughly 25% of the go-to-market organization logged in to practice on their own time. "That wasn't mandated," DeJohn said. "That was them seeing the value in this sandbox practice environment."

Other clusters show results too. Support reps handle 20% more cases with Claude-based triage agents that read open cases against account history and draft resolution notes, and the reclaimed time goes to platform migrations and what DeJohn calls "plenty of side quests." Account teams build monthly business reviews in about 30 minutes, with Claude drafting each brief straight from Snowflake and surfacing the moments worth spotlighting, which helped the team deliver close to 1,000 reviews in a single week, a company record.

Leadership re-scores the portfolio each month against whatever new problems the company is seeing, with the team aiming for an agent for every job, department, role, and process. Rob Murphy, Impel CMO, sees the whole effort as a mirror of Impel's own pitch to dealers. "Our entire business is about bringing highly specialized vertical AI solutions to dealers and OEMs," he said. "The things we've done with Anthropic's models and tools have delivered the same impact that we have with dealers: making the employee experience better, driving business results, and improving relationships with our customers."

> "As a company trusted by thousands of automotive dealers, we needed powerful models without compromising company or customer data."

Benjy KestChief of Staff Impel
