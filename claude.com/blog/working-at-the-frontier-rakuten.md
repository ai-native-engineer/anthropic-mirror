<!-- source: https://claude.com/blog/working-at-the-frontier-rakuten -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7912d5b05a5c7ed8ae86_Object-CodeChatCode.svg)

# Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5

Yusuke Kaji, General Manager of AI for Business at Rakuten, has been testing Claude models since Sep 2024. Here’s why he thinks Claude Fable 5 is a step change for long-running enterprise agents.

* Category

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)
* Product

  [Claude Code](https://claude.com/product/claude-code)

  [Claude Cowork](https://claude.com/product/cowork)

  [Claude Platform](https://claude.com/platform/api)
* Date

  July 20, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/working-at-the-frontier-rakuten

As General Manager of AI for Business at Rakuten, Yusuke Kaji’s job is to “find the seeds of transformative innovation and scale them across the company.”

One of those seeds was Claude.

Since March 2025, Rakuten has used Claude to speed up software development with Claude Code, stand up agents across its business functions, and power AI features for millions of customers. According to Kaji, Rakuten chose to partner with Anthropic for its enterprise focus, leadership, and product taste.

Across nearly a dozen model launches, he's watched the work he can hand to an agent keep growing: first using Claude Code to [ship production software](https://claude.com/customers/rakuten), then building custom [Claude Managed Agents](https://claude.com/customers/rakuten-qa) for teams across the company. He likens testing out new models with embarking on a “new quest.”

“The way a good leader prepares stretch goals for their people, we prepare stretch tasks for a new Claude,” he adds. “Maybe Claude is nudging us to stretch, too."

When he tested Claude Fable 5, he knew something felt different. The model could run on its own for far longer than its predecessors, and for the first time, checking its own work and completing nuanced tasks overnight while Kaji slept.

That extra autonomy is what lets Rakuten hand its agents bigger, longer-running jobs, and transform the way they work.

### **Building an AI-native workforce**

Rakuten is remaking itself around AI, a project it calls AI-nization – their company-wide effort to infuse AI into everything we do for customers, business partners, and employees.. When Claude Managed Agents arrived, Rakuten deployed agents across product, sales, marketing, and finance inside a week, plugged into Slack, Microsoft Teams, and the company's own task system.

For Kaji and his team, the constraint about building agents used to be who could write code; now, it's who understands the business problem.

"The modern corporation is designed to minimize the cost of communication," he says. "I believe agents like Claude Code can shine when we work with them to minimize the cost of new innovation as well, like a quick transition from idea to production." Give a capable person agents that hold context and taste, and "it allows the hidden talent to unlock their potential and scale their potential 100 times more."

But running agents in every function around the clock surfaces a new constraint: human judgment. While Rakuten's agents close issues roughly 10x faster across every domain, the number of tasks the organization takes on keeps rising. Adding more agents doesn't add judgment. So the faster the agents run, the more the organization's progress depends on a person closing the loop.

### **Powering agents that run for hours, unattended**

For most builders, the hardest part of building long-running agents is setting them up to succeed with minimal oversight. Connecting it to the right tools and context is one thing, but in Kaji’s experience, there were always limits to how long an agent could go without needing a human in the loop to validate its work.

Before Claude Fable 5, setting an agent loose on a multi-hour task without human oversight was always a gamble. "If they choose the right path in the first step, everything is fine," Kaji says. "But if they choose the wrong direction in the first pass, the agent spends significant time to fix the path, or even fails to reach the destination." On a job meant to run five hours or a full day, one early wrong assumption could burn the entire run, and the only way to catch it was a person checking in.

The failure mode was a lack of self-verification. Any model can take a wrong first step. The problem with earlier models was that they didn't check their own work as they went, so an early wrong turn went unnoticed. It compounded over the run and produced a suboptimal result hours later.

According to Kaji, Claude Fable 5 changes the calculus for days-long agentic runs because it checks its own work as it goes, far more often than any prior model.

"We tested Fable, and we love its capability for self-reflection and self-verification," Kaji says. "Compared with previous models, it understands its mistake before I point it out at 2 a.m. or 3 a.m.—so that I can sleep."

### **What sets Claude Fable 5 apart**

Kaji’s team cite three behaviors that distinguish Claude Fable 5 from its predecessors, and signal a step-change in frontier intelligence:

* **It re-checks its own assumptions.** When the state of the task changes midway, Fable 5 notices and corrects a wrong assumption before acting on it, rather than committing to a bad path and discovering it hours later.
* **It returns to first principles at each step.** It re-validates against the original intent without being told, the course-correction Kaji used to have to make himself when a run started down the wrong path..
* **It matches the team's taste.** Even with minimal guidance, its judgment on ambiguous calls lines up with theirs. Kaji has a name for this, a term he coined: taste alignment. "Taste alignment is smoother with Fable than any previous model from your company, or any other model we’ve used."

Most importantly, longer autonomy changes the unit of work Kaji can delegate.

“Before Fable, we had to break work into well-defined chunks for the agent to execute," he says. Now he can hand over a whole task and run several at once.

Claude Fable 5 changes what happens in between. It reflects at each step, catches a bad early assumption, and finds its own way back to first principles — re-navigating to the right outcome without anyone steering it. Because the model self-corrects mid-run, sign-off becomes feasible for the first time, and the unit of work Kaji delegates shifts from the task to the decision. The agents also carry memory between runs: "Our agents with memory remember what went wrong in past sessions and avoid repeating those mistakes."

As a result, the absolute number of tasks keeps climbing, but the ones that truly need a human stay at a focusable level. Not having to jump in and steer mid-run is, he says, is the biggest productivity win of all—it lets his team spend its time on the decisions only people should make, and keeps an AI-native organization accelerating instead of stalling on human course-correction.

#### Balancing cost and efficiency

Frontier capability comes at a frontier price, and Kaji is direct that cost decides how widely he can deploy.

"As a large enterprise, we want to balance intelligence and cost," he says. His team measures task completion ratio alongside cost per task, then sends Fable 5 the work where the extra capability changes the outcome and lets smaller models keep the rest.

For Kaji, two things make the math work in Fable 5's favor: it gets more done with fewer tokens and fewer wrong turns, and it needs less hand-holding.

### **What’s next**

The frontier Kaji is testing now isn't individual speed. It's getting agents to coordinate people. Claude Code has sped up his own work and his colleagues', but the hard part of any organization is the alignment between people, matching one person's context and taste to another's. He's exploring agents that "coordinate or organize, more like a manager," holding the nuance that usually gets lost between team members.

"We do not see AI agents as future colleagues or competitors. They are systems around us." And he holds Anthropic to its own advice, that you should build for the model coming in three or six months rather than the one in front of you.

"I think we as a society still haven't found the model–task fit yet for Claude Fable 5," he says, "but it already stands out as a model that crossed the line and came over to our world.

***Get started with*** [***Claude Fable 5***](http://anthropic.com/news/claude-fable-5-mythos-5)***.***

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d23008bbc20c0ffaeb6f_43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)

Jun 18, 2026

### Centrally manage authorization for MCP connectors

Enterprise AI

[Centrally manage authorization for MCP connectors](#) Centrally manage authorization for MCP connectors

[Centrally manage authorization for MCP connectors](https://claude.com/blog/enterprise-managed-auth) Centrally manage authorization for MCP connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d222061abf091318fb82_423062049d4676b41d52b16068cbb5e21603190e-1000x1000.svg)

Aug 21, 2026

### The AI-Native SDLC playbook

Enterprise AI

[The AI-Native SDLC playbook](#)The AI-Native SDLC playbook

[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)The AI-Native SDLC playbook

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

Aug 13, 2026

### Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

Agents

[Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions](#)Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

[Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions](https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions)Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

Aug 20, 2026

### Build production agents with computer use, the Skills API, and the Files API

Product announcements

[Build production agents with computer use, the Skills API, and the Files API](#)Build production agents with computer use, the Skills API, and the Files API

[Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api)Build production agents with computer use, the Skills API, and the Files API

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Code

Claude Cowork

Claude Platform

Coding

Agents
