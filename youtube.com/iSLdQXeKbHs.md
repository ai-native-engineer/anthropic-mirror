---
title: "Understanding knowledge gaps in AI models"
url: https://youtu.be/iSLdQXeKbHs
channel: "Claude"
date: 2026-04-22
duration: "5:24"
lang: en-orig
youtube_id: iSLdQXeKbHs
processed_at: 2026-06-26T08:08:03Z
---

# Understanding knowledge gaps in AI models

- 채널: [Claude](https://www.youtube.com/channel/UCV03SRZXJEz-hchIAogeJOg)
- 발행: 2026-04-22
- 길이: 5:24
- 영상: <https://youtu.be/iSLdQXeKbHs>

## 자막 (en-orig)


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
