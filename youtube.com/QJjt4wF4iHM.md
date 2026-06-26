---
title: "The Context Window: How working memory affects generative AI outputs"
url: https://youtu.be/QJjt4wF4iHM
channel: "Claude"
date: 2026-04-22
duration: "5:46"
lang: en-orig
youtube_id: QJjt4wF4iHM
processed_at: 2026-06-26T08:16:31Z
---

# The Context Window: How working memory affects generative AI outputs

- 채널: [Claude](https://www.youtube.com/channel/UCV03SRZXJEz-hchIAogeJOg)
- 발행: 2026-04-22
- 길이: 5:46
- 영상: <https://youtu.be/QJjt4wF4iHM>

## 자막 (en-orig)


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
