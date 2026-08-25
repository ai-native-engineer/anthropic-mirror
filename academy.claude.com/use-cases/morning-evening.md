<!-- source: https://academy.claude.com/use-cases/morning-evening -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Daily bookends

A briefing to start the day and a wrap to close it.

10 minClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-xxhorrny.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-kkbwysr5.png)

## Set up

### Try a plugin

The Productivity plugin ships with `/start` and `/update` as a starting point, already structured to read your calendar and channels and rank what matters. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Productivity6 skills for inbox sweeps, daily rundowns, meeting prep, and decision logs

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=productivity)

`/start`Read calendar, inbox, and channels and write a one-page start-of-day briefing

[Run](claude://cowork/new?q=%2Fstart)

`/update`Log what landed, what slipped, and queue tomorrow's opener

[Run](claude://cowork/new?q=%2Fupdate)

Show all 4 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/edf4ec9c7c18805c.svg)

Google Calendar

[Connect](https://claude.ai/desktop/directory/google-calendar-calendarmcp)

![](images/b6bf6491858dcff4.svg)

Slack

[Connect](https://claude.ai/desktop/directory/slack)

![](images/f37dc3507c90f690.svg)'%3e%3cpath%20d='M11.9091%2034H16.3636V23.6969L10%2019.1515V32.1818C10%2033.1879%2010.8559%2034%2011.9091%2034Z'%20fill='%234285F4'/%3e%3cpath%20d='M31.6364%2034H36.0909C37.1473%2034%2038%2033.1848%2038%2032.1818V19.1515L31.6364%2023.6969'%20fill='%2334A853'/%3e%3cpath%20d='M31.6364%2015.8182V23.6969L38%2019.1515V16.7272C38%2014.4788%2035.305%2013.1969%2033.4182%2014.5454'%20fill='%23FBBC04'/%3e%3cpath%20d='M16.3636%2023.697V15.8182L24%2021.2727L31.6364%2015.8182V23.697L24%2029.1515'%20fill='%23EA4335'/%3e%3cpath%20d='M10%2016.7272V19.1515L16.3636%2023.6969V15.8182L14.5818%2014.5454C12.6918%2013.1969%2010%2014.4788%2010%2016.7272Z'%20fill='%23C5221F'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_4766_38693'%3e%3crect%20width='28'%20height='20'%20fill='white'%20transform='translate(10%2014)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e)

Gmail

[Connect](https://claude.ai/desktop/directory/gmail-gmailmcp)

![](images/3cb5db332ced9f49.svg)

Microsoft 365

[Connect](https://claude.ai/desktop/directory/microsoft-365)

![](images/d9bcb0bb9b2b1fff.svg)

Linear

[Connect](https://claude.ai/desktop/directory/linear)

![](images/ea7c24639ab8053c.svg)

Notion

[Connect](https://claude.ai/desktop/directory/notion)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Create a `Daily` folder and point Cowork at it. Each morning briefing and evening wrap writes there as `YYYY-MM-DD.md`, so the evening run reads what the morning run set out to do, and Monday's briefing can look back over last week. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your priorities, mute list, and tone stay attached.

Daily

2026-04-28.mdApr 28, 20263 KB

2026-04-27.mdApr 27, 20264 KB

priorities.mdApr 20, 20261 KB

In Cowork’s chat bar:Daily

## The prompt

### Copy this into Claude Cowork

Run my morning briefing. Tell me what's on fire, what's due, who's waiting on me, and the three things I should do first. Keep it under a page. Tonight I'll ask you to run /update and you'll write the wrap: what got done, what slipped, and what tomorrow opens with.

DailyOpen in Cowork

### Why this works

Prompt

**Name the sections you want.** On fire, due, waiting on me, top three: a fixed shape you can scan in thirty seconds.

Prompt

**Set a length limit.** A briefing you'll actually read, not another inbox.

Prompt

**Connect each run to the next.** The wrap feeds tomorrow's briefing, so carry-over never drops.

Source

**Let prior runs supply the context.** Each run reads yesterday's file, so context compounds without you re-explaining.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /start skill with my feedback.

DailyOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it at 8am and 6pm

The briefing should be waiting when you sit down. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skills run on their own at the start and end of every workday.

**/schedule** Run /start every weekday at 8:00am and /update every weekday at 6:00pm, both writing to Daily/<today>.md.

DailyOpen in Cowork

Scheduled taskActive

Daily bookends

Runs `/start` at 8am and `/update` at 6pm against Calendar, Slack, and Gmail and appends both to today's file in Daily.

Every **weekday at 8:00am and 6:00pm**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/start` and `/update` now carry your channel list, your priority rules, and your tone. Share them so anyone on your team starts and ends the day with the same one-page rhythm, and nobody's asking "what did I miss" in standup.

Share the skill

In Cowork, open **Skills** → `/start` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your buckets and mute list baked in, so they don't repeat Steps 1-3.

## What changes for your day

You have a one-page briefing ready each morning and an end-of-day record of what got done and what carries over. Open items continue from one day's file to the next without you tracking them.

You did this for the daily briefing. The same approach covers a weekly look-ahead, pre-meeting briefs, and project status checks — each one becomes a skill in your team's shared set.

[Next: Prep call look-ahead](https://academy.claude.com/use-cases/week-ahead-prep)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for your day](#what-changes-for-your-day)
