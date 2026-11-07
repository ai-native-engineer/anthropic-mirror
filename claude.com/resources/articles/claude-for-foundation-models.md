<!-- source: https://claude.com/resources/articles/claude-for-foundation-models -->

Today we're releasing Foundation Models framework support for Claude through a new Swift package that lets Apple developers use Apple's Foundation Models framework to call Claude for more complex workflows.

![](https://assets.claude.com/2c536ac9545ae24001d8f6d0ce604702e7f27eee.png)

Apple’s Foundation Models framework gives developers access to tap into models natively from Swift. It is very easy to use and can return typed Swift values through guided generation in as few as three lines of code. Developers can use this to tap into Apple’s on-device models for fast, local tasks like summarization or extraction.

Developers can now use Apple’s Foundation Models framework to hand off to Claude when a request calls for multi-step reasoning, code generation, and more. Claude can also search the web for current information and execute code for data analysis. Stream Claude's response back into the same view.

Because Apple's framework returns typed Swift values from @Generable annotations, developers arrive at the Claude API call with clean inputs instead of raw user text.

## What this unlocks

The Foundation Models framework already powers a range of intelligent on-device features — journaling apps that surface personalized prompts, document apps that summarize contracts, learning apps that explain a concept at a student's level. Adding Claude extends each of those patterns.

![](https://assets.claude.com/1fe4afefb5a24989001f5b36f9a211f597442586.png)

A journaling app can generate daily prompts on-device, then ask Claude to find threads across months of entries. A study app can define a term on-device, then hand off to Claude when the student follows up with "why does this matter for everything else we've covered?"

It's one experience for the user, backed by the right model for each step.

## Getting started

Claude support with the Foundation Models framework will be available tomorrow and works through Apple's Foundation Models framework on iOS 27, iPadOS 27, macOS 27, and visionOS 27, and watch OS 27. Add it to your project, sign in with an Anthropic API key, and pass typed outputs from Apple's on-device pass into a Claude request — the package handles streaming, tool calls, and structured responses back into your SwiftUI view.

[ArticleNov 5, 2026

### Introducing Personal Finance in Claude

Ask Claude about your money and get straight answers from the accounts you connect.](https://claude.com/resources/articles/introducing-personal-finance-in-claude)[ArticleNov 5, 2026

### More visibility and control over Claude Enterprise for security teams

Claude EnterpriseClaude apps](https://claude.com/resources/articles/claude-enterprise-security-updates)[ArticleNov 4, 2026

### New agents and products for security, productivity, and creative work on Claude Marketplace](https://claude.com/resources/articles/new-agents-and-products-claude-marketplace)[ArticleNov 2, 2026

### Make long-running agents faster with message threads

New in the Messages API, send your conversation once, and the API receives only what’s new with every turn.

Claude Platform](https://claude.com/resources/articles/message-threads)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
