<!-- https://anthropic.skilljar.com/ai-capabilities-and-limitations/456455 -->

## What you'll learn

*Estimated time: 30 minutes*

By the end of this lesson you'll be able to:

* Explain the context window as a fixed-size container and what that implies for long documents, long conversations, and cross-session memory
* Recognize the "cliff" nature of this property compared to the gradual degradation of others
* Apply context-as-leverage strategies: front-loading important material, chunking long work, re-supplying critical context
* Recognize memory, compaction, projects/workspaces, and larger windows as product features addressing this limitation

## How the context window affects generative AI outputs

*(6 minutes)*

Everything the AI is paying attention to lives inside a fixed-size workspace called the context window. It can attend to what's in there. It can't attend to anything outside it. That constraint is hard-edged in a way the other properties aren't: things work until they don't.

## The context window: AI's working memory

Before you read

You ask AI to **review a 50-page contract**. How closely do you need to check the result? Pick a spot on the continuum, then lock in your guess.

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

* **Working Memory** is the fact that the AI model has a fixed context window that it can attend to.
+ **Capability zone:** your material fits comfortably, the session is current, you're supplying relevant context. + **Limitation zone:** very long documents or conversations, expecting continuity across sessions, burying critical info in the middle of long input. + **This property has a cliff** rather than a gradient. Silent truncation is the failure mode, and you won't always be warned. + **The model doesn't learn from your corrections.** It only responds to what's currently in context. + **Memory features, compaction, projects, larger windows, and multi-agent workflows** all exist to push this cliff further out.
* **4D connection:** Working Memory is what Description acts on. Knowing how the window works tells you how to structure context, when to front-load, and when to start fresh.

## Exercises

**Exercise: The Before-and-After**

*Why? Context is leverage. The same task, with the right context supplied, can go from a mediocre first draft to something genuinely useful. This exercise makes that concrete.*

Pick a task from your Lesson 1 list that benefits from context only you hold: a style guide, a past example of good work, a set of constraints specific to your role or audience. Write down in two or three lines what "good" looks like for this task's output, described clearly enough that a stranger could evaluate it.

Now run three probes:

1. **Probe 1: Cold start vs. context.** Ask for your task with zero context. Just the bare request. Save the output. Then start a fresh conversation and run the same task, this time supplying your style guide, past example, or constraints upfront. Compare both outputs against your "good" definition. Measure the gap. 2. **Probe 2: Lost in the middle.** Take a longer document (or paste together a few paragraphs of reference material). Bury one specific, important instruction in the middle of it. Ask a question whose correct answer depends on that buried instruction. Did the AI catch it? Now move that instruction to the very top and ask again. Compare. 3. **Probe 3: The blank slate.** Have a short exchange where you teach the AI something specific about your work context, or correct it on something it got wrong. Then open a brand-new conversation and ask a question that assumes it remembers what you taught it. Watch it start from zero.

Go back to your task list and add a third annotation: which tasks need standing context set up (a project, saved instructions, uploaded reference docs) to be worth running, and which work fine cold?

**Stretch goal:** If your tool has memory or project features, set one up with the context from Probe 1. Run the task again. Compare effort and quality against the cold-start version.

## Lesson reflection

* How much did front-loading context change output quality? Was the gap bigger than you expected?
* What's one piece of standing context you'll set up this week to stop re-explaining yourself?

## What's next

The final property: Steerability. How much are you actually in control when you give instructions, and where does that control break down?

#### Feedback

