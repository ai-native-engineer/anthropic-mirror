<!-- source: https://academy.claude.com/courses/ai-native-sdlc-playbook/parallel-sessions-and-subagents -->

Lesson 7 of 14 · The AI-Native SDLC PlaybookParallel sessions and subagents

3. /[The AI-Native SDLC Playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook)

[The AI-Native SDLC Playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook)

# Parallel sessions and subagents

Lesson 74 min

One engineer can drive several streams of work at once.

A **parallel session** is another full Claude Code instance, working a separate task in its own Git worktree. Each independent session knows nothing about the others, and the engineer steering them is the only thing they share.

**A [subagent(opens in new tab)](https://code.claude.com/docs/en/sub-agents)** runs inside a single session as a scoped helper with its own context window and tool limits and suits jobs that recur in multiple tasks, such as verifying the app runs as expected.

Parallel sessions raise the number of tasks an engineer can have in flight, while subagents keep each session focused on its own task. The engineer's job is steering and reviewing all of them.

## What changes[](#what-changes)

| Traditional | AI-native |
| --- | --- |
| One engineer works one task at a time and spends a significant portion of their day/week on builds, tests, and reviews. Switching between tasks while waiting is possible, but the context switch is tiring enough that few people choose to. | One engineer runs several Claude sessions at once, each in its own worktree on its own task. Repeated jobs become subagents with their own context and tool limits. The engineer's job shifts to orchestrating and, eventually, to building and monitoring loops. |

## Getting started[](#getting-started)

* **Prerequisites**: The `CLAUDE.md`, since all sessions read the file. The feedback loop (**Stage 4: Test**) also helps here, because less supervision from the engineer is needed when a session can verify its own work.
* **Infrastructure**: A Git repository, since isolation comes from worktrees, and permission settings tuned so sessions are not waiting on approval prompts for commands the organization considers safe.

## How to execute it[](#how-to-execute-it)

1. The engineer splits the work into tasks that touch different files, using the plan from the plan mode play (**Stage 3: Build**) to see where the work is independent. Tasks that share files run in a single session, one after another.
2. Each parallel task gets its own worktree, for example `claude --worktree feature-auth` in one terminal and `claude --worktree fix-rate-limit` in another. A worktree is a separate checkout on its own branch, which stops sessions colliding on files.
3. Two or three sessions is a sensible starting point. The practical ceiling is how many streams one person can review properly, so add sessions only while review is keeping up.
4. Turn repeated jobs into subagents, as defined in Markdown files in `.claude/agents/`, each with a name, a description of when to use it, and the tools it may touch. Examples include a code simplifier that strips needless complexity after the main agent finishes, a verifier that runs the app and checks behavior, and a researcher that explores the codebase and reports back without flooding the main context. Check the definitions into Git so the whole team shares them.

## What it looks like[](#what-it-looks-like)

`.claude/agents/verifier.md`:

markdown

```
---

name: verifier
description: Runs the app and checks the change works before the session reports done
tools: Bash, Read

---
Start the app with make run. Exercise the changed behavior and the two
nearest neighboring flows. Report what you ran, what you saw, and any
behavior that does not match plan.md. Do not fix anything; report only.
```

## Governance considerations[](#governance-considerations)

More sessions means more output, so the controls have to come from configuration in the repo. Hooks and permission settings there apply to all sessions, and what a session does is logged and attributed to the engineer who ran it.

## How to measure it[](#how-to-measure-it)

* **Leading indicator**: Concurrent sessions per engineer while review quality holds, counted from the OpenTelemetry export, and the share of the day spent steering rather than waiting.
* **Lagging indicator**: Changes merged per engineer per week read alongside the rework rate as determined per the PR history.

[Previous lessonSkills as institutional knowledge](https://academy.claude.com/courses/ai-native-sdlc-playbook/skills-as-institutional-knowledge)[Next lessonGive Claude a feedback loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/give-claude-a-feedback-loop)

Lesson 7 of 14 · The AI-Native SDLC PlaybookParallel sessions and subagents

Introduction

* [Introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction)

Stage 1: Plan

* [Capture as intent.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/capture-intent)

Stage 2: Design

* [Requirements and design](https://academy.claude.com/courses/ai-native-sdlc-playbook/requirements-and-design)

Stage 3: Build

* [Claude Code plan mode as the default starting point](https://academy.claude.com/courses/ai-native-sdlc-playbook/plan-mode)
* [The CLAUDE.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/claude-md)
* [Skills as institutional knowledge](https://academy.claude.com/courses/ai-native-sdlc-playbook/skills-as-institutional-knowledge)
* [Parallel sessions and subagents](https://academy.claude.com/courses/ai-native-sdlc-playbook/parallel-sessions-and-subagents)

Stage 4: Test

* [Give Claude a feedback loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/give-claude-a-feedback-loop)
* [Continuous evals in CI](https://academy.claude.com/courses/ai-native-sdlc-playbook/continuous-evals-in-ci)

Stage 5: Deploy

* [AI in the PR review loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/ai-in-the-pr-review-loop)
* [Hooks as approval gates](https://academy.claude.com/courses/ai-native-sdlc-playbook/hooks-as-approval-gates)
* [CI/CD integration and deployment](https://academy.claude.com/courses/ai-native-sdlc-playbook/ci-cd-integration-and-deployment)

Stage 6: Maintain

* [Closing the loop on metrics](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-the-loop-on-metrics)

Closing

* [Closing thoughts and resources](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-thoughts-and-resources)

* [Course complete](https://academy.claude.com/courses/ai-native-sdlc-playbook/complete)

* [What changes](#what-changes)
* [Getting started](#getting-started)
* [How to execute it](#how-to-execute-it)
* [What it looks like](#what-it-looks-like)
* [Governance considerations](#governance-considerations)
* [How to measure it](#how-to-measure-it)
