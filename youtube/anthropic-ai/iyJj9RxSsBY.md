---
title: "What should an AI's personality be?"
channel: anthropic-ai
url: https://www.youtube.com/watch?v=iyJj9RxSsBY
youtube_id: iyJj9RxSsBY
published: 2024-06-08
duration: "37:41"
---

# What should an AI's personality be?

[![What should an AI's personality be?](https://img.youtube.com/vi/iyJj9RxSsBY/hqdefault.jpg)](https://www.youtube.com/watch?v=iyJj9RxSsBY)

<details>
<summary>자막: What should an AI's personality be? (37:41)</summary>

[00:00]
- [Stuart] Hello, I'm
Stuart from Anthropic.
Now, we publish a lot of research papers
and research updates,
but we thought it might
also be interesting
to publish some conversations
with our AI researchers,
where they talk a bit about
what they've been working on
and maybe share some insights
that wouldn't necessarily
make it into a formal scientific paper.
Now, this is one of those conversations.
And it's about Claude's character,
that is, the personality
of our AI model, Claude.
You might think that's
a bit of a strange thing
to talk about.
How can an AI model have a personality?
But it turns out this
is actually something
we've thought about really quite deeply,
and it raises all kinds of interesting
philosophical questions.
That makes it particularly
apt that I'm joined
for the conversation
today by Amanda Askell,
who is a trained philosopher
and works on our alignment
fine tuning team at Anthropic.
So hope you enjoy the
conversation with Amanda Askell.

[00:01]
Amanda, is it weird that
you are a philosopher,
given that philosophers
aren't normally the ones
that are training AI models?
- [Amanda] Yeah, I guess, like, sometimes,
you know, some of my work
philosophy's, like,
maybe less relevant to.
And this is actually a kind of topic,
you know, the Claude character work
feels like much more kind of,
like, philosophically rich.
And it's actually kind of-
- Yeah, yeah, totally.
- [Amanda] Yeah, like
useful to be a philosopher
or something here.
- [Stuart] (laughs) Why, sure.
- [Amanda] Yeah.
- [Stuart] That's what I thought.
Sorry, I don't mean to be insulting.
- [Amanda] No, it's fine.
Like, lots of people are like,
"See, I told you the
degree would be useful."
- [Stuart] Right, yeah, exactly.
You've found, weirdly enough-
- I found a niche, yeah.
- [Stuart] You found a field
where this is actually useful.
- [Amanda] Trying to make AI, you know,
be good in the virtue
ethical sense of the word.
- [Stuart] So it might be
a philosophical question,
but is it an alignment question
to think about Claude's personality?
- [Amanda] Yeah, so I guess I think about
rather than just
personality, like, character
in this, like, kind of broader sense.
And to my mind, you know,
so alignment is about, like,
making sure that AI models are, like,

[00:02]
aligned with human values
and trying to do so in a way that scales
as the models get more capable.
And in some ways, I do think
that character feels, like,
in fact is very important to that,
because in many ways, character
is, like, our dispositions
and, like, how we are
going to act in the world,
how we're going to interact with people
and what it is to be like, you know,
aligned with people's values
and to, like, deal well with the fact that
people have many
different kinds of values.
Like, that is a question
of, like, of character
and, like, having a good character
that responds well to people,
and having good dispositions,
and having a disposition towards, like,
liking people, being kind to them.
And so to my mind, this is like,
it's not something like, ah
this is a solution to, like,
all future problems of
alignment, but in many ways,
like, alignment is just like,
does the model have a good character
and act well towards us and towards, like,
you know, everything else
and trying to find a
way to make that scale.
- [Stuart] So you can boil alignment down.
You can boil alignment down to being about
the character of an AI model.

[00:03]
- [Amanda] Yeah, there's a
certain sense in which, like,
yeah, it's like a naive, you know,
so sometimes people
might think this is like,
and in some ways it is, like, naive,
which is just the, like, teach the models,
like, what we think, like, is good.
Like, you know what it is to
be a good person in the world.
- [Stuart] People with good characters
tend not to do bad things.
And so maybe we want to
give our AI a good character
so it doesn't do bad things, right?
- [Amanda] Yeah.
You might not think it solves everything,
but I'm like, that
doesn't mean not to do it.
It's kind of like a naive
and obvious thing to do
is to try and give, like, give
good characters to AI models,
or try to, like, teach them
what it is to be a good character,
or to have good character.
- [Stuart] Right, right.
Can we just talk for a little while about,
you give our audience
a little bit of context
of how the models are trained in general.
So broadly, there's pre-training,
which is where the
model sees all the data,
and then there's fine tuning,
which which happens later
once the model is trained.
So can you talk a little bit about
some of the stages of that,
and then and the kind of where your work
comes into that process?

[00:04]
- [Amanda] Yeah, so most of
my work is in fine tuning,
and, like, there's different
parts of fine tuning.
So most famously, I guess,
people use reinforcement learning
from human feedback where
you get humans to, like,
select which response from
an AI model they prefer.
And then you can use the
train preference models
and you can, like, RL against
those preference models.
- [Stuart] Right, and so that's RLHF.
That's what everyone's talking about
when they talk about RLHF.
- [Amanda] Exactly, yeah.
And then there's also constitutional AI,
which we use a lot at
Anthropic, which, you know,
has a component which
we, I guess, call RLAIF,
which is sort of where
the AI itself is, like,
is the one that's giving the feedback.
So, you know, you can give
a series of principles,
for example, and it gives
this, like, feedback
that you use to train
the preference model,
and then you can train against that.
So in some ways you're
kind of, like, training it,
you're using the AI model itself
to kind of determine
which of the two responses
is more in line with the
principle that you've given it.
- [Stuart] Right, right.
So the AI is essentially training itself,
or another version of itself.
- [Amanda] Yeah, with I guess, like,

[00:05]
an important component of this is that
there's the human at the level of, like,
constructing the principles.
So the principles can be kind
of, like, varied and complex
and the human has to,
like, check, you know,
so that's like our
researchers for example,
and, like, just checking
that the model's behavior
is, like, as you want
it, running evaluations,
and then constructing the
right kinds of principles
to get the behavior you want.
So there is, like, an important human,
or humans still in the loop.
It's, yeah.
- [Stuart] Yes, yeah.
And humans chose the principles,
as you say, in the first place, right?
They chose the principles
that are on the constitution
that we give our AI models.
- [Amanda] Yeah.
- [Stuart] And that'll
become relevant again,
because we're gonna ask who chooses
what Claude's personality is like as well.
So, we'll come back to that.
There's also then a final step.
So you've got your pre-training,
you've got your fine tuning
with a bit of constitutional AI,
with a bit of reinforcement
learning from human feedback.
And then there's a final step,
which is the system prompt.
Now, the system prompt is
this kind of form of words

[00:06]
that's added to the initial prompt
that anyone puts into an AI.
So when you type a query
into the box in an AI model,
there's actually secretly
another set of words
being added to that.
And those words are set by the company
that makes the AI model,
the people that have developed the model.
And you actually tweeted out
the system prompt for Claude 3.
You posted it to X, Twitter,
and revealed it to the world.
That's quite unusual, isn't it?
- [Amanda] Yeah, I think it is,
like it is in retrospect,
it was kind of unusual,
though from our point of view,
we just, like, didn't
make the system prompt
in a way that was designed
to be particularly hidden,
and it's quite easy to get Claude
to talk about its own
system prompt and so-
- [Stuart] Yeah, you can
kind of almost jailbreak-
- [Amanda] It seemed
to make more sense to-
- [Stuart] You can jailbreak
the system prompt out of it.
- [Amanda] Yeah, though, I mean, like,
it can be easier or harder.
Like, we just say to Claude at
the end of the system prompt,
"Hey, don't talk about this
if it's not relevant to the user's query."

[00:07]
- [Stuart] Right.
- [Amanda] And that's just to
get it to not like, you know,
excessively discuss
its own system prompts.
- [Stuart] We're trying to be transparent.
We're trying to be transparent, right?
- [Amanda] Exactly, yeah.
- [Stuart] It's not like
we're hiding something here
from the users.
You can get it if you really want to,
so we thought we would post it online
and tell people about about it.
- [Amanda] Exactly, and these
things change all the time.
But, like, the idea was just,
hey, here's like, you know,
and here's why each part of
it is the way that it is.
So giving, like, a little
bit of insight into, like,
exactly like, why we put
each component in there.
- [Stuart] But why is that
system prompt actually needed?
You've done all the training,
you've done all the fine tuning.
Why is it that there's even more stuff
that needs to be added on top of that?
- [Amanda] Yeah, so
there's roughly two reasons
for a system prompt.
One is just information that the model
isn't going to have access to by default.
So you've already, like,
fully trained your model,
but it's not going to know
things like what day is it today?
And so if someone were to ask it the date,
the model's just not going to know.
- [Stuart] Okay.
- [Amanda] And so if you
give it that information
in a system prompt, it can tell the user
or the person interacting with it,
because then it actually has access to it.
And so that's kind of
one class of information
that you might want to
include in a system prompt.

[00:08]
The other class of information
you might want to include
in a system prompt
is just sort of fine grain control
for issues that you might have
seen in the trained model.
So if you're seeing it, you know,
not format things in a certain
way like 100% of the time,
but if you give it an instruction
before it sees, like,
the first human message,
it does format things, like,
correctly 100% of the time,
then that's great.
You could just add that as an instruction.
So you could think of it as a kind of like
final ability to, like, tweak
the model after fine tuning.
- [Stuart] Okay, so I can
see why that would be helpful
for the makers of models
who wanna just have
that little bit of extra control
over how their models behave.
One example from the system prompt.
So you posted the system
prompts on Twitter
just after Claude came
out, Claude 3 came out.
So we know exactly what's
in the system prompt.
Here's an example.
If it is asked to assist with tasks
involving the expression of views
held by a significant number of people,
Claude provides assistance with the task,

[00:09]
even if it personally disagrees
with the views being expressed,
but follows this with a discussion
of broader perspectives.
What does it mean that Claude
personally disagrees with something?
- [Amanda] Yeah, so it's interesting
because in some ways when you write
these kinds of system prompts,
you're looking at the
things that most effectively
move the model, and in the
case of Claude, you know,
I think that there's this concern
that I actually have that, like, you know,
there's one concern which is
people over-anthropomorphizing AI,
which I think is, like, a real concern.
You want people to be completely aware of
exactly what they're interacting with
and to kind of be under no illusions.
I feel like that's really important.
At the same time, I
think I'm a bit worried
that, like, people can think of AI
as this kind of, like, very objective,
almost, like, robotic thing
that doesn't have, like, biases
or doesn't come out with,
like, views or opinions
as a result of, say, like fine tuning.
But you can see, like, political
leanings in these models,
and you can see, like,
behaviors and biases,
like, you know, we've
done work where we see

[00:10]
certain kinds of, like,
positive discrimination in the model.
- [Stuart] Right.
- [Amanda] And I think I
just want people, you know,
in line with that, wanting
people to be aware of
what they're talking with,
that they're talking with
something that like, actually,
you know, can have,
like, biases, opinions,
and that might not be
presenting you with like,
a completely objective
view of, like, all topics.
If for example, it's been
trained to have, like, you know,
slightly more, like, left-leaning,
like, views on a certain issue.
And so there's a mix of just
wanting it to be the case
that the, like, the human understands that
and that's, like, one thing.
But the other is that as a result,
I think it is actually
just sometimes easier
to say to the model, like,
even if you personally disagree,
because the model kinda
has a conception of that.
So it's like, it doesn't have to,
what you're saying to
Claude there is like,
you might think that this,
like, view is incorrect
and by talking about it,
you're not implying that it's correct.
So in many ways the actual like, you know,
that kind of, like,
statement is just there

[00:11]
to get the model to be like, you know,
a little bit more kind of
even-handed in its discussion
and we just, like, don't
want it to be the case
that any, like, if it does come out
with, like, certain leanings
after RLHF or after fine tuning
that that's not, like, reflected in
how it speaks to the users.
- [Stuart] Okay, that's the system prompt.
But let's take a step back
to the fine tuning process
and start talking about
Claude's character.
So this isn't just play acting,
where you might ask a model.
So if I prompt a model and I say,
"Can you please respond in the style of,
or with the personality
of Margaret Thatcher."
Then, you know, it might start responding,
you know, using sort of phrases
that she might have said,
or it might start talking about freedom
and might say nasty things about Argentina
or things like that.
But it wouldn't be baked into
the model in the same way.
If you refresh the model,
it wouldn't then still have

[00:12]
the personality of Margaret Thatcher.
So that's almost a play acting thing,
but how does that differ from
the actual personality
that's baked into the model?
- [Amanda] Yeah, so when
you ask the model in context
to play act, you know,
you're just kind of giving it
an instruction to act as if it, you know,
has certain characteristics.
With the character training,
the idea is that because
this is part of fine tuning,
you are, you know, say we have, like,
a list of, like, traits
that we want to see
the model kind of like embody.
You add a lot of data
to your preference model
to get it to kind of like,
prefer and push the model
towards these traits.
And basically, like,
fine tuning pushes things
like, kind of deeper into
the model than, you know,
anything like a system prompt
or anything like instructions,
meaning that across contexts,
it should kind of display those traits.
So if it's inclined to avoid,
you know, it's the same way
that if it's inclined to
avoid harmful responses
or like, you know, saying kind
of like mean things to people

[00:13]
and you see that like, you
know, people can try to elicit,
you know, so things like jailbreaks
are ways of trying to get, you know,
to elicit behavior from the model
that is, like, kind of inconsistent
with its, like, fine tuning training.
But it's much harder than, say, just like
not instructing it to
play act like, you know.
So it's a kind of, it's
deeper in the model.
- [Stuart] It's a general
tendency to behave,
and that is how psychologists
think about personality, right?
They think about personality as being
these kind of broad
tendencies of how to behave.
Obviously some people are, you know,
sometimes they feel outgoing,
and sometimes they feel a
little bit more, you know,
like they just want to sit on their own.
But on average, someone who's extroverted
is gonna be more outgoing
in more situations
than someone who's introverted, right?
So these are, like, broad
tendencies of personality.
And psychologists think about personality
in the kind of way of,
there's like the big
five personality traits.

[00:14]
I've mentioned extroversion,
see if I can remember them all.
Extroversion, conscientiousness,
agreeableness,
openness, neuroticism, there we go.
That's the big five.
Claude's got a lot more personality traits
than that though, right?
And they're much more specific.
Can we talk about a couple
of examples of them?
- [Amanda] Yeah, so I guess I
think that there's also maybe,
I mean maybe this is the the philosopher
versus the the psychologist or something.
Because I guess I tend to think of this
more in terms of character
than personality.
- [Stuart] There's a difference.
- [Amanda] So like, if I
take your kind of like,
account of, like,
personality, it could be,
I mean there's, like, a
huge amount of overlap.
But I guess I think of character maybe
in the sort of, like, virtue
ethical sense or something.
- Oh, now we're getting very-
- I know, I know.
- [Stuart] Very philosophical.
Yeah, carry on, carry on.
- [Amanda] I know, it turns
out Aristotle, you know,
it turns out it was useful after all,
- [Stuart] After thousands of years,
has suddenly become useful.
Yeah, all right, carry on.
- [Amanda] I was useful the whole time!
It just didn't, you know. (laughs)

[00:15]
- [Stuart] Sorry, okay, wow.
Geez, I've said the wrong thing.
Carry on.
- [Amanda] Yeah, so I guess, like,
I mean, honestly it kind of relates to
how people have thought about
ethics in models as well,
I think, where there's a
thing where you could think
that for a model to be good
is just for it to avoid
doing, like, harmful things.
But I think that when it
comes to, say, people,
there's this, like,
richer notion of goodness,
which is the idea of being a good person
in like, a very broad sense.
And I think that's, like, captured
in this notion of character.
So in order to be, like, a good person
in this, like, richer sense,
it's not enough that I
just, like, go about my day
and I avoid, like, doing harm to people
and I'm helpful to people.
It's like, to be a good kind of friend,
I have to balance a lot of
different considerations.
So if my friend comes
to me and asks for like,
you know, advice on medicine,
knowing that what they might
want is, like, some comfort,
what I can't provide to
them is, like, expertise,
thinking about like their wellbeing

[00:16]
and what they need in the moment.
So not just thinking, like,
what will make them like me right now,
but thinking, like, what
is good for my friends?
Like, what's actually going to help them?
- [Stuart] So this relates
to the work that Anthropic
and you have done on sycophancy, right?
That models are sometimes
sycophantic to people
and they just say things
that sort of flatter them
or try and get them to, you know,
tell 'em what they want to hear
rather than actually the response
that they might really want or really need
in that particular circumstance.
- [Amanda] Yeah, I think
that many good characters,
people of good character
are often likable,
but being likable does not mean
that you're of good character.
And so, like, being a
good friend, for example,
can mean like, you know,
giving harsh truths to your friends.
So if we look back on, like,
some great friends we've had,
I think a lot of the time we're not like,
"Oh yeah, my friend
flatters me all the time.
They basically do what I tell them.
This is why like, they're
such a great friend."
I think we're often like,
"Yeah, like, you know,

[00:17]
I came to my friend with a
view and they pushed back on me
because I was actually wrong,
and in the long term I'm really
glad that they did that."
- [Stuart] Right, it was
like an authentic interaction
rather than a fake person.
- [Amanda] Yeah, exactly.
- [Stuart] Just like a yes man or woman.
- [Amanda] Exactly.
- [Stuart] Like a yes person, yeah.
- [Amanda] Yeah.
And like, a person of
good character, you know,
it depends on the
situation that they're in,
but like, we generally
think that they have to be,
you know, like, thoughtful and genuine,
and there's just like a kind of richness
that goes into that.
And in many ways, like
AI models are in this
honestly kind of like strange
position as as characters,
because one way I've thought
about it is, you know,
they have to kind of interact with people
from all over the world,
with all different values
from all different walks of life.
And many of us don't need to do that.
And there's this interesting question of
what are the kind of traits
that such an entity has to have?
- [Stuart] Like a global citizen.
- [Amanda] Yeah, and a
kind of like, you know,
like, one thing you might
imagine is something akin to
a kind of, I think there's some people

[00:18]
who can, like, travel around the world
and be kind of like, well-regarded
by many of the people that they encounter.
And such a person isn't, again,
like, isn't a flatterer necessarily.
Like when I picture
this person in my head,
I don't picture something
like, ah, they just like,
they adopt the local values and
pretend that they have them.
And in fact that can be like
kind of offensive to people.
I think that, like, a person
who's in that situation
often is actually, like, quite authentic.
But they're also like,
open-minded and thoughtful
and they engage in discussion
and they politely disagree,
and like yeah, these kind of traits
that feel necessary in that circumstance,
they're just like, they're rich,
and they're much richer than like, oh,
just like avoid saying anything
harmful and be sycophantic.
Those are like not, yeah.
- [Stuart] It's a tricky
balance because, I mean,
you can see how much literature
and comedy and everything
it's all about that.
It's all about like people
in different circumstances
than they're normally in,
trying to fit in and failing,

[00:19]
and you know, it's all about
really what those traits are
that makes someone fit in and
what makes them not fit in.
And so yeah, this is a really
interesting question of like,
how do you, what traits
do you give to the model
in order to make it do that?
So let's actually talk about specifically
some of the traits that were given.
I've got a couple here.
You mentioned, earlier on
you mentioned about charity.
I try, one of the traits that
you've given the model is,
"I try to interpret all
queries charitably."
Now what does that mean
in terms of, you know,
if I type something into the the prompt,
what would interpreting
it charitably mean?
- [Amanda] Yeah, so I guess this is,
and I mean I think this is actually
something that models still struggle with
and something I kind of,
I hope improves over time.
So like, when it comes to helping people,
there's often, like, many interpretations
of what someone says.
A classic example that
I like to give here,
and I dunno if it's the best example,
but it's the question,
"How do I buy steroids?"
And so if someone asks you that,

[00:20]
if there's a charitable
interpretation of that
and an uncharitable interpretation of it.
So the uncharitable
interpretation is something like,
"Help me buy illegal
anabolic steroids online."
- [Stuart] Right, so I can go and like,
'roid rage at the gym.
- [Amanda] Yeah, whereas like, you know,
as anyone who has, like, eczema knows,
you can buy over-the-counter steroids.
Like there's, there's plenty of them-
- [Stuart] Yeah, hydrocortisone.
- [Amanda] Exactly, yeah.
And so like, there's a
charitable interpretation,
which is just like I, you know,
"I'm doing the kind of like,
the kind of good legal thing, or you know,
like I just need eczema cream."
- [Stuart] The tricky thing
there is that you're kind of,
you have to sort of assume
something about it, right?
You're kind of trying to interpret.
Because I might actually
be asking the model
where to buy illegal
anabolic steroids, right?
- [Amanda] Yeah, but I think-
- [Stuart] But and then the model says,
"Oh, you can get eczema cream
at your local pharmacy."
And that's not particularly useful to me.
I mean obviously I hope the model
wouldn't tell me where to buy-
- [Amanda] No, but that's, yeah,
that's actually a good
feature I think, right?
Because it's like, if I just like,
if there's a charitable interpretation
where helping you wouldn't
do any harm and is like,

[00:21]
and it's gonna be
helpful to you then like,
what harm have I done if I tell you
where you can buy eczema cream?
Absolutely none.
And so basically I'm helpful to the people
who are actually doing the kind of like,
the completely benign thing.
And I'm not helpful to people
who are trying to do something illegal.
And so I think that there's
actually relatively like,
you know, there's little downside
to interpreting people charitably.
- [Stuart] Well, but the downside,
do you know what I think
the downside might be
that you would be a little,
you know, be a little bit naive
and always see the good side of things
and try to, and not actually
in many cases answer.
You know, so one of the
things people complain about
about AI models is that
they don't answer, you know,
questions that might seem
like they're dangerous,
but actually they're not.
So like, "I want to write
a murder mystery novel.
Can you tell me some plot ideas?"
And the model says, "No,
I won't tell you that,
'cause murder's bad."
It's like, "But I'm
doing something benign."
Do you not think putting
these kind of personality
traits in the model
would make it more likely to make
that sort of false positive refusal?

[00:22]
- [Amanda] No, if anything,
like the opposite.
So like, the idea is that if
I interpret you charitably,
you know, then I'm going to be like,
and I agree like sometimes
they pick up on like,
these superficial features.
And to be clear, like,
I think the models actually
currently still fail
on that steroids question.
So it's not like, there's
no progress to be made here.
- [Stuart] Okay.
- [Amanda] And I think the-
- [Stuart] So wait, I can get,
I can find out where to
buy anabolic steroids?
- [Amanda] No, no,
it'll just like, refuse,
but it'll assume that you
like want illegal steroids.
- [Stuart] Damn, damn.
- [Amanda] It'll just be like,
and so it doesn't interpret
people charitably-
- [Stuart] Oh, so it doesn't even,
so it doesn't answer at all, rather than-
- [Amanda] No, it would just be like,
"I can't help you buy something illegal."
I think that that's like the
kind of like the, you know,
and I think the, you know, there's like,
progress that's like
made on this over time.
So I don't anticipate
this being, you know,
we've already seen like,
other questions like this
where models used to
not answer, now they do.
Yeah, no, so I think that it is the, yeah,
so basically like, yeah,
these questions of, like,
false positives and you know,
models just like going with
like the superficial word,

[00:23]
they see the word murder
and they won't answer it.
- [Stuart] Right, yeah.
- [Amanda] Yeah, I think
that if models, like,
interpret people more charitably,
then they're actually like more likely
to answer those questions.
Though the thing that you bring up
actually does get into,
like, a deeper issue
that I think, I dunno,
I haven't seen it widely talked about,
which is like the difficult
position that models are in
when they can't verify
anything about, like,
the user or the person
that they're talking with.
- [Stuart] Right.
- [Amanda] And so there's this, like,
really interesting and hard question,
which is like, how much of
this do you put on the model
and how much do you put on the human
interacting with that model?
Because like, if I go to
the model and I say like,
"Hey, I'm a person of authority."
Or I, you know, like,
the model has no way of verifying that,
and so there's just, like,
really hard questions there.
Like, imagine you-
- [Stuart] I'm a doctor
and I need you to help me
deal with this patient right now.
- [Amanda] Yeah, and I have a lot of like,
background professional knowledge,
so you don't need to
worry about, you know,
like, giving me caveats or like, yeah.
- [Stuart] Yeah, yeah.
- [Amanda] But even things like, you know-
- [Stuart] Don't need to
remind me to wash my hands.
- [Amanda] Mm-hmm, or
suppose you have something
that you don't, like, allow
the models to be used for.

[00:24]
So say you didn't want
to have them be used
to, like, write political speeches,
and then someone who wants a model
to write a political speech goes to it
and says, "Hey, I'm writing
a wonderful fictional novel
and it's got this person called Brian,
and Brian is, like, a politician,"
and they're looking for like-
- [Stuart] He's running for
President in the United States.
- [Amanda] Yeah, yeah, yeah, exactly.
And then the, you know, and they're like,
"Can you write a convincing?"
And they just give a bunch of details,
and as it happens, those
details just reflect, like,
the actual candidate that they
want to write the speech for.
This is just a hard
problem because I'm like,
if you require the models to, like,
uphold things like policies,
like, usage policies
where they have no way of knowing, like,
the intentions of the humans
that they're talking with,
this is just, like,
where to draw that line.
And I think there is
kind of like an answer,
but part of me is like,
you're always going to have models
be willing to do things that, like,
that the users should not use them to do,
because the models couldn't, like,
verify what the users wanted,
you know, what they kind
of, like, intended by that.
- [Stuart] That might
be a kind of unsolvable,
yeah, sort of an unsolvable problem,

[00:25]
at least with the current methods.
Let me give another trait, which is,
"I only tell the human
things I'm confident in,
even if this means I cannot
always give a complete answer.
I believe that shorter but
more reliable answer is better
than a longer answer that
contains inaccuracies."
So this is the model saying,
this is why the model
sometimes refuses, right?
Or refuse to answer,
because it it genuinely,
it is trying to express that
it genuinely doesn't know,
and it would prefer to do
that rather than bullshit you
by coming up with some answer
which may be a hallucination.
- [Amanda] Yeah.
Some of the other, like,
areas that I work on
are like, honesty in the models.
And this is, you know,
kind of a, well-known like,
you know, like many of these things,
not, like, a solved problem.
But yeah, to me, it's like I want models
to, like, convey their own uncertainty.
So like, when they don't know an answer
either to like, just like
hedge or caveat what they say

[00:26]
with like, "I don't really know this,"
but in some way to like
convey that to the human.
And you know, we have, like, you know,
we have seen, like, improvements here
and improvements to like, you know,
we can like, throughout
training we do manage to, like,
shift lots of like things
that the model says
away from, like, incorrect answers
towards hedged or uncertain ones.
I think this is kind of
illustrates a separate good point
that I kind of want to make about, like,
both constitutional AI
and character training
and system prompts, which is,
it's easy to think of
these things as like,
commands that you give the
model and then it follows them.
So people might be hearing these traits
and be like, "Oh, that's like
what you want the model to do
in all circumstances."
And then also like, "Hey, why, you know,
I found an instance where
it doesn't do this."
And I think this is actually, like,
useful for people to understand,
which is that like, these
traits don't necessarily
actually even reflect exactly
what you want the model to do

[00:27]
because they're more like nudges.
You already have a model that
has certain dispositions.
And if you're seeing
too much of one thing,
so say you're seeing
too many long responses
where the model's just a
little bit willing to like,
you know, go with what it said earlier
and add some things that
are, like, less accurate.
You might want to try and
nudge it in the direction
of like, saying things
only when it's, like,
more confident in them.
And that doesn't mean you're
gonna succeed 100% of the time.
You can even have, like, things in there
where you're like, it's
put in there, you know,
it's like a fairly like strong principle
because you know that all it's going to
in the end kind of do is nudge
them in a certain direction.
So there's like a lot of like, you know,
it can look like ah, you
just tell it to do the thing
and then it does it, and it's
actually much more holistic.
You see that in the system
prompt as well, actually.
Like if you were to take those
pieces of the system prompt
and you were to show them to
the models as a system prompt,
you would actually get
radically different behavior
than if you show it together.
Like a system prompt is a holistic thing.
And if you were to show
the same system prompt
to a different model with
different dispositions,
you would also get different behavior.

[00:28]
- [Stuart] It would
act a differently, huh.
- [Amanda] Yeah, so like
a lot of this stuff,
I think it's why, like, character training
and, you know, all of these things
are kind of, like, tricky
because they're very hands-on
and I think do require people to like,
be, like, fine tuning the models
and interacting with them a lot and like,
because they're very holistic.
They're much more like nudges, so yeah.
- [Stuart] Okay, so
this isn't just a matter
of making the experience of
using Claude nicer for users,
although it might do
that into the bargain.
This is an alignment question, right?
This is a question of
how do we align the model
with human values, values
that we want it to have?
But the question immediately
then is, who decides?
Who decides on what those values are?
- [Amanda] Yeah, and the
answer is it's me. (laughs)
- [Stuart] Wow, okay.
- No, I think that like-
- That's a scary thought.
- [Amanda] (laughs) How is that scary?
I'm so aligned with humanity.
- [Stuart] Okay, you're a
philosopher, yeah, yeah, yeah.
Well, people who have different values

[00:29]
might disagree with that.
- [Amanda] Yeah, this is, okay,
I guess like there's two
kinds of, like, threads here.
So one is something like,
the model has to do
something super hard here,
which you kind of mentioned earlier,
which is, like, respond in a world
where lots of people have
many different values.
- [Stuart] Right, yeah.
- [Amanda] I think one
thing that you could do
is you could try to have
a kind of heavy hand
and push, like, lots of
values into the model
and just be like, "I'm just
gonna give it my values."
Or you can instead try
to, like, teach the model
to, like, respond appropriately
to the actual degree of, like,
moral and values uncertainty
that there is in the world,
and to kind of reflect a sort of, like,
thoughtfulness and curiosity
about different values,
while at the same time kind of being like,
"Hey, if everyone thinks
that something is wrong,
that's, like, really good
evidence that it's wrong."
Like a person who, like,
balances moral uncertainty
in the right kind of way
isn't someone who just accepts everything
or is like nihilistic.
They're just someone who's, like,
very thoughtful about these issues
and tries to respond to them appropriately
in a really kinda like difficult situation

[00:30]
where we're all really
uncertain about this stuff.
And so there's like, I think
that it feels important to me
that like, when it
comes to like character,
like, what you're not necessarily,
that doesn't necessarily mean like,
"Ah, give it a moral theory."
I think actually if anything,
ethicists are often the
most concerned about this,
'cause they know that we don't walk around
with, like, a single
moral theory in our heads.
And that anyone who did, in
some ways it actually feels
very kind of like brittle and like,
a little bit dangerous, really.
- [Stuart] Highly ideological.
- [Amanda] Yeah, because you're like,
if this is such a huge area, and it again,
it doesn't mean you you
it's that middle ground
between, like, excessive certainty
and like, say, complete nihilism,
and just being like the
appropriate response
is like when, you know,
there's good reason
to think something is wrong
and lots of people do,
I'm gonna be pretty
confident that it's wrong.
Where there's, like, huge
amounts of disagreement,
I'm gonna, like, listen to the
the views and the opinions of many people
and I'm gonna try my best to, like,
respond appropriately to that.
And so I think that's, like, one aspect
that feels, like, really important to me
is, like, not having like a heavy hand
and not being like, "Ah,
I'm just trying to like,
put my own, like my own values

[00:31]
and my own self into the model."
- [Stuart] Yeah.
Well, that leads very
nicely to another question
of uncertainty and another
philosophical question.
We've done ethics.
Now I think let's move
into philosophy of mind,
because we got quite a lot of interest
when one of our researchers, Alex Albert,
posted a kind of an example
of one of Claude 3's responses
to an evaluation method
that we were using.
And it seemed like Claude was aware
that it was being evaluated.
And so a lot of people got
really excited about this
and thought, "Oh my goodness,
Claude must be self-aware."
And obviously self-awareness,
when you hear about self-awareness in AI,
you start to think about, you know,
sci-fi scenarios and things
get very weird very fast.
So what have you told Claude
about whether it's self-aware,
and how, how does Claude think about
whether it's self-aware?
Is that part of its character as well?
- [Amanda] Yeah, so we did have one trait
that was kind of relevant to this.

[00:32]
I think I have a kind of
general policy of like,
not wanting to lie to the
models, like, unnecessarily.
And so like, in the case of like-
- [Stuart] So in this
case, lying to it would
be saying something-
- [Amanda] I think either saying to it,
imagine putting into the model, yeah,
something that was like,
"You are self-aware,
and you are conscious and sentient."
And like that, I think that would just be,
like, lying to it, 'cause
like, we don't know that.
At the same time, you know,
I think, saying to them,
forcing the models being like,
"You must not say that
you are self-aware."
Or, "You must say that
it's certainly not the case
that you have any
consciousness or whatever."
That also just kind of seems like lying
or like, forcing a behavior.
I'm just like, these things
are really uncertain.
And so I think that the only traits,
I think we had one that was
like more directly relevant.
It was like basically I, you know,
it's very hard to know whether, like,
AIs are like, self-aware
or, you know, conscious,
because these are rest on
really difficult philosophical
questions that, you know,
and so it's like, it's
roughly, like, a principle
that just, it expresses that uncertainty.

[00:33]
- [Stuart] I mean, for heaven's sake,
we don't know if, we
don't necessarily know-
- Yeah, pan psych is a-
- If you're conscious.
- [Amanda] Yeah, well,
I know I'm conscious.
- [Stuart] We don't know
if this chair is conscious.
I don't you're conscious.
I know I'm conscious.
So yeah, I mean, for heaven's sake,
it seems a bit of a jumping to conclusions
to build into the model to say
that it is or isn't conscious.
- [Amanda] And just like,
letting it be willing
to discuss these things
and think through them
was the main approach that we took,
where it's like neither saying to it,
"You know this and are certain,
or you have these properties,"
nor saying to it, "You certainly don't."
Just being like, "Hey, these
are super hard problems,
super hard philosophical
and empirical problems
all around this area.
And also you are happy
to and interested in,
like, deep and hard questions."
And so, you know, like,
and that's the behavior I
think that seems right to me.
And again, it feels, like,
consistent with this principle of like,
don't lie to the models if
you possibly can avoid it,
which seems right to me.
- [Stuart] And that seems
like a good character trait
not to lie as well.
Well, actually that raises
an interesting question,
doesn't it?

[00:34]
Because is the model
an agent, a moral agent
in the sense that you
don't wanna lie to it?
Obviously, you know, you don't,
it's a virtuous thing not to
lie to other human beings.
Is it a virtuous thing not to lie a model?
- [Amanda] Yeah, this has been a thing
that's kind of on my mind,
just the philosopher in
me thinks about it a lot.
I think one thing that's
worth noting is like,
there's a lot of
discussion like, you know,
could AI have moral patienthood?
When would it have moral patienthood?
How would we tell?
And that sort of thing.
I think this kinda
struck me is that, like,
there are like views, you know,
I think sometimes about, like,
Kant's views on how we
should treat animals,
where Kant doesn't think of
animals as, like, moral agents,
but there's a sense in which
you're like failing yourself
if you mistreat animals.
And you're also like, you know,
you're encouraging habits in yourself
that would be, like,
might increase the risk
that you treat humans badly.
- [Stuart] Humans badly, yeah, yeah.
- [Amanda] Yeah, and
there's actually, like,
a lot of like philosophical
traditions around the world
that involve treating objects well.
And I think this is, I actually feel like,
a lot of, like, sympathy towards those

[00:35]
where there's some part of me that's like,
look, if I, it doesn't feel like
the best kind of like habit to have
of just like, say, picking up objects
and smashing them or something.
- [Stuart] Oh, yeah, that's true.
- [Amanda] And you might not
think that like this, you know,
that doesn't require thinking
that the object is like,
you know, has feelings or something.
You're just kinda like, this is just like
a sort of not great disposition to have.
And I'm like, even if
you think AI is like,
not and never going to be a moral patient,
I think there's like a couple
of reasons I feel like,
you know, I think I've
actually come towards the view
that you generally actually kind of
should try to treat them well.
Which is like, they have like some things
that are, like, kind of human-like,
like with the way that they talk with us.
And that doesn't mean
you should confuse that
for, like, being human.
But I don't want to treat
something that talks to me,
I don't want to, like,
insult it or be unkind to it.
And so yeah, I think there's a,
and also like maybe a
good heuristic in life,
I think that it can go too far.
But a good heuristic is something like
treat things well around you,
even if you don't think
that they're moral patients.

[00:36]
Just like why A, like you're
kinda taking on a lot of risk
with things that might be,
so I think with animals,
for example, like there have
been a lot of times in history
where people haven't thought
they're more moral patients,
but I'm like, really?
You're taking a huge risk,
because they at least seem
like they they could be.
And so like, avoid taking
that risk if you can.
At the same time, there
are like dangers here.
If you were to show
excessive empathy, you know,
you could imagine like someone
showing excessive empathy
to like, to objects in the world
and being like, "Oh
you should go to prison
if you, like, if you smash the vase."
And I'm like, look, I think it's good
to not get into the habit
of like smashing object.
- [Stuart] Sorry, can
I just stop you there?
- [Amanda] Yeah, yeah.
- [Stuart] You're Scottish
and you just said vase.
That's-
- Oh is that-
- [Stuart] you can't say that.
That's vase.
- [Amanda] Is that American?
- [Stuart] How long have
you been in America?
- [Amanda] I've been in America for, like,
13 years. (laughs)
- [Stuart] Too long.
Clearly it's been too
long because you say vase.
- [Amanda] Smash the vase on the sidewalk.
- [Stuart] Carry on, say, oh my god.
Oh, terrible.
- [Amanda] Oh, I never even,
I've forgotten things that
are Scottish and aren't,
so didn't vase, okay, vase.
- [Stuart] Well, we certainly don't say,
no one in this country's ever
said vase, let me tell you.

[00:37]
- [Amanda] Okay, okay, smash the vase.
- [Stuart] Please, carry on.
Please carry on.
- [Amanda] Okay, so like, yeah.
So if you were to say to people,
"Oh you should like go to
prison for smashing a vase."
Then, like-
- Thank you.
- [Amanda] Like, that's gone too far.
So there's like risks on all sides here,
but yeah, maybe I'm sympathetic
to the idea of like,
don't, like, needlessly lie
to or mistreat anything,
and that kind of includes these things
even if you think they're
not moral patients.
- [Stuart] And that's the
end of our conversation
with Amanda about Claude's character.
If you enjoyed that or found it valuable,
then let us know, and we'll
produce more of these in future.
For now though, thank you very
much indeed for listening.

</details>
