<!-- source: https://claude.com/blog/auto-mode -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225c16d1b0cc3b1ded5_6457c34fbcb012acf0f27f15a6006f700d0f50de-1000x1000.svg)

# Auto mode for Claude Code

Auto mode provides a safer long-running alternative to `--dangerously-skip-permissions`.

  [Claude Code](https://claude.com/blog/category/claude-code)

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Code
* Date

  March 24, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/auto-mode

***Update****: Auto mode is generally available in Claude Code for all users. (July 10, 2026)*

Today, we're introducing auto mode, a new permissions mode in Claude Code where Claude makes permission decisions on your behalf, with safeguards monitoring actions before they run. It's available now as a research preview on the Team plan, and coming to the Enterprise plan and API users in the coming days.

## How it works

Claude Code's default permissions are purposefully conservative: every file write and bash command asks for approval. It’s a safe default, but it means you can't kick off a large task and walk away, since Claude will request frequent human approvals along the way. While some developers choose to bypass permission checks with --dangerously-skip-permissions, skipping permissions can result in dangerous and destructive outcomes and should not be used outside of isolated environments.

Auto mode is a middle path that lets you run longer tasks with fewer interruptions while introducing less risk than skipping all permissions. Before each tool call runs, a classifier reviews it to [check for potentially destructive actions](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default) like mass deleting files, sensitive data exfiltration, or malicious code execution.

Actions that the classifier deems as safe proceed automatically, and risky ones get blocked, redirecting Claude to take a different approach. If Claude insists on taking actions that are continually blocked, it will eventually trigger a permission prompt to the user.

## What to expect

Auto mode reduces risk compared to --dangerously-skip-permissions but doesn't eliminate it entirely, and we continue to recommend using it in isolated environments. The classifier may still allow some risky actions: for example, if user intent is ambiguous, or if Claude doesn't have enough context about your environment to know an action might create additional risk. It may also occasionally block benign actions. We’ll continue to improve the experience over time.

Auto mode may have a small impact on token consumption, cost, and latency for tool calls.

## Getting started

Auto mode is available in Claude Code as a research preview for Claude Team users today, and will roll out to Enterprise and API users in the coming days. It works with both Claude Sonnet 4.6 and Opus 4.6.

* **For admins**: Auto mode will soon be available for all Claude Code users on Enterprise, Team, and Claude API plans. To disable it for the CLI and VS Code extension, set "disableAutoMode": "disable" in your managed settings. Auto mode is disabled by default on the Claude desktop app, and can be toggled on using Organization Settings -> Claude Code.
* **For developers**: Run `claude --enable-auto-mode` to enable auto mode, then cycle to it with Shift+Tab. On Desktop and in the VS Code extension, first toggle auto mode on in Settings -> Claude Code, then select it from the permission mode drop-down in a session.

[Explore the docs](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode) for more information.

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

Get Claude Code

curl -fsSL https://claude.ai/install.sh | bash

Copy command to clipboard

irm https://claude.ai/install.ps1 | iex

Copy command to clipboard

Or read the [documentation](https://code.claude.com/docs/en/overview)

Try Claude Code

[Try Claude Code](https://claude.ai/code)Try Claude Code

Developer docs

[Developer docs](https://code.claude.com/docs/en/overview)Developer docs

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225e31f7aa22c1f28cb_46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

Jul 24, 2026

### Claude models explained: choosing the best model for your use case

Enterprise AI

[Claude models explained: choosing the best model for your use case](#)Claude models explained: choosing the best model for your use case

[Claude models explained: choosing the best model for your use case](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)Claude models explained: choosing the best model for your use case

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d222061abf091318fb82_423062049d4676b41d52b16068cbb5e21603190e-1000x1000.svg)

Jul 24, 2026

### The new rules of context engineering for Claude 5 generation models

Claude Code

[The new rules of context engineering for Claude 5 generation models](#) The new rules of context engineering for Claude 5 generation models

[The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) The new rules of context engineering for Claude 5 generation models

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d231b45c2193efbb0f02_1869137c9d7f2a38b50e804d707e10e85de05ddb-1000x1000.svg)

Jul 23, 2026

### Think through hard problems in voice mode

Product announcements

[Think through hard problems in voice mode](#)Think through hard problems in voice mode

[Think through hard problems in voice mode](https://claude.com/blog/think-through-hard-problems-in-voice-mode)Think through hard problems in voice mode

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d224d39f9b8e905d1823_b68cbb43d7c8f56f0b14cc867e8d4d74445f78b0-1000x1000.svg)

Jul 22, 2026

### Building verification loops in Claude Code with skills

Claude Code

[Building verification loops in Claude Code with skills](#)Building verification loops in Claude Code with skills

[Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)Building verification loops in Claude Code with skills

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

    

    

    

    

    

    

    

    

    

    

Claude Code

Coding
