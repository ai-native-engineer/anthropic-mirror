<!-- source: https://academy.claude.com/courses/claude-101/connecting-your-tools -->

Lesson 8 of 13 · Claude 101Connecting your tools

3. /[Claude 101](https://academy.claude.com/courses/claude-101)

[Claude 101](https://academy.claude.com/courses/claude-101)

# Connecting your tools

Lesson 815 min

In this lessonBy the end, you’ll be able to

* Explain what connectors are and why they matter for your work with Claude
* Navigate the connectors directory and set up your first connection
* Use connected tools effectively in your conversations with Claude

## What are connectors?[](#what-are-connectors)

## Key takeaways[](#key-takeaways)

* **Connectors transform Claude from an assistant into an informed collaborator** by giving Claude access to the same tools, data, and context that you use every day. Instead of starting every conversation from scratch, Claude can work directly with your actual information.
* **Connectors allow Claude to read information and perform actions on your behalf.** Depending on the connector and permissions you grant, Claude can search your files, retrieve documents, analyze data, create new content, update records, and execute tasks across your connected applications—all from within your conversation.
* **The Model Context Protocol (MCP) powers connectors.** Think of MCP like USB-C for AI—a universal standard that allows Claude to connect to many different applications through a single, consistent interface. This open standard means developers can build connectors for any tool, and those connectors work seamlessly with Claude.
* **There are two types of connectors: web connectors and desktop extensions.** Web connectors link Claude to cloud services like Google Drive, Notion, Slack, and Asana. Desktop extensions run locally on your computer through the Claude Desktop app, giving Claude access to local files and native applications.

## Finding and connecting tools[](#finding-and-connecting-tools)

Below is a request Claude can already handle — everything it needs is in the words you typed. Nothing else is connected yet. **Turn on a source and watch the request grow:** each connection lets you ask for something that lives outside your message.

Anthropic maintains a directory of recommended connectors at claude.ai/directory. The directory is organized into two tabs:

* **Web:** Cloud services and applications (Gmail, Notion, Slack, Asana, Linear, Stripe, and many more)
* **Desktop extensions:** Local tools that run on your computer through the Claude Desktop app

The directory lists connectors rather than individual applications, so one entry can cover several related tools. The Atlassian Rovo connector, for example, reaches both Jira and Confluence, so look for Atlassian rather than either app by name. If a tool you need doesn't have its own entry, you can add it as a custom connector instead.

To browse available connectors, you can also click the **+** button in the lower left of the chat window, then select **Connectors**.

### Setting up a web connector[](#setting-up-a-web-connector)

Here's how to connect a cloud service:

1. **Find the connector:** Navigate to claude.ai/directory, or click **+** > **Connectors** in any chat
2. **Click Connect:** Select the connector you want to add
3. **Authenticate:** You'll be redirected to the service's login page. Sign in with your existing credentials
4. **Grant permissions:** Review the specific permissions Claude is requesting, then authorize access
5. **Test the connection:** Return to Claude and try a simple request, like "Can you access my [tool name]?"

Once connected, Claude can search, read, and in some cases take actions within that service—depending on the permissions you've granted.

### Desktop extensions[](#desktop-extensions)

Desktop extensions require the Claude Desktop app rather than the web interface. These extensions let Claude interact with local applications, your file system, and native features on macOS or Windows.

Some desktop extensions include:

* Local file access for reading and organizing documents
* Browser control for automated web tasks
* Native application integration (like Figma for design work)

To install a desktop extension:

1. Download and install the [Claude Desktop app(opens in new tab)](https://claude.ai/download)
2. Open the app and navigate to Settings > Extensions
3. Browse available extensions and click Install
4. Follow any additional setup steps specific to that extension

## Using connectors in your work[](#using-connectors-in-your-work)

Once you've connected your tools, Claude considers them when responding to your requests. Here are some practical ways to use connected tools:

**Project management (Asana, Linear, Jira)**

* “What are my highest priority tasks due this week?”
* “Create a new task for reviewing the Q4 budget proposal”
* “Summarize the status of our product launch project”

**Communication (Slack, Gmail)**

* “Find the email thread where we discussed the vendor contract”
* “Draft a reply to the latest message in the #marketing channel”
* “What did the team decide about the timeline in yesterday's discussion?”

**Documentation (Notion, Google Drive, Confluence)**

* “Search our documentation for our brand voice guidelines”
* “Summarize the meeting notes from last week's product review”
* “What does our style guide say about using contractions?”

**Business tools (Stripe, PayPal, HubSpot)**

* “Show me revenue trends for the past quarter”
* “What's the status of the Acme Corp opportunity?”
* “List recent transactions over $1,000”

## Security and permissions[](#security-and-permissions)

When you connect Claude to external services, you're granting it access to read—and sometimes modify—data within those services. Here are some important considerations:

* **Scoped access:** Permissions are specific to what the connector needs and you can toggle individual permissions on and off within each application's menu.
* **Claude sees what you see:** Claude can only access data *you* have access to. Connecting your work email doesn't give Claude access to your CEO's inbox—only your own.
* **Revocable at any time:** You can disconnect a service through Claude's settings or through the third-party service's security settings. Just as with Skills, you can also find or build custom connectors. Exercise the same caution — only install connectors from trusted sources.

## Lesson reflection[](#lesson-reflection)

Before moving on, consider:

* Which of your daily work tools would be most valuable to connect to Claude?
* What tasks currently require you to copy and paste information that connectors could handle automatically?
* Are there workflows where combining data from multiple connected sources would save you significant time?

## What's next[](#whats-next)

In the next lesson, you'll learn about Enterprise Search—a specialized feature for Claude for Work users that connects Claude to your organization's knowledge sources with custom prompts optimized for your company's context.

For more information on connectors and the Model Context Protocol, visit the [Anthropic Help Center(opens in new tab)](https://support.claude.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp) or explore the connector directory at claude.ai/directory.

[Previous lessonWorking with skills](https://academy.claude.com/courses/claude-101/working-with-skills)[Next lessonEnterprise search](https://academy.claude.com/courses/claude-101/enterprise-search)

Lesson 8 of 13 · Claude 101Connecting your tools

Meet Claude

* [What is Claude?](https://academy.claude.com/courses/claude-101/what-is-claude)
* [Your first conversation with Claude](https://academy.claude.com/courses/claude-101/your-first-conversation-with-claude)
* [Getting better results](https://academy.claude.com/courses/claude-101/getting-better-results)
* [How you'll work with Claude on your desktop](https://academy.claude.com/courses/claude-101/claude-desktop-app-chat-cowork-code)

Organizing your work and knowledge

* [Introduction to projects](https://academy.claude.com/courses/claude-101/introduction-to-projects)
* [Creating with artifacts](https://academy.claude.com/courses/claude-101/creating-with-artifacts)
* [Working with skills](https://academy.claude.com/courses/claude-101/working-with-skills)

Expanding Claude's reach

* [Connecting your tools](https://academy.claude.com/courses/claude-101/connecting-your-tools)
* [Enterprise search](https://academy.claude.com/courses/claude-101/enterprise-search)
* [Research for deep dives](https://academy.claude.com/courses/claude-101/research-mode-for-deep-dives)

Putting it all together

* [Claude in action: use-cases by role](https://academy.claude.com/courses/claude-101/claude-in-action-use-cases-by-role)
* [Other ways to work with Claude](https://academy.claude.com/courses/claude-101/other-ways-to-work-with-claude)

Conclusion & badge

* [What's next?](https://academy.claude.com/courses/claude-101/what-s-next)
* [Course quizQuiz](https://academy.claude.com/courses/claude-101/certificate-of-completion)

* [Completion badge](https://academy.claude.com/courses/claude-101/badge)

* [What are connectors?](#what-are-connectors)
* [Key takeaways](#key-takeaways)
* [Finding and connecting tools](#finding-and-connecting-tools)
* [Using connectors in your work](#using-connectors-in-your-work)
* [Security and permissions](#security-and-permissions)
* [Lesson reflection](#lesson-reflection)
* [What's next](#whats-next)
