<!-- source: https://claude.com/resources/use-cases/source-insights-from-your-tools-to-build-a-deck -->

Professional

Extended Thinking

Browser Use

# Source insights from your tools to build a deck

Claude Opus 4.6 chases leads across scattered sources, surfaces what no single source shows on its own, and builds a presentation around the through-line.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Professional
* Model

  Opus 4.6
* Features

  Extended Thinking

  Browser Use
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/source-insights-from-your-tools-to-build-a-deck

1

## Describe the task

Opus 4.6 follows leads across your connected tools without needing direction at each step. Give it a starting point and it pulls search terms from what it finds, follows people to their updates, follows updates to the data they reference, and reconciles sources that disagree. By the time it builds the deck, it's working from evidence it gathered and cross-referenced itself.

Once the deck exists, [Claude in PowerPoint](https://claude.com/claude-for-powerpoint) lets you keep refining directly in your slides — restructuring sections, adjusting talking points, or adding charts.

*I’m prepping for board meeting Friday. Q3 was the quarter where everything happened at once: we shipped the platform consolidation, closed the Apex partnership, and lost two enterprise accounts.*

*Start with the Q3 project tracker in my local files — it has the key people, channels, and documents. Follow each person across their channels, emails, and documents they reference. When you find data, check it against other sources — the revenue numbers probably don’t agree. Figure out which is current.*

*The board needs to understand whether the consolidation bet is paying off despite the churn. Create a PowerPoint deck (12–15 slides) with speaker notes, an Excel data appendix, and a two-page Word brief. Make an argument, not a summary.*

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

Through Cowork in [Claude Desktop](https://claude.com/download) [Research Preview], connect your local files and tools. Point Claude at a Slack channel, a Drive folder, or an email thread to give it a starting point.

Connect Slack and Google Drive through connectors. [Claude in Chrome](https://claude.com/resources/tutorials/simplify-your-browsing-experience-with-claude-for-chrome) [beta] grabs current data from live dashboards.

[Extended Thinking](https://support.anthropic.com/en/articles/11145627-what-is-extended-thinking-and-how-do-i-use-it) lets Opus 4.6 scale its reasoning to match the complexity of the task — more sources and more conflicting data means deeper thinking before it starts building.

## Required context

* Cowork with access to local files ([supported formats](https://claude.com/download))
* At least one connected source: Slack, Google Drive, or email
* Adaptive Thinking: ON

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690a5eb066fb294c24a6fb96_slack.svg)

Slack

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68efe41a8723b1875b5dfcbd_gmail.svg)

Gmail

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690a5f5599435352d469eb6d_google-icon.svg)

G Suite

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

## Optional context

* [Extended Thinking](https://support.anthropic.com/en/articles/11145627-what-is-extended-thinking-and-how-do-i-use-it) lets Opus 4.6 scale its reasoning to match the complexity of the task — more sources and more conflicting data means deeper thinking before it starts building.
* [Claude in Chrome](https://claude.com/resources/tutorials/simplify-your-browsing-experience-with-claude-for-chrome) (for live dashboard data from analytics or revenue platforms)
* Previous quarter’s board deck (for continuity and comparison)

Extended Thinking

3

## What Claude creates

Opus 4.6 works outward from the starting point you give it, pulls context from each source it finds, and saves three files locally: a presentation with narrative structure, a supporting data appendix, and an executive pre-read. If Claude in Chrome is connected, Claude opens relevant pages in new browser tabs to pull live data from dashboards and analytics platforms directly.

From Claude

Here’s what I found and how I pieced it together:

I started in #platform-consolidation on Slack. The kickoff thread from July identified the core team: @maria (engineering), @james (partnerships), and @priya (customer success). From there:

* @maria’s weekly updates in #engineering-updates gave me the velocity metrics and the 22% cost reduction from consolidation.
* @james’s messages in #partnerships led me to the Apex term sheet in your local files and the close date (September 28).
* @priya flagged the two enterprise losses in #customer-success. I found the full churn details in a CSV on your desktop and the related email thread where both customers cited migration friction.
* The finance team’s Q3 report on Drive shows $4.2M revenue, but I pulled the Looker dashboard via Chrome and it shows $4.6M — the difference is the Apex revenue that closed after the report was finalized. I used $4.6M and noted the discrepancy in the appendix.
* Current NPS from Delighted (via Chrome): 47, down from 52 last quarter. The drop tracks with the two enterprise losses.

**The quarter’s argument in one sentence:** The platform consolidation cut engineering costs 22% and landed the Apex partnership, but migration friction cost you two enterprise accounts — and the retention data shows that’s a fixable execution problem, not a product problem.

I’ve saved three files:

1. **Q3 Board Presentation** (q3-board-deck.pptx): 14 slides with speaker notes and anticipated board questions.
2. **Data Appendix** (q3-data-appendix.xlsx): Six tabs covering revenue reconciliation, customer retention, NPS trends, engineering velocity, pipeline, and Apex partnership economics.
3. **Executive Brief** (q3-executive-brief.docx): Two-page pre-read framing the consolidation bet and what the churn data actually shows.

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Turn the deck into an interactive board briefing

Static slides work in the room. An interactive version lets board members explore the data on their own time.

*Take the board deck and build an interactive HTML briefing I can share as a link. Each section should have the narrative up top with expandable charts underneath — let them click into the revenue reconciliation, the NPS trend, the churn timeline. Make the Apex partnership economics explorable so they can adjust assumptions.*

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Pre-brief each board member on what matters to them

Opus 4.6 already knows the quarter’s full context. Use that to draft targeted pre-reads before the meeting.

*Draft a Slack message for each board member based on what they’ll care about most. The CFO gets the revenue reconciliation and Apex economics. The product lead gets the consolidation impact and engineering velocity. The customer advocate gets the churn story and the NPS data. Personalize each one — don’t just cut the same deck three ways.*

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Stress-test the narrative before you present it

The hardest board questions come from the data you glossed over. Opus 4.6 has read every source and knows where the weak points are.

*You’ve seen all the raw data. Play devil’s advocate — what are the three toughest questions the board could ask about this quarter, and where is our narrative weakest? Then update the speaker notes with how to handle each one, citing specific data points from the appendix.*

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Point Opus 4.6 at a starting resource and tell it to follow what it finds

Opus 4.6 can pull search terms from what it reads, so a document that names people, channels, and files gives it more threads to follow across your tools. A project tracker or kickoff doc works well. Once you have the tools you'd like Claude to access, tell it to work outward: "Follow each person across their channels, emails, and documents they reference. Check data against other sources." Paired with Cowork, it sustains that work across as many steps as the task requires.

### Keep refining in PowerPoint

Once Claude has finished the task, the output files save to your working folder through Cowork. Open the deck in PowerPoint and use [Claude in PowerPoint](https://claude.com/claude-for-powerpoint) to make pinpoint edits, restructure slides, or add charts. Ask Claude to update the appendix or brief to match.

### Build a plugin for recurring presentations

If your team builds quarterly decks with a consistent structure, you can package that process as a Cowork plugin. A plugin teaches Claude your specific framework: which sources to check, which metrics the board expects, how to structure the argument, and what format the deliverables should follow.

### Start another task while this one runs

Cross-source research and deck building runs across many steps. Open a new session from the sidebar for other work. You'll see a grey dot in the sidebar when this one needs attention.

## Ready to try for yourself?

Point Opus 4.6 at your quarter.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698446deb44156e33889f4f8_Screenshot%202026-02-04%20at%2011.29.30%E2%80%AFPM.png)

Open artifact in new window

[Open artifact in new window](#)Open artifact in new window

## Related use cases

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

[Process batches of vendors with Cowork](/resources/use-cases/process-batches-of-vendors-with-cowork)Process batches of vendors with Cowork

Process batches of vendors with Cowork

Use case

[Use case](/resources/use-cases/process-batches-of-vendors-with-cowork)Use case
