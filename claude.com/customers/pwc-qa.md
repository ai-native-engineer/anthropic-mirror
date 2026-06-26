<!-- source: https://claude.com/customers/pwc-qa -->

Q&A | Claude Code

# How PwC trained 400 consultants on Claude Code in a single session

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ef83dcf20ef28c1bc4b322_pwc_light.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ef83d6220d873723cb7718_pwc_dark.svg)

Industry:

Professional services

Company size:

Large

Product:

Claude Code

Claude Enterprise

Location:

North America

6 weeks → 2.5 days

Legacy code analysis compressed

30,000-person training rollout

underway across PwC

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Legacy code analysis compressed

Read more

[Read more](#)Read more

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Legacy code analysis compressed

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

6 weeks → 2.5 days

Legacy code analysis compressed

[Prev](#)Prev

[Next](#)Next

[Pricewaterhouse Coopers](https://www.pwc.com/us/en.html), or PwC, is a global professional services firm offering audit, tax, and consulting services to businesses and organizations worldwide. PwC and Anthropic [recently announced an expanded alliance](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html), driving impact across client work and the firm. Partner Ussama Baggili leads legacy and mainframe modernization at PwC, where he built systemized Claude Code workflows that have spread to a firm-wide training initiative. We spoke with Baggili about why PwC puts business users on Claude Code from day one and how a single training session got 400 leaders and consultants building apps in under an hour, and what that means for the firm.

## Anthropic: You've been one of the more active Claude Code users inside PwC. What were you trying to solve when you started?

**Ussama Baggili, PwC:** Everybody's trying to figure out how to get ahead with AI, but not everybody is able to use AI effectively. Claude is giving us the ability to re-energize the AI mindset in our people. It's a lot more relatable. People feel that they're getting to results faster that are both higher fidelity and also more in tune with where they're going.

We have these blind spots in our organization that we weren't able to connect. Claude Code is how we started connecting those.

What we're trying to do is get people thinking differently by treating Claude as a capable colleague. We started with coding, which is the obvious entry point. But I discovered that a lot of what Claude Code is really good at is analysis: working through the problem before you even get to the coding part. The early realization was that the analysis itself was the deliverable. You could take it and then make it polished. And once I saw that, it changed how I thought about who should be using it.

## What do you mean by that? There's a common assumption that Claude Code is for developers and that non-technical users should start somewhere simpler.

**Baggili:** People say, "Maybe we’ll start with chat and then graduate to Claude Code. It’s too complicated for people to want to use it right away" But I think that's very limited. I think starting with Claude Code at the beginning is actually a more optimal and natural segway for continued progress into more technical realms. When we were first planning our internal training, the thought was that it’s best to use the Claude  chat version. However, believing in choice and not assuming we know best how the Claude products set will be used, we decided to run the training in Claude Code CLI within VS Code to start building muscle memory on more technical usage from which point the trainees can decide which one they preferred for their regular usage.

## That's a bold bet with a non-technical audience. How did you set that up to succeed?

**Baggili:** Installing Claude Code can be complex if there are restrictions on package installations. We managed to get it down to a single-line script that people could run to get everything installed.

Then the question become, how do we get 400 people to pace through a real training in about an hour and walk out energized? If things go wrong on the install, if they stumble on their prompting, they may not feel the benefit of using Claude Code.

So I thought, couldn't we build a skill or plugin within the training itself that helps people pace forward as they type their prompts? Think of it as a coach plugin within Claude Code. It tells people: great, here's what we're going to take you through in this training and helps set the training structure.

Then, the second most notable thing is to coach on how to work with Claude with the outcome in mind first, and then working backwards from there. The Claude Code coach plugin is wired into a project distribution that has a [CLAUDE.md](http://claude.md) that points to a coaching workflow for Claude. It is triggered upon session start and is visible to the user upon first interaction. It walks them through the steps to ‘here's your first prompt.’

## What did the training actually walk people through?

**Baggili:** It simulates a day in the life of three key tasks we do often. One, we respond to proposals. Two, we produce functional and technical specs for the things we're going to build. And three, we build applications or mobile applications.

The coach plugin walks them through their first prompt. And within 15 to 20 minutes, people had their initial draft RFP responses ready for their review. Within another 15 to 20 minutes, they had their functional and technical draft specs. By the time we finished the hour, people were posting screenshots of the mobile apps they had built with Claude Code in the team chat.

Regardless of whether it was perfect, people walked out positive and optimistic about Claude Code and why they needed it.

"Claude is giving us the ability to re-energize the AI mindset in our people."

Ussama Baggili

Partner, PwC

## What was the reaction after the session?

**Baggili:** People were already planning what to do next. We did a round of Q&A at the end, and people said things like: ‘Monday, this is what we're doing.’ Or, ‘Tonight I'm going to talk to my teams. I need everybody on this.’

My thinking was: how do I get this to be enticing enough for people to be yearning for it, so that they could do more with it *immediately*? Not tomorrow, not next week. We had already taken down the barriers to installation, dealt with the security hurdles, and made it as frictionless as possible.

## You mentioned that the shift from coding to analysis was a turning point for you. What does that look like in your day-to-day practice?

**Baggili:** Once I started producing decks and HTML deliverables with Claude Code, clients gravitated toward them. They were no longer shelfware. Clients could click through them quickly. So what started as 100% coding work shifted toward a non-coding output that was actually more valuable for our clients.

## Can you walk through a specific example?

**Baggili:** I lead our legacy and mainframe modernization practice. We often get these projects last minute where a client says, "We run AS400," or they have an ERP system for supply chain, or a healthcare TPA system. Systems that don’t have documentation or code that nobody can read anymore because the people who wrote it are retired.

With Claude Code, if they give us access to their code, we know how to run the analysis and give you a point of view very quickly in a package that's deliverable-worthy. We can show them previous examples and say, "Don't worry, you don't have to spend a fortune to get there. We'll help you see what you need to know." You're going to have documentation now.

The crazy part is what used to be six weeks' worth of engagements is now about two and a half days of doing that. The typical discovery process required significant effort towards collecting, manually reviewing documentation, interviewing stakeholders, reviewing findings, iterating over interim-deliverables and shaping the recommendation.  With Claude Claude, the majority of these activities can be performed by the agent. That’s made us very credible with clients.

## Anthropic: Where did you take it from there?

**Baggili:** That’s when I started to see other use cases. If it can do this, can it also produce all this daunting work that we don't care to do? We started systemizing our proposals and offerings with Claude skills and Claude plugins. By packaging them into a systemized way of working, we built what's essentially an executive assistant in Claude Code. If you give me any question, I give it to my executive assistant and it spits out a deck with our branding, diagrams, workflows, and content—in minutes. We also started providing it to our leaders so they could use it across the organization.

## Anthropic: What's next?

**Baggili:** Now the idea is becoming global and the question is: how do we keep this going? How do we take this across all of our offerings for our 400,000 people and repeat the success we are witnessing in the US?

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

training rollout underway across PwC

Read more

[Read more](#)Read more

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

training rollout underway across PwC

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

30,000-person

training rollout underway across PwC

"What used to be six weeks' worth of analysis is now about two and a half days."

Ussama Baggili

Partner, PwC

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

## Related stories

[Quantium scales Claude across Australia's largest enterprises](/customers/quantium-qa)Quantium scales Claude across Australia's largest enterprises

Quantium scales Claude across Australia's largest enterprises

Customer story

[Customer story](/customers/quantium-qa)Customer story

[JAKALA brings production AI agents to enterprise clients across Europe with Claude](/customers/jakala)JAKALA brings production AI agents to enterprise clients across Europe with Claude

JAKALA brings production AI agents to enterprise clients across Europe with Claude

Customer story

[Customer story](/customers/jakala)Customer story

[How Brainlabs gave 1k+ marketers at its media agency an AI coworker with Claude Cowork and skills](/customers/brainlabs)How Brainlabs gave 1k+ marketers at its media agency an AI coworker with Claude Cowork and skills

How Brainlabs gave 1k+ marketers at its media agency an AI coworker with Claude Cowork and skills

Customer story

[Customer story](/customers/brainlabs)Customer story

[TRY accelerates creative excellence with Claude](/customers/try)TRY accelerates creative excellence with Claude

TRY accelerates creative excellence with Claude

Customer story

[Customer story](/customers/try)Customer story
