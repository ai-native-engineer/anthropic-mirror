<!-- source: https://claude.com/customers/zendesk -->

Case Study

# Zendesk built custom agents on Claude and reached 1 million agent executions in 7 weeks

[Try Claude](https://claude.ai)

![Zendesk logo](https://assets.claude.com/eb4ae3eeaffc7fb16618696c1baa3ef6c6224977.svg)

Industry:
:   Software

Company size:
:   Large

Product:
:   [Claude Platform](https://claude.com/platform/api)

Partner:
:   AWS

Location:
:   North America

1 million custom agent executions

in the first seven weeks of early access

Up to 80% reduction

in human handle times for customers running custom agents

Zendesk, which provides AI for customer and employee service, built a way for its customers to create their own AI agents for the parts of their service work that are specific to their business. The agents run on Claude, and they ran 1 million times in their first seven weeks of early access.

## With Claude, Zendesk:

* Built its custom agent builder with a five-person team, working with Claude Code and the Claude Agent SDK, going from proof of concept to early access in four months
* Went from zero to 1 million custom agent executions within seven weeks of early access
* Helped one customer that handles more than 14 million service requests a year automate duplicate merging at 99% accuracy in its pilot
* Raised automated resolution by up to 10% while cutting human handle times by up to 80% for customers running custom agents
* Runs Claude through Amazon Bedrock, inside the AWS environment and hosting regions it already operates

## The challenge

## The work that stayed manual

Zendesk already helps companies automate a large share of their customer requests with AI. The harder part is the work that happens between a customer’s first message and the final outcome, like exceptions to a return policy, complicated warranty claims, or detailed billing questions.

Smaller companies handled that work with people, one request at a time. Larger ones with AI teams built one-off automations, which took a lot of engineering time and only covered the easiest cases. “Every customer is so unique to what they do,” said Abhinay Kathuria, Director of AI/ML at Zendesk. “There’s a lot that happens behind-the-scenes, and a lot of this was being handled manually.”

## The solution

## Powering custom agents with Claude Sonnet

Kathuria’s team tested models from Anthropic and other providers on the testing system they use across Zendesk products. It scores each model on 15 metrics using agents like the ones customers actually write, and the team runs it again whenever a new model comes out. Because these agents act on real customer requests, getting the answer right matters a lot.

Zendesk chose Claude Sonnet 4.6. Sonnet did “exceedingly well” on pilot tasks like reading PDFs, and in Zendesk’s testing, it needed fewer steps to reach a decision. “A competitor model might come to the same conclusion, but it might take four or five planning turns to get there,” Kathuria said. “Sonnet could handle a lot of those in one shot.”

Kathuria now makes the same argument to Zendesk customers. “You can’t just look at token price in isolation,” he said. “You have to look at the cost per task.”

Where Claude runs came down to security and data locality. Zendesk already runs its infrastructure on Amazon Web Services (AWS), so it serves Claude through Amazon Bedrock. Zendesk keeps model processing in the AWS hosting regions it already uses, which helps it meet customers’ data-residency and governance requirements. Zendesk says this also means its customers don’t have to approve or manage an additional cloud subprocessor. “Our most important security benefit is that Claude runs through the AWS environment we already operate and govern,” Kathuria shares.

## Agents written in English, connected to the tools teams already have

To set up a custom agent, a Zendesk customer writes instructions in plain English, then connects the agent to Zendesk actions and outside tools like Jira and Google Drive in a few clicks. It takes about 30 minutes to set up something that used to take months of engineering work.

Take incident triage. When a lot of similar tickets come in at once, the agent notices, files a Jira issue, posts in Slack to let engineers know, and tells the affected customers the problem is being worked on. Once the fix ships, it closes all the related tickets and adds a note explaining what went wrong.

Zendesk is also building a router to send each task to the right place. Simple requests, like working out what a customer is asking for, take one call to Sonnet. Harder ones go through a longer process where the agent plans its steps before acting. After each run, the agent reviews its own work and saves what it learned as a skill it can use next time.

Customers decide which actions each agent is allowed to take. Zendesk is also shipping ways to watch and test agents, including a log of every tool call, simulated conversations, and A/B testing. “Our customers are asking for exactly the same things we need internally,” Kathuria said. “A lot more agent observability, and how to test these agents in production.”

> “Our most important security benefit is that Claude runs through the AWS environment we already operate and govern,”

Abhinay KathuriaDirector of AI/ML, Zendesk

## The outcome

## 1 million agent executions in seven weeks

In the first seven weeks of early access, custom agents ran 1 million times. General availability is planned for Zendesk's AI Summit in November and several large customers are getting ready to move much more volume onto them. “We have four or five customers who are going to run 20 million tickets through these agents powered by Claude every year,” Kathuria said.

Across customers running custom agents, automated resolution has gone up by as much as 10%. Zendesk calls its long-term goal an Autonomous Service Workforce, where AI handles 80% or more of customer and employee requests and people handle the rest with help from AI. Next, it plans to offer more specialized agents built for specific industries and types of work.

“The era of generic, one-size-fits-all AI agents is over. The best agents are specialists: deeply grounded in the work, the industry, and the business they serve,” said Shashi Upadhyay, President of Product, Engineering and AI at Zendesk. “Our custom agents powered by Claude are taking on more complex work, earning trust, and driving more measurable impact for our customers.”

> “Our custom agents powered by Claude are taking on more complex work, earning trust, and driving more measurable impact for our customers.”

Shashi UpadhyayPresident of Product, Engineering and AI, Zendesk

[![Supermetrics](https://assets.claude.com/3ac4171a81008be0340e5c3d8ccb46571c3edfb3.svg)

### Supermetrics lets marketers manage ad campaigns from a conversation with Claude](https://claude.com/customers/supermetrics)[![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

### How Atlassian builds AI agents teams can trust with Claude and Google Cloud](https://claude.com/customers/atlassian)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### Rocket Money on building agents that fix their own code](https://claude.com/customers/rocket-money-qa)[![Rocket Money](https://assets.claude.com/cabc58f91e6bcb5b5ed8fb2da747e25daaf3aea0.svg)

### How Rocket Money built its personal finance agent with Claude](https://claude.com/customers/rocket-money)
