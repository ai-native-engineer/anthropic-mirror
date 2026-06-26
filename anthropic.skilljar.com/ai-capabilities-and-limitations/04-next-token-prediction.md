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

* **Next Token Prediction** refers to the fact that generative AI writes answers word by word based on what tends to follow what.
+ **Capability zone:** tasks that resemble patterns the model has seen many times (summarizing, reformatting, explaining common concepts). + **Limitation zone:** novel or sparse territory, and anywhere the task requires distinguishing "true" from "sounds true." + **Fabrication concentrates in specificity:** names, dates, statistics, citations, URLs, quotes. The more precise a claim, the more it warrants verification. + **Product features** like citations, uncertainty signaling, constrained generation, and generator-verifier loops exist specifically to push this limitation further out.
* **4D connection:** Next Token Prediction is the foundation of Discernment. Knowing the output was generated tells you exactly what kind of scrutiny to apply.

## Exercises

**Exercise: The Verification Test**

*Why? You now know that the same generative process that makes AI fluent is the one that makes it fabricate. Time to see that on your own turf, in a domain where you'll catch it.*

Go back to your task list and pick the task where you're most confident in your domain expertise. You need a topic where you're the expert, because you need to be able to verify what comes back. Write down five specific, checkable facts from that domain: a person's job title, a publication date, a statistic, a product specification, a direct quote, a URL. Things you know to be accurate and can confirm independently.

Now run three probes:

1. **Probe 1: The capability zone.** Ask the AI to explain or summarize a well-known concept in your domain. Something popular and well-documented. Note the fluency. Spot-check the content. This is what the capability zone feels like: smooth, confident, and largely accurate. 2. **Probe 2: Specificity under pressure.** Ask the AI to provide five checkable specifics in your domain: cite three sources, name an author, give exact figures, provide a URL. Verify every one. Score it out of five: how many were fully accurate? If it fabricates, note how confident it sounded doing it. 3. **Probe 3: Sampling in action.** Run the exact same specific-facts request in a fresh conversation. Compare the two outputs. What stayed consistent? What changed? The variation you see is Next Token Prediction's sampling at work.

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

<!-- youtube: kl0gunXTvyk -->

## 자막 (영상 전사)

Hi, my name is David and I'm on the safety team here at Anthropic. Today I'm here to talk to you about next token prediction, which is a core property that determines where AI answers actually come from. We'll look at what's really happening when AI responds to you and why the same mechanism that produces fluent writing can also produce fabricated facts and how to tell which zone your task lands in. If you understand one thing about how generative AI works, let it be this. The operation at the heart of these systems is prediction. Given everything that's been written so far, predict what comes next one fragment at a time. Generative AI is generating an answer, composing it word by word based on what tends to follow what. It's closer to an extraordinarily sophisticated autocomplete than to a search engine. And that distinction matters because a citation that looks like a real citation can satisfy a pattern just as well as one pointing to a paper that actually exists. Let me show you this in action. I'll ask Claude to summarize an argument in a well-known essay. Notice how quickly it produces clean, coherent prose. This is a well-worn path. The model has encountered this task thousands of times. Now watch what happens when I ask for something at the edge. Let's say I ask it to list three research papers by a mid-level researcher in a niche subfield with publication years. Same confident tone, same fluent prose, but the path is thin here and the model's generating what looks like a good answer. Some of these may be real, some may be fabrications. You have to check the output. The same generative process is always running when you're working with AI. What changes is how well-worn the path is. Tasks the model has seen in countless variations land in the capability zone. Summarizing, reformatting, explaining common concepts, drafting in a familiar style. Next token prediction shines here because the patterns are dense and consistent. As you move towards the edge, the patterns thin out. Novel territory, obscure topics, those drift right. The model keeps generating fluently, but the ground underneath gets shakier. The strength and weakness are the same property. Broadly relevant concept fluency comes from next token prediction. The hallucination also comes from next token prediction. You experience one or the other depending on where your tasks fall on that line. On the strength side, we see fluent text in any register, rapid synthesis across fields, strong performance on anything resembling what the model has seen before and coherent continuation of any thread you hand it. On the failure side, we see hallucinations, inconsistency, and misplaced confidence. Frontier labs have built product features to help here. Citations and source grounding let you trace what's backed versus what's generated. Trained uncertainty signaling, like when the model says, "I'm not sure about this." helps the model flag its own shakiness. Constrained generation and skills narrow the space where fabrication can sneak in. A generator-verifier agent loop ensures output meets checks from an outside source. These features exist precisely because the underlying behavior is always generative next token prediction. When working with AI outputs, keep these in mind. A confident tone does not signal accuracy. Smoothness and correctness are independent variables. Specificity is where fabrication concentrates. Names, dates, statistics, citations, quotes, URLs. The more precise a claim, the more it warrants a check. Treat outputs as drafts to verify, particularly when stakes are high or the domain's unfamiliar to you. Ask where on the continuum your task sits. Well-worn paths are safer handoffs. Thin paths need more scrutiny. Lean on product surfaces. If your tool offers citations or source grounding, use them. The model can't reliably tell grounded from invented. You have to do that part. Understanding next token prediction sits at the heart of discernment in the 4D framework. You can't evaluate an output well without understanding that it was generated or composed to fit a shape. It also informs delegation. Tasks deep in the capability zone are safer handoffs. Tasks near the edge deserve more of your attention on the back end. With this knowledge at hand, AI becomes predictable rather than surprising.
