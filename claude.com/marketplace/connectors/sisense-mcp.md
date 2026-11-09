<!-- source: https://claude.com/marketplace/connectors/sisense-mcp -->

Connector URL`https://mcp.sisense.com/mcp`

More[Documentation (opens in new tab)](https://docs.sisense.com/main/SisenseLinux/mcp-server.htm)[Support (opens in new tab)](https://sisense.com/support/)[Privacy policy (opens in new tab)](https://sisense.com/about/legal/privacy-policy/)

Sisense connects Claude to your organization's analytics, so you can ask questions of governed company data in plain language and get answers grounded in the models your data team maintains. No query language, no dashboard hunting.

Admins, one setting first: add https://\*.claudemcpcontent.com to Sisense's CORS allowed origins. Without it, charts and dashboards don't render and users get text only.

Self-hosted Sisense: Add to Claude works only for Sisense Managed Cloud. Self-hosted customers add a custom connector with their own /mcp URL: https://docs.sisense.com/main/SisenseLinux/mcp-connect-ai-agent.htm

What you can do:

- Discover the data sources your account can access

- Inspect a model's tables and fields, and how they join

- Ask a business question in plain language. Sisense builds and runs the query and returns the numbers.

- Chart the result, then refine it: add a filter, switch the chart type, break a metric down another way. Each turn builds on the last.

- Open an existing dashboard, or build one from charts in the chat, then filter it or add an AI summary. Dashboards are drafts in the chat and are never saved to Sisense.

- Check your Pulses: see what fired, why, and the data behind it.

Charts and dashboards render as live Sisense visualizations in the conversation, using the same engine as your Sisense dashboards, so you can explore them instead of looking at a static image.

Access and governance: every request runs as the signed-in Sisense user, and existing permissions and data security apply unchanged. The connector never creates, edits or deletes dashboards, widgets, models or data. Running a Pulse on demand sends its notifications if it fires.

Before you connect, you need a Sisense account on an instance with Sisense Intelligence (Cloud-Linked Features) enabled, and access to the data you want to ask about.

## Tools

* getDataSources
* getDataSourceFields
* getDataPreview
* buildQuery
* loadSkill
* createWidget
* updateWidgetTitle
* updateChartType
* rebindWidgetQuery
* updateWidgetSorting
* updateChartTrendForecast
* updateWidgetStyle
* updateWidgetDataOptions
* updateChartMeasureTypes
* loadDashboard
* createDashboard
* addDashboardWidgets
* removeDashboardWidgets
* replaceDashboardWidgets
* addDashboardFilters
* addDashboardNarration
* updateDashboardTitle
* updateDashboardRowHeight
* listPulses

Show all 30 tools

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://assets.claude.com/a8994e05e594a562449127d44e0fe86c31d8e41c.svg?w=128&fit=max&auto=format)

### [Google Drive](https://claude.com/marketplace/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://assets.claude.com/89209c1f16bf517eb431ff08e811de0778d70689.svg?w=128&fit=max&auto=format)

### [Supabase](https://claude.com/marketplace/connectors/supabase)

Manage databases, authentication, and storage

[Add Supabase in Claude (opens in new tab)](https://claude.ai/directory/11ca66fc-1e98-49d5-ab9b-7cb4672a8f10 "Add in Claude")

![](https://assets.claude.com/11f81df36177359e07a76903f59116d6f7e4f856.jpg?w=128&fit=max&auto=format)

### [Box](https://claude.com/marketplace/connectors/box)

Search, edit and get insights on your Box content

[Add Box in Claude (opens in new tab)](https://claude.ai/directory/a5380429-c773-4180-b642-301418240c8c "Add in Claude")

![](https://assets.claude.com/7ef12b4f58f26b511f7bc69fbc6c583b926c2022.svg?w=128&fit=max&auto=format)

### [Salesforce - Beta](https://claude.com/marketplace/connectors/salesforce-headless-360)

Sell, serve, and operate at scale with Salesforce.

[Add Salesforce - Beta in Claude (opens in new tab)](https://claude.ai/directory/a352dbf6-c732-43d4-84c1-0bbb389d3921 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=vidiq.com&sz=96)

### [vidIQ](https://claude.com/marketplace/connectors/vidiq)

Research and create for YouTube, Instagram & TikTok

[Add vidIQ in Claude (opens in new tab)](https://claude.ai/directory/dc5bb20f-6ebd-4dbe-a47e-c2d20fa25acc "Add in Claude")

![](https://assets.claude.com/47f22a5129fd644c95a682e474b104001065dd42.jpg?w=128&fit=max&auto=format)

### [Zapier](https://claude.com/marketplace/connectors/zapier)

Automate workflows across thousands of apps via conversation

[Add Zapier in Claude (opens in new tab)](https://claude.ai/directory/1f6f271e-3d29-4241-b35e-8abe6def4891 "Add in Claude")
