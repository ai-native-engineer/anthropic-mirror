<!-- source: https://claude.com/customers/spotify-boris-office-hours -->

Q&A | Spotify

# Office Hours: Asynchronous coding and the end of the IDE with Spotify

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Office Hours with Boris Cherny

[Office Hours with Boris Cherny](https://claude.com/office-hours)Office Hours with Boris Cherny

[Play video](#)Play video

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7cbcd161e079777f192c2f_26-115-CustomerConvo-Spotify-THUMBNAIL-04.jpg)

Office Hours with Boris Cherny

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7ceba17e3c474c1e3f0fde_og_office-hours.webp)

The best engineering teams are rethinking how they work with AI. Boris Cherny talks with technical leaders to uncover what's changing for their teams, from how they’re building with Claude Code to organization design, and the shifting workflows that come with it.

Read more

[Read more](https://claude.com/office-hours)Read more

Office Hours with Boris Cherny

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

The best engineering teams are rethinking how they work with AI. Boris Cherny talks with technical leaders to uncover what's changing for their teams, from how they’re building with Claude Code to organization design, and the shifting workflows that come with it.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Office Hours with Boris Cherny

The best engineering teams are rethinking how they work with AI. Boris Cherny talks with technical leaders to uncover what's changing for their teams, from how they’re building with Claude Code to organization design, and the shifting workflows that come with it.

[Prev](#)Prev

[Next](#)Next

At [Spotify](https://www.youtube.com/watch?v=9DHZLw5653E&t=34s), 73% of pull requests are now AI-authored, and anyone with an idea can have a working prototype in an hour or two. Boris Cherny sat down with Chief Architect and VP of Engineering Niklas Gustavsson to talk about life after the IDE, throwing agents at 20 million lines of code, and why the fundamentals still apply.

### Read the full transcript:

**Boris Cherny, Creator of Claude Code, Anthropic:** Niklas, thanks for joining me for this conversation. I wanted to start with: how did you get into coding?

**Niklas Gustavsson, Chief Architect and VP of Engineering, Spotify:** My formal background is actually in biology, so I’m a molecular biologist by training. In that area, when I was doing my PhD studies, we started having what was then considered big data. We had a lot of data from genome sequencing. So I felt that I needed to improve my ability to do programming essentially. So I switched over — what was intended to be a sabbatical year ended up being, I guess, now close to 30 years of being in this industry. That then led into working primarily with backend distributed systems type of engineering for a bunch of companies around where I live, and then joined Spotify in 2011. And yeah, I’ve been there since then.

**Boris:** So fast forward to today, with all the change right now with agents and LLMs, I feel like your personal usage—and Spotify’s usage—is on the frontier of what I see in the industry. What was your first “fueled AGI moment” personally?

**Niklas:** I think I have had a few, depending a little bit on the problem that we were trying to solve. We started pretty early as LLMs came about to try to use them to automate code changes, and that was a real struggle to begin with. But after a while, as we started figuring out how we can use LLMs and judges and whatnot, we started getting some pretty inspiring results from that.

**Boris:** And this was like a few years ago. **Niklas:** It was pre-Claude. It was like early GPT days, something like that. We were struggling. But after a while we started figuring out how to tack pieces together. And yeah, that was super inspiring. And again, the results we got then weren’t like—we can fix all our problems—but it was giving an insight of where this is heading in the future. So that was certainly one. For my own personal coding, the real breakthrough moment was probably Opus 4.5, back in November/December. It went from being this smart autocomplete to something that I could actually throw real problems at. And I didn’t have to do all that much prompt engineering. It was just: tell it roughly what I wanted it to do, and it was able to do a pretty damn good job at it.

**Boris:** It felt like a pretty fast shift.

**Niklas:** Yeah, I actually remember talking to you back in, I think, September last year, and you said something like, “I don’t think at the end of the year anyone is going to be using an IDE.” And I didn’t say this out loud, but in my head I was thinking—that’s crazy. That’s never going to happen. I could imagine that happening on maybe a two year timeframe, something like that. But two months seemed a little bit extreme. And then two months later I found myself not using an IDE anymore. And the way that I was working had completely changed. A change that I had not seen in, again, the 30 years that I’ve been doing this. **Boris:** The biggest thing for me was also just not having to edit code anymore. My workflow up to then was — I have the model write, like, maybe 80% of the code or 70% of the code depending on the model. And then I always had to go into an IDE to do the last mile edits, and I just stopped having to do that. And that was crazy. Yeah. But I think that’s a big part of the reason that it felt like such a— **Niklas:** Yeah, it completely inverted the way I work. It’s been very initially strange. But now it feels very strange to go back.

“I found myself not using an IDE anymore. The way that I was working had completely changed. A change that I had not seen in the 30 years that I've been doing this type of work.”

Niklas Gustavsson

Chief Architect and VP of Engineering, Spotify

**Boris:** I think that’s right. What’s your workflow like today? How do you use Claude Code? How does Spotify use Claude Code? **‍
Niklas:** I use it in a—I’m going to say fairly vanilla way. I run it in a bunch of Max sessions in a terminal, usually have a bunch of agents running in the background whenever I do some work.

**Boris:** How many terminal tabs?

‍**Niklas:** I will have anything between 5 and 10 tabs, and then I use some panes because I like to have a terminal where I can actually get diff and whatnot. So I have this setup with a matrix of Claude sessions and matching terminals in a set of work trees that I work in. The way that we’re set up is that we have a few very large monorepos which we’re gradually moving towards, but we still have thousands of small polyrepos—that remains. So most of my work happens in those monorepos, so I usually have a few Claude sessions and terminals going on there. And then when I need to dip into one of our polyrepos, I will open up a more temporary Claude session.

**Boris:** Do you feel like a monorepo is a better fit for Claude, or—

**Niklas:** I was a bit worried, to be honest, about the monorepo setup and agents originally, because I think with some of the prior tools we’ve been using, we’ve been seeing issues with indexing and things like that, and these are fairly large repositories—our backend is more than 20 million lines of code. But turns out it works amazingly well in those repositories. And I think one of the things we found is how good Claude is at looking at other code in the repository to get, I guess, inspiration for the problem you’re trying to solve. It has required iterating on our CLAUDE.md files and whatnot to get it to understand the tooling we use and whatnot. But generally speaking it works really well.

**Boris:** Yeah. I wanted to ask about some of the infra that you built. Obviously you built Honk. Feel like from the earliest days of experimenting with models, to building Honk, to building background agents on the Claude Agent SDK—you see the future before other people do. What is it about the culture or the people working on it that kind of leads to this? Just tell me that story. How has it been going?

**Niklas:** 5 or 6 years ago now, we identified that our code base was growing much, much faster than the number of engineers we had to support it—like seven times faster. The statement was that over time, we just had more and more code that we needed to maintain. And Spotify, as a company that has an endless source of ideas of things we want to ship to our users—being bogged down by maintenance was not a good place to be.

We started automating, trying to automate as much of that maintenance as possible. A lot of that was pretty dull work, like migrating to the latest Java version or a library update or whatever, and a lot of it was moving from some API to some other API across all our code.

So we built out this infrastructure that we call fleet management, which is all about—instead of imagining before that, when we were doing a migration, we would send out the migration description or tutorial to all our teams and ask them to do that migration manually for all their components—instead of doing that, we imagined: can we find ways where we can do mutations towards our entire code base, living in thousands of repositories?

**Boris:** Because every team was kind of doing the same thing.

**Niklas:** Yeah, yeah—hundreds of teams doing the same operation manually over thousands of components. So each of these migrations took months and months and months to complete. We could maybe do ten of them a year, and we were barely keeping up with being on the supported version of the framework that we’re on. And in our internal surveys, migrations was top of the list of all the things that people were annoyed by.

So again, we started automating this. We built out all of this infrastructure to do this. We’ve merged millions and millions of those types of PRs, but they all relied on these deterministic scripts that you would apply and that would make those code changes or configuration changes. And one of the things we found pretty early was — code has an enormous API surface, so trying to make changes to code gets very complicated very quickly. We pretty quickly ran into a ceiling of how complex the changes we can do were. Even switching out a method in an API becomes pretty complicated when you can call that in five different ways—like if it’s a lambda or a call in different types of ways depending on what the code looks like.

**Boris:** So doing this with just traditional static analysis—like AST transformation.

**Niklas:** Exactly.

**Boris:** Because let’s say there’s an API and you alias it to a variable or something. Now you need variable and state tracking. That’s exactly right. It’s messy.

**Niklas:** So each script that we had to migrate code turned into thousands of lines of taking care of every edge case in that code. So that inspired us—pretty much as soon as the early LLMs came along, of like, hey, can we apply these to this problem? And early on it didn’t work all that well, partly because the models weren’t good enough, partially because we were very naive in how we were trying to do it. We were basically just putting the code in front of the model and trying to get it to one-shot that change.

So that didn’t work. Over time, models improved and our thinking about how to do this improved. We started applying LLMs as judge to make sure that the output was as intended. We started breaking down the problem, decomposing the problem in various ways. So many, many, many iterations of this and many internal hacks to try to take on this problem in different ways. We started consolidating that, and that then became what we now call Honk. And it was a very different beast originally. It was not on top of Claude, it was more a bunch of homegrown things. But it was the first sort of light in the tunnel of like, yeah, this is actually a problem that we can solve.

Then we’ve done many, many iterations on Honk. So today we released what we call V2. But I think in reality it’s V8 or something like that. We just didn’t keep track of the iterations we did on it. And it started out as this ‘automate these code changes, schedule and orchestrate over all our repositories.’ But pretty quickly engineers figured out that, hey, this is useful for other things as well. I want to mention this thing on Slack and have it do a task for me, or all of those types of things. So today, Honk has grown into being a much more ubiquitous tool for us.

**Boris:** Tell me about the architecture of Honk. What are the big pieces? You talked about: there’s the agent that codes, and this is just built on the Claude Agent SDK. And then you also have a verification step, like an agentic verifier. Tell me more about that.

**Niklas:** So we used to have a judge in Honk. But we actually removed that because we found that the agent and models — going back to Claude 3 or 4 — got good enough that we didn’t need the judge anymore. The judge was very important in the first iterations of it. It made us go from, if I remember the numbers correctly, roughly 20–30% success rate on PRs to 80% success rate. So it was a big, big change. But then again, as we talked about, the models caught up and the agent harness caught up. So we have now eliminated that judge from Honk.

Honk architecturally is fairly simple. It’s the Claude Agent SDK running in a Kubernetes pod. It has access to a set of tools. It used to be prior to V2 that those tools were predefined: an allowlisted set of tools that we trusted to give to that agent. Now users can add their own tools, just those tools. So now the agent can use any of our internal tools.

And one of the most important tools that it has access to is that it can run verification—like, run CI builds—and it can run those both on Linux and macOS. macOS is particularly important to us because iOS development, for example, needs macOS builds.
‍ **Boris:** And is this just building, or are you doing a full — like, open up the iOS simulator, have the model start the app — how deep does it go? **Niklas:** It can do those types of tests. We definitely have cases where we integrate the simulator and Claude to automate things like going directly from designs in Figma to UI implementations, and we’ve been using that for porting, for example, our TV apps from our iOS apps. So it’s been a very effective way for us to work. **Boris:** I feel like verification is one of these things that we talk about a lot, but I think when you’re doing this kind of closed-loop development where it’s an agent that’s given a task and then has to maybe fan out and break down the task, and just needs to do a lot of work without a human in the loop—yes, it’s just the single most important thing. And I feel like one of the common mistakes I see is companies under-investing in how well that verification loop works.

**Niklas:** I think that’s very true. And I think it’s true for us as well. One of the major changes that we did in our engineering practices as part of that was to strengthen our test automation, because part of that fleet management was prior to that.

So we have a very strong notion of software ownership within Spotify. We have divided our code base into many thousands of components. Each of those components has well-defined ownership—it’s owned by a particular team, and that team is fully responsible for it. They probably designed it originally, implemented it, and they operate it.

And part of that, prior to the investments we did in fleet management, was around—that team was in the loop for every change that got merged to their code base. And that meant that in some cases, we could be a bit sloppy on test automation, because that team could always check every PR if they needed to. But with starting to automate PRs towards our source code, one of the things was — we needed to change the expectations for teams: you might no longer be in the loop for these changes, we’re going to be auto-merging most of these changes without you ever seeing the PR. So that meant having to build out much better test automation to make sure that all our software could survive those types of automated changes. Now, zooming into where we are today, that’s been very, very helpful for us, because now we can throw agents at that and use the same verification that we had in place before. That being said, we are still improving our test automation because—I agree with you—it’s one of the most important aspects we’ve found to make agents effective, but also for us to feel comfortable throwing agents at our source code.

**Boris:** One of these trade-offs that people talk about all the time in engineering: reliability and quality on one side and speed on the other side. And to me, it feels kind of like a false dichotomy, because if you want to go faster, the thing that you need to do is automate your quality practices so that they’re better encoded. It’s not in someone’s head. It’s actually in a skill, or in a CLAUDE.md, or in some set of instructions. It’s something that Claude can do. And that’s ultimately what lets you go faster. And this is just another example of how in engineering, productivity is always about investing in infrastructure. It’s not about working more hours, it’s about just making the infrastructure better and better. And that sounds like what you were talking about.

**Niklas:** But you need to be very conscious about both the quality aspects while you’re trying to get the speed. And I think there is a real risk of slipping up on the quality if you’re not very actively investing into it. And we’re seeing that we’re keeping our quality metrics neutral while significantly improving our speed. But that does not come for free. We’ve needed to make these investments into test automation that—as we talked about—I think we’re going to have to continue our investments into our reliability practices as well. Some of those are changing as part of this transition.

**Boris:** And I guess as you try to go faster and faster and faster, you have to invest even more in reliability just in case.

**Niklas:** That’s exactly right. We make something like 4,500 production deployments every day. So there’s a lot of opportunities for things to go wrong. We need to have good practices around making sure that everything that ships into production has the quality that we want.

**Boris:** What’s the story with doing this many deployments? Is it kind of—in the past it was just continuous deployment and now maybe it’s faster signal for the agent? Or how are you thinking about it?

**Niklas:** This is something we’ve always been optimizing for, for as long as Spotify existed. I think we want to be able to have a developer take an idea and ship it into production as quickly as possible. That used to be weeks or months back, a few years ago. And we’ve continued to try to optimize that. And now it’s an hour or something like that. As I mentioned before, we have lots of ideas. We want to validate and explore those ideas. And the faster we can get feedback on that — in some cases that might be feedback from our internal users, in some cases it might be feedback from our external users. But in both of those cases, the faster we can iterate, we’ve found that we both build better products and we’re able to ship them faster to our users. Not every idea ships in an hour. Many ideas take lots of exploration before we’re able to ship them. But the notion of being able to get that quick validation is super important. And yeah, agents are certainly part of that loop as well. **Boris:** So for Spotify, the engineering org is very big, it’s like thousands of engineers, right?

**Niklas:** Yeah, it’s 2,900 engineers.

**Boris:** 2,900 engineers. How do you think about ROI and measurements, just making sure you’re moving in the right direction?

**Niklas:** So in terms of measuring ROI, it’s been relatively easy and we’ve seen very clear signals in that space. We’re seeing a 75% plus improvement in PR frequency, for example, that we can directly attribute to AI tooling. And I think by now 73% of PRs are directly attributed to being AI-authored. So those types of metrics we’re doing pretty well on. But then of course, we want to connect that to user value and revenue.

**Boris:** And how do you measure something like that? Is it an A/B test or some kind of holdout, like case studies? How are you thinking?

**Niklas:** Yeah. So we want to basically be able to connect the deliverables that engineers do—PRs, deployments—into what we call a work item. Basically the planned work that we have. And then that connects to A/B tests and rollouts. And then we’re able to, from that, attribute back and say this PR contributed to this DOD that we have, and that contributed to this user value. That’s the idea, and we’re trying to build those connections right now.

**Boris:** Yeah. I feel like back in the day. like we’ve worked in developer productivity for a while, when you have a big team, you want to make them more productive. And back in the day, a big win was like a few percentage points. Exactly, exactly. If you were lucky enough to be able to measure that. And with improvements nowadays, it’s just so obvious to everyone. Yeah. As engineers, we still want to measure it.

**Niklas:** Yeah. The discussion initially was fairly easy because we could see such large improvements. But as the maturity is getting there and the costs have been improving, I think the precision around those ROI estimates—the expectations on the precision—is going up as well. So that’s why we’re trying to improve how we can do that type of measurement.

**Boris:** Part of it is about the improvement in productivity. And then part of it is how much does it cost to get that improvement. And now people are seeing these like many dozens or hundreds of percentage points of improvement. And now you really want to attribute it — figure out how many tokens did it take, how many hours did it take? What was the productive output?

How Anthropic teams use Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6905133b69fcac6a5cbadb2f_og_how-anthropic-teams-use-claude-code.jpg)

From debugging production issues to navigating unfamiliar codebases to building custom automation—here's how teams across Anthropic use Claude Code.

Read more

[Read more](https://claude.com/blog/how-anthropic-teams-use-claude-code)Read more

How Anthropic teams use Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

From debugging production issues to navigating unfamiliar codebases to building custom automation—here's how teams across Anthropic use Claude Code.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

How Anthropic teams use Claude Code

From debugging production issues to navigating unfamiliar codebases to building custom automation—here's how teams across Anthropic use Claude Code.

"You need to have the same engineering practices that we had before. There’s a new actor in your code base, but the fundamentals seem to apply equally well."

Niklas Gustavsson

Chief Architect and VP of Engineering, Spotify

**Boris:** I want to end on maybe one question. What advice would you give your peers? What advice would you give to other CTOs and engineering leaders, like VPs of engineering at other companies?

**Niklas:** What we found is that these investments in foundational capabilities—we talked about test automation and verification—I’m going to say the same is true for another aspect that we’ve seen, which is standardization. So we’ve been driving more consistent code bases, more alignment on the tools that we use, the frameworks that we use. And we’ve seen, this was originally an investment we did to simplify things for humans and make humans more productive. But we’ve seen the same thing transition really well to agents as well. So as I mentioned before about Claude being able to find inspiration from other pieces of code in our repos, if they look ten different ways, Claude is going to be more confused. So we’ve been seeing the more consistency we have, the better our agents work. So I think if there’s one piece of advice I would give, it would be to not ignore those types of investments. You need to have the same engineering practices that we had before. They still apply in this new world, they might look different. There’s a new actor in your code base, but the fundamentals seem to apply equally well. At least that’s been the case in our environment.

**Boris:** What’s your advice for engineers that maybe have been doing engineering work for a while? I know Spotify has talked about engineers shipping on the subway, which is really cool. Obviously engineering is changing. What’s your advice to everyone that’s in the middle of it and trying to figure it out?

**Niklas:** Yeah. Let me talk about this from a more personal angle. I’m someone who’s always truly enjoyed the problem-solving part of coding. This is going to sound as nerdy as it is, but in my spare time I will do competitive programming at times because it’s just a fun mental exercise. In the back of my head, I was always a bit worried, like we were talking about before. about how this was completely changing the way we were working. And I was pretty worried about that from just my personal point of view. Like, am I not going to get that part of the hard mental challenge of solving problems?

Now I find myself having five agents working in the background, and my way of interacting with them is very different from the way that I was working a year or two ago. And for me, it’s turned out that I was wrong. The thing that I like to do is solving problems. And the way that I solve those problems turns out to not be the most critical piece for me. This is always going to be personal—different people are going to have to make that transition in different ways. But I think: focus on the types of problems that you’re able to solve. I find myself both more productive in that I can bring more value from the work that I do, and I can also solve problems that I really couldn’t solve before. I can jump into code bases that would have taken me days or weeks to get into before and be contributing things that I just could not do before. So for me, that’s been amazing. And again, it’s going to look different for different people. But I think give it a shot and find a way that you can use those tools in the way that you like.

**Boris:** I feel like for me, I’ve seen this big shift from implementation time—because now Claude Code does it in the background while I do other stuff. And instead, what’s filled up that time for me is thinking about what’s next, talking to customers, and also actually much more prototyping than I expected. Some of it is for external products, some of it is for internal automations. How has that change worked for you?

**Niklas:** I think it’s been similar for me. And we didn’t talk about this, but one thing that we’re making a big investment in is prototyping in particular. And this is targeted both towards engineers but also the non-engineering cohort.

One of the things that Claude and similar tools have unlocked is to allow anyone to take their idea, whatever that idea is, express that in natural language and have Claude go implement that. So as folks started figuring this out, including non-engineers, they started trying to do this in our real apps. And they’re pretty complex beasts of code. But they were starting to see signs that they could do it. So we started, a few months ago, basically building out the infrastructure to make that simple. So today we have a very simple way to get going and build an end-to-end prototype in our mobile apps and our backend. We have an internal app store for those prototypes where you can share them and take a look at someone else’s prototype or try your app.

And that’s been a real unlock for folks that—maybe before, including engineers that maybe weren’t super familiar with how to build something in our mobile apps—to be able to express ideas that used to take motivating a bunch of engineers to try to build that for you. And now you can go in and within an hour or two, you have a working prototype that you can start sharing with people to show what that actual idea looks like in real life, with real users, real data, and so on. So yeah, those types of things were unimaginable a year ago, and now we’re doing them every day. **Boris:** Yeah, I love that. Have you seen a shift in who’s producing this? Is it like engineers doing it, or is it mostly coming from designers and product managers? How has that changed? **Niklas:** It’s everyone, up to our co-CEOs, who have prototypes in that app store at the moment. So it’s actually been a bunch of our senior execs have built prototypes that are good. An idea that they always had in the back of their head. They have an entire engineering team that could build that out, but that team is focused on other things. So for them to then be able to try something out more quickly than they could before and get a touch and feel for what this thing is going to look like. It allows you to test out an idea in a day instead of weeks or months.

**Boris:** Niklas, thank you so much.

‍

Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525504b02eec936ac51b_68c469d41149ace562bfd24d_og-claude-product-claude-code.jpeg)

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Prev](#)Prev

[Next](#)Next

## Related stories

[How Atlassian builds AI agents teams can trust with Claude and Google Cloud](https://claude.com/customers/atlassian)How Atlassian builds AI agents teams can trust with Claude and Google Cloud

How Atlassian builds AI agents teams can trust with Claude and Google Cloud

Customer story

[Customer story](https://claude.com/customers/atlassian)Customer story

[Rocket Money on building agents that fix their own code](https://claude.com/customers/rocket-money-qa)Rocket Money on building agents that fix their own code

Rocket Money on building agents that fix their own code

Customer story

[Customer story](https://claude.com/customers/rocket-money-qa)Customer story

[How Rocket Money built its personal finance agent with Claude](https://claude.com/customers/rocket-money)How Rocket Money built its personal finance agent with Claude

How Rocket Money built its personal finance agent with Claude

Customer story

[Customer story](https://claude.com/customers/rocket-money)Customer story

[How Notion ships and scales agents with Claude Managed Agents](https://claude.com/customers/notion-qa)How Notion ships and scales agents with Claude Managed Agents

How Notion ships and scales agents with Claude Managed Agents

Customer story

[Customer story](https://claude.com/customers/notion-qa)Customer story
