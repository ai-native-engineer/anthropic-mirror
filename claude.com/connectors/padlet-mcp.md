<!-- source: https://claude.com/connectors/padlet-mcp -->

[Skip to main content](#main-content)

Connector URL`https://mcp.padlet.com/`

More[Documentation (opens in new tab)](https://padlet.help/l/en/article/pofbiabhv1-mcp-server)[Support (opens in new tab)](mailto:hello@padlet.com)[Privacy policy (opens in new tab)](https://legal.padlet.com/privacy)

Padlet is a visual board platform used by teachers, students, and teams to collect, organize, and share content on collaborative boards called padlets. The Padlet connector links the user's own Padlet account via OAuth so they can work with their padlets directly in conversation.

With this connector, users can:

- Create padlets and organize them with sections, layouts, wallpapers, and appearance settings.

- Add, edit, arrange, pin, and sort posts, and draw connections between posts on Freeform boards.

- Read, search, and summarize board content, including AI analysis of images, videos, audio, and document attachments.

- Comment on posts and moderate discussion.

- Manage sharing settings by modifying permissions, passwords, collaborators, and email invitations.

- Schedule automations such as timed freezes, and freeze or unfreeze boards on demand.

- Grade student submissions and sync grades to a connected LMS (e.g. Canvas or Schoology) via LTI.

- For school and team library admins: manage membership and invitations, per-role permissions, SSO configuration (OAuth providers and SAML), approved email domains, content safety, and allowed attachment types.

The connector does not yet fully support Padlet's Sandbox (whiteboard) format; it works with Padlet's other board formats.

All actions run against the authenticated user's Padlet account and respect Padlet's permission model — the connector can only see and change what the signed-in user could see and change in Padlet itself. Deletions of posts and sections are soft-deletes that can be restored with a dedicated restore tool, and the small number of irreversible operations (deleting comments, automations, or custom fields, removing collaborators, invitations, or approved domains) are annotated as destructive so the assistant confirms with the user before proceeding.

## Tools

* add\_comment\_to\_post
* add\_library\_approved\_domain
* analyze\_post\_attachments
* bulk\_invite\_library\_members
* complete\_library\_onboarding\_step
* create\_automation
* create\_library\_saml\_connection
* create\_padlet
* create\_padlet\_arcade\_activity
* create\_post\_connection
* create\_posts
* delete\_automations
* delete\_comment
* delete\_custom\_fields
* delete\_post\_connection
* freeze\_padlet
* get\_comment\_url
* get\_current\_user\_info
* get\_library\_approved\_domains
* get\_library\_attachment\_type\_settings
* get\_library\_content\_safety
* get\_library\_info
* get\_library\_invite\_links
* get\_library\_oauth\_settings

Show all 76 tools

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

![](https://www.google.com/s2/favicons?domain=canva.com&sz=96)

### [Canva](https://claude.com/connectors/canva)

Search, create, autofill, and export Canva designs

[Add Canva in Claude (opens in new tab)](https://claude.ai/directory/eb9240f2-e1c1-43c1-828f-0fda40c22e4c "Add in Claude")

![](https://www.google.com/s2/favicons?domain=microsoft.com&sz=96)

### [Microsoft 365](https://claude.com/connectors/microsoft-365)

Access your company's SharePoint, OneDrive, Outlook, and Teams directly in Claude

[Add Microsoft 365 in Claude (opens in new tab)](https://claude.ai/directory/ce0c9cda-5ea5-44c5-9cf2-40810dfa6582 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=atlassian.com&sz=96)

### [Atlassian Rovo](https://claude.com/connectors/atlassian)

Access Jira & Confluence from Claude

[Add Atlassian Rovo in Claude (opens in new tab)](https://claude.ai/directory/11ba10d9-477b-4988-bd1c-90a7fa680dc1 "Add in Claude")

![](https://www.notion.so/images/notion-logo-block-main.svg)

### [Notion](https://claude.com/connectors/notion)

Connect your Notion workspace to search, update, and power workflows across tools

[Add Notion in Claude (opens in new tab)](https://claude.ai/directory/69f3a300-cc60-48c4-b237-dfac56530dbf "Add in Claude")
