<!-- source: https://claude.com/blog/workload-identity-federation -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

# Secure access to the Claude Platform with Workload Identity Federation

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

* Date

  June 17, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/workload-identity-federation

Workload Identity Federation (WIF) is now generally available on the Claude Platform. WIF is compatible with any OIDC-compliant identity provider and covers all Claude API endpoints, including when accessing the endpoints through our first-party SDKs and Claude Code.

With WIF for workloads and [ant auth login](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart#authentication) for interactive sessions, developers never have to handle a static API key when building with the Claude Platform.

## How Workload Identity Federation works

WIF replaces static API keys with short-lived, scoped credentials issued at request time. Whether you're a two-person startup running GitHub Actions or an enterprise with detailed credential policies, you can now authenticate with the Claude Platform the same way you authenticate with the rest of your stack.

With WIF, there are no static Anthropic credentials to create, rotate, or leak. Workloads authenticate with the identity they already have: an AWS IAM role, a GCP or Kubernetes service account, an Azure managed identity, a GitHub Actions token, Okta, or other OIDC-compliant providers.

We're also introducing service accounts to the Claude Platform, so each workload can have its own identity, roles, and audit trail instead of a shared API key. First, a federation rule binds an external identity to a service account. Then, when a workload requests access, the Claude Platform verifies the workload's signed OIDC token, matches its claims against your federation rules, and issues a short-lived access token bounded by the service account's roles. Every exchange and request is recorded against that service account in your audit logs.

## Set up your first workload in minutes

The [Claude Console](https://platform.claude.com/) has a guided setup flow for configuring workload identities. The setup validates each step and finishes with a test command that confirms your workload can authenticate.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a2f08711ad72d3a0d542c25_Screenshot%202026-06-13%20at%209.20.12%E2%80%AFAM.png)

## Run your whole organization without static keys

WIF is compatible with the [Admin API](https://platform.claude.com/docs/en/build-with-claude/administration-api) for organization management. Federation rules can be configured for least-privilege access through fine-grained scopes.

Federation configuration is also fully programmatic for organizations operating at scale. New Admin API endpoints let you create and update issuers, service accounts, and federation rules.

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## Getting started

API keys work alongside WIF, so you can migrate one workload at a time. Read the setup [guides](https://platform.claude.com/docs/en/build-with-claude/workload-identity-federation) for each identity provider, or open the [Claude Console](https://platform.claude.com/) to connect your first workload.

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d231b45c2193efbb0f02_1869137c9d7f2a38b50e804d707e10e85de05ddb-1000x1000.svg)

Jul 23, 2026

### Think through hard problems in voice mode

Product announcements

[Think through hard problems in voice mode](#)Think through hard problems in voice mode

[Think through hard problems in voice mode](https://claude.com/blog/think-through-hard-problems-in-voice-mode)Think through hard problems in voice mode

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a025cf25f0694905405e054_Object-Scale.svg)

May 12, 2026

### Claude for the legal industry

Product announcements

[Claude for the legal industry](#)Claude for the legal industry

[Claude for the legal industry](https://claude.com/blog/claude-for-the-legal-industry)Claude for the legal industry

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3f14a08cb97bf1b16d40ef_ObjectClouds.svg)

Jul 7, 2026

### Claude Cowork is coming to mobile and web

Product announcements

[Claude Cowork is coming to mobile and web](#)Claude Cowork is coming to mobile and web

[Claude Cowork is coming to mobile and web](https://claude.com/blog/cowork-web-mobile)Claude Cowork is coming to mobile and web

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Business
