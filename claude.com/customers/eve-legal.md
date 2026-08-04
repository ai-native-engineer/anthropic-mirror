<!-- source: https://claude.com/customers/eve-legal -->

Case study | Claude Platform

# Eve Legal helps plaintiff law firms settle cases 60 days faster with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ebbdde1a3d17f2d9e91607_eve-light-mode.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ebbde617bb08ba0d0157b8_eve-dark-mode.svg)

Industry:

Legal

Company size:

Startup

Product:

[Claude Platform](https://claude.com/platform/api)

[Claude Code](https://claude.com/product/claude-code)

Location:

North America

60 days faster settlement times

for firms on Eve

Cut engineering triage from three hours to minutes

with its internal Claude-powered developer tool

[Eve Legal](https://www.eve.legal/) is an AI-native platform for plaintiff-side law firms. Roughly two years after launch, over 1,700 firms run on the platform, 500 of them added this quarter alone. Claude runs the platform's heaviest workflows: analyzing a firm's operations and lawyer performance, dissecting case files that stretch to 70,000 pages, and drafting demand letters in each firm's house style. It also monitors thousands of cases across a firm each night, deploying agents based on the findings.

## With Claude, Eve Legal helps plaintiff law firms:

* Settle cases up to 60 days faster
* Increase settlement values by up to 30%
* Take on up to 30 additional cases per lawyer per year
* Turn case files of 2,000 to 100,000 pages into legal work output automatically
* Process 12.5 million documents a month
* Answer, prioritize, and sign potential clients automatically with voice agents
* Cut engineering triage from three hours to minutes with Wall-E, its internal Claude-powered developer tool

## The challenge

Claude for Statrtups

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0cb8c1f8c5c525e8c554b3_problem-solvers-padded-200kb.jpg)

Join the founders building on Claude. Access community and resources to accelerate your growth.

Read more

[Read more](https://claude.com/programs/startups)Read more

Claude for Statrtups

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Join the founders building on Claude. Access community and resources to accelerate your growth.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude for Statrtups

Join the founders building on Claude. Access community and resources to accelerate your growth.

## Contingency law runs on hours nobody bills

Most plaintiff firms don't work on retainer. They typically take cases on contingency and get paid only when a case settles, so every hour spent on manual casework is an hour the firm absorbs itself until an outcome. The casework can often be demanding. For example, for personal injury attorneys, a single case file arrives as anywhere from 2,000 to 100,000 pages of unstructured records, which a paralegal previously analyzed line by line to build a medical chronology. It includes the ledger of a client’s injuries, the treatment timeline, what it cost, and what came after, all before any can go out.

That labor puts a hard ceiling on how many cases a firm can take, and clients’ cases that don't justify the hours often go unrepresented. Software previously built for the industry typically focused on tracking the labor as opposed to actually taking on the labor. Eve was started to take on all of the heavy manual labor that the legal profession entails," said Jay Madheswaran, CEO & Co-Founder of Eve.

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

## A 400-suite benchmark where Claude keeps coming out on top

For Eve, taking on that labor started with a decision about how central AI would be."We went all-in on AI from the start," Madheswaran said. "It's not, 'How can an attorney work with AI to do this task?' Instead, Eve created a new world where attorneys ask, 'What work do I need to approve that Eve has already done for me?'"

Eve evaluates model candidates against a proprietary benchmark it calls PlaintiffBench: around 420 test suites run against every model the company uses. "We are only willing to move forward on a model when we have confidence in those benchmarks," said Matt Noe, Co-founder and Chief Product Officer.

Claude Opus 4.8 is the production default for the platform's most complex work. Injury cases hinge on timelines, so a model has to reason precisely about when treatments happened and in what order; Noe names Claude's temporal reasoning as the standout. Accuracy across enormous records matters just as much. "Faithfulness and grounding on long documents is another dimension where we measure models, and Claude always stands at the top," Noe noted.

Firms hand Eve their document templates, noting that Eve’s drafts must sound like the firm wrote them. "We found Claude models, in particular Opus, really give us the style adherence of the law firm," Noe said. "It's very personalized to the lawyer's style of writing." Eve routes its hardest scenarios and long, multi-turn tasks to Claude Opus, and uses Claude Sonnet for lighter extraction work.

## One custom harness, routing traffic across three clouds

Inside Eve, those models carry a case through its entire lifecycle. When a new document lands, Claude classifies it, triggers the right workflow, extracts its contents, and builds it into the chronology and downstream drafts, all of which lawyers work with conversationally, chatting with their cases directly inside Eve. Claude also works at the top of the funnel: Eve transcribes calls coming into a firm's call center and scores each one, so intake teams know immediately which cases they can genuinely help with. These workflows earned their autonomy about a year ago, when Eve moved the whole system from a retrieval-augmented generation (RAG) architecture to an agentic one.

Eve built the infrastructure around the models itself. The harness reaches Claude through three routes, the native Claude Platform, Amazon Bedrock, and Google Cloud, switching between them automatically so workflows keep running as the company grows. The same engineering care goes to the output itself. "The work product that plaintiff lawyers ship has to have really high quality," Noe noted. "We really take pride in delivering that quality of product work for them that they can put in front of their clients."

Eve turns the same tooling on itself, building Claude Code into every engineering workflow, including Wall-E, its internal developer productivity system. When a support ticket or production incident hits Slack, Wall-E spins up an isolated environment where Claude agent loops debug the issue and open a merge request, cutting triage from three to four hours down to minutes. Even the finance team runs on it: Claude-built dashboards flag when the cost of a workflow, like writing a demand draft, creeps up week over week.

"Faithfulness and grounding on long documents is another dimension where we measure models, and Claude always stands at the top."

Matt Noe,

Co-founder and Chief Product Officer, Eve

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## Two months faster to settlement

Firms on Eve settle cases up to 60 days faster, case life cycles run 50% faster, and settlement values are up 30% across customers. "Even the best lawyers at a firm are like, 'Oh, wait, I missed this,'" he said. The gains compound overnight. "You're creating agents powered by Claude that are taking on the work while you are sleeping," Madheswaran explained, "so that when you wake up, you're approving legal work that has been done overnight."

The platform processes more than 12.5 million documents a month. The capacity Eve frees up lets lawyers, in Madheswaran’s words, "get back to practicing law." Firms take on up to 30 additional cases per lawyer per year across personal injury, immigration, and labor and employment. At a firm of 100 or 1,000 people, that compounds into thousands more people represented than before. That reclaimed time goes to the clients themselves. "Eve’s taking on those tasks so that they can actually deal with the human element of what is oftentimes the worst thing that's ever happened to a client," Madheswaran said. "It's nice when altruism and a business model work hand in hand."

None of it is left to chance: a dedicated AI outcomes team guides every new firm through its first 90 days, automating 80% of the work the firm previously did manually. Last month, Eve expanded from managing cases to optimizing firms: attorney workloads, case prioritization, and revenue projections. Next on the roadmap are deeper agentic workflows, multi-step drafting, and agents that learn from a firm's feedback on everything from writing style to case strategy. "Personalizing it per case, per lawyer, and per organization," Noe said. "Those are all the areas where we are pushing towards."

"When you wake up, you're approving legal work that has been done overnight."

Jay Madheswaran,

CEO & Co-Founder of Eve

## Related stories

[GC AI powers legal workflows for 1,500 companies, saving lawyers 14 hours a week with Claude](https://claude.com/customers/gc-ai)GC AI powers legal workflows for 1,500 companies, saving lawyers 14 hours a week with Claude

GC AI powers legal workflows for 1,500 companies, saving lawyers 14 hours a week with Claude

Customer story

[Customer story](https://claude.com/customers/gc-ai)Customer story

[Thomson Reuters CTO on piloting Cowork with Claude Enterprise](https://claude.com/customers/thomson-reuters-qa)Thomson Reuters CTO on piloting Cowork with Claude Enterprise

Thomson Reuters CTO on piloting Cowork with Claude Enterprise

Customer story

[Customer story](https://claude.com/customers/thomson-reuters-qa)Customer story

[Wordsmith uses Claude to transform legal operations from 4-day bottlenecks to 4-minute workflows](https://claude.com/customers/wordsmith)Wordsmith uses Claude to transform legal operations from 4-day bottlenecks to 4-minute workflows

Wordsmith uses Claude to transform legal operations from 4-day bottlenecks to 4-minute workflows

Customer story

[Customer story](https://claude.com/customers/wordsmith)Customer story

[Legora helps lawyers work more efficiently with Claude](https://claude.com/customers/legora)Legora helps lawyers work more efficiently with Claude

Legora helps lawyers work more efficiently with Claude

Customer story

[Customer story](https://claude.com/customers/legora)Customer story
