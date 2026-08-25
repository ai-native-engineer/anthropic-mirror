<!-- source: https://academy.claude.com/use-cases/contract-playbook-review -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Contract redlining

Clause-by-clause G/Y/R with redlines you can send back.

15 minLegalClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-hd3p5r1z.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-ci2tqnmp.png)

## Set up

### Try a plugin

The Commercial Legal plugin ships with `/review` and other commercial-contracting skills as a starting point, already structured to walk an agreement against your playbook, flag the deviations, and draft the redlines. It's one of twelve practice-area plugins for legal teams; if your admin manages plugins and it's not available yet, skip this, nothing below requires it.

Commercial LegalReviews vendor agreements, NDAs, and SaaS subscriptions against your sales-side or purchasing-side playbook, tracks renewals and cancel-by deadlines before they're missed, routes escalations to the right approver, and translates reviews into summaries business stakeholders will actually read.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fclaude-for-legal&plugin=commercial-legal)

`/review`Review a vendor agreement, NDA, or SaaS subscription against your playbook.

[Run](claude://cowork/new?q=%2Freview)

`/escalation-flagger`Route a contract issue to the right approver per the escalation matrix in your practice profile, and draft the ask.

[Run](claude://cowork/new?q=%2Fescalation-flagger)

`/cold-start-interview`Run the cold-start interview to learn your commercial contracts practice and write your team practice profile.

[Run](claude://cowork/new?q=%2Fcold-start-interview)

Show all 9 skills

First run

Commercial Legal comes from Anthropic's **Claude for Legal** source, which a workspace has to enable once under **Browse Anthropic sources**. On a Team or Enterprise plan an admin does that from the organization's plugin settings (it then shows up for everyone); on an individual plan you can do it yourself. If **Add** doesn't take you straight to the plugin, that's usually the missing step. Once it's installed, run `/cold-start-interview` (a two-minute quick start on sensible defaults, or ten-plus minutes with your real documents) so the plugin learns your playbook; every other skill reads from that.

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

Ironclad

Pull the counterparty draft and your playbook from the Ironclad workflow; the clause table and redline write to your working folder.

[Connect](https://claude.ai/desktop/directory/ironclad)

![](images/3cb5db332ced9f49.svg)

Microsoft 365

Draft redlines as tracked changes in the Word file and save to SharePoint.

[Connect](https://claude.ai/desktop/directory/microsoft-365)

iManage

Read the incoming draft, prior redlines, and your precedent library from the matter workspace.

[Connect](https://claude.ai/desktop/directory/imanage)

NetDocuments

Read the incoming draft and your playbook from the matter workspace; the clause table writes to your working folder.

[Connect](https://claude.ai/desktop/directory/netdocuments)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

### Set the working folder

Put the incoming MSA and your contract playbook in one folder on your machine, then in Cowork click **+ Add folder** and select it. [Save it as a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) so your playbook, instructions, and memory stay attached and you don't re-upload them for the next contract — Cowork reads from the folder and writes the clause table and redlined draft back to it.

Files you add stay on your machine and aren't used to train Claude — Cowork reads them locally to do the work.

**Just want to try it once first?** Skip the project — click **+ Add folder** on a one-off folder and jump to the prompt below.

Contracts / Acme-MSA

Acme-MSA-v3-counterparty.docxApr 24, 2026182 KB

contract-playbook-2026.pdfJan 6, 2026412 KB

In Cowork’s chat bar:Contracts / Acme-MSA

## The prompt

### Copy this into Claude Cowork

Review this MSA clause by clause against our contract playbook. For each clause, mark it green, yellow, or red against our standard, explain why in one or two sentences, and where it's yellow or red draft the redline and the rationale for opposing counsel.

Contracts / Acme-MSAOpen in Cowork

### Why this works

Prompt

**Compare against your own baseline.** G/Y/R means deviation from your playbook, not a textbook.

Prompt

**Ask for the fix and the reasoning.** Paste-ready language plus rationale that holds up with counsel.

Prompt

**Save the detail for the problems.** One line for standard clauses; detail goes where the risk is.

Source

**Write results back to the same folder.** Review and redline write back next to the original.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /review skill with my feedback.

ContractsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Make it a live artifact

A review memo is stale the moment opposing counsel sends v4. Ask Cowork to publish the clause table as a live artifact and the deal team has one link that stays current — re-run the skill or schedule it to refresh.

Publish that clause table as a live artifact for the deal team. Re-run it against whatever the latest counterparty draft is in this folder, and keep a short "what changed since last turn" note at the top.

Contracts / Acme-MSAOpen in Cowork

### Run it on every new contract

Paper arrives, the first-pass review should already be waiting. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and set the customized skill to run every weekday morning, checking the intake folder for new contracts.

**/schedule** Weekdays at 9am, check Contracts/Intake for new files and run /review on each one, writing the clause table and redlined draft to a subfolder named for the counterparty.

ContractsOpen in Cowork

Scheduled taskActive

First-pass contract review

Each weekday at 9am, checks Contracts/Intake for new files, runs `/review` on each one, and writes the clause table and redlined draft to a counterparty subfolder.

Every **weekday at 9 am — checks Contracts/Intake for new files**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/review` now carries your playbook, your red-flag list, and your fallback positions. Share it so every reviewer on the team scores paper the same way, and the business sees a consistent first pass no matter who picks it up.

Share the skill

In Cowork, open **Skills** → `/review` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your playbook and positions baked in, so they don't repeat Steps 1-3; each teammate still runs `/cold-start-interview` the first time, pointed at the same playbook, because the plugin keeps its setup per person.

## What changes for the contracts queue

Each contract is checked against your playbook with a redline and rationale on every clause that departs from your standard. Your review starts at the flagged terms instead of page one.

You did this for one MSA. The same approach works for NDAs, DPAs, and vendor agreements — each one becomes a skill your team runs the same way.

### Finish it where the file lives

[![](https://academy.claude.com/surfaces/word-icon.svg)

Claude in Word

Draft the redline as tracked changes

Install](https://claude.com/download)

[Next: Outside counsel management](https://academy.claude.com/use-cases/outside-counsel-review)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for the contracts queue](#what-changes-for-the-contracts-queue)
