<!-- source: https://claude.com/marketplace/connectors/customer-io -->

More[Documentation (opens in new tab)](https://docs.customer.io/ai/mcp/claude/)[Support (opens in new tab)](mailto:win@customer.io)[Privacy policy (opens in new tab)](https://customer.io/legal/privacy-policy)

Connect Claude to your Customer.io workspace with full read, write, and delete access — granted independently, per workspace, via OAuth.

What Claude can do today:

• Build and edit automations (campaigns), broadcasts, and newsletters

• Create segments from plain-English audience definitions

• Inspect and update customer profiles and attributes

• Draft, QA, and publish emails in Design Studio

• Analyze deliveries, opens, clicks, and conversions; diagnose deliverability

• Manage CDP Data Pipelines: sources, destinations, and reverse ETL

• Guide SDK setup and app integration end to end

The connector exposes Customer.io's Journeys UI API and Data Pipelines API through verb-scoped tools — cio\_read\_api (GET), cio\_write\_api (POST/PUT/PATCH), and cio\_delete\_api (DELETE) — so reads, writes, and deletes are approved separately. Built-in schema introspection (cio\_schema) and server-maintained skills (cio\_skills\_list / cio\_skills\_read) give Claude authoritative, always-current guidance for complex workflows like automation wiring, segment conditions, and email design patterns, scoped to your account's plan.

Safety is built in: every write and delete supports a dry-run preview before execution, and credentials never pass through Claude — authentication is OAuth, with workspaces and permission scopes selected at connect time.

Try: "Analyze last month's welcome automation performance." "Build a segment of users inactive for 90 days." "Draft a re-engagement email and QA it." "Why did deliveries drop this week?"

## Tools

* cio\_prime
* cio\_auth\_status
* cio\_schema
* cio\_skills\_list
* cio\_skills\_read
* cio\_read\_api
* cio\_write\_api
* cio\_delete\_api

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://assets.claude.com/a8994e05e594a562449127d44e0fe86c31d8e41c.svg?w=128&fit=max&auto=format)

### [Google Drive](https://claude.com/marketplace/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://assets.claude.com/53ca8822f4c024f9b358b1e44148a1dc3c616dbe.svg?w=128&fit=max&auto=format)

### [Gmail](https://claude.com/marketplace/connectors/gmail)

Draft replies, summarize threads, & search your inbox

[Add Gmail in Claude (opens in new tab)](https://claude.ai/directory/2701e52f-b826-4aaf-8b25-11f2a97c98b0 "Add in Claude")

![](https://assets.claude.com/20c8443aa72ae4e4d77f923e6c33314713f965e8.svg?w=128&fit=max&auto=format)

### [Microsoft 365](https://claude.com/marketplace/connectors/microsoft-365)

Access your company's SharePoint, OneDrive, Outlook, and Teams directly in Claude

[Add Microsoft 365 in Claude (opens in new tab)](https://claude.ai/directory/ce0c9cda-5ea5-44c5-9cf2-40810dfa6582 "Add in Claude")

![](https://assets.claude.com/bdf25f3db0bfe9b74855f504c31bd8522659edae.svg?w=128&fit=max&auto=format)

### [Slack](https://claude.com/marketplace/connectors/slack)

Send messages, create canvases, and fetch Slack data

[Add Slack in Claude (opens in new tab)](https://claude.ai/directory/597f662f-36de-437e-836e-5a81013cbfbe "Add in Claude")

![](https://www.gemini.com/favicon.ico)

### [Gemini](https://claude.com/marketplace/connectors/gemini-mcp)

Anthropic verifiedTrending

Connect AI assistants to live crypto markets, prediction markets, your trading accounts, all through our secure read-only plugin

[Add Gemini in Claude (opens in new tab)](https://claude.ai/directory/88e8f327-f2f0-442b-a60c-9a7c2147d1f1 "Add in Claude")

![](https://assets.claude.com/cb89159037733bf1e8c66783990c1d38c53231d4.jpg?w=128&fit=max&auto=format)

### [HubSpot](https://claude.com/marketplace/connectors/hubspot)

CRM context for every answer, insight, and action

[Add HubSpot in Claude (opens in new tab)](https://claude.ai/directory/875dee50-9b3f-452b-af8c-fbc839966273 "Add in Claude")
