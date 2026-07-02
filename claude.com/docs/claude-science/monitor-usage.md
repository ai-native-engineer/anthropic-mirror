<!-- source: https://claude.com/docs/claude-science/monitor-usage -->

Claude Science usage counts against each member’s standard weekly quota and uses the same seat as the rest of claude.ai. You can track adoption in the Activity dashboard and through the Admin API.

##  Analytics in Organization settings

Go to Organization settings > Analytics > All Activity and select Claude Science in the product filter to see active members, sessions, and spend for this product.
The Monitor usage link on the Claude Science row in Organization settings > Capabilities links to Analytics.

##  Admin API

The Claude Enterprise Admin API (Enterprise plans only) returns Claude Science usage alongside your other products.
Per-member metrics (GET /v1/organizations/analytics/users, science\_metrics object):

| Field | Description |
| --- | --- |
| distinct\_session\_count | Number of distinct Claude Science sessions. Null on aggregated rows where a distinct count can’t be computed. |
| message\_count | Number of messages sent in Claude Science sessions. |
| delegation\_count | Number of delegations (handoffs to a specialized agent) in Claude Science sessions. |
| remote\_compute\_job\_count | Number of remote compute jobs launched from Claude Science sessions. |
| skills\_used\_count | Total number of skill invocations in Claude Science sessions. |

See the Admin API reference for authentication and the full schema.

[Manage on devices](/docs/claude-science/manage-on-devices)[What's not available yet](/docs/claude-science/whats-not-available-yet)
