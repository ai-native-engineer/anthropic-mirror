<!-- source: https://academy.claude.com/courses/claude-code-in-action/verification-skills -->

Lesson 3 of 9 · Claude Code in ActionVerification skills

3. /[Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action)

[Claude Code in Action](https://academy.claude.com/courses/claude-code-in-action)

# Verification skills

Lesson 35 min

Verification skills

As your project grows, you start noticing the same work happening over and
over. You already know skills are a good way to automate repeated work. In
this lesson we look at one specific job that skills are great for:
verifying your own work. If there's one skill worth building first, this
is it.

## Why a verification skill is the one to build first

Think about how you normally check Claude's work. You ask it to refactor something, it finishes, and then you have to remember to double-check it. Maybe you ask it to run the tests. Maybe you read the diff yourself. The problem is that the checking depends on you remembering to ask for it. Skip that step once and bad code slips through.

A verification skill removes that dependency. Here's the shape of it. You ask Claude to refactor something. When it finishes, the change matches the skill's description, so the skill fires on its own. From there it:

* Runs the test suite.
* Reads the diff.
* Checks that no test was weakened just to make things pass.
* Reports pass or fail, with the evidence attached.

The whole flow runs without you asking. The description on the skill is what triggers it, and once triggered it walks the same steps every time.

Notice the last check in that chain. It's not enough to run the tests and see green. A test can be quietly loosened so it passes no matter what. So the skill reads the diff and confirms tests weren't weakened. "Done" isn't "the code looks right" from reading the diff alone. Done is the gates being run and observed, with the results stated explicitly.

This same shape carries any procedure your team repeats. A release checklist. A migration recipe. A pre-PR check. The rule of thumb: if you've typed the same multi-step instruction twice, that's a skill.

## A skill folder can hold more than instructions

A skill isn't just a single `skill.md` file. The folder around it can carry other things, and this is what makes skills powerful for verification.

* Drop a `reference.md` next to the skill for detailed material, then link to it from `skill.md`. Claude only reads it when it actually needs that depth. Your main file stays short.
* Put scripts in the folder too. Claude executes them rather than loading their contents into context. That means a skill can carry its own tooling, like a `check.sh` that runs all the gates.

The takeaway: keep `skill.md` itself lean. Push the heavy material, the long explanations and the executable scripts, into side files. The lean file describes what to do; the side files hold the depth and the tools.

## Which instruction surface owns which rule

By now you've got three places to put instructions, and it's easy to mix them up. Here's a quick way to keep them straight.

Conventions that apply all the time, things like naming rules or where files go, belong in your `CLAUDE.md` file. Procedures and reference material tied to a particular kind of task belong in a skill.

There's a third case. A rule that Claude must not be able to skip belongs in a hook, not in either of the above. That's because `CLAUDE.md` and skills are both instructions that Claude follows, while a hook is code that actually runs. If skipping the rule isn't acceptable, don't leave it up to instruction-following.

## The recap

A skill is a folder with a `skill.md` inside it: a name, a description that triggers it, and the procedure itself. Only the descriptions load into context until a skill is actually needed, so there's no cost to packaging every procedure you repeat.

Start with verification. Build the skill, check it into your project's `.claude/skills`, and now the whole team inherits the same move. Everyone's work gets checked the same way, automatically, without anyone having to remember to ask.

[Previous lessonA CLAUDE.md that follows](https://academy.claude.com/courses/claude-code-in-action/a-claude-md-that-follows)[Next lessonPermission modes](https://academy.claude.com/courses/claude-code-in-action/permission-modes)

Lesson 3 of 9 · Claude Code in ActionVerification skills

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

* [Why a verification skill is the one to build first](#why-a-verification-skill-is-the-one-to-build-first)
* [A skill folder can hold more than instructions](#a-skill-folder-can-hold-more-than-instructions)
* [Which instruction surface owns which rule](#which-instruction-surface-owns-which-rule)
* [The recap](#the-recap)
