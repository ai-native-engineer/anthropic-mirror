<!-- source: https://academy.claude.com/courses/claude-code-in-action/github-actions-and-code-review -->

Lesson 7 of 9 · Claude Code in ActionGitHub Actions and Code Review

3. /[Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action)

[Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action)

# GitHub Actions and Code Review

Lesson 76 min

GitHub Actions and Code Review

The best place to hand off repetitive work is the pull request. It's where
review happens, where changes land, and where a lot of your busywork lives.
There are two ways to put Claude to work here, and they solve different
problems. One is a managed service you turn on. The other is a GitHub
Action you wire up yourself. Let's walk through both and figure out when to
reach for each.

## The managed path: Code Review

The simplest option is Code Review. It's an Anthropic-hosted service that reviews your pull requests through the Claude GitHub app. There's nothing for you to build or host. You turn it on, and it starts posting findings as inline comments right on the lines that matter.

An organization admin enables it from the Claude Code admin settings. You'll find a Code review section with a Configure button that hooks it up to your repositories.

From there the admin installs the Claude GitHub app, picks which repos it watches, and decides when it runs. You have a few choices for timing:

* Once when a PR opens
* On every push to the PR
* Only when someone comments `@claude review`

Once it's on, everything runs on Anthropic's infrastructure. A set of review agents analyzes the diff against your full codebase, not just the changed lines in isolation. Then it posts findings as inline comments on the specific lines, tagged by severity, with a summary table in the check run.

Here's what one of those findings looks like. It lands as a comment from Claude, right on the line, with a clear explanation and a suggested fix.

The nice part is it deduplicates and ranks the findings. So instead of a wall of nitpicks, you read a handful of real issues worth your attention.

## What Code Review will and won't do

A couple of things to keep in mind about the boundaries here:

* It never approves or blocks the PR. The judgment call stays with a human. Claude flags things; you decide.
* There's no managed autofix. The service posts findings only.
* It's a research preview right now, available on team and enterprise plans, so expect the behavior to keep moving.

Since there's no autofix in the service, applying a finding is a local move. From your own terminal, the `/code-review` command reviews a diff, and its `--fix` flag applies the findings to your working tree. So the flow is: Claude finds it in the PR, you pull it down and fix it locally.

## The do-it-yourself path: the GitHub Action

Code Review handles review. When the job goes beyond review, you reach for the GitHub Action. This is for custom CI: implementing changes from a comment, running scheduled reports, anything you'd normally write a workflow for. It runs the agent on PR comments, scheduled jobs, and any GitHub event.

Setup starts inside Claude Code. Run the `/install-github-app` command. You'll need repo admin to do this. The slash command walks you through installing the GitHub app and setting the Anthropic API key secret on the repo.

The action itself is `anthropics/claude-code-action@v1`. Here are the inputs you'll actually use:

* `anthropic_api_key` — optional.
* `github_token` — defaults to `secrets.GITHUB_TOKEN`.
* `trigger_phrase` — what the action listens for in comments. Defaults to `@claude`.
* `use_bedrock` / `use_vertex` — switch to those providers if you're on Bedrock or Vertex.
* `prompt` — the instruction for the run.
* `claude_args` — a string of CLI arguments passed straight through to Claude Code.

## A workflow that responds to @claude

Drop a workflow into `.github/workflows/claude.yaml` and it listens for `@claude` on PR comments and issue comments. The core step looks like this:

yaml

```
- uses: anthropics/claude-code-action@v1
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    github_token: ${{ secrets.GITHUB_TOKEN }}
    trigger_phrase: "@claude"
    prompt: "Your instructions here"
    claude_args: "--max-turns 5 --model claude-sonnet-5"
```

Now someone writes `@claude implement the spec in the linked Linear issue` on a pull request, and the action picks it up. Claude pushes commits and posts comments describing what it did.

## A workflow that runs on a schedule

The same action works for a daily rollup. A cron trigger fires at, say, 9:00 UTC, the action runs, and Claude posts the results. You can also add a `workflow_dispatch` trigger so you can kick it off manually from the Actions tab.

When the action runs, you can watch it work through the steps in the Actions tab, just like any other GitHub workflow.

## Tuning the run with claude\_args

The `claude_args` line is where the fine-tuning happens. A few knobs worth knowing:

* `--max-turns 5` puts a hard cap on the agent loop, so it can't run forever.
* Permission mode. For an unattended job you'll want it to not stop and ask, since there's no one there to answer.
* Allowed tools. Give the job exactly what it needs and nothing more. For a report, that means read-only.

## Which one should you use?

Here's the short version:

* For PR reviews, take the managed path. Enable Code Review, let the GitHub app post inline findings, and apply fixes locally with `/code-review --fix`.
* Reach for the action when the job is more than review. Use `/install-github-app` for setup, one workflow for `@claude` mentions, one for cron, and all the tuning lives in `claude_args`.

Start with the managed service. Move to the action the moment you need Claude to actually do something in CI, not just comment on it.

[Previous lessonRoutines and headless](https://academy.claude.com/courses/claude-code-in-action/routines-and-headless)[Next lessonTrust it: Verifying unsupervised runs](https://academy.claude.com/courses/claude-code-in-action/trust-it-verifying-unsupervised-runs)

Lesson 7 of 9 · Claude Code in ActionGitHub Actions and Code Review

Steer the work

* [Steering long sessions](https://academy.claude.com/courses/claude-code-in-action/steering-long-sessions)

Configure Claude

* [A CLAUDE.md that follows](https://academy.claude.com/courses/claude-code-in-action/a-claude-md-that-follows)
* [Verification skills](https://academy.claude.com/courses/claude-code-in-action/verification-skills)
* [Permission modes](https://academy.claude.com/courses/claude-code-in-action/permission-modes)
* [Hooks](https://academy.claude.com/courses/claude-code-in-action/hooks)

Automate repeat work

* [Routines and headless](https://academy.claude.com/courses/claude-code-in-action/routines-and-headless)
* [GitHub Actions and Code Review](https://academy.claude.com/courses/claude-code-in-action/github-actions-and-code-review)

Verify and share

* [Trust it: Verifying unsupervised runs](https://academy.claude.com/courses/claude-code-in-action/trust-it-verifying-unsupervised-runs)
* [Plugins](https://academy.claude.com/courses/claude-code-in-action/plugins)

Quiz

* [Course quizQuiz](https://academy.claude.com/courses/claude-code-in-action/course-quiz)

* [Completion badge](https://academy.claude.com/courses/claude-code-in-action/badge)

* [The managed path: Code Review](#the-managed-path-code-review)
* [What Code Review will and won't do](#what-code-review-will-and-wont-do)
* [The do-it-yourself path: the GitHub Action](#the-do-it-yourself-path-the-github-action)
* [A workflow that responds to @claude](#a-workflow-that-responds-to-claude)
* [A workflow that runs on a schedule](#a-workflow-that-runs-on-a-schedule)
* [Tuning the run with claudeargs](#tuning-the-run-with-claudeargs)
* [Which one should you use?](#which-one-should-you-use)
