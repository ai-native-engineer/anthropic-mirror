<!-- source: https://www.anthropic.com/features/making-of-claude-code -->

# The Making of Claude Code

Origins

#### **BEN MANN Anthropic co-founder and Labs team lead**

  

When we started Anthropic and eventually decided to build a product—which was a controversial thing in itself—the first thing we made was a coding assistant. It was a VS Code extension. You could chat with it, and it would give you four different suggestions of what to do for each prompt you gave it.

  

#### **SHAUNA KRAVEC Head of Reinforcement Learning at Anthropic**

  

At the beginning of 2022, we were already thinking about coding assistants and building models that could do autonomous software engineering. We built the original RL codebase and figured out how to do all the training for agents.

  
  

We were interested in coding because we thought that the path to transformative AI would route through the ability to automate large chunks of software engineering work.

  

#### **DAWN DRAIN Research Engineer at Anthropic**

  

My main project for my first three years at Anthropic, beginning in 2021, was to try and make a model that was as good at coding as possible—at least as good as me.

  

#### **SHAUNA KRAVEC**

  

With our RL training, we started with easy tasks. Can the model write a simple function? Then: can we get the model to write a function and then test if it’s correct? At first, the models were really terrible at it.

  

#### **BEN MANN**

  

Our

early coding assistant 

was fairly popular in the spring of 2022. We had around 100 external users.

  

#### **SHAUNA KRAVEC**

  

The infrastructure you need to do agentic coding is far more complicated than what you need for a chatbot. Especially if you’re thinking about code execution; you need to think about which environment the code actually runs in, and how to manage that securely and effectively. Many of the challenges people face with agents right now [in 2026] are the same exact challenges we had then.

  

#### **DAWN DRAIN**

  

Another tricky problem we hit in 2022 was harness design—the scaffolding around the model that lets it actually act. A teammate on RL and I got a persistent shell working inside the container so the model could execute code, stream input and output, and play nicely with timeouts.

  

#### **BEN MANN**

  

I came back from

paternity leave 

and helped launch the first version of the API, and we basically forgot about the coding assistant for a while.

  

#### **DAWN DRAIN**

  

But on the research side, we just kept working on making models better at agentic coding.

The spark

#### **SHAUNA KRAVEC**

  

At the end of 2022, we moved towards working on more open-ended agents and making them useful. By 2023, we were able to do things like basic function calling, some search, a few bits and pieces.

  

#### **BEN MANN**

  

Shauna’s team was seeing tremendous progress. They figured out how to give the model a bash tool, to give it the ability to search around—these are the key pieces that make agentic coding work.

  

#### **DAWN DRAIN**

  

I spent an embarrassingly long time trying to teach Claude to write diffs, because that seemed like the most natural way to express an edit in text. We eventually built something we called `clide`, a name that had been coined for a previous form by our colleague Eli Tran-Johnson. It was basically an internal command-line tool that let you chat with Claude for code editing and dev tasks.

  

#### **SHAUNA KRAVEC**

  

It was wonky—it was very, very ahead of its time.

  

#### **BEN MANN**

  

I was hacking on clide in my spare time. I loved it. I thought it was really good, but it could be so much better.

  

#### **DAWN DRAIN**

  

We had this feature in clide that fanned out a hundred Claude Haikus in parallel, so you could ask a question about an entire folder that had no hope of fitting in the context window. I had a lot of fun pairing sessions where I would whip out clide to answer a question, and people would always ask me how I knew about these cool tools.

  

#### **SID BIDASARIA Member of Technical Staff on the Labs team and engineer number two on Claude Code at Anthropic**

  

Everyone talked about clide, but it was clunky and so slow to start up.

  

#### **ADAM WOLFF First manager on the Claude Code team at Anthropic**

  

The clide agent was one of the last features I added to clide before I started working on Labs. clide didn’t have a bash tool, so it was limited in what it could do. I set it up so it could infer from a partial change what you were trying to do. So it was baby agentic.

  
  

The first time it worked, I was dancing around my kitchen. I couldn't believe it.

  

#### **BEN MANN**

  

In January 2024, I started the Labs team. I saw a hole in the market for agentic coding. When Boris joined Labs that September, he wanted to do a linter. He wanted to bite off a small piece of agentic coding. I was like, “No, no, no, no, you have to do the big thing.”

  

#### **BORIS CHERNY Head of Claude Code at Anthropic**

  

You had to use all these incantations to get clide to work. But even though it wasn’t great software, it was amazing and magical in a way, because it saw the future.

  
  

I had written a whole pull request by hand, and then Adam rejected it. But he said, “Actually, you should use clide for this.” And so I wrote `--string-edit`, or whatever it was. I just copy and pasted the issue into clide and it wrote the full request. It was a five- or ten-line pull request. I had never seen anything like that. It was just shocking. It felt like the future.

  

#### **BEN MANN**

  

He was like, “Holy shit.” We’d seen the pieces—we just needed to put them together.

  

#### **RAPHAEL LEE First engineering manager on the Labs team at Anthropic**

  

Boris was assigned the area of agentic coding. He was very intentional about the approach he wanted to take.

  

#### **BORIS CHERNY**

  

My starter project was to “automate coding.” So I thought, “Okay, first I need to learn how to use the API,” because I hadn’t used it yet. I started playing around, but I didn’t know what we wanted to build, exactly.

  
  

I was hacking around and I built this

demo 

that I called Claude CLI.

  
  

No one understood what the Claude CLI demo was. I didn’t really understand it either. But looking at it now, you can see the original elements are still there. I asked it to find out what music I was listening to. It just screenshotted Apple Music and read it. It’s kind of magical—it’s just *doing* it.

  
  

This was about two days of work. To recreate this today with Claude Code would take two minutes.

  
  

I posted it on Slack. I think I got two or three likes.

  

#### **IGOR KOFMAN Member of Technical Staff on the Labs team at Anthropic**

  

It was obvious to me that this was the right approach.

  

#### **BORIS CHERNY**

  

The day after posting this, I walked in and saw Robert working, and I recognized those red and green lines for code, which are kind of iconic now. He was like, “Yeah, it’s doing my coding.” It was just the craziest thing—it was useful.

  

#### **ROBERT BOYCE Member of Technical Staff on the Labs team at Anthropic**

  

I don’t recall exactly what I was doing at the time; probably something in the Claude desktop app. The app was very simple at the time, not much more than tool definitions in a loop and a simple REPL UI.

  

#### **BORIS CHERNY**

  

Of course, it was really, really far from good. But I felt this intense urgency to work on it and to make it good. I started working every weekend. My friends were like, “What’s going on? Come hang out!” But there was just this thing I couldn’t stop thinking about. And it still feels just as urgent today.

  

#### **IGOR KOFMAN**

  

Initially at Anthropic, I wanted to work on bringing the power of AI to people who are not engineers. Coding seemed like the obvious thing that we were definitely going to solve. I wanted to work on something less obvious. About three months in, I realized coding is definitely the thing to focus on, because it’s on the critical path to everything else.

The team

#### **ADAM WOLFF**

  

