<!-- source: https://support.claude.com/en/articles/9534590-cost-and-usage-reporting-in-the-claude-console -->

**Note:** Usage and Cost reporting is visible to the following user roles: **Developer, Billing, and Admin**. See [Claude Console Roles and Permissions](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions) for more information.

The Claude Console provides detailed cost and usage reporting to help you effectively manage your API usage and associated costs. This guide walks you through these features and how to use them.

## Accessing Cost and Usage Reports

Users with access to these reports can click into them on the left navigation menu on the Console:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584654217/db0a977417e38e43639f060d96e0/image.png?expires=1787358600&signature=e075192061b724dea6d960fa27820e23c771e648161529393f04b46127338d55&req=dSUvEs97mYNeXvMW1HO4zYCWiSMbhM6cuqqBX2puyxTadzYx8D1g8yGo%2F3WM%0AbIC%2F64ZEyfea09RKM1U%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584654217/db0a977417e38e43639f060d96e0/image.png?expires=1787358600&signature=e075192061b724dea6d960fa27820e23c771e648161529393f04b46127338d55&req=dSUvEs97mYNeXvMW1HO4zYCWiSMbhM6cuqqBX2puyxTadzYx8D1g8yGo%2F3WM%0AbIC%2F64ZEyfea09RKM1U%3D%0A)

---

## Usage Reporting

The [Usage page](https://platform.claude.com/usage) offers a detailed breakdown of your API usage across different models and API keys.

### Key Features

* **Detailed Breakdown**: View usage data by model, date/time, and API key. Click into the bars on the bar chart for hour and minute granularity.
* **Flexible Filtering**: Use selectors to choose specific models, months, or API keys
* **Visual Representation**: A chart with input and output token counts.
* **Usage Statistics**: See total input and output tokens for your selected filters.
* **Rate-Limited Requests:** Review your requests that were blocked due to hitting rate limits.
* **Rate Limit Use:** Visualizations of input and output tokens per minute compared with the overall ITPM or OTPM rate limit.
* **CSV Export**: Download your usage data for further analysis or reporting.

### How to Use

1. Select the Workspace you want to view (or choose "All Workspaces").
2. Select the model you want to view (or choose "All Models").
3. Choose the month you're interested in (or narrow to a specific month/day).
4. Select an API key (or view data for all keys).
5. The chart and statistics will update based on your selections.
6. Use the export button to download a CSV of the displayed data.

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584664321/59b50eba0b61e0789f7055fcf9f4/image+%285%29.png?expires=1787358600&signature=c42cfa0d805eb3ab7666ec5110b0378cff30de382f50f808910ed7ce3d80ec66&req=dSUvEs94mYJdWPMW1HO4zQwER3QpJIdgqMITUZbanFBwZub2VwDw5hFsWsaY%0Az50BGN8hZXV7uf512rs%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584664321/59b50eba0b61e0789f7055fcf9f4/image+%285%29.png?expires=1787358600&signature=c42cfa0d805eb3ab7666ec5110b0378cff30de382f50f808910ed7ce3d80ec66&req=dSUvEs94mYJdWPMW1HO4zQwER3QpJIdgqMITUZbanFBwZub2VwDw5hFsWsaY%0Az50BGN8hZXV7uf512rs%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584693386/aed472efe163abcbc14fa32f3699/rate+limited+requests.png?expires=1787358600&signature=dcd4e62eb4ebee50508d5a139b54b332c532a84cbf649f8df0b746936183ce94&req=dSUvEs93noJXX%2FMW1HO4zRxEwWxO41lq21D6pckxWMaJsEEuPZQv7uXuw5zb%0AC9rvsmrx9o1XMI%2BCCNg%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584693386/aed472efe163abcbc14fa32f3699/rate+limited+requests.png?expires=1787358600&signature=dcd4e62eb4ebee50508d5a139b54b332c532a84cbf649f8df0b746936183ce94&req=dSUvEs93noJXX%2FMW1HO4zRxEwWxO41lq21D6pckxWMaJsEEuPZQv7uXuw5zb%0AC9rvsmrx9o1XMI%2BCCNg%3D%0A)

### Rate Limit Use

The Usage page also includes a separate section displaying rate limit use per-model for input and output tokens. You can click the dropdown in the upper left corner of this section to change the model and view related rate limit metrics. These visualizations can be used to determine when you’re hitting peak use for your organization, which specific rate limits need to be increased, and how you can increase your caching rate.

**Rate Limit Use + Caching - Input Tokens:** This chart displays the hourly maximum number of uncached input tokens per minute (ITPM) alongside your cache rate (i.e. the percentage of input tokens read from the cache) and your current ITPM rate limit.

**Rate Limit Use - Output Tokens:** This chart displays the hourly maximum number of output tokens per minute (OTPM) alongside your current OTPM rate limit.

---

## Cost Reporting

The [Cost page](https://platform.claude.com/cost) helps you understand your spending across different models.

### Key Features

* **Model-Specific Data**: View costs for individual models or all models combined.
* **Monthly Breakdown**: See costs for specific months.
* **Daily Cost Chart**: Visualize your spending over time.
* **Total Cost Statistics**: Get an overview of your total spending for the selected period, including web search and code execution costs.
* **CSV Export**: Download cost data for your records for further analysis.

### How to Use

1. Choose the Workspace you want to view costs for (or select "All Workspaces").
2. Choose the model you want to view costs for (or select "All Models").
3. Select the month you're interested in.
4. You can see the chart, token cost, and tool use costs, which will update based on your selections.
5. Use the export button to download a CSV of the cost data.

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584679401/4d0bc8ed08625e1adee414e77030/CleanShot+2025-06-23+at+08_54_40%402x.png?expires=1787358600&signature=cd3b76c49acad132acfa845b979bd12af8b2b0e5944e6d066bc2a39080cff2b4&req=dSUvEs95lIVfWPMW1HO4zUR%2Bh5vAVthnCyIF5nuUsbwG6HfYjI52u8if1ra2%0AM99jqhkRCMiy0ux5MyA%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584679401/4d0bc8ed08625e1adee414e77030/CleanShot+2025-06-23+at+08_54_40%402x.png?expires=1787358600&signature=cd3b76c49acad132acfa845b979bd12af8b2b0e5944e6d066bc2a39080cff2b4&req=dSUvEs95lIVfWPMW1HO4zUR%2Bh5vAVthnCyIF5nuUsbwG6HfYjI52u8if1ra2%0AM99jqhkRCMiy0ux5MyA%3D%0A)

**Note**: Currently, it's not possible to break down usage or cost by individual users.

* [Claude Console roles and permissions](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions)
* [Manage usage credits for paid Claude plans](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)
* [View usage analytics for Team and Enterprise plans](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans)
* [Models, usage, and limits in Claude Code](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)
* [Claude Enterprise consumption guide](https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide)
