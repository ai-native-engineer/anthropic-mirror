<!-- source: https://claude.com/blog/enterprise-managed-auth -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d23008bbc20c0ffaeb6f_43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)

# Centrally manage authorization for MCP connectors

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Enterprise

  Claude apps
* Date

  June 18, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/enterprise-managed-auth

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

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3414e70a75001b66e8d27f_asana-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3414e7f48cd2308583c215_asana-light.svg)

"Enterprise-managed auth is a foundational milestone in realizing Asana's vision as the operating system for human-agent teams. By providing organizations with a secure, controlled way to connect Claude to their most critical workflows, we are unlocking the ability to scale AI-driven value across the enterprise—backed by the absolute governance, compliance, and trust that large-scale deployment demands."

Arnab Bose, CPO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a84a22074cc407a84848_Atlassian_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a84a22074cc407a84848_Atlassian_light.svg)

“Enterprise-managed auth makes Atlassian Rovo MCP easier for Claude Enterprise customers to adopt at scale, giving employees a simple way to connect Claude to the Atlassian work they already rely on across Jira, Confluence, and Teamwork Graph. Just as importantly, it gives admins a centralized place to manage MCP clients' access, so organizations can move faster with AI while maintaining the governance they expect."

Brendan Haire, VP of Engineering, Rovo and AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94f6f82b1f84f489887_Canva_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94baddb6685c1e5410d_Canva_dark.svg)

"Canva is already trusted by 95% of the Fortune 500, and our MCP server lets even more teams create, edit and publish on-brand designs with Canva's AI and design tools, all in the same workflow. Enterprise-managed auth with Okta makes it clear and simple for enterprises to manage AI access with a system they already trust, enabling teams to create with AI, safely and at scale."

Anwar Haneef, GM & Head of Ecosystem

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d1ee4cb7c69d15a44ec7d6_Figma%20Dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d1ee481c19e67f332ef755_Figma%20Light.svg)

"The Figma MCP brings the power of code and canvas together so teams can move faster, explore more and ship products that stand out. As MCP adoption grows, enterprise-managed auth makes it easier for enterprises to scale their MCP deployments securely without slowing teams down."

Devdatta Akhawe, VP of Engineering

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a341e95b3dc7be545d7a477_granola-dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a341e93bb7e7bd486f93263_granola-light.svg)

"It's great to see Anthropic and Okta make it easier for enterprises to connect to MCP servers securely, centrally and at scale. Granola helps teams capture some of the most important context at work: decisions, details and follow ups as they happen. MCP makes this useful across team tools, and enterprise-managed auth makes it available frictionlessly across teams."

Chris Pedregal, CEO & co-founder

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6989420bd171609a4d78b31e_logo_hubspot-light-mode.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6989420ff5d1708aeefc4396_logo_hubspot-dark-mode.svg)

“Enterprise-managed auth is the security and user experience that we've been looking for with MCP connections. Folks just perform a standard login to Okta and they're connected with their personal context to all MCP hosts in our software ecosystem. Personal identity passes through, but no one gets tripped up on a multitude of OAuth grants. It's a huge win for enterprise management, especially paired with selective control of individual tools exposed by those MCP hosts.”

Andrew Meinert Director, System Operations & AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bf6f1fdcf6881c9918dd0e_Linear_Logo_0%202%20(1).svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68bf6f187456bf5ca9c27129_Linear_Logo_0%201%20(1).svg)

"Logging in once and automatically having all your MCP connectors automatically set up is pretty magical."

Tom Moor, Head of Engineering

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3407a0610055531404ba06_okta-logo-black.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a34079e0e3beac5523dc868_okta-logo-white.svg)

"The momentum around MCP is incredible, but as we move toward an interconnected AI workforce, security can't be an afterthought. By embedding the Cross App Access protocol into MCP as the Enterprise-Managed Authorization extension, as well as implementing it in the Claude ecosystem, we turn identity into a centralized governance plane and give security teams strict compliance control and users a seamless, secure experience."

