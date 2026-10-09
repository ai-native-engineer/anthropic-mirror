<!-- source: https://claude.com/marketplace/connectors/mittwald -->

Connector URL`https://mcp.mittwald.de/mcp`

More[Documentation (opens in new tab)](https://developer.mittwald.de/mcp/)[Support (opens in new tab)](mailto:opensource@mittwald.de)[Privacy policy (opens in new tab)](https://www.mittwald.de/datenschutz)

Manage your mittwald hosting infrastructure through natural conversation — without leaving Claude.

This connector gives Claude direct access to the mittwald Cloud Platform:

- Projects & servers — create, inspect and update projects, check filesystem usage, manage memberships and invites

- Apps — install and manage PHP, Node.js, Python and static apps; track dependencies and apply upgrades

- Containers & stacks — deploy stacks, start/stop/restart containers, stream logs, manage registries and volumes

- Databases — administer MySQL and Redis instances and their users; get ready-to-run commands for dumps, imports, port forwarding and phpMyAdmin

- Domains, DNS & certificates — inspect domains, edit DNS zones, configure virtual hosts, request TLS certificates

- Mail — manage mail addresses and delivery boxes

- Cronjobs — schedule, trigger and inspect jobs and their execution logs

- Access — SSH and SFTP users, SSH keys, API tokens, sessions, organisation members

- Backups — create backups and schedules, list them, retrieve download URLs

Authentication runs through OAuth 2.1 with PKCE against your mittwald account, so Claude only acts with the permissions you grant — no API tokens to copy around.

For safety, the connector never opens shells, tunnels or file transfers itself. SSH access, database dumps and backup downloads come back as a command or URL for you to run locally, keeping credentials and data on your machine.

## Tools

* mittwald\_app\_copy
* mittwald\_app\_get
* mittwald\_app\_list
* mittwald\_app\_list\_upgrade\_candidates
* mittwald\_app\_ssh
* mittwald\_app\_uninstall
* mittwald\_app\_update
* mittwald\_app\_upgrade
* mittwald\_app\_versions
* mittwald\_backup\_create
* mittwald\_backup\_delete
* mittwald\_backup\_download
* mittwald\_backup\_get
* mittwald\_backup\_list
* mittwald\_backup\_schedule\_create
* mittwald\_backup\_schedule\_delete
* mittwald\_backup\_schedule\_list
* mittwald\_backup\_schedule\_update
* mittwald\_certificate\_list
* mittwald\_certificate\_request
* mittwald\_container\_delete
* mittwald\_container\_list
* mittwald\_container\_logs
* mittwald\_container\_restart

Show all 116 tools

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://raw.githubusercontent.com/grafana/ai-marketplace/12be5634a492f73c189d466c5449d09b853ad7a4/plugins/grafana-cloud-mcp/assets/logo.svg)

### [Grafana Cloud](https://claude.com/marketplace/connectors/grafana-cloud)

Anthropic verifiedNew

Query metrics, logs, and traces and manage dashboards and alerts

[Add Grafana Cloud in Claude (opens in new tab)](https://claude.ai/directory/3392c633-e335-4638-bda7-5b259808c3f7 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=monday.com&sz=96)

### [monday.com](https://claude.com/marketplace/connectors/monday)

monday.com project management & CRM for projects, tasks, portfolios, boards, workflows, milestones, dependencies, forms, dashboards, cross-project portfolio status, and critical paths.

[Add monday.com in Claude (opens in new tab)](https://claude.ai/directory/49e0f9ba-7d45-4fb6-b098-55eec956fbc6 "Add in Claude")

![](https://assets.claude.com/89209c1f16bf517eb431ff08e811de0778d70689.svg?w=128&fit=max&auto=format)

### [Supabase](https://claude.com/marketplace/connectors/supabase)

Manage databases, authentication, and storage

[Add Supabase in Claude (opens in new tab)](https://claude.ai/directory/11ca66fc-1e98-49d5-ab9b-7cb4672a8f10 "Add in Claude")

![](https://assets.claude.com/e64f9962a277a8943b084a17b6a9386a7eb95a61.svg?w=128&fit=max&auto=format)

### [Miro](https://claude.com/marketplace/connectors/miro)

Access and create new content on Miro boards

[Add Miro in Claude (opens in new tab)](https://claude.ai/directory/72480fb8-32ed-4075-b1c4-79e09c858b29 "Add in Claude")

![](https://assets.claude.com/f8c4f0634cd056e248c7ea396b1839b922470ac6.jpg?w=128&fit=max&auto=format)

### [Vercel](https://claude.com/marketplace/connectors/vercel)

Analyze, debug, and manage projects and deployments

[Add Vercel in Claude (opens in new tab)](https://claude.ai/directory/7eb42afe-0087-4493-a105-da2b021d5c03 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=microsoft.com&sz=96)

### [Microsoft Learn](https://claude.com/marketplace/connectors/microsoft-learn)

Search trusted Microsoft docs to power your development

[Add Microsoft Learn in Claude (opens in new tab)](https://claude.ai/directory/89a7ddf5-2a6b-410c-be11-aa0e1a1b35a6 "Add in Claude")