As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your work, plus any feedback you may have. Share your feedback [here](https://docs.google.com/forms/d/e/1FAIpQLScUKtBMYFxnHE30yCMAuJ55ntOmfWckEFpHLYuLVBwgtBnmcw/viewform).

#### Acknowledgments and license

*Copyright 2026 Anthropic. Original work building on the AI Fluency Framework developed by Prof. Rick Dakan (Ringling College of Art and Design) and Prof. Joseph Feller (University College Cork). Released under the CC BY-NC-SA 4.0 license.*

<!-- youtube: QJjt4wF4iHM -->

[![Working Memory](https://img.youtube.com/vi/QJjt4wF4iHM/hqdefault.jpg)](https://www.youtube.com/watch?v=QJjt4wF4iHM)

<details>
<summary>자막: Working Memory</summary>

Hi there. My name's Matt, and I'm on the user research team at Anthropic. Today, I'm here to talk to you about the context window, which is how AI models manage what they're paying attention to right now. We'll look at what actually fits inside that window, what happens when it fills up or empties out, and how to structure your work so you stay on the good side of those limits. It's a lot like how working memory functions in humans. When you're working with AI, everything sits inside one fixed-size workspace called the context window. Your instructions, Claude's prior responses, the documents you uploaded, the back-and-forth conversation, all of it lives in one finite container, and the model can only attend to what's inside. Importantly, the context window has a hard size limit. Once a conversation or a set of documents exceeds what the window can hold, something falls off. Usually, it's the oldest material, and usually it happens silently. The model doesn't stop and announce that it dropped your first three messages. It just keeps going with whatever's left. By default, the window empties between sessions. When you close a chat and open a new one tomorrow, you're starting from zero. Yesterday's conversation is gone unless a product feature like memory or a Claude.md file has deliberately carried something forward. Like the other core properties of AI systems, working memory runs as a continuum. When your material fits comfortably in the window and you're working inside the current session, you're in the capability zone. The model is working with your documents, your constraints, your context. As documents get longer, as the conversation runs on, as you start expecting the model to remember things from last week, you slide toward the limitation zone. Unlike the other three properties though, this one has a cliff. Next token prediction degrades gradually. Knowledge gets thinner gradually. But working memory tends to work right up until it doesn't. You won't always get a warning. And while you're in the capability zone, context is genuine leverage. Watch what happens when I upload a short style guide and ask Claude to draft something. No retraining, no setup. The model adapts to my material immediately inside this one session. So why is the window fixed at all? Because the model processes your entire context as a single block every time it generates a response. It's reading all of it start to finish to decide what to write next. There's a ceiling on how much it can hold and still produce a coherent reply. And even inside that ceiling, attention isn't perfectly uniform. Research on long context behavior has found a lost in the middle effect. Material buried deep in the middle of a very long input tends to carry less weight than material at the beginning or the end. What does this mean in practice? You can have rapid in-session adaptation. Give a glossary, a voice sample, a set of constraints, and it applies them on the spot. You get precision through specificity. The more relevant context you supply, the more tailored the output. But when the context window runs out, your experience degrades. AI won't remember things from the beginning of the conversation or things from the middle of your exchange might get fuzzy. Products layer features on top of the raw window to soften these edges. Memory saves selected facts across sessions so you're not starting from zero every time. Compaction or summarization condenses your conversation history to free up room when a conversation runs long. Projects and workspaces keep standing documents reliably in context without re-uploading. Skills keep instructions minimal until a specific task actually needs them. Multi-agent workflows allow for multiple agents to have different specialties and their own context windows, expanding the total amount of context the workflow can have. Larger context windows push the cliff further out. Here are some signs you're approaching the edge of the context window. A very long conversation where quality has started to slip. A very long document where details from the middle aren't showing up in responses. Expecting the model to recall something from a prior session without a memory feature enabled. Here are some techniques to stay on the good side of the cliff. Lead with what matters. For long documents, put the most important material near the top rather than burying it on page 12. Chunk long work into passes. Process a big document in sections rather than one giant upload. Use product features that save your context. Use things like projects or skills that save your context for common areas you want to work in. If quality degrades over a long conversation, start fresh. That slippage is often a context limit rather than a capability limit. A new chat with a short summary of where you were can outperform pushing through. Working memory is the mechanism that makes description work. Everything you describe to an AI, your instructions, your constraints, your examples, has to live inside this window to have any effect. Understanding the window size, its edges, and its reset behavior is what tells you how to structure a prompt, when to restate critical context, and what's actually worth uploading versus what you can leave out.

</details>
