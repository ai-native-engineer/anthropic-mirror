<!-- source: https://claude.com/marketplace/connectors/toffu -->

Connector URL`https://mcp.toffu.ai/mcp`

More[Documentation (opens in new tab)](https://toffu.ai/docs)[Support (opens in new tab)](mailto:support@toffu.ai)[Privacy policy (opens in new tab)](https://toffu.ai/privacy)

Toffu connects Claude to a company's marketing stack: ad accounts (Google Ads, Meta Ads, LinkedIn Ads and others), analytics, content channels and marketing memory.

Read-only tools: get\_account\_context, query\_campaign\_performance, list\_entities, list\_campaigns / list\_ad\_sets / list\_ads, api\_request (reads only, writes are refused), creative\_report, account\_health, get\_task\_result.

Tools that can make changes, and how each is confirmed:

- propose\_\* tools (propose\_change, propose\_create\_campaign, propose\_update\_ad\_set, propose\_write, ...) store the change and return a preview. Nothing reaches the ad account.

- apply\_change and apply\_write run one stored proposal. The apply call is the confirmation: the client makes it after showing the user the preview, and the server runs nothing it was not asked to apply. undo\_change reverts an applied change within 24 hours.

- All writes are off until a workspace owner or admin turns on MCP write access in Toffu, and server-side budget limits apply to every apply.

- send\_message hands a task to the Toffu agent for analysis, reports and drafts. It cannot change ad accounts, publish content, send messages or edit Toffu settings; it returns any proposed change as a draft for the user to apply with propose\_\* and apply\_change.

## Tools

* apply\_change
* creative\_report
* get\_account\_context
* get\_task\_result
* propose\_change
* query\_campaign\_performance
* send\_message
* undo\_change

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://assets.claude.com/a8994e05e594a562449127d44e0fe86c31d8e41c.svg?w=128&fit=max&auto=format)

### [Google Drive](https://claude.com/marketplace/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://assets.claude.com/cb89159037733bf1e8c66783990c1d38c53231d4.jpg?w=128&fit=max&auto=format)

### [HubSpot](https://claude.com/marketplace/connectors/hubspot)

CRM context for every answer, insight, and action

[Add HubSpot in Claude (opens in new tab)](https://claude.ai/directory/875dee50-9b3f-452b-af8c-fbc839966273 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=monday.com&sz=96)

### [monday.com](https://claude.com/marketplace/connectors/monday)

monday.com project management & CRM for projects, tasks, portfolios, boards, workflows, milestones, dependencies, forms, dashboards, cross-project portfolio status, and critical paths.

[Add monday.com in Claude (opens in new tab)](https://claude.ai/directory/49e0f9ba-7d45-4fb6-b098-55eec956fbc6 "Add in Claude")

![](https://assets.claude.com/89209c1f16bf517eb431ff08e811de0778d70689.svg?w=128&fit=max&auto=format)

### [Supabase](https://claude.com/marketplace/connectors/supabase)

Manage databases, authentication, and storage

[Add Supabase in Claude (opens in new tab)](https://claude.ai/directory/11ca66fc-1e98-49d5-ab9b-7cb4672a8f10 "Add in Claude")

![](https://assets.claude.com/625f40fd713ca178d49e75e5f8df15e0e0843d40.png?w=128&fit=max&auto=format)

### [Shopify](https://claude.com/marketplace/connectors/shopify)

Build, manage, and analyze your Shopify store

[Add Shopify in Claude (opens in new tab)](https://claude.ai/directory/80917cb7-3071-4fca-b053-a4262d356c60 "Add in Claude")

![](https://cdn.bfldr.com/ENSXS21L/at/f5h33bhb29nhpm6963gngs66/webex-3d-symbol-color.png?format=png)

### [Webex for Claude](https://claude.com/marketplace/connectors/webex-suite)

Access your Webex meetings, messaging, and Vidcast content securely in Claude.

[Add Webex for Claude in Claude (opens in new tab)](https://claude.ai/directory/d044bab2-de8d-438e-9333-de76d1a8304a "Add in Claude")
