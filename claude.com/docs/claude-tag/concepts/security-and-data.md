<!-- source: https://claude.com/docs/claude-tag/concepts/security-and-data -->

In channels, Claude acts under its own service accounts that an Owner provisions. By default it can read and post in Slack channels it’s been added to and search public channels by keyword; it has no access to your external systems until an Owner adds connections. Each connection is scoped to specific channels and workspaces, and the actions Claude takes in connected tools are attributable to its own service accounts.
Every channel request, whether a person typed it or a schedule triggered it, follows the same path: it runs in a sandbox Anthropic hosts, leaves that sandbox only through Agent Proxy, and reaches your systems under the agent’s own accounts. DMs run on the user’s own claude.ai account instead and are covered separately on [How agent identity works](/docs/claude-tag/concepts/agent-identity#direct-message-channels).

##  How a request travels

Each Slack thread runs in its own sandbox, and every outbound call from that sandbox passes through the same checkpoints.
![Diagram showing the request path across three zones. A task mentioned in your Slack workspace runs in a session sandbox on Anthropic's infrastructure, one sandbox per thread, holding no credentials. Outbound requests pass to Agent Proxy, which injects the credential drawn from the credential store; a request matching no rule is blocked. Credentialed requests reach your systems, like GitHub, a data warehouse, monitoring, or any HTTP API. A dashed return path shows results posting back in the thread, as Claude.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/request-path.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=e8776cf0edd1f3ec912b9b044c9cc838)
![Diagram showing the request path across three zones. A task mentioned in your Slack workspace runs in a session sandbox on Anthropic's infrastructure, one sandbox per thread, holding no credentials. Outbound requests pass to Agent Proxy, which injects the credential drawn from the credential store; a request matching no rule is blocked. Credentialed requests reach your systems, like GitHub, a data warehouse, monitoring, or any HTTP API. A dashed return path shows results posting back in the thread, as Claude.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/request-path-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=a2ed5f3270989c3ed3d9b9a78a72bff0)

| Checkpoint | The guarantee |
| The sandbox | Runs on Anthropic’s infrastructure and holds no credentials |
| Agent Proxy | Injects credentials from the credential store at request time, and blocks traffic to unlisted hosts by default |
| Your systems | See the agent’s own accounts, so its actions there are attributable |

###  Compute and the sandbox

Sessions run in sandboxes Anthropic hosts, the same managed compute behind [Claude Code on the web](https://code.claude.com/docs/en/web-quickstart). Each Slack thread gets its own sandbox.
When a thread goes quiet, its sandbox is released; replying in the thread builds a fresh one. What persists across that release and rebuild:

* **Persists:** The thread, its visible work, and anything pushed to a branch, opened as a pull request, or posted into Slack.
* **Does not persist:** Files that existed only inside the sandbox. To keep generated files, ask Claude to push them to a branch or post them in the thread.

Claude Tag retains channel memory and session transcripts. Because of that retention, Claude Tag isn’t available to organizations with Zero Data Retention (ZDR) enabled.

###  Credential storage

Credentials you provision are kept in a separate credential store, not in the proxy itself. When an outbound request matches a rule, [Agent Proxy](/docs/claude-tag/concepts/agent-identity#agent-proxy), the network layer between the sandbox and any external host, retrieves the credential from that store and injects it at the boundary, so the model and the sandbox are not given the key.
This means:

* **A saved credential is not displayed again.** The setup screens are write-only.
* **The credential travels only to the hosts you named** when you added the connection.
* **You can narrow the credential further**, to one host, one path prefix, or read-only methods, in [Add connections](/docs/claude-tag/admins/add-connections).

###  Network egress

Outbound traffic from a channel session’s sandbox is default-deny. Requests go only to hosts an Owner allowed, either on the [bundle’s Domains tab](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential) or through a [connection’s Allowed websites](/docs/claude-tag/admins/connections/custom#fill-out-the-connect-another-app-form), and every request gets one of three outcomes:

* **Matches a credential rule.** The credential is attached at the boundary and the request proceeds.
* **Matches only an allowlist.** The request is sent without credentials.
* **Matches nothing.** The request is blocked outright; the host is unreachable rather than merely unauthenticated.

![Flow diagram across two zones. Inside Anthropic's infrastructure, a session sandbox that holds no credentials sends every outbound request to Agent Proxy, which matches it against admin rules. Three outcomes branch toward your systems: on a rule match, the credential is attached at the boundary and the request proceeds; on an allowlist-only match, the request is sent without credentials; on no match, the request is blocked entirely — the default-deny outcome — and the host is unreachable.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/proxy-decision.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=9e578cca43452a4feaf952acbf1d597b)
![Flow diagram across two zones. Inside Anthropic's infrastructure, a session sandbox that holds no credentials sends every outbound request to Agent Proxy, which matches it against admin rules. Three outcomes branch toward your systems: on a rule match, the credential is attached at the boundary and the request proceeds; on an allowlist-only match, the request is sent without credentials; on no match, the request is blocked entirely — the default-deny outcome — and the host is unreachable.](https://mintcdn.com/claude-ai/5JFKyLlO7sHMMf5J/images/claude-tag/diagrams/proxy-decision-dark.svg?fit=max&auto=format&n=5JFKyLlO7sHMMf5J&q=85&s=67414f3d0c8dcb15ec33823fc28bf7c1)
Because requests to unlisted hosts are blocked, data can only leave the sandbox to hosts you’ve allowed. The egress boundary is the Allowed websites list, which an admin sets on each connection and on a bundle’s Domains tab; see [Set allowed websites](/docs/claude-tag/admins/add-connections#set-allowed-websites) and [Allow a host without a credential](/docs/claude-tag/admins/add-connections#allow-a-host-without-a-credential).

###  Service accounts

In channels, Claude acts under service credentials of its own, not under the account of the person who tagged it. The Slack surface is the Claude app, code work goes through the Claude GitHub App, and every other connected tool uses a service account an Owner provisions in an Access bundle. See [How agent identity works](/docs/claude-tag/concepts/agent-identity) for the full model.
A connection belongs to that agent identity and is shared by everyone the bundle’s scope covers. Anyone in a channel under that scope can ask Claude to act with the credential, so whatever the connected account can read or write is available to every member of those channels. Connect a dedicated identity you control for each service, such as a `[email protected]` seat or a native service account, rather than a personal login. A dedicated account keeps the agent’s actions separately auditable in each tool’s logs and lets you revoke its access without affecting a person; see [Create a dedicated account per service](/docs/claude-tag/admins/add-connections#create-a-dedicated-account-per-service).
DMs with `@Claude` run on the user’s own claude.ai account instead, with that user’s personal connectors, and work there is attributed to them. Personal connectors apply only in DMs, never in channels. Admins can disable DMs organization-wide; see [Allow or disable direct messages](/docs/claude-tag/admins/restrict-access#allow-or-disable-direct-messages).

##  Member access

By default, anyone in a connected Slack workspace can invoke Claude in channels, with or without a Claude account. An Owner can narrow that to organization members only, or to members whose role grants it. The setting and the role-based configuration are on [Members](/docs/claude-tag/admins/restrict-access#members). It governs DMs as well as channels.

* [How agent identity works](/docs/claude-tag/concepts/agent-identity): the identity model in full, including DM attribution
* [Restrict where Claude Tag operates](/docs/claude-tag/admins/restrict-access): the controls that exist and the ones that don’t
* [Audit Claude Tag activity](/docs/claude-tag/admins/audit): the trails for tracing what it did

[How agent identity works](/docs/claude-tag/concepts/agent-identity)[Glossary](/docs/claude-tag/concepts/glossary)
