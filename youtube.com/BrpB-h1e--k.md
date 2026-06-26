---
title: "Building with Claude Managed Agents and Asana AI teammates"
url: https://youtu.be/BrpB-h1e--k
channel: "Claude"
date: 2026-05-08
duration: "24:57"
lang: en-orig
youtube_id: BrpB-h1e--k
processed_at: 2026-06-26T08:00:10Z
---

# Building with Claude Managed Agents and Asana AI teammates

- 채널: [Claude](https://www.youtube.com/channel/UCV03SRZXJEz-hchIAogeJOg)
- 발행: 2026-05-08
- 길이: 24:57
- 영상: <https://youtu.be/BrpB-h1e--k>

## 자막 (en-orig)


[00:00]
Hi everyone. I'm Arnauld from Asana and
I'm here to talk to you about how we've
built Asana's AI teammates on Claude
managed agents.
Our vision at Asana is to bring forward
this promise of the agentic enterprise
where human beings and AI agents can
work together to get complex multi-step
work done. Whether you're in IT or
operations or product or marketing, our
vision is the AI agent is an actor in
the system. It's got a deep set of
skills. It's got all of the context
required and it can work hand-in-hand
with other human beings to get
multi-step work done. Things like
approvals, complete end-to-end
workflows, getting to real-world
outcomes.

[00:01]
So, that's what we've been building and
AI teammates within Asana are generally
available as of March.
What we see today though in the
enterprise is
almost everybody is experimenting with
AI agents. They're building AI agents.
There's a lot of like utilization of
them. But, most most companies are still
using AI agents in the single player way
where an individual can go ahead and
interact with the agent, get an outcome,
and then they pass it on to someone else
to complete those multi-step processes.
You don't end up with compounding
knowledge. You don't end up with this
concept of a a shared enterprise memory.
Uh you don't end up with concepts like
uh true multiplayer multiple
human-in-the-loop interactions.
And uh throughout this presentation I'll
showcase like what have we done that's
sort of set this up and how does
Claude's managed agents capability help
us complete these complex multi-step uh
multi-step workflows. So, our vision is
like full multiplayer mode. You have
agents that are real actors in the
system. They've got sharing and our back

[00:02]
controls just like you would be
onboarding a new teammate, a new human
teammate into the system. They have the
contacts. Uh they can work with multiple
people. They can get nudges and
interactions with multiple people and
they can complete uh complete these
end-to-end jobs to be done. In fact,
like one funny anecdote is I was just
chatting with Hannah before I got on
stage and there are a bunch of like
former Asanas who are now at Anthropic
and one of them had built an AI uh
teammate for us uh that's a competitive
intelligence researcher. And so now,
even though they're no longer at Asana,
uh we still use it on a day-to-day basis
and all of the historical interactions
that he had to set up the context and
the knowledge when, you know, we were
doing competitive responses to RFPs, is
ingrained in that agent and it's just
getting better and better as more people
join the team and keep using it. So,
that con- that concept of uh enterprise
memory
uh and then the shared ability of the
the ability for multiple people to use

[00:03]
agents has been phenomenal for us
internally in our use.
The The other concept that we've been
working on and, you know, again, is
available is this ability to ensure that
the agent gets
complete context about how your
enterprise works. Who does what by when
and why, historical decisions,
approvals, ways in which people have had
back and forth on a particular campaign
brief or a project plan that have
finally led to its approval, those
decisions are tracked inside Asana and
we provide those to the teammate in a
way, again, that preserves security,
guardrails, auditability, so you can get
real-world results and action.
So, Asana is the system of action for
work and it's that so binding layer
where, once you start introducing
agents, you can treat them like human
beings in your team. You know, like we
have a work graph that we've been
building for over 17 years. And it's

[00:04]
this idea that every company has a
mission and vision that is tracked by
goals. Goals are in portfolios.
Portfolios are delivered by a multitude
of projects. Each project has a set of
tasks. And those tasks could have
approvals, workflows, and other things
embedded in them. And as you build out
this context graph that is uh designed
for both human beings and AI agents,
human beings have a easy to comprehend
way, a UI, to interact with like how
your work gets done. And then agents
have a way to represent themselves and
get that uh get that context they need
to get work done and perform in a true
multiplayer way across multiple human
beings following the right security and
guardrails required by your enterprise.
So, we've been building all of this out
for context, shared memory, and ensuring
agents are real actors in the system.
The place where we leverage Claude's
managed agents capability is to complete
those multi-step actions in a way where
where Anthropic's tooling is allowing us

[00:05]
to go complete the task. So, in the demo
that I'll showcase, what you'll see is a
multi-step interaction between a
marketer who's releasing uh a new
campaign as well as multiple people on
their team. And that campaign requires
them to not only write a brief, but also
start producing a few mock-ups for what
that landing page is going to look like
so that the human beings on the team can
get to a shared understanding of whether
that's good to go or not.
So, it involves creating, you know, a
complex document using the right set of
enterprise context uh required to
produce it, as well as creating multiple
iterations of what that landing page,
the public website, should look like.
So, it's like generating HTML. It's a
multi- It's a multi-step action.
So, with the managed agents capability,
there's a few different things that that
uh we use to make AI teammates far more
powerful. So, it helped us reduce our
prototyping costs. Like, we got much
faster prototyping for these actions and
skills.

[00:06]
It comes built in with a verification
loop, so we know that the quality of the
content we'll get at at the end of the
process is high. And then it has this
built-in grader, where once Asana passes
in the outcome it wants to Claude
managed agents, you know, we know that
the grader will go ahead and iterate
through that outcome multiple times to
ensure that we're getting a high-quality
output. So, again, this is allowing us
to focus on the things that is unique to
Asana, the human interface layer to go
ahead and coordinate across multiple
people, the system of context that we're
building out, the security that we're
building out, so that if you're using
the same agent as me or Nigel or Tony,
and we are, you know, we're in different
work graph objects or different
projects, the agent won't leak
information across the other. So, we
focused on that, and the quality of the
output is something we're leveraging
Claude managed agents for.
So, again, like if I compare and
contrast the way in which uh
AI teammates is working today with
Claude managed agents versus the

[00:07]
messages API that we're previously
using,
uh we're getting, again, faster
prototyping because we're not having to
build a manual agent loop, file
management, code execution.
Uh the verification process has gotten
way better with this uh with this sort
of built-in product. And then we can
also enable multiple agents in parallel
to work independently, because a lot of
these like knowledge worker actions like
require multiple agents to work in
parallel to produce a full plan and to
iterate through it.
So, uh again, like as of today, there
are over 21 pre-built agents uh called
AI teammates within Asana. Uh we
designed the pre-built ones to match our
ideal customer profiles across the uh
office of the PMO within marketing,
within IT, within HR, within R&D, and
they can do things like they can help
you with launch planning, they can help
you with
writing specs, they can help you with
goal management, they can help you with
resource management and capacity

[00:08]
planning. And so they're using all of
these existing constructs within Asana
for tracking portfolio goals, for
tracking timeline updates, and they're
taking real action within them as well
as in downstream systems. So they can
pull in data from Google Drive and
Office 365, and we're adding a whole
bunch more integrations over the coming
weeks, and they can take action within
them as well. They can produce slides,
they can add comments, they can create
full HTML, and a lot of those like
capabilities are possible because we've
invested in managed agents, and it sort
of allowed us to run that verification
loop and and multi-step multi-step
workflow.
Um
So like another example I'll give you is
we've been obviously dogfooding this
internally at Asana for months now, and
over over those months I have an agent
for the product management team, which
is me and my directs, and it's like a
it's the product or thought buddy, and
it's got all of the context around you
know why we made certain trade-off
decisions, what the strategy is, and

[00:09]
things like that. And so when our
marketing team for example has questions
about hey, we are planning Work
Innovation Summit London, which is our
next event that's coming up. Here is a
draft of the keynote speech. Could we
get the product team's input on it? The
first thing they do is actually they
create a task in Asana and they assign
that to the product or thought buddy,
and it has all of the trade-offs, the
current roadmap, all the
context for how our roadmap works within
Asana, and it produces a plan, and it
produces
a set of feedback on that on that
keynote speech that is like highly
optimized for the way in which we work
and is
is correct and is accurate from the
perspective of it's using all of the
real-time context.
And again, it's done in a multiplayer
way. So, everybody in the product team
can see that response and they can react
to it. They can give it nudges and it'll
remember that across multiple runs.
So, that's a lot of talking about like
what we've done with pre-built agents,

[00:10]
the multi-step workflows, and outcomes
that are possible with Claude managed
agents,
enterprise memory, shared memory. We
should see it in action to like really
get you a sense for what we're talking
about.
So, let's let's roll the video and I'll
talk you through it. So, in this video,
the the human the human being is is a
marketer and they're trying to launch a
new campaign and they're going to use AI
teammates that are leveraging Claude's
managed agents under the covers. And the
way they'll kick it off is you'll see
them in a Kanban board inside Asana and
they'll just create a new task saying,
"Hey, I'm going to go ahead and and plan
for a new campaign brief." So, let's
roll the video and see that in action.
Yep. So, this is a person.
They're like, "Okay, I've got this like
task to go ahead and create a campaign
brief and prototype a landing page."
Like, it's not only a document, but it's
also a product for a landing page. And
perhaps they haven't used AI teammates
before. They go to the teammate gallery.
They choose one of the pre-built
teammates that have all of their

[00:11]
behavior guidance and description in it.
And when they go in over here and they
customize it for their use, it will
automatically pick up the right work
graph objects, like the previous
campaign projects or portfolios
to add to that teammate's memory so that
it can it can go ahead and produce
better content. So, it's the teammate
has gone ahead and and sort of first
planned out its response
and it's created a
a document which is its campaign brief.
And you'll notice it's also created
an HTML file, which is the landing page
mock-up for this new campaign.
And again, because if you track all of
your processes in Asana, it'll
automatically pick up that context. This
is showcasing what you would see in the
cloud console, right? So, in the console
we pass in the outcome as to the manage
agents product. And then
what we can see is
the runs in within the console to to
highlight that manage agents is is

[00:12]
actually running the greater to to
ensure that the verification loop is
complete and the outcome is is as
appropriate. So, again, like the
combination has an allowed our
development team to ensure that we're
getting high quality outcomes. That's
delivering on the customer promise that
we have, which is you're getting all the
security benefits of our back controls
and app actors, like agents is a true
actor within the system. You're getting
the enterprise context, and then manage
agents is delivering on the outcome. So,
they've gone from just an idea or a
task, which would have taken them a
bunch of time to create the brief, maybe
send it over to creative, and get a
mock-up in place for what that landing
page should look like, down to a land to
to a a page immediately.
Um and then interacting with the agent
and asking to iterate on it is as simple
as talking to it via comments, right?
So, let's say
it picked up green as the primary color,
but the primary color has now changed

[00:13]
based on the summer
whatever team. You can say this is
great, but let's make the primary color
blue,
and you can give it some feedback that
this is our new company sort of primary
color. This will actually get ingrained
into the agent's memory, so if a
different marketer picks up and uses
that agent, it will not make that same
mistake again. It will remember that the
new color scheme is blue.
Uh and so you can see that the campaign
brief writer is working on behalf of
Sushi admin.
Um,
and you'll notice that the memory is
getting created. That's the reason why
we're sort of expanding that. It's not
something that an end user has to go
care about, but we highlight that the
memory is getting created. And boom,
you've got like a blue uh, campaign
brief landing page.
Now, I want to showcase multiplayer in
action. So, uh, this is great. So, maybe
the marketer feels like this is a a good
starting point. They've got a brief.
They've got a mock-up of the page. Now,
they want to bring in uh, somebody else
on their team who can review it and give
them feedback. And you'll notice the

[00:14]
teammate is going to work in multiplayer
mode. So, this new person comes in um,
and they're like, "Okay, uh, teammate,
uh, thank you for doing this, but I
would pref- I would love to see a- an
iteration of it that is more
minimalistic in its uh, in its look and
feel." So, again, just just type it out
as if it's a it's a comment, and it is a
real comment. You can hit go, and then
again, like the cloud manager agent's
functionality will run in the background
and create that minimalistic view.
The other things to call out is because
this is a shared workspace, everything
that's happened, the interactions
between the human beings and the AI
agent is also tracked in the task, and
it's fully auditable. So, at some point
in time, if you need to like bubble this
up to your manager or your lead and get
their approval, you can simply convert
it to an approval. They'll see all the
prompts that have gone in. They'll see
the back and forth between the AI agent
and the multiple humans, and it gives
them that much more confidence that
confidence that the right questions have
been answered, and they're getting the

[00:15]
the best possible outcome without a
bunch of back and forth, right? Like,
"Did you consider a minimalist version?
Did you consider that the the decision
was made to go ahead and move to the
blue color, etc."
Um,
and again, I'm not showing it here in
the demo, but if you go into the the
teammate's detail page, uh, there is
also a concept of uh, who owns or
manages that AI agent. So, these are
back controls and calling out mean that
there's a definition of the human beings
who are the agent sponsors and who can
manage it. And so, those human beings
get a chance to delete memories or
change the parts of the Asana context
graph that the agent has access to to
ensure that it continues to behave
consistently going forward.
Okay.
So, again, like what you're seeing here
is what we have generally available
today. It's using uh it's using these
sort of multi-step actions. It's
documenting everything. It's working in
a multiplayer way. The future for us is
thinking about more capable, more more

[00:16]
multi-step workflows, right? Like uh
what what about entire launch planning
processes? What about resource
management and capacity planning across
hundreds of people? How do you make that
better? How do you how do you generate
dynamic dashboards? How do you generate
risk reports? How do you automatically
alert uh end users on what remediation
steps they could take to go fix issues
and things like that. Uh we're
partnering with Anthropic on learning
faster from team patterns and agent
skills. And we're also identifying
opportunities to move work forward more
proactively. So, proactivity is
something we're working on where if an
agent is uh or an Asana AI teammate is
part of a project or is like looking at
your Kanban board, even if you haven't
assigned it any task, it can
automatically wake up and be like, "Hey,
I can pick that up." or "I've seen uh
this particular issue in a different
project before and this is how you go
ahead and resolve it.
So, what this has allowed us to do as a
company is, you know, we've been able to
focus on all of the aspects that make

[00:17]
Asana great, like the fact that you can
define in a human-readable way what your
multi-step processes as a marketing team
or the office of the PMO or in IT.
And you can interact with these agents
in a way that is very human. It feels
like you're onboarding a new person onto
the team. You're giving them the context
with these projects or documents. You're
giving them feedback. And multiple
people can use them. So,
even in my example of like this person
who's like no longer at Asana, all of
the work that they've done and those
memories are reusable by people on the
team to keep doing that work faster and
doing that work better going forward.
Okay. So, that was
a primer on how we're using managed
agents to deliver Asana AI teammates.
We have about five-ish minutes left, so
I can open it up and take some questions
if there's any in the audience.
Yeah.
Thank you.

[00:18]
Cool, there's a person in the back.
>> Great talk again.
Um, just quick question for you. You
mentioned earlier that the validation of
the like the agent itself happens on the
Anthropic side of things. Just curious
what that looks like and what you folks
would encode in there. Like you
mentioned that Asana has a bunch of
domain knowledge. Does that go into the
verification? Sorry, I didn't realize I
was talking outside of it. Does that go
into the verification process also?
>> So, I I only heard parts of the question
about how do we run the verification
process. Do you Do you mind just
>> Yeah, I can rephrase the whole thing.
So, you mentioned the verification
process happens on the Anthropic side of
things where with they're looking at the
outputs of the managed agents and seeing
if it's in alignment with what like the
spec is for the output. Is there Asana
domain knowledge being injected there as
well? How do you folks go about managing
the contract between the managed agents
and what you folks want it to actually
providing you?
>> Yeah, it's a good question. I think at a

[00:19]
high level what we're doing is we are
passing in the Asana context as part of
the outcome definition.
Uh, as well as um, yeah, yeah, that's
the place we're doing that. And then as
we've been testing it out internally
before we release like a pre-built uh,
capability to our customers, that the
there's like there's like another level
of QA that happens obviously within
Asana like with by our engineering team.
And then in the the the real world use
case and utilization of this is again
because we are a very like human in the
loop system, if there's any issues with
the quality of the output for a
particular customer because perhaps
their context stuff isn't as fully
fleshed out or isn't as detailed, the
more you use it and the more nudges you
give it across multiple people, all of
that compounds and just keeps getting
better. So because we record that back
within Asana and we put it put push it
back as part of the call to run the
managed agent every single time.
>> Yeah, makes sense. Thanks again, great
talk.
>> Yeah. Yeah.

[00:20]
>> Hey, thanks for your talk. Uh
really insightful. Uh could you speak a
bit more about how you designed the
rubric uh on like your like the rubric
that your grader sees to iterate uh on
the uh outputs that it generates?
Were there any learnings there?
>> Were there any learnings about on the
rubric that the grader sees?
Um
I'm curious like do you have a do you
have thought Bradley on our engineering
team? Hi Bradley.
>> [laughter]
>> Um do you have any thoughts on that
Bradley that I mean I don't know if you
learned anything unique as part of that.
>> Sorry, could you repeat the question
again?
>> Uh the question was
um
the question was if I understood it
correctly like uh
the the grader exact how do are there
any unique ways in which you've been
using that? Is that correct?
>> Yeah, how was your experience writing a
a rubric for the outcomes grader uh and
having it iterate on problems?

[00:21]
>> I I think we want to approach it like we
approach any other prompt. So it I think
in the end uh all the text that you
provide to the model is a different form
of prompt and you want to have different
evaluations for the outcomes for
different things that we're trying to
achieve. So, if you're able to
instrument that just like anything else,
you're able to iterate quickly and make
confident decisions.
>> Great.
Any more questions?
Right.
There's one over here.
>> Thank you.
Um thanks for the talk today. I was
curious how you're thinking of skill
maintenance over time.
>> Uh how are we thinking about scaling
teams or
>> Skill maintenance. So, skill maintenance
for mock-down files.
>> Yeah, so uh again like we're a product
for like knowledge workers. We want to
make it as simple and straightforward
for our customers to deploy and use this

[00:22]
as possible. And so, the way in which
I'm thinking about it from a product
strategy perspective is Asana will
decide what skills get baked into the
uh the finished like generally available
product and we're adding more
and we're designing those based off like
working backwards from our ideal
customer profiles and the the advances
we're seeing in the in the underlying
sort of model provider.
Um and that allows us to be very like
prescriptive about okay, here are the
additional capabilities that will be
available in a GA way, like a generally
available way, that to the end user,
like if you're in IT or operations,
you're thinking about the job to be done
for the teammate. Like I'm trying to go
ahead and produce perhaps like a Figma
design output or something of that sort.
And so, it'll be marketed and messaged
in that way and it's a shrink-wrapped
product. So,
again like over time we might open it up
so that customers can design their own
skills and like highly customize their
AI teammates, but the the
sort of primary go-to-market motion and

[00:23]
the primary sort of use cases, we
pre-design these AI teammates and the
value from a skills perspective. So,
they're like shrink-wrapped.
And then that way we get we get to
control on the R&D side the quality
level, which ones get released,
how that what the life cycle is, and so
on and so forth.
>> Thank you.
>> Yeah.
Great.
We have one more, okay. So, maybe this
is the last one because I see the
counter clock is showing about a minute.
>> So,
I'm also also building my my product
with the CMA as well. And one of the
problem I'm facing is
integrating with the third-party tools.
Like customer always want to integrate
to some other things beside beyond our
platform. How do you manage that? Like
you integrate that with the Asana level
or at the agent level or how do you
manage the third-party integration?

[00:24]
>> Third-party integrations for the grader.
Um Bradley, what's what's been our
experience so far? Like we've we've got
a few of those built out, so I'm kind of
curious, yeah.
>> Yeah, in terms of third-party
integrations and managed agents, we
integrate them at actually both levels.
So, we integrate them directly with our
own AI teammates agent loop, and we also
integrate them at the MCP level with
managed agents. So, we want to make sure
that the managed agents when we're using
them have the you know, all of the
context that they need
and that we're also supplying context
when we're not using managed agents.
>> Awesome. Well, thanks everybody for
joining us. We're at the end of our time
today. And yeah, if you have a chance,
give AI teammates a try.
Thank you.
