---
title: "Scaling interpretability"
channel: anthropic-ai
url: https://www.youtube.com/watch?v=sQar5NNGbw4
youtube_id: sQar5NNGbw4
published: 2024-06-13
duration: "53:18"
captions: en-orig
---

# Scaling interpretability

[![Scaling interpretability](https://img.youtube.com/vi/sQar5NNGbw4/hqdefault.jpg)](https://www.youtube.com/watch?v=sQar5NNGbw4)

<details>
<summary>자막: Scaling interpretability (53:18)</summary>

[00:00]
I'm Josh Batson and I'm here with other
members of the interpretability team at
anthropic to talk about some of the
engineering work that went into our big
recent release about interpreting the
insides of Claude 3 sonnet so why don't
we start with some introductions
Jonathan who are you I'm Jonathan Marcus
I have worked on the interpretability
team for a amazingly long eight months
uh prior to this I worked at Jump
Trading doing quantitative Finance for
like 13 years great adley uh yeah my
name is adley I'm also on the inability
team I've been here doing Nary learning
stuff and Spar out cter stuff for about
the last 14 months before this I was
working on efficient large lingo model
inference at another
startup TC yeah and I'm Tom or or uh TC
I've been on the inter team about the

[00:01]
last year working on the on dictionary
learning before that I worked at at the
same company Jonathan did so jump doing
doing uh high frequency trading and uh
before that I was at at Facebook for 5
years doing kind of backend infer work
there so the reason we're here now is
because there was a big interpretability
release recently what were you trying to
do there and
why yeah I think that the the best way
to describe this is that back last year
we published paper called towards mono
semanticity which really demonstrated
that this technique could work to
extract interpretable features on a very
very small language model and then in
the month since then we've just been
scaling this up until we reach the size
of getting really good features from one
of the models that is deployed into
production by
anthropic help me understand what's the
difference between like a small language
model and the one you were tackling for

[00:02]
this
work yeah the the the SK the small one
would be so different from any language
model you've actually use like if you
tried to ask it any sort of question
that you might think a a language model
would be very good at it's going to
totally fail fail everything it's just
kind of a very very poor model so it was
helpful for the early work work we were
doing because we think it has a lot of
the same structure as a as a large model
but it's much smaller so it's much
easier to work with but it's kind of not
useful for any actual task and even if
you asked it uh a fairly basic question
like uh like uh what do cats say I'm not
confident it would actually get that get
that right it wouldn't meow no I don't
think so but maybe we didn't actually
try someone said a good analogy which is
like eight months ago we it's like we
said hey I think the earth is made of
dirt and so I like we had a hand drill
and we know went a couple inches down
like hey there's dirt there and now we

[00:03]
made this like giant laser drill and
went into the Earth's manle like hey
there's lava there and yes I know that
person was
you somebody
somebody uh I think that's a really good
I that when you said that it really
stuck with me because it's like yes it's
technically the same thing and yes we
expected there to be Lava but it's just
been a huge engineering effort to
actually D drill down haha and figure
out what's down there and we've actually
found a lot of what we expected but it's
really cool now that we're there I think
the thing that I want to add there is
just how rewarding it is to look at
these large language models that can
actually do all of these really powerful
things so in the one layer model we were
finding we were finding features but the
features corresponded to things like
counting to 10 and generating the r

[00:04]
string of letters and numbers that you
see after URLs and when you when you
scale this up to a much more powerful
model the same technique can find
features that really just are
interesting not just from a scientific
perspective but that just represent
interesting Nuance topics and that can
really just shine a light into how this
system is able to perform really hard
tasks and in particular large language
models can perform tasks that we don't
know how to program computers to do they
really just like have all of these
capabilities that we don't understand
and so if you can find the features from
them then you can really get this really
fascinating insight into how they are
able to do these
things what are some of the features
that you saw that were the most like
striking or moving to you I really liked
the um functions that add numbers in in
a code feature and that it was kind of

[00:05]
not not very narrow and not just firing
on functions that are kind of obviously
a plus b but if there's some function
which calls some other function which is
which is adding then the feature also
lights up for that so it has some like
deeper understanding of what a function
that ads is than the very basic one uh I
thought that was that was super cool and
maybe surprising that it exists but for
a lot of these features you kind of when
you first see them you're shocked and
then when you think about it more you're
like oh yeah that seems like a useful
and very reasonable thing for the for
the model to like do maybe I shouldn't
have been so surprised that it was there
I remember first
finding the this veganism
feature
that it's it was really cool and I did
not expect to see it it was not even the
biggest model and I'm not a vegan
but
disclaimer uh but it was really
interesting to see that this same model
could identify the concept of not eating

[00:06]
meat of being worried about factory
farming and uh wearing like not wearing
leather but also in a lot of different
languages and the fact that I was able
to tie all of these Concepts together
was a I like couldn't believe what I was
seeing the model
actually you know it's not just
repeating patter it's not just repeating
arbitrary words in some random in some
random way it like definitely very
concretely this model this connection
was already built into the model and we
just discovered it in there and that
just that really blew my mind yeah I
think one of the things which was kind
of impressive for me was getting a sense
of like how the model is thinking about
this stuff I think when language models
first started getting big there there
was some notion that maybe they're just
repeating things they've seen in the
training data and when it says something
it's because there was an extremely Sim
ilar sentence out there and it just kind

[00:07]
of grabbed that and then gave you
whatever somebody said in that context
but seeing these features that are like
multimodal multilingual about something
what what do you mean multimodal
multimodal I mean that the image of the
thing um makes the same feature fire as
the text of the thing one of my favorite
ones there was there was a feature about
back doors uh in in code that also fired
on images of like uh hacked USB thumb
drives and various forms of
subterfuge yeah yeah it it I think there
were like five or six different devices
with like hidden cameras in them and it
fired for like various various hidden
cameras in in like in like everyday
objects which again in hindsight seems
like totally like it makes total sense
but I I definitely wouldn't have guessed
that right you the part of the model
that literally recognized like a line of
cod that had a problem would would be
the same thing which is like there's a

[00:08]
pen with a camera in it yeah and then
even you could act you could like
artificially activate that and say hey
can you finish my function and it would
write it while introducing a subtle
vulnerability that could be uh that
could be hacked
later that one really blew my mind I did
appreciate that Claude was kind enough
to label the function back door
any other any other favorites can we
talk about Golden Gate Claude yeah I
mean Golden Gate Claude
was was so much fun first what is Golden
Gate Claude what is Golden Gate Claude
exactly uh Golden Gate Claude was so we
had a feature in the paper it was kind
of the headline and we really liked it
where Claude would uh activate on
descriptions of the Golden Gate Bridge
uh you know the iconic Majestic towering

[00:09]
bridge between uh mirand and San
Francisco uh so someone had the amazing
idea of hey do you think we can talk to
Golden Gate Golden Gate Claude and this
was my favorite Parts about anthropic I
thought this was going to be hard but
then someone from the engineering team
just went into our code
base figured it out and implemented
Golden Gate Claude
as an experiment like hey do you think I
can
actually take the results of your
dictionary learning paper and just use
it and then we tried it and it and it
worked and then everybody started
playing with it that was such a cool
experience to actually have the results
of our paper brought to life like that
yeah it was incredible we put out the
paper on Tuesday morning and then we
were all out to dinner on Tuesday night

[00:10]
and people inside the company were
excited by that figure where when we
turned on the Golden Gate feature and
asked Claude what is your physical form
Claude said that it was the Majestic
Golden Gate Bridge itself and that was
just like a little static thing and and
and Oliver was like let's do it let's
make Golden Gate claw and while we were
eating and celebrating they started
working and 36 hours later there was a
polished product that be shipped and the
world got to like talk to a model that
had this feature we discovered only
weeks before Amplified and getting a
feeling for like what it what it means
to kind of Drive the model in One
Direction or another
so um I know the model was really big
cla's really big compared to the ones we
were working on before um what did you
have to do to take the the dictionary
learning technique for finding the
features
and and scale it up to work on something

[00:11]
like that man yeah first of all I just
want to say this is a really long
question to answer because this was
probably the bulk of our work between
the publishing of towards monos
semanticity and the publishing of this
paper like this was just there were just
so many things and we should get into
them but I just want to emphasize that
we are just not going to be able to talk
about a fraction of the things that had
to be done here because this
was this was is just such a really big
effort I also want to like frame it
slightly differently like like when when
we first got the results in in in
towards mono semanticity and we started
thinking about what we're doing next we
didn't immediately go Oh we're going to
scale this to like Sonet this will
definitely work like we didn't know if
this would work at like larger scale so
we didn't want to spend you know eight
months just like just like scaling and
then check if it actually worked so it
was it was much more of a like kind of
back and forth between the engineering
side and the and the research side to

[00:12]
kind of what experiments can we do to
scale this up to give us more confidence
that scaling it up actually works so it
was kind of not this like monolithic
thing that we could just plan it was
something where we we were kind of
scaling it in pieces confirming that
this that this still looks good and then
and then scaling it more as we as we got
more
confidence so what what is scaling
actually look
like so I think one example here is I
very illustrative this is something that
came up pretty early on in the process
as we're scaling this up where when
we're working on towards mono
semanticity all of our models fit on a
single GPU every sparse Auto encoder
that we trained fit on a single GPU and
what we realize very quickly is if
you're going to keep scaling this up
this is no longer going to work you're
going to have to chain a bunch of GPS
together and imp M something that we

[00:13]
call op sharing where you take the
parameters of the sparse Auto encoder
and distribute them among a large number
of
gpus can what is a sparse Auto encoder
maybe not everyone knows what they are
so an autoencoder is something that
takes in some data some vector and
transforms it into another
representation from which you can read
back the original that's the auto is
that you get back the the original
encoder is you change the representation
a sparse Auto encoder is one where this
new representation you get is very
sparse there's only a few elements in
there that are nonzero and this can be
really nice because if you're trying to
understand what does this data mean and
there's exactly three non-zero elements
in the encoding you can just go look at
each of those whereas if the original
Vector had a thousand components or or
something might not make any sense and
the basic bet we made here which is
shocking to me that this worked at

[00:14]
all was we took some of the latent
States the vectors inside clae trained a
sparse Auto encoder to see if we could
represent those as a sum of just a few
pieces each time and the answer was yes
and then when we looked at each of those
pieces they were shockingly
interpretable um from a math perspective
I think a sparse autoencoder is really
simple there's just two matrices
involved D um from an engineering
perspective I think it proved to be a
lot less simple and so you could write
down the math from our paper in October
and we could copy and paste basically
the same math to our paper now and that
is not how it worked like on on the
Silicon oh my
God I think one of something that feels
really interesting here to me is that
when we first started this project last
year we were experimenting with a bunch
of different techniques for this and we
were experimenting with a bunch of more

[00:15]
complicated techniques there's a lot of
fancy math out there that addresses this
problem it's possible that that math
might still work better but we really
just saw a lot of success with sparse
Auto encoders because you could just
really scale them up we tried running
all of these other techniques but you
could only run them on a small amount of
data and one of the things we realized
is that in order to see really good
results you have to run this on a of
data much more data than anybody in the
classic mathematical literature ever
does and so sparse Auto encoders are in
some way just mind-bogglingly simple in
a pretty beautiful way and it's just
this philosophy that if you take a
simple algorithm and it's scalable and
you can just really turn up the numbers
you can get really beautiful stuff out
of
it but turning the numbers up
like that's the hard

[00:16]
part I I don't I do almost no
math you do math you do math but like
there's so much so much goes
into hey let's make this thing 10 100 a
th000 x and so on
bigger and that just breaks all our
abstractions breaks all our code in so
many different ways it's it just becomes
too big in all these Dimensions that you
didn't that you were totally unprepared
for it causes weird bugs I think one of
you told me one of those Dimensions was
around like shuffling the data someone
talked through what the shuffle problem
was and and what you had to do yeah so
there's this penly hard problem in
machine learning where you have your
input
data um and you want to make sure
that you're if you've got like a whole
bunch of A's and a whole bunch of B's

[00:17]
and a whole bunch of C's and a whole
bunch of D's and you feed them through
your model if you just feed them in an
order it's going to learn hey I should
only learn A's hey I should only learn
B's uh but if it's all mixed up then it
has to learn the whole distribution at
every
step and this Shuffle process is very
easy when your data is small you just
you load into memory you know do like
random shuffle and then you write it
back out
that's not that hard now you have what
do you do when you have pedabytes of
data it's like
oh oh so um I guess it might be like if
you have to shuffle a deck of cards you
can just do it with your hands yeah and
if somebody gave you seven consecutive
miles of cards stacked end to end it's
like not clear how you would Shuffle
that deck yeah at all that's a really
good analogy so uh right it's like I
have 100 warehouses full of cards yeah

[00:18]
and so we did I ended up like we talked
about a lot figured out hey is there a
way to do this in parallel and it's
like well if you're going to shuffle 100
warehouses of cards first you're going
to shuffle one Warehouse of
cards uh and you know break it up into
100 sub problems and then how do I
shuffle 100 one Warehouse of cards I'm
going to break it up and like do it by
section and then you're going to like
mix the different sections in
some in some like Pro
proably uh it's some provable way that
Mak sure that every section gets mixed
with every other section and like I
don't know that's that sounds really
simple uh in a sense it kind of was once
once we had understood the problem that
oh we just need to make this like
multi-stage parallel Shuffle where we
break it down like oh probably anyone
could not anyone but like a lot of
people can like imp that is part of like
a coding interview it's like not that

[00:19]
hard of an algorithmic problem but to
get to the point where we even realized
like
that oh just just framing the problem
was 90% of the work once we did that and
we could conceptualize it as oh we need
to do a multi-stage parallel Shuffle and
then once you get your like recursion
properly defined then it's a pretty easy
task to scale it to something oh you
want to do 100 terabytes you want to do
10 pedabytes cool just add another
another layer I think some more context
there is interesting because we're kind
of focusing on when like the part after
we decided we're going to speed up
Shuffle but I think the part before that
kind of shows a lot of what this job is
about where what was happening is we
were scaling things up and then and then
running running running experiments as
we scale and the shuffle step before we
we made it better was taking longer and
and longer so we knew that like this
step is not scaling well and it's making
it slower to get research results but

[00:20]
also we know there's something better
there but there wasn't something that I
could do in like a couple hours I was
like oh this is maybe a few days a few
weeks so we're kind of putting it off
because we can still get get get
experimental results until eventually
this thing's taking you know 24 hours
something like that and we're like okay
we finally need to like fix that and
then I think the fix that we did you
kind of could do something that is maybe
like more like perfect or totally nail
Shuffle but we're not focused on like
what is the like Optimal the platonic
ideal of parallel Shuffle what we care
is our job's taking 24 hours how can it
not take take 24 hours so I think a lot
of this job is like we want to get to
get experimental results that's that's
our focus and then given that goal how
do you get those so it's generally not
how do you make any step perfect it's
how do you make any step as good as we
need to to get the results that we need
right now and then as those results come
back you gain more or less confidence in

[00:21]
the approach which you have and as you
have more confidence that this codebase
and this and this approach is something
we're going to be using six months later
a year later you you're willing to
invest more time into making things
better and I think the kind of the heart
of the job is how do you make that
trade-off of how much time to invest
into any one piece of this of this of
this whole pipeline I I want to draw
that out more it sounds like this kind
of engineering where an experimental
result at the end feels like a different
process than maybe you know producing a
product like could you say more about
about what it's like to do engineering
for
research yeah I I think it's interesting
to to compare it to to my first job at
at at Facebook and I was building a
service a backend service which like
powered the the like Facebook website
and I would say the big difference is
kind of the requirements of the code um
at that at that job at Facebook it never
really changed we always knew that this
was going to run at scale it it like it

[00:22]
like couldn't couldn't crash we like
cared about the like cost of the servers
we were running on but I was there a few
years and it was kind of always the same
goals where in in a in a kind of
research engineering job now like you
don't know which bits of the code you're
going to be throwing out in two weeks
and then which bits of the of of the
code you're going to be using like years
later and a lot of the like original
dictionary learning code was methods
which we've like deleted they're gone
we're like never touching it and
spending time like making that code
perfect would be totally wasted because
it's uh it's uh deleted but also like
over this year-long process we've kind
of honed in on what we're doing is
working and this core thing is good we
need to make this better we're going to
be using this longer and if the if the
if the code quality is crap like it's
going to be slowing us down for like
years so we need to to like really go
and like and like polish this more so I
think you kind of constantly have to be
have have to keep those trade-offs in
the back of your of your head and
they're kind of changing changing under

[00:23]
you like as you
work there's another dimension to this
that I'd like to talk more about which
is there's a whole bunch of ideas that
we want to try and when you're looking
at implementing these ideas you're
thinking about how to design the
infrastructure and like with any
software design certain infrastructure
designs are going to make certain things
easy and certain things hard so there's
this really tricky thing and I think in
some ways it's an impossible problem and
you can only try to do this very poorly
but trying to
anticipate which directions you want to
go in in the future trying to
anticipate what general categories of
ideas you might want to try and trying
to anticipate how do we make these
General categories easier and what are
we closing off what what are we making
harder to do and trying to make those
tra offs is a really really difficult

[00:24]
challenge
that
we try our best at but is something that
is just impossible to be perfect at did
you make any big
mistakes
none I think a lot of the erors here
feel more like we maybe should have
cleaned something up a month
sooner so it's it's it's kind of like oh
maybe we should have done this sooner
but but because your your your kind of
your trade-offs are changing under you
if you should have like if right now
you're like uh I'm not really sure
should we do this should we not do this
in a month it's frequently blindingly
obvious like oh yeah we should
definitely do that so you do lose that
month of like it would have been better
if you got there sooner but I generally
think you kind of get shoved in the
right direction
eventually but I I also think that
there's an important point that I am not
a Prof professional scientist where I'm

[00:25]
just looking to publish papers I'm also
not a professional engineer where I'm
just looking to build the most perfect
beautiful harmonious well abstracted
system like we have a specific Target
which is you know being able to figure
out and do enough science to figure out
interpretability so that we know how
these machines work to achieve a
specific safety
goal
that we have to do enough science to get
there we have to build enough engineer
ing stuff to support the science But
ultimately it's it's quite possible at
the end of the day we will throw away
every single thing we've built except
for that one end result and so I don't
want to spend any additional time
researching stuff that's not going to
help I don't want to spend any
additional time building stuff that's
not going to help and like getting that
tradeoff is super hard I'm not always so
good at it but you guys are so thank
it's also always easier in hindsight
yeah
so what was the what was the most

[00:26]
confounding bug in this
process yeah so one of the really
dangerous parts of machine learning and
especially when you're doing machine
learning on this weird undiscovered
topic is that it's really hard to know
if you've written your code right I
remember my machine learning Professor
told me this in college and I'm like
that doesn't seem so hard this like
can't possibly be such a big problem and
then you realize that this is just the
thing that is going to eat up more of
your time than any other problem so we
had cases where you know we just lost
weeks of effort because we had something
and the we had some evaluation metrics
and the evaluation metrics are bugged in
a way that makes them too good to be
believed and really exciting and we
spend a lot of time chasing that down
before we realize that there's just some
really subtle
bug in our metrics and it's very hard to
test for that and you you basically end

[00:27]
up needing to spend a lot of engineering
time trying to make sure that these
things work and that you can trust your
evaluations here bugs and metrics are
scary because if you're trying to make
the number go down and the numbers going
down you're like this is great
everything's great and then it turns out
you were just like chasing a complete
illusion for weeks so how do you deal
with that like what is it tests like
what's testing like for for kind of
research research code I think I think
kind of uh correctness bugs like that
are very difficult to test because it's
kind of not clear what the correct
answer is so your your like classic unit
test kind of doesn't really cover this
well I think the thing that helped here
was to uh like kind of log as many
metrics as you possibly can can you
while this uh process is is like
training can you think of every possible
number you can like log and then graph
those and then for your runs you can at
these graphs and be like what should

[00:28]
this look like does this make sense and
I I I think there's no easy answer here
it's just time I think the other piece
of this is just really going through the
light the like code carefully and being
like I know what like the math for the
ml says uh this should be doing but like
what is it actually doing and we've had
a number of times where that where that
didn't match and I think tracking those
down is is a very important thing and I
would also say that that like there's
kind of latent bugs in master that
you're worried about I think there's
like another way that this comes up of
every time you have a new idea for how
the ml will change you code that up and
you run it and then sometimes the
results are like oh this is worse than
than your Baseline and you're not really
sure was the idea bad or when I coded it
up was it bugged and you don't know and
I think that's kind of a difficult
trade-off of what to do next because you
can go and you can stare at the code you
can go and stare at graphs and try and

[00:29]
understand like like does this thing
like was it bugged in some ways but at
some point you have to decide this idea
doesn't work and I'm giving up and I'm
moving on to like something else one of
the Striking things for me who is more
of a science background working on a
team of really skilled Engineers has
been realizing the power of like pulling
some of the engineering work forward to
increase your iteration time and I think
that the more the more that your ideas
matter you know then you want to spend a
lot of time thinking but if you have no
idea of what's going to work or not then
making it so you can test a lot of ideas
quickly really pays off and this kind of
Relentless looking at how would I run
this experiment okay could I run that
experiment in a day instead of in a week
could I run it in an hour instead of in
a day could I kick it off in a minute
and like your ideas might be better but
like no no one has ideas that are
like 200 times better such that you
would rather you know take that long to
to run an experiment speak for yourself
I think this comes back to the shortterm

[00:30]
versus long-term tradeoff which is I
think really just like one of the
fundamental tensions about doing this
sort of research engineering where you
have to decide how much effort to invest
into making things better long term
versus how much you want to just try
something try it in the hacki possible
way and get results quickly and I think
that unlike in unlike in a lot of
traditional engineering you don't just
want to lean all the way towards the
long-term thing it depends on a lot of
factors it depends on how confident you
are that something in this general area
will work it depends on how reusable do
you think this infrastructure is going
to be in the future and how easy is this
going to be to cat up and get working
really well but it's also you know
informed by the science of do we think
that dictionary
learning is a process that we should be
going so all in on just is having the
the like the faith Guided by our

[00:31]
scientific intuition that if we keep
pushing here we're pushing blindly like
we don't we don't actually know if we're
going to be going towards anywhere until
until we you know drill down far enough
and oh there's lava like it's just it's
just a lot of dirt and then all of a
sudden
you you like pull back up and you
realize oh my gosh we've actually gone
so far
and we've actually found something but
for a while you're just fumbling in the
dark and like nothing works nothing
looks good nothing makes sense but you
just have to believe that like if we
keep researching in this direction like
maybe there's signs of life and
eventually we're going to see something
useful personal question why do you like
doing this work so for me in my previous
roles I I um at at the company used to
work on on the inference team so the
inference team is there is much less of
the search aspect of it we kind of know
exactly the operations that that that

[00:32]
need to be done the like math and we
just need to make them go really really
fast and it is it leads you to these
really interesting kind of systems low
low lowlevel GPU optimization problems
but to me it's like I can kind of plan
out what the next six months will will
look like you can kind of figure out
we're going to design it exactly like
this and we need to do a b c and d and
you have this like exact plan and then
you go and do it and I kind of found the
work of doing that exact plan a little
tedious or boring there are plenty of
people at the company who love that I
just don't personally where on this team
like we can't plan 6 months out right
and we don't know what to actually build
and and you're following where the
research results lead you and kind of
everything's constantly changing so I
really love that that piece of this job
adley what do you like about this work
yeah I think there's two questions there
which is why I love the research part
and why I love the engineering part
because really I love both of them and I
love the research part just
because honestly there's no better way

[00:33]
to describe than this it's just a really
beautiful problem and it's really
fascinating to try to understand this
and it feels amazing when you can shine
a tiny little bit of light in the black
box of models one of the things that I
like about this is the engineering is a
lot of fun sure but it's also the
problem itself it's like and this goes
back to why do I like how does this
compare
to my previous job doing Quant Finance
versus
this studying markets was actually very
fascinating
the the there they're always changing
there there was a lot of interesting
modeling to be done but here we're
essentially doing like computational
Neuroscience on an artificial mind and
no one's ever done that before in
history because these have never existed
and no one's ever done we're like among

[00:34]
the first people right now to ever have
access to artificial Minds as big with
the amount of computational
infrastructure that it takes to analyze
them we are literally like trying to
figure out how these things think we are
studying
cognition in a very quantitative way and
that's it's so mind-blowing to me that
almost the same skill set that I was
previously using to predict the next
price now
becomes decoding
thought
and I loved Finance for many many years
but this just feels so much more
meaningful to me and I think the really
exciting part about trying to tackle
these problems with engineering is that
it makes them
solvable if you ask yourself how do you
do neuroscience and an artificial mind
that's not the type of problem that

[00:35]
you're really like going to solve or
maybe you could solve it but you're
going to you don't have high confs in
anything there is something about
building the infrastructure to do this
and building the infrastructure to do a
lot of experiments that makes it feel
possible to say we are actually going to
do this engineering is just a way of
making this successful and making this
possible so so uh for the people
listening to us who think this sounds
kind of
cool uh do you have any advice about
getting into you know into
interpretability research uh or AI
research from an engineering side the
first thing I'd say is I think a lot of
people uh think the work of the
interpretability team is much more uh
needs much more of the research skill
set than it actually does like the
research skill set is important but the
engineering skill set like really really
matters too so we are not just looking
at people who have only done like math

[00:36]
and and like ml we need people who are
who are very strong at like coding too
and like currently we're bottlenecked by
hiring kind of very very strong
Engineers so we need more people like
that kind of asking us for for for uh
for jobs would be the first thing um
what what you can do if you're
interested in this and you're a great
engineer is ask us for a
job because we are hiring people like
you that's silly but I think I think
it's very easy to underestimate the
contributions that you're able to make
especially if you think of yourself more
as an engineer coming into this and I
really the advice is just to apply the
other thing I would note on the on the
engineering skill sets kind of what
we're looking for what people might
learn is that I think we need a lot of
breadth of that we are not like we need
to make gpus go fast for the work that
we do but we're not pushing things to
the to the to the bleeding edge right so
we need people who can kind of do a

[00:37]
bunch of different skills and come in
and and notice like oh I can do a quick
change which gives us a big win we
aren't people who we aren't really
looking for the skill set of I can spend
two months to to use the graphics card
10% more more efficiently here we're not
going to spend two months on that we're
going to move on to to to like
paralyzing other jobs figuring out why
some python code's really slow so you
kind of need this breath to be able to
figure out out like which point in this
complicated pipeline is the bottleneck
right now and let's go make that like a
bit better in a few days is is kind of a
big skill that that that we'd really
love to see more of yeah it seems like
the team has a lot of full stack
engineering where the stack you know
goes down to like you know you could do
fuse GPU kernels and all the way up to
building front-end interfaces for like
looking at how images make CLA talk
differently and that you never know
where in that entire chain might be the
thing you need to do you know there was

[00:38]
a I remember a frontend bug the other
day that actually turned out to be like
an OP sharting bug so you thought this
might be okay the the server like is is
rejecting your request and then it just
turned out that no actually we had
shuffled around these tensors in a
transpose way and and that needed to be
what's fixed and so um it's it actually
means there's a ton of ways to
contribute and also this kind of breadth
and fluency uh can really pay off so so
Josh you're you're a scientist
more than us like on the I'd say we all
shade pretty on the engineering
side what's your biggest frustration
with people like
me I mean people like you are so
Charming um no I don't think I don't
think there's a there's a there's a
frustration I think it makes for very
good collaborations um because often
times you know we're we're so early days
that there's there's often a lot of room
for improvement and sometimes it turns

[00:39]
out that like we should just be like
plotting the correct metric or um
changing the initialization scheme for a
matrix that could also speed up the
training process by 5x and it could be
that that you need to speed up the
training process by 5x by
parallelization and so I think that
there's just these opportunities this is
what I mean by the full stack actually
continues all the way into like the
mathematics and all of these pieces of
it so I think that um um it's really
helpful to have a very interdisciplinary
approach to this stuff because sometimes
you can you know sharpen the exper like
did you really need to run your
ablations over the entire data set or
you trying to estimate a scaler at which
point statistics tells you you need a
thousand samples and then you're like
pretty much good and you can save save a
lot of time I think
also I I've actually really enjoyed the
even though you're on like separate sub
team so I don't get to work with you
nearly enough I really enjoy the few
times that we did get to collab right
cuz I think we have such complimentary
skill sets where i' I've said it before

[00:40]
I'm not that great at the math I don't I
still don't know ml sorry guys I'll
leave but
like I really like the culture of
collaboration that lets we're like you
and I will just sit together and pair
program on a problem and we have very
complimentary interests and skills where
when we work together we are just
like very very powerful and I think that
that's a lesson the reason I bring this
up is for people considering hey do you
think I could come into interpret and be
useful it's like yes if you are good at
some of these things but not all there's
so much value when you pair with other
people who have different skill sets and
we really benefit from that
collaboration I think that one of the
really fun things about this is you
start to learn from those collaborations
like the shape of a problem that could
be solved which is like well in advance

[00:41]
of having any idea of how to solve it
but I'm like um like I bet Jonathan
could help with like this part of the
thing feels stuck and I don't know
enough to yet be able to do that but
then we can sit together like oh yeah
that's the kind of thing that I could
like bang out right now or on the
visualization side I just like I feel
like I'm clicking around between 17
Windows right now and I'm actually my
we've gotten the paralyzation down it's
like super fast to run these jobs and
now it's taking me like 30 minutes to
like look at the results and then we
bring and Pierce is like oh yeah yeah
yeah like we can totally make that part
better and then when you put that all
together you get this like really
incredible like scientific system where
you actually all of the parts sort of
work and like you know at what comes out
the other side of some of the more
beautiful papers I think I've ever been
involved in or actually got me in part
to join the team was just like you just
see these like Jewel likee figures that
come from you know people obsessed with
like working in figma to just like dial
all the details in which is not
something that I thought you know maybe
working in figma isn't part of the
standard like engineering toolkit but it
turns out that like that also is a force

[00:42]
multiplier yeah one one like explicit
thing that I want to mention that was
kind of baked into those answers is like
how the team is structured here I think
a lot of people think that there's a
separate research team and a separate
engineering team and kind of throughout
the conversation here we've been talking
about the interplay between those so
like separating those like just doesn't
work like we don't do that there isn't
like like these separate researchers who
are telling the like Engineers like
build this like these these problems are
fundamentally like entwined together and
you have to work on them together so the
way the like whole company works not
just the the the interpretability team
is kind of the research and the
engineering always go goes goes together
and that's just absolutely crucial for
this job adly if a friend came to you
and was like what was the most fun or
weird or quirky quirky thing you got to
do yeah I think that there is like a
surprising collection of problems that
comes in after you have trained 34

[00:43]
million features and now you want to as
silly as it sounds you want to see what
these features do and this is a tricky
problem at scale because these
features only activate on very specific
sequences of text that's what the sparse
and sparse Auto encoder means and so if
you want to really visualize all of them
you have to to run a lot of features
through a lot of text and then do things
like we also want to visualize what does
this feature do on the nearby text and
what does what does the distribution of
this feature look like and solve a bunch
of problems like that that I believe at
this point it's something like a 10 or
12 step very distributed pipeline just
because this is what of the things that
breaks really quickly once you scale up

[00:44]
the problem and there's just so many
steps that something is always breaking
and something different is always
becoming the bottleneck and so it's this
process of just looking at this finding
the bottleneck and trying to distribute
that further yeah sometimes things like
even matrix multiplication doesn't work
anymore where you realize that you want
to understand interactions this on my
team between 34 million features here
and 34 million features there and
genuinely you could just multiply the
matrices but then you couldn't store the
result anywhere or put the result
anywhere and so you really starting to
do some like fancy looping indexing and
compression to compute a product just
big numbers times big numbers are very
big numbers one of the things which we
hit is the the the default pytorch MML
implementation for certain shape Matrix
multiplies is just much slower so we're
like profiling jobs and we look at it

[00:45]
and most of our time is in Matrix
multipli so we think this is great we're
we're running really fast but we
calculate efficiency numbers
efficiency's not great so we then go to
someone else else at the uh company
who's who's kind of more of an expert in
this narrow ER area and he and he tells
us that oh yeah try try this other
Matrix multiply implementation it'll be
much faster and we're generally doing
that of like when we get to the really
thorny problems like that we at someone
else else at the like company because
we're not experts at that but it does
matter and we we do need to make these
things faster so we using the the
unbeknownst to us like a slow version of
multiply these matrices uh well it is
the default it is a version that is
normally fast but for the specific
shapes of the of the tensors we were
running Matrix multiply on it was not
fast and there's kind of different
different implementations for that so
under the hood for for for multiply what
generally happens is based on the shapes

[00:46]
of the of the matrices there's like
different different ways the the like
GPU kernels actually work so some some
implementations kind of pick pick the
the like wrong the the wrong approach
and are just randomly slower so we kind
of run into problems like that it's
randomly slower how do we fix this and
uh yeah you kind of don't have the time
to go be an a like expert in this area
you just need to kind of quickly find
something that'll that'll speed it up I
think this is such a fun example because
you would think that matrix
multiplication is just heavily optimized
but in a very physical sense our problem
was just a weird shape it was a weirdly
shaped Matrix and so we just run into
all of these problems because
interpretability research is just doing
really weird things like this and so you
run into all of these weird things that
happen yeah thinking thinking like
distributed is sort of funny for this
too we were doing some like attribution
calculations where you you're just

[00:47]
multiplying a vector by bunch of other
vectors and like you have to think
carefully about where they are living
and which direction you send information
because if you send this over here you
get to send some scalers back but if you
send this over here it's like a matrix
is going back and all of a sudden like
you've spent just enormous amounts of
time shuttling data back and forth where
like again I'm was trained as a
mathematician you write the equation and
all of the letters are on the same line
right there's no there's no like
communication bottleneck between the A
and the V that it's next to yeah I was
looking at a at a open source
implementation of of of sparse Auto
encoder training that only runs on a
single graphics card and I was just
shocked by like this is so simple like
this is so easy why do we have so much
code and then you go through all the
various points where where where we we
had to like scale this up a thousand
times bigger and it's just like that is
where all the all the all the code code
comes from and there's kind of so many
little battles there of like this random

[00:48]
thing doesn't doesn't scale is like 2x
slower that that that like we've put in
which we didn't have to do back when
when like we were doing uh very very
small jobs which just fit on a on a
single graphics card I think that also
speaks some to some of the
complimentarity of the of the work that
can kind of happen in Academia or more
open source environments um and what you
can do at a company with the scaled
models where like you can try out a lot
ideas at small scale and it like isn't
that hard from an engineering
perspective and then to get that to
actually work on models that are many
orders of magnitude larger you're just
like entering new Realms of physical
difficulty um to get anything off the
ground sometimes it feels like there's
the gift though which is that in the
bitter lesson that Richard Sutton talks
about which is sometimes the scalable
thing is better because you can always
put more scale in if you do the
engineering um and you hit the upper
limit of being clever
and so even though some of these methods
are quite conceptually simple it's

[00:49]
turned out that like on the rich data
distributions that actually make up
these networks they show really amazing
things it's really fun I think that the
bitter lesson applies not just to
training a model but also to
interpretability where I think people
often think of interpretability as
trying to get this like very principled
understanding and there is some of that
but there's a lot of that that just
really has the same properties as the B
lesson where you just take something
simple and do it at scale and you pick
the scalable thing and it is really
beautiful to me that that works not just
for making good models but also for
understanding models the other point I'd
make with like scaling and the bitter
lesson is that uh the company has given
us access to to the like compute which
we need to to actually scale this and
it's been really fun that like the thing
blocking us from scaling further is like
whether the ml actually works at that
scale or the infrastructure works at
that scale it like hasn't been can we

[00:50]
actually get the graphics cards to like
to like run on which would be kind of a
much more frustrating reason to to not
be able to
scale uh where do you see
interpretability in a year I think that
where I see interpretability in a year
is if everything goes well I mean this
is a super bullish case but we will
figure out so we did one slice through
the middle layer of Sonet
and I would want to analyze the entire
the entirety of every layer every piece
of all of our production models and not
just analyze them right now we only
found features we don't know how they
fit together we don't know how they
work in a variety of different contexts
and I and I really want us to do the
circuits work to figure out like what do
these
features mean on their own what do they
mean together working in
concert yeah one thing that I think I'm

[00:51]
just surprisingly excited about is just
actually continuing to scale this up
there's a lot about what we need to do
that is going to need to be different
there's definitely going to be lots of
opportunities to change the way we do
things but at the same time these things
seem to work better as you keep scaling
them up and so I'm really excited about
just trying to eek out the last few
orders of magnitude and see what happens
and if you would like to help us with
that we are hiring we would love to work
with you can I just say I love the
phrase the last few orders of
magnitude there's so much in that one
those few
words so why why are we doing uh
interpretability I think one of the
things I want to emphasize here is I
have a lot of uncertainty about the
types of challenges that are going to
arise with large language models and I'm

[00:52]
very uncertain about the direction
things will go in the future but
inability feels very robust to me I'm
very excited to work on this because I
think it can help with a really wide
range of problems in a really wide range
of scenarios it's just understanding
model seems good and if you can do that
better that's probably
helpful yeah understanding model seems
good and if you can do that it seems
like it'll help you with any of the
behaviors you might maybe that's
something I really like about
interpretability or rather the
approaches we're taking which are which
are sort of um completionist right it's
trying to map the full diversity of the
model um because if you can do that you
can zoom in to the parts that you need
later whereas if you're just focused on
like one particular behavior of Interest
it might not generalize or it might be
missing the sort of the important part
of the story and so you can do
interpretability focused on like one
Behavior at a time
but if you want the whole picture you
need to scale and that's why you need

[00:53]
people like the ones at the table who
can make the scaling
happen here here here here all right
hands in do one two three CLA one two
three CL

</details>
