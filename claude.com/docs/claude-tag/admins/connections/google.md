<!-- source: https://claude.com/docs/claude-tag/admins/connections/google -->

Connections are added inside an [Access bundle](/docs/claude-tag/admins/add-connections#your-first-access-bundle). At [`claude.ai/admin-settings/claude-tag`](https://claude.ai/admin-settings/claude-tag), open **Access bundles** in the left navigation, click into a bundle (or **Create** one), and go to its **Credentials** tab.

Connecting Google Drive, Calendar, and Gmail lets Claude read documents, spreadsheets, calendar events, and email from any channel under the bundle’s scope. You add it as a connection inside an [Access bundle](/docs/claude-tag/admins/add-connections); the credential belongs to the agent, not to any person.
This is an HTTP API connection, not a personal claude.ai connector. A member’s own Google connector applies only in DMs.

##  Choose OAuth or a service account

The connection picker offers two routes:

| Route | When to use |
| **OAuth (Connect button)** | Fastest path. An admin signs in with a Google account that has access to the content Claude needs. |
| **GCP service-account key** | When you want a dedicated non-human identity in Google with auditable access, or need domain-wide delegation across your Workspace. |

Both routes create a credential and an allowed-websites rule path-scoped to that Google service (the Drive API path for Drive, the Calendar API path for Calendar, the Gmail API path for Gmail).

##  Add the connection with OAuth

Use a dedicated Google account for this connection (for example, `[email protected]`), not your own. The connection is shared: anyone in a channel under the bundle’s scope can ask Claude to read whatever this account can see in Drive, Calendar, and Gmail. A dedicated account starts with no access until you share the specific folders and calendars Claude needs, and keeps its activity under a separate identity in Google’s audit log.

In the bundle, click **Connect** next to **Google Drive**, **Google Calendar**, or **Google Gmail**. A scope checklist appears with read-only scopes selected by default. Each scope grants a specific permission:

| Scope | What it lets Claude do |
| `openid`, `userinfo.email` | Identify the connected account (selected by default) |
| `calendar.readonly` | Read events and calendars |
| `calendar.events.readonly` | Read events only (narrower than `calendar.readonly`) |
| `calendar` | Create, edit, and delete events |
| `drive.readonly` | Read files and folders |
| `drive.file` | Create and edit files Claude itself created |
| `gmail.readonly` | Read email |

Check write scopes only if Claude should create or edit. Click **Sign in with Google Calendar** (or **Sign in with Google Drive**, or **Sign in with Google Gmail**), approve the Google consent screen, and the credential is saved.
The connection’s reach is whatever the signed-in Google account can see. Share the relevant folders and calendars with that account in Google before testing.

##  Add the connection with a service account

In the bundle, click **Connect another app** at the bottom of the Credentials tab, then choose **GCP access token (with Service Account Key)**.

| Field | Value |
| GCP service account key (JSON) | The JSON key file from Google Cloud Console |
| Scopes (optional) | The Google API scopes to request (for example `https://www.googleapis.com/auth/drive.readonly`). The field is labeled optional, but Drive and Calendar calls fail without the matching scope listed here. |
| Subject (optional) | A user email to impersonate via domain-wide delegation. Set this for Workspace data (Drive, Calendar, Gmail, Docs). |
| Allowed websites | `*.googleapis.com` |

For Google Workspace data (Drive, Calendar, Gmail, Docs), the service account needs domain-wide delegation configured in your Google Admin console with the matching API scopes. Google’s guide is at [developers.google.com/identity/protocols/oauth2/service-account](https://developers.google.com/identity/protocols/oauth2/service-account#delegatingauthority).
The Agent Proxy injects the credential at the network boundary; the model and the sandbox are not given the key. See [how Agent Proxy works](/docs/claude-tag/concepts/agent-identity#agent-proxy).

##  Verify the connection

In a channel under the bundle’s scope, in a new thread:

@Claude what can you access from this channel?

Google Drive, Calendar, or Gmail appears in the list once the connection is live. Connection changes can take a moment to reach a running thread; testing in a fresh thread is the reliable way to confirm.

* [What this connection adds](/docs/claude-tag/users/use-cases/find-answers): grounding answers in your team’s documents
* [Give Claude access](/docs/claude-tag/admins/add-connections): the full credential-type and allowed-hosts reference

[Gong](/docs/claude-tag/admins/connections/gong)[HubSpot](/docs/claude-tag/admins/connections/hubspot)
