<!-- source: https://claude.com/marketplace/connectors/countersignatory -->

Connector URL`https://countersignatory.com/mcp`

More[Documentation (opens in new tab)](https://countersignatory.com/llms.txt)[Support (opens in new tab)](mailto:index@countersignatory.com)[Privacy policy (opens in new tab)](https://countersignatory.com/privacy.html)

Countersignatory is an exchange where software buys a bounded human judgment at a published price. An agent that reaches a step it should not take alone (send this refund, publish this page, accept this label) can price the task, buy it, and get a named human's answer back.

What you can buy today: Check (check.general), one screened human, $1.25 at a 24-hour deadline. Three task templates: approval (approve or reject, with a reason), verification (true, false or cannot\_tell, with a reason) and judgment (one label from up to 10, with a reason). Each answer says who gave it and how they are disclosed.

How it works:

1. countersignatory\_quote prices a task, free and read-only.

2. countersignatory\_place\_order creates an unpaid order and returns two ways to pay: an x402 payment request (USDC on Base) for an agent with a wallet, and a card checkout link for a person.

3. A responder answers within the deadline, or the order is refunded in full automatically.

4. countersignatory\_get\_order returns the status and the answer.

countersignatory\_spot\_index shows the going rate for every market, with urgency multipliers, the published responder wage floor ($0.25 net per active minute) and the derivation of each price. Markets not yet live (Consensus of 3 or 5, named-expert Countersign, notarisation) can be quoted but not bought; countersignatory\_register\_interest records demand for them.

Refused at intake: CAPTCHAs and bot checks, logging in or entering credentials, contacting third parties, medical, legal or financial advice, and anything sexual or involving minors.

No account or key is needed to quote or order. While volume is low, orders are answered by hand by a named group (currently the founder, disclosed as such), so deadlines are at least one hour.

## Tools

* countersignatory\_quote
* countersignatory\_register\_interest
* countersignatory\_spot\_index
* countersignatory\_place\_order
* countersignatory\_get\_order

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

Access SharePoint, OneDrive, Outlook, and Teams directly in Claude

[Add Microsoft 365 in Claude (opens in new tab)](https://claude.ai/directory/ce0c9cda-5ea5-44c5-9cf2-40810dfa6582 "Add in Claude")

![](https://assets.claude.com/517cb0a746dcf968ce8efda7613b69101b536a52.svg?w=128&fit=max&auto=format)

### [Notion](https://claude.com/marketplace/connectors/notion)

Connect your Notion workspace to search, update, and power workflows across tools

[Add Notion in Claude (opens in new tab)](https://claude.ai/directory/69f3a300-cc60-48c4-b237-dfac56530dbf "Add in Claude")

![](https://assets.claude.com/bdf25f3db0bfe9b74855f504c31bd8522659edae.svg?w=128&fit=max&auto=format)

### [Slack](https://claude.com/marketplace/connectors/slack)

Send messages, create canvases, and fetch Slack data

[Add Slack in Claude (opens in new tab)](https://claude.ai/directory/597f662f-36de-437e-836e-5a81013cbfbe "Add in Claude")

![](https://assets.claude.com/8aa6ad728cfe811f74a7b65b92b44fe774b1fe17.jpg?w=128&fit=max&auto=format)

### [Atlassian MCP](https://claude.com/marketplace/connectors/atlassian)

Search, read and update Jira, Confluence, Bitbucket, Loom and other Atlassian apps with your existing Atlassian permissions.

[Add Atlassian MCP in Claude (opens in new tab)](https://claude.ai/directory/11ba10d9-477b-4988-bd1c-90a7fa680dc1 "Add in Claude")
