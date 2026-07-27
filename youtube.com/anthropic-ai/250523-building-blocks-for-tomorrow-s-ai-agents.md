---
title: "Building Blocks for Tomorrow’s AI Agents"
channel: anthropic-ai
url: https://www.youtube.com/watch?v=oDks2gVHu4k
youtube_id: oDks2gVHu4k
published: 2025-05-23
duration: "29:06"
captions: en
---

# Building Blocks for Tomorrow’s AI Agents

[![Building Blocks for Tomorrow’s AI Agents](https://img.youtube.com/vi/oDks2gVHu4k/hqdefault.jpg)](https://www.youtube.com/watch?v=oDks2gVHu4k)

<details>
<summary>자막: Building Blocks for Tomorrow’s AI Agents (29:06)</summary>

[00:00]
[Music] [Applause]
good afternoon and welcome back from lunch you
know whenever I do a tech conference I always ask
to do the session right after a lunch because I
know only the most motivated hardworking smartest
most beautiful people come right am I right so
thank you thank you for being here um I'm Brad
Abrams i'm a product manager at Enthropic uh and
we're going to talk about components for building
agents today you saw Michael in the keynote talk
about our Anthropic developer platform here and
today we're going to build uh drill into this
agenic components when we think about building
agents there's really three key parts of this
first is fundamentally building the agent and
starting with our foundational models with the
Claude 4 family of models with enhanced reasoning

[00:01]
memory support much improved tool calling and long
range planning is a great way to start there's
also a set of components that you can reuse that
saves your precious engineering resources to work
on different things but we know regardless of how
good our models are they're only as intelligent
is the data that you bring to them and that's
what the connect pillar is all about how can we
help you bring more context in that helps the
intelligence of the model and finally none of
that matters if you can't deliver a service that's
reliable that's stable that's performant uh and
cost-effective and that's what optimize is so this
is sort of our agenda for today let's drill into
build so with build I want to talk about the code
execution tool customers have told us that while
uh large language models can do many amazing
things there's still some tasks that require

[00:02]
uh traditional software development when
you're doing advanced data analytics you
have a giant spreadsheet need to understand
uh do deep analysis of that data that's still
the domain where a human might need to write code
because that code is auditable uh it's performant
uh it's repeatable it does the same every time
so um so some some of those use cases are still
better done with code but you know our models
are actually pretty good at writing code so we
thought why not give Claude a computer and let
it write and execute that code and that's what
code execution is all about let me explain it by
drilling in uh one level deep on an example so
we have a client here it calls claude and and
then that goes to a container we have a whole
uh set of containers so every organization gets um
a ded a dedicated container um and here the client

[00:03]
is actually requesting container ID one your
client can decide uh how to use the containers
how to allocate them uh the client has this prompt
i don't know if anybody's already figured out the
answer to this i'll let you noodle on that for
a second um Claude uh thinks about that for a
minute and decides you know actually this is be
best best done by writing code so Claude chooses
the code execution tool writes a set of Python
code that will answer that question um and then
we hand it over to the container the container
executes that and then we get some uh results back
so all of standard out comes back standard error
comes back uh and any files that were created in
while executing on that container come back and
then the model then reasons over that results and
comes up with a quippy answer so the answer was
42 and Opus with its uh insightful humor here has

[00:04]
come up with a good good joke about that so that's
generally how code execution works and it's very
simple to set up those of you that are already
customers will recognize the messages API it's
the core way to use our models so it's the exact
same API you've been using before we've just added
a new tools block um and keep in mind this is
really all you need to do to to set this up it's
uh one method call brings all of this power and
that's just what Shopify found was interesting
uh as they experiment with this with this
code execution tool we're building they have a
uh sidekick agents that helps merchant
merchants build their storefronts and
they're building AB testing experience there
and having the power of this code execution
tool is helping them bring that insight so to
really understand let's switch over to a demo

[00:05]
yeah let's switch over to the demo so doing
a demo in a tech conference at any time is a
harrowing experience but when you're launching a
brand new model with a bunch of new features uh
in front of a live stream it's it's particularly
crazy so hopefully this will work well so what
we have here we've uh Thank you thank you we we
have uh vibecoded a little command line client
just to explain how the system works very very
basic system here and we're using um opus 4 uh
so what I'm going to do here is just give a very
simple query here i'll let you think about what
the answer to this one is so we pass this query
to claude 4 and it has the code execution tool
enabled um Claude's going to reason about that
for a second decide to call the code execution
tool and then we get streaming results so this is
one one uh HTTP call but we're getting streaming

[00:06]
responses back the code gets written by the model
passed to the tool the tool is executed the the
code and we got that standard out there that's the
100th prime number and then the model gives its
its quippy answer here thank you first demo worked
i'm feeling I'm feeling good let's let's push it
a little bit harder okay so I have some AB test
results here uh I have to make uh shop my Shopify
friends happy um I have some AB test results here
i've uploaded those with the files API which we
also announced today uh and then what I'm going
to do now is do some uh analysis of it so you
can see this prompt says analyze the uploaded AB
tests and compare control and treatment calculate
the statistical significance and key metrics and
make a recommendation so using all parts of the
model here we're doing some code execution notice
in this first turn the model has never seen this

[00:07]
this spreadsheet before so it first has to analyze
the types in the spreadsheet what's there it gets
those results back and then since it understands
them it now writes deeper code to go understand
uh what's really happening here and pull out some
insights so we're now we're executing that code
on the VM um and we get all the results back in
standard out and I got to say I just love Opus
because it doesn't give up he didn't get exactly
what he wanted out of that analysis so it's look
I need to drill in more i need to understand
a little bit more before I can do this so it
um drills in more uh writes some additional
data analysis code and see here it's writing
the output for itself to read so all these
print statements are going to come back
to standard out and then we're going to pass
that to the model so those came back and now
the model is reasoning about what its response
is and it makes that business recommendation

[00:08]
that we asked for and justifies it with the
analysis of all that data so pretty pretty
good great let's switch back to the slides
okay so that's the first live demo great
code execution tool um the codeex code
execution tool is an enthropic hosted
computing environment um and it's flexible
developer controlled so you don't need to
tie to threads or whatever like devel you can
control which request goes to what container
and your containers are isolated from everybody
else's um and you get 50 free container hours
today which is a good amount to get started
and then love to scale with you so we have
some pricing to to let that scale and the
best part is that's available for you to use
today wow this is a good audience good okay let's
move on and talk about the connect uh pillar here

[00:09]
how you can bring data into the into the model
so many of our customers have told us that again
while the model's reasoning is great it was
trained at some specific time um and maybe they
need more recent information whether that's for
financial use cases say the latest stock prices
or for in the legal case maybe there's some case
law rulings that need to be kept up to date or
um even in coding you may need to get the latest
API documentation to make sure your code works
uh beautifully so in all those cases that real-
time information is is very important and that's
the role that web search plays so let's drill in
uh in a similar example and check in how how web
search works in our system so again I have the
same sort of setup a client gives this prompt
um what are the most significant technological
breakthroughs announced in the past three months

[00:10]
and what publicly traded companies uh would
benefit from them so that's actually a pretty
complicated problem i mean you might pay an
analyst money to actually answer this question
what Claude does is it doesn't transform that
prompt into a query it actually reasons about
the overall task that you've been uh asked claude
to do and it decides well the first thing I need
to do is do a broad query and really understand
the technological breakthroughs um it issues
that query we pass it to a search engine and
get a set of search results back so just think
about the standard tin blue links so we get
title URL and content from each of the websi
uh these uh websites and so all that context goes
into the model and then the model says okay given
the prompt that I was given and this additional
context what do I need to do now so it says okay
well I need to drill into one of those particular
trends so it it um picks this small language model

[00:11]
drills in and and finds companies that are related
to that gets the same search results and content
back into the model and then the model decides
again to do another search now this one I don't
really know is a a techn a trend that I'm aware of
but we learn new things with Claude every day so
it's really fantastic um and keep in mind all
of these things are happening in that one API
call that I showed you one API call and all the
you get all of this power so we get the search
results back um and then this is an interesting
case it does this one final search um to to go
one level deeper into the small language models to
get a really deep insight into this particular one
um and gets the results from that and then it
produces uh its report so it reports a complete
report and all of the data is now cited so there's
actually footnotes citations for every fact so

[00:12]
that you can go back and verify make sure there's
no hallucinations and it is exactly what you want
uh and this is uh again as I mentioned one API
call messages API and there's a tool very similar
to the code execution tool we showed earlier um
in this case you can actually restrict the domain
so say you're building uh customer support agents
you might want to restrict the domain to just the
uh just one domain so you get accurate answers
and you can also control the max turns if you
want to be a little conservative on how many
tokens you spend although it's my business
that you spend a lot of tokens so feel free
um okay and that's what Kora has really found
interesting they're building a consumer agent and
they really value that live upto-date information
because consu consumers oftentimes ask about
what's going on uh contemporarily and and so

[00:13]
they're they're really valuing that and again
we're seeing customers across legal coding tools
um find this very valuable so let's do another
demo so let's switch back to the demo machine okay
so now let's try a search query um what are the
bench scores for all of anthropics models since
35 uh so this is a a contemporary one this is one
that's sort of real time right now so we'll see
how well this this works um so what it's doing now
is it's actually considering that query looking at
all the tools it has available um you know we saw
before it whoa that's good times um let's try that
one again we know it's real if um so it's looking
at all the tools it has available and deciding
which one to call um so in this case it calls the
search tool and it starts with 35 because that's

[00:14]
the data that we gave it so it does that search
for 35 um and then it does a more general search
so Claude's not satisfied with the answer from
the first turn so we're not like structuring oh
do three searches these are the searches claude's
deciding what searches to do how many of searches
when to stop what to drill in on um and here
it looked like it it this gets to get updated
we don't quite have the Sonnet four scores up but
they will be there very soon okay but can we put
these things together um so this is a question
I have wondered with for a long time and that's
how many elephants can travel over the Golden Gate
Bridge in an hour if you think about this question
uh which is a very important question you know
there's actually some pieces of data you need
to know you might need to know um how what the
weight capacity of the Golden Gate Bridge is
uh the walking speed of an elephant but then
even once you have that data you need to do

[00:15]
some computational work to go understand so
Claude's doing all the did all the searches
now it's doing the computational work or at
least it's writing the code for that and as
soon as it finishes writing the code um it will
we pass this over to the code execution tool and
it will execute that code there we go it executes
it um and gets this data and that goes back into
the model uh the model sees that data and it
forms its answer which is 7,000 can go does
that that seems plausible right okay so that's
uh web search with with code executor it's good
okay okay uh let's go back to slides if
we can okay so that's web search um and
it's it's anthropic's agentic search
capability so it's not just simply

[00:16]
passing a search query and getting a
result the model is actually deciding
uh how to search how many times to search doing
that loop over and over again uh and that's
done with our citation support so everything
there is fully grounded and auditable and it's
uh highly composable developer controlled so it's
very easy to add you can have a lot of controls as
developers and then it's reasonably priced so you
can you can use that at scale and that's available
today so let's talk about MCP connector next
uh we've just been blown away at the industry
excitement around MCPs i see a new MCP launch
literally every day so that ecosystem is growing
uh very quickly and in fact just last two week
last week uh Claude Aai launched support for
remote MCPs and claude AAI and many of our
customers have been wondering how they can
take advantage of that ecosystem of MCPs within
their own agents and MCP connector is the answer

[00:17]
to that so let's take a look at how that looks
under the covers so this is a little bit more
uh complicated setup we have our client and we
have three different MCPs connected uh and that's
because we're serving query our agent's going
to serve queries like like this one that like
a product manager might need to do for a team
after a after a launch uh create an email with
a creative and motivational image about my Asana
project status and send it to the team so there's
several components here um and Claude's got
these three MCPs to go figure out how to do that
so the first thing Claude decides to do is to
call the Asana MCP and a specific tool there uh
the Asana MCP has got tens of tools that you
can call but Claude has picked out the right
one this list workspaces and notice we're doing
this call my Asana task are are authenticated

[00:18]
not everybody can see them so we actually have
to do a ooth request to the MCP server so when
you make this API call you pass a ooth token into
the messages API we exchange that OOTH token for
access token and then make the call to the Asana's
MCP server in a secure way so we do that call we
get the results back and we say okay uh this this
is this is the workspace that that user has assign
uh Claude then decides to drill in it picks
this um search method to search for this code
with Claude in MCP demo that's one I set up in
context is knowing what my uh project is we find
the project ID um Claude gets that project gets
details about that project ID finally finds this
um the actual project ID for this and it can call
get tasks just pausing for a second a complicated

[00:19]
software enterprise software project uh like Asana
you know has a complicated API structure and even
you as a developer or I as a developer might take
some time to go understand that but notice how
Claude is whipping through this very quickly and
it gets right at the tasks so all that happened
very quickly but we're not done with the overall
prompt so Claude's using that long range planning
that um capability to figure out what to do next
so it's got the tasks next what it needs to do
is to create an image if you remember the prompt
I said to create an image about that so no we're
not going to announce a image creation model from
Anthropic uh today but there are uh tons of MCP
servers out there that do image creation um and if
you're really deep in this MCP space you know that
most of those are actually local MCP servers like
intended to run on your local machine but this

[00:20]
support and the cloud AAI support is all about
remote MCPs so look luckily Cloudflare offers
an MCP remote service where you can take any of
these local MCPs and host it on Cloudflare in a
secure way and that's what we've done we've taken
one of the open source um MCP providers hosted it
on Cloudflare and then made that available to
the model and so the model chooses to call that
with uh when I made these slides the project was
definitely not in good shape so which is why the
the query is what it is um and we call that MCP
server and get a result back get both the image uh
URL as well as the actual image comes back in the
result and that both of those go back to Claude so
Claude now has the tasks it now has the image the
next thing it needs to do is send that email so
Claude will compose a email with all of that data
and then it needs to send it so in this case we're

[00:21]
going to use the Zapier MCP server zapier has
got hundreds of enterprise connections and a very
well-designed MCP system that lets you enable or
disable expose just exactly what you need and have
um uh enterprise control over that so we've set
it up to just expose Gmail uh and we've and the
model has chosen to use this subject and whatnot
to to make that work and so we get the response it
has it has sent that email and this is what this
is what it looked like more recently a little bit
happier a little bit happier picture but we did
we did actually get the email and this is very
easy to set up hopefully you're getting a little
bit of a pattern here a very composable system
it uses the existing messages API at this time
we're just using this new MCP servers attribute
and you can list as many MCP servers as you
need here um you just give the URL and a and a

[00:22]
name um and then you pass if you need if it's an
OOTH service pass the authorization token there
so we're very fortunate to have several
uh remote MCPs that are live today that
uh you can use with the MCP API whether you're
doing task management or you're doing payments
you're creating a video you're doing machine
management there's an MCP for you to get those
done uh so these are all available today
and then I'm sure tomorrow there's going
to be a ton a ton more and that's really what
Zapier has found interesting uh because with
our mutual customers we can now their their
customers can now build really powerful agents
very easily with a combination of our MCP API
support and and their MCP so let's look at a
demo okay so let's use this one um what are my
open task in a sauna just to warm us up make

[00:23]
sure we can get this so again what you're going
to see this time is that it calls the get asauna
um tasks so it's passing this and then we get that
nice list of ASA tasks and uh a nice response but
you know I thought maybe we should like pull all
of the pieces together here so hang with me with
this query create an email with a creative and
motivational image about my Asana project status
including some analysis on the percentage
complete and any news on the web about those
tasks and send it to the team so that starts by
going through uh a sauna getting the tasks uh out
of there um and then it's got to do it's got to
use code executor so it's now it's writing code

[00:24]
uh to analyze the status of all those tasks and
get our percent complete that being done it knows
what all the tasks are so now it does a search for
our conference finds the latest information maybe
a tweet from one of you will show up there um and
it decides to drill in a little bit more on cloud
for opus and sonnet so now it decides to create
that motivational image and notice the prompt it's
uh giving to our MCP so that's that's pretty
nice the rocket launching uh looks beautiful
now what it needs to do is take all the data
that you just saw um and pull that together
into like a really nicely formatted email and
that's going to take the model just a minute to
uh build this this entire email but it's going to
take that email and call the uh Zapier MCP service
and send it so hopefully any minute it will get
that email it's almost I can feel it okay there

[00:25]
it is so it's it's almost done thanks we have to
have that moment we have we have to have it um
so it's a little uh funny formatting here because
it's uh JSON HTML in this JSON viewer that we're
using here but it's generating this whole email
um and then of course the real tests if this was
like an actual live demo we'd expect like to
get an email so let's see if we actually get
this email so you can see we've been practicing
but yeah this is the one that we just Oh that
was 44 minutes ago let's see if there's a more
recent one yeah here we go this one zero minutes
ago there it is oh we got to show you real look i
mean we did zero prompt engineering on this thing
look how nicely formatted Opus comes up with this
email so really fantastic okay let's move back to

[00:26]
the slides um and I think I have to finish up
very quickly um MCB connector is uh remote MCP
simple to set up ooth support only standard
token prices okay let's drill into optimize
you can't really talk about optimization without
talking about prompt caching um prompt caching
lets you reuse part of your prompts uh that are
used frequently that saves capacity cost and
um latency and we've had customers say well your
five minutes of time between cache hits uh isn't
enough for some humans maybe walk away from
the computer and come back or some longrunning
agents so we've added a new option in addition to
the five minutes we launch with a new option of
extending that to one hour with the same um 90%
discount on cash hits um and batch processing

[00:27]
um is a great way to effectively process large
amounts of data and now that batch supports
web search code execution and MCP connector
it's not just for batch processing anymore
it's your async agentic uh API so you can get
a 50% discount for using that and you can build
async agents very quickly but we've also had
customers tell us that they need dedicated
uh they need um reliability dedicated capacity
to make sure that they can serve the needs of
their users so we offer as of today we're offering
customers the ability to com to buy uh a month's
worth of capacity uh at a discount uh and with
this 99% reliability so a discount for longer
commits okay so uh that's a wrap so we talked
about uh build clawed for long range planning

[00:28]
and code execution we talked about bringing your
data in with web search and MCP connector and then
we talked about how to optimize that with prompt
caching batch and priority tier so unfortunately
we're out of time but I will be out there for
questions so thank you very much for coming
[Music]
go go go go go [Music]

[00:29]
yep yep

</details>
