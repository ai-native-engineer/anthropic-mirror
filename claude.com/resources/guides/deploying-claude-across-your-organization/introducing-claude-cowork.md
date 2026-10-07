<!-- source: https://claude.com/resources/guides/deploying-claude-across-your-organization/introducing-claude-cowork -->

Chapter 028 min read

# Introducing Claude Cowork

8 min read

32 min remaining

Until recently, most AI tools have been conversational: you ask it a question, it provides an output in the context of a chat window.

Agents change that relationship. You describe an outcome, AI plans the steps, executes them, and delivers something tangible across your files and tools. While coding agents paved the way, functions beyond software engineering are transforming their work by building specialized agents.

Learn more

Learn how enterprises are building and using agents in our 2026 State of AI Agents Report.

Powered by Claude, Claude Cowork is the product surface where this happens for knowledge work, the way Claude Code is the agentic harness for developers. It runs on your desktop and meets your work where it already lives: local files and folders, connected cloud apps like Slack and Google Drive, and the browser via Claude in Chrome. Claude can also work across Excel and PowerPoint, carrying context from one to the other so an analysis and the deck that presents it happen in a single session.

The difference between Claude Cowork and a chat window is agency. You don't re-explain your brand voice, your data schema, or your approval process on every turn. Claude holds that context across the task and moves between the spreadsheet, the slides, and the memo the way a colleague would.

Get started

