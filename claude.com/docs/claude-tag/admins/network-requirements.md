<!-- source: https://claude.com/docs/claude-tag/admins/network-requirements -->

If a service you want to connect (a data warehouse, an internal API, a GitHub organization with an IP allow list) restricts access by source IP, add Anthropic’s egress range to its allowlist. Hand this page to the team that manages it.

##  Add Anthropic’s egress range to your allowlist

Requests from Claude to your services originate from Anthropic’s network. To let them through, add Anthropic’s published egress range to the service’s allowlist:

160.79.104.0/21

The authoritative list is [Anthropic’s published IP addresses](https://platform.claude.com/docs/en/api/ip-addresses); check it when you create the rule.
The range is shared across Anthropic services, and dedicated per-organization egress addresses aren’t available, so the allowlist entry admits Anthropic’s infrastructure as a whole. Your credential’s [allowed websites](/docs/claude-tag/admins/add-connections#set-allowed-websites) are what scope which of *your* systems Claude can call.
Allowlist changes on enterprise systems can take days to take effect, which is why the [setup overview](/docs/claude-tag/admins/setup-overview#before-you-start) sends you here before step 1.

##  Internet reachability

A connected service must accept traffic from the internet (restricted by IP allowlist if you like). A service reachable only inside your private network can’t be connected; private networking such as PrivateLink or VPC peering is not supported.

##  IP allowlist vs. allowed websites

The IP allowlist on your service and the [allowed websites](/docs/claude-tag/admins/add-connections#set-allowed-websites) on a connection are opposite sides of the same boundary:

|  | IP allowlist | Allowed websites |
| --- | --- | --- |
| **Who configures it** | Your team, on your service | You, on the connection in Claude |
| **What it decides** | Which networks may reach the service | Which hosts a credential may be sent to |

##  Events and webhooks

Events from connected services, like GitHub activity, are delivered directly to Anthropic, so there is no inbound listener to configure on your side.

* [Add connections](/docs/claude-tag/admins/add-connections#set-allowed-websites): the allowed-websites setting (the other direction: what Claude is allowed to reach)
* [How agent identity works](/docs/claude-tag/concepts/agent-identity): how credentials are injected at the network boundary
* [Setup overview](/docs/claude-tag/admins/setup-overview): back to the console flow once the allowlist is in place

[Migrate from legacy Claude in Slack](/docs/claude-tag/admins/migrate-from-earlier)[Get started](/docs/claude-tag/users/getting-started)
