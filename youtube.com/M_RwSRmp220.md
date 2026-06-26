---
title: "How steerability affects generative AI outputs"
url: https://youtu.be/M_RwSRmp220
channel: "Claude"
date: 2026-04-22
duration: "5:13"
lang: en-orig
youtube_id: M_RwSRmp220
processed_at: 2026-06-26T08:11:40Z
---

# How steerability affects generative AI outputs

- 채널: [Claude](https://www.youtube.com/channel/UCV03SRZXJEz-hchIAogeJOg)
- 발행: 2026-04-22
- 길이: 5:13
- 영상: <https://youtu.be/M_RwSRmp220>

## 자막 (en-orig)


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
