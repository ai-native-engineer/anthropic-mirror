---
title: "How AirOps chases friction to build AI products with Claude"
channel: claude
url: https://www.youtube.com/watch?v=M5uwBawBDpw
youtube_id: M5uwBawBDpw
published: 2026-05-22
duration: "26:47"
---

# How AirOps chases friction to build AI products with Claude

[![How AirOps chases friction to build AI products with Claude](https://img.youtube.com/vi/M5uwBawBDpw/hqdefault.jpg)](https://www.youtube.com/watch?v=M5uwBawBDpw)

<details>
<summary>자막: How AirOps chases friction to build AI products with Claude (26:47)</summary>

[00:00]
[music]
>> Hey, how's it going everyone? Um I'm
Dylan. I work on the product team at
AirOps. And yeah, excited to walk you
through uh how you know, tell us how
AirOps chases friction
um with building AI products with
Claude. And I guess the main really big
takeaway I want you guys to come away
with is building agents um and just
making agents accessible is honestly
really hard problem. Um I guess like
with developers it's a bit easier.
People are used to
um kind of all these different concepts,
but when you try to make these
accessible to, you know, personas like
marketers, there are a lot of friction
points. And going to talk through some
of the friction points that we um have
seen and battled with.

[00:01]
So, just to start off, quick intro of
who we are at AirOps. Um we are a growth
marketing um platform for AI search. And
AI search for you guys is kind of like
SEO but for engines like ChatGPT,
Gemini, Claude. You know, buyers are
asking on Claude different, you know,
questions of, "Hey, I want to buy like
these pair of sunglasses. You know, how
do you know and how are you making sure
that you are showing up for these
searches?" So, we help brands see how
they're appearing in search, um identify
gaps, take action on those gaps, whether
that be, you know, creating content,
refreshing content, um and then being
able to measure the impact of whether or
not, you know, the actions that they're
taking actually worked.
And so, quick agenda, um I'm just going
to walk through real quickly how we got
here, kind of our approach um for
agents, um a quick just run through of
what we just launched last week with
AirOps Next, um and then two friction
points that we really focus and dial in
on for our launch
um when it comes to making and giving

[00:02]
people the power of Claude
and making that super accessible.
And then closing with a couple of other
friction points that we're really
looking at for our next
you know come next act.
So how we got here?
AirOps used to be or still is but we
were mainly focused on
orchestrating content through a
traditional workflow builder so
node-based style kind of like an N A N A
N
where you can drag and drop these
different nodes, you can
orchestrate different variables and how
things flow through this you know
elaborate workflow. And with a workflow
builder style and especially with our
core customer and audience being
marketers,
you would hit this complexity ceiling
where you're trying to teach a content
marketer what liquid text is, what JSON
is and all these you know different
concepts
and they also had this short shelf life
which
as new models came out, you know, Claude
would release
you know, Opus 46, 47, you know, it
keeps on going. You would have to update

[00:03]
these different steps. It changes the
way that you're building this workflow
so customers are constantly having to go
and update this workflow they just spent
so much time in building
and also just if they update a step in
like step one, they don't realize that
variables and outputs are referenced in
step 20 so there's there's a bunch of
the complexity and this it was really
brutal.
And scaling enterprise use cases
obviously then required someone
technical to help really guide through
this workflow creating process. So our
goal was to really lower this barrier to
entry for
content marketers to build and ship you
know, their ideas and the way they want
to create content. And also while still
maintaining
that quality bar which
is a very big focus for them because of
course brands don't want to just be
pumping you know, AI slop out and having
governance around keeping those
enterprise standards.
So this is a quick just preview of Well,
not preview, but a look at what our
workflow studio looked like. This use
case was actually to create a content

[00:04]
brief with internal links. So, as you
can see, it's it gets kind of gnarly in
there.
Um just for something that this seemed
pretty simple. Uh it just goes to show
like how
much thought goes into a lot of these
workflows and the way that they want to
create and, you know, orchestrate
content. So, how do How can we take
this,
you know, kind of structure and create
an agent experience while still
harnessing, you know, the way that we
use cloud code and these other uh agent
tools.
So, I think the first really breaking
point when we decided to invest uh
heavier into agents was really with the
lost the with the release of Opus 4.5. I
think that's when a lot of people
started to see um
really how smart the models were in tool
calling, being able to follow
instructions,
um
to uh in all in a way that, you know,
they weren't breaking, you know, the
standards that they were setting for it.
And for us, we at the same time we're
trying to make building easier. And one
of the ways that we do that, and I'll
I'll dive more into it a bit later, is
through kind of this document-based

[00:05]
style builder. And the first thing that
we tried doing was actually taking this
kind of like Google Doc in a way and
with an LLM compiling a workflow in the
background, which was, you know, an
interesting idea. It was like a bit
brittle, like there's a lot of, you
know, error points that can happen
there, trying to turn like this
non-deterministic um you know, kind of
instructions and making this actual
workflow.
Uh then what after that was then, you
know, using a traditional agent
orchestration framework um
where you're, you know, kind of defining
these nodes, you're letting an LLM
decide different um
decision points. And we got to a point
where we were getting pretty good
outputs, but with those traditional
frameworks, they honestly are like
pretty brittle. If I ever want to change
the way I want to orchestrate different
sub-agents, um Um, basically have to
make code changes, right? Like I
actually have to go and change the way
I'm routing these different nodes and
steps together.
And that's when we really decided to,
you know, invest heavier into the Cloud
Agent SDK where
it's honestly pretty pretty awesome that

[00:06]
you can kind of orchestrate agents just
through markdown files and provide
skills um, in different contexts really
just by manipulating this environment
and harness rather than actually like,
you know, doing that programmatically
programmatically through
um,
you know,
a traditional agent framework. So,
that's what kind of led to our launch
which we just had last week with AirOps
next. And briefly just to run through
exactly what did what did we exactly
launch? Um, the first one was Quill
which was kind of our our branding of
our agent captain for content marketers.
Um, Quill had access to all the data
that we provide to teams, um, whether
that be AI search data, the brand
context and brand kit which houses like
literally everything about a brand. So,
you know,
you know, Quill is following the
instructions of how content should be
created.
And um, just making it easier throughout
the UI to get people from insights they
see in the dashboards to actual actions.
Um, being able to take the findings and
gaps and get to that in the very next
step.

[00:07]
The next one is playbooks. So, playbooks
is basically our new building
experience. Um,
and for all you like developers out
there it's
pretty much like a skill. That's very
much like what we grounded in is like
how can we
make skills accessible and marketers are
all like used to the kind of document
based style. Um, but we just allowed for
like collaboration on these playbooks
slash skills and also uh, governance and
versioning. So, you know, you'll have
people with, you know, 10 different
versions of this playbook of uh, how do
I want to create this this piece of
content?
And just real quick just results that
we've seen from customers. Um, we did,
you know, case study with Parallel. We
helped them produce and create content
and they saw a 130% increase in citation
rate, uh, 42% increase in share of
voice, and they were able to go live in
1 week, which for us is a huge
accomplishment just because
traditionally, especially because we
work with these enterprise customers,
it usually takes around a month, at
least with like the workflow builder of
constant feedback going back and forth,

[00:08]
like "Hey, this is, you know, not really
how I want to be speaking in my in my
blog.
Um
you know, citations that are like kind
of being hallucinated or aren't right.
They're not These are other citations
that I want to use for this piece of
content." So,
it was really incredible to be able to
get to um that acceptance criteria in
such a short amount of time.
And other just like quick customer
quotes, too. Um
incredible to see how Agents has moved
what really like LLMs can do and how
marketers are viewing using, you know,
these more objective workflows. Um you
know, Animal saying it felt more like a
mid-level strategist for their team. And
um at Rock Content, being able to focus
on off-boarding a lot of the tedious
tasks and really focusing on like where
does my expertise come in and being able
to add that value to the agent while
it's creating that content and um
feeding that unique context.
So, we were able to really accomplish
this by focusing on two main friction

[00:09]
points. So,
when building and trying to bring
high-quality Agents to these more, you
know, highly professional and enterprise
use cases, um we really had to focus on
how do we fit into the actual workflow
of these content marketers? And, you
know, how do we make sure that we ensure
uh quality outputs through the way that
we're building our harness and
orchestrating our harness?
So, the first one um friction point I
want to talk through is uh I I have it
saying like endless use cases forces
intentionality. And I think a lot of us
have
probably been there, too, when we first
started using cloud code or using an
agent and we're like, this thing is like
really powerful. Like I can do a ton of
different things. You're like, it's
really easy to start sprawling into this
spiral of
um
yeah, just like there's so many
different use cases and I think and not
only on like the product engineering
side, but also for customers,
how do we be very intentional about
what's the actual like problem that
we're trying to solve here and how do we

[00:10]
really force it and understand like what
is
you know, this workflow that we're
trying to solve for people. So
um kind of like in my head now I have
this like like mini like Steve Ballmer
head just going like marketers,
marketers, marketers, you know, just
like really
trying to focus on who is like my
customer in this use case so that I want
to tackle.
Um and just a quick glimpse into what
does like this workflow look like for a
content marketer. This is one example
use case for content creation where
they'll discover
um what do they want to create on,
they'll research of the specific topic
that they want to make sure that they're
ranking in AI search or traditional
search for, they'll draft a brief, draft
the article, and then add any sort of
like internal linking and best practices
when it comes to SEO and AEO. And
throughout this whole process, there are
different human review points. Um
human review comes up a ton in human
loop comes up a ton in content
marketing, uh especially just with
when you're being cognizant about the

[00:11]
content that you're pushing out. You
really want to make sure that it is
adhering to the way that your brand
talks to the information that you're
serving out in the internet um and just
giving you the best shot of also being
surfaced um within
kind of like generative AI search.
So, that whole process kind of led us to
focus on two parts when it comes to the
most I got these are kind of like the
two most important parts we saw with the
content marketing flow.
One is having a document based kind of
like IDE, which again it like our
playbook view.
We wanted uh you know, marketers are
super familiar with documents. They are
used to Google Docs. Um they've probably
been working with Docs for for years and
ages, even before like technology like
you have this piece of paper that you're
kind of defining how you want to do
something. So, making that familiar
versus, you know, this node-based
workflow builder. Um transparency was
also really important. One thing that
users actually really liked about the
workflow builder was that they could
actually see what tools were being used
at each step. So, how do you still have

[00:12]
a document but at the same time
when I read through, I can understand
like this this is the exact tool that
I'm using at this instant. Um this is
the type of context I'm feeding at this
point. Um I'm just being transparent
around that. And that kind of goes hand
in hand with control as well. How can I
make sure that I'm still in control of
this, you know, set of instructions or
uh workflow that I'm building?
Um especially now that it is really like
not as like deterministic because it is
like a document. So, um those are three
areas that we that we focused on.
And then, again, on enforcing human
review. How can we bring governance,
configurability, accountability into an
agentic workflow, which I think is
pretty unique for us, and I don't think
um a lot of
brands like kind of like tackle like
that problem. I think a lot of it is
like with agents, also with coding is
kind of let it go. It will it will
finish what's done with, and human
review in that instance with coding is
usually like with PR reviews after it's
literally finished the whole job. It's
rarely ever like while it's going

[00:13]
through the actual, you know, coding
process, it'll
you know, kind of like ask for feedback
of taste in in different areas. So, um
that was like another area that we that
we really focused on.
And with that, I actually want to jump
into a quick uh just like demo of what
this looks like within
um within AirOps.
So,
yeah, the first thing I want to cover is
our playbook. And again, it's kind of
like this skill, this natural language
builder where I can go in and either
like type in like with a slash command
and you know, define different inputs,
different outputs, and also all these
different tools that, you know, content
marketers can use and that they're super
used to using. And with it when it comes
to tools as well, you can add any MCP.
So, there's other outside connectors
that you usually use, you can use those
and access them.
Um we also have the ability to schedule
different triggers. So, this gives this
kind of like always-on skill or playbook
or agent that, you know, can do the

[00:14]
certain action at either a scheduled
cadence, based off webhooks. Um we also
have monitor which we've um kind of like
partnered with like uh parallel when it
comes to just being able to put a query
in I like saying, you know, watch the
internet in a way. So, when certain
things happen,
um
it would trigger off this playbook to
then run. And then the last one is uh AO
insights. So, whenever a metric drops,
let's say like my
citation rate dropped in the last um
like last week, that it would trigger
off one of these playbooks. It can go
and like do this research and come back
to me of, "Hey, like this is the reason
why um this happened."
And as I jump through into this kind of
process of, you know, someone basically
create this SOP of how they want to
create this blog,
uh if I come to the
outline section,
we enforce human review by adding the
ability to assign different users at the
end of each section.
So,

[00:15]
as it as, you know,
the agent goes through this whole
playbook, it'll come to this section
step and decide to I think we have a
tool in the background that will then
like fire off. And basically, since I'm
assigned, I'm the only person that can
actually unblock this agent. Other
people can still leave like comments on
the outputs and artifacts and different
feedback, but I'm kind of like this
gatekeeper now that um
has to review this piece of content and
we're trying to we do that to ensure
like that governance.
And what that actually looks like and
how that surface to users, one way is
through our inbox. So, we have an we
have an inbox within AirOps where every
single time human review happens or
different opportunities are surfaced,
users can actually come in here and see
those directly. So, I can, you know,
click on one of these um items, it will
open up our
basically like agent runs on the right
side is basically this agent like
running through its whole process. I can
kind of see its thought traces. On the
left side, all the different, you know,
outputs and artifacts that are, you
know, one defined by me through that

[00:16]
playbook. And I can then either, you
know, edit this existing document, leave
certain comments, and then, you know,
kind of kick it off and approve it.
The other way that we also surface this
governance and human review is through
our grid.
So, our grid is our way of orchestrating
content or orchestrating
basically content at scale. So, in this
specific example, I'm just kind of
showing um like the way that you can
actually collaborate with these. So,
Augustine is also in this document with
me. Um I'm able to edit it, also leave
human review. If I close this out, I can
see within the grid all these different
um
you know, kind of outputs that are that
are running. We're basically kind of
like running uh skills at scale where
each one of these rows is a specific job
that I want to accomplish and I'm
running that playbook. Um and I can also
then see like human review at scale and
click in these different uh cells to
um then leave like my feedback and
ensure that, you know,

[00:17]
all this content's talking in my right
tone of tone of voice.
Uh
awesome. The second friction point I
want to talk about was
with agents, um the biggest worry is
around consistency, especially when
you're coming from this workflow base.
So, how you know, how did we tackle
going about producing quality outputs?
Um how do we, you know, make sure that
customers are also seeing that and and,
you know, being aligned to that as well.
One of um the ways that we visualize
this is actually like this this graphic
here was um
created in in use and reference by our
VP of sales, which is like funny enough
is actually like one of the best
explanations I feel like I've seen seen
of harness engineering. Um you know, on
the product side we we tried a couple of
times, but it's just funny like from,
you know, the go-to-market side it was
the best way that we've been able to
explain this where um you kind of have
this car where you then have an engine,
the model obviously being, you know,
Claude, Opus, or Sonnet, whatever engine

[00:18]
that you want to pick for that. And
everything else that goes around that,
everything else that you build on top of
it is super important in terms of
creating a super great agent. So, the
two that I want to focus on and the one
that we focused on the most was around
tools and the way that we were
orchestrating context.
And, you know, the Claude agent SDK and
also Claude managed agents API have been
super helpful in terms of being able to
iterate on this quickly. Um
and just making sure that we're like
kind of like programmatically setting
these different um sub-agents. And yeah,
they they've been like super
instrumental in terms of us getting to a
quality uh output.
So, the first one I want to cover is
around tools and
basically the background on tools are
you could give an agent a bunch of
primitive tools. So, in this specific
example, what we were always trying to
accomplish with Claude and our agent was

[00:19]
helping um Claude understand what is
wrong with a page on my website.
We have different tools like access to
uh you know, traffic data, citation
data,
um scrapers so I can find like similar
competitor pages and we started off like
honestly with a skill of a here's like
here's the way of dissecting whether or
not a page is losing, what's wrong with
a specific page, are like the schemas
off, how's it compared to competitor
pages and
they'll kind of go on like these like
safari trips and it's honestly like a
bit like token inefficient. So, one
thing that we want to focus on is how
can we create specialized tools of
jobs that Claude does that we know are
is going to do like over and over again
and how can we just make that a bit more
deterministic where you know, Claude can
then put a URL and immediately spit out
everything about that page as well as
different structured, you know, content
gaps
versus like other similar pages in that
in that space as well as what should be
my target keywords and my target prompts
for it.

[00:20]
The second tool that we made in just
like a workflow that we saw that was
super common with content marketers was
our page versus tool which was
essentially being able to benchmark my
page against, you know, top ranking
pages in that space
and finding what exactly is behind those
pages and how can I, you know,
how can I close those gaps? So, this is
just like a really simple way of
getting context efficiently. It's kind
of like a code mode in a way. I don't
know that's been, you know, something
that's been popular nowadays is being
able to be more programmatic in terms of
how we're fetching context versus kind
of like looping through these different,
you know, tool calls. It's like can I
actually just like produce code that
will fetch exactly what I need
in, you know, one loop.
The second one is through sub agents.
Sub agents have definitely been
instrumental and crucial in terms of
getting to that quality of output. Um in
general, like what we tell users to with
playbooks and honestly when you're first
creating your agent harness is that you

[00:21]
actually just start off with, you know,
Claude itself and just have it go
through its own tool calls and really
not trying to make it too complex in all
the context you're trying to, you know,
give to it. So, that's that's where we
start off with and we were reaching a
couple of
um
kind of like air spots when it came to
the quality of the outputs we're
getting. So,
what we did was decide to add on like
over time certain sub-agents. The first
one was a compliance check. So, being
able to just make sure that we're not
like kind of polluting that main context
window just because context are honestly
is like still a huge problem and will
probably continue to be a problem when
it comes to like what are, you know, the
tokens and text that you're attending
to.
Um so, being able to spin off the
sub-agent that will go through and have
everything that needs to know about my
brand and whether or not the content
that I just produced is following those
rules. It'll, you know, come back with a
score whether or not it adhered to them,
what were the things wrong with it, and
then the agent can then take that
feedback and then kind of make edits.
The second one we did was around

[00:22]
writing.
Um we first again like tried just using
like the regular Claude, you know,
harness to actually write the content,
but we found that it was better to spin
off a sub-agent with its own very
focused context window to focus solely
on just writing that piece of content.
Um so, it's not distracted by any of the
research that was created um or any of
maybe like old compliance checks um and
just being able to like very focused in
on that one job.
The next one is um a brand kit
sub-agent. So, again like brand kit for
us is basically just like kind of a
knowledge base or context layer of
everything you need to know about a
brand. And this is something that we
kick off actually at the beginning of
all of our runs where we have a um brand
kit sub-agent that will go and fetch all
of the relevant context it needs and
then stores it as like an internal
artifact. So, then throughout the whole
process
um our main agent loop can then
reference those artifacts versus having
to like use tools in our MCP to refetch
like that context cuz then what happens
is
um in different sub-agents you might

[00:23]
actually have different brand context
that was fetched over time. So, just
being able to fetch that up front, store
as an artifact, and then just redirect
the agent to always be referencing
um that same artifact.
And then finally, um just still being
able to add custom ones. This is more
more for us like internal
um tool where like some of our like
solutions architect who work for our
customers can spin off different
sub-agents when when needed. Um and just
really helps with
>> [snorts]
>> just maintaining that context. I think
that's
definitely been the biggest learning is
although like context windows do
continue to grow, um you know, you have
like a million context window with um
with Opus 4.7, but just still being
really cognizant that just because it
is, you know, larger doesn't mean that
you should be like using the whole
thing. You should still be very
efficient of what sorts of contexts are,
you know, you're letting the model
attend to.
Yeah, and in terms of results, what we
saw was actually a 8% decrease in like
fewer tokens consumptions around at
least that specific tool. So, instead of

[00:24]
again like that tool spinning off
different primitives and going over and
over again, you actually just have this
one tool call that fetches a page um and
then all the results from it.
The second one from that also like those
specialized tools was also speed. Um
beforehand, while it was making like
those 20 different tool calls to fetch
all the context it needs, you just have
this one entry point that spits out
everything that you need. Um and then
when it comes to the quality side, we
had 10 enterprise customers while we
were do running this beta actually start
publishing uh publishing content in
under 2 weeks. So, they're able to
self-serve and also, you know, get to a
quality of output through these agents,
which was something that used to be kind
of like a whole handing experience. Um
it was also had like a really high um
kind of like ceiling.
So, yeah, um when it comes to like
building these agents and with Claude
being able to execute and making it
easier to execute on things. Um, it's
really easy to think that there are no

[00:25]
more problems to solve, but really every
single time a problem is solved, just
that friction point always keeps moving.
So, those are kind of the two that we um
were really chasing after and we really
want to tackle. And there's a ton more
that we also want to continue chasing,
but I think just overall it's a great
thing to just continue to chase friction
because that really is how you create
production, you know, agents and make
those more accessible to users outside
of, you know, more technical spaces. So,
just to quickly close out, um the next
two kind of friction points that we're
looking to battle and excited to show
more learnings on are around really
self-improvement and feedback loops,
which there were awesome talks yesterday
around dreaming sequences and, you know,
how I I think the most interesting one
is actually how do you structure
summaries of different traces? Um, what
what's the best way of collecting the
most relevant memories and also like
forgetting is actually a feature, like
being able to forget certain types of
memories.
And the last one is benchmarking content
creation agents. Um, I think something

[00:26]
really interesting about our space is
that it isn't uh law, it isn't coding,
it's not something that is really easy
to say whether or not it's, you know,
something's correct. There is a lot of
taste that goes into a piece of content
that you create and there's a lot of
opinions of how I want certain contexts
to be formatted and created. So, what
are like the best ways that we are
creating benchmarks so that every single
time we do change our harness, we add a
sub-agent or we decide to add a skill to
our harness, how do we know that it's
actually improving outputs and not just,
you know, kind of vibes that that we're
going after.
Um,
but yeah, I'm around all day, would love
to, you know, chat with you guys and
hear about what you guys are building,
but yeah, I hope this was was helpful.
Thank you.
>> [applause]
[music]

</details>
