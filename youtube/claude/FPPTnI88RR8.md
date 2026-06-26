---
title: "How Anthropic uses Claude in Cybersecurity"
channel: claude
url: https://www.youtube.com/watch?v=FPPTnI88RR8
youtube_id: FPPTnI88RR8
published: 2026-05-12
duration: "3:42"
---

# How Anthropic uses Claude in Cybersecurity

[![How Anthropic uses Claude in Cybersecurity](https://img.youtube.com/vi/FPPTnI88RR8/hqdefault.jpg)](https://www.youtube.com/watch?v=FPPTnI88RR8)

<details>
<summary>자막: How Anthropic uses Claude in Cybersecurity (3:42)</summary>

[00:00]
Cyber security at Anthropic I would
[music] say is I'm biased but I think
it's one of the most interesting parts of
the company. There's no [music] precedent
for what we're building and so securing it
is also kind of you know a new frontier.
The thing that I've always kind of [music] been
stuck on is that we have these tools to do this
work, but a lot of them don't actually fit
[music] what the analysts or investigators,
people with boots on the ground are
doing. Before investigating a security
event would be [music] jumping between five
to six different tools, running, you know,
three to four different query languages over
different databases. For a simple investigation,
it would take a couple hours at least [music] and
a couple days at most. And that is part of why we
built Clue. Clue is a detection and response
platform that we've built with cloud code.
One thing that makes Clue so powerful is
it is connected to our internal system. So
it has access [music] via tool use to query our
data warehouses, but it also has the ability to

[00:01]
query like internal knowledge of our company.
[music] So Slack messages and our code bases.
That is usually like that missing piece [music]
that really helps alerts be contextualized for
your environment. to note this is just a
sample set of data that I've imported into
clue. So this isn't actually anthropic internal
information. How we start in clue investigate is
the user being me would ask a question. So I say
a developer just gave themselves [music] admin
access. Is this authorized? Can you check for
credential compromise and what actions they
took afterwards? [music] And so we have asked
Claude to come up with a plan on how it would
investigate this. [music] Comes up with these six
steps. Then it will kick up a bunch of queries.
And so these are the tools that's reaching out
for more information to help us figure out what's
going on. And we see the assistant Claude has
come back and has gathered some more information.
And it says, you know, this kind of looks like a
pretty classic privilege escalation. Here's some

[00:02]
of the reasons I'm coming to that verdict.
And it's going to issue some more queries.
This is again this is sample data but it the
source IP when looked up was a Russian data center
and it was flagged as malicious by virus total
and it then actually comes to you know good news
this [music] seems to be isolated but it's also
identifying there's some gaps in our security
posture on this system so there's some afteraction
items that we could take and then finally the
final investigation summary that Claude will come
up with and share with you all the investigations
that were taken and the findings we have this
ability to go through immense amounts of data,
immense amounts of alerts [music] and then just
raise what actually a human should look at. I had
been working on our Q4 plans and I was like okay
we're going to work on this suppression engine
and this is going to take you know at least 1 to
[music] two months. One of our new hires built
it in a week. Most of it is because Claude Code is
able to explain to [music] them here's how this is

[00:03]
set up. Here's how it's working. And it feels like
for me when I bring people on that I'm giving them
a tool that will [music] give them that autonomy
rather than them having to, you know, kind of like
swim in the deep end immediately. [music] I'm
building the tools that I wish that I had. And
I'm actually able to [music] do what I feel like
is pushing from being a practitioner to being a
researcher, kind of a scientist, [music] because
I'm getting to test out a lot of the ways that,
you know, I've only imagined us being able to
process, you know, this immense [music] amount
of data and have more visibility into our
systems that previously was just out of reach.

</details>
