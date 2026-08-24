<!-- source: https://academy.claude.com/use-cases/eng-performance-reviews -->

Loading

## Set up

### Try a plugin

The Engineering plugin ships with `/code-review` as a starting point, already structured to gather a report's shipped work and frame it against a career ladder. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.



Engineering9 skills for postmortems, design docs, on-call handoffs, and cost reviews

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=engineering)

`/code-review`Gather a report's shipped work and draft the review against your career framework

[Run](claude://cowork/new?q=%2Fcode-review)

`/standup`Compile a report's PRs, reviews, and incidents into an evidence packet

[Run](claude://cowork/new?q=%2Fstandup)

Show all 10 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23181717'%20d='M12%20.3a12%2012%200%200%200-3.8%2023.39c.6.11.82-.26.82-.58v-2.03c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.33-1.76-1.33-1.76-1.09-.74.08-.73.08-.73%201.2.09%201.84%201.24%201.84%201.24%201.07%201.83%202.81%201.3%203.49%201%20.11-.78.42-1.31.76-1.61-2.67-.3-5.47-1.33-5.47-5.93%200-1.31.47-2.38%201.24-3.22-.13-.3-.54-1.52.11-3.18%200%200%201.01-.32%203.3%201.23a11.5%2011.5%200%200%201%206%200c2.29-1.55%203.3-1.23%203.3-1.23.65%201.66.24%202.88.12%203.18.77.84%201.23%201.91%201.23%203.22%200%204.61-2.8%205.63-5.48%205.92.43.37.81%201.1.81%202.22v3.29c0%20.32.22.7.82.58A12%2012%200%200%200%2012%20.3'/%3e%3c/svg%3e)

GitHub

Pull each report's merged PRs, reviews given, and incidents responded to over the period.

[Connect](https://claude.ai/desktop/directory/github)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.951%209.85a1.47%201.47%200%201%201-2.94%200%201.47%201.47%200%200%201%201.47-1.471h1.47V9.85Zm.735%200a1.47%201.47%200%201%201%202.94%200v3.679a1.47%201.47%200%201%201-2.94%200V9.85Z'%20fill='%23E01E5A'/%3e%3cpath%20d='M6.157%203.943a1.47%201.47%200%201%201%200-2.943%201.47%201.47%200%200%201%201.47%201.471v1.472h-1.47Zm0%20.746a1.47%201.47%200%201%201%200%202.943H2.47a1.47%201.47%200%201%201%200-2.943h3.687Z'%20fill='%2336C5F0'/%3e%3cpath%20d='M12.049%206.16a1.47%201.47%200%201%201%202.94%200%201.47%201.47%200%200%201-1.47%201.472h-1.47V6.16Zm-.736%200a1.47%201.47%200%201%201-2.94%200V2.471a1.47%201.47%200%201%201%202.94%200V6.16Z'%20fill='%232EB67D'/%3e%3cpath%20d='M9.843%2012.057a1.47%201.47%200%201%201%200%202.943%201.47%201.47%200%200%201-1.47-1.471v-1.472h1.47Zm0-.735a1.47%201.47%200%201%201%200-2.943h3.687a1.47%201.47%200%201%201%200%202.943H9.843Z'%20fill='%23ECB22E'/%3e%3c/svg%3e)

Slack

Surface the threads where they led, unblocked a teammate, or drove a decision.

[Connect](https://claude.ai/desktop/directory/slack)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%20100%20100'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%235E6AD2'%20d='M1.225%2061.523c-.222-.949.908-1.546%201.597-.857l36.512%2036.512c.689.689.092%201.819-.857%201.597a50.06%2050.06%200%200%201-37.252-37.252Zm-1.22-13.59a.98.98%200%200%200%20.283.724l50.055%2050.055a.98.98%200%200%200%20.724.283%2049.9%2049.9%200%200%200%208.636-1.518.976.976%200%200%200%20.462-1.647L2.17%2038.835a.976.976%200%200%200-1.647.462%2049.9%2049.9%200%200%200-1.518%208.636Zm4.194-17.443a.988.988%200%200%200%20.184%201.152l63.975%2063.975a.988.988%200%200%200%201.152.184%2050.4%2050.4%200%200%200%206.08-3.495.993.993%200%200%200%20.161-1.53L9.224%2024.249a.993.993%200%200%200-1.53.161%2050.4%2050.4%200%200%200-3.495%206.08Zm9.723-13.067a.99.99%200%200%201-.026-1.377C23.068%206.08%2036.765-.002%2051.888-.002c27.59%200%2049.957%2022.367%2049.957%2049.957%200%2015.123-6.082%2028.82-16.048%2038.013a.99.99%200%200%201-1.377-.026z'/%3e%3c/svg%3e)

LinearOptional

List the projects and epics they shipped and the cycle outcomes they owned.

[Connect](https://claude.ai/desktop/directory/linear)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)



**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (your career framework, the review template, last cycle's reviews, your team roster) into one folder and point Cowork at it. Cowork reads the framework from there and writes one draft per report back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your framework and your writing voice stay attached.

Reviews / 2026-Q1

eng-career-framework.pdfJan 12, 2026220 KB

review-template.mdJan 12, 20262 KB

team-roster.mdApr 1, 20261 KB

In Cowork’s chat bar:Reviews / 2026-Q1

## The prompt

### Copy this into Claude Cowork

I'm writing quarterly reviews for my reports. For each engineer in my team list, draft the review in our framework with evidence linked for every claim, drawing on their work this quarter and their last review's growth areas. Flag where I need to add my own judgment; do not write the rating.



Reviews / 2026-Q1Open in Cowork

### Why this works

Prompt

**Require evidence for every claim.** The draft is defensible in calibration; nothing rests on vibes.

Prompt

**Include prior context to show progress.** The review tracks progress, not just a snapshot of this quarter.

Prompt

**Keep judgment calls yours.** Saying the rating is yours to make tells Claude where its job ends. The draft gathers and organizes the evidence, then stops.

Source

**Give it your review framework.** Every draft maps to your levels and your competencies, not a generic ladder.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /code-review skill with my feedback.



ReviewsOpen in Cowork



**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it at the start of every cycle

The evidence packet should be ready before review season opens. Type `/schedule` or open **Scheduled** in the Cowork sidebar, and the customized skill builds the drafts as soon as the quarter folder appears.

**/schedule** Every Monday at 9am, if a new quarter folder exists under Reviews, run /code-review for everyone in team-roster.md and write each draft to Reviews/<quarter>/<name>.md.



ReviewsOpen in Cowork

Scheduled taskActive

Quarterly review drafts

When a new quarter folder appears, runs `/code-review` for each report against GitHub, Linear, and Slack and writes evidence-linked drafts to the cycle folder.

Every **Monday at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/code-review` now carries your career framework, your evidence sources, and your tone. Share it so every manager in the org drafts against the same ladder, and calibration compares apples to apples.



Share the skill

In Cowork, open **Skills** → `/code-review` → **Share** and pick your peer managers (or your whole workspace, if your admin allows). They get the skill with your framework baked in, so they don't repeat Steps 1-3.

## What changes for review season

Each report has a review draft with evidence linked for every claim and the places that need your judgment clearly marked. Your time goes to the assessment and the conversation, not to gathering what they shipped.

You did this for one review cycle. The same approach covers promotion packets, calibration prep, and peer-feedback summaries — each one becomes a skill your team runs the same way.

[Next: Draft the incident postmortem](https://academy.claude.com/use-cases/incident-postmortem)
