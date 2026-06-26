---
title: "How AI models use next token prediction"
url: https://youtu.be/kl0gunXTvyk
channel: "Claude"
date: 2026-04-22
duration: "4:15"
lang: en-orig
youtube_id: kl0gunXTvyk
processed_at: 2026-06-26T08:09:33Z
---

# How AI models use next token prediction

- 채널: [Claude](https://www.youtube.com/channel/UCV03SRZXJEz-hchIAogeJOg)
- 발행: 2026-04-22
- 길이: 4:15
- 영상: <https://youtu.be/kl0gunXTvyk>

## 자막 (en-orig)


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
