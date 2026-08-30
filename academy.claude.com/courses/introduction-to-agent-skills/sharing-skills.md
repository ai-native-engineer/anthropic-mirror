<!-- source: https://academy.claude.com/courses/introduction-to-agent-skills/sharing-skills -->

Lesson 5 of 6 · Introduction to agent skillsSharing skills

3. /[Introduction to agent skills](https://academy.claude.com/courses/introduction-to-agent-skills)

[Introduction to agent skills](https://academy.claude.com/courses/introduction-to-agent-skills)

# Sharing skills

Lesson 515 min

In this lessonBy the end, you’ll be able to

* Share skills with your team by committing them to a Git repository
* Distribute skills across projects through plugins and marketplaces
* Deploy skills organization-wide using enterprise managed settings
* Configure custom subagents to use specific skills

## Sharing skills[](#sharing-skills)

Sharing skills · 4 min

SummaryTranscript

Skills become much more valuable when they're shared across a team or
organization. This video covers the three main distribution methods —
repository commits, plugins, and enterprise managed settings — and explains
how to configure custom subagents to use skills. You'll learn which
approach fits which scenario and how to handle an important gotcha:
subagents don't inherit skills automatically.

## Key takeaways[](#key-takeaways)

* **Project skills** in `.claude/skills` are shared automatically through Git — anyone who clones the repo gets them
* **Plugins** let you distribute skills across repositories via marketplaces for broader community use
* **Enterprise managed settings** deploy skills organization-wide with the highest priority, ideal for mandatory standards and compliance
* **Subagents don't automatically see your skills** — you must explicitly list skills in a custom agent's frontmatter `skills` field
* Built-in agents (Explorer, Plan, Verify) **can't access skills at all** — only custom subagents defined in `.claude/agents` can

Skills become much more valuable when they're shared. A PR review skill that only you use is helpful, but that same skill shared across your entire team standardizes code review and creates a consistent experience across your organization. Let's look at the different ways you can distribute skills.

## Committing Skills to Your Repository[](#committing-skills-to-your-repository)

The simplest sharing method is committing skills directly to your repository. Place them in `.claude/skills`, and anyone who clones the repo gets those skills automatically — no extra installation needed.

When you push updates, everyone gets them on the next pull. This approach works well for:

* Team coding standards
* Project-specific workflows
* Skills that reference your codebase structure

The `.claude` directory contains your agents, hooks, skills, and settings — all version-controlled and shared with the team through normal Git workflows.

## Distributing Skills Through Plugins[](#distributing-skills-through-plugins)

Plugins are a way to extend Claude Code with custom functionality designed to be shared across teams and projects. In your plugin project, create a `skills` directory that follows a similar file structure to the `.claude` directory — each skill gets its own folder with a `SKILL.md` file inside.

After you distribute your plugin to a marketplace, other users can discover and install it into Claude Code for themselves.

![](https://academy.claude.com/assets/media/de5659fdb86772a1528fe14df72a785694c848f4e93e5047ff4ce0f448fe874f.png)

This approach is best when your skills aren't too project-specific and can be useful to community members beyond your immediate team.

## Enterprise Deployment Through Managed Settings[](#enterprise-deployment-through-managed-settings)

Administrators can deploy skills organization-wide through managed settings. Enterprise skills take the highest priority — they override personal, project, and plugin skills with the same name.

![](https://academy.claude.com/assets/media/2373313fe9e584333d54a9b2fced74895f23601919dfee21fc676e9f61ab2d74.png)

The managed settings file supports features like `strictKnownMarketplaces` to control where plugins can be installed from:

json

```
"strictKnownMarketplaces": [
  {
    "source": "github",
    "repo": "acme-corp/approved-plugins"
  },
  {
    "source": "npm",
    "package": "@acme-corp/compliance-plugins"
  }
]
```

This is the right choice for mandatory standards, security requirements, compliance workflows, and coding practices that *must* be consistent across the organization. The keyword here is "must."

## Skills and Subagents[](#skills-and-subagents)

Here's something that surprises people: subagents don't automatically see your skills. When you delegate a task to a subagent, it starts with a fresh, clean context.

There are important distinctions to understand:

* **Built-in agents** (like Explorer, Plan, and Verify) can't access skills at all
* **Custom subagents** you define *can* use skills, but only when you explicitly list them
* Skills are loaded when the subagent starts, not on demand like in the main conversation

To create a custom subagent with skills, add an agent markdown file in `.claude/agents`. You can use the `/agents` command in Claude Code to create one interactively:

![](https://academy.claude.com/assets/media/dc6b8b0e1a6076788a757058dc8e5af5ef8de682b5e2102d7ff72e6c774d845e.png)

The generated agent file includes a `skills` field that lists which skills to load. Here's what the frontmatter looks like:

yaml

```
---
name: frontend-security-accessibility-reviewer
description: "Use this agent when you need to review frontend code for accessibility..."
tools: Bash, Glob, Grep, Read, WebFetch, WebSearch, Skill...
model: sonnet
color: blue
skills: accessibility-audit, performance-check
---
```

When you delegate to this subagent, it has both skills loaded and applies them to every review. First make sure the skills exist in your `.claude/skills` directory, then either create a new subagent or add the `skills` field to an existing agent's markdown file.

This pattern works really well when:

* You want isolated task delegation with specific expertise
* Different subagents need different skills (frontend reviewer vs. backend reviewer)
* You want to enforce standards in delegated work without relying on prompts

## Lesson reflection[](#lesson-reflection)

* Which sharing method (repository, plugin, enterprise) makes the most sense for the skills you've been thinking about building?
* Do you have workflows where custom subagents with specific skills would improve consistency in delegated work?

## What's next[](#whats-next)

In the final lesson, you'll learn how to troubleshoot common skill issues — from skills that don't trigger, to priority conflicts, to runtime errors — with a practical checklist you can reference anytime.

[Previous lessonSkills vs. other Claude Code features](https://academy.claude.com/courses/introduction-to-agent-skills/skills-vs-other-claude-code-features)[Next lessonTroubleshooting skills](https://academy.claude.com/courses/introduction-to-agent-skills/troubleshooting-skills)

Lesson 5 of 6 · Introduction to agent skillsSharing skills

Lessons

* [What are skills?](https://academy.claude.com/courses/introduction-to-agent-skills/what-are-skills)
* [Creating your first skill](https://academy.claude.com/courses/introduction-to-agent-skills/creating-your-first-skill)
* [Configuration and multi-file skills](https://academy.claude.com/courses/introduction-to-agent-skills/configuration-and-multi-file-skills)
* [Skills vs. other Claude Code features](https://academy.claude.com/courses/introduction-to-agent-skills/skills-vs-other-claude-code-features)
* [Sharing skills](https://academy.claude.com/courses/introduction-to-agent-skills/sharing-skills)
* [Troubleshooting skills](https://academy.claude.com/courses/introduction-to-agent-skills/troubleshooting-skills)

* [Course complete](https://academy.claude.com/courses/introduction-to-agent-skills/complete)

* [Sharing skills](#sharing-skills)
* [Key takeaways](#key-takeaways)
* [Committing Skills to Your Repository](#committing-skills-to-your-repository)
* [Distributing Skills Through Plugins](#distributing-skills-through-plugins)
* [Enterprise Deployment Through Managed Settings](#enterprise-deployment-through-managed-settings)
* [Skills and Subagents](#skills-and-subagents)
* [Lesson reflection](#lesson-reflection)
* [What's next](#whats-next)
