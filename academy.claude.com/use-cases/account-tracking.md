<!-- source: https://academy.claude.com/use-cases/account-tracking -->

Loading

## 1. Set up

### Try a plugin

The Sales plugin ships with `/pipeline-review` and other customer success skills as a starting point, already structured to weigh usage, tickets, and sentiment into one call. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.



Sales8 skills for account research, call prep, pipeline review, and account health

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=sales)

`/pipeline-review`Score account health from usage, tickets, NPS, and the success plan

[Run](claude://cowork/new?q=%2Fpipeline-review)

`/call-summary`Cluster a folder of call transcripts into themes with counts and quotes

[Run](claude://cowork/new?q=%2Fcall-summary)

Show all 9 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%2300A1E0'%20d='M10.01%205.56a4.18%204.18%200%200%201%203.02-1.3c1.58%200%202.96.88%203.7%202.19a5.12%205.12%200%200%201%202.1-.45%205.18%205.18%200%200%201%200%2010.36c-.37%200-.73-.04-1.07-.11a3.77%203.77%200%200%201-4.94%201.55%204.3%204.3%200%200%201-7.99-.2%203.98%203.98%200%200%201-.82.09%203.97%203.97%200%200%201-1.96-7.43%204.57%204.57%200%200%201%207.96-4.7'/%3e%3c/svg%3e)

Salesforce

Custom connector

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%231F8DED'%20d='M21%200H3a3%203%200%200%200-3%203v18a3%203%200%200%200%203%203h18a3%203%200%200%200%203-3V3a3%203%200%200%200-3-3ZM7.2%204.8a.8.8%200%201%201%201.6%200v9.067a.8.8%200%201%201-1.6%200V4.8Zm-3.2.8a.8.8%200%201%201%201.6%200v6.933a.8.8%200%201%201-1.6%200V5.6Zm16.533%2011.933c-.12.107-2.987%202.534-8.533%202.534s-8.413-2.427-8.533-2.534a.8.8%200%200%201%201.066-1.2c.04.04%202.56%202.134%207.467%202.134s7.413-2.08%207.467-2.134a.8.8%200%200%201%201.066%201.2ZM20%2012.533a.8.8%200%201%201-1.6%200V5.6a.8.8%200%201%201%201.6%200v6.933Zm-3.2%201.334a.8.8%200%201%201-1.6%200V4.8a.8.8%200%201%201%201.6%200v9.067Zm-3.2.8a.8.8%200%201%201-1.6%200V4a.8.8%200%201%201%201.6%200v10.667Zm-3.2%200a.8.8%200%201%201-1.6%200V4a.8.8%200%201%201%201.6%200v10.667Z'/%3e%3c/svg%3e)

Intercom

Read open conversations and recent tickets so the health call reflects what support is actually seeing.

[Connect](https://claude.ai/desktop/directory/intercom)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)



**Want to try this task before setting anything up?** Add your files to a
working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the usage export, the success plan, the latest NPS responses) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the health summary back to it. If you track this account ongoing, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your health criteria, instructions, and memory stay attached.

Accounts / Northwind / health

usage-export-apr.csvApr 25, 202664 KB

success-plan.docxFeb 3, 202638 KB

nps-responses-q1.csvApr 2, 202612 KB

In Cowork’s chat bar:Accounts / Northwind / health

## 2. The prompt

### Copy this into Claude Cowork

From the usage data, open Zendesk tickets, NPS responses, and success plan for Northwind, write the account health summary to the account folder: call it red, yellow, or green with the reason in one or two sentences, then the two actions to take this week.



Accounts / Northwind / healthOpen in Cowork

### Why this works

Prompt

**Give a fixed set of answers.** "Red, yellow, or green" makes Cowork commit
to one status instead of hedging, and "with the reason" means the call is
defensible when leadership asks.

Prompt

**Say how many items you want.** "Two actions I should take this week" keeps
the output to what you'll actually do before Friday, not a backlog of
everything that could help.

Source

**Name the sources to weigh together.** Naming usage, tickets, NPS, and the
success plan together means health is weighed across product, support,
sentiment, and goals, not just whichever dashboard you checked last.

Source

**Include the goals to measure against.** The success plan and usage export
sit in the working folder, so the health call is measured against the goals
you actually agreed with the customer.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and
Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about"
so you know where to look first when you review the draft.

## 3. Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the
/pipeline-review skill with my feedback.



AccountsOpen in Cowork



**Tip:** tell Claude to edit the skill for you.

## 4. Make it repeatable

### Run it across your book every week

Health should be tracked, not checked when something breaks. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill writes a fresh summary for every account in your book each week.

**/schedule** Every Monday at 7am, run /pipeline-review for each account in my
book and write the summary to the matching health folder under Accounts. Roll
up anything red into one digest at the top.



AccountsOpen in Cowork

Scheduled taskActive

Weekly account health

Runs `/pipeline-review` for every account in your book and writes the summary
to its health folder, with red accounts rolled up into one digest.

Every **Monday at 7:00 AM**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## 5. Share with your teammates

Your customized `/pipeline-review` now carries your usage thresholds, your risk rules, and your summary format. Share it so every CSM scores health the same way, and the red/yellow/green means the same thing across the whole book.



Share the skill

In Cowork, open **Skills** → `/pipeline-review` → **Share** and pick your
teammates (or your whole workspace, if your admin allows). They get the skill
with your thresholds and format baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Sales plugin

Your tools

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%2300A1E0'%20d='M10.01%205.56a4.18%204.18%200%200%201%203.02-1.3c1.58%200%202.96.88%203.7%202.19a5.12%205.12%200%200%201%202.1-.45%205.18%205.18%200%200%201%200%2010.36c-.37%200-.73-.04-1.07-.11a3.77%203.77%200%200%201-4.94%201.55%204.3%204.3%200%200%201-7.99-.2%203.98%203.98%200%200%201-.82.09%203.97%203.97%200%200%201-1.96-7.43%204.57%204.57%200%200%201%207.96-4.7'/%3e%3c/svg%3e)Salesforce![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cg%20fill='%2303363D'%3e%3cpath%20d='M11%207.7v13.1H.2L11%207.7Z'/%3e%3cpath%20d='M11%203.2a5.4%205.4%200%200%201-10.8%200H11Z'/%3e%3cpath%20d='M13%2016.3V3.2h10.8L13%2016.3Z'/%3e%3cpath%20d='M13%2020.8a5.4%205.4%200%200%201%2010.8%200H13Z'/%3e%3c/g%3e%3c/svg%3e)Zendesk![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)Google Drive

Your workspace

Accounts

Every account in your book has a current health summary — scored the same way, written to its folder, with the next actions already named.

[Next: Transcript theme extractor](https://academy.claude.com/use-cases/transcript-themes)
