<!-- source: https://claude.com/skills -->

# Teach Claude your way of working

Turn your expertise, procedures, and best practices into reusable capabilities so Claude can apply them automatically, every time.

[Start using skills](https://claude.ai/settings/capabilities)

[![](https://assets.claude.com/85aca3edcc57aadbb9259395ad06959d43540ffd.png)](https://assets.claude.com/3ec626bfee08f251c31203f17f02c5c032213ffe.webm)

## Expert output, every time

### Get consistent results on specialized tasks

Skills give Claude details on how you want to create documents, analyze data, and automate workflows, so you get consistent outputs every time.

### Capture what your organization knows

Package your company’s procedures, best practices, and institutional knowledge so teams work consistently and new members get expert-level results from day one.

### Build once, use everywhere

The same skill runs across Claude.ai, Claude Code, and the API without needing to modify for each platform.

### Stack skills for complex work

Combine skills for multi-step workflows. Claude uses what’s needed, when it’s needed—no manual selection required.

## How teams use skills

Claude comes with built-in skills for common workflows. You can add your organization’s procedures, or build your own from scratch.

### Built-in workflows

Claude can handle the essentials every team needs.

* Create Excel sheets with working formulas, Powerpoints with your branding, and more
* Analyze and visualize your own data
* Convert and transform files between formats

### Company-specific skills

Package your organization’s knowledge so everyone gets consistent results.

* Apply brand guidelines or follow preferred formats in docs, meetings notes, and more
* Use [pre-built skills for financial services (opens in new tab)](https://claude.com/solutions/financial-services), like DCF modeling and comps analysis
* Create industry-specific workflows, like healthcare documentation or compliance procedures

### Individual workflows

Create skills for how you personally work.

* Build custom note-taking systems
* Make your own development workflows
* Create research and analysis methods for Claude to follow

Equipping agents for the real world with Agent Skills

![](https://assets.claude.com/d122b162b8d58ed01ce613dc0ce87ae415ebfa62.jpg)

Introducing Agent Skills, a new way to build specialized agents using files and folders.

[Read more (opens in new tab)](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

Improving frontend design through Skills

![](https://assets.claude.com/ac15277f0d2cacd9cf9fd4244fc28dfe7e5e6819.jpg)

Best practices for building richer, more customized frontend design with Claude and Skills.

[Read more](https://claude.com/blog/improving-frontend-design-through-skills)

## Create your own

![A visual example of a user asking Claude to help create a skill in the Claude platform. Claude uses the Skill Creator Skill to create a Sales Call Prep skill based on a previous conversation.](https://assets.claude.com/572b84df17db14b777351330da9080808c60a0c7.jpg)

### Try the skill-creator skill

Describe what you want, and Claude generates the folder structure, formats the SKILL.md file, and bundles your resources.

[Create a skill](https://claude.ai/settings/capabilities)

```
---
name: internal-comms
description: A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).
license: Complete terms in LICENSE.txt
---
## When to use this skill
To write internal communications, use this skill for:
- 3P updates (Progress, Plans, Problems)
- Company newsletters
- FAQ responses
- Status reports
- Leadership updates
- Project updates
- Incident reports
## How to use this skill
To write any internal communication:
1. **Identify the communication type** from the request
2. **Load the appropriate guideline file** from the `examples/` directory:
    - `examples/3p-updates.md` - For Progress/Plans/Problems team updates
    - `examples/company-newsletter.md` - For company-wide newsletters
    - `examples/faq-answers.md` - For answering frequently asked questions
    - `examples/general-comms.md` - For anything else that doesn't explicitly match one of the above
3. **Follow the specific instructions** in that file for formatting, tone, and content gathering
If the communication type doesn't match any existing guideline, ask for clarification or more context about the desired format.
## Keywords
3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms
```

### Develop your own SKILL.md file

For developers who want full control, skills are just folders with a SKILL.md file containing instructions in Markdown. Add reference files, executable scripts, or code—whatever Claude needs to do the job.

[Read developer docs (opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)

![Notion](https://assets.claude.com/19e0cdfaef9d2980bddd19cd993076d62b46c0c7.svg)

> “With Skills, Claude works seamlessly with Notion - taking users from questions to action faster. Less prompt wrangling on complex tasks, more predictable results.”

MJ Felix, Product Manager

![Rakuten](https://assets.claude.com/5463fa5a44d12868ceec5ae30bfc8c412cafdeae.svg)

> “Skills streamline our management accounting and finance workflows. Claude processes multiple spreadsheets, catches critical anomalies, and generates reports using our procedures. What once took a day, we can now accomplish in an hour.”

Yusuke Kaji, General Manager AI

![Canva](https://assets.claude.com/f047885ca3dadf9a16509752ef150ebb9bd424bb.svg)

> “Canva plans to leverage Skills to customize agents and expand what they can do. This unlocks new ways to bring Canva deeper into agentic workflows—helping teams capture their unique context and create stunning, high-quality designs effortlessly.”

Anwar Haneef, GM & Head of Ecosystem

![Figma](https://assets.claude.com/30df15cbd261edbc52262a1fa2d1339f3a1a372b.svg)

> “Skills guide how Claude works in the design canvas, bringing consistency and reliability to agent workflows in Figma. Teams can use Claude to build Figma assets that stay true to their craft and vision, and move fluidly between code and the canvas—without losing context.”

Matt Colyer, Director of Product

![Box](https://assets.claude.com/f7051ef3388f6fcd83051cffcba21499a021e446.svg)

> “Skills teaches Claude how to work with Box content. Users can transform stored files into PowerPoint presentations, Excel spreadsheets, and Word documents that follow their organization's standards—saving hours of effort.”

Yashodha Bhavnani, Head of AI

![Notion](https://assets.claude.com/19e0cdfaef9d2980bddd19cd993076d62b46c0c7.svg)

> “With Skills, Claude works seamlessly with Notion - taking users from questions to action faster. Less prompt wrangling on complex tasks, more predictable results.”

MJ Felix, Product Manager

![Rakuten](https://assets.claude.com/5463fa5a44d12868ceec5ae30bfc8c412cafdeae.svg)

> “Skills streamline our management accounting and finance workflows. Claude processes multiple spreadsheets, catches critical anomalies, and generates reports using our procedures. What once took a day, we can now accomplish in an hour.”

Yusuke Kaji, General Manager AI

![Canva](https://assets.claude.com/f047885ca3dadf9a16509752ef150ebb9bd424bb.svg)

> “Canva plans to leverage Skills to customize agents and expand what they can do. This unlocks new ways to bring Canva deeper into agentic workflows—helping teams capture their unique context and create stunning, high-quality designs effortlessly.”

Anwar Haneef, GM & Head of Ecosystem

![Figma](https://assets.claude.com/30df15cbd261edbc52262a1fa2d1339f3a1a372b.svg)

> “Skills guide how Claude works in the design canvas, bringing consistency and reliability to agent workflows in Figma. Teams can use Claude to build Figma assets that stay true to their craft and vision, and move fluidly between code and the canvas—without losing context.”

Matt Colyer, Director of Product

![Box](https://assets.claude.com/f7051ef3388f6fcd83051cffcba21499a021e446.svg)

> “Skills teaches Claude how to work with Box content. Users can transform stored files into PowerPoint presentations, Excel spreadsheets, and Word documents that follow their organization's standards—saving hours of effort.”

Yashodha Bhavnani, Head of AI

![Notion](https://assets.claude.com/19e0cdfaef9d2980bddd19cd993076d62b46c0c7.svg)

> “With Skills, Claude works seamlessly with Notion - taking users from questions to action faster. Less prompt wrangling on complex tasks, more predictable results.”

MJ Felix, Product Manager

1/5

## More resources

[A complete guide to building skills for Claude

Blog](https://claude.com/blog/complete-guide-to-building-skills-for-claude)

[Skills explained: How Skills compares to prompts, Projects, MCP, and subagents

Blog](https://claude.com/blog/skills-explained)

[How to create Skills: Key steps, limitations, and examples

Blog](https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples)

Skills | Claude by Anthropic
