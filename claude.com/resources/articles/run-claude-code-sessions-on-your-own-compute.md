<!-- source: https://claude.com/resources/articles/run-claude-code-sessions-on-your-own-compute -->

Now in public beta, self-hosted environments let you run Claude Code sessions on your own infrastructure. Start a session from the web, mobile, desktop, or a routine, and it runs inside your network, next to your internal services, toolchains, and security controls, rather than on Anthropic-hosted infrastructure.

For most enterprises, we strongly recommend our hosted offering for operational simplicity with no infrastructure to run or maintain. Self-hosted environments are for teams whose network, tooling, or compliance requirements call for keeping agent execution on infrastructure they control. If you go this route, plan to staff engineering to own setup and ongoing maintenance.

### **Why self-host**

We saw organizations in our preview program adopt self-hosted environments for a few key reasons:

* **Network access:** sessions run inside your network and can reach internal services, databases, and registries without exposing them to the public internet
* **Customizability:** pre-install compilers, SDKs, and internal CLIs in your environment so every session starts ready to build
* **Compliance:** source code and build artifacts stay on infrastructure you control

![Faire](https://assets.claude.com/1ae334c9f7d397f84da34c8aeff571d3b8bc89d9.svg)

> “Self-hosted environments let us integrate Claude Code into our existing development workflows while maintaining our security and operational controls. This setup means Claude can generate PRs, help fix CI issues, and respond to developer workflow events, with compute that can scale based on demand. Claude understands our codebase, making it a strong fit for how our engineering teams build.”

George Jacob, Senior Engineering Manager

### **Data stays on your infrastructure**

Repository checkouts, build artifacts, secrets, and any files a session creates or modifies all stay on infrastructure you provision.

The conversation itself, including prompts, responses, and tool results (which can include code that Claude reads), is sent to Anthropic for inference, and the session transcript is stored so a session can be picked up from any surface.

### **How it works**

When using self-hosted environments, you deploy a set of [runners](https://code.claude.com/docs/en/self-hosted-environments#key-concepts). These long-lived processes pick up sessions and start a Claude Code process for each [session](https://code.claude.com/docs/en/self-hosted-environments#session-lifecycle). Runners come in two modes.

1. **Fixed:** you keep a set number running and sessions are distributed across them.
2. **On-demand:** an orchestrator watches for queued sessions, starts a runner as sessions arrive, and stops them when work finishes so capacity tracks demand.

Runners can serve more than one session, but each session runs in its own checkout, so work stays isolated between developers and accounts. Sessions from every supported surface route to the same environment, so you set it up once and it works wherever your team starts a session.

**Note**: Self-hosted environments differ from [Remote Control](https://code.claude.com/docs/en/remote-control), which lets developers continue sessions running on their own machines from a phone or browser. Sessions using Remote Control end when that machine stops running the session and are tied to the user who ran `claude`, whereas self-hosted environments run sessions on shared infrastructure your platform team operates and can be used by any user.

### **Getting started**

Self-hosted environments are available in public beta to organizations on Claude Team and Enterprise plans. They are off by default and not available for organizations using ZDR.

Plan on a platform, developer experience, or developer productivity team owning setup and ongoing operation, including building and maintaining the runner image, updating runners, and running the orchestrator if you use on-demand mode.

See the [documentation](https://code.claude.com/docs/en/self-hosted-environments) to learn more. Share feedback via [GitHub](https://github.com/anthropics/claude-code/issues) or through your Anthropic account team.

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
