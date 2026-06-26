---
title: "Mastering Claude Code in 30 minutes"
url: https://youtu.be/6eBSHbLKuN0
channel: "Anthropic"
date: 2025-05-22
duration: "28:07"
lang: en-orig
youtube_id: 6eBSHbLKuN0
processed_at: 2026-06-26T07:57:21Z
---

# Mastering Claude Code in 30 minutes

- 채널: [Anthropic](https://www.youtube.com/channel/UCrDwWp7EBBv4NwvScIpBDOA)
- 발행: 2025-05-22
- 길이: 28:07
- 영상: <https://youtu.be/6eBSHbLKuN0>

## 자막 (en-orig)


[00:00]
[Music]
[Applause]
Hello. Hey everyone. Uh, I'm Boris. I'm
a member of technical staff here at
Anthropic and I created quad code and
here to talk to you a little bit about
some practical tips and tricks for using
quad code. Um it's going to be very
practical. I'm not going to go too much
into the history or the theory or
anything like this. Uh and yeah, before
we start actually can we get a quick
show of hands? Who has used quad code
before? Yeah. All right. That's what we
like to see. For everyone that didn't
raise your hands, uh I know you're not
supposed to do this while people are
talking, but if you can open your laptop
and type
this and this will help you install quad
code. Uh just so you can follow along

[00:01]
for the rest of the
talk. All you need is NodeJS. If if you
have it, this should work.
Yeah, if you well, you don't have to you
don't have to follow along, but if you
don't have it yet, yeah, this is your
chance to install it so you can follow
along. So, what is quad code? Quad code
is a new kind of AI assistant and
there's been different generations of AI
assistance for coding. Most of them have
been about completing, you know, like a
line at a time, completing a few lines
of code at a time. Cloud code is not for
that. It's fully agentic. So, it's meant
for building features, for writing
entire functions, entire files, fixing
entire bugs at at the same
time. And what's kind of cool about
Cloud Code is it works with all of your
tools and you don't have to change out
your workflow, you don't have to swap
everything to start using it. So,

[00:02]
whatever IDE you use, if you use VS Code
or if you use Xcode or if you use uh Jet
Brains IDEs, there's some people at
Anthropic that you can't pry Vim from
their cold dead hands, but they use quad
code because quad code works with every
single ID, every terminal out there.
It'll work locally uh over remote SSH,
over T-Max, whatever environment you're
in, you can run it.
It's general purpose and this is
something where if you haven't used
these kind of free form coding
assistants in the in the past, it can be
kind of hard to figure out how to get
started because you open it up and you
just see a prompt bar and you might
wonder like what do I what do I do with
this? What do I type in? It's a power
tool so you can use it for a lot of
things. Um, but also because it can do
so much, we don't try to guide you
towards a particular workflow because
really you should be able to use it
however you want as an engineer.
As you open up Cloud Code for the first
time, there's a few things that we
recommend doing uh to get your

[00:03]
environment set up. And these are pretty
straightforward. So run terminal setup.
This will give you shift enter for new
lines. So you don't have to do like
backslashes to enter new lines. This is,
you know, it it makes it a little bit
nicer to use. Do theme to set light mode
or dark mode or doltonize
themes. Um you can do slashinstall
github app. So today we in we announced
a GitHub app where you can at mention uh
claude on any GitHub issue or pull
request. So to install it just run this
command in in your
terminal. Um you can customize the set
of allowed tools that you can use so
you're not prompted for it every time.
This is pretty convenient. Um for stuff
that I'm prompted about a bunch, I'll
definitely customize it in this way so I
don't have to accept it every time. And
something that I actually do is for a
lot of my prompts I won't handype them
into cloud code. If you're on Mac OS,
you can go into your system settings
under accessibility is dictation and you
can enable it. And so something I do is
you just hit like that dictation key
twice and you can just speak your

[00:04]
prompt. And it helps a lot to have
specific prompts. So this is actually
pretty awesome. You can just talk to
quad code and uh like you would another
engineer and you don't have to type a
lot of
code. So when you're starting out with
quad code, it's so free form and it can
do everything. What do you start with?
The thing I recommend above everything
else is starting with codebased Q&A. So
just asking your question, asking
questions to your codebase. This is
something that we teach new hires at
Enthropic. So on the first day in
technical onboarding, you learn about
cloud code, you download it, you get it
set up, and then you immediately start
asking questions about the codebase. And
in the past when you're doing technical
onboarding, it's something that taxes
the team a lot, right? You have to ask
other engineers on the team questions.
You have to look around the code and
this takes a while. You have to figure
out how to use the tools. It t this
takes a long
time. With cloud code, you can just ask
cloud code and it'll explore the
codebase. It'll answer these kind of
questions. And so at Anthropic,
onboarding used to take about two or
three weeks for technical hires. It's

[00:05]
now about two or three
days. What's also kind of cool about Q&A
is we uh we don't do any sort of
indexing. So there's no remote database
with your code. We don't upload it
anywhere. Your code stays local. We do
not train generative models on the code.
So it's there, you control it. There's
no indices or anything like this. And
what that means is also there's no
setup. So you start cla you download it,
you start it. There's no indexing. You
don't have to wait. You can just use it
right
away. This is a technical talk. So um
I'm going to show some very specific
prompts and very specific code samples
that you can use and hopefully improve
and up your quad code experience.
So some kind of questions that you can
ask is uh you know like how is this
particular piece of code used or how do
I instantiate this thing and cloud code
it won't just do like a text search and
try to answer this. It'll often go a
level deeper and it'll try to find
examples of how is this class
instantiated how is it used and it'll
give you a much deeper answer. So
something that you would get out of a
wiki or documentation instead of just

[00:06]
like command
f something that I do a lot also is ask
it about git history. So for example,
you know, why does this function have 15
arguments and why are the arguments
named this weird way? And this is
something I bet in all of our code
bases, you have some function like this
or some class like this and cloud code
can look through git history and it'll
look to figure out how did these
arguments get introduced and who
introduced them and what was the
situation what are the issues that those
commits linked to and it'll look through
all this and summarize it and you don't
have to tell it that in all these in all
this detail you just ask it. So just say
look through git history and it'll know
to do
this. The reason it knows it by the way
is not because we prompted it to.
There's nothing in the system prompt
about looking through git history. It
knows it because the model is awesome
and if you tell it to use git, it'll
know how to use git. So we're lucky to
be building on such a good
model. I often ask about uh GitHub
issues. So um you know it can use web
fetch and it can fetch issues and look
up context on issues too. And this is

[00:07]
pretty
awesome. Yeah. And this is something
that I do every single Monday in our
weekly standup is I ask what did I ship
this week? And Quad Code looks the log.
It knows my username and it'll just give
me a nice readout of everything I I
shipped and I'll just copy and paste
that into a
document. So yeah, that's tip number one
for people that have not used Cloud Code
before. If you're just showing it to
someone for the first time, on boarding
your team, the thing we definitely
recommend is start with codebased Q&A.
Don't start by using fancy tools. Don't
start by editing code. Just start by
asking questions about the codebase. And
that'll teach people how to prompt. And
it'll start teaching them this boundary
of like what can claude code do? What is
it capable of versus what do you need to
hold its hand with a little bit more?
What can be oneshotted? What can be
two-shotted, threeshotted? What do you
need to use interactive mode for in a
ripple? Once you're pretty comfortable
with Q&A, you can dive into editing
code. This is the next thing. And the
cool thing about uh any sort of agentic

[00:08]
uh you know like using a LM in a agentic
way is you give it tools and it it's
just like magical. It figures out how to
use the tools. And with cloud code we
give it a pretty small set of tools.
It's not a lot. And so it has a tool to
edit files. It has a tool to run bash
commands. Uh it has a tool to search
files. And it'll string these together
to explore the code, brainstorm and then
finally make
edits. And you don't have to prompt it
specifically to use this tool and this
tool and this tool. You just say, you
know, do this thing and it'll figure out
how to do it. It'll string it together
in the right way that makes sense for
quad
code. There's a lot of ways to use this.
Something I like to do sometimes is
before having quad jump in to write
code, I'll ask it to brainstorm a little
bit or make a plan. This is something we
highly recommend and something I see
sometimes is people, you know, they take
quad code and they ask it, hey,
implement this enormous like 30,000 wine
uh feature and sometimes it gets this
right on the first shot. But sometimes
what happens is the thing that it builds

[00:09]
is not at all the thing that you wanted.
And the easiest way to get the result
you want is ask it to think first. So
brainstorm ideas, make a plan, run it by
me, ask for approval before you write
code. And you don't have to use plan
mode. You don't have to use any special
tools to do this. All you have to do is
ask claud and it'll know to do this. So
just say before you write code, make a
plan. That's
it. This is also I wanted to include
this one. This commit push. This is a
really common incantation that I use.
There's nothing special about it, but
Claude is kind of smart enough to
interpret this. So it'll make a commit.
It'll push it to the branch, make a
branch, and then make a pull request for
me on GitHub. You don't have to explain
anything. It'll look through the code.
It'll look through the history. It'll
look through the git log by itself to
figure out the commit format and all the
stuff and it'll make the commit and push
it the right
way. Again, we're not system prompting
it to do this. It just knows how to do
this. The model is
good. As you get a little bit more
advanced, you're going to want to start
to plug in your team's tools. And this

[00:10]
is where Cloud Code starts to really
shine. And there's generally two kinds
of tools. So, one is batch tools. And an
example of this, I just made up this
like barley CLA. This isn't a real
thing. Um, but you can say use the CLI
to do something and you can tell quad
code about this and you can tell it to
use for example like d-help to figure
out how to use it. And this is
efficient. If you find yourself using it
a lot, you can also dump this into your
quadm which we'll talk about in a bit.
So cloud can remember this across
sessions. But this is a common pattern
we follow at anthropic and we see
external customers use too. And same
thing with MCP. Um, quad code can use
batch tools, it can use MCP tools. So,
you know, just tell it about the tools
and you can add the MCP tool and you can
tell it how to use it and it'll it'll
just start using
it. And this is extremely powerful cuz
when you start to use code on a new
codebase, you can just give it all of
your tools, all the tools your team
already uses for this codebase and cloud
code can use it on your

[00:11]
behalf. There's a few common
workflows and this is the one that I
talked about already. So kind of do a
little bit of exploration, do a little
bit of planning and ask ask me for
confirmation before you start to write
code. These other two on the right are
extremely powerful when cla has some way
to check its work. So for example by
writing unit tests or screenshotting and
puppeteer or screenshotting the iOS
simulator, then it can iterate. And this
is incredible because if you give it for
example a mock and you say build this
web UI, it'll get it pretty good. But if
you let it iterate two or three times,
often it gets it almost perfect. So the
trick is give it some sort of tool that
it can use for feedback to check its
work and then based on that it will
iterate by itself and you're going to
get a much better result. So whatever
your domain is, if it's unit test or
integration test or screenshots for apps
or web or anything, just give it a way
to see its result and it'll iterate and
get
better. So these are the next tips.

[00:12]
teach Quad how to use your tools and
figure out the right workflow. Um, if
you want Quad to jump in and code, if
you wanted to brainstorm a little bit,
make a plan, if you wanted to iterate,
kind of have some sense of that so you
know how to prompt Quad to do what you
want. As you go deeper beyond tools, you
want to start to give Quad more context.
And the more context, the smarter the
decisions will be because as an engineer
working in a codebase, you have a ton of
context in your head about your systems
and all the history and and everything
else. So you can there's different ways
to give this to Claude and as you give
Cloud more context it'll do
better. There's different ways to do
this. The simplest one is what we call
quad MD and quad.mmd is the special file
name. The simplest place to put it is in
the project route. So the same directory
you start quad in. Put a quad MD in
there and that'll get automatically read
into context at the start of every
session and essentially the first user
turn will include the quad MD.
You can also have a local cloudmomd and

[00:13]
uh this one you don't usually check into
source control. So cloudmd you should
check into source control share with
your team so that you can write it once
and share it with your team. This one
you don't check in it's just for you.
The kinds of things you put in cloudmd
it's like common bash commands common
mcp tools uh architectural decisions
important files anything that you would
kind of typically need to know in order
to work in this codebase. Try to keep it
pretty short because if it gets too
long, it's just going to use up a bunch
of context and it's usually not that
useful. So just try to keep it as short
as you can. And for for example, in our
codebase, we have uh common batch
commands, we have a style guide, we have
a few core files, kind of things like
that. All the other quad MDs, you can
put them in other nested child
directories and cloud will pull them in
on
demand. So these are the quadmds that
will get pulled in automatically. Um but
then also you can put in put cloudmds in
nested directories and those will get
put those will get automatically pulled
when cloud works in those

[00:14]
directories. Um and of course if you're
you know a company maybe you want a
quadd that's shared across all the
different code bases and you want to
manage it on behalf of your users and
you can put it in your enterprise route
and that'll get pulled in
automatically. There's a ton of ways to
pull in context. I actually had a lot of
trouble putting this slide together just
to communicate the breath of ways you
can do this. But quadmd is pulled in
automatically. You can also use slash
commands. So this is quad/comands and
this can be in your home directory or it
can be checked into your project. And
this is for
slashcomands. And over
here we have a few examples of the slash
commands that we have in cloud code
itself. And so for example, if you're in
the cloud code repo and you see issues
getting labeled, that's actually this
workflow running here. It's label GitHub
issues and we have a GitHub action
running, the same one we talked about
this
morning where Cloud Code will run this
command and it's just a slash command.
It'll run and it'll label the issues so

[00:15]
humans don't have to. It just saves us a
bunch of
time. And of course, you can atmention
files to pull them into context. Um, and
like I said before, quadm in a nested
directory get pulled in when quad works
in that
directory. So give quad more context and
it's definitely worth taking the time to
tune context. You can run it through a
prompt improver. Consider who the
context is for. If you want to pull it
in every time, if you want to pull it in
on demand, if you want to share it with
a team, if it's a personal preference,
definitely take the time to tune it.
This will improve performance
dramatically uh if you do it
right. As you get more advanced, you're
going to want to think about this a
little bit more. This kind of hierarchy
of different ways to pull in everything.
So like not just quadmd, but also config
and uh kind of everything about quad you
can pull in in this hierarchical way. So
projects uh are specific to your git
repo and this you can check in or you

[00:16]
can make it just for you. You can also
have global configs that are across all
your projects or you can have enterprise
policies and this is essentially a
global config that you row out for all
of your employees, everyone on your team
automatically. And this slide is like
pretty information dense, but the point
is this applies to a lot of stuff. So
you can do this for slash commands, you
can do it for permissions. So for
example, if you have a batch command
that you would run for all your
employees uh like all your employees use
this like test command for example, you
can actually just check it into this
enterprise policies file and then any
employee when they run this command, it
will be auto approved which is pretty
convenient. And you can also use this to
block commands. So for example, let's
say there's a URL that should never be
fetched. Um just add it to this config
and that'll make it so an employee
cannot overwrite it and that that URL
can never be fetched. So pretty
convenient both to unblock people and
also just to keep your codebase
safe. And then same thing for MCP
servers. Have a MCP JSON file, check it
into the codebase. That way anytime

[00:17]
someone runs quad code in your codebase,
they'll be prompted to install the MCP
servers and share it with the
team. If you're not sure which of these
to use, this is like a kind of an insane
matrix because we support a lot of stuff
and engineer workflows are very flexible
and every company is different, so we
kind of want to support everything. So
if you're not sure how to get started, I
would recommend start with shared
project
context, you write this once and then
you share it with everyone on the team
and you get this kind of network effect
where you know someone does a little bit
of work and everyone on the team
benefits. There's a lot of tools built
into quad to manage this. Uh so as an
example, if you run memory, you can see
all the different memory files that are
getting pulled in. So maybe I have an
enterprise policy. I have my user
memory. I have project quadd. And then
maybe there's a nested quadmd that's
only pulled in for certain
directories. And then similarly when you
do slashmemory you can edit particular
memory files. When you type pound sign
to remember something you can pick which

[00:18]
memory you want it to go
to. So yeah that's the next tip. take
the time to configure QuantumD, MCP
servers, all the stuff that your team
uses so that you can use it once,
configure it once, and then share it
with
everyone. Um, an example of this is uh
in our apps repo uh for anthropic. This
is like the repo that we have all of our
uh web and apps code in. There's a
Puppeteer MCP server and we share this
with the team. Um, and there's an MCP
JSON checked in. So any engineer working
that repo can use Puppeteer in order to
pilot end to end tests and to screenshot
automatically and iterate so that every
engineer doesn't have to install it
themselves. This is a talk about pro
tips. So I I just want to take a quick
inter key bindings that people may not
know. It's a it's very hard to build for
terminal. It's also very fun. It feels
like rediscovering this new design
language. But something about terminal
is it's it's extremely minimal. And so

[00:19]
sometimes it's hard to discover these
key bindings. And here's just a quick
reference sheet. So anytime you can hit
shift tab to accept edits. Uh and this
switches you into auto accept edits
mode. So bash commands still need
approval, but edits are auto accepted.
And you can always ask quad to undo them
later. Um for example, I'll do this if I
know Claude's on the right track or if
it's writing unit tests and iterating on
tests. I'll usually just switch into
auto accept mode so I don't have to okay
every single
ite. So, for example, if it's not using
a tool correctly and you want it to use
it correctly from then on, just type the
pound sign and then tell it what to
remember and it'll remember it. It'll
incorporate it into QuadMD
automatically. If you ever want to drop
down to bash mode, so just run a bash
command. You can hit the exclamation
mark and type in your command. That'll
run locally, but that also goes into the
context window. So, Claude will see it
on the next turn. Um, and this is pretty
good for longunning commands if you know
exactly what you want to do or any
command that you want to get into
context and cloud will see the command

[00:20]
and the
output. You can appment mention files
and folders. Uh, anytime you can hit
escape to stop what Claude is doing. Um,
no matter what Claude is doing, you can
always safely hit escape. It's not going
to corrupt the session. It's not going
to mess anything up. So maybe Claude is
doing a file edit. I'll hit escape. I'll
tell it what to do differently. Or maybe
it suggested a 20 line edit and I'm like
actually 19 of these lines look perfect
but one line you should change. I'll hit
escape. I'll tell it that and then I'll
tell it to redo the
edit. Uh you can hit escape twice to
jump back in history. Um and then after
you're done with the session you can
start quad with resume to resume that
session if you want. Um or d-
continue. And then anytime if you want
to see more output, hit control R and
that'll show you the entire output. The
same thing that Claude sees in its
context
window. The next thing I want to talk
about is the Cloud Code SDK. So we
talked about this at the top. Uh right
after this, Sid is doing a session I

[00:21]
think just across the hallway and he's
going to go super deep on the SDK. If
you hadn't played around with this, if
you used the -p flag in Claude, this is
what the SDK is. And we've been learning
a bunch of features over the last few
weeks to make it even even
better. Um, so yeah, you can you can
build on top of this. You can do cool
stuff. This is exactly the thing that
claude code uses. It's exactly the same
SDK. And so, for example, something you
can do is claw-p. So, this is the the
CLI SDK. You can pass up you can pass a
prompt. You can pass some allowed tools
which could include specific batch
commands and you can tell it which
format you want. So you might want JSON
or you might want streaming JSON if you
want to process this somehow. So this is
awesome for for building on. We use this
in CI all the time. We use this for
incident response. We use this in all
sorts of pipelines. So really
convenient. Just think of it as like a
Unix utility. You give it a prompt, it
gives you JSON. You can use this in any
way. You can pipe into it. You can pipe
out of it.

[00:22]
The piping is also pretty cool. So you
can use like for example git status and
pipe this in and you know use jq to
select the result. It the combinations
are endless and it's sort of this new
idea. It's like a super intelligent Unix
utility and I think we barely scratched
the surface of how to use this. We're
just figuring this
out. You can read from like a GCP bucket
read you know like a giant log and pipe
it in and tell cloud to figure out
what's interesting about this log. Um,
you can fetch data from like the Sentry
uh CLI. You can also pipe it in and have
Claude do something with
it. The final thing, and this is
probably like the most advanced use
cases we see. I'm sort of a quad normy.
So, I'll have usually like one cloud
running at a time and maybe I'll have
like a few terminal tabs for a few
different repos running at a time. When
I look at power users in an ad of
anthropic, almost always they're going
to have like SSH sessions. They'll have
uh like T-Max tunnels into their quad
sessions. They're going to have a bunch

[00:23]
of checkouts of the same repo so that
they can run a bunch of quads in
parallel in that repo or they're using
git work trees to have some kind of
isolation as they do this. And we're
actively working on making this easier
to use. But uh for now like these these
are some ideas for how to do more work
in parallel with quad. You can run as
many sessions as you want.
Uh, and there's a lot that you can get
done in
Perl. So, yeah, that's it. I wanted to
also leave some time for Q&A. So, I
think this is the last slide that I
have. And yeah, if folks have questions,
there's mics on both
sides. And yeah, we'd love to answer any
questions.
[Applause]
I did.

[00:24]
Hey Boris, thanks for building a cloud
code and I was wondering what was the
hardest implementation like part of the
implementation for you of building it.
I think there's a lot of tricky
parts. Um I think one part that is
especially tricky is the things that we
do to make bash commands safe. Um bash
is inherently pretty dangerous and it
can change system state in unexpected
ways. But at the same time, if you have
to manually approve every single batch
command, it's super annoying as an
engineer and you can't really be
productive because you're just
constantly approving every command. And
just kind of navigating how to do this
safely in a way that that scales across
the different kinds of code bases people
have because not everyone runs their
code in a Docker container um was was
pretty tricky. And essentially the thing
we landed on is there's some commands
that are readon. There's some static
analysis that we do in order to figure
out which commands can be combined in
safe ways. And then we have this pretty
complex tiered permission system so that
you can allow list and block list

[00:25]
commands at different levels.
Hi Boris, you mentioned uh giving an
image to cloud code which made me wonder
if there's some sort of multimodal
functionality that I'm not aware of. Is
that are you just pointing it at an
image on the file system or something?
Yeah, so cloud code is fully multimodal.
Um, it has been from the start. It's in
a terminal, so it's a little uh hard to
discover. Uh, but yeah, you can take an
image and just drag and drop it in.
That'll work. Uh, you can give it a file
path. That'll work. Um, you can copy and
paste the image in and that works
too. Um, so I'll use this pretty often
for if I have like a mock of something,
I'll just drag and drop in the mock.
I'll tell it to implement it. I'll give
it up a tier server so it can iterate
against it. And yeah, it's just fully
automated.
Um, hey, uh, why did you build a CLI
tool instead of an IDE?
Yeah, it's a it's a good question. I
think there's probably two reasons. One
is, uh, we started this at anthropic and

[00:26]
at anthropic people use a broad range of
IDEs and some people use VS Code, other
people use Zed or Xcode or Vim or Emacs
and it was just hard to build something
that works for everyone and so terminal
is just the common denominator. The
second thing is at Enthropic we're uh we
see up close how fast the model is
getting better and so I think there's a
good chance that by the end of the year
people aren't using IDs anymore and so
we want to get ready for this future and
we want to avoid overinvesting in UI and
other layers on top given that the the
way the models are progressing it just
it may not be useful work pretty soon.
Yeah. How much have you I don't know if
this is is this on how much you used
quad code for machine learning modeling
and almost that autoML experience. I was
curious what the experience has been so
far with that. Yeah, I think I think the
question was how much are we using cloud
code for machine learning and and

[00:27]
modeling? We actually use it for this a
bunch. So both engineers and researchers
at anthropic use quad code every day. Um
I think about 80% of people at Enthropic
that are technical use quad code every
day. And hopefully you can see that in
the product and kind of the amount of
love and dog fooding we've put into it.
Um, but this includes researchers who
use tools like the notebook notebook
tool to edit and run notebooks. Okay,
very cool. Thank you.
All right, I think that's it.
[Music]
Thanks. Heat. Heat.
[Music]
