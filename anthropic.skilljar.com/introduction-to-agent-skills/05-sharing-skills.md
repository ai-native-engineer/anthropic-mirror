<!-- https://anthropic.skilljar.com/introduction-to-agent-skills/434529 -->

**What you'll learn**

*Estimated time: 20 minutes*

By the end of this lesson you'll be able to:

* *Share skills with your team by committing them to a Git repository*
* *Distribute skills across projects through plugins and marketplaces*
* *Deploy skills organization-wide using enterprise managed settings*
* *Configure custom subagents to use specific skills*

## Sharing skills

*(4 minutes)*

Skills become much more valuable when they're shared across a team or organization. This video covers the three main distribution methods — repository commits, plugins, and enterprise managed settings — and explains how to configure custom subagents to use skills. You'll learn which approach fits which scenario and how to handle an important gotcha: subagents don't inherit skills automatically.

#### Key takeaways

* **Project skills** in `.claude/skills` are shared automatically through Git — anyone who clones the repo gets them
* **Plugins** let you distribute skills across repositories via marketplaces for broader community use
* **Enterprise managed settings** deploy skills organization-wide with the highest priority, ideal for mandatory standards and compliance
* **Subagents don't automatically see your skills** — you must explicitly list skills in a custom agent's frontmatter `skills` field
* Built-in agents (Explorer, Plan, Verify) **can't access skills at all** — only custom subagents defined in `.claude/agents` can

Skills become much more valuable when they're shared. A PR review skill that only you use is helpful, but that same skill shared across your entire team standardizes code review and creates a consistent experience across your organization. Let's look at the different ways you can distribute skills.

## Committing Skills to Your Repository

The simplest sharing method is committing skills directly to your repository. Place them in `.claude/skills`, and anyone who clones the repo gets those skills automatically — no extra installation needed.

When you push updates, everyone gets them on the next pull. This approach works well for:

* Team coding standards
* Project-specific workflows
* Skills that reference your codebase structure

The `.claude` directory contains your agents, hooks, skills, and settings — all version-controlled and shared with the team through normal Git workflows.

## Distributing Skills Through Plugins

Plugins are a way to extend Claude Code with custom functionality designed to be shared across teams and projects. In your plugin project, create a `skills` directory that follows a similar file structure to the `.claude` directory — each skill gets its own folder with a `SKILL.md` file inside.

After you distribute your plugin to a marketplace, other users can discover and install it into Claude Code for themselves.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1771527270%2FSkills5_07.1771527270067.png)

This approach is best when your skills aren't too project-specific and can be useful to community members beyond your immediate team.

## Enterprise Deployment Through Managed Settings

Administrators can deploy skills organization-wide through managed settings. Enterprise skills take the highest priority — they override personal, project, and plugin skills with the same name.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1771527270%2FSkills5_08.1771527270381.png)

The managed settings file supports features like `strictKnownMarketplaces` to control where plugins can be installed from:

```
"strictKnownMarketplaces": [ { "source": "github", "repo": "acme-corp/approved-plugins" }, { "source": "npm", "package": "@acme-corp/compliance-plugins" } ]
```

This is the right choice for mandatory standards, security requirements, compliance workflows, and coding practices that *must* be consistent across the organization. The keyword here is "must."

## Skills and Subagents

Here's something that surprises people: subagents don't automatically see your skills. When you delegate a task to a subagent, it starts with a fresh, clean context.

There are important distinctions to understand:

* **Built-in agents** (like Explorer, Plan, and Verify) can't access skills at all
* **Custom subagents** you define *can* use skills, but only when you explicitly list them
* Skills are loaded when the subagent starts, not on demand like in the main conversation

To create a custom subagent with skills, add an agent markdown file in `.claude/agents`. You can use the `/agents` command in Claude Code to create one interactively:

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1771527270%2FSkills5_13.1771527270779.png)

The generated agent file includes a `skills` field that lists which skills to load. Here's what the frontmatter looks like:

