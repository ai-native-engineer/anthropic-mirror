<!-- source: https://academy.claude.com/use-cases/ask-the-company -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Build an 'Ask the Company' agent

Plain-English answers over your wiki, code, and warehouse.

10 minEngineeringClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-mjmk2gjq.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-bpm7r9eg.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Engineering plugin ships with `/documentation` as a starting point, already structured to fan out across connected sources, cite what it finds, and name an owner when it's not sure. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

EngineeringStreamline engineering workflows — standups, code review, architecture decisions, incident response, and technical documentation. Works with your existing tools or standalone.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=engineering)

`/documentation`Write and maintain technical documentation.

[Run](claude://cowork/new?q=%2Fdocumentation)

`/architecture`Create or evaluate an architecture decision record (ADR).

[Run](claude://cowork/new?q=%2Farchitecture)

Show all 10 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/9d4cebe262b9da95.svg)'%20d='M.87%2018.26c-.25.4-.52.87-.75%201.23a.75.75%200%200%200%20.25%201.02l4.96%203.05a.75.75%200%200%200%201.04-.25c.2-.33.45-.76.73-1.21%201.95-3.22%203.91-2.83%207.45-1.14l4.92%202.34a.75.75%200%200%200%201-.36l2.36-5.34a.75.75%200%200%200-.38-.98c-1.04-.49-3.1-1.46-4.96-2.36-6.68-3.24-12.36-3.03-16.62%204Z'/%3e%3cpath%20fill='url(%23cfB)'%20d='M23.13%205.74c.25-.4.52-.87.75-1.23a.75.75%200%200%200-.25-1.02L18.67.44a.75.75%200%200%200-1.04.25c-.2.33-.45.76-.73%201.21-1.95%203.22-3.91%202.83-7.45%201.14L4.53.7a.75.75%200%200%200-1%20.36L1.17%206.4a.75.75%200%200%200%20.38.98c1.04.49%203.1%201.46%204.96%202.36%206.68%203.24%2012.36%203.03%2016.62-4Z'/%3e%3c/svg%3e)

Confluence

Search the wiki and runbooks for the documented answer first. Confluence access comes through the Atlassian Rovo connector (Jira and Confluence).

[Connect](https://claude.ai/desktop/directory/atlassian)

![](images/92b68e492ad6094d.svg)

GitHub

Read code, READMEs, and CODEOWNERS to answer "how does X work" and "who owns X."

[Connect](https://claude.ai/desktop/directory/github)

![](https://academy.claude.com/assets/v1/snowflake-f7euzg40.svg)

SnowflakeOptional

Query the warehouse for "how many" and "why did the metric move" questions.

[Connect](https://claude.ai/desktop/directory/snowflake)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

Drag the files that anchor the agent (your service catalog export, the team directory, the glossary, the "where to find things" onboarding doc) into one folder and point Cowork at it. These become the routing table the agent consults before searching anywhere else. [Create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) from that folder so the catalog and ground rules stay attached as the agent evolves.

Platform / ask-company

service-catalog.yamlApr 18, 202694 KB

glossary.mdMar 2, 202611 KB

team-directory.mdApr 1, 20266 KB

In Cowork’s chat bar:Platform / ask-company

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Build an internal "ask anything" agent for engineers. When someone asks "how do I get a staging API key," "what owns the orders table," or "why did deploys slow down last month," find the answer across our systems, cite the source, and tell them who to ask if you're not sure. Get one good answer first, then turn it into a shared skill.

Platform / ask-companyOpen in Cowork

### Why this works[](#why-this-works)

Prompt

**Give an example for each question type.** A how-to, an ownership lookup, a metric why: covers the question types engineers actually ask.

Prompt

**Cite the source, every time.** Engineers trust the link, not the prose; citations make the answer verifiable.

Prompt

**Name an owner when unsure.** Asking for "the owning team or channel" gives Claude something to fall back on when it's not confident. You get a pointer to follow up on instead of a guess to verify.

Source

**Put reference docs in the working folder.** Service catalog and team directory tell Cowork where to look and who to point to.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you[](#make-cowork-work-for-you)

The plugin's `/documentation` is a generic starting point. Once Step 2 answers your three questions well, tell Cowork to write your version of the skill. Layer in which spaces and repos to search first, the "I'm not sure" threshold, the tone, and the systems that are off-limits. A few minutes of conversation and the skill speaks your stack from then on.

Make what we've done in this task so far into a skill, or edit the /documentation skill with my feedback.

Platform / ask-companyOpen in Cowork

**Tip:** tell Claude to edit the skill for you.

## Make it repeatable[](#make-it-repeatable)

### Make it a live artifact[](#make-it-a-live-artifact)

Once the agent answers your test questions well, publish it as a live artifact so anyone in the org has one link to ask. The artifact runs the shared skill behind the scenes; the platform team owns the skill and keeps tuning it.

### Log every question it couldn't answer[](#log-every-question-it-couldnt-answer)

The agent gets better when you know where it falls short. Type `/schedule` or open **Scheduled** in the Cowork sidebar, and a weekly run writes the unanswered questions to your folder so the platform team can fill the gaps.

**/schedule** Every Friday at 4pm, list the questions /documentation couldn't confidently answer this week, group them by topic, and write them to Platform/ask-company/gaps-<week>.md with a suggested owner for each.

Platform / ask-companyOpen in Cowork

Scheduled taskActive

Ask-company gap report

Weekly, lists the questions the agent couldn't answer, groups them by topic, and writes a gap report with suggested owners.

Every **Friday at 4:00pm**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

Your customized `/documentation` now carries your sources, your routing table, and your confidence rules. Share it workspace-wide so every engineer asks the company the same way, and the answer to "how do I…" stops depending on who's in the channel.

Share the skill

In Cowork, open **Skills** → `/documentation` → **Share** and pick your whole workspace. Everyone gets the same front door to wiki, code, and warehouse, with the platform team keeping it tuned.

## What changes for the org[](#what-changes-for-the-org)

Internal questions get a sourced answer from across your wiki, code, and warehouse, with an owner named when the agent isn't certain. Engineers check one response instead of searching each system.

You did this for everyday engineering questions. The same approach covers on-call runbook lookup, data-catalog search, and new-hire onboarding — each one becomes a skill in your team's shared plugin.

[Next: Write the design doc or RFC](https://academy.claude.com/use-cases/design-doc)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [What changes for the org](#what-changes-for-the-org)
