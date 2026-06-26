---
title: "Tool use with the Claude 3 model family"
url: https://youtu.be/6wkFb2_cUik
channel: "Anthropic"
date: 2024-04-04
duration: "2:13"
lang: en-orig
youtube_id: 6wkFb2_cUik
processed_at: 2026-06-26T07:57:50Z
---

# Tool use with the Claude 3 model family

- 채널: [Anthropic](https://www.youtube.com/channel/UCrDwWp7EBBv4NwvScIpBDOA)
- 발행: 2024-04-04
- 길이: 2:13
- 영상: <https://youtu.be/6wkFb2_cUik>

## 자막 (en-orig)


[00:00]
one of the newest exciting features of
the cloud 3 Model family is tool use
also known as function calling tools
that cloud can use are represented by a
Json schema that tells the model about
the capabilities of the tool and the
arguments it accepts during generation
the model can make a call to any of its
tools which the client can then dispatch
and return the
results for example this Hau model which
is our fastest and most affordable model
has access to a fetch webpage tool and a
stand boxed python reppel tool so it can
retrieve information from the internet
and run code we're going to use it to
retrieve an implementation of quick sort
one of the most popular sorting
algorithms and check how fast it runs on
a sample
input now because Haiku is pretty fast
I've actually slowed down this demo by
5x so that we can see the tokens being
generated you can see that Haiku is able
to link together several different tools
to accomplish a
task now things get even more

[00:01]
interesting when models can call other
models as
tools for example let's say I want to
find the fastest implementation of
quicksort
online here I'm asking Opus our most
advanced model to find 100 permissively
licensed quick sort implementations on
GitHub then 100 houp models write tests
to determine how fast each
implementation is and then we'll be able
to determine which is the quickest quick
sort while we let this run here's how it
works under the hood
we've given Opus A dispatch sub agents
tool to parallelize this work where it
can write a prompt template and provide
a list of
arguments the Haiku sub agents each get
the template filled in with their
respective argument then all of the
answers get return to Opus which Returns
the fastest
implementation and here we see that the
fastest result is available here and it
has some additional optimizations that
some of the other implement don't have

[00:02]
tool use with sub agents is a great way
to combine the intelligence of Opus and
the speed and affordability of haiku to
take action on large amounts of
information at scale hope you try it out
soon
