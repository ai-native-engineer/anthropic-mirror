<!-- source: https://claude.com/resources/articles/claude-code-on-the-web -->

***Update:** Cloud sessions (previously known as Claude Code on the web) are now generally available for Pro, Max, and Team users, and for Enterprise users with premium seats or Chat + Claude Code seats. Read the [docs](https://code.claude.com/docs/en/claude-code-on-the-web) for the latest information. September 23, 2026.*

Today, we're introducing Claude Code on the web, a new way to delegate coding tasks directly from your browser.

Now in beta as a research preview, you can assign multiple coding tasks to Claude that run on Anthropic-managed cloud infrastructure, perfect for tackling bug backlogs, routine fixes, or parallel development work.

## Run coding tasks in parallel

Claude Code on the web lets you kick off coding sessions without opening your terminal. Connect your GitHub repositories, describe what you need, and Claude handles the implementation.

Each session runs in its own isolated environment with real-time progress tracking, and you can actively steer Claude to adjust course as it’s working through tasks.

With Claude Code running in the cloud, you can now **run multiple tasks in parallel** across different repositories from a single interface and **ship faster** with automatic PR creation and clear change summaries.

## Flexible for every workflow

The web interface complements your existing Claude Code workflow. Running tasks in the cloud is especially effective for:

* Answering questions about how projects work and how repositories are mapped
* Bugfixes and routine, well-defined tasks
* Backend changes, where Claude Code can use test-driven development to verify changes

You can also use Claude Code on mobile. As part of this research preview, we’re making Claude Code available on our iOS app so developers can explore coding with Claude on the go. It’s an early preview, and we hope to quickly refine the mobile experience based on your feedback.

## Security-first cloud execution

Every Claude Code task runs in an isolated sandbox environment with network and filesystem restrictions. Git interactions are handled through a secure proxy service that ensures Claude can only access authorized repositories—helping keep your code and credentials protected throughout the entire workflow.

You can also add custom network configuration to choose what domains Claude Code can connect to from its sandbox. For example, you can allow Claude to download npm packages over the internet so that it can run tests and validate changes.

Read our [engineering blog](https://www.anthropic.com/engineering/claude-code-sandboxing) and [documentation](https://docs.claude.com/en/docs/claude-code/sandboxing) for a deep dive on Claude Code’s sandboxing approach.

## Getting started

Claude Code on the web is available now in research preview for Pro and Max users. Visit [claude.com/code](http://claude.com/code) to connect your first repository and start delegating tasks.

Cloud-based sessions share rate limits with all other Claude Code usage. [Explore our documentation](https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web) to learn more.

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
