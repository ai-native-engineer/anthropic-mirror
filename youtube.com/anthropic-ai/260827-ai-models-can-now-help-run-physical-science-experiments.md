---
title: "AI models can now help run physical science experiments"
channel: anthropic-ai
url: https://www.youtube.com/watch?v=P1zBiAQU1IA
youtube_id: P1zBiAQU1IA
published: 2026-08-27
duration: "11:10"
captions: en
---

# AI models can now help run physical science experiments

[![AI models can now help run physical science experiments](https://img.youtube.com/vi/P1zBiAQU1IA/hqdefault.jpg)](https://www.youtube.com/watch?v=P1zBiAQU1IA)

<details>
<summary>자막: AI models can now help run physical science experiments (11:10)</summary>

[00:00]
Scientists come up with theories
about how the world works.
But just coming up with a
theory isn't good enough.
And so we have to build experiments,
physical measurement devices,
to test our theories.
That process of building the experiment
takes maybe 80% of a scientist's time.
They're building devices,
they're setting things up,
they're debugging hardware,
debugging software.
These are things that aren't
really related to doing
science, but it's what
makes science actually work.
When I joined Anthropic, I had a
vision for using AI to accelerate
running scientific experiments,
But I thought it was a pie in the
sky, crazy idea, until I saw the
work of neuroscientist Arco Bast,

[00:01]
who studies how memories are
formed in the brain in real time.
I'm in the lab for a year now, and I'm
setting up a very difficult experiment.
So the stuff is over here.
That's a custom -built microscope.
You see the laser beam in here.
That's actually what's happening
when you're imaging in the
brain, that you have this laser
beam that scans and moves.
It's really, really important that
everything is precisely aligned.
There are so many components,
and I just want to
have them talk to each
other in a seamless way.
The problem is that each device has
a different language that it speaks,
and getting the devices to talk to each
other in their languages is very difficult.
But Arco figured out a way to do this
that could work between any two devices.

[00:02]
Set beam one to 50% power.
Yeah, we got a beam.
And the beam is there.
When I was standing in that
room watching him run his
experiment, I had kind of
an epiphany in that moment.
what he had built wasn't
just applicable to this lab.
This idea could be used to have AI run
any science experiment in the world.
I was basically speechless.
Is this ours? I believe
everything on the table is ours.
We've got to start putting this together.
So Arco and I started working together
to create a general way for AI
to interact with devices, which we're
calling Model Hardware Standard.
Look, with a very sophisticated
microscope, and this microscope has
so many degrees of freedom, you
should see it moving now, right?
Yay, moved. It moved.

[00:03]
It did. Yes, I think
everything looks good.
Okay. Okay.
Once we had a working prototype,
we had to test this on other
devices to see how it worked
beyond just neuroscience.
Go to the left boundary first.
One of the first things that I did was
to define the safe range of this arm.
How far is it allowed
to go out of the table?
And so if we ask Claude to maybe
intentionally move out of the safety range,
you can kind of see that this motion,
this movement was refused by MHS.
Oh, that's incredible. Can
it grab anything right now?
Oh, great question.
We've never asked Claude
to do this from scratch,
and so I have no idea what
it'll cook up for us.
There are turns that I need to... Oh.

[00:04]
Wow. Oh.
Wait, wait, wait, what?
What?
Oh my God.
Okay, that was sick.
That was really cool.
The mere fact that I was able
to build this from scratch
today and it achieved it
in a matter of minutes.
That's insane.
And of course, we also have to
work with the manufacturers
and the vendors who build the devices.
So we started working with
Danaher to get Claude
to connect with their Leica microscope.
We have to remind ourselves
that Claude has never
seen anything related to
this application before.
It will make mistakes. So we can think
about this as an iterative process.
You have to imagine that I as a scientist
spent weeks making this sample alive

[00:05]
to this point of view and I spent
thousands of dollars in ingredients.
I see. Okay. If you break
them, your experiment is gone.
You can even see how it's thinking.
It's now brightly trying to change settings
of the microscope to get an image.
and I think we need to help it.
What's interesting here is
you can see that when I asked
it to switch to a higher
magnification, it is very aware
of going to a higher mag can
crash it into the sample.
It's amazing.
It knows how to operate a microscope.
Do you think we're at a point
now, I could enter a bunch
of commands and get a focused
image and query what is the
image and add false color
and all that type of stuff?
We should try it.

[00:06]
That's incredible.
That's awesome. What is the
different colors right now?
Could we ask it? Magenta red slash pink.
Lignified cell walls.
These things are the cell
walls. That's great.
What we accomplished in a
day is pretty transformative.
Claude walked in. We told him nothing.
He's just trying to figure it out.
Tomorrow I think we should try to give
it, you know, treat it as a colleague.
Oh, there's a lot going on in there.
Let's say a scientist
wanted to look at this,
they would have to sit and wait
and keep tracking it. Correct.
For like hours. Correct.
Yeah, I had a nice one, but it swam away.
I'm wondering if Claude can write
a program that can track that.

[00:07]
Claude is almost done with the
initial script to do the tracking.
That's off. Oh, shoot.
Yeah.
Yeah, damn.
I actually think it needs to build
a UI so we can see what it is doing
because just running a script in
the background is not acceptable.
This looks good. Yo, that's awesome.
It's doing what it should. Yeah, it is.
It's tracking. It's tracking.
Three minutes, four minutes.
It's been tracking for a few minutes.
No way. We've just been watching it.
Chasing algae.
Amazing that we managed that.
It managed it.
This is a prototyping system
somehow, or a very dynamic
system where you can create
something very quickly.
Maybe it's even good enough
for some science applications.
The PhD can do his PhD work
faster because he doesn't

[00:08]
need to spend two years to get it
running. He only needs two months.
And then he can focus on biological
questions, which is what our goal is.
I still can't believe it.
We're very impressed.
I think Model Hardware Standard opens the
door for a lot of new types of science.
The obvious example is in pharmaceuticals.
Here at Genentech, we make
medicines for patients
with serious and even life
-threatening diseases.
It takes many, many
iterations to make a drug.
We will test thousands or even hundreds
of thousands or even millions of
molecules to find the right molecule
that will really help patients.
So we are going to start an
experiment where Claude will

[00:09]
run a series of operations
and then interpret the data.
If you aspirate out of
a well that has bubbles,
you're not getting the
correct transfer amount.
If we were trying to aspirate
out of this, we're going
to get the proper amounts in
the wells with no bubbles
and then improper amounts in
the ones with the bubbles.
With Claude, we could potentially
check during the production
runs for these bubbles to
see if they are happening,
and hopefully it has the context
and knowledge to make adjustments.
Claude will do some execution,
take the reading and then
change the parameters of the
execution slightly to see if
it can improve the experiment
overall in a closed loop.
Speeding up this loop means
we are just able to make more
shots on the goal and can
get to the answers faster.
This is fewer bubbles.

[00:10]
It's got bubbles in two, but not the rest.
So this is better.
This is really the first time in
history where we are enabling
AI to interact with the physical
world in drug discovery.
It's definitely historic, yeah.
I think it's very difficult for us
to predict how AI and model hardware
standard will affect the world
30, 50 years in the future.
These are the best moments
when there's something
I couldn't do before and now I can do it.
Something I couldn't see before and
now I can see it. That's the drive.
I want to understand things we
don't understand right now.
Imagine what we'll see in drug
development, in quantum computing,
in nuclear fusion, in big
technologies that could change the

[00:11]
world when scientists have
access to this technology.

</details>
