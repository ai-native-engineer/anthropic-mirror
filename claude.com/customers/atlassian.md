<!-- source: https://claude.com/customers/atlassian -->

Case study | Claude Platform

# How Atlassian builds AI agents teams can trust with Claude and Google Cloud

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![Atlassian logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a84a22074cc407a84848_Atlassian_light.svg)![Atlassian logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a84a22074cc407a84848_Atlassian_light.svg)

Industry:

Software

Company size:

Large

Product:

[Claude Platform](https://claude.com/platform/api)

[Claude Code](https://claude.com/product/claude-code)

Partner:

Google

Location:

Australia

5 million+ agents executed

in customer business workflows each month

Millions of users on Rovo Chat

with Claude as a base agent model

[Atlassian](https://www.atlassian.com/) makes the software that teams use to plan, build, and ship their work together, including Jira, Confluence, and more than 20 other products used by over 350,000 customers worldwide. AI is now built into everything Atlassian ships, and customers are asking it to take on more of the real work itself. Claude handles the most complex and long-running of that work, on a platform built with Google Cloud.

## At Atlassian, Claude helps power:

* More than 5 million AI agents running in customer business workflows each month
* Rovo Chat, its in-app assistant used by millions, with Claude as a base agent model
* Rovo CLI, the primary experience for developer AI
* Rovo Max, an early-access mode of Rovo Chat, which plans, reasons, and executes across Atlassian tools taking on complex work.
* Rovo Studio, which uses a variety of models, including Claude (Opus 4.8 and Sonnet 4.6) for low code/no code agents and automations

## The challenge

Claude on Google Cloud

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69eaf379756a2219fdd60403_Screenshot%202026-04-23%20at%209.36.06%E2%80%AFPM.png)

Build advanced AI agents with Claude on Google Cloud.

Read more

[Read more](https://claude.com/partners/google-cloud)Read more

Claude on Google Cloud

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Build advanced AI agents with Claude on Google Cloud.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude on Google Cloud

Build advanced AI agents with Claude on Google Cloud.

## Agents customers trust with work that matters

Chatting with an AI assistant, asking it to summarize a thread or draft an update, still leaves the work to a person. Atlassian's customers want to hand that work to a trusted and capable agent instead: reviewing incoming contracts as a first line of defense, triaging support tickets, and surfacing new sales leads.

Handing an agent that kind of consequential, repeatable work raises a higher bar than chat. The agent has to use Atlassian's own capabilities from inside the product itself, the way a person does,  in order for the business to trust the result. "We're good at building UIs for humans," said Sherif Mansour, Head of AI at Atlassian. "The next muscle is making sure those capabilities are usable by agents as well. How do I make sure agents are an equivalent customer of our software?"

Trust is hardest to earn where the work is most valuable: complex, long-running tasks where a wrong answer compounds the longer an agent works. It only gets harder as Atlassian opens more of its surface to agents, across hundreds of AI capabilities in more than 20 apps, and trust hinges on how they are deployed, what they can access, and what they return. Until agents earn it, customers won't hand them the work worth automating. "Scale, complexity, and trust seem to be the three biggest themes that keep coming up over and over again," Mansour said.

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

## Putting Claude behind the hardest work

Atlassian put Claude behind the workloads where the cost of a wrong answer is highest. For its reasoning tiers, Claude stood out for consistent instruction-following, strong long-context handling, and dependable tool orchestration.

"We prioritize reliability in enterprise workflows,” Mansour said. “The Claude models are better at following complex instructions consistently and handling larger amounts of context without losing important details, especially where quality and trust matter a lot."

That work shows up first in Rovo Chat, the in-app assistant that helps customers move work forward inside Jira, Confluence, and the rest of the suite. Rovo Chat serves millions of users with Claude as one of its models, choosing the right tools and skills from among the thousands Atlassian has exposed. Claude also powers Rovo CLI, Atlassian's primary developer AI experience, and is also behind Rovo Max—a mode of Chat in early access—that takes a goal rather than a task and works until it reaches it. To do that, Rovo Max draws on Teamwork Graph, Atlassian's connected map of the billions of objects that span a customer's apps, and runs inside a managed environment where admins control its packages and network access. Many of Atlassian's customers are also software and IT teams, and Claude handles their code review and code generation, work that often calls for reading across large repositories. Some go further and hand a Jira ticket straight to a Claude-powered agent that picks up the work and carries it out.

Inside Atlassian, the same kind of work runs on Claude Code. It's used heavily across engineering, and a recent pilot extended it to non-technical teams, where product managers and designers used it to prototype, commit small code changes, and build custom internal apps.

## An open platform, built on Google Cloud

Claude runs on the internal AI platform Atlassian built to serve models across its products. At its center sits an AI model gateway built on Gemini Enterprise Agent Platform (formerly Vertex AI) as the primary routing path, managing and interconnecting AI workloads across providers. Atlassian scales that framework on Google Kubernetes Engine alongside Google Cloud's GPUs and TPUs. "In the world of AI, you cannot use one tool for everything," Mansour said. "Working with Google Cloud and Anthropic gives us the ultimate enterprise toolbox to automatically route the right workload to the right model at the perfect time." When a team builds a new capability, it writes its own evaluations, benchmarks models on quality and cost, and deploys whichever performs best.

Atlassian moved the platform behind its high-volume custom agents to Google's Gemini Flash family. "We have significantly reduced operational costs for our customers running continuous AI workflows on our platform," Mansour explained. "By using Gemini and Claude through Google Cloud, we hit a rare trifecta: costs dropped, quality improved, and latency remained optimized." Gemini Flash is now the default for those general-purpose customer agents, while Claude carries the complex, long-running work. When vendors retire models, the team swaps in newer ones without re-architecting. "A long-term roadmap in the world of AI is probably no more than three months these days," Mansour said. "What's most important for all organizations is how do you have your teams empowered with a set of tools to respond to change quickly."

"By using Gemini and Claude through Google Cloud, we hit a rare trifecta: costs dropped, quality improved, and latency remained optimized."

Sherif Mansour

Head of AI, Atlassian

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## Millions of agents, and one that made its own video

More than 5 million agents ran in customer business workflows in a single month, a figure that keeps climbing as customers drop agents into more loops across their workflows. Claude drives the most complex of those experiences.

What that looks like in practice came through in an internal Rovo Max demo. Someone handed the agent a Jira board and asked it to "create me an Instagram reel" for everything the team had shipped. It had no access to Instagram and no built-in way to make a video. The agent read the board, used Teamwork Graph to follow the linked context, and pulled in connected Figma designs and Google Docs. It found libraries to generate video, wrote its own script, and produced a reel with the right announcements, stopping only where it needed an Instagram account, which a human provided. “All of that is powered by Claude," Mansour said.

Where Atlassian takes this next rests on two problems it wants to keep solving for customers: their workflows and their context. The workflows already exist. "Our customers run billions, with a B, of workflows in Jira and Confluence," Mansour said, and the opportunity is finding the steps inside them where an agent can deflect a ticket, surface a lead, or cut the time a task takes. Context is the more durable problem, and the one Teamwork Graph is built to solve. "If you assume that every customer, including ourselves, has access to more and more intelligence every year, and the cost also drops at the same time, then what is the most sustainable differentiation any company can have?" Mansour asked. "It's just the context. It sounds like an abstract term, but the context is really just the knowledge they have everywhere."

“The Claude models are better at following complex instructions consistently, especially where quality and trust matter a lot."

Sherif Mansour

Head of AI, Atlassian

## Related stories

[Rocket Money on building agents that fix their own code](https://claude.com/customers/rocket-money-qa)Rocket Money on building agents that fix their own code

Rocket Money on building agents that fix their own code

Customer story

[Customer story](https://claude.com/customers/rocket-money-qa)Customer story

[How Rocket Money built its personal finance agent with Claude](https://claude.com/customers/rocket-money)How Rocket Money built its personal finance agent with Claude

How Rocket Money built its personal finance agent with Claude

Customer story

[Customer story](https://claude.com/customers/rocket-money)Customer story

[How Notion ships and scales agents with Claude Managed Agents](https://claude.com/customers/notion-qa)How Notion ships and scales agents with Claude Managed Agents

How Notion ships and scales agents with Claude Managed Agents

Customer story

[Customer story](https://claude.com/customers/notion-qa)Customer story

[Deepgram ships 4–10x more durable code with Claude](https://claude.com/customers/deepgram) Deepgram ships 4–10x more durable code with Claude

Deepgram ships 4–10x more durable code with Claude

Customer story

[Customer story](https://claude.com/customers/deepgram)Customer story
