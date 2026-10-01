<!-- source: https://claude.com/blog/introducing-the-claude-apps-gateway -->

Explore here

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a42c9bc20d2072552ef256a_Node-EnterpriseAgents.svg)

# Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud

* Category

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  [Claude Code](https://claude.com/product/claude-code)
* Date

  June 29, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/introducing-the-claude-apps-gateway

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
* **Roll it out**:  Configure the `forceLoginMethod` and `forceLoginGatewayUrl` parameters in `managed-settings.json` on client machines. Clients connect to your gateway on first boot.

[See the documentation](https://code.claude.com/docs/en/claude-apps-gateway) to learn more.

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e6fa9211768bbce0b_6e00dbffcddc82df5e471c43453abfc74ca94e8d-1000x1000.svg)

Sep 30, 2026

### Claude for Government is now generally available

Product announcements

[Claude for Government is now generally available](#)Claude for Government is now generally available

[Claude for Government is now generally available](https://claude.com/blog/claude-for-government-is-now-generally-available)Claude for Government is now generally available

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

Sep 25, 2026

### Build plugins for Claude

Product announcements

[Build plugins for Claude](#)Build plugins for Claude

[Build plugins for Claude](https://claude.com/blog/build-plugins-for-claude)Build plugins for Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

Sep 23, 2026

### Claude Marketplace: one place to discover plugins, agents, and services from our partners

Product announcements

[Claude Marketplace: one place to discover plugins, agents, and services from our partners](#)Claude Marketplace: one place to discover plugins, agents, and services from our partners

[Claude Marketplace: one place to discover plugins, agents, and services from our partners](https://claude.com/blog/claude-marketplace)Claude Marketplace: one place to discover plugins, agents, and services from our partners

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22deea97e4a5b5e5739_8d339ae8ecedecc1409db8f5bbb99c958db56946-1000x1000.svg)

Sep 24, 2026

### Claude Tag now supports personal connectors in channels

Product announcements

[Claude Tag now supports personal connectors in channels](#)Claude Tag now supports personal connectors in channels

[Claude Tag now supports personal connectors in channels](https://claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels)Claude Tag now supports personal connectors in channels

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
