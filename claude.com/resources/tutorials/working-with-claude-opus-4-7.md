<!-- source: https://claude.com/resources/tutorials/working-with-claude-opus-4-7 -->

[](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)

  2. Working with Claude Opus 4.7

  * [Ask questions about this page](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)
  * [Copy as markdown](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)

# Working with Claude Opus 4.7
A practical guide to the newest version of Claude's most capable generally available model class 
Professional
Claude.ai
[Copy link](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)
https://claude.com/resources/tutorials/working-with-claude-opus-4-7

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a038f7a9aecb959a25c7496_Screenshot%202026-05-12%20at%201.37.11%E2%80%AFPM.png)
Claude Opus 4.7 is the model to reach for when the work is substantial and worth getting right. Learn what it's best at, how it handles reasoning and effort, and when it's the right model for the job — with examples to follow along.
### 1. Follows instructions more closely
Models differ in how strictly they follow instructions or how ‘steerable’ they are. Opus 4.7 is likely to take your instructions more literally than Opus 4.6 did. This means you should think about what you need to emphasize or include within your prompt. 
**What this means for you:** Write your directions once and clearly. And re-read any instructions Claude already has from you, including [Project instructions](https://support.claude.com/en/articles/9517075-what-are-projects) or [scheduled task ](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)prompts. Certain instructions like "_be brief_ " or "_skip the obvious parts_ " may now be followed more precisely.
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69e0edafd880b074f652214f_f8707d65.png)
Opus 4.7 follows instructions more literally than earlier models. 
### 2. Reads images at full resolution
Opus 4.7 reads images at higher resolution than prior models, which means small details come through more clearly: chart labels, values in a busy table, fine print in a screenshot. This applies anywhere you give Claude an image: a claude.ai chat, a Cowork task, Claude in Chrome reading the page in front of you.
**What this means for you:** Opus 4.7 is the model to pick when the details in an image matter. It can more reliably read from images like a full dashboard, a scanned form, or a chart with small labels, catching details previous models may have missed.
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69e0edafd880b074f6522158_8c8a2e40.png)
Images are read at higher resolution. Small text — axis labels, table cells, footnotes — is legible without cropping or upscaling first.
### 3. Thinks through problems at the right depth
With Opus 4.6, [extended thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking) was a toggle you managed: turn it on for hard tasks, off for quick stuff. If you left it on, every question paid the thinking tax whether it needed to or not. Now, with Opus 4.7, extended thinking becomes [**adaptive thinking**](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking). This means that when the toggle is on, Claude makes the decision on how much to think per question. It answers simple things immediately and takes the time on hard ones.
**What this means for you:** You can leave Extended thinking on and stop managing it. Simple questions come back faster than they did on Opus 4.6 with thinking on; hard questions still get the depth. You get both without choosing.
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69e0edafd880b074f652215b_ee07d853.png)
With Extended thinking on, Opus 4.7 decides per question how much to think. Simple questions finish fast; harder ones get more time automatically.
### 4. Better at document and spreadsheet work
Opus 4.7 is stronger at producing and reviewing its own work on office tasks, so the files it returns are more complete and correct on the first pass. Whether it's redlining a Word doc, building a slide deck, or working through a spreadsheet, it's more likely to spot its own layout and formula mistakes before outputting the file. That cuts down the rounds of back-and-forth it takes to reach something usable.  

