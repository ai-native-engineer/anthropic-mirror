<!-- https://anthropic.skilljar.com/claude-code-in-action/486930 -->

As your project grows, you start noticing the same work happening over and over. You already know skills are a good way to automate repeated work. In this lesson we look at one specific job that skills are great for: verifying your own work. If there's one skill worth building first, this is it.

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

<!-- youtube: soLPOXXAc1w -->

## 자막 (영상 전사)

As your project continues to grow and grow, you want to automate the work that's constantly repeated. You already know that skills are great for this, but here are some tips on how you can use skills to help you verify your work. So this example is the skill that's worth building first. Ask Claw to refactor something and when it finishes, the description matches, task that edited code and the skill fires. It runs a suite, reads a diff, checks that no test has weakened to pass, and reports pass or fail with the evidence attached. Checking the work no longer depends on you remembering to ask for it. The same shape carries any procedure your team repeats, a release checklist or a migration recipe. If you've typed the same multi-step instruction twice, well, that's a skill. Now a skill folder can hold more than just a skill.md file. Drop a reference.md beside it for detailed material and link it from that skill. Cloud reads it only when it needs the depth. Cloud executes scripts in the folder rather than loading them. So a skill can carry its own tooling. So keep your skill.md file itself lean and push the heavy material into those side files. So a quick way to keep the three instruction surfaces straight, conventions that apply all the time go into your Cloud.md file and procedures or reference materials tied to a kind of task go into a skill. A rule Cloud must not be able to skip belongs in a hook because Cloud.md and skills are both instructions that Cloud follows rather than code that runs. A skill is a folder with a skill.md, a name, a description that triggers it, and the procedure itself. Only descriptions load until a skill is needed, so package every procedure you repeat. Start with verification and check it into the Claude skills, and your team inherits the same move.
