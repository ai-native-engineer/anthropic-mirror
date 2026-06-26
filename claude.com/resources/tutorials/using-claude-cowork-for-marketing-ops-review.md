<!-- source: https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review -->

[](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)

  2. Using Claude Cowork for marketing ops: run a weekly review that preps itself

  * [Ask questions about this page](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)
  * [Copy as markdown](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)

# Using Claude Cowork for marketing ops: run a weekly review that preps itself
Claude Cowork runs the gathering for your weekly review on a schedule, so you’re not pulling the numbers and starting the draft by hand each week. Your time goes into what the review says.
Marketing
Claude Cowork
7
[Copy link](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)
https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0b69b56deb3e7a96d01504_Screenshot%202026-05-18%20at%2012.31.38%E2%80%AFPM.png)
###### Watch the full workflow in the video, then follow the steps below to set it up yourself.
**In the video** — Ian, who works in marketing ops, runs his weekly metrics review: a detailed doc for the team and a one-slide summary for leadership. A skill he wrote does the gathering, a scheduled task runs it without him, and he steers the narrative on Monday morning.
Follow along to set up
[1Build the prep skillSet up once](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#step-1-build-the-prep-skill)[2Schedule the prep runSet up once](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#step-2-schedule-the-prep-run)[3Run the weekly reviewEvery week](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#step-3-run-the-weekly-review)[4Save what you learned into the skillEvery week](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#step-4-save-what-you-learned-into-the-skill)
If you haven’t set up Cowork yet, start with [Get started in three steps](https://claude.com/resources/tutorials/get-started-in-claude-cowork-in-three-steps), then [Customize Cowork](https://claude.com/resources/tutorials/customize-claude-cowork) for connectors and skills.
To dive deeper into Claude Cowork, take the full [Intro to Claude Cowork course](https://anthropic.skilljar.com/introduction-to-claude-cowork).
Set up once
##  Step 1: Build the prep skill
The report is the last thing Claude writes in the video. Before that comes the gathering: the same information is scattered across your email, calendar, and project tracker, and every week Claude pulls it together into a rough first draft for you to review and finish in Cowork.
That information gathering process is the same every week, no matter what the report says. So you build it into a prep skill once. The prep skill tells Claude what data to pull, where to find it, and how to lay out the starting draft.
To set it up:
  1. 1Start a new task in Cowork.
  2. 2Describe your weekly report — the data sources, the format, and the questions a reader would ask of it.
  3. 3Ask Claude to write it as a skill.
  4. 4Run it once on a real week, read the file, and add anything it missed.

To start now, open Cowork and describe the report you want to prepare — Claude writes the skill as a plain-text file you can open from Customize → Skills to read or change any time:
Help me build a skill that prepares my weekly metrics review. Walk me through what to pull, where to find it, what the draft should look like, and when to pause and ask — then write it as a skill.
Copy prompt [ Open in Cowork ](claude://cowork/new?q=)
Working folder
Ask
Set up once
##  Step 2: Schedule the prep run
Now put the prep skill you built in step 1 on a schedule, so it runs on its own and the data is ready when you start.
There are two ways to create it: type /schedule in any task, or open Scheduled in the sidebar and add a new one.
Here’s the prompt to set it up — replace the blanks with your own:
/schedule Every Sunday around 5pm, run the prep step of your weekly review skill. Read last week's review, pull the data from your warehouse, and write a starting draft to your working folder.
Copy prompt [ Open in Cowork ](claude://cowork/new?q=)
Working folder
Ask
Every week
##  Step 3: Run the weekly review
The scheduled task from step 2 already ran the prep: the data is pulled together into a doc in a folder you chose on your desktop, a starting draft is written, and Claude has named a few possible focus areas.
Ask _"How did the prep go?"_ and Claude walks you through what it pulled and what it couldn’t resolve. From there it’s a short back-and-forth to continue building the full report:
  * **Pick the focus:** from what it found, Claude offers a few candidates for the report’s focus. Which one fits this week is your call.
  * **Answer what it flags:** a good prep skill asks for clarification instead of guessing. In the video the segment structure changed, so Claude raises one question before it continues.
  * **Approve the outline, then expand:** check the metrics table and main points first. Once they read right, tell Claude to expand, and it fills in the detail without changing what you approved.

From there, you can tell Claude to turn the weekly review into any format you need, or finish the work in your other tools:
  * **Any format:** the finalized doc, a one-slide summary for leadership, or whatever cut you need
  * **Finished in your tools:** the summary message posted to your team’s channel, the follow-ups created as tasks in your tracker

Anything that sends or shares waits for your yes.
Claude pulls the numbers, but the call is yours: the focus, what the review says, what goes out. Weighing that is what the AI Fluency framework calls **discernment** — applying your own judgment to what Claude produced.
More on the habit: [The 4 Ds of AI Fluency](https://claude.com/resources/tutorials/the-4-ds-of-ai-fluency-behavioral-indicators), or [the Framework and Foundations course](https://anthropic.skilljar.com/ai-fluency-framework-foundations)
Every week
##  Step 4: Save what you learned into the skill
Running the review, you made corrections — a number fixed, a table simplified, a section redirected — and each one is something the skill can learn from. The skill is your process written down, so before you close Cowork, ask Claude to fold those corrections back in:
**Ask Claude before you close Cowork:** _"What did we learn this week that should go into the skill for next week?"_
Claude reads back through the work you just did, names what you changed and why, and writes it into the skill. Next week the prep already knows your preferences, your format, and your sources — you don’t re-instruct it on the same things.
Because a skill is a plain-text file in a folder, you can share it. Anyone on the team can run the same review and pick up the same improvements.
This workflow fits any recurring report where the prep is the same every cycle:
  * **Sales pipeline review** — pipeline by stage, slipped deals, weekly delta
  * **Financial close** — variance to plan, open items, the explainers
  * **Product metrics rollup** — usage by segment, feature adoption, what changed
  * **Board prep** — the same numbers, one altitude up

The setup is the same every time:
  1. 1Start a task in Cowork and describe the report — what it covers, where the data comes from, what the format looks like, when Claude should pause and ask.
  2. 2Add a prep mode the scheduled task can run on its own — pull the numbers, write a starting draft, stop.
  3. 3Schedule it for earlier in your workday, while your computer is on.
  4. 4Keep read-only tools always allowed; anything that sends or changes data waits for you.

When you arrive, the data is there and the candidates are named. The focus call is still yours.
  * [Claude Cowork 101](https://anthropic.skilljar.com/introduction-to-claude-cowork). The full Cowork course to go deeper into the product.
  * [Customize Cowork](https://claude.com/resources/tutorials/customize-claude-cowork). How to set up connectors, skills, and instructions.
  * [AI Fluency: Framework and Foundations](https://anthropic.skilljar.com/ai-fluency-framework-foundations). The full AI fluency course for effective, efficient, and ethical AI use.
  * [The 4 Ds of AI Fluency](https://claude.com/resources/tutorials/the-4-ds-of-ai-fluency-behavioral-indicators). The practical skills and mental models behind building AI fluency.
  * [Use Cowork safely](https://support.claude.com/en/articles/13364135-use-cowork-safely). Access, approvals, and what Claude can see.

  * [Step 1: Build the prep skill](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#step-1-build-the-prep-skill)
  * [Step 2: Schedule the prep run](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#step-2-schedule-the-prep-run)
  * [Step 3: Run the weekly review](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#step-3-run-the-weekly-review)
  * [Step 4: Save what you learned into the skill](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#step-4-save-what-you-learned-into-the-skill)
  * [Make it yours](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#make-it-yours)
  * [Learn more](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#learn-more)

[Using Claude Design for prototypes and UX](https://claude.com/resources/tutorials/using-claude-design-for-prototypes-and-ux)Using Claude Design for prototypes and UX
Using Claude Design for prototypes and UX
[Tutorial](https://claude.com/resources/tutorials/using-claude-design-for-prototypes-and-ux)Tutorial
[Using Claude Design for presentations and slide decks](https://claude.com/resources/tutorials/using-claude-design-for-presentations-and-slide-decks)Using Claude Design for presentations and slide decks
Using Claude Design for presentations and slide decks
[Tutorial](https://claude.com/resources/tutorials/using-claude-design-for-presentations-and-slide-decks)Tutorial
[Claude for Marketing](https://claude.com/resources/tutorials/claude-for-marketing)Claude for Marketing
Claude for Marketing
[Tutorial](https://claude.com/resources/tutorials/claude-for-marketing)Tutorial
[Next](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)Next
[Button Text](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)Button Text
[Button Text](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)Button Text
[Button Text](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)Button Text
[](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)
  
[](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)
  
[](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)
  

[](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)
  
[](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)
  
[](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)
  

[](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)
  
[](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)
  
[](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)
  

[](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)
[](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)
  
[](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review#)

[English (US)](https://claude.com/resources/tutorials/using-claude-cowork-for-marketing-ops-review)
