<!-- source: https://academy.claude.com/courses/introduction-to-claude-cowork/getting-set-up -->

Lesson 2 of 14 · Introduction to Claude CoworkSetting up Claude Cowork

## Install Cowork

You can run Cowork in the Claude desktop app on Mac and Windows, or in the cloud (in beta, on eligible plans) from the web and the Claude mobile app. This lesson walks through setup on the desktop, where Claude works directly with your local files. If you don't have the app yet, install it from [claude.com/download(opens in new tab)](https://claude.com/download), open it, sign in, and choose Cowork. If Cowork isn't visible, you may need a paid plan or a more recent version of the desktop app. The Help Center's [Get started with Claude Cowork(opens in new tab)](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) article walks through setup step by step.

## Pointing Claude at a folder

Click **Work in a project or folder** in the prompt bar and pick a folder on your computer. This is the single most important setup choice you'll make for each new task, because the folder is where the work lives. Claude reads every file inside (Word docs, Excel files, PDFs, PowerPoints, whatever's there) and saves finished outputs back to the same location.

Choose a folder that's scoped to one project or stream of work. Claude doesn't need access to your entire documents folder, just the one that includes the files it needs for the task. See the interactive below for an example.

Loading

**The folder is where Cowork has read AND write access.** It can open your files, edit them, create new ones, and organize them. This is the main difference from Chat: In Chat, Claude can read what you upload but can't save anything back to your computer — in Cowork, Claude can.

**Pick a real folder with the right context.** Cowork works best when the folder has the context for what you're doing — the source materials, the relevant documents, the templates.

**Cloud-based files behave differently.** What a cloud connector lets Claude do varies. Many — like the default Google Drive and M365 connectors — are read-and-search only. Others can also create or edit. To confirm what your connectors can do, check each connector's description when you enable it. Your working folder is where Claude edits your files directly, so that's where documents get built and revised. A session in the cloud reaches your connectors, not the folders on your computer, so start file work from the desktop when the files live on your machine.

## Adding connectors

Connectors are how Claude reaches into the apps where your work already happens — your email, your calendar, your team messaging tool, your CRM, your cloud storage. You set them up once in the **Customize** area and then you can toggle off/on the connectors you need for each task.

Connectors most people set up first:

* **Email and calendar** (Outlook via M365 or Gmail) — for pulling context out of meetings, drafting follow-ups, finding past threads
* **Messaging** (Slack or Teams via M365) — for searching channel history and synthesizing what your team has said
* **Cloud storage** (SharePoint or OneDrive via Microsoft 365, Google Drive, Box) — for accessing documents that don't live on your local machine
* **CRM and project tools** — Notion, HubSpot, Asana, Linear, and others, depending on what your team uses and where your real data lives

Once a connector is on, you reference it naturally in your prompts. "Check what the team said in Slack about the launch" or "find the customer follow-up email from last quarter" — Claude knows where to look.

Try this interactive below to see the power of connecting Claude to your work.

Loading

A note for tools that don't have a connector: for internal dashboards, vendor portals, or web apps behind a login, **Claude in Chrome** is the bridge. It's a browser extension that lets Claude read and interact with pages directly. We'll cover it in Module 3 — for now, just know that "no connector" doesn't mean that the data is out of reach. (Note that Claude in Chrome may not be available on some enterprise plans.)

## The permissions model

When you pick a folder, you're automatically authorizing Claude to read and write in it. When it comes to the tasks inside that folder, Cowork has two permission modes. In the default — “Ask before acting” — Claude pauses for your okay before each action that touches the outside world: sending an email, posting a message, sharing a file. In “Act without asking,” it doesn't pause for those, so only switch to it for tools and tasks you trust. One thing is constant in both modes: Claude always asks before permanently deleting a file, and that prompt can't be skipped.

Loading

The point of all of this: you can hand Claude a substantial piece of work, knowing it won't take an action that surprises you. That's what "delegating, not just chatting" actually feels like — and it only works because the permissions model is doing real work in the background.

## Try it now

The best way to understand this is to do it. Delegate one small task before you move on — both to confirm your setup works and to feel what Cowork is like.

**Step 1 — Pick a folder with real work in it.** Point Claude at an actual project: a client account, a deliverable you're in the middle of, a folder you'd be working in this week anyway. If you'd rather not point Claude at the live folder just yet, copy the contents into a new folder and use that. Just make sure to use real material, not toy files. Cowork is only as useful as the context it has, and the goal here is to feel that.

**Step 2 — Connect one app.** Start with the one where most of your work context lives. For many users, email and cloud storage (e.g. Google Drive, Box, M365) are the highest-value first connectors.

**Step 3 — Ask Claude to summarize the contents of the folder.** Something like:

Take a look at everything in this folder and write me a brief on what you've learned — what's in the folder, how the documents relate to one another, any surprising insights, or other information you think would be pertinent to share.



Open in Cowork

**Step 4 — Read the brief and check it against your own knowledge.** What did Claude catch that you might have missed? What did it miss or get wrong? What surprised you?

## What’s next

In the next lesson, you'll learn how to recognize the work in your day-to-day that is best suited for Cowork — the patterns to look for, and how to map your own workflows to them. By the end of it you'll have a specific task picked out and ready to delegate.
