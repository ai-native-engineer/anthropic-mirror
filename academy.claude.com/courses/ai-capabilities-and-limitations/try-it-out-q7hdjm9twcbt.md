<!-- source: https://academy.claude.com/courses/ai-capabilities-and-limitations/try-it-out-q7hdjm9twcbt -->

Lesson 9 of 13 · AI Capabilities and LimitationsTry It Out: Working Memory

3. /[AI Capabilities and Limitations](https://academy.claude.com/courses/ai-capabilities-and-limitations)

[AI Capabilities and Limitations](https://academy.claude.com/courses/ai-capabilities-and-limitations)

# Try It Out: Working Memory

Lesson 910 min

## Context Degradation

*When more context makes things worse*

A natural instinct when using AI is to give it **everything**. Paste in the whole document. Include every message. Add all the context you can find. More information means better answers, right?

Not always. There's a phenomenon that anyone who has crammed for an exam knows intuitively: **there's a limit to how much you can hold in mind at once**. And the things in the middle tend to disappear first.

Before we talk about how this affects AI models, let's see how it affects **you**.

## The Memory Test

## The U-Shaped Curve

What you just experienced has a name: the **serial position effect**. Psychologists have studied it for over a century. Items at the beginning of a list benefit from **primacy** (they get rehearsed more), and items at the end benefit from **recency** (they're still fresh). The middle gets neither advantage.

The fascinating part: **large language models exhibit the same pattern**. In 2023, researchers at Stanford tested what happens when you place a key fact at different positions within a long context window. Accuracy was highest when the fact appeared at the very beginning or very end — and dropped by more than 30% when it was buried in the middle.

This isn't a quirk. It's structural. Transformer attention patterns naturally weight the edges of the context window more heavily.

## What This Means for Prompting

If you paste a 20-page document into a prompt and ask a question about something on page 11, the model is more likely to miss it than something on page 1 or page 20. This has real implications for how you structure context.

The practical advice is straightforward: **put your most important instructions at the beginning and end of the context**. If a constraint absolutely must be followed, state it early in the system prompt and restate it near the end. Don't rely on the model to give equal weight to everything in between.

This is the starting point, not the ceiling. As you get more fluent you'll discover increasingly sophisticated ways to structure context so the model reliably understands what matters — leveraging where in the window information sits, what to include versus cut, and how to keep critical instructions from sliding into the dead zone. The goal is always the same: make it obvious to Claude what you actually need.

## The Bigger Picture

Context degradation is the reason that "just give it more context" is not always the answer. Every piece of context you add pushes other pieces further into the middle — the attention dead zone. This is the core tension of **context engineering**: not just what to include, but where to put it and what to leave out.

Key takeaway

More context ≠ better results. The model's attention is finite. Curate
ruthlessly, place strategically, and repeat what matters.

Your own memory test told you this already. The words in the middle vanished. The same thing happens inside every long conversation, every pasted document, every context window that's been filled to the brim. The fix isn't more — it's smarter.

[Previous lessonWorking Memory](https://academy.claude.com/courses/ai-capabilities-and-limitations/working-memory)[Next lessonSteerability](https://academy.claude.com/courses/ai-capabilities-and-limitations/steerability)

Lesson 9 of 13 · AI Capabilities and LimitationsTry It Out: Working Memory

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

* [Context Degradation](#context-degradation)
* [The Memory Test](#the-memory-test)
* [The U-Shaped Curve](#the-u-shaped-curve)
* [What This Means for Prompting](#what-this-means-for-prompting)
* [The Bigger Picture](#the-bigger-picture)
