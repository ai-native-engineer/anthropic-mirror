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
