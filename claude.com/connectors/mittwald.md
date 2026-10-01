<!-- source: https://claude.com/connectors/mittwald -->

[Skip to main content](#main-content)

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

![](https://www.google.com/s2/favicons?domain=supabase.com&sz=96)

### [Supabase](https://claude.com/connectors/supabase)

Manage databases, authentication, and storage

[Add Supabase in Claude (opens in new tab)](https://claude.ai/directory/11ca66fc-1e98-49d5-ab9b-7cb4672a8f10 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=monday.com&sz=96)

### [monday.com](https://claude.com/connectors/monday)

Manage projects, tasks, portfolios, boards, workflows, milestones, dependencies, forms and dashboards with monday.com project management & CRM.

[Add monday.com in Claude (opens in new tab)](https://claude.ai/directory/49e0f9ba-7d45-4fb6-b098-55eec956fbc6 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=vercel.com&sz=96)

### [Vercel](https://claude.com/connectors/vercel)

Analyze, debug, and manage projects and deployments

[Add Vercel in Claude (opens in new tab)](https://claude.ai/directory/7eb42afe-0087-4493-a105-da2b021d5c03 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=miro.com&sz=96)

### [Miro](https://claude.com/connectors/miro)

Access and create new content on Miro boards

[Add Miro in Claude (opens in new tab)](https://claude.ai/directory/72480fb8-32ed-4075-b1c4-79e09c858b29 "Add in Claude")

![](https://cdn.b12.io/branding/b12-logo-purple.png)

### [Website Generator by B12](https://claude.com/connectors/website-generator-by-b12)

Build a website or web app in minutes! Generate, design, write code, and create copy for your website. Powered by B12. Contact: hello@b12.io

[Add Website Generator by B12 in Claude (opens in new tab)](https://claude.ai/directory/e25b319d-9c6a-4baa-90a3-0bb8eb5e25b0 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=zapier.com&sz=96)

### [Zapier](https://claude.com/connectors/zapier)

Automate workflows across thousands of apps via conversation

[Add Zapier in Claude (opens in new tab)](https://claude.ai/directory/1f6f271e-3d29-4241-b35e-8abe6def4891 "Add in Claude")
