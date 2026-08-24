<!-- source: https://academy.claude.com/use-cases/vendor-negotiation -->

Loading

## Set up

### Try a plugin

The Operations plugin ships with `/vendor-review` already structured to diff two contract versions into a redline table and turn usage and comparables into leverage. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.



OperationsOptimize business operations — vendor management, process documentation, change management, capacity planning, and compliance tracking. Keep your organization running efficiently.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=operations)

`/vendor-review`Evaluate a vendor — cost analysis, risk assessment, and recommendation.

[Run](claude://cowork/new?q=%2Fvendor-review)

`/risk-assessment`Identify, assess, and mitigate operational risks.

[Run](claude://cowork/new?q=%2Frisk-assessment)

Show all 9 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

Pull the signed agreement, the renewal PDF, and the comparable quotes from the procurement folder.

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)



Brex

Pull current spend with the vendor so the negotiation opens with the real number, not list price.

[Connect](https://claude.ai/desktop/directory/brex)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.951%209.85a1.47%201.47%200%201%201-2.94%200%201.47%201.47%200%200%201%201.47-1.471h1.47V9.85Zm.735%200a1.47%201.47%200%201%201%202.94%200v3.679a1.47%201.47%200%201%201-2.94%200V9.85Z'%20fill='%23E01E5A'/%3e%3cpath%20d='M6.157%203.943a1.47%201.47%200%201%201%200-2.943%201.47%201.47%200%200%201%201.47%201.471v1.472h-1.47Zm0%20.746a1.47%201.47%200%201%201%200%202.943H2.47a1.47%201.47%200%201%201%200-2.943h3.687Z'%20fill='%2336C5F0'/%3e%3cpath%20d='M12.049%206.16a1.47%201.47%200%201%201%202.94%200%201.47%201.47%200%200%201-1.47%201.472h-1.47V6.16Zm-.736%200a1.47%201.47%200%201%201-2.94%200V2.471a1.47%201.47%200%201%201%202.94%200V6.16Z'%20fill='%232EB67D'/%3e%3cpath%20d='M9.843%2012.057a1.47%201.47%200%201%201%200%202.943%201.47%201.47%200%200%201-1.47-1.471v-1.472h1.47Zm0-.735a1.47%201.47%200%201%201%200-2.943h3.687a1.47%201.47%200%201%201%200%202.943H9.843Z'%20fill='%23ECB22E'/%3e%3c/svg%3e)

SlackOptional

Pull stakeholder asks and pain points from the vendor channel so the brief covers what the business actually wants.

[Connect](https://claude.ai/desktop/directory/slack)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)



**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Put the current agreement, the renewal proposal, your usage export, and the comparable quotes in one folder. Cowork diffs the two contracts there and writes the redline table and the brief back next to them. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your procurement folder so your fallback positions and standard contract terms stay attached for every renewal.

Procurement / Northwind-renewal-2026

Northwind-MSA-2024-signed.pdfMay 12, 2024412 KB

Northwind-renewal-proposal-2026.pdfApr 18, 2026388 KB

usage-and-comparables.xlsxApr 24, 202638 KB

In Cowork’s chat bar:Procurement / Northwind-renewal-2026

## The prompt

### Copy this into Claude Cowork

Compare the current agreement to the renewal proposal and summarize every material change as a redline table (clause, current, proposed, our position). Then write the negotiation brief: our leverage, their likely pushback, three asks ranked by value, and the walk-away line. Keep it to one page I can take into the call.



Procurement / Northwind-renewal-2026Open in Cowork

### Why this works

Prompt

**Name the columns you want.** Clause, current, proposed, our position: nothing slips through and Legal can scan it in two minutes.

Prompt

**Ask for a ranked shortlist.** Three, by value. You walk in knowing what to trade and what to hold.

Prompt

**Ask for the decision point.** The brief isn't done until it says when you'd leave the table.

Source

**Ground it in your own spend data.** The argument is built from your numbers, not the vendor's slide.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /vendor-review skill with my feedback.



ProcurementOpen in Cowork



**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it before every renewal

The brief should exist before the vendor's AE books the call. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill watches the renewal calendar and drops a brief 60 days out.

**/schedule** Every Monday at 9am, check the contracts spreadsheet for any vendor renewing in the next 60 days, run /vendor-review against that vendor's folder, and write the brief to Procurement/<vendor>-renewal-<year>/.



ProcurementOpen in Cowork

Scheduled taskActive

Renewal negotiation briefs

Weekly, finds vendors renewing in the next 60 days, runs `/vendor-review` on each, and writes the redline and brief to the vendor folder.

Every **Mondays at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/vendor-review` now carries your standard fallback positions, your redline format, and what your Legal team will and won't accept. Share it so every category owner walks into renewals with the same prep.



Share the skill

In Cowork, open **Skills** → `/vendor-review` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your positions and redline format baked in, so they don't repeat Steps 1-3.

## What changes for the renewal call

Every material change in the renewal is documented with your position on it, and the negotiating brief is written from your own usage and spend data. You start the conversation prepared rather than reacting to the vendor's terms.

You did this for one renewal. The same approach covers SOW reviews, contract amendments, and price-increase notices — each one becomes a skill your team runs the same way.

[Next: Screen a vendor for risk](https://academy.claude.com/use-cases/vendor-risk-review)
