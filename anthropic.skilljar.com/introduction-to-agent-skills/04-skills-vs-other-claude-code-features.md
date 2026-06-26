<!-- https://anthropic.skilljar.com/introduction-to-agent-skills/434528 -->

**What you'll learn**

*Estimated time: 15 minutes*

By the end of this lesson you'll be able to:

* *Compare skills to CLAUDE.md, subagents, hooks, and MCP servers*
* *Choose the right Claude Code customization feature for a given use case*
* *Design a complementary setup that combines multiple features effectively*

## Skills vs. other Claude Code features

*(3 minutes)*

Claude Code offers several customization options, and choosing the wrong one can lead to unnecessary complexity. This video breaks down when to use skills versus CLAUDE.md, subagents, hooks, and MCP servers. You'll learn the key differences between each option and how they complement each other in a typical development setup.

#### Key takeaways

* **CLAUDE.md** loads into every conversation and is best for always-on project standards. **Skills** load on demand and are best for task-specific expertise
* **Subagents** run in isolated execution contexts — use them for delegated work. **Skills** add knowledge to your current conversation
* **Hooks** are event-driven (fire on file saves, tool calls). **Skills** are request-driven (activate based on what you're asking)
* **MCP servers** provide external tools and integrations — a different category entirely from skills
* Each feature handles its own specialty — **combine them** rather than forcing everything into one approach

Claude Code offers several customization options: Skills, CLAUDE.md, subagents, hooks, and MCP servers. They solve different problems, and knowing when to use each prevents you from building the wrong thing. Let's break them down.

## CLAUDE.md vs Skills

CLAUDE.md loads into every conversation, always. If you want Claude to use TypeScript strict mode in your project, put it in your CLAUDE.md file.

Skills load on demand. When Claude matches a request to a skill, that skill's instructions join the conversation. Your PR review checklist doesn't need to be in context when you're writing new code — it activates when you ask for a review.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1771527266%2FSkills4_06.1771527266559.png)

**Use CLAUDE.md for:**

* Project-wide standards that always apply
* Constraints like "never modify the database schema"
* Framework preferences and coding style

**Use Skills for:**

* Task-specific expertise
* Knowledge that's only relevant sometimes
* Detailed procedures that would clutter every conversation

## Skills vs Subagents

Skills add knowledge to your current conversation. When a skill activates, its instructions join the existing context.

Subagents run in a separate context. They receive a task, work on it independently, and return results. They're isolated from the main conversation.

**Use Subagents when:**

* You want to delegate a task to a separate execution context
* You need different tool access than the main conversation
* You want isolation between delegated work and your main context

**Use Skills when:**

* You want to enhance Claude's knowledge for the current task
* The expertise applies throughout a conversation

## Skills vs Hooks

Hooks fire on events. A hook might run a linter every time Claude saves a file, or validate input before certain tool calls. They're event-driven.

Skills are request-driven. They activate based on what you're asking.

**Use Hooks for:**

* Operations that should run on every file save
* Validation before specific tool calls
* Automated side effects of Claude's actions

**Use Skills for:**

* Knowledge that informs how Claude handles requests
* Guidelines that affect Claude's reasoning

## Putting It All Together

A typical setup might include:

* **CLAUDE.md** — always-on project standards
* **Skills** — task-specific expertise that loads on demand
* **Hooks** — automated operations triggered by events
* **Subagents** — isolated execution contexts for delegated work
* **MCP servers** — external tools and integrations

Each handles its own specialty. Don't force everything into skills when another option fits better — and you can use multiple at a time. Skills provide automatic task-specific expertise, CLAUDE.md is for always-on instructions, subagents run in isolated contexts, hooks fire on events, and MCP provides external tools.

Use skills when you have knowledge that Claude should apply automatically when the topic is relevant, and combine them with other features for comprehensive customization.

## Lesson reflection

* Look at your current CLAUDE.md file. Is there anything in it that would work better as a skill (loaded only when relevant)?
* Think about your team's development workflow. Which combination of Claude Code features (skills, hooks, subagents, MCP) would address your most common pain points?

## What's next

In the next lesson, you'll learn how to share skills with your team and organization — from committing them to repositories, to distributing via plugins, to enterprise-wide deployment through managed settings.

#### Feedback

As you progress through the course, we'd love to hear how you're using skills in your work, plus any feedback you may have. Share your feedback [here](https://forms.gle/RvHPBwQt9ZmcDc1P9).

<!-- youtube: IgNN4v0BJdU -->

[![Skills Vs Other Claude Code Features](https://img.youtube.com/vi/IgNN4v0BJdU/hqdefault.jpg)](https://www.youtube.com/watch?v=IgNN4v0BJdU)

<details>
<summary>자막: Skills Vs Other Claude Code Features</summary>

Claw Code offers several customization options. Skills, claw.md, sub aents, hooks, MCP servers. They solve different problems. Knowing when to use each prevents you from building the wrong thing. So, let's run them down. Cloud.md loads into every conversation always. So, if you want claude to use TypeScript strict mode in this project, then put it in your cloud. MD file skills load on demand. When Claude matches a request, your PR review checklist doesn't need to be in the context when you're writing a new code. It activates when you ask for a review. So, use Claude MD for project-wise standards that always apply constraints like never modify the database schema, framework preferences, and coding style. Then use skills for task specific expertise, knowledge that's only relevant sometimes, and detailed procedures that would clutter every conversation. Skills add knowledge to your current conversation. When a skill activates, its instructions join the existing context. Sub aents run in a separate context. They receive a task, work on it independently, and return results. They're isolated from your main conversation. Use sub agents when you want to delegate a task to a separate execution context. You need different tool access that the main conversation does. You want isolation between delegated work and your main context. Use skills when you want to enhance cla's knowledge for the current task. The expertise applies throughout a conversation. Hooks fire on events. A hook might run a llinter every time Claude saves a file or validate input before certain tool calls. They're all event driven, while skills, they're request driven. They activate based on what you're asking. So use hooks for operations that should run on every file save, validation before specific tool calls, or automated side effects of clause actions. Then use skills for knowledge that informs how claw handles requests, guidelines that affect clause reasoning. A typical setup might include a claw.md file for always on project standards, skills for task specific expertise, hooks for automated operations. Each handles its own specialty. Don't force everything into skills when another option fits best. You can use multiple at a time. Skills provide automatic task specific expertise. CloudMD is for always on instructions. Sub aents run in isolated context. [music] Hooks fire on events. MCP provides external tools. Use skills when you have knowledge that Claude should apply automatically when the topic is relevant and combine them with other features for comprehensive customization.

</details>
