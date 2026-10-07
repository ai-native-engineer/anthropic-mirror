<!-- source: https://claude.com/resources/guides/financial-services-guide-to-building-autonomous-ai-agents/better-together -->

Chapter 039 min read

# Better together: How Anthropic and AWS power autonomous AI agents

9 min read

27 min remaining

Building AI agents for financial services requires exceptional precision and accountability. Your agents need to understand complex regulations, handle sensitive data securely, and explain every decision they make. One wrong calculation or data breach can trigger serious consequences.

This is why leading financial institutions are turning to [Claude (opens in new tab)](https://claude.ai/), Anthropic's family of advanced AI models known for their industry-leading coding and reasoning capabilities, nuanced understanding, and unwavering emphasis on safety and reliability. Claude doesn't just process data; it understands context, maintains consistency across complex workflows, and provides the explainability that regulators demand.

Deployed through Amazon Bedrock, AWS's fully managed service that delivers enterprise grade security, privacy and responsible AI capabilities, Claude becomes even more powerful. Bedrock eliminates the infrastructure complexity that typically slows innovation, while providing the robust governance controls and compliance frameworks that financial services require.

In this section, we'll share core capabilities of Claude and Amazon Bedrock, as well as additional services and solutions that support agentic development on AWS, including:

* **Anthropic's Financial Analysis Solution (FAS)** for building custom financial services agents
* **Model Context Protocol (MCP)** for providing agents with secure access to relevant data and tools
* [**Strands Agents SDK** (opens in new tab)](https://strandsagents.com/latest/) for building and running agents with minimal code
* [**Amazon Bedrock AgentCore** (opens in new tab)](https://aws.amazon.com/bedrock/agentcore/) IaaS for deploying and operating agents at scale

Together, Claude in Amazon Bedrock represents more than just technology. It's a complete solution that enables financial institutions to build powerful, safe agents at scale without compromising on the security, compliance, and reliability that define trust in financial services.

## Choose the right Claude model for your needs

The Claude family offers a range of models to match different financial services use cases and performance requirements:

**Claude Haiku** models provide lightning-fast responses for high-volume, cost-sensitive applications like customer support and document processing.

**Claude Sonnet** models balance strong performance with efficiency, making it ideal for complex tasks like financial analysis and risk assessment.

**Claude Opus** models deliver maximum intelligence for the most demanding applications requiring deep reasoning and comprehensive analysis.

At the core of Claude's design is a commitment to transparency and trustworthiness, critical requirements for financial services where decisions must be auditable, compliant, and aligned with regulatory standards.

### Building trust with explainable AI

Your stakeholders need to trust AI decisions. Claude's [Constitutional AI framework (opens in new tab)](https://www.anthropic.com/research/constitutional-ai-harmlessness-from-ai-feedback) ensures every decision can be explained and audited. With SOC 2 Type II certification and a guarantee that your data never trains the model, you can deploy AI without compromising security or intellectual property.

### Achieve superior financial reasoning and analysis

Claude's reasoning capabilities set it apart in the complex world of financial analysis, where nuanced understanding can mean the difference between profit and loss. Claude Opus 4.1 demonstrates [top performance (opens in new tab)](https://www.vals.ai/benchmarks/finance_agent-04-22-2025) on the Finance Agent Benchmark, outperforming competitors on critical financial reasoning tasks, from analyzing earnings transcripts to building complex valuation models.

Agents in the wild

The Norwegian sovereign wealth fund experienced 20% productivity gains (equivalent to 213,000 hours saved) with Claude in Bedrock. [Learn more here (opens in new tab)](https://claude.com/resources/webinars/nbim-ai-journey).

## Deploy Claude at enterprise-scale with Amazon Bedrock

For financial institutions seeking to harness Claude's capabilities while maintaining enterprise-grade security, performance, and integration with existing infrastructure, Bedrock emerges as the purpose-built platform that bridges cutting-edge AI with the stringent demands of financial services.

### Ensure security and meet compliance requirements

Bedrock keeps your data within your secure AWS environment. Your information never leaves your control or gets used to train models. With private endpoints in your VPC, you can connect Claude to internal systems while maintaining complete isolation—critical for sensitive use cases like anti-money laundering analysis.

Agents in the wild

With Claude in Bedrock, Brex automated 75% of expense transactions with a 94% compliance rate, vs. the industry standard of 70%. [Learn more here (opens in new tab)](https://www.anthropic.com/customers/brex).

### Scale seamlessly and optimize performance

Amazon Bedrock also transforms how financial institutions deploy and manage AI models like Claude at scale, eliminating the complexity of infrastructure management while delivering consistent, high-performance AI inference.

Agents in the wild

IG Group experienced triple-digit improvements in speed-to-market for their global trading platform and financial services products with Claude. [Learn more here (opens in new tab)](https://www.anthropic.com/customers/ig-group).

## Accelerate financial analysis with Anthropic's Financial Analysis Solution

In addition to using Claude in Bedrock, financial institutions can leverage Anthropic's [Financial Analysis Solution (opens in new tab)](https://www.anthropic.com/news/claude-for-financial-services) (FAS) as a production-ready foundation for building AI agents specifically geared towards financial services use cases. FAS accelerates agent development through pre-built integrations with over 10 critical financial data providers:

* **Market intelligence:** Direct connections to FactSet, S&P Capital IQ, and other data sets enable agents to access real-time market data, corporate fundamentals, and historical analytics without custom API development.
* **Deal and company data:** Integrations with Daloopa, Morningstar, and PitchBook allow agents to automatically pull deal comparables, financial metrics, and industry benchmarks for due diligence workflows.
* **Enterprise analytics:** Native connections to Databricks, Snowflake, and Box ensure agents can seamlessly access proprietary data lakes, financial models, and internal research.

Beyond connectivity, the solution equips financial agents with specialized tools:

* **Native Office Integration:** Agents can directly manipulate Excel models and generate PowerPoint presentations, eliminating manual data transfer between AI insights and deliverables
* **Agentic Research Workflows:** Pre-configured patterns for equity research, credit analysis, and portfolio optimization that combine web search, document analysis, and quantitative modeling
* **Financial Prompt Library:** Battle-tested prompts for DCF modeling, comparable analysis, earnings interpretation, and risk assessment that encode best practices from leading financial institutions

## Provide contextual awareness with Model Context Protocol

Another technology financial services organizations can use to build autonomous AI agents is [Model Context Protocol (MCP) (opens in new tab)](https://modelcontextprotocol.io/), an open framework developed by Anthropic that enables financial agents to connect and interact with external tools, applications, and data sources.

MCP's true power emerges when orchestrating multiple specialized agents into collaborative intelligence networks. Financial institutions can create agent teams where each member brings specific expertise.

Consider a private equity due diligence workflow:

1. **Market Analysis Agent** connects to a FactSet MCP server to gather sector trends and comparable transactions
2. **Financial Modeling Agent** accesses internal data warehouses through enterprise MCP servers to build valuation models
3. **Risk Assessment Agent** queries compliance databases and regulatory feeds to identify potential issues
4. **Synthesis Agent** aggregates insights from all specialists to generate investment committee materials

## Build flexible agentic systems with Strands Agents

Strands Agents is an open source SDK that accelerates how financial teams can build Claude-powered autonomous AI agents by eliminating boilerplate code and focusing on business logic. Its model-driven architecture particularly suits financial analysis where requirements evolve rapidly with market conditions.

This simplicity enables financial teams to iterate rapidly, adjusting agent behavior for new regulations, market conditions, or investment strategies without rebuilding infrastructure.

## Deploy agents in production with Amazon Bedrock AgentCore

[Amazon Bedrock AgentCore (opens in new tab)](https://aws.amazon.com/bedrock/agentcore/) provides purpose-built services and tools to handle dynamic agent workloads, offering capabilities like secure identity management, memory, code interpretation, web automation, gateway and observability, all working together to eliminate the need to manage complex agent infrastructure.

While complete session isolation ensures that agents handling different clients' data never intersect, integration with existing identity providers enables automated permission management aligned with institutional access controls.
