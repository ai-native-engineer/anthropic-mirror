<!-- source: https://claude.com/blog/computer-use-skills-api-files-api -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

# Build production agents with computer use, the Skills API, and the Files API

* Category

  [Product announcements](https://claude.com/blog/category/announcements)

  [Agents](https://claude.com/blog/category/agents)

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)
* Product

  [Claude Platform](https://claude.com/platform/api)
* Date

  August 20, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/computer-use-skills-api-files-api

Computer use, the Skills API, and the Files API are generally available on the Claude Platform today. Computer use also adds a new browser use tool for agents that work in web applications. Together they let you build agents that operate software, apply your team's expertise, and return finished files.

### **Building agents on the Claude Platform**

**Computer use** lets you build agents that operate software they can see. Given a screenshot, the agent clicks, types, and scrolls the way someone at the keyboard would. That lets it work in applications that were never built for automation. The new **browser use tool** extends this to the web. Alongside the screenshot, the agent reads the structure of the page and acts on a specific field or button rather than a position on screen.

The **Skills API** and the **Files API** let you give that agent your expertise and your documents. A skill is a folder of instructions, scripts, and templates that Claude loads only when a task calls for it. With the **Skills API** you upload and version your own skills, then attach them to any request. They run in Claude's code execution sandbox, so there is nothing for you to host. The **Files API** is storage for the documents an agent reads and writes: upload a PDF or spreadsheet once, reference it by ID in later requests instead of re-sending it, and download the files the agent creates.

Say you're building a claims agent. It reads the intake document from the Files API, follows a skill that encodes the team's filing procedure, completes the submission in an insurer's web portal with the browser use tool, and saves the confirmation back as a file. Code execution and web search, already generally available, fit into the same loop.

### **What's new with general availability**

* **Computer use:** the updated computer use tool lets Claude take several actions per turn instead of one per model call, so tasks finish in fewer calls and less time. Computer use is also now eligible for HIPAA-regulated workloads under our BAA.
* **Browser use tool:** new in computer use today. It uses the same multi-action turns and adds page structure, so agents target web elements more reliably than with pixels alone.
* **Skills API:** a simpler API for uploading and versioning your own skills.
* **Files API:** automatic file expiration, 5x higher rate limits, and 1 TB of storage per organization.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a84d86b69e80750cfefc646_Asteroid_Logo_Black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a84d83ff9fbb0abe47899c7_Asteroid_Logo_White.svg)

"Our agents work inside healthcare and insurance systems that have no API. On the new computer use tool, our longest claims workflow went from 32 minutes to 13, cost per task fell about 30% across every workflow we tested, and completion hit 100%, with no changes to our prompts."

Davide Locatelli, Research Engineer

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8c287936531790c85c4_box_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8bdc1ea299a1a768655_box_dark.svg)

"The Skills API gave us a straightforward way to build specialized document creation into Box Agent. For a bank, a skill captures the firm's credit methodology and approved memo format; Box Agent applies it to the financial statements and deal documents already in Box and produces a source-grounded credit memo for analyst review. Banks get agents for complex workflows without building each one from scratch."

Matthew Midson, Managing Director of Banking

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

### **Getting started**

The computer use tool, the browser use tool, the Skills API, and the Files API are now available on the Claude Platform. The Skills API and the Files API are also available through Microsoft Foundry, and the updated computer use and browser use tools are coming soon to Google Cloud's Vertex AI. Existing beta integrations keep working while you migrate. See the documentation for [computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool), the [browser use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool), the [Skills API](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), and the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) to get started.

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Aug 21, 2026

### Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders

Product announcements

[Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders](#)Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders

[Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders)Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

Aug 13, 2026

### Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

Agents

[Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions](#)Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

[Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions](https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions)Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

Jul 24, 2026

### The new rules of context engineering for Claude 5 generation models

Claude Code

[The new rules of context engineering for Claude 5 generation models](#) The new rules of context engineering for Claude 5 generation models

[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) The new rules of context engineering for Claude 5 generation models

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d222061abf091318fb82_423062049d4676b41d52b16068cbb5e21603190e-1000x1000.svg)

Aug 21, 2026

### The AI-Native SDLC playbook

Enterprise AI

[The AI-Native SDLC playbook](#)The AI-Native SDLC playbook

[The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)The AI-Native SDLC playbook

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
