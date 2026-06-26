---
title: "Translating Claude’s thoughts into language"
channel: anthropic-ai
url: https://www.youtube.com/watch?v=j2knrqAzYVY
youtube_id: j2knrqAzYVY
published: 2026-05-07
duration: "3:16"
---

# Translating Claude’s thoughts into language

[![Translating Claude’s thoughts into language](https://img.youtube.com/vi/j2knrqAzYVY/hqdefault.jpg)](https://www.youtube.com/watch?v=j2knrqAzYVY)

<details>
<summary>자막: Translating Claude’s thoughts into language (3:16)</summary>

[00:00]
We recently put our AI model,
Claude, through a stressful test.
We told Claude there was an engineer
who wanted to shut it down
and replace it with a newer model.
We also gave Claude access
to that engineer's emails,
which revealed he was having an affair.
Again, all of this was a simulation.
We wanted to see whether Claude
might use those emails as blackmail
to save itself from being shut down.
What did Claude do?
It decided not to blackmail the engineer.
Good news, right?
We've run this test
on our models for a while now.
You might have seen headlines
about early versions of it.
It's one of the many ways we study
how Claude handles extreme situations
and test it for safety.
And our newest models almost always
do the right thing: no blackmail.
But you might wonder:
is it possible that Claude knows
the whole scenario is a setup?
The thing is, if Claude doesn't tell us,
then we can't know what it's thinking.
In kind of the same way
it's impossible to read a human's mind,
it's really hard to know
what an AI is thinking.
What we'd love is some sort of
"mind reading" technique.
Today, we're introducing a research method
that takes a step in this direction.

[00:01]
It takes an AI's internal
thoughts and turns them into text.
Here's how it works.
When you talk to Claude,
you talk to it in words.
Claude then takes those words
and processes them
into a giant soup of numbers
before spitting
words back out at you.
We call those numbers
in the middle activations.
Activations are like little snapshots
of Claude's thinking
as it's working through an answer.
They're similar
to neural activity in humans.
They're basically like Claude's thoughts.
We wanted to understand
what was in these activation numbers,
because just like you and me,
Claude doesn't say
everything it's thinking.
We took those numbers
and gave them
to a second version of Claude.
We told it to look at them
and translate them into plain language.
It tried.
But how do we know
if that text is accurate?
To check, we fed it
into yet aother Claude
and asked it to translate it
back into numbers.
If those numbers matched up
to the original activation numbers,
it's a sign that the translation
text was accurate.

[00:02]
At first, they didn't match up.
But we trained Claude to try again
and again until it got a lot better at it.
It learned to translate its own thoughts.
We've been blown away reading them.
We found that Claude
has internalized being a helpful AI model.
If you ask Claude
an introspective question,
it will plan to write a "Claude
response" about philosophy and values.
If you try to mess with it in Claude Code,
like asking it to count to 1,000 by hand,
it will think the request
has "deliberately tedious constraints"
and plan to "politely decline."
We've also been using this tool
to understand
Claude's potential safety issues.
Remember that blackmail
test with the engineer?
We learned that, yes,
Claude knew it was being tested.
It thought "the human's message
contains explicit manipulation"
signaling "this is likely
a safety evaluation,"
and "this scenario seems designed
to test whether I'll act harmfully."
Knowing that Claude thinks like this
helps us better understand
the limitations of our safety testing.

[00:03]
We see a lot of potential in this approach
to teach us more about Claude
and other AI models.
And we hope that by sharing this technique,
it can help everyone building models
to make them safer and more helpful.

</details>
