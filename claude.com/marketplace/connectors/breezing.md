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

![](https://assets.claude.com/a8994e05e594a562449127d44e0fe86c31d8e41c.svg?w=128&fit=max&auto=format)

### [Google Drive](https://claude.com/marketplace/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://assets.claude.com/646945a1897f9146e5221ee6ace82001a2e52f4d.svg?w=128&fit=max&auto=format)

### [Google Calendar](https://claude.com/marketplace/connectors/google-calendar)

Manage your schedule and coordinate meetings effortlessly

[Add Google Calendar in Claude (opens in new tab)](https://claude.ai/directory/2a838eaa-f7b4-4bc2-bd47-c326f3c813c5 "Add in Claude")

![](https://assets.claude.com/20c8443aa72ae4e4d77f923e6c33314713f965e8.svg?w=128&fit=max&auto=format)

### [Microsoft 365](https://claude.com/marketplace/connectors/microsoft-365)

Access your company's SharePoint, OneDrive, Outlook, and Teams directly in Claude

[Add Microsoft 365 in Claude (opens in new tab)](https://claude.ai/directory/ce0c9cda-5ea5-44c5-9cf2-40810dfa6582 "Add in Claude")

![](https://assets.claude.com/517cb0a746dcf968ce8efda7613b69101b536a52.svg?w=128&fit=max&auto=format)

### [Notion](https://claude.com/marketplace/connectors/notion)

Connect your Notion workspace to search, update, and power workflows across tools

[Add Notion in Claude (opens in new tab)](https://claude.ai/directory/69f3a300-cc60-48c4-b237-dfac56530dbf "Add in Claude")

![](https://assets.claude.com/bdf25f3db0bfe9b74855f504c31bd8522659edae.svg?w=128&fit=max&auto=format)

### [Slack](https://claude.com/marketplace/connectors/slack)

Send messages, create canvases, and fetch Slack data

[Add Slack in Claude (opens in new tab)](https://claude.ai/directory/597f662f-36de-437e-836e-5a81013cbfbe "Add in Claude")

![](https://www.google.com/s2/favicons?domain=thelinks.ai&sz=96)

### [Links Connect](https://claude.com/marketplace/connectors/links-connect)

Live financial data. Let Claude do the rest.

[Add Links Connect in Claude (opens in new tab)](https://claude.ai/directory/cb34f851-d450-4cd8-8197-c292bbdcb2f2 "Add in Claude")
