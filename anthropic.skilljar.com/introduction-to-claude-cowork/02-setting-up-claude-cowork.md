<!-- https://anthropic.skilljar.com/introduction-to-claude-cowork/444165 -->

### ⁠

## What you'll learn

*Estimated time: 18 minutes*

By the end of this lesson you'll be able to:

* Give Claude a place to work: a folder on your computer in the desktop app, or a project
* Connect the apps where your work lives
* Recognize what Claude asks before doing — and what it doesn't — so you can hand off work with confidence

## Get set up

You can use Cowork in the Claude desktop app (Mac and Windows), on the web, or in the Claude mobile app. This lesson uses the desktop app, because that is where Claude can work directly with files on your computer. If you don't have it yet, install it from [claude.com/download](https://claude.com/download), open it, and sign in; you'll need a paid Claude plan. The Help Center's [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) article walks through setup step by step.

## Pointing Claude at a folder

Click **Work in a project or folder** in the prompt bar and pick a folder on your computer. This is the single most important setup choice you'll make for each new task, because the folder is where the work lives. Claude reads every file inside (Word docs, Excel files, PDFs, PowerPoints, whatever's there) and saves finished outputs back to the same location.

Choose a folder that's scoped to one project or stream of work. Claude doesn't need access to your entire documents folder, just the one that includes the files it needs for the task. See the interactive below for an example.

**The folder is where Cowork has read AND write access.** It can open your files, edit them, create new ones, and organize them. That's what makes a working folder different from attaching files to a message: Claude doesn't only read what's there, it saves finished work back to the same place.

**Pick a real folder with the right context.** Cowork works best when the folder has the context for what you're doing — the source materials, the relevant documents, the templates.

**Cloud-based files behave differently.** What a cloud connector lets Claude do varies. Many — like the default Google Drive and M365 connectors — are read-and-search only. Others can also create or edit. To confirm what your connectors can do, check each connector's description when you enable it. Your working folder is where Claude edits your files directly, so that's where documents get built and revised. When the files live on your computer, start the task from the desktop app; a task started from the web or your phone can reach your connectors but not your local folders.

## Adding connectors

Connectors are how Claude reaches into the apps where your work already happens — your email, your calendar, your team messaging tool, your CRM, your cloud storage. You set them up once in the **Customize** area and then you can toggle off/on the connectors you need for each task.

Connectors most people set up first:

* **Email and calendar** (Outlook via M365 or Gmail) — for pulling context out of meetings, drafting follow-ups, finding past threads
* **Messaging** (Slack or Teams via M365) — for searching channel history and synthesizing what your team has said
* **Cloud storage** (SharePoint or OneDrive via Microsoft 365, Google Drive, Box) — for accessing documents that don't live on your local machine
* **CRM and project tools** — Notion, HubSpot, Salesforce, Asana, Linear, and others, depending on what your team uses and where your real data lives

Once a connector is on, you reference it naturally in your prompts. "Check what the team said in Slack about the launch" or "find the customer follow-up email from last quarter" — Claude knows where to look.

Try this interactive below to see the power of connecting Claude to your work.

A note for tools that don't have a connector: for internal dashboards, vendor portals, or web apps behind a login, **Claude in Chrome** is the bridge. It's a browser extension that lets Claude read and interact with pages directly. We'll cover it in Module 3 — for now, just know that "no connector" doesn't mean that the data is out of reach. (Note that Claude in Chrome may not be available on some enterprise plans.)

## The permissions model

When you pick a folder, you're automatically authorizing Claude to read and write in it. When it comes to the tasks inside that folder, Cowork has two permission modes. In the default — “Ask before acting” — Claude pauses for your okay before each action that touches the outside world: sending an email, posting a message, sharing a file. In “Act without asking,” it doesn't pause for those, so only switch to it for tools and tasks you trust. One thing is constant in both modes: Claude always asks before permanently deleting a file, and that prompt can't be skipped.

The point of all of this: you can hand Claude a substantial piece of work, knowing it won't take an action that surprises you. That's what "delegating, not just chatting" actually feels like — and it only works because the permissions model is doing real work in the background.

## Try it now

The best way to understand this is to do it. Delegate one small task before you move on — both to confirm your setup works and to feel what Cowork is like.

