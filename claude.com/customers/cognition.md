<!-- source: https://claude.com/customers/cognition -->

Q&A | Claude Platform

# Building an autonomous AI engineer: A Q&A with Cognition

[Try Claude](https://claude.ai)

![Video thumbnail](https://assets.claude.com/9d1bb7a3e975709514ee3337201df52330edf814.jpg)

Industry:
:   Software

Company size:
:   Startup

Product:
:   Claude Platform

Location:
:   North America

3.5x increase in merged PRs

per week after adopting Claude Sonnet 3.6

![Problem Solvers landing page](https://assets.claude.com/516bf8e49c81e551455b1e24a0fc3678725df957.jpg)

The most driven founders are problem solvers. Watch their unscripted conversations with the Anthropic engineers.

[Read more](https://claude.com/problem-solvers)

![](https://assets.claude.com/79e69363abf8229785d0b20187dfcfece31aead8.png)

"There’s so much more for us to do together than separate, and that’s what we’re excited about." —Scott Wu

[Cognition](https://cognition.ai/) is the company behind Devin, one of the first AI software engineers. Devin launched in early 2024 and has since become an established name in AI engineering and enterprise AI transformation. The early move into the emerging AI software engineering space drove explosive demand; Cognition has deployed its AI engineers across enterprises including Goldman Sachs, Mercedes-Benz, and the US Army.

Scott Wu, CEO, and Walden Yan, co-founder and CPO, sat down with Anthropic to discuss what makes autonomous agents fundamentally different from code-completion tools, how Claude's capabilities have shaped Devin's evolution, and what's ahead for software engineering.

## Anthropic: You've always had a bet on autonomous agents, going back to early 2024 when the technology was much earlier. What's uniquely challenging about powering an agent that works autonomously?

**Scott Wu, Cognition:** The bar for an autonomous agent is fundamentally different from the bar for a code-completion tool. Users systematically under-specify tasks. They have context the agent doesn't. The agent has to clarify, ask the right questions back, and infer intent correctly, because a wrong starting point means the entire trajectory goes off course.

The agent also has to stay focused over long horizons without drifting. A lot of our engineering work goes into trajectory monitoring, which means detecting when an agent is going off track, and steering it back. Before today's frontier models, the primary failure mode was consistency. Some trajectories would work, but the output quality degraded over long contexts, variance was high, and it just wasn't reliable enough to trust autonomously.

Real-world success for us looks like this: a well-scoped ticket comes in, the agent ships it, the PR gets merged. That's the bar our customers hold us to

**Walden Yan, Cognition:** Claude models were very early on, natively agentic. Devin has a lot of particular behaviors that we like to keep around for our users. Having a long set of evals allows us to have the confidence that when we swap a new model in, we don't regress on any important product behaviors, which is really important for us. We want to be able to speak definitively internally about which models we think are best and use those for our capabilities.

## How would you describe what the overall experience of working with Devin is like?

**Scott:** The whole idea is getting you to a point where you as a human can operate in terms of higher level decisions and trade-offs and not have to think about every single little detail in the code. Devin will send you a screen video recording of ‘You told me to fix a bug, I fixed it, here's the PR, but by the way, I actually went through and clicked through myself to make sure it works now.’ And here's like a video of that working.

![](https://assets.claude.com/72ab209a0f97734d7de623d31aaa08aa2636b359.png)

"The far-out vision is Devin not just being an IC engineer, but giving it much higher-level goals." —Walden Yan

## Cognition routes across multiple models. What specifically makes Claude well-suited for the autonomous, long-horizon work you route to it?

**Scott:** One is just the ability to do long-running tasks. With a lot of models, you generally see that after enough time, they get confused or forget what they were doing. Claude models have been ahead of the curve at being able to follow through and consistently work on a longer-running task.

Two is having intelligent usage of the tools available to it. With Devin, we give the model access to all sorts of different things: the PR itself, the commit history, different files of the codebase, the ability to ask a clarifying question. It takes a certain kind of intelligence to know how to use the different tools at your disposal, or when to use a tool at all.

The third is more subjective. You want to be able to give the agent a two-line description of what you *think* needs to happen and have it expand from there and already know what you mean about the other details. It’s a little different from the binary of ‘Did it do the task or not?’ We've often found that Claude models perform particularly well at that.

> "Claude models have been ahead of the curve at being able to follow through and consistently work on a longer-running task."

Scott WuCEO, Cognition

## When you get access to a new model, what does the evaluation process look like?

**Scott:** We have our own set of internal evals that cover all the different parts of software engineering. We have an eval for how good you are mechanically at performing an edit in a file. We have one for how good you are at locating the right files in the codebase that correspond to this issue the user described. And then we have end-to-end evals for what we'd expect a software engineer to do.

When Claude Sonnet 3.6 came out in 2024, that was the biggest leap we'd seen in that benchmark score. We started using it internally, and we 3.5xed merged PRs per week because there were just so many more tasks you could start to work with that model on.

## How quickly does a new Claude model typically make it into Devin's production workflows?

**Walden:** We try to implement it as soon as we have access. If we're confident the model is strictly better than what we have out there, we'll usually straight swap out on day one. The feedback loop goes both ways. Anthropic has sent engineers to work with us to try new capabilities with models. And then the feedback we gave and sent a lot of examples on—that did improve the future models, which was really nice to see.

## You've talked about how much engineering sits in the harness around the models. Can you give a sense of what that infrastructure looks like?

**Scott:** Every time we change which model handles which part of the workflow, the harness has to change with it. Prompts, tool definitions, context management, trajectory monitoring, and guardrails are all tuned to the specific model behind them. Keeping that surface area stable while the underlying model mix evolves is a constant engineering investment. Roughly 50 to 70 engineers work on the model integration surface across the full product.

And there's so much depth in software engineering as a whole. VM sandboxing alone is something we've rebuilt many times. How fast is the VM ready from the moment you kick off the agent? That's a really hard problem, because it's not just the actual spin up. The agent has to be ready to go with the latest code, the latest dependencies, the right repos.

## Enterprise usage of Devin has been accelerating. What's driving that growth?

**Walden:** I think our usage of Devin since late last year is up at least 7x. It's partially new use cases like debugging and security scanning. It's also partially that greater long-horizon consistency means people can let these agents run for longer and trust them.

So much of software engineering is actually maintenance and fixing bugs, not building new software. If you can free up their time by having Devin automatically start responding to bugs, that would be massively helpful. We are seeing the new Claude models getting quite good at using third-party MCPs to look at logs and incidents.

![](https://assets.claude.com/68cf96b0ecc009bcfd6842920b5777fab4a4c3b8.png)

"Claude models have been ahead of the curve at being able to follow through and consistently work on a longer-running task." —Scott Wu

## As coding itself gets easier with AI, how do you think about where Cognition focuses?

**Scott:** One thing that happens now that the part of writing the code gets so much easier is you actually start thinking about all the other parts of the process and how to really optimize this.

I really don't believe that there's just a single product for all of code or all of software engineering. The question for us has always been, what is the thing that we really want to narrow in on and focus on above all else? And how are we going to make that into a true best-in-the-world experience? For us, that is largely the entire flow of how you work with and use a full remote agent.

## Looking ahead, what are you most excited about?

**Scott:** I love typing code, but I don't think it's something that we'll need to do for all that much longer. Right now, our engineers at Cognition don't type code anymore. You can just give instructions and prompts to your agents and have them go work on it. We're pretty quickly getting to a world where you can really just work with the specs and diagrams of what you want your product to be, and English can be the source of truth of how we build software.

That's exciting because it means way more people will get the chance to build software of their own. Walden has this line I've always loved: for so long we've all been living in survival mode of Minecraft, and pretty soon we're going to be in creative mode. It really feels like we’re living in the golden age of software engineering. There’s so much more for us to do together than separate, and that’s what we’re excited about.

**Walden:** The far-out vision is Devin not just being an IC engineer, but giving it much higher-level goals, having it come up with its own tasks, and spin up its own engineering team to go execute on.

Choosing the right Claude model

![Choosing the right Claude model](https://assets.claude.com/7388619b452db0af26c78442a275c86c5ebe3124.jpg)

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

> "The far-out vision is Devin not just being an IC engineer, but giving it much higher-level goals."

Walden YanCo-founder and CPO, Cognition

[![Supermetrics](https://assets.claude.com/3ac4171a81008be0340e5c3d8ccb46571c3edfb3.svg)

### Supermetrics lets marketers manage ad campaigns from a conversation with Claude](https://claude.com/customers/supermetrics)[![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

### How Atlassian builds AI agents teams can trust with Claude and Google Cloud](https://claude.com/customers/atlassian)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### Rocket Money on building agents that fix their own code](https://claude.com/customers/rocket-money-qa)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### How Rocket Money built its personal finance agent with Claude](https://claude.com/customers/rocket-money)
