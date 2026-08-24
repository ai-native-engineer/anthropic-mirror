<!-- source: https://academy.claude.com/use-cases/design-doc -->

Loading

## Set up

### Try a plugin

The Engineering plugin ships with `/system-design` as a starting point, already structured to fill an RFC template and look up prior art across your wiki. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.



EngineeringStreamline engineering workflows — standups, code review, architecture decisions, incident response, and technical documentation. Works with your existing tools or standalone.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=engineering)

`/system-design`Design systems, services, and architectures.

[Run](claude://cowork/new?q=%2Fsystem-design)

`/architecture`Create or evaluate an architecture decision record (ADR).

[Run](claude://cowork/new?q=%2Farchitecture)

Show all 10 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cdefs%3e%3clinearGradient%20id='cfA'%20x1='22.64'%20y1='24.36'%20x2='9.98'%20y2='17.07'%20gradientUnits='userSpaceOnUse'%3e%3cstop%20offset='0'%20stop-color='%230052CC'/%3e%3cstop%20offset='1'%20stop-color='%232684FF'/%3e%3c/linearGradient%3e%3clinearGradient%20id='cfB'%20x1='1.36'%20y1='-.36'%20x2='14.02'%20y2='6.93'%20gradientUnits='userSpaceOnUse'%3e%3cstop%20offset='0'%20stop-color='%230052CC'/%3e%3cstop%20offset='1'%20stop-color='%232684FF'/%3e%3c/linearGradient%3e%3c/defs%3e%3cpath%20fill='url(%23cfA)'%20d='M.87%2018.26c-.25.4-.52.87-.75%201.23a.75.75%200%200%200%20.25%201.02l4.96%203.05a.75.75%200%200%200%201.04-.25c.2-.33.45-.76.73-1.21%201.95-3.22%203.91-2.83%207.45-1.14l4.92%202.34a.75.75%200%200%200%201-.36l2.36-5.34a.75.75%200%200%200-.38-.98c-1.04-.49-3.1-1.46-4.96-2.36-6.68-3.24-12.36-3.03-16.62%204Z'/%3e%3cpath%20fill='url(%23cfB)'%20d='M23.13%205.74c.25-.4.52-.87.75-1.23a.75.75%200%200%200-.25-1.02L18.67.44a.75.75%200%200%200-1.04.25c-.2.33-.45.76-.73%201.21-1.95%203.22-3.91%202.83-7.45%201.14L4.53.7a.75.75%200%200%200-1%20.36L1.17%206.4a.75.75%200%200%200%20.38.98c1.04.49%203.1%201.46%204.96%202.36%206.68%203.24%2012.36%203.03%2016.62-4Z'/%3e%3c/svg%3e)

Confluence

Look up prior RFCs and architecture pages and write the new doc straight into your engineering space. Confluence access comes through the Atlassian Rovo connector (Jira and Confluence).

[Connect](https://claude.ai/desktop/directory/atlassian)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23181717'%20d='M12%20.3a12%2012%200%200%200-3.8%2023.39c.6.11.82-.26.82-.58v-2.03c-3.34.73-4.04-1.61-4.04-1.61-.55-1.39-1.33-1.76-1.33-1.76-1.09-.74.08-.73.08-.73%201.2.09%201.84%201.24%201.84%201.24%201.07%201.83%202.81%201.3%203.49%201%20.11-.78.42-1.31.76-1.61-2.67-.3-5.47-1.33-5.47-5.93%200-1.31.47-2.38%201.24-3.22-.13-.3-.54-1.52.11-3.18%200%200%201.01-.32%203.3%201.23a11.5%2011.5%200%200%201%206%200c2.29-1.55%203.3-1.23%203.3-1.23.65%201.66.24%202.88.12%203.18.77.84%201.23%201.91%201.23%203.22%200%204.61-2.8%205.63-5.48%205.92.43.37.81%201.1.81%202.22v3.29c0%20.32.22.7.82.58A12%2012%200%200%200%2012%20.3'/%3e%3c/svg%3e)

GitHub

Read the relevant code and past ADRs so the proposal references the system as it actually is.

[Connect](https://claude.ai/desktop/directory/github)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23000'%20d='M4.46%204.44c.74.6%201.02.56%202.42.46l13.18-.79c.28%200%20.05-.28-.05-.32l-2.19-1.58c-.42-.33-.98-.7-2.05-.6L2.99%202.53c-.46.05-.56.28-.37.46l1.84%201.45Zm.8%203.1v13.87c0%20.74.37%201.02%201.21.98l14.49-.84c.84-.05.93-.56.93-1.16V6.6c0-.6-.23-.93-.74-.88l-15.14.88c-.56.05-.75.33-.75.93Zm14.3.74c.1.42%200%20.84-.42.89l-.7.14v10.24c-.6.33-1.16.51-1.63.51-.74%200-.93-.23-1.49-.93l-4.56-7.16v6.93l1.44.33s0%20.84-1.16.84l-3.21.18c-.1-.18%200-.65.33-.74l.84-.23V9.98l-1.16-.1c-.1-.42.14-1.02.79-1.07l3.44-.23%204.75%207.25V9.42l-1.21-.14c-.1-.51.28-.88.74-.93l3.21-.18Z'/%3e%3c/svg%3e)

NotionOptional

Pull the RFC template and publish the draft into your design-review database.

[Connect](https://claude.ai/desktop/directory/notion)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)



**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (your RFC template, the one-pager or notes you've already written, related past RFCs, the service's architecture diagram) into one folder and point Cowork at it. Cowork reads from there and writes the draft, the alternatives table, and the diagram back to it. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from your RFCs folder so your template, your review checklist, and your team's writing conventions stay attached.

RFCs / 0087-streaming-events

rfc-template.mdJan 4, 20262 KB

notes-streaming-migration.mdApr 24, 20265 KB

current-pipeline-diagram.pngMar 11, 2026142 KB

In Cowork’s chat bar:RFCs / 0087-streaming-events

## The prompt

### Copy this into Claude Cowork

Write a design doc for moving our event pipeline from batch to streaming. Look up prior art and architecture constraints, then draft the proposal in our RFC template: problem, goals and non-goals, two or three approaches with trade-offs, the recommendation, and open questions. I'll fill in the parts only I know.



RFCs / 0087-streaming-eventsOpen in Cowork

### Why this works

Prompt

**Ask for prior art explicitly.** Cowork searches your wiki and past RFCs so the doc cites what's been tried before.

Prompt

**Force two or three approaches.** You get a real trade-off table, not a sales pitch for the first idea.

Prompt

**Say which parts you'll fill in.** Cowork handles structure and lookup; you spend time on the actual judgment call.

Source

**Give it your template to follow.** Output follows your sections and headings, so reviewers see the structure they expect.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /system-design skill with my feedback.



RFCsOpen in Cowork



**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it from any one-pager

Design docs start as a paragraph in a Slack thread or a notes file. Type `/schedule` or open **Scheduled** in the Cowork sidebar, and the customized skill watches your RFCs/inbox folder and turns any new one-pager into a structured first draft.

**/schedule** Weekdays at 9am, check RFCs/inbox for new one-pagers, run /system-design on each one, and write the structured draft to a numbered folder under RFCs/.



RFCsOpen in Cowork

Scheduled taskActive

RFC inbox to draft

Weekdays at 9am, picks up new one-pagers from RFCs/inbox, runs `/system-design` with prior-art lookup, and writes a structured draft to a numbered RFC folder.

Every **weekday at 9:00am**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/system-design` now carries your template, your prior-art sources, and your reviewers' standing questions. Share it so every tech lead's RFC arrives in the same shape, and architecture review spends time on the decision instead of the formatting.



Share the skill

In Cowork, open **Skills** → `/system-design` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your template and review checklist baked in, so they don't repeat Steps 1-3.

## What changes for design review

You have a complete RFC draft in your template, with prior art and trade-offs filled in from your own sources — ready to edit and review instead of write from a blank page.

You did this for one proposal. The same approach covers API changes, schema migrations, and architecture decisions — each one becomes a skill your team runs the same way.

[Next: Build an "Ask the Company" agent](https://academy.claude.com/use-cases/ask-the-company)
