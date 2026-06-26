---
title: "Building signals that trade themselves"
channel: claude
url: https://www.youtube.com/watch?v=EOg4gY0Yln0
youtube_id: EOg4gY0Yln0
published: 2026-05-21
duration: "20:45"
---

# Building signals that trade themselves

[![Building signals that trade themselves](https://img.youtube.com/vi/EOg4gY0Yln0/hqdefault.jpg)](https://www.youtube.com/watch?v=EOg4gY0Yln0)

<details>
<summary>자막: Building signals that trade themselves (20:45)</summary>

[00:00]
I'm Sharan Fernando.
I'm head of data and AI at Man Group.
Man Group are an alternative investment
manager.
We manage over 200 billion dollars of
assets.
Our clients are pension funds, sovereign
wealth funds, and large institutions.
We manage real people's money.
Thousands of people's pensions and
investment capital.
So, when we think about AI, the stakes
are high for us.
Our clients are real people
from the teachers in Canada,
the metal workers in Japan.
So, we really need to get AI right.
If we get this wrong, we could lose real

[00:01]
money.
One of the really large parts of our
business is systematic trading,
and that represents a huge opportunity
to be aided by AI.
By systematic trading, I mean
algorithmic trading capabilities
that look across thousands of securities
and hundreds of markets to make
investment decisions.
So, systematic trading is really about
trading signals.
And you can think of a signal like a
fantasy football team.
You can think that we want to pick the
best players for our squad based on some
intuitive strategy.
So, the green bars here would be a
starting lineup.
The red bars would be the reserve squad,
the people that you don't want in the
team.
And the people in the middle,
they might come in, you might kind of
transfer them in, but they're they're

[00:02]
not the star players at the moment.
Maybe your subs bench.
So, a signal is really about thinking
about a striker maybe hitting form, but
you need to transfer them in before the
Friday deadline when the price might go
up.
And then you have savvy managers who are
really thinking about form, fixtures,
and what might happen to get the most
points in the season.
And they want to transfer the right
players in at the right time and at the
right cost.
So, this is
quite similar to systematic trading. A
trading signal is really just this with
stocks. So, the bars here would
represent company stocks.
We want to back the ones that would make
money,
and we want to short the ones that
won't.
So, in this example, we've ranked the
stocks by the past 3-month returns,

[00:03]
and we run that through history to see
if it would have made money.
The interesting question is always what
is that factor that you want to rank
things by? What's the strategy to get
the right stocks in your team?
And does it work?
And how do you know whether it works or
not?
Well, the truth is you never really
know.
I'd love to be able to tell the future,
but I can't.
So, the best thing that we can do
is look at what happened historically.
We run that strategy, we codify it, and
we run it against 15 years of history,
or even longer.
And what that does is it runs that
strategy through lots of macroeconomic
environments, through lots of stresses,
and we can see how it performed.
And that backtest produces lots of
statistical factors.
Some examples might be how much money
did it make? So, what's the annualized

[00:04]
return? When it lost money, and they
always do at some point,
how much did it lose?
And we call that a drawdown. And we look
at some even more complex statistical
factors. One's called a sharp ratio,
which compares the volatility of that
strategy
versus how much it returned.
And it's this process, this systematic
trading workflow, that we think that we
can use
AI to really enhance, to come up with
those ideas, to run the back tests.
And that has been our focus.
So, there are trading signals running
right now in production at Man Group, a
regulated investment firm,
running real capital
that were researched, back tested, and
proposed by AI.
By that, I mean humans came up with the
idea Sorry, AI came up with the idea. AI

[00:05]
got the data.
AI ran the back test. AI then wrote up
the strategy proposal. And AI
productionized the signal.
Humans, of course, reviewed all of the
output to make sure that it was
sensible.
But AI AI was at the center of that
process.
And I'm sure you want to know what was
that signal? What was that investment
idea?
How much money did it make? How can I
use it?
Sorry. I'm not going to tell you that
today. That's our IP. What I'm here to
tell you about today is our journey.
What was the foundation that allowed us
to do that? And how can you apply those
learnings in your company?
And it really starts with AI
understanding our workflows.
And to do that, we use skills.

[00:06]
Can I have a show of hands in the
audience as to who's written a skill?
Okay, that's great. Most of you.
So, coming up with the signal
is the quick bit.
The hard part is everything that you
need,
everything that's underneath it, all of
the workflows that make it happen,
that allow you to act on it.
Think of it like an iceberg. The signal
is the tip.
Underneath it are all of the workflows
that make it possible.
How do you clean the data? How do you
stitch prices?
How do you detect outliers?
How does it run? What's the
infrastructure it runs on?
How do you run those back tests?
And this is where it can quickly go
wrong.
If different teams are running different
versions of those workflows, you get
different answers.
One team's back test looks amazing.
Another team's looks average.

[00:07]
And because they're using different
workflows, you don't really know whether
it was the idea
that was better in one team than the
other,
or whether they're just measuring things
differently.
Shared workflows fix that.
One common foundation
means that effort isn't duplicated, and
you have consistency. The outputs are
comparable. And that's extremely
important in systematic trading when
we're comparing signals.
Out of the box, Claud is an amazing
general-purpose tool.
It does a lot, but it doesn't know us.
It doesn't know our data.
It doesn't know our systems. It doesn't
know how we work. And it's the same for
everybody in this room.
So, the first thing
that we had to do was teach it.
Not by retraining it.

[00:08]
Not by doing fine-tuning.
But by giving it access to our data,
our capabilities,
and our workflows.
That's our superpower.
We have decades of institutional
knowledge and systematic research. And
some of the best technical capabilities
on the street.
And if we can connect that with AI, then
AI can leverage that superpower.
Skills are the connective layer
that allow AI to leverage that
superpower.
So, getting them right is paramount.
And that was our focus.
But we got it wrong before we got it
right. And I want to tell you about our
story today.
We really focused on adoption. We went
all-in. We were doing skills workshops.
Anthropic helped us with that. We were
doing hackathons. We wrote a blog. We

[00:09]
were doing show-and-tell sessions.
Everybody was writing skills. The
adoption was really out of this world.
But we started to see some cracks in our
approach.
It was really the power users that were
building the skills.
It wasn't the process owners.
And
what that meant is that all of the
skills really represented a local
optimization for one user. They weren't
common organizational solves.
And nothing was really more symptomatic
of this than when we ran one of the show
and tell sessions one day, and there was
a guy who used to travel a lot at my own
group, and he had loads of expenses to
do. He spent loads of time doing this.
So, he wrote a skill for it. He gave
lots of pictures of receipts to Claude,
and it would do the expense report for
him. And he brought this to the show and
tell session,
and he even shared it with a few people
in his team, and it was working really

[00:10]
well.
And then a few days later, the expense
approver came to them and was like, "Why
is Claude creating so many expense
reports for my cost center? People from
technology, people from the people team.
Why do I have to approve all of them?
Like, I'm in sales. I I don't want to
approve everybody else's expense
reports." And we dug into it, and it was
just because the the cost center code
was hard coded. And it was really just
that that was this um this local
optimization.
Nobody had reviewed that skill. It
worked for him, it worked for his team,
so it was going to work for everybody.
But that's not the case.
And he wasn't accountable for that. He
kind of thought it was quite funny, and
I mean, so did I, to be honest.
Um but it was really symptomatic of a
broader problem.
People were just codifying their ways of
doing things. They weren't the
organizational ways of doing things. And
in many cases, they weren't actually the
workflow owner.
And this is a huge problem when it comes
to things like back testing and

[00:11]
systematic trading.
It starts to become a blocker to you
scaling to enterprises.
Agents can't leverage those. There's no
commonality.
And we saw that something had to change.
Has anyone else faced this problem when
they've been writing skills that it was
actually the process, it was the people
who were the power users of a process,
rather than the owners of it, that were
writing the skills? Can I have a show of
hands for that?
Good.
Yeah, we really saw that across the
board.
But we saw that skills governance
started to be the secret sauce that
unlocked these enterprise use cases.
If you could connect your common
workflows
to AI, give it access to your data and
your capabilities,
you could really allow agents to act on
those skills.
And if you can do that, you can allow

[00:12]
cloud code
to do problems as complex as systematic
trading.
So our solve this was to have a common
marketplace.
Every skill was visible, tagged, and
tested with evals.
We wanted to ensure consistency.
Imagine a library.
It captures decades of institutional
knowledge.
There are sections for the finance
department, the people department, the
research department.
We care for every item. We care for
every skill in those departments.
The skill is owned by the workflow
owner.
They're all tested, usage is tracked,
they're all reviewed. They have a life
cycle.
And they're all visible to everybody to
install.
It's really that care that makes this

[00:13]
work.
And it's the foundation that moves
skills from individual productivity
solves
to a foundation that can set you up for
the agent to cage.
And it's through that that we were able
to apply skills to systematic trading.
So now, I will give you a bit of a
flavor for what it's like to build a
systematic signal. We've We've a demo
and a video on that.
>> This is Man a knowledge.
It's where you'll find our collection of
skills and Man Group's context store.
The skill suggestions are tailored to
each business unit. They have clear
ownership and are organized into managed
and community skills.
Skills and plugins can easily be
installed in Claude. Plugins are useful
groups of skills. For example, here we
have a data plugin which gives us access
to Man Group's data sets.
We can also skills individually. For
example,
this is the data set skill

[00:14]
which allows me to search Man Group's
alternative data sets.
Now those foundational skills are
installed, we can start to get a flavor
of what it's like to build a systematic
trading signal.
We can use the alternative data set
skill to search for research such as
credit card data.
We ask Claude, what credit card data
sets are available and it identifies a
data set of US consumer transactions.
We can plot Amazon's monthly credit card
spend against its stock price returns.
These are the results of the credit card
data compared to the stock price for the
same period.
The blue bars are credit card spend and
the line is the stock price.
Interestingly, in the graph, you can see
spikes for seasonal spend such as Black
Friday and Christmas.
Next, we run a back test to see if
credit card spend is predictive of the

[00:15]
stock price by comparing the peaks in
credit card spending with the profits
and losses of the stock.
In the results, the signal shows better
performance than a buy and hold
strategy.
We can see that investing $1,000 in 2021
using the signal would now be worth
around $2,500.
This could be a fluke for Amazon, so
let's run it on a broader universe of
retail companies.
As there are multiple companies, we'll
run it using our distributed compute
infrastructure.
Each company is running an individual
worker, and then the findings are
collected.
In this case study, we leveraged four
skills to create a systematic trading
signal.
In reality, our signal research is much
more nuanced, accounting for things like
seasonality, inflation, and broader sets
of securities.
We do this with agents as well as humans
exploring these ideas.
The key takeaway is that the governance
of these skills is key. It ensures that

[00:16]
everyone has access to the same data,
and everyone uses the same workflows.
>> Okay, so hopefully what you can see is
that if you get that foundation right
across the board,
if you've got access to all of the data,
you can start to leverage more
capabilities. Everything from scaling
your compute to getting alternative
credit card data sets. And these are
often owned by different teams.
And it's really that that allows you to
scale to the Agentech platform.
So, what did we learn along the way?
These are the things that I would tell
past me, and that you can take away.
Firstly, focus on that organizational
context.
That is your IP, it's your moat. It's
one of the few safe spaces left in AI.
The frontier labs are not going to solve

[00:17]
context for you. It's not on the
internet, they don't know your
workflows, and you already have that
context.
You have decades of it.
The work is on exposing it, not
reinventing it.
And skills are how that those decades of
institutional knowledge become
leveraged.
Treat those skills like production code
because that's what they will become.
Plan your approach before you plan the
rollout. Who's going to own the skill?
Who's going to review it?
How does it get retired?
How does it get tested?
Decide this be sure before shipping the
first skill, not after the hundredth
like us.
Adoption is not a licensing problem.
It's a people problem. Once you've got
that platform in place, you need to
encourage people to engage with it.
We need to really think about how we

[00:18]
capture that organizational context and
rethink our workflows rather than just
augmenting them.
And that's a training problem. It's an
engagement problem. So you really need
to outreach to people who are using this
platform.
And it's through this it's through these
ideas that we've been able to scale. Man
Group's about 17,800 people 1,700 people
something like that. And we now have 750
of them using Claude Code across
developers, quants, the people team, the
finance team, everybody across all of
the departments is using Claude Code.
We're seeing a lot of engagement
because they're able to use those
capabilities in a simple way. They don't
need to know about everything. They have
the skills platform
that understands our workflows.
We now have over 100 governed skills and

[00:19]
at least as many community skills
that are looked after in a library
and they're well governed.
And what this has done is it has allowed
us to unlock the capability
to use AI in systematic trading.
So, skills governance really unlocks AI
at that enterprise scale.
The thing that I'm most proud of
is that I feel that we've got our eyes
on the prize.
We have a solid bedrock
built on decades of institutional
knowledge.
And in the not-too-distant future, I can
see us having swarms of agents
leveraging those skills to look for new
investment opportunities.
So, what's the takeaway for you?
Really think about how you're going to
capture that context.

[00:20]
Which department owns it?
What's the process for governing them?
Where will they live? How will you test
them? How will you retire them?
Connect a golden path from your AI
platform to your capabilities and your
context.
Once you have that basis of knowledge,
if you care for it and AI can leverage
it,
that will really set you up for the
agent cage.
Thank you very much, everyone.

</details>
