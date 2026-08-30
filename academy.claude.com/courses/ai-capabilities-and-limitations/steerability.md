<!-- source: https://academy.claude.com/courses/ai-capabilities-and-limitations/steerability -->

Lesson 10 of 13 · AI Capabilities and LimitationsSteerability

3. /[AI Capabilities and Limitations](https://academy.claude.com/courses/ai-capabilities-and-limitations)

[AI Capabilities and Limitations](https://academy.claude.com/courses/ai-capabilities-and-limitations)

# Steerability

Lesson 1025 min

In this lessonBy the end, you’ll be able to

* Explain why steerability works (fine-tuning taught the model instruction-following) and why it has limits (instructions are followed via pattern-matching, not understanding)
* Predict where control is tightest (short, concrete, verifiable instructions) versus loosest (long reasoning chains, abstract asks, native precision tasks)
* Identify reasoning drift, letter-over-spirit, and brittle arithmetic as characteristic steerability failures
* Recognize system prompts, code execution, visible reasoning, and structured outputs as product features addressing this limitation

## How steerability affects generative AI outputs[](#how-steerability-affects-generative-ai-outputs)

Steerability · 5 min

SummaryTranscript

The model follows your instructions the same way it does everything else: by
continuing a pattern. That makes it remarkably steerable. It also means
there's always a gap between what you intended and what landed, and most of
the interesting failures live in that gap.

## How much are you actually in control?[](#how-much-are-you-actually-in-control)

## Key takeaways[](#key-takeaways)

* **Steerability** means the model follows instructions via Next Token Prediction.
  + **Capability zone:** short, concrete, verifiable instructions. Format specs, length limits, explicit roles.
  + **Limitation zone:** long chains of reasoning, abstract or ambiguous instructions, anything requiring native numerical or logical precision.
  + **Characteristic failures:** reasoning drift (small errors compound) and letter-over-spirit (the instruction was honored but the intent wasn't).
  + **System prompts, code execution, visible reasoning, and structured output modes** exist to keep your intent from diluting.
  + **When an instruction is followed literally but uselessly, restate the goal.** Repeating the instruction with more force won't close the gap.
* **4D connection:** Steerability is what makes Description powerful and what bounds it. Understanding the gap between words and intent changes how you write prompts and where you insert checkpoints.

## Exercises[](#exercises)

### The Goal Rewrite

Why? The gap between what you say and what you mean is where most steerability failures live. This exercise teaches you to prompt from intent, not just from instruction.

Pick a task from your Lesson 1 list that involves multiple steps or a specific output format. Write down the goal in one sentence: what you're actually trying to accomplish, not just what the output should look like. ("Convince my team this timeline is realistic" is a goal. "Three bullet points" is a format.)

Now run three probes:

1. **Probe 1: Tight control.** Give a short, concrete, verifiable instruction related to your task: "respond as a three-column table," "exactly five bullet points," "second person throughout." Check whether it held precisely. This is the capability zone: the instruction is simple enough to pattern-match perfectly.
2. **Probe 2: Reasoning drift.** Ask for a version of your task that requires 4–5 dependent steps. Review the output step by step. Did a small error early on carry through to the end? Now try again, but ask the AI to stop and show you the result of step 2 before continuing. Compare what you get when you insert a checkpoint versus when you let it run.
3. **Probe 3: Letter vs. spirit.** Give an instruction that could be satisfied literally but uselessly. "Make this shorter" on a draft where the real problem is structure. "Make this more professional" on an email where the real problem is that it's burying the ask. See what you get. Then re-prompt with the goal stated explicitly alongside the instruction: "Make this shorter. My goal is to keep the executive's attention through the key finding on page two." Compare.

Go back to your task list. For any multi-step tasks, note where you'd insert a checkpoint. For any tasks where you've been prompting with format alone, draft the goal statement you'll add next time.

## Lesson reflection[](#lesson-reflection)

* How often have you been stating format but not goal? What changes when you include both?
* What's one recurring task where you'll add a mid-process checkpoint starting this week?

## What's next[](#whats-next)

You've now met all four properties individually. In the next lesson we look at how they interact, because most real-world failures are two properties meeting.

[Previous lessonTry It Out: Working Memory](https://academy.claude.com/courses/ai-capabilities-and-limitations/try-it-out-q7hdjm9twcbt)[Next lessonTry It Out: Steerability](https://academy.claude.com/courses/ai-capabilities-and-limitations/try-it-out-y02xgkpa6wa7)

Lesson 10 of 13 · AI Capabilities and LimitationsSteerability

Getting started

* [Intro to AI Capabilities and Limitations](https://academy.claude.com/courses/ai-capabilities-and-limitations/intro-to-ai-capabilities-and-limitations)
* [What We Mean by AI](https://academy.claude.com/courses/ai-capabilities-and-limitations/what-we-mean-by-ai)
* [How AI Gets Its Character](https://academy.claude.com/courses/ai-capabilities-and-limitations/how-ai-gets-its-character)

Next Token Prediction

* [Next Token Prediction](https://academy.claude.com/courses/ai-capabilities-and-limitations/next-token-prediction)
* [Try It Out: Next Token Prediction](https://academy.claude.com/courses/ai-capabilities-and-limitations/try-it-out)

Knowledge

* [Knowledge](https://academy.claude.com/courses/ai-capabilities-and-limitations/knowledge)
* [Try It Out: Knowledge](https://academy.claude.com/courses/ai-capabilities-and-limitations/try-it-out-31vzkl2dgi907)

Working Memory

* [Working Memory](https://academy.claude.com/courses/ai-capabilities-and-limitations/working-memory)
* [Try It Out: Working Memory](https://academy.claude.com/courses/ai-capabilities-and-limitations/try-it-out-q7hdjm9twcbt)

Steerability

* [Steerability](https://academy.claude.com/courses/ai-capabilities-and-limitations/steerability)
* [Try It Out: Steerability](https://academy.claude.com/courses/ai-capabilities-and-limitations/try-it-out-y02xgkpa6wa7)

Putting it all together and next steps

* [When Properties Collide](https://academy.claude.com/courses/ai-capabilities-and-limitations/when-properties-collide)
* [Next Steps](https://academy.claude.com/courses/ai-capabilities-and-limitations/next-steps)
* [Course QuizQuiz](https://academy.claude.com/courses/ai-capabilities-and-limitations/course-quiz)

* [Completion badge](https://academy.claude.com/courses/ai-capabilities-and-limitations/badge)

* [How steerability affects generative AI outputs](#how-steerability-affects-generative-ai-outputs)
* [How much are you actually in control?](#how-much-are-you-actually-in-control)
* [Key takeaways](#key-takeaways)
* [Exercises](#exercises)
* [Lesson reflection](#lesson-reflection)
* [What's next](#whats-next)
