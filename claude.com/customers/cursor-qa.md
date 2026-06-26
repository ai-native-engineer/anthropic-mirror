<!-- source: https://claude.com/customers/cursor-qa -->

Q&A | Claude Platform

# A conversation with Cursor on building coding agents for professional developers

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a28accb336596a020952082_YouTube%20Thumbnail_Cursor_200kb.jpg)

Industry:

Software

Company size:

Large

Product:

Claude Code

Location:

North America

60% of the Fortune 500

builds software with Cursor

15 to 700 people

in two years

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0cb8c1f8c5c525e8c554b3_problem-solvers-padded-200kb.jpg)

The most driven founders are problem solvers. Watch their unscripted conversations with the Anthropic engineers.

Read more

[Read more](https://claude.com/problem-solvers)Read more

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

The most driven founders are problem solvers. Watch their unscripted conversations with the Anthropic engineers.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

The most driven founders are problem solvers. Watch their unscripted conversations with the Anthropic engineers.

[Prev](#)Prev

[Next](#)Next

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a28ae750a5981a9f2a00cc5_Screenshot%202026-06-09%20at%204.39.21%E2%80%AFPM_4mb.jpg)

"We started working on Cursor at the end of 2022, and the premise was that eventually all of software was going to flow through models." —Michael Truell, Cursor co-founder

[Cursor](https://cursor.com/) is an AI coding platform used by software engineers at more than 60% of the Fortune 500 to build and ship production software, increasingly by directing coding agents rather than writing every line by hand. Co-founder Michael Truell sat down with Anthropic to talk about the role Claude plays in the product, how the work of building software has changed, and where coding is headed next. The following conversation has been edited for length and clarity.

## How do you describe Cursor these days?

**Michael Truell, Cursor:** For the longest time, building software was about writing in a language that only computers could understand. You write very basic statements: if this then that, loop over this many times, take this piece of data and move it over there. The thing that made it hard is that computers couldn't fill in the gaps. You had to spell out everything exactly for them. What's changed over the past few years is that building software is starting to feel like working with a human colleague. With Cursor, it looks like asking a bunch of helpers to go and build parts of your software. People with no engineering background at all can build their own internal tools, purpose-built for their workflow.

## Plenty of people try coding and bounce right off it. What made it stick for you?

**Truell:** I started coding when I was 12 and rapidly became obsessed with it. That came from the feeling of being able to build without barriers, which I think is one of the special things about programming. In so many other domains, you're limited by the people you know, or the resources you can pull together, or even lab space. But with coding, you just need a computer, and you can build things that you dream up in your mind.

## Early on, Cursor ran on other models by default. Sonnet 3.5 was the model that changed that. What did you see in it back then?

**Truell:** We started working on Cursor at the end of 2022, and the premise was that eventually all of software was going to flow through models. We were a very scrappy team back then, and we were using some other models by default. A couple of folks went and really went deep on evaluating the various models in the market, through offline evals, through internal dogfooding, and then also through A/B tests. They came back surprised. Sonnet 3.5 was this big jump, and so we moved quickly on it. That was the start of a multi-year run of improvements with each model since.

"Over the last 12 months, the models have gotten capable enough to do longer and longer range work, which has been really consequential for us."

Michael Truell

Co-founder, Cursor

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a28af6112c7ce11a06c31de_Screenshot%202026-06-09%20at%204.41.12%E2%80%AFPM_4mb.jpg)

"Each model release is a moment where new things become possible in the product." —Michael Truell, Cursor co-founder

## What is it about the models, specifically, that's mattered most for what Cursor can build?

**Truell**: Sonnet 3.5, then 3.7, then Sonnet 4 were big step-ups. They improved in intelligence, but also in things like the UX of the model, its personality, and its ability to write clean code. The most important one was the ability to take action and take on whole tasks instead of just answering queries. A lot of that capability now arrives inside the models themselves, so each release is a moment where new things become possible in the product.

Over the last 12 months, the models have gotten capable enough to do longer and longer range work, which has been really consequential for us. Beyond the models themselves, a few of Anthropic's API features have mattered for agentic coding. Prompt caching is incredibly important for models doing longer and longer range work. And having access to fast versions of Anthropic models has been big for making coding agents useful, including one of our earliest features, called Tab, which predicts the next set of things a programmer is going to do across a codebase.

## Models aside, what made you decide to build on Anthropic?

**Truell**: Anthropic’s commitment to principles is well known when it comes to the safety side of things. But it also extends to how you serve customers. From the start, there's been a commitment to really being a platform that folks can build lasting businesses on top of, and that comes from being principled.

## What does the newest generation of coding agents look like?

**Truell**: AI coding has moved through a few eras: the tab era, the assistive editor era, the coding agents era, and now remote agents. One of the important blockers to tackle is giving coding agents their own computer. We've been doing a bunch of recent product work on remote coding agents that can run for long periods of time. The agents can come back to you and show their work with a video of what they've run and tested. That work is enabled by the computer use capabilities coming out of new Claude model releases. We're also seeing folks use coding agents programmatically, not just interactively. They fix issues in an issue tracker automatically, address customer bugs as they come in, upgrade dependencies as they need to be upgraded, and patch security issues as they're found.

## Cursor has grown incredibly fast. What does this moment feel like from the inside?

**Truell**: This is a great time to be working on a company, because a whole new set of companies have been made possible that have different business physics. Two years ago, we were 15 people in a room, and now we're 700 people and serve over 60% of the Fortune 500. It’s not lost on us just how special and unprecedented it is historically.

AI agents

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f5244ff22e3ab8e64404d_68c469d3872afd7941c5e6f2_og-claude-agents.jpeg)

Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

Read more

[Read more](/solutions/agents)Read more

AI agents

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

AI agents

Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

"Two years ago, we were 15 people in a room, and now we're 700 people and serve over 60% of the Fortune 500."

Michael Truell

Co-founder, Cursor

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a28afa7b02b7048588749d0_Screenshot%202026-06-09%20at%204.40.15%E2%80%AFPM_4mb.jpg)

