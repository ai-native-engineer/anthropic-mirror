<!-- source: https://claude.com/docs/claude-tag/concepts/agent-identity -->

Claude Tag’s identity depends on where you message it.
In Slack channels, Claude acts with its own service accounts, rather than as a specific user. An organization Owner [provisions this identity during setup](/docs/claude-tag/admins/setup-overview), so it arrives with its own account in each system it works in: the Claude app in Slack, the Claude GitHub App on GitHub, and a service account in every other connected tool. Actions it takes are attributed to those accounts; for example, posts come from the Claude app and pull requests show the Claude GitHub App as the author.
In direct messages (DMs) between a user and `@Claude`, the provisioned identity does not apply. DMs are one-to-one only; group DMs aren’t supported. A DM has no channel to scope it to, so a DM session runs on [the individual’s own claude.ai account](#direct-message-channels) instead, with their personal connectors. Work Claude does within a DM is attributed to that user; for example, a pull request opened from a DM lists the author as the user who asked for it. Admins can disable DMs organization-wide; see [Allow or disable direct messages](/docs/claude-tag/admins/restrict-access#allow-or-disable-direct-messages).

How Claude behaves in channels (its standing instructions, plugins, and channel memory) is configured separately from its identity; see [custom instructions](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions), [plugins](/docs/claude-tag/admins/add-connections#attach-plugins), and [memory](/docs/claude-tag/users/memory) for more information.

##  Channel sessions

When Claude works on a channel task, three systems are involved:

* The ask happens in your Slack workspace, when a user tags Claude to do something or a scheduled task starts.
* The work Claude does runs in a sandbox on Anthropic’s infrastructure, with nothing installed in your network.
* The agent’s credentials for any additional connections, such as GitHub or a data warehouse, reach those systems to pull the required information. An organization Owner sets up those credentials as part of [provisioning the identity](/docs/claude-tag/admins/setup-overview#setup-steps).

The diagram below traces one request through this process.
![Diagram showing the request path across three zones. A task mentioned in your Slack workspace runs in a session sandbox on Anthropic's infrastructure, one sandbox per thread, holding no credentials. Outbound requests pass to Agent Proxy, which injects the credential drawn from the credential store; a request matching no rule is blocked. Credentialed requests reach your systems, like GitHub, a data warehouse, monitoring, or any HTTP API. A dashed return path shows results posting back in the thread, as Claude.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/request-path.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=e8776cf0edd1f3ec912b9b044c9cc838)
![Diagram showing the request path across three zones. A task mentioned in your Slack workspace runs in a session sandbox on Anthropic's infrastructure, one sandbox per thread, holding no credentials. Outbound requests pass to Agent Proxy, which injects the credential drawn from the credential store; a request matching no rule is blocked. Credentialed requests reach your systems, like GitHub, a data warehouse, monitoring, or any HTTP API. A dashed return path shows results posting back in the thread, as Claude.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/request-path-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=a2ed5f3270989c3ed3d9b9a78a72bff0)

1

Tag Claude in a channel

A user asks Claude to chart last week’s signups or fix a deploy test. The request starts a new session.

2

The session sandbox starts

Claude does the work in an isolated environment Anthropic builds for this thread, reading files, writing documents, and running code. The credentials you provision are not placed in the sandbox; they stay in the credential store and are injected at the proxy.

3

The request crosses Agent Proxy

When the work needs something outside the sandbox, like calling the GitHub API or querying a warehouse, the request crosses Agent Proxy, the network boundary between the sandbox and everything else. Agent Proxy checks it against the rules an admin configured, and decides whether it proceeds and what credential, if any, travels with it.

4

Agent Proxy attaches a credential

A matching credential comes from the credential store, where an admin’s [connections](/docs/claude-tag/admins/add-connections) are kept. Once saved, a credential is never displayed again; Agent Proxy retrieves it only at the moment of injection and attaches it to the request at the boundary, so the model and the sandbox itself are not given the key.

5

The result posts back, as Claude

The credentialed request reaches your system, like GitHub or the warehouse, and the result returns to the thread.

###  Agent Proxy

For each outbound request from the sandbox, Agent Proxy checks the destination against what an admin configured, with three possible outcomes:

| When the destination | Result |
| Matches a connection’s rule | The proxy attaches that connection’s credential and forwards the request. The credential stays at the proxy; the model and sandbox are not given it. |
| Is on the [network allowlist](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential) but matches no connection | The proxy forwards the request without a credential. |
| Matches neither | The proxy blocks the request. |

The default is deny: a host stays unreachable from the sandbox until an admin adds it to a connection rule or the allowlist.
The same rules apply to code Claude runs in the sandbox, like `curl` or a `fetch` call: a request is blocked unless its host matches a connection rule or the allowlist.
Nothing is installed inside your network. Your systems see only requests authenticated with the credentials Agent Proxy attached. For the endpoints and addresses your network team may need to allowlist, see [Network requirements](/docs/claude-tag/admins/network-requirements).

###  Agent access

What Claude can reach in a channel comes from the [Access bundles](/docs/claude-tag/admins/add-connections) an admin attached to that channel’s scope. Anyone in the channel gets the same capability, and the same request can do more in `#platform-eng` than in a general channel.
This design has four consequences.

* **Configure once.** Everyone in the scope can use it immediately.
* **Predictability.** What Claude can do never changes based on who asked.
* **Personal connectors apply in DMs.** A shared channel uses only the service-account connections an admin attached, not connectors on anyone’s claude.ai account.
* **Clean audit.** Actions in connected tools show up under a service account your security team already knows how to reason about.

That service-account identity is also how Claude appears wherever it acts. In Slack, it posts as the Claude app. On GitHub, commits and pull requests show the Claude GitHub App, and pull requests link back to the Slack thread they came from. In every other connected service, actions appear under the service account an admin provisioned, in that service’s audit log.

##  Direct message channels

A DM with Claude works differently from a channel. There is no scope to attach an identity to, so a DM session runs with your own claude.ai account instead, the same way a Claude Code session on the web does, using your own connectors and credentials, with results attributed to you. The diagram contrasts with the channel path above; the sandbox is the same engine, but everything around it is yours.
![Diagram showing how a DM session reaches your systems. A message to Claude in a direct message runs in a session sandbox on Anthropic's infrastructure, the same engine as a channel session, but it runs with your identity. From there it reaches your systems through your own connectors and accounts, like GitHub or Drive, using your own credentials. A dashed return path shows results posting back in the DM, as Claude.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/dm-identity.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=d4089034f46e4a760f9fac9d36a689cc)
![Diagram showing how a DM session reaches your systems. A message to Claude in a direct message runs in a session sandbox on Anthropic's infrastructure, the same engine as a channel session, but it runs with your identity. From there it reaches your systems through your own connectors and accounts, like GitHub or Drive, using your own credentials. A dashed return path shows results posting back in the DM, as Claude.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/dm-identity-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=a3ca3c8aa926704742402882f4345b1b)
The table lines up the two paths on the four dimensions that differ.

|  | In a channel | In a DM |
| --- | --- | --- |
| Acts as | Its own service accounts | You |
| Access | The channel’s Access bundles | Your personal connectors |
| Attribution | The agent’s accounts, in each tool’s audit log | Your name |
| Billing | The organization | Your seat |

Three of those differences are worth spelling out.

* **Connectors.** The connectors on your account are available, including MCP servers you’ve added.
* **Billing.** Usage bills to your seat rather than the organization’s service key.
* **Channel-side configuration.** It doesn’t follow you in; the agent’s connections and repository grants don’t apply in DMs.

DM work runs under your credentials, so it’s attributed to you. A pull request opened from a DM uses your GitHub connection and shows you as the author. The agent-identity guarantee is a property of channel sessions, where only provisioned service accounts exist.
Use channels for shared work and DMs for personal tasks, or for data you’d rather access under your own authenticated identity than a shared channel credential.

###  Claude Tag versus Claude Code in Slack

A DM with Claude Tag runs under your own account, which is also how [Claude Code in Slack](https://code.claude.com/docs/en/slack) works, routing a coding @-mention to a Claude Code session on the web under the requester’s own account. The two can look identical. The table shows how to tell them apart.

|  | Claude Tag in a channel | Claude Code in Slack |
| --- | --- | --- |
| **Runs under** | The agent identity an admin provisioned | Your own Claude account, linked in the Claude app |
| **GitHub** | The Claude GitHub App; pull requests belong to the app | Your GitHub connection on claude.ai/code; pull requests open under your account |
| **Access** | Follows the channel’s Access bundles | Follows you |
| **Billing** | The organization | Your seat |

If `@Claude` in your workspace opens pull requests as you, you’re seeing Claude Code in Slack, not a Claude Tag session.

* [Security and data handling](/docs/claude-tag/concepts/security-and-data): where credentials are stored, what leaves your tenant, and what runs unattended
* [Give Claude access](/docs/claude-tag/admins/add-connections): provision the access this page describes
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): narrow where this agent identity is allowed to act

[How Claude Tag works](/docs/claude-tag/concepts/how-it-works)[Security and data handling](/docs/claude-tag/concepts/security-and-data)
