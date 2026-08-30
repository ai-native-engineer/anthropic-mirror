<!-- source: https://academy.claude.com/use-cases/quickly-prep-for-your-week -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Quickly prep for your week

Prepare and prioritize for your upcoming week through connecting your calendar and mail platforms.

15 minClaude.ai

Try in ClaudeCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-hteb4ys0.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-n0jyfw6m.png)

![Quickly prep for your week result](https://academy.claude.com/assets/v1/quickly-prep-for-your-week-holgruap.png)

## 1. Describe the task[](#1-describe-the-task)

Planning your week typically means opening your calendar, scanning your inbox, maybe checking a few documents—then trying to mentally synthesize which meetings need prep, what's urgent, and how to distribute your time. Claude can read through your calendar and inbox simultaneously, identify connections you'd miss while context-switching between tools, and create a structured overview showing what needs attention and when you actually have time to handle it.

To start, tell Claude which dates to analyze, where to search, and what the format for the output document.

Help me plan my upcoming week: October 27-31.

Using my M365 connector look at my Outlook calendar and find all meetings that need prep, or where I'm making decisions. Show me where I'm overbooked, where I have real focus time, and any scheduling problems I need to fix now.

From my Outlook inbox and summarize any weekend emails I need to handle, any threads from last week that become urgent this week if ignored, and anyone blocked waiting for my response.

Create an overview document of my must-dos, daily structure, preparation I still need to do, blocks of time I need for deep work, and email triage of high-priority vs can-wait.

Open in Claude

## 2. Give Claude context[](#2-give-claude-context)

To help Claude analyze your week effectively, give Claude access to your workspaces. Use the [Microsoft 365 connector(opens in new tab)](https://www.anthropic.com/news/productivity-platforms) to give Claude access to your Outlook calendar, email, SharePoint documents, OneDrive files, and Teams conversations.

### Required context[](#required-context)

In [Settings > Connectors(opens in new tab)](https://claude.ai/customize/connectors), you'll find the [Microsoft 365 connector(opens in new tab)](https://www.anthropic.com/news/productivity-platforms).

Claude can then search across your connected tools simultaneously—identifying which meetings need prep, what's urgent in your inbox, and how your schedule and communications relate to each other.

![](images/3cb5db332ced9f49.svg)

Microsoft 365

[Connect](https://claude.ai/directory/microsoft-365)

Browse all connectors[Open in Claude](https://claude.ai/customize/connectors)

## 3. What Claude creates[](#3-what-claude-creates)

Claude reads your sources simultaneously, analyzing what matters, and showing you how to prepare for the week ahead.

Done! I've searched your calendar and found **10 events** through October 21-25:

Monday 10/21:

* Engineering Sync - 10:00 AM to 10:30 AM (30 minutes)
  + Notes: No prep needed
* Marketing Planning - 2:00 PM to 3:00 PM (60 minutes)

Tuesday 10/22:

* Product Strategy - 11:00 AM to 12:30 PM (90 minutes)
  + Notes: Q4 resource allocation, 12-page pre-read unread
* VP Check-in - 3:00 PM to 3:30 PM (30 minutes)

Wednesday 10/23:

* Board Meeting - 9:00 AM to 11:00 AM (2 hours)
  + Notes: Presenting budget section
* Customer Success - 1:00 PM to 1:45 PM (45 minutes)
  + Notes: Can reschedule if needed

Thursday 10/24:

* Design Review - 10:00 AM to 10:30 AM (30 minutes)
* Finance Sync - 3:00 PM to 3:30 PM (30 minutes)

Friday 10/25:

* Retro + One-on-ones - 9:00 AM to 1:00 PM (4 hours)

Calendar shows 65% booked. Reality: 85% with prep time. Monday 11 AM-12:30 PM is your only 90-minute focus block before Wednesday's board meeting.

**Your Emails:**

Found 11 emails requiring action:

* Urgent (respond today): Sarah Chen: budget data - sent Fri 4:47 PM, 2 follow-ups, blocking Q4 forecast, Legal: contract signature - Tuesday deadline, IT: software access - 2 weeks old, likely blocking someone
* High priority (this week): Engineering roadmap comments - Tuesday meeting agenda depends on this, CFO Q3 numbers - needs tonight for Wed board presentation, Design team: rebrand timeline - before Thu meeting, Customer Success: expansion deal - time-sensitive
* Medium priority (batch Thursday): 8 threads - industry updates, partnership intros

3 threads become urgent by Wednesday if you don't handle them Monday.

**Week Analysis:**

Critical gap: Board presentation Wed 9 AM, zero prep time Tuesday. Board deck (47 slides) sent Friday evening, unreviewed.

Fix this: Block Tuesday 7-9 PM for review, OR arrive Wed 7 AM. Don't wing it.

Thursday is your only real focus day: 4+ hours unstructured time. First substantial block all week. Protect this for Q4 plan draft and batch email processing.

**Action Items Right Now:**

1. Block Tuesday 7-9 PM or Wed 7 AM for board prep
2. Respond to Sarah Chen
3. Open Marcus's product strategy doc
4. Protect Thursday from new meetings

**View your formatted document**

## 4. Follow up prompts[](#4-follow-up-prompts)

Continue the conversation with Claude to refine, expand, or explore further.

### Draft out urgent responses[](#draft-out-urgent-responses)

Ask Claude to write replies based on dashboard triage. Claude can identify urgent emails and draft replies based on the email thread and relevant documents. You can then easily copy these drafts to your inbox. Specify which emails to respond to and what each response should accomplish.

Draft three email responses: Reply to Finance (confirm I'll send the Q3 budget variance data by end of day Tuesday, apologize for delay). Reply to Legal (confirm vendor agreement will be signed and returned by Tuesday 3 PM). Reply to IT (approve contractor access request for the staging environment, apologize for 4-day response delay).

Open in Claude

### Create meeting prep materials[](#create-meeting-prep-materials)

After seeing which meetings need prep, Claude can search email threads, SharePoint documents, and OneDrive files to gather relevant background. It pulls context from where your work actually lives rather than you hunting through each system.

For my Thursday board meeting, search my emails and documents for budget discussions, Q3 performance data, and board questions sent ahead. Create a one-page brief: decisions they expect, questions raised in advance, key numbers needed, topics requiring more input.

Open in Claude

### Adjust the output to your needs[](#adjust-the-output-to-your-needs)

Claude can quickly restructure the format of your document. If you want it more compact, more detailed, or different styling, Claude adjusts to match how you actually work.

Refine the output to have tighter spacing so more content fits on one page. Change the font and use Arial instead of Times New Roman. For each meeting, add who's attending and their email address.

Open in Claude

## 5. Tricks, tips, and troubleshooting[](#5-tricks-tips-and-troubleshooting)

### Use your [organization's search project(opens in new tab)](https://support.claude.com/en/articles/12489464-using-enterprise-search) for company-wide information[](#use-your-organizations-search-project-for-company-wide-information)

When you connect tools like calendar and email individually, Claude searches only your personal files and messages. If you need information from across your organization—team documents in SharePoint, company-wide Slack channels, other people's shared files—look for a project in your sidebar named "Ask [Your Company Name]". This is a separate project your admin sets up that connects to company-wide sources, not just your individual accounts. When you use that project, Claude searches across all the tools your organization has connected: everyone's shared documents, team channels, company knowledge bases.

### Be specific about timeframes and priorities[](#be-specific-about-timeframes-and-priorities)

Claude searches more effectively when you provide clear parameters. "Plan my week" searches all meetings and emails. "Plan my week, focusing on client meetings and budget proposal items" tells Claude exactly which calendar entries and email threads to prioritize.

### Create a variety of outputs.[](#create-a-variety-of-outputs)

Beyond creating a Word document, Claude can save your weekly plan as a spreadsheet, add it to your Notion workspace, or send it as a Slack message to yourself. The file is convenient for reference, but if you want your plan living in the tools you use daily, enable those [connectors(opens in new tab)](https://claude.ai/customize/connectors) and ask Claude to output there instead.

### Turn this workflow into a Skill[](#turn-this-workflow-into-a-skill)

Once you've refined this workflow, create and save it as a [Skill(opens in new tab)](https://www.anthropic.com/news/skills) so Claude can automatically complete the task in any chat. Skills teach Claude how to complete a task the same way you do, searching through the right sources, including the right information and styling, and saving it in the correct format. Learn more about how to [create a custom skill using Claude.(opens in new tab)](https://support.claude.com/en/articles/12599426-how-to-create-a-skill-with-claude-through-conversation)

## 6. Ready to try for yourself?[](#6-ready-to-try-for-yourself)

Connect Claude to your Microsoft 365 workspaces and prepare for the week ahead. Claude can search your calendar, email and other tools to show what needs attention and when you have time to handle it.

Help me plan my upcoming week: October 27-31.

Using my M365 connector look at my Outlook calendar and find all meetings that need prep, or where I'm making decisions. Show me where I'm overbooked, where I have real focus time, and any scheduling problems I need to fix now.

From my Outlook inbox and summarize any weekend emails I need to handle, any threads from last week that become urgent this week if ignored, and anyone blocked waiting for my response.

Create an overview document of my must-dos, daily structure, preparation I still need to do, blocks of time I need for deep work, and email triage of high-priority vs can-wait.

Try in Claude

* [1. Describe the task](#1-describe-the-task)
* [2. Give Claude context](#2-give-claude-context)
* [3. What Claude creates](#3-what-claude-creates)
* [4. Follow up prompts](#4-follow-up-prompts)
* [5. Tricks, tips, and troubleshooting](#5-tricks-tips-and-troubleshooting)
* [6. Ready to try for yourself?](#6-ready-to-try-for-yourself)