"The biggest trend we're excited about is coding agents that can run for hours or days productively and really work *with* you." —Michael Truell, Cursor co-founder

## Coding has changed faster than almost any other kind of work. Where do you think this goes next?

**Truell**: Coding has been a bellwether for what's going to happen in a lot of other spaces. The move from asking questions to really taking on action is fertile ground for people who want to build companies in other fields. For us, we want to give folks more autonomy and help them be more empowered. The biggest trend we're excited about is coding agents that can run for hours or days productively and really work *with* you. We're also excited about companies starting to have software factories internally that are always improving their software on autopilot.

## You're helping run a 700-person company now. Do you still build things yourself?

**Truell**: I do, regularly, each week. One of the fun things about AI coding getting so good is that people can build their own personal tools. I'm kind of an infovore, so I've built utilities that pull from our wikis and team communication systems and keep me in touch with projects as they move. It's amazing how much you can see into what's going on across the company.

Choosing the right Claude model

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c2dd485d80024bc14f48c6_choosing%20model.jpeg)

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Choosing the right Claude model

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

[Prev](#)Prev

[Next](#)Next

## Related stories

[How Vercel built an ecosystem on the open skills standard](/customers/vercel-qa)How Vercel built an ecosystem on the open skills standard

How Vercel built an ecosystem on the open skills standard

Customer story

[Customer story](/customers/vercel-qa)Customer story

[Box builds document creation into its AI agent with Claude](/customers/box)Box builds document creation into its AI agent with Claude

Box builds document creation into its AI agent with Claude

Customer story

[Customer story](/customers/box)Customer story

[Juno helps people with chronic illness find patterns in their symptoms with Claude](/customers/juno)Juno helps people with chronic illness find patterns in their symptoms with Claude

Juno helps people with chronic illness find patterns in their symptoms with Claude

Customer story

[Customer story](/customers/juno)Customer story

[Inside Delight.ai’s AI/ML team: Building internal tools with Claude Code](/customers/delightai-qa)Inside Delight.ai’s AI/ML team: Building internal tools with Claude Code

Inside Delight.ai’s AI/ML team: Building internal tools with Claude Code

Customer story

[Customer story](/customers/delightai-qa)Customer story
