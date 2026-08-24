<!-- source: https://academy.claude.com/use-cases/transcript-themes -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Transcript theme extractor

The themes across your calls, counted and quoted.

10 minSalesClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-kzha9gcj.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-kjzr1f4d.png)

## Set up

### Try a plugin

The Sales plugin ships with `/call-summary` and other voice-of-customer skills as a starting point, already structured to read a batch of transcripts and roll them up into named themes with counts and quotes. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

Sales8 skills for account research, call prep, pipeline review, and account health

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=sales)

`/call-summary`Cluster a folder of call transcripts into themes with counts and quotes

[Run](claude://cowork/new?q=%2Fcall-summary)

`/pipeline-review`Score account health from usage, tickets, NPS, and the success plan

[Run](claude://cowork/new?q=%2Fpipeline-review)

Show all 9 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%2300A1E0'%20d='M10.01%205.56a4.18%204.18%200%200%201%203.02-1.3c1.58%200%202.96.88%203.7%202.19a5.12%205.12%200%200%201%202.1-.45%205.18%205.18%200%200%201%200%2010.36c-.37%200-.73-.04-1.07-.11a3.77%203.77%200%200%201-4.94%201.55%204.3%204.3%200%200%201-7.99-.2%203.98%203.98%200%200%201-.82.09%203.97%203.97%200%200%201-1.96-7.43%204.57%204.57%200%200%201%207.96-4.7'/%3e%3c/svg%3e)

Salesforce

Read call notes logged to the opportunity so the themes tie back to accounts.

Custom connector

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the transcript exports, any prior themes brief, your theme taxonomy if you have one) into one folder on your machine, then point Cowork at it. Cowork reads every transcript in place and writes the themes brief back to the same folder. If you run this every quarter, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your taxonomy, instructions, and memory stay attached.

Calls / 2026-Q1

northwind-2026-01-14.txtJan 14, 202642 KB

acme-2026-02-03.txtFeb 3, 202638 KB

globex-2026-03-11.txtMar 11, 202651 KB

themes-taxonomy.docxJan 6, 202618 KB

In Cowork’s chat bar:Calls / 2026-Q1

## The prompt

### Copy this into Claude Cowork

Read every transcript in this folder and cluster what customers are saying into themes. For each theme give me the count, the best one-line quote, and which accounts said it. Write the one-page themes brief to the folder for product and marketing.

Calls / 2026-Q1Open in Cowork

### Why this works

Prompt

**Ask for the evidence behind each finding.** "Count, best one-line quote, which accounts" turns each theme into evidence, so product and marketing can size it and hear it in the customer's words.

Prompt

**Name the audience.** "Share with product and marketing" tells Cowork to write a brief, not a spreadsheet, and to lead with what those teams act on rather than a raw cluster dump.

Prompt

**Set a length limit.** Asking for a one-page brief forces ranking by frequency, so the long tail of one-off mentions doesn't bury the three themes that matter.

Source

**Keep source and output in one folder.** Every transcript sits in the working folder, so Cowork reads the full quarter in one pass and writes the brief back next to the source files for traceability.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /call-summary skill with my feedback.

CallsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it as the quarter closes

Themes are most useful when they land before planning, not after. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill reads the quarter's folder and writes the brief as soon as the new quarter folder appears.

**/schedule** Every Monday at 9am, if a new quarter folder exists under Calls, run /call-summary on the previous quarter's folder and write the themes brief there. Include a section on what's new versus last quarter.

CallsOpen in Cowork

Scheduled taskActive

Quarterly call themes

Runs `/call-summary` on the previous quarter's transcript folder and writes the one-page brief, with a section on what's new versus last quarter.

Every **Monday at 9:00 AM**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/call-summary` now carries your taxonomy, your segment splits, and your brief format. Share it so anyone on the CS or sales team can run it on their own calls, and product hears the same theme names from every region.

Share the skill

In Cowork, open **Skills** → `/call-summary` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your taxonomy and format baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Sales plugin

Your tools

Gong![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)Google Drive

Your workspace

Calls

What customers are saying across your calls is organized into themes, each counted, quoted, and attributed to accounts — a one-page brief ready to share instead of assemble by hand.

[Next: Account research](https://academy.claude.com/use-cases/account-research-brief)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
