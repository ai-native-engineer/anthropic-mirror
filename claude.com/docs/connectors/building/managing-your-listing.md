<!-- source: https://claude.com/docs/connectors/building/managing-your-listing -->

Organizations that submit to the [Connectors Directory](/docs/connectors/directory) get a submissions dashboard in Claude.ai at [Admin settings > Directory](https://claude.ai/admin-settings/directory/submissions). Use it to track submissions through review, monitor your published server’s health and usage, and edit your listing.

The dashboard covers directory-listed remote MCP servers only. Custom connectors and local servers (desktop extensions) don’t appear here, and the dashboard shows only your own organization’s submissions.

##  Access the dashboard

The dashboard is part of your organization’s admin settings, so you need:

* **A Team or Enterprise organization**
* **Directory management access.** By default, only organization Owners and Primary owners have it. On Enterprise, an Owner can delegate access through a custom role with the **Directory management** or **Libraries** permission; see [Before you start](/docs/connectors/building/submission#before-you-start) for the steps. Team plans don’t have custom roles, so on Team this stays with Owners.

The same access covers everything on this page: viewing submissions, metrics, and reviewer feedback, and editing and submitting listings.

##  Track submission status

The dashboard lists each of your organization’s submissions with its current status. Open a submission to see its full details and any reviewer feedback. When reviewers request changes, their feedback appears on the submission’s detail page; address it and resubmit from the same page.

##  Server health and usage metrics

Metrics are in beta. They’re computed daily from directory usage and can lag by up to 24 hours. Time windows with fewer than 5 calls, and per-product rows with fewer than 50 calls, are omitted.

Once your server is published, its detail page shows health and usage data.

###  Health

The health badge summarizes your server’s recent reliability:

| Status | Meaning |
| **Healthy** | The 30-day disconnect rate is at or below 5% |
| **Degraded** | The 30-day disconnect rate is above 5% |
| **Collecting…** | The server is published, but metrics haven’t been computed yet (metrics update daily) |
| **Not live** | The server isn’t published yet; health appears after publication |

###  Topline metrics

* **Directory rank**: your position in the directory, ranked by 30-day active users. A “Trending” tag marks servers in the top 10 by recent growth.
* **Active users (30d)**: distinct accounts that called your server.
* **Tool calls (30d)**: total tool calls, shown with the disconnect rate.
* **Error rate (30d)**: overall error rate, shown with the most common error types.

###  Error breakdown

A table breaks errors out over 1-day, 7-day, and 30-day windows: total calls, overall error rate, tool versus request error rates, HTTP 4xx and 5xx rates, and the top error types in each window.

###  Usage by product

A per-product table shows 7-day calls, error rate, and p50/p95/p99 latency for each Claude surface your server is used from, such as Claude.ai, Claude Desktop, Claude Code, and Cowork.
Error rates reflect traffic through Anthropic’s HTTP proxy, so servers reached only via legacy WebSocket won’t show data here. A high rate on a single product may reflect a client-side issue on Anthropic’s end rather than a problem with your server.

###  Usage by tool

A per-tool table shows 7-day calls, the overall error rate, and the tool-result error rate for your top 15 tools by call volume.

##  Edit your listing

Open your submission’s detail page to edit the listing. You can change directly:

* **Listing metadata**: tagline, description, categories, documentation and privacy policy links, support contact, and icon
* **Company details**: company name and website
* **Display name**: editable, but changing the name of a published server affects existing users and requires re-review

Save your edits as you go, then submit them for review. Submitted changes show as pending until a reviewer approves them, and you can discard pending changes before they’re approved.
The URL slug is locked: it’s permanent after publication, since it determines your listing URL.
For other edits or escalations, email `[email protected]`.

[After publishing](/docs/connectors/building/after-publishing)[MCPB (desktop extensions)](/docs/connectors/building/mcpb)
