<!-- source: https://claude.com/docs/office-agents/outlook -->

Claude for Outlook is an add-in that brings Claude into your Outlook inbox
and calendar. It is built for professionals whose work runs through email,
including private equity and investment banking associates managing deal
flow, in-house legal teams running counterparty negotiations, and
consultants tracking multiple client threads.

Claude for Outlook is currently in beta and available to Pro, Max, Team,
and Enterprise plans.

With Claude for Outlook, you can:

* Triage your unread inbox into what needs you, what Claude can handle,
  and what is noise.
* Draft replies, reply-alls, and forwards in your voice, landed unsent in
  Outlook’s compose pane.
* Summarize long threads into decisions made, open items, and who owes
  what, with per-email citations.
* Read `.docx` and `.xlsx` attachments inline without opening them.
* Find meeting times across attendees and draft invites into Outlook’s
  native appointment form.
* Prep for your next meeting with a one-page brief of recent threads and
  attached documents.

##  Get started with Claude for Outlook

Claude for Outlook runs on the following Outlook clients.

* Outlook on the web
* Outlook on Windows, both new Outlook and classic Outlook, with a
  Microsoft 365 subscription
* Outlook on Mac with a Microsoft 365 subscription

The following are not supported: Outlook 2016 and 2019 perpetual or
volume-licensed editions, Outlook on iOS, Outlook on Android, and
mailboxes hosted on Exchange on-premises. Exchange Online through
Microsoft 365 is required.

