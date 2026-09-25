<!-- source: https://claude.com/customers/cursor-qa -->

Q&A | Claude Platform

# A conversation with Cursor on building coding agents for professional developers

[Try Claude](https://claude.ai)

![Video thumbnail](https://assets.claude.com/35263bf572b1ea343eafabd13f3535e5c772f6fd.jpg)

Industry:
:   Software

Company size:
:   Large

Product:
:   [Claude Code](https://claude.com/product/claude-code)

Location:
:   North America

60% of the Fortune 500

builds software with Cursor

15 to 700 people

in two years

![Problem Solvers landing page](https://assets.claude.com/516bf8e49c81e551455b1e24a0fc3678725df957.jpg)

The most driven founders are problem solvers. Watch their unscripted conversations with the Anthropic engineers.

[Read more](https://claude.com/problem-solvers)

![](https://assets.claude.com/bcef56f06975ec56f0a57f21859c05c6e681da14.jpg)

"We started working on Cursor at the end of 2022, and the premise was that eventually all of software was going to flow through models." —Michael Truell, Cursor co-founder

[Cursor](https://cursor.com/) is an AI coding platform used by software engineers at more than 60% of the Fortune 500 to build and ship production software, increasingly by directing coding agents rather than writing every line by hand. Co-founder Michael Truell sat down with Anthropic to talk about the role Claude plays in the product, how the work of building software has changed, and where coding is headed next. The following conversation has been edited for length and clarity.

## How do you describe Cursor these days?

**Michael Truell, Cursor:** For the longest time, building software was about writing in a language that only computers could understand. You write very basic statements: if this then that, loop over this many times, take this piece of data and move it over there. The thing that made it hard is that computers couldn't fill in the gaps. You had to spell out everything exactly for them. What's changed over the past few years is that building software is starting to feel like working with a human colleague. With Cursor, it looks like asking a bunch of helpers to go and build parts of your software. People with no engineering background at all can build their own internal tools, purpose-built for their workflow.

## Plenty of people try coding and bounce right off it. What made it stick for you?

**Truell:** I started coding when I was 12 and rapidly became obsessed with it. That came from the feeling of being able to build without barriers, which I think is one of the special things about programming. In so many other domains, you're limited by the people you know, or the resources you can pull together, or even lab space. But with coding, you just need a computer, and you can build things that you dream up in your mind.

## Early on, Cursor ran on other models by default. Sonnet 3.5 was the model that changed that. What did you see in it back then?

**Truell:** We started working on Cursor at the end of 2022, and the premise was that eventually all of software was going to flow through models. We were a very scrappy team back then, and we were using some other models by default. A couple of folks went and really went deep on evaluating the various models in the market, through offline evals, through internal dogfooding, and then also through A/B tests. They came back surprised. Sonnet 3.5 was this big jump, and so we moved quickly on it. That was the start of a multi-year run of improvements with each model since.

> "Over the last 12 months, the models have gotten capable enough to do longer and longer range work, which has been really consequential for us."

Michael Truell Co-founder, Cursor

![](https://assets.claude.com/c59bbbff1fc956b21017d4acac31c27c4a7d24f8.jpg)

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

![AI agents](https://assets.claude.com/bdc16daf5e533d3c67f77bbbed786c7d7e693dce.jpg)

Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

[Read more](https://claude.com/solutions/agents)

> "Two years ago, we were 15 people in a room, and now we're 700 people and serve over 60% of the Fortune 500."

Michael Truell Co-founder, Cursor

![](https://assets.claude.com/e8d8f96ffb4c0f7056b92aa85b8af6d3876817ee.jpg)

"The biggest trend we're excited about is coding agents that can run for hours or days productively and really work with you." —Michael Truell, Cursor co-founder

## Coding has changed faster than almost any other kind of work. Where do you think this goes next?

**Truell**: Coding has been a bellwether for what's going to happen in a lot of other spaces. The move from asking questions to really taking on action is fertile ground for people who want to build companies in other fields. For us, we want to give folks more autonomy and help them be more empowered. The biggest trend we're excited about is coding agents that can run for hours or days productively and really work *with* you. We're also excited about companies starting to have software factories internally that are always improving their software on autopilot.

## You're helping run a 700-person company now. Do you still build things yourself?

**Truell**: I do, regularly, each week. One of the fun things about AI coding getting so good is that people can build their own personal tools. I'm kind of an infovore, so I've built utilities that pull from our wikis and team communication systems and keep me in touch with projects as they move. It's amazing how much you can see into what's going on across the company.

Choosing the right Claude model

![Choosing the right Claude model](https://assets.claude.com/7388619b452db0af26c78442a275c86c5ebe3124.jpg)

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

[![Supermetrics](https://assets.claude.com/3ac4171a81008be0340e5c3d8ccb46571c3edfb3.svg)

### Supermetrics lets marketers manage ad campaigns from a conversation with Claude](https://claude.com/customers/supermetrics)[![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

### How Atlassian builds AI agents teams can trust with Claude and Google Cloud](https://claude.com/customers/atlassian)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### Rocket Money on building agents that fix their own code](https://claude.com/customers/rocket-money-qa)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### How Rocket Money built its personal finance agent with Claude](https://claude.com/customers/rocket-money)
