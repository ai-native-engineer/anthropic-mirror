---
title: "Giving coding agents their own computers: How Cursor built cloud agents"
channel: claude
url: https://www.youtube.com/watch?v=BbYSGxtsMic
youtube_id: BbYSGxtsMic
published: 2026-05-08
duration: "14:35"
---

# Giving coding agents their own computers: How Cursor built cloud agents

[![Giving coding agents their own computers: How Cursor built cloud agents](https://img.youtube.com/vi/BbYSGxtsMic/hqdefault.jpg)](https://www.youtube.com/watch?v=BbYSGxtsMic)

<details>
<summary>자막: Giving coding agents their own computers: How Cursor built cloud agents (14:35)</summary>

[00:00]
Hello.
Um, okay. So,
uh
models are getting really good.
And for more and more work, the
bottleneck is no longer the model
intelligence.
The bottleneck is humans giving the
models the tools and the contacts and
the increasingly ambitious uh tasks and
objectives to go flex their potential.
So, um at Cursor, we've been working on
removing that bottleneck and I'm going
to share a bit about how we've been
doing that um and hopefully it's helpful
to some of you in in your work.
Uh with models this good, we kind of see
the job that we have as setting our
agents free um safely uh uh and and
having them go off and work on bigger
bigger tasks. So, we've kind of gone
through three stages of uh the process.
The first was um giving our agents the

[00:01]
tools and the context to be more
autonomous. The second is um we had to
learn how to take advantage of these
more capable models. There's actually a
lot of work in figuring out how to
update your your sort of patterns uh and
behaviors.
And as you do that, as you're leveraging
more more agents and uh getting more
work done, you start to see the places
where uh there's stress and strains and
where the agents fall over and you work
to to uh improve that and that brings
you to the third stage which is building
the system that builds the system. So,
instead of spending your day uh
hand-holding agents from task A to D,
you take that time to uh build the
system that can solve for A to Z.
So, we started thinking about how to
make our agents more capable, how to
make them work more like we do.
Uh we started with
uh looking at what we do with humans to
onboard people to to uh Cursor. So, when
a developer joins Cursor,
they get a computer.
They are uh we help them set up their

[00:02]
dev environment. We have a ton of
documentation, maybe too much, about how
to do all the different things that uh
developers need to do in their daily
work. Um so, we give them all this all
this context and all this material. And
and uh crucially their computer.
If you imagine if we thought
think about what the the we were doing
with the the models, we were kind of
just like throwing the onboarding
process was you throw them into a code
base and from the model's perspective,
you have that thousands of lines of code
whizzing by, you don't know like what
you're doing, you just have some task
you have to go solve, uh and it's kind
of incredible that this works as well as
it does. Um I know if like I had to work
this way and I was just site reading
code and I couldn't test the
application, um I would also probably
frustrate and annoy uh the humans who
did have to do the testing for me.
So, um
we decided to build an onboarding agent.
And we built a a Claude onboarding
agent. Anybody can go to um
uh cursor.com/onboard.
You can put set up your repo and the

[00:03]
Claude onboarding agent gets to work and
it starts exploring your code base not
to make a change but to figure out how
to run it.
And this is a little bit about how it
goes. So, it's exploring, it's looking
around,
um and depending on how fast this one's
playing, you'll see it can start uh
using the app and it'll come back with a
demo. And it's not just looking to
figure out like what to run, what the
services are, um but there are sort of
these complex things it needs to do like
figure out their different environment
variables, what permissions does it
need. Um so, it's this interactive
process with with the uh developer to
make sure the services are are running
properly.
So, once we have the agents onboarded,
we realize there's still quite a bit of
work to do because you have all these
developers uh running many Claude agents
every day. So, any problems are
multiplied out across all those those
runs. And so, every time the agents run,
they have to start their dev environment
from scratch. When you're doing local
dev, you probably leave things running.
Um not true for the cloud cloud agents.
So, we wanted to optimize their dev X.
They were spending a lot of time

[00:04]
sleeping, uh waiting for things to start
up. They didn't uh have good ways of
waiting for things, so we built an an
any dev CLI tool. Um so, they were able
to start services, wait for the services
to start, check on statuses. They had
sort of a Swiss Army knife for things
like uh creating test accounts and
signing in for services, third-party
services, things like that. So, what we
saw was uh as we made the dev
environments better, more developers
started running more cloud agents and
getting more out of it. So, there's sort
of a positive feedback loop that starts
to take place.
Um and then of course, we also had to
give them uh all the sort of
documentation that we give our our human
developers. So, we made sort of
simplified versions of this so they
could get uh when they find themselves
in sort of these edge cases or hard
problems, they have the materials there
to to lean on.
So, uh in doing this process, we sort of
derived these kind of basic principles
of autonomy. Um the first is you have to
give your agents eyes. So, everything
that you can see, the agents need to be
able to see, too.
Uh basic version of this is if, you

[00:05]
know, the agent's running an app, you
should be able to see that app. If you
go and make changes and you use that app
yourself and change something in the
state, the agent needs to be able to see
what you changed. Another sort of
interesting one is uh that we found is
the the agent chats where you wind up
needing to debug what happened in a
chat, and you want the agent to be able
to see the same uh the other agent's
chat uh just like you do.
Uh the next thing is giving the agents
uh tools so that they can do all the
things that you can do with sort of
reasonable security constraints. Um this
is like, you know, basic basic one,
really important one is they should be
able to run the applications that you
can run, and they should be able to use
the services that you should you can
run.
Um
agents are auto regressive, so it is
also very important that you have a sort
of high-quality codebase and and
instructions and everything else so that
uh you get high quality and high quality
out.
The foundational primitive we believe
for human autonomy is computer use.
Um
So the first domain where agents have
really excelled has been coding and we

[00:06]
think computer use is is the next really
important domain.
Um and this is raw pixels in, mouse and
keyboard out.
Um and the Claude family of models are
really good at this. And this is this is
not the hard part of this is not
clicking in the right place. The hard
part is uh
sort of better explained is like if
coding is like chess where you can see
all the pieces out on the board,
navigating these GUIs is more like a
video game where you can only see a
little slice at a time. There are
one-way doors. There are game over
states that you can get into.
Um and so you need this sort of
higher-level metacognition and
backtracking and the sort of general
general intelligence uh uh
skills that the Claude family's really
good at. So uh
uh Claude's Claude 47 is our computer
use model. Here's an example. It was
told to go off and build this private
marketplace feature.
Um
So it goes off and records this demo
where it's implemented all the little
pieces. We have like
uh this
URL input and there's CSVs it needs to
add. Um

[00:07]
And what's great is that it's not just
using that to do its own end-to-end
testing to make sure that the changes
that it made works. You as the developer
get to uh have a really high bandwidth
method of reviewing the work of the
agent before you get into code. And this
becomes really really valuable when you
are running many of these agents um
simultaneously in the cloud and bouncing
between them. So that's the next thing
is once you have these autonomous agents
onboarded, you need to learn
to give them more work and give them
bigger bigger challenges to go tackle.
Um two sort of basic modes. The first is
uh you have like a lot of tasks and a
lot of bugs and issues and you kind of
have to learn when to just uh
like stop putting those in your notes or
start stop putting them in your two
tracker and just kick off prompts. Put
them right into a prompt box and kick
them off. And when you do
uh you then have a bunch more of these
agents running and again it's great to
be able to have those demos that come
back instead of having to review lots
and lots of code.
Um and the sort of second pattern is
much bigger projects um where you can
give a cloud agent autonomous agent much

[00:08]
larger units of work and have it work
for much longer.
Um one of the things we were surprised
by we kind of knew that if we made the
agents more powerful developers would do
more exciting things. Um and we were
sort of surprised by the extent to which
this was true. And um one of the sort of
really important things was the security
that the cloud provided for for
developers. Um there's sort of this idea
of like security through freedom which
sounds like Orwellian propaganda but uh
in the same way that you're sort of
setting your agents free to go take
things on in the cloud um on their own
you also sort of set yourself free as a
developer where you don't have to worry
as much about uh you know resource
management and context switching. Um you
don't have to worry about the agents
going and doing things that they really
should not with your environment
variables.
Um
and there's there's a way in which we
were all surprised by how much more
enjoyable this made programming.
Um

[00:09]
really really important skill that we we
are still working on learning
um when the agents fail
is really worth it to take time out to
figure out what went wrong, debug it
and implement a fix that's again going
to be sort of multiplied out across your
whole team and your company. Um it's the
same sort of dynamic where so failure
modes if they persist make the agents
sort of continually uh
uh compounding failure across the entire
company. Um and people don't want to use
the the agents as much and they don't
lean on them as much. But the inverse is
also true when you invest in them
uh and you you make them work better
everybody wants to use them more. People
are building trust with the agents.
They're finding that they can sort of
one-shot bigger and bigger tasks, and
then they want to invest more in it. So,
this is a really important change in how
you think about your work, where you're
kind of programming programming the
system.
And so, you've onboarded your agents. We
gave them the tools to make them really
powerful.
Uh we started learning how to leverage
them and scale them up, and we were

[00:10]
seeing where they they fell over. We
started working on this sort of loop of
how you teach them to work better.
And we realized that it does start to
feel like coding again.
Um so, of course, we thought, well, the
agents should do this.
Um we've got a few ways that we're
trying to have the agents do this. This
is uh sort of the most important one and
the one I'm going to talk about today
um is agents iteratively improving their
own workflows.
And so, we call this the agent
experience. There's the developer
experience. So, you have the agent
experience, and you need to care just as
much if not more about the agent
experience.
Um the way that our system works is
agents uh go about their business, and
they are told to report issues as they
come up. Um it's really just like what
we do with uh the pattern I was
describing for humans, where if you see
something wrong, say something, uh
report it, and and try to work on a fix.
All those reports are accumulated in a
system of record. It's really again very
uh
similar to how human human systems work.
Um managers will go in and review all
the issues and categorize them and

[00:11]
dedupe them um and bucket them into
their issues that can be sort of their
technical problems that can be
addressed. Then there are issues of um
permission, where the agents just don't
have access to something. Uh so, they
need to get permission. There are issues
of ignorance, where the agents need uh
they don't still know what to do, and
they need the humans to come in and tell
them what the right right right way to
solve the problem is.
Um so, then in the last step, of course,
these are then fixed by both agents and
humans, and the goal is to over time
have a less and less human involvement,
so we can have those issues that the
agent solve are solved end-to-end. We
don't really need to review. We can have
really high trust in their work.
Um and they have all the context that
they need, and they don't need uh
anything else from us.
So, I'm going to go through a couple
examples. So, this is our most important
skill. It's the WCF skill,
which of course stands for work on the
factory.
And you can see it's like uh
every every cloud agent gets this skill.
Um
and it's almost the exact same prompt
that I was just showing in the previous
slide. Work on the factory is the idea

[00:12]
that when something is annoying, broken,
or confusing, you take a moment to
report it, so we can improve the tools
and workflows rather than just grinding
through.
Um
models a while ago would not have been
doing a very good job of this, but today
uh
they get annoyed, and they find things
broken, and they get confused, and they
like realize that, and they report it.
Um so, we get this this uh system of
record where they go and report all
these issues.
Um of course, you then have to solve the
issues, and this is its own uh really
important challenge if you want this
whole system to be sort of uh
self-improving.
And so, we were finding with these these
agent development experience problems,
having the agent just go solve them and
and try to one-shot was not that
effective because there's a lot of flake
in those problems.
So, something only happens once in a
while.
And so, we taught it to actually have
the cloud agent that goes and solves it
kick off a bunch more cloud agents with
the change in the development
experience, and make sure that across
that sort of eval set that there's a
robust solution. And so, then when the
problem when the solution and uh the PR

[00:13]
comes back to the human's review,
there's a high degree of trust that
actually this uh is is well validated
well validated well validated solution.
Um
This is slightly premature.
Um
Yeah, so I think that these are both
really good examples of where there's
how these sort of skills can work as um
uh sort of background uh a garbage
collection processes or cleanup
processes in the operating system. Uh
And we think that these while these are
sort of clearly applied for the the
coding domain,
in the same way we sort of speed run a
lot of AI development in coding, these
patterns are going to generalize
well outside of coding and to other
domains. And even if you think about it
already, cloud development experience is
not really a coding problem. There are a
lot of variables in that and very few of
them really are are just sort of coding
issues.
Okay, so now now the thank you slide.
If you'd like to talk more about
self-improving identity systems,
please talk to me. You can find me on X

[00:14]
at my name.
And if you'd like to set your agents
free, you can go to cursor.com/onboard
and have Claude onboard to your codebase
and maybe ship your next ambitious
feature.
So, thank you very much.

</details>
