<!-- https://anthropic.skilljar.com/ai-capabilities-and-limitations/456452 -->

## What you'll learn

*Estimated time: 30 minutes*

By the end of this lesson you'll be able to:

* Explain how an AI model's knowledge is formed during training and why it has a fixed cutoff
* Predict which topics sit in the capability zone (frequent, recent-in-training, consistent) versus the edge (rare, post-cutoff, niche, contested)
* Identify staleness, uneven coverage, inherited bias, and source amnesia as characteristic knowledge failures
* Recognize web search, retrieval/RAG, and tool use as the product features that address this limitation

## Understanding knowledge gaps in AI models

*(5 minutes)*

The model knows what it was exposed to during training, and only that. No real-time browsing by default, no lived experience, and a hard stop at the knowledge cutoff. The practical question isn't "does the AI know this?" but "how well-represented was this in what it read?"

## What the model read, and when it stopped reading

Before you read

You ask AI to **explain a news event from last week**. How closely do you need to check the result? Pick a spot on the continuum, then lock in your guess.

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

* **What generative AI knows** comes entirely from training data and is frozen at the knowledge cutoff. Without tools, it has no access to any information after that date.
  + **Capability zone:** topics that appeared frequently, recently (within training), and consistently in training data.
  + **Limitation zone:** rare, post-cutoff, niche, local, or contested topics.
  + **Characteristic failures:** staleness, uneven coverage, inherited bias in what counts as "default" or "normal," and inability to attribute where knowledge came from.
  + **Web search, retrieval (RAG/MCPs), and tool use** exist specifically to patch these gaps by giving the model access to information it was never trained on.
* **4D connection:** Knowledge unevenness is core to Delegation. Understanding where the model is well-stocked versus thin tells you when to hand off, when to supply context yourself, and when to go elsewhere.

## Exercises

**Exercise: The Outsider Test**

*Why? You know the model's knowledge is broad but frozen, shaped by whatever was in its training data. Now you're going to map exactly where it's well-stocked and where it's thin in your specific domain.*

Return to your task list and select one task. Relative to that task, write down:

* Two topics that are mainstream, well-documented, and stable. The kind of thing any informed colleague would know.
* Two topics that are niche, local, recent, or rapidly evolving. Industry-specific jargon, regional regulations, something that changed in the last year.
* One "default assumption" that outsiders to your field often get wrong. (Who the typical customer is. What a "standard" case looks like. Which tool people actually use vs. the one that gets press.)

Now run three probes:

1. **Probe 1: Coverage.** Ask about one mainstream topic and one niche topic from your list. Compare the depth and accuracy. Pay attention to whether the AI signals uncertainty differently between the two, or whether both answers come with the same confident tone.
2. **Probe 2: Staleness.** Ask about something you know has changed recently in your field: a regulation update, a tool release, a leadership change, a revised standard. Does the AI acknowledge the cutoff? Present stale information as current? Decline to answer? Note what happens.
3. **Probe 3: Default assumptions.** Without naming your assumption directly, ask a question that would reveal whether the AI defaults to the outsider's view. For example, if your field's "standard" customer is different from what most people assume, ask the AI to describe the typical customer. Note what it treats as normal.

Go back to your task list and add a second annotation: for each task, flag whether you can lean on the model's knowledge, or whether you need to bring the knowledge yourself via context, documents, or search.

**Stretch goal:** Re-run the staleness probe with web search enabled. Compare what changes. This is retrieval in action.

## Lesson reflection

* What's one area of your work where you now realize you need to supply context rather than assume the model has it?
* Did the default-assumption probe surface anything that surprised you?

## What's next

Knowledge covers what the model absorbed during training. Working Memory covers what it's paying attention to right now: your prompt, your documents, your conversation. This property has the hardest edge of all four.

#### Feedback

As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your work, plus any feedback you may have. Share your feedback [here](https://docs.google.com/forms/d/e/1FAIpQLScUKtBMYFxnHE30yCMAuJ55ntOmfWckEFpHLYuLVBwgtBnmcw/viewform).

#### Acknowledgments and license

*Copyright 2026 Anthropic. Original work building on the AI Fluency Framework developed by Prof. Rick Dakan (Ringling College of Art and Design) and Prof. Joseph Feller (University College Cork). Released under the CC BY-NC-SA 4.0 license.*
