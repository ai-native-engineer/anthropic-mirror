<!-- source: https://academy.claude.com/courses/ai-capabilities-and-limitations/working-memory -->

Lesson 8 of 13 · AI Capabilities and LimitationsWorking Memory

## How the context window affects generative AI outputs

Loading

Working Memory · 6 min

SummaryTranscript

Everything the AI is paying attention to lives inside a fixed-size workspace
called the context window. It can attend to what's in there. It can't attend
to anything outside it. That constraint is hard-edged in a way the other
properties aren't: things work until they don't.

## The context window: AI's working memory

Loading

## Key takeaways

* **Working Memory** is the fact that the AI model has a fixed context window that it can attend to.
  + **Capability zone:** your material fits comfortably, the session is current, you're supplying relevant context.
  + **Limitation zone:** very long documents or conversations, expecting continuity across sessions, burying critical info in the middle of long input.
  + **This property has a cliff** rather than a gradient. Silent truncation is the failure mode, and you won't always be warned.
  + **The model doesn't learn from your corrections.** It only responds to what's currently in context.
  + **Memory features, compaction, projects, larger windows, and multi-agent workflows** all exist to push this cliff further out.
* **4D connection:** Working Memory is what Description acts on. Knowing how the window works tells you how to structure context, when to front-load, and when to start fresh.

## Exercises

### The Before-and-After

Why? Context is leverage. The same task, with the right context supplied, can go from a mediocre first draft to something genuinely useful. This exercise makes that concrete.

Pick a task from your Lesson 1 list that benefits from context only you hold: a style guide, a past example of good work, a set of constraints specific to your role or audience. Write down in two or three lines what "good" looks like for this task's output, described clearly enough that a stranger could evaluate it.

Now run three probes:

1. **Probe 1: Cold start vs. context.** Ask for your task with zero context. Just the bare request. Save the output. Then start a fresh conversation and run the same task, this time supplying your style guide, past example, or constraints upfront. Compare both outputs against your "good" definition. Measure the gap.
2. **Probe 2: Lost in the middle.** Take a longer document (or paste together a few paragraphs of reference material). Bury one specific, important instruction in the middle of it. Ask a question whose correct answer depends on that buried instruction. Did the AI catch it? Now move that instruction to the very top and ask again. Compare.
3. **Probe 3: The blank slate.** Have a short exchange where you teach the AI something specific about your work context, or correct it on something it got wrong. Then open a brand-new conversation and ask a question that assumes it remembers what you taught it. Watch it start from zero.

Go back to your task list and add a third annotation: which tasks need standing context set up (a project, saved instructions, uploaded reference docs) to be worth running, and which work fine cold?

**Stretch goal:** If your tool has memory or project features, set one up with the context from Probe 1. Run the task again. Compare effort and quality against the cold-start version.

## Lesson reflection

* How much did front-loading context change output quality? Was the gap bigger than you expected?
* What's one piece of standing context you'll set up this week to stop re-explaining yourself?

## What's next

The final property: Steerability. How much are you actually in control when you give instructions, and where does that control break down?
