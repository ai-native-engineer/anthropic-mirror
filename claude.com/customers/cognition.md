<!-- source: https://claude.com/customers/cognition -->

Q&A | Claude Platform

# Building an autonomous AI engineer: A Q&A with Cognition

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0ca101c2f6cd237e4dba12_problem-solvers-800kb.jpg)

Industry:

Software

Company size:

Startup

Product:

Location:

North America

3.5x increase in merged PRs

per week after adopting Claude Sonnet 3.6

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0c9be29f26b99ef8719a4d_Image2_cleaned.png)

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0c9c170d8bc33cdd66d95b_Image3_cleaned.png)

"The far-out vision is Devin not just being an IC engineer, but giving it much higher-level goals." —Walden Yan

## Cognition routes across multiple models. What specifically makes Claude well-suited for the autonomous, long-horizon work you route to it?

**Scott:** One is just the ability to do long-running tasks. With a lot of models, you generally see that after enough time, they get confused or forget what they were doing. Claude models have been ahead of the curve at being able to follow through and consistently work on a longer-running task.

Two is having intelligent usage of the tools available to it. With Devin, we give the model access to all sorts of different things: the PR itself, the commit history, different files of the codebase, the ability to ask a clarifying question. It takes a certain kind of intelligence to know how to use the different tools at your disposal, or when to use a tool at all.

The third is more subjective. You want to be able to give the agent a two-line description of what you *think* needs to happen and have it expand from there and already know what you mean about the other details. It’s a little different from the binary of ‘Did it do the task or not?’ We've often found that Claude models perform particularly well at that.

"Claude models have been ahead of the curve at being able to follow through and consistently work on a longer-running task."

Scott Wu

CEO, Cognition

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0c9c3e0069932f2ca68d85_Image1_cleaned.png)

"Claude models have been ahead of the curve at being able to follow through and consistently work on a longer-running task." —Scott Wu

## As coding itself gets easier with AI, how do you think about where Cognition focuses?

**Scott:** One thing that happens now that the part of writing the code gets so much easier is you actually start thinking about all the other parts of the process and how to really optimize this.

I really don't believe that there's just a single product for all of code or all of software engineering. The question for us has always been, what is the thing that we really want to narrow in on and focus on above all else? And how are we going to make that into a true best-in-the-world experience? For us, that is largely the entire flow of how you work with and use a full remote agent.

## Looking ahead, what are you most excited about?

**Scott:** I love typing code, but I don't think it's something that we'll need to do for all that much longer. Right now, our engineers at Cognition don't type code anymore. You can just give instructions and prompts to your agents and have them go work on it. We're pretty quickly getting to a world where you can really just work with the specs and diagrams of what you want your product to be, and English can be the source of truth of how we build software.

That's exciting because it means way more people will get the chance to build software of their own. Walden has this line I've always loved: for so long we've all been living in survival mode of Minecraft, and pretty soon we're going to be in creative mode. It really feels like we’re living in the golden age of software engineering. There’s so much more for us to do together than separate, and that’s what we’re excited about.

**Walden:** The far-out vision is Devin not just being an IC engineer, but giving it much higher-level goals, having it come up with its own tasks, and spin up its own engineering team to go execute on.

Choosing the right Claude model

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69c2dd485d80024bc14f48c6_choosing%20model.jpeg)

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Read more

[Read more](#)Read more

Choosing the right Claude model

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

"The far-out vision is Devin not just being an IC engineer, but giving it much higher-level goals."

Walden Yan

Co-founder and CPO, Cognition

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

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

[A conversation with Cursor on building coding agents for professional developers](/customers/cursor-qa)A conversation with Cursor on building coding agents for professional developers

A conversation with Cursor on building coding agents for professional developers

Customer story

[Customer story](/customers/cursor-qa)Customer story
