<!-- source: https://claude.com/resources/articles/enterprise-managed-auth -->

***Update: Enterprise-managed authorization is now generally available and supports Datadog, Notion, and Slack with Exa, Miro, and Zoom coming soon in addition to the existing support for Asana, Atlassian, Canva, Figma, Granola, Linear, and Supabase. (August 24, 2026)***

Admins can now provision MCP connectors for their whole organization through their identity provider, starting with Okta. Users get connector access automatically on first login, with authorization configured centrally by their organization.

Connectors make Claude more useful at work — they give Claude the context it needs from the tools that your teams already use. Until now, turning them on required action at two steps: admins enabled a connector for the organization, and then every individual user authorized it themselves.

Enterprise-managed authorization streamlines that second step. Admins authorize a connector once, users inherit access through the IdP groups and roles they already have, and the connector is there the first time someone opens Claude. The result is zero-touch connector setup for the end user.

Enterprise-managed auth is the first implementation of the [Enterprise-Managed Authorization extension](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization) to the Model Context Protocol. It's built on an open standard so any connector can support it — including the custom connectors your own teams build — and they all work the same way for every Claude customer.

### How it works

Connect your identity provider to Claude and choose which MCP connectors to enable for your organization. When an employee logs in, their connectors are already there. Access stays consistent across Claude chat, Claude Code, and Cowork.

For admins, this folds MCP access management into the same workflow that governs the rest of your stack: provision once, scope by group, manage revocation through the IdP. Because checking access with the IdP is frictionless, admins can shorten access token lifetimes without impacting productivity — so when someone is deprovisioned, their connector access expires fast instead of lingering on an old token. Access runs through the identity provider you already trust, so connectors fall under the same security and access controls as everything else, rather than a separate surface to monitor.

Admins can also require that a connector only ever connects through the IdP, which keeps work and personal use cleanly separated and prevents someone from accidentally linking a personal account to a work tool.

### Built with an ecosystem

Enterprise-managed authorization works across three groups: the identity providers that govern access, the MCP providers that support the standard, and the Claude customers deploying managed connections across their teams.

**Identity providers.** Okta is supported at launch, with support for additional identity providers coming soon.

**MCP providers.** Asana, Atlassian, Canva, Figma, Granola, Linear, and Supabase support Enterprise-managed auth at launch, with Slack coming soon.

**Claude customers.** Hubspot, Ramp, and Webflow are among the organizations rolling out enterprise-managed auth across their teams.

