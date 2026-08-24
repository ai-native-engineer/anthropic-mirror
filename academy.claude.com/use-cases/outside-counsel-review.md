<!-- source: https://academy.claude.com/use-cases/outside-counsel-review -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Outside counsel management

Off-pattern entries and budget drift surfaced before the partner call.

10 minLegalClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-kwp2o4y3.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-hfgoshpu.png)

## Set up

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

iManage

Matter files, budgets, and invoice history so the variance check runs against the system of record.

[Connect](https://claude.ai/desktop/directory/imanage)

NetDocuments

Matter workspaces and billing detail so off-pattern entries are checked against your guidelines, not a sample.

[Connect](https://claude.ai/desktop/directory/netdocuments)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23F25022'%20d='M1%201h10.5v10.5H1z'/%3e%3cpath%20fill='%237FBA00'%20d='M12.5%201H23v10.5H12.5z'/%3e%3cpath%20fill='%2300A4EF'%20d='M1%2012.5h10.5V23H1z'/%3e%3cpath%20fill='%23FFB900'%20d='M12.5%2012.5H23V23H12.5z'/%3e%3c/svg%3e)

Microsoft 365

The variance table lands as Excel and the talking points as Word, ready for the partner conversation.

[Connect](https://claude.ai/desktop/directory/microsoft-365)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

### Set the working folder

Put your outside counsel billing guidelines and the matter budget tracker in one folder on your machine, then in Cowork click **+ Add folder** and select it. [Save it as a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) so your guidelines, instructions, and memory stay attached for the next firm review — Cowork reads from the folder and writes the variance table and talking points back to it.

Files you add stay on your machine and aren't used to train Claude — Cowork reads them locally to do the work.

**Just want to try it once first?** Skip the project — click **+ Add folder** on a one-off folder and jump to the prompt below.

Legal-Ops / OC-Review-Q2

outside-counsel-billing-guidelines.pdfJan 6, 2026312 KB

matter-budgets-FY26.xlsxApr 30, 202688 KB

In Cowork’s chat bar:Legal-Ops / OC-Review-Q2

## The prompt

### Copy this into Claude Cowork

Pull the billing and matter data for this firm from the connected matter system. Flag entries that are off-pattern against our billing guidelines, list every matter drifting against its budget with the variance and driver, and draft the talking points for the relationship-partner conversation.

Legal-Ops / OC-Review-Q2Open in Cowork

### Why this works

Prompt

**Check against your guidelines, not a generic rule.** "Off-pattern against our billing guidelines" means the flag is your block-billing or staffing rule, not a textbook one.

Prompt

**Ask for the variance and the driver.** A matter over budget is a number; why it's over is the conversation, so each row names the activity that pushed it.

Prompt

**End with the deliverable.** "Draft the talking points" turns the analysis into the prep you'd write anyway, so the partner conversation starts from substance.

Source

**Pull from the matter system directly.** The iManage or NetDocuments connector means the review covers every matter and invoice, not the ones that made it into a spreadsheet.

### Get a better draft

Practice

**Add an example to match.** Drop a prior partner-review memo into the folder and Cowork matches your structure and tone.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know which entries to verify against the invoice before you raise them.

## Make Cowork work for you

No plugin ships with this one yet — once the prompt is producing the review the way you want, turn it into your own skill. A few minutes of conversation and it runs with your guidelines and format from then on.

Make what we've done in this task so far into a skill called /oc-spend-review.

Legal-OpsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it before every partner review

The variance table and talking points should be waiting before the quarterly review, not built the night before. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the skill runs monthly across every panel firm.

**/schedule** First Monday of each month at 8am, run /oc-spend-review for every firm on the panel and write the variance table and talking points to a subfolder named for the firm.

Legal-OpsOpen in Cowork

Scheduled taskActive

Outside counsel spend review

Runs `/oc-spend-review` for every panel firm and writes the variance table and talking points to a per-firm subfolder.

Every **first Monday of each month at 8am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your `/oc-spend-review` now carries your billing guidelines, your variance thresholds, and your talking-point format. Share it so legal ops and the in-house owners run every firm the same way, and the partner conversation starts from the same prep.

Share the skill

In Cowork, open **Skills** → `/oc-spend-review` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your guidelines and thresholds baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your tools

iManageNetDocuments![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23F25022'%20d='M1%201h10.5v10.5H1z'/%3e%3cpath%20fill='%237FBA00'%20d='M12.5%201H23v10.5H12.5z'/%3e%3cpath%20fill='%2300A4EF'%20d='M1%2012.5h10.5V23H1z'/%3e%3cpath%20fill='%23FFB900'%20d='M12.5%2012.5H23V23H12.5z'/%3e%3c/svg%3e)Microsoft 365

Your workspace

Legal-Ops

Off-pattern entries and matters drifting against budget surface monthly with the driver named, so the relationship-partner conversation runs on substance instead of a spreadsheet hunt.

[Next: Regulatory and compliance](https://academy.claude.com/use-cases/regulatory-analysis)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
