<!-- https://anthropic.skilljar.com/ai-capabilities-and-limitations/456459 -->

## What you'll learn

*Estimated time: 25 minutes*

By the end of this lesson you'll be able to:

* Recognize that most AI failures involve two or more properties interacting
* Diagnose common failure patterns (hallucinated citations, long-conversation drift, confidently wrong math, agreeable bad premises) by identifying which properties are at play
* Apply a targeted fix based on which property is the limiting factor

## Diagnosing AI failures

*(3 minutes)*

The four properties don't operate in isolation. Most real failures are two of them intersecting. Once you can name which two, you know which fix to reach for.

## Two properties meeting: diagnosing what went wrong

# When Properties Collide

Most real-world AI failures are two properties meeting at the same time.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6rh0oaxpxl8bv3641a1ejj76o%2Fpublic%2F1774568560%2FpictoInference.1774568559957.png)

Next Token Prediction

Generates what sounds right

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6rh0oaxpxl8bv3641a1ejj76o%2Fpublic%2F1774568560%2FpictoGlobe.1774568560630.png)

Knowledge

Knows what it was trained on

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6rh0oaxpxl8bv3641a1ejj76o%2Fpublic%2F1774568561%2FpictoChip.1774568561218.png)

Working Memory

Attends to what's nearby

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6rh0oaxpxl8bv3641a1ejj76o%2Fpublic%2F1774568561%2FpictoKnobs.1774568561703.png)

Steerability

Follows the loudest instruction

drag two properties near each other to see what happens when they collide

#### Key takeaways

* **Real-world failures are usually two properties interacting**, not one.
* **Diagnostic pairs to recognize:**
+ Next Token Prediction + Knowledge (hallucinated specifics) + Working Memory + Steerability (long-conversation drift)
* **Naming the properties at play** points you straight to the fix: verify specifics, re-supply context, offload to code execution, or invite pushback.
* **This diagnostic move is Discernment applied.** You evaluate better when you know what kind of wrong you're looking at.

## Exercises

**Exercise: The Failure Diagnosis**

*Why? Most real-world AI failures aren't one property acting up. They're two properties meeting at the same time. Naming which two changes the fix entirely.*

Think back across your experience with AI (including what you've observed during this course). Identify two or three times an AI output genuinely disappointed or surprised you. For each one, describe it in a sentence or two: what you asked, what you got, what was disappointing or surprising.

1. **Walk through each event with the AI.** Describe what happened and ask: "Based on the four properties (Next Token Prediction, Knowledge, Working Memory, Steerability), which ones were likely at play here, and why?" 2. **Evaluate its diagnosis against what you now know.** Do you agree? If not, push back. (Remember the sycophancy fingerprint from Lesson 3: the AI may agree with your framing too readily. If you think it's wrong, say so.) 3. **For each diagnosis, ask:** "Given that diagnosis, what's the most targeted fix?" If you can, test the adjustment right now on a similar task.

Now look at your Lesson 1 task list with all its accumulated annotations (property tags from Lesson 2, verification scores from Lesson 4, knowledge flags from Lesson 5, context needs from Lesson 6, goal statements from Lesson 7). For the tasks that gave you the most trouble, name which two properties were colliding. Write the diagnosis next to each one.

## Lesson reflection

* Did naming the property pair change what fix you'd reach for? Before this course, would you have tried a different (less effective) fix?
* Which property pairing do you think you'll encounter most often in your day-to-day work?

## What's next

In the final lesson, we consolidate what you've built, connect it back to the 4D Framework as a complete system, and point you to where to go deeper.

#### Feedback

As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your work, plus any feedback you may have. Share your feedback [here](https://docs.google.com/forms/d/e/1FAIpQLScUKtBMYFxnHE30yCMAuJ55ntOmfWckEFpHLYuLVBwgtBnmcw/viewform).

#### Acknowledgments and license

*Copyright 2026 Anthropic. Original work building on the AI Fluency Framework developed by Prof. Rick Dakan (Ringling College of Art and Design) and Prof. Joseph Feller (University College Cork). Released under the CC BY-NC-SA 4.0 license.*

<!-- youtube: SPkg5WRfnEE -->

## 자막 (영상 전사)

Over the last few lessons, we've covered four properties that shape how AI systems behave. Next token prediction, knowledge, working memory, and steerability. Now you have four lenses, but they don't exist in isolation. They're interconnected. Most real-world AI surprises aren't single property failures. They're two properties meeting at the same time. And when you can name which two, fix becomes obvious. You ask Claude about a niche topic, and it gave you a paper title, author names. Sounds great. Then you go to look it up, and it doesn't exist. This is next token prediction meeting knowledge. Next token prediction is doing what it always does, generating what a plausible answer looks like. A good citation has a title on the right cadence, a journal that sounds real, names that fit the field. Meanwhile, there's a knowledge gap underneath, and the model doesn't know the gap is there. It can't tell the difference between what it knows and what it's generating. When you observe this, verify specifics independently. Or better, use a tool with source grounding, so the model is retrieving real documents rather than generating citation-shaped text. You set up careful constraints at the start of a long conversation. 20 messages later, Claude is ignoring half of them. This is working memory meeting steerability. Your early context has faded, either pushed out of the window or just receiving less attention than what you said recently. And because steerability works by following whatever instructions are most salient right now, your later messages are quietly overriding the earlier ones. Resupply critical context. Or if the conversation has gotten unwieldy, start a fresh one and put the essentials up front. Even before starting your conversation with AI, ask, "Which properties am I looking at with the task I'm trying to accomplish? That question comes first because the diagnosis determines the fix. A knowledge problem and a working memory problem can produce outputs that look similar on the surface, but they need completely different responses. If you jump straight to how do I fix my prompt, you're guessing. If you name the properties first, you're operating strategically. This diagnostic step is discernment in action. Naming the property level failure is exactly what turns vague dissatisfaction into a targeted iteration. You move from that wasn't quite right to I need to reground this in a source, or I need to invite pushback. And it feeds back into delegation. If you keep seeing the same compound failure on the same kind of task, that's signal. It tells you which task types to restructure, which to break into smaller pieces, which to keep for yourself. The patterns you diagnose today shape how you delegate tomorrow.
