<!-- https://anthropic.skilljar.com/ai-capabilities-and-limitations/456457 -->

## What you'll learn

*Estimated time: 30 minutes*

By the end of this lesson you'll be able to:

* Explain why steerability works (fine-tuning taught the model instruction-following) and why it has limits (instructions are followed via pattern-matching, not understanding)
* Predict where control is tightest (short, concrete, verifiable instructions) versus loosest (long reasoning chains, abstract asks, native precision tasks)
* Identify reasoning drift, letter-over-spirit, and brittle arithmetic as characteristic steerability failures
* Recognize system prompts, code execution, visible reasoning, and structured outputs as product features addressing this limitation

## How steerability affects generative AI outputs

*(5 minutes)*

The model follows your instructions the same way it does everything else: by continuing a pattern. That makes it remarkably steerable. It also means there's always a gap between what you intended and what landed, and most of the interesting failures live in that gap.

## How much are you actually in control?

Before you read

You ask AI to **write exactly 100 words, no more**. How closely do you need to check the result? Pick a spot on the continuum, then lock in your guess.

![](ed975e22-1033-4415-b205-6194868cd5a8)
![]()

##

Capability Limitation

Trust it Spot-check Check details Verify carefully High risk

Your guess

Typical

What this enables

Where it characteristically fails

Product features that push the edge out

Pick a stop, then lock in your guess. The lesson opens up once you do.

Lock in my guess

Check your intuition

Lock in your guess above to compare against the typical placement.

#### Customize

Bar height

Pictogram size

Palette

Sky → Clay Olive → Clay Cactus → Fig Slate → Clay

#### Key takeaways

* **Steerability** means the model follows instructions via Next Token Prediction.
+ **Capability zone:** short, concrete, verifiable instructions. Format specs, length limits, explicit roles. + **Limitation zone:** long chains of reasoning, abstract or ambiguous instructions, anything requiring native numerical or logical precision. + **Characteristic failures:** reasoning drift (small errors compound) and letter-over-spirit (the instruction was honored but the intent wasn't). + **System prompts, code execution, visible reasoning, and structured output modes** exist to keep your intent from diluting. + **When an instruction is followed literally but uselessly, restate the goal.** Repeating the instruction with more force won't close the gap.
* **4D connection:** Steerability is what makes Description powerful and what bounds it. Understanding the gap between words and intent changes how you write prompts and where you insert checkpoints.

## Exercises

**Exercise: The Goal Rewrite**

*Why? The gap between what you say and what you mean is where most steerability failures live. This exercise teaches you to prompt from intent, not just from instruction.*

Pick a task from your Lesson 1 list that involves multiple steps or a specific output format. Write down the goal in one sentence: what you're actually trying to accomplish, not just what the output should look like. ("Convince my team this timeline is realistic" is a goal. "Three bullet points" is a format.)

Now run three probes:

1. **Probe 1: Tight control.** Give a short, concrete, verifiable instruction related to your task: "respond as a three-column table," "exactly five bullet points," "second person throughout." Check whether it held precisely. This is the capability zone: the instruction is simple enough to pattern-match perfectly. 2. **Probe 2: Reasoning drift.** Ask for a version of your task that requires 4–5 dependent steps. Review the output step by step. Did a small error early on carry through to the end? Now try again, but ask the AI to stop and show you the result of step 2 before continuing. Compare what you get when you insert a checkpoint versus when you let it run. 3. **Probe 3: Letter vs. spirit.** Give an instruction that could be satisfied literally but uselessly. "Make this shorter" on a draft where the real problem is structure. "Make this more professional" on an email where the real problem is that it's burying the ask. See what you get. Then re-prompt with the goal stated explicitly alongside the instruction: "Make this shorter. My goal is to keep the executive's attention through the key finding on page two." Compare.

Go back to your task list. For any multi-step tasks, note where you'd insert a checkpoint. For any tasks where you've been prompting with format alone, draft the goal statement you'll add next time.

## Lesson reflection

* How often have you been stating format but not goal? What changes when you include both?
* What's one recurring task where you'll add a mid-process checkpoint starting this week?

## What's next

You've now met all four properties individually. In the next lesson we look at how they interact, because most real-world failures are two properties meeting.

#### Feedback

As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your work, plus any feedback you may have. Share your feedback [here](https://docs.google.com/forms/d/e/1FAIpQLScUKtBMYFxnHE30yCMAuJ55ntOmfWckEFpHLYuLVBwgtBnmcw/viewform).

#### Acknowledgments and license

*Copyright 2026 Anthropic. Original work building on the AI Fluency Framework developed by Prof. Rick Dakan (Ringling College of Art and Design) and Prof. Joseph Feller (University College Cork). Released under the CC BY-NC-SA 4.0 license.*
