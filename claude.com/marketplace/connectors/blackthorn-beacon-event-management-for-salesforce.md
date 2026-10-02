<!-- source: https://claude.com/marketplace/connectors/blackthorn-beacon-event-management-for-salesforce -->

Connector URL`https://forge.blackthorn.io/api/mcp`

More[Documentation (opens in new tab)](https://forge.blackthorn.io/about)[Support (opens in new tab)](https://community.blackthorn.io/s/support-request)[Privacy policy (opens in new tab)](https://docs.blackthorn.io/docs/blackthorn-privacy-policy)

Blackthorn Events turns Salesforce into an event platform; this MCP server lets Claude operate it directly, no exports, no copy-paste.

Connect with Salesforce OAuth 2.0 + PKCE and Claude gets 94 tools across the event lifecycle:

- Reporting: dashboards, event metrics, ROI, pipeline/finance snapshots, registration funnels, attendee status, session popularity, email performance, donation reports, CSV export.

- Events, sessions & tickets: create/update events, ticket types, sessions; clone an event (dry-run preview first) in seconds.

- Attendees & registrations: create, update, look up, and manage records.

- Speakers & sponsors: create and update records tied to your events.

- Forms: build registration forms, add questions, create managed dropdowns.

- Email & audiences: browse templates, list segments/audiences, schedule campaigns, pull performance metrics.

- Escape hatch: a SOQL query tool (SELECT-only, LIMIT-enforced) and an object-describe tool for anything else.

- Every write is guarded: deletes require an explicit confirm flag, and the server resolves event names to Salesforce IDs for you, it never asks for a raw record ID or echoes internal field names into chat.

Salesforce stays the system of record. Reads/writes go through standard Salesforce APIs into the Blackthorn-managed objects your team already uses, no shadow database, no bulk copy of your CRM data. Claude never sees your Salesforce password; refresh tokens are encrypted at rest.

Typical asks: "What's registration looking like for the Q3 conference, give me the funnel and where people drop off," "Clone last year's user conference into a new event for October," "Add a dietary-restrictions question to the registration form," "Which sponsors haven't been invoiced yet," "Export the VIP segment as a CSV," or "Schedule the reminder email for everyone who hasn't checked in yet."

Built for planners, marketers, and ops teams running events on Blackthorn's Salesforce-native package.

## Tools

* salesforce\_sobject\_create
* salesforce\_sobject\_get
* salesforce\_sobject\_update
* salesforce\_soql\_query

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://assets.claude.com/e476a6c2c2f961f5f2120482f37b1daafc1506d9.jpg?w=128&fit=max&auto=format)

### [Canva](https://claude.com/marketplace/connectors/canva)

Search, create, autofill, and export Canva designs

[Add Canva in Claude (opens in new tab)](https://claude.ai/directory/eb9240f2-e1c1-43c1-828f-0fda40c22e4c "Add in Claude")

![](https://storage.googleapis.com/media-assets-299d7136-cb52-d546-ee02-34bc1307c35f/mcp-directory/icons/pubmed.svg)

### [PubMed](https://claude.com/marketplace/connectors/pubmed)

Search biomedical literature from PubMed

[Add PubMed in Claude (opens in new tab)](https://claude.ai/directory/81cc5080-a204-4aa1-a694-fa868a3c8721 "Add in Claude")

![](https://assets.claude.com/46519c8cd657205f9f26b243952e1bd41a07d517.svg?w=128&fit=max&auto=format)

### [Salesforce - Beta](https://claude.com/marketplace/connectors/salesforce-headless-360)

Sell, serve, and operate at scale with Salesforce.

[Add Salesforce - Beta in Claude (opens in new tab)](https://claude.ai/directory/a352dbf6-c732-43d4-84c1-0bbb389d3921 "Add in Claude")

![](https://assets.claude.com/2ceed63f77b47ed3a782d750eb83f107b3c5226a.svg?w=128&fit=max&auto=format)

### [Consensus](https://claude.com/marketplace/connectors/consensus)

Explore scientific research

[Add Consensus in Claude (opens in new tab)](https://claude.ai/directory/65247229-f0c7-49df-9044-fcbb8b3894c6 "Add in Claude")

![](https://storage.googleapis.com/media-assets-299d7136-cb52-d546-ee02-34bc1307c35f/mcp-directory/icons/clinical-trials.png)

### [Clinical Trials](https://claude.com/marketplace/connectors/clinical-trials)

Access ClinicalTrials.gov data

[Add Clinical Trials in Claude (opens in new tab)](https://claude.ai/directory/c1754944-3ad1-49ab-bec5-9aeae3a6a9a3 "Add in Claude")

![](https://assets.claude.com/949ad8b2de4362c0b945dda5655db3a666ded338.jpg?w=128&fit=max&auto=format)

### [Jotform](https://claude.com/marketplace/connectors/jotform)

Create forms, surveys, quizzes & analyze submissions

[Add Jotform in Claude (opens in new tab)](https://claude.ai/directory/aed7e2be-868e-4046-9e12-5c917b4e6b97 "Add in Claude")