I did not study computer science in college. I was a film major. But I always liked building stuff with computers. I read the first issue of *Wired* magazine in 1993, and I felt like, “Oh my god, I’ve got to be part of this.” So I moved out to the Bay Area. I was a game designer for the first part of my career, and then I became a programmer. Eventually, I worked on a big project called [React](https://www.youtube.com/watch?v=8pDqJVdNa44), which is now a very popular web framework.

<!-- yt-inline:8pDqJVdNa44 -->
[![How A Small Team of Developers Created React at Facebook | React.js: The Documentary](https://img.youtube.com/vi/8pDqJVdNa44/hqdefault.jpg)](https://www.youtube.com/watch?v=8pDqJVdNa44)

<details>
<summary>자막: How A Small Team of Developers Created React at Facebook | React.js: The Documentary (1:18:15)</summary>

[00:00]
[Music]
Check, one two, one two. 1, 2, 3, 4.
The quick brown fox jumps over the lazy dog.
This is React Podcast, I'm Chantastic. Today
we're going back, way back. Back to the beginning
of React. 10 years in the rear view mirror
it may feel like React was always going to
succeed. That a framework by Facebook was
too big to fail. But this isn't that kind
of story. In fact there were many times in
React's history where it seemed like it wasn't
going to succeed at all. So what happened?
How did react go, in 10 years, from looking

[00:01]
dead on arrival to becoming the dominant front-end
JavaScript framework that it is today.
It starts at Facebook in 2011. jQuery and backbone
are dominating front-end JavaScript but more
opinionated tools like Ember, Angular and
Knockout are already on the scene. In the
outside world, Gangnam Style has just been
uploaded to YouTube, Call Me Maybe is topping
the charts, and the freshest meme is the Overly
Attached Girlfriend. In Internet years it's
basically been an eternity. So strap in, set
yourself away, enable that do not disturb
because this is quite the underdog story.
[Music]
I see this camera has a red light on but this
one doesn't.
[Music]

[00:02]
Just clip it on with this.
Testing one two, testing.
[Music]
[Computer turning on]
When I got the offer to work at Facebook,
I told my mom, I was like really excited.
The Social Network the movie had just come
out and she had you know seen it recently
and she was actively discouraging me from
joining because she was like Mark Zuckerberg
doesn't seem like a very nice boy. Facebook
in the time I was there was, I don't think
there'll be anything like it ever again. It
was certainly not like anything that I had
experienced before. In fact just a couple
months after I joined Kanye West came to visit

[00:03]
Facebook's campus and he got up on a table
in the cafe and you know rapped a few bars
and I was working mostly with this guy who
had just graduated from college and I was
trying to explain to him you know I've worked
these crap jobs in software, at that point
had been like 10 or 15 years, nothing like
this ever happens, not to software engineers.
"You're my stressing, you're my masseuse,
mama say mama sa mama dandeson". JavaScript at
the time, I think, was going through this
little bit of an existential crisis as to
whether it was like a real programming language
or a toy programming language. And so there
was a lot of churn. So you had jQuery was
popular and MooTools was popular and there
was so many different like warring frameworks
to try to get the mind share. And there's
a lot of similarities between them but each
one had its kind of bespoke differences and
none of them were actually really fantastic
for building really kind of complicated user

[00:04]
interfaces and apps. There was this trend
towards more sophisticated applications that
do more stuff and at Facebook we still had
a primarily sort of server rendered technology
stack which you know, one of the things that
we fought against for a really long time was
just growing JavaScript bundle sizes so as
we moved more and more stuff to the client,
the client got slower and slower so we actually
swung the pendulum towards server-side rendering
and towards you know minimal amounts of JavaScript
for a while. And there was this feeling that
we knew that what we were doing for client-side
development wasn't working but also that server
side wasn't going to get us all the way there.
So I think that was the kind of environment
that React came out of.
[Music]
I joined Facebook back in 2010. I've been
doing a lot of open source work particularly

[00:05]
in the JavaScript world. I was a committer
on the Dojo.js toolkit back in the day, which
is one of the the granddaddies of the JavaScript
movement along with prototype and jQuery.
I spent my first two years at Facebook on
the mobile team. We had started off a big
push to compete with Apple and Google and
we thought that our best chance of success
as a company was to go directly to the web
and really push to build out the HTML5 ecosystem.
So as part of that we developed, myself and
two other engineers called Vladimir Kolesnikov
and Will Bailey, built a framework called
Bolt.js so named because we bolted together
a bunch of things that each of us liked.
Bolt was basically more or less Facebook's implementation
of a client-side MVC. I think it was like
a pretty good version, maybe a better version,
of things like Backbone and a couple of other
Frameworks that had existed at the time.

[00:06]
But it was born from a place of the specific constraints
of Facebook. It's the heart of your Facebook
experience. Completely rethought from the
ground up. We've been working on it all year
and we're calling it Timeline. Facebook was
one of the first big products that was really
an experience more than anything else. You're
not trying to buy groceries or get tickets
or anything like that on Facebook, you really
just want to be entertained. And as such you
know the user interface itself needs to be
really pleasing. Bolt was not a tool belt,
it was truly an application development framework.
Something designed and meant to build complicated
interactive rich apps and was being used to
build pretty complicated very real products
at Facebook at the time. We ended up having
to essentially replicate most of Facebook,
all the various apps, be it timeline, chat,
newsfeed. We had a whole photos app that we
built and so obviously the team had to expand
greatly. Like that so I think at some point

[00:07]
we probably had maybe 25 engineers working
on all this between building Bolt and building
apps built on Bolt and that's just on the
mobile team. Bolt was never the problem, it
was the architecture that would eventually
break down for us. As the product itself got
more complex and as we added more engineers
to the team, we didn't hit a wall but it started
to get really, really hard to make changes.
And so you know that was around the time that
Jordan was on the ads team and he's like I
wonder, there's got to be a better way.
Jordan is an enigmatic figure. He uh he's
a little secretive so there's not much that
I know about him. Jordan and I aren't necessarily..
we haven't necessarily been in the spotlight
much. Especially Jordan kind of shied away
from spotlights since the early days. Jordan
was a product engineer at the time, working
on ads and ads has one of the most complicated

[00:08]
pieces of UI across all of Facebook at the
moment. On the ads team they were hitting much
you know really hitting the limits of what
you can do without React complexity wise.
And just the developers ability to hold in
their head and understand a bit of code that
somebody else wrote and you know look at the
screen and say okay this code is doing that
and I need to know why. And Jordan had a lot
of very interesting ideas around how you could
take what we had done in Bolt and make it
much more functional and make it more ability..
make it easier for it to scale with people's
ability to understand large applications.
And so we had a lot of ongoing dialogue and
he would come back and forth to us with various
ideas how to change it. I think one of the
original names for react was FBolt which is
Functional Bolt.
He saw that there was an opportunity to do
it.. to solve some of the tricky parts in
Bolt in an easier way. So what Jordan decided
to do, or at least the story that he had told

[00:09]
me, was: "hey wouldn't it be easier if, any
time anything happened, in the app: API state
changes, user type something, we just blow
away the entire UI and we re-render all of it".
If you look at what every other framework
was doing at the time, it was called two-way
data binding and this was not that. It was
like: forget about data binding we're not
going to do that at all. Anytime anything
changes we're just going to re-render and
then there's an asterisk which says well we're
not going to re-render everything, we're going
to try to render as little as possible but
conceptually we're not going to manage these
relationships between views and models, we're
just gonna.. Honestly I thought it was completely
crazy. At the time I was really down on frameworks
in general and I thought there was no way
that was going to work. To many people that
seemed like magic, it was so far outside of
everybody's idea of how things should work
and do work that yeah it took a lot of convincing.

[00:10]
[Music]
I've been working at Facebook for 10 years
now. I met this person called Jordan Walke.
Some people told me he had an interesting
project about JavaScript and I may be interested.
And so I had this meeting with him and one
thing he asked me at the beginning of the
meeting was: what is the most difficult thing
to do in the front-end right now? And I mean,
I was six months out of school, I was like
I don't know and the thing he told me is:

[00:11]
updates. You need to find the DOM node that
is going to change, you need to change the
listener to the click event and remove it
and do all of this, which is pretty complicated.
And this was also a massive source of bugs
within the Facebook codebase.
I was like, yeah you're right, this is probably the hardest
thing.
And he was like: I have a solution for this.
I was like, okay this guy is crazy,
like this is never going to work, it's never
going to be performant. The meeting ended
and for a few weeks I forgot about the idea.
But one weekend I was like, okay maybe I should
try this, maybe there's something to it.
Before joining Facebook, I worked on a way to find
your guild in World of Warcraft and we basically
needed to search through like 20.000 guilds.
And I did a lot of performance work to be

[00:12]
the fastest way possible to display when you
change all of those filters in real time.
And I was like: okay I spent months, full
time, working on making this super performant,
let's try it with React. And in practice it
took me like half an hour to write it and
it was actually not as performant but around
the same order of magnitude at performance.
And I was like mind blown and to this day
I became the biggest React fan in the world.
I was in the photos team and spending all
of my working hours like trying to use React
on my own projects in the photos team, evangelizing.
I felt like it could change the world
which it did.
[Music]
[Chantastic] Jordan is making headway on his
project. He's gotten others involved and they're
seeing the value. But not everyone is impressed.
One manager started to take notice but saw

[00:13]
Jordan's project as a distraction. So they
asked Lee Byron to meet with Jordan and put
a stop to it (to focus efforts on Bolt). We
get into a room. Instantly I knew that this
was going to be weird because we showed up
with very different energies. I'm showing
up with this like, okay Jordan I want to understand
what's going on with your project but I also
want to help make sure that we are spending
our time well and we're working on things
that are gonna have longevity and solving
problems we want to have. And Jordan came
in with like, can I show you a demo of what
I've been working on like this is so exciting
and it does this and it does that. And eventually
like towards the end of this meeting with
him I had to kind of admit like he had something
really compelling. Like I was now really interested
in learning more about what he was doing.
So Jordan's pitch to me was like I only want
to invest in this and work on it if it's going
to be something that people will use and if
that's not going to be the case, sure we're
not going to do this. He's like but I feel
really strongly that all the ways we've been
doing UI development up until now have been

[00:14]
flawed. Whether they're a JavaScript library
that doesn't quite work for us or whether
it's like a 30 year old tried and true model
for doing UI application development. They
all suffer from the same base problem: a state
management and I think this is the way forward,
and Lee if you could just dig into the code
and learn more and try it and then come back
and we'll talk about this again, then we can
figure this out. I was like all right all
right and so I did I dug around the code and
it was um a little hard to understand, but
I eventually got to play with it and got to
build a couple of things and had to admit,
coming away, that like yes there was something
incredibly interesting there. And that was
how I got sucked into the project and I ended
up working on it quite a bit for the the next couple of months.
Lee brings this rigor and sort of design
mentality to these things that
really helped with the initial versions of
React in terms of standardizing it and turning

[00:15]
it from something that was kind of like an
ugly baby that had just grown up at Facebook
to something that really people could approach
from around the world.
[Music]
There were a couple of problems that I faced right away
when trying to understand the code base and
build something. Not only was the the set
of tools and the mental models really different
from what I was used to as a UI engineer.
The syntax and the programming concepts involved,
just the terminology, was also really different.
My takeaway was, you know, okay the whole
bid here was that this would be simpler but
I can't help but feel like this is really
complicated. Mostly as a desire for me to
understand the model but also with a hope
that it would kind of end up helping resolve
some things, I wanted to build a glossary.
Like what are all the things the concepts
and then what are all the actions or verbs

[00:16]
that are going on here. And so I literally
just listed them all out. And then I would
go back to Jordan, I'd go back to other people
working on it, and ask questions like did
I get this right? Are these definitions right?
And they go yeah okay, no you should really
think about it that way, and be like okay,
well that's not how this.. And it would go
back and forth and back and forth and I'd
be honing these definitions and along the
way we'd realize like, oh this concept and
that concept are the same, we're going to
name them one thing instead of two things.
So unwinding all of this and essentially writing
up what ended up being like a reimagining
of the component life cycle and therefore
sort of the entire front-facing API for React.
And I was very happy to see like incredible
enthusiasm around that. Jordan was like "ah
this is amazing, this really clarifies the
ideas". At that point a handful of other folks
had gotten involved with the project too and
then I spent sort of the next month or so,
sort of piece by piece folding those into

[00:17]
place and pretty significantly changing the
surface API of React in the process. That
was I think the first shift from this being
a thing that existed mostly in Jordan's head,
that other people were playing with, to a
thing that all of a sudden felt owned by the
whole team. Where team here is like a collection
of UI Engineers scattered across Facebook
who were sort of bought in on this vision,
who now felt that we now have the same terminology
we can use when someone has a question, anyone
can jump in and answer it rather than only
Jordan. That was the first big shift.
[Music]
[Dog snoring]
One of the first projects that React was used
for was the UFI, the Universal Feedback Interface,
which is basically the likes, comments and
shares at the bottom of each post. This was
still during Facebook's kind of web era, when
Facebook on the web was like the sort of big
driver of engagement. Newsfeed had a billion
people hitting it every day and was massively

[00:18]
tuned for performance. Heavily interactive
surface both on the input side of course you're
like clicking it to add likes, you're typing
into it to add comments, but also on the receiving
side we want comments to come in live, so
as you're looking at it as a comment comes
in we want it to just pop up right there.
And there was this product desire for that
interface to feel almost like a one-off chat
thread, and that was so cool at that time.
And as that started to work the second thread
was well okay if this can work for this really
isolated sense of messaging then what if it
could work for messaging as a whole and this
was another really complicated and fraught
with bug surface area. That was when a lot
of the ideas in React congealed, the JSX syntax
was introduced and some of the ideas about
how to work with data and React sort of were
clarified. A couple of our UI Engineers, along

[00:19]
with the messaging team, if I remember correctly
Jing Chen was sort of the champion of this
project, realized that we needed a completely
new way to think about state too.
[People clapping]
So my name is Jing and I'm a software engineer
in the product infrastructure team at Facebook.
[Chantastic] Flux is an application architecture designed
around React's principle of unidirectional
data flow. Paired with Flux, React could go
beyond the view layer to model entire applications.
This shift in how to think about state paired
very well with how React was thinking about
updating UI and ended up being sort of the
next chapter for how to think about React
being more than just how do you model complicated
UI but how do you model sufficiently complicated
applications. Like this was something that
expanded the full screen and multiple touch
points and had navigation to it and it allowed
us to step into that next chapter. I remember
asking Jing like hey how's it going with this
React stuff? Do you think this is going to

[00:20]
work? She was like, yeah this is pretty good,
I'm pretty sure it's gonna work. That was
when I became more convinced.
[Music]
Instagram joined Facebook in 2012. I think
we had started calling it React by then and
there was a couple of engineers from Facebook
that went to join Instagram to help them expand
the product offering. At the time Instagram
was just an iOS and an Android app and they
wanted to have a web presence as well.
[Music]
I spent 11 years in San Francisco, it was really fun
I made a lot of great friends
but the change of pace out in the countryside is great.
It's just very peaceful
and nice.
I went to Facebook straight out of school.

[00:21]
I studied computer science undergrad
and I got a master's degree. Facebook was,
believe it or not, the cool place to work
back in 2010. It was this great product, that
everybody used. It was super cool on college
campuses and I was really excited to work there.
[Music]
I joined Facebook video. The pitch was, we're
the third largest video site in the world,
after YouTube and Dailymotion I think, and
there was like one engineer working on it
and like you get to be engineer number two
and I was like that sounds pretty cool. We
worked really closely with the iOS photos
team in the Android Photos team and we were
building an Instagram killer and nobody remembers
this but it was called Facebook Camera.
One morning the photo's team got called into the
office early. They said like be at HQ at 8am
and then the VP of engineering was like hey
we bought Instagram, they're your new co-workers now.
And these were like the people that were
like our fierce competitors you know. We looked

[00:22]
at them a little bit as the enemy, I'm sure
they looked at us a little bit as the enemy.
They were a really small team at the time,
they had their core fundamentals really nailed
but there was a lot of stuff they needed to
figure out, that they did not have the team
to figure out on their own and a big one of
those was what does it mean for Instagram
to be on the web. The web experience is really
important for driving growth and so this was
a pretty important priority and so me and
this designer, Maykel Loomans, started building
all the web stuff. And that's kind of where
React enters the picture, when we started
developing this website.
[Music]
We were given this mandate to use client rendering
so I went to the product infrastructure team
at Facebook, which was run by Tom Occhino.
Product infrastructure's role was to support
any team that needed help and do it in a way
that your key indicators of success are going

[00:23]
to be other teams saying "yeah that really
helped us". You go to them and you kind of
consult the Council of Elders and they give
you their recommendation and I said, hey we
need to do client rendering, what do we do?
And the recommendation at the time was yeah
we don't know. We've got like three different
things that we're working on, you should go
try one. We had something called Bolt.js,
there was a second thing called JS.HTML and
then there was this this thing called React.
Pete went and spoke to Jordan about using
React and he came and talked to me about potentially
using Bolt for it but I think he really, really
liked Jordan's ideas around functional programming.
The conceptual model of react was like crazy
innovative and it really, really spoke to
me. My background was in distributed systems.
I was not somebody that loved front-end or
thought front-end was doing things well, so

[00:24]
the fact that React came in with like a totally
fresh approach and didn't really care too
much about existing best practices, like I
was I was on board with that. So while I had
evaluated all three I really just dove in
on React to build a prototype first and that
ended up shipping on Instagram.com which was
the second use of React in production ever
and the first use of building a full application
end to end in React.
When I chose React for Instagram it was not
well known within Facebook and it was this
kind of crazy science experiment.
Not even close. By the time Instagram was,
and you know Pete started playing with it,
it was significantly better than it was in
the early, early stage but it still needed
a ton of iteration. We had to take this thing
that was very much tied to Facebook's infrastructure
which back then was a big giant PHP application
and I had to go get that working in a Django

[00:25]
application which is a totally different system.
And what was key was not doing that once but
making that a repeatable process and making
sure that that pipeline didn't break. I think
he hit a number of really interesting problems
along the way which quite proved the fact
that React was not quite ready for that scale
and along the way Pete, and the team that
he was working with, built a lot of really
interesting things.
[Music]
Some of these products ended up being fairly
successful. There were relatively short time
to deliver a relatively high quality product.
That showed that this model could work and

[00:26]
it was not just that, but people liked developing
using it. And so that kind of spread and took
off and especially is it got more and more
investment, it became clear that this was
what we wanted to use and it was really ads
that was kind of using Bolt more. It had a
higher level of investment, more people working
in that code base, that already knew it and
more components so it was a harder shift to
make.
The ads team just before I joined ads from
the mobile team had done a full rewrite of
the ads creation flow into Bolt. Which took
them I think upwards of six months replacing
a very old PHP application with what time
was considered a very modern JavaScript application.
But at the same time React was also now actually
deployed for real on Facebook and had a team
that was forming around it. So we now had
two viable frameworks that were both live

[00:27]
on Facebook, both solving real problems. We
shouldn't have two. Especially two that were
similar. Similar enough to confuse people.
Like if you looked at the code, their code
almost looked identical but that worked really
differently. It would actually be an absolute
nightmare if you had to work in both. So we
had to decide which to use.
[Music]
A lot of this ended up being a conversation
between myself and Jordan. We did an evaluation
of both of them. A lot of performance-based
stuff and trying to figure out where the edge
cases were. On the pro side of React, obviously
there's all the things that we know now: it
handles complexity way, way more. Even when
writing the ads creation flow in Bolt we had
already hit one place that you just could
not do in Bolt without writing spaghetti code,
and you can do in React. So we knew in the
future even if it was only 10% of the experience
we were building, we're going to run into
this problem again. Now it might only be 10%

[00:28]
unmaintainable but as you scale that across
a company that is growing rapidly, this becomes
an absolute mess. The cons of it on the other
hand were that React in a lot of ways was
not battle tested yet. There's a lot of things
that simply didn't work in React. It couldn't
handle forms, they'd never done a text box
and there's a lot of complexities around handing
awkward form controls like radio buttons and
so on that it messed up. Just performance
issues where it would try and re-render large
blocks so they hadn't had to do all of the
performance improvements that obviously exist
now. On the organizational side the other
con was that we had just done the six-month
rewrite in Bolt. Facebook had done an IPO
recently and the stock had halved since IPO.
Facebook wasn't making enough money and so
the ads team is the team that makes, you know,
that's where the money starts. If we stop
for four months we're gonna have to tell everybody
sorry no money for you so there was a lot
of conversation back and forth about all this.
It got very difficult. Initially a lot of
the engineers that used Bolt, including Shane,
realized just what you said. Like look we've

[00:29]
invested so much in this thing and it's really
worked for all this stuff, certainly we can
work through the next set of challenges we're
having. So initially there was opposition
to React coming in and saying like how are
you gonna, you know, this new thing that's
not even proven yet. This is our business,
this is really important. When Jordan and
I were working through it, there was definitely
uh some emotions uh there um and mostly I
think it came from uh each of us having a
lack of context of where the other one was
coming from. So I think there was a lot of
talking past each other. In the end Mike Schroepfer
stepped in and said, look make the right technical
decision, make the right long-term decision
and whatever it is I'll back you up. But if
you need to pause product development for
four months you can. We all kind of just got
in rooms and you know worked through all these
things and got everything out in the air of
what's a technical problem, what's an organization
problem, what's a financial problem and kind
of a came to the understanding eventually

[00:30]
through uh with lots and lots of coffee that
React was the right way to go, but um it was
not a straight line at all.
He ultimately was one of the biggest proponents or decision
makers in ads switching everything over to
React and that doesn't happen in most companies.
In most companies if that's your baby project
you try to undermine the other, the upstart,
because you're you know you're really defensive
over your own thing. That was not the vibe
at Facebook at the time and I think that Shane
in particular really exemplified that.
There was still a lot of work to do on the ads creation
flow. Tensions were mounting and the team
was stuck. Here again to get them unstuck,
is Jing Chen.
We'd have this thorny management issue and a lot of people disagreeing with each other,
up and down the management chain
on both sides of you know in ads and in this
product infrastructure group, that was building
React, and we'd send Jing in to talk to the engineers and everyone would come out, like

[00:31]
patting each other on the back, full agreement,
a plan to move forward. So she's great at
building a consensus because she's able to
drill into the important technical details,
identify them really quickly and get everyone
talking about the same thing. She obviously
helped both build the product but she also
made sure that every time we found a bug in
React or just something that it didn't handle
yet, she either stepped back from product
and then just fixed the framework. Or she
went back to the team and said look we need
two or three engineers working on this stuff
for the next month to unblock the ads team.
The ads manager was complicated enough that
it actually ended up being a really great
source of performance improvements and finding
like, where are the true points where it just
doesn't quite scale. So I think it was a lot
of using the building blocks that we had and
as you start to assemble them into a really
complicated looking application, what are
the new problems that come out of that, that
we need to solve. And there was definitely
a lot of those. This is one of the most fun
intense periods of my career as I remember

[00:32]
it. We would be going to meet with the team
and we would have to help them put some feature
in and we would code it up ourselves first
in React just to make sure that the that they
wouldn't hit any rough edges. Or more like
to find all the rough edges that we knew they'd
hit and figure out what the solutions would
be. So it was really exciting because we were
working on two things at the same time. One
was delivering this really complicated, really
important software project for Facebook: the
ads manager. And the other was refining this
framework that we really believed in which
was React. By the time we had rebuilt the
ads creation flow, which I think took about
four months, it had been battle tested with
basically everything about the browser supports,
all the form fields and everything, and also
massive performance issues that had been resolved,
so at that point it was kind of felt that
it was ready to be open sourced because you
know we we used it in multiple different types

[00:33]
of contexts and that you know it would actually
be generally useful to the public.
[Music]
[Mumbled question]
What did you say, Evan?
Uh there is not, sorry.
Open sourcing React was never
a question for me. That was the
goal from the very beginning. Tom had this
idea, he called it project perception, and
he was really angry I think it's probably
the best word for it. He was angry that Facebook
was hiring all these luminaries from the JavaScript
world. They would come to Facebook and
because we discouraged people from writing
client-side JavaScript and because it was
a hard environment to maneuver in, they would
actually go pick up mobile because that was
where a lot of the interesting client-side
development was happening. And Tom was determined
to change this around. I remember going to
this conference and I was talking to someone

[00:34]
and I told them I worked at Facebook on JavaScript
and they're like why would you do that? I
hate what Facebook does to the JavaScript
industry. You have hired all these really
great people from these really great projects
and we have no idea what they're working on
now. They've given nothing back. So I think
when React came along I started very early
on talking about if this thing works for us
I really want us to find a path to open source.
And I was running that up the management chain
very early so when the time came to open source
it, there were some meetings, it was controversial
but we had all the support we needed already.
The process of open sourcing is interesting.
There's first a technical problem to solve.
You have to figure out how to extract it out
of your infrastructure and make it work in
the open source, which is all the homework
that we did for Instagram. We made this call

[00:35]
that like we will not impact developer productivity
at all, it's going to be entirely on the open
source team, which was just a bunch of people
that wanted to open source it, to make it
work. Then actually pulling the trigger on
open source, we had to write a lot of documentation.
We spent actually a lot of time with the documentation
to explain like, hey what is React, what are
all the concepts and we tried to put ourselves
in the shoes of somebody that want to build
an app. How do we give the documentation in
a way it helps them do that. Paul O'Shannessy
did a lot of this because he really had the
experience with what the ecosystem needed
to make this work at the time. Paul O'Shannessy
was a huge force on open sourcing. As was
James Pearce who was the head of Facebook
open source. James had joined the company
and he really wanted to change Facebook's
open source image. We had previously open
sourced a lot of stuff but we let it rot.
We would say, hey we're an open source company,

[00:36]
here's our great framework and then we would
just never maintain it. And James and Paul
in particular were pretty instrumental in
saying, hey if we're going to open source
React, we're going to do it right. Internally
there was a lot of excitement because we had
already been using this thing for a while and it
was working for us, we were excited about it.
We chose JSconf US which was kind
of the, I don't know, the Oscars of JavaScript
- is that fair representation maybe? You know
all the celebrities are there and everyone's
paying attention and everybody watches it
live on YouTube. Tom and Jordan put together
this presentation. Tom is a great speaker
and Jordan is a brilliant engineer, it was
like a Lennon and McCartney type of situation.
There was no way that this thing could possibly fail.
[Music]
It was in Florida, at like 9 00 a.m.
We were in Menlo Park and we woke up early,

[00:37]
we took the first bus into the office. It
was completely empty and we're getting ready
to like press the button on the repo to open
source it. Jordan and I were all excited we
got up on stage. I'm going to talk a bit about
how we do JavaScript application development
at Facebook. It was a little unconventional,
I did a little bit of it, he did more of it.
So along with react we are shipping an embeddable
XML syntax and we're calling that JSX. And
we jumped into showing some code and that
code looked different, it looked weird. Here
we have React used with JSX. And people were
rightfully skeptical we'll call it.
Everyone hated it, everyone thought it was awful!
[Music]
Internally we were expecting a much better
reception. Or at least an "oh that's interesting
reception". We thought there'd be some language
nerds in there who would think "oh I can
do fully functional programming in the UI,
oh at least that's interesting". It was a

[00:38]
really humbling experience, it was kind of
a letdown for us because we had worked nights
and weekends on getting this thing open sourceable
and then when we go to launch it, everyone
hated it. The thing that everyone focuses
on is that people really hated JSX.
I haven't watched this video in a while.
See these divs are not exactly what you're
used to they're not DOM nodes, they're special
reactives and I'll get to why that's important.
I don't remember thinking that they were hating
it. I don't remember at all thinking that
they were like tweeting a bunch of stuff.
This is the slide for sure. We haven't talked
about any problems we're trying to solve,
we haven't talked about why this is working
for us or what were the principles of design.
We're just like boom here's some XML in your
JavaScript and people are like hey what is
happening. Uh poor Jordan..
What we didn't really fully understand
was how big of a delta

[00:39]
there was between where the rest of the world
was in the JavaScript community and where
Facebook was. I don't blame them. I don't
think anybody who tweeted Facebook is crazy
was crazy themselves. I think they were kind
of right, we were a little crazy.
I think there was a moment for me personally where
I felt like, you know, my goal with the open
sourcing of this was to get us closer to the
community and I may have set us back a step.
I may have demonstrated that we actually have
no idea what we're doing because what we're
doing is so much different than what the rest
of the community was doing. And internally
there was a "well we messed that up". We made
the wrong call.
Because I think the measure
of success would have been "wow Facebook engineering
is doing some really cool stuff" and instead
it was "Facebook engineering has no idea what
they're doing".
I think that JSconf appearance
might have been Jordan's last conference for
a good few years. I think Tom Occhino also

[00:40]
didn't go back for a while as well. It turned
into a bit of a troll fest for no good reason.
And particularly for something that was as
innovative and useful and you know just fantastic
for developer productivity and just, it's
literally a gift to everybody. Here, move
faster for free. To have people misunderstand
it and say all these bad things about it,
that were just you know knee-jerk reactions
without actually having taken time to think
about it, can only.. Must have felt very bad.
Especially because both Jordan and Tom had
already gone through all this internally in
Facebook for two years. But inside in Facebook
it's a smaller scale you can just get in a
meeting room and talk about it but you can't
really do that with the whole world can you.
There were some technical decisions that were
made as part of React that were self-evident
within Facebook but were like crazy when given
to a different audience in the community.
There was this notion of separation of concerns.
At the time you shouldn't put your HTML, CSS
and JavaScript into the same file. You should

[00:41]
really extract them out and you should have
this separation. And so this was like very
like the best practice at the time. What was
interesting about the approach to separation
of concerns in React is that you separate
your concerns into different components. So
rather than saying: I have my view concerns
over here and my model concerns over here,
you say you have your newsfeed concerns over
here, your photo concerns over here, your
admin panel concerns over here. So it's a
different way of separating concerns and so
there was a lot of backlash around like oh
those people at Facebook are clowns, they
don't know how to write software. We thought
that React probably had no future outside
of Facebook.
[Music]
It looked like all hope was lost for our friends
at the Facebook office. But fortunately someone
outside of Facebook was willing to give it
a chance.

[00:42]
[Music]
When I first started using React in 2013, it was not
popular in the community. It had just been
announced at JSconf.
I saw the announcement
post on Hacker News and immediately thought
that it would be helpful for one of the projects
that I was working on at the time. I was building
an interactive math question editor at Khan
Academy and it was something that had a very
component oriented architecture. I was trying
to use Backbone.js at the time and found that
the state management was getting a little
bit hard and when I looked at React I thought
to myself, wow this actually looks like it
solves a lot of the problems that I have right now.
I'm looking at this post from 2013 that I
guess I wrote a week after I learned about

[00:43]
React and it was right after I had started
trying to use it and somebody had asked "how
is Facebook's React JavaScript library". And
I was a few days into using it and so I decided
to write an answer to that question based
on my experience.
The answer I wrote is very
positive. I think I was having a really good
time using it and it was solving my needs
really well. One line from the post says,
I just rewrote a 2000 line project in React
and have now made a handful of pull requests
to React. Everything about React I've seen
so far seems really well thought out and I
am proud to be the first non-facebook production
user of React. And I talked a little bit more
about some of the technical details and how
it was helping me. It's cool to look back
and it's almost a bit of a time capsule to

[00:44]
see how even one week into React being released,
I was already pretty excited about it and
I think that excitement lasted for a long
time. I converted my entire code base that
I was working on at the time over to React.
I think it ended up being less code and it
was easier to understand and it was faster.
Pretty quickly I said "okay I want to keep
using React" and I ended up deploying that
to production, my rewritten code, and that
was I think the first production code using
React outside of Facebook.
It was a brand new project that had just been
open sourced and not many people had used
it before, and so there were a bunch of rough
edges. It seemed like maybe nobody had tried
to use it in a particular way before. Or if
something just wasn't documented well enough

[00:45]
and I was trying to use it a slightly different
way than it was intended I ran into these
little bugs or issues where it didn't work
quite as I was expecting it to. For some of
those I read through the source code and tried
to figure out: okay why isn't this working,
is there anything that I can be doing differently
for other cases? I ended up joining the IRC
chat channel where a lot of the core team
members were hanging out after it had been
open sourced. They helped me get started not
just using React but also starting to contribute
to it as I started filing issues and helping
other people who were in that chat room, as
well as starting to make small code changes
and starting to improve React over time.
Her perspective from Khan Academy and just being
outside of Facebook was so valuable, so helpful!
Sophie started as someone using React externally
then sort of like moved on to being someone

[00:46]
who contributed to React core externally then
became the most significant contributor to
React core then we would have these like weekly
team meetings and invite Sophie to come and
so Sophie like worked out with her local manager
at her company to like carve out Friday afternoons
to come to Facebook and hang out with us.
And so determined not to do what we had done
previously where we hired folks from the open
source community and then they never contributed
anything back, she became the first ever open
source recruited member of the team.
Sophie's involvement lifted the spirits of
the React team. It also got them thinking
that maybe, just maybe, the rest of the ecosystem
had dismissed React unfairly. They had something
special, they knew it. What they didn't know
was how to convince everyone else.

[00:47]
I think there are people on the team like me and Jordan
and Tom and Chedeau who like the challenge
and the competitive nature of it. We knew
that this was good technology and I was so
sure of that, I viewed it as just a a messaging
problem, you know, okay we gotta crack how
we message this to people because they don't
get it and we have to figure out how to bring them there.
The open source feels like a milestone
and it feels like this is the end. But in
practice it is just the beginning. Because
when you open source you actually have zero
users, now you need to actually build a community,
get all of the bugs fixed, make sure it actually
solves the use case for the people. And so
this is like when the journey begins. We buckled
down. And we also realized I think that really
when you have a project like this that's um
different you have to convince people one
by one. So I think that's really what we focused on.

[00:48]
And we learned a lot doing that. We learned
that the ideas in React are solid, but really
the ideas are not what people encounter when
they adopt a framework. What they encounter
are the docs and the error messages. What
they need more than anything else when they
adopt something is an incremental way of doing that.
So the team got to work. They focused
on spreading the knowledge of React one concept
at a time, one person at a time.
Then an opportunity arose: another conference.
Later the same year, thank goodness,
Pete gave a talk at JSconf EU.
I had my desk over by the product
infrastructure team. I was sitting next to
Tomo and he's like, oh we're just like sponsoring
this JSconf EU conference and we have to give
a keynote and I don't want to give it. Because
I think he was like he didn't want to go through
all that stuff. Because you know after you
give the talk like people go and yell at you

[00:49]
after you get off stage and when you go to
the happy hour and stuff. It's not the most
pleasant thing in the world. And I was like,
I'll do it! I'll take the free trip to Berlin
and go give a talk at a conference. Hey I'm
Pete, I'm gonna talk to you about a library
for creating user interfaces that we call
React. We open sourced this at JSconf US a
couple months ago. And we got some kind of
sarcastic responses on Twitter, a little bit
of snickering, that kind of thing. We weren't
really communicating what we were doing so
I'd like to talk to you today about the design
decisions around React, what we're doing differently
than other Frameworks and kind of the implementation
that lets us make these decisions and make them really fast.
For this talk it was like,
here's what makes React different.
I'm not even trying to say it's good, I'm not even
trying to say you should use it, I'm trying
to say that this is interesting and there's
a lot of interesting stuff about how this
thing works that you should pay attention
to. And that really resonated with people.

[00:50]
And so we got these kind of early innovators
you know if you think of the crossing the
chasm diagram, where you've got your your
early adopters and then you've got your laggards
and in the middle you have your kind of normal
companies. That talk really got those early
adopters fired up and evangelizing React inside
of their own companies. After Pete's talk,
interest started to pick up. People started
paying attention. They just wanted to, you
know, let me just see if there's something
there. And so we got this kind of like slow
burn of adoption of React. And it prompted
some really interesting conversations. It
recruited Brandon Bloom into the community
who came from the functional programming world,
somewhere. He started talking to his friends
and said, hey I think this React thing is
actually worth paying attention to. And then
he goes and talks to his friend David Nolen
who is this very well known, very well respected,
really great musician and JavaScript developer.
I think he was working at the New York Times
at the time and I was passing through New

[00:51]
York to do something and we grabbed coffee.
And I asked Pete some questions and Brandon
Bloom, that was my friend that said you should
really look at React. And the reason I was
excited about it, more than I think you could
have been if you were JavaScript developer,
JavaScript is kind of multi-paradigm you can
do object oriented you can do functional if
you want but it's not required but in Clojure
and ClojureScript functional is the most idiomatic
thing and nothing existed. Like we were sort
of like always trying to get things to work
but it always felt like there was friction.
I was still early in my career right and this
is like really senior super smart engineer
and it was the type of thing where he would
ask me questions about it and I would stumble
to explain it and I would explain it poorly
and then he would repeat it back to me in
like a super eloquent great way and I was
like yes, I'm gonna steal that! And so when
I sat with Brandon and Pete it was like this

[00:52]
huge light bulb went off, I was like: finally
this is so random, Facebook made this functional
UI framework. Eureka! I mean it was definitely
a eureka moment. It it did allow ClojureScript
programmers to finally write a reasonably
performant functional UIs. And it was very
natural, it was a very, very good fit.
Like a week or two later he wrote this blog post
called the Future of JavaScript MVCs that
just like changed the trajectory of the project.
In many ways you look at React and you're
like there's no way this could be fast, there's
no way it could be efficient. And then I showed
these diagrams of what Backbone and React/Om
look like and React is much better. Especially
when you're using persistent data structures.
So my article I think was focusing purely
on the technical benefits of the design. It
removed the superficial consideration and
I think people started saying, okay I will

[00:53]
try it. Not I'm going to use it but it removed
that "I'm never going to use that" to "oh
I'll give it a shot, this is interesting".
Once that post came out like within three
months after that I would say that we were
one of the big contenders if you were picking
a JavaScript framework.
If you want to spread
an idea you need to really convince a few
people and have those people share your message,
you can't just be shouting it yourself.
More people started to realize that React had some
good ideas and made UI development simpler
in a lot of ways. Over the course of the next
I would say like year or two, we're kind of
just tracking things like Google Alerts of
how many times is it being mentioned, who's
writing about it, what projects are cropping
up. Because React was very unopinionated about
a lot of stuff that you need in order to build
a front-end web application and you know people

[00:54]
would fill in the blanks. And there was a
bunch of state management libraries that cropped
up and there was a bunch of router libraries
that cropped up and server-side rendering
strategies. And so there was this sort of
slow burn of adoption over the next year or two.
React is a small focused UI library but
it proved capable when tackling Facebook's
hardest problems and other big companies noticed.
But there was one company especially eager
to rethink best practices.
[Music]
We first heard about React back in 2014. The
Netflix website had been built using Java Web.
It was very slow, it took about 15 minutes
to get up a build and we decided to move to
a more modern framework. There we go. Now
at the time we weren't quite sure if you know

[00:55]
this React thing was going to work out. It
was kind of new and so we were very apprehensive,
especially since we were building the future
of the next 10 years of the website, right,
we make a bad choice now we got to backtrack
years worth of work. And so we were very careful
about not jumping into something that was
too bleeding edge. And so what they did was
they actually pitted two teams against each
other. Each was given 30 days to build a prototype
with one being React and the other one being
Backbone and after 30 days the choice was clear.
So thank you all for coming out tonight. We're
really excited to have you here and share
the learnings that we've had, building the
new UI in React for the past year. It was
not this stage, it was our next stage over,
where I gave my React presentation back I
guess in 2015. Same feeling like oh my goodness
I've got to convince all these people that
React is amazing.
But I guess it worked. So I was part of the
team that built the new site using React.

[00:56]
At first it was very clunky, like you're writing
components and they're not quite, you know,
you're putting too much logic into them or
you're thinking too big. It's not clear the
difference in the paradigm. And then you start
to use it and you go okay wait wait wait I'm
thinking much more atomic. Hence the symbol
of react. I'm thinking about this individual
reusability, okay now I'm thinking about the
testability of these components, I'm seeing
the benefits now come out of it. I can reuse
this over here, we can test this over here,
we can change this here, we can add props
in here. And it becomes very exciting to see
that new paradigm come to play and go: this
is going to be revolutionary, this is going
to change the world. Let's go back in time
one year to the old Netflix UI, you guys might
remember this one. The overall look and feel
is kind of like this old DVD kind of box art
feel and so I actually want to show you one
of the early prototypes of what we thought
the new UI would look like. We knew that going
forward the world was changing, web was changing,
things were moving faster, and our competition
was moving faster as well. So choosing React

[00:57]
and going with a more modern framework really
helped us accelerate how fast we could build
the website, how fast we could get new changes
out the door, how fast we could try improvements
for our customers to make the best possible
experience.
And because of that we've been at the forefront
of leading what UI design looks like in terms
of web development. We've had a lot of companies
copy us, which we take is a great compliment,
but we were there first because of react and
its ability to move so quickly in terms of
design. This is how it ended up turning out
and this is a UI that's big and immersive
and completely built in React. So we're very
very proud of it and the result.
[Music]
Netflix was now praising React publicly and with a
second big company betting big on React,
the framework grew in popularity. In fact it kind
of took on a life of its own and the community
started to take off.
[Music]

[00:58]
React at this point was getting more
popular
and somebody on Twitter mentioned "hey it would be cool to have a React conference"
and a lot of people started commenting and
tweeting about this. And I went to my manager
Tom Occhino. And he was like: there's like
50 tweets about React today, like people are
talking about organizing conferences, should
we organize a conference? And I was like,
I don't know what that means, I don't know
how to do that, but like maybe. I was very
opposed to doing a conference. I thought it
was very cool that we got so much traction
without really pouring marketing money into it.
Even though React came from big tech company
juggernaut Facebook, it was a small group
of people that were like really dedicated
to seeing this thing succeed, so it felt like
this very indie you know Rebel Alliance type
of project. And so I was like we don't need

[00:59]
a user conference, like we got this cool vibe
going on, let's see how far we can push it.
I was totally wrong.
We had said to ourselves,
I think it would be fun to host a React conference
but are there even enough people using React
who would want to go to that, and eventually
we decided: Well let's try it, let's try to
host the conference, and see how it goes.
Within a minute, all of the tickets were sold
out and we actually crashed the website that
were handling the actual payment system.
Schrep, the CTO of Facebook, actually reached
out to me saying like: hey I have this very
important like VP or CTO of some company that
wants in that couldn't get in. Like hey can
you do us a favor and I was like I would love
to, it's the CTO and everything, but like
you know we're completely booked. Certainly
we were very surprised about how quickly the

[01:00]
tickets had sold out. We didn't realize just
how much the React ecosystem had grown and
just how much enthusiasm had been created
by early adopters.
[Music]
We put it together pretty quickly as far as
conference planning goes and we just had it
on campus in one of our cafes and we bussed
people from the nearest hotel. And it was
very, very under produced but it worked out
really, really well.
Good morning everyone
and welcome to React.js conf!
The conference went like extremely, extremely
well. As the organizer of the conference,
I'm so excited to be here. And we open sourced
a bunch of our projects like React Native
and we started talking about GraphQL, about
Relay. And so yeah it was a massive success.

[01:01]
There is this moment where you go and you
see the stage and there's a giant wood cut
out like logo of the React atom. And I was
like, my friend Maykel, the designer at Instagram,
drew that in front of me like in the middle
of the night before we were going to open
source this thing, because we needed a logo,
and I was like: Maykel just like throw something
together real quick. And now it's this thing
that somebody has built a giant sign with
this on it and there's something about the
physical impact of that, that's really cool.
That was the moment when it dawned on me that
React was becoming something different, you know.
So for a long time what React was to
me was a software project and the reason why
I wanted people to adopt it was because I
really thought it would make their software
better and make their lives better and make
their on-call rotations better. There are
a lot of reasons why I thought it would help
them. After that conference what I realized
is that React was becoming a community. There
were meetups that would happen the immediate

[01:02]
next week that would have an expanded audience
that they could go deeper into some of the
things that were discussed was really, really
cool and a huge recognition for us that the
community was going to be an incredible part
of what would make React work and at that
point was definitely already a really important
part of what had gotten React to that point so far.
[Music]
It's proven to me that engaging
with your open source community is actually
more important than the technical work itself,
like if you don't have a community you don't
have an open source project. I'm excited that
we just continue rethinking best practices.
I want to thank this community for making
it possible for us to keep investing in this
and keep working on it. That's all I got,
thanks.
It was a real high point for, not just for
me but for the team, and you know I think
for Facebook engineering. I think we really
felt like not just validated but like we were
actually like doing something that people
cared about and it was a really, really good

[01:03]
feeling. It was already like more widely used
within the company but now it was like, okay
how do we actually start converting everything
to React, how do we remove and deprecate all
of the other frameworks and really like double
down on React. Oh hey, how is it going? Going
from like an interesting product to this is
the next big thing. So it was a really amazing
time to be around and to get the whole company
working together as one, you know, to make
this happen.
Let's see, I have some keepsakes up here,
which will be not easy for me to get down
but.. Let's see.
I have some stickers, oh this is a fun one,
this is the first ever React die cut sticker.
We ordered like a bunch of these and put them
on our laptops and I never wanted to use the

[01:04]
last one that I had. Facebook open source
stickers. Oh some of these will be a trip
down memory lane for folks. React conf. We
made you know, 2018 Facebook open source it's
a good one. React conf attendee badge. This
was a book from the original React.js conf
at Facebook's headquarters so this had a list
of the speakers and the schedule and um here's
the keynote. Me and Christopher Chedeau. We
had all sorts of swag made and a bunch of
other stuff.. So pretty good stuff, pretty
good memories.
The team became inundated with questions from
the community and a new developer enters React's
orbit.
[Music]

[01:05]
What should I do with my hands?
So you're saying that I should actually uh
start like uh.. Let me focus for a second.
Just for the record, I did not create React,
React was created by Jordan Walke.
I worked at a small startup. We were creating a sort
of a digital publishing platform so there
was a really complex post editor with different
blocks or like a scrollable text with like
different effects and stuff. And so creating
a dynamic kind of interactive editor for for
these things was really difficult. And were
doing it with Backbone. I kind of wanted to
give React a try because it was supposed to
solve this problem. The first React component
I wrote was a like button so it was just like
a button you click it and it says like you
like this or you and somebody like this or

[01:06]
you and like 40 others like this. So there
was a bit of like a split and logic, and then
the way you would express this in other Frameworks
at the time, you had to kind of manually watch
what's changed and update it. And in React
you could just say, if nobody liked this show
this, if one person like this, show this,
otherwise show this and like it's a very natural
way to write this kind of code. And yeah I
just wrote that button and I was like yeah
that looks good, ship it. And so we actually
rewrote the entire app in React over the course
of like 9 months while still shipping new
features. So React sped up our development
so much that we were able to add new features
faster, at the same time as we were replacing
old features, that's why I really kind of
fell in love with it.
A lot of things didn't exist back then. Like
there was no such thing as a React ecosystem.

[01:07]
So if you needed something, it didn't exist,
you'd have to write it. So like you'd have
to figure out how to do it because otherwise
you're not going to have a product, right.
So that's kind of what I did for a bunch of
things. One of those projects in particular
was.. I just saw a big opportunity there.
It was called React Hot Loader at the time.
So I wanted to give a talk about that, but
somebody else had done a talk that mentioned
it earlier at React conf. A really clever
fellow called Dan Abramov figured this out
and he created the React Hot Loader. And I
felt that well then that just wouldn't be
interesting because people kind of already
saw it which in retrospect I don't think it
would be true but that's how I saw it at the
time. So I wanted to kind of spice it up a
little bit and I wanted to make a proof of
concept of a thing I saw in a Bret Victor
demo that is often referred to as time traveling.
If you're designing something embedded in

[01:08]
time, you need to be able to control time,
you need to be able to see across time, otherwise
you're designing blind. I didn't really know
how to do it but I thought that's a cool idea
for a talk. So I'm gonna send the proposal
if the proposal is successful then I'll just
figure it out. And it turned out that the
proposal was more successful than I thought
it would be and so I made a proof of concept
for that and that proof of concept became
known as Redux.
So my talk is about developer
tools because React and Hot Loading and time
travel these are all developer tools. He was
literally creating Redux in service of being
able to deliver this talk and I called it
presentation driven development because the
thing that shook out of it was you know this
sort of like canonical state management library
for React apps for several years. Most of
my work is around the React ecosystem because
that's what inspired me to contribute to the
open source in the first place, but there
are two particular projects that I'm going
to talk about today. It was very validating

[01:09]
to give that talk but I was not surprised
by the response because well I had my doubts
but also I thought the talk was good.. like
I thought it's a really good talk. And I was
glad that people also liked it but I think
it was actually not the talk that was really
like the moment for me. I think it was just
like being there.
It kind of felt like
going to Hogwarts for the first
time. I think it kind of had this this feeling
because there were all these people who I
only knew them as these avatars and when you
meet somebody in person they kind of become
three-dimensional of course. You kind of see
the whole picture. And I think it was just
like such a wholesome feeling. It's the feeling
that we are all trying to figure out what
we can do with this thing and we don't know
it yet and we're just playing with it.

[01:10]
That's also where I met Jing Chen. I had asked
for her advice before because she's one of
the co-creators of the Flux architecture.
So it was nice to meet her in person and she
mentioned that actually Facebook is hiring
in London. And so they arranged an interview
for me right at the conference which was like
our normal interview process the same I think
like four interviews or something like this
but I missed the second day of the conference
but we just did an interview there and so
that's kind of how I got into Facebook. We
just quickly grabbed them out of the conference
a little bit like on the down low and then
conducted the interviews in the basement of
a hotel I think.
No Dan is special, he's always been a little
special.
I guess like I would think of myself
as like maybe the first member of what would
become the React team as you know it today

[01:11]
because I joined a little bit earlier than
I think Andrew, Brian, Luna and and like a
bunch of other people who work with us now.
And I joined at the time when a few people
who worked with us before were just about
to leave. So I was kind of in this transitional
period when the team was changing a lot.
[Music]
Remember the old days?
Do you remember the first time you
met Andrew?
Uh I think I've met.. I do! I think
I met him yeah.. I thought it was at React
conf. Well that was the clear moment, maybe,
was that the first time? Did you get invited
to React conf because of that.. He had a speech.
I met him like I think before that. I met
you and Sophie and Joe and Tim like all in
the same week. Yeah he started asking some
questions that were very similar to the questions

[01:12]
that on the team we were talking about internally
and so I just remember like, I gotta connect
you with like Sebastian and Jordan and the
rest of the team. Yeah and then also I was
like to the recruiters I was like yeah this
guy like we gotta hire this Andrew guy. And
I think we were really fortunate early on
to have a bunch of people that kind of stepped
up and they were this seems cool, I just want
to be a part of this, I just want to help.
I didn't realize it was kind of like a freshman
class sort of feeling at the time. Sophie
had started managing the team around that
time as well and I couldn't have really asked
for a better both project and set of colleagues
and team to join. The beginning of phase two.
Yeah, that's cool.
Awesome! I feel
like we really brought it home there at the end.
Like man we're nailing this!
[Music]
React was now out of the hands of
its founders.

[01:13]
It was ready to take on new life in the care of a
new community grown and future-minded team.
We tried to watch some of the numbers like the number of GitHub stars
or the number of npm downloads. On Google
Trends, how many people are searching for
React and none of those numbers are perfect
but basically all of them kept going up over
time and eventually got to a point where we
looked at it and said oh yeah like millions
of people essentially are using React.
There are a lot of little details in how we did
things that encourages an ecosystem to participate,
that were critical parts in making it what
it is today. We didn't put everything in the
framework. We left a lot of it to the ecosystem
to innovate. And we got a lot of contributions,
we got a lot of interest that way, we got
a lot of things spurring from that. It was

[01:14]
not ever a foregone conclusion. Like it's
still surreal to me that it's as popular as
it is. It's this great example of this like
underdog technology within a big company where
there could have been these forces that really
pushed back on it. I think a lot of elements
of good timing, good fortune, good luck, good
leadership support, all sort of like aggregated
to allow React to be a success, that had we
missed a few of those or had a handful more
things failed instead of succeeded, then I
do not think React would be in the spot that
it is today. I feel like you can't take anyone
out of it and have it be what it became. I
think in the early days obviously Jordan,
right. Like this thing wouldn't exist. And
then Jing Chen just absolutely critical. I
mean she was so instrumental in the early
days of React that it just wouldn't have been
a thing that we cared about if it didn't prove
itself. And then Shane O'Sullivan is responsible
for you know really I mean a very hard decision

[01:15]
to like I'm gonna go this path instead of
that thing. And then the engineers that worked
on refining and iterating on it and turning
it into something good it was Chedeau and
Paul O'Shannessy and Pete Hunt. And my manager
Adam Wolff, when I was like you know asking
all these questions about like should we be
doing, like is this even worth it, especially
after JS conf when we were feeling defeated,
you know, he was there to pick me back up
and be like: no look it is delivering value,
this is good, keep going. And there's different
phases too right, you have the early, early
days and you had the like for the next literally
almost we're going on 10 years now, with Sebastian's
technical leadership and Andrew and Dan and
Dominic and Flarney and Sophie and I just
feel like it's just a group of incredible
people and if you take any of them out of
it it just looks pretty different. It was
really a team effort, it was really a team
effort from the very beginning.
[Music]

[01:16]
Misko Hevery says that awesome solutions
are rarely created by large organizations.
It's almost always one person with passion
and vision that slowly start to infect others.
This is a great summary of how React became
React. Because it was never inevitable, it
was always this wild idea that kept gathering
momentum, person by person. And many expected
React to fail and if it weren't for the hard
work of a few determined developers
it very well could have.
This is just the beginning of the React story.
The story of how a community transformed an
underdog UI library into the most popular
JavaScript framework today.
This is React Podcast, I'm Chantastic.
[Music]

[01:17]
I'm like so tempted to just surprise FaceTime
Jordan right now be like: interview!
It's just really strange to think that you're just
so close to death.
The first React T-shirt that we made.
Thousands of developers find jobs across Europe
using Honeypot. If you're up for a new challenge
in one of these European cities, sign up at
honeypot.io. If you want to see more tech

[01:18]
documentaries then subscribe so you don't
miss the next one.

</details>


  

#### **BORIS CHERNY**

  

I asked Adam to be our manager. At first he said no a bunch of times because he wanted to be an IC again, but eventually he agreed after I nagged and got a few beers with him.

  

#### **IGOR KOFMAN**

  

I started coding in BASIC when I was around seven years old. The first piece of software I made was a game to teach math to my little brother, who was five. “Two plus two is what?” Then, if you got it right, it would play music. We were living in Ukraine, and it was likely on a computer imported from the West. You put a tape in it—it was probably a

Commodore 64. 

#### **FIONA FUNG Org Leader for Claude Code and Cowork at Anthropic**

  

There was a language called Turing, which was created by the University of Toronto. I created my first game with that. It was just like art. Programming is a way for you to tell a story and create.

  

#### **CAT WU Head of Product for Claude Code at Anthropic**

  

I joined Anthropic in summer 2024. When Boris posted his Claude CLI demo, I started using it to build RL environments, and I was so impressed by how much faster it made me.

  
  

I was sending Boris paragraphs of feedback. Just as quickly, Boris was responding that he’d landed a feature or a fix for many of the requests. I was probably one of the more active users at that point. He asked me, “Do you want to join this?”

  

#### **MEAGHAN CHOI Product Designer at Anthropic**

  

My very first interaction with the team was probably in December 2024. Designing for

CLI 

tools is not a common thing. But I remember seeing Claude CLI, and I thought, “We could make this a cool product, it just needs a little bit of design love.” So I asked if I could do a quick two-week spike.

  

#### **SID BIDASARIA**

  

I joined the Labs team in August 2024. Boris had this cool CLI thing, so I jumped onto that. I’ve never had one expertise throughout my career, and I had never written a developer tool or a coding tool before. This was completely new.

Building

#### **BORIS CHERNY**

  

In October 2024, I was working on it so hard. Every week, I was like, “Raph, give me engineers, please!”

  

#### **RAPHAEL LEE**

  

We fed almost all of Anthropic Labs to Claude Code. The other part became the MCP team. It would have been great to hire faster! The team mostly grew in the early days through internal transfers and slow, high-quality external hires.

  

#### **ADAM WOLFF**

  

Growing teams is such a double-edged sword. Boris was pushing hard for rapid growth. I wanted the opposite, and I held it back as much as I could. It’s nice to have the extra firepower, but scale makes everything about process, culture, and vision more difficult.

  
  

I also saw this as an early experiment with the ways that Claude Code would change engineering teams and our expectations for productivity. Even with a relatively small team, we were flying through features and smashing bugs at a rate I’d never seen before.

  

#### **BORIS CHERNY**

  

In hindsight, keeping the team small was actually very important to our success. It helped us be really creative with resources, and kept us from overengineering. And it forced us to use Claude more. Otherwise, we couldn’t go fast enough.

  

#### **SID** **BIDASARIA**

  

It was just me, Boris, and a little bit of Ben hacking on this until December 2024. After we got the green light, six or seven folks jumped in from the Labs team and a couple other teams, and we started a final two-week sprint. A lot of the core features you see today were built in those two weeks, like bug reporting and the login flow. That sprint was when I felt like, “Okay, this is turning into something real.”

  

#### **ADAM WOLFF**

  

With React, everything we did to make it adoptable internally at Facebook had made people start to adopt it externally. We understood better what the advantages were, what the pitfalls looked like, what the paths looked like. This was the same for Claude Code.

  

#### **SID** **BIDASARIA**

  

There were no PR restrictions, no review restrictions on the codebase. We would just ship fixes immediately. One incredible thing Boris did early on was build in auto-updates and really good user metrics. So as soon as someone came to us and said, “We don’t like this,” we could ship a fix and they’d have it five minutes later.

  

#### **RAPHAEL LEE**

  

Feedback started pouring in. Boris and Sid would reply to every comment in minutes, and would often put up same-day or same-hour PRs, since Claude Code was so fast to hack on.

  

#### **SID BIDASARIA**

  

Being a CLI product rather than a web app meant no complex architecture to navigate. We could iterate so quickly because it’s just a client application. Super simple.

  

#### **BEN MANN**

  

It’s not very obvious to people who haven’t been working on model productization for a while that you have to build something that works 20 or 30 percent of the time now, so that when the next model comes out, it works 80 percent of the time. And that’s enough to get market traction. And then the next model after that is 90-something percent, and then you really make progress. And you have to have high pain tolerance, because you’re going to get it wrong over and over.

  
  

You have to be in the now, but also be looking towards the future.

Launch

#### **CAT WU**

  

We got a lukewarm reception during the early-access program before launch. Some people felt it was a cool idea, but it had a ton of bugs. But we took the leap to

launch it externally, 

in February 2025.

  
  

That’s when we officially renamed Claude CLI to Claude Code. Alex Isken, from Product Marketing, proposed the name. We liked the simplicity of it.

  

#### **IGOR KOFMAN**

  

Late one night before launch I thought, “Wouldn’t it be cool if we had an ASCII logo?” I collaborated with Claude to fill out some ASCII art fonts, and we turned that into the iconic

Claude Code all-caps logo. 

It was a little delight as you logged on.

  

#### **MEAGHAN CHOI**

  

My favorite thing was adding the little

"Clawd" 

character to the terminal. Sam McAllister had originally made Clawd for the launch of Claude 3.5 Sonnet. You don’t really get to do that kind of thing in products very often.

  

#### **AUSTIN RAY AI DevX Lead and Staff Software Engineer at Ramp**

  

I’ve been a CLI guy my whole career. So I was at the terminal whenever I could be. Someone posted about Claude Code after it was released as a research preview [in February 2025], and I found it. Within the first five minutes of using it, I was like, “Oh yeah, this is going to fundamentally change everything.”

  

#### **KYLE EASTERLY CEO of Delve Group and Claude Community Ambassador**

  

I was eight or nine, on a motor home trip with my grandparents, when I learned to code. My granddad had a laptop, and it had a DOS batch file help manual. I coded up a little detective crime scene investigation game just using if statements.

  
  

Fast forward all the way to 2025, I was working as a consultant on a software project for a nonprofit called the Statewide Independent Living Council of Alaska—they do disability services for youth. They get a bunch of high schoolers together to set goals around what they want to do after they graduate. They ran these workshops with pen and paper, and one out of ten kids would finish.

  
  

When I started making them an app, I was already using Claude, and I’d use the Workbench and go back and forth, copying and pasting a bunch of files into my clipboard, wrapping tags around them. Claude Code was released during that project, and I switched mid-project—*boom*.

  

#### **AUSTIN RAY**

  

I got chills when I was first using it. If it can read, edit, and run bash, it can do anything. It was able to do the steps, and those primitives were all that was required to build everything else.

  
  

I immediately started evangelizing it [within Ramp]. I messaged everyone on our channels to see who else was using this. And I just started going to people’s desks and saying, “Alright, you gotta trust me. I’m not going to leave until we do this. Install Claude Code, boot it up in your terminal, let’s try a few things. What are you working on right now? Why don’t you tell it that? And then let’s see what happens.”

  
  

Boris, Cat, and I had weekly feedback meetings. And so we just naturally built that relationship of developer and user.

  
  

I’ve always been a tinkerer, really into automation, snowballing, and repeated recursive optimization of your own workplace. [Claude Code] was the perfect substrate for that skill set.

  

#### **JARRED SUMNER Founder of Bun**

  

When I tried to use Claude Code, I asked it to implement websocket client compression in Bun, I fed it the RFC for it, and then it just figured out how to implement it. It did kind of a bad job at first, but then after a bunch of prompting it fixed itself. And then I basically changed how we prioritized at Bun to make it easier to use with Claude Code.

  
  

I was probably too obsessed with it relative to its impact at the time.

  

#### **TRISTAN HUME Member of Technical Staff on performance engineering at Anthropic**

  

Most of my tasks required a lot of context. I was working on hard kernels for accelerators that often weren’t publicly documented on the internet. Claude Code wasn’t very good at writing its own tooling and doing a lot of investigation to learn something on the fly. So it just wasn’t very useful, except for very limited tasks.

  

#### **JARRED SUMNER**

  

There was a discussion, I think maybe in August or September [2025], about somebody wanting to ban using Claude Code at Bun. But I was just not going to let that happen.

  

#### **MEAGHAN CHOI**

  

When the Claude 4 models came out, that’s really when our moment came. Until then, there wasn’t actually that much UX design we could do. The model just wasn’t ready for the product that we wanted to build. But then it was.

  

#### **BORIS CHERNY**

  

We also rolled out subscriptions. So it was two things that enabled Claude Code’s takeoff: a business model innovation coupled with a model innovation.

  

#### **DAWN DRAIN**

  

I don’t actually think Claude Code owes that much to `clide`. Once you cross the model capability threshold, the form factor kind of reveals itself.

  

#### **KYLE EASTERLY**

  

It’s been a fundamental shift in how we work. Back when I started playing with AI in 2022, I couldn’t picture Claude Code in my head. But I could see that if it could just make up a working app, I could extrapolate from there.

  

#### **SID BIDASARIA**

  

I never thought it would become this big of a product—that was completely surprising. It’s still surprising to me today.

The new world

#### **BORIS CHERNY**

  

In February 2025, Claude Code was writing maybe 10 percent of my code. By May it went up to 30, 40 percent. I remember I was at the [Code with Claude](https://www.anthropic.com/events/code-with-claude-2025) developer conference when Sonnet 4 came out, sitting in the back room, coding, and I thought, “Wow, this is really getting good.” The model was so much better, so agentic, so good at coding. By winter 2025, 100 percent of my code was written by Claude Code. Not a single line by hand.

  

#### **KYLE EASTERLY**

  

There are two types of developer. One type really likes writing code—it’s almost like a zen garden they’re tending. It’s flow, it’s nice. And then there’s another type—and there’s some overlap, it’s not a pure binary—whose highest moment of achievement is when somebody in the real world is using that piece of software and likes it. That’s the camp I sit in.

  

#### **SHAUNA KRAVEC**

  

I’m a Claude Code power user. I have my whole swarm of twelve different Claudes running around—reading documents, updating things, pulling from Slack. Being a research lead, I haven’t actually written a lot of code in the last few years. Now I’m able to write more because it’s just so much easier.

  

#### **IGOR KOFMAN**

  

As the models and Claude Code get better and better, we’ll get to the next level of abstraction, where you’re not managing a bunch of Claudes—now you’re managing the Claudes’ manager.

  

#### **TRISTAN HUME**

  

I saw my coworkers getting immense leverage, having Claude work on tasks in the background, and I didn’t have a great way of doing that. I basically had to take a week off my normal work just to set up a new dev environment. But it’s clear that the way you have to code if you want to be maximally productive has changed.

  

#### **BORIS CHERNY**

  

My wife and

dog 

were hanging out on the couch while I coded all day yesterday with Claude Code. I wrote 88 commits.

  

#### **CAT WU**

  

When we first launched, everyone was reading every single permission request Claude Code made. These days, a huge portion of our users just auto-accept everything. I think the transition shows that Claude has earned their trust.

The future

#### **ADAM WOLFF**

  

React showed me the limits of having a successful project. It started as this very pure computer science idea: that functional programming would be a better way to represent user interface state than message passing. By the time it crossed a million DAU, it had become something else entirely. It was a logo and a brand and a feeling, much more than a computer science idea. The thing the median React user liked about it may or may not even have been traceable to the core insight.

  
  

I’m sure that Claude Code will evolve in the same way: whatever you think Claude Code is, whether you think it’s the terminal or the personality of Claude or this specific prompting technique you’re using, none of those things matter at the limit.

  

#### **AUSTIN RAY**

  

When I was initially driving Claude Code adoption at Ramp, I was intentional about building a community and a culture of experimentation, sharing how we fail, what works and what doesn’t, and talking about it in a public space. Compounding tribal knowledge is key.

  

#### **FIONA FUNG**

  

The role of software engineering is going to change. I worked on developer tools for eleven and a half years, and I do not pretend to know what next month is going to look like. We need to be curious and lean heavily into learning from our users, both internal and external.

  

#### **TRISTAN HUME**

  

I tried pushing it as far as it could go. I had Claude write, from scratch, a new alternative to Jupyter Notebooks—not looking at any of the code, just letting it go, and even using the browser to test the UI. It actually made something that worked. But when I tried using it, I found I didn’t like it. I need to wait for a Claude that has the taste—that knows all the things I need and can just do them in the background.

  

#### **AUSTIN RAY**

  

It’s the obsession with, “Can I make this faster? Can I make this better?” That’s the Ramp culture. It’s definitely “Embrace the frontier, just try things.” We’ll try anything if it helps our customers.

  

#### **KYLE EASTERLY**

  

A nonprofit organization like the Statewide Independent Living Council could never have afforded custom software before. The grant money for a build like that just doesn’t exist. A whole category of things just became possible.

  
  

We can now take fuel-delivery logs up on the North Slope [of Alaska] that are handwritten, transcribe them, and put them into a CSV file. We’ve just launched a tablet app for that customer.

  
  

We tell our clients that you have to see it for yourself, you can’t just be told how AI is going to work.

  

#### **SHAUNA KRAVEC**

  

The autonomous software engineering agent vision is more or less coming to fruition.

  
  

I think that a lot of the *positive* ideas about what AI will do for people ultimately come down to AI being effective in a way that is open-ended, that can solve problems people could not solve on their own. We talk about accelerating research, curing cancer, going to the moon—you’re not going to get that from a model that just answers questions. You need a model that can be out there in the world, acting.

  

#### **MEAGHAN CHOI**

  

Coding has historically been very inaccessible. Putting it in the hands of so many people and seeing what they’ve been creating, internally and externally, has been really rewarding.

  

#### **SHAUNA KRAVEC**

  

My original background is in theoretical physics. People have been working on the same hard problems for centuries, in some cases. The rate of progress is quite a bit slower than AI and is often blocked by really difficult, expensive things. You’re only going to build so many colliders.

  
  

I think that for most of 2026 and 2027, there’s going to be quite a lot happening in as little as three months. Three months of progress in 2024 would have been an improvement, but less dramatically so. That’s the disorienting part, and I’m not sure if anybody is ready for it.

  

#### **IGOR KOFMAN**

  

My mom was a scientist, and she would use punch cards for coding. I would help her debug her punch cards. My dad was an engineer, but he didn’t know how to code until someone donated a Commodore to the Dom Pionerov in Kyiv—our local version of a YMCA. He got a book on coding, and we would read it at home together. That’s how I got into writing software.

  
  

I do not write any code by myself anymore, as of winter 2025.

  

#### **BORIS CHERNY**

  

This is the

IBM 029 

—it’s similar to what my grandpa programmed with in the Soviet Union. And

this 

is one of the first text editors, which is still installed on every single Mac. And then it evolved, it evolved, it evolved, and it keeps evolving. And then somewhere on the spectrum is Claude Code.

Interviews were recorded in February–May 2026, and have been edited and condensed.
