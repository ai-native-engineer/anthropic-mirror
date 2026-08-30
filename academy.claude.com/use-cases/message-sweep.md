<!-- source: https://academy.claude.com/use-cases/message-sweep -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Slack and Teams message sweep

A topic-grouped sweep of your important channels.

10 minClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-jabaz0im.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-nbrkrt31.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Productivity plugin ships with `/start` and other personal-inbox skills as a starting point, already structured to read across apps and sort by urgency. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Productivity6 skills for inbox sweeps, daily rundowns, meeting prep, and decision logs

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=productivity)

`/start`Sweep unreads across Slack, Teams, and email and group by topic

[Run](claude://cowork/new?q=%2Fstart)

`/update`Turn a long thread into a one-paragraph summary with owners

[Run](claude://cowork/new?q=%2Fupdate)

Show all 4 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/b6bf6491858dcff4.svg)

Slack

[Connect](https://claude.ai/desktop/directory/slack)

![](images/3cb5db332ced9f49.svg)

Microsoft 365

Sweep Teams chats and Outlook threads so the daily roundup covers the Microsoft side too.

[Connect](https://claude.ai/desktop/directory/microsoft-365)

![](images/f37dc3507c90f690.svg)'%3e%3cpath%20d='M11.9091%2034H16.3636V23.6969L10%2019.1515V32.1818C10%2033.1879%2010.8559%2034%2011.9091%2034Z'%20fill='%234285F4'/%3e%3cpath%20d='M31.6364%2034H36.0909C37.1473%2034%2038%2033.1848%2038%2032.1818V19.1515L31.6364%2023.6969'%20fill='%2334A853'/%3e%3cpath%20d='M31.6364%2015.8182V23.6969L38%2019.1515V16.7272C38%2014.4788%2035.305%2013.1969%2033.4182%2014.5454'%20fill='%23FBBC04'/%3e%3cpath%20d='M16.3636%2023.697V15.8182L24%2021.2727L31.6364%2015.8182V23.697L24%2029.1515'%20fill='%23EA4335'/%3e%3cpath%20d='M10%2016.7272V19.1515L16.3636%2023.6969V15.8182L14.5818%2014.5454C12.6918%2013.1969%2010%2014.4788%2010%2016.7272Z'%20fill='%23C5221F'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_4766_38693'%3e%3crect%20width='28'%20height='20'%20fill='white'%20transform='translate(10%2014)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e)

Gmail

[Connect](https://claude.ai/desktop/directory/gmail-gmailmcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

This one runs almost entirely through connectors, so the working folder is light. Point Cowork at a notes folder if you want each day's sweep saved as a file you can search later; otherwise the sweep stays in the chat and the drafts stay in Slack and Teams. If you run it daily, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) so your channel list and reply preferences stay attached.

Notes / Inbox-Sweeps

sweep-2026-04-24.mdApr 24, 20263 KB

sweep-2026-04-23.mdApr 23, 20262 KB

In Cowork’s chat bar:Notes / Inbox-Sweeps

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Sweep my unread Slack DMs and mentions, Teams activity feed, and Gmail inbox from the last 24 hours. Group everything by topic, not by app. For each topic, tell me whether it needs a reply from me, needs reading, or is just FYI. Draft a reply for everything in the first bucket and keep each to three sentences or fewer.

Notes / Inbox-SweepsOpen in Cowork

### Why this works[](#why-this-works)

Prompt

**Say how to group the results.** The same conversation often spans a Slack thread, a Teams ping, and an email; "by topic, not by app" collapses them into one item so you reply once instead of three times.

Prompt

**Sort by the action needed.** Separating "needs a reply" from "needs me to read it" from "FYI" means the drafts only land where you'd actually type, and the rest is skimmable.

Prompt

**Set a length limit.** "Three sentences or fewer" keeps the replies in your voice for a quick edit-and-send rather than a paragraph you'd never write yourself.

Source

**Let the connected tools supply context.** Slack, Teams, and Gmail are read live through the connectors, so the sweep reflects what's actually sitting unread right now, not a stale export.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /start skill with my feedback.

NotesOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Run it every morning at 8am[](#run-it-every-morning-at-8am)

The sweep should be waiting before you open Slack. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs every weekday morning against your live connectors.

**/schedule** Run /start every weekday at 8:00am against Slack, Teams, and Gmail, and post the topic-grouped sweep with drafts to me as a Slack DM.

NotesOpen in Cowork

Scheduled taskActive

Morning message sweep

Runs `/start` across Slack, Teams, and Gmail and DMs you the topic-grouped list with reply drafts.

Every **weekday at 8:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/start` now carries your channel list, your priority senders, and your skip rules. Share it so teammates with the same channels get the same sorted morning, and new joiners inherit the watch-list on day one.

Share the skill

In Cowork, open **Skills** → `/start` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your channel list and skip rules baked in, so they don't repeat Steps 1-3.

## Going forward[](#going-forward)

### Now in your Cowork

Your processes

Productivity plugin

Your tools

![](images/b6bf6491858dcff4.svg)Slack![](images/3cb5db332ced9f49.svg)Microsoft Teams![](images/f37dc3507c90f690.svg)'%3e%3cpath%20d='M11.9091%2034H16.3636V23.6969L10%2019.1515V32.1818C10%2033.1879%2010.8559%2034%2011.9091%2034Z'%20fill='%234285F4'/%3e%3cpath%20d='M31.6364%2034H36.0909C37.1473%2034%2038%2033.1848%2038%2032.1818V19.1515L31.6364%2023.6969'%20fill='%2334A853'/%3e%3cpath%20d='M31.6364%2015.8182V23.6969L38%2019.1515V16.7272C38%2014.4788%2035.305%2013.1969%2033.4182%2014.5454'%20fill='%23FBBC04'/%3e%3cpath%20d='M16.3636%2023.697V15.8182L24%2021.2727L31.6364%2015.8182V23.697L24%2029.1515'%20fill='%23EA4335'/%3e%3cpath%20d='M10%2016.7272V19.1515L16.3636%2023.6969V15.8182L14.5818%2014.5454C12.6918%2013.1969%2010%2014.4788%2010%2016.7272Z'%20fill='%23C5221F'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_4766_38693'%3e%3crect%20width='28'%20height='20'%20fill='white'%20transform='translate(10%2014)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e)Gmail

Your workspace

Inbox-Sweeps

`/start` groups your unreads across Slack, Teams, and email by topic, with drafts ready for the messages that need a reply — one list to act on instead of three apps to check.

[Next: Prep call look-ahead](https://academy.claude.com/use-cases/week-ahead-prep)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
