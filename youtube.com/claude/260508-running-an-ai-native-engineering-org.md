---
title: "Running an AI-native engineering org"
channel: claude
url: https://www.youtube.com/watch?v=igO8iyca2_g
youtube_id: igO8iyca2_g
published: 2026-05-08
duration: "28:38"
captions: en-orig
---

# Running an AI-native engineering org

[![Running an AI-native engineering org](https://img.youtube.com/vi/igO8iyca2_g/hqdefault.jpg)](https://www.youtube.com/watch?v=igO8iyca2_g)

<details>
<summary>자막: Running an AI-native engineering org (28:38)</summary>

[00:00]
[music]
>> Hey folks, do y'all hear me okay?
Okay, I I I swear this is not a Claude
Code thing, but do you guys mind if I
take a photo? Cuz cuz Boris and Jared
had their session at 2:00 and I really
thought this was going to be empty. I'm
like, there is just no way people would
still be coming in from that session.
So,
Oh my gosh.
>> [screaming]
>> Thank you, prompt. I promise me and
Boris don't just do selfie words all the
time.
>> [laughter]
>> But good afternoon and thanks for
attending. So, yeah, my name is Fiona
Fung and I lead Claude Code and Cowie
engineering and product. So, I work
really closely with Boris and Cat. And
before Anthropic, I had led and grown
teams at Meta and then also Microsoft.
And so, for today's talk, this is kind
of like overall agenda, but the whole
idea is what are some of the lessons I
learned and helping Claude Code and

[00:01]
Cowie kind of like grow and as we're
building out this team. And kind of like
what things I and it's it's interesting
as lessons I learned even if I think
about my time at Meta or even Microsoft,
but even Anthropic. Like it's funny, I
did this slide deck maybe like a month
ago and also already I've had to change
some of the content cuz for example,
when I started this deck, there were no
routines and that even like that way of
working was different for me.
And so, yeah, like we really want to
like I want to kind of cover five themes
that I've noticed. One which is the
bottlenecks have moved, they've shifted.
And so, when bottlenecks shift, what are
then some of the team norms that we had
to rewrite within the Claude Code team?
I also wanted to share a little bit
about all these team norms we had to
rewrite, how we rolled them out, and
also what are some of the proof as some
of the you know, like some some signals
that I get of well, yeah, we're trending
in the right direction. And it's always
going to be important for me to kind of
look at to see is it still serving us,
trending in the right direction? And
then I'll end it with a few kind of like

[00:02]
questions that I still have for myself,
and then also some suggestions for you
to maybe take an action and embark uh to
your teams to have conversations
together.
So with that, the first section, the
bottlenecks have moved. I call it the
shift. But you'll probably hear me
repeat this kind of subtitle text a lot,
which is what served you prior may not
serve you any longer. And when actually
even when I think about all my
experience, whether it was like at
Anthropic or Meta or Microsoft, the
constant growth mindset is just a muscle
that has served me really well. And
especially right now when the rate of I
don't know if y'all are feeling it, the
rate of change is just a little bit
crazy, right? Like I remember the first
time I started doing some live coding
was last year, and it was still making
some some, you know, bugs that I'm like,
"Ah, why why are you using constants
everywhere? That's not good engineering
practice." And now it's it's, you know,
just become so much more capable. But
that's that's what I I'm seeing as this
interesting shift of when the
bottlenecks moved, how do you think
about adapting uh in terms of everything

[00:03]
else around that bottleneck?
So maybe y'all are feeling this too, but
like for years engineering bandwidth was
the expensive thing. Like coding
throughput was really expensive. And
when you think about all the processes
we have of shipping software, a lot of
it was around Hi, welcome. There's a
chair. Take away those reserved tags.
There's no one sitting.
>> [laughter]
>> And there's another one right here, sir.
Welcome. Um but yeah, like all of that,
like even when you think about how we
used to do planning, like remember we
used to do like waterfall and then
agile, everything was used to be because
engineering bandwidth was really
expensive. Actually, I'll take a little
segue here.
This is not the first time our Like when
you think about our industry, we've
always had to adapt. Like I'm going to
put you all in a time machine. Come back
with me all the way to the year 2000s.
That was when I started my career. I
worked on Visual Studio, and we were
shipping Visual Studio 2005.
And I kid you not, in those days, if
folks remember, we used to ship software

[00:04]
on like CD-ROMs. Before CD-ROMs, it was
actually floppy disk. And so, I still
remember VS 2005, there were really hard
deadlines. We had to hit those deadlines
cuz we had to get the software to the
manufacturing lab to print on the CDs,
to put in the boxes, to ship in the
stores. And so, when you when you even
think about that, when we were able to
distribute software online, that also
changed how we ship software. And so,
that's what I'm finding really
interesting of this this new, you know,
shift that I'm seeing is engineering
bandwidth. It's no longer the expensive
thing.
So, for example, on the Cloud Code team,
for sure, coding is rarely the slow part
anymore.
Um and I would say it's not even that
it's not the slow part, it's just also
the throughput has really, really
increased. So, it's not only like, "Yay,
we're all all getting to build more."
It's just the amount that we're
generating has also changed a lot.
And so, what we saw was, you know, when
your your bottleneck shifts from kind of
the coding and the actual act of typing,
like if you remember, it used to be
writing code was expensive or writing

[00:05]
tests or refactoring. I remember all of
these conversations of, "We have to
schedule some time to do refactoring.
Oh, but we have to do product work, and
this is expensive. When are you going to
find that time to do it?" All of that
has shifted now. That is no longer the
bottleneck. And so, when that happened,
sometimes I notice the bottlenecks end
up shifting towards other areas.
And so, what happened? Like, for
example, verification, review,
cross-functional partners, security.
Because coding is no longer the
bottleneck, and also we're doing so much
more of it, these are some of the new
bottlenecks that we're seeing. So, it's
really always us asking, "Is this code
correct? Who reviews this code?" That's
like probably one of the top questions I
get from all fellow end leaders. Like,
"How are humans keeping up with how you
guys are doing like code reviews.
And interestingly, also how is it
maintained? Because now it is also a lot
easier for us all to generate a lot of
code. So also thinking about that
maintenance cost, too.
So with that, these were some of the

[00:06]
processes that I noticed quietly stops
working. And I love that phrase quietly
stops working cuz I don't know if you
all like a lot of times we all put in
processes hopefully for a reason, right?
Like we're thinking, "Hey, there was a
gap here or we want to improve." But
what I've found over the years is rarely
do processes kill themselves. We tend to
just layer more and more and more
processes on. Like I remember that on
one team, we had so many SLAs. Like
there was a P0 bug SLA, a high pri- like
sub review instead of like Anyways,
there's so many SLAs. After a while I'm
like, "Oh no, we need to stack rank
priorities so that all the engineers
knew which SLA was going to be even more
important." And I remember even at that
time I thought, "Hey, we should start
thinking about what things we should
defrag a little bit." But um yeah, so
these are the processes that might have
served you. Do you remember again is
that line of what may have served you
may not serve you any longer. But like
the planning norms. We used to spend a
lot more time, you know, pre-planning
because coding time was expensive. Uh
code ownership, there used to also be a
lot of questions of who who who wrote

[00:07]
this code? Who owns it? That's a little
bit of an other question now. Uh code
reviews what we'll get into a little
bit.
Team makeup is interesting, too. It's
not only like roles are blurring, right?
Like so between like engineers can also
So now now have AI to help augment
non-engineering roles. My
non-engineering partners are also all
shipping code. So what happens when
roles start blurring and you don't have
those, you know, like the silos anymore?
And then that also goes to knowledge
share. Knowledge sharing and onboarding
and everything is another signal that
we're noticing at Cloud Code how we used
to do things change a little bit, too.
And so, you know, in the first section
we talked about the shift. So, within
the Cloud Code team, what are some of
the norms that we have to rewrite? So, I
want to share some of those with you and
then, you know, hopefully some of them
will resonate with you or you might find
helpful.
And so, number one is code review. Uh
like human judgment of like who actually
needs it and we'll kind of go through

[00:08]
all of these, but you know, like the
onboarding is also changed, how we do
planning, you heard about me talk about
like planning a lot, hiring, especially
with roles blurring and kind of team
makeup how that has changed for us, too.
And also org shape, that's kind of one
of my favorite spicy topics. I'll share
that story with y'all when I start
proposing that at Anthropic. I love my
recruiting partners, they're awesome,
but I remembered, you know, one
recruiting partner really did think I
was crazy. Um so, I want to share that
with y'all, too.
So, how have planning changed? But also
technical debates.
Planning, we do a lot less of it. Like I
would also say and also the timing, I
call it like JIT planning, almost like
JIT compiling because even when I first
joined, I'm like, "Don't we need a
six-month roadmap?" And we, you know, we
put some effort in, we wrote it, it was
pretty good for three months, and then I
came back over the new year and and so
many things had changed already. So, I
realized well, six-month roadmap just
seems like a little bit too long. So,
again, it's how do you make sure you
kind of like do just the right amount in
the right time because again,

[00:09]
prototyping and code generation is just
not the bottleneck that it used to be.
The technical debate one is a fun one,
too.
So, in technical debates, code wins.
I'll share with y'all when I first
joined the Cloud Code team, I wanted to
do a refactoring. I wanted to like get
to learn about the code base. And me and
Boris had a healthy technical debate of,
you know, which which way to go, and I
almost leaned into my old toolbox. I
almost tapped him on the shoulder to go,
"Let's go to that room and have a
whiteboard and we can and I'm like, wait
wait wait wait wait a minute. Nowadays,
I can just generate all the different
options we've been discussing. I
generated three PRs. And the cool part
about that for the technical debate is I
really cared not only about the
implementation of the API, but also the
impact to all the callers into the API.
And so when I can have Claude help me
generate the three different versions,
it allowed us to have a debate of not
only implementation, but also impact to
the colleagues. So I think that's
another really interesting kind of

[00:10]
pivotal change. Um so yeah, like you
know, when building is cheap, arguing
expensive, again, how does that shift
your team norms a bit? I do want to call
out this makes it even more important to
make sure you set up team culture for
how you think about alignment. For
example, what totally won't fly is
because code is, you know, so much
faster for us to generate, it shouldn't
be like the last person who check in
wins, you know, like I'm going to stay
up at 3:00 p.m. to submit this PR. I set
up a routine so that I get the last word
in. So definitely a no-no. That makes it
even more important to make sure you
have good team culture that can have
open, honest technical debates, but also
a good team alignment.
Uh so I talked a lot about kind of what
we reduce in in planning. On Cloud Code,
we definitely have reduced the design
doc before every code ritual. I would
say certain teams and for definitely
certain scenarios it's still really
important to think about design docs,
especially as we're doing like kind of
like async discussions. But on Cloud

[00:11]
Code, most of our discussions is like
instead of a doc, a PR. That's kind of
like one of the word we have of "Hey, we
found an idea, go prototype." That's the
other thing. We don't really do a lot of
product reviews because the landscape is
changing fast. So let's prototype, let's
actually get a lot of internal ants
using it, and I'm really a big fan of
shipping it out to all of you, and then
hearing all the excellent feedback so
that we can really And And again, like
that that has changed our planning
ritual to be a lot less design docs, and
mostly discussions are in PRs or
prototypes.
Um so we reduced that, but what did we
double down on? And I think this is an
area where we actually need to do more
and continue to being better, it's the
verification. Cuz again, it's like the
throughput is different. Um, and there
are new ways to break. So, how can you
scale out? And I call it kind of shift
left. Like in the old days, you would
get code out and and I would love to for
me to find bugs before any of you find
it. And what's better than me finding a
bug is actually what I call shift left,
like more more automation, so we catch
it earlier to the source. So, that is

[00:12]
something that I think we need to
continue to double down on. And the
other thing that's interesting is also
because roles are blurring. For example,
my designers like I would love to have
more confidence that when I checked in
this code, I don't break something. Like
I remember it, I fixed a I fixed a bug
in resume or something and the next day
I was catching up on Boris's, you know,
threads and I saw someone tag him up,
"I'm noticing a bug." I remembered
having that sinking feeling. I don't
know if y'all have ever like
Did I just catch a bug? Like so because
of the throughput like I just really
want to make sure everybody, regardless
of roles, just has a lot higher
confidence um for the change that
they're putting in.
Who made this change? And so my advice
here is again, because a lot all our all
our PRs are assisted by Claude, it's a
little bit of an odd question. And so
for us, what is more helpful than just
that question is what I call like double
clicking into it. Like so in the old
days, when you used to ask, "Who made
this change?" What question are you
really trying to answer? Are you looking
for who caused this regression?
Definitely don't want to blame, but just

[00:13]
want to know who was the last person
that touched this code that might have
caused this break. Or are you looking
for an expert to answer customer
question? Or are you looking to gain
context? So, whatever is that double
click question, also think about is
there a way you can automate. It's
funny, I mentioned that to change this
slide deck. When I started this talk
about a month ago, part of my every
morning is I would, you know, bring up
my desktop code and go into here's a
customer feedback channel and I kind of
want to ask it to summarize and and that
was just a morning ritual I would do
with my morning cup of coffee. Now it's
routines, right? Like I can set that up
and then even better than what I had
done before, which was how I kick it
off. I'll be like, with my morning cup
of coffee, I always get to kind of a
pretty good overview. So that's my point
of like code ownership is a little bit
more fuzzy, but on the flip side, double
click to what question you're really
trying to answer and seeing how Claude
can actually help you with those.
How do you keep up with code reviews? So
I'm really glad if y'all saw uh the
keynote this morning, Kat talked about
it. We definitely leverage heavily

[00:14]
Claude code review. Now what's
interesting is going to be where do you
trust Claude like a lot,
but then where do you still want a
human?
And so for sure like, you know, and
actually Claude also, as Kat showed
y'all the the Claude also does a great
job babysitting PRs. And so we
definitely have Claude handle all the
styling and lint and PR feedback
requests, even like maybe catching some
bugs and fixing them before it even uh
does a full commit. And also uh adding
tests. That's what like really what
we've leaned heavily into Claude for.
But where I still definitely want a
human is that expertise. It's all about
trust but verify. So for example, legal
review, I always definitely want to make
sure I'm getting my legal partner still.
Uh it's you know, like risk tolerance.
So for example, trust boundaries and
security sensitive code, I still want to
make sure I'm pulling in the experts. Um
the other area which which is kind of
fun is also that product sense and
taste. Like I remember one of the hobby
like one of the fun things I like to to

[00:15]
use Claude for is that I like to
decorate Claude for the holidays or the
seasons. And I remember last uh holiday,
I wanted to update Claude in the
terminal to, you know, give him a little
holiday theme. And I asked Claude code
to you turn Claude into a snowman.
Claude wasn't that good at ASCII art in
those days. And I remembered asking,
that's where product sense really comes
in. I asked my design partner, "Hey, can
you review this for me?" And she gave me
such good feedback. She's like, "You
turned Claude into like the Mr. Peanut
character." Cuz I was trying to
make him snow match. I was like, "Okay,
I'm going to do something more simple."
So, Claude was like ice blue with
snowflake, but keep in mind kind of that
product sense as well.
Which leads me to what should my team
makeup be? Because roles are blurring,
Claude is augmenting.
I'll share with you on Claude Code,
there's two profiles for engineers that
I'd really heavily indexed on. One are
like creative builders with product
sense. Usually, you'll see these are,
you know, the dreamers. There will be a
big sense of curiosity. They're really

[00:16]
passionate about, "Oh, here's a problem.
Here's a Maybe I could, you know, ship a
product that solves that problem." But
then there'll be a lot of iteration to
make sure you're delivering a delightful
experience. Um the other one is deep
systems expertise. So, when I first
joined Claude Code team, I noticed
actually we were pretty good with
product generalists and creative folks,
but we were missing folks with like
distributed systems expertise. And when
you're building things like Claude Code
remote to ensure we can run Claude's
everywhere, you really still need um
those expertise. So, I would say, you
know, whichever software engineering
lead you're part of or or supporting,
think about those hard parts of where
you might want to continue to still
double down. But for sure what I index
less on is raw throughput because thanks
to the models, we just saw a lot more uh
efficient.
The cross-functional gaps is another
interesting one. So, for example, I
remember that I wanted to do an update
to how we do survey responses, but I
didn't have a dedicated content designer
to work with me. And I'm a engineer, my
writing skills are quite terrible. I I

[00:17]
struggle to write things in a short and
succinct form. I don't want the surveys
to like, you know, overload you all in
the terminal of cuz every line space is
really important. But that's where
Claude, like in the old days I would be,
"Who is a group of content designer I
can work with?" And I can can of changes
back and forth. But now Claude has
really helped me to augment that role
and was a really good content design
partner for me to kind of like make sure
the verbage is is good and succinct. And
on the flip side, like I say a PM our PM
code a lot, which is really fun to see.
So again, like I I would say with Claude
like you have non-traditional coders now
being able to do more engineering, but
you also have engineers that we can also
now lean in to do things that was
traditionally, you know, like not on the
technical side but more of where the
content or design. So it's very
interesting. I found that Claude and AI
has really augmented roles kind of like
all around.
This was a spicy one. Uh
so I'm definitely like I remember when I
first joined Claude Code everyone's

[00:18]
like, "Okay, you're going to grow the
team by certain amount." and I could
tell recruiters were still using the
typical, you know, 10 ICs to one manager
and then how do you start think about
nesting? Um I really have leaned into
keeping it really scrappy. And actually
maybe I would step back to whether it's
at Anthropic or Meta or Microsoft,
whether it was like Visual Studio or
Facebook Marketplace or AR/VR devices or
Claude, like what I have found to really
help me ship great product is heavy
heavy heavy dogfooding. Especially for
leaders where nowadays it's actually
fun. I can still be in the code, but for
a while it wasn't. And when you can't
get your hands on the code, I would
always make sure I would make your time
so that I'm actually using my product
days in days out. And so that's why I
wanted every manager in Claude Code to
start out as an IC first. And also like
earn some street cred with the team and
and really learn how to be an effective
engineer.
Uh and and then I really structured the
org to be as flat as possible cuz I want
us to be super agile. This was just my
my recruiters had some concerns cuz I

[00:19]
remember they said, "You want to hire
managers and they will start as an IC
first. No manager would be interested in
that." I'm like, "Well, this is what
dogfooding on the Claude Code team's
about. And this is what I expect. And if
someone's not interested, it's better
for us to do uh earlier separation. But
also again, this is like there's no way
I would have been able to ramp or be
able to do code cuz my time is, you
know, there's just a lot of context
switching without Claude. And so for
those of you in the room who are
managers, I really, you know, like
encourage y'all to kind of like lean in.
It's I'll I'll be honest for for a long
time at Meta, I would still try every
year to do one PR a year just to but the
the code the the workflows would always
change. Like I all the internal tools,
like by the time I learn one command, it
would have changed. Nowadays, I don't
even remember get commands. I just
always ask Claude to to help me out out
with all of that.
Now with sharing, what becomes your new
source of truth?
So for example, on our team on Claude
Code, the code is the source of truth.

[00:20]
That's why I would go back to when I'm
like answering customer requests. I just
have my desktop Claude with desktop
Claude Code and then I have all my, you
know, like local repository so actually
answer a lot of customer questions. So
for us, just having that code base be
the source of truth also like prevents
some of the lag that you might have had
before of how to keep up the
documentation, you know, correct with
the code. But I would say this is where
it's like do what makes sense for your
team. So for example, if you still have
a lot of really good specs, check those
into the repositories and then have
Claude lean in to help, you know, like
hey, you know, like take a look at how
verify my code execution so matches what
I expect on the spec.
And so how did we roll it out? Cuz these
were like I had just gone through some
of the norms that we had changed. And I
think it's interesting, there's a blend
of what do we kind of like mandate as
team norms? Like make sure you're
gaining alignment with the team. And
then where do I really enable each, you
know, like we have pods within Claude
Code. Want to make sure I enable each
pod to do what makes sense for them as

[00:21]
well.
So in terms of the balance, in terms of
forcing function, it's align with the
teams on the must do. So, these are a
few of the core Claude code team
principles that we really live and
breathe. And by the way, if you remember
again, I I'll go back to that growth
mindset and always think about something
still serving you. We keep these up to
date. So, every few months, we'll be
like, "Hey, is this still having, you
know, the same effect or serving the
purpose that we wanted when we started
it?" So, for example, and I should
replace this slide. It's not every
engineer uses Claude code. You know,
that's obvious. It's actually every
Claude code team member, including
cross-functional partners. And actually,
we all use co-work quite a bit, too.
Uh Claudify everything you can. This is
one thing where we're like, "You know
what's better than one of us doing it?
Having Claude." So, always think about
Is there some way for you to automate,
whether it's verification, more shift
left, but always be thinking what you're
doing something right now? Is there some
way that Claude could actually help you
do it?
And the last one's my favorite, explicit
permission to kill old processes. Cuz

[00:22]
again, processes will kill themselves.
But as your supporting teams is really
important to always get that fast
feedback for your team of what are the
things that, you know, like are we spend
We're spending a lot of I'm actually I
remember when I first joined Claude
code, we used to do stand-ups. And then
the team got a little bit big, so then
we had a spreadsheet where we would all
put up our, you know, like weekly
process progress. And then I was like,
"Oh, wait, we should just do a
skill, right? like a a stand-up script.
So, then we can just run Claude and all
of us can always be very be much more
kept aware of what everybody else is
doing." So, that's just something
another example of one day I remember
spreadsheet Wait, "Does this still make
sense anymore?" So, always question and
always look to defrag and kill old
processes.
What I want to make sure that I leave a
lot of room for pods to adapt. It's For
each team really has a lot of high
agency for how, you know, they do triage
or leverage Claude to do triage, any
planning rituals or stand-ups, how they
think about on-calls, and also which
workflows to Claudify first. So, we

[00:23]
don't usually mandate thou shalt
automate this. We have some suggestions
and learnings, but always give room to
your team, especially they may be, you
know, touching on different problem
areas.
So, if I zoom out, what were the three
things I prioritize on, you know, I I
when I joined Cloud Code that I felt has
to make the biggest difference? Keeping
the team as flat as possible.
Um like managers release a pop pods of
work, but really keep it agile. So, for
example, on on Cloud Code and co-work,
we have one overall team mission. Cuz
sometimes when you start creating pods,
each pod then wants maybe to set up
their own mission, and then anytime you
have to shift, it might be take a lot of
time to to walk people through that, but
it's really as flat as you can. I felt
that served us really well.
The cloudify everything better than you
doing it. I see how Cloud can help you.
It really frees us up to do more of the
harder work. And again, the processes,
they do pile on. So, I encourage you to
kind of like work with your team to see
what are the processes that actually you

[00:24]
should be able to let go.
So, does it actually work?
I can't go into the explicit numbers,
but I think these are three general kind
of metrics that you can look at as
you're rolling out, you know, changes on
your team that might start steering you
to yeah, this seems like it's kind of uh
starting to be successful. The
onboarding ramp-up time that has
dramatically reduced. Uh so, that's an
interesting thing like like how soon an
engineer or a designer or, you know,
like a PM can start being effective on
your team.
Uh the PR cycle time shortening. I think
this one's interesting to double click
into a bit cuz it's it might actually
help you identify a gap that's not just
in terms of lack of AI adoption, but
where the rest of the pipeline might be
struggling to scale. So, for example,
again, as as we're now like, you know,
just putting in some through so much
more code, sometimes a product
infrastructure can build and CI still
keep up with the amount uh that
engineers are checking in.
Uh so, both of those should go down, but
then what should go up a little bit is

[00:25]
cloud-assisted commit. For example, for
us, it's by default every commit is
cloud-assisted. I don't think I've seen
a non-cloud-assisted commit probably in
the last 4 months or so. Um, but
hopefully these three things are are
kind of like metrics that you can kind
of take a look at at your team and see
how it resonates. I would also say
though, um, outside of just number of
commit, also think about the end goal.
Like if you zoom out,
what is the product that you're trying
to make more delightful for users? Or
what is the problem you're trying to
solve? Cuz sometimes you see it on all
the headlines of this company said X
percent of code is now generated by AI.
I think throughput is great, but really
think about how you measure what it is
that you're actually really trying to
solve. Like for example, we really want
to make sure we're keeping an eye on
quality and reliability, so those are
some of the things that we're paying
more attention to as well.
Okay, so the my last section is to audit
your own effort. I'll share with you
transparently, actually, I still have a
couple of questions that I'm still
asking myself. Um, the iOS and Android

[00:26]
org is a very interesting one. Like when
engineers can now more efficiently kind
of flex across different mobile
platforms, does a more traditional way
of, you know, uh, having an iOS team and
an Android team still make sense? That's
something that I'm still kind of
thinking through. How much do you push
that fully automated review? Again, like
when do you kind of strike that balance
between fast enough and we lost
something important? It goes back to the
trust but verify. And what's interesting
is you even might have heard today in
earlier during Danella's talk, the model
capabilities do keep improving. So also,
even if you might need to do more verify
than than trust for a certain section of
work, that might also change with the
next model. So it's why it's always
important to re-evaluate. And roles are
blurring, so how do you make sure that
everybody feels equally uh, productive?
So if I were to leave you with one, you
know, thing to take back of is, you
know, pick your noisiest workflow. And
by noisiest workflow, it could be most

[00:27]
expensive, what's something that, you
know, what you yourself might be
dreading, or even your team might not
really look forward to it. And ask, is
it still really serving what's the
purpose of there? Like, actually, I'll
share another funny story. There was a
team I was on where we used to have this
weekly review. It's a very expensive
review, like 50 people, you know, in
this large room. And then I noticed
everybody's on their laptops. Except for
when it's their time to give status
report, and then they they pop their
head up, say the status, and then go
back down. And I'm like, this is a very
expensive meeting. And I just asked that
simple question of why are we having it?
And just that one question, everybody's
like, yeah, it's true. And so we
canceled it. So, that's why it's always
important to to think. And And so, yeah,
like I I figured this might be something
fun for you to take back and look and
see what's one piece of workflow that
you might consider, can you either
automate, or maybe even is it still, you
know, proving is it still serving its
intended purpose.
So, with that, that's the end of our
talk. I'm like, thank you.

[00:28]
>> [applause]
>> Thank you.
Thank um thanks a lot for thanks a lot
for attending. I really, really for sure
thought this room was going to be empty.
So, thanks for not having by myself. And
I'm around here today and tomorrow. So,
if you have any questions or want to
chat more, feel free to introduce
yourself. I'm happy to chat.
Thank you.

</details>
