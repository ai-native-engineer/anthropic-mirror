---
title: "Live coding session with Boris Cherny and Jarred Sumner"
url: https://youtu.be/DlTCu_pNDHE
channel: "Claude"
date: 2026-05-06
duration: "32:00"
lang: en
youtube_id: DlTCu_pNDHE
processed_at: 2026-06-26T08:02:22Z
---

# Live coding session with Boris Cherny and Jarred Sumner

- 채널: [Claude](https://www.youtube.com/channel/UCV03SRZXJEz-hchIAogeJOg)
- 발행: 2026-05-06
- 길이: 32:00
- 영상: <https://youtu.be/DlTCu_pNDHE>

## 자막 (en)


[00:01]
Please welcome to the stage head of Claude
[music] Code of Anthropic, Boris Churnney,
and creator of fun at Anthropic, Jared Sumner.
[music]
Hello.
All right. So, this is a developer conference.
We're going to be doing a little bit of talking,
but mostly we're just be like coding. So,
this is for the developers in the room.
I'm going to start by talking
a little bit about how uh
how bun uses cloud code to to build and and
maintain bond and also kind of how our setup
uh works and because it's kind of a a slightly
more advanced setup than uh what's common today.
Um but first I'm going to get a few agents
running to just fix some GitHub issues. Uh

[00:02]
this is classic Jared doing work during a talk.
Um so so in buns repo uh every time somebody
submits an issue uh we have a cloud bot
automatically run and try to reproduce
the issue. So you can see this person has
uh this this side effects and this is
like one of the most recent issues. Um
and and we can see that Robun which is our our our
bot uh uh went and managed to reproduce the issue
uh and submitted a PR automatically. Um and
and this PR is like it has uh it all these
PRs always have tests. Um it's one of the actual
hard requirements before it can submit a PR. Um uh
and so so the challenge here is like does
this code look correct? Um and one of the
things we do to to check that is does the test
fail in the previous version of bond and pass

[00:03]
uh in the in this debug branch. And it the
bot actually can't submit a PR without that
uh being the case. And so this is just to make
sure you understand. So this is like every single
issue that goes up in the bun issue tracker, you
have Robo Bun automatically try to reproduce it
before anyone looks at it. Yeah. And this saves
a lot of time because we have so many open GitHub
issues. Um it it really moves the challenge from
is from just fixing and debugging the issue to
is this the right thing to merge? Like is
this the right fix? Um how how good is it?
Is it is this doing like a 100% of yours?
Is it like 10%. We can go to the insights
uh uh and go to contributors and then if we
go uh last three months uh uh and this is
specifically to main we can see that Robbun is now
a bigger contributor to Bun than I am [laughter]

[00:04]
and that's with merging not all of its
PRs for sure. You can see we have a lot
of PRs open right now. Um the the challenge
is really how do we know can we merge the PR?
Um, and that's the tests. Um, and then the other
thing that's really interesting about this is uh
uh we have automatic code review bots that
that run. Um, and then they're going back
and forth. So like Code Rabbit leaves a
comment and then Roboun leaves a comment
and then they go back and forth and
they and Code Rabbit did the [laughter]
I love this. And it also marks the
comments as resolved when it's done. Um,
and you you can see they actually went a lot like
there's a lot of back and forth here. There's like
30 comments or something. And so you're using
like a combination of agents. So this is like
code review. This is like quad code review and
then also code rabbit and like you're using
them together. Yeah. And I I think basically like
code rabbit is is good for like kind of stylistic

[00:05]
issues and things that are like make sure that
it follows the cloud MD and then the the cloud
code review is really good at here's this really
subtle edge case that would have taken me like 30
minutes of reading all the code and having all
the context to to like figure out and and so so
it's really good at surfacing bugs that you you
need the full context to really understand. Um,
and I think basically it's it's really hard to
to actually have all this automation without
having code review that is in the loop with the
with claude there replying or replying is like
very performative but like at like fixing um and
that's also a big part of like what used to take
so much time uh when like why PRs would take so
much time to merge is because you'd have to like
like check out the branch locally, fix a
lint error, then run the llinter locally,

[00:06]
then push it back up. And there's all this
switching cost that's constantly there.
And so when you So I think this is like an
especially good use case for for LLMs because
otherwise like it just takes up so much time to
to ship and and I guess like especially for the
bun codebase because it's like it's systems code.
It's, you know, it's very easy to repro issue and
then see if the issue is fixed because this is
kind of back to what we were talking about before
with like this kind of verification loop. It's
all systems code. So, it's really like a test case
on a particular architecture and you can
essentially like repro or verify anything.
Yeah, that's one of one thing that makes it easier
in buttons codebase is because it's a a CLI tool.
um because uh we don't need to run a browser
to test things, but you can also just like
have something set up to like take a screenshot
or record a video or those sorts of things.
Um in Bun's case, we don't need that, at
least not yet. Uh uh there's a couple things

[00:07]
we could do that for like we have some
front end stuff that would be nice. Um
but yeah, I think this is like the the direction
that I think is really interesting is because
it saves so much time. Um and this is not this is
something that like this is specifically for bun
but the more generalizable thing when because most
products are not open source um uh is like instead
of an issue maybe the starting point is like a
customer support ticket. So like you could you
could imagine automatically uh h passing customer
support tickets to a cloudbot to then go and try
to reproduce the issue and then submit a PR and
then uh having code review go back and forth. Um,
and that's where I think for a lot of companies
it becomes a lot more impactful because it just
saves so much developer time. We should think
of some kind of name for this pattern. It's
like adversarial code review or or something like
that. Yeah, I don't know. Um, but I do think like

[00:08]
there's also a few other things about this that's
uh like the if you just do this then it doesn't
quite work. the very first step you need is
to like make sure the development environment
is set up. Um like I I think this has been talked
about before but like uh like cloud MD is uh
very important um because otherwise it's going to
just submit PRs that don't quite make sense for
you to merge. Um so like we very much emphasize
in buns codebase that it runs this special command
to do the build. Um and this both builds and runs
the command. So it like forwards the arguments. Um
because that's also one confusing thing is like
uh because bun has to be compiled uh you want to
make sure that it's running the actual changes
and not like a debug build that's like stale. Um
we also go into a lot of detail about how to run
tests, how to write tests, um where to put the
test, um uh and a lot of like here's how here's
all the issues that we've run into previously.

[00:09]
Like basically the the pattern here is like every
time that you find yourself repeating something
it should probably go in cloud MD
because the the question now is like
how do you make it maintainable to have
lots of claws running all the time and uh
and to do that it needs to be written down. It
needs to be documented. Um so like a really small
detail is like we we check the we have it like to
make sure that claude sees the error message uh we
make it print the air message before uh the like
less informative uh conditions. So, so this is
sort of like you have quad write a test and then
the test is bad or something about it doesn't work
and then you see this kind of repeated like once
or twice and then you just tell Quad add it to the
quad MD so that every time in the future when you
write a test you do it correctly the first time.
Yeah. So this is like uh like compound
engineering. It's kind of this.

[00:10]
Um and then also it's helpful to like give
it an overview of where all the folders are
like what all like how the code is laid out.
Um, and like about dependencies. Um, uh, uh,
another thing I think is interesting is like
making sure that it can read your CI errors
and like build logs. like you want to you
want to set up the agent to be able to
be able to read the code
like to do the full loop of
make of like writing the code testing the code
works checking CI monitoring CI um and uh uh
reading all the errors so that way by the time
it gets to a person everything is like set up
like the ideal is that you read the code and you
you have very clear indications that you can be
high confidence to merge it And the only way for
that to be true is if it is set up for success.

[00:11]
It's interesting. I remember when we when we first
met, you were talking about like your vision of
like everyone being able to run hundreds of agents
in parallel and how that would work. And I feel
like I didn't really get it at the time. Although
now like every night I I'm I'm running like
hundreds of agents every single night. And I feel
like now I'm finally there. But this is a thing
that you've been thinking about for a long time.
So it feels like this is sort of like the setup
in order to be able to kind of scale up agents
way more like you need the self-verification so
that agents can run autonomously. Yeah. Like this
has gone through many iterations in buns codebase.
Um we previously just had a discord bot where I
could just at mention the bot and it would spin
up a container. Um uh it didn't have like the CI
stuff. It didn't have uh the code review stuff.
Um, and it's so much better now,
especially with like Opus 47. Um,
uh, uh, it's all this stuff is getting so
much better. Um, oh yeah, we can also check on

[00:12]
how, uh, how it's going. It looks like
it created a PR, the first one. Um, uh,
and it wrote tests. Um, so maybe while we
look at this, I'm curious for like just to
get a show of hands for people in the room, like
as people think about their development process,
raise your hand if it looks something like this
where you have like a bunch of terminal windows
or desktop tabs and you're kind of pasting in
issues. Okay, so that's like maybe half of people.
And then what if it looks like Roboun or
something more like that where it's like
closing the loop a little more? It's like the
next level of abstraction starting to get there.
Yeah, I think it's like it's not surprising
because I think model capabilities are just
getting there. Like I think 47 is the first model
where it's really felt like it's able to do this.
And in the past maybe you could do it with
like a bunch of scaffolding like you just
throw a bunch of tokens at it and it can kind
of work. But now it's like efficient enough.
You can actually do this dayto-day. Yeah.
Um let's see. So the first PR is there. Uh

[00:13]
let's see if it did any others.
Uh okay. It did two PRs. Um uh
this looks very plausible. It's cool. And
this like this before after is this like
do you tell it to do that or sometimes it does
it? Um uh it's it's pretty good about knowing
like when it should do that like when it's like
a string formatting thing. Mhm. Um uh it's also
it also kept like bun style of the label which is
good because node style is slightly different. Um
let's see does this change look good? Um
yeah. Uh mostly what I'm thinking right now is
uh it it's it did this. This is good because like
you don't want to write one bite
at a time. You want to write uh
in in chunks um and then it used uh
saturation uh to to but I don't like

[00:14]
that or like it shouldn't have to do that.
Does anyone here actually know Zigg sort of
I feel looking at this code and and you can see it
followed the patterns from the from the cloud MD
await using and then that that pattern of of
uh reading all the pro like resolving all the
promises at the same time and so like what's your
workflow like when you when you see something like
this are you usually going in and like commenting
or are you just going to wait for like code review
to come in and and drop a comment? Um, usually it
depends on that like how complicated it is. Um,
in this case, I'll usually I'll wait for like this
one is actually pretty simple. I feel pretty high
confidence that if the test pass then uh I would
probably merge this. Um but I still would wait for
uh the code review for for at least for
the cloud code review one to run um uh

[00:15]
just in case because what I really like
about that is it will find things that
like from from that aren't in the diff that
are like from tracing the control flow. um
which is what you want when it's like a
human reviewing it is like somebody who
has a lot of context who who can think what are
all the edge cases that this might run into and
and the signal to noise ratio is pretty good. It's
something maybe like 10% of the time it's wrong
like that's and and for like how that used to
be like with other code review products that
we've tried it was like basically you
had to ignore most of what it said. Um
it's pretty cool. How how long how long has
something like this worked? Is it like a latest
model thing or like have you had like like Robo
Bun or this kind of like automated repro automated
fixing like this whole pipeline? Like how how long
has that been actually possible? We can probably
like see this in a chart somewhere. Um that's
kind of a lot of commits but I think that's
that might not be on main. That might
be that the the Rust thing. Um uh uh

[00:16]
yeah I heard bun is going to be written
in Rust soon. Is that I don't know.
We're there's a I just have a quad
running and we'll see what happens. Um uh
but you can see like the the the volume of commits
there. It's like kind of lower and then it it's
it's definitely gotten up a lot and then it's gone
up a lot. Uh now really the bottleneck is like
do I feel good about merging this? Am I confident
that its changes are correct? And that's new
because it used to be like the code wasn't
good enough. What do you think? What do you
think is left like like what's it going to take
before well like is there like a missing tool
or like a missing model capability or model
version or something for you to kind of feel
like Robban can fully close the loop. Issue comes
in and then like fix goes out automatically.
I think it needs a little bit more uh it needs
it takes a lot of time to verify the changes

[00:17]
are correct. M um this was kind of already true
like when it's a person pushing up a PR. Um uh
but I think the the challenge is like how do
we make it how do we make sure to communicate
sufficient proof that the changes are correct.
Um or making it easier to like roll back things.
Um that's I think those are kind of
the two directions. But I think like
for the majority of like simple issues, we should
probably be pressing merge a lot more. And the
bottleneck now is actually like CI and like
making sure that uh like like the and and having
like fully running the code like the the
making sure all the test stuff works. M um
but I think it's like basically there for like
and the large projects are still non-trivial

[00:18]
but also I've been doing some pretty large
PRs lately with with cloud mostly with in the
not as much with Robo Bun but with like cloud
code um like uh we recently added support for uh
a built-in image processing library to
bond. I could probably pull up the PR. Um,
uh, and that was Claude. Um, uh, and also we
did a bunch of follow-up PRs, too. Uh, yeah,
it's like it's interesting because I think like
when I look at different people using quad code,
everyone is like at a kind of different level
of like sophistication or kind of like adoption
of this. And I think for me the hardest thing
is the model changes very often. So I have to
like constantly reune and kind of recalibrate to
what it can do. And like as an engineer, it's hard
cuz it's like a very weird technology. It's like
the first technology I've used that's like that.
And I I sort of feel like this is actually the
way that you do it is ahead of how the quad code
team does it for quad code itself. And to me like
that that like the way the quad code team does it
is actually very automated. But this is like
even further ahead. This is like almost like

[00:19]
full liftoff like full fully closed loop. Like
in the last two weeks we've added an HTTP3 server
to bun. Uh there's a PR for an HTTP2 server.
There's uh fetch support for HTTP 3 and HTTP2.
Um there's this image processing API. There's
the ongoing Rust rewrite which may not ship. Uh
uh uh that that's like the most
ambitious one I've done so far.
Uh and I done is too strong of a word because
it's very much not done. Uh uh so and so even
something like this like this is like a benchmark.
So Claude ran this benchmark for you. Yeah, Claude
ran this benchmark. Uh I gave it like a this ran
on like a separate like uh on like a Linux box. Um
uh yeah and it and I was like make it faster
than sharp and that's basically what I did. Um
I gave it like a few ideas like oh you could try
like read this code in JavaScript core to like
figure out the how to like avoid cloning the
type array when it's not strictly necessary. Um,

[00:20]
but like it it then went and did it and figured it
out. Um, uh, and like uh, yeah, it's pretty crazy
honestly because it was these this wouldn't none
of this would have worked uh, several months ago.
Yeah. I I feel like like within like
within anthropic like within an AI lab,
you call this kind of thing hill climbing. And
this is this idea that like if you give the model
some sort of metric and then you give it a way to
verify its result, you can just make it iterate
and keep going and keep going until it hits
that metric. Um, and this is something like
47 I think is uniquely good at. And I think
it's something really underutilized because I
think it's the first model that's actually very
good at that. And if you just give it a target,
you give it a way to like improve the performance
and you give it a way to measure, it'll just like
keep going until until it's done if you let it go
in auto mode. Yeah. And we can also see like uh

[00:21]
this is another case where like the code review
comments was really really helpful because like
there was like in this PR there's
like 100 comments or something uh
and it's just going and fixing everything.
Um uh uh like it goes on for a while and
in the meantime you're just working on something
else. Yeah, I was this was not like my the thing I
was 100% focused on. I was maybe like 10% focused
on this. I was doing like five things at once. Um
uh uh and this definitely wasn't possible like
6 months ago. Um 3 months ago like this is like
very recent that this is doable. Okay. So how
how are our sessions doing? Yeah. So we have
one PR there. There's almost another PR
coming up it looks like pretty soon. Um uh
this one is should be the trickiest one. Uh
um it mostly looks good though. Um like the
or like it looks plausible based on this

[00:22]
these changes. I wouldn't exactly do it this
way, but I think that's we need like a better
more optimized way to do this because that's
a lot of checks. Um and and looking looking at
your setup here, so you're using you mostly use
CLI. Yeah. And um do you always use auto mode
for permissions? Auto? Yeah. And then before
that I used dangerously skip permissions. Um
[laughter]
no you guys can delete stuff if you do that. I
don't I think I'm not supposed to recommend that.
Um but I think it's just not fun to wait for
Claude to like press approve because then you just
like go off and do something else and then it's
just been sitting there. So that's why auto mode
is really good because it's actually like a real
way to fix that instead of just like trusting.
And I I also noticed like the the input like the
little composer it's stuck to the bottom of the
screen. So you're using no flicker mode. Yeah, I'm
using no flicker. Honestly, I think we should just

[00:23]
like make that the default because it's so much
better. Um like you can see I can scroll really
fast and like like you could scroll fast before
but like sometimes there would be a flicker and
now there's not. Um, have have
folks tried no flicker mode for CLA?
Yeah, a few people. So, it's like
we launched it on April Fools. So,
you can think it [laughter] in hindsight
it came across as a joke a little bit, but
if you actually do quad code, no flicker equals 1
quad. So, just like set that environment variable,
we totally rewrote the renderer that's running
in the CLI. So, it's using virtualized scrolling,
virtualized selection. And so what this means is
like constant memory usage, constant CPU usage,
and also some nice stuff like uh like if Jared
types, he can actually like click around the
composer. And so you can actually click and mouse
events work, which is pretty crazy for a terminal.
So I'm just also having it monitor
the PR. Um, and you can see it's uh

[00:24]
it ran some commands and then it's going to go
to sleep for 20 minutes and wake back up. Um,
20 minutes is probably a little
bit too long, but it's okay. Um
uh oops. And what's that? Is that like using
like a loop or something? I think so. Uh uh. Uh
yeah. And then it's let's see how else is
it doing. And then the other ones are still
uh apparently it fixed an extra bug as well. Uh
uh. Okay. So we got Okay, so it's been what? It's
been like 20 minutes or so. 25 minutes and we
got one. How many PRs have we gotten? Two. Uh,
three PRs. Three PRs. That's not bad.
Yeah. And I think we'll get a fourth one
once it finishes running the tests. And then
in the meantime, Robo is still running and
kind of like generating even even more PRs.
Yeah. Every time somebody submits an issue,

[00:25]
it it tries to reproduce it. Yeah. I I kind of
feel like every like the the way quad code makes
you think is every time there's a new bottleneck,
you have to kind of automate that bottleneck and
then there's always some other bottleneck after
and you kind of move on to that and like it
started like writing code was the bottleneck and
now it's no longer the bottleneck and then like
verification and running tests that was like the
bottleneck and it's no longer the bottleneck and
now there's like a deeper layer of verification
maybe that maybe that's it. What do what do
you think are the bottlenecks remaining? It's
definitely this deeper layer of verification. Um I
feel like the bottleneck after that is going to be
like planning like what should we do, what should
we not do and what is the right way to fix this.
Um and like ideally Claude would be smart enough
or like we could trust Claude enough to to merge
the PRs by itself. Um and I think like in a in
certain projects you could pro probably do that
um and just have that be automatic completely.

[00:26]
Um, I think Bun is not yet or like it's not
yet there for Claude or sorry for for Bun. Um,
but I think it'd be really cool if if like we had
the tooling uh for us to feel confident enough
to do that. So So like right now Robbo it doesn't
like build features. It it doesn't do like feature
requests yet. It it that's true. Yeah, it doesn't
do feature requests but it we do also use it
sometimes. We we so we can also uh uh appmentntion
it in either discord or slack and it will like
try to implement the feature. Um uh so sometimes
when people are like hey bun is missing this thing
um then I just at mention the bot and
maybe like an hour later there's a PR. Um
a bunch of times I've somebody's
like tweeted at me something like
this can you fix this bug or whatever
and that's basically what I do. Um,
and then I reply with a link to the PR. Um,
should we add a Robbo account on Twitter? Um uh

[00:27]
and I think like so like it can do feature
requests, but I'm I'm hesitant for it to
implement literally everything anybody asked for
in a GitHub issue cuz that's kind of a lot cuz in
some ways it's it's kind of crazy to put something
like an image processing library inside a bun,
but like we talk about engineering taste and
there's like an element of taste that goes
into that. you felt like that's a good idea and
like we're not sure yet if Quad is at the point
where you would also think this is a good idea
but you know at some point in the future it'll
get there maybe it's starting to get and I do
think that like PRs become suggestions like
having uh like not merging PRs used to be like you
feel bad if you don't merge like a co-orker's PR
uh because like they put work into that but you
don't have to feel bad when it's like claude
Um uh so like if the PR is wrong or or or or
for for or whatever reason then you can just
not merge it. And uh but it does mean that like
the like the the bar for uh what you merge is like

[00:28]
should should it be there because I think that's
also a difference with with when it's like people
because with people you want you don't want
people to feel bad about their like lost work.
Um, so sort of in some ways it does actually end
up raising the bar for what you decide to merge.
Yeah, it's interesting how like as the bottlenecks
move, the dynamics change a little bit.
It's sort of like having to trust each
other, having to trust people on the
team. This kind of changes a little bit.
Now it's a little bit more about like do
we have the right automation and like do we
trust automation like as as a group? Yeah.
So I think we're almost at time. Is there
any like maybe one last thing we want to
we want to show people where we can kind of check
in on kind of like the progress that we've made?
Um I don't think so. Uh uh yeah,
it's it's still going one last

[00:29]
onto that fourth PR and it's going back and
forth like found a bug and then fixed a bug. Uh
looks like it's about to submit the
PR now. Okay, let's wait for this one.
Love to have one more. This is like the cool thing
about auto mode. It's like in auto mode I can let
like cloud runs like for hours and hours at a
time. Like I run it almost every night. I'll
just have a bunch of quads running in auto mode.
And I was like before this it just didn't work
cuz it always got stuck at some kind of
permission request. And that was crazy.
Like this entire thing was one prompt and and that
just ran for 30 minutes. Yeah. This is all I said.
Okay. So, it's pushing at
it's about to submit the PR.
That sounds like the right fix, too. This has
been an issue that's been open for a long time.

[00:30]
Okay. And we got a PR
Yeah, we can go to this issue and
we can see how many up votes it has.
20. Yeah, it's kind of a lot.
Cool. Maybe we can pause there. Um, but to
me, this is just like such a cool vision
of where engineering is going, I think,
for everyone in this room. And, you know,
we're going to see this first. we're going to
have to figure it out first and then everyone
else is going to have to figure this out. So, you
know, like we were talking about this morning,
just excited to be on this journey together. And
like you can see, we haven't figured everything
out yet. Um, but I think like the mode that
we're in is just constantly experimenting,
constantly trying to to see what the
next bottleneck is so we can solve it.
It's very exciting. This is
so cool. Like this stuff.

[00:31]
[applause] Cool. All right. Should
I like Yeah, you can weave it.
Come on,
bro.