[Get started (opens in new tab)](https://support.claude.com/en/articles/13345190-get-started-with-cowork) with Claude Cowork today.

## Chat, Cowork, or Code: choosing the right Claude surface

Claude Cowork is one of three ways to work with Claude in the desktop app. Part of deploying it well is helping people know when to reach for it and when one of the other two is the better fit.

**Chat** is for quick exchanges: exploring an idea, iterating on a paragraph, getting an answer without leaving the app you're already in, and most of your organization is already here. In-flow tasks include reading a dense PDF and asking for the one-sentence takeaway, sanity-checking a claim ahead of a meeting, or making sense of a long Slack thread you walked into cold.

**Cowork** is for knowledge work that takes real effort: pulling information from many sources, making sense of it, and producing something finished like a document, deck, or spreadsheet. Folder access, enterprise connectors, browser, scheduled tasks, plugins. When the output is a deliverable rather than an answer, this is the surface. The projects Cowork excels at include turning a folder of customer interview transcripts into a themed findings doc, building a competitive landscape from a dozen vendor sites and their recent announcements, or a scheduled Friday-morning task (for instance, a weekly revenue report) that pulls metrics from connected tools and drops a formatted brief into a shared folder.

**Code** is the full development environment for engineers: direct codebase access, plan and code modes, visual diffs, git integration, local or remote environments. It's where your developers already live, and Claude Cowork doesn't try to replace it. Examples include shipping a feature across a multi-service codebase with tests, building a web application, or migrating legacy code.

Choosing between Chat, Claude Cowork, and Claude Code by task

| If the task is... | Reach for | Why |
| --- | --- | --- |
| A question, a rewrite, a quick brainstorm | Chat | Fast, conversational, no setup |
| Research, analysis, or a finished document built from your files and systems | Claude Cowork | Folder access, connectors, skills, scheduled runs |
| Writing, testing, or shipping software | Claude Code | Codebase access, diffs, git, dev environments |

The three share the same Claude underneath; what changes is the workspace around it.

## Why Claude Cowork

For business leaders, the value of Claude Cowork shows up in four places.

### Speed

With Claude Cowork, work that took hours compresses into minutes. Call prep that took thirty minutes of digging through CRM notes, email threads, and call recordings takes two. A first-pass contract review that blocked a deal for a week happens the same afternoon. Now, employees can spend their time on work that requires judgment calls, strategy, and cross-functional creativity.

### Quality

Claude Cowork delivers finished deliverables, not drafts that need another pass: a financial model with formulas that tie, a competitive teardown with cited sources, a QBR narrative written the way your CRO expects to read it, or a customer response that sounds like your brand because it's grounded in your style guide and past replies. Because Cowork pulls directly from your systems of record—whether that's Google Drive, Excel, PowerPoint, Slack, Teams, or more—the numbers and names are straight from the source.

### Scale

When your best analyst's workflow lives in a skill rather than in her head, it stops being tribal knowledge and becomes organizational infrastructure. Claude Cowork allows organizations to tackle complex, multi-step tasks at scale, across teams. The playbook your top AE uses to prep for renewals, the checklist your senior counsel runs on every MSA, and the format your RevOps lead built for pipeline reviews become encoded in your organizational workflows, allowing every person on the team to work with the same context and processes. Consistency improves because everyone runs the same playbook, and the playbook itself compounds as the team refines it.

### Capacity for work you weren't doing

The more interesting effect of Claude Cowork is the work that wasn't happening at all because nobody had time to do it: the regulatory monitoring your legal team wanted to do across forty jurisdictions but couldn't staff, the per-account dashboards your sales managers wanted but couldn't get engineering cycles for, or the quarterly competitive sweep marketing always meant to run. This is where functional leads tend to see the biggest return—not doing the same work faster, but doing the work that mattered but was never a P0.

## Customizing Claude Cowork with plugins

Out of the box, Claude Cowork is a generalist. [Plugins (opens in new tab)](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork) are what turn it into a specialist for every function.

A plugin bundles three things:

* [Skills (opens in new tab)](https://agentskills.io/home) are encoded workflows (markdown files) that tell Claude how your team does something. A variance analysis skill knows which tables to query, what to compare against, and how your CFO likes the output formatted. A morning briefing skill knows to pull today's calendar, check your priority deals, and surface the three things that need attention before 9am. Skills can be invoked directly via slash commands or triggered automatically when Claude recognizes they're relevant.
* [Subagents (opens in new tab)](https://code.claude.com/docs/en/sub-agents) are autonomous workflows Claude runs end to end without you watching: an agent that monitors regulatory filings across jurisdictions and flags what's material to your business, or one that checks your book of accounts for untracked revenue every Friday.
* [Connectors (opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) are two-way integrations built on [MCP (opens in new tab)](https://modelcontextprotocol.io/docs/getting-started/intro) (Model Context Protocol, a universal standard for connecting AI applications to external data and tools) that let Claude read from and write to the systems your team already uses, including Salesforce, Slack, BigQuery, Docusign, Jira, Google Workspace, and a growing directory of others. Connectors respect your existing permissions; Claude sees what the user sees.

Plugins are file-based and written in markdown, which means they're portable, version-controllable, and editable by anyone who can write a how-to doc. You don't need an engineering team to build one. [Anthropic's own Legal plugin (opens in new tab)](https://www.youtube.com/watch?v=tJP6SKfo49c) was built by a product lawyer in an afternoon by pointing Claude at the team's existing memos, risk frameworks, and policy documents.

<!-- yt-inline:tJP6SKfo49c -->
[![How Anthropic uses Claude in Legal](https://img.youtube.com/vi/tJP6SKfo49c/hqdefault.jpg)](https://www.youtube.com/watch?v=tJP6SKfo49c)

<details>
<summary>자막: How Anthropic uses Claude in Legal (3:40)</summary>

[00:00]
This is
a legal lamp. That's what we call it.
And I was working on a project
to learn more about how Claude Code works.
And so I was trying to
think of a fun project that would sort of
make my desk come to life more.
And now I can type a message
and ask this lamp to blink in Morse code.
It says it's thinking it's going to do
four quick blinks and two quick blinks,
which is H. I.
Abracadabra.
It's kind of magical. I'm not an engineer.
I'm non-technical.
I don't know how to code.
But with Claude Code,
you don't have to know how to code.
And you can just kind of talk to it
in plain language. And.
No lawyer
likes doing the same repetitive exercise
over and over and over again.
The work can be dull.
You can make mistakes before Claude.
I had a ton of busywork.
Things I would put off
to the end of the day, because I just knew
it'd take a lot of time,
but not using the best parts of my brain.
So we put our heads together and realized
we might be able to use Claude to help

[00:01]
get our best work done and build
workflows.
It used to be that the marketing team
would reach out to me, maybe a day before
a launch and say, hey, we've got this
really exciting launch happening tomorrow.
We're so sorry.
The blog post just came together.
We need you to quickly read this and flag
anything that might be problematic.
So, I asked,
Claude wants to just build me a workflow.
Here's what I care about.
And to my surprise, Claude
just ran with it and set it up.
If I were a marketer and I needed to get
one of my blog posts reviewed,
I would open up this link
to the Marketing Materials Software
review tool,
which is pinned in my channel.
I would cut and paste.
So let me copy their blog post.
I'm going to go back to the review tool.
I'm going to paste all that content
and then I'm going to click
the Analyze Content button.
And this is going to send Claude off
on its journey reviewing my material.
There we have it.
Review results.
Claude is identified
five issues to address.
So it wants to make
sure I focus on accuracy.

[00:02]
It wants to review the security claims,
wants to make sure we have publicity
rights on third
party content,
as well as partnership considerations.
And it gave me props.
It said what looks good
clear the feature descriptions.
Comprehensive integration
details, specific use cases.
Here are the items that require
legal tickets.
Review.
I'm going to click on Generate
Slack message for legal team.
And Claude has now summarized the issues
here.
I'm going to click on Copy the Clipboard
and I'm going to click
go to Legal Tickets to file on my ticket.
To tee it up for legal review,
it identifies the most important issues.
It helps me prioritize.
Sort of has like a low, medium, high risk
level signal.
That's based on a framework
that I gave it.
So it's kind of acting as my eyes
and ears to that first pass.
As we build these types of automations
and in new workflows, I'm always trying
to ensure that a human remains in the loop
from the legal team.
We know that AI systems
can still hallucinate.
I'm still making sure
I'm reviewing the work.

[00:03]
But this is really helping us move
with more speed and sort
of preemptively flagging things
within the legal department.
We're using Claude
in so many different ways.
So we're using it to do redlining
exercises and commercial, matters.
We're using Claude to help us,
with our conflict of interest
policy and reviewing outside business
activity requests.
When people reach out to me and ask,
how do I get started?
I tell them to think of their most routine
work.
Just open up Claude and give it a shot.
You really don't know what it's capable of
doing until you give it a shot.

</details>
