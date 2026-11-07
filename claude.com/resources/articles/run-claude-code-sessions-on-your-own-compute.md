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

Self-hosted environments for Claude Code | Claude by Anthropic
