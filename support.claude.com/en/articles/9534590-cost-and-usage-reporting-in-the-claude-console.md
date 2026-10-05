<!-- source: https://support.claude.com/en/articles/9534590-cost-and-usage-reporting-in-the-claude-console -->

**Note:** Usage and Cost reporting is visible to the following user roles: **Developer, Billing, and Admin**. See [Claude Console Roles and Permissions](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions) for more information.

The Claude Console provides detailed cost and usage reporting to help you effectively manage your API usage and associated costs. This guide walks you through these features and how to use them.

## Accessing Cost and Usage Reports

Users with access to these reports can click into them on the left navigation menu on the Console:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584654217/db0a977417e38e43639f060d96e0/image.png?expires=1791161100&signature=31557c807b988d9db42dfcc334517061f737fd5376e76570187be6f8ead965bb&req=dSUvEs97mYNeXvMW1HO4zYCWiCUZh8ebuqqBX2puyxRncJUA8XiZFCDPkIrh%0A2r1Y9RuUZj7On9VQv8U%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584654217/db0a977417e38e43639f060d96e0/image.png?expires=1791161100&signature=31557c807b988d9db42dfcc334517061f737fd5376e76570187be6f8ead965bb&req=dSUvEs97mYNeXvMW1HO4zYCWiCUZh8ebuqqBX2puyxRncJUA8XiZFCDPkIrh%0A2r1Y9RuUZj7On9VQv8U%3D%0A)

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

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584664321/59b50eba0b61e0789f7055fcf9f4/image+%285%29.png?expires=1791161100&signature=69f7904da84a4686b1707c508cf4db841a1050ce00705a6b0167ab80c5700a25&req=dSUvEs94mYJdWPMW1HO4zQwERnIrJ45nqMITUZbanFCO3teO5FKCKImzlRXV%0AqCIhSjGY6PSqpGKbCKE%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584664321/59b50eba0b61e0789f7055fcf9f4/image+%285%29.png?expires=1791161100&signature=69f7904da84a4686b1707c508cf4db841a1050ce00705a6b0167ab80c5700a25&req=dSUvEs94mYJdWPMW1HO4zQwERnIrJ45nqMITUZbanFCO3teO5FKCKImzlRXV%0AqCIhSjGY6PSqpGKbCKE%3D%0A)

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584693386/aed472efe163abcbc14fa32f3699/rate+limited+requests.png?expires=1791161100&signature=408ecc740d33d2814cf3d44a2217d4a6809bc151156a9cc3686b24b58daef4a0&req=dSUvEs93noJXX%2FMW1HO4zRxEwGpM4FBt21D6pckxWMZYKEEOPauAedjfw8dM%0A10ht1ZdYLwLjXG1D1YY%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584693386/aed472efe163abcbc14fa32f3699/rate+limited+requests.png?expires=1791161100&signature=408ecc740d33d2814cf3d44a2217d4a6809bc151156a9cc3686b24b58daef4a0&req=dSUvEs93noJXX%2FMW1HO4zRxEwGpM4FBt21D6pckxWMZYKEEOPauAedjfw8dM%0A10ht1ZdYLwLjXG1D1YY%3D%0A)

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

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584679401/4d0bc8ed08625e1adee414e77030/CleanShot+2025-06-23+at+08_54_40%402x.png?expires=1791161100&signature=6d65eca2c7bc36485941cb1af7a40715511646bd9848fda92eb6607e09fbbfd4&req=dSUvEs95lIVfWPMW1HO4zUR%2Bhp3CVdFgCyIF5nuUsbwHgSEgaCagNoPK3Xwx%0ABk9PfP2tizo%2BSXUrImc%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584679401/4d0bc8ed08625e1adee414e77030/CleanShot+2025-06-23+at+08_54_40%402x.png?expires=1791161100&signature=6d65eca2c7bc36485941cb1af7a40715511646bd9848fda92eb6607e09fbbfd4&req=dSUvEs95lIVfWPMW1HO4zUR%2Bhp3CVdFgCyIF5nuUsbwHgSEgaCagNoPK3Xwx%0ABk9PfP2tizo%2BSXUrImc%3D%0A)

**Note**: Currently, it's not possible to break down usage or cost by individual users.

* [Manage usage credits for paid Claude plans](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)
* [View usage analytics for Team and Enterprise plans](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans)
* [Claude Code on Console to Enterprise migration](https://support.claude.com/en/articles/14128775-claude-code-on-console-to-enterprise-migration)
* [Models, usage, and limits in Claude Code](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)
* [Claude Enterprise consumption guide](https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide)
