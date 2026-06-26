<!-- source: https://claude.com/resources/tutorials/the-4-properties-of-ai -->

# The 4 Properties of AI

This tutorial offers a full overview of the 4 properties of AI. It's a quick reference to help you understand the things that make AI capable in some situations and limited in others.

  AI Fluency
* Product

  AI Fluency
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/the-4-properties-of-ai

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a04d60264912fa007c89415_Screenshot%202026-05-13%20at%2012.50.18%E2%80%AFPM.png)

*Want the deep dive with hands-on exercises?* Take the full [AI Capabilities & Limitations](https://anthropic.skilljar.com/ai-capabilities-and-limitations) course.

[Next Token Prediction

Where do AI answers come from?](#next-token-prediction)
[Knowledge

What does AI actually know?](#knowledge)
[Working Memory

What is AI paying attention to?](#working-memory)
[Steerability

How much am I in control?](#steerability)

## Next Token Prediction

> *Where do AI answers come from?*

Generative AI writes answers word by word based on what tends to follow what. It is a vastly sophisticated autocomplete — not a search engine.

[Watch the lesson · 5 min](https://www.youtube.com/watch?v=kl0gunXTvyk)

<!-- yt-inline:kl0gunXTvyk -->
[![How AI models use next token prediction](https://img.youtube.com/vi/kl0gunXTvyk/hqdefault.jpg)](https://www.youtube.com/watch?v=kl0gunXTvyk)

<details>
<summary>자막: How AI models use next token prediction (4:15)</summary>

[00:00]
Hi, my name is David and I'm on the
safety team here at Anthropic. Today I'm
here to talk to you about next token
prediction, which is a core property
that determines where AI answers
actually come from. We'll look at what's
really happening when AI responds to you
and why the same mechanism that produces
fluent writing can also produce
fabricated facts and how to tell which
zone your task lands in.
If you understand one thing about how
generative AI works, let it be this. The
operation at the heart of these systems
is prediction. Given everything that's
been written so far, predict what comes
next one fragment at a time.
Generative AI is generating an answer,
composing it word by word based on what
tends to follow what. It's closer to an
extraordinarily sophisticated
autocomplete than to a search engine.
And that distinction matters because a
citation that looks like a real citation
can satisfy a pattern just as well as
one pointing to a paper that actually
exists.
Let me show you this in action. I'll ask
Claude to summarize an argument in a
well-known essay. Notice how quickly it

[00:01]
produces clean, coherent prose. This is
a well-worn path. The model has
encountered this task thousands of
times.
Now watch what happens when I ask for
something at the edge. Let's say I ask
it to list three research papers by a
mid-level researcher in a niche subfield
with publication years.
Same confident tone, same fluent prose,
but the path is thin here and the
model's generating what looks like a
good answer.
Some of these may be real, some may be
fabrications. You have to check the
output.
The same generative process is always
running when you're working with AI.
What changes is how well-worn the path
is. Tasks the model has seen in
countless variations land in the
capability zone. Summarizing,
reformatting, explaining common
concepts, drafting in a familiar style.
Next token prediction shines here
because the patterns are dense and
consistent. As you move towards the
edge, the patterns thin out. Novel
territory, obscure topics, those drift
right. The model keeps generating
fluently, but the ground underneath gets

[00:02]
shakier. The strength and weakness are
the same property. Broadly relevant
concept fluency comes from next token
prediction. The hallucination also comes
from next token prediction.
You experience one or the other
depending on where your tasks fall on
that line.
On the strength side, we see fluent text
in any register, rapid synthesis across
fields, strong performance on anything
resembling what the model has seen
before and coherent continuation of any
thread you hand it. On the failure side,
we see hallucinations, inconsistency,
and misplaced confidence.
Frontier labs have built product
features to help here. Citations and
source grounding let you trace what's
backed versus what's generated. Trained
uncertainty signaling, like when the
model says, "I'm not sure about this."
helps the model flag its own shakiness.
Constrained generation and skills narrow
the space where fabrication can sneak
in. A generator-verifier agent loop
ensures output meets checks from an
outside source. These features exist
precisely because the underlying
behavior is always generative next token

[00:03]
prediction.
When working with AI outputs, keep these
in mind. A confident tone does not
signal accuracy. Smoothness and
correctness are independent variables.
Specificity is where fabrication
concentrates. Names, dates, statistics,
citations, quotes, URLs. The more
precise a claim, the more it warrants a
check.
Treat outputs as drafts to verify,
particularly when stakes are high or the
domain's unfamiliar to you.
Ask where on the continuum your task
sits. Well-worn paths are safer
handoffs. Thin paths need more scrutiny.
Lean on product surfaces. If your tool
offers citations or source grounding,
use them.
The model can't reliably tell grounded
from invented. You have to do that part.
Understanding next token prediction sits
at the heart of discernment in the 4D
framework. You can't evaluate an output
well without understanding that it was
generated or composed to fit a shape. It
also informs delegation. Tasks deep in
the capability zone are safer handoffs.
Tasks near the edge deserve more of your
attention on the back end. With this

[00:04]
knowledge at hand, AI becomes
predictable rather than surprising.

</details>


What this enables

* Fluent, natural-sounding text in any style
* Rapid synthesis across large amounts of material
* Strong performance on tasks resembling its training data

Where it characteristically fails

* Hallucination — plausible isn't the same as true
* Confabulation concentrates in specifics: names, dates, citations, stats, URLs
* Misplaced confidence — smooth prose wraps a guess

Claude features that push the edge out

Citations & source grounding
Constrained generation
Generator–verifier loops

## Knowledge

> *What does AI actually know?*

What the model knows comes entirely from its training data, frozen at a knowledge cutoff — what it read, and when it stopped reading.

[Watch the lesson · 5 min](https://www.youtube.com/watch?v=iSLdQXeKbHs)

<!-- yt-inline:iSLdQXeKbHs -->
[![Understanding knowledge gaps in AI models](https://img.youtube.com/vi/iSLdQXeKbHs/hqdefault.jpg)](https://www.youtube.com/watch?v=iSLdQXeKbHs)

<details>
<summary>자막: Understanding knowledge gaps in AI models (5:24)</summary>

[00:00]
Hi, my name is David and I'm on the
safety team here at Anthropic. Today I'm
going to talk to you about what AI
models actually know and just as
importantly what they don't. We'll
explore where AI's knowledge comes from,
why it has sharp edges, and how you can
predict which topics are going to be
reliable for you and which ones aren't.
A model like Claude has been exposed to
more data than any human could digest in
many lifetimes. That makes it feel like
it knows everything, but it doesn't.
Generative AI models have predictable
knowledge gaps.
AI models learn by reading enormous
quantities of text, mostly drawn from
the internet, public data sets, and
other written sources. Through billions
of rounds of given everything so far,
what comes next, the model builds
internal representations of concepts,
relationships, and facts. That's how it
knows things. It's also the only way it
knows things. The model doesn't have
experiences, it doesn't browse the web
in real time unless a product explicitly

[00:01]
gives it a search tool. And critically,
training ends on a specific date. That
date's called the knowledge cutoff.
Everything that happened after that
moment simply isn't there.
Let me show you why that matters in
practice. I'm going to ask Claude two
questions. First, explain how
photosynthesis works. Watch the
response. Detailed, accurate, confident.
This is a topic that has appeared
thousands of times in the training data,
described consistently, and hasn't
changed. Now a second question. Who's
the current mayor of Toledo?
The model might give me a name. It might
be right. It might be the person who
held that job 2 years ago. The model has
no way to know the difference.
Think of the model's knowledge as a
continuum. On one end, the capability
zone, mainstream science, popular
programming languages, well-documented
history. Topics that showed up
frequently, consistently, and before the
cutoff. Here, the model is
extraordinarily deep. On the other end,
rare topics, post-cutoff events, niche
domains, local knowledge. The further
you drift towards this edge, the less
you should trust the answer.

[00:02]
The question to ask isn't does the AI
know this? It's how well represented was
this in what it read.
This training process produces some
genuine strengths. The model's general
knowledge is extraordinarily broad.
It's deeply competent in the domains
that are well represented in the
training data. And it makes connections
across fields because concepts that
appear together in text end up near each
other in the model's internal
representation.
That's where embeddings are, words and
ideas mapped as points in a vast
mathematical space where similar
meanings cluster. Ask about a biology
concept and the model can pull in
relevant chemistry and history and
economics without being told to.
But the same process creates
characteristic limitations, knowledge
cutoff. Anything after the training
simply doesn't exist for the model.
Staleness, information that was true at
the time of training may have changed.
The model has no mechanism to know this.
Uneven coverage, frequent topics are
handled well, rare topics are handled
poorly. Minority languages, niche
domains, recent developments all suffer.
Inherited bias, the model's sense of

[00:03]
what's normal or default reflects its
training data's blind spots. That shows
up in assumptions about what a doctor
looks like, what a family looks like, or
what counts as a professional.
Source amnesia, the model usually can't
tell you where a piece of knowledge came
from.
I read this somewhere isn't a citation.
This is why modern AI products ship with
features designed to work around these
limits. Web search pulls current
information at response time, routing
around the cutoff.
MCPs connect the model to documents it
never trained on, like your company's
wiki or a specialized database.
Tools let the model call real-time
calculators or databases instead of
relying on absorbed patterns.
Explicit cutoff disclosure just tells
you when a training ended so you can
know to double-check.
If you're using these features, you're
extending the model's knowledge at
runtime.
If you're not, you're relying entirely
on what it absorbed during training.
Knowledge gaps are most likely to show
up when the topic is time sensitive.

[00:04]
Current events, recent research, who
holds a position, what something costs.
The domain is niche, local, or in a less
represented language.
The question postdates the cutoff.
You're relying on the model's sense of
typical or normal.
Or web search is turned off.
Here's how to protect yourself. Verify
anything time sensitive. Assume the
model may be out of date.
Test before you trust in a new domain.
Brilliance in one area doesn't transfer
to the one next door.
Watch for default assumptions that
reflect training data rather than
reality.
When the tools exist, search, retrieval,
use them.
They're there specifically to patch
these gaps. Understanding the knowledge
property directly shapes two of the four
AI fluency competencies.
Delegation. Before you hand a task to
the model, ask yourself, is this a
domain the model knows well, or one
where you need to bring the knowledge
yourself through context, documents, or
search?
Discernment. When you get an answer
back, you now know which of these claims
need independent verification. Anything

[00:05]
in the model's weak zone, recent, rare,
or local, warrants a second look.
The model's knowledge is broad, deep,
frozen, and imperfect all at once. Once
you can see where the edges are, you
stop being surprised by them.

</details>


What this enables

* Extraordinarily broad general knowledge
* Deep competence in well-represented domains
* Unexpected connections across fields

Where it characteristically fails

* Knowledge cutoff & staleness — true-then isn't true-now
* Uneven coverage of niche, local, or recent topics
* Source amnesia — "I read this somewhere" isn't a citation

Claude features that push the edge out

Web search
Retrieval (RAG / connectors)
Tool use for real-time data

## Working memory

> *What is the AI paying attention to right now?*

Everything the model is attending to lives inside a fixed-size context window. Context is leverage — until you hit the cliff.

[Watch the lesson · 6 min](https://www.youtube.com/watch?v=QJjt4wF4iHM)

<!-- yt-inline:QJjt4wF4iHM -->
[![The Context Window: How working memory affects generative AI outputs](https://img.youtube.com/vi/QJjt4wF4iHM/hqdefault.jpg)](https://www.youtube.com/watch?v=QJjt4wF4iHM)

<details>
<summary>자막: The Context Window: How working memory affects generative AI outputs (5:46)</summary>

[00:00]
Hi there. My name's Matt, and I'm on the
user research team at Anthropic. Today,
I'm here to talk to you about the
context window, which is how AI models
manage what they're paying attention to
right now.
We'll look at what actually fits inside
that window, what happens when it fills
up or empties out, and how to structure
your work so you stay on the good side
of those limits. It's a lot like how
working memory functions in humans.
When you're working with AI, everything
sits inside one fixed-size workspace
called the context window.
Your instructions, Claude's prior
responses, the documents you uploaded,
the back-and-forth conversation, all of
it lives in one finite container, and
the model can only attend to what's
inside.
Importantly, the context window has a
hard size limit. Once a conversation or
a set of documents exceeds what the
window can hold, something falls off.

[00:01]
Usually, it's the oldest material, and
usually it happens silently.
The model doesn't stop and announce that
it dropped your first three messages. It
just keeps going with whatever's left.
By default, the window empties between
sessions. When you close a chat and open
a new one tomorrow, you're starting from
zero.
Yesterday's conversation is gone unless
a product feature like memory or a
Claude.md file has deliberately carried
something forward. Like the other core
properties of AI systems, working memory
runs as a continuum.
When your material fits comfortably in
the window and you're working inside the
current session, you're in the
capability zone.
The model is working with your
documents, your constraints, your
context. As documents get longer, as the
conversation runs on, as you start
expecting the model to remember things
from last week, you slide toward the
limitation zone.
Unlike the other three properties
though, this one has a cliff.

[00:02]
Next token prediction degrades
gradually.
Knowledge gets thinner gradually.
But working memory tends to work right
up until it doesn't. You won't always
get a warning.
And while you're in the capability zone,
context is genuine leverage. Watch what
happens when I upload a short style
guide and ask Claude to draft something.
No retraining, no setup. The model
adapts to my material immediately inside
this one session.
So why is the window fixed at all?
Because the model processes your entire
context as a single block every time it
generates a response. It's reading all
of it start to finish to decide what to
write next.
There's a ceiling on how much it can
hold and still produce a coherent reply.
And even inside that ceiling, attention
isn't perfectly uniform.
Research on long context behavior has
found a lost in the middle effect.
Material buried deep in the middle of a
very long input tends to carry less
weight than material at the beginning or
the end.

[00:03]
What does this mean in practice?
You can have rapid in-session
adaptation.
Give a glossary, a voice sample, a set
of constraints, and it applies them on
the spot. You get precision through
specificity. The more relevant context
you supply, the more tailored the
output.
But when the context window runs out,
your experience degrades. AI won't
remember things from the beginning of
the conversation or things from the
middle of your exchange might get fuzzy.
Products layer features on top of the
raw window to soften these edges. Memory
saves selected facts across sessions so
you're not starting from zero every
time.
Compaction or summarization condenses
your conversation history to free up
room when a conversation runs long.
Projects and workspaces keep standing
documents reliably in context without
re-uploading.
Skills keep instructions minimal until a
specific task actually needs them.
Multi-agent workflows allow for multiple

[00:04]
agents to have different specialties and
their own context windows, expanding the
total amount of context the workflow can
have.
Larger context windows push the cliff
further out.
Here are some signs you're approaching
the edge of the context window.
A very long conversation where quality
has started to slip.
A very long document where details from
the middle aren't showing up in
responses.
Expecting the model to recall something
from a prior session without a memory
feature enabled.
Here are some techniques to stay on the
good side of the cliff. Lead with what
matters. For long documents, put the
most important material near the top
rather than burying it on page 12.
Chunk long work into passes. Process a
big document in sections rather than one
giant upload.
Use product features that save your
context. Use things like projects or
skills that save your context for common
areas you want to work in.
If quality degrades over a long
conversation, start fresh.

[00:05]
That slippage is often a context limit
rather than a capability limit. A new
chat with a short summary of where you
were can outperform pushing through.
Working memory is the mechanism that
makes description work.
Everything you describe to an AI, your
instructions, your constraints, your
examples, has to live inside this window
to have any effect.
Understanding the window size, its
edges, and its reset behavior is what
tells you how to structure a prompt,
when to restate critical context, and
what's actually worth uploading versus
what you can leave out.

</details>


What this enables

* Rapid in-session adaptation to *your* docs, data, and constraints
* Coherent work across long threads while space remains
* Precise grounding in supplied material

Where it characteristically fails

* Hard length limits — a cliff, not a gradient
* "Lost in the middle" — buried details get less attention
* No persistent memory by default; corrections don't carry over

Claude features that push the edge out

Memory
Projects
Context compaction
File & artifact attachments

## Steerability

> *How much am I in control?*

The model follows instructions by continuing a pattern, not by understanding intent. Remarkably steerable — but a gap always exists between what you meant and what landed.

[Watch the lesson · 5 min](https://www.youtube.com/watch?v=M_RwSRmp220)

<!-- yt-inline:M_RwSRmp220 -->
[![How steerability affects generative AI outputs](https://img.youtube.com/vi/M_RwSRmp220/hqdefault.jpg)](https://www.youtube.com/watch?v=M_RwSRmp220)

<details>
<summary>자막: How steerability affects generative AI outputs (5:13)</summary>

[00:00]
Hi there. My name's Matt and I'm on the
user research team at Anthropic.
Today, I'm here to talk to you about
steerability in AI models.
We'll look at why instructions work so
well most of the time, why they
sometimes land in a way that's
technically correct but totally useless,
and what you can do to keep the model
pointed at what you actually want.
If you've ever told an AI "Be concise."
and it dutifully trimmed the response
but cut the one part you cared about,
you've already encountered this topic.
Steerability is the model's ability to
follow your directions. You say "Respond
with a table." and you get a table. You
say "Write this from a skeptic's point
of view." and it shifts perspective.
Specify a role, a tone, a format, a word
limit, a set of rules, and the model
applies them, often on the first try.
This didn't happen automatically. Out of
the box, a pre-trained model is a
document completer but no concept of

[00:01]
helping. Fine-tuning is a second round
of training where the model learns from
curated examples of good assistant
behavior.
That's where it picks up the habit of
treating your text as a request,
breaking tasks into steps, and following
the rules you set. But steerability
isn't the same thing as understanding.
The model follows your instructions
through the same pattern completion
engine it uses for everything else.
There's always some gap between the
words you typed and the intent you had
in mind. And many interesting AI
limitations live in that gap.
Let me show you what that gap looks
like.
I'll ask Claude "Summarize this report
in under 100 words and make it punchy."
So, that's 100 words. It's punchy. The
instruction was followed to the letter.
But the one qualified finding I actually
needed made the summary less punchy, so
it got cut.
The model honored what I said and missed
what I meant. It helps to picture your
instructions on a spectrum.

[00:02]
On one end, you've got directions that
are short, concrete, and easy to check.
"Respond as a table."
"Under 100 words." "Use this exact
schema."
These sit firmly in the capability zone.
The pattern is simple to match and you
can verify it at a glance. Slide toward
the other end and control starts to thin
out. Long chains of reasoning where a
small mistake in step two quietly
carries through steps three, four, and
five.
Abstract directions like "Be
insightful." where the model has to
guess what you mean. So, the question to
ask yourself isn't "Did I write a good
prompt?" It's more like "How much room
is there between what I typed and what I
actually want?" When you're in the
capability zone, steerability gives you
a lot.
Tight control over format and style, the
ability to set a persona and have the
model hold it across a whole
conversation,
multi-step task execution where you lay
out a process and it works through it,
and iterative refinement where

[00:03]
"Shorter." "More formal." "Try the
opposite angle." all land.
Drift toward the edge and you'll see
reasoning drift. Small errors compound
over long chains and the model doesn't
notice.
Letter over spirit, like we just saw.
The instruction is honored literally but
uselessly.
Instructions as an attack surface.
Because the model follows instructions
embedded in text, a malicious
instruction hidden inside a document or
web page can be followed, too.
This is called prompt injection. More of
a security concern than a daily one, but
worth knowing exists.
A few product features are built
specifically to narrow these gaps.
System prompts and custom instructions
give you standing directions that don't
dilute as the conversation gets longer.
Visible reasoning lets you catch drift
at step two rather than discovering it
in the final answer.
And structured output modes, JSON
schemas, function calling narrow the
room for letter over spirit wandering.

[00:04]
State the goal alongside the steps.
"I'm trying to persuade a skeptical
audience." gives the model more to work
with than a format spec alone.
Break long chains with checkpoints.
Ask for an intermediate result you can
verify before the model keeps going.
When an instruction lands literally but
uselessly, restate the goal rather than
the instruction. Repeating "Be concise."
louder doesn't fix a concision problem
that was really an intent problem.
Keep concrete, verifiable instructions
near the task. Short and checkable beats
long and ambiguous. In the 4D framework,
steerability is both the thing
description exploits and the constraint
it operates inside.
Good description narrows the gap between
your words and your intent. And it
shapes delegation, too.
Tasks that need long reasoning chains or
native numeric precision need either
tighter human checkpoints or a different
tool entirely. The model will follow
you.
Your job is to make sure following you
and doing what you actually need point

[00:05]
in the same direction.

</details>


What this enables

* Precise control over format, style, length, and tone
* Role-setting and persona
* Multi-step execution and iterative refinement

Where it characteristically fails

* Reasoning drift — small errors compound over long chains
* Letter-over-spirit — instruction honored, intent missed
* Prompt injection — other text in context can steer it too

Claude features that push the edge out

System prompts / custom instructions
Extended (visible) thinking
Code execution

## Go deeper

Anthropic Academy · Free course

AI Capabilities and Limitations Course

Work through each property with hands-on exercises, videos, and real examples in the full course. You'll learn to spot which property is in play when AI surprises you — and what to do about it.

[Take the course](https://anthropic.skilljar.com/ai-capabilities-and-limitations)

About 90 minutes

## Related tutorials

[Why does bias exist in AI models?](/resources/tutorials/why-does-bias-exist-in-ai-models)Why does bias exist in AI models?

Why does bias exist in AI models?

Tutorial

[Tutorial](/resources/tutorials/why-does-bias-exist-in-ai-models)Tutorial

[The 4 Ds of AI Fluency — Behavioral Indicators](/resources/tutorials/the-4-ds-of-ai-fluency-behavioral-indicators)The 4 Ds of AI Fluency — Behavioral Indicators

The 4 Ds of AI Fluency — Behavioral Indicators

Tutorial

[Tutorial](/resources/tutorials/the-4-ds-of-ai-fluency-behavioral-indicators)Tutorial

[What is sycophancy in AI models?](/resources/tutorials/what-is-sycophancy-in-ai-models)What is sycophancy in AI models?

What is sycophancy in AI models?

Tutorial

[Tutorial](/resources/tutorials/what-is-sycophancy-in-ai-models)Tutorial

[Why do AI models hallucinate?](/resources/tutorials/why-do-ai-models-hallucinate)Why do AI models hallucinate?

Why do AI models hallucinate?

Tutorial

[Tutorial](/resources/tutorials/why-do-ai-models-hallucinate)Tutorial