**What this means for you:** Choose Opus 4.7 when you're asking Claude to create office files. You'll get a draft you can open and continue working in rather than one you have to rebuild. This applies to file creation in claude.ai Chat and Cowork, and to Claude in Excel and Claude in PowerPoint.
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69e0edafd880b074f6522155_fc9f4454.png)
Office files — spreadsheets, docs, slides — come back more complete on the first pass.
### 5. More selective about searching the web and using connectors
Claude has tools it can use mid-task: web search for current information, files you've attached or put in a Project, and connectors like Google Drive and Slack. On any given question it decides whether to use them or to answer from what it already has.
Left to decide, Opus 4.7 reaches for those tools less often than 4.6 did. Unless you ask, it's more likely to answer from what it already has than to search or pull from a connector on its own.
**What this means for you:** Before you prompt, decide whether the answer needs a specific source. If it lives on the web or in your files and tools, name it in your prompt. If not, leave it out and Claude answers faster from what it already knows. Afterward, check in Claude's thinking what it drew from, and if it answered on its own where you needed something looked up or pulled from connected tool, follow up by pointing it to the right source.
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69e0edafd880b074f6522152_7f78b341.png)
If the answer should come from somewhere specific — Drive, Slack, the web — name it in the prompt. That makes the lookup intentional rather than Claude’s judgment call.
Opus 4.7 makes good use of the context you've already given Claude — so it's worth setting up once.
  * **On claude.ai** — turn on [Memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory), put ongoing work in a [Project](https://support.claude.com/en/articles/9517075-what-are-projects) with its source files and custom instructions, and add [connectors](https://support.claude.com/en/articles/11176164-use-connectors) plus [web search](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search) so Claude can pull from your tools when you ask.
  * In **Cowork** — point a [Project](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-cowork) at a real folder, set per-project instructions, and enable [connectors](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork), [browser access through Claude in Chrome](https://claude.com/resources/tutorials/simplify-your-browsing-experience-with-claude-for-chrome) so tasks can navigate your browser, and [scheduled tasks](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork) so recurring work can read from your sources and run on its own.
  * **Across devices** — install the [mobile app](https://claude.com/download) and use Dispatch to send work to Cowork when you're away from your desk → See how to [ Send work to Claude with Dispatch](https://claude.com/resources/tutorials/dispatch-in-claude-cowork).
  * In **Excel and PowerPoint** — install [Claude in Excel](https://claude.com/claude-for-excel) and [Claude in PowerPoint](https://claude.com/claude-for-powerpoint) to work directly inside your files.

  * [What Claude Opus 4.7 does well and how to use it](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#what-claude-opus-4-7-does-well-and-how-to-use-it)
  * [Set yourself up to get more from it](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#set-yourself-up-to-get-more-from-it)

[Tasks to try with @Claude in your workspace](https://claude.com/resources/tutorials/tasks-to-try-with-claude-tag-in-your-workspace)Tasks to try with @Claude in your workspace
Tasks to try with @Claude in your workspace
[Tutorial](https://claude.com/resources/tutorials/tasks-to-try-with-claude-tag-in-your-workspace)Tutorial
[Best practices for using @Claude](https://claude.com/resources/tutorials/best-practices-using-claude-tag)Best practices for using @Claude
Best practices for using @Claude
[Tutorial](https://claude.com/resources/tutorials/best-practices-using-claude-tag)Tutorial
[Using Claude Cowork for legal: answer fast questions on past decisions](https://claude.com/resources/tutorials/using-claude-cowork-for-legal-question-briefing)Using Claude Cowork for legal: answer fast questions on past decisions
Using Claude Cowork for legal: answer fast questions on past decisions
[Tutorial](https://claude.com/resources/tutorials/using-claude-cowork-for-legal-question-briefing)Tutorial
[Using Claude Cowork for marketing ops: run a weekly review that preps itself](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review)Using Claude Cowork for marketing ops: run a weekly review that preps itself
Using Claude Cowork for marketing ops: run a weekly review that preps itself
[Tutorial](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review)Tutorial
[Next](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)Next
[Button Text](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)Button Text
[Button Text](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)Button Text
[Button Text](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)Button Text
[](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)
  
[](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)
  
[](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)
  

[](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)
  
[](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)
  
[](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)
  

[](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)
  
[](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)
  
[](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)
  

[](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)
[](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)
  
[](https://claude.com/resources/tutorials/working-with-claude-opus-4-7#)

[English (US)](https://claude.com/resources/tutorials/working-with-claude-opus-4-7)
[日本語 (Japan)](https://claude.com/ja/resources/tutorials/working-with-claude-opus-4-7)
[Deutsch (Germany)](https://claude.com/de/resources/tutorials/working-with-claude-opus-4-7)
[Français (France)](https://claude.com/fr/resources/tutorials/working-with-claude-opus-4-7)
[한국어 (South Korea)](https://claude.com/ko/resources/tutorials/working-with-claude-opus-4-7)
