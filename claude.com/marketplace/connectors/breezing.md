<!-- source: https://claude.com/marketplace/connectors/breezing -->

Connector URL`https://mcp.breezing.io/mcp`

More[Documentation (opens in new tab)](https://learn.breezing.io/mcp/introduction)[Support (opens in new tab)](mailto:hello@breezing.io)[Privacy policy (opens in new tab)](https://breezing.io/privacy/)

Breezing is crypto accounting software for accountants, finance teams and Web3 businesses. It imports transactions from more than 70 blockchains and exchanges, prices them in your base currency, computes cost basis and net gain or loss, and books journals to Xero, QuickBooks Online and Bexio.

The Breezing connector gives Claude the same Public API your team uses behind the dashboard. Claude can list companies, wallets, transactions, balances, contacts, rules, reports and tasks. It can categorize transactions by assigning accounts from your chart of accounts, create and apply rules for recurring patterns, group trades and internal transfers, lock closed periods, start balance and net gain or loss calculations, generate token and account reports, and trigger the sync to your accounting platform.

What it never does: the connector cannot move funds. Breezing reads blockchain and exchange data through public addresses and read-only exchange keys, and it has no ability to sign transactions or transfer assets. It also never deletes records. Destructive actions stay in the Breezing dashboard.

Every tool that changes data is flagged, so Claude asks you to confirm before it writes. Access uses a Breezing API key you create in your company settings, scoped to the companies you choose with read or write permission per company, and you can revoke it at any time.

Setup: sign in to Breezing, create an API key under Company settings, then add the Breezing connector in Claude and paste the key on the authorization page. Documentation: https://learn.breezing.io/mcp/introduction

## Tools

* active\_issues\_list
* active\_issues\_refresh
* assets\_list
* assets\_update
* balances\_calculate
* balances\_get
* bexio\_accounts\_refresh
* bexio\_sync
* companies\_list
* company\_get
* company\_update
* contacts\_create
* contacts\_get
* contacts\_list
* contacts\_update
* ngl\_calculate
* qbo\_accounts\_create
* qbo\_accounts\_refresh
* qbo\_classes\_refresh
* qbo\_entities\_refresh
* qbo\_sync
* reports\_create\_account
* reports\_create\_explorer\_balances
* reports\_create\_token

Show all 60 tools

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://raw.githubusercontent.com/grafana/ai-marketplace/12be5634a492f73c189d466c5449d09b853ad7a4/plugins/grafana-cloud-mcp/assets/logo.svg)

### [Grafana Cloud](https://claude.com/marketplace/connectors/grafana-cloud)

Anthropic verifiedNew

Query metrics, logs, and traces and manage dashboards and alerts

[Add Grafana Cloud in Claude (opens in new tab)](https://claude.ai/directory/3392c633-e335-4638-bda7-5b259808c3f7 "Add in Claude")

![](https://assets.claude.com/a8994e05e594a562449127d44e0fe86c31d8e41c.svg?w=128&fit=max&auto=format)

### [Google Drive](https://claude.com/marketplace/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://assets.claude.com/8aa6ad728cfe811f74a7b65b92b44fe774b1fe17.jpg?w=128&fit=max&auto=format)

### [Atlassian MCP](https://claude.com/marketplace/connectors/atlassian)

Search, read and update Jira, Confluence, Bitbucket, Loom and other Atlassian apps with your existing Atlassian permissions.

[Add Atlassian MCP in Claude (opens in new tab)](https://claude.ai/directory/11ba10d9-477b-4988-bd1c-90a7fa680dc1 "Add in Claude")

![](https://assets.claude.com/646945a1897f9146e5221ee6ace82001a2e52f4d.svg?w=128&fit=max&auto=format)

### [Google Calendar](https://claude.com/marketplace/connectors/google-calendar)

Manage your schedule and coordinate meetings effortlessly

[Add Google Calendar in Claude (opens in new tab)](https://claude.ai/directory/2a838eaa-f7b4-4bc2-bd47-c326f3c813c5 "Add in Claude")

![](https://assets.claude.com/20c8443aa72ae4e4d77f923e6c33314713f965e8.svg?w=128&fit=max&auto=format)

### [Microsoft 365](https://claude.com/marketplace/connectors/microsoft-365)

Access your company's SharePoint, OneDrive, Outlook, and Teams directly in Claude

[Add Microsoft 365 in Claude (opens in new tab)](https://claude.ai/directory/ce0c9cda-5ea5-44c5-9cf2-40810dfa6582 "Add in Claude")

![](https://www.gemini.com/favicon.ico)

### [Gemini](https://claude.com/marketplace/connectors/gemini-mcp)

Anthropic verifiedTrending

Connect AI assistants to live crypto markets, prediction markets, your trading accounts, all through our secure read-only plugin

[Add Gemini in Claude (opens in new tab)](https://claude.ai/directory/88e8f327-f2f0-442b-a60c-9a7c2147d1f1 "Add in Claude")
