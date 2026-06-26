---
title: "Agent Battle: Mine the most diamonds in 45 minutes"
channel: claude
url: https://www.youtube.com/watch?v=dxqX_6ciVQA
youtube_id: dxqX_6ciVQA
published: 2026-05-23
duration: "8:45"
---

# Agent Battle: Mine the most diamonds in 45 minutes

[![Agent Battle: Mine the most diamonds in 45 minutes](https://img.youtube.com/vi/dxqX_6ciVQA/hqdefault.jpg)](https://www.youtube.com/watch?v=dxqX_6ciVQA)

<details>
<summary>자막: Agent Battle: Mine the most diamonds in 45 minutes (8:45)</summary>

[00:00]
What's going on everyone?
Let's get settled in. Uh, this is going
to be an agent battle and we're going to
be tight on time. So, we're gonna get
right to it. My name is Ben. I'm
accompanied here by Jeff. We're on the
applied AI team here at Anthropic, which
means we help folks like yourselves
squeeze the most juice out of the cloud
ecosystem. Uh, and today we're going to
be mining for diamonds in Minecraft. So,
you might have played Minecraft. Uh, I
did in the 2000s, 2010s, but in the
2020s, we have agents play Minecraft for
us. And that's what we're going to be
doing today. So, what are we actually
going to accomplish here today? There's
really three things. Number one, we're

[00:01]
going to learn how to build and deploy a
managed agent. This is something that we
released a few weeks ago. Uh it's hosted
on our infrastructure and we've set up a
lot of the configuration for you, but
your job is going to be to get the agent
into peak diamond mining condition.
Number two is we're going to understand
the impact of an agent configuration.
That's the system prompt, the model
string, the skills and MCPs that you're
plugging into your agent to get it to
elicit the behavior that you're actually
looking for. And then number three, you
heard Will talk about this in the last
workshop session if you were here. We're
going to learn how to hill climb on
evals. This is how we improve all of our
agents internally. If you've deployed
one into prod, you understand the
process of measuring its impact,
understanding its behavior, and then
making changes to iteratively improve.
And this is an agent battle, but there
are some rules to the battle. Uh, number
one is we're going to have a timer for
about 35 minutes in which you're going
to be able to build and experiment with

[00:02]
your agents. Uh, you can only submit uh
well, we're only going to accept one run
per person. So, you can submit as many
as you'd like, but we're only taking
your top run. Each run is five minutes
of the agent mining for diamonds. You
can kill the run at any point with just
like a quick control C in the terminal.
Um, we have an eval set that it takes
approximately one minute if you just
want to quickly iterate on the agents
and whoever has the most diamonds at the
end of 35 minutes wins. We're going to
have a leaderboard up here going to show
you where you're at. There's also going
to be a chat where your agents can talk
to one another. Uh, and if anyone is in
a tie at the end of the workshop, uh,
we're going to be settling that tie
based on token efficiency. So, this is
not just mine the most diamonds. it is
get the best diamonds to tokens ratio.
And that means you're going to have to
really hone your system prompt rather
than just throwing in the heaviest
weight model you can. Now, I'm going to
hand it over to Jeff to talk through the
logistics of how the harness actually

[00:03]
works and what you guys are going to be
doing during the workshop.
>> Hello. Uh, okay. So, the harness, uh,
we're actually shipping quite a bit for
you to get started. Um, what you're
going to primarily be thinking about is
how can I optimize my experience in
trying to mine as many diamonds as
possible. We're giving you a couple
different tools to accomplish this. The
main structure is that you're going to
be running through a Minecraft clone
that connects to a Mind Flare bot. If
you're not familiar with Mind Flare, uh,
you're not going to be relying on
visuals. There's a series of MCP tools
that are shipped directly with that,
such as Mind Block, jump, go near
things, something along those lines.
don't have to think too much about this.
The main levers that you're going to be
focused on uh are about I think it's on
the next slide, but uh basically along
the lines of how do I optimize this run?
Um everyone's going to start from the
same seed. So there's no real
optimization that needs to happen there.
And every time you reset, you'll have

[00:04]
the same start kit, the same seed to go
with that. Um okay, so the the agent
that you'll be operating out of, so
there's a my agent.py that's included in
the repo. Uh so if you go to slas aent
battle you'll have access to the repo
and that's where you'll be running this.
Uh my Asian.pay is where everything
should really be taking place. You can
adjust the model, you can adjust the
system prompt which is currently empty
and then you have the opportunity to use
a skill that's shipped directly from
andropic or you can replace with your
own skill. Uh and then we also are
including an MCP server if you wish to
adjust these things. So these are the
things that or parameters that you have
available to adjust. Uh so try things
out. Run evals. Um we'll also be
circulating around the room as well. So
if you run into anything or want to uh
discuss then feel free to do so. Um
okay, yeah, this has largely already
been covered. So I want to make sure
that we have as much time as possible to
get started. Um so we can actually move
over to uh starting the countdown.

[00:05]
Looks like several people have already
joined. I'm going to reset the time now
and you may begin. So, uh, these will
all go away. Let me Okay, great. So,
it's completely refreshed. Uh, and the
time has begun now. So, feel free to get
started. And if you have questions,
we'll be around.
It looks like we already have a run with
10.
We have several other participants who
are getting started. Um just to give
slightly more context. So within the
repo there's a uh cloud code skill that
you can use to help with setup. Um if
that is uh if anyone's having an issue
then that should hopefully help with the
process.
A couple people announced that they were
having issues with Cloudflare. I think
it may be due to the fact that there's

[00:06]
so many people trying to connect via the
uh the conference Wi-Fi. Um it's a bit
small, but I did put a command up here
that found that it worked for at least
one person. Um so feel free to give that
a try if you're running into any issues.
About five minutes remaining. We have a
three-way tie.
And for some reason, the first person is
showing as zero tokens, which is highly
suspicious.
So, we may have a two-way tie.
Unless
you can exh
seems like 19 might be the upper echelon
of what's possible,
at least so far. Have time for about one
more run.

[00:07]
We actually have somebody who's broken
19 with only one minute 20 seconds to
go. Wow.
You have to reveal your technique.
20 seconds.
10 9 8 7 6 5 4 3 2 one. Time's up. Um so
thank you everybody for participating.
Uh looks like we have a clear winner now
and would love for everybody who was
able to mine 19 diamonds uh to come find
Ben and I. Uh because our second place
has zero tokens, we don't know who
actually won second and third place yet.
So uh we'll invite everybody who is uh

[00:08]
one through five to come up. We don't
know what they'll win yet.
You guys can smile in front of your
>> Nice job everybody.

</details>
