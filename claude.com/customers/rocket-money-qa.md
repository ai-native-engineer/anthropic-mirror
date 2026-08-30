<!-- source: https://claude.com/customers/rocket-money-qa -->

Q&A | Claude

# Rocket Money on building agents that fix their own code

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a8e170db69adaa238d89c2d_logo_rocketmoney-light-mode.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a8e17136685ddacc4602392_logo_customer-dark-mode.svg)

Case Study: Rocket Money

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a8e47e6e408ec5b4d828e55_og_case-study-ROCKET.jpg)

Read how Rocket Money built its personal finance agent with Claude.

Read more

[Read more](https://claude.com/customers/rocket-money)Read more

Case Study: Rocket Money

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Read how Rocket Money built its personal finance agent with Claude.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Case Study: Rocket Money

Read how Rocket Money built its personal finance agent with Claude.

[Prev](#)Prev

[Next](#)Next

[Rocket Money](https://www.rocketmoney.com/) is a personal finance app that tracks spending, cancels subscriptions, negotiates bills, and automates savings. Its newest product, Rowan, is a financial assistant built on Claude that users reach by text message. Anthropic spoke with Aaron Dignan, VP of Product & AI, and Chase Adams, VP of AI Engineering, about the architecture behind Rowan and their approach to building agents in consumer AI.

## Anthropic: What’s the bet behind Rowan, and how is it different from what already exists in the personal finance space?

**Aaron Dignan, Rocket Money:** The way I think about it, over time, technology brings to everyone what used to be exclusive to the 1%. Take an Uber or a Waymo, and you're doing what was reserved for a celebrity 20 years ago. Money works the same way. The most successful people have a finance expert looking after things and advising them. What would it mean to put that in everyone's pocket? Because of AI, you don't need to be a celebrity to access that anymore. You just text: ‘How much did I spend on clothes last month, and was that a good idea?’ A much larger number of people want to manage their money well but don't have the time, aptitude, or interest to sit in an app. Rowan can take that on for them.

## What does Rowan actually do?

**Dignan:** Rowan is an assistant running on Claude models that sits on top of the Rocket Money app which already tracks spending, cancels subscriptions, negotiates bills, and automates savings. Users reach Rowan by text message, and an in-app version is coming soon. You ask Rowan questions in plain language, like: How much did I spend on this? Can you negotiate this bill? Can you cancel this subscription? Then Rowan goes and does the work. We're about to roll out free-trial tracking, where Rowan reads your Gmail, notices you started a trial, and texts you the day before it renews so you can decide whether to keep it.

**Chase Adams, Rocket Money:** I don't want to make anyone open a dashboard or read a graph. Rowan should be the thing that notices a subscription you forgot about, or flags a charge that looks off, and just tells you. The experience we're going for is that you get the value without having to think about it.

"With the least amount of context, Claude tends to get the most things right."

Chase Adams,

VP of AI Engineering, Rocket Money

## You tested every major model at your last company. Why go all in on Claude?

**Dignan:** Being co-founders of an AI automation platform meant we had to build integrations for every company’s models, so our hands were in the “dirt” constantly. When you work with every provider in that way, you develop an intuitive sense of how each one behaves. Claude's approach to agentic engineering kept producing higher quality and higher reliability, and it was the most natural to build on. Pair that with the rate of development, the consistency, and a philosophical position that aligned with ours, and it was an easy call. There are plenty of decent models out there, but who can we count on to reliably keep delivering progress?

## How do you make product bets in an environment where models are constantly improving?

**Dignan:** When we plan, we don't design only for today's models. We assume that even without AGI or ASI (artificial superintelligence), the models get 10-20% better over the next couple of years. Then we ask what it looks like to manage money in that world. In two or three years, the idea that people will still pick up their phone and wonder what's happening with their money seems unrealistic.

## Most teams build one big agent with a lot of tools. How is Rowan put together differently?

**Adams:** Rather than a monolithic agent that you throw all the tools at and hope it figures things out, we built an agent-workflow hybrid. A classifier running on Haiku 4.5 reads each request and decides which subagent should handle it. We use Sonnet 5 for most subagents, and for a financial task that needs real reasoning we reach for Opus. On the way out, a single subagent acts as a response formatter so the voice and tone stay tight. Everything is single-responsibility. I would rather have five back-to-back calls with small context than one call with a huge context, because of recency and primacy effects. With the least context, Claude tends to get the most things right.

**Dignan:** It is much more common right now to use a simple harness, give the orchestrator a bunch of tools, and cross your fingers. But we're in finance. Our accuracy needs to be 100%. We built a blueprint and a harness that is a little unusual to pull that off. When we don't get what we want, we can trace the thread of exactly where it went wrong to a specific classifier or a specific call, and fix it for everyone.

## You call your philosophy "third way engineering." What does that mean?

**Dignan:** Most people are either agent-pilled or programmatically stuck in the past, and neither is right. Picture ASI showing up tomorrow. The world's most incredible intelligence would not cancel a streaming subscription by hand in the browser, then do it again by hand the next time, and again. It would notice the pattern and write code to automate it. So let's behave as if that intelligence is already here, and let the agent do only the job it needs to do—which is fixing the programmatic part when it breaks.

**Adams:** A cancellation should be codified into a procedure a computer runs over and over until it breaks. Usually it’s because a website changed. At that point an agent steps in, figures out where it broke, self-heals the process, and turns it back into code so it can run on autopilot again. Agent Skills was where this clicked for us. With Skills, it isn't just markdown files anymore, you can put scripts in it. We looked at that and realized we were already doing this, so we turned the idea into a document the whole team follows.

## Personal finance is a high-trust domain. How do you keep accuracy high and decide what to automate?

**Adams:** We rely a lot on structured output, which lets us run evals against deterministic results instead of asking a model to judge itself. We also built distinct classifier fall-throughs that catch off-topic requests early, so a conversation never drifts away from money. We haven't had any meaningful hallucination patterns with our beta users so far. And when someone thinks they've found one, it turns out to be a data problem under the hood, not the model making something up. For the agentic actions, we use Claude to classify whether an agent actually completed the work, like whether a cancellation succeeded. If it didn't, the agent classifies why not. Then it hands off to a human in the loop to decide what happens next.

## Why do you part ways with the industry on how to build agents?

‍**Adams:** I have a counterintuitive belief, which is that by the time agents are good enough to be good enough, they won't need most of what we are doing now. What I see across the industry is that if you can get an agent 70% of the way there, people say, that's great. But if you are building something focused, where people genuinely care about it being right, there is a lot more complexity in keeping it from going off the rails. A generic harness hides that complexity. That is why we built the system the way we did.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Read more

[Read more](#)Read more

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

"There are plenty of decent models out there, but who can we count on to reliably keep delivering progress?"

Aaron Dignan,

VP of Product & AI, Rocket Money

## As Rowan starts taking actions out in the world, it will run into other companies' agents. How does that change things?

**Dignan:** These spaces are very tractable. Once Rowan starts taking action at scale, it opens up different possibilities. If our agent is going to call some company's line 30,000 times a day, at some point, the best move is to agree to handle it at the API layer and do it programmatically on behalf of users. There is a genuinely interesting game theory coming: when the insurance company's bot is answering the phone, and that's an agent, and our agent is the one calling, what is the most elegant way to solve that? I look forward to seeing how we apply pressure to the system and how the system reacts for the benefit of consumers.

## Where do you want to take Rowan?

‍**Adams:** The best use of AI is carving out the small things you carry in your head and shouldn't have to. I don't want to remember that three birthdays land in one month and that my budget should flex for it. We do those things in our heads, we do them badly, and they stress us out. Rowan can take them off your plate.

**Dignan:** The scope within money alone is almost endless, so the discipline is staying focused rather than saying yes to everything. Our hypothesis is that people will eventually hire a handful of specialized agents for the major roles in their life, not have one agent for everything. Even a billionaire wouldn't hire one person to handle their food, their health, their money, and their business. Specialization is what keeps each one focused and high quality, so we will put real walls around what Rowan is and stay focused.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

## Related stories

[How Atlassian builds AI agents teams can trust with Claude and Google Cloud](https://claude.com/customers/atlassian)How Atlassian builds AI agents teams can trust with Claude and Google Cloud

How Atlassian builds AI agents teams can trust with Claude and Google Cloud

Customer story

[Customer story](https://claude.com/customers/atlassian)Customer story

[How Rocket Money built its personal finance agent with Claude](https://claude.com/customers/rocket-money)How Rocket Money built its personal finance agent with Claude

How Rocket Money built its personal finance agent with Claude

Customer story

[Customer story](https://claude.com/customers/rocket-money)Customer story

[How Notion ships and scales agents with Claude Managed Agents](https://claude.com/customers/notion-qa)How Notion ships and scales agents with Claude Managed Agents

How Notion ships and scales agents with Claude Managed Agents

Customer story

[Customer story](https://claude.com/customers/notion-qa)Customer story

[Deepgram ships 4–10x more durable code with Claude](https://claude.com/customers/deepgram) Deepgram ships 4–10x more durable code with Claude

Deepgram ships 4–10x more durable code with Claude

Customer story

[Customer story](https://claude.com/customers/deepgram)Customer story