![Slack](https://assets.claude.com/d28a34b6acf04e16d9b8806ee16d3ca66f00b389.svg)

> “Slack is the place where humans and agents are working side by side, in the same conversation, with the same context, toward the same goals. Through the Slack MCP server, all of this becomes accessible to Claude, not just to read but to act on. Enterprise-managed auth means organizations can roll out access to all users without friction. Security teams configure it once through their existing identity provider and users get seamless access.”

Rod García, VP of Engineering

![Supabase](https://assets.claude.com/e42031c6a0e0c0cd1f5f598d9efb9e640b1fc6b3.svg)

> “The only way to use Supabase through Claude was to be an org owner or hand out Personal Access Tokens to everyone on your team. Enterprise-managed auth fixes that: your IdP controls access and roles, so builders can use Claude to explore and query their data without IT compromising on security to get there.”

Bil Harmer, CISO

![Webflow](https://assets.claude.com/5ad498f237d04754725acb0af0c23e5d27611d33.svg)

> “Our team opens Claude and every tool they’re cleared for is right there, scoped by the identity groups IT already runs. Enterprise-managed auth turned AI into something people use instead of request, and we’re taking it across Webflow.”

Reed Shackelford, Senior Manager, Enterprise AI Operations

![Asana](https://assets.claude.com/b8ffecd4a133f2860151d51156002816a54772e7.svg)

> “Enterprise-managed auth is a foundational milestone in realizing Asana's vision as the operating system for human-agent teams. By providing organizations with a secure, controlled way to connect Claude to their most critical workflows, we are unlocking the ability to scale AI-driven value across the enterprise—backed by the absolute governance, compliance, and trust that large-scale deployment demands.”

Arnab Bose, CPO

![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

> “Enterprise-managed auth makes Atlassian Rovo MCP easier for Claude Enterprise customers to adopt at scale, giving employees a simple way to connect Claude to the Atlassian work they already rely on across Jira, Confluence, and Teamwork Graph. Just as importantly, it gives admins a centralized place to manage MCP clients' access, so organizations can move faster with AI while maintaining the governance they expect.”

Brendan Haire, VP of Engineering, Rovo and AI

![Canva](https://assets.claude.com/f047885ca3dadf9a16509752ef150ebb9bd424bb.svg)

> “Canva is already trusted by 95% of the Fortune 500, and our MCP server lets even more teams create, edit and publish on-brand designs with Canva's AI and design tools, all in the same workflow. Enterprise-managed auth with Okta makes it clear and simple for enterprises to manage AI access with a system they already trust, enabling teams to create with AI, safely and at scale.”

Anwar Haneef, GM & Head of Ecosystem

![Figma](https://assets.claude.com/30df15cbd261edbc52262a1fa2d1339f3a1a372b.svg)

> “The Figma MCP brings the power of code and canvas together so teams can move faster, explore more and ship products that stand out. As MCP adoption grows, enterprise-managed auth makes it easier for enterprises to scale their MCP deployments securely without slowing teams down.”

Devdatta Akhawe, VP of Engineering

![Granola](https://assets.claude.com/3db5669fc35f363040dcf5ec573f2401d3f0e1a0.svg)

> “It's great to see Anthropic and Okta make it easier for enterprises to connect to MCP servers securely, centrally and at scale. Granola helps teams capture some of the most important context at work: decisions, details and follow ups as they happen. MCP makes this useful across team tools, and enterprise-managed auth makes it available frictionlessly across teams.”

Chris Pedregal, CEO & co-founder

![Hubspot](https://assets.claude.com/d6f4aa0286766975a05548621fb66283ec2bfe32.svg)

> “Enterprise-managed auth is the security and user experience that we've been looking for with MCP connections. Folks just perform a standard login to Okta and they're connected with their personal context to all MCP hosts in our software ecosystem. Personal identity passes through, but no one gets tripped up on a multitude of OAuth grants. It's a huge win for enterprise management, especially paired with selective control of individual tools exposed by those MCP hosts.”

Andrew Meinert Director, System Operations & AI

![Linear](https://assets.claude.com/02794cae131d86ae8d46e3238f14d1a7ad685181.svg)

> “Logging in once and automatically having all your MCP connectors automatically set up is pretty magical.”

Tom Moor, Head of Engineering

![Okta](https://assets.claude.com/87c2bb73c73e8c1bfcd74b6f3535cb097f060b2b.svg)

> “The momentum around MCP is incredible, but as we move toward an interconnected AI workforce, security can't be an afterthought. By embedding the Cross App Access protocol into MCP as the Enterprise-Managed Authorization extension, as well as implementing it in the Claude ecosystem, we turn identity into a centralized governance plane and give security teams strict compliance control and users a seamless, secure experience.”

Aaron Parecki, Director of Identity Standards

![Ramp](https://assets.claude.com/6db782273272dd89f11df7b54089328994fe718e.svg)

> “Before enterprise-managed auth, onboarding a new hire to their full toolkit meant a queue of per-connector OAuth approvals. Now they log in to Claude on day one already connected — 2,000 employees, provisioned through Okta, zero extra steps.”

Cameron Leavenworth, Staff IT Engineer, AI

![Slack](https://assets.claude.com/d28a34b6acf04e16d9b8806ee16d3ca66f00b389.svg)

> “Slack is the place where humans and agents are working side by side, in the same conversation, with the same context, toward the same goals. Through the Slack MCP server, all of this becomes accessible to Claude, not just to read but to act on. Enterprise-managed auth means organizations can roll out access to all users without friction. Security teams configure it once through their existing identity provider and users get seamless access.”

Rod García, VP of Engineering

![Supabase](https://assets.claude.com/e42031c6a0e0c0cd1f5f598d9efb9e640b1fc6b3.svg)

> “The only way to use Supabase through Claude was to be an org owner or hand out Personal Access Tokens to everyone on your team. Enterprise-managed auth fixes that: your IdP controls access and roles, so builders can use Claude to explore and query their data without IT compromising on security to get there.”

Bil Harmer, CISO

![Webflow](https://assets.claude.com/5ad498f237d04754725acb0af0c23e5d27611d33.svg)

> “Our team opens Claude and every tool they’re cleared for is right there, scoped by the identity groups IT already runs. Enterprise-managed auth turned AI into something people use instead of request, and we’re taking it across Webflow.”

Reed Shackelford, Senior Manager, Enterprise AI Operations

![Asana](https://assets.claude.com/b8ffecd4a133f2860151d51156002816a54772e7.svg)

> “Enterprise-managed auth is a foundational milestone in realizing Asana's vision as the operating system for human-agent teams. By providing organizations with a secure, controlled way to connect Claude to their most critical workflows, we are unlocking the ability to scale AI-driven value across the enterprise—backed by the absolute governance, compliance, and trust that large-scale deployment demands.”

Arnab Bose, CPO

![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

> “Enterprise-managed auth makes Atlassian Rovo MCP easier for Claude Enterprise customers to adopt at scale, giving employees a simple way to connect Claude to the Atlassian work they already rely on across Jira, Confluence, and Teamwork Graph. Just as importantly, it gives admins a centralized place to manage MCP clients' access, so organizations can move faster with AI while maintaining the governance they expect.”

Brendan Haire, VP of Engineering, Rovo and AI

![Canva](https://assets.claude.com/f047885ca3dadf9a16509752ef150ebb9bd424bb.svg)

> “Canva is already trusted by 95% of the Fortune 500, and our MCP server lets even more teams create, edit and publish on-brand designs with Canva's AI and design tools, all in the same workflow. Enterprise-managed auth with Okta makes it clear and simple for enterprises to manage AI access with a system they already trust, enabling teams to create with AI, safely and at scale.”

Anwar Haneef, GM & Head of Ecosystem

1/12

### Getting started

Enterprise-managed auth is available today in beta for customers on the Claude Team and [Enterprise](https://claude.com/solutions/enterprise) plans. [Learn more](https://support.claude.com/en/articles/15537633) on our Help Center and [apply for access](https://claude.com/form/ema-waitlist) to get started.

Any identity or MCP provider can add support for enterprise-managed auth by implementing the [open extension](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth) to the MCP authorization spec. Submit interest to join the beta [here.](https://docs.google.com/forms/d/e/1FAIpQLSf1goHGNDVFK7rncYuh6wnRpWSy7eGOcgL1i8uw3oyKFO9UUA/viewform?usp=sharing&ouid=101055591948883487705)

[ArticleSep 30, 2026

### How Anthropic's sales team rebuilt inbound with Claude Managed Agents

Carl Johnson, a sales development leader at Anthropic, shares how a Claude-powered buying agent now answers most inbound customers, and how that changed the way our sales team works.

Claude Platform](https://claude.com/resources/articles/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents)[ArticleSep 23, 2026

### How to prepare for AI-driven code modernization projects

How to organize AI-driven modernization projects for critical systems and regulated enterprises.

Claude Code](https://claude.com/resources/articles/how-to-prepare-for-ai-driven-code-modernization-projects)[ArticleSep 23, 2026

### How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel on Claude Marketplace

CodeRabbit expanded its Vercel plan through Claude Marketplace, and Power Digital and ThoughtSpot expanded their Snowflake capacity using their existing Anthropic commitment.

Claude Platform](https://claude.com/resources/articles/how-coderabbit-power-digital-and-thoughtspot-scale-with-snowflake-and-vercel-on-claude-marketplace)[ArticleSep 17, 2026

### Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5

Balyasny Asset Management (BAM) Chief AI Officer Charlie Flanagan on why the firm uses Claude Fable 5 and the role of safeguards in deploying frontier intelligence safely and reliably across the organization.
‍

Claude PlatformClaude Code](https://claude.com/resources/articles/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
