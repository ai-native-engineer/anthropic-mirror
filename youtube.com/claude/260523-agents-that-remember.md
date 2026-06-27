---
title: "Agents that remember"
channel: claude
url: https://www.youtube.com/watch?v=geUv4CjPpxI
youtube_id: geUv4CjPpxI
published: 2026-05-23
duration: "28:42"
captions: en-orig
---

# Agents that remember

[![Agents that remember](https://img.youtube.com/vi/geUv4CjPpxI/hqdefault.jpg)](https://www.youtube.com/watch?v=geUv4CjPpxI)

<details>
<summary>자막: Agents that remember (28:42)</summary>

[00:00]
Hello everyone. Thank you all for
joining us today.
Um my name is Kevin.
Uh I'm an engineer here at Anthropic and
today we'll be learning about how to
build agents that remember. Um so
today we're going to talk a little bit
about the base case with agents today,
uh which is that they're isolated and
this kind of limits their usefulness in
a lot of real-world workflows.
Uh we'll look at how we can actually
solve this problem uh with our new agent
memory stores feature that we've
launched. Uh this will give agents
access to a live memory store that they
can read and write to over multiple
sessions.
And then we'll look at how we can
improve these memory stores over time uh
using a new feature that we call

[00:01]
dreaming.
Uh and then finally we'll get to see how
all of this ties together with both our
CLI and also our awesome console
interface.
Um so in the previous uh workshops, I
think we've learned a little bit about
how Cloud Managed Agents has these
concepts called an agent, environment,
and a session.
Uh in this workshop, we're going to add
two additional concepts here. The first
one here is a memory store. Uh so a
memory store is a persistent file
system-like store that gives uh that it
attaches as a resource to sessions that
you create and it gives agents access to
uh it gives agents the ability to read
and write information across sessions.
A dream uh is what is a asynchronous job
that runs in the background. Uh it looks
over an input memory store and a bunch
of your previous sessions that are
represented as transcripts and then we
run a harness over them to distill new
information that maybe the original
agents missed. We do things like

[00:02]
fact-checking.
Uh we also organize and consolidate and
deduplicate information so that your
memory stores don't grow unbounded over
time.
So, uh also in case anyone in this room
has not already uh downloaded the
workshop repository you'll need for
this, uh here is the URL.
I'll give a few seconds for folks to
just grab that. Okay.
Um so, let's kind of like talk a little
bit about the problem today. So, when
you when you create agents on Cloud AI
today, and sessions,
um most of the time you're creating one
session at a time and these are
isolated, right? The agent doesn't
remember information from the past and
it doesn't transfer information to
future sessions. Um so, I want to kind
of like take us through this this base
case today.
Uh so, if I switch over to my computer,
um I'm in our workshop repository here.
Uh hopefully everyone can see this uh in
the back, but I've just run the
bootstrap script that we've uh included
in the repository.
Uh and what this has done is basically

[00:03]
created uh some seed information for us.
So, we have an agent,
uh we have an environment, we have a few
like previous sessions that talk about
things like the keynotes uh from day one
as well as you know, uh a previous
workshop.
And so, uh what I'm going to do from
here
is actually go ahead and start walking
through this guide with you guys. Feel
free to follow along on your computers.
Uh I'll be using the CLI and then also
showing kind of the console interface uh
for each of these steps.
So, first we're going to create uh a
session that basically tells it some
some new information. Uh
So, I'm going to copy this command here.
And as you can see, we are creating a
session with the agents that we've
created before
uh with the environment ID.
Uh and we've given it a title here of
just like write test with no memory.
Great. Uh so, now that we created this
session, uh I'm going to quickly switch
over to my console here.
Um and you'll see that
uh let me just move this over. You'll

[00:04]
see that the session shows up in
console. Uh it doesn't it has a status
of idle, nothing running yet.
Uh so then we're going to switch back
and then I'm going to send
this session some new information.
Uh so once I copy this,
and what I'm doing here is sending a
first user message here with information
about the CMA talk yesterday, uh
naming a few keywords like multi-agent
orchestration, multi-agent orchestration
outcomes, and memory. And I've also just
given it this URL, you know, example
that I took notes and uploaded them
here.
So if I switch back over to my console,
uh we should see this event pop up.
And what we sort of expect the the agent
or the model will do here is it'll just
respond say like, "Great. Thanks for the
information.
Not sure what else you want me to do
here."
Uh so we'll give it a sec
and maybe folks to catch up.

[00:05]
Let's see if we get a little refresh.
Ah, sorry.
Yeah, so it looks like the model
responded here. Uh let's collapse this.
Yeah, it's basically saying, "Okay,
great. Thanks for telling me this
information."
Uh so then if we go
Sorry?
Uh this is using, I believe, Sonnet, the
agent that was created at the beginning.
Yeah.
Um
Cool. So if I go back here uh
to my workshop here, we're going to
create basically a second section that's
kind of the retest. So I'll go through
these steps a little bit faster.
Uh and then again, I'll send it a
message here that's this time I'm going
to ask it for information about the
stuff that I just told it.
And if I go back to our console here and
check out the other session that should
have been created,
we would expect the agent to basically
um say something like, "Yeah, I don't

[00:06]
really have access information. I can
help you in these various ways." Great.
So, that's effectively the base case
today. Uh so, if I go back to the slides
real quick, this is a quick recap of
what we did. We told it something, asked
another session about it later, no
information is transferred between the
sessions.
So, how do we solve this problem, right?
Um
just like in humans, uh we've introduced
the sort of concept of memory. And
again, a memory store here in the Cloud
Managed Agents platform is a file
system-like store. Uh under the hood,
you can or you can create as many memory
stores as you like here, so you don't
have to necessarily restrict a memory
store to one organization. You can
create it per user, per workspace, etc.
It's up to you to kind of define what
the boundaries of the memory store are.
Uh and then under the hood, this memory
store gets attached as a file system to
the the session container, and the model
has tools to read and write to it. Uh
the actual interesting thing here is
that we've actually
mounted it as a file system because it's
such a powerful interface for the model.

[00:07]
Uh you can use things like bash to like
uh like explore the file system. It can
use grep to kind of search for keywords.
Uh it can also read files and do a bunch
of like really powerful things um that
make it much more useful for the agent.
Um so, I'll switch back to my computer
here and we'll walk through kind of how
to create a a memory store.
Um so, first things first is actually
creating it. So, I'm going to copy this
uh command here. Feel free again to
follow along on your computers.
Um and the kind of parameters that you
need here are mainly just like a name.
Uh so, I'm calling mine CWC memory. You
can give it a quick description. Uh and
then I'll show you also in console later
that there are two additional parameters
that you can set here, but let me just
follow through with the simple example.
Uh once I create this memory store, you
can actually see it in console
under manage agents, memory stores.
And you'll see that it's active. Uh you

[00:08]
can actually click into it and view uh
essentially a file system viewer of
what's currently in it. Of course,
there's nothing in it right now.
Additionally, uh we offer functionality
uh we offer the ability for you to like
add manually add memories, so you can
create like a file under a specific
path, add some content, etc.
If I go back just a brief second and
talk about uh creating a new memory
store, there's actually two sort of
additional parameters that you can uh
set on the memory store
uh when we actually mount it. So, if I
go back to the repository here,
um the next step once you create a
memory store is to actually use it with
your sessions.
So, I'm going to again copy a few of
these commands. So, the first one here
is basically just
giving us the shape that we need to pass
the sessions API requests.
I'll paste it in our terminal here so we
can see it better.
Um so again, the memory store here, you
just pass in a memory store ID.

[00:09]
Uh and you can also give it a prompt
around uh that will steer the agent to
read and write specific information. So,
you might want it to focus on maybe like
a specific um link or a specific like
area of focus on. Let's say you're
baking making like a investment agent,
right? Uh you want to focus on specific
things to remember for the future.
Uh so, you can do that with the prompt
parameter.
Uh additionally, there is an access
field uh that defaults to read or write.
Um you can change that to read only,
which will make it so that the session
and the agent only be able to read from
that memory store, cannot update it.
So, once I run this,
um you'll see I have created a new
session in console.
Uh and this time it'll have a memory
store attached.
And then if I send it events here, this
time we'll just basically repeat the
test that we did just before. So, let me
grab this.

[00:10]
Again, same text as before, we're
telling it new information.
Uh and hopefully we'll be able to
observe a different behavior this time.
Yeah, so clicking into uh if you click
into the session details, you'll see the
the information that I just gave it.
And now the model is like first looking
at memory to see, okay, was there
anything that like I need to remember
for this conversation?
Uh and now it's going to actually like
Of course, there's nothing in our memory
store. So, now what it's going to do is
actually save the content that I told it
to that memory store directly.
And it saved it under this like
sessions.md file.
And it's great telling me that uh what
it did.
Um so, then if I go back and do that
same test that we did before, this time
I'll just copy both.
Uh sorry, just

[00:11]
Again, or this time we're going to
create a new session with the same
memory store that we were just using.
Uh and we will send it
an event here
asking at what are the things that it
found uh or learned from the CMA talk.
Once again, going back to our console
UI, we can see the recall test running.
And as we would expect, the model is now
first looking at its memory store to see
if there's any information.
And again, it's now using grep to find
uh any sort of keywords here. It's
looking for CMA.
And great, it found like a lot of
information that we just told it from
the from our previous session.
And it now it's able to answer my
question, right? Um and this is like of
course a very simple example, but this
illustrates kind of the power of of
memory and this is like something that
was kind of difficult to do before,
right?

[00:12]
I'll give quick pause in case anyone's
straggling.
Um okay, great. So, what what else kind
of can you can you do with the memory
store here? Well, we actually offer uh
additional sort of endpoints that allow
you to manually inspect the store
itself. Uh so, I'll use the CLI here,
but for instance, you can list all of
the memory files that are in the memory
store.
We can like
do that.
Um there's also each um memory a memory
store's a memory files in a memory store
are also versioned. Uh so, anytime you
make a change to a file, etc., there's a
new version that's created, and we offer
a set of endpoints for that.
And then I can also kind of take you
through the memory store UI.
So, each memory store you create again
is here, and if we go back to our like
kind of file system view, you can
actually see the files that it created.

[00:13]
Uh there will be like a directory
structure here if Claude is creating
kind of subdirectories to organize
memory files.
You can actually edit these memory files
directly if you wanted to. So, for
instance, if Claude wrote something um
that was incorrect, or maybe you just
wanted to add more information, you can
do that. And again, as we saw before,
you can add additional memories to a
memory store.
Uh okay, so
I'm going to go back to the slides real
quick.
And as we just talked about, uh, this is
how you create a memory store and then
mount it on a session that you want to
use it on. Again, it's up to you to kind
of decide which of your sessions will
use memory, which ones will not.
Uh, we also saw how you can like list
memories and see what's currently in a
memory store.
And let's move on to talk a little bit
about dreaming now. Um, so
when you have agents that are reading

[00:14]
and writing to this memory store over
time, uh, we've noticed that often times
they can start just kind of dumping
information to that memory store. So,
it'll start writing maybe every every
task you ask it to do it'll maybe record
its information, right? And over time
your memory store is going to grow,
right? And there's no real process, uh,
before that would allow you to sort of
organize that memory, maybe check to see
if anything was stale, and and
consolidate any duplicates, right? And
so, this is where the dreaming comes in.
Uh, dreaming is a is a batch process
that runs again asynchronously. You
launch it, uh, using uh, our API or
through console, and it'll run a a new
dreaming harness that we built that is a
multi-agent setup. It will look over
each of the input sessions that you've
given it. So, you specify like an input
memory store that you want it to dream
over along with like a group of
transcripts that you think might help or
enrich that memory store. It'll look
through each one, do again fact
checking, enriching with additional
details, maybe dates, specific
identifiers, uh, and then it will also

[00:15]
organize those memory files and see if
there's any duplicates, anything that it
can help uh, fix so that when you and
it'll produce an output memory store
such that in the future, when you attach
that output to additional sessions, it
will hopefully increase efficiency, uh,
efficiency of like information
retrieval, and also hopefully increase
the intelligence of the agent.
So, let's take a look at how this works.
I'll again switch back to my computer
and we'll walk through it together.
Uh so, what you to to get get started
with dreaming, basically, you'll need to
actually create the dream job.
And I'll I'll go through a little bit of
the parameters here. So, the model uh
here that we're choosing is Claude Opus
47. You can choose between or Sonnet 46
depending on kind of the level of
quality you want as well as maybe like
token costs.
Uh it takes in two inputs. So, you'll
need the memory store that you want it

[00:16]
to dream over as well as a list of
session IDs. Uh so, this is up to you to
decide. You can
you know, maybe dream over daily and
dream over maybe like 10 sessions at a
time or 20, right? It could go, you
know, all the way up to like 100. We're
also looking to scale it further uh
beyond that.
I Optionally, you can also provide the
dream job some additional instructions
that you might add. So, we provide it
with a default prompt that does a bunch
of things. If you wanted dreaming to,
for instance, specifically fix a few
things, like maybe you're working in a
domain that requires like very specific
details, right? You might ask a dream
job to really focus on, "Hey, make sure
you backfill these details so I remember
for the future, right?" You can also get
it to You can also steer it to maybe
like organize files a bit more, like I
want the specific structure in my memory
store, please do that.
Uh so, let's actually go and run this
command here.
Great. We'll get We'll get back a dream
ID.
And then, once again, I'll go back to
our console here.
And so, dreams are under, again, manage
agents, dreams.

[00:17]
And once I create the dream job, it'll
start pen- it'll start with pending, but
it'll start running pretty shortly
after.
And you can actually see the status of
the job both in console and through the
API. I'll show both. But in console
here, you'll see the input memory store
as well as a token count.
And generally, like uh dream job can
take, you know, depending on the size or
the number of transcripts that you give
it, it could take anywhere from, you
know, a couple minutes to hours at a
time.
And that's really the benefit of doing
it asynchronously, right? Like this is
not something that you want to do live
while your agents are working.
And we'll just give it a a minute here
to to run. As you guys can see,
as it's running, as agents or as the
harness itself is running, we're
updating the token count for you, so you
can track its progress over time.
The other really cool thing here is that
Dreamings actually built directly on top
of Cloud Managed Agents primitives.
So you can actually see that we are
creating a session for the dream job
itself. And you can actually click into
it to see exactly what the dream is
doing. This offers a really nice amount
of like observability as you can like
diagnose issues potentially.

[00:18]
And so you can see the prompt that we
give it. There's a lot of details here
that I'll kind of that you can explore
on your own time. But the under the
hood, the the Dreaming harness itself is
launching sub agents to look over all of
the transcripts that you've given it.
And each sub agent essentially has a
system prompt that tells it what to do,
look over it. And the orchestrator is
responsible for just like making sure
all the agents are running and kicking
them off as they go.
So we'll give it another minute for to
let this run.
Another thing to call out here is that
while

[00:19]
we don't actually touch the input memory
store at all that you create. So this is
a non-destructive process. What we
actually do is we will clone your input
memory store into what's called an
output memory store. And the dream job
will be writing basically to a new
memory store such that any edits that
are made are non-destructive and then
we'll see down the line how you can
utilize this output memory store in your
future sessions.
Generally this takes about a minute or
so depending on
how fast the job runs.
Uh one other thing is that you'll see
that I'm sort of checking on the job
periodically as it's running in console.
When you do this programmatically we
offer an API that allows you to just
essentially query
for the dream job and it'll have a
status so you can pull for the status.

[00:20]
Great. So looks like it just completed
and the cool thing here is that in
console we actually show you a diff of
what it did. So you can see dreaming
here
it created an index file. This index
file has sort of these slugs that
reference the various like memory files
that
a future agent might need. And the main
goal of this is really just that future
agents it's a lot more efficient to kind
of look at an index file and it quickly
grok like what it needs to go look for
instead of maybe doing a a wider grep.
Additionally it's actually adding like
additional information that was not
present in the in the first couple of
sessions that I created. So it's
creating this event logistics file that
gives the whole schedule of Code with
Claud.
Um a bunch of names as well.
Uh and again schedule for day two.
Uh and you also see that it actually
kind of reformatted the memory file that
I created in a previous session. So this
time it is adding again a slug, a
description of the event, some
additional metadata.

[00:21]
And again adding more details. And
generally we find that like
more information actually really does
help future sessions. And if you think
about it intuitively, um while an
agent's working on a task currently,
it's kind of hard to predict down the
line what it might need, right? That's
just generally a harder prediction
problem. So, it's actually good to kind
of write additional details down that a
future agent might remember. And
Dreaming can always like go back and
like remove stuff that is no longer
needed.
Uh and if I go to the output memory
store here,
I'll just click on it.
Um
again, you can see all the files that I
created. It's another good way to sort
of see what's going uh what Dream
Dreaming did. Uh and if you wanted like
a human-in-the-loop kind of review
process, this is kind of where uh this
is super helpful. Uh human can kind of
go in and see if the
Dreaming harness made any mistakes.
Okay, great. Um just going to switch
back to the slides real quick cuz I want
to show a diagram.

[00:22]
Um
yeah. So, again, under the hood, this is
sort of what how Dreaming works, right?
This is a multi-agent harness.
Uh we have an orchestrator that is
mainly responsible for spinning up
sub-agents. And again, we spawn one
sub-agent per input session that you
give it.
Um and kind of the the reasons behind
this are we actually kind of want
Dreaming to be exhaustive by design. Uh
if you give it 100 chances, you want to
make sure like Claude is looking over
all the information to make sure it's
not missing anything, right? Um
great. So, let me let me switch back to
my computer again.
Uh and this time I'm going to actually
like walk through how we might use this
in a future session.
So,
uh once the dream uh is done, you can
actually go and grab the output memory
store using this. So, again, we're we're
just retrieving the dream resource uh
with the dream ID that we created and
then
uh querying or just grabbing the the
JSON memory store ID.

[00:23]
Great. So, this is the memory store.
And again, you can
look through what memories it created.
Uh and then now we'll do this sort of
test again that we did before with the
two sessions. So, I will create a new
session here.
And you'll notice that this is now using
the output memory store from dreaming.
Once again, we'll send it an event here.
We're just asking it
what sessions I attended, what resources
do I have links for, and what follow-ups
did I flag.
Once again, going back to the console,
it's really a great way to, you know,
visualize what's going on here.

[00:24]
And you'll see that this time when it's
reading from memory, you'll see all the
stuff that dreaming did, right? So, the
index, the event logistics.
And it's now reading kind of it's
starting to read the index first.
Okay, great. Now it knows I'm going to
go straight to the sessions file.
It's being a little exhaustive here,
just checking for, you know, event
logistics.
Okay, great. Let's see what it came up
with. So, as you can see, I
I'd have to go back and show you the the
previous session, but this time I think
there's a lot actually a lot more
information here. So, it gave me a recap
of all the sessions I I attended. Uh
it's giving me timestamps now about like
all the sessions that were that were
planned for day two, as well as like the

[00:25]
resource links, right? I think this kind
of showcases again like how dreaming can
really enrich information that is
transferred between sessions.
And then optionally at the end, you
know, if you're really happy with the
output memory store here, you can go
ahead and actually retire the old memory
store.
So this won't affect like your previous
sessions. It just means that you know it
will keep you the number of memory
stores in your organization down to a
reasonable level.
Great. So I'm going to kind of switch
back to the slides here.
And talk a little bit how you can kind
of view sessions, memory stores and
dreaming as three composable layers
here, right? If you think of a session
as a as an isolated instance of an agent
running,
it's one usually typically one
conversation thread, typically
ephemeral, right? A memory store
augments that. So now you can connect
information between your sessions across

[00:26]
multiple sessions, right?
And then finally with dreaming, you're
now organizing, enriching, and improving
your memory stores over time, so that as
you scale up the number of sessions you
have, and as you scale up the
information that is being processed
through those sessions, your memory
stays at a reasonable level. It's
manageable. It doesn't blow up. Also, it
checks for things like staleness to make
sure all the information is most is
up-to-date. Okay?
I wanted to highlight some of the maybe
good questions that I got from the
audience here. So one of them was around
generally like sort of what is the like
token usage of this feature like? So as
I said before, like I think by design we
actually do want it to be exhaustive, so
we do expect it to use a lot of tokens.
The the nice thing here is that because
most of the processing is agentic, most
of the tokens are actually cached. So
we're expecting like about a 95% cache
rate cash hit rate on um um
like most dream sessions, right? And
additionally, we are exploring like
other ways of offering this at lower

[00:27]
costs to you. So, uh example of this
would be like similar to our batch API,
we could offer things at a 50% discount
by scheduling at a different times. Uh
other additional like token usage
controls include like switching the
model, steering the prompt a little bit
more, also providing more like just
general budgeting of tokens.
Um
Great. Um so, I think we're just about
winding down. So, I'm going to quickly
kind of go over again for the folks
remaining in the room uh like what we
went over today.
Uh so, again, we talked about the
problem that most agents face today,
which is like how do you remember
information across sessions? I think
this is
a pretty like well-established kind of
problem now.
And we talked about how memory is kind
of the first step to addressing this,
right? You give agents access to
something where they can dump the
information, read from it, etc.
Uh but we also saw how this creates a
problem where memory stores are can grow

[00:28]
unbounded over time. They can grow
disorganized, information can grow
stale, etc. And then we saw how dreaming
can be used as a way to mitigate this
problem, right? So, we we take another
set of agents that their entire job is
to improve that memory store for future
use.
Um and with that, I'd like to thank
everyone for for coming to this
workshop. Um hopefully, it was helpful.
And hopefully, by the end you'll learn
how to uh or you'll you'll know how to
like integrate maybe memory into your
own use cases.

</details>