Aaron Parecki, Director of Identity Standards

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad6788c7a1b711a85623_Ramp_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad62e2f100f80635f7a7_Ramp_dark.svg)

“Before enterprise-managed auth, onboarding a new hire to their full toolkit meant a queue of per-connector OAuth approvals. Now they log in to Claude on day one already connected — 2,000 employees, provisioned through Okta, zero extra steps.”

Cameron Leavenworth, Staff IT Engineer, AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68db36ce5254656fdbac3c90_SLA-Slack-from-Salesforce-logo%201.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68db36d1588af40e62128f8f_SLA-Slack-from-Salesforce-logo-inverse%201.svg)

“Slack is the place where humans and agents are working side by side, in the same conversation, with the same context, toward the same goals. Through the Slack MCP server, all of this becomes accessible to Claude, not just to read but to act on. Enterprise-managed auth means organizations can roll out access to all users without friction. Security teams configure it once through their existing identity provider and users get seamless access.”

Rod García, VP of Engineering

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3413cc60038a6b9254745b_supabase-dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3413ca2450bd8db73b97f3_supabase-dark-light.svg)

“The only way to use Supabase through Claude was to be an org owner or hand out Personal Access Tokens to everyone on your team. Enterprise-managed auth fixes that: your IdP controls access and roles, so builders can use Claude to explore and query their data without IT compromising on security to get there.”

Bil Harmer, CISO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3413a64096a140ea0118d8_webflow-logo-dark.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3413a24969057e976d25c4_webflow-logo-white.svg)

“Our team opens Claude and every tool they’re cleared for is right there, scoped by the identity groups IT already runs. Enterprise-managed auth turned AI into something people use instead of request, and we’re taking it across Webflow.”

Reed Shackelford, Senior Manager, Enterprise AI Operations

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

### Getting started

Enterprise-managed auth is available today in beta for customers on the Claude Team and [Enterprise](https://claude.com/solutions/enterprise) plans. [Learn more](https://support.claude.com/en/articles/15537633) on our Help Center and [apply for access](https://claude.com/form/ema-waitlist) to get started.

Any identity or MCP provider can add support for enterprise-managed auth by implementing the [openextension](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth) to the MCP authorization spec. Submit interest to join the beta[here.](https://docs.google.com/forms/d/e/1FAIpQLSf1goHGNDVFK7rncYuh6wnRpWSy7eGOcgL1i8uw3oyKFO9UUA/viewform?usp=sharing&ouid=101055591948883487705)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

Jul 28, 2026

### Bringing MCP 2026-07-28 to Claude

Product announcements

[Bringing MCP 2026-07-28 to Claude](#)Bringing MCP 2026-07-28 to Claude

[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)Bringing MCP 2026-07-28 to Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d224f466b800c4a5a016_a7b8978859371a024139418f3366bb0600ee1675-1000x1000.svg)

Jul 24, 2026

### How the product designer who built Claude Design uses it to explore ideas before building them

Enterprise AI

[How the product designer who built Claude Design uses it to explore ideas before building them](#)How the product designer who built Claude Design uses it to explore ideas before building them

[How the product designer who built Claude Design uses it to explore ideas before building them](https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them)How the product designer who built Claude Design uses it to explore ideas before building them

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225e31f7aa22c1f28cb_46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

Jul 24, 2026

### Claude models explained: choosing the best model for your use case

Enterprise AI

[Claude models explained: choosing the best model for your use case](#)Claude models explained: choosing the best model for your use case

[Claude models explained: choosing the best model for your use case](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)Claude models explained: choosing the best model for your use case

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

Jul 2, 2026

### Giving admins more visibility and control over Claude spend

Product announcements

[Giving admins more visibility and control over Claude spend](#)Giving admins more visibility and control over Claude spend

[Giving admins more visibility and control over Claude spend](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)Giving admins more visibility and control over Claude spend

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Enterprise

Claude apps

Business

Productivity

Work
