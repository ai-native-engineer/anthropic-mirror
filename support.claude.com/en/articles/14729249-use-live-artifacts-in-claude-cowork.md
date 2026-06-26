<!-- source: https://support.claude.com/en/articles/14729249-use-live-artifacts-in-claude-cowork -->

# Use live artifacts in Claude Cowork

April 24, 2026

This article explains how to use live artifacts in **[Claude Cowork](https://claude.com/product/cowork)**—persistent, interactive HTML dashboards that Claude builds for you. Live artifacts refresh with current data from your connected apps and live in their own tab across tasks.

## Availability

Live artifacts are available on paid Claude plans (Pro, Max, Team, Enterprise) on:

* **Claude Desktop for macOS**
* **Claude Desktop for Windows**

Cowork requires the latest version of Claude Desktop. Download or update at **[claude.com/download](https://claude.com/download)**.

## What are live artifacts?

A live artifact is a persistent, interactive HTML page that Claude creates for you in Cowork —a tracker, a dashboard, a comparison tool, a reference—shaped around your specific work. Every live artifact you create is saved to the “Live artifacts” tab in Cowork, and you can reopen, refresh, and iterate on it from any future session.

Live artifacts differ from **[artifacts in chat](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)** in a few ways:

* **They live on their own.** You don’t have to find the chat they came from. Every live artifact shows up in the “Live artifacts” tab in your Cowork sidebar.
* **They refresh with current data.** When you open a live artifact, it can pull from your connected apps and local files so the view reflects today, not the day it was built.
* **They keep their history.** Each update saves a version. You can review how the artifact has evolved and restore an earlier version.

## Create a live artifact

There are two ways to create a live artifact in Cowork.

### From a Cowork task

Ask Claude to build what you need. A few examples:

* “Build me a dashboard that shows open tasks by project, pulling from Asana and Linear.”
* “Create a tracker that monitors my top five competitors — recent releases, blog posts, pricing changes.”
* “Put together a morning brief with my Slack mentions, today’s calendar, and open pull requests.”

When you describe the artifact, mention the connected apps or local files Claude should use. The result saves automatically to the “Live artifacts” tab.

### From the Live artifacts tab

1. Open Cowork on Claude Desktop and select “Live artifacts” from the sidebar.
2. Click “New artifact” in the top right.
3. Choose “Chat with Claude” to start a new conversation focused on building an artifact from scratch.

## Open and refresh an artifact

To reopen an artifact, select “Live artifacts” from the Cowork sidebar and click the one you want.

When you open a live artifact, it pulls fresh data from your connected apps. Most of the time you won’t need to refresh manually, as a short cache holds recent data so the artifact loads quickly, and it re-queries your connected apps on its own. If you want to force new data, use the refresh button in the artifact’s header.

## Version history

Each time you iterate on a live artifact with Claude, the previous version is saved. Open the artifact’s version history to:

* See how the artifact has changed over time.
* Compare an earlier version with the current one.
* Restore an earlier version if an update didn’t work out.

## Example use cases

* **Persistent team dashboard:** A weekly metrics view that pulls from your connected analytics tools and spreadsheets. Built once, refreshed every time you open it.
* **Working project tracker:** A tracker pulling from Linear, Slack, and your calendar. Close the session, open it next week — it’s refreshed with current data.
* **Competitive intelligence:** A dashboard that tracks what your top competitors are shipping. Built in one session, updated from any future thread.
* **Morning brief:** A single page with your Slack mentions, today’s calendar, and open pull requests. Open it each morning to see the current state.

## Current limitations

* **Local, not cloud.** Live artifacts live on your computer. If you switch devices, they don’t come with you.
* **Not shareable yet.** Live artifacts are for your own use at launch. Sharing is on the roadmap.
* **Live artifacts use your connectors without asking.** Live artifacts can only use the connectors you approved during creation or update. However, unlike normal sessions, artifacts don't ask for permission before using connectors. Use care when creating live artifacts that use connectors that can make changes to your data.

[Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)[Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)[Assign tasks from anywhere in Claude Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)[Organize your tasks with projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)[Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)
