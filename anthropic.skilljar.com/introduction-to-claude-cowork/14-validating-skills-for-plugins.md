<!-- https://anthropic.skilljar.com/introduction-to-claude-cowork/485949 -->

## What you'll learn

*Estimated time: 8 minutes*

By the end of this lesson you'll be able to:

* Explain what an eval is and why it matters before you share or rely on a skill
* Run a lightweight eval through skill-creator

## Why this matters

When you build a skill or bundle them into a plugin, you're essentially building a small product that other people will use. And like anything you'd hand to a colleague — a template, a spreadsheet model, a checklist — it's worth a test drive before it leaves your desk.

When you use a skill you built, you know how to work around any issues or failures. You know exactly what to ask it, what files to give it, and what the answer is supposed to look like. A teammate doesn't have any of that. They might phrase the request a little differently, hand it slightly different inputs, or hit an edge case — an unusual-but-real situation, like a request that's just outside what the skill was designed for. That's where skills tend to stumble, and the person using it won't know why.

Testing a skill with evals — short for evaluations — is how you catch those stumbles before someone else does. Don't let the word intimidate you. An eval is just a try-out: a realistic request goes in, you look at what comes out, and you tell Claude what to fix. No code, no test scripts — just your judgment about whether the result is good enough to put your name on.

## How the eval system works

When you build a skill with skill-creator — Claude's built-in helper for creating skills — it walks you through evals as part of the process. Here's what that actually looks like.

Skill-creator comes up with two or more realistic prompts someone might use with your skill. For each prompt, it produces a pair of outputs:

* One where Claude uses your skill
* One where Claude answers the same prompt *without* your skill

That second one is the comparison point. It's there so you can see, side by side, what difference your skill is actually making — not just "is this output okay," but "is this output better than what Claude would have done on its own."

Review each pair and give feedback in plain English, right on the review page. As you read each pair, you're really just answering two questions:

* Is the skill version the one I'd use? If yes, great — note what made it better so the skill keeps doing that.
* If not, what's missing or off? Be specific. "The tone is too formal" or "it skipped the executive summary" gives Claude something to act on; "this isn't quite right" doesn't.

Once you submit your feedback, Claude revises the skill for you based on what you said.

## Iterate on the skill

Your feedback is the fix. Once you submit it, Claude updates the skill — rewriting the instructions, adjusting the examples, tightening what it asks for — and you can run the same prompts again to see if the change stuck.

Change one thing at a time. If the first round showed the skill was too wordy *and* missing a section, pick the one that matters more, fix it, re-run, then come back for another review. You'll be able to tell what actually moved the needle. If you're still not happy with the outputs after the revision, run it again — it's a loop, not a one-time gate. Most skills are ready after one or two rounds. The bar for shipping a skill — to yourself, to a teammate — isn't perfect evals. It's that the cases you care about pass meaningfully better than the baseline, and that you've named the cases you don't yet handle.

And if the outputs already look great on the first pass? You're done. Evals aren't a hoop to jump through — they're there for when you need confidence, not ceremony.

## Try it now

Step through a mock eval review below — three prompts, each with a with-skill and a without-skill output side by side.

For each pair: pick the version you'd actually send, and write one line of feedback you'd give Claude. That's the whole loop.

## What’s next

In the next lesson, you'll move from "this works for me" to "this works for the team" — the patterns and choices that turn personal workflows into shared infrastructure.

<!-- embed: https://academy.claude.com/embed/courses/introduction-to-claude-cowork/SkillEvalReview -->

Exercise: For three mock meeting-recap prompts, the learner compares a with-skill and without-skill output against house-rule checks, picks which they'd send, and writes feedback for Claude to revise.

Read an eval

An eval is just two outputs side by side, with a few rules of what “good” looks like. **Your job is to pick which one you’d actually send** — and tell Claude what to change.

**1** of 3

Typical case

### Recap a regular team sync

Prompt

Write the recap for today’s product sync. Notes are in `notes/2026-05-01-product-sync.md`.

With skill✓✓✓✓4/4

Product sync — recap

Decisions

* Ship the new onboarding flow to 10% of new sign-ups starting Monday.
* Pause the in-app tour redesign until after launch.

Action items

* Maya — finalize the rollout plan by Fri May 9.
* Devon — instrument the new flow for activation rate by Wed May 7.
* Priya — draft the announcement post by Mon May 12.

Open questions

* *Do we need legal sign-off on the new copy before 10%?*

House rules

* ✓Pass:Leads with decisions
* ✓Pass:Every action item has an owner and a date
* ✓Pass:Open questions called out
* ✓Pass:Under 150 words

Without skill×××✓1/4

Product sync recap

The team had a productive discussion about the new onboarding flow this morning. After reviewing the latest mockups, the group decided to move ahead with a 10% rollout starting next Monday. The in-app tour redesign came up but the consensus was to revisit it after launch.

Maya offered to finalize the rollout plan and Devon mentioned he’d look at the instrumentation. Priya is going to draft something for the announcement. There was also some back and forth about whether legal needs to weigh in on the new copy — the team didn’t reach a conclusion on that.

Overall *a productive meeting with clear next steps*.

House rules

* ×Fail:Leads with decisions
* ×Fail:Every action item has an owner and a date
* ×Fail:Open questions called out
* ✓Pass:Under 150 words

Which one would you send?

One thing you’d tell Claude to change
