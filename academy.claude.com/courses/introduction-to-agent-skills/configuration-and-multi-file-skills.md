<!-- source: https://academy.claude.com/courses/introduction-to-agent-skills/configuration-and-multi-file-skills -->

Lesson 3 of 6 · Introduction to agent skillsConfiguration and multi-file skills

3. /[Introduction to agent skills](https://academy.claude.com/courses/introduction-to-agent-skills)

[Introduction to agent skills](https://academy.claude.com/courses/introduction-to-agent-skills)

# Configuration and multi-file skills

Lesson 310 min

In this lessonBy the end, you’ll be able to

* Configure advanced skill metadata fields including allowed-tools and model
* Write effective skill descriptions that reliably trigger on the right requests
* Use allowed-tools to pre-approve the tools a skill needs without limiting Claude to them
* Organize complex skills using progressive disclosure and multi-file structures

## Configuration and multi-file skills[](#configuration-and-multi-file-skills)

Configuration and multi-file skills · 4 min

SummaryTranscript

This video covers the advanced techniques that make skills more powerful:
the full set of metadata fields, how to write descriptions that trigger
reliably, pre-approving the tools a skill needs, and
organizing larger skills across multiple files using progressive
disclosure. You'll learn how to keep your skills efficient while still
supporting complex use cases.

## Key takeaways[](#key-takeaways)

* **`name` and `description` are required** — `allowed-tools` and `model` are optional but powerful additions
* A good description **answers two questions**: What does the skill do? When should Claude use it?
* **`allowed-tools`** pre-approves the listed tools while the skill is active, so Claude can use them without asking, and it doesn't limit Claude to those tools
* **Progressive disclosure**: keep SKILL.md under 500 lines and link to supporting files (references, scripts, assets) that Claude reads only when needed
* **Scripts execute without loading their contents into context** — only the output consumes tokens, keeping context efficient

A basic skill works with just a name and description, but there are several advanced techniques that can make your skills much more effective in Claude Code. Let's walk through the key fields, best practices for descriptions, tool permissions, and how to structure larger skills.

## Skill Metadata Fields[](#skill-metadata-fields)

The agent skills open standard defines the core fields in the SKILL.md frontmatter, and Claude Code adds a few of its own, such as `model`. Two are required, and the rest are optional:

* **name** (required) — Identifies your skill. Use lowercase letters, numbers, and hyphens only. Maximum 64 characters. Should match your directory name.
* **description** (required) — Tells Claude when to use the skill. Maximum 1,024 characters. This is the most important field because Claude uses it for matching.
* **allowed-tools** (optional) — Pre-approves the listed tools, so Claude can use them without asking permission while the skill is active.
* **model** (optional) — Specifies which Claude model to use for the skill.

## Writing Effective Descriptions[](#writing-effective-descriptions)

Be explicit with your instructions. If someone told you "your job is to help with docs," you wouldn't know what to do — and Claude thinks the same way.

A good description answers two questions:

1. What does the skill do?
2. When should Claude use it?

If your skill isn't triggering when you expect it to, try adding more keywords that match how you actually phrase your requests. The description is what Claude uses to decide whether a skill is relevant, so the language matters.

## Pre-approving tools with allowed-tools[](#pre-approving-tools-with-allowed-tools)

Sometimes a skill relies on the same handful of tools every time it runs, and you don't want to approve each call by hand. The `allowed-tools` field pre-approves the tools you list, so Claude can use them without a permission prompt for the rest of the turn that invoked the skill. The grant clears when you send your next message.

![](https://academy.claude.com/assets/media/621465b21ab002652a474badb3067969c4a1d8d41ba549845efb08df03a59c41.png)

In this example, the `allowed-tools` field is set to `Read, Grep, Glob, Bash`. When this skill is active, Claude can use those four tools without asking permission. It doesn't lose access to anything else: if the skill's instructions lead Claude to edit or write a file, that goes through your normal permission settings like any other tool call. One caution: listing `Bash` on its own pre-approves shell commands in general, so reserve that for skills you trust, or narrow it to a pattern such as `Bash(git status *)`.

yaml

```
---
name: codebase-onboarding
description: Helps new developers understand the system works.
allowed-tools: Read, Grep, Glob, Bash
model: sonnet
---
```

If you omit `allowed-tools` entirely, nothing is pre-approved and Claude uses its normal permission model for every tool. To go the other way and take tools away while a skill is active, use a separate Claude Code frontmatter field, `disallowed-tools`, which removes the tools you list from the set Claude can use.

## Progressive Disclosure[](#progressive-disclosure)

Skills share Claude's context window with your conversation. When Claude activates a skill, it loads the contents of that SKILL.md into context. But sometimes you need references, examples, or utility scripts that the skill depends on.

Cramming everything into one 2,000-line file has two problems: it takes up a lot of context window space, and it's not fun to maintain.

Progressive disclosure solves this. Keep essential instructions in SKILL.md and put detailed reference material in separate files that Claude reads only when needed.

The open standard suggests organizing your skill directory with:

* **scripts/** — Executable code
* **references/** — Additional documentation
* **assets/** — Images, templates, or other data files

Then in SKILL.md, link to the supporting files with clear instructions about when to load them:

![](https://academy.claude.com/assets/media/eb7c2e2da1af718a5bd29c2cbaec5cf809dfd5a0e21769d49861997d98199328.png)

In this example, Claude reads `architecture-guide.md` only when someone asks about system design. If they're asking where to add a component, it never loads that file. It's like having a table of contents in the context window rather than the entire document.

A good rule of thumb: **keep SKILL.md under 500 lines**. If you're exceeding that, consider whether the content should be split into separate reference files.

## Using Scripts Efficiently[](#using-scripts-efficiently)

Scripts in your skill directory can run without loading their contents into context. The script executes and only the output consumes tokens. The key instruction to include in your SKILL.md is to tell Claude to *run* the script, not *read* it.

This is particularly useful for:

* Environment validation
* Data transformations that need to be consistent
* Operations that are more reliable as tested code than generated code

## Lesson reflection[](#lesson-reflection)

* Think about a skill you'd like to build that involves multiple files. How would you structure the SKILL.md versus supporting reference files?
* For a skill your team shares, which tools would you pre-approve with `allowed-tools`, and which would you rather Claude keep asking about?

## What's next[](#whats-next)

In the next lesson, we'll compare skills to the other ways you can customize Claude Code — CLAUDE.md, subagents, hooks, and MCP servers — so you can choose the right tool for each situation.

[Previous lessonCreating your first skill](https://academy.claude.com/courses/introduction-to-agent-skills/creating-your-first-skill)[Next lessonSkills vs. other Claude Code features](https://academy.claude.com/courses/introduction-to-agent-skills/skills-vs-other-claude-code-features)

Lesson 3 of 6 · Introduction to agent skillsConfiguration and multi-file skills

Lessons

* [What are skills?](https://academy.claude.com/courses/introduction-to-agent-skills/what-are-skills)
* [Creating your first skill](https://academy.claude.com/courses/introduction-to-agent-skills/creating-your-first-skill)
* [Configuration and multi-file skills](https://academy.claude.com/courses/introduction-to-agent-skills/configuration-and-multi-file-skills)
* [Skills vs. other Claude Code features](https://academy.claude.com/courses/introduction-to-agent-skills/skills-vs-other-claude-code-features)
* [Sharing skills](https://academy.claude.com/courses/introduction-to-agent-skills/sharing-skills)
* [Troubleshooting skills](https://academy.claude.com/courses/introduction-to-agent-skills/troubleshooting-skills)

* [Course complete](https://academy.claude.com/courses/introduction-to-agent-skills/complete)

* [Configuration and multi-file skills](#configuration-and-multi-file-skills)
* [Key takeaways](#key-takeaways)
* [Skill Metadata Fields](#skill-metadata-fields)
* [Writing Effective Descriptions](#writing-effective-descriptions)
* [Pre-approving tools with allowed-tools](#pre-approving-tools-with-allowed-tools)
* [Progressive Disclosure](#progressive-disclosure)
* [Using Scripts Efficiently](#using-scripts-efficiently)
* [Lesson reflection](#lesson-reflection)
* [What's next](#whats-next)
