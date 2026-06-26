<!-- source: https://claude.com/customers/notion-qa -->

Q&A | Claude Managed Agents

# How Notion is building a workspace where teams and agents collaborate

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d66e4b0c9ac6ae2011f8bf_notion-qa-thumbnail.jpeg)

Industry:

Software

Company size:

Large

Product:

Claude Managed Agents

Location:

North America

30+ concurrent agent tasks

from a single task board

Self-improving skills database

maintained by Claude after every completed task

Case Study: Notion

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d66fcff40d6b828398a62c_og_case-study-notion.jpg)

Learn how Notion uses Claude to power enterprise AI search, reduce costs by 90% with prompt caching, and build agent workflows.

Read more

[Read more](http://claude.com/customers/notion)Read more

Case Study: Notion

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Learn how Notion uses Claude to power enterprise AI search, reduce costs by 90% with prompt caching, and build agent workflows.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Case Study: Notion

Learn how Notion uses Claude to power enterprise AI search, reduce costs by 90% with prompt caching, and build agent workflows.

[Prev](#)Prev

[Next](#)Next

Notion is a collaborative AI workspace where teams and agents work together. With the launch of [Claude Managed Agents](https://claude.com/blog/claude-managed-agents), a suite of composable APIs for building and deploying agents at scale, Notion product manager Eric Liu and his team have been building agent orchestration that lets Notion users delegate real work to coding and knowledge work agents from their task boards. He spoke with Anthropic about what's hard about deploying agents across an organization and what surprised him when he started using it himself.

## Most agent tools today are designed for a single person working with a single agent. What breaks when organizations try to scale that?

**Eric Liu, Notion:** The challenge of deploying agents at scale is really about collaboration. Right now, agents feel very one-to-one. It's you and an agent in an interface. But what does it look like for your whole team, with all of the approval processes and everything required to actually use agents at scale? That's fundamentally the same problem we've solved before at Notion, which is human collaboration. Now it's agent and human collaboration, and it turns out a lot of the same patterns around suggested edits, version history, and shared knowledge bases are really critical. Agents are doing so much of the work now that people are spending more of their time as editors and reviewers.

## Why did you decide to add Managed Agents into Notion?

**Liu:** Our customers don't want to use one agent to talk to another agent to do a backflip to get things connected. They just want to be in Notion and say, "Claude, help me make this website." Managed Agents was great because we just pull in the API and it works within the product.

Our agent is good at using Notion, but it's not the best at coding, and Claude models are very good at that. We also don't generate the long tail of artifacts. We focus on what's native to Notion: your company knowledge. But there's a whole world of other files that Claude is really good at generating.

## Walk us through what you built.

**Liu:** The way I think about it is that you’re creating these software building blocks in Notion and you can construct them into any workflow you want. For example, we created a task board that acts as an orchestrator. You create a task, move it to "ready to start," and it invokes a Claude session. You can mention the task, and it exists in all the surfaces you're collaborating with your team on. Claude picks up context from connected pages, our design system, API docs, and product requirements documents. In other words, you're working with Claude just like a colleague.

The nice thing is that you're not limited to one task. For our customers, what that means is that they can kick off a ton of jobs in Notion, 30 or 40 at the same time, and our platform routes them to the right person for approvals. That's what makes doing it in Notion so valuable.

“You're working with Claude just like a colleague.”

Eric Liu

Product Manager, Notion

## How is Managed Agents integrated into Notion’s Custom Agents?

**Liu:** Having an infrastructure layer that can do long-running tasks is really essential. You might need to run a coding agent for 20 minutes, an hour, or for a really long time. That ability to continue to run it, to manage memory, to have high quality outputs over time is a layer that's super critical on top of the model itself. The Managed Agents product is like a playground for me. Even with the early prototype, we saw 12 hours of prototyping work collapse into about 20 minutes. Then your whole team can jump in and refine it together.

Underneath, all agents are basically coding agents. And that's unlocking a lot of non-coding use cases. If you're creating a presentation for marketing or sales, you're taking knowledge and generating an artifact, whether that's a PDF, slides, or something else. That synthesis of information into an artifact is roughly the same workflow that works really well in coding. We're seeing that transition into the rest of knowledge work.

## What’s the experience like for users?

**Liu:** Working with agents in a place that people are already familiar with can be a huge unlock. People now see Claude show up in their Notion task doing work, and they give a thumbs up or thumbs down. That's an interface they already understand.

When I was prototyping new features for Notion using the task board workflow I mentioned, I had about 30 tasks. I took all of them and just dragged them to start. I went and got a snack, came back, and all the prototypes were made. Then I tagged in somebody on my team, and we jammed on the same output together right in Notion. We've turned AI solo work into a collaborative moment.

That was the point where I was like, everybody should be doing this. It's something that feels very foreign right now, where it's usually just you and an agent. This is everybody building something together.

## One of the more interesting things you've built is a skills database that updates itself. How does that work?

**Liu:** Once there's a merged pull request or a completed task, Claude identifies the lessons the agent can learn and feeds them back into the skills as updates. A lot of these skills are basically auto-maintained. Every time you say "this is a great prototype" or "this is a great PDF," that feeds into the skills. The quality keeps improving without someone manually updating the knowledge base.

## How do you think Notion changes over the next six months or so as a result of this?

**Liu:** It will have a lot more agents. The interface we built for Notion has really been about humans doing the tasks. But the interface is becoming more about human beings reviewing the work of agents. Approval flows, suggested edits, all those things that humans already understand, we are the translation layer to agents. We'll keep the same primitives around the page and the database, but we're going to build a lot more around version control, human in the loop, and reviews.

I think the question becomes: how can humans become the reviewers of agentic work rather than directly the doers? I think that paradigm applies to a lot of AI.

Claude Managed Agents: Get to production 10x faster

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d6874d9013e4890f253b80_managed-agents-og.jpg)

We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

Read more

[Read more](https://claude.com/blog/claude-managed-agents)Read more

Claude Managed Agents: Get to production 10x faster

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Managed Agents: Get to production 10x faster

We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

“We saw 12 hours of prototyping work collapse into about 20 minutes. Then your whole team can jump in and refine it together.”

Eric Liu

Product Manager, Notion

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
