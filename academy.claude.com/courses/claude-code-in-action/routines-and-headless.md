<!-- source: https://academy.claude.com/courses/claude-code-in-action/routines-and-headless -->

Lesson 6 of 9 · Claude Code in ActionRoutines and headless

3. /[Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action)

[Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action)

# Routines and headless

Lesson 67 min

Routines and headless

Once you trust Claude to do a task, the next move is to stop doing it by
hand. If it's the same prompt on a recurring trigger, you shouldn't have to
sit there and kick it off yourself every time. This lesson covers two ways
to hand that work off: routines, where you build nothing, and headless
mode, where you get full control from your own scripts.

Think of it as a spectrum. On one end you have routines that run on
Anthropic's managed infrastructure. On the other end you have headless mode
and the Agent SDK, which run Claude Code from your own code. Let's start
with the end where you build the least.

## Routines: a saved prompt that runs in the cloud[](#routines-a-saved-prompt-that-runs-in-the-cloud)

A routine is the most direct way to automate a task. There's no script and no server. It bundles three things: a prompt, the repository it works on, and any connectors it needs. Then it runs that bundle in the cloud whenever it's triggered.

The key part is that the infrastructure is Anthropic's. There's no machine of yours staying on overnight, and there's no workflow file for you to maintain. You describe the job once and it just runs.

A routine can fire on a few kinds of triggers:

* A cron schedule, like every morning at 9am.
* An HTTP POST to its API endpoint, so your own code can kick it off.
* A GitHub event, like a new pull request landing.

Anything that's the same prompt on a recurring trigger is a good fit. A morning dependency audit. A PR triager that fires when a new pull request comes in. A daily scan of your Sentry tickets to figure out what's most urgent.

Here's the mental model for what a routine ties together: a prompt, the repo, connectors, and a schedule.

## Two ways to create one[](#two-ways-to-create-one)

You can create a routine from the web at `claude.ai/code/routines`. You give it a name, write the instructions describing what Claude should do in each session, pick a repository, and choose a trigger.

You can also create one from inside Claude Code without leaving your terminal. Just run the `/schedule` command and describe what you want in plain language, for example:

`/schedule daily dependency audit at 9am`

Same idea, either entry point. Pick whichever fits your flow.

## Three things to know before you rely on routines[](#three-things-to-know-before-you-rely-on-routines)

Before you lean on routines for anything important, keep these three limits in mind.

* **Routines are a research preview.** Behavior and limits will keep moving, so don't be surprised if things change.
* **A recurring schedule runs at most hourly.** If you need something more frequent, routines aren't the tool.
* **Each run starts from a fresh clone of your default branch and can only push to `claude/` prefixed branches** unless you loosen that per repo. This is the guardrail that keeps an autonomous run from rewriting main.

## Headless mode: when you need your own environment[](#headless-mode-when-you-need-your-own-environment)

Routines are great when the work fits in the cloud. But sometimes the job needs your environment, or logic wrapped around the run. That's when you drop to headless mode.

The core of headless mode is the `-p` flag (short for `--print`). It runs Claude Code as a one-shot command with no interactive UI. It reads standard in and writes standard out, so it pipes like any other shell tool:

`claude -p "summarize the changes in this diff"`

One thing worth knowing: `-p` skips auto-discovery of hooks, skills, plugins, MCP servers, and the CLAUDE.md file. You get Claude plus the tools you allow explicitly, and nothing the local environment happens to load. The upside is that startup is much faster this way.

## Getting structured output back[](#getting-structured-output-back)

Because headless mode pipes like any shell tool, you'll often want structured data back instead of prose. You can pair a JSON schema with the JSON output format, and Claude will constrain its output to match your schema.

The object that matches your schema lands in the `structured_output` field of the JSON response. So you can pull it out with a `jq` command and pipe it into a database or another script:

bash

```
claude -p "Extract the exported function names from src/core/style.js" \
  --output-format json \
  --json-schema '{"type":"object","properties":{"functions":{"type":"array","items":{"type":"string"}}},"required":["functions"]}' \
  | jq '.structured_output.functions'
```

That gives you a clean array you can hand to whatever comes next.

## Multi-step automation with sessions[](#multi-step-automation-with-sessions)

For work that happens across multiple steps, you don't have to cram everything into one command. Capture the session's ID from the JSON output and resume it later:

`claude --resume "$(jq -r .session_id /tmp/plan.json)"`

One script kicks off the work. Another resumes it later with full context. This is handy when the first pass produces a plan and a second pass carries it out.

## Deterministic runs for CI[](#deterministic-runs-for-ci)

When CI needs the same results every single run, there's a mode built for that.

The `--bare` flag gives you deterministic mode. It's the right choice when you're running Claude Code inside a pipeline and you want repeatable, predictable output rather than anything that varies run to run.

## The Agent SDK: Claude Code inside your own app[](#the-agent-sdk-claude-code-inside-your-own-app)

The last step on the spectrum is the Agent SDK. This gets you a library that embeds Claude Code inside your own TypeScript or Python applications.

Both languages expose a `query` function and the same primitives as the CLI. You pass a prompt plus options, like:

* `allowedTools` to control what Claude can do,
* a system prompt,
* and a permission mode.

Then you iterate over the messages Claude streams back and handle them however your app needs. It's the same engine as the CLI, just callable from inside your product.

## Which one should you reach for?[](#which-one-should-you-reach-for)

Here's the quick decision guide:

* **Routines** are the default for repeat work. They run on Anthropic's infrastructure with nothing for you to host.
* **Headless mode with `-p`** is for when the job needs your pipeline and you want to pipe data through a script.
* **`--bare`** is for when CI needs the same results every single run.
* **The Agent SDK** is for when the work belongs inside your own product.

Start with routines. Drop down the spectrum only when the job actually needs the extra control.

[Previous lessonHooks](https://academy.claude.com/courses/claude-code-in-action/hooks)[Next lessonGitHub Actions and Code Review](https://academy.claude.com/courses/claude-code-in-action/github-actions-and-code-review)

Lesson 6 of 9 · Claude Code in ActionRoutines and headless

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

* [Routines: a saved prompt that runs in the cloud](#routines-a-saved-prompt-that-runs-in-the-cloud)
* [Two ways to create one](#two-ways-to-create-one)
* [Three things to know before you rely on routines](#three-things-to-know-before-you-rely-on-routines)
* [Headless mode: when you need your own environment](#headless-mode-when-you-need-your-own-environment)
* [Getting structured output back](#getting-structured-output-back)
* [Multi-step automation with sessions](#multi-step-automation-with-sessions)
* [Deterministic runs for CI](#deterministic-runs-for-ci)
* [The Agent SDK: Claude Code inside your own app](#the-agent-sdk-claude-code-inside-your-own-app)
* [Which one should you reach for?](#which-one-should-you-reach-for)
