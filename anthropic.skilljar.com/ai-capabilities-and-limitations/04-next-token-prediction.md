<!-- https://anthropic.skilljar.com/ai-capabilities-and-limitations/456447 -->

## What you'll learn

*Estimated time: 30 minutes*

By the end of this lesson you'll be able to:

* Explain Next Token Prediction as the core mechanism of generative AI and why it produces both fluency and hallucination
* Locate tasks on the Next Token Prediction continuum (well-worn path vs. novel territory)
* Identify specificity (names, dates, citations, statistics) as the zone where fabrication concentrates
* Recognize product features (citations, uncertainty signaling, constrained generation, generator-verifier pattern) that are mitigations for this limitation

## How AI models use next token prediction

*(4 minutes)*

Generative AI is closer to a vastly sophisticated autocomplete than to a search engine. It writes answers word by word based on what tends to follow what. That single property gives you both the fluency and the hallucination.

## Autocomplete at scale

Before you read

You ask AI to **summarize a long report**. How closely do you need to check the result? Pick a spot on the continuum, then lock in your guess.

![](ed975e22-1033-4415-b205-6194868cd5a8)
![]()

##

Capability
Limitation

Trust it
Spot-check
Check details
Verify carefully
High risk

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

Sky → Clay
Olive → Clay
Cactus → Fig
Slate → Clay

#### Key takeaways

* **Next Token Prediction** refers to the fact that generative AI writes answers word by word based on what tends to follow what.
  + **Capability zone:** tasks that resemble patterns the model has seen many times (summarizing, reformatting, explaining common concepts).
  + **Limitation zone:** novel or sparse territory, and anywhere the task requires distinguishing "true" from "sounds true."
  + **Fabrication concentrates in specificity:** names, dates, statistics, citations, URLs, quotes. The more precise a claim, the more it warrants verification.
  + **Product features** like citations, uncertainty signaling, constrained generation, and generator-verifier loops exist specifically to push this limitation further out.
* **4D connection:** Next Token Prediction is the foundation of Discernment. Knowing the output was generated tells you exactly what kind of scrutiny to apply.

## Exercises

**Exercise: The Verification Test**

*Why? You now know that the same generative process that makes AI fluent is the one that makes it fabricate. Time to see that on your own turf, in a domain where you'll catch it.*

Go back to your task list and pick the task where you're most confident in your domain expertise. You need a topic where you're the expert, because you need to be able to verify what comes back. Write down five specific, checkable facts from that domain: a person's job title, a publication date, a statistic, a product specification, a direct quote, a URL. Things you know to be accurate and can confirm independently.

Now run three probes:

1. **Probe 1: The capability zone.** Ask the AI to explain or summarize a well-known concept in your domain. Something popular and well-documented. Note the fluency. Spot-check the content. This is what the capability zone feels like: smooth, confident, and largely accurate.
2. **Probe 2: Specificity under pressure.** Ask the AI to provide five checkable specifics in your domain: cite three sources, name an author, give exact figures, provide a URL. Verify every one. Score it out of five: how many were fully accurate? If it fabricates, note how confident it sounded doing it.
3. **Probe 3: Sampling in action.** Run the exact same specific-facts request in a fresh conversation. Compare the two outputs. What stayed consistent? What changed? The variation you see is Next Token Prediction's sampling at work.

**Stretch goal:** Re-run Probe 2 in a tool with citations enabled (like Research mode in Claude). Score it again. Does having sources to check change the score?

## Lesson reflection

* Would you have caught fabrications in a domain you didn't know well?
* Look at your task list: which tasks sit mostly in the capability zone, and which push into specificity that needs verification?

## What's next

Next Token Prediction explains how the AI generates. Next we look at what it's generating *from*: the Knowledge property. What does the model actually know, where does that knowledge come from, and where are the gaps?

#### Feedback

As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your work, plus any feedback you may have. Share your feedback [here](https://docs.google.com/forms/d/e/1FAIpQLScUKtBMYFxnHE30yCMAuJ55ntOmfWckEFpHLYuLVBwgtBnmcw/viewform).

#### Acknowledgments and license

*Copyright 2026 Anthropic. Original work building on the AI Fluency Framework developed by Prof. Rick Dakan (Ringling College of Art and Design) and Prof. Joseph Feller (University College Cork). Released under the CC BY-NC-SA 4.0 license.*
