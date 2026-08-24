<!-- source: https://academy.claude.com/use-cases/offer-process -->

Loading

## 1. Set up

### Try a plugin

The Human Resources plugin ships with `/draft-offer` and other recruiting skills as a starting point, already structured to fill an offer template, draft the email, and lay out the call deck. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.



Human Resources9 skills for recruiting, onboarding, performance reviews, comp analysis, and org health reporting

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=human-resources)

`/draft-offer`Assemble the offer email, filled offer fields, and screenshare deck for a finalist

[Run](claude://cowork/new?q=%2Fdraft-offer)

`/comp-analysis`Benchmark a proposed offer against your comp bands and recent closes

[Run](claude://cowork/new?q=%2Fcomp-analysis)

Show all 9 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.951%209.85a1.47%201.47%200%201%201-2.94%200%201.47%201.47%200%200%201%201.47-1.471h1.47V9.85Zm.735%200a1.47%201.47%200%201%201%202.94%200v3.679a1.47%201.47%200%201%201-2.94%200V9.85Z'%20fill='%23E01E5A'/%3e%3cpath%20d='M6.157%203.943a1.47%201.47%200%201%201%200-2.943%201.47%201.47%200%200%201%201.47%201.471v1.472h-1.47Zm0%20.746a1.47%201.47%200%201%201%200%202.943H2.47a1.47%201.47%200%201%201%200-2.943h3.687Z'%20fill='%2336C5F0'/%3e%3cpath%20d='M12.049%206.16a1.47%201.47%200%201%201%202.94%200%201.47%201.47%200%200%201-1.47%201.472h-1.47V6.16Zm-.736%200a1.47%201.47%200%201%201-2.94%200V2.471a1.47%201.47%200%201%201%202.94%200V6.16Z'%20fill='%232EB67D'/%3e%3cpath%20d='M9.843%2012.057a1.47%201.47%200%201%201%200%202.943%201.47%201.47%200%200%201-1.47-1.471v-1.472h1.47Zm0-.735a1.47%201.47%200%201%201%200-2.943h3.687a1.47%201.47%200%201%201%200%202.943H9.843Z'%20fill='%23ECB22E'/%3e%3c/svg%3e)

Slack

[Connect](https://claude.ai/desktop/directory/slack)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23F25022'%20d='M1%201h10.5v10.5H1z'/%3e%3cpath%20fill='%237FBA00'%20d='M12.5%201H23v10.5H12.5z'/%3e%3cpath%20fill='%2300A4EF'%20d='M1%2012.5h10.5V23H1z'/%3e%3cpath%20fill='%23FFB900'%20d='M12.5%2012.5H23V23H12.5z'/%3e%3c/svg%3e)

Microsoft 365

[Connect](https://claude.ai/desktop/directory/microsoft-365)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3crect%20width='24'%20height='24'%20rx='5'%20fill='%234C00FF'/%3e%3cpath%20fill='%23fff'%20d='M12%204.5a2.6%202.6%200%201%200%200%205.2%202.6%202.6%200%200%200%200-5.2Zm-1.6%206.7v3.62l-3.27-3.27L5.2%2013.5l6.8%206.8%206.8-6.8-1.93-1.95-3.27%203.27V11.2h-3.2Z'/%3e%3c/svg%3e)

DocuSignOptional

[Connect](https://claude.ai/desktop/directory/docusign)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)



**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the candidate summary, your offer letter template, the comp approval, the benefits one-pager) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the filled offer, the email draft, and the HTML deck back to it. If you run offers regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from the role's offers folder so your templates and tone stay attached.

Hiring / Senior-PM-Growth / offers

offer-letter-template.docxJan 12, 202654 KB

candidate-summary-ARivera.pdfApr 22, 202688 KB

comp-approval.xlsxApr 23, 202622 KB

benefits-overview-2026.pdfFeb 3, 2026410 KB

In Cowork’s chat bar:Hiring / Senior-PM-Growth / offers

## 2. The prompt

### Copy this into Claude Cowork

Put together the offer package for our finalist. Fill out the offer fields for my review, draft a warm email to the candidate that sets up the call, and build a short HTML presentation I can screenshare on the offer call covering the role, the numbers, and why we're excited about them.



Hiring / Senior-PM-Growth / offersOpen in Cowork

### Why this works

Prompt

**Ask for related outputs together.** Naming the email, the filled offer, and the deck in one prompt means the three artifacts agree on title, numbers, and start date because they were written together.

Prompt

**Say the output is for review.** "Fill out the offer fields for my review" makes the output a draft you approve, so nothing goes to the candidate or to signature until a person has checked the numbers.

Prompt

**Ask for personalized content.** "Why we're excited about them" pulls specifics from the candidate summary into the screenshare, so the call opens on what they bring rather than a generic pitch.

Source

**Put your source files in the folder.** The offer template, the approved numbers, and the benefits one-pager sit in the working folder, so the filled offer and the deck quote your real terms and land back next to them.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## 3. Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /draft-offer skill with my feedback.



HiringOpen in Cowork



**Tip:** tell Claude to edit the skill for you.

## 4. Make it repeatable

### Run it on a schedule

Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs every weekday morning. It checks the hiring folder for candidates who moved to Offer overnight so the package is ready before the recruiter opens it.

**/schedule** Weekdays at 9am. Check the hiring folder for candidates who moved to Offer overnight, run /draft-offer for each, and write the email draft, filled offer, and HTML deck to Hiring/<role>/offers.



HiringOpen in Cowork

Scheduled taskActive

Offer package on stage change

Runs `/draft-offer` each weekday morning for any candidate who moved to Offer overnight and writes the email, filled offer, and deck to the role's offers folder.

Every **Weekdays at 9am · checks the hiring folder for new Offer-stage candidates**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## 5. Share with your teammates

Your customized `/draft-offer` now carries your offer template, your email tone, and your branded deck layout. Share it so every recruiter and hiring manager produces the same quality of offer artifact, and candidates get a consistent experience no matter which team is closing them.



Share the skill

In Cowork, open **Skills** → `/draft-offer` → **Share** and pick your recruiting team (or your whole workspace, if your admin allows). They get the skill with your templates and guardrails baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Human Resources plugin

Your tools

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)Google Drive![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3crect%20width='24'%20height='24'%20rx='5'%20fill='%234C00FF'/%3e%3cpath%20fill='%23fff'%20d='M12%204.5a2.6%202.6%200%201%200%200%205.2%202.6%202.6%200%200%200%200-5.2Zm-1.6%206.7v3.62l-3.27-3.27L5.2%2013.5l6.8%206.8%206.8-6.8-1.93-1.95-3.27%203.27V11.2h-3.2Z'/%3e%3c/svg%3e)DocuSign

Your workspace

Hiring / offers

You have a complete, consistent offer package for each finalist — drafted from your approved terms and templates, ready for your review before anything goes to the candidate.

[Next: Onboarding plan](https://academy.claude.com/use-cases/open-new-role)
