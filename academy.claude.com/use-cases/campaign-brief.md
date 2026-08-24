<!-- source: https://academy.claude.com/use-cases/campaign-brief -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Build a campaign brief

A formatted campaign brief from rough notes.

10 minMarketingClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-f1fouzqt.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-iw1rj94h.png)

## Set up

### Try a plugin

The Marketing plugin ships with `/campaign-plan` and other campaign-planning skills as a starting point, already structured around objective, audience, message, and metrics. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

MarketingCreate content, plan campaigns, and analyze performance across marketing channels. Maintain brand voice consistency, track competitors, and report on what's working.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=marketing)

`/campaign-plan`Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics.

[Run](claude://cowork/new?q=%2Fcampaign-plan)

`/draft-content`Draft blog posts, social media, email newsletters, landing pages, press releases, and case studies with channel-specific formatting and SEO recommendations.

[Run](claude://cowork/new?q=%2Fdraft-content)

Show all 7 skills

### Connect your tools

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23000'%20d='M4.46%204.44c.74.6%201.02.56%202.42.46l13.18-.79c.28%200%20.05-.28-.05-.32l-2.19-1.58c-.42-.33-.98-.7-2.05-.6L2.99%202.53c-.46.05-.56.28-.37.46l1.84%201.45Zm.8%203.1v13.87c0%20.74.37%201.02%201.21.98l14.49-.84c.84-.05.93-.56.93-1.16V6.6c0-.6-.23-.93-.74-.88l-15.14.88c-.56.05-.75.33-.75.93Zm14.3.74c.1.42%200%20.84-.42.89l-.7.14v10.24c-.6.33-1.16.51-1.63.51-.74%200-.93-.23-1.49-.93l-4.56-7.16v6.93l1.44.33s0%20.84-1.16.84l-3.21.18c-.1-.18%200-.65.33-.74l.84-.23V9.98l-1.16-.1c-.1-.42.14-1.02.79-1.07l3.44-.23%204.75%207.25V9.42l-1.21-.14c-.1-.51.28-.88.74-.93l3.21-.18Z'/%3e%3c/svg%3e)

Notion

[Connect](https://claude.ai/desktop/directory/notion)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder

Drag the files you'll use (the strategy notes, your brief template, the brand guidelines, last quarter's best brief) into one folder on your machine, then point Cowork at it. Cowork reads from it and writes the formatted brief and deck back to it. If you'll spin up campaigns regularly, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from the parent Campaigns folder so the template and brand voice stay attached.

Campaigns / Spring-Launch

strategy-notes.docxApr 24, 202622 KB

brand-guidelines-2026.pdfJan 8, 20262.1 MB

brief-template.docxFeb 3, 202618 KB

In Cowork’s chat bar:Campaigns / Spring-Launch

## The prompt

### Copy this into Claude Cowork

Turn the strategy notes into a formatted campaign brief: objective, audience, key message, channel plan, timeline, and success metrics. Then build a short deck from the brief to walk the team through at kickoff. Keep the voice consistent with our brand guidelines.

Campaigns / Spring-LaunchOpen in Cowork

### Why this works

Prompt

**Name the sections.** Listing objective, audience, message, channels, timeline, and metrics up front means the brief follows your template, not a generic outline reviewers have to remap.

Prompt

**Ask for both deliverables at once.** "Build a short deck from the brief" gets you the kickoff artifact in the same pass, so the brief and the slides tell exactly the same story.

Source

**Point to your style guide.** "Consistent with our brand guidelines" points at the file in the folder, so headlines and copy come back sounding like you, not like a template.

Source

**Let the working folder supply context.** Strategy notes, template, and brand guide sit in the working folder, so the brief and deck are written back next to the source and the campaign folder is complete from day one.

### Get a better draft

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask for options.** Add "draft three versions with different angles" and pick the one that works best, or mix the best lines.

## Make Cowork work for you

A plugin skill is a starting point — customize it with your own practices and expertise. A few minutes of conversation and it runs with your standards from then on.

Make what we've done in this task so far into a skill, or edit the /campaign-plan skill with my feedback.

CampaignsOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable

### Run it on every new campaign

Strategy notes get dropped, the brief should already be drafting. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and the customized skill runs every weekday morning against any new strategy-notes files in Campaigns.

**/schedule** Weekdays at 9 am, check Campaigns for new strategy-notes files and run /campaign-plan on each one, writing the brief and kickoff deck to a subfolder named for the campaign.

CampaignsOpen in Cowork

Scheduled taskActive

Campaign brief from strategy notes

Checks Campaigns each weekday morning for new strategy-notes files, runs `/campaign-plan` on each, and writes the brief and deck to a campaign subfolder.

Every **weekday at 9 am — Campaigns folder**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates

Your customized `/campaign-plan` now carries your template, your brand voice, and your metrics framework. Share it so every campaign owner starts from the same structure, and stakeholders see one consistent brief format no matter who runs the program.

Share the skill

In Cowork, open **Skills** → `/campaign-plan` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill with your template and voice baked in, so they don't repeat Steps 1-3.

## Going forward

### Now in your Cowork

Your processes

Marketing plugin

Your tools

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)Google Drive![](data:image/svg+xml,%3csvg%20viewBox='0%200%2024%2024'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20fill='%23000'%20d='M4.46%204.44c.74.6%201.02.56%202.42.46l13.18-.79c.28%200%20.05-.28-.05-.32l-2.19-1.58c-.42-.33-.98-.7-2.05-.6L2.99%202.53c-.46.05-.56.28-.37.46l1.84%201.45Zm.8%203.1v13.87c0%20.74.37%201.02%201.21.98l14.49-.84c.84-.05.93-.56.93-1.16V6.6c0-.6-.23-.93-.74-.88l-15.14.88c-.56.05-.75.33-.75.93Zm14.3.74c.1.42%200%20.84-.42.89l-.7.14v10.24c-.6.33-1.16.51-1.63.51-.74%200-.93-.23-1.49-.93l-4.56-7.16v6.93l1.44.33s0%20.84-1.16.84l-3.21.18c-.1-.18%200-.65.33-.74l.84-.23V9.98l-1.16-.1c-.1-.42.14-1.02.79-1.07l3.44-.23%204.75%207.25V9.42l-1.21-.14c-.1-.51.28-.88.74-.93l3.21-.18Z'/%3e%3c/svg%3e)Notion

Your workspace

Campaigns

You start each campaign with a brief and kickoff deck already drafted in your template and voice — ready to review instead of write.

[Next: Create on-brand content](https://academy.claude.com/use-cases/on-brand-content)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
