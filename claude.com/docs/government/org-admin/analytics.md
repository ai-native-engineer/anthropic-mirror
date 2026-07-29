<!-- source: https://claude.com/docs/government/org-admin/analytics -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

> **Who this is for:** Organization owners who need to understand how their organization is using Claude and how quickly it is consuming credits.

Use this page to review requests, tokens, spend, top users, and credit balance over time across your organization.
Because this data takes a moment to compute, the page starts with a **Load analytics** button. After the data loads, the results are cached for the rest of your session. You can click **Refresh** to fetch the latest numbers, and this button becomes available again 30 seconds after the previous load.

##  How the data is gathered

Usage figures on this page are compiled from the same metering that enforces your users’ rate limits, so the request, token, and spend numbers here will closely match what your users experienced. All times are shown in your browser’s time zone; if your browser reports a time zone the service does not recognize, times fall back to UTC.

##  Managed and self-managed views

A control at the top switches between **Anthropic-managed tiers** and **Self-managed tiers**. The two are shown separately because their economics differ: managed-tier seats are purchased as seats, while **self-managed tiers** (tiers your organization created itself on the [Tiers](https://claude.com/docs/government/org-admin/seat-tiers) page) draw down the billing account’s balance. Spend figures and the credit panel are therefore shown only in the **Self-managed** view. If your organization has only one kind of tier, only that tab is shown.

##  Credits (self-managed view only)

The credit panel and burndown chart only appear in the **Self-managed tiers** view, and only once credit data is available for your organization. The runway estimate within the panel only appears once there has been enough recent activity to compute a burn rate.

When credit data is available, the credit panel shows the current position of the account your organization draws from as of right now. It displays the **Credits remaining** out of the total added to the account, with a progress bar marked at the 70 percent and 90 percent warning thresholds. It also shows a runway estimate that tells you roughly how many days remain at your trailing 7-day burn rate, and it adds a **Depleted**, **Low balance**, or **Approaching limit** badge when one of those conditions applies.
The runway figure divides your remaining balance by your average daily spend over the last seven complete days. It is shown as “less than 1 day” when the balance is nearly exhausted and as “more than 180 days” when spend is low enough that a longer projection would not be meaningful. If there has been no spend at all in the last seven days, no runway is shown.
Below the panel, the **Credit burndown** chart plots your balance over the last 30 days, with markers on the days credits were added, and projects forward to the date you are estimated to reach $0.

The credit panel and burndown always reflect the current position and are not affected by the time-window selector described below. The 7-day lookback used for the burn rate is also fixed and does not change when you switch the usage window.

##  Active users

The **Active users** section shows how many distinct people used Claude over fixed periods: the average number of daily active users over the last 7 days, the number of weekly active users over the last 7 days, and the number of monthly active users over the last 30 days. These figures always use the same fixed lookbacks and are not affected by the time-window selector below.

##  Usage

Everything below the **Usage** divider is scoped to a time window that you choose with the **24 hours**, **7 days**, or **30 days** selector.
The summary tiles show the number of requests, the input and output token counts (a token is roughly a piece of a word, and it is the unit that Claude’s usage is measured in), and, in the self-managed view, the estimated spend for the selected window.
The **Token usage** chart plots input and output tokens over the window. It shows hourly data when you select the 24-hour window and daily data for the 7-day and 30-day windows.
The **Active users over time** chart plots the number of distinct users who made at least one request in each period of the window, using the same hourly or daily buckets as the token chart.
The **By product** table breaks usage down by which Claude product it came from (for example, Claude Desktop or Claude Code), with the same request, token, and spend columns as the other tables. This table only appears once your deployment has recorded usage from at least one product.
The **By model** table lists each model used in the window along with its request count, input tokens, output tokens, and, in the self-managed view, its spend.
The **Top users** table lists the most active users in the window with the same columns. The table starts with ten rows, and you can click **Show more** to reveal additional users. Up to 100 users are listed individually, and beyond that a note tells you how many more are not listed.

##  Things to know

* A user counts as **active** in the selected window if they made at least one request in it, regardless of which seat tier they were on at the time.
* The **spend** column appears only in the self-managed view and is the amount debited from your billing account’s balance. The managed view has no spend column because managed-tier usage is covered by the seat price rather than by credit drawdown.
* If the credit panel is missing from the self-managed view, credit data for your organization’s billing account is unavailable. The rest of the page will still load.
* Usage that was cleared with **Reset usage limits** on the [Users](https://claude.com/docs/government/org-admin/users) page still appears here. The reset only clears the counter that enforces a user’s limit; it does not remove the activity from analytics.
