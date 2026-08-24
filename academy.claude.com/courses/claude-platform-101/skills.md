<!-- source: https://academy.claude.com/courses/claude-platform-101/skills -->

Lesson 8 of 13 · Claude Platform 101Skills

3. /[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

[Claude Platform 101](https://academy.claude.com/courses/claude-platform-101)

# Skills

Lesson 86 min

Skills

**Skills** are folders of instructions, scripts, and resources that Claude
loads dynamically to improve performance on specialized tasks. At the core
of every Skill is a `SKILL.md` file — a packaged set of instructions you
upload once and then attach to any `messages.create` call. You're teaching
Claude how *you* do something: your status report format, your review
checklist, your release notes. Claude reads the Skill, follows the
procedure, and produces output in your shape.

## Skills vs. tools

It's worth being clear on the difference, because the two solve different problems:

* **Tools** connect Claude to data and actions. "Look up this code section," "send this email" — Claude calls the tool, and something else runs.
* **Skills** teach Claude a procedure. "Generate the daily status report following this template" — it's a playbook Claude reads and follows, which sometimes means running bundled scripts itself.

A simple way to remember it: tools are about **what** Claude can do, while Skills are about **how** you want it done.

![Side-by-side comparison of tools and Skills: tools connect to data, take actions, and run code — what Claude can do; Skills teach a procedure with just instructions, no code runs — how you want it done](https://academy.claude.com/assets/media/fd2be0ac3b94e987b89d3865962a16834bd580142870e7eda1c0b608800f5a3d.png)

One more thing worth knowing: Skills don't load fully into context on startup. Only the name and description load at first. When your agent decides a Skill is relevant, it then loads the full Skill into context. That keeps your context lean even when many Skills are available.

## Uploading a Skill

Skills are uploaded once to your workspace, then referenced by ID. You can upload directly on the Claude Platform, or do it programmatically:

python

```
skill = client.beta.skills.create(
    display_title="Status Report Generator",
    files=files_from_dir("status-report-skill"),  # folder containing SKILL.md
)

print(skill.id)  # reference this ID in future requests
```

For this example, I want a **status report generator**. All the rules for what makes a good status report — sections, tone, how to summarize, how to handle blockers — live in a Skill packaged ahead of time. The activity log itself is just a string passed in at request time.

## Attaching a Skill to a request

Skills attach to a request through the container configuration — a `skills` array inside the container, where each entry names a `skill_id` and `version`. Here's the full call for the status report generator:

python

```
response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    betas=["skills-2025-10-02", "code-execution-2025-08-25"],
    container={
        "skills": [
            {
                "type": "custom",
                "skill_id": skill.id,
                "version": "latest",
            }
        ]
    },
    tools=[
        {
            "type": "code_execution_20250825",
            "name": "code_execution",
        }
    ],
    messages=[
        {
            "role": "user",
            "content": f"Generate the daily status report from this activity log:\n\n{activity_log}",
        }
    ],
)
```

A few things worth pointing out:

* We're calling `client.beta.messages.create`, not the standard one, and passing the skills feature via the **beta header**. As of this video, Skills are still a beta feature.
* `container.skills` is where the Skill attaches. It's a **list**, so you can layer multiple Skills onto one call.
* **Code execution** is turned on here too. It's required: on the API, Skills run inside the code execution tool's container, which is what lets Skill procedures do real work — like running scripts in a terminal.

## Running it

The output is a status report formatted exactly the way the Skill says to format it. Sections, tone, blocker handling — all of it comes from the `SKILL.md` file you uploaded. The user prompt is one line; the procedure lives in the Skill.

![Terminal output of the generated daily status report, with Done and Blockers sections and a summary formatted by the Skill](https://academy.claude.com/assets/media/5c1e886ab00552e07e934c958bbd602d6064d8e85fe68d5e2f889f6475936085.png)

In a production app, this is how a team standardizes output across an entire feature. With this daily status report endpoint, every PM gets the same structure, the same tone, the same sections, in the same order — without anyone copy-pasting a template into a prompt.

![A project management app with a Daily reports page, where each project's activity log has a one-click Generate report button backed by the Skill](https://academy.claude.com/assets/media/4478cdfddef8b5db5e3feed935cb6d163dcefd01f337a9425d0fd447b62b31b2.png)

## Recap

* **Skills package your procedures.** A `SKILL.md` file (plus any scripts and resources) teaches Claude how you want something done.
* **Tools vs. Skills:** tools are about what Claude can do; Skills are about how you want it done.
* **Skills load progressively.** Only the name and description load at startup; the full Skill loads into context when the agent decides to use it.
* **Upload once** with `client.beta.skills.create`, then **attach** with `container.skills` on any `messages.create` call — a list, so you can layer multiple Skills.
* **Pair with code execution** when the Skill's procedure needs to do real work.
* Reach for a Skill when the **how** matters as much as the **what**.

[Previous lessonBuilt-in tools](https://academy.claude.com/courses/claude-platform-101/built-in-tools)[Next lessonMCP](https://academy.claude.com/courses/claude-platform-101/mcp)

Lesson 8 of 13 · Claude Platform 101Skills

What is the Claude Platform?

* [What is the Claude Platform?](https://academy.claude.com/courses/claude-platform-101/what-is-the-claude-platform)
* [Your first API call](https://academy.claude.com/courses/claude-platform-101/your-first-api-call)
* [Choosing the right model](https://academy.claude.com/courses/claude-platform-101/choosing-the-right-model)

Teaching your agent

* [The agent loop explained](https://academy.claude.com/courses/claude-platform-101/the-agent-loop-explained)
* [What is tool use?](https://academy.claude.com/courses/claude-platform-101/what-is-tool-use)
* [What is thinking?](https://academy.claude.com/courses/claude-platform-101/what-is-thinking)

Extending your agent

* [Built-in tools](https://academy.claude.com/courses/claude-platform-101/built-in-tools)
* [Skills](https://academy.claude.com/courses/claude-platform-101/skills)
* [MCP](https://academy.claude.com/courses/claude-platform-101/mcp)
* [Context management](https://academy.claude.com/courses/claude-platform-101/context-management)

Managed Agents

* [What are managed agents?](https://academy.claude.com/courses/claude-platform-101/what-are-managed-agents)
* [Building your first managed agent](https://academy.claude.com/courses/claude-platform-101/building-your-first-managed-agent)

Building with Claude Code

* [Building with Claude Code](https://academy.claude.com/courses/claude-platform-101/building-with-claude-code)

Quiz

* [Claude Platform 101 quizQuiz](https://academy.claude.com/courses/claude-platform-101/claude-platform-101-quiz)

* [Completion badge](https://academy.claude.com/courses/claude-platform-101/badge)

* [Skills vs. tools](#skills-vs-tools)
* [Uploading a Skill](#uploading-a-skill)
* [Attaching a Skill to a request](#attaching-a-skill-to-a-request)
* [Running it](#running-it)
* [Recap](#recap)
