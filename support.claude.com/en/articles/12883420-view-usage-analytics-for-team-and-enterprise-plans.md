<!-- source: https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans -->

# View usage analytics for Team and Enterprise plans

Updated this week

This article explains how to view and export usage analytics for your organization.

Usage analytics are available to Team plan Owners and Primary Owners, and Enterprise plan Owners, Primary Owners, and Admins. Enterprise Admins can view all analytics except Spend.

Usage analytics help you track team activity, feature adoption, and spend directly from your admin dashboard. You can monitor how your organization uses Claude and export detailed reports for your own analysis.

Primary Owners and Owners can access analytics via dedicated Analytics settings by clicking your initials in the lower left corner and selecting **[Analytics](https://claude.ai/analytics/activity)** from the menu. Additionally, the Claude.ai, Claude Code, and Cowork options offer product-specific analytics.

## All activity

This page includes the following analytics:

## Usage

* Weekly active users (WAU)
* Utilization rates (WAU / total seats)
* Pending invites
* Daily, weekly, and monthly active users, with filters for Claude (chat), Claude Code, and Claude Cowork
* Top connectors

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2153394909/693f3ae0ec2ea158a1f1e233c024/CleanShot+2026-03-11+at+14_52_44%402x.png?expires=1782460800&signature=18e412a29c256830ccb3115147881d294af6fb16cdca19ac9ae31a96ce291a82&req=diEiFcp3mYhfUPMW1HO4zbQxEME1CSJqSPAYazQ9kuIjV9QITLgUowQJLdHV%0AR%2BfG7vvZCHtXxQ%2Bpgh0%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2153394909/693f3ae0ec2ea158a1f1e233c024/CleanShot+2026-03-11+at+14_52_44%402x.png?expires=1782460800&signature=18e412a29c256830ccb3115147881d294af6fb16cdca19ac9ae31a96ce291a82&req=diEiFcp3mYhfUPMW1HO4zbQxEME1CSJqSPAYazQ9kuIjV9QITLgUowQJLdHV%0AR%2BfG7vvZCHtXxQ%2Bpgh0%3D%0A)

## Spend

**Note:** If you're on a **[seat-based Enterprise plan](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans#h_6a78e30e26)**, spend reports only appear if your organization has **[enabled usage credits](https://support.claude.com/en/articles/12005970-)**. The spend data covers overage spend only—usage within seat-based allotments isn't included.

This section includes the following analytics:

* Total spend (month-to-date, quarter-to-date, year-to-date) — the graph shows your actual spend and list price
* Spend by model (1 month, 3 months, 1 year)
* Top 10 users by spend leaderboard

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2434747802/80667668d997d87426b7c04fd54c/SpendGraph.png?expires=1782460800&signature=ededfdb9fd502a7ce6de9f3d71326aaf871646728bc183b373237e01bccf58ec&req=diQkEs56molfW%2FMW1HO4zfK6rvnpOpAHHjVUKeN2QU8KOAMjIW%2Bg3U5b%2FPNy%0ALQC4rNWNgEZ4rvUW6gM%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2434747802/80667668d997d87426b7c04fd54c/SpendGraph.png?expires=1782460800&signature=ededfdb9fd502a7ce6de9f3d71326aaf871646728bc183b373237e01bccf58ec&req=diQkEs56molfW%2FMW1HO4zfK6rvnpOpAHHjVUKeN2QU8KOAMjIW%2Bg3U5b%2FPNy%0ALQC4rNWNgEZ4rvUW6gM%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2153419527/18cba69667e2af1a6f4f2e5ca2c5/CleanShot+2026-03-11+at+15_03_28%402x.png?expires=1782460800&signature=fad5d785db50a8e8c9776c5b83d0e65a3377814fa29ccacb1d523405cb1819d6&req=diEiFc1%2FlIRdXvMW1HO4zdGt%2BiasDf9hP9LVpsbj5NelsVn9EBIrRibEhq0T%0Ae2wVfNCPENY%2B3y0Sw4Y%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2153419527/18cba69667e2af1a6f4f2e5ca2c5/CleanShot+2026-03-11+at+15_03_28%402x.png?expires=1782460800&signature=fad5d785db50a8e8c9776c5b83d0e65a3377814fa29ccacb1d523405cb1819d6&req=diEiFc1%2FlIRdXvMW1HO4zdGt%2BiasDf9hP9LVpsbj5NelsVn9EBIrRibEhq0T%0Ae2wVfNCPENY%2B3y0Sw4Y%3D%0A)

