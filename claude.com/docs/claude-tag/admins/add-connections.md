<!-- source: https://claude.com/docs/claude-tag/admins/add-connections -->

[1 · Pair workspace](/docs/claude-tag/admins/pair-workspace)[2 · Give access](/docs/claude-tag/admins/add-connections)[3 · Spend limit](/docs/claude-tag/admins/set-spend-limit)[4 · Test it](/docs/claude-tag/admins/test-it)

Role you needOwner in your Claude organization to create the bundle; an Admin can add credentials to a bundle that already exists. You’ll also need a credential for each service, created by you or by that service’s admin.

Before this stepA [paired workspace](/docs/claude-tag/admins/pair-workspace)

Do I need this?Optional to startYou need a connection only when Claude should act in a system beyond Slack, like querying BigQuery, reading Google Drive, or filing Linear tickets. Slack-only use cases like triage, catch-up, and turning threads into docs run with none.  
  
You can add connections any time after setup (they apply to new threads immediately), but adding the systems your team expects before they onboard means their first requests succeed.

##  Your first Access bundle

An [Access bundle](/docs/claude-tag/concepts/glossary#access-bundle) is a named set of credentials, repository grants, and instructions that Claude uses in the channels the bundle covers. A connection is one service credential inside a bundle, like a Datadog API key or a warehouse service account, that Claude uses to act in that service from any channel under the bundle’s [scope](/docs/claude-tag/concepts/glossary#scope).
If you’re in the setup wizard, it has already created your first bundle (named **Slack default**) and is showing you its connection list; skip to [Decide what to connect](#decide-what-to-connect). The steps below are for creating a bundle outside the wizard, on the admin page directly.

1

Open the admin page

Go to [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag). Under **Claude Tag’s access**, the **Slack** tab shows your scopes (Default Slack access, then each workspace).

2

Create a bundle on a scope

On the scope where you want the bundle to apply, click **+** next to **Access bundles** and choose **Create new bundle**. This creates the bundle and attaches it to that scope in one step; the bundle dialog opens.

3

Name the bundle

Click the pencil next to **Untitled profile** to rename it (the console uses “profile” and “Access bundle” interchangeably).

You can also create an unattached bundle by clicking **Create** on the **Access bundles** page in the left navigation, then attach it to scopes afterward.
Connections belong to the [agent identity](/docs/claude-tag/concepts/agent-identity), not to any person. Personal claude.ai connectors apply only in DMs.
Name a bundle after what it grants, since the name is what you’ll read when deciding which bundles to bind to a channel: `data-readonly`, `github-write`, `monitoring`, `gtm-tools`. A capability name stays meaningful when the same bundle serves several teams; a team name (`devprod-team`) works when one team’s full access is the unit you’ll reuse.

###  Why create more than one bundle

Multiple bundles let you grant access by capability and compose it per channel. For example, with separate `data-readonly`, `github-write`, and `monitoring` bundles: `#platform-eng` gets all three, `#gtm-analytics` gets only `data-readonly`, and `#incidents` gets `monitoring` plus `github-write`. Each credential is defined once, so rotating a Datadog key means editing one bundle without touching the others.
A bundle also has Domains, Plugins, and Instructions tabs alongside Credentials and Repositories. Use the bundle’s Instructions for guidance that should travel with a credential; use [per-scope custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions) for guidance tied to a place.

##  Decide what to connect

Six categories cover most of the work teams hand to Claude. Any service with an HTTP API can be added; start with the categories that match what your teams already do.
Read-only connections are most useful in combination: an answer that joins the ticket, the deploy, and the error rate needs all three systems connected. Connecting many systems read-only is a different decision from granting write access anywhere.

| Connect | Examples | Recommended access | What it adds |
| --- | --- | --- | --- |
| Knowledge and docs | Google Drive, [Notion](/docs/claude-tag/admins/connections/notion), Confluence | Read | Answers grounded in design docs, runbooks, and prior decisions |
| Code | GitHub, [GitLab](/docs/claude-tag/admins/connections/gitlab) | Read and write | Branches, pull requests, review, CI follow-up. GitHub is [configured separately](/docs/claude-tag/admins/configure-github) |
| Data warehouse | BigQuery, [Snowflake](/docs/claude-tag/admins/connections/snowflake), Redshift | Read | Data questions answered with charts in the thread; recurring reports |
| Monitoring | [Sentry](/docs/claude-tag/admins/connections/sentry), [Datadog](/docs/claude-tag/admins/connections/datadog), [PagerDuty](/docs/claude-tag/admins/connections/pagerduty) | Read | Logs, metrics, and errors for debugging and incident work |
| Issue tracking | [Linear](/docs/claude-tag/admins/connections/linear), [Asana](/docs/claude-tag/admins/connections/asana), Jira | Read and write | File tickets and post status updates where work lives |
| Go-to-market | [HubSpot](/docs/claude-tag/admins/connections/hubspot), [Gong](/docs/claude-tag/admins/connections/gong), [Salesforce](/docs/claude-tag/admins/connections/salesforce) | Read | Pipeline and customer state for account questions |

Per-service instructions, with the credential fields and allowed-websites values, are in the [connection guides](/docs/claude-tag/admins/connections/overview).

###  Create a dedicated account per service

The credential you connect is Claude’s account in that tool, not yours. Anyone in a channel under the bundle’s scope can use it through Claude, so connect a dedicated identity you control rather than your personal login.

For each tool, create that identity specifically for the agent rather than reusing a shared bot key. The pattern depends on the service.

| Service type | Recommended pattern |
| Google Workspace (Drive, Calendar, Docs) | Create a virtual user like `[email protected]` and share the folders and calendars it needs. If using a GCP service-account key with domain-wide delegation, restrict the delegation to that single subject and the minimum OAuth scopes; DWD can otherwise impersonate any user in your domain. |
| SaaS with native service accounts (Datadog, Snowflake, Sentry) | Create a service account in that tool’s admin, scope it to the project or read-only role, and use its API key |
| SaaS without service accounts (Linear, Asana on most plans) | Create a dedicated user seat for the agent and use a personal access token from that seat |
| Cloud APIs (AWS, GCP) | Create a dedicated IAM principal with the narrowest policy that covers the work |

A dedicated account keeps the agent’s activity separately auditable in each tool’s logs and lets you revoke its access without touching anyone else’s. Grant read-only wherever the categories below say read; Claude can never exceed what the key allows.
If the person who administers a service isn’t you, send them this:

Please create a service account in [service] for our Claude agent, scoped to [read-only / the specific project], and send me the credential through [your secrets channel]. It will be used by an org-managed agent, with the credential injected at a network proxy; the agent itself never holds the key. Details: https://claude.com/docs/claude-tag/admins/add-connections

###  Limit access to specific resources

A connection has no setting for which pages, folders, or projects Claude can reach inside a tool. The connection’s reach is whatever the connected account can access in that tool. To narrow Claude to a subset, narrow the account:

* **Confluence or another wiki:** give the service account read access to only the spaces or pages Claude should see
* **Google Drive:** share only the relevant folders with the dedicated Google account; see [Google Workspace](/docs/claude-tag/admins/connections/google)
* **Project or ticket trackers:** add the service account to only the projects it needs

The host, path, and method restrictions on a connection control which API endpoints Claude can call, not which records those endpoints return. Use them alongside account-level scoping, not instead of it.
For a shared or external channel, put the narrowed connection in its own bundle and [attach that bundle only to that channel](/docs/claude-tag/admins/attach-to-scope#attach-to-a-channel), so the credential is unavailable elsewhere.

##  Connect a service that isn’t in the list

For a service without a preset Connect button, use **Connect another app** at the bottom of the bundle’s Credentials tab. See the [Custom connection guide](/docs/claude-tag/admins/connections/custom) for the form fields, credential types, and how to add a custom MCP server.

##  Allow a host without a credential

For a public API or any host Claude should reach without an injected credential (your status page, a public package registry, an internal service that accepts unauthenticated reads), use the bundle’s **Domains** tab instead of adding a connection. Enter the hostname (a wildcard is allowed as the leftmost label) and the ports. Requests to that host go through without a credential attached; everything else stays default-deny.

##  Add a connection

On the bundle’s **Credentials** tab, click **Connect** next to a listed service, or **Connect another app** at the bottom for a service not in the list.
For a custom connection, choose the credential type:

| Credential type | Use for |
| Bearer | API keys and OAuth bearer tokens. Most SaaS REST APIs. |
| Basic | HTTP Basic authentication. |
| AWS SigV4 | Signed requests to AWS APIs with an access key pair. |
| GCP service account key | Google Cloud APIs via a service-account JSON key. Google Workspace services like Drive and Calendar also use this; see [the Google guide](/docs/claude-tag/admins/connections/google). |
| OAuth 2.0 client credentials | Server-to-server OAuth. |
| OAuth 2.0 JWT bearer | Server-to-server OAuth. Salesforce uses this. |
| OAuth 2.0 authorization code | Sign in once as an admin; the agent acts as that account. |

Credentials are injected at the network boundary by Agent Proxy; the model and the sandbox are not given the key. A request to a host you haven’t allowed is blocked, not sent. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

###  Set allowed websites

List the hosts a connection’s credential may be sent to. A wildcard works only as the leftmost label, like `*.example.com`.
To change a connection’s name or allowed websites after saving, open the **⋮** menu on that connection’s row in the bundle’s **Credentials** tab and choose **Edit**. The same menu has **Rotate secret** (where the credential type supports it) and **Delete**.
Check the host against your account’s region before saving. Some presets fill a default host that may not match your account’s region; a Datadog key, for example, only works against your account’s Datadog site, like `api.datadoghq.com` or `api.datadoghq.eu`.

###  Restrict by path or method

After saving, you can restrict a connection by URL path or HTTP method, like allowing `GET` but not `DELETE`, for control tighter than host-level.

###  Connections vs claude.ai connectors

The connection gallery lists credential types the agent can hold, not the connectors your organization or its members have set up on claude.ai. A connection authenticates the agent, not a person; a connector on someone’s personal claude.ai account doesn’t appear here. For Google services, use a service-account key or the OAuth sign-in option, both of which give the agent one credential with access to the data the channel needs. Personal connectors keep working in [DMs](/docs/claude-tag/concepts/agent-identity#direct-message-channels).

##  Attach plugins

A connection grants access; a plugin teaches Claude how to use it well. A plugin is a bundle of skills, reusable instructions for working with a specific tool or following a specific process, and you attach plugins to the same Access bundle or scope that carries the connection, so the credential arrives with directions for using it.
A Datadog API key, for example, makes the API reachable, and a Datadog plugin tells Claude which endpoints answer which questions. Sessions in covered channels pick up attached plugins automatically; there is nothing for channel members to install or enable.
Anthropic provides plugins for common tools, and you can add your own from a [skills repository](/docs/claude-tag/admins/skills-repo). To give Claude organization-wide skills, bundle them in a plugin.
Updated plugins and skills apply to new threads only. A thread already running keeps the versions it began with; start a fresh thread to pick up the latest.
Claude can’t publish a new skill version from inside a thread; that update happens in admin settings.

##  Verify the connection saved

* Each connection is listed in the bundle with the host you set.
* New connections apply to new threads only: an existing thread keeps the connections it started with, so test in a fresh thread.

* [Set a spend limit](/docs/claude-tag/admins/set-spend-limit): fund usage so the connections you just added can run
* [Configure GitHub access](/docs/claude-tag/admins/configure-github): repository access, configured on a separate page
* [How agent identity works](/docs/claude-tag/concepts/agent-identity#agent-proxy): how the credentials you just added reach Claude without entering its sandbox

[1. Pair your Slack workspace](/docs/claude-tag/admins/pair-workspace)[3. Set a spend limit](/docs/claude-tag/admins/set-spend-limit)
