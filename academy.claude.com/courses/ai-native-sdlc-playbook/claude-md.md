<!-- source: https://academy.claude.com/courses/ai-native-sdlc-playbook/claude-md -->

Lesson 5 of 14 · The AI-native SDLC playbookThe CLAUDE.md

3. /[The AI-native SDLC playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook)

[The AI-native SDLC playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook)

# The CLAUDE.md

Lesson 53 min

`CLAUDE.md` gives Claude the context a new joiner would need, covering conventions, commands, architecture, and the mistakes the team sees most often. Knowledge that used to sit in people's heads and on wikis becomes a file the agent reads at the start of every session, maintained by the whole team and iterated on whenever a mistake is made.

## Getting started[](#getting-started)

* **Prerequisites**: None.
* **Infrastructure**: A repo, Claude Code installed, and one engineer who knows the codebase well.

## How to execute it[](#how-to-execute-it)

1. Run `/init` in the repo. Claude generates a starting `CLAUDE.md` from what it finds.
2. Cut the generated file down to what a new joiner would need on day one. Keep the build, test, and lint commands, the conventions that matter, and the things Claude keeps getting wrong.
3. Check `CLAUDE.md` into Git at the repo root so the whole team shares one version and changes are reviewed like code.
4. A working rule helps here. When Claude makes a mistake twice, the correction goes into `CLAUDE.md`.
5. Keep it under a page, because Claude reads all of it at the start of a session and anything stale is taking up context for no benefit.

## What it looks like[](#what-it-looks-like)

This `CLAUDE.md` belongs to the repo for an insurer's customer portal. The older internal system that holds the claims is `claims-core`, and `intent/` keeps the planning files for each change.

`CLAUDE.md`:

markdown

```
# Claims portal
## Commands
- Build: make build
- Test: make test (unit), make itest (integration, needs docker)
- Lint: make lint (runs in CI; fix before pushing)
- Run: make run (portal on :3000, claims-api on :8000)
## Conventions
- claims-api is Python 3.12 and FastAPI. portal is TypeScript and React.
- Every endpoint needs a test in claims-api/tests.
- Dates cross the API as ISO 8601, never as formatted text.
## Architecture
- portal/ is the customer site, claims-api/ is its backend, and
  intent/ holds the intent.md, spec.md and plan.md for each change.
- Only claims-api talks to claims-core. The portal never calls it.
- claims-core allows 50 requests a second. Cache reads; never poll it.
## Things Claude gets wrong
- Do not log request or response bodies in claims-api; they can hold PII.
- Do not bump dependency versions; the platform team owns them.
```

## Governance considerations[](#governance-considerations)

`CLAUDE.md` is version controlled, so the instructions the agent works to are reviewable and auditable. Team conventions are applied through the file, changes to it are logged in Git history, and code owners approve those changes in PR review.

## How to measure it[](#how-to-measure-it)

* **Leading indicator**: How often Claude repeats a mistake `CLAUDE.md` should have caught. The corrections or changes to the `CLAUDE.md` should be tracked within the Git history.
* **Lagging indicator**: Time to first merged PR for a new member of the team from PR history.

[Previous lessonClaude Code plan mode as the default starting point](https://academy.claude.com/courses/ai-native-sdlc-playbook/plan-mode)[Next lessonSkills as institutional knowledge](https://academy.claude.com/courses/ai-native-sdlc-playbook/skills-as-institutional-knowledge)

Lesson 5 of 14 · The AI-native SDLC playbookThe CLAUDE.md

Introduction

* [What changes and where to start](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction)

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

* [Getting started](#getting-started)
* [How to execute it](#how-to-execute-it)
* [What it looks like](#what-it-looks-like)
* [Governance considerations](#governance-considerations)
* [How to measure it](#how-to-measure-it)
