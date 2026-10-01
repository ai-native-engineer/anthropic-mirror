<!-- source: https://claude.com/connectors/customer-io -->

[Skip to main content](#main-content)

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

![](https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://drive.google.com&size=64)

### [Google Drive](https://claude.com/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://mail.google.com&size=64)

### [Gmail](https://claude.com/connectors/gmail)

Draft replies, summarize threads, & search your inbox

[Add Gmail in Claude (opens in new tab)](https://claude.ai/directory/2701e52f-b826-4aaf-8b25-11f2a97c98b0 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=microsoft.com&sz=96)

### [Microsoft 365](https://claude.com/connectors/microsoft-365)

Access your company's SharePoint, OneDrive, Outlook, and Teams directly in Claude

[Add Microsoft 365 in Claude (opens in new tab)](https://claude.ai/directory/ce0c9cda-5ea5-44c5-9cf2-40810dfa6582 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=slack.com&sz=96)

### [Slack](https://claude.com/connectors/slack)

Send messages, create canvases, and fetch Slack data

[Add Slack in Claude (opens in new tab)](https://claude.ai/directory/597f662f-36de-437e-836e-5a81013cbfbe "Add in Claude")

![](https://agent.enrichlabs.ai/avatars/helena.png)

### [Helena by Enrich Labs](https://claude.com/connectors/helena-by-enrich-labs)

Trending

Your AI marketer for paid ads, SEO, email, social, and analytics

[Add Helena by Enrich Labs in Claude (opens in new tab)](https://claude.ai/directory/0da6abdc-62c3-4272-940b-898189371a48 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=asana.com&sz=96)

### [Asana](https://claude.com/connectors/asana)

Connect to Asana to coordinate tasks, projects, and goals

[Add Asana in Claude (opens in new tab)](https://claude.ai/directory/41aefcf3-a829-45eb-8cee-d90b93912f57 "Add in Claude")
