---
title: "Building with Claude on Google Cloud"
channel: claude
url: https://www.youtube.com/watch?v=SqHsS737CeA
youtube_id: SqHsS737CeA
published: 2026-05-08
duration: "26:29"
---

# Building with Claude on Google Cloud

[![Building with Claude on Google Cloud](https://img.youtube.com/vi/SqHsS737CeA/hqdefault.jpg)](https://www.youtube.com/watch?v=SqHsS737CeA)

<details>
<summary>자막: Building with Claude on Google Cloud (26:29)</summary>

[00:00]
Hello everyone.
Thank you for being for being here
today. I'm pretty much excited to have
this session with you. I know we are
almost at the end of the event. So thank
you for bear with us.
So just to start, let me to introduce
myself. I'm Ivan Nardini. I'm a
developer advocate at Google Cloud
working on building content in
partnership with Anthropic. And in order
to start this presentation today, I just
want to ask a very simple a very simple
question. So how many of you in the last
week use any AI tool
to code or build application?
Okay, the majority.
How many of you use the same AI tool to
build and deploy application on Google
Cloud?
Yeah, just a few of them. So the the
goal here today is just try to make it
better. So in these in this demo, what
I'm going to show you is how you can use

[00:01]
Cloud on Google Cloud to build and
deploy application
end to end. And in order to do that, I'm
going to wear
five different hats.
And we will start from
imagine the use case, right? Imagine the
scenario. You are an enterprise context.
In an enterprise context, you probably
have a team like the one that we are
visualizing here that
it's engaged to build a new feature or a
new product. So starting from the left,
you probably have a PM. Some of you in
this room are PMs. And the PM might have
an idea of how to improve a particular
product or how to implement a feature.
And starting from this idea, he share
this idea with a UI UX design which
allows him to design the idea, to
visualize the idea. And after the idea
start getting a shape, then the idea is

[00:02]
sent to a software engineer that
essentially start developing the core
logic behind this idea in order to ship
and make the application accessible or
the feature the future feature
accessible to everyone.
And
but before to ship it, in order to be
confident on what you are releasing, you
probably have to pass a security review.
So that's why you have a
role like the security engineer that
will allows you to be confident in the
release. And finally, once the
application gets released,
you probably have a data persona like a
growth marketer or a data analyst that
analyze the data that are collected
through the app in order to generate
insight and produce feedback to the PM
in a way that the product or the feature
itself gets
improved. So these are kind of you know,
all the personas that in a simple way we
can imagine are involved in the software

[00:03]
development life cycle. Now with respect
to these personas, Claude could the
Anthropic's coding agent augment all of
them providing several components that
we are going to use
today. So as I said, in the for the
remaining part of this presentation, I'm
going to put the hat of all these
personas. I'm going to show you how you
can use these Claude cool components
together with Claude on Google Cloud in
order to ship, build and ship a very
simple a feedback application that at
the end of the presentation we are going
to use to rate my my performance here.
But
before to start building, of course you
need to set up and the
Claude code that we are going to use.
And I'm so excited and so proud that we
work together with Anthropic to make
this process of setting up Code in order
to use model on Google Cloud in a very

[00:04]
simple way, in a very straightforward
way. So,
you have multiple methods to use cloud
models on Google Cloud in Code, but the
simplest one, the faster one is using
the application default credential,
which
automatically
finds your credential, for example, the
user one, and based on the environment
that you're going to use. And as you can
see in this representation, recently
Code also introduced this wizard that
will simply allows you to
detect your project and your region
where the models are served, and um
check which models are available in your
project, and
like
you to pin them in order to start
building your application.
At this point, like
probably you're familiar with this, and
you're wondering, "Okay, but what's what
is different to use just Code Code with
with cloud models? Why using cloud on
GCP, on Google Cloud?"
So, there are many reason why you want

[00:05]
to do why you want to do this. So, first
of all, because you pay for what you
use. So, the
usage of a cloud models on Google Cloud
is per token, so you don't receive a
message message cap. And also, if you're
building a
enterprise application that needs to go
to production, you can always access to
what is called provisioning throughput,
which essentially will reserve some
throughput for you in order to build
this kind of application.
Um the other important reason why you
want to consider like cloud on Google
Cloud is as I said, the setup is pretty
straightforward using the ADC. You don't
have API to rotate, or you know,
environment variable to set in some
sense.
So, it's a it's a happy journey in in
the with respect to this aspect. You can
access model in your project with your

[00:06]
own
you know, policies set and also like the
data stays in your project while you are
interacting with the Cloud Code.
And model are served in multiple
regions. So, you have global endpoint,
you have regional endpoint depending on
you know, the availability that you that
you need. And as a Google Cloud talking
about availability, we have very great
availability service that standards that
will allows you to
use Cloud and on one of the most
performing infrastructure that you can
find in the in the market. So, these are
all some of the main reason why you want
to consider Cloud on Google Cloud
especially in an enterprise contest.
So, now that you have like few reasons
of why using Cloud
on Google Cloud,
we are ready to build.
And so, as I said, I will start wearing
the hat of a PM.
So, imagine that you just join the
company or maybe you're already part of
the company. You have you you want to

[00:07]
improve our services, you want to
implement a new
features
with respect to a particular product.
What it was happening in the past is
that you have the idea, you go to a UI
UX designer and you ask him to prototype
and visualize the idea. Now, with the
with the Cloud and Cloud Code, all you
you what you can do is just
drawing a picture like the one that you
see here while you're drinking a coffee
maybe in San Francisco and then let
Cloud doing
implementing the idea for you.
So, let's see this
in action.
So, this is a the Cloud Code UI, like
you will probably familiar with that.
And you are familiar with the Cloud MD,
which is essentially give some
instruction.
Here we just say um that we are a PM, we
want us we want to have a starting from
the picture, we want to render

[00:08]
a a prototype of the the app, the
wireframe that we are going to then use
and pass to the UX designer. And in few
minutes, you can see how Cloud was
capable of rendering it and um
just starting from a very simple uh
picture or drawing that you you um did
while you were drinking your coffee. So,
pretty pretty straightforward. But,
imagine how much time you save in doing
this because compared to what you were
doing in the past with the back and
forth
um to in order to get this first
prototype of your idea.
Okay. So, at this point,
the PM gives like uh creates a
prototypes and pass these prototypes to
the UI UX
uh developer. And uh at this point, he
needs to implement a more solid uh
interface in order to use it in uh in
production. So, in in this particular

[00:09]
use case, what we want to create it's at
least three like uh pages from the
landing to the thanking uh
message like message page and a
dashboard
that I would allow me to show you in the
real time what can be the feedback that
I will receive from the room.
So, in this case,
there are many ways you can you can
implement this, but in this case, I want
to use an additional capabilities of
Cloud Code, which is the plan mode. So,
with the plan mode, what we do, we put
Cloud in a mode where it thinks um
before to um like it thinks and propose
what is going to do before to implement
uh any code. And this is very important
because it gives me like a degree of
freedom of deciding to change something
better according to my preference or
according to some standard that probably
I will get access through an MCP server
using uh Figma, for example.
So, now that we have uh in mind what

[00:10]
we're going to build, let's see this in
action as well. So, we started from uh
the wireframe from the PM.
Similar prompt. I enable the plan uh the
plan mode. And so, as you can see
compared to before,
um in this case, I'm simulating the
receiving some instruction from Figma
using a design doc. But uh as you can
see compared to before, it creates a
plan on what it's going to do with
respect to all the components that are
defined in the slide.
We look at them. We are happy. We
accept. And Copilot will implement all
of them. And at the end, what we get
is uh this uh
optimized version. So, as you can see,
we start from here and we get this.
Very very straightforward. But you can
see how we are shifting from a prototype
to something that can be used uh in this
session in a very simple way.

[00:11]
Okay. So, this is the part that probably
every view or every of you in this room
like you do every day, right?
Um
let's uh let's wear the third hat, which
is the one of the software engineer.
And uh the software engineer
he receive this uh front end like all
the components that I was showing you
before.
And uh
maybe it doesn't know anything as
probably uh some of you in this room. It
doesn't know how to deploy this
application on Google Cloud, right? So,
how you can how you can do that? How you
can, you know,
uh hand to have this a clear picture of
what are the components on Google Cloud
that you need to use in order to deploy
a very simple application like the one
that uh I show you today.
Luckily, it's not a problem because as a
Google Cloud,
we invest a lot of time to integrate
with these a large uh bycoding ecosystem

[00:12]
that now is
um growing around uh
models. And
uh we have we in the last few months, we
released two um important components.
So, the first one is uh the developer
knowledge API with this with uh the
associated MCP server. And the second
one is the Google Cloud Skills.
So, with the knowledge with the
developer knowledge API, you get access
to the a fresh documentation from Google
Cloud that can be directly consuming
cloud code
uh through the MCP server. And it will
have cloud code to figure it out what
what is the best
uh architecture, what is the best
implementation uh to deploy a certain
application on Google Cloud. This is
very important because again, what what
we are saying here is that you don't
need to know uh like how to deploy an
application on Google Cloud. You can
just leverage cloud code and this MCP
server that we expose now on on Google

[00:13]
Cloud side to build application like
this one. So, in this case, uh probably
what we want we are going to do is that
we are going to deploy the feedback API
on a serverless function like a Cloud
Run. We will connect with a web uh web
um
oriented DB like a Firestore to corre-
to collect the raw responses that we we
will give through the feedback app. And
then, because we want to have that that
analytics part,
we will build uh
implementation in a way that we can
store those raw response in an
analytical data warehouse like BigQuery.
And we BigQuery we will post process and
we'll consume this information in a
dashboard
uh in a in a in a dashboard like the one
that you can find in a in Looker. But
again, it you you can build this
using
a Co-Code in combination with the MCP
server without no without you having a

[00:14]
prior knowledge of how to do that.
This, like the MCP server and the
developer knowledge API that I just
mentioned, it got paired with also the
skill part. And the skill part is if
with the MCP server you will be able to
design the architecture, with the skills
you will be able to cover the single
blocks of this architecture. For
example, we release a
a simple skills that
enabled Cloud to deploy on Cloud Run, to
deploy an API on Cloud Run, or
to connect like Cloud Run with
Firestore. So, it's more about the
implementation itself rather than, you
know, giving the overall picture.
So, once you get Co-Code enabled with
the MCP server uh of the documentation
and the skills that I just mentioned,
you can just directly implement uh the
architecture that I was showing you

[00:15]
before and you can do this in parallel.
So, another components that you can use
in Co-Code is a sub agents. And as you
can see here, we are going to spin up
three different sub agents, one for the
API, one for the ingestion pipeline, and
the other one for the dashboard. And you
can parallelize the implementation of
each of these components just like you
run a team a team sprint
in the in your normal like usual
development life cycle.
So, let's see this in action as well.
So, here we are again.
First of all, I just want to show you
that we have enabled the MCP server of
the documentation and we have the skills
some of the skills that we pre-built.
One one time more, I provide a very
simple prompt. The first step is
designing the cloud-native back end. So,
it will start
like it will provide me
a draft of the architecture. In this

[00:16]
case, I could use again the plan mode,
but for simplicity I didn't. And then he
used the skill, one of the skill that I
provide in order to implement the API.
Let's say that we are happy with the API
spec, then we have the architecture, we
have the API spec. The next step is
running multiple agents in parallel in
order to implement the
the three components of the app that I
was showing you.
It's it's pretty quick. As you notice,
GoCode like it also manage the testing
part after you finish the implementation
and at the end you will get your
your app, which is now ready to deploy
on Google Cloud.
Okay.
So, at this point
we have we have the code of the app that
is ready to be deployed, but because we
are deploying on cloud and we want to

[00:17]
open this up to a larger audience, we
want to deploy it in a confident
confidently. Like
so,
this is this is when you want to
consider to run a security review. Now,
depending on your company, you can you
can have different security
requirements. So, for example, you may
want to check if your
application is solid with respect to the
most common
uh OWASP issue
or because you are deploying this
application on cloud and one one thing
that you need to consider is probably
you will use what is called a service
account and you want to limit
the the service account when you call a
particular API like the one related to
reading and writing at DB with respect
to certain role. So, you are you you're
sure that
you're limiting what it can happen when
when the application runs on operation
on the on the cloud itself. So, again,

[00:18]
these are just a couple of examples of
um
uh what you want to consider in a
phase like this one and of course this
representation is a strong
simplification of what can happen in the
in the real life. Um it's just a one of
the possible scenario that you can have
and you can see why it's also a
simplification because we are letting
the security engineer not only to
approve if the app is secure enough to
be deployed, but it will also deploy the
app in this case.
But again, this is just a demo so we
have this degree of freedom. With that
being said, let's run the final demo and
let's uh get the app uh running.
So,
in this case, as you can see, I use a
pre-built security review that you can
find in CoCode. Uh
very simple um
very simple prompt also in the in this
case.
And what is happening is a CoCode run
the first task essentially

[00:19]
double check
that everything is aligned. It found
like a possible issue and it
automatically fixed it. So, in a way
that the app now is secure and once it
is secure, you deploy the back uh
the back end API, and you deploy the API
itself.
So, what we get at the end of this, it's
an end point with our app. The app is
live, so I will uh
quickly unlock my laptop, and I will ask
the backstage to share on my laptop.
So, the uh the app, as you can see, is
up and running on GCP. Uh for people
that doesn't know GCP, this is Cloud
Run, is a serverless uh
service that you can use in order to
deploy app, and uh
the app at the end looks like this one.
So, if you remember, I showed you the
original
I showed you the feedback uh frame at

[00:20]
the beginning. So, what we can do now,
live, I can just give me a score. What
do you think the session is going so
far?
Give me
>> Oh, five.
>> Five? Oh, okay. Thank you, man. I really
appreciate that.
Okay, cool session. Let's be Let's be
simple. I saw me, and then
uh in real time, it updates the number
of response, the score, and uh you know,
the visualization. And also, just for
fun, I built a feedback analyzer. So,
once I click this, it will run, it will
call
Cloud Code
Cloud on Google Cloud, and uh based on
the feedback and the comments that you
sent, it will generate this
this summary. So,
pretty pretty straightforward.
I will ask to go back on the
presentation.
Thank you.
Okay.
So, at this point, we have the app, we
collect we collect good feedback. Thank

[00:21]
you again, man.
Uh but, the development life cycle is
still there. Uh we have the last step to
cover, which is essentially people there
start using our app. If you saw one of
the KPI that I had on the dashboard was
the time the response time. So, how long
is
was taking you to just in uh uh like
providing a feedback. So, these are the
kind of information that you can use in
order
uh to like uh
through this data uh you can collect
this data, analyze them, and generate uh
insights in a way that they can be used
in order to improve uh the uh
application. Now,
running uh if you are new on Google
Cloud, there are several services that
you can use in order to analyze these
data that comes from the app. So, a
couple of them, one as I said at the
beginning is an analytical data
warehouse, which is BigQuery, and uh for
the reporting part, you have a tool like

[00:22]
Looker. But again, as we said before,
you don't need to know how to use
BigQuery in order to analyze those data,
as well as how to build a dashboard in
Looker, because we also provide a MCP
server for doing this. Now, for the sake
of time, I'm not going to demo how to
use an MCP server to query BigQuery or
building a dashboard, but uh I want to
quickly share with you
um where you can find uh this
information in order to do that after
this session, because we are going to
release the code. So, I will ask uh to
shift back on my laptop. Thank you.
So, um
Okay.
Loading time. So, with respect to all
the MCP server that are available on
Google Cloud, we uh recently announced
the uh agent platform. So, in the agent
platform, you have uh uh services that
uh is represented by the agent registry,
and in the agent registry, you have the

[00:23]
list of all the MCP server that we
natively support on Google Cloud. So,
for example, we have the developer
knowledge service that I just show you,
and we also have the BigQuery the
BigQuery MCP server that you can use
in order to
uh
query the data that we just collected
from the app. Um it's very like this
registry is relevant because it tells
you how to set uh how to set the MCP
server on your side, as well as it gives
you some observability feature, and the
description of all the tools that you
will find uh for the MCP server. So, you
know how Clockwork will be able to use
uh this uh this um this server to uh
query your data. With respect to the um
Looker part, also like
uh we released the MCP toolbox of DB.
This is a open-source um like a model

[00:24]
context protocol server, and which
include an integration with Looker, and
it's very well um
we have a very very very well-documented
quick start on how to set up with uh
Clockwork and start to using it in order
to consume that data from BigQuery and
build your dashboard. So, I leave you
this as an exercise. Like uh we didn't
we are going to release the code, so you
can go home and integrate these two
parts. It's pretty straightforward, but
the dashboard that you uh you can
create, they are pretty they are pretty
powerful, and you will see uh how nice
they can be.
Okay, back to the
presentation.
I think I'm just in time. So, time to uh
time to wrap up. What I tried to explain
you today
is essentially uh two things. So, first
of all, I was trying to and I hope I did
I did good enough. I was trying to show
you how like all the components of our
clock code, including skills, MCP
server, sub agents, they can really like

[00:25]
speed up the process of software
development, as well as how you can use
clock code with
cloud models on GCP in a very seamless
way. Like if you saw we run several
sessions across like multiple personas,
and like it was the experience was just
straightforward. It was just a
incredible. So,
this is what you can get if you combine,
you know, clock code with cloud models
on on GCP. As I said, the the code
is going to be available right after the
session. We have a great quick start,
and we have a very well maintained
documentation both on Google Cloud side
and Anthropic side. So, I highly
recommend to just go there and check
out. And then, I hope I covered
everything, but if you still have
questions or you want to provide
additional feedback, just feel free to

[00:26]
reach out. These are my social media
accounts.
point.
So, with that being said,
thank you so much, and it was a pleasure
being here today.
>> [snorts]

</details>
