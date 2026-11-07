<!-- source: https://claude.com/resources/articles/introducing-the-claude-apps-gateway -->

Today, we're introducing the Claude apps gateway for Amazon Bedrock and Google Cloud. Previously, running Claude Code on these platforms has meant provisioning a cloud credential per developer, manually pushing settings to every laptop, and standing up separate tooling to see per-developer spend. The gateway is a self-hosted control plane that gives you corporate SSO login, centrally enforced policy, role-based access, and per-user cost attribution for Claude Code.

## **Deploying the gateway**

The gateway is run as a single stateless container deployed on Linux and backed by a PostgreSQL database. It holds your upstream credential, authenticates developers against your identity provider, distributes and enforces managed settings, and reports per-user usage to a collector you operate. Onboarding a developer means adding them to your Identity Provider (IdP). Offboarding means removing them.

The gateway is built and shipped by Anthropic inside the same `claude` binary your developers already install, so you can run it in one stateless container on your infrastructure. Because the gateway and the client are built together, the `/login` flow is gateway-aware, the client applies managed settings automatically at sign-in, and policy is enforced consistently on every request.

## **How the gateway works**

The gateway handles:

* **Identity.** It acts as an OpenID Connect (OIDC) relying party against Google Workspace, Microsoft Entra ID, Okta, or any standards-compliant OIDC provider, and issues a short-lived session. No long-lived secrets sit on developer machines.
* **Policy.** You can define managed settings once on the server, and clients receive the policy at sign-in and the gateway enforces it on every request. You can adjust allowed models and default settings centrally.
* **Telemetry.** The client stamps a usage metric for every request, and the gateway relays it over OTLP to a collector you configure, in your network and on your retention schedule.
* **Routing.** The gateway holds your upstream credential and routes inference to the Claude API, Amazon Bedrock, or Google Cloud, with optional failover between providers.
* **Spend caps.** The gateway allows you to set daily, weekly, and monthly spend limits. Limits can be applied per organization, group, or user.

The gateway does not send inference traffic or usage data to Anthropic unless you configure it to use the Claude API. We're also publishing the protocol the gateway uses, so other gateway developers can implement the same features.

## **Getting started**

The gateway is available now. To get started:

* **Deploy the gateway**: Download the Claude Code CLI binary, point `gateway.yaml` at your OIDC issuer and upstream credential, and register one OIDC app in your IdP.
* **Roll it out**: Configure the `forceLoginMethod` and `forceLoginGatewayUrl` parameters in `managed-settings.json` on client machines. Clients connect to your gateway on first boot.

[See the documentation](https://code.claude.com/docs/en/claude-apps-gateway) to learn more.

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
