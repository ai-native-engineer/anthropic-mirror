<!-- source: https://academy.claude.com/tutorials/using-claude-cowork-for-marketing-ops-review -->

Loading

**Watch the full workflow in the video, then follow the steps below to set it up yourself.**

**In the video** — Ian, who works in marketing ops, runs his weekly metrics review: a detailed doc for the team and a one-slide summary for leadership. A skill he wrote does the gathering, a scheduled task runs it without him, and he steers the narrative on Monday morning.



If you haven’t set up Cowork yet, start with [Get started in three steps(opens in new tab)](https://academy.claude.com/tutorials/get-started-in-claude-cowork-in-three-steps), then [Customize Cowork(opens in new tab)](https://academy.claude.com/tutorials/customize-claude-cowork) for connectors and skills.

To dive deeper into Claude Cowork, take the full [Intro to Claude Cowork course(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-cowork).

## Step 1: Build the prep skill

Set up once

The report is the last thing Claude writes in the video. Before that comes the gathering: the same information is scattered across your email, calendar, and project tracker, and every week Claude pulls it together into a rough first draft for you to review and finish in Cowork.

That information gathering process is the same every week, no matter what the report says. So you build it into a prep skill once. The prep skill tells Claude what data to pull, where to find it, and how to lay out the starting draft.

**To set it up:**

1. Start a new task in Cowork.
2. Describe your weekly report — the data sources, the format, and the questions a reader would ask of it.
3. Ask Claude to write it as a skill.
4. Run it once on a real week, read the file, and add anything it missed.

To start now, open Cowork and describe the report you want to prepare — Claude writes the skill as a plain-text file you can open from `Customize → Skills` to read or change any time:

Help me build a skill that prepares my [weekly metrics review]. Walk me through what to pull, where to find it, what the draft should look like, and when to pause and ask — then write it as a skill.

Working folderOpen in Cowork

## Step 2: Schedule the prep run

Set up once

Now put the prep skill you built in step 1 on a schedule, so it runs on its own and the data is ready when you start.

There are two ways to create it: type `/schedule` in any task, or open `Scheduled` in the sidebar and add a new one.

Here’s the prompt to set it up — replace the blanks with your own:

/schedule Every [Sunday around 5pm], run the prep step of [your weekly review skill]. Read last week's review, pull the data from [your warehouse], and write a starting draft to [your working folder].

Working folderOpen in Cowork

## Step 3: Run the weekly review

Every week

The scheduled task from step 2 already ran the prep: the data is pulled together into a doc in a folder you chose on your desktop, a starting draft is written, and Claude has named a few possible focus areas.

Ask *"How did the prep go?"* and Claude walks you through what it pulled and what it couldn’t resolve. From there it’s a short back-and-forth to continue building the full report:

* **Pick the focus:** from what it found, Claude offers a few candidates for the report’s focus. Which one fits this week is your call.
* **Answer what it flags:** a good prep skill asks for clarification instead of guessing. In the video the segment structure changed, so Claude raises one question before it continues.
* **Approve the outline, then expand:** check the metrics table and main points first. Once they read right, tell Claude to expand, and it fills in the detail without changing what you approved.

From there, you can tell Claude to turn the weekly review into any format you need, or finish the work in your other tools:

* **Any format:** the finalized doc, a one-slide summary for leadership, or whatever cut you need
* **Finished in your tools:** the summary message posted to your team’s channel, the follow-ups created as tasks in your tracker

Anything that sends or shares waits for your yes.



Where your judgment applies

Claude pulls the numbers, but the call is yours: the focus, what the review says, what goes out. Weighing that is what the AI Fluency framework calls **discernment** — applying your own judgment to what Claude produced.

More on the habit: [The 4 Ds of AI Fluency(opens in new tab)](https://academy.claude.com/tutorials/the-4-ds-of-ai-fluency-behavioral-indicators), or [the Framework and Foundations course(opens in new tab)](https://academy.claude.com/courses/ai-fluency-framework-foundations)

## Step 4: Save what you learned into the skill

Every week

Running the review, you made corrections — a number fixed, a table simplified, a section redirected — and each one is something the skill can learn from. The skill is your process written down, so before you close Cowork, ask Claude to fold those corrections back in:

**Ask Claude before you close Cowork:** *"What did we learn this week that should go into the skill for next week?"*

Claude reads back through the work you just did, names what you changed and why, and writes it into the skill. Next week the prep already knows your preferences, your format, and your sources — you don’t re-instruct it on the same things.

Because a skill is a plain-text file in a folder, you can share it. Anyone on the team can run the same review and pick up the same improvements.

## Make it yours

This workflow fits any recurring report where the prep is the same every cycle:

* **Sales pipeline review** — pipeline by stage, slipped deals, weekly delta
* **Financial close** — variance to plan, open items, the explainers
* **Product metrics rollup** — usage by segment, feature adoption, what changed
* **Board prep** — the same numbers, one altitude up

**The setup is the same every time:**

1. Start a task in Cowork and describe the report — what it covers, where the data comes from, what the format looks like, when Claude should pause and ask.
2. Add a prep mode the scheduled task can run on its own — pull the numbers, write a starting draft, stop.
3. Schedule it for earlier in your workday, while your computer is on.
4. Keep read-only tools always allowed; anything that sends or changes data waits for you.

When you arrive, the data is there and the candidates are named. The focus call is still yours.

## Learn more

* [Claude Cowork 101(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-cowork). The full Cowork course to go deeper into the product.
* [Customize Cowork(opens in new tab)](https://academy.claude.com/tutorials/customize-claude-cowork). How to set up connectors, skills, and instructions.
* [AI Fluency: Framework and Foundations(opens in new tab)](https://academy.claude.com/courses/ai-fluency-framework-foundations). The full AI fluency course for effective, efficient, and ethical AI use.
* [The 4 Ds of AI Fluency(opens in new tab)](https://academy.claude.com/tutorials/the-4-ds-of-ai-fluency-behavioral-indicators). The practical skills and mental models behind building AI fluency.
* [Use Cowork safely(opens in new tab)](https://support.claude.com/en/articles/13364135-use-cowork-safely). Access, approvals, and what Claude can see.
