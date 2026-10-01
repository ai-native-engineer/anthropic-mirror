<!-- https://anthropic.skilljar.com/introduction-to-claude-cowork/444167 -->

### ⁠

## What you'll learn

*Estimated time: 16 minutes*

By the end of this lesson you'll be able to:

* Set global instructions so Claude starts every session already knowing how you work
* Decide when a piece of work belongs in a project
* Choose between the three ways to start a project

## Onboard your new collaborator

Claude remembers things from your conversations on its own, and that memory applies in Cowork tasks too. The context that reliably carries from task to task, though, is the context you set up deliberately: **global instructions**, which apply to every Cowork session, and **projects**, where Claude builds memory automatically from the conversations you have inside them. Most people start with global instructions and add projects as recurring work surfaces.

## Global instructions: the brief that applies to every session

Global instructions are a standing brief. You write them once, in Settings, and Claude will reference them during every session — every chat, every scheduled task.

To set them up:

1. Open **Settings** in Claude and find **Global instructions** (called **Instructions for Claude** in some versions of the app).
2. Write your brief and save.

What to put in it: who you are and what you do; the shorthand and acronyms you use (so Claude doesn't have to ask what "the QBR deck" is); and how you like output delivered (format, length, tone, etc.). The interactive below shows a few worked examples based on different roles.

Your global instructions don't need to be complete on day one. As you work with Cowork more, you'll notice corrections you keep giving (*"share the bottom line up front in your responses"* or *"don't use Oxford commas"*) — those are global-instruction candidates.

## Projects: a scoped workspace for a stream of work

Global instructions cover *you*. Projects cover *what you're working on*.

A project is a workspace tied to a specific stream of work — a customer, a recurring deliverable, a launch. Inside the project are three things you can set up and one that Claude builds for you:

* **Instructions** — like global instructions, but scoped to this project. ("This project is for our weekly transformation team meetings. The purpose is to gather data from across the organization and distill it into a slide deck each week.")
* **Scheduled tasks** — recurring runs you've set up that belong to the project: the Friday status pull, the pre-meeting brief, the end-of-month rollup. You set these up from a conversation inside the project, and they run with the project's context every time.
* **Context** — one or more folders or links Claude should work from. Every conversation in the project has access to them.
* **Memory** — what Claude learns from the conversations you have inside the project. This builds up over time as you work; you don't write it.

That last one is the difference projects make. Outside of a project, each session starts fresh apart from your global instructions. Inside one, every conversation adds to what Claude knows — so the next task opens with the client's situation, last week's decisions, and what's still open already in hand.

Review the examples below to get a sense for the makeup of a Cowork project.

Some streams of work that are good for a project:

* **A client or account.** The folder of meeting notes and deliverables, and the standing instructions for the account. Every meeting prep, follow-up, and review draft happens inside the project, and Claude picks up the relationship as it goes.
* **A recurring deliverable.** The monthly report, the quarterly review, the weekly leadership update. Each new cycle is a new conversation inside the same project that automatically builds on the insights from the last time.
* **A launch or initiative.** The redesign, the migration, the new program rollout. Briefs, decisions, status updates — the whole thread of the work in one place until it ships.

## Three ways to start a project

There are three ways to create a project, depending on where the materials already live:

* **From scratch** — start empty, add instructions and context as you go.
* **From an existing folder on your computer** — point the project at a folder you already work out of. The folder becomes the project's working directory.
* **From an existing project** — if you've already built up a project in your conversations with Claude, start from it so its instructions and knowledge carry over.

To create one, click **Projects** in the sidebar, then **New project**, and choose whichever option makes the setup easiest for you. You can change the working folder, instructions, and connectors at any time.

## Try it now

Put both layers in place — global instructions for you, and one project for a stream of work you're in right now.

1. **Write a first-pass global instructions block.** Don't overthink it — just start with a few sentences.

   A useful starter:

   I'm a [role] at [company], working on [main 1–2 streams of work]. Here are
   some common [acronyms/shorthand] you need to know. Most of my deliverables
   are [docs, decks, briefs, models — whatever]. I want updates and briefs
   concise — lead with the recommendation, keep background to one paragraph.
   I like to review the .md previews before creating the final document file.
2. **Create a project for one stream of work.** Pick something recurring — a customer account, a monthly deliverable, a current initiative. Point it at the folder where the materials already live, or start fresh if there isn't one yet.

## What’s next

In the next lesson, you'll meet skills — how to teach Claude the processes you and your team rely on, so the way you do specialized work happens automatically.

<!-- embed: https://academy.claude.com/embed/courses/introduction-to-claude-cowork/ContextGlobalInstructions -->

Explorer: switches between three role-based examples of a global-instructions brief, showing how each sample text and the default behaviors it produces teach what details belong in standing Claude instructions.

Global instructions

Instructions for Claude

Claude will keep these in mind across chats and Cowork within Anthropic’s guidelines. Learn more

I lead product for a 200-person B2B SaaS company in late-stage growth.
My team ships PRDs, launch briefs, and quarterly roadmaps.
Default to crisp, decision-oriented writing — lead with the user problem before the solution.
When citing a metric, name the source doc.
Always flag assumptions I should pressure-test before sharing.

What this gets you

Defaults to PRD and brief formats without you specifying.

Leads with the user problem before the solution.

Cites the source doc for any metric.

<!-- embed: https://academy.claude.com/embed/courses/introduction-to-claude-cowork/ContextProjectSetups -->

Explorer: toggle between three example Cowork project setups—a customer account, a recurring deliverable, and a launch—to see how instructions, scheduled tasks, context, and memory shift for each kind of work.

Three workstreams, three project setups

### Northwind — account

Instructions

Formal tone. Address the EB by name (Sarah Chen, VP Ops). Always end with “draft for review.”

Scheduled

* Mon 8amPull weekend Northwind activity from CRM and draft a 3-line account update
* Renewal −30 daysDraft the renewal-prep brief

Context

On your computer

Clients/Northwind/

QBR-prep/

Memory

Memory

eb-prefs-sarah-chen.md

renewal-march-15.md

qbr-price-sensitivity.md

Links

Salesforce / Northwind account

Notion / Northwind customer profile

A project for **one customer account** — one folder, one EB, one set of guardrails. Cowork stops asking “who’s this for?” every time.
