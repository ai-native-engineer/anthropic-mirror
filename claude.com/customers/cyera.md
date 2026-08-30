<!-- source: https://claude.com/customers/cyera -->

Case study | Claude Enterprise

# Cyera scales agentic AI across 1,500 employees with Claude Enterprise

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a755437bdd73dced6999628_logo_cyera2-light-mode.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a755440205f26561ab3f47c_logo_cyera2-dark-mode.svg)

Industry:

Cybersecurity

Company size:

Large

Product:

[Claude Enterprise](https://claude.com/solutions/enterprise)

[Claude Cowork](https://claude.com/product/cowork)

Partner:

AWS

Location:

North America

88% weekly active usage of Claude

across roughly 1,500 employees

40 tools connected to Claude Cowork

making one agent the front door to company systems

[Cyera's](https://www.cyera.com/) AI Security platform gives organizations the confidence to embrace AI by making data the foundation of security. It discovers and classifies data everywhere it lives, and knows which AI agents and identities can reach it. Internally, Claude is the default way its 1,500 employees work: Claude Code for R&D, Cowork for everyone else.

## With Claude, Cyera:

* Reached 88% weekly active usage of Claude across roughly 1,500 employees
* Connected 40 tools and seven homegrown MCP servers servers to Claude Cowork
* Opened self-service data analytics to the whole company over a governed Snowflake semantic layer
* Cut daily triage of its internal Ask Claude channel from five or six hours to roughly 30 minutes
* Gave its legal team a Cowork plugin with 20 playbooks that pre-reviews inbound NDAs

## The challenge

Q&A: Cyera on Claude Cowork

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a755c508a2b7d1fe654251e_og_case-study-Cyera%20(1).jpg)

Read how Cyera uses Claude Cowork as the front door to 40 tools.

Read more

[Read more](https://claude.com/customers/cyera-qa)Read more

Q&A: Cyera on Claude Cowork

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Read how Cyera uses Claude Cowork as the front door to 40 tools.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Q&A: Cyera on Claude Cowork

Read how Cyera uses Claude Cowork as the front door to 40 tools.

## Everyone wanted what R&D had, but not the terminal

Most of Cyera's employees could see what agentic AI was doing for the engineering org and didn’t have access themselves. Claude Code had spread across most of R&D, and the engineers driving that adoption began teaching go-to-market leaders to install it. A few took to it; most stalled at the command line.

"I spent a lot of time teaching non-technical folks how to get into the terminal," said Joe Tustin, Principal Technologist, Applied AI at Cyera. "It was great to see them navigate their computers using the command line and understand where they are from a file directory perspective, but they were uncomfortable to run commands and connect to Snowflake through an API. These were all new things for them."

Cyera's own customers show where that leads: employees without an AI tool at work find one anyway, without their security team’s oversight. "Saying no AI is not a strategy," Tustin added. "You end up with people that use AI on their own, completely outside their company’s network. If you're worried about shadow AI, you need to give them a sandbox environment to test in."

## The solution

Cowork

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525604b02eec936ac521_696fc8952f473c6520149cfa_4f58536f1c08deac7a94811f4be57881_og-claude-cowork.jpeg)

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

Read more

[Read more](https://claude.com/product/cowork)Read more

Cowork

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Cowork

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

## One governed agent connected to 40 tools

The team considered building its own wrapper around Claude Code, an app it would maintain and push to laptops, and surveyed the open-source projects appearing around agentic AI. Everything required an engineer at the keyboard: the interfaces made sense to someone who already knew what a cron job was, but at the time there was little else built for business users.

The answer was Claude Cowork. "We knew we wanted a general-purpose agentic tool so that people could solve their own workflows," Cyera VP of AI Steve Klementowski said, and Cowork put that capability into an approachable interface for the company to use.

“I test as many models as possible,” Tustin said. “I look for how models keep the thread through the task and how it handles arriving at crossroads—does it take the distraction bait or evaluate when to stop? Claude holds context, follows instructions, and has been consistent as my daily driver.”

The Cyera team paired that intuition with concrete measures.

“One thing that doesn't get talked about enough is model knowledge cutoff dates: the time elapsed between the first day of the models’ training and when the user is interacting with it,” Tustin said. “Claude Opus 5 has the most recent training data of any major model. That matters because when the model already knows about a recent API change or a new library version, you skip the step where you have to explain it. That new information is exactly where models get in trouble and trapped. It prevents delays, wasted time, and tokens.”

Cyera then connected Claude to Slack, Salesforce, Asana, Google Drive, Notion, and dozens of other systems. "We've connected 40 tools now to Claude Cowork, and we have built four or five homegrown MCP servers," he added. "It's tough to replicate that. You can only create so many central focal points."

The wiring came with rules. Before rollout, the team ran data-mapping exercises: which systems Claude would connect to, which contained production data, and how Cyera would maintain observability.

To solve questions about access, Cyera relied on what Tustin calls "Cyera on Cyera": using its own platform to map who could reach which Snowflake tables, then re-scoping permissions where needed. A rollout to 1,500 employees raised the stakes: opening analytics company-wide put Snowflake in front of people who had never queried it. Plus, while Cyera's research across 2.4 million workers found employees typically access only 4% of the data they're granted, agents can use whatever their permissions allow. To make the newly governed data usable, the data engineering team built a semantic layer of 40 documented tables by department, paired with a built-in skill on company-specific definitions and conventions.

After a brief pilot to iterate on feedback from cross-departmental leaders, Cyera’s AI team rolled out Cowork to the entire company in just 17 days. A full day of livestreaming showing off the tool’s capabilities, twice weekly office hours, and 20 dedicated sessions for specific departments all helped drive rapid adoption of Cowork. So did close partnership with the data and RevOps teams to make sure the tool would provide actual value to a wide range of employees.

“We had to do a lot of work with the system and business owners for each system we connected to in order to understand what people wanted to use it for, what type of data they needed, and how Claude could access it,” Tustin said. “So that was a huge unlock.”

"I test as many models as possible. Claude Opus 5 has the most recent training data of any major model."

Joe Tustin,

Principal Technologist, Applied AI

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## The outcome

## 88% of the company, every week

Weekly active usage of Claude Enterprise across Cyera's 1,500 employees has reached between 88%, including the newest hires. "We had someone three weeks into the job respond to a 60-page RFP using Claude to give it an initial pass," Klementowski said. Behind the number, the workflows share a shape: an agent takes the repetitive first pass, a person reviews before anything ships.

Employee questions about Claude flow into an internal Ask Claude channel. A scheduled task checks it about every 30 minutes, reads new messages against Cyera's knowledge bases and past answers, and drafts replies for the owner's review, turning five or six hours of daily triage into roughly 30 minutes.

On the marketing side, the team runs more than 1,000 events a year, from CISO dinners to DataSecAI gatherings with hundreds of executives. Ahead of a New York event, the team used Cowork to query Salesforce for every tri-state opportunity and contact, build a 3,500-person list matching the target demographic, and reach out to every salesperson and their manager. Registrations went from 105 to more than 400 overnight. The team's Asana tickets and requests used to get reviewed in a weekly meeting that ran an hour or more, and bounced back and forth when a Figma file or a URL was missing. Now every member has an Asana agent: gatekeepers catch the missing pieces before a ticket is submitted, and the marketer who runs the review has an agent that polls the rest to keep everything current. "It saved her maybe 12 hours a week, which is insane," Tustin added.

Sales took the same idea to outreach. BDRs build targeted prospect lists for upcoming events and webinar follow-ups, then draft with a skill built from the top performers: intros that "memorialize the best work from the best BDRs," reach Gmail in minutes instead of hours. "It's not only a time-saving thing," Klementowski noted. "It's also trying to drive quality improvements."

The legal team launched a Claude plugin with 20 playbooks on day one. Inbound vendor NDAs get assessed against Cyera's positions, whether terms overstep or run too weak, with response bullets drafted for a lawyer to review and send.

Individual workflows stack underneath the team ones. Cyera's privacy and GRC analyst pointed an agent at his own back catalog: whenever he publishes something new, it scans everything he has ever posted in the domain, flags what newer policies have invalidated, and opens tickets assigned to him. A cleanup he'd get to maybe once a month now runs every week.

Klementowski runs one too: a DM triage that reads his Slack messages, checks whether he has replied, researches his calendar, Google Drive, Notion, past call recordings, and Snowflake, and drafts responses he sends with a click, saving up to 30 minutes per run.

The broadest effect runs through Snowflake. "Everyone in the company is doing self-service analytics now," he added, and the analytics team spends less time producing reports and more time improving the data and context people query against.

The same reallocation shows up company-wide. "People are finding it's not that it was never part of their job, but they never had time to do that part of their job," Tustin explained. "Once people get to that point where they're like, now I'm creating things because I'm having fun, I think people are enjoying it a lot more."

With access solved, attention turns to what teams do with it. "Learning these tools requires time in them, so we have to invest in enablement." Klementowski said. “Now we're focusing on the most strategic projects that we can take on, and how we can help level up our teams.”

"Saying no AI is not a strategy. You end up with people that use AI on their own, completely outside their company’s network."

Joe Tustin,

Principal Technologist, Applied AI

## Related stories

[Vega's cyber defense platform returns 67% of analysts' time with Claude](https://claude.com/customers/vega)Vega's cyber defense platform returns 67% of analysts' time with Claude

Vega's cyber defense platform returns 67% of analysts' time with Claude

Customer story

[Customer story](https://claude.com/customers/vega)Customer story

[Cyera on making Claude Cowork the front door to 40 tools](https://claude.com/customers/cyera-qa)Cyera on making Claude Cowork the front door to 40 tools

Cyera on making Claude Cowork the front door to 40 tools

Customer story

[Customer story](https://claude.com/customers/cyera-qa)Customer story

[Kai delivers preemptive exposure management with Claude](https://claude.com/customers/kai) Kai delivers preemptive exposure management with Claude

Kai delivers preemptive exposure management with Claude

Customer story

[Customer story](https://claude.com/customers/kai)Customer story

[How Artemis helps security teams cut incident resolution time by 96%](https://claude.com/customers/artemis)How Artemis helps security teams cut incident resolution time by 96%

How Artemis helps security teams cut incident resolution time by 96%

Customer story

[Customer story](https://claude.com/customers/artemis)Customer story
