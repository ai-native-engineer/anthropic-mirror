<!-- source: https://claude.com/connectors/maven-bio -->

[Skip to main content](#main-content)

Connector URL`https://mcp.mavenbio.com/`

More[Documentation (opens in new tab)](https://mavenbio.com/mcp/docs)[Support (opens in new tab)](mailto:help@mavenbio.io)[Privacy policy (opens in new tab)](https://mavenbio.com/mcp/privacy)

Maven Bio gives Claude real-time structured life sciences data. Drug products, companies, clinical trials, indications, deals, financings, mechanisms, and targets, linked to each other and to the source documents behind them.

Ask in plain language. Claude resolves the entity, pulls canonical records, then reads the primary source. "AZD6738" and "ceralasertib" land on the same drug. A landscape query returns the programs in a given indication. A claim about an approval traces back to the FDA letter itself.

The Maven Bio connector enables:

- Resolving messy names, aliases, and internal codes to canonical entities

- Proactively monitoring opportunities: FDA actions, trial readouts, and press releases scoped to the entities a monitor tracks, each signal carrying its source

- Discovery by criteria: "Phase 3 KRAS G12C inhibitors," "public oncology companies with late-stage pipelines"

- Competitive landscaping by indication, grouped by phase, company, or mechanism

- Evidence-based analysis: Search and read FDA filings, SEC filings, clinical papers, press releases, and conference abstracts as full text, structured sections, or extracted citations

- Deal benchmarking: Public-company financials, financing rounds, and BD deals filterable by indication

- Counts and aggregations across the entity graph

Maven Bio MCP server authenticates every call, enforces read-only access and response limits. Users sign in with OAuth 2.1 against their existing Maven Bio identity.

## Tools

* aggregate\_records
* fetch\_related
* get\_artifact
* get\_deals
* get\_financials
* get\_financings
* get\_monitors
* get\_recent\_events
* list\_artifacts
* match\_entity
* read\_document
* research\_bio\_evidence
* research\_entity
* research\_landscape
* search\_documents
* search\_entities

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://drive.google.com&size=64)

### [Google Drive](https://claude.com/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://calendar.google.com&size=64)

### [Google Calendar](https://claude.com/connectors/google-calendar)

Manage your schedule and coordinate meetings effortlessly

[Add Google Calendar in Claude (opens in new tab)](https://claude.ai/directory/2a838eaa-f7b4-4bc2-bd47-c326f3c813c5 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=microsoft.com&sz=96)

### [Microsoft 365](https://claude.com/connectors/microsoft-365)

Access your company's SharePoint, OneDrive, Outlook, and Teams directly in Claude

[Add Microsoft 365 in Claude (opens in new tab)](https://claude.ai/directory/ce0c9cda-5ea5-44c5-9cf2-40810dfa6582 "Add in Claude")

![](https://www.notion.so/images/notion-logo-block-main.svg)

### [Notion](https://claude.com/connectors/notion)

Connect your Notion workspace to search, update, and power workflows across tools

[Add Notion in Claude (opens in new tab)](https://claude.ai/directory/69f3a300-cc60-48c4-b237-dfac56530dbf "Add in Claude")

![](https://www.google.com/s2/favicons?domain=atlassian.com&sz=96)

### [Atlassian Rovo](https://claude.com/connectors/atlassian)

Access Jira & Confluence from Claude

[Add Atlassian Rovo in Claude (opens in new tab)](https://claude.ai/directory/11ba10d9-477b-4988-bd1c-90a7fa680dc1 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=slack.com&sz=96)

### [Slack](https://claude.com/connectors/slack)

Send messages, create canvases, and fetch Slack data

[Add Slack in Claude (opens in new tab)](https://claude.ai/directory/597f662f-36de-437e-836e-5a81013cbfbe "Add in Claude")
