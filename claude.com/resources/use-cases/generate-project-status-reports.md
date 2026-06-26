<!-- source: https://claude.com/resources/use-cases/generate-project-status-reports -->

Professional

Connectors

# Generate project status reports

Pull status updates from your emails, Slack channels, meeting notes, and project tools to create a tracker that shows who's working on what, what's blocked, and where things stand—all in one place.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Professional
* Model

  Sonnet 4.5
* Features

  Connectors
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/generate-project-status-reports

1

## Describe the task

Status reporting often means sifting through your various tools and messages to find updates and decisions. Claude simplifies this by querying multiple data sources at once, extracting information from different formats, and creating organized reports. This turns hours of manual work into minutes.

Ask Claude to pull information from your connected tools and create a tracker that consolidates everything. The key is being specific about what you need tracked and where to look.

I need to consolidate project status from multiple sources into a task tracker.

Pull information from:

* Gmail (past 2 weeks, search "Project Hermes")
* Slack #hermes-sprint channel
* Google Drive "Project Hermes" folder
* Recent calendar meetings

For each task, I need to see:

* Who owns it and what they're working on
* Current status (not started, in progress, blocked, done)
* Any blockers and how long they've been stuck
* Notes from their updates about plans and challenges

Create an Excel tracker and include these features: visual status indicators, cell comments with context from sources (so I can hover and see the details), dropdown menus for status and priority (to make updates easy), and data bars showing progress visually.   
  
The tracker should make it obvious at a glance where the problems are and who needs help.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

Enable [connectors](https://claude.com/blog/connectors-directory) and [integrations](https://support.claude.com/en/articles/10168395-setting-up-claude-integrations) to give Claude direct access to your tools as live data sources, not just pasted snippets.

## Required context

Once you’ve connected your [Google Drive](https://support.claude.com/en/articles/10166901-using-the-google-drive-integration), [Gmail, Google Calendar](https://support.claude.com/en/articles/11088742-using-the-gmail-and-google-calendar-integrations?q=googel+driv), and [Slack](https://www.claude.com/claude-and-slack) tools, make sure they are toggled on in the chat bar settings.   
  
Claude can then access your email threads, Drive file updates, calendar events, and Slack conversations to piece together what's actually happening with your project.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68efe427f3a0ebdeb2c3a468_google_drive.svg)

Google Drive

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68efe41a8723b1875b5dfcbd_gmail.svg)

Gmail

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

## Optional context

Use [Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking) for better results when making Word, Excel, and PowerPoint files.

Extended Thinking

3

## What Claude creates

Claude searches your connected tools, finds status updates from different sources, reconciles them into a single view, and creates an Excel tracker with visual indicators and context in cell comments.

From Claude

I've searched your connected tools for Project Hermes updates and created a consolidated tracker.

Found across your tools:

* 147 Gmail messages mentioning Project Hermes
* 312 Slack messages in #hermes-sprint
* 23 documents in Google Drive /Project Hermes folder
* 18 calendar meetings with "Hermes" in the title

Key insights from consolidation:

* Sarah said "80% done" in Slack but mentioned complexity in her 1-on-1 notes, so I adjusted to 45% in the tracker
* Mike's been blocked on API spec for 4 days (mentioned in Slack Nov 1, still blocked Nov 4)
* Lisa's approval escalated to VP Engineering (email thread shows 3 escalation attempts)
* Team consensus from standup: data migration is highest risk item
* I’ve created a spreadsheet file with 25 tasks, visual indicators, and cell comments with context from all sources.

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Deep dive blockers

Pull all related conversations about a blocker to understand the full context.

The tracker shows Lisa's been blocked on approval for 4 days. Find every mention of this blocker across Slack, email, and meeting notes. I need to see the complete escalation history and current status.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Create weekly status report

Generate an executive summary from the tracker data.

Using the task tracker data, create a one-page status report for leadership. Include: overall progress percentage, number of blockers, which workstreams are at risk, and top 3 items that need executive attention.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Create a Skill for recurring reports

Create a custom [skill](https://support.claude.com/en/articles/12512176-what-are-skills) for generating status reports to embed all the steps involved in the process. Once created, you can use the skill anywhere in Claude by referencing  its name or description. This triggers Claude to run the workflow automatically.

### Specify how to handle missing information

If Claude can't find certain information—maybe there's no Slack discussion or Drive files haven't been updated—it's better to say "no progress documented" than to have gaps silently smoothed over. In your prompt, you can specify: "If you don't find information for a work stream, note that explicitly rather than omitting it."

### Add visual polish

Claude can opt for certain default fonts, colors, and styles. For differentiated outputs, you can request changes: "Choose a color scheme that's unique and aesthetically beautiful—avoid standard blues and grays," or "Select typography that feels modern and confident, not generic corporate." Specificity drives better design.

## Ready to try for yourself?

Work with Claude to consolidate information between your project tools so you can focus on making decisions instead of copy and pasting into documents.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690a4d605ca4e2de836aac23_Screenshot%202025-11-04%20at%2011.00.43%E2%80%AFAM.png)

Open artifact in new window

[Open artifact in new window](#)Open artifact in new window

## Related use cases

[Source insights from your tools to build a deck](/resources/use-cases/source-insights-from-your-tools-to-build-a-deck)Source insights from your tools to build a deck

Source insights from your tools to build a deck

Use case

[Use case](/resources/use-cases/source-insights-from-your-tools-to-build-a-deck)Use case

[Evaluate a company from the science to the balance sheet](/resources/use-cases/evaluate-a-company-from-the-science-to-the-balance-sheet)Evaluate a company from the science to the balance sheet

Evaluate a company from the science to the balance sheet

Use case

[Use case](/resources/use-cases/evaluate-a-company-from-the-science-to-the-balance-sheet)Use case

[Build analysis from browser charts and folder data](/resources/use-cases/build-analysis-from-browser-charts-and-folder-data)Build analysis from browser charts and folder data

Build analysis from browser charts and folder data

Use case

[Use case](/resources/use-cases/build-analysis-from-browser-charts-and-folder-data)Use case

[Build a daily briefing across your tools](/resources/use-cases/build-a-daily-briefing-across-your-tools)Build a daily briefing across your tools

Build a daily briefing across your tools

Use case

[Use case](/resources/use-cases/build-a-daily-briefing-across-your-tools)Use case
