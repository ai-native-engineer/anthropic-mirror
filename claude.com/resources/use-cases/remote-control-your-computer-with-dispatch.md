<!-- source: https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch -->

[](https://claude.com/resources/use-cases-category/cowork)
Cowork
[](https://claude.com/use-cases-features/cowork)
Cowork
[](https://claude.com/use-cases-features/connectors)
Connectors
  * [Login](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2/login)

[Try Claude](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2)Try Claude
[Try Claude](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2)Try Claude

[](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
[Try Claude](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2)Try Claude
[Try Claude](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2)Try Claude

  * [Login](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2/login)

[Try Claude](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2)Try Claude
[Try Claude](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2)Try Claude

  2. Remote control your computer with Dispatch

  * [Ask questions about this page](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
  * [Copy as markdown](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)

# Remote control your computer with Dispatch
Use Dispatch in Claude Cowork to send instructions from your phone. Claude runs the task on your computer — reading files, pulling data, searching the web — and the result is waiting when you sit down.
Cowork
Cowork
Connectors
[Copy link](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
https://claude.com/resources/use-case/remote-control-your-computer-with-dispatch

Dispatch turns your phone into a remote control for Claude on your computer. You send a message from the Claude mobile app, and Claude runs the task on your machine — reading local files, pulling data through [connectors](https://claude.com/connectors), searching the web, and compiling results. When you get back to your desk, the work is done and waiting.
The key requirement: your computer needs to be awake and running the Claude desktop app. The [keep-awake](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork#keep-awake) toggle in [Dispatch settings](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork) prevents your computer from sleeping while you are away. Turn that on before you leave.
Dispatch works best when you give Claude a prompt with complete instruction upfront — what to read, where to look, and what format you want back. On your computer, Claude can read files, pull from Google Drive, check [Gmail](https://claude.com/connectors/gmail), and search the web. This can all occur locally until you ask Claude to send them.
Here, one message from your phone turns a local spreadsheet and a set of web searches into a finished competitive landscape report, saved to Google Drive before you sit down.
_I need a competitive landscape summary for our Q2 planning meeting. Start with the spreadsheet at in my Sales folder - I think it’s called competitor-tracker.xlsx — that has our current list of competitors and their pricing.  
For each competitor listed there, search the web for any product launches, pricing changes, or funding announcements from the last 90 days.   
Put together a report with one section per competitor: what they have changed since our last update, how their pricing compares to the figures in the spreadsheet, and anything we should flag for the planning meeting. Save the report as a Google Doc in my Strategy folder on Drive._
[Next](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)Next
[Ask Claude](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)Ask Claude
Claude reads the local spreadsheet on your computer and uses web search to gather recent competitor information. The [Google Drive connector](https://claude.com/connectors/google-drive) saves the finished report directly to your Drive.
These connectors give Claude the access needed to complete the task:
  * Google Drive — to save the finished report as a Google Doc in your Strategy folder.
  * Local files — to read the competitor tracking spreadsheet from your Documents folder.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68efe427f3a0ebdeb2c3a468_google_drive.svg)
Google Drive
![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)
![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)
![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)
These connectors are not required but can add useful context:
  * Gmail — Claude can check recent emails for competitor mentions or forwarded articles your team has shared.[‍](https://claude.com/connectors/google-calendar)
  * [Google Calendar](https://claude.com/connectors/google-calendar) — Claude can confirm the date of the Q2 planning meeting and note the deadline in the report.

Claude reads the spreadsheet, searches for recent news on each competitor, and produces a structured report. Here is an example of what Claude sends back to your phone when the work is finished:
I read **competitor-tracker.xlsx** and found 6 competitors listed. I searched for recent activity on each one. Here is a summary — the full report is saved as Q2 Competitive Landscape in your Strategy folder on Google Drive.
**Competitor A — Prismatic**
  * Raised a $40M Series C on February 12, 2026. Their blog post mentions expanding into enterprise integrations.
  * Pricing unchanged from the spreadsheet ($49/seat/mo for Pro). No public changes since January.  
  

  * **Flag:** The new funding and enterprise push puts them closer to our mid-market segment.   
  
**Competitor B — Conduit Labs**
  * Launched a new API management tier on March 3, 2026.
  * Pricing increased: the Growth plan moved from $29/seat/mo to $39/seat/mo. The spreadsheet still shows the old price.
  * **Flag:** Their price increase narrows the gap with our Standard plan ($45/seat/mo). Could be a positioning advantage for us.   
  
**Competitor C — Stackline**
  * No major announcements in the last 90 days. Last press mention was a December 2025 partnership with Datadog.
  * Pricing matches the spreadsheet ($99/seat/mo Enterprise only).
  * **Flag:** None. Stable quarter.   
  
**Competitors D–F:** Runo, Pipeshift, and Arcway had no pricing changes or notable announcements. Full details are in the Google Doc.

The report includes a comparison table with current pricing for all 6 competitors alongside our plans. Let me know if you want me to add anything before the planning meeting.
### Make this a recurring Monday report
Any Dispatch task can become a [scheduled task](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork) that runs on a cadence. Instead of remembering to send this prompt each week, set it once and Claude runs it automatically.
**_/Schedule_** _Run this every Monday morning so the report is ready when I sit down._
[Next](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)Next
[Ask Claude](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)Ask Claude
### Review the report at your desk
After Dispatch finishes a task on your computer, you can pick up the work on your laptop. The report is already saved — now open it on your desktop to review, edit, and finalize.
_I'm back at my desk now. Open the report so I can review and edit it._
[Next](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)Next
[Ask Claude](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)Ask Claude
### Share key findings on Slack
Claude can route output to connected tools like [Slack](https://claude.com/connectors/slack), Gmail, or Google Drive. Once the report is done, send the highlights to your team without copying and pasting.
_Post a summary of the key findings to #strategy on Slack._
[Next](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)Next
[Ask Claude](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)Ask Claude
### Turn on keep-awake before stepping away
The keep-awake toggle in Dispatch settings prevents your computer from sleeping so Claude can finish tasks while you are gone. It does not keep the screen on — just the machine. Turn it on before you leave your desk.
### Set connector permissions deliberately
For connectors like Slack and Gmail, set read access to always-allow and send access to [needs-approval](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities). This lets Claude gather information freely but check with you before posting or emailing on your behalf.
### Include the file path when you know it
Claude can search for files by name, but including the path (like ~/Documents/Sales/competitor-tracker.xlsx) saves time and avoids ambiguity when multiple files have similar names.
### Scheduled tasks keep your reports fresh
Once you have a prompt that works, save it as a scheduled task to run weekly or monthly. Claude runs the same instructions on the latest data, so the report stays current without you re-typing the request.
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69de735c9e466c972b821bf9_Screenshot%202026-04-14%20at%2010.03.17%E2%80%AFAM.png)
[Open artifact in new window](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)Open artifact in new window
[Audit a folder of visual assets against your guidelines](https://claude.com/resources/use-cases/audit-a-folder-of-visual-assets-against-your-guidelines)Audit a folder of visual assets against your guidelines
Audit a folder of visual assets against your guidelines
[Use case](https://claude.com/resources/use-cases/audit-a-folder-of-visual-assets-against-your-guidelines)Use case
[Adapt a standard textbook page to every reading level](https://claude.com/resources/use-cases/adapt-a-standard-textbook-page-to-every-reading-level)Adapt a standard textbook page to every reading level
Adapt a standard textbook page to every reading level
[Use case](https://claude.com/resources/use-cases/adapt-a-standard-textbook-page-to-every-reading-level)Use case
[Handle a request while away from your keyboard](https://claude.com/resources/use-cases/handle-a-request-while-away-from-your-keyboard)Handle a request while away from your keyboard
Handle a request while away from your keyboard
[Use case](https://claude.com/resources/use-cases/handle-a-request-while-away-from-your-keyboard)Use case
[Kick off long-running computer tasks from the Claude mobile app](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app)Kick off long-running computer tasks from the Claude mobile app
Kick off long-running computer tasks from the Claude mobile app
[Use case](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app)Use case
[Next](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)Next
[Button Text](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)Button Text
[Button Text](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)Button Text
[Button Text](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)Button Text
[](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
  
[](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
  
[](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
  

[](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
  
[](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
  
[](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
  

[](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
  
[](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
  
[](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
  

[](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
[](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)
  
[](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch#)

[Log in](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2/login)Log in

[English (US)](https://claude.com/resources/use-cases/remote-control-your-computer-with-dispatch)
