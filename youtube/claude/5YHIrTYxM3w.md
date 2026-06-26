---
title: "AI with Claude on AWS: From code to orchestration"
channel: claude
url: https://www.youtube.com/watch?v=5YHIrTYxM3w
youtube_id: 5YHIrTYxM3w
published: 2026-05-20
duration: "19:42"
---

# AI with Claude on AWS: From code to orchestration

[![AI with Claude on AWS: From code to orchestration](https://img.youtube.com/vi/5YHIrTYxM3w/hqdefault.jpg)](https://www.youtube.com/watch?v=5YHIrTYxM3w)

<details>
<summary>자막: AI with Claude on AWS: From code to orchestration (19:42)</summary>

[00:00]
[music]
>> Good afternoon, everybody.
Let's continue with the agenda. Thank
you for joining this session. My name is
Antonio Rodriguez. I work in Amazon Web
Services and I'm also a developer as
many of you and also a cloud whisperer
as I like to say we are really just
whispering orders these days not really
writing code.
And uh in this session we're going to be
talking about how to take the
applications that you are building in
Cloud Code from prototypes that you
might have in your computer to fully
production ready applications that you
can have in the cloud in this case with
Amazon Web Services.
And uh I think the story that
we are telling today is a story about
teamwork, a story about better together.
Because
I remember I joined the team and I

[00:01]
started working with Anthropic
more than 3 years ago. I remember we
were still launching Claude 2 as the big
amazing model that was you know changing
and shifting the ground uh below us. And
uh
on since then we have tried to combine
the best frontier models that Anthropic
has been developing with the best cloud
provider
that we had in Amazon Web Services.
And uh
this session by the way is a hands-on
session. So what we are going to do is
that I'm going to give you a brief
introduction into how do we work
together Anthropic and AWS and how you
can use Claude in AWS in many different
ways that we have available today. And
then we are going to give you some
accounts in AWS so that you can
free of charge and with no limitations
test Claude in in in Bedrock in this
case and also in in general in AWS so
that you can see
how to use it. You have a guided

[00:02]
instructions and a workshop, and again,
we are going to give you an environment
so that you can play around with it.
So, um
again, this collaboration uh started and
has been continued as a very long-term
relationship. And um we have proven this
year by year. Amazon has invested
has done a multi-billion investment in
Anthropic uh because we really believe
that we are building the future of AI
together.
And at the same time, we are the primary
cloud provider for Anthropic. And uh
Anthropic has committed
uh more than 100 billion in usage in AWS
as well in the infrastructure that we
are offering for powering the models
that you are using every day with
Claude.
And
an example of
this investment is Project Rainier.
Project Rainier is actually uh one of
the largest
AI computer
infrastructure that was built for
training and hosting the Claude models
that you are using today with Anthropic.

[00:03]
We are also using uh custom and
purpose-built chip sets that are
specifically made for the Claude models
in the chip sets that we call Trainium.
So, we have our third generation of
Trainium chip sets already built by
Amazon. So, you can actually get the
best speed and also use it in the most
cost-effective way
when you are expanding
tokens with with Claude.
And I think that if we start diving into
the technical part of this
collaboration, there are three angles
that we basically offered you when you
use Claude through AWS. I think the
first one is that you have a very
comprehensive list of features that you
can use
for, let's say, a company the model that
you are using. So, in Bedrock, you have
a full platform.
So, you can combine and fine-tune the
models as well. We are the only provider
that allows you to fine tune Haiku in
example in the cloud.
And we have full integrations with the

[00:04]
rest of the features that we have
available in Bedrock and the AWS
ecosystem in general.
The second and very important point is
the security. So, we can make sure that
you keep control of your data at all
times. We avoid this hopping of data
going to the public internet. You can
keep everything private in your AWS
boundary. So, we make sure that you
always align with the compliance and
security
best practices that you might have in
your companies or or the regulations.
If you are working in banking or health
care,
this kind of industries is highly
regulated industries. It's very
important
that you actually have these options for
controlling everything that you're doing
in cloud.
And obviously the data privacy part, we
work nowadays in the latest generation
inference engine that we have in
Bedrock.
We have zero operator access in the
platform, which means that no one from
Amazon or from Anthropic can actually
get access to those instances. So, your

[00:05]
data remains fully private. We are not
sharing that data with anyone. No one is
using that data for training models or
anything like that. So, you keep a full
restriction and again this is because we
need to align with a lot of compliance
regulations that our customers need.
There are hundreds of thousands of
customers who are using these models
every day and therefore it's very
important for us to align on those.
Last but not least the scalability. The
using those models cloud models through
Bedrock gives you
practically infinite scalability in the
sense that you can really decide how do
you want to do the deployments. You have
full flexibility for choosing regions as
well. In example, you could decide that
you want to deploy cloud only in London
region in AWS or only in the European
region in example if you have to align
with GDPR and and these kind of
regulations.
Now, if we see the whole ecosystem, who
who is familiar with Amazon Bedrock by

[00:06]
the way in this room?
Okay, so I was expecting less hands to
be honest because
this is really
a cloud
event, but it's great to hear that you
are using Bedrock or you know about
Bedrock and this and Bedrock has been
growing a lot since the the beginning
since the last three or four years when
we released the service. And today,
apart from the core which is obviously
the foundation models that you have
access to and obviously Anthropic cloud
models are a very important part part of
that. You also have other features that
help you in the full journey as a
developer. So, you have a feature that
help you doing evaluation, that help you
doing prompt optimization,
that help you fine-tuning the models as
we mentioned before or doing model
distillation as well if you need it. We
also give you some features that help
you connecting if you have rack use
cases, you can have knowledge bases that
are fully managed so that you can attach
to it as well.
We have guardrails which is a way in
which you can apply content filters, you

[00:07]
can deny topics, you can
protect PII data or sensitive data by
doing automatic masking and so on.
And you can also control hallucinations
from the models by doing
proper grounding, automated reasoning
checks.
And
even more important in the last
two years I would say
tools for building with agentic AI. And
this
if you are using cloud agents, then
awesome. But if you are using the cloud
agent SDK and you are looking for an
infrastructure for hosting your agents
in a secure way in the cloud, then you
can also use Amazon Bedrock agent core
which is again fully compatible with any
open framework that you might be using
for agent AI today like LangChain, like
Crew AI, and obviously Cloud Agency SDK
as well.
Now, if I have to summarize in a single
slide everything that I'm saying so far
on the why the better together story,

[00:08]
why is it better to
use Cloud in AWS, I would say this is
probably the slide, right? So, first of
all, as I mentioned, the data
sovereignty that you can get when you
are using Cloud in AWS, you have a full
control of the environment that you are
setting up and where you are using it.
You also have centralized billing from
AWS, so you can actually have a single
bill. If your companies are already
using AWS or you are using AWS for other
things, you can have a a consolidated a
single bill that is actually having the
usage of Cloud included with everything
else that you might be doing today.
You have full observability through our
services like CloudWatch or CloudTrail
as well, in which you can actually see
details of metrics, logs.
You can see the traces of everything
that has happened.
And we also offer SLAs, so we make sure
that you have guaranteed availability on
the services. So, you have an uptime
that is
secure for your applications and you can
go

[00:09]
safe to production and make sure that
you can scale at the at the cloud scale
safely.
Um another very important point is that
we have built-in auth integration. So,
if you're using single sign-on or if
you're doing
open authorization OAuth, or if you're
using IAM roles in AWS in example,
um you can directly integrate that with
your identity provider. You could be
using Microsoft Entra ID, you could be
using Okta, you could be using any of
those identity providers today. And that
is a built-in integration that you can
do also for using Cloud in Bedrock.
And uh last point, you can use private
link, which means that all the
communication can remain fully private.
So, uh you make sure that no data is
being sent to the public internet at any
point uh when you are using Cloud in
Bedrock again.
As I mentioned, I mentioned about
compliance before. These are some of the
uh compliance regulations that we
uh support and we are uh good for you to

[00:10]
use as well. Like an example, FedRAMP,
HIPAA, and so on and so forth. There is
a full list online if you want to check
it out. And uh
and more information about all of these
topics.
Now, the good news is that today you
have three ways of using Cloud in AWS.
And actually, this is uh the the most
options that you are going to find in
the whole industry right now. First
First one is you can use Cloud models
directly through Amazon Bedrock, as I
mentioned before. So, basically,
everything that I was saying so far in
which you have the same uh high quality
output that you might be getting uh
directly, but in this case, uh fully
through the Amazon Bedrock uh APIs that
are offered to you. We have a recently
added Opus 4.7 and included the messages
API as well, so that you can directly
invoke with the messages API if that's
the method that you prefer.
Now, we have also recently launched
Cloud platform in on AWS. Cloud platform
on AWS is actually generally available

[00:11]
since a few days ago, and this allows
you to have the same exact experience
that you might be using today directly
with Anthropic, but in this case, with a
consolidated billing through AWS and
having the access control fully done on
AWS as well.
We act as a gateway in this case, and we
send all the inference requests to
Anthropic, so that they can process the
request for you. So, it's giving you the
best of both worlds. So, you get again
the security, the billing, the
consolidated access control that we are
giving in AWS, and at the same time you
have all the feature parity with
Anthropic, including everything that we
have been hearing in this event, and the
latest features that you might be using
today, including web search, files,
agents, and so on and so forth.
Now, the third way in which you can use
it is also if you are not using
programmatically Cloud, but you are
rather using Cloud Desktop. So, you
might be using CodeWhisperer, you might
be using
Cloud Code through the Cloud Desktop
application. You can also use it

[00:12]
directly from AWS, and again, you can
pay in a consolidated bill in AWS.
And you have two ways of doing that as
well. One is through the Cloud
Enterprise in the in the AWS
Marketplace, in which you pretty much
subscribe to the number of developers
that you have using this application as
well. But you now also have the option
of using it
let's say point directly the
CodeWhisperer 3P, which is one of the
latest additions also that the Anthropic
team did for connecting Cloud Desktop to
third parties. In this case, you can
connect Cloud Desktop to Bedrock, or you
can connect even Cloud Desktop to the
Cloud platform on AWS if you prefer to
do so. So again, you have all sort of
combinations to make your life easier,
and pretty much meet you where you are
on your needs on this.
Perfect. Let's dive into the actual
workshop that we are going to be
building together. I just want to
make a recap that first of all, you need

[00:13]
two prerequisites for running this
workshop. One is you need an AWS
account, so that's we got you covered.
We are going to give you again a
workshop account that has
an environment that you can play around
with, and you can pretty much be
free of charge, free of any concern of
using that environment. And then the
other thing is that you obviously need
to have Cloud Code installed as an
application.
And we have a few options for you. So,
if
the folks in the back help me switch
into my laptop, I can show you what is
exactly what we are doing. Um you are
going to find that in the accounts that
we are setting up for you, we are having
the workshop that is called introduction
to cloud code on AWS. And this workshop
has some instructions to how to set up
everything that we are doing. We are
pretty much uh playing around with the
Scaled Draw
tool with the repository of a Scaled
Draw, so that you can see how cloud code
can help you playing around with Scaled
Draw and drawing architecture diagrams
for you in example. Um this is a basic

[00:14]
workshop is if you are already an
advanced user. So who who is getting
started with cloud code in this room?
All right, who would say that is a ninja
in cloud code? So you are you have all
the skills on cloud code.
Who is in the middle?
All right.
Who's not answering? So [snorts]
yeah, I guess most of the room is
probably in the middle. So you will find
that probably module one is basic for
you. So it's just using cloud code on
AWS and learning how to set it up and
point to Scaled Draw and so on.
Module two and module three are probably
more interesting for you. We are going
to start playing with the context. We
are going to start using Playwright MCP,
so we can actually take a screenshots of
the diagram that we are drawing and
making modifi- automated modifications
through cloud code on it. You are also
playing around with the
Git
Git workflows and on cloud code and so
on. And in the module three, we are

[00:15]
going to play with sub agents and
plugins. And we are also creating custom
skills, hooks, and some advanced
parameters for configuration.
I just want to mention that we have an
even more advanced workshop that is also
available for you if you look for this
URL. And basically there you have other
things that are very interesting for
teams who wants to move to production in
a safe way. So, here you can learn how
to set up uh team standards, how to
implement and and distribute advanced
workflows as well, how to do a
scalability, cost control, and so on.
So, in example, you could see uh how to
set up dashboards like this one for
making sure that you can control all the
use that you are doing of cloud code
tokens
uh in your accounts and so on and so
forth, developer productivity
measurements, measuring return of
investment of your applications, and so
on.
And last, you have also options for
using uh the cloud agent SDK on the
Amazon uh bedrock agent core, so that

[00:16]
you can learn how to build the agents
connected to the cloud infrastructure
uh that we have uh here in in AWS as
well.
But coming back to our workshop, again,
uh you have uh different ways of doing
it. You will see that at the very
beginning, you will uh see a screen that
looks like this with some terms and
conditions. So, I just want to remind
everybody that those are workshop
accounts is individual for you, but make
sure that you don't upload confidential
information, personal information, or
anything like that. You will have to
agree to the terms and conditions, and
click on the join event. And from that
point on, uh you are going to see pretty
much this experience that you have in
the instructions here, where you're
actually going to have a an environment
fully deployed for you. And uh you will
see a URL here that will take you to a
terminal and a uh pretty much a Visual
Studio Code UI where you can actually
work on all the instructions that we're
doing in the workshop.
Let's say that you don't want to follow
this path, and you want to do it in your

[00:17]
own machine, then you can do it. You can
use uh cloud directly in a terminal. If
you prefer, you can configure it for
pointing to bedrock
uh with instructions that we're giving
you in the workshop.
Let's say that you want to use
CodeWhisperer uh or or the cloud desktop
app, uh you can do it as well. Again,
here I'm pointing to my Bedrock account.
So, I have a Cloud Desktop pointing to
Bedrock. And uh here I'm doing the
Scully draw
uh application on the on the workshop
that we have for you uh over there as
well.
And uh there is more information. At the
end, we are going to be sharing with you
uh more on the a guidance in example for
how to use Cloud Code and co-work on
Amazon Bedrock. There is a full block
from my colleagues uh who is uh covering
all of this in detail, and so on and so
forth.
All right, let's go back to the slides
uh please on the back.
Thank you.
Perfect. So, um the instructions for
accessing the accounts are very easy.
All you have to do is go to
join.thatworkshop.aws,

[00:18]
and you have to input that access code
that you see on the screen. I think my
colleagues uh have been around uh over
there. You have the two uh solutions
architects from AWS who can help you
with questions. If you have any
questions, just raise your hand,
and we can get uh close, and we can help
you out. We also have been handing over
some uh pieces of paper that has this
information, so uh you can get it uh
easier for copy and paste it in in your
uh laptops.
Um one last comment uh with regards to
advanced configurations, if you want to
use uh things like in example uh
configuring the settings that you're
using in Cloud Code manually, um this is
the kind of uh parameters that you will
need to set up. You might take a picture
now uh if you want. So, the here is how
to set up uh the region pointed to
Bedrock, choose the default model, and
so on and so forth. And then on the
right-hand side, you also have uh some
parameters for reducing the token usage
or doing rate limiting, and uh how to

[00:19]
enable auto reporting for telemetry, and
uh things like that.
You also have some information here
about uh uh how to configure extensions
in the case that you're using Visual
Studio. Uh but again, it is all about
asking Cloud to configure itself, or you
can do it manually if you prefer through
the extensions that we have there. It
helps you with some things like an
example, disable the login prompt that
is a bit annoying every time that you
start, or things like
hiding the onboarding
message that you always get in in Cloud
Code and and so on and so forth.

</details>
