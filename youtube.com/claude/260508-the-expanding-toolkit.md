---
title: "The expanding toolkit"
channel: claude
url: https://www.youtube.com/watch?v=KLCuxMDZSDg
youtube_id: KLCuxMDZSDg
published: 2026-05-08
duration: "21:22"
captions: en-orig
---

# The expanding toolkit

[![The expanding toolkit](https://img.youtube.com/vi/KLCuxMDZSDg/hqdefault.jpg)](https://www.youtube.com/watch?v=KLCuxMDZSDg)

<details>
<summary>자막: The expanding toolkit (21:22)</summary>

[00:00]
[snorts]
>> Hello everybody.
How are folks doing today? My name is
Lucas. I'm a research PM here at
Anthropic.
And today I'll be talking about the
expanding toolkit. But first of all, I
want to say thank you everybody for
joining us at our code with Claude
conference. We're very grateful you're
here and we love speaking directly to
our users.
Cool. So, what am I going to talk about
today?
The overarching theme of today's talk is
that the scaffolding that you had to
build last year actually ships with the

[00:01]
model today.
So, I want you all to think of the model
no longer as just an input-output LLM
box, but rather as a series of tools
around that model that expands its
capabilities and leads to better
performance.
So, in other words, we see the model
itself as an expanding toolkit.
And so, this talk will be a series of
befores and afters. On the left side,
you'll see basically what things look
like previously.
And on the right side, you'll see what
that same task looks like, but now in
2026.
Most of this will be heavily like
heavily simplified. And so, what you'll
notice is that not just you know, not
just better reliability,
but you also get much simpler
development as well. So, you have to
focus less on the actual retries,
wrappers, and so forth, and more so on

[00:02]
just getting the outcome that you're
looking for.
And so, we'll be covering things like
tool use, context management, code
execution, and computer use.
Then I'll be sharing some practical tips
for each of those.
And then for the Cloud Code fans in the
audience, I'll also have quick tips
specific to Cloud Code.
So, a year ago building an agent really
meant building around the model.
You know, you might have routers to pick
the right tools. You might have retry
loops. You might have output validators,
context compaction. You might even have
to do some coordinate math if you're
doing computer use.
You'd have a hundred lines of code,
hundreds of lines of scaffolding before
you even build any product.
Now, that scaffolding hasn't
disappeared, but it moved. It now ships
with the model itself.
So, the point isn't really that the work
went away, it's that you don't have to
own it anymore.

[00:03]
Cool. So, now the first capability that
I want to talk about is tool use.
Specifically tool routing and retries.
On the left side, you can see what this
looked like previously.
You couldn't really trust the model with
the full tool set.
It would eat into the context window,
and so you'd have to build a router.
And the way you might build this router
is through things like string matching,
heuristics. You know, you might say,
"Oh, if the model mentions SQL, then
give it the database tool."
And then you also needed a retry
decorator on top of that because the
tools failed often enough that you
actually needed back off.
Well, routers like those are basically
guesses about the user intent written in
conditional if statements.
They're brittle, and they're sort of the
first thing that breaks when you try
actually adding a new tool.
Now, on the right, we have what the new

[00:04]
paradigm is.
The model can actually search through
tools and pick the right tool itself.
The model's intelligent enough and tool
selection accuracy is now high enough
that tool routers and pre-filtering
usually makes things worse, not better.
We want the model to make decisions
about what tools are relevant in the
context it's working in.
And now, when a tool errors, you can
actually trust that Claude will see that
error, recover on its own, and call the
tool again.
So, no more pesky tool re-routers, no
more heuristics around when to bring in
certain tools. That's all built into the
model today.
Now, as promised, uh oh,
can we go back one slide?
Now, as promised, a quick tip for uh
tool use. And this one is very powerful
and one that I actually use uh quite
frequently.

[00:05]
And so,
uh when you're giving when you're giving
a tool to Claude, most developers
typically give the input to that tool to
Claude.
So, you might tell Claude, you know,
here are the parameters you need in
order to call this tool and to use this
function.
But actually, what you can do is give
Claude a description of the output
schema as well. And so, you can see in
the example I have here in the
description, I actually outlined,
you know, this search docs tool will
search the docs and it'll return the ID,
title, snippet, and score.
And so, by doing this, um you can
actually let Claude know what to expect
from this tool call. So, for example, if
Claude wanted to rank the outputs of
this tool, it already knows that a score
will be returned by this tool,
effectively saving it a round trip from
the harness.
And so, by doing this, you get more
efficient and more intelligent outputs

[00:06]
from Claude when using this tool.
And now for a Claude code quick tip,
this is another one that I like to use
frequently. You can actually use pre-
and post-tool use hooks defined in your
Claude settings. So, what this means is
Claude calls a specific tool or after
Claude calls a specific tool, you can
actually have something happen
programmatically.
And so, you might do this to block
certain tool calls in specific
situations, or you might use this to
like analyze and log outputs
programmatically after the tool call's
made.
Um can we go forward one on the speaker
notes?
Cool. So, next I'll be speaking about
context management.
You know, long-running agents previously
meant that you had to build your own
memory system.
You might do something like chunking.

[00:07]
You might even do rag, something that's
uh very, very popular, especially to
manage those pesky context windows.
You might even call another model to
summarize what's going on after every
end turns or end tokens.
So, again, the the idea is you were
building a scaffolding so that you could
practically extend the model's context
window.
And then you might even also have cash
breakpoints that you had to then move by
hand in order to save on cost and cash
previous turns.
Well, now we've simplified all of that
tremendously.
And by offering 1 million context length
at flat pricing, that already reduces
most of the window pressure.
And then you pair that with server-side
compaction as well as context editing,
and it basically turns the rest of that
all into just a few lines of config,
which you can see on that right side.
And this is how we get much closer to

[00:08]
the feeling of an infinite context
window that was mentioned at the morning
keynote today.
And so again, this is just another
example of how a lot of scaffolding that
you had to previously build in order to
make the model work in the ways that you
want is now just completely built into
the API and is just a single API call
away.
So now for a quick tip on context
management.
So we actually recommend that every end
turn you actually clear tool results.
And by pruning stale tool outputs, think
about things like screenshots or search
results or file reads, you can actually
save tremendously on on context while
keeping the decisions that they
informed, which Claude mentions in its
transcript.
And so you can imagine you have a
transcript here where the model read a
huge file, it also had to get a
screenshot, then it made some decision

[00:09]
based on that, and then it had a search
that dumped a ton of text.
By clearing those results and just
keeping the core task, the decision that
was made based on those tool results,
and the results that the agent analyzed
itself, you can save on tokens in real
time.
And now for the Claude Code fans, uh
this quick tip, um I I suspect a lot of
you might already know this one, but I
like it a lot, and if you have Claude
Code open right now, I suggest you try
it. Do {slash} context to actually get
this live colored grid breakdown of
what's filling your context window.
And that's a great way to kind of
viscerally see what I'm describing here
in terms of how much space messages,
tool results, systems, and MCP
definitions takes in your context
window. And you'll also see some
optimization suggestions there as well.
Cool. Next up is code execution.

[00:10]
So, previously the write, run, and fix
loop used to be the developer's job.
You might find a VM provider,
spin up a sandbox in the VM they
provide. You would then have to have the
model output some code, put that code on
the VM, run that model's code, parse the
feedback, parse the traceback from
running that code, feed it back into the
model, and then you'd have to run that
on repeat until the model succeeded at
the task it wanted to do on that VM.
Well, we wanted to massively simplify
that. And so, now we actually offer a
code execution tool, which automatically
gives Claude a hosted sandbox on the
server side.
So, this means that that entire loop
that I just described effectively
happens inside a single API turn. So, no
more harness round trips between Claude
and whatever VM you're using.
Claude can just in the back end on the
API side tap into that separate computer

[00:11]
that's being used just for Claude's
scratch pad and work.
And now, this one is maybe a little less
of a tip and more so a mental model as
to how to think about code execution and
versus your local bash.
So, when we give Claude the code
execution tool, it basically gets its
own computer to do stuff on. So, think
about this in a way of like giving
Claude a little calculator or something,
except it's an entire computer that it
can actually use. And so, this means
that Claude can use this computer for
things like stateless compute, data
analysis. It can, you know, install
custom libraries here. But basically, it
can do all this work without actually
disrupting or cluttering your local file
system and your local computer.
Then, when Claude does need to access
something that only exists on your local
computer, maybe it's your repo or a
Python MV that you have installed, or

[00:12]
just any other local context you have,
it can then go back to the real bash on
your computer, and it intelligently
knows which of the two to use.
Now, for another Claude code quick tip,
um
you can actually use /schedule to
schedule cron-triggered autonomous runs.
And so, think about this self-iteration
loop I described on the previous slide,
but now on a timer, happening exactly
when you need it, and completely
autonomously done by Claude.
And now, last but certainly not least,
this is an area where I spend a lot of
my time uh working with Claude, um is
computer use.
So, previously for a computer use, let's
say you wanted uh Claude to drive your
laptop, most laptops have a 1080p
screen, and you had to send that image
to Claude.
So, in order to have reliable clicks,
you needed a pile of image glue. So,

[00:13]
what that would look like is you first
take your 1080p image, you downscaled it
to what fit Claude's pixel limits, you
tracked the factor of that downscaling,
then when the model would sample a
click, you would then need to scale that
click back up to your original
resolution.
So, you'd have to write all that code,
and then wrap it in retries and verify
statements as well.
Well, this was very big pain point and
we've heard the feedback and so Opus 47
can now actually take native resolution
screenshots and return one-to-one pixel
coordinates up to 1440p,
which captures the vast majority of
display resolutions.
So now that means that the scaling math
is completely gone and you can simply
send your image and trust that Claude
will click exactly where it needs to.
And we're really excited about this uh
capability as well because computer use
as a capability is something that over

[00:14]
the last 12 months has made great leaps
and bounds.
So our headline evaluation here is
called OS World. And that's basically um
an eval that tracks how well the model
can complete complicated tasks on
professional software as well as
consumer-grade software.
And so less than 12 months ago, Claude
was scoring below 50% on this eval. So
it could not complete half the tasks
that was at that was asked of Claude.
Now we're about to hit 80% on this eval
and we just reported 78% on Opus 47.
So making computer use easier to use is
something that's very exciting for us as
we see it as a as an aspiring capability
that is just now at the cusp of broad
usability.
So as I mentioned, um
you know, we support resolutions up to
1440p, but we actually really encourage
developers uh to experiment across
resolutions and formats. Now if you're

[00:15]
doing really high-res stuff like 4K, we
still recommend that you downscale on
your side.
However, you're doing anything up to
1440p, we recommend that you try
different resolutions to see what works
best for you as well as different image
formats like JPEG, PNG, or WebP.
Each of these compresses images
differently and creates different
compression artifacts. And so by testing
it on your use case and the kinds of
UI's that you're trying to automate, you
can find what works best for you.
Now, a Claude code quick tip here is
that Claude code can actually leverage
your Chrome browser session itself. So
if you're in Claude code and you have
Claude in Chrome installed, which you
can get on claude.ai/chrome,
this means that your Claude code session
that that agent's harness can actually
start to use and navigate the web. And
this includes local development as well.
And I'll show you something really cool
that you could do uh with that in a

[00:16]
second.
So now we're actually going to do a
short demo. I'll show a short
pre-recorded demo of an agentic coding
loop with Claude code and you'll see
computer used in action while with the
Claude in Chrome extension.
Cool.
So basically we what we'll have what we
have here is a uh Claude code session
and we've been working on a project
management dashboard, but it has a
couple bugs.
The first bug is that the new button
isn't actually adding a card. And the
new button should be adding a card. So
we asked Claude to open it in Chrome and
try it itself.
And so we'll see this dashboard load as
soon as Claude decides to open the
browser.
Cool. So you can see Claude is connected
through Claude in Chrome here.
And so the first thing that Claude's
going to try to do is to reproduce the

[00:17]
issue.
So you could see it spun up Claude in
Chrome and it's going to test this live
board itself.
So first Claude is now trying to type
something. You could see in the bottom
left of the uh dashboard there. Claude's
trying to type something, but it's
seeing some issues.
And so, in real time, Claude is both
testing and debugging side by side, same
way that you might do uh, QA and eng in
order to fix these bugs.
So, now you can see it tried typing
something.
Didn't work.
And now Claude will actually go into the
code and make the code changes to wire
up the card creation successfully.
And now you can see that Claude has
successfully created the card. So, it
found the issue by actually testing it,
tried it, and fixed it.
But now with creation working, Claude is

[00:18]
also going to check some other features.
For example, whether these cards can be
correctly uh, dragged across columns.
So, Claude can actually do drag actions
as well.
And so, Claude just tried to drag the
review PR into done, but it accidentally
landed in to do.
It recognizes that that's a bug, has the
insight within Claude code,
and then it diagnoses that drag-and-drop
box, and it's going to actually write
the fix in real time.
Then it retests the flow
by once again creating It retests the
flow from the ground up, so it'll once
again create the new item.
Great, thank you, Claude. That's
working. And now it'll test the
drag-and-drop flow with that review PR
now correctly going into the done
section.
From there, Claude will recap the fixes
it made, and will summarize all its
changes.

[00:19]
Now, we think that this is a really
powerful loop because most software
today is created for humans, and so it
has to be tested in a human-like way.
So, giving Claude the capability to do
browser use and computer use during its
development cycle allows it to close
that loop where it can create
human-focused software and actually
solve bugs itself directly
without the developer needing to come in
and handhold Claude to the bug and the
solution.
So, now to wrap up the call and bring it
back to the main theme and the main
point that we really want to get across.
The rule that you should have in your
mind is any code that you are writing
that is compensating for model
unreliability will have a half-life of
just months.
You should leave that work to us.
We will continue to make Claude more
reliable and more capable through this
expanding toolkit that comes with the
model.

[00:20]
So, things like retry logic, routers,
planners, verification loops, all of
these are going to get absorbed in the
model and they have been getting
absorbed in the model as I've shown you
in the prior slides in this talk.
Versus code that connects your model to
your world, that code tends to compound.
Your custom tools, your data, your off,
your specific context.
The model can't absorb what it can't
see.
So, giving it that is much more valuable
as opposed to compensating for any model
shortcomings today.
And we believe that the ecosystem is
moving in the same direction.
So, we believe that in the near future
every agent every piece of software will
be getting a front door for agents.
And so, the interesting work is no
longer making the model more reliable.
The interesting work is what you put on
the other side of your agent front door
that nobody else can.

[00:21]
Thank you very much for coming to my
talk and for coming to the Code with
Cloud conference. Uh my name is Lucas
and I'll be walking around if you have
any additional questions, definitely
feel free to come say hi. Uh thank you
all very much.
>> [applause]

</details>