**Step 1 — Pick a folder with real work in it.** Point Claude at an actual project: a client account, a deliverable you're in the middle of, a folder you'd be working in this week anyway. If you'd rather not point Claude at the live folder just yet, copy the contents into a new folder and use that. Just make sure to use real material, not toy files. Cowork is only as useful as the context it has, and the goal here is to feel that.

**Step 2 — Connect one app.** Start with the one where most of your work context lives. For many users, email and cloud storage (e.g. Google Drive, Box, M365) are the highest-value first connectors.

**Step 3 — Ask Claude to summarize the contents of the folder.** Something like:

Take a look at everything in this folder and write me a brief on what you've learned — what's in the folder, how the documents relate to one another, any surprising insights, or other information you think would be pertinent to share.

[Open in Cowork](claude://cowork/new?q=Take%20a%20look%20at%20everything%20in%20this%20folder%20and%20write%20me%20a%20brief%20on%20what%20you've%20learned%20%E2%80%94%20what's%20in%20the%20folder%2C%20how%20the%20documents%20relate%20to%20one%20another%2C%20any%20surprising%20insights%2C%20or%20other%20information%20you%20think%20would%20be%20pertinent%20to%20share.)

**Step 4 — Read the brief and check it against your own knowledge.** What did Claude catch that you might have missed? What did it miss or get wrong? What surprised you?

## What’s next

In the next lesson, you'll learn how to recognize the work in your day-to-day that is best suited for Cowork — the patterns to look for, and how to map your own workflows to them. By the end of it you'll have a specific task picked out and ready to delegate.

<!-- embed: https://academy.claude.com/embed/courses/introduction-to-claude-cowork/SetupFolderPicker -->

Exercise: the learner clicks through nested folders in a simulated file tree to choose where Claude Cowork should work for a sample writing task, seeing how many files and what content comes into scope at each level. It teaches picking the smallest folder that still holds everything the task needs.

You’re about to ask Cowork to write the **Q3 competitive memo**. Pick the folder it should work in.

Add folder for Cowork

Your computer

Click a folder to see what comes into scope.

**Pick the smallest folder that holds what the task needs.** You can always add another folder later if you need to give Cowork access to something outside it.

<!-- embed: https://academy.claude.com/embed/courses/introduction-to-claude-cowork/SetupConnectorToggles -->

Exercise: the learner toggles connectors like Gmail, Calendar, Slack, and Drive on or off and watches a panel show what Claude Cowork can reach and draft, teaching that connector access is task-scoped and shapes what gets done automatically versus manually.

Connectors

Try it

### Toggle the connectors Cowork can reach for this task.

Each task only uses the connectors you’ve toggled on. Flip them and watch what changes — both the reach and the kind of work Cowork can actually do.

Customize

Connectors for this task

**0** of 4 on

Gmail

Read mail, draft replies, find past threads

Google Calendar

See meetings, create or update events, pull context from invites

Slack

Search channels, summarize threads, send messages

Google Drive

Search documents, pull data, summarize folders

What Cowork can reach

0Nothing connected yet.

Cowork can still reason, but can’t access any of your tools.

Flip a connector and Cowork can pull from that source for this task.

Worked example

“Draft a Monday status update from this week’s Slack threads, the meetings on your calendar, open email threads, and the planning doc in Drive.”

With nothing connected, Cowork can still reason about what you upload or paste in — but it can’t see any of these sources.

Reach: none

<!-- embed: https://academy.claude.com/embed/courses/introduction-to-claude-cowork/SetupPermissionsModel -->

Diagram: Shows Claude Cowork's two permission modes, "Ask before acting" and "Act without asking," plus the always-on deletion safeguard and added controls over connectors and web access.

Permissions

The mode selector

### Cowork uses a mode selector for approvals.

Pick how Claude should handle approvals each task. A few guardrails apply regardless of the mode you choose.

Ask before acting

Claude pauses so you can approve each action.

Best for

New tools, unfamiliar files, or anything you want to watch closely.

Act without asking

Claude works without pausing for approval. Faster, but riskier.

Best for

When you’re actively supervising and working with trusted files and sites.

In both modes

Cowork always asks before permanently deleting files. No exceptions.

You also control

* **Connectors and MCPs** — which ones Claude can reach, and how often each one asks for permission.
* **Web access** — your org’s admin can turn web search off, and you can limit which sites Claude in Chrome can visit.

Assess how much you trust a connector or website before extending access beyond Claude’s default settings.
