<!-- source: https://academy.claude.com/use-cases/regulatory-analysis -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Regulatory and compliance

What changed, what applies to you, what to do by when.

10 minLegalClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-btqx4o1h.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-mbqnkmu3.png)

## Set up

### Try a plugin

The Regulatory Legal plugin ships with `/policy-diff` and other regulatory-change skills as a starting point, already structured to read a new rule against your current policies and pull out which ones it touches and where the gaps are. It's one of twelve practice-area plugins for legal teams; if your admin manages plugins and it's not available yet, skip this, nothing below requires it.

Regulatory LegalWatches regulatory feeds, diffs new rules against your policy library, tracks comment deadlines and open gaps, and writes the digest your team reads Monday morning.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fclaude-for-legal&plugin=regulatory-legal)

`/policy-diff`Diff a specific regulatory change against the indexed policy library.

[Run](claude://cowork/new?q=%2Fpolicy-diff)

`/reg-feed-watcher`Check regulatory feeds now and report what's new since the last check, filtered by your materiality threshold.

[Run](claude://cowork/new?q=%2Freg-feed-watcher)

`/cold-start-interview`Cold-start interview — builds your watchlist, indexes the policy library, and learns your materiality threshold so the monitor surfaces signal instead of noise.

[Run](claude://cowork/new?q=%2Fcold-start-interview)

Show all 8 skills

First run

Regulatory Legal comes from Anthropic's **Claude for Legal** source, which a workspace has to enable once under **Browse Anthropic sources**. On a Team or Enterprise plan an admin does that from the organization's plugin settings (it then shows up for everyone); on an individual plan you can do it yourself. If **Add** doesn't take you straight to the plugin, that's usually the missing step. Once it's installed, run `/cold-start-interview`: the full pass (ten-plus minutes, pointed at the policies in your working folder) is what indexes your policy library for `/policy-diff` to read against — the two-minute quick start gets you going on sensible defaults but skips that index. Every other skill reads from that setup.

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23F25022'%20d='M1%201h10.5v10.5H1z'/%3e%3cpath%20fill='%237FBA00'%20d='M12.5%201H23v10.5H12.5z'/%3e%3cpath%20fill='%2300A4EF'%20d='M1%2012.5h10.5V23H1z'/%3e%3cpath%20fill='%23FFB900'%20d='M12.5%2012.5H23V23H12.5z'/%3e%3c/svg%3e)

Microsoft 365

[Connect](https://claude.ai/desktop/directory/microsoft-365)

CoCounsel Legal (Thomson Reuters)

Ground the applicability brief in authoritative content with citations you can verify.

[Connect](https://claude.ai/desktop/directory/cocounsel-legal)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

### Set the working folder

Put the regulation PDF, your product descriptions, and your current policies in one folder on your machine, then in Cowork click **+ Add folder** and select it. [Save it as a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) so your product context, instructions, and memory stay attached for the next rule that drops — Cowork reads from the folder and writes the applicability brief and action table back to it.

Files you add stay on your machine and aren't used to train Claude — Cowork reads them locally to do the work.

**Just want to try it once first?** Skip the project — click **+ Add folder** on a one-off folder and jump to the prompt below.

Regulatory / EU-AI-Act

eu-ai-act-final-text.pdfApr 22, 20264.1 MB

product-descriptions.docxMar 3, 202688 KB

current-privacy-and-ai-policies.pdfJan 12, 2026612 KB

In Cowork’s chat bar:Regulatory / EU-AI-Act

## The prompt

### Copy this into Claude Cowork

Read this regulation against our product descriptions and current policies. Draft the compliance brief: what changed from the prior rule, which provisions apply to us and why, and for each what we need to do and by when. Save it to the folder for product and compliance leads.

Regulatory / EU-AI-ActOpen in Cowork

### Why this works

Prompt

**Compare against your own documents.** "Against our product descriptions and current policies" turns a 400-page rule into an applicability call, so the brief talks about your products by name, not the regulation in the abstract.

Prompt

**Ask for what's changed since last time.** "What changed from the prior rule" skips the parts you already comply with and puts the new obligations at the top of the brief.

Prompt

**Pair each action with a deadline.** "What we need to do and by when" makes every applicable provision land as an owner-ready task with a deadline, not a paragraph of analysis.

Source

**Let the working folder supply context.** The regulation, your product descriptions, and your policies sit in the working folder, so the brief is written against what you actually ship and the action table is saved next to the source text.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /policy-diff skill with my feedback.

RegulatoryOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it on every new regulation

A final rule drops, the applicability brief should already be drafting. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs whenever a new regulation is added to the watch folder.

**/schedule** Weekdays at 9am, check Regulatory/Watch for any new file and run /policy-diff against it and write the applicability brief and action table to a subfolder named for the regulation.

RegulatoryOpen in Cowork

Scheduled taskActive

New-regulation applicability brief

Runs `/policy-diff` on every new file in Regulatory/Watch and writes the brief and action table to a subfolder named for the regulation.

Every **Weekdays at 9am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/policy-diff` now carries your policy library, your jurisdictions, and your memo format. Share it so product, privacy, and compliance all read the same brief, and the action table follows the same structure every time a rule drops.

Share the skill

In Cowork, open **Skills** → `/policy-diff` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your jurisdictions and memo format baked in, so they don't repeat Steps 1-3; each teammate still runs `/cold-start-interview` the first time, pointed at the same policy library, because the plugin keeps its index per person.

## Going forward

### Now in your Cowork

Your processes

Regulatory Legal plugin

Your tools

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)Google Drive![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23F25022'%20d='M1%201h10.5v10.5H1z'/%3e%3cpath%20fill='%237FBA00'%20d='M12.5%201H23v10.5H12.5z'/%3e%3cpath%20fill='%2300A4EF'%20d='M1%2012.5h10.5V23H1z'/%3e%3cpath%20fill='%23FFB900'%20d='M12.5%2012.5H23V23H12.5z'/%3e%3c/svg%3e)Microsoft 365

Your workspace

Regulatory

New regulations are read against your own products and policies, with a specific action and deadline for each provision that applies — ready to assign instead of research.

[Next: Legal research](https://academy.claude.com/use-cases/legal-research-memo)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
