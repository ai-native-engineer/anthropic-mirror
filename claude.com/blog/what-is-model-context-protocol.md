<!-- source: https://claude.com/blog/what-is-model-context-protocol -->

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

# What is Model Context Protocol? Connect AI to your world

Connect AI assistants to your tools without custom integrations using Model Context Protocol.

Explore Connectors

[Explore Connectors](https://claude.com/partners/mcp)Explore Connectors

  [Agents](https://claude.com/blog/category/agents)
* Product

  Claude apps
* Date

  October 31, 2025
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/what-is-model-context-protocol

AI models are only as good as the context provided to them. AI assistants like [Claude](https://claude.ai) can answer questions and perform an impressive range of tasks, but if they can't access the data or tools they need, they're limited in what they can do for you. You typically solve this by copying and pasting context from one tab to another, whether it's editing a document in Google Drive, replying to a thread in Slack, or updating code in an IDE. This process is slow, manual, and risks leaving out important context.

The **Model Context Protocol (MCP)** offers a solution that is open and widely available across all AI apps and assistants. In this article, you'll learn what MCP is, how it works and why it matters, and who it's for. You'll see examples of MCP in action and understand how you can start using or building with MCP today.

## What is the Model Context Protocol (MCP)?

The **Model Context Protocol** is an open standard that defines how LLMs communicate with external systems.

Think of MCP as **USB-C for LLMs**. Just as USB-C provides a universal connector for your phone, laptop, and other devices, MCP provides a universal format for LLMs to connect with external systems. Before USB-C, every electronic gadget had its own cable: Lightning for iPhone, micro-USB for Android, proprietary connectors for cameras. As more devices adopted USB-C, connectivity became seamless across the ecosystem.

MCP brings this same simplicity to AI integrations. Before MCP, every application and database required custom code to connect with LLMs. Google Drive needed its own integration, Slack needed another, Figma yet another. Now, MCP provides a single, standardized format for connecting these tools to Claude and other AI applications.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68f64b7d51a1d57549b3ad8e_What%20is%20MCP_%20Final%402x.png)

## Where did MCP come from?

MCP was created at Anthropic by David Soria Parra and Justin Spahr-Summers. The idea originated from David's frustration with constantly copying code between Claude Desktop and his Integrated Development Environment (IDE). Recognizing this as a classic M×N problem where multiple applications need multiple integrations, David pitched building a protocol to solve this to Justin. They designed MCP based on the popular Language Server Protocol and open-sourced it in November 2024 with Anthropic's support to ensure the entire AI ecosystem could benefit.

## How does MCP work?

MCP works through a two-sided approach. AI agents and chatbots like Claude create **MCP Clients**, so they can connect to applications like Notion, Canva, or Figma, who make their tools and data available through **MCP Servers**.

By building an **MCP Client**, AI agents and chatbots can access thousands of MCP Servers built by the community, giving them a straightforward path to extend their capabilities. By building an **MCP Server**, companies and developers can make their products readily available to AI, creating a new avenue to provide value.

As MCP is open-source, anyone can build an MCP Server or Client.

## Why is MCP important?

MCP allows LLMs to go beyond chat and perform real-world tasks: reading an email thread and sending a reply, accessing a codebase and deploying an update, or reviewing a design brief and generating a first draft. The protocol creates a foundation for LLMs to connect with external systems, tools, and applications to access data and take actions. This provides:

### Universal compatibility for AI

**AI assistants gain access to thousands of tools** — Once an AI assistant implements MCP (via an MCP client), it can instantly connect to thousands of MCP-compatible applications, from specialized coding tools to enterprise workflow platforms, without building custom integrations for each one.

**Tools and applications connect to every AI assistant at once** — Companies like Notion, Figma, or Asana build a single MCP server that works with any AI assistant that’s compatible (i.e. has implemented an MCP client). Developers only need to build one integration for all AI connections.

### An Open, AI-native ecosystem

**Anyone can build and share** — As an open standard, MCP servers published by developers or companies are compatible with any MCP client. This openness has created a thriving ecosystem of thousands of community-built servers, accelerating the availability of tools and applications for AI assistants..

**Makes software AI-accessible by design** — Traditional software is built for humans using web interfaces. MCP provides a parallel interface designed for AI interaction, allowing applications to become truly AI-native. This means better, more reliable integrations between AI models and the tools people already use.

### A foundational protocol for agents

MCP creates the infrastructure for AI agents to access any number of services and tools, creating true end-to-end task automation. As more applications adopt the protocol, the vision of AI agents that can independently handle complex, multi-step workflows becomes increasingly practical.

## Who is MCP for?

Developers get a standardized way to build integrations once and have them work with any compatible AI. Enterprises gain secure, IT-controlled AI connectivity that scales across their organization. Consumers can connect their favorite tools to AI instantly, with no technical knowledge required.

### For developers: one standard for connecting AI to applications

Developers can follow a single standard to connect external products to your AI applications and agents. This simplifies the process of building integrations, grows the number of available products to connect to, and improves the overall quality and security of connectivity in the ecosystem.

Building an agent that will connect to many applications? Building an application that will connect to many agents? MCP provides you with access to an ecosystem of compatible tools with streamlined integration.

### For enterprises: secure, scalable AI connectivity across your organization

Enterprises can drive internal adoption of AI tools and applications more effectively, as MCP simplifies the process of connecting your systems to AI. This helps make AI more connected within your organization, expanding its capabilities and usefulness for your staff.

### For consumers: instant access to your favorite tools

MCP provides end-users with seamless connectivity between their favorite AI assistants and work tools. It makes it easier to automate tasks and avoid copying and pasting across tabs. In short, MCP gives AI greater access and connectivity to your world.

In [Claude](https://claude.ai), you can instantly connect to MCP Servers, known as [**Connectors**](https://claude.com/partners/mcp). This provides you with a straightforward way to connect Claude to your favorite work apps.

## Connectors (MCP) in action

The real value of MCP becomes clear when you see it in action with the tools you already use. Here are some examples of MCP being used to power integrations in Claude, known as **Connectors**:

### Canva in Claude

The Canva Connector allows Claude to generate new designs directly within Canva. Using MCP, Claude can connect to the tools Canva provides to generate designs on the canvas.

### Notion and Linear in Claude

Using the Notion and Linear Connectors, Claude can access your pages in Notion and use them to update tickets in Linear. Here MCP creates a seamless transfer of unstructured context into organized tickets in a separate project management system.

### Figma in Claude Code

The Figma Connector allows Claude to access designs within Figma. This lets Claude Code create working prototypes of websites, applications, or user interfaces based on designs created in Figma.

### Available Claude Connectors

Claude Connectors include integrations for:

* **Notion** for workspace documentation
* **Linear** for issue tracking
* **Stripe** for payment data
* **Canva** and **Figma** for design assistance
* **Hubspot** for automating CRM tasks
* **Sentry** for error tracking
* ...and many more

Each connector takes just a few seconds to configure to become part of Claude's working context. Outside of Claude, there is an ecosystem of MCP servers on the [open-source MCP Registry](https://modelcontextprotocol.io).

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e948c50eec666207cdd811_2.png)

## Start exploring MCP

Two paths exist based on your needs.

### Connectors in Claude

[Connectors](https://claude.com/partners/mcp) are pre-built, giving Claude instant access to tools, databases, and applications, and providing you with a new set of capabilities. Open [Claude](https://claude.ai/directory), browse available connectors, and click to add them.

### Build custom MCP connections

MCP is open-source, meaning that anyone can adopt MCP to connect AI to applications. The [Model Context Protocol documentation](https://modelcontextprotocol.io) walks through how to build with MCP.

## Getting started

If you want to try MCP, start by browsing for a Claude Connector you can immediately start using with Claude.

If an existing MCP server doesn't already exist, creating your own takes some work, but isn't too complex if you know TypeScript or Python. The [Model Context Protocol quickstart](https://modelcontextprotocol.io/quickstart) has working examples you can modify for your needs.

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

### Is MCP only for Claude?

No. MCP is an open-source protocol. While Claude pioneered adoption of MCP, other AI providers have now adopted the same protocol, allowing anyone to connect to the same ecosystem of MCP servers.

### Do I need programming skills to use MCP?

Not for using [connectors](https://claude.com/partners/mcp). Browse, install, authenticate. That's it. Building custom MCP servers requires TypeScript or Python knowledge, but the growing [connector library](https://claude.com/partners/mcp) covers most mainstream tools.

### How does security work for MCP?

Each server requests specific permissions to allow Claude to access it. You can approve or deny access and revoke permissions at any time.

### What is the performance like for MCP?

MCP uses efficient protocols. Stdio transport for local servers provides minimal overhead. Server-sent events (SSE) and Streamable HTTP for remote servers maintain persistent connections. Response streaming prevents timeouts on large data operations. The protocol supports pagination, filtering, and partial responses to handle large datasets efficiently.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

Mar 5, 2026

### Skills explained: How Skills compares to prompts, Projects, MCP, and subagents

Agents

[Skills explained: How Skills compares to prompts, Projects, MCP, and subagents](#) Skills explained: How Skills compares to prompts, Projects, MCP, and subagents

[Skills explained: How Skills compares to prompts, Projects, MCP, and subagents](/blog/skills-explained) Skills explained: How Skills compares to prompts, Projects, MCP, and subagents

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2319ef2161fcf9ba649_ddad92700787ec1bf1d80359c0c5e6ca305682b0-1000x1000.svg)

Oct 30, 2025

### Building AI agents for financial services

Agents

[Building AI agents for financial services](#)Building AI agents for financial services

[Building AI agents for financial services](/blog/building-ai-agents-in-financial-services)Building AI agents for financial services

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d228c83775fcc75f4e6d_74409af25137110ac04cc39e4d5ea0a2fbcea421-1000x1000.svg)

Oct 30, 2025

### Building AI agents for healthcare and life sciences

Agents

[Building AI agents for healthcare and life sciences](#)Building AI agents for healthcare and life sciences

[Building AI agents for healthcare and life sciences](/blog/building-ai-agents-in-healthcare-and-life-sciences)Building AI agents for healthcare and life sciences

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22f70ecef3c9356822a_928166e443bc1b1f19ebadf4fd11b7c45fce4153-1000x1000.svg)

Nov 19, 2025

### How to create Skills: Key steps, limitations, and examples

Claude Code

[How to create Skills: Key steps, limitations, and examples](#)How to create Skills: Key steps, limitations, and examples

[How to create Skills: Key steps, limitations, and examples](/blog/how-to-create-skills-key-steps-limitations-and-examples)How to create Skills: Key steps, limitations, and examples

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

    

    

    

    

    

    

    

    

    

    

Claude apps

Productivity
