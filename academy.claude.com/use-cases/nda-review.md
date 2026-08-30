<!-- source: https://academy.claude.com/use-cases/nda-review -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# NDA triage at scale

Standard NDAs routed for signature; only exceptions hit counsel.

10 minLegalClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-dydenpqj.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-jd1jgfwn.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Commercial Legal plugin ships with `/review` and other commercial-contracting skills as a starting point, already structured to screen an NDA against your playbook and sort it green, yellow, or red so standard paper splits from the exceptions. It's one of twelve practice-area plugins for legal teams; if your admin manages plugins and it's not available yet, skip this, nothing below requires it.

Commercial LegalReviews vendor agreements, NDAs, and SaaS subscriptions against your sales-side or purchasing-side playbook, tracks renewals and cancel-by deadlines before they're missed, routes escalations to the right approver, and translates reviews into summaries business stakeholders will actually read.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fclaude-for-legal&plugin=commercial-legal)

`/review`Review a vendor agreement, NDA, or SaaS subscription against your playbook.

[Run](claude://cowork/new?q=%2Freview)

`/stakeholder-summary`Translate a contract review into a summary the business stakeholder will actually read.

[Run](claude://cowork/new?q=%2Fstakeholder-summary)

`/cold-start-interview`Run the cold-start interview to learn your commercial contracts practice and write your team practice profile.

[Run](claude://cowork/new?q=%2Fcold-start-interview)

Show all 9 skills

First run

Commercial Legal comes from Anthropic's **Claude for Legal** source, which a workspace has to enable once under **Browse Anthropic sources**. On a Team or Enterprise plan an admin does that from the organization's plugin settings (it then shows up for everyone); on an individual plan you can do it yourself. If **Add** doesn't take you straight to the plugin, that's usually the missing step. Once it's installed, run `/cold-start-interview` (a two-minute quick start on sensible defaults, or ten-plus minutes with your real documents) so the plugin learns your playbook — the full pass, with your NDA positions in it, is what lets `/review` clear standard paper to green; every other skill reads from that.

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/a3bfc5814bd6a3e2.svg)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

![](images/3cb5db332ced9f49.svg)

Microsoft 365

[Connect](https://claude.ai/desktop/directory/microsoft-365)

![](images/0b7839904dd03a68.svg)

DocuSignOptional

[Connect](https://claude.ai/desktop/directory/docusign)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

### Set the working folder[](#set-the-working-folder)

Put your standard mutual template and your NDA playbook in one folder on your machine, then in Cowork click **+ Add folder** and select it. [Save it as a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) so your playbook and template are loaded once and every inbound NDA runs against the same project knowledge — Cowork reads from the folder and writes the triage card back to it.

Files you add stay on your machine and aren't used to train Claude — Cowork reads them locally to do the work.

**Just want to try it once first?** Skip the project — click **+ Add folder** on a one-off folder with a single NDA and jump to the prompt below.

NDAs / Intake

mutual-nda-northwind.docxApr 24, 202664 KB

nda-playbook.pdfJan 6, 2026318 KB

standard-mutual-nda.docxNov 20, 202548 KB

In Cowork’s chat bar:NDAs / Intake

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Triage this NDA against our NDA playbook. For each criterion in the playbook, mark whether this paper meets our standard. If everything passes, mark it cleared and route for signature. If anything is off-standard, list only the exceptions with a one-line reason each so counsel reviews just those.

NDAs / IntakeOpen in Cowork

### Why this works[](#why-this-works)

Prompt

**Check against your playbook.** "Each criterion in the playbook" turns triage into your team's fixed checklist, so every NDA is screened the same way against positions you've already taken.

Prompt

**Define the two outcomes.** "Mark it cleared and route for signature" or "list only the exceptions" gives Cowork a binary decision to make, which is what lets standard paper move without a lawyer touching it.

Prompt

**Set a length limit.** "One-line reason each" means the exception list is a scan, not a memo, so counsel opens the file already knowing which clause to go to.

Source

**Let the working folder supply context.** Your mutual template and NDA playbook sit in the working folder, so "our standard" means your positions on term, law, and carve-outs, not a generic checklist.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you[](#make-cowork-work-for-you)

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /review skill with my feedback.

NDAsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Run it on every new NDA[](#run-it-on-every-new-nda)

NDAs arrive throughout the day. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill checks NDAs/Intake each weekday morning and runs /review on any new files before your day starts.

**/schedule** Weekdays at 9am — run /review on every file in NDAs/Intake that wasn't there on the last run. Route cleared NDAs to DocuSign for signature and move them to NDAs/Processed. For anything with exceptions, write the triage card to NDAs/Exceptions and post the list to #legal-nda-review in Slack so counsel picks it up.

NDAsOpen in Cowork

Scheduled taskActive

NDA intake triage

Each weekday morning, runs `/review` on files added to NDAs/Intake since the last run. Cleared paper routes to DocuSign and moves to NDAs/Processed (the executed copy lands wherever your DocuSign envelope settings already send it); exceptions get a triage card in NDAs/Exceptions and a Slack post to #legal-nda-review for counsel.

Every **weekday at 9:00 AM — checks NDAs/Intake for new files**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/review` now carries your full playbook checklist, your approved jurisdictions, and your escalation triggers. Share it so every requester and paralegal screens NDAs the same way, and counsel only sees the paper that actually needs them.

Share the skill

In Cowork, open **Skills** → `/review` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your checklist and routing rules baked in, so they don't repeat Steps 1-3; each teammate still runs `/cold-start-interview` the first time, pointed at the same playbook, because the plugin keeps its setup per person.

## Going forward[](#going-forward)

### Now in your Cowork

Your processes

Commercial Legal plugin

Your tools

![](images/a3bfc5814bd6a3e2.svg)Google Drive![](images/3cb5db332ced9f49.svg)Microsoft 365![](images/0b7839904dd03a68.svg)DocuSign

Your workspace

NDAs/Intake

Each incoming NDA is screened against your playbook, with non-standard terms listed and everything else cleared for signature — review starts at the exceptions, not the full document.

[Next: Contract review against your playbook](https://academy.claude.com/use-cases/contract-playbook-review)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
