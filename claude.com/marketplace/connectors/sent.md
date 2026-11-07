<!-- source: https://claude.com/marketplace/connectors/sent -->

Connector URL`https://mcp.sent.dm/mcp`

More[Documentation (opens in new tab)](https://docs.sent.dm/)[Support (opens in new tab)](mailto:support@sent.dm)[Privacy policy (opens in new tab)](https://www.sent.dm/legal/privacy-policy)

Connect Claude to Sent to send text messages on SMS, WhatsApp, and RCS for messaging agents, notifications, reminders, alerts, one-time passcodes (OTP).

- Messages: Send [template messages](https://docs.sent.dm/start/quickstart/first-template) to one or many recipients. Choose a channel or let smart routing choose it. Schedule sends up to 30 days ahead. View message content, channel, status, and delivery events: queued, sent, delivered, read, or failed. Opted-out recipients are blocked automatically.

- Templates: Search by name, status, or category. Get templates and their variables by ID or name. Delete unused templates.

- Contacts: Create contacts from phone numbers, up to 10 per call. List, view, and delete contacts. Check message counts and success rates by channel.

- Compliance: Check SMS sender requirements by country and number type: 10DLC, toll-free, short code, local, mobile, or alphanumeric sender ID. Get a setup plan with the required fields.

- Sender Profiles: Create, list, view, update, and delete profiles for your organization. Check channel readiness for each profile. Submit required documents in the Sent dashboard.

- Phone number lookup: Check validity, carrier, line type, country, VoIP status, and porting details. Each lookup is paid.

- Analytics: View the deliverability rate, message volume over time, and total contacts.

- Account: Check account details, balance, onboarding, and KYC status.

- Feedback: Send connector feedback to the Sent team.

Try asking:

- "Send the `order\_shipped` template to +14155550123 on WhatsApp, then check if it was delivered."

- "What do I need to set up a 10DLC sender in the US?"

Claude can access only the Sent organization and Sender Profile you authorize. Messages go to real recipients. Creating a Sender Profile can claim a phone number and incur registration fees. Deleting one can disconnect WhatsApp and release its numbers.

## Tools

* account.get
* balance.get
* contacts.create\_many
* contacts.delete
* contacts.get
* contacts.list
* contacts.message\_summary
* dashboard.contacts
* dashboard.deliverability
* dashboard.messages\_sent
* messages.activities.list
* messages.get
* messages.send
* numbers.lookup
* onboarding.status
* templates.delete
* templates.get
* templates.get\_by\_name
* templates.list
* compliance.requirements
* compliance.setup\_plan
* feedback.send
* sender\_profiles.list
* sender\_profiles.get

Show all 25 tools

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
