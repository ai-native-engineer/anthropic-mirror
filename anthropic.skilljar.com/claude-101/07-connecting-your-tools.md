<!-- https://anthropic.skilljar.com/claude-101/383397 -->

## What you'll learn

*Estimated time: 16 minutes*

By the end of this lesson you'll be able to:

* Explain what connectors are and why they matter for your work with Claude
* Navigate the connectors directory and set up your first connection
* Use connected tools effectively in your conversations with Claude

## What are connectors?

## Key takeaways

* **Connectors transform Claude from an assistant into an informed collaborator** by giving Claude access to the same tools, data, and context that you use every day. Instead of starting every conversation from scratch, Claude can work directly with your actual information.
* **Connectors allow Claude to read information and perform actions on your behalf.** Depending on the connector and permissions you grant, Claude can search your files, retrieve documents, analyze data, create new content, update records, and execute tasks across your connected applications—all from within your conversation.
* **The Model Context Protocol (MCP) powers connectors.** Think of MCP like USB-C for AI—a universal standard that allows Claude to connect to many different applications through a single, consistent interface. This open standard means developers can build connectors for any tool, and those connectors work seamlessly with Claude.
* **There are two types of connectors: web connectors and desktop extensions.** Web connectors link Claude to cloud services like Google Drive, Notion, Slack, and Asana. Desktop extensions run locally on your computer through the Claude Desktop app, giving Claude access to local files and native applications.

## Finding and connecting tools

Below is a request Claude can already handle — everything it needs is in the words you typed. Nothing else is connected yet. **Turn on a source and watch the request grow:** each connection lets you ask for something that lives outside your message.

Anthropic maintains a directory of recommended connectors at claude.ai/directory. The directory is organized into two tabs:

* **Web:** Cloud services and applications (Gmail, Notion, Slack, Asana, Linear, Stripe, and many more)
* **Desktop extensions:** Local tools that run on your computer through the Claude Desktop app

The directory lists connectors rather than individual applications, so one entry can cover several related tools. The Atlassian Rovo connector, for example, reaches both Jira and Confluence, so look for Atlassian rather than either app by name. If a tool you need doesn't have its own entry, you can add it as a custom connector instead.

To browse available connectors, you can also click the **+** button in the lower left of the chat window, then select **Connectors**.

### Setting up a web connector

Here's how to connect a cloud service:

1. **Find the connector:** Navigate to claude.ai/directory, or click **+** > **Connectors** in any chat
2. **Click Connect:** Select the connector you want to add
3. **Authenticate:** You'll be redirected to the service's login page. Sign in with your existing credentials
4. **Grant permissions:** Review the specific permissions Claude is requesting, then authorize access
5. **Test the connection:** Return to Claude and try a simple request, like "Can you access my [tool name]?"

Once connected, Claude can search, read, and in some cases take actions within that service—depending on the permissions you've granted.

### Desktop extensions

Desktop extensions require the Claude Desktop app rather than the web interface. These extensions let Claude interact with local applications, your file system, and native features on macOS or Windows.

Some desktop extensions include:

* Local file access for reading and organizing documents
* Browser control for automated web tasks
* Native application integration (like Figma for design work)

To install a desktop extension:

1. Download and install the [Claude Desktop app](https://claude.ai/download)
2. Open the app and navigate to Settings > Extensions
3. Browse available extensions and click Install
4. Follow any additional setup steps specific to that extension

## Using connectors in your work

Once you've connected your tools, Claude considers them when responding to your requests. Here are some practical ways to use connected tools:

**Project management (Asana, Linear, Jira)**

* “What are my highest priority tasks due this week?”[Open in Claude](https://claude.ai/new?q=What%20are%20my%20highest%20priority%20tasks%20due%20this%20week%3F)
* “Create a new task for reviewing the Q4 budget proposal”[Open in Claude](https://claude.ai/new?q=Create%20a%20new%20task%20for%20reviewing%20the%20Q4%20budget%20proposal)
* “Summarize the status of our product launch project”[Open in Claude](https://claude.ai/new?q=Summarize%20the%20status%20of%20our%20product%20launch%20project)

**Communication (Slack, Gmail)**

* “Find the email thread where we discussed the vendor contract”[Open in Claude](https://claude.ai/new?q=Find%20the%20email%20thread%20where%20we%20discussed%20the%20vendor%20contract)
* “Draft a reply to the latest message in the #marketing channel”[Open in Claude](https://claude.ai/new?q=Draft%20a%20reply%20to%20the%20latest%20message%20in%20the%20%23marketing%20channel)
* “What did the team decide about the timeline in yesterday's discussion?”[Open in Claude](https://claude.ai/new?q=What%20did%20the%20team%20decide%20about%20the%20timeline%20in%20yesterday's%20discussion%3F)

**Documentation (Notion, Google Drive, Confluence)**

* “Search our documentation for our brand voice guidelines”[Open in Claude](https://claude.ai/new?q=Search%20our%20documentation%20for%20our%20brand%20voice%20guidelines)
* “Summarize the meeting notes from last week's product review”[Open in Claude](https://claude.ai/new?q=Summarize%20the%20meeting%20notes%20from%20last%20week's%20product%20review)
* “What does our style guide say about using contractions?”[Open in Claude](https://claude.ai/new?q=What%20does%20our%20style%20guide%20say%20about%20using%20contractions%3F)

**Business tools (Stripe, PayPal, HubSpot)**

* “Show me revenue trends for the past quarter”[Open in Claude](https://claude.ai/new?q=Show%20me%20revenue%20trends%20for%20the%20past%20quarter)
* “What's the status of the Acme Corp opportunity?”[Open in Claude](https://claude.ai/new?q=What's%20the%20status%20of%20the%20Acme%20Corp%20opportunity%3F)
* “List recent transactions over $1,000”[Open in Claude](https://claude.ai/new?q=List%20recent%20transactions%20over%20%241%2C000)

## Security and permissions

When you connect Claude to external services, you're granting it access to read—and sometimes modify—data within those services. Here are some important considerations:

* **Scoped access:** Permissions are specific to what the connector needs and you can toggle individual permissions on and off within each application's menu.
* **Claude sees what you see:** Claude can only access data *you* have access to. Connecting your work email doesn't give Claude access to your CEO's inbox—only your own.
* **Revocable at any time:** You can disconnect a service through Claude's settings or through the third-party service's security settings. Just as with Skills, you can also find or build custom connectors. Exercise the same caution — only install connectors from trusted sources.

## Lesson reflection

Before moving on, consider:

* Which of your daily work tools would be most valuable to connect to Claude?
* What tasks currently require you to copy and paste information that connectors could handle automatically?
* Are there workflows where combining data from multiple connected sources would save you significant time?

## What's next

In the next lesson, you'll learn about Enterprise Search—a specialized feature for Claude for Work users that connects Claude to your organization's knowledge sources with custom prompts optimized for your company's context.

For more information on connectors and the Model Context Protocol, visit the [Anthropic Help Center](https://support.claude.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp) or explore the connector directory at claude.ai/directory.