**Note:** The spend leaderboard can be delayed by one to two days. For more current month-to-date spend per user, refer to spend limits by person in **[Organization settings > Usage](https://claude.ai/admin-settings/usage)**.

## Export a spend report

You can export a detailed cost and usage report as a CSV file. The report provides per-user, per-model visibility into token usage and estimated spend within a selected time period, updated daily.

To export spend data:

1. Navigate to **[Settings > Analytics](https://claude.ai/analytics/activity)**.
2. Scroll down to the **Spend** section.
3. Click the "Export Spend Report" button.
4. Select a time period: MTD, Last Month, Last 90 Days, or Custom.
5. If you select "Custom," choose your start and end dates. You can go back up to 90 days, and the most recent data available is from yesterday.
6. Click "Download."

### What's included in the report?

Each row in the CSV represents a specific person's usage of a specific model, with spend summed across the entire date range selected for the export. The report includes the following fields:

* User's email
* Account UUID
* Product (such as Chat, Claude Code, Cowork, or Office Agents)

  + Office Agents aggregates usage from the Claude add-ins for Excel, PowerPoint, and Word.
* Model and model family
* Request count (`total_requests`)

  + The count of individual API calls made to Claude. Each time an app or user sends a message and gets a response, that counts as a request.
* Prompt tokens (`total_prompt_tokens`)

  + The number of tokens consumed by the input side of each request. This includes system prompts, conversation history, user messages, tool definitions, etc.
* Completion tokens (`total_completion_tokens`)

  + The number of tokens generated by Claude when it responds*,* including extended thinking tokens.
* Net spend (`total_net_spend_usd`)

  + Your cost (in USD) after any discounts, credits, or negotiated rates are applied. This is what you actually spent.
* Gross spend (`total_gross_spend_usd`)

  + Your cost (in USD) before any discounts or credits.

Analytics chat, the Analytics API, and exported spend reports from the analytics dashboard should closely match your invoice. The cost and usage endpoints of the Analytics API export include both discounted price and list price.

**Note:** Some activity previously grouped under Claude Code, including Code Review and security features, now appears as separate line items.

**Important:** Spend data refreshes daily and has a one-day delay. For usage-based Enterprise plans, the export captures your organization's full usage. For seat-based Enterprise plans with usage credits enabled, **the export only reflects spend that exceeds your seat allotment.**

## Claude.ai

Navigate to **[Analytics > Claude.ai](https://claude.ai/analytics/usage)** to view usage and activity metrics for your organization. This page includes the following analytics:

## Chats

* Chats per day
* Percentage of users with 1 or more chat
* Total number of chats (1 week, 1 month, 3 months, 1 year)

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916169034/e3e557f223fcd6976fa5b6353095/CleanShot+2026-01-05+at+15_32_41.png?expires=1782460800&signature=b5b9fa10de26b036e1bba6771a5027d2a08b08f8441e5817d66e7b8c1340f714&req=dSkmEMh4lIFcXfMW1HO4zZyh9TGa%2BIlzRyyyIe2wZ0Uoo2BI%2BLg3knO7IPFo%0A2n5bk1gwW76Bpo04OS8%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916169034/e3e557f223fcd6976fa5b6353095/CleanShot+2026-01-05+at+15_32_41.png?expires=1782460800&signature=b5b9fa10de26b036e1bba6771a5027d2a08b08f8441e5817d66e7b8c1340f714&req=dSkmEMh4lIFcXfMW1HO4zZyh9TGa%2BIlzRyyyIe2wZ0Uoo2BI%2BLg3knO7IPFo%0A2n5bk1gwW76Bpo04OS8%3D%0A)

## Projects

* Projects created per day
* Percentage of users with 1 or more project
* Top 10 users by projects used (month-to-date, quarter-to-date, year-to-date, 1 year)

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916170133/666961061f9a044385e0ea1debdd/CleanShot+2026-01-05+at+15_36_27.png?expires=1782460800&signature=716329faaba0fcf9f858c16b6b3b9b656306be0fbe6433f5d5f95eab808add2a&req=dSkmEMh5nYBcWvMW1HO4zed16ibq2xhSqVPXIl8sPeaHP8HckHijOTyV72%2F9%0A6h77OEn62PpF8f7BoFY%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916170133/666961061f9a044385e0ea1debdd/CleanShot+2026-01-05+at+15_36_27.png?expires=1782460800&signature=716329faaba0fcf9f858c16b6b3b9b656306be0fbe6433f5d5f95eab808add2a&req=dSkmEMh5nYBcWvMW1HO4zed16ibq2xhSqVPXIl8sPeaHP8HckHijOTyV72%2F9%0A6h77OEn62PpF8f7BoFY%3D%0A)

## Artifacts

* Artifacts created per day
* Percentage of users with 1 or more artifact
* Top 10 users by artifacts generated (month-to-date, quarter-to-date, year-to-date, 1 year)

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916171160/cd17d2abba34659b9d8f6231df5a/CleanShot+2026-01-05+at+15_37_20.png?expires=1782460800&signature=59308a2cbdb4894fe39e2755a7da844af81321edd0075d799cad09c329102932&req=dSkmEMh5nIBZWfMW1HO4zXYF0VvmuwDx4Jgm1Axxim2XgZobbVJUJjR13Zk3%0ANWviEHYpo%2BQ8ZBzxjDI%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1916171160/cd17d2abba34659b9d8f6231df5a/CleanShot+2026-01-05+at+15_37_20.png?expires=1782460800&signature=59308a2cbdb4894fe39e2755a7da844af81321edd0075d799cad09c329102932&req=dSkmEMh5nIBZWfMW1HO4zXYF0VvmuwDx4Jgm1Axxim2XgZobbVJUJjR13Zk3%0ANWviEHYpo%2BQ8ZBzxjDI%3D%0A)

