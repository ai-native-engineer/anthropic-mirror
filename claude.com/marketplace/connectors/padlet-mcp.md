<!-- source: https://claude.com/marketplace/connectors/padlet-mcp -->

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

![](https://assets.claude.com/a8994e05e594a562449127d44e0fe86c31d8e41c.svg?w=128&fit=max&auto=format)

### [Google Drive](https://claude.com/marketplace/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://assets.claude.com/646945a1897f9146e5221ee6ace82001a2e52f4d.svg?w=128&fit=max&auto=format)

### [Google Calendar](https://claude.com/marketplace/connectors/google-calendar)

Manage your schedule and coordinate meetings effortlessly

[Add Google Calendar in Claude (opens in new tab)](https://claude.ai/directory/2a838eaa-f7b4-4bc2-bd47-c326f3c813c5 "Add in Claude")

![](https://assets.claude.com/e476a6c2c2f961f5f2120482f37b1daafc1506d9.jpg?w=128&fit=max&auto=format)

### [Canva](https://claude.com/marketplace/connectors/canva)

Search, create, autofill, and export Canva designs

[Add Canva in Claude (opens in new tab)](https://claude.ai/directory/eb9240f2-e1c1-43c1-828f-0fda40c22e4c "Add in Claude")

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
