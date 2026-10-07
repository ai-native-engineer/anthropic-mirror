<!-- source: https://claude.com/resources/guides/building-effective-ai-agents/executive-summary -->

Chapter 016 min read

# Executive summary

6 min read

63 min remaining

## Generative AI answers questions. AI agents solve problems

For companies across industries, agents offer the potential for scaling operations in ways current automation could never deliver: open-ended problem-solving, dynamic decision-making, and complex multistep processes where the path forward isn't predetermined.

Organizations are seeing significant results from autonomous agents in production. For example, [Coinbase (opens in new tab)](https://www.claude.com/customers/coinbase), the leading cryptocurrency exchange managing $226 billion in quarterly trading volume, built agentic customer support systems powered by Claude. Their Claude-powered agents handle thousands of messages per hour while maintaining 99.99% availability—critical when customers need constant access to their funds. The platform has spawned 35-50 internal AI applications, transforming how the company serves millions of users globally.

[Tines (opens in new tab)](https://www.claude.com/customers/tines), the workflow orchestration and automation platform for security and IT teams, built agentic workflow systems with Claude. Their agents dynamically handle workflow logic during execution, collapsing complex multi-step security operations into single-agent operations, corresponding to 100x time-to-value improvement.

And [Gradient Labs (opens in new tab)](https://www.claude.com/customers/gradient-labs), the company building customer operations agents for financial services, deployed a customer support agent with Claude that understands customer queries within context and executes standard operating procedures. Achieving 80-90% resolution rates, their agents can handle complex workloads with limited human intervention, enabling employees to focus on relationship building and other strategic work.

AI agents open up countless possibilities for organizations of every size and sector, but implementing them requires careful consideration of architecture patterns, cost management, and operational governance.

## The business case for AI agents

Think of an [AI agent (opens in new tab)](https://www.anthropic.com/research/building-effective-agents) as a smart digital assistant that can work independently to solve complex business problems by using tools that connect to your real systems. At its core, an AI agent represents a sophisticated evolution of large language models that can autonomously direct their own processes and [tool usage (opens in new tab)](https://www.anthropic.com/engineering/writing-tools-for-agents) to accomplish complex tasks.

Traditional automation requires rigid prewritten scripts with every step mapped in advance. Agents work differently. They assess a task, choose appropriate tools, try approaches, evaluate results, and adjust strategies as needed, much like a skilled employee tackles unfamiliar projects. For example, an agent handling customer support escalations could read the issue, check account history, consult knowledge bases, draft personalized responses, and loop in specialists, all without human intervention.

What makes these systems powerful is their capacity for autonomous reasoning and [tool selection (opens in new tab)](https://www.anthropic.com/engineering/writing-tools-for-agents), combined with the ability to recover from errors and maintain persistence toward goal completion. Unlike traditional workflows where predefined code paths orchestrate AI interactions, agents maintain dynamic control over their decision-making processes, adapting based on environmental feedback and intermediate results.

This makes them particularly valuable for scaling complex operations where exact steps can't be predetermined, such as incident response, data analysis, customer onboarding flows, or development workflows where automated testing creates feedback loops for iterative problem-solving.

## What organizations are achieving

The organizations deploying agents are seeing numbers that matter.

At a retail bank, for example, AI agents transformed credit risk memo creation. What used to take relationship managers weeks of manually reviewing ten different data sources now delivers [20 to 60 percent productivity gains (opens in new tab)](https://www.mckinsey.com/capabilities/quantumblack/our-insights/seizing-the-agentic-ai-advantage) and cuts credit turnaround time by 30 percent. A European equipment manufacturer with over €10 billion in revenue mapped out their agentic AI strategy and found

* from teams running these systems in production
* Architecture patterns from single agents to multi-agent orchestration, with clear guidance on matching your specific problem to the right pattern(s)
* Technical requirements including API capabilities, tool integration, and memory management for production-ready agents that actually work at scale
* Security and compliance frameworks for protecting sensitive data while managing the unique risks that come with autonomous systems
* Implementation strategies for building teams and infrastructure that scale with model improvements (instead of fighting against them)
* Future-readiness indicators to help you build systems that grow more powerful as the underlying models improve – without growing more complex

Let's dive in.