```
--- name: frontend-security-accessibility-reviewer description: "Use this agent when you need to review frontend code for accessibility..." tools: Bash, Glob, Grep, Read, WebFetch, WebSearch, Skill... model: sonnet color: blue skills: accessibility-audit, performance-check ---
```

When you delegate to this subagent, it has both skills loaded and applies them to every review. First make sure the skills exist in your `.claude/skills` directory, then either create a new subagent or add the `skills` field to an existing agent's markdown file.

This pattern works really well when:

* You want isolated task delegation with specific expertise
* Different subagents need different skills (frontend reviewer vs. backend reviewer)
* You want to enforce standards in delegated work without relying on prompts

## Lesson reflection

* Which sharing method (repository, plugin, enterprise) makes the most sense for the skills you've been thinking about building?
* Do you have workflows where custom subagents with specific skills would improve consistency in delegated work?

## What's next

In the final lesson, you'll learn how to troubleshoot common skill issues — from skills that don't trigger, to priority conflicts, to runtime errors — with a practical checklist you can reference anytime.

#### Feedback

As you progress through the course, we'd love to hear how you're using skills in your work, plus any feedback you may have. Share your feedback [here](https://forms.gle/RvHPBwQt9ZmcDc1P9).

<!-- youtube: OCBi3eScNLk -->

[![Sharing Skills](https://img.youtube.com/vi/OCBi3eScNLk/hqdefault.jpg)](https://www.youtube.com/watch?v=OCBi3eScNLk)

<details>
<summary>자막: Sharing Skills</summary>

Skills become more valuable when shared. A PR review skill that only you use is helpful. The same skill shared across your team standardizes code review and provides a consistent experience amongst your organization which much better. Here are ways you can share your skills. Now the simplest sharing method is committing skills to your repository. Place them include/skills. Anyone who clones a repository gets these skills automatically. No extra installation. It's just what you're doing already. When you push update, everyone gets them on the next poll. This works well for team coding standards, project specific workflows, skills that reference your codebase structure. Another way you can distribute your skills is through plugins. Think of plugins as ways to extend cloud code with custom functionality, but designed to be shared across teams and projects. In your plug-in project, create a directory called skills. This will then follow a similar file structure to the cloud directory in our project with the name of the skill with a skill.md file. And after you distribute your plugin to a marketplace, other users can download it into cloud codes for themselves to use. This is best if your skills have functionality that isn't too project specific and can be used by community members. Administrators can deploy skills organizationwide through managed settings. Enterprise skills take highest priority. Like we discussed before, they override personal project and plug-in skills with the same name. This is for mandatory standards, security requirements, compliance workflows, coding practices that must be consistent across the organization. Keyword must. Here's something that surprises people. Sub agents don't automatically see your skills. Yeah, when you delegate a task to a sub agent, it starts with a fresh, clean context. Built-in agents like the explorer, plan, and verify can't access skills at all. Only custom sub agents you define can use them and only when you explicitly list them. To create a custom sub agent with skills, add an agent.mmd file include/ aents. The skills field lists which skills to load. These skills are loaded when the sub aent starts, not in demand like in the main conversation. So take that into consideration. First ensure the skills exist. Okay, it exists. Then create the sub agent using the claw code sub aent creator. If you have a sub agent that you want to add these skills to already just go to the existing agent.md file. Then after that create the skills fields and add your skills. When you delegate to the sub agent it has both skills loaded and applies them to every single review. Now this pattern works really well when you want isolated task delegation with specific expertise. Different sub agents need different skills. Front-end reviewer versus back-end reviewer. You want to enforce standards and delegated work without relying on prompts. Only list skills that are always relevant to the subage's purpose. Share skills through project directories for team access, plugins for cross repository distribution, or enterprise deployment for organizationwide standards. Sub agents don't inherit skills automatically, so list them explicitly in the sub agents skills field. Built-in agents can't access skills. Only custom sub agents can in your claw/ agents. Skills load when the sub agents start, so only list skills that are always relevant to its purpose.

</details>
