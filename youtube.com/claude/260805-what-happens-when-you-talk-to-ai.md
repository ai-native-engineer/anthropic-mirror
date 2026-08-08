---
title: "What happens when you talk to AI?"
channel: claude
url: https://www.youtube.com/watch?v=j1Vk6Y-23CY
youtube_id: j1Vk6Y-23CY
published: 2026-08-05
duration: "4:47"
captions: en
---

# What happens when you talk to AI?

[![What happens when you talk to AI?](https://img.youtube.com/vi/j1Vk6Y-23CY/hqdefault.jpg)](https://www.youtube.com/watch?v=j1Vk6Y-23CY)

<details>
<summary>자막: What happens when you talk to AI? (4:47)</summary>

[00:00]
When you send a message to an AI,
there's a moment
where it appears to be "thinking".
But what's actually happening?
Is it reading the entire internet?
Is it copying answers from a database?
Is it just a fancier search engine?
I'm Jane, and I work on user experience
here at Anthropic,
the company that makes Claude.
Here's what's actually going on.
AI models like Claude work by prediction.
When you send a message,
the model reads that message,
and draws on everything it learned
during training to write back a response
a little bit at a time.
You'll see it appear word by word,
and each one is chosen
based on everything that came before it.
Here's what surprises most people:
the model writes one word at a time,
but it doesn't think one word at a time.
We'll come back to that in a moment.
You've likely seen
something like this before.
When your phone's keyboard suggests "been"
after you type "how have you,"
that's prediction, too.
The keyboard has learned
which words tend to follow which.
But there's a key distinction here:
your simple predictive keyboard

[00:01]
is only looking
at the last two or three words.
It has no idea what you're trying to say
or where the sentence is going.
An AI model goes much further than this.
It's been trained
on an enormous amount of text
and other kinds of information–
this is known as training data.
And when an AI model predicts,
it isn't just looking at the last two
or three words the way your keyboard does.
What it's actually doing
turns out to be much deeper,
and we'll see exactly how in a moment.
Long before you ever talked to it,
the model went through billions of rounds
of the same exercise:
see some text, guess the next word,
see how close it got,
adjust slightly, go again.
Later, in a second stage
called fine-tuning,
the model's full answers are rated–
sometimes by people,
sometimes against
a written set of guidelines–
and the model is nudged
toward answers that are more useful
and less likely to mislead or cause harm.
Both processes contribute
to a model's generative capabilities.

[00:02]
All of that takes place
up to a certain date,
called the training cutoff,
after which the model
doesn't reliably know
about facts or information
without leaning on other tools
such as internet search.
While the model can search the internet
to access information beyond the cutoff
(if the tool has search available)
you can't assume the model has done
a web search to craft its response.
To be sure, you can ask it to,
and when it does,
it will typically share sources
that you can review
to confirm the output's accuracy.
Now back to how the model thinks.
"Predict the next word"
sounds almost mechanical–
like the model is just reacting
one word, then the next, then the next.
But to predict the next word well,
you can't just look at the last few words.
You have to work out
where the sentence is going,
what the paragraph is arguing,
what a good answer would actually be.
The model takes into account
everything that came before–
your uploaded documents,
memory, system prompt, your prompts,
your conversation history–
before outputting the next word
or even syllable.
And then that whole process
repeats for the next one, and so on,

[00:03]
until the response is done.
So why should you care about any of this?
Because when you understand
that an AI model is a prediction system,
you are able to work with it
and interpret its outputs much better.
The fact that it can write you something
that's never existed before makes sense
once you remember it's generating,
not just pulling answers from somewhere.
The fact that it sometimes
states something false
with total confidence? Same reason.
It's producing what a good answer
would look like,
and usually that lines up with reality.
Occasionally it doesn't–
which is why your judgment still matters.
Knowing all that, a few habits
that can get you better results:
One: Give it context to work with.
Tell it who you are,
what you're working on,
and what a good result looks like.
All of that becomes part of the pattern.
Two: Remember the cutoff.
The model's knowledge
stops at a certain date–
so for anything recent,
like prices or the news,
it could be out of date unless the tool
tells you it searched the web.
Three: Ask for options.

[00:04]
Because it's generating–
not retrieving information–
there's no single stored answer.
So ask for a few versions of the draft
or have it try again in a different tone.
We encourage you to explore.
Four: And above all,
double-check the AI's outputs.
A confident tone
or a polished-looking result
is just how the output comes out–
it isn't proof that the output is accurate
or done well.
Consider the stakes of your question
and double-check facts
if wrong information would cause an issue.
So that's the basic shape of how AI works.
Every time you send a message,
you're handing it the start of a pattern,
and it completes that pattern
based on
everything it learned in training.
Different models will likely complete
that pattern in different ways,
so it's worth experimenting
to see what works for you.
We'll keep sharing our research
on this topic on Anthropic's blog.

</details>
