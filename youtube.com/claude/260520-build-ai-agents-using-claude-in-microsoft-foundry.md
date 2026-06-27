---
title: "Build AI agents using Claude in Microsoft Foundry"
channel: claude
url: https://www.youtube.com/watch?v=TQd_YQvydVg
youtube_id: TQd_YQvydVg
published: 2026-05-20
duration: "34:16"
captions: en-orig
---

# Build AI agents using Claude in Microsoft Foundry

[![Build AI agents using Claude in Microsoft Foundry](https://img.youtube.com/vi/TQd_YQvydVg/hqdefault.jpg)](https://www.youtube.com/watch?v=TQd_YQvydVg)

<details>
<summary>자막: Build AI agents using Claude in Microsoft Foundry (34:16)</summary>

[00:00]
Hi everyone. Good afternoon.
Um Thank you for joining us in this
session today. Um my name is Marlene
Mungami and I am a senior developer
advocate at Microsoft. And I'm joined
today as well by two of my colleagues,
uh Liam Hampton, who's also from
Microsoft, and Chris Snoring, who I'm
not sure where Chris is.
He's probably around the room somewhere.
And today we are going to be building AI
agents using Claude in Microsoft
Boundary. And the approach that we're
taking today is super practical. So,
we're not just going to be talking about
what AI agents are, but we're actually

[00:01]
going to be building them using Claude
models in Boundary. So, we'll take a
look at what that looks like in a
second.
I'm just going to move through my
slides. So,
one of the things I'm going to point out
is that in this session today,
by the end of the session, you're going
to have deployed Claude models in
Microsoft Boundary. You're also going to
plug that model into an agent, and
finally you'll give that agent tools as
well.
So,
just to get started before we start the
workshop, some things to point out in
terms of some of the changes we're
seeing in the industry right now. You
probably have noticed that over time, or
over the past few years especially,
we've really seen the the industry
moving away from just single-turn AI
conversations where you're just talking
to an AI and it's giving you a response.
And now, we're actually building agentic
systems where our agents can plan,

[00:02]
um they can reason, and they can take
action on our behalf over time. And
there's three specific things that are
new challenges that come with these
agentic systems. The first thing is that
the models need to be able to handle
multi-step reasoning over long context.
And the second thing is the systems need
to be reliable. Especially when you're
working with enterprises, they need to
be reliable, they need to have
observability built in, and they also
need to be secure.
And then the third thing is that, uh as
developers are building out their
agents, they need to be able to connect
to different tools and external systems,
data sources as well, to bring that
information in for their agent. And this
next wave of AI actually makes it so
that, even though
we love the Claude models, and I think
the models are getting better every day,
you can't just rely on the models
getting better. We also need systems to

[00:03]
be able to actually have those models
with that intelligence executed. So, um
this is exactly where we believe this
partnership between Microsoft and Claude
comes into play.
So, we What is Microsoft Foundry? How
many of you have actually used Foundry
before or are Microsoft users? Okay,
great. That's a decent amount. That's
that's a really good number. And for
those of you who are new to Foundry,
Microsoft Foundry is our unified
platform for building AI applications
and agents at scale. So, you can work in
the tools that you want with Foundry,
whether you're using things like GitHub,
Visual Studio Code, Visual Studio
itself, or Copilot Studio, you can work
wherever you would like. And um at the
core in Foundry, we have several
different products that we offer. The
first is Foundry models like Claude. The
second is we have something called agent

[00:04]
service. We also have tools and
integrations, and then we also offer
some different machine learning
services, things like fine-tuning that
you can access through the platform.
Now, we support over 1,400 built-in
connectors and MCP tools. So, your
agents can take real action in the real
world. So, you can use things like you
can build agents that have access to SAP
or ServiceNow and and different things
like that. So, you can work on real
systems.
And our agents or we believe that agents
that are built on Foundry come with some
enterprise-ready features. So, you'll
have built-in security, you have
built-in observability,
governance features as well. And then we
also have integrations with Microsoft
Defender, Microsoft Purview, and Entra
ID. So, you're not working with .env
files all the time. So, we really focus
on security as well.
We do believe that actually when you use

[00:05]
Microsoft Foundry, this is us moving
from just building prototypes or being
empowered to build prototypes and
actually deploying those agents into
production
enterprise environments.
So, why exactly should developers use
Claude in Foundry?
There are a couple of different
advantages of doing this. There are four
things that we think developers love
about this combination. The first thing
is best in class reasoning for agents.
You are here at a Claude code
conference. So, I'm assuming you like
the Opus or the Claude models. Opus 4.7
is my current daily driver. So, I'm a
big fan. And we've really seen that a
lot of developers love these models.
They are excellent at planning and
working with long context over time and
understanding that context, which is
critical for agents. We also see that
when you're using Foundry, you're not
just getting the model itself.
You are also going to have the ability

[00:06]
to create agents in the platform,
orchestrate those agents, and then um
give those agents access to the tools
that we saw earlier on. And then like I
mentioned, you have enterprise features
that come out of the box. So, you get to
actually get security compliance and so
on like we talked about. And then we
have this faster development to
production cycle. So, we have a number
of different tools that we offer,
including built-in evaluation tools,
observability, monitoring tools,
integrations that can take your agent
from that prototype and deploy it into
production. So, instead of building out
your own platform from scratch, with
Microsoft Foundry, you get all of these
pre-built, and you're able to uh scale
your applications. Great. So, now that
we kind of have an idea of what Foundry
and Claude offer together, we are going
to go straight into the workshop. So, I
really encourage you to work alongside

[00:07]
with us. So, if you have a laptop, go
ahead and navigate We're going to switch
over to the workshop screen now, so my
laptop.
And you can go ahead and navigate to
this website here.
We have cupcakes
in the beginning here. And so, if you go
through the workshop with us, you will
get a cupcake. So, we are bribing you to
also do the workshop with us.
Um but don't worry if you if you would
prefer just to watch, you can. But if
you have your laptop, go ahead and
navigate to this page, uh that website,
and it will open up the workshop page
for you to take a look at us uh at the
workshop with us.
Um, I will give you just a couple of
minutes to do that. It's
aka.ms/cloudworkshop
for the link we are going to get started
on.
And once you take this, so we can go
ahead and copy this website.
I already have it open, but once you

[00:08]
copy it, you should see a screen coming
up that looks like this. And if you're
on that screen, just click the launch
button and it will launch this
environment for you. So, this
environment is going to start preparing
um to load our content and it already
has loaded. And you should find yourself
on this screen.
So, we, like I mentioned, are going to
be building out an agent with uh AI
Foundry with Microsoft Foundry and
Cloud. And you can go through I will
mention several things. The first thing
is that if you feel pretty confident um
and you are a self-paced person and you
like going ahead, you should be able to
just go through the instructions and
click next and it will have the
instructions as you go along. So, you
can actually do this workshop at your
own speed and go quickly if you'd prefer
going on your own. But I'm also going to
walk you through step-by-step each of
the steps. And if you got any problems
throughout the workshop, uh my

[00:09]
colleagues are here and we're here to
help you if you have any issues.
So, the first thing I will mention
before I start reading is you can We're
using an environment called Skillable
and to you don't have to type things in.
If I click on a uh an input uh box and I
click on the Skillable part here, it's
going to immediately fill out that box
for me. So, wherever your you would like
something filled in, if you see this
green box, you can just click it and it
will automatically fill in that box for
you. So, you don't have to type things
out by hand, um, all the time.
So Skillable is going to open this
virtual machine for you and we'll be
doing the workshop here.
And we have an introduction to what
we're doing. Welcome to Sparkles, which
is the friendliest cupcake shop on the
internet. And Sparkles has a big
problem. We have the most bakery We have
a a big problem where most bakeries
would love to have this problem where we
have

[00:10]
too many customers and too many flavors
and not enough hands behind the counter.
And so we're going to build today an AI
agent that's going to help the Sparkles
team be able to handle all of the
the the incoming traffic from people
wanting to get cupcakes. So the first
thing you're going to do is you're going
to start by navigating to the browser.
So you can click in, uh, after you've
signed in and it's going to launch the
browser for you.
And when you open click the browser, it
is going to open up on the Foundry page.
And you can When you get to this page,
just click on the sign up button. And if
you scroll down,
oh, we're going to switch over to the
next tab.
You can go ahead and where it says sign
in with the username details, I'm just
going to click on that
and it's going to fill in the username
for me.
So I'm now on the second page and then I
scrolled down it you Once you click on

[00:11]
the Edge, um, icon, it's going to open
Foundry immediately. You can navigate
there and then I clicked on the username
to fill that out and I'm going to press
next. I'm going to fill in the password
so I can go ahead and sign in.
Uh, all of these instructions again are
there so if you want to go
quickly, you are welcome to do that.
So this is Microsoft Foundry. This is
what it looks like. I love purple so I'm
a big fan of the design.
But once you have Foundry uh, opened up,
you can click on the project that comes
up. So, this is the project here. We can
go ahead and click on that project.
And that's going to open us
for us
um
this project space here. And we should
be able to click on that, I believe.

[00:12]
Oh, wait. Actually, let's go back.
And
let's click on the start building page
instead.
So, when we click on the start building
page, it should take us here.
And then we can click on this toggle
that says build.
And when we get to that builds toggle
we have some boxes here on the side. And
those boxes say models. So, we're going
to click on that.
And so, I clicked on the build button
and then I clicked on this models button
to the side and it brought up this page
for me.
Now, when I'm on this page this shows me
which models are available for me to
use. So, you'll see that you already
have Claude Sonnet 4.6. And when I click
on this model
here
it's going to open a playground
environment for me in Foundry.

[00:13]
And this playground environment allows
me to be able to chat with the model.
These are some custom instructions. So,
the custom instructions on this side are
saying you are an AI assistant that
helps people find information. And I can
chat with the model here. So, once you
finish this step, you can switch on
you can switch to this page here and
it's going to give you some information.
So, here in the Foundry environment,
this is a great place to experiment with
the model and see and compare different
models to see which ones you like and
how they perform with different system
prompts. So in our instructions, we So
we can just say here
hello
to the model.
Hello, who are you?
And
it's going to respond and say hello, I'm
Claude an AI assistant made by
Anthropic. So it's working as expected.

[00:14]
But again, we can switch out that system
prompt if we want to try Oh.
If we want to try different system
prompts, we have to click here. I'm
going to delete the current ones and
then I'm going to click this green
button for it to fill. And our new
system prompt is that I'm you are a
sentient cupcake.
Answer every question with frosting
related puns. So we will say what do you
think? Let's say what do you think
of Claude?
And hopefully it's going to give us an
answer. It's saying What is it saying
here?
It's saying I think Claude is simply
frosting with potential. You could say
they're icing They're the icing on the
cake when it comes to AI assistance.
Wow, who would have expected? Maybe we
should ask what they think of GPT. I'm
joking.
Wrong conference.
Anyway, yeah. But there's lots of

[00:15]
different questions that you can test
out and different system prompts and I
think the playground is a fantastic way
for us to do that. So this is one way
or interface that we can use to be able
to try out our models and decide you
know, obviously you can you can test out
more serious prompts and different
features with it here.
So once you are done with this step,
with this uh testing out in the
playground, we can move on to part
three, where we want to actually take
the model that we have in the foundry
environment, and actually bring it into
our development environment, so into our
IDE. So, we have VS Code already
installed here. And like the
instructions say, in foundry, we can
click on the details tab here. And when
we click on the details tab, the main
thing we want to grab is this URI, our
target URI. And so, once we have this,
we want to get the target URI, and we
want to get the API keys.
Um and once we have that, we are going

[00:16]
to go ahead, and we're going to open up
VS Code.
And when we open up VS Code, it's going
to come with some pre-built files
already uh available for us to use. So,
the main thing we're going to start by
editing is our .env file. So, here
this is a little bit tricky, is that we
want to make sure
that we update the endpoint. So,
if we go here,
I'm just making it so that you can see.
We want to
uh paste in that endpoint that we have,
and we want to remove at the end it says
v1/messages,
and that's not going to work. We have to
remove the v1/messages part, and the
endpoint should end with Anthropic. So,
this is what we want it to look like.
There's a note for us as well,
um
in here about what it should look like.

[00:17]
So, it should end like that.
And I'm going to go back as well, and
I'm going to grab my API key.
Ideally, I would not be pasting it so
you can see on stage, but it's okay for
today.
Uh we paste the API key in here.
And it's already seeing that Claude
Sonnet 4.6 is our model. So now when we
have these three environment variables,
we're ready to start testing our agent
locally.
Um and when we we're here,
we will open up the agent.py file, which
is where we're going to test. So I'm now
going to try to expand
my VS Code.
And hopefully you will have finished and
already completed the EMB file.
So the next step is that we want to
build out our agent for helping with the
cupcake store. And we are going to be
using Microsoft Agent Framework. And

[00:18]
this is a pipe It's available in Python
and I think it might be available in
TypeScript as well. This is a framework
that is also built by Microsoft. It's
open source
for you to use and it's a great way for
you to get started with building agents.
So the main thing that we want to do is
there's a number of different
dependencies if you would like you can
find those there's an SDK to be able to
install this. But you can read a little
bit more about this.
I would say you want to also make sure
that the terminal is open. But we're
just going to move on to the next step
where we
copy here this
uh block of code.
I'm going to paste that block of code
in.
And this is going to be all of the code
that we need to run our Sparkles agent
with Agent Framework. So we're importing
um our agent.
And then we're going to initiate the
client here. So this is what the chat
client looks like. And it's going to

[00:19]
detect which environment variables we
put into the dot EMB file so that it can
use them. So we have the deployment, the
key, and the endpoint that we set as
well. And then we're going to
uh define the agent here in our Python
code, and we're calling the agent a
cupcake agent.
So, now when we want to run this, there
should be a command for us to be able to
type, so we can copy this command here,
paste it in our terminal, and when we
run it, it should start our agent for
us. So, this is just Python code that's
going to start a a terminal here, so we
can greet our agent and say hello to the
agent.
And it should be ready to start saying,
"Hi, how are you? Is there something I
can help you with today?" So, this is
just a basic sort of hello world to
Microsoft Agent Framework.
Now, once you are feeling comfortable
with this, again, if you would like to

[00:20]
spend more time reading about Microsoft
Agent Framework, you can
go a little bit slower if you would like
as well.
But, the next step here is that we want
to connect to the cupcake store MCP
server. So,
for those of you
We've probably heard about How many of
us have heard about MCP before? It's an
anthropic conference. I am assuming most
of us have, but MCP is Model Context
Protocol, and this is an open standard
for letting AI agents talk to external
systems. So, an MCP server is going to
uh when we publish this, this is going
to allow us to access a different set a
number of different set of tools, which
can be functions the agent can call.
It's also going to allow us to access
prompts, which are just going to be
reusable instruction snippets that we
can plug into the agent as well.
And then, it's also going to let us
access resources, which are data that

[00:21]
can be sent over HTTP in a specific way
that your agent will expect. So, with
MCP, one of the nice things is that you
just need a URL and you can plug it in
and you get like a the full API
available in a format that's easy for
your agent to read. There's obviously
some
thoughts that people have about how MCP
sort of handles context, but there's
also a number of ways that you can
handle that with context engineering as
well. So, here, the first thing that we
are going to do is we're going to pull
down
the terminal and I'm going to
delete everything that's currently in
the terminal and instead
I want to replace it with
what's in this new code block.
And in this code block, you'll see that
we've connected to this MCP server,
which is our cupcake store MCP server.

[00:22]
And this will have all of the
information from our store about, you
know, how many cupcakes are available,
what flavors are available as well, and
all of this you get through this URL
that you can connect to.
So, once we have the MCP server in the
code, we we provide it to the agent as a
tool. So, the agent will be able to
access the information that's available
through that server. So, in our example
here,
I'm just going to close and restart the
agent. I'm just control C or we can just
type in exit.
Oh, what just happened here?
I think I pressed control C uh
and okay.
And we can run the same command
that we did earlier to get our agent
going, but this time it will have the
information from our cupcake store
because of the MCP server that we

[00:23]
connected it to earlier. So, here
we're asking we want to ask the agent
what flavors do you have today?
And
I'm not sure if it's going to I hope I
updated so it has the correct flavors,
but I think it says
I think there might be some confusion.
I'm not an AI assistant.
Oh, it's because I did not save the
file.
You see and this is where this is a good
example of why it needs the MCP server
because it needs to have that context
available for it to be able to know
which flavors are available. So, we're
going to save the file
and we're going to rerun the agent and
we're going to ask it that question
again to see which cupcake flavors we
have available today. We're going to ask
the agent what flavors do you have
today?
And it should let us know
what they are.
Okay. So, let's us know it has we have

[00:24]
classic today actually available in the
front. We have classic vanilla, we have
lemon sponge, we have red velvet, and we
also have chocolate flavor as well for
the flavors that are available. So,
these are
This is just a basic overview of how to
connect to an MCP server and in our case
the cupcake server as well.
So, then the third step here is that we
want to load instructions and a welcome
banner
from MCP. So, the agent is we want it to
have a specific persona and we also want
the agent to greet us in a specific way
and we can do that by making the
updating the system prompt to make sure
that it
works in a specific way. So, again what
we can do is just copy this
code
and
I'm going to paste it through.

[00:25]
Whoop.
And you will see that we have
got some instructions that we're pulling
in from the AC at the MCP server. So,
we're actually getting a prompt which is
already available through the MCP
server,
um which is going to have some agent
instructions. And we also have the
specific welcome banner that we're
getting as well as the prompt. So, this
is how The prompts are reusable. So,
this is a great way to
uh simplify workflows if you're if
you're going to have people build with
your project, for example.
So, again to get this to work, all we
need to do
Whoop. All we need to do is run the same
command.
Uh
I don't know if I pressed exit.
Ah, I did not press exit.
Let's clear that.
And let's rerun the agent.
And when we do, we should now see it

[00:26]
have a custom banner
because we got that from the MCP server
as a prompt. Tell it this is how you
should introduce yourself. And then it's
also going to know that this is how I
should respond to the user or interact
with the user. So, it's saying, "Hi
there. Happy to help you order a cupcake
today. First, do you already have a
custom a customer ID or do you want to
order a new one? Enter an existing ID."
So,
if you have gotten to this stage, we are
almost at the stage where we can order a
cupcake. And we have more instructions
here on what to do.
So,
we can try we can answer the question. I
don't actually have a an ID, but I can
create Say I want the agent to create a
new ID for me. So, I'm saying create
one.
And these instructions and the agent is
saying, "Great, what's your first name?"
I'll say Marlene is my first name.

[00:27]
Uh the agent is saying, "What's my last
name?" I'll say my last name.
And then, "What city are we in?" London
is the city we are in.
Okay.
And great, it's saying, "You're perfect.
Let me register you Let me get you
registered. Now you're all set, Marlene.
Your customer ID is this number here.
Please write that down." I'm just going
to copy it. And you'll need it if you
want to order again in the future. Let's
pick a cupcake. So, whatever flavor
you'd like. I like red velvet, so I am
going to go with number four.
And when I
enter that number, then all of this is
coming from the MCP server cuz it has
those custom instructions and custom
prompts. And it says, "Red velvet is a
good choice. Could you look at the big
dashboard at the front of the room and

[00:28]
read the six character voucher." So,
once I've gotten to this stage, I've now
will be able to see the vouchers
available to me or, you know, I can I
can see We just have This is going to
refresh every few minutes, every minute
or so, I think.
Um Oh.
Yeah.
And it's mainly just so we don't get
overwhelmed by cupcake orders. But once
you do you put in the voucher that you
see on the screen,
uh oh, I I pasted in a customer ID. Ah.
Oh, okay. People have already
ordered. I will serve you later. But
once you put that in, the agent is going
to put your name here.
And you can It should first start
in this page. Oh wow, so many people.
I'm amazed by how many people have
already ordered.
And so we're preparing your order. Once
your order is done, it's going to appear

[00:29]
here and then you can come to the front
to collect your cupcake. So again, I'm
not going to change back to order mine
because
I want the voucher to be on the screen,
but basically you paste in the voucher
and then once your name appears,
then you are ready to go with the order.
I think
do we have to
Liam?
I think do we have to approve the orders
that are being prepared from the
dashboard?
Okay.
So then Liam at the front here is going
to start to approve some of these
orders.
Can B is the first order, I think. I'm
not sure if Cap was the first order.
But these should then
show on the ready for pickup
part.

[00:30]
And
this is just an introduction. We wanted
to create something that was fun and
again an introduction to how to use
Foundry again. We're using the cloud
models that are available. We're using
Sonnet for this workshop and then um
we are plugging that into Foundry. I see
Nick has gone to the test feed.
Um Nick N.
But you can you can actually order a
real cupcake. You you don't need to
test. It's fine to test as well, but uh
real cupcake is also allowed as well.
Um
we should have
I'm going to take a second just to
double check.
I think we have got it working now.
And if you see your name on the pickup
ready, you can come to chat to Liam and
Chris and they will have the cupcake
ready for you. Yay!

[00:31]
Uh, Renato, Chris K, Simon Y,
Yusuke, Terry O, Vicky, and Cat.
Your cupcakes are ready at the front.
Nick N is still stuck in the test feed.
You got to make it over to the main
feed.
I should have a link just to mention we
will have like the full workshop
available and the code for this.
Um, so afterwards if you wanted to try
it out at home or if you had any
questions, you can feel free to
um, try it out on your own later. And

[00:32]
we'll be around
uh,
the rest of the day and throughout the
workshop. So if you wanted to chat to us
and ask us questions about Foundry, you
can also go ahead and and check.
Actually, if anyone has questions now,
you can also ask. Let me know.
Um,
and yeah. Other than that, that's pretty
much our workshop for today.
Um, yeah. Thank you very
I'll let the names
keep going.
On screen.
I do think we had one more slide at the
end to show. If we can switch maybe to
Baris, Steve, Tom, C and as well can
collect. Oh, no. Those are preparing but
Damian, James, Tom, Dima, Chris
can all come and grab your cupcakes.
Ah, perfect. Yes. We have a

[00:33]
final slide um just to
reiterate
some of your points and to also say
a couple of things to work on in the
future and if you want to keep working
with um Microsoft and Foundry
go ahead and
uh Bing search Microsoft Foundry and it
should come up and you can go ahead and
experiment with it. We have free Azure
credits so you can try.
Review the documentation. We have pretty
good documentation
um on Foundry docs there.
And you can also go ahead and take some
of our free courses. We have some
courses available through Microsoft
Learn.
Um
if you go to this link, those courses
will be available for you to try.
Um I think there's also some of the code
that will be available there, too.
All right. I think that is it for
the workshop today.
I'm going to switch back to my local

[00:34]
machine so you can see the orders in
case
Perfect. Um yeah, thanks for joining us,
everyone.

</details>
