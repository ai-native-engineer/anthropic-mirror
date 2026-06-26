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
