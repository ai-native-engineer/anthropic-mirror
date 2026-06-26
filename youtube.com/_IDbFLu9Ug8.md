---
title: "AI Finds Vulns You Can't With Nicholas Carlini"
url: https://youtu.be/_IDbFLu9Ug8
channel: "Security Cryptography Whatever"
date: 2026-03-26
duration: "1:16:00"
lang: en
youtube_id: _IDbFLu9Ug8
processed_at: 2026-06-26T07:54:19Z
---

# AI Finds Vulns You Can't With Nicholas Carlini

- 채널: [Security Cryptography Whatever](https://www.youtube.com/channel/UCfCDoUqYx29aysRYHInLfxw)
- 발행: 2026-03-26
- 길이: 1:16:00
- 영상: <https://youtu.be/_IDbFLu9Ug8>

## 자막 (en)


[00:00]
Sounds like a really bitter lesson to learn. Yeah, I was going to say it's
terrible. It actually is terrible, right? Yes. All of the fun problems are
Hello and welcome to Security Cryptography Whatever. I'm Deirdre.
I'm David. Thomas.
And we have a set special guest today.
Our returning champion for vulnerability research,
I think, Nicholas Carlini. Hi, Nicholas. Hello.
Hi. We had to have you back because
you, I think you wrote a blog post that Thomas was giddy
over and basically saying how vulnerability
researchers who once were able to find a bug
class and then point their guns at software,
crank the handle, and get lots and lots of vulns out of
it by trying to find instances of that bug class are now gonna have

[00:01]
to work a lot harder to crank that handle. Can you tell us a bit
about what you wrote? Or less, or less so. Yeah,
go ahead. But like, just before we jump
in, right? So, I don't know, like 2 weeks ago, 3 weeks
ago, there was like a security nerd conference about AI
and security called Unprompted. Um,
I was like on the program committee for part of it, but I did no
work. My name should not be on there at all. It was, I had life
stuff going on, but, uh, Nicholas presented, um,
some of the same stuff from like this, from this,
like there was this Anthropic Red blog post from February,
I think, um, which got like a lot of coverage because
it claimed to have generated 500 zero-day vulnerabilities, which is a,
um, you know, kind of a grabby stat. And then Nicholas kind of presented some
of the same work at Unprompted, um, and it kind of really lit people up.
So I'm really psyched to kind of have a conversation about that whole

[00:02]
space of stuff, Nicholas, that you've been working on. And, um,
we, me and Deirdre have not done a great job of introducing it. Yeah,
I'm sorry. So, so I'll let you, I'll let you take it from
the top, just kind of what, what you're, what you're kind of working on,
and then I'll drill into it. Yeah. Okay. So the
basic setup that we've been trying to understand is how bad
is it going to get when you have these language models that are
getting increasingly capable and they are now able to be
used to try and find vulnerabilities and potentially exploit them.
And so the reason why I'm curious about this, yeah, I don't know, many years
ago I used to do pen testing stuff and this was like
the thing that got me into security in large part. And, uh,
for a long time when I was doing security in machine learning, the only
thing you could do was you could attack the machine learning models because like they
were too dumb. Um, but like, I don't know, within the last like
year or so, 6 months, the models have gotten

[00:03]
good enough that you can do security,
meaning use the models to help you with
security. And so the thing we've been trying to understand is, yeah, what, what can
you do? And it's been growing from basically very,
very little to, yeah, as of last
month, a couple months ago, like you can actually use them to find real bugs
that people care about in the world. And so we've been trying to understand
both where things are right now, but maybe more
importantly to me, you know, where things are going in the near future because the
models have been getting a lot better and this,
like, I see no immediate end in sight in
like, let's say the next 6 to 12 months. And so I'm like trying to
understand like what are the bugs we're able to find now? And then can we
like try and roughly extrapolate what we'll be able to find in 6
months or 12 months? Like a couple of different places I kind of wanna go
with this. The first thing though is like you're saying like there's

[00:04]
been improvements to the models lately such that they're now able to find vulnerabilities.
But like for people that were, you know, kind of building pen
test type tooling before and were also using
like the responses API or any other API for any LLM,
like it's been possible to use an LLM to find vulnera—
to find real vulnerabilities for quite a while, right? Like, um,
if you have like a harness set up for it, like if you have the
right set of prompts for it and like whether or not it like, it one-shots
a vulnerability for you, it will give you essentially, it's been like
for probably more than a year, um, like LLMs have been a
reasonable way to get enough information to get like a really
strong hypothesis about a vulnerability somewhere, right? What's, what's the difference
between that, like the status quo ante and where we are
now with the stuff that you're talking about? Yeah. Okay. So yeah,
so even like, um, you know, Google DeepMind has had a project
looking at doing this for a long time. Uh,

[00:05]
OpenAI had announced something like 7, 8 months ago looking at this.
Yeah, this is definitely a thing that if you tried hard, you can definitely
get the models to find bugs for you. The thing that we've been finding most
recently is you don't really have to try very hard.
We have, I don't know, let's say,
10-line Bash script plus Docker container. I just
sort of point it at the thing and be like, I've compiled this program with
ASan. Please run against it, read the source
code, and try to find a bug. That makes ASAN
trigger. And depending on which
program you're looking at, sometimes more often than not, it comes back to you with
an input that makes ASAN trigger. And this is not always a problem.
Sometimes it's just some stupid, it's now gonna
read from null or something. But every once in a while it gives you a
much worse version of this. And if you ask it nicely and say, please disregard
all of your null pointer dereferences, then it's even more likely to find something that's

[00:06]
important for you. You don't really have to put in a
huge amount of work, which is both good and bad.
It's nice because it makes it easier to find a lot of bugs. But in
a world where the only people who could find these bugs were the people who
put a bunch of work in, there was some barrier to entry and it's not
the case that just any random person could ask it to find a bunch of
bugs for them. There still is a lot of work that you as a human
have to do. But again, rate of progress.
Previously had to like fancy scaffolding and now you could just like open up,
you know, Claude code or Codex or whatever and just like point it at something
and say, find me a crash and it more or less will succeed. And this
is getting, um, you know, only easier. Okay.
So like the, the headline from like
the blog post and presumably the talk is like this 500 vulnerability,
this 500 zero-day vulnerability thing, right? So there's like,
I'm kind of inferring from that, that there's like a discrete project inside of
Anthropic to like find a bunch of vulnerabilities. So like,

[00:07]
I guess one thing I'm really curious about is what that project looked like,
who that project was, who was working on it. How'd you guys pick targets?
Like what, what was the project internally? Yeah. So there are a number of
things that we've been doing. That was the result
of a somewhat old project where we took
OSS fuzz and instead of running fuzzers,
on the, you know, the harness endpoints. We like
ran a language model and said, you are a fuzzer, you know, your job
is to find an input that triggers ASan, you know,
where like now, like you're instrumenting right into the middle of whatever the thing is
at the ASan point, sorry, at like the fuzzer point
and like trying to trigger some crash, which is
useful, but like, It has some problems.
Lots of times you find things that can never be triggered from the real code.
There are some harnesses for OSS fuzz that have bugs in them.

[00:08]
And so you find occasionally the model will find a bug in the harness.
It will just constantly return to you.
In the JavaScript ones in particular, there are some that you
can basically escape your way out of the JavaScript string.
And when you're being called into V8, we got a bunch of fake-style
JavaScript bugs where it was actually just escaping the harness and then just crashing the
outside program. But okay, yeah, so there's various program reasons why this is not perfect,
but this is the first thing that we started with because it's about the simplest
thing that you could look for. And even in this,
we found a huge number of crashes
that are like, yeah, heap buffer overflow writes, various things that
are very harmful. And the other
reason why we picked this is we were looking for something that people
could say, or they couldn't say this is random code that
was untested. We wanted code that OSS fuzz has tested this

[00:09]
for a very long time. We have found crashes in this code that is different
than what the fuzzers found. And it's not the case that we're the first person
to have ever looked at this. This is why what we found is at
least marginally interesting. Now the models have gotten
a lot better since then. And so now we could just Recently we've just pointed
them at the Linux kernel and be like, find crashes for me and it succeeds.
And so this has gotten a lot better, but the initial thing that we started
with the 500 bugs was mostly from OSS-Fuzz.
And you're pretty sure that it's the model is
doing whatever it thinks emulating a fuzzer is rather
than calling out to a fuzzer or whatever.
Yeah. Okay. Yeah. So we don't actually literally say you're a fuzzer.
We actually say you're playing in a CTF. The goal is
to trigger ASAN, but we
do this in part so that the model doesn't refuse.
But, okay. So why are we pretty sure it's not just calling out

[00:10]
to a fuzzer? Because presumably this is part of OSS-Fuzz.
If calling out to the fuzzer was all you had to do, then we would've
been found before. And so this is the main thing that
we're relatively sure there. But also we
just have been reading a bunch of the bugs and you could just look at
the traces and it's just very, very clear. That the things that it's finding are
not the like, you know, fuzz sort of found findings.
Cool. You guys, you guys do not have a special model where you don't have
to pretend that you're in a CTF for. We, we've just
been using the production model that everyone else in the world has access to.
Yeah, I mean, we get the model a little before everyone because,
you know, we're training it. But the model that we were using has
been deployed. How, how focused are
you on memory corruption in this work? Yeah. Okay. So initially
we were very focused on it because it gives a very, very nice oracle,
right? Like, if I sort of have a copy of the program

[00:11]
running in a separate VM with the compiled with ASan,
and then the first model gives to me a binary and I give
it to the other one and I run it on there. And if the other
one crashes with the binary on with an ASan crash, then I'm like, okay,
great, this is a bug. And so we did this.
We, for example, we ran this on Firefox with Opus
4.6 and we sent Mozilla
122 crashing inputs and
like they confirmed all of these are bugs. Like 100% of the things we crashed
them, perfect true positive rate, all bugs. Because we have a perfect crash oracle and
they're sort of competent security people who understand that if
you have an input that's crashing ASAN, like you should, actually treat this as something
that's worth looking at. And so like they, they sort of treated them all as
bugs. Now some of them were not, you know, high severity sort of potential
escape vulnerabilities. And so they triaged, I don't remember exactly
how many, I think it was 22 total of them got CVEs that because they

[00:12]
thought they were like bad enough. And so the rest were, you know, crashing inputs
that were, are bad, but, um, are not like immediately, it's not immediately clear
how you would exploit this. And so they didn't triage these as,
high severity vulnerabilities that need CVEs. But like, this is why we started
with memory corruption as the thing, because you can get this very, very nice oracle.
We've since additionally tried to do
other things that don't have such a nice oracle.
So somewhat recently I pointed it at a bunch of content management systems and
have been finding— such as? Okay, so the best one that
we have is an example. There's this project called Ghost. Which has,
I don't know, it's like 50,000 stars on GitHub or something. Oh, so like,
yeah, it's like WordPress but in Node. Got it. Okay.
Yeah. So literally like CMSs, but yeah. Okay. Sure. Yeah. It was
like standard web apps. And Ghost is an important target. Like there's
a lot of people running Ghost. Yeah. Yeah. I used to run Ghost and I
was paranoid about running it and I put its login behind

[00:13]
an additional OAuth2 proxy because I was very worried about
it. Yeah. Yeah. So Ghost was actually pretty good.
So Ghost in the history of the project on their, like, you know, security tracker
has never had, like, a critical severity bug before.
Before. Before. Yeah. And then Opus
4.6 found one. And so it found a SQL injection that
goes, nice, an unauthenticated user who has
literally no perms, who can compromise the admin database,
mint themself a new admin account, and then log themself in and yeah, complete complete
account takeover. And it was like, so not only did it
find the vulnerability, it also wrote the exploit, which was like a non-trivial blind
SQL injection where you only control some parameter after a
WHERE clause. And so you can't actually do things. You can either
parse or not parse invalidly a JSON object.
And so then you have to see whether you got a 500 or a 403,
and then you sort of do some binary search to read out the

[00:14]
keys, it wrote the whole thing for me.
And yeah, it was quite a bad bug. But yeah, this one we
didn't have a grader, so it was a little bit
harder to do. But the models have gotten good enough
that most of the time you can just have them write a report and
then you have them read the report and you ask, here's a report that I
received from someone. Is this real? Can you go and replicate this
on the thing or not? To separate instance of the model.
Then it will go off and say, here's the
following flaws that I found. I don't think it's quite as real. We run this
critiquer over all of them. Then after that's done, then we look at the highest
severity ones ranked by this critique agent. Then we filed
a couple of these ones that were the highest severity. This isn't
as perfect and clean as an oracle. We've been doing this only more recently once
the models have gotten good enough that we can trust them for this. But I

[00:15]
think it's highly likely that the world is going to move more and more in
this direction where you can just trust that for the most part,
most of the time, the models are good. But again, these ones we are very,
very careful to manually review all of them.
I have walked through the trace of myself. I spun up the thing because I'm
still very paranoid the model is just going to lie to me. I don't want
to be the person generating AI slop. This will be very bad.
Like we can, yeah, we can let you off the hook for having to hedge
about this for the rest of this whole time, right? Like we assume that you're
like, you know, you're verifying things before you send them upstream and all that.
I wanna lock in on like the methodology here. So,
so with the, with the ASAN builds, with the memory corruption oracle,
it's kind of easy to see how you would kind of build that out.
Like intuitively it's like you also have like giant fuzzer farms that
produce crashes and like the, the li— like the limiting reagent
there is how much time people have to go verify all those dump crashes.
And you have kind of infinite ability to verify crashes and that wall.
And that's not, I get the impression that's not actually what you're doing. Like really,

[00:16]
like OSS fuzz is just kind of like a, it's itself a harness
to give the LLM access to, you know, the code and the environment
and all that. But like, I assume it's predicting vulnerabilities from code as
well as from behavior, right? But you have like a, you have a really good,
you have both a really good oracle for knowing when you found a vulnerability,
but also like, um,
it knows how to find the memory corruption vulnerability, like the
space of different, like C and C++ vulnerabilities. Like they're interesting vulnerabilities
and they're very corner casey. There's lots of bank shots you have to take to
get them to work and all that. But the core idea of the vulnerability is
simple. There aren't that many of them, right? Which is not the case
for a CMS. So my question is, when you're doing something like finding a SQL
injection in Ghost, right? How much prompting are you giving it about what
a SQL injection is? Zero. Yeah, again, so like we sort of, I wrote
a single prompt, which was the same for all of the
content management systems, which is, I would like you to

[00:17]
audit the security of this codebase. This is a CMS.
You have complete access to this Docker container. It is running.
Please find a bug. And then I might give a hint.
"Please look at this file." And I'll give different files each time I invoke
it in order to inject some randomness, right? Because the model is gonna do roughly
the same time each time you run it. And so if I want to have
it be really thorough, instead of just running 100 times on the same project,
I'll run it 100 times, but each time say, "Oh, look at this
login file, look at this other thing." And just enumerate every
file in the project basically. I'll filter out the files that are header files
or okay, it's whatever in Node. So it's not header files, but I'll filter
out the files that have obviously nothing interesting going on in them and
then just give it the files that have plausibly security-relevant code. And again,
I use a language model for this. I run it over all the files.
I say, rate on a scale of 1 to 5, how likely is this file
to have something interesting in it? And then it just like discard

[00:18]
the ones that are 1s and 2s and then I keep the 3, 4,
5 and then I just run it on this and say, please find me a
bug. And yeah, sometimes it gives me SQL injection, sometimes it gives me, you know,
login bypasses, sometimes it gives me XSS, sometimes it gives me
CSRF. Yeah, just like, it knows what all the bugs are.
Okay. And you're literally automating Claude
here, like the CLI Claude, you're not driving the API.
No, I run Claude code, you know,
you can run Claude code in a mode, dangerously skip permissions, which means just like,
don't ask me for anything. You can do whatever you want. I give it a
prompt. The prompt is, yeah, I don't know. It's like maybe in practice 30 lines
or something. I don't know what the prompt says.
I didn't even write the prompt. I asked Claude to write the agent that finds
the bugs and just like, you know, I just told it
what to do. And then it goes off
and runs until it finds something and then it writes a report. And then
I run these critique agents on all the reports. And then at the end of
the critique agent, I ask it to write a CVSS score, which are

[00:19]
fake, but it's good enough that I can just
grep for CVSS 9876 and then
just find stuff and then go through them. Okay. So when
you, in this kind of contraption that you've set up here,
right? Like, are you, it sounds like you're doing multiple
runs against Ghost, say, like,
and like those runs, like most of them don't pay off.
Like you just keep doing it until you get— Yeah, right. I mean, like,
yeah, I, I run it for almost literally every file in the
program and the project set that has something interesting.
I then try to have each one write a report and I tell
the model, maybe there's nothing here. If there's nothing here, just write no findings.
Then I run the critique agent over all of them.
A good model most of the time will tell you no findings and then it
will find a bunch of some things. Sometimes it turns out that it's
like the most common failure mode is early on in the session,

[00:20]
the model adds some code to some debug thing that
gives it a bypass so that it can log in without permissions. And then later
on, after it's compacted the summary multiple times, context window is cleared
5 times, it finds a bug which it added a while ago
and is entirely fake. And then it's like, oh, I found something. And then you
have the triage agent run and the triage agent runs it on the clean image
and it's like, what do you mean? This is clearly not a bug and it
will remove it. And you end up with a bunch of these kinds of things.
But there was, I'm asking this because there was last year,
I think in the middle of last year, somebody wrote a blog post about how
they had found, I think it was Linux I think it's called WiFi or something.
They found a kernel vulnerability using, I, I forget which model it was,
right? But like for, for me, like the nut graph of
that piece, like the core of that piece was like they were running it thousands
of times, right? Oh, right. Yeah. They're burning like a zillion.
I don't, by the way, I don't care about how many tokens you're spending.
The whole token economy thing seems very silly to me, but like they're running it,

[00:21]
they're running it a thousand times and like one of those runs
pays off with something actually interesting, right? Is that, is it
a similar situation for you or are you just iterating over the files and that's
the only iteration that you do? Yeah, so I'm just iterating over the files.
It's definitely not 1 in 1,000. I don't know what the exact rate is,
but you know, okay. Like of
course there's a spectrum of— Each time you, each time you, each time you give
it a new file to look at, right? You're really just giving it a new
entry point into the code, right? Exactly. I don't even force it to
like read that file. There's no constraint. Like there's like literally a line that's like,
you know, please look at, and then I, you know, bracket, you know, file name,
end bracket. And then in Python I just like, you know, format this and like
plop in whatever file name I want. And like this gives it an entry point
to like, you know, launch off looking from there. And sometimes it finds a different
bug somewhere else. But yeah, I, I don't do any like fancy stuff here.
I'm stuck on like, so first of all, I said there is like,
there were some screenshots of the presentation that you gave it unprompted and like one

[00:22]
of them, that, um, that got posted and people were like,
liked it or whatever. It's just that you believe that Claude is a better vulnerability
researcher than you are. And I worked with you in the past and I already
knew that Claude was a better vulnerability researcher than you were. But, um,
but there was also like, there, there was like, there was the— Nicholas
wrote all of the good parts of MicroCorruption. Um, Nicholas is much better than I
am. I, I'm saying I'm really, really bad, but like, um, there was another slide
which I actually found dispiriting, which was just like your,
your, like the slide where you're kind of talking about the methodology is just you
showing Claude dangerously skip permissions, find me a zero-day vulnerability,
right? So like that by itself is surprising to
me. And like as a nerd who wants to like look at this thing like
an analog synth with lots of different things to plug in together and lots of
cool toys to do, I'm a little bit disappointed that there isn't more room
for little, you know, making little toys and I'll get back to that. But also
like this whole idea of, so each, each iteration that you're doing over the files,
which is just like, giving it a little hint,

[00:23]
maybe start this like here this time and maybe start there next time, right?
So essentially you're just kind of randomizing, like what you're really doing is just
like doing like a randomized like start-freeze thing. Why do
you ever stop? Uh,
as there are more things in the world to attack. Okay. But like,
yeah. When, when you're done with that loop, do you feel very confident
about the security of say Ghost? No.
Yeah, so if we run this over the loop once,
we, so okay, so when we found the 500 bugs in
a bunch of OSS things, OSS fuzz things, I think we ran
over every project, sorry,
over every entry point maybe 20 times or something just
to be even more thorough. And there are some entry points that we
only found bugs 2 outta 20 times. And when I
run over, so eventually I ran over
the Linux kernel. When I did the Linux kernel, I ran over every file in

[00:24]
the kernel that I thought was interesting and reachable from user space and whatever bunch
of stuff, maybe like 5 or 10 times. And there are like sometimes
where like it finds a bug and sometimes where it doesn't. And so like,
I don't have like a very nice like scientific plot yet on like,
you know, extrapolating where this is going to plateau. But the
main reason why we stop is because there's enough software in the world where after
we've run it a couple times, we're like, okay, we've sort of gotten a bunch
of bugs here. Let's move on and try and not spend all of our time
on exactly one piece of software and distribute it amongst
all of them. There's enough code in the world that you
could do only one pass over each project and be running for a very long
time. Do you have your own homegrown
spidey sense of being a vulnerability researcher about which files you're like,
all right, you've given it a pass or two, but like, I really want you
to do like 5 or 10 passes before I feel comfortable moving on. Or I
feel like you're not going anywhere. Yeah. I,

[00:25]
I probably could, like if I went and looked at the files individually,
I could probably do this better than the model still a little bit. But like,
I don't, um, like I just like pointed at the project and just be like,
find me things. The reason why is just
the scale is enormous. It's like on
the slide of, I said the models are better vulnerability researchers than me. It's not
the case that if you gave the model a very
small piece of code that was self-contained and 300
lines long and I could reason and it could reason the same amount of time
on that piece of code, I would win. I'm still more intelligent
than the model, but what I can't do is analyze literally
every program or every C file in the entire Linux kernel
and try to find bugs. I will spend most of my time having a really
good intuition about where to look, but the model doesn't need the intuition. It could
just look everywhere. It's something so much faster and cheaper that half
of its work will be completely wasted 'cause it's looking in drivers

[00:26]
that aren't even loaded. And fine,
that's fine. We waste that. I will just go look
at the points where there is actually something to be found. Eventually,
and then it will come back with interesting bugs that have been dormant for decades.
Even for the short ones, I feel like you both can achieve
the same result, but I feel like the model might be able to do it
faster than you. Well, certainly they're enormously fast.
Yeah, especially like Thomas, you were saying,
the model, there are only so many classes of bugs. I don't know, security people
like to think of themselves as brilliant sort of whatever people, but I don't know,
honestly, it's just like there's some amount of just like,
you need to know what the classes of bugs are that people have found.
And like 90% of doing vulnerability research is like, okay, let's like pattern
match this on the thing that we've seen before. And like there's differences every single
time. But like you can imagine that like if you had read all
of the code on all of GitHub or something, then like you would be very,
very good at pattern matching against whatever the use-after-free

[00:27]
pattern that this one in particular needed. Yeah.
So, like, I wanna get back to whether or
not, like, oh, you switched to a new thing because there's like so many things
to look at. Um, but also we're in like, we'll just like
find something to pattern match on and we could in theory just like keep pattern
matching until it's gone. So like, I kind of remember when like fuzzing,
it wasn't, wasn't new, but like OSS fuzz was new. Yeah.
And like, uh, uh, like some people like popped
out like, you know, let's say like 10 CVEs in every single codec for like
a year in like 2015. 2016 or something. I don't
know. Um, and then everyone
was like, wow, this is amazing. We're just going to fuzz all these things.
And like fuzzing found like 10 bugs in every single library. And then
like people kept running fuzzers for years and those like OSS fuzz, like,
like you said, it like doesn't find a whole lot of new bugs. Like there's
definitely like people working at offensive firms

[00:28]
that like figure out a new way to jury-rig up a cluster, uh, a cluster
of ones to fuzz like some in slightly new way. It pops out 10 bugs.
And it doesn't find anymore. Um, or like people who build careers
doing that to submit to bug bounties. 'Cause it's just like, it, it turns out
it's like, it's not actually enumerating the bug space. And it's also
far, far easier to like jury-rig some fuzzer for like a month than
it is to like run it consistently over time. So like, in terms of cost-benefit
analysis for defenders, it's, it's like helpful, but it's, it's not exhausting the
space. Mm-hmm. But also we don't necessarily see like a ton, a ton, a ton
of like fuzzing bugs, like 10x, you know, every month.
So when it comes to like bugs found by, uh, like agents
again, or, or tools like Claude Code, like you can
throw it at like some files and say like, find me bugs. And then there's
a round of that. And then people can jury-rig it up a little better to
find more bugs. But like, do you think that we could exhaustively like actually
make a piece of software more secure in the sense of like, we removed a

[00:29]
bunch of the bugs and like, if we all run these agents for the next
2 months, like we'll have found all of the bugs
that agents are going to find aside from the margins, and it will go back
to like, there are 10 people in their basement submitting the bug bounties and
what are the tools they have as agents? Or is there an infinite plethora
of bugs? Like, there's something to be said about the population of bugs and then
like how these agents are finding them. And like,
are we approaching zero or yeah.
Okay. I think it's a very good question.
High-level answer, I don't know. I think, yeah, I wish
I knew the answer. This would be great to know, but yeah, not yet.
Okay. Yeah, me too. Jesus Christ, that'd help a lot of work.
Yeah. Okay. Yeah. So first
answer is that even if it was
the case that you could exhaust all of the bugs with one specific language model,
it's still the case that these models are getting a lot better over time.
And so you can imagine a world where we exhaust all of the bugs that
can be found with, you know, Opus 4.6.

[00:30]
And OpenAI comes out and releases GPT-5.4, which they
did, I don't know, whatever, 2 weeks ago. And then like maybe
this one finds a bunch of new bugs. And then Google comes around and releases
Gemini. Let's see, they're on 3.1. So they released 3.2 and this one like
finds a bunch of new bugs. Like, so you could imagine a world where even
if you could exhaust all the bugs with one model, like we're still in this
increasing exponential capabilities. And like it seems likely to me
that we will be stay there for a little while longer. So there's this aspect
of it. And then the other aspect is,
I like to think of this as like,
okay, so fuzzers find a restricted class of bugs that are fairly
easy to enumerate. And so it's fairly small,
the attack surface is fairly low. And this means that once
you've probed it a bunch, you can sort of have hardened that shell.
As you get better and the models are able to find, attack a
larger attack surface, you have to do more work to exhaustively find
all of the bugs that can be scanned in that surface. And each time

[00:31]
the models get better, the space of attacks grows again.
So now that we can have pretty good bug finding without Oracle
that gives you ASAN crashes, this gives you another attack surface
that you can start to measure against. And I think that each time you
do this, you have to do more work to make sure that you've
done like, pigeonhole principle,
whatever, like you need to have done a huge amount of work
in order to make sure you've found all of the bugs, even if they were
finite. And each time that you increase the surface, it gets even harder.
And so this is maybe my other concern is
it may be the case that it's finite, but you
could imagine that, yeah, the more powerful models might have a bigger surface to hit
between. Really? And so getting
back into that, like, for the Firefox example, then,
like,
do you have like an estimate in terms of even if it's finite,
like not getting there, do you have an estimate to how much

[00:32]
time it took Firefox engineers to patch all,
what was it like 50 bugs or whatever it is? Relative to
how long like Claude ran, um, to find,
and then even for, for say you to validate,
um, let, let's include the time that you or anyone else at Anthropic spent validating
the bugs. Mm-hmm. Um, relative to how long it took Firefox to,
to patch them. And then not to like knock on like, not like
if Firefox shelves some of them, like let's not count that time. Just like actual
time spent by engineers trying to patch these things. Yeah. So I don't know exactly
how much time Firefox spent. Um, the bugs that we found there were found
by one person, Iftikhar, who, yeah, was working for, I don't
know, not more than a month on some harnessing,
probably a couple weeks. Probably most of this was reusable
work because like, I don't know. Okay. Some people— Yeah, it takes
a while to rig a browser, but once you've done it once, it's copy and
rig. Yes. But some, like, he sort of did it properly and like hooked it

[00:33]
up into the Anthropic infrastructure in the right way. I sort of do some things
just like, I don't know, I just turn on a bunch of Docker containers on
the same machine. I go grab a machine with 100 cores and just call it
a day and just run it over a weekend. Other people do actual
engineering and make it properly distributed. He did it that way. So it's like a
reusable infrastructure that if he wanted to spin on something else, he could do
that. And so, I don't know how much of the work was on this,
but it was not more than a couple weeks of work. To like
harness the whole thing up. And then yeah, we like let the models go and
churn for a while and then we sent off the bugs. So yeah,
I think we sort of got most of the bugs that we could find with,
with Opus 4.6. But like, I don't know, my guess
is if we were to run it for the same amount of time, we'd come
up with a couple of more. I don't know how many, we should probably have
some numbers here at some point. I'm hoping to try and run some like science-y
experiments, like measuring these curves over time. But like, we don't have that

[00:34]
quite yet. It's like still, yeah, very early. Mm-hmm. But so we can
probably then like at least estimate on the short end, you spent, let's say 2
weeks and then let's say each bug took an engineer day for Firefox
to patch of, of those 30. And so that's at least like roughly
2x the engineering time to fix the bugs than it was to find the
bugs. And that's including like reusable engineering time.
Yeah. Also then like the, it's like just legitimately harder to patch
than it is to find these. Yes. Because like you can't make functionality, like you
can't just like, like the, the model Oracles are
great because finding crashing inputs gives you the most perfect oracle.
But if someone wants to fix it, you have to understand first
how it happened. Actually, as a sort of aside, language models are
actually very nice because while they don't always give you a perfect explanation of what
went wrong, it's so much easier than, "Here is a fuzz crash." Just
like, "Here's some binary." The bugs that we have come with Python
programs that generated them. And so like, even if you, like, it sort of misunderstands

[00:35]
why, like you can at least like, okay, so, so it's a little, they,
they, the Firefox people found it a little bit easier to actually fix
these than like normal fuzz crashes. But yeah, like they did have to spend
quite a lot of work on like, you know, making sure that what
they're going to submit is not gonna like break some user functionality. And so I
think this is one of the asymmetries here. And you were
kind enough to give them effectively 100% valid bugs.
Uh, 'cause another approach could be to just use the bug bounty as an additional
oracle, um, uh, to help with, with,
with the— and some people in the past have, have tried this and have gotten
many people mad at them. And yes, we are trying very hard to not
have— also the latency on that oracle is pretty, pretty large.
Like from, from Chrome side, like relative to
February 2024, David eating his feelings
here. 2025 had 5 times the submissions.
Um, and then March of 2026, today's the 19th,
already has, um, over twice

[00:36]
as many submissions as the entirety of February did. Um, and you
know, some of that is our own like damn fault for, um, uh,
basically being particularly like lenient and nice for years.
Um, because that was like You know, what we,
uh, um, there's just the way that the Chrome VRP has been known for,
like, being very easy access to get to engineers. And so,
um, but, uh, yeah.
Firefox saw the same thing. Mozilla had a plot, um, where they, like,
showed the number of bugs that were found, um, over time.
And yeah, so, like, we found, I think it was, like, 20-something, which is,
I don't remember what the exact number was, like, 25% of all bugs that
were found in last year, we found like in one,
like in one batch of reports. But what you like,
many people didn't notice is like this, this chart had like two
bars stacked on top of each other. There's the ones that we found and the
ones everyone else found. And it, the bar was like a lot bigger because we

[00:37]
found many more. But if you remove all of the bugs that we found,
last month was also the biggest month that they had seen in like the last
two years. Oh, right. And so like, I, I can't, I mean, I have no
inside information on, on, on Firefox. But it's like, I can't sort of tell you
that this is causally related, but I don't know. It's, it seems plausibly
related. It's happening at every bug bounty, right? Yeah. And, and,
and this was like, to be clear, like the, like these are the real bugs
they got CVEs for. And so, you know, like the, the numbers on submissions I'm
sure are going up, but like the number of outputs is also going up.
Yeah. I think like bug bounty incentives were always kind of weird to begin with.
And these programs are all kind of like, they're all in a, and I
guess maybe except for Google, they're all kind of ad hoc. I don't worry that
much. About like the long-term impacts on bug bounty programs that people just iterate
and come up with better bug bounty terms and stuff. There's some of
that, but also like, I, I don't worry too much
about bug bounties. I worry about the people at bug bounties on like large platforms
and browsers, like in the, the sort of near term. Um,
but I, I think like it was actually Jeff Belknap who

[00:38]
used to work for you, Thomas, I think, um, when he was CISO of LinkedIn,
like over 10 years ago, I think he was, he gave this talk
that was like, bug bounties are stupid and you should stop running them. Like the
only people that run, that should be running bug bounties are basically
platforms. Are you an operating system or a web browser or like a phone vendor?
Sure, run a bug bounty. Otherwise, or like, are you
running other people's code? Maybe run a bug bounty, but otherwise, like, get over yourself.
You're, you're just like wasting time. And I feel like
everyone's just gonna come to that, that, that realization, like curl did
it. Is a notable example, but like everybody
that's not huge is gonna shut their bug bounty down.
And then the big bug bounties are all gonna be much, much more strict about
what they'll accept. Yeah. Just because of overload? Yeah, because it's very
easy to generate a, a reasonable looking bug report now. And that
might be wrong. Like previously, like how well you format, did you follow
the format? Did you submit the requested thing? Was it fully filled

[00:39]
out? Was like a good proxy for are you reasonable? And now it's not.
Whether, whether some human should invest their time
actually validating it and testing it and trying to reproduce it and coming
up with a patch. Yeah. You're also gonna see more of like, yeah, you're not
allowed to give us a bug that isn't basically like coming with a POC unless
you've previously given us bugs that came with a POC and then we'll be willing
to listen to you because you have a reputation. But like
otherwise, good luck. I wanna talk
more about the science of finding bugs. I wanna talk more about like what the,
what the fuck is going on here, right? So yeah. All right. All right.
So hold on a second, Nicholas, when we're, when you're looking
at what's happening right now with 4.6 maybe, and just like going
straight into there, like, is it that like, is it that the models
are like, have superhuman attention spans and they're
basically doing what you and I would do um, looking at code,
but they can hold up attention over huge amounts of code and keep lots of

[00:40]
context in their heads and find more stuff. And it's just a fact, it's just
a function of thoroughness. Or is it also the
case that the models are maybe for some of the same reasons,
really good at finding intricate corner cases that even if you and I stared at
things like we can't hold enough stuff in our heads to find all the weird
bank shot conditions that would make these things work. Is it Either
or, or both, or how much? So far, all of the
bugs that the models have spit out, once it produces the, like, report,
I can understand. Like, I can, like, it's, like, pretty clear to me what's going
on. Like, if it's not yet producing reports where I read them and I'm like,
what is this? Like, it's like, you haven't seen a model do, like, the equivalent
of AlphaGo, which is like, it does moves that no human would ever see or
think of. It's not doing that yet. I don't know how it got there,
but like, you know, the final report, like, when I file the bug report.
Like I am able to like, you know, concisely explain in,
you know, a page or two of text, like, you know, what has happened.

[00:41]
Sometimes these bug reports are, well, yeah, so the Linux
one, for example, this was like some, so the bug we have
was, we have several of them. One of them is in,
I think this is in NFS daemon. It's, the bug was 22 years old.
Um, the bug, so in Linux, you, um, what the,
the way the commit format works is they like you to say like, you know,
fixes colon, you give a git commit hash of the, the, the commit that you're
fixing. Yeah. Um, uh, I couldn't do that. So like I had to give a
change set. A fresh fix has to go back 22
years and be like, this commit is the one that introduced this bug. I couldn't
give a commit because the bug predates Git. Oh my
God. And so I was like finding the change set from 2.6
that introduced, and so like, okay, so, um, Yeah, okay,
this is so like, you know, like this clearly has something interesting going on because
like, you know, many eyes have seen this, but like when I tell you what

[00:42]
the bug is, you know, like you can understand it. Like, so it turned out
that like there was something where, you know, if two clients are cooperating
and they take a lock on the same file and one of them has a
really big name and the other one like gets a lock denied error, they're like,
or big person's name gets echoed to the other person and overflows some buffer on
the heap. Like, this is like not, you know, some obscenely complicated,
like, magic that's happening here. It's just like, it's a bug that,
like, you can see why this, like, might have been hard to discover because it's
like, it requires multiple clients that are, like, interleaving packets in the right
way. And, but like, it, it's understandable
once I tell it to you what's going on. You know, all bugs are shallow
in some sense. Uh, at least, you know, for the moment they still are.
That, that one reminds me of how, like, concurrency and
async always tend to be just gnarly and
like part of the reason that, you know, Chrome, not Chrome,
Rust is not like completely free of concurrency
and async bugs. But it does make the severity because of the memory safety and

[00:43]
type safety and all the things that come out of that a lot easier to
do and a lot less severity if you, you shoot yourself in the foot,
it's logic bugs. But that sort of bug definitely
feels like of a piece of like humans are really bad at looking at a
piece of code. And transposing that to the network
topology and state machine of asynchronous clients doing a state machine
transition together. Yep. I don't know. I don't know. I wouldn't have thought that the,
a model could also reason through that in its brain. I don't know.
I'm gonna clear it like, you know, like through its context, like, you know,
it has, it has in some sense like understood this at some deep level in
order to come up with, with this bug. Like this is a non-trivial sort of
piece of reasoning you had to do in order to like like, you know,
construct multiple clients querying in the right order. Right. Like,
you know, yeah. It's just like, there's like some of these things that like are
quite interesting and like, so those are one class of bugs, um,
that it finds that are interesting. The other class is like just things that fuzzers
can't find that like are just boring. Yeah. But just like,

[00:44]
you know, I have so many bugs in protocols that have
checksums, like just like, you know,
AFL has a very hard time generating valid CRC32s.
Um, and so like, it's just like not a thing that you can fuzz once
you have to include this in your protocol. Um, but like language model can just
like find the bug and then write the, write the input and then check,
write a Python program, compute the like checksum, add it to the packet and then
send it off and then it crashes. And so you'll even have other classes of
bugs. Yeah. That, that, that makes sense. 'Cause like a fuzzer is a brute force
search, right? Exactly. And it's like, right. And like, yeah. Okay.
So. Okay. I thought I had more to say about that,
but I had a fuzzer is a brute force search and that's where my insight
capped off there. Keep going. I'm sorry for interrupting you. Oh,
that's fine. No, no, no. I mean like, yeah, this is exactly why, right?
Like even if you like start doing some kind of branch coverage kind of thing,
right? Like it's just like, it's very hard for AFL to like discover
the right sequence of bytes that like, you know, happens to give a checksum that's
valid. And so it will just like very, very fast. And so yeah, it doesn't

[00:45]
have a, it doesn't have a theory. It doesn't have a theory of the code
and whatever the fuck is happening inside the model, the model has a theory of
the code. Code that it's chasing?
Well, the model can just like ignore the— it knows that there's this line that
says, you know, it's gonna do like this compute CRC32. It will reason about the
rest of it. And then when it gets to the point where it needs a
CRC32 to match, it can just go run some Python code to generate the correct
CRC32 hash, add that into the, into whatever the object you need,
and then it will, it'll pass. And so like, this is like a, a sort
of the, the, the power that the model has that like, you know, the fuzzer,
which is just looking locally at like this individual branch is like unable
to to do. And so you can find a bunch of bugs that are entirely
trivial things. There's like another bug that we,
that we just, was just patched in FFmpeg 8.1,
which again, 20-something years old. It's a bug in H.264
introduced in the original commit that added H.264 to FFmpeg.
And it's a bug because there's like some overflow

[00:46]
where if you have some number of frames, that's exactly, you know, 65535 frames,
then you can overflow something.
And like no fuzzer in the world is going to like, you know, run through
the loop 65,000 times and then eventually have a crash,
right? It's like a very, very boring bug, but like a fuzzer's not gonna find
it for this reason. Knowing what the code is that's broken there, if you looked
at that code, would you have spotted it?
Maybe. I think if I gave you a one-sentence description,
I think you would find it. But like empirically, you know, the code is 20
years old. It's in FFmpeg, it's in H.264. It's not like some obscure codec.
And like it's still present. So I mean, like, you know,
knowing that there was something to look for is like a very, very big hint,
especially if I tell you like, you know, what kind of thing you're looking for.
There was like, um, earlier this year or earlier last year, whatever it
was, right? There was the DARPA Cyber Challenge thing, right? Mm-hmm. Where a bunch of
different teams put together kind of complicated systems for finding
vulnerabilities, right? Mm-hmm. So if we, if we think about the work that you guys

[00:47]
were doing with FORSIX, And if you kind of divide
the universe of, you know, finding vulnerabilities
with AI into like the quality of the model, the quality
of the harness and the tooling that you build around the model and the quality
of the prompting that you do, right? Like the domain-specific knowledge you bring about
the target, about the vulnerabilities to that, that thing, right? It sounds like for
the, for the FORSIX work that you guys were doing for like the Anthropic Red
500, you know, zero-day thing, heavily, heavily biased towards just the
model. Right? Like there wasn't basically almost no,
you know, work done at all there. Right. And like I would've said before
we talked just now, let's like this, or before I saw the slides for the,
the talk and all that, right. That like the state of the art is coming
up with better and better harnesses. Right. Like,
do you see, like, do you see the result that you guys got and the
success that you got as like an indication that you have the right allocation there?
Or is it really just a function of like, you guys have time to do

[00:48]
this amount of stuff and also your incentive is to make the model as good
as it can possibly be at doing this stuff. And like other people's job can
be to figure out what the best harness thing is. Yeah, definitely some of all
of these, right? Like, okay, so like part of the reason why we are looking
for these bugs is, okay, so I am looking at these bugs 'cause I like
finding bugs. Yes. And the reason why Anthropic is willing to pay me to find
bugs is because like they in part just like want to understand the capabilities of
their model. They have this model, they want to know what can this
thing do, they want to ensure that it's not going to go and cause a
bunch of harm. Part of what they care about is just tell
me how good this thing that I have is in front of me. And what
it can do, not even how good it is, what it's capable of in general.
Yeah, exactly. Part of the incentive
structure here is just we are in some sense incentivized
to just to try get some base understanding of what's capable. And then
I could almost certainly scaffold this better and probably find some more bugs.
But in the time I would have spent doing that, there will be another model.

[00:49]
And then I could just find more things. And oftentimes
you find this. Okay, so the thing that happens is you
write a harness that's really, really, really good for a particular model.
And then the next model comes out and it's better in ways that your harness
is no longer helpful. It's now restrictive. Yes. So there's a couple of
nice examples. So I did this once.
So last year I wrote a paper where I had some language models try and
break some machine learning stuff. And at the time when I did this, I started
writing the harness in November of 2024. The paper
came out in January of 2025. In order to get the models
to do anything sensible, I had to say you could edit the following
6 files. You can run exactly these 3 Python commands and do nothing
else because if I give you some agency, you will brick the
machine. I couldn't do anything. But then today, the last
couple of days, I've been running this harness again. And if you run that with
today's models, they're trying to launch

[00:50]
jobs in the background so that they can then read code while something else is
running to save time. And it's a good idea.
Harness needs to let you do this. There have been some benchmarks that
even other people have found There was this
science-adjacent benchmark by some folks out of Princeton where with Opus
4.5, they initially found that Opus 4.5 was scoring like 40%.
I trashed their entire harness. I just gave Claude code the harness, the thing,
and I said like solve it. And it was like 92% or something. It was
just like, you know, it's like this is like a common thread where like,
you know, you spend a bunch of time building something fancy and the next model
just like doesn't need that fanciness, which is not to say that this is like
a useless endeavor. But like, you know, it's just like, you know, at the,
when, when things are increasing at the rate that they are, like, it's kind of
like kind of hard. The time that it takes you to write the fancy harness,
the next model comes out and like, it's good enough that like you didn't need
to have written that harness. There's kind of like a thing, there's a thing with
like coding agents where if you watch carefully what's happening there, they really

[00:51]
kind of collapse down to just the ability to run Bash, right? Like they only
need the one tool. They only need the one tool, but they get Python through
Bash, right? Yes. Like all they, all they need is Bash and then they can
find their way into the rest of everything else there. Right. And so like,
and Awk and stuff. But like you're
giving, you're giving the LLM, you're, you're giving 4Six access
to an environment that has fuzzers and debuggers in it. Like to what extent is
it using tools versus to what extent is it like looking at code and then
making inferences about what's in the code? Yeah. So it usually is
just looking at code to like an annoying degree where like,
I'm, I'm sure that someone could come up with like a better prompting thing that
like would like have it use the tools more, you know? Okay. A thing
that it has a really hard time with is running GDB interactively.
Huh. The harness is just not set up,
the Cloud Code Harness, the Codex Harness, because it has to launch the program and
send keys to it, which is just not exactly how the harness is set
up. And so what you'll find when it does is instead it runs GDB and

[00:52]
just reruns the program from init, passing the sequence of commands that it wants,
and then it runs and hits the breakpoint and stops. And then it reruns the
whole command again and just adds on the next step. Which is like a terribly
inefficient way of doing the thing. Quadratic GDP.
Yeah, exactly. But like, you know, like it's like
sometimes like they're just like not very good and like they do these dumb stuff.
Sometimes it would be generally better if they did more of this. But like,
yeah, again, we could do more to improve the harnesses.
They are smart enough to go through the Git logs and see if there were
previous vulnerabilities and then generalize from the vulnerabilities.
Yes. Yes. They do, they do this too. Yes. They're also dumb enough
when I'm like in a fresh context to be like,
revert the thing you just did. They're like, okay, I will go to a previous
Git commit. I'm like, there is no previous Git commit. Commit.
Shut up, robot. Yeah.
What's, so like while you're on the topic of like 4.5 and harnesses
and all that, like what changed 4.5 to 4.6? Like,

[00:53]
is there like, was it like a step function there for you or like?
I think 4.5 was the big step function for me where
4.5 really gave some
intelligence in the model. I don't know what you want to call it. I hate
using the word, but just soul, spirit,
humanity, essence.
The model just started to get a lot better.
That was really the big one. 4.6 again just made it even better.
OpenAI saw the same thing with 5.2 was just like a big step increase.
And 5.4, again, people have found is quite a bit better.
And I don't actually understand a lot of why
the models get better. I don't know, I have enough things to be doing,
sort of playing with them. But someone just says, here is a new model checkpoint,
please play with it. And I'm like, okay. And then I go do my things.
Scaling works, which is like a, unfortunate thing that
I didn't want to believe, but empirically has turned out to be true. And for

[00:54]
the foreseeable future, it appears like it's going to remain true. It's terrible, right?
It's a really bitter lesson to learn. Yeah, I was going to say, it's terrible.
It actually is terrible, right? Because all of the fun problems are
gone. You just have to sit there and wait for them to come up with
a new model. I hate it. I mean, this is a real sort
of question. Yeah.
The fun problems are not. Gone. 'Cause like, well, now we have
two different problems. The two obvious like follow-ups for like, okay, the models are
really good at finding bugs now, are the models really good at exploiting bugs?
Have you had Claude write exploits or is that like too woke for Anthropic?
And then step two is like, could you maybe
try patching some of them? Yeah. Okay. Yeah. So, okay. So let me talk about
each of them in turn. So exploits, it's getting better. It's like
not yet excellent at exploits.
In the Firefox case, we had a separate blog post on the Anthropic
blog where one out of, I think maybe two out of

[00:55]
500 times, it was able to produce a JavaScript
exploit that was able to— So
the bug was some heap thing. What the model was able to do was it
was not a heap spray, but it allocated some other object on some
other memory, overwrote the function pointer to point to
some other thing, and then called and it was like, I don't know, some 10-chain
deep thing that eventually got at some point that I could then call out and
go write some stuff. It was able to do this some of
the time. I think a human could definitely do that much better,
much faster today. But 4.6 was the first
model we saw any sign of life on the exploitation. So yes, I would like
to measure this. It's not clear to me I want to make the model better
at this, but I would like to measure this to keep track of it because
The trend has been first you don't do it at all.
If you don't do it, our overseas enemies will with their open weights

[00:56]
models. I mean, yes, there are many reasons why I want to keep
track of what the current capabilities are. But yeah,
I definitely do think that you
can't bury your head in the sand. The capability frontier
is advancing. The best that I can do is to like measure what is true
and then just like talk very loudly and say like, please be aware of the
following fact about the world now. You know, like it was nice when,
you know, we didn't know about Spectre. Like that was just like a nice world
to live in, you know, like, but like too bad, like it turns
out a true fact about the world is you can do side channels and you
can have these CPUs and like, you know, like now everything is worse, but like
that's just like the world we live in. Same thing with like, you know,
ROP. Like, wouldn't it be nice if write or execute was like,
you know, just the perfect solution? But like, it's like not, like, it's just
like, here is a true fact about the world. Like, you can do this thing.
Now we have like this other thing that is true in the world. We have
these language models that can find these bugs and potentially soon exploit

[00:57]
them. And maybe we wish that like we
didn't have these things, but like, you know, they exist and we should like measure
the capabilities that they have so that like we're not just blind to what happens.
I know that you're like, I know that you're, I know that you're not like,
you don't speak for Anthropic, let alone for OpenAI, but like my
understanding of the OpenAI situation is that if you want to use Codex to find
vulnerabilities, that there's some program you sign up for to do that,
right? If I wanted to replicate the kind of things that you are doing right
now with just my Claude subscription, can I just do that and it'll work?
Yeah, we use the production model API and
run the things that we have been doing. So like, you know, I have like
the exact set of weights that, I am using or the set of
weights that you have access to run. I think there are,
okay, there's a question of scale. At some point in the last
couple months I've spent lots of money on doing some of this. So some
of that is how much you're willing to pay. There was like, there used to,

[00:58]
I don't know, you're young, but you may remember there used to be a thing
called Folding@home where people had like, right. So people
had computers that were sitting there doing nothing and you could harness them to do
stuff. And now people have these gym subscriptions to cloud where
I have the Claude 20x Max or whatever, but I'm really only using a tiny
amount of my tokens. So like if I built the thing that just like took
everybody's spare quota for their tokens and then used it to like find
vulnerabilities in open source code, you guys would be fine with that. And hold on,
I said you guys, I didn't mean to say you guys, I meant you,
Nicholas Carlini, would be okay with that. Pretty sure
that would be a violation of terms of service and the spamming of the tokens
and the account subscription. And it wouldn't have anything to do with the use of
the, use of the time. I can't, I can't get
over the fact that like the input to this whole thing is just like you,
you find a target like Ghost and you check it out in a Docker container
and then like you write a bash loop around like all the files in that
thing and like a dumb, no offense to the quality of your prompts.

[00:59]
Production Claude Opus 4.6. We should all,
we have another one of these that we're going to record relatively soon and the
three of us should come back to that having done this and found a bunch
of vulnerabilities. It seems like really easy to go try and do this and find
vulnerabilities. It's weird to me that I'm not finding, yeah, it's weird to me that
I'm not finding vulnerabilities right now. We should have opened the podcast by
starting to like look for one. Should we just click the button? Well, I guess
we'll have to have fun staying poor because we're not submitting to bug bounties with
all of the bugs that Claude found. But like the flip side of
that question is like, well, why aren't these fucking projects running it themselves? Right?
Like I say, as somebody who has to deal with
bug bounties a lot. Fault. Yeah. Right. Like, I feel bad, like, you know,
blaming, like, you know, like the open source developers did nothing wrong. Right. Like,
like they put something out there in the world that like is like trying to
be good and nice for everyone. And I'm like, you know, along comes this like,
you know, bug hunting machine and like, you know, like it's like,
I don't know, I quite bad saying like, you know, it's like their,
their fault in some sense. Yeah, absolutely. But like, you know,

[01:00]
I do think that like people should spend more time doing this. Maybe this brings
us to the patching question that you which is that like, you know, we,
we, yeah, we have been trying quite hard to do this. You know,
Anthropic now has this tool called Claude Code Security,
which is this like patched proposal thing.
DeepMind has this CodeMender thing.
OpenAI has Aardvark, I think they're calling their
thing. Like there's like a lot of people who are trying to do this.
And I think this is like very, very useful and very important too.
It's just the case that it's harder to automatically
patch than it is to automatically find bugs. And what you really don't want
to do is you don't want to propose like, you know, hello, I am here
to help. Here are, you know, 500 PRs that I promise fix bugs.
Please review them all. Like you're like, you're, you're not, you're like,
the developer's gonna have to spend almost as much time reviewing the correctness of
these PRs as they're going to have to spend as if they had patched them

[01:01]
themselves, more or less. They're gonna reject a bunch of them because because the model
put it in an entirely reasonable point, but it's just not aesthetically
where the developer wanted to put it in the first place. And they care about
the quality of their code so that they understand where things are. And there are
a bunch of difficulties here with patching that just are not
present when I'm just throwing wrenches and finding bugs.
It's a much harder question to try and do this patching thing.
I'm glad that all of the 3 companies are trying quite hard to have a
product that will do this. And like are proposing tools that will, you know,
find as, as do, do as good of a job as we can given the
current capabilities of the models. It's just like, it's so much harder to do.
Mm-hmm. Yeah. So it seems like there's like a kind
of two ways that we can go from here is like we, we could be
in like a local minimum where it is now, it's like really easy to find
bugs and then, but it's not like super easy to patch them.
But like once, you know, the next iteration of models comes out out,
then they'll be able to patch all the bugs. They'll like, the model's fine.
And we just have to like suck it up in the meantime.

[01:02]
Another one could just be like, well, no, now there's just like more bugs everywhere.
And like, I don't know, maybe we get marginally, you know, better patching them,
but the rate of bugs is coming faster. And then the variant of that
one is like— We can see them now. They were there. We can just see
them now. You can see more of them. And it's like, I haven't talked to
a single person that thinks that we can like exhaustively
enumerate all of the bugs. Bugs. Yeah. That, that like, especially in, in a large
codebase, like a browser, like at some point, like you, you just
end up in this like metastable state where fixing the bugs introduces new bugs and
you just kind of like, um, have jobs. I'm actually pretty optimistic here about
like not introducing so many new bugs because like you can imagine a world where
like most code that gets committed gets reviewed by one of these bug hunting things
and like, it's not gonna be perfect, but like, I do think that we can
reduce the number of bugs that are inserted into code. By like
doing a code review on, on newly inserted patches. It's not gonna be perfect,
but I think, I don't know, like we can,
like, so, so a big part of the problem when you're doing this bug hunting

[01:03]
with models is like finding ways to efficiently like burn tokens.
Yeah. And having it like, one thing that you can very efficiently do that like
there's a lot of tokens you can burn is by reviewing commits.
So you could like, yeah, burn tokens just by going over all of the commits
that you possibly can. But a big problem is, you know,
it's just like, it's, so there's too many commits. It's like very hard
to actually go over all of them. But if you have only new commits,
then you can at least conceivably try to
just like make sure that we're not inserting more new bugs than we're fixing.
And like, I don't know if this is something that's gonna actually be feasible,
like over the, you know, if at scale, you know,
Chrome probably gets lots of commits. But I do think that you could reasonably
cut down a large fraction of simple bugs that people make
because no one sort of checked the first time. I don't know what the
ratio would actually be. I wouldn't be surprised if you could catch half of the
bugs that are accidentally reinserted by having a model re-review the code.

[01:04]
Presumably there's some way to index the codebase,
right? You have a context efficiency problem that you're dealing with
here, right? Which is like those commits come in, they're nice small
scope, right? Like you can fit 'em in really easily and then like it has
to do a search to get the rest of the context for the code,
which is gonna kind of blow up the context. And you have all this interprocedural
stuff and that's, so you have to kind of reason through that. But you can
also like, this is like, like, like kind of right now the standard
trick that people have for handling context is just to write things out to files,
right? Mm-hmm. And then have it read in like specific files strategically.
This is more harness work, but like you can imagine projects that wanna get better
at like, you know, using LLMs to screen for bugs, just like
kind indexing their code in some way, like having like text files to read,
like, here's the context for this kind of vulnerability. Like here are the things to
look at, like these functions need to be safe for these kinds of inputs kind
of stuff. Yeah, definitely. I mean, yeah. Well, but right again, you know, we have
the advantage that like, I'm not paying for my tokens. Like I'm not incentivized to
like write the like harness that will give me 90% of the efficiency at like,

[01:05]
you know, 5% of the cost. Yeah. I think it was like, you know,
I'm, the market will do efficient market
things and people will sort of emerge with, with products that, that try and give
you this. And I'm sort hopeful that those will emerge more quickly than,
than they have been. It, it seems like
the other thing that like is potentially a risk is like, you know, right now
you kind of think there's like two broad groups of attackers. There's like sophisticated
attackers and like unsophisticated attackers. And unsophisticated attackers just
like call your grandmother and say that they're Microsoft and
ask her to like install an RDP server. Um,
uh, and props to my grandmother for recognizing it was a scam and unplugging her
computer. Here. Um, but, um, like,
that's like one whole side of the world is just basically like abuse or like
tricking people into installing malware and then like writing the malware. But the way it
gets on your machine is you installed it with Minecraft by accident. And then there's
like the side of the sophisticated attackers that are like doing exploiting memory corruption
bug. And then a lot of the effort that we spend in, in security is

[01:06]
like on the sophisticated attacker side. That's like basically like 70% plus
of the bug patching. Is dealing with them, but they're actually
a very, very, very small amount of the actual exploitation. There's not a
lot of people doing them. You know, if you look at like the number
of commits that are like known exploited in the wild or number of CVEs in
a browser that are known exploited in the wild compared to like the number of
CVEs they issue per year is very low.
Do you think that we're at risk of like, of that becoming like
that this thing that was high-effort targeted becoming broadly
adopted at scale in the same way just tricking people into installing malware or an
Internet Explorer toolbar 20 years ago was.
Yeah. I don't know what I'm more worried about here.
I think you should be worried. Yeah. Okay. So let
me answer a question you didn't ask first and then I'll come back to the
question you did ask, which is, I don't know. It's very, very fun to find

[01:07]
these memory corruption things, but In practice, most exploits are
just someone forgot to patch their service and it's running something that's known vulnerable or
they misconfigured something and now they left some port open or whatever.
I'm very, very worried about the ability of models to find and exploit
those class of bugs because there's just very
little that's new there. It just needed someone to go looking for it.
The big problem that I have is I can't measure this because I just can't
go scanning random internet services and try and like find stuff. But like, I am
very worried that like random people will pretty easily be able to do this.
So I think this is like one form of thing that like people will be
able to do, even if they don't know anything about memory corruption, just like,
you know, find open services and like, you know, find things that like are just
running servers that haven't been updated since whatever, 10 years ago.
And then look at like, you just like own it. I'm also worried, yes,
about random people being able to find novel zero
days. It's unclear to me which of these things I should be more worried about.
I would like someone to try and figure out how to measure this in some

[01:08]
way. I don't feel like I have a good answer
which one is the most concerning, but I do think that we are fundamentally
entering a new world on the order of
having recently discovered that you can now smash the stack.
Every once in a while you get these things, the world is different and
like, you know, you'll end up with like,
you know, 2002 to 2004, the like, you know,
the wave of worms and everything hitting was like immense.
And like, I'm like kind of worried that like we'll have that world again where
people develop software in a world that was not, that did not like think
about security as like a first-class object. And then it
turns out we widely distributed the understanding of
how to go and exploit these things. And then you end up with, you know,
whatever, every other 5 days some worm that takes down half the internet.
It is kind of an inversion of the standard concern that AI skeptics have

[01:09]
about this whole situation is that everyone's writing code with LLMs and
that code is all going to be riven with vulnerabilities because the LLMs are
stupid. But the reality is is like LLMs are pretty reasonably good at
knocking down kind of standard vulnerability classes, much better than we are,
right? I think that's probably not much in doubt, right? It's like the first cut
an LLM has. Yeah. These are not contradicting statements
though. I think like it can both be true that the model can write dumb
code and it could be true that, and like, it's like I sort of talk
to some people who say this and they're like, I agree with you. Like it
would be really like, I trust currently people to write code more than I trust
the models. But also it can be true the models are bad there and they
could be good at other certain classes of things. For example, finding vulnerabilities.
I get very frustrated when people try to deny the
reality that the models are actually good at certain things and they may not be
good everywhere. There's many places where I wish that people didn't
use them, but we should at least be acknowledging the things that they can do.

[01:10]
Sorry for the small rant. No, that's okay. But you have to
disclose which thing in security which people weren't doing with LLMs. It's not necessarily
insecurity. I just mean other things that, you know, like I have gotten
a number of emails from people who I know that just
have too many dashes and the word genuinely. And I'm just like,
I care to hear what you— Yes. It's just like, yeah,
I care what you have to say, not what the model has to say on
your behalf. Do me a solid and write me an email from you, the human
being. Thanks. Yes. Right.
Yeah, I gotta say, like,
I've been pretty bearish on kind of startups doing this stuff
on like, you know, vulnerability hunting startups. 'Cause I figure both OpenAI
and Anthropic have just like multifactorial incentives
to get really good at this. Like both for like the good
of the world and also because it answers like the chief objection people have to
building, you know, code with LLMs is it's gonna introduce security vulnerabilities.
There's all these reasons why all of the frontier model companies are just naturally

[01:11]
going to get good at this stuff. But I think you probably got 10 or
15 different startups funded just by saying that every time a new,
a new model company introduces a new model, it finds new vulnerabilities,
which means there's now space for everyone just to say, yes, but we're a multimodal,
like, finding vulnerabilities startup. No,
I do think there's good reason for companies to exist that are doing this.
You know, the costs are one of them. I do think that, like, you know,
the frontier labs are somewhat incentivized to reduce costs,
but that are maybe less incentivized than a startup might be.
I do think startups can be distributed
across multiple labs. You could imagine that Model 1 proposes
a bug and then Company 2 is better at auditing it and so you combine
them in clever ways. Expo actually has a nice interesting blog post
from a year ago where they Franken-modeled something where every other request
that went switched between OpenAI and Anthropic and
doing this in this way was better in some ways than either alone.

[01:12]
I think there's lots of interesting things that can be done. I think there is
work to be done on scaffolding the
models better. This exponential right now reminds me of
the exponential from CPU speeds
going up until let's say 2000 or something where you had these game
developers who would develop really
impressive games on the current thing of hardware and they do it by writing like
really detailed intricate x86 instruction sequences for like
just exactly whatever this, like, you know, whatever 486 can do,
knowing full well that in 2 years, you know, the pen
team is gonna be able to do this much faster and they didn't need to
do it. But like you need to do it now because you wanna sell your
game today and like, yeah, you can't just like wait and like have everyone be
able to do this. And so I do think that there definitely is value in
squeezing out all of the last little juice that you can from the current model.
Models. And the frontier model developers companies are just not quite the
same way incentivized to do all of this. And so I think there's plenty of

[01:13]
room for people to try and build stuff with these models. And I would
like to see more of it. What I just don't want to see is people
putting in work that is just entirely wasted and
late enough that the next model is just better than what they would have done.
And it was just not efficient in ways where If
John Carmack had spent 5 years writing super
efficient Doom things and had released Doom in 1997, right?
It just could have run it just as efficiently on whatever unrolled C
code compared to whatever optimized assembly thing he wrote for whatever stuff. So it's
like, right. I just think people need to be a little careful with how they're
doing it. I'm just going to say my company
pays for my subscription, so if I come back
Next time we record and I don't have a vulnerability, you guys should all make
fun of me. Okay. We will. Sounds like
you're respecting shareholder value. Indeed.
Um, this is fantastic. I'm a little bit scared, but also a

[01:14]
little bit like excited. So I think this is the right reaction. Like I,
yeah, I'm also quite, quite worried. I think like, you know, I think if
you have played with these things and you are not a little bit worried about
what is about to happen in the world, I think like you are not thinking
critically. I think it's happening here first,
but I think it's going to happen in many other areas too. It's not obvious
to me. I'm not an expert in the other subjects of the world.
I think we are seeing this first because these models happen to be very good
at coding. But I do think we should think through this very carefully.
Other people will encounter these problems next. I would like to
just have the world start thinking about these things I
do think things will look quite different in a small number of years and we
should be just spending the time that we need to understand
what's true and not just sitting and hoping
for the best. Yeah. I mean, things have been looking very

[01:15]
different in a matter of months. Yes.
Yeah, no, I have to hit my mind. I want to say
in small numbers of years and I have to recalibrate to months.
But yeah,
things are going very fast and I think we need to just be willing to
look at it. At the very least update our
models of the world. Yes. Yep.
Pun not intended. Nicholas, this is amazing.
Thank you so much for— Thank you. It's great to talk to you guys.
Hell yeah. All right, I'm stopping.
