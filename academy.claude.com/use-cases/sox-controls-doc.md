<!-- source: https://academy.claude.com/use-cases/sox-controls-doc -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# SOX & controls documentation

Process narrative, RCM, and flowchart in under an hour.

10 minFinanceClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-gtq6ufl9.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-dqfzjo1d.png)

## Set up

### Try a plugin

The Finance plugin ships with `/sox-testing` and other close and compliance skills as a starting point, already structured to turn a walkthrough into narrative, matrix, and flowchart. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

FinanceStreamline finance and accounting workflows, from journal entries and reconciliation to financial statements and variance analysis. Speed up audit prep, month-end close, and keeping your books clean.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=finance)

`/sox-testing`Generate SOX sample selections, testing workpapers, and control assessments.

[Run](claude://cowork/new?q=%2Fsox-testing)

`/audit-support`Support SOX 404 compliance with control testing methodology, sample selection, and documentation standards.

[Run](claude://cowork/new?q=%2Faudit-support)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/a3bfc5814bd6a3e2.svg)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

![](images/3cb5db332ced9f49.svg)

Microsoft 365

[Connect](https://claude.ai/desktop/directory/microsoft-365)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (your walkthrough notes, prior-year narrative, the RCM template, system screenshots) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the narrative, matrix, and flowchart back to it. If you'll document several processes this cycle, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from the parent Controls folder so the template and house style stay attached.

Controls / Order-to-Cash

walkthrough-notes-OTC.docxApr 22, 202638 KB

RCM-template.xlsxJan 12, 202624 KB

prior-year-narrative-OTC.pdfMar 9, 2025312 KB

system-screenshots/Apr 22, 20266 items

In Cowork’s chat bar:Controls / Order-to-Cash

## The prompt

### Copy this into Claude Cowork

Here's how this process runs. Write the process narrative in our standard format, build the risk and control matrix mapping each risk to its control, owner, and frequency, and draw the flowchart. Flag any step where a control looks missing or a segregation of duties issue shows up.

Controls / Order-to-CashOpen in Cowork

### Why this works

Prompt

**Start from the current state.** "Here's how this process actually runs" anchors the documentation in operational reality, not last year's narrative, so the matrix matches what auditors will walk.

Prompt

**Ask for related outputs in one prompt.** Naming the narrative, the matrix, and the flowchart in one prompt keeps them consistent with each other; the same step number means the same thing in every file.

Prompt

**Ask it to flag what's missing.** Asking to "flag any step where a control looks missing" so you can find the gaps while documenting, when they're still easy to fix.

Source

**Let the working folder supply the format.** Your RCM template and prior-year narrative sit in the working folder, so "our standard format" resolves to your actual columns and headings without you pasting them in.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /sox-testing skill with my feedback.

ControlsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it on every walkthrough

When a process owner drops their walkthrough notes, the documentation package should already be drafting. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs whenever a new walkthrough is added to the Controls folder.

**/schedule** Weekdays at 9am, check Controls for any new walkthrough file and run /sox-testing against it and write the narrative, RCM, and flowchart to a subfolder named for the process.

ControlsOpen in Cowork

Scheduled taskActive

Controls documentation package

Runs `/sox-testing` on every new walkthrough in Controls and writes the narrative, matrix, and flowchart to a process subfolder.

Every **weekday at 9am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/sox-testing` now carries your RCM columns, your control-ID scheme, and your narrative voice. Share it so every process owner produces the same audit-ready package, and internal audit sees one consistent format across the cycle for $0 instead of consulting rates.

Share the skill

In Cowork, open **Skills** → `/sox-testing` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your template and standards baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Finance plugin

Your tools

![](images/a3bfc5814bd6a3e2.svg)Google Drive![](images/3cb5db332ced9f49.svg)Microsoft 365

Your workspace

Controls

Each process has audit-ready documentation in your standard format, with control gaps and segregation-of-duties issues already flagged for follow-up.

[Next: Prep an audit request](https://academy.claude.com/use-cases/explain-a-variance)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
