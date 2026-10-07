<!-- source: https://claude.com/resources/articles/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous -->

To help address this, we’ve introduced two new features in Claude Code built on top of sandboxing, both of which are designed to provide a more secure place for developers to work, while also allowing Claude to run more autonomously and with fewer permission prompts. ByThese features are examples of **native sandboxing**: defining set boundaries within which Claude can work freely, they increase security and agency..

## Our current approach to keeping users secure

Claude Code runs on a permission-based model: by default, it's read-only, which means it asks for permission before making modifications or running any commands. There are some exceptions to this: we use static analysis to auto-allow safe commands like echo or cat, but most operations still need explicit approval.

But constantly clicking "approve" slows down development and can lead to ‘approval fatigue’, where users might not pay close attention to what they're approving. To make Claude Code both safer and more effective, we wanted to find a better method.

## Sandboxing: a safer and more autonomous approach

Sandboxing creates pre-defined boundaries within which Claude can work more freely, instead of asking for permission for each action.

With our update to Claude Code, we’re shifting to this approach. We’re building Our approach to sandboxing is built on top of operating system-level features to enable two new features, each of which are based on the followingtwo sets of boundariesmain things:

1. **Filesystem isolation**, which ensures that Claude can only access or modify specific directories. This is particularly important in preventing a prompt-injected Claude from modifying sensitive system files.
2. **Network isolation**, which ensures that Claude can only connect to approved servers. This prevents a prompt-injected Claude from leaking sensitive information or downloading malware.

It is worth noting that effective sandboxing requires *both* filesystem and network isolation. Without network isolation, a compromised agent could exfiltrate sensitive files like SSH keys; without filesystem isolation, a compromised agent could easily escape the sandbox and gain network access. It’s by using both techniques that we can provide a safer agentic experience for Claude Code users.

### Two new sandboxing features in Claude Code

#### Sandboxed bash tool: safe bash execution without permission prompts

Today, We're introducing a new sandbox runtime, available in research preview, that lets you define exactly which directories and network hosts your agent can access, without the overhead of spinning up and managing a container. This can be used to sandbox arbitrary processes, agents and MCP servers. It is now available as an open source research preview here: [Github link?]

In Claude Code, we use this runtime to sandbox the bash tool, which allows Claude to run commands within the defined limits you set. These commands are safer by default, they require fewer user permission prompts, so Claude can run more autonomously. If Claude tries to access something *outside* of the sandbox, you'll be notified immediately, and can choose whether or not to allow it.

We’ve built this on top of OS level primitives such as [Linux bubblewrap](https://github.com/containers/bubblewrap) and MacOS seatbelt to enforce these restrictions at the OS level. They cover not just Claude Code's direct interactions, but also any scripts, programs, or subprocesses that are spawned by the command.

As described above, this sandbox enforces both:

1. **Filesystem isolation,** by allowing read and write access to the current working directory, but blocking the modification of any files outside of it.
2. **Network isolation,** by only allowing internet access through a unix domain socket connected to a proxy server running outside the sandbox. This proxy server enforces restrictions on the domains that a process can connect to, and handles user confirmation for newly requested domains. IAnd if you’d like further-increased security, we alsoeven support customizing this proxy to enforce arbitrary rules on outgoing traffic.

‍

Both components are configurable: you can easily choose to allow or disallow specific file paths or domains.

![](https://assets.claude.com/957f5aaf1b2662b9ac5fe25815f0a8491f8966ff.png)

Sandboxing ensures that even a successful prompt injection is fully isolated, and cannot impact overall user security. This way, a compromised Claude Code can't steal your SSH keys, or phone home to an attacker's server.

To get started with this feature, run: `claude --sandbox`, and read more technical details about our security model here.

To make it easier for other teams to build safer agents, we have open sourced [XXX]. We believe that other AI companies should consider adopting this technology for their own agents in order to enhance the security posture of their agents.

#### Claude Code on the web: running Claude Code securely in the cloud

Today, we're also releasing [Claude Code on the web](https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web), enabling users to run Claude Code in an isolated sandbox in the cloud. Claude Code on the web executes each Claude Code session in an isolated sandbox where it has full access to its server in a safe and secure way. We've designed this sandbox to ensure that sensitive credentials (such as git credentials or signing keys) are never inside the sandbox with Claude Codenever enter the sandbox environment. This way, even if the code running in the sandbox is compromised, the user is kept safe from further harm.

Claude Code on the web uses a custom proxy service that transparently handles all git interactions. Inside the sandbox, the git client authenticates to this service with a custom-built scoped credential. The proxy verifies this credential and the contents of the git interaction (e.g. ensuring it is only pushing to the configured branch), then attaches the right authentication token before sending the request to GitHub.

![](https://assets.claude.com/bb8f554ea106223c996c309677b3eb2950d45f01.png)

## Getting started

Our new sandboxed bash tool and Claude Code on the web offer substantial improvements in both security and productivity for developers using Claude for their engineering work.

To get started with these tools:

1. Run `claude --sandbox` and check out [our docs](https://docs.claude.com/en/docs/claude-code/sandboxing) on how to configure this sandbox.
2. Go to [claude.com/code](http://claude.ai/code) to try out Claude Code on the web.

‍

Or, if you're building your own agents, check out our open-sourced sandboxing code, and consider integrating it into your work. We look forward to seeing what you build.

## FAQ

How do I use Claude Code?

To start using Claude Code, you need to set up an API key and follow the documentation provided. This will guide you through the process of making requests and handling responses effectively.

What are the application areas for Claude?

From chatbots to automated content generation, Claude's versatility makes it a valuable tool for businesses and developers alike.

How does Claude improve over time?

User feedback plays a crucial role in Claude's improvement. By analyzing user interactions, developers can identify areas for enhancement and implement necessary changes.

[ArticleSep 24, 2026

### Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind.

Our latest Opus model is priced and trained to optimize costs for how developers code now.

Claude CodeClaude Enterprise](https://claude.com/resources/articles/claude-opus-5-5-built-for-coding-sessions-that-use-more-context)[ArticleSep 14, 2026

### Agentic coding is straining CI. Here’s how we scaled test impact analysis at Anthropic

Our CI job volume increased 25x over 6 months. We patched our test selection service three times before finding a sustainable solution.

Claude CodeClaude Enterprise1 more: Claude TagClaude Tag](https://claude.com/resources/articles/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)[ArticleAug 24, 2026

### How an Anthropic field marketer uses Claude Code to send weekly personalized updates to every sales rep

Adam Ward, on Anthropic’s marketing team, shares how he uses Claude to turn one weekly sales report into a personalized Monday briefing for every account executive he supports.

Claude Code](https://claude.com/resources/articles/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep)[ArticleAug 20, 2026

### The Claude Code guide for startups

How fast-growing startups use Claude Code to ship—five operating principles drawn from interviews with more than a dozen companies.

Claude Code](https://claude.com/resources/articles/claude-code-guide-for-startups)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