## Claude Code analytics

Navigate to **[Analytics > Claude Code](https://claude.ai/analytics/claude-code)** to view usage and activity metrics for your organization. For more specific details, refer to **[Claude Code usage analytics](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)**.

## Claude Cowork analytics

Navigate to **[Analytics > Cowork](https://claude.ai/analytics/cowork)** to view usage and activity metrics for Claude Cowork across your organization. This page includes:

* Cowork sessions per day
* Percentage of users with one or more Cowork sessions
* Daily, weekly, and monthly active Cowork users

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2253604219/0d21918d55e10b3e5d2a92e65c90/42a47632-08c2-4557-a087-fc080c4dda80?expires=1782460800&signature=13d26cff42e29d019bdf435cd06d206579bae567e084e2b048c39746f98f87fa&req=diIiFc9%2BmYNeUPMW1HO4zSCqp6YDEn8W8zs2pRdG0k7fK%2BxmkUj1XSwg54cL%0AQImFrGuLRfdaU8V0Juk%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2253604219/0d21918d55e10b3e5d2a92e65c90/42a47632-08c2-4557-a087-fc080c4dda80?expires=1782460800&signature=13d26cff42e29d019bdf435cd06d206579bae567e084e2b048c39746f98f87fa&req=diIiFc9%2BmYNeUPMW1HO4zSCqp6YDEn8W8zs2pRdG0k7fK%2BxmkUj1XSwg54cL%0AQImFrGuLRfdaU8V0Juk%3D%0A)

**Note:** Cowork analytics are available alongside Chat and Claude Code data in the **[Analytics API](https://platform.claude.com/docs/en/manage-claude/analytics-api)**.

## Access your analytics data programmatically

If you’re on an Enterprise plan and want to pull analytics data into your own dashboards or reporting tools, the Analytics API gives you programmatic access to the same usage and engagement metrics available in the analytics dashboard. To get started, refer to our **[Analytics API docs](https://platform.claude.com/docs/en/manage-claude/analytics-api)**.

[What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)[Manage usage credits for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans)[Claude Code usage analytics](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)[Use analytics chat to ask Claude about usage](https://support.claude.com/en/articles/14729354-use-analytics-chat-to-ask-claude-about-usage)[Claude Enterprise consumption guide](https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide)
