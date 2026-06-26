---
title: "Anthropic’s new 100K context window model is insane!"
url: https://youtu.be/2kFhloXz5_E
channel: "AssemblyAI"
date: 2023-05-11
duration: "9:11"
lang: en-orig
youtube_id: 2kFhloXz5_E
processed_at: 2026-06-26T07:55:59Z
---

# Anthropic’s new 100K context window model is insane!

- 채널: [AssemblyAI](https://www.youtube.com/channel/UCtatfZMf-8EkIwASXM4ts0A)
- 발행: 2023-05-11
- 길이: 9:11
- 영상: <https://youtu.be/2kFhloXz5_E>

## 자막 (en-orig)


[00:00]
oh it worked anthropic just launched a
model with a 100 000 total context
window this is a 10x Improvement and
context window size and enables us to
now feed entire books or any long
document directly into the model and
then ask complex questions about the
input text most other language models at
the moment can handle only between two
to eight K tokens with a few exceptions
but 100K is unseen to the state so this
is an incredible step forward so let me
explain what this means and then I'll
show you a cool demo the context window
refers to the total number of tokens an
llm can take in at inference time a
helpful rule of thumb is that 100 tokens
correspond to around 75 words so for
example if a model can handle 4096
tokens you can feed around 3 000 words
into it with anthropic's new Cloud Model
you can now feed around 75 000 words
into it let's put this in context Mary
Shelley's Frankenstein contains around
75 000 Earth so the whole book fits into

[00:01]
the model this five hour long podcast
contains 58 000 words and about 65 000
words are spoken in eight Star Wars
episodes to consume and digest this
content it takes us humans many many
hours Claude can do all of this in less
than one minute here are some possible
things you can do with it for example
Claude can digest summarize and explain
technical documents like financial
statements legal contracts or research
papers you can also use it to ask
questions and find answers in Long
documents without having to search just
drop your documents into the context and
ask what you're looking for but it can
do much more than summarization or
simple Q and A because the whole
document is in the context Claude can
respond with analysis or perform complex
tasks that require synthesizing
information across the entirety of your
document in my opinion this is awesome
but I think instead of just talking
about it let's look at it in action so
let's look at a demo and I want to try

[00:02]
this out with a podcast episode from The
Lex Friedman podcast and this is the
episode with John Carmack one of the
founders of Doom and Quake this is a
pretty cool episode which I highly
recommend watching but it is five hours
long so now I want to analyze this much
quicker and the first step is to get the
transcript so we get the text that we
can then feed into the model for this we
can use our assembly AI API and I
already created a lot of tutorials here
on this channel how to do this so I
won't go into detail now but basically
here I have a helper function that sends
two API requests one to start the
transcript and then want to get the
transcript when it's completed and then
I will save this to a Json file and you
could either upload a local file or if
the file is already hosted somewhere
then you can use the URL directly which
is the case here so you can get this
from various places here I'm using
listen notes so now let's run the code
and get our transcript and it worked and

[00:03]
saved the file so let's take a quick
look here we get the text the following
is a conversation with John CarMax so it
worked and as you can see this is a very
long file here so it would take us a lot
of time to consume this content so the
first thing I want to do is to tell
Claude to give us a summary of this so
let's load our text again and then first
let's get a rough estimation of how many
words are in it by calling the dot split
method and then also by applying our
rule of thumb to get the tokens so as
you can see we have almost 58 000 words
in it and 77 000 tokens so this should
fit into the model and how to use
anthropics Claude we can use their
python SDK that we can install and then
import and then of course we also need
an API token and then we can set up a
client and then we call client
completion and give it a prompt and also
select a model as you can see here we
use claw version 1.3 and then the new

[00:04]
one with the 100K context window then we
also set the max tokens to sample and
then we print response.completion and
now we need to specify our prompt so let
me copy and paste this here so first we
give a little bit of context we say here
is the transcript of a Lex Friedman
podcast and then we dump the whole
transcript in here and then we say
you're an expert at writing factual
summaries write a summary of the
transcript in about 10 sentences and
then the assistant replies with I would
be happy to help here's the summary so
let's run this and see what we get and
here we get our summary so let's read it
very quickly John Carmack is a legendary
programmer and game developer who
co-founded ID software he is known for
groundbreaking games like Wolfenstein 3D
doom and Quake which is correct then he
started programming as a kit and quickly
developed a passion for it then also he

[00:05]
left softest and started ID software
then they're talking about 3D graphics
and this time at Oculus then also about
AGI so yeah all of this is correct so
now that we know what the podcast is
about let's ask some specific questions
about a few topics so first let me copy
and paste the same code in here and now
since I know that they are talking about
programming let's ask a question about
this section so let me ask based on the
transcript what are some of karmic's
views on C plus select one or two
relevant quotations about C plus plus
from the transcript and then explain
karmic's opinion and by the way we can
also get rid of this this is just to set
the tone a little bit so let's try this
prompt and here we get our response so
here are two relevant quotations from
karmic about C plus plus when I'm
sitting down to do what I consider kind
of serious programming it's still in C
plus plus and it's really kind of a c
flavored C plus plus at that where I'm
not big into the modern template meta

[00:06]
programming sort of things and also he
says that he spent a few years working
with lisp and Haskell and then later
here he says and that changed a lot of
the way I write my C plus code based on
what I learned and then the model
concludes based on these quotes it seems
karmic value C plus plus for serious
programming work but prefers a simpler C
flavored style without heavy use of
templates or object orientation so I
think this is really impressive it
answered a specific question about one
of the topics in this long podcast now
let's ask for something where the model
has to look in different places of the
podcast so let me again copy and paste
this and now let's ask here do they talk
about what video games Carmack
developed and then let's say if so
please list them here so let's run this
cell and I made a small typo but it

[00:07]
didn't matter so here we got our
response yes Sean karmic discusses
several video games that he developed in
the conversation and then it lists it as
requested wolvenstein 3D Doom quake and
Commander Keane he also mentions other
games that he was inspired by like Super
Mario Bros Battlezone or Star Wars the
our card game and finally he discusses
some of the tools and Technologies used
to develop these games so yeah I think
this is super helpful so it even found
some more information so to me this is
very impressive and I also have to give
a shout out to our assembly AI API
because the transcript was very accurate
and worked perfectly together with
Claude so here are just two more cool
ideas you can try out with it for
example you could throw in entire
documentation pages and then ask please
review these documents carefully and
then provide a summary of a specific
section in this case or you can throw in
entire long papers for example from
archive and then then ask can you

[00:08]
explain the section on XXX to me please
briefly explain the background ideas and
then explain the new contributions of
this paper so yeah try this out on your
own and let me know what you think
alright hopefully this demo could give
you an idea of what's possible with this
100K context window model now if you've
watched our last video about Vector
databases I will drop this here you
might be wondering if this makes them
unnecessary well this large context
window doesn't completely solve the
problem for a longer context or if you
need to query over a collection of books
or transcripts for example you'd still
need additional workarounds to store the
data but if your data fits into the
context window this new model indeed
helps to avoid spinning up custom Vector
databases to me this is an incredible
step forward and I think you just gotta
try it yourself and play around with the
model to get a feeling for what this
enables so let me know in the comments
what you think about it so if you want
to try it out and learn more then check
out anthropics blog post about it all
also if you want to easily combine this

[00:09]
with audio or video data then check out
our assembly AI API both links will be
in the description below and I hope you
enjoyed this video and then I hope to
see you next time bye
