<!-- source: https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous -->

Introducing Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/68c469d2d09b203c164ad8e6_og-claude-education.jpg)

See Claude Code in action—from concept to commit in one seamless workflow.

Read more

[Read more](https://claude.com/product/claude-code)Read more

Introducing Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b862e6ee6520aee5bc0741_vid-placeholder.avif)

[Next](#)Next

See Claude Code in action—from concept to commit in one seamless workflow.

Read more

[Read more](https://claude.com/product/claude-code)Read more

[Next](#)Next

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b862e6ee6520aee5bc0741_vid-placeholder.avif)

Introducing Claude Code

See Claude Code in action—from concept to commit in one seamless workflow.

Read more

[Read more](https://claude.com/product/claude-code)Read more

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

# Beyond permission prompts: making Claude Code more secure and autonomous

In Claude Code, Claude writes, tests, and debugs code alongside you, navigating your codebase, editing multiple files, and running commands to verify its work. Giving Claude this much access to your codebase and files can introduce risks, especially in the case of prompt injection, such as Claude deleting files you didn't intend.

  [Claude Code](https://claude.com/blog/category/claude-code)
* Product

  Claude Code
* Date

  October 8, 2025
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous

To help address this, we’ve introduced two new features in Claude Code built on top of sandboxing, both of which are designed to provide a more secure place for developers to work, while also allowing Claude to run more autonomously and with fewer permission prompts. ByThese features are examples of **native sandboxing**: defining set boundaries within which Claude can work freely, they increase security and agency..

## Our current approach to keeping users secure

Claude Code runs on a permission-based model: by default, it's read-only, which means it asks for permission before making modifications or running any commands. There are some exceptions to this: we use static analysis to auto-allow safe commands like echo or cat, but most operations still need explicit approval.

But constantly clicking "approve" slows down development and can lead to ‘approval fatigue’, where users might not pay close attention to what they're approving. To make Claude Code both safer and more effective, we wanted to find a better method.

## Sandboxing: a safer and more autonomous approach

Sandboxing creates pre-defined boundaries within which Claude can work more freely, instead of asking for permission for each action.

With our update to Claude Code, we’re shifting to this approach. We’re building Our approach to sandboxing is built on top of operating system-level features to enable two new features, each of which are based on the followingtwo sets of boundariesmain things:

1. **Filesystem isolation**,which ensures that Claude can only access or modify specific directories. This is particularly important in preventing a prompt-injected Claude from modifying sensitive system files.
2. **Network isolation**,which ensures that Claude can only connect to approved servers. This prevents a prompt-injected Claude from leaking sensitive information or downloading malware.

It is worth noting that effective sandboxing requires *both* filesystem and network isolation. Without network isolation, a compromised agent could exfiltrate sensitive files like SSH keys; without filesystem isolation, a compromised agent could easily escape the sandbox and gain network access. It’s by using both techniques that we can provide a safer agentic experience for Claude Code users.

### Two new sandboxing features in Claude Code

#### Sandboxed bash tool: safe bash execution without permission prompts

Today, We're introducing a new sandbox runtime, available in research preview, that lets you define exactly which directories and network hosts your agent can access, without the overhead of spinning up and managing a container. This can be used to sandbox arbitrary processes, agents and MCP servers. It is now available as an open source research preview here:  [Github link?]  
  
In Claude Code, we use this runtime to sandbox the bash tool, which allows Claude to run commands within the defined limits you set. These commands are safer by default, they require fewer user permission prompts, so Claude can run more autonomously. If Claude tries to access something *outside* of the sandbox, you'll be notified immediately, and can choose whether or not to allow it.

We’ve built this on top of OS level primitives such as [Linux bubblewrap](https://github.com/containers/bubblewrap) and MacOS seatbelt to enforce these restrictions at the OS level. They cover not just Claude Code's direct interactions, but also any scripts, programs, or subprocesses that are spawned by the command.  
  
As described above, this sandbox enforces both:

1. **Filesystem isolation,** by allowing read and write access to the current working directory, but blocking the modification of any files outside of it.
2. **Network isolation,** by only allowing internet access through a unix domain socket connected to a proxy server running outside the sandbox. This proxy server enforces restrictions on the domains that a process can connect to, and handles user confirmation for newly requested domains. IAnd if you’d like further-increased security, we alsoeven support customizing this proxy to enforce arbitrary rules on outgoing traffic.

‍

Both components are configurable: you can easily choose to allow or disallow specific file paths or domains.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e6c0f6e8c717994091347a_60aa4f4b.png)

Sandboxing ensures that even a successful prompt injection is fully isolated, and cannot impact overall user security. This way, a compromised Claude Code can't steal your SSH keys, or phone home to an attacker's server.

To get started with this feature, run: `claude --sandbox`, and read more technical details about our security model here.

To make it easier for other teams to build safer agents, we have open sourced [XXX]. We believe that other AI companies should consider adopting this technology for their own agents in order to enhance the security posture of their agents.

#### Claude Code on the web: running Claude Code securely in the cloud

Today, we're also releasing [Claude Code on the web](https://docs.claude.com/en/docs/claude-code/claude-code-on-the-web), enabling users to run Claude Code in an isolated sandbox in the cloud. Claude Code on the web executes each Claude Code session in an isolated sandbox where it has full access to its server in a safe and secure way. We've designed this sandbox to ensure that sensitive credentials (such as git credentials or signing keys) are never inside the sandbox with Claude Codenever enter the sandbox environment. This way, even if the code running in the sandbox is compromised, the user is kept safe from further harm.

Claude Code on the web uses a custom proxy service that transparently handles all git interactions. Inside the sandbox, the git client authenticates to this service with a custom-built scoped credential. The proxy verifies this credential and the contents of the git interaction (e.g. ensuring it is only pushing to the configured branch), then attaches the right authentication token before sending the request to GitHub.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e6c0f6e8c717994091347d_7b19e1a8.png)

## Getting started

Our new sandboxed bash tool and Claude Code on the web offer substantial improvements in both security and productivity for developers using Claude for their engineering work.

To get started with these tools:

1. Run `claude --sandbox` and check out [our docs](https://docs.claude.com/en/docs/claude-code/sandboxing) on how to configure this sandbox.
2. Go to [claude.com/code](http://claude.ai/code) to try out Claude Code on the web.

‍

Or, if you're building your own agents, check out our open-sourced sandboxing code, and consider integrating it into your work. We look forward to seeing what you build.

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

### How do I use Claude Code?

To start using Claude Code, you need to set up an API key and follow the documentation provided. This will guide you through the process of making requests and handling responses effectively.

### What are the application areas for Claude?

From chatbots to automated content generation, Claude's versatility makes it a valuable tool for businesses and developers alike.

### How does Claude improve over time?

User feedback plays a crucial role in Claude's improvement. By analyzing user interactions, developers can identify areas for enhancement and implement necessary changes.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225588ad176f7c4aafd_abc884c723daea810d2e986455358281a2f94102-1000x1000.svg)

Jun 24, 2026

### Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

Claude Code

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](#)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](/blog/agent-identity-access-model)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7912d5b05a5c7ed8ae86_Object-CodeChatCode.svg)

Jun 3, 2026

### Running an AI-native engineering org

Claude Code

[Running an AI-native engineering org](#)Running an AI-native engineering org

[Running an AI-native engineering org](/blog/running-an-ai-native-engineering-org)Running an AI-native engineering org

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

May 12, 2026

### How Anthropic's cybersecurity team built a threat detection platform with Claude Code

Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](#)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](/blog/how-anthropic-uses-claude-cybersecurity)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2222403b092e0358b0e_cd4fd51deacd067d4e30aee4f4b149f6cba1b97b-1000x1000.svg)

Apr 20, 2026

### Meet the winners of our Built with Opus 4.6 Claude Code hackathon

Claude Code

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](#) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

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
