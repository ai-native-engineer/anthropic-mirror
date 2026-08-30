<!-- source: https://claude.com/customers/notion-qa -->

Q&A | Claude Managed Agents

# How Notion ships and scales agents with Claude Managed Agents

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69d66e4b0c9ac6ae2011f8bf_notion-qa-thumbnail.jpeg)

Industry:

Software

Company size:

Large

Product:

Claude Managed Agents

Location:

North America

18,000 Claude agents

created in the first three weeks

90% of agent turns triggered by automations,

not chat

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

Three weeks after launching External Agents, collaborative AI workspace [Notion](http://claude.com/customers/notion) had 18,000 agents created by customers, and 90% of agent activity running on automated triggers rather than chat. Notion built the feature on Claude Managed Agents, Anthropic's suite of composable APIs for building and deploying agents at scale. Product manager Eric Liu spoke with Anthropic about what Managed Agents handled and what's surprised him since launch.

## Anthropic: You shipped External Agents on Managed Agents recently. How are people actually using them?

**Eric Liu, Notion:** We want Notion to be the best collaboration platform for agents and teams. A key part of that mission is bringing the best agents to work natively in Notion, and Claude is at the top of that list: the number one external agent people wanted to use in Notion. So far it's about 18,000 Claude agents created, and those agents have done about 140,000 steps. We were pleasantly surprised by how quickly it ramped up, with very little marketing. A large percentage of people creating agents in Notion now create Claude agents. We're seeing strong depth of usage too. 90% of the turns people are doing with Claude are automations in Notion, triggered on a Notion page, a Slack message, or scheduled runs. It's not directly chatting with Claude; the wrapper we built around it for automations is what's resonating with our customers. Our top workspaces are really using it for multiplayer workflows: a workspace will have three or four agents running dozens of threads per day, mainly through automations.

## Anthropic: How would you explain what you’ve built with Managed Agents?

**Liu:** You’re creating these software building blocks in Notion and you can construct them into any workflow you want. For example, we created a task board that acts as an orchestrator. You create a task, move it to "ready to start," and it invokes a Claude session. Claude picks up context from connected pages, our design system, API docs, and product requirements documents. In other words, you're working with Claude just like a colleague.

The nice thing is that you're not limited to one task. Customers can kick off 30 or 40 jobs at the same time, and our platform routes them to the right person for approvals. People are automating the busy work: experiment flag cleanup, a lot of different mini tasks around triage.

"Claude is the number one external agent people wanted to use in Notion."

Eric Liu

Product Manager, Notion

## Anthropic: Why did you decide to add Managed Agents into Notion?

**Liu:** Users were asking us for Claude. Our customers don't want to use one agent to talk to another agent to do a backflip to get things connected. They just want to be in Notion and say, "Claude, help me make this website." Managed Agents was a great solution because we just pulled in the API and it worked within the product.

We focus on what's native to Notion: your company knowledge. Our agent is good at using Notion, but it's not the best at coding, and Claude models are very good at that. There's a whole world of other files that Claude is really good at generating. Underneath, all agents are basically coding agents. And that's unlocking a lot of non-coding use cases. If you're creating a presentation for marketing or sales, you're taking knowledge and generating an artifact, whether that's a PDF, slides, or something else. That synthesis of information into an artifact is roughly the same workflow that works really well in coding. We're seeing that transition into the rest of knowledge work.

## Anthropic: Teams can implement Managed Agents three ways: as Claude-branded agents in the product, as an unbranded engine behind their own agent, or as internal agents. Why did Notion go Claude-branded?

**Liu:** Our vision with Notion is to make it the command center for agents: allowing teams to use their favorite agent and use it natively within Notion. If you are a collaboration product, the idea of being able to use an agent in the product is the core user journey. The benefit of bringing in Claude is people trust the intelligence of the model and the experience.

The session streams from Managed Agents into Notion's client. But to the user, they don't know any of that is happening. All they're seeing is that Claude is writing files, writing Notion pages, updating things, commenting and doing everything that teammates and other agents can do.

## Anthropic: What did Managed Agents handle that you didn't have to build yourselves?

**Liu:** Having an infrastructure layer that can do long-running tasks was really essential. That ability to continue to run tasks, to manage memory, and to have high quality outputs over time is a layer that's super critical on top of the model itself.

The best surprise was that we didn't have to set up any of this. All of the skills, all the different packages we need, it was very easy to go and spin up.

The sandbox is really important if you want coding use cases. Part of our flow for users is the ability to connect their GitHub, and through that they can pull in their repos and then run the code. The GitHub endpoint in Managed Agents was really useful.

## Anthropic: You've said most agent tools are designed for a single person working with a single agent. What breaks when organizations try to scale that?

**Liu:** The challenge of deploying agents at scale is really about collaboration. Right now, agents feel very one-to-one. It's you and an agent in an interface. But what does it look like for your whole team, with all of the approval processes and everything required to actually use agents at scale? That's fundamentally the same problem we've solved before at Notion, which is human collaboration. Now it's agent and human collaboration, and it turns out a lot of the same patterns around suggested edits, version history, and shared knowledge bases are really critical.

## Anthropic: You've been using this yourself. What's that been like?

**Liu:** The Managed Agents product is like a playground for me. Even with the early prototype, we saw 12 hours of prototyping work collapse into about 20 minutes. Then your whole team can jump in and refine it together.

When I was prototyping new features for Notion using the task board workflow, I had about 30 tasks. I took all of them and just dragged them to start. I went and got a snack, came back, and all the prototypes were made. Then I tagged in somebody on my team, and we jammed on the same output together right in Notion. We've turned AI solo work into a collaborative moment. That was the point where I was like, everybody should be doing this.

People now see Claude show up in their Notion task doing work, and they give a thumbs up or thumbs down. That's an interface they already understand.

## Anthropic: You've described teams deploying an army of agents: a separate Claude for each stage of work, mostly running on triggers. How do you make sure they act safely?

**Liu:** We've created a Claude agent for each stage: one that investigates, one that plans, and one that builds. What's useful about that is each agent can have its own permissions, its own contexts, and its own automations. The review agent is managed by a few people, but many people can manage the investigator agent.

Every agent that you create is locked down from a permission standpoint by default, which means it starts private. You have to share it explicitly. Then we have a bunch of different access permissions: some people will only be able to chat with it, some people can trigger it, some people can edit it. When you have 20 or 30 people working on the same shared task board, how do you make sure that at the right point, the right person is brought in? The way that we think about solving the automated workflow is also solving the permissions and collaboration problems. Those go hand in hand.

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

"The benefit of bringing in Claude is people trust the intelligence of the model and the experience."

Eric Liu

Product Manager, Notion

## Anthropic: You preload Claude's public skills, run a skills marketplace, and let agents maintain their own skills database. Why are skills such a big part of this?

**Liu:** Claude has a lot of great skills, so we preloaded the ones that are publicly available for making PowerPoints, PDFs, and docs. Within Notion, we have a whole marketplace of skills, and we're letting folks bring in their own skills for their own Claude agent.

With skills, it's more about *how* you do something, and not so much if it can do it. It’s not about knowing how to make a PowerPoint, but more about "Hey, this is our flavor of PowerPoint. This is how we like it written."

A lot of these skills are basically auto-maintained. Once there's a merged pull request or a completed task, Claude identifies the lessons the agent can learn and feeds them back into the skills as updates. Every time you say "this is a great prototype" or "this is a great PDF," that feeds into the skills. The quality keeps improving without someone manually updating the knowledge base.

## Anthropic: How do you think Notion changes over the next six months as a result of this?

**Liu:** The interface is becoming more about human beings reviewing the work of agents. We are the translation layer to agents. We'll keep the same primitives around the page and the database, but we're going to build a lot more around version control and humans in the loop.

The question becomes: how can humans become the reviewers of agentic work rather than directly the doers? I think that paradigm applies to a lot of AI.

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

[Rocket Money on building agents that fix their own code](https://claude.com/customers/rocket-money-qa)Rocket Money on building agents that fix their own code

Rocket Money on building agents that fix their own code

Customer story

[Customer story](https://claude.com/customers/rocket-money-qa)Customer story

[How Rocket Money built its personal finance agent with Claude](https://claude.com/customers/rocket-money)How Rocket Money built its personal finance agent with Claude

How Rocket Money built its personal finance agent with Claude

Customer story

[Customer story](https://claude.com/customers/rocket-money)Customer story

[Deepgram ships 4–10x more durable code with Claude](https://claude.com/customers/deepgram) Deepgram ships 4–10x more durable code with Claude

Deepgram ships 4–10x more durable code with Claude

Customer story

[Customer story](https://claude.com/customers/deepgram)Customer story
