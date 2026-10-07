<!-- source: https://claude.com/resources/articles/computer-use-skills-api-files-api -->

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

![Asteroid](https://assets.claude.com/20b0b49c00d64218f9441a26dc9a504dc09b4c7e.svg)

> “Our agents work inside healthcare and insurance systems that have no API. On the new computer use tool, our longest claims workflow went from 32 minutes to 13, cost per task fell about 30% across every workflow we tested, and completion hit 100%, with no changes to our prompts.”

Davide Locatelli, Research Engineer

![Box](https://assets.claude.com/f7051ef3388f6fcd83051cffcba21499a021e446.svg)

> “The Skills API gave us a straightforward way to build specialized document creation into Box Agent. For a bank, a skill captures the firm's credit methodology and approved memo format; Box Agent applies it to the financial statements and deal documents already in Box and produces a source-grounded credit memo for analyst review. Banks get agents for complex workflows without building each one from scratch.”

Matthew Midson, Managing Director of Banking

### **Getting started**

The computer use tool, the browser use tool, the Skills API, and the Files API are now available on the Claude Platform. The Skills API and the Files API are also available through Microsoft Foundry, and the updated computer use and browser use tools are coming soon to Google Cloud's Vertex AI. Existing beta integrations keep working while you migrate. See the documentation for [computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool), the [browser use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool), the [Skills API](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), and the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) to get started.

[ArticleOct 1, 2026

### Customize Claude Code with mods

Change how Claude Code behaves and looks with a few lines of TypeScript.

Claude Code](https://claude.com/resources/articles/claude-code-mods)[ArticleSep 30, 2026

### Claude for Government is now generally available

Claude Code CLI and Claude for Microsoft 365 also now available in early access.](https://claude.com/resources/articles/claude-for-government-is-now-generally-available)[ArticleSep 25, 2026

### Build plugins for Claude

You can now submit plugins to the Claude directory through a new developer portal, track them through review, and see usage analytics once they’re live.

Claude apps](https://claude.com/resources/articles/build-plugins-for-claude)[ArticleSep 24, 2026

### Claude Tag now supports personal connectors in channels

Claude Tag can now use your connectors for requests you make in a channel. Nobody else can use them, and you're in control of how to present the output.

Claude Tag](https://claude.com/resources/articles/claude-tag-now-supports-personal-connectors-in-channels)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
