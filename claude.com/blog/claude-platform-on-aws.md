<!-- source: https://claude.com/blog/claude-platform-on-aws -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

# Introducing the Claude Platform on AWS

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Platform
* Date

  May 11, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-platform-on-aws

The Claude Platform on AWS is now generally available, offering a new way for AWS customers to access the full set of Claude Platform features with AWS authentication, billing, and commitment retirement. Claude also remains available on Amazon Bedrock, where AWS is the data processor.

Starting today, Claude Platform on AWS customers can deploy agents at scale with [Claude Managed Agents](https://claude.com/blog/claude-managed-agents) and build with tools like code execution, skills, the advisor strategy, and more.

## Access the complete Claude Platform via AWS

The Claude Platform on AWS brings the full set of Claude API features to AWS customers for the first time, with all new features and betas shipping the same day they go live on the native Claude API.

Authentication runs through AWS IAM, audit logging through CloudTrail, and billing through a single AWS invoice that fully retires against existing commitments. Customers use their existing AWS credentials and IAM policies, so teams stay within the tools and permissions they already manage.

Claude Platform on AWS will be available in most AWS commercial regions and support global and U.S. inference geographies.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fcc87b15a611db84c61768_logo_reliaquest-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fcc89e5fe2e0869c3fead4_logo_reliaquest-dark.svg)

“Claude Platform on AWS helped simplify how we access Claude, improved the experience for key users like our Claude Code engineers, and gave us a practical path to integrate further frontier AI capabilities into our cybersecurity and engineering workflows, while staying within our existing cloud operating model. The Anthropic team was engaged, collaborative, and gave us confidence as we expanded usage.”

Jonathan Echavarria, Principal Research Scientist

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fcc823ca0eaa97b917abdf_logo_openrouter-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69fcc82ab6096dc10f41e565_logo_openrouter-dark.svg)

“Using Claude Platform on AWS gives OpenRouter and our users direct access to the latest and greatest features of the native Claude API; everything our cutting edge customers and use cases need is available and we control access through the same AWS IAM credentials we use for other AWS services. It has delivered consistent performance on uptime, latency, and throughput, and working directly with the Anthropic team has helped us move faster.”

Tomas Oliva, AI Platform Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692482151d80f9362c5b90c9_emergent-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692482163de140b3aa9e1ebb_emergent-white.svg)

“Claude Platform on AWS gives us the canonical Anthropic API with AWS as the access layer, so we get full feature parity and day-one access to new model capabilities. Support has been one of the best parts, and it felt like one team across both companies, not two separate relationships. That kind of collaboration during scale-up is rare, and it's a big reason we've been able to keep moving as fast as we have.”

Avinash Vishwakarma, Chief Architect

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## What's included

The Claude Platform on AWS includes native platform features, like:

* [**Claude Managed Agents (beta)**](https://platform.claude.com/docs/en/managed-agents/overview)to build and deploy agents at scale
* [**Advisor strategy (beta)**](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)to give agents an intelligence boost by consulting an advisor model
* [**Web search**](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) **and** [**web fetch**](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool) to augment Claude’s knowledge with current, real-world data from across the web
* [**Code execution**](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) to run Python code, create visualizations, and analyze data directly within API calls
* [**Files API (beta)**](https://platform.claude.com/docs/en/build-with-claude/files) for uploading and referencing documents across conversations
* [**Skills (beta)**](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) to teach Claude best practices so it delivers consistent results
* [**MCP connector (beta)**](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector) to connect Claude to any remote MCP server without writing client code
* [**Prompt caching**](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for reducing costs and latency on repeated context
* [**Citations**](https://platform.claude.com/docs/en/build-with-claude/citations) for grounding responses in source documents
* [**Batch processing**](https://platform.claude.com/docs/en/build-with-claude/batch-processing) for high-volume, asynchronous workloads

Claude Platform on AWS customers also get access to the Claude Console, Anthropic's development environment for building and testing with Claude. The Console includes management for agents, skills, environments, vaults, observability tools, and more.

Claude Opus 4.7, Sonnet 4.6, and Haiku 4.5 are available, with new models shipping on the Claude Platform on AWS as they launch.

## Choosing the right path for developers

Both the Claude Platform on AWS and Claude on Amazon Bedrock enable AWS customers to build on Claude models. The difference is in who operates the service and which features are available.

The **Claude Platform on AWS** is a first of its kind offering for Anthropic, giving you all native Claude API features from day one. Anthropic operates the service and data is processed outside the AWS boundary. This is a good option for companies that want the full Claude Platform experience.

**Claude on Amazon Bedrock** keeps AWS as the data processor and operates within the AWS boundary. This is a good fit for companies that have strict regional data residency requirements or need their data processed exclusively within AWS's infrastructure.

## Getting started

The Claude Platform on AWS is available today. To get started, visit the [Claude Platform on AWS](https://aws.amazon.com/claude-platform/) or explore the [documentation](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws).

If you have an existing Bedrock private offer, please contact your Anthropic or AWS account executive before getting started with Claude Platform on AWS to ensure your discounts are applied correctly. Discounts cannot be applied retroactively to usage incurred before a Claude Platform private offer is accepted.

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

Jul 28, 2026

### Bringing MCP 2026-07-28 to Claude

Product announcements

[Bringing MCP 2026-07-28 to Claude](#)Bringing MCP 2026-07-28 to Claude

[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)Bringing MCP 2026-07-28 to Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

Jul 2, 2026

### Giving admins more visibility and control over Claude spend

Product announcements

[Giving admins more visibility and control over Claude spend](#)Giving admins more visibility and control over Claude spend

[Giving admins more visibility and control over Claude spend](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)Giving admins more visibility and control over Claude spend

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d23008bbc20c0ffaeb6f_43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)

Jun 18, 2026

### Centrally manage authorization for MCP connectors

Enterprise AI

[Centrally manage authorization for MCP connectors](#) Centrally manage authorization for MCP connectors

[Centrally manage authorization for MCP connectors](https://claude.com/blog/enterprise-managed-auth) Centrally manage authorization for MCP connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

Sep 10, 2024

### Claude for Enterprise

Product announcements

[Claude for Enterprise](#)Claude for Enterprise

[Claude for Enterprise](https://claude.com/blog/claude-for-enterprise)Claude for Enterprise

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Platform

Agents
