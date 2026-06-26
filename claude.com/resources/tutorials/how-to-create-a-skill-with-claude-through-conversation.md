<!-- source: https://claude.com/resources/tutorials/how-to-create-a-skill-with-claude-through-conversation -->

# How to create a skill with Claude through conversation

Learn how to create Claude Skills through natural conversation by describing workflows and having Claude structure them into reusable formats.

  Professional
* Product

  Claude.ai
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/how-to-create-a-skill-with-claude-through-conversation

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6940879838595598d35b8db0_Screenshot%202025-12-15%20at%202.11.23%E2%80%AFPM.png)

With Skills, you are able to teach Claude specific workflows, tools, and processes. By creating a skill, you're giving Claude a playbook it can reference whenever you need a particular type of help—whether that's generating reports in your company's format, cleaning and using data the way you normally do, or pulling and analyzing CRM data your way.

‍  
There are two paths for creating skills. You can create skills by writing the files yourself for full control over structure and implementation. See [*How to create custom skills*](https://support.claude.com/en/articles/12512198-creating-custom-skills) *and* [*Skills authoring best practices*](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices) for that approach.

‍  
This guide focuses on the other path: creating skills through conversation with Claude. You describe your process naturally, and Claude handles the formatting and structure. This approach makes Skills accessible to anyone, regardless of technical background.

‍  
​*New to skills? See* [*What are Skills*](https://support.claude.com/en/articles/12512176-what-are-skills) *and* [*Skills user guide*](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills) to get started learning about Skills.

‍

## Creating a skill through conversation

Creating a skill with Claude means having a conversation where you explain your approach and share any materials you want included. Claude translates this into a properly formatted skill that can work in future chats.

#### 1. Start a conversation

Open a new chat and say something like "I want to create a skill for quarterly business reviews" or "I need a skill that knows how to analyze customer feedback."  
  
If you have materials that show your approach—templates you use, examples of work you're proud of, brand guidelines you follow, data files you reference—upload them. You can also mention any connected tools Claude should use. If you are unsure of what else to include, ask Claude for guidance.

#### 2. Answer Claude's questions

Claude will ask about your process. Provide enough detail that someone capable but unfamiliar could follow your approach.​

You'll get questions about concrete usage ("Can you give examples of when you'd use this skill?") or about your process ("What makes output good for this type of work?").

#### 3. Claude builds the Skill

In Claude's thinking, you will see it read a *skill-creator* skill to follow best practices in creating a properly structured skill*.* Claude will create a SKILL.md file (the instruction file every skill needs), organize any materials you've provided, and generate code for operations you've described that need to happen consistently. Claude then packages everything into a skill file.

#### 4. Activate and test the skill

Save the the skill file that Claude creates. In [Settings > Capabilities > Skills](https://claude.ai/settings/capabilities), you can view your library of skills and turn them on or off as needed.

Try using your skill by describing a task the skill should address. See if Claude recognizes the situation (you'll see "Using [skill name]" in Claude's thinking) and whether it produces the expected outcome. If something's off, ask Claude to update the skill with your desired changes. Repeat this process until your skill works effectively.

## Skills you can build

You can build skills for a range of tasks. Skills can capture how your organization works, enable specialized expertise you don't personally have, or work together to handle complex workflows.

* **CRM automation skill:** creates contacts, updates opportunities, maintains data standards to eliminate repetitive entry**‍**
* **Legal contract review skill:** evaluates agreements against standard terms, identifies risky clauses, suggests protective language**‍**
* **Sprint planning skill:** calculates team velocity, estimates work accounting for patterns, allocates capacity, generates planning docs**‍**
* **SEO content skill:** analyzes opportunities, structures for search intent, optimizes while maintaining brand voice**‍**
* **Music composition skill:** creates original tracks with realistic instruments, applies genre conventions, exports for production**‍**
* **Report automation skill:** gathers monthly data, applies calculations, generates visualizations, formats in template, distributes to stakeholders**‍**
* **Skill reviewer skill:** evaluates another skill's effectiveness, suggests improvements to instructions, identifies missing edge cases, recommends structure changes

## What you can include within a skill

Skills bundle three types of content together—instructions, reference materials, and scripts. Knowing these components helps you articulate what you need when creating a skill with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6940871eecee99bd9e66f05a_380d5eae-c159-4643-80e3-ce1be19b6d57.png)

#### ​Instructions

**‍**Every skill needs a SKILL.md file that explains your process. When asking Claude to create a skill, describe your process for Claude to structure it into proper instructions. At the top of your [SKILL.md](http://skill.md/) file, will be the skill's name and what it does. Claude scans this information first to decide whether or not to load and use the full skill during your conversations. Below that are clear instructions on how to do the task.

#### Reference materials and assets

Sometimes instructions alone aren't enough and Claude needs actual files to reference or use in the output. To include these, upload any relevant files or information when creating your Skill. Claude determines whether to embed guidance in the SKILL.md instructions or bundle it as a reference file.

* **Brand assets:** font files, logos, color palettes, design templates**‍**
* **Reference documents:** policy guides, workflow procedures, database schemas**‍**
* **Templates:** spreadsheet with formulas, presentation layouts, document styles**‍**
* **Data files:** CSV lookup tables, JSON configurations, pricing databases**‍**
* **Media files:** audio samples, images, video clips

#### Scripts

**‍**These are executable code files that Claude can run to handle complex operations more reliably than instructions alone. You don't need to write these yourself. When you describe tasks that need scripts, Claude recognizes them and creates the code automatically. Examples include:

* **Data work** for tasks like cleaning data, running calculations, and creating charts or dashboards**‍**
* **Document work** to handle file processing tasks like batch editing and applying formatting**‍**
* **Integrations** to connect your skill to other tools you use, such fetching data from external sources**‍**
* **Media processing** to transform images, edit videos, and generate audio

## Additional Resources

#### Getting started

* [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)[‍](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)
* [Teach Claude your way of working using skills](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)

#### Going deeper

* [Help Center: How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)[‍](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)
* [Skill authoring best practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices) [‍](https://github.com/anthropics/claude-cookbooks/tree/main/skills)
* [Skill cookbooks](https://github.com/anthropics/claude-cookbooks/tree/main/skills)[‍](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
* [Agent skills overview](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)

## Related tutorials

[Tasks to try with @Claude in your workspace](/resources/tutorials/tasks-to-try-with-claude-tag-in-your-workspace)Tasks to try with @Claude in your workspace

Tasks to try with @Claude in your workspace

Tutorial

[Tutorial](/resources/tutorials/tasks-to-try-with-claude-tag-in-your-workspace)Tutorial

[Best practices for using @Claude](/resources/tutorials/best-practices-using-claude-tag)Best practices for using @Claude

Best practices for using @Claude

Tutorial

[Tutorial](/resources/tutorials/best-practices-using-claude-tag)Tutorial

[Using Claude Cowork for legal: answer fast questions on past decisions](/resources/tutorials/using-claude-cowork-for-legal-question-briefing)Using Claude Cowork for legal: answer fast questions on past decisions

Using Claude Cowork for legal: answer fast questions on past decisions

Tutorial

[Tutorial](/resources/tutorials/using-claude-cowork-for-legal-question-briefing)Tutorial

[Using Claude Cowork for marketing ops: run a weekly review that preps itself](/resources/tutorials/using-claude-cowork-for-marketing-ops-review)Using Claude Cowork for marketing ops: run a weekly review that preps itself

Using Claude Cowork for marketing ops: run a weekly review that preps itself

Tutorial

[Tutorial](/resources/tutorials/using-claude-cowork-for-marketing-ops-review)Tutorial
