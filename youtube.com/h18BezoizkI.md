---
title: "How do you improve speed and decrease costs with prompt caching?"
url: https://youtu.be/h18BezoizkI
channel: "Anthropic"
date: 2024-11-25
duration: "4:47"
lang: en
youtube_id: h18BezoizkI
processed_at: 2026-06-26T08:06:10Z
---

# How do you improve speed and decrease costs with prompt caching?

- 채널: [Anthropic](https://www.youtube.com/channel/UCrDwWp7EBBv4NwvScIpBDOA)
- 발행: 2024-11-25
- 길이: 4:47
- 영상: <https://youtu.be/h18BezoizkI>

## 자막 (en)


[00:00]
Let's talk a little
bit about prompt caching.
It's a feature that we've
released relatively recently,
leads to tremendous cost savings.
We'd just love to know more,
especially with customers
that you've worked with
where this is a good fit
and how they can start leveraging this.
Yeah, for sure. So prompt
caching is a feature we can add
on top of our models.
So Anthropic, we're training models,
but we can also build
things on top of the models
to make them faster, more efficient.
And prompt caching is a
particularly exciting one.
And so the idea with prompt
caching is if you have a prompt
that you're running, let's
say you have a workflow,
I don't know, you're
labeling a bunch of data,
you're doing a big backfill,
something like this,
and you have a prompt and it
has a bunch of examples in it,
and then just a little
bit at the end that's like
categorized as email for
me, something like that.
What prompt caching lets you
do is the start of the prompts
that is fixed, you can actually
kind of cache that portion.
One, it makes your queries
run quite a bit faster.

[00:01]
And two, because we're
doing less calculations,
there's less compute, there's
actually a meaningful cost
savings that we pass on to our developers.
And so what this means is that
the prompts that you cache
or the input tokens that you cash,
you get a nice 90% discount
and all of a sudden your
prompts run quite a bit faster.
And I, I've heard a
bit from folks internally
that prompt caching also
allows for the ability
to make your first initial
prompt much larger, things like
adding more examples and so on.
What else can you potentially
unlock with prompt caching?
Yeah, that's a great point.
So once you have prompt caching, all
of a sudden you might start
doing things with your prompt
that you wouldn't have considered before.
And the big one is now
you could add 20, 50,
a hundred more examples
to your prompt, which might
help with task accuracy.
And you won't incur the cost of doing that
because now all those are cached
and you are getting responses
in the same, about the same

[00:02]
amount of time, and you're still
paying about the same price.
That sounds fantastic.
So why not cache everything?
That's a good question.
That might not be practical.
So for sure, this doesn't
make sense for every prompt.
Certainly there's workflows
out there where, you know,
the content that you're
putting into the prompt is
wildly different.
A lot of RAG use cases come to mind
where you might be pulling
in, depending on, you know,
what the end user is asking
for, different kind of cuts
of your knowledge base, things like that.
It might not make sense
for every workflow.
So dynamic data is really
where this is gonna not work as well.
Right. We're gonna be
thinking about prompts
where there's just this
large fixed amount of text
that you're passing into
the model every time.
Got it. And are there
considerations to think about
between prompt caching
and different models like
Haiku or Sonnet?
That's a good point. For instance,
you could imagine you might
be able to use prompt caching
with a model like Sonnet
and all of a sudden get
some of those nice cost

[00:03]
and latency characteristics that you might
otherwise have had to,
like, use Haiku for right?
On top of that,
you know, if you're able
to use prompt caching with Sonnet,
perhaps on like a more absolute
basis, you know, being able-
Sonnet is slower, more
expensive, the 90%, you know,
the discounts and the latency
boost might matter a little
more than on a model like Haiku,
which is already very fast, very cheap.
So prompt caching is gonna
save a tremendous amount
and message batching,
also another feature that
we recently released can also
help with cost savings.
Let's talk about that
for a little bit for some
of the wins that customers can get.
Can you walk me through that
feature and that might be
a good use case for it?
So that's another feature
that we recently released
that sits on top of the models.
And the idea here is you
can pass a bunch of prompts
to us at one time
and say, Hey,
I don't totally care when you
get the responses back to me,
Anthropic, do it when it makes sense.
And then we, over the course of 24 hours,
usually much faster than
that, process those prompts

[00:04]
and return them to the user.
And because of that, we
can pass on a 50% discount.
And you can use prompt caching
and batching together to really
save. Is that accurate?
You can, yes. Wow.
So considering those
with an even smaller model,
especially one like 3.5
Haiku that has quite a bit
of intelligence, there are tremendous
cost savings you could see here.
Absolutely.
That's fantastic.
And for folks that wanna get started
with using prompt
caching, message batching
and so on, where would
you recommend they go?
I would recommend they go
to the Anthropic docs.
We have great documentation
for all these features.
Excellent. I know a lot of
folks on your team also have
been working on cookbooks
and really good use cases
as well. So a lot of good resources.
Yeah, you're gonna see
docs, you're gonna see code,
examples, everything
you need to get started.
Awesome.