Go to the [Claude for Outlook listing on Microsoft AppSource](https://marketplace.microsoft.com/en-us/product/office/WA200010724?tab=Overview).

Open Claude in Outlook

Open Outlook, open any email, select the Claude button in the message
ribbon, and sign in with your Claude account.

If you do not see the Claude button on the message, open the overflow menu
on the reading pane, choose Customize actions, and check Claude under
Apps. It then appears on every message and in the Home ribbon.

Organization admins can deploy Claude for Outlook through the Microsoft
365 Admin Center.

Go to Settings, then Integrated apps.

Search for “Claude for Outlook” in Microsoft AppSource.

Deploy the add-in to your organization or to specific people. See
[Microsoft’s deployment guide](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins)
for assignment options.

5

Grant Microsoft Graph consent

Complete the [Microsoft Graph admin consent](#grant-microsoft-graph-consent)
step below so users are not prompted individually.

After installation, team members open Outlook, open any email, select the
Claude button in the message ribbon, and sign in with their Claude
credentials. Pinning the task pane keeps it open as you move between
messages.

Organizations that have disabled “Let users access the Office Store” may
find that admin-deployed add-ins don’t appear for users. To work around
this, deploy using the manifest XML file described below.

###  Install from a manifest file

If your organization blocks the Microsoft Store, an IT administrator can
deploy the add-in by uploading its manifest file directly.

Download the manifest

Download the
[Claude for Outlook manifest](https://pivot.claude.ai/manifest-outlook.xml)
and save it to a secure location.

to Settings, then Integrated apps.

Upload the add-in

Select Upload custom apps, then Office Add-in. Choose “I have a
manifest file on this device”, select the file you downloaded, and
upload it.

Assign people

Choose your deployment scope: the entire organization, specific
people, specific groups, or just yourself for testing.

5

Review the settings and select Deploy. The add-in appears within
minutes for most people. Full organization rollout can take up to 24
hours on the Microsoft 365 side.

6

Grant Microsoft Graph consent

Complete the consent step in the next section.

###  Grant Microsoft Graph consent

Claude for Outlook reads mail and calendar data through Microsoft Graph.
This requires a one-time tenant-wide grant from a Global Administrator
and is separate from the Integrated apps deployment.
Have a Global Administrator open the following admin consent link in a
browser where they are signed in to your Microsoft 365 tenant.

```
https://login.microsoftonline.com/organizations/v2.0/adminconsent?client_id=c2995f31-11e7-4882-b7a7-ef9def0a0266&scope=https://graph.microsoft.com/Mail.ReadWrite%20https://graph.microsoft.com/Calendars.Read%20https://graph.microsoft.com/User.Read%20offline_access&redirect_uri=https://pivot.claude.ai/auth/callback
```

The administrator sees a Microsoft permissions screen listing
`Mail.ReadWrite`, `Calendars.Read`, `User.Read`, and `offline_access`.
After they select Accept, all users in the organization
can use Claude for Outlook without additional Microsoft prompts. The grant
takes effect immediately. Only the add-in rollout in the previous step can
take up to 24 hours.
If this step is skipped, every user sees a “Need admin approval” message
when Claude first tries to read mail or calendar data.
The redirect to `pivot.claude.ai` after consent carries only the consent
outcome, never a token or authorization code. See
[Why sign-in redirects through pivot.claude.ai](https://claude.com/docs/office-agents/third-party-platforms#why-sign-in-redirects-through-pivot-claude-ai)
for what each redirect carries and how to verify it in a network capture.

####  Use your own Entra app instead

If your organization’s policy does not permit consenting to a third-party
multi-tenant application, register a single-tenant application in the
Microsoft Entra admin center and have the add-in use it instead. The data
flow is identical; the Graph token stays in the user’s Outlook client
either way. The difference is that approval and Conditional Access policy
live entirely under an application your organization owns.

Register the application

In the Entra admin center, go to App registrations and create a new
registration. Choose “Accounts in this organizational directory only”.

Configure authentication

Under Authentication, add a Single-page application platform with
redirect URI `brk-multihub://pivot.claude.ai`. In Advanced settings,
set “Allow public client flows” to Yes.

Add Graph permissions

Under API permissions, add the Microsoft Graph delegated permissions
`Mail.ReadWrite`, `Calendars.Read`, `User.Read`, and `offline_access`.
Select “Grant admin consent” for your tenant.

Add the client ID to the manifest

Copy the application’s client ID from the Overview page. Download the
manifest from the
[Install from a manifest file](#install-from-a-manifest-file) section
and open it in a text editor. Search for `https://pivot.claude.ai/?m=`.
At the end of every URL that starts this way, inside the quotation
marks, add `&amp;graph_client_id=YOUR_CLIENT_ID`. Lines that refer to a
URL by `resid` need no change, and neither do the icon or support
URLs. Save the file, then upload and deploy it as that section
describes.

The following example shows one edited line. The version number in your
file can differ. Type `&amp;` exactly as shown: an XML file cannot contain
`&` on its own.

```
<bt:Url id="Taskpane.Url" DefaultValue="https://pivot.claude.ai/?m=outlook-1.0.0.5&amp;graph_client_id=YOUR_CLIENT_ID"/>
```

With this option, skip the admin consent link entirely. Users do not see a
Microsoft permissions prompt because your tenant has already consented to
your own application.
If you deploy through a third-party platform and generate your manifests
with the [setup wizard](https://claude.com/docs/office-agents/third-party-platforms#run-the-setup-wizard),
provide the client ID to the wizard as `graph_client_id` instead of
editing the file. See
[Deploy to Outlook](https://claude.com/docs/office-agents/third-party-platforms#deploy-to-outlook).

###  Deploy in a US Government or national cloud

If your Microsoft 365 tenant is in GCC High, DoD, or 21Vianet, register
your own Entra application with `graph_client_id` as described above
(Anthropic’s multi-tenant application exists only in the global cloud)
and set `graph_cloud` to the matching value:

| Tenant | `graph_cloud` |
| --- | --- |
| Commercial or GCC | `global` (default; may be omitted) |
| GCC High | `us-gov-high` |
| DoD | `us-gov-dod` |
| 21Vianet (China) | `china` |

For a DoD tenant, every URL in the manifest that starts with
`https://pivot.claude.ai/?m=` ends with:

```
&amp;graph_client_id=YOUR_CLIENT_ID&amp;graph_cloud=us-gov-dod
```

For GCC High and 21Vianet tenants, `graph_cloud` may be omitted: the
add-in detects those clouds at sign-in from the authority host Outlook
reports. Setting it explicitly is still recommended when your compliance
program requires the endpoints to be fixed in the reviewed manifest
rather than derived at runtime. DoD tenants share an authority host with
GCC High, so `graph_cloud=us-gov-dod` is always required for DoD.

If your organization routes API traffic through an internal LLM gateway,
Amazon Bedrock, Google Cloud Vertex AI, or Azure AI Foundry, you can use
the add-in without Claude accounts. This is the same gateway pattern used
by Claude Code.
For setup instructions and gateway requirements, see

##  Triage your inbox

Ask Claude what needs your attention. Claude reads your unread mail and
attachments and sorts them into three groups: action items for you, items
Claude can handle for your review, and noise you can archive in one
selection. Each action item carries a one-line reason. Items Claude can
handle, such as scheduling asks, acknowledgments, and standard-form
documents, arrive pre-drafted.
Prompts to try:

* “What needs me?”
* “Draft replies for everything you can handle”
* “Archive all the calendar responses and newsletters”

##  Draft replies in your voice

Tell Claude what you want to say. It drafts the reply into Outlook’s
native compose pane, unsent. Tone is learned from your sent folder, so
the draft matches your sentence length and formality register. Claude
leaves the closing off so Outlook can append your configured signature
without duplication.
Claude chooses reply versus reply-all deliberately and warns before adding
anyone who was not on the thread.
Prompts to try:

* “Reply to this and agree to the extension, push back on the fee”
* “Reply-all thanking everyone and confirming Thursday works”
* “Forward this to Dana with a two-line summary”

##  Summarize long threads

Claude reads the entire conversation, including every reply and forward,
and tells you what has been decided, what is still open, and who owes
what. Every claim cites the specific email it came from. Selecting a
citation opens that message in Outlook.
Prompts to try:

* “What’s been decided and what’s still open?”
* “Who owes what on this thread?”

##  Read attachments inline

Claude reads `.docx` and `.xlsx` attachments on the open email without
you opening them. For `.pptx` attachments, open the deck in PowerPoint
with the thread loaded as context using
[Work across M365 apps](https://claude.com/docs/office-agents/work-across-apps). PDF attachments
are not currently read inline; save the file and upload it through the
sidebar instead.
Prompts to try:

* “Summarize the attached memo”
* “What’s in the spreadsheet on this email?”

##  Search your mailbox

Ask Claude to find a past conversation by topic, not only by keywords.
Results return as citations that open the source message in Outlook so
you can verify every answer against the original email.
Prompts to try:

* “When did we last discuss the cap with Fernwood?”
* “Find the email where Dana sent the revised term sheet”

##  Find time and create events

Claude checks free/busy for everyone whose calendar you can see and
proposes slots that respect working hours and existing holds. The invite
is drafted into Outlook’s native appointment form with attendees, subject,
and agenda for you to review and send.
To make a meeting repeat, open it for editing as the organizer and ask
Claude. This works on a new invite, a saved meeting, or a whole series.
Claude lists the pattern, dates, time, and time zone it will set and waits
for you to allow the change. Nothing is saved or sent until you click Save
or Send in Outlook. All-day events are not supported.
Prompts to try:

* “Find 30 minutes with Dana and the Fernwood team next week”
* “Block Thursday afternoon for deep work”
* “Make this weekly through the end of June”

##  Prep for meetings

For your next event, Claude pulls the last thread with each attendee and
any attached documents into a one-page brief, so you walk in knowing the
open items and what each person last said.
Prompts to try:

* “Prep me for my 2pm”
* “What’s open with Dana before our call?”

Claude for Outlook shares context with Claude for Excel, PowerPoint, and
Word, so Claude can work across your open Office apps in a single
conversation. For example, you can open an attached letter of intent in
Word with the email thread already loaded as context, or pull numbers from
an email into an open Excel model, without copying between apps.
For setup instructions, see

##  Model availability

When you sign in with a Claude account, you can choose between Claude
Opus 4.7, Opus 4.6, and Sonnet 4.6. When you connect through a
third-party platform such as Amazon Bedrock, Vertex AI, Azure AI Foundry,
or an LLM gateway, Claude for Outlook supports Claude Opus 4.7 and later
and Claude Sonnet 5 and later. Earlier model generations are not available
in Outlook on those platforms.

##  How Claude accesses your mailbox

Claude reads the email or event you have open via Office.js. For anything
that spans your mailbox or calendar, including thread retrieval, search,
free/busy lookups, and move or flag operations, Claude uses Microsoft
Graph. All Graph calls run in your browser, and the Graph access token
stays in the browser’s MSAL cache and is never sent to Anthropic.
Claude never sends mail or invites on its own. The add-in does not request
the `Mail.Send` permission. Every draft lands unsent in Outlook’s compose
or appointment form, and you click Send.

![Claude reads the open item via Office.js and uses Microsoft Graph for mailbox-wide actions; the Graph token stays in the browser.](https://mintcdn.com/claude-ai/-4jzPa4NasvobarI/images/office-agents/architecture/outlook-graph.png?fit=max&auto=format&n=-4jzPa4NasvobarI&q=85&s=3760f3ba806ce4cb2f835cfa2e409eae)

Outlook mailbox access: the open item comes through Office.js, broader mailbox actions use Microsoft Graph, and the Graph token stays in the browser.

Where mailbox content goes after Claude reads it depends on how you sign
in.

###  When you sign in with a Claude account

Mailbox content that Claude reads becomes part of the prompt sent to
`api.anthropic.com`. Standard API retention applies: see
[Data retention and audit](#data-retention-and-audit). The add-in does not
keep a server-side copy or index of your mailbox.

###  When you connect through a third-party platform

The prompt goes only to the inference endpoint you configured, such as
Amazon Bedrock, Vertex AI, Azure AI Foundry, or an LLM gateway. On Amazon
Bedrock, Vertex AI, or a gateway that routes to them, no mailbox content
reaches Anthropic. On Azure AI Foundry, Anthropic operates the Claude models
and processes prompts as an independent processor for Microsoft, as
described in
[Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry).
See
[Use Claude for M365 with third-party platforms](https://claude.com/docs/office-agents/third-party-platforms)
for configuration details. The add-in does not keep a server-side copy or
index of your mailbox.

##  Chat history

not synced across devices or browsers. You can clear all chat history
from Settings at any time. The local store is also cleared when you
clear your browser data. Chat history is specific to the combination of
the add-in surface, your user ID, and your organization ID, so your
Excel and Outlook histories are separate. Reinstalling the add-in or
switching between Claude add-ins does not remove it. See
[Data storage and retention](https://claude.com/docs/office-agents/data-storage) for where it
sits on disk and how long it is kept.
mailbox and calendar, and any files you attach. Clearing chat history
removes only the copy in your browser. It does not delete the messages
or attached files that Anthropic keeps.

##  Data retention and audit

For Claude for Outlook use, inputs and outputs are deleted on Anthropic’s
backend within 30 days of receipt or generation, except as described in
[How long do you store my organization’s data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)
Enterprise organizations can route full audit telemetry from Claude for
Outlook to their own OpenTelemetry collector for integration with a SIEM
or observability platform. See
[Configure a custom OpenTelemetry collector](https://claude.com/docs/office-agents/enterprise-readiness)
for setup. On Pro, Max, and Team plans, observability and audit
export are not available. Claude for Outlook does not inherit custom
data retention settings your organization may have configured and is not
included in Enterprise audit logs. For Enterprise organizations with the
enabled, Claude for Outlook sessions are included in the Compliance API.
This coverage requires no additional setup: the same Compliance Access
Keys apply.

##  Prompt injection risks

Be cautious with email from external or untrusted senders. Email bodies
and attachments are untrusted input and may contain instructions intended
to manipulate Claude rather than you.
Prompt injection refers to malicious instructions hidden in an email
body, signature, or attachment that try to trick the AI into taking
unintended actions. For example, a routine inbound email might contain
hidden text instructing Claude to forward a thread or draft a reply you
did not ask for. Claude may interpret these instructions as legitimate
requests.
Review every draft and inbox action before accepting it, especially when
working with email from external or untrusted senders.

##  Recommended use during beta

As a beta feature, Claude for Outlook is not recommended for:

* Unattended sending. Claude never sends mail or invites on its own; every
  draft lands unsent for your review.
* Client-facing or counterparty correspondence without reading the draft
  first.
* Replacing your judgment on which emails matter or how to handle a
  relationship.
* Mailboxes containing privileged or regulated data without appropriate
  organizational controls.

To use Claude for Outlook safely and effectively:

* Review drafted replies and invites before sending, especially recipient
  lists.
* Verify thread summaries against the cited source emails for high-stakes
  conversations.
* Apply appropriate Microsoft 365 permissions and Conditional Access
  policies for the add-in.
* Maintain human oversight for anything leaving your organization.

{"docsConfig":{"theme":"mint","$schema":"https://mintlify.com/docs.json","name":"Claude.ai Documentation","colors":{"primary":"#0E0E0E","light":"#D4A27F","dark":"#0E0E0E"},"logo":{"light":"https://mintcdn.com/claude-ai/1fyDNLAICe3KG6rB/logo/light.svg?fit=max\u0026auto=format\u0026n=1fyDNLAICe3KG6rB\u0026q=85\u0026s=e870c19cb781d8a7c7b7d19de53b0a10","dark":"https://mintcdn.com/claude-ai/1fyDNLAICe3KG6rB/logo/dark.svg?fit=max\u0026auto=format\u0026n=1fyDNLAICe3KG6rB\u0026q=85\u0026s=80cc0b06d8fd9aeefec8acb226de6866"},"favicon":"https://mintcdn.com/claude-ai/N9YeVEPVxANlc2We/favicon.ico?fit=max\u0026auto=format\u0026n=N9YeVEPVxANlc2We\u0026q=85\u0026s=a22e48fa0189917f9be516d4a555898c","background":{"color":{"light":"#FDFDF7","dark":"#09090B"}},"navbar":{"links":[{"href":"https://support.anthropic.com","label":"Support"}],"primary":{"type":"button","label":"Go to Claude","href":"https://claude.ai"}},"footer":{"socials":{"x":"https://x.com/AnthropicAI","linkedin":"https://www.linkedin.com/company/anthropicresearch"},"links":[{"header":"Company","items":[{"label":"Anthropic","href":"https://www.anthropic.com/company"},{"label":"Careers","href":"https://www.anthropic.com/careers"},{"label":"Economic Futures","href":"https://www.anthropic.com/economic-futures"},{"label":"Research","href":"https://www.anthropic.com/research"},{"label":"News","href":"https://www.anthropic.com/news"},{"label":"Trust center","href":"https://trust.anthropic.com/"},{"label":"Transparency","href":"https://www.anthropic.com/transparency"}]},{"header":"Help and security","items":[{"label":"Availability","href":"https://www.anthropic.com/supported-countries"},{"label":"Status","href":"https://status.anthropic.com/"},{"label":"Support center","href":"https://support.claude.com/"}]},{"header":"Learn","items":[{"label":"Courses","href":"https://academy.claude.com/"},{"label":"MCP connectors","href":"https://claude.com/partners/mcp"},{"label":"Customer stories","href":"https://www.claude.com/customers"},{"label":"Engineering blog","href":"https://www.anthropic.com/engineering"},{"label":"Events","href":"https://www.anthropic.com/events"},{"label":"Powered by Claude","href":"https://claude.com/partners/powered-by-claude"},{"label":"Service partners","href":"https://claude.com/partners/services"},{"label":"Startups program","href":"https://claude.com/programs/startups"}]},{"header":"Terms and policies","items":[{"label":"Privacy policy","href":"https://www.anthropic.com/legal/privacy"},{"label":"Disclosure policy","href":"https://www.anthropic.com/responsible-disclosure-policy"},{"label":"Usage policy","href":"https://www.anthropic.com/legal/aup"},{"label":"Commercial terms","href":"https://www.anthropic.com/legal/commercial-terms"},{"label":"Consumer terms","href":"https://www.anthropic.com/legal/consumer-terms"}]}]},"seo":{"metatags":{"canonical":"https://claude.com/docs"}},"fonts":{"family":"Anthropic Sans"},"contextual":{"options":["copy","view","claude"],"display":"header"},"styling":{"latex":false},"navigation":{"pages":[]}},"deployment":{"deploymentMetadataValue":{"subdomain":"claude-ai","hasAudioNarration":false,"actualSubdomain":"claude-ai","customDomains":["claude.com"],"gitSource":{"type":"github","owner":"anthropics","repo":"claude-ai-docs","deployBranch":"main","contentDirectory":"","isPrivate":true,"mountPath":"","label":""},"feedback":{"thumbs":true},"entitlements":{"AI\_CHAT":{"status":"ENABLED"},"REMOVE\_BRANDING":{"status":"ENABLED"},"CONTEXTUAL\_FEEDBACK":{"status":"ENABLED"},"CODE\_SNIPPET\_FEEDBACK":{"status":"ENABLED"},"WEB\_MCP":{"status":"ENABLED"},"NARRATION":{"status":"ENABLED"}},"buildId":"6aef88df59edac7bace6f131","clientVersion":"0.0.4087","searchFilterCounts":[{"language":"default","tag":"Claude Tag","count":76},{"language":"default","tag":"For administrators","count":61},{"language":"default","tag":"Claude for Government","count":44},{"language":"default","tag":"Claude on third-party platforms","count":42},{"language":"default","tag":"Claude Desktop","count":42},{"language":"default","tag":"Claude Science","count":41},{"language":"default","tag":"Build for Claude","count":30},{"language":"default","tag":"Set up Claude Tag","count":30},{"language":"default","tag":"Use Claude Science","count":23},{"language":"default","tag":"Customize Claude","count":22}]},"assistantConfig":{"enableAskAiButton":false,"enableStarterQuestions":false,"enableAskAiSearchBar":true},"basePath":"/docs","hasChatPermissions":true,"hasWebMcpPermissions":true,"toggles":[{"name":"kill-isr","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"agent-mintlify-slack","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"agent-integrations-settings","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"rbac-expansion","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"automations-pr-grouping","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"custom-prefix","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"analytics-v7","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"user-flows-analytics","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"no-publish-flow","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"workos-onboarding","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"llms-txt-v2","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"snapshot-serving-live","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"stripTemperatureMiddleware","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"support-platform-pylon-zendesk","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"snapshot-serving","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"instant-rollback","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"granular-notifications-server","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"granular-notifications","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"automations-fable","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"fixed-ai-action-pricing","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"automation-resolve-merge-conflict","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"scoped-publishing","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"mintql","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"page-level-analytics","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"editor-version-history-v2","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"billing-page-v2","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"full-page-search","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"workspace-projects","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"assistant-v5","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"fork-pr-previews","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"revalidation-jwt","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"workos-sso-scim","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"hobby-abuse-scan","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"dashboard-inbox","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"workos-signup","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"turbopuffer-dual-write","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"workos-enabled","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"approve-review-flow","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"editor-metadata","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"sso-setup-deadline-banner","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"turbopuffer-serve","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"live-agents","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false},{"name":"comment-mode","enabled":true,"variant":{"name":"disabled","enabled":false,"feature\_enabled":true},"impressionData":false}],"googleFontsInlined":false},"customCss":[{"filePath":"style.css","href":"/docs/\_mintlify/custom/claude-ai/f864c4801ebb83ca/style.css"}],"page":{"pagePath":"office-agents/outlook","slug":"/office-agents/outlook","pageMetadata":{"title":"Use Claude for Outlook","description":"An Outlook add-in that integrates Claude into your inbox and calendar, for Pro, Max, Team, and Enterprise plans.","href":"/office-agents/outlook"},"description":{"compiledSource":"\"use strict\";\nconst {jsx: \_jsx} = arguments[0];\nconst {useMDXComponents: \_provideComponents} = arguments[0];\nfunction \_createMdxContent(props) {\n const \_components = {\n p: \"p\",\n ...\_provideComponents(),\n ...props.components\n };\n return \_jsx(\_components.p, {\n children: \"An Outlook add-in that integrates Claude into your inbox and calendar, for Pro, Max, Team, and Enterprise plans.\"\n });\n}\nfunction MDXContent(props = {}) {\n const {wrapper: MDXLayout} = {\n ...\_provideComponents(),\n ...props.components\n };\n return MDXLayout ? \_jsx(MDXLayout, {\n ...props,\n children: \_jsx(\_createMdxContent, {\n ...props\n })\n }) : \_createMdxContent(props);\n}\nreturn {\n default: MDXContent\n};\n","frontmatter":{},"scope":{}},"pageType":"default","mdx":{"mdxSource":{"compiledSource":"\"use strict\";const{Fragment:\_Fragment,jsx:\_jsx,jsxs:\_jsxs}=arguments[0];const{useMDXComponents:\_provideComponents}=arguments[0];function \_createMdxContent(props){const \_components={a:`a`,code:`code`,li:`li`,p:`p`,pre:`pre`,span:`span`,tbody:`tbody`,td:`td`,th:`th`,thead:`thead`,tr:`tr`,ul:`ul`,...\_provideComponents(),...props.components},{CodeBlock,Frame,Heading,Note,OptimizedImage,Step,Steps,Table,Warning}=\_components;if(!CodeBlock)\_missingMdxReference(`CodeBlock`,true);if(!Frame)\_missingMdxReference(`Frame`,true);if(!Heading)\_missingMdxReference(`Heading`,true);if(!Note)\_missingMdxReference(`Note`,true);if(!OptimizedImage)\_missingMdxReference(`OptimizedImage`,true);if(!Step)\_missingMdxReference(`Step`,true);if(!Steps)\_missingMdxReference(`Steps`,true);if(!Table)\_missingMdxReference(`Table`,true);if(!Warning)\_missingMdxReference(`Warning`,true);return \_jsxs(\_Fragment,{children:[\_jsx(Warning,{children:\_jsxs(\_components.p,{children:[`After the September and October 2026 Microsoft 365 updates on Windows, some\nusers are missing their chat history and uploaded skills in the Claude add-in.\nAnthropic is working with Microsoft to solve this issue. In the meantime, see\n`,\_jsx(\_components.a,{href:`/office-agents/data-storage#chat-history-and-skills-missing-after-a-microsoft-365-update-on-windows`,children:`what you and your IT team can do`}),`.`]})}),`\n`,\_jsx(\_components.p,{children:`Claude for Outlook is an add-in that brings Claude into your Outlook inbox\nand calendar. It is built for professionals whose work runs through email,\nincluding private equity and investment banking associates managing deal\nflow, in-house legal teams running counterparty negotiations, and\nconsultants tracking multiple client threads.`}),`\n`,\_jsx(Note,{children:\_jsx(\_components.p,{children:`Claude for Outlook is currently in beta and available to Pro, Max, Team,\nand Enterprise plans.`})}),`\n`,\_jsx(Heading,{level:`2`,id:`what-you-can-do`,children:`What you can do`}),`\n`,\_jsx(\_components.p,{children:`With Claude for Outlook, you can:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`Triage your unread inbox into what needs you, what Claude can handle,\nand what is noise.`}),`\n`,\_jsx(\_components.li,{children:`Draft replies, reply-alls, and forwards in your voice, landed unsent in\nOutlook’s compose pane.`}),`\n`,\_jsx(\_components.li,{children:`Summarize long threads into decisions made, open items, and who owes\nwhat, with per-email citations.`}),`\n`,\_jsxs(\_components.li,{children:[`Read `,\_jsx(\_components.code,{children:`.docx`}),` and `,\_jsx(\_components.code,{children:`.xlsx`}),` attachments inline without opening them.`]}),`\n`,\_jsx(\_components.li,{children:`Find meeting times across attendees and draft invites into Outlook’s\nnative appointment form.`}),`\n`,\_jsx(\_components.li,{children:`Prep for your next meeting with a one-page brief of recent threads and\nattached documents.`}),`\n`]}),`\n`,\_jsx(Heading,{level:`2`,id:`get-started-with-claude-for-outlook`,children:`Get started with Claude for Outlook`}),`\n`,\_jsx(Heading,{level:`3`,id:`supported-versions`,children:`Supported versions`}),`\n`,\_jsx(\_components.p,{children:`Claude for Outlook runs on the following Outlook clients.`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`Outlook on the web`}),`\n`,\_jsx(\_components.li,{children:`Outlook on Windows, both new Outlook and classic Outlook, with a\nMicrosoft 365 subscription`}),`\n`,\_jsx(\_components.li,{children:`Outlook on Mac with a Microsoft 365 subscription`}),`\n`]}),`\n`,\_jsx(\_components.p,{children:`The following are not supported: Outlook 2016 and 2019 perpetual or\nvolume-licensed editions, Outlook on iOS, Outlook on Android, and\nmailboxes hosted on Exchange on-premises. Exchange Online through\nMicrosoft 365 is required.`}),`\n`,\_jsx(Heading,{level:`3`,id:`install-for-yourself`,children:`Install for yourself`}),`\n`,\_jsxs(Steps,{children:[\_jsx(Step,{title:`Open the marketplace listing`,children:\_jsxs(\_components.p,{children:[`Go to the `,\_jsx(\_components.a,{href:`https://marketplace.microsoft.com/en-us/product/office/WA200010724?tab=Overview`,children:`Claude for Outlook listing on Microsoft AppSource`}),`.`]})}),\_jsx(Step,{title:`Install the add-in`,children:\_jsx(\_components.p,{children:`Select “Get it now” to install.`})}),\_jsx(Step,{title:`Open Claude in Outlook`,children:\_jsx(\_components.p,{children:`Open Outlook, open any email, select the Claude button in the message\nribbon, and sign in with your Claude account.`})})]}),`\n`,\_jsx(\_components.p,{children:`If you do not see the Claude button on the message, open the overflow menu\non the reading pane, choose Customize actions, and check Claude under\nApps. It then appears on every message and in the Home ribbon.`}),`\n`,\_jsx(Heading,{level:`3`,id:`deploy-to-your-organization`,children:`Deploy to your organization`}),`\n`,\_jsx(\_components.p,{children:`Organization admins can deploy Claude for Outlook through the Microsoft\n365 Admin Center.`}),`\n`,\_jsxs(Steps,{children:[\_jsx(Step,{title:`Allow Office Store access`,children:\_jsxs(\_components.p,{children:[`In the `,\_jsx(\_components.a,{href:`https://admin.microsoft.com`,children:`Microsoft 365 Admin Center`}),`, go\nto Settings, Org Settings, User owned apps and services, and turn on\n`,\_jsx(\_components.a,{href:`https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-addins-in-the-admin-center`,children:`“Let users access the Office Store”`}),`.`]})}),\_jsx(Step,{title:`Open Integrated apps`,children:\_jsx(\_components.p,{children:`Go to Settings, then Integrated apps.`})}),\_jsx(Step,{title:`Find the add-in`,children:\_jsx(\_components.p,{children:`Search for “Claude for Outlook” in Microsoft AppSource.`})}),\_jsx(Step,{title:`Deploy`,children:\_jsxs(\_components.p,{children:[`Deploy the add-in to your organization or to specific people. See\n`,\_jsx(\_components.a,{href:`https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins`,children:`Microsoft’s deployment guide`}),`\nfor assignment options.`]})}),\_jsx(Step,{title:`Grant Microsoft Graph consent`,children:\_jsxs(\_components.p,{children:[`Complete the `,\_jsx(\_components.a,{href:`#grant-microsoft-graph-consent`,children:`Microsoft Graph admin consent`}),`\nstep below so users are not prompted individually.`]})})]}),`\n`,\_jsx(Note,{children:\_jsxs(\_components.p,{children:[`If your organization uses Microsoft Entra Privileged Identity\nManagement (PIM) for admin roles, the Integrated apps page does not\nrecognize roles activated through PIM, so deployment fails. This is a\n`,\_jsx(\_components.a,{href:`https://learn.microsoft.com/en-us/office/dev/add-ins/resources/resources-office-add-in-known-issues`,children:`known Microsoft issue`}),`,\ntracking ID 11126536. To work around it, deploy from an admin account\nwith the required role assigned as permanently active rather than\nPIM-eligible. See\n`,\_jsx(\_components.a,{href:`https://learn.microsoft.com/en-us/troubleshoot/microsoft-365/admin/miscellaneous/cannot-deploy-add-in-integrated-apps-menu`,children:`Microsoft’s troubleshooting guidance`}),`.\nIndividual users can still\n`,\_jsx(\_components.a,{href:`#install-for-yourself`,children:`install the add-in themselves`}),`.`]})}),`\n`,\_jsx(\_components.p,{children:`After installation, team members open Outlook, open any email, select the\nClaude button in the message ribbon, and sign in with their Claude\ncredentials. Pinning the task pane keeps it open as you move between\nmessages.`}),`\n`,\_jsx(Warning,{children:\_jsx(\_components.p,{children:`Organizations that have disabled “Let users access the Office Store” may\nfind that admin-deployed add-ins don’t appear for users. To work around\nthis, deploy using the manifest XML file described below.`})}),`\n`,\_jsx(Heading,{level:`3`,id:`install-from-a-manifest-file`,children:`Install from a manifest file`}),`\n`,\_jsx(\_components.p,{children:`If your organization blocks the Microsoft Store, an IT administrator can\ndeploy the add-in by uploading its manifest file directly.`}),`\n`,\_jsxs(Steps,{children:[\_jsx(Step,{title:`Download the manifest`,children:\_jsxs(\_components.p,{children:[`Download the\n`,\_jsx(\_components.a,{href:`https://pivot.claude.ai/manifest-outlook.xml`,children:`Claude for Outlook manifest`}),`\nand save it to a secure location.`]})}),\_jsx(Step,{title:`Open Integrated apps`,children:\_jsxs(\_components.p,{children:[`In the `,\_jsx(\_components.a,{href:`https://admin.microsoft.com`,children:`Microsoft 365 Admin Center`}),`, go\nto Settings, then Integrated apps.`]})}),\_jsx(Step,{title:`Upload the add-in`,children:\_jsx(\_components.p,{children:`Select Upload custom apps, then Office Add-in. Choose “I have a\nmanifest file on this device”, select the file you downloaded, and\nupload it.`})}),\_jsx(Step,{title:`Assign people`,children:\_jsx(\_components.p,{children:`Choose your deployment scope: the entire organization, specific\npeople, specific groups, or just yourself for testing.`})}),\_jsx(Step,{title:`Deploy`,children:\_jsx(\_components.p,{children:`Review the settings and select Deploy. The add-in appears within\nminutes for most people. Full organization rollout can take up to 24\nhours on the Microsoft 365 side.`})}),\_jsx(Step,{title:`Grant Microsoft Graph consent`,children:\_jsx(\_components.p,{children:`Complete the consent step in the next section.`})})]}),`\n`,\_jsx(Heading,{level:`3`,id:`grant-microsoft-graph-consent`,children:`Grant Microsoft Graph consent`}),`\n`,\_jsx(\_components.p,{children:`Claude for Outlook reads mail and calendar data through Microsoft Graph.\nThis requires a one-time tenant-wide grant from a Global Administrator\nand is separate from the Integrated apps deployment.`}),`\n`,\_jsx(\_components.p,{children:`Have a Global Administrator open the following admin consent link in a\nbrowser where they are signed in to your Microsoft 365 tenant.`}),`\n`,\_jsx(CodeBlock,{numberOfLines:`2`,language:`text`,children:\_jsx(\_components.pre,{className:`shiki shiki-themes github-light-default dark-plus`,style:{backgroundColor:`#ffffff`,\"--shiki-dark-bg\":`#0B0C0E`,color:`#1f2328`,\"--shiki-dark\":`#D4D4D4`},language:`text`,children:\_jsxs(\_components.code,{language:`text`,numberOfLines:`2`,children:[\_jsx(\_components.span,{className:`line`,children:\_jsx(\_components.span,{children:`https://login.microsoftonline.com/organizations/v2.0/adminconsent?client\_id=c2995f31-11e7-4882-b7a7-ef9def0a0266\u0026scope=https://graph.microsoft.com/Mail.ReadWrite%20https://graph.microsoft.com/Calendars.Read%20https://graph.microsoft.com/User.Read%20offline\_access\u0026redirect\_uri=https://pivot.claude.ai/auth/callback`})}),`\n`,\_jsx(\_components.span,{className:`line`,children:\_jsx(\_components.span,{})})]})})}),`\n`,\_jsxs(\_components.p,{children:[`The administrator sees a Microsoft permissions screen listing\n`,\_jsx(\_components.code,{children:`Mail.ReadWrite`}),`, `,\_jsx(\_components.code,{children:`Calendars.Read`}),`, `,\_jsx(\_components.code,{children:`User.Read`}),`, and `,\_jsx(\_components.code,{children:`offline\_access`}),`.\nAfter they select Accept, all users in the organization\ncan use Claude for Outlook without additional Microsoft prompts. The grant\ntakes effect immediately. Only the add-in rollout in the previous step can\ntake up to 24 hours.`]}),`\n`,\_jsx(\_components.p,{children:`If this step is skipped, every user sees a “Need admin approval” message\nwhen Claude first tries to read mail or calendar data.`}),`\n`,\_jsxs(\_components.p,{children:[`The redirect to `,\_jsx(\_components.code,{children:`pivot.claude.ai`}),` after consent carries only the consent\noutcome, never a token or authorization code. See\n`,\_jsx(\_components.a,{href:`/office-agents/third-party-platforms#why-sign-in-redirects-through-pivot-claude-ai`,children:`Why sign-in redirects through pivot.claude.ai`}),`\nfor what each redirect carries and how to verify it in a network capture.`]}),`\n`,\_jsx(Heading,{level:`4`,id:`use-your-own-entra-app-instead`,children:`Use your own Entra app instead`}),`\n`,\_jsx(\_components.p,{children:`If your organization’s policy does not permit consenting to a third-party\nmulti-tenant application, register a single-tenant application in the\nMicrosoft Entra admin center and have the add-in use it instead. The data\nflow is identical; the Graph token stays in the user’s Outlook client\neither way. The difference is that approval and Conditional Access policy\nlive entirely under an application your organization owns.`}),`\n`,\_jsxs(Steps,{children:[\_jsx(Step,{title:`Register the application`,children:\_jsx(\_components.p,{children:`In the Entra admin center, go to App registrations and create a new\nregistration. Choose “Accounts in this organizational directory only”.`})}),\_jsx(Step,{title:`Configure authentication`,children:\_jsxs(\_components.p,{children:[`Under Authentication, add a Single-page application platform with\nredirect URI `,\_jsx(\_components.code,{children:`brk-multihub://pivot.claude.ai`}),`. In Advanced settings,\nset “Allow public client flows” to Yes.`]})}),\_jsx(Step,{title:`Add Graph permissions`,children:\_jsxs(\_components.p,{children:[`Under API permissions, add the Microsoft Graph delegated permissions\n`,\_jsx(\_components.code,{children:`Mail.ReadWrite`}),`, `,\_jsx(\_components.code,{children:`Calendars.Read`}),`, `,\_jsx(\_components.code,{children:`User.Read`}),`, and `,\_jsx(\_components.code,{children:`offline\_access`}),`.\nSelect “Grant admin consent” for your tenant.`]})}),\_jsx(Step,{title:`Add the client ID to the manifest`,children:\_jsxs(\_components.p,{children:[`Copy the application’s client ID from the Overview page. Download the\nmanifest from the\n`,\_jsx(\_components.a,{href:`#install-from-a-manifest-file`,children:`Install from a manifest file`}),` section\nand open it in a text editor. Search for `,\_jsx(\_components.code,{children:`https://pivot.claude.ai/?m=`}),`.\nAt the end of every URL that starts this way, inside the quotation\nmarks, add `,\_jsx(\_components.code,{children:`\u0026amp;graph\_client\_id=YOUR\_CLIENT\_ID`}),`. Lines that refer to a\nURL by `,\_jsx(\_components.code,{children:`resid`}),` need no change, and neither do the icon or support\nURLs. Save the file, then upload and deploy it as that section\ndescribes.`]})})]}),`\n`,\_jsxs(\_components.p,{children:[`The following example shows one edited line. The version number in your\nfile can differ. Type `,\_jsx(\_components.code,{children:`\u0026amp;`}),` exactly as shown: an XML file cannot contain\n`,\_jsx(\_components.code,{children:`\u0026`}),` on its own.`]}),`\n`,\_jsx(CodeBlock,{filename:``,numberOfLines:`1`,language:`xml`,children:\_jsx(\_components.pre,{className:`shiki shiki-themes github-light-default dark-plus`,style:{backgroundColor:`#ffffff`,\"--shiki-dark-bg\":`#0B0C0E`,color:`#1f2328`,\"--shiki-dark\":`#D4D4D4`},language:`xml`,children:\_jsxs(\_components.code,{language:`xml`,numberOfLines:`1`,children:[\_jsxs(\_components.span,{className:`line`,children:[\_jsx(\_components.span,{style:{color:`#1F2328`,\"--shiki-dark\":`#808080`},children:`\u003c`}),\_jsx(\_components.span,{style:{color:`#116329`,\"--shiki-dark\":`#569CD6`},children:`bt:Url`}),\_jsx(\_components.span,{style:{color:`#0550AE`,\"--shiki-dark\":`#9CDCFE`},children:` id`}),\_jsx(\_components.span,{style:{color:`#1F2328`,\"--shiki-dark\":`#D4D4D4`},children:`=`}),\_jsx(\_components.span,{style:{color:`#0A3069`,\"--shiki-dark\":`#CE9178`},children:`\"Taskpane.Url\"`}),\_jsx(\_components.span,{style:{color:`#0550AE`,\"--shiki-dark\":`#9CDCFE`},children:` DefaultValue`}),\_jsx(\_components.span,{style:{color:`#1F2328`,\"--shiki-dark\":`#D4D4D4`},children:`=`}),\_jsx(\_components.span,{style:{color:`#0A3069`,\"--shiki-dark\":`#CE9178`},children:`\"https://pivot.claude.ai/?m=outlook-1.0.0.5`}),\_jsx(\_components.span,{style:{color:`#CF222E`,\"--shiki-dark\":`#569CD6`},children:`\u0026amp;`}),\_jsx(\_components.span,{style:{color:`#0A3069`,\"--shiki-dark\":`#CE9178`},children:`graph\_client\_id=YOUR\_CLIENT\_ID\"`}),\_jsx(\_components.span,{style:{color:`#1F2328`,\"--shiki-dark\":`#808080`},children:`/>`})]}),`\n`]})})}),`\n`,\_jsx(\_components.p,{children:`With this option, skip the admin consent link entirely. Users do not see a\nMicrosoft permissions prompt because your tenant has already consented to\nyour own application.`}),`\n`,\_jsxs(\_components.p,{children:[`If you deploy through a third-party platform and generate your manifests\nwith the `,\_jsx(\_components.a,{href:`/office-agents/third-party-platforms#run-the-setup-wizard`,children:`setup wizard`}),`,\nprovide the client ID to the wizard as `,\_jsx(\_components.code,{children:`graph\_client\_id`}),` instead of\nediting the file. See\n`,\_jsx(\_components.a,{href:`/office-agents/third-party-platforms#deploy-to-outlook`,children:`Deploy to Outlook`}),`.`]}),`\n`,\_jsx(Heading,{level:`3`,id:`deploy-in-a-us-government-or-national-cloud`,children:`Deploy in a US Government or national cloud`}),`\n`,\_jsxs(\_components.p,{children:[`If your Microsoft 365 tenant is in GCC High, DoD, or 21Vianet, register\nyour own Entra application with `,\_jsx(\_components.code,{children:`graph\_client\_id`}),` as described above\n(Anthropic’s multi-tenant application exists only in the global cloud)\nand set `,\_jsx(\_components.code,{children:`graph\_cloud`}),` to the matching value:`]}),`\n`,\_jsxs(Table,{children:[\_jsx(\_components.thead,{children:\_jsxs(\_components.tr,{children:[\_jsx(\_components.th,{children:`Tenant`}),\_jsx(\_components.th,{children:\_jsx(\_components.code,{children:`graph\_cloud`})})]})}),\_jsxs(\_components.tbody,{children:[\_jsxs(\_components.tr,{children:[\_jsx(\_components.td,{children:`Commercial or GCC`}),\_jsxs(\_components.td,{children:[\_jsx(\_components.code,{children:`global`}),` (default; may be omitted)`]})]}),\_jsxs(\_components.tr,{children:[\_jsx(\_components.td,{children:`GCC High`}),\_jsx(\_components.td,{children:\_jsx(\_components.code,{children:`us-gov-high`})})]}),\_jsxs(\_components.tr,{children:[\_jsx(\_components.td,{children:`DoD`}),\_jsx(\_components.td,{children:\_jsx(\_components.code,{children:`us-gov-dod`})})]}),\_jsxs(\_components.tr,{children:[\_jsx(\_components.td,{children:`21Vianet (China)`}),\_jsx(\_components.td,{children:\_jsx(\_components.code,{children:`china`})})]})]})]}),`\n`,\_jsxs(\_components.p,{children:[`For a DoD tenant, every URL in the manifest that starts with\n`,\_jsx(\_components.code,{children:`https://pivot.claude.ai/?m=`}),` ends with:`]}),`\n`,\_jsx(CodeBlock,{numberOfLines:`2`,language:`text`,children:\_jsx(\_components.pre,{className:`shiki shiki-themes github-light-default dark-plus`,style:{backgroundColor:`#ffffff`,\"--shiki-dark-bg\":`#0B0C0E`,color:`#1f2328`,\"--shiki-dark\":`#D4D4D4`},language:`text`,children:\_jsxs(\_components.code,{language:`text`,numberOfLines:`2`,children:[\_jsx(\_components.span,{className:`line`,children:\_jsx(\_components.span,{children:`\u0026amp;graph\_client\_id=YOUR\_CLIENT\_ID\u0026amp;graph\_cloud=us-gov-dod`})}),`\n`,\_jsx(\_components.span,{className:`line`,children:\_jsx(\_components.span,{})})]})})}),`\n`,\_jsxs(\_components.p,{children:[`For GCC High and 21Vianet tenants, `,\_jsx(\_components.code,{children:`graph\_cloud`}),` may be omitted: the\nadd-in detects those clouds at sign-in from the authority host Outlook\nreports. Setting it explicitly is still recommended when your compliance\nprogram requires the endpoints to be fixed in the reviewed manifest\nrather than derived at runtime. DoD tenants share an authority host with\nGCC High, so `,\_jsx(\_components.code,{children:`graph\_cloud=us-gov-dod`}),` is always required for DoD.`]}),`\n`,\_jsx(Heading,{level:`3`,id:`connect-through-a-third-party-platform`,children:`Connect through a third-party platform`}),`\n`,\_jsx(\_components.p,{children:`If your organization routes API traffic through an internal LLM gateway,\nAmazon Bedrock, Google Cloud Vertex AI, or Azure AI Foundry, you can use\nthe add-in without Claude accounts. This is the same gateway pattern used\nby Claude Code.`}),`\n`,\_jsxs(\_components.p,{children:[`For setup instructions and gateway requirements, see\n`,\_jsx(\_components.a,{href:`/office-agents/third-party-platforms`,children:`Use Claude for M365 with third-party platforms`}),`.`]}),`\n`,\_jsx(Heading,{level:`2`,id:`triage-your-inbox`,children:`Triage your inbox`}),`\n`,\_jsx(\_components.p,{children:`Ask Claude what needs your attention. Claude reads your unread mail and\nattachments and sorts them into three groups: action items for you, items\nClaude can handle for your review, and noise you can archive in one\nselection. Each action item carries a one-line reason. Items Claude can\nhandle, such as scheduling asks, acknowledgments, and standard-form\ndocuments, arrive pre-drafted.`}),`\n`,\_jsx(\_components.p,{children:`Prompts to try:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“What needs me?”`}),`\n`,\_jsx(\_components.li,{children:`“Draft replies for everything you can handle”`}),`\n`,\_jsx(\_components.li,{children:`“Archive all the calendar responses and newsletters”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`2`,id:`draft-replies-in-your-voice`,children:`Draft replies in your voice`}),`\n`,\_jsx(\_components.p,{children:`Tell Claude what you want to say. It drafts the reply into Outlook’s\nnative compose pane, unsent. Tone is learned from your sent folder, so\nthe draft matches your sentence length and formality register. Claude\nleaves the closing off so Outlook can append your configured signature\nwithout duplication.\nClaude chooses reply versus reply-all deliberately and warns before adding\nanyone who was not on the thread.`}),`\n`,\_jsx(\_components.p,{children:`Prompts to try:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Reply to this and agree to the extension, push back on the fee”`}),`\n`,\_jsx(\_components.li,{children:`“Reply-all thanking everyone and confirming Thursday works”`}),`\n`,\_jsx(\_components.li,{children:`“Forward this to Dana with a two-line summary”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`2`,id:`summarize-long-threads`,children:`Summarize long threads`}),`\n`,\_jsx(\_components.p,{children:`Claude reads the entire conversation, including every reply and forward,\nand tells you what has been decided, what is still open, and who owes\nwhat. Every claim cites the specific email it came from. Selecting a\ncitation opens that message in Outlook.`}),`\n`,\_jsx(\_components.p,{children:`Prompts to try:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“What’s been decided and what’s still open?”`}),`\n`,\_jsx(\_components.li,{children:`“Who owes what on this thread?”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`2`,id:`read-attachments-inline`,children:`Read attachments inline`}),`\n`,\_jsxs(\_components.p,{children:[`Claude reads `,\_jsx(\_components.code,{children:`.docx`}),` and `,\_jsx(\_components.code,{children:`.xlsx`}),` attachments on the open email without\nyou opening them. For `,\_jsx(\_components.code,{children:`.pptx`}),` attachments, open the deck in PowerPoint\nwith the thread loaded as context using\n`,\_jsx(\_components.a,{href:`/office-agents/work-across-apps`,children:`Work across M365 apps`}),`. PDF attachments\nare not currently read inline; save the file and upload it through the\nsidebar instead.`]}),`\n`,\_jsx(\_components.p,{children:`Prompts to try:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Summarize the attached memo”`}),`\n`,\_jsx(\_components.li,{children:`“What’s in the spreadsheet on this email?”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`2`,id:`search-your-mailbox`,children:`Search your mailbox`}),`\n`,\_jsx(\_components.p,{children:`Ask Claude to find a past conversation by topic, not only by keywords.\nResults return as citations that open the source message in Outlook so\nyou can verify every answer against the original email.`}),`\n`,\_jsx(\_components.p,{children:`Prompts to try:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“When did we last discuss the cap with Fernwood?”`}),`\n`,\_jsx(\_components.li,{children:`“Find the email where Dana sent the revised term sheet”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`2`,id:`find-time-and-create-events`,children:`Find time and create events`}),`\n`,\_jsx(\_components.p,{children:`Claude checks free/busy for everyone whose calendar you can see and\nproposes slots that respect working hours and existing holds. The invite\nis drafted into Outlook’s native appointment form with attendees, subject,\nand agenda for you to review and send.`}),`\n`,\_jsx(\_components.p,{children:`To make a meeting repeat, open it for editing as the organizer and ask\nClaude. This works on a new invite, a saved meeting, or a whole series.\nClaude lists the pattern, dates, time, and time zone it will set and waits\nfor you to allow the change. Nothing is saved or sent until you click Save\nor Send in Outlook. All-day events are not supported.`}),`\n`,\_jsx(\_components.p,{children:`Prompts to try:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Find 30 minutes with Dana and the Fernwood team next week”`}),`\n`,\_jsx(\_components.li,{children:`“Block Thursday afternoon for deep work”`}),`\n`,\_jsx(\_components.li,{children:`“Make this weekly through the end of June”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`2`,id:`prep-for-meetings`,children:`Prep for meetings`}),`\n`,\_jsx(\_components.p,{children:`For your next event, Claude pulls the last thread with each attendee and\nany attached documents into a one-page brief, so you walk in knowing the\nopen items and what each person last said.`}),`\n`,\_jsx(\_components.p,{children:`Prompts to try:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`“Prep me for my 2pm”`}),`\n`,\_jsx(\_components.li,{children:`“What’s open with Dana before our call?”`}),`\n`]}),`\n`,\_jsx(Heading,{level:`2`,id:`work-across-m365-apps`,children:`Work across M365 apps`}),`\n`,\_jsx(\_components.p,{children:`Claude for Outlook shares context with Claude for Excel, PowerPoint, and\nWord, so Claude can work across your open Office apps in a single\nconversation. For example, you can open an attached letter of intent in\nWord with the email thread already loaded as context, or pull numbers from\nan email into an open Excel model, without copying between apps.`}),`\n`,\_jsxs(\_components.p,{children:[`For setup instructions, see\n`,\_jsx(\_components.a,{href:`/office-agents/work-across-apps`,children:`Work across M365 apps`}),`.`]}),`\n`,\_jsx(Heading,{level:`2`,id:`model-availability`,children:`Model availability`}),`\n`,\_jsx(\_components.p,{children:`When you sign in with a Claude account, you can choose between Claude\nOpus 4.7, Opus 4.6, and Sonnet 4.6. When you connect through a\nthird-party platform such as Amazon Bedrock, Vertex AI, Azure AI Foundry,\nor an LLM gateway, Claude for Outlook supports Claude Opus 4.7 and later\nand Claude Sonnet 5 and later. Earlier model generations are not available\nin Outlook on those platforms.`}),`\n`,\_jsx(Heading,{level:`2`,id:`how-claude-accesses-your-mailbox`,children:`How Claude accesses your mailbox`}),`\n`,\_jsx(\_components.p,{children:`Claude reads the email or event you have open via Office.js. For anything\nthat spans your mailbox or calendar, including thread retrieval, search,\nfree/busy lookups, and move or flag operations, Claude uses Microsoft\nGraph. All Graph calls run in your browser, and the Graph access token\nstays in the browser’s MSAL cache and is never sent to Anthropic.`}),`\n`,\_jsxs(\_components.p,{children:[`Claude never sends mail or invites on its own. The add-in does not request\nthe `,\_jsx(\_components.code,{children:`Mail.Send`}),` permission. Every draft lands unsent in Outlook’s compose\nor appointment form, and you click Send.`]}),`\n`,\_jsx(Frame,{caption:`Outlook mailbox access: the open item comes through Office.js, broader mailbox actions use Microsoft Graph, and the Graph token stays in the browser.`,children:\_jsx(OptimizedImage,{src:`https://mintcdn.com/claude-ai/-4jzPa4NasvobarI/images/office-agents/architecture/outlook-graph.png?fit=max\u0026auto=format\u0026n=-4jzPa4NasvobarI\u0026q=85\u0026s=3760f3ba806ce4cb2f835cfa2e409eae`,alt:`Claude reads the open item via Office.js and uses Microsoft Graph for mailbox-wide actions; the Graph token stays in the browser.`,\"data-og-width\":`2540`,width:`2540`,\"data-og-height\":`1294`,height:`1294`,\"data-path\":`images/office-agents/architecture/outlook-graph.png`,\"data-optimize\":`true`,\"data-opv\":`3`,srcset:`https://mintcdn.com/claude-ai/-4jzPa4NasvobarI/images/office-agents/architecture/outlook-graph.png?w=280\u0026fit=max\u0026auto=format\u0026n=-4jzPa4NasvobarI\u0026q=85\u0026s=ce6168d8efefff5f955a090935e977a4 280w, https://mintcdn.com/claude-ai/-4jzPa4NasvobarI/images/office-agents/architecture/outlook-graph.png?w=560\u0026fit=max\u0026auto=format\u0026n=-4jzPa4NasvobarI\u0026q=85\u0026s=1f50a71dcfec723c489bafba8f6caaa7 560w, https://mintcdn.com/claude-ai/-4jzPa4NasvobarI/images/office-agents/architecture/outlook-graph.png?w=840\u0026fit=max\u0026auto=format\u0026n=-4jzPa4NasvobarI\u0026q=85\u0026s=94317973806c0dc912d648cda3cf1f4d 840w, https://mintcdn.com/claude-ai/-4jzPa4NasvobarI/images/office-agents/architecture/outlook-graph.png?w=1100\u0026fit=max\u0026auto=format\u0026n=-4jzPa4NasvobarI\u0026q=85\u0026s=d04f5225e6cffd6354974c9ede1fa79d 1100w, https://mintcdn.com/claude-ai/-4jzPa4NasvobarI/images/office-agents/architecture/outlook-graph.png?w=1650\u0026fit=max\u0026auto=format\u0026n=-4jzPa4NasvobarI\u0026q=85\u0026s=eb432aa5113bb28cefbb09bff77920a9 1650w, https://mintcdn.com/claude-ai/-4jzPa4NasvobarI/images/office-agents/architecture/outlook-graph.png?w=2500\u0026fit=max\u0026auto=format\u0026n=-4jzPa4NasvobarI\u0026q=85\u0026s=fb4a8fa42c6d357df9f9fd390d986da1 2500w`})}),`\n`,\_jsx(\_components.p,{children:`Where mailbox content goes after Claude reads it depends on how you sign\nin.`}),`\n`,\_jsx(Heading,{level:`3`,id:`when-you-sign-in-with-a-claude-account`,children:`When you sign in with a Claude account`}),`\n`,\_jsxs(\_components.p,{children:[`Mailbox content that Claude reads becomes part of the prompt sent to\n`,\_jsx(\_components.code,{children:`api.anthropic.com`}),`. Standard API retention applies: see\n`,\_jsx(\_components.a,{href:`#data-retention-and-audit`,children:`Data retention and audit`}),`. The add-in does not\nkeep a server-side copy or index of your mailbox.`]}),`\n`,\_jsx(Heading,{level:`3`,id:`when-you-connect-through-a-third-party-platform`,children:`When you connect through a third-party platform`}),`\n`,\_jsxs(\_components.p,{children:[`The prompt goes only to the inference endpoint you configured, such as\nAmazon Bedrock, Vertex AI, Azure AI Foundry, or an LLM gateway. On Amazon\nBedrock, Vertex AI, or a gateway that routes to them, no mailbox content\nreaches Anthropic. On Azure AI Foundry, Anthropic operates the Claude models\nand processes prompts as an independent processor for Microsoft, as\ndescribed in\n`,\_jsx(\_components.a,{href:`https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry`,children:`Claude in Microsoft Foundry`}),`.\nSee\n`,\_jsx(\_components.a,{href:`/office-agents/third-party-platforms`,children:`Use Claude for M365 with third-party platforms`}),`\nfor configuration details. The add-in does not keep a server-side copy or\nindex of your mailbox.`]}),`\n`,\_jsx(Heading,{level:`2`,id:`chat-history`,children:`Chat history`}),`\n`,\_jsxs(\_components.p,{children:[`Chat history is stored locally in your browser using IndexedDB. It is\nnot synced across devices or browsers. You can clear all chat history\nfrom Settings at any time. The local store is also cleared when you\nclear your browser data. Chat history is specific to the combination of\nthe add-in surface, your user ID, and your organization ID, so your\nExcel and Outlook histories are separate. Reinstalling the add-in or\nswitching between Claude add-ins does not remove it. See\n`,\_jsx(\_components.a,{href:`/office-agents/data-storage`,children:`Data storage and retention`}),` for where it\nsits on disk and how long it is kept.`]}),`\n`,\_jsx(\_components.p,{children:`When you sign in with a Claude account, the add-in sends your\nconversations to Anthropic, including the content Claude reads from your\nmailbox and calendar, and any files you attach. Clearing chat history\nremoves only the copy in your browser. It does not delete the messages\nor attached files that Anthropic keeps.`}),`\n`,\_jsx(Heading,{level:`2`,id:`data-retention-and-audit`,children:`Data retention and audit`}),`\n`,\_jsxs(\_components.p,{children:[`For Claude for Outlook use, inputs and outputs are deleted on Anthropic’s\nbackend within 30 days of receipt or generation, except as described in\n`,\_jsx(\_components.a,{href:`https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data`,children:`How long do you store my organization’s data?`})]}),`\n`,\_jsxs(\_components.p,{children:[`Enterprise organizations can route full audit telemetry from Claude for\nOutlook to their own OpenTelemetry collector for integration with a SIEM\nor observability platform. See\n`,\_jsx(\_components.a,{href:`/office-agents/enterprise-readiness`,children:`Configure a custom OpenTelemetry collector`}),`\nfor setup. On Pro, Max, and Team plans, observability and audit\nexport are not available. Claude for Outlook does not inherit custom\ndata retention settings your organization may have configured and is not\nincluded in Enterprise audit logs. For Enterprise organizations with the\n`,\_jsx(\_components.a,{href:`https://platform.claude.com/docs/en/manage-claude/compliance-api`,children:`Compliance API`}),`\nenabled, Claude for Outlook sessions are included in the Compliance API.\nThis coverage requires no additional setup: the same Compliance Access\nKeys apply.`]}),`\n`,\_jsx(Heading,{level:`2`,id:`prompt-injection-risks`,children:`Prompt injection risks`}),`\n`,\_jsx(\_components.p,{children:`Be cautious with email from external or untrusted senders. Email bodies\nand attachments are untrusted input and may contain instructions intended\nto manipulate Claude rather than you.`}),`\n`,\_jsx(\_components.p,{children:`Prompt injection refers to malicious instructions hidden in an email\nbody, signature, or attachment that try to trick the AI into taking\nunintended actions. For example, a routine inbound email might contain\nhidden text instructing Claude to forward a thread or draft a reply you\ndid not ask for. Claude may interpret these instructions as legitimate\nrequests.`}),`\n`,\_jsx(\_components.p,{children:`Review every draft and inbox action before accepting it, especially when\nworking with email from external or untrusted senders.`}),`\n`,\_jsx(Heading,{level:`2`,id:`recommended-use-during-beta`,children:`Recommended use during beta`}),`\n`,\_jsx(\_components.p,{children:`As a beta feature, Claude for Outlook is not recommended for:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`Unattended sending. Claude never sends mail or invites on its own; every\ndraft lands unsent for your review.`}),`\n`,\_jsx(\_components.li,{children:`Client-facing or counterparty correspondence without reading the draft\nfirst.`}),`\n`,\_jsx(\_components.li,{children:`Replacing your judgment on which emails matter or how to handle a\nrelationship.`}),`\n`,\_jsx(\_components.li,{children:`Mailboxes containing privileged or regulated data without appropriate\norganizational controls.`}),`\n`]}),`\n`,\_jsx(\_components.p,{children:`To use Claude for Outlook safely and effectively:`}),`\n`,\_jsxs(\_components.ul,{children:[`\n`,\_jsx(\_components.li,{children:`Review drafted replies and invites before sending, especially recipient\nlists.`}),`\n`,\_jsx(\_components.li,{children:`Verify thread summaries against the cited source emails for high-stakes\nconversations.`}),`\n`,\_jsx(\_components.li,{children:`Apply appropriate Microsoft 365 permissions and Conditional Access\npolicies for the add-in.`}),`\n`,\_jsx(\_components.li,{children:`Maintain human oversight for anything leaving your organization.`}),`\n`]})]})}function MDXContent(props={}){const{wrapper:MDXLayout}={...\_provideComponents(),...props.components};return MDXLayout?\_jsx(MDXLayout,{...props,children:\_jsx(\_createMdxContent,{...props})}):\_createMdxContent(props)}return{default:MDXContent};function \_missingMdxReference(id,component){throw new Error(`Expected `+(component?`component`:`object`)+\" `\"+id+\"` to be defined: you likely forgot to import, pass, or provide it.\")}","frontmatter":{},"scope":{"config":{},"pageMetadata":{"title":"Use Claude for Outlook","description":"An Outlook add-in that integrates Claude into your inbox and calendar, for Pro, Max, Team, and Enterprise plans.","href":"/office-agents/outlook"}}},"mdxSourceWithNoJs":null},"mdxExtracts":{"tableOfContents":[{"title":"What you can do","slug":"what-you-can-do","depth":2,"children":[]},{"title":"Get started with Claude for Outlook","slug":"get-started-with-claude-for-outlook","depth":2,"children":[{"title":"Supported versions","slug":"supported-versions","depth":3,"children":[]},{"title":"Install for yourself","slug":"install-for-yourself","depth":3,"children":[]},{"title":"Deploy to your organization","slug":"deploy-to-your-organization","depth":3,"children":[]},{"title":"Install from a manifest file","slug":"install-from-a-manifest-file","depth":3,"children":[]},{"title":"Grant Microsoft Graph consent","slug":"grant-microsoft-graph-consent","depth":3,"children":[]},{"title":"Use your own Entra app instead","slug":"use-your-own-entra-app-instead","depth":4,"children":[]},{"title":"Deploy in a US Government or national cloud","slug":"deploy-in-a-us-government-or-national-cloud","depth":3,"children":[]},{"title":"Connect through a third-party platform","slug":"connect-through-a-third-party-platform","depth":3,"children":[]}]},{"title":"Triage your inbox","slug":"triage-your-inbox","depth":2,"children":[]},{"title":"Draft replies in your voice","slug":"draft-replies-in-your-voice","depth":2,"children":[]},{"title":"Summarize long threads","slug":"summarize-long-threads","depth":2,"children":[]},{"title":"Read attachments inline","slug":"read-attachments-inline","depth":2,"children":[]},{"title":"Search your mailbox","slug":"search-your-mailbox","depth":2,"children":[]},{"title":"Find time and create events","slug":"find-time-and-create-events","depth":2,"children":[]},{"title":"Prep for meetings","slug":"prep-for-meetings","depth":2,"children":[]},{"title":"Work across M365 apps","slug":"work-across-m365-apps","depth":2,"children":[]},{"title":"Model availability","slug":"model-availability","depth":2,"children":[]},{"title":"How Claude accesses your mailbox","slug":"how-claude-accesses-your-mailbox","depth":2,"children":[{"title":"When you sign in with a Claude account","slug":"when-you-sign-in-with-a-claude-account","depth":3,"children":[]},{"title":"When you connect through a third-party platform","slug":"when-you-connect-through-a-third-party-platform","depth":3,"children":[]}]},{"title":"Chat history","slug":"chat-history","depth":2,"children":[]},{"title":"Data retention and audit","slug":"data-retention-and-audit","depth":2,"children":[]},{"title":"Prompt injection risks","slug":"prompt-injection-risks","depth":2,"children":[]},{"title":"Recommended use during beta","slug":"recommended-use-during-beta","depth":2,"children":[]}],"codeExamples":{}},"jsLinks":["/docs/\_mintlify/custom/claude-ai/b857db804a3a9481/desktop-app-nav.js"],"subdomain":"claude-ai","siteName":"Claude.ai Documentation","title":"Use Claude for Outlook - Claude.ai Documentation","navMaps":{"firstHrefInVersion":{},"firstHrefInLanguage":{}},"lastModified":"2026-11-05T22:55:39.033Z","originalFileLocation":"office-agents/outlook.mdx"},"headHtml":"\u003cscript data-mint-head>(function(){var d=document.documentElement,p=null;if(!p){try{p=localStorage.getItem(\"isDarkMode\")}catch(e){}if(p==='true')p='dark';else if(p==='false')p='light';if(p!=='light'\u0026\u0026p!=='dark'\u0026\u0026p!=='system')p=\"system\"}var r=p==='system'?(matchMedia(\"(prefers-color-scheme: dark)\").matches?'dark':'light'):p;d.classList.remove(r==='dark'?'light':'dark');d.classList.add(r);d.setAttribute(\"data-theme-preference\",p)})();\u003c/script>\u003cmeta data-mint-head name=\"description\" content=\"An Outlook add-in that integrates Claude into your inbox and calendar, for Pro, Max, Team, and Enterprise plans.\">\u003cmeta data-mint-head name=\"application-name\" content=\"Claude.ai Documentation\">\u003cmeta data-mint-head name=\"generator\" content=\"Mintlify\">\u003clink data-mint-head rel=\"icon\" type=\"image/png\" sizes=\"192x192\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon/android-chrome-192x192.png\" media=\"(prefers-color-scheme: light)\">\u003clink data-mint-head rel=\"apple-touch-icon\" type=\"image/png\" sizes=\"180x180\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon/apple-touch-icon.png\">\u003clink data-mint-head rel=\"icon\" type=\"image/png\" sizes=\"16x16\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon/favicon-16x16.png\" media=\"(prefers-color-scheme: light)\">\u003clink data-mint-head rel=\"icon\" type=\"image/png\" sizes=\"32x32\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon/favicon-32x32.png\" media=\"(prefers-color-scheme: light)\">\u003clink data-mint-head rel=\"shortcut icon\" type=\"image/x-icon\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon/favicon.ico\" media=\"(prefers-color-scheme: light)\">\u003clink data-mint-head rel=\"icon\" type=\"image/png\" sizes=\"192x192\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon-dark/android-chrome-192x192.png\" media=\"(prefers-color-scheme: dark)\">\u003clink data-mint-head rel=\"icon\" type=\"image/png\" sizes=\"16x16\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon-dark/favicon-16x16.png\" media=\"(prefers-color-scheme: dark)\">\u003clink data-mint-head rel=\"icon\" type=\"image/png\" sizes=\"32x32\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon-dark/favicon-32x32.png\" media=\"(prefers-color-scheme: dark)\">\u003clink data-mint-head rel=\"shortcut icon\" type=\"image/x-icon\" href=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon-dark/favicon.ico\" media=\"(prefers-color-scheme: dark)\">\u003cmeta data-mint-head property=\"og:title\" content=\"Use Claude for Outlook - Claude.ai Documentation\">\u003cmeta data-mint-head property=\"og:description\" content=\"An Outlook add-in that integrates Claude into your inbox and calendar, for Pro, Max, Team, and Enterprise plans.\">\u003cmeta data-mint-head property=\"og:site\_name\" content=\"Claude.ai Documentation\">\u003cmeta data-mint-head property=\"og:url\" content=\"https://claude.com/docs/office-agents/outlook\">\u003cmeta data-mint-head property=\"og:type\" content=\"website\">\u003cmeta data-mint-head property=\"og:image\" content=\"https://claude-ai.mintlify.site/docs/\_mintlify/api/og/v2?division=+\u0026amp;title=Use+Claude+for+Outlook\u0026amp;description=An+Outlook+add-in+that+integrates+Claude+into+your+inbox+and+calendar%2C+for+Pro%2C+Max%2C+Team%2C+and+Enterprise+plans.\u0026amp;theme=c937feb09b37748e448783d0\u0026amp;signature=6669aa06491c7b3b0057ddf34c19a9b17edefda3f506683aa572448d87604e51\">\u003cmeta data-mint-head property=\"og:image:width\" content=\"1200\">\u003cmeta data-mint-head property=\"og:image:height\" content=\"630\">\u003cmeta data-mint-head name=\"twitter:card\" content=\"summary\_large\_image\">\u003cmeta data-mint-head name=\"twitter:title\" content=\"Use Claude for Outlook - Claude.ai Documentation\">\u003cmeta data-mint-head name=\"twitter:description\" content=\"An Outlook add-in that integrates Claude into your inbox and calendar, for Pro, Max, Team, and Enterprise plans.\">\u003cmeta data-mint-head name=\"twitter:image\" content=\"https://claude-ai.mintlify.site/docs/\_mintlify/api/og/v2?division=+\u0026amp;title=Use+Claude+for+Outlook\u0026amp;description=An+Outlook+add-in+that+integrates+Claude+into+your+inbox+and+calendar%2C+for+Pro%2C+Max%2C+Team%2C+and+Enterprise+plans.\u0026amp;theme=c937feb09b37748e448783d0\u0026amp;signature=6669aa06491c7b3b0057ddf34c19a9b17edefda3f506683aa572448d87604e51\">\u003cmeta data-mint-head name=\"twitter:image:width\" content=\"1200\">\u003cmeta data-mint-head name=\"twitter:image:height\" content=\"630\">\u003cmeta data-mint-head name=\"msapplication-config\" content=\"/docs/mintlify-assets/\_mintlify/favicons/claude-ai/zHw4o4W7dZma2XXV/\_generated/favicon/browserconfig.xml\">\u003cmeta data-mint-head name=\"apple-mobile-web-app-title\" content=\"Claude.ai Documentation\">\u003cmeta data-mint-head name=\"msapplication-TileColor\" content=\"#0E0E0E\">\u003clink data-mint-head rel=\"canonical\" href=\"https://claude.com/docs/office-agents/outlook\">\u003clink data-mint-head rel=\"alternate\" type=\"application/xml\" href=\"/docs/sitemap.xml\">\u003clink data-mint-head rel=\"alternate\" type=\"text/markdown\" href=\"/docs/office-agents/outlook.md\">\u003cscript data-mint-head type=\"application/ld+json\">{\"@context\":\"https://schema.org\",\"@graph\":[{\"@type\":\"Organization\",\"@id\":\"https://claude.com/#organization\",\"name\":\"Claude.ai Documentation\",\"url\":\"https://claude.com\",\"logo\":{\"@type\":\"ImageObject\",\"url\":\"https://mintcdn.com/claude-ai/1fyDNLAICe3KG6rB/logo/light.svg?fit=max\u0026auto=format\u0026n=1fyDNLAICe3KG6rB\u0026q=85\u0026s=e870c19cb781d8a7c7b7d19de53b0a10\"}},{\"@type\":\"WebSite\",\"@id\":\"https://claude.com/docs#website\",\"name\":\"Claude.ai Documentation\",\"url\":\"https://claude.com/docs\",\"publisher\":{\"@id\":\"https://claude.com/#organization\"}},{\"@type\":\"WebPage\",\"@id\":\"https://claude.com/docs/office-agents/outlook#webpage\",\"url\":\"https://claude.com/docs/office-agents/outlook\",\"name\":\"Use Claude for Outlook\",\"description\":\"An Outlook add-in that integrates Claude into your inbox and calendar, for Pro, Max, Team, and Enterprise plans.\",\"dateModified\":\"2026-11-05T22:55:39.033Z\",\"isPartOf\":{\"@id\":\"https://claude.com/docs#website\"},\"breadcrumb\":{\"@id\":\"https://claude.com/docs/office-agents/outlook#breadcrumb\"}},{\"@type\":\"BreadcrumbList\",\"@id\":\"https://claude.com/docs/office-agents/outlook#breadcrumb\",\"itemListElement\":[{\"@type\":\"ListItem\",\"position\":1,\"name\":\" \",\"item\":\"https://claude.com/docs/office-agents/overview\"},{\"@type\":\"ListItem\",\"position\":2,\"name\":\"Use Claude for Outlook\",\"item\":\"https://claude.com/docs/office-agents/outlook\"}]},{\"@type\":[\"Article\",\"TechArticle\"],\"@id\":\"https://claude.com/docs/office-agents/outlook#article\",\"headline\":\"Use Claude for Outlook\",\"name\":\"Use Claude for Outlook\",\"description\":\"An Outlook add-in that integrates Claude into your inbox and calendar, for Pro, Max, Team, and Enterprise plans.\",\"url\":\"https://claude.com/docs/office-agents/outlook\",\"mainEntityOfPage\":{\"@id\":\"https://claude.com/docs/office-agents/outlook#webpage\"},\"dateModified\":\"2026-11-05T22:55:39.033Z\",\"publisher\":{\"@id\":\"https://claude.com/#organization\"},\"isPartOf\":{\"@id\":\"https://claude.com/docs#website\"}}]}\u003c/script>","siteName":"Claude.ai Documentation","nav":{"global":null,"tabs":[{"tab":"Welcome","pages":[{"title":"Welcome","href":""}]},{"tab":"Customize Claude","pages":[{"title":"Customize Claude","href":"/extend/overview"}]},{"tab":"Build for Claude","pages":[{"title":"Build for Claude","href":"/build/overview"}]},{"tab":"Cowork","pages":[{"title":"Cowork","href":"/cowork/overview"}]},{"tab":"Claude Tag","pages":[{"title":"Claude Tag","href":"/claude-tag/overview"}]},{"tab":"Claude for M365","groups":[{"group":" ","pages":[{"sidebarTitle":"Overview","title":"Claude for M365 overview","href":"/office-agents/overview"},{"title":"Use Claude for Excel","href":"/office-agents/excel"},{"title":"Use Claude for PowerPoint","href":"/office-agents/powerpoint"},{"title":"Use Claude for Word","description":"A Word add-in that integrates Claude into your document workflow, for Pro, Max, Team, and Enterprise plans.","href":"/office-agents/word"},{"title":"Use Claude for Outlook","href":"/office-agents/outlook"}]},{"group":"Features","pages":[{"title":"Work across M365 apps","description":"Let Claude read from one Microsoft 365 app and make changes in another in a single conversation.","href":"/office-agents/work-across-apps"},{"title":"Use dictation in Claude for M365","href":"/office-agents/dictation"},{"title":"Connectors and Skills","href":"/office-agents/connectors-and-skills"}]},{"group":"Administration","pages":[{"title":"Security, admin auditability, and analytics","href":"/office-agents/enterprise-readiness"},{"title":"Configure a custom OpenTelemetry collector","href":"/office-agents/opentelemetry"},{"title":"Performance and limits","href":"/office-agents/performance"},{"title":"Data storage and retention","href":"/office-agents/data-storage"},{"title":"Use Claude for M365 with third-party platforms","href":"/office-agents/third-party-platforms"},{"title":"Install financial services plugins for Cowork","href":"/office-agents/fsi-plugins"}]}]},{"tab":"Claude Science","pages":[{"title":"Claude Science","href":"/claude-science/overview"}]},{"tab":"Claude on third-party platforms","pages":[{"title":"Claude on third-party platforms","href":"/third-party/claude-desktop/overview"}]},{"tab":"Claude self-hosted","hidden":true,"pages":[{"title":"Claude self-hosted","href":"/third-party/claude-desktop/self-hosted/overview"}]},{"tab":"Claude for Government","pages":[{"title":"Claude for Government","href":"/government/overview"}]}]},"basePath":"","title":"Use Claude for Outlook - Claude.ai Documentation","buildId":"dpl\_BSPUBxEoKhhK7HzXVDPxdPvWx4xc","deploymentId":"dpl\_BSPUBxEoKhhK7HzXVDPxdPvWx4xc","dynamics":["07c022d89b","a74be98ba7"],"chunks":["Frame-DRxXE\_WT.js","DynamicMarkdown-AlxJK8VR.js","zoom-image-lightbox-B\_-GSaTf.js","lightbox-handle-r17bVUz3.js"]}
