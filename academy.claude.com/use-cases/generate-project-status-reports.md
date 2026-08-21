<!-- source: https://academy.claude.com/use-cases/generate-project-status-reports -->

![Generate project status reports result](https://academy.claude.com/assets/v1/generate-project-status-reports-izl8gxwu.png)

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

Enable [connectors(opens in new tab)](https://claude.com/blog/connectors-directory) and [integrations(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) to give Claude direct access to your tools as live data sources, not just pasted snippets.

Once you’ve connected your [Google Drive(opens in new tab)](https://support.claude.com/en/articles/10166901-using-the-google-drive-integration), [Gmail, Google Calendar(opens in new tab)](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors), and [Slack(opens in new tab)](https://www.claude.com/claude-and-slack) tools, make sure they are toggled on in the chat bar settings.

Claude can then access your email threads, Drive file updates, calendar events, and Slack conversations to piece together what's actually happening with your project.

![](images/a3bfc5814bd6a3e2.svg)

Google Drive

[Connect](https://claude.ai/directory/google-drive-drivemcp)

![](images/f37dc3507c90f690.svg)'%3e%3cpath%20d='M11.9091%2034H16.3636V23.6969L10%2019.1515V32.1818C10%2033.1879%2010.8559%2034%2011.9091%2034Z'%20fill='%234285F4'/%3e%3cpath%20d='M31.6364%2034H36.0909C37.1473%2034%2038%2033.1848%2038%2032.1818V19.1515L31.6364%2023.6969'%20fill='%2334A853'/%3e%3cpath%20d='M31.6364%2015.8182V23.6969L38%2019.1515V16.7272C38%2014.4788%2035.305%2013.1969%2033.4182%2014.5454'%20fill='%23FBBC04'/%3e%3cpath%20d='M16.3636%2023.697V15.8182L24%2021.2727L31.6364%2015.8182V23.697L24%2029.1515'%20fill='%23EA4335'/%3e%3cpath%20d='M10%2016.7272V19.1515L16.3636%2023.6969V15.8182L14.5818%2014.5454C12.6918%2013.1969%2010%2014.4788%2010%2016.7272Z'%20fill='%23C5221F'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_4766_38693'%3e%3crect%20width='28'%20height='20'%20fill='white'%20transform='translate(10%2014)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e)

Gmail

[Connect](https://claude.ai/directory/gmail-gmailmcp)

Browse all connectors[Open in Claude](https://claude.ai/customize/connectors)

### Optional context

Use [Extended Thinking(opens in new tab)](https://support.claude.com/en/articles/10574485-using-extended-thinking) for better results when making Word, Excel, and PowerPoint files.

[

Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking)

Claude searches your connected tools, finds status updates from different sources, reconciles them into a single view, and creates an Excel tracker with visual indicators and context in cell comments.

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

### Deep dive blockers

Pull all related conversations about a blocker to understand the full context.

The tracker shows Lisa's been blocked on approval for 4 days. Find every mention of this blocker across Slack, email, and meeting notes. I need to see the complete escalation history and current status.

### Create weekly status report

Generate an executive summary from the tracker data.

Using the task tracker data, create a one-page status report for leadership. Include: overall progress percentage, number of blockers, which workstreams are at risk, and top 3 items that need executive attention.

### Create a Skill for recurring reports

Create a custom [skill(opens in new tab)](https://support.claude.com/en/articles/12512176-what-are-skills) for generating status reports to embed all the steps involved in the process. Once created, you can use the skill anywhere in Claude by referencing its name or description. This triggers Claude to run the workflow automatically.

### Specify how to handle missing information

If Claude can't find certain information—maybe there's no Slack discussion or Drive files haven't been updated—it's better to say "no progress documented" than to have gaps silently smoothed over. In your prompt, you can specify: "If you don't find information for a work stream, note that explicitly rather than omitting it."

### Add visual polish

Claude can opt for certain default fonts, colors, and styles. For differentiated outputs, you can request changes: "Choose a color scheme that's unique and aesthetically beautiful—avoid standard blues and grays," or "Select typography that feels modern and confident, not generic corporate." Specificity drives better design.

Work with Claude to consolidate information between your project tools so you can focus on making decisions instead of copy and pasting into documents.

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

Try in Claude
