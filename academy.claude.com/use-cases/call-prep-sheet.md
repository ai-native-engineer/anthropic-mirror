<!-- source: https://academy.claude.com/use-cases/call-prep-sheet -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Call prep

Where the deal is and what to ask on this call.

10 minSalesClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-fzzs6i6o.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-my91enox.png)

## Set up

### Try a plugin

The Sales plugin ships with `/call-prep` and other deal-cycle skills as a starting point, already structured to read the opp, the transcripts, and the plan and write a sheet you can scan a minute before the call. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

SalesProspect, craft outreach, and build deal strategy faster. Prep for calls, manage your pipeline, and write personalized messaging that moves deals forward.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=sales)

`/call-prep`Prepare for a sales call with account context, attendee research, and suggested agenda.

[Run](claude://cowork/new?q=%2Fcall-prep)

`/account-research`Research a company or person and get actionable sales intel.

[Run](claude://cowork/new?q=%2Faccount-research)

Show all 9 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%2300A1E0'%20d='M10.01%205.56a4.18%204.18%200%200%201%203.02-1.3c1.58%200%202.96.88%203.7%202.19a5.12%205.12%200%200%201%202.1-.45%205.18%205.18%200%200%201%200%2010.36c-.37%200-.73-.04-1.07-.11a3.77%203.77%200%200%201-4.94%201.55%204.3%204.3%200%200%201-7.99-.2%203.98%203.98%200%200%201-.82.09%203.97%203.97%200%200%201-1.96-7.43%204.57%204.57%200%200%201%207.96-4.7'/%3e%3c/svg%3e)

Salesforce

Custom connector

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3crect%20width='24'%20height='24'%20rx='5'%20fill='%23FFC127'/%3e%3cpath%20fill='%23000'%20d='M12%204.2%205.4%2018.9h3.37l1.02-2.42h4.42l1.02%202.42h3.37L12%204.2Zm0%204.87%201.54%203.64h-3.08L12%209.07Z'/%3e%3c/svg%3e)

ApolloOptional

Surface recent intent signals and contact changes so the prep sheet is current.

[Connect](https://claude.ai/desktop/directory/apollo)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the mutual action plan, your own notes, the proposal) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the prep sheet back to it. If you prep calls regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so your account context, instructions, and memory stay attached.

Accounts / Northwind / calls

mutual-action-plan.xlsxApr 14, 202622 KB

call-notes-apr10.docxApr 10, 202611 KB

proposal-v2.pdfApr 8, 2026410 KB

In Cowork’s chat bar:Accounts / Northwind / calls

## The prompt

### Copy this into Claude Cowork

I'm meeting Northwind tomorrow. From the Salesforce record, the last three Gong transcripts, and the mutual action plan, write the prep sheet: where the deal is, what they care about, the two or three asks I should make on this call, and the likely objections with our response.

Accounts / Northwind / callsOpen in Cowork

### Why this works

Prompt

**Ask for what to do on the call.** "Two or three asks I should make" turns the sheet from a recap into a plan, so you walk in knowing what you need to land before the call ends.

Prompt

**Pair objections with responses.** "With our response" means each likely pushback comes with the line you'll use, drawn from what's already worked on the transcripts.

Source

**Give enough history to spot patterns.** Naming the last three Gong calls gives Cowork enough history to spot what the buyer keeps returning to, which is where "what they care about" comes from.

Source

**Include the documents you maintain.** The mutual action plan and your own notes sit in the working folder, so deal status is read from the document you actually maintain, not just the CRM stage field.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /call-prep skill with my feedback.

AccountsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it before every external call

Prep should be waiting before the meeting reminder fires. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill builds a sheet for every external call on your calendar each morning.

**/schedule** Every weekday at 7:30am, run /call-prep for each external meeting on today's calendar and write each sheet to the matching account's calls folder under Accounts.

AccountsOpen in Cowork

Scheduled taskActive

Morning call prep

Runs `/call-prep` for each external meeting on today's calendar and writes the sheet to the account's calls folder.

Every **weekday at 7:30 AM**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/call-prep` now carries your discovery framework, your objection playbook, and your sheet format. Share it so every rep walks into calls with the same prep, and managers can read any sheet the same way.

Share the skill

In Cowork, open **Skills** → `/call-prep` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your framework and playbook baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Sales plugin

Your tools

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%2300A1E0'%20d='M10.01%205.56a4.18%204.18%200%200%201%203.02-1.3c1.58%200%202.96.88%203.7%202.19a5.12%205.12%200%200%201%202.1-.45%205.18%205.18%200%200%201%200%2010.36c-.37%200-.73-.04-1.07-.11a3.77%203.77%200%200%201-4.94%201.55%204.3%204.3%200%200%201-7.99-.2%203.98%203.98%200%200%201-.82.09%203.97%203.97%200%200%201-1.96-7.43%204.57%204.57%200%200%201%207.96-4.7'/%3e%3c/svg%3e)SalesforceGong![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)Google Drive

Your workspace

Accounts

Every call gets a one-page prep sheet built from current deal data, with the asks to make and the likely objections already answered.

[Next: Pipeline reviews](https://academy.claude.com/use-cases/pipeline-review)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
