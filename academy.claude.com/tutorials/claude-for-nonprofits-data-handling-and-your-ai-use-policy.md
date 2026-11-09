<!-- source: https://academy.claude.com/tutorials/claude-for-nonprofits-data-handling-and-your-ai-use-policy -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# Claude for Nonprofits: Data handling and your AI use policy

Get to a clear yes on AI use: answer "how does Claude handle our data?", write a one-page AI use policy leadership will sign, and invite your whole staff to the account you govern.

25 minClaude

[Open Claude](https://claude.ai/new)

## What you'll have at the end[](#what-youll-have-at-the-end)

Your organization has Claude seats. You may be just starting out or mid-rollout. Some may be sitting unused, and some staff may already be using personal AI accounts you can't see. Training and use cases are part of the answer, but the first step is to put in writing how to use AI safely at work and what the guardrails are. This tutorial is that foundation, in three phases.

By the end, you'll have:

1. **Answered "how is my data used by Claude?" in writing**, with links to the public pages your executive director (ED), board or legal counsel can check for themselves.
2. **Written a one-page AI use policy** that leadership has signed and that gives staff clear guardrails around AI use.
3. **Invited every staff member to your organization's Claude account** and told them what the policy allows and what it doesn't. AI use moves off personal accounts and onto the account you govern.

This isn't product training or a settings walk-through: for those see [Claude Academy(opens in new tab)](https://academy.claude.com/collections/nonprofits) and the [Claude Enterprise Administrator Guide(opens in new tab)](https://academy.claude.com/tutorials/claude-enterprise-administrator-guide), and if you haven't set up your account yet, start with [Getting started with Claude for nonprofits(opens in new tab)](https://academy.claude.com/tutorials/getting-started-with-claude-for-nonprofits).

This tutorial covers both Enterprise and Team plans. It's written for Team. Where Enterprise differs, an **On Enterprise** callout says so.

## Before you start[](#before-you-start)

**Who this is for.** You, the admin in charge of your organization's Claude settings, holding the Owner or Primary Owner role (roles below). If Organization settings > Members says you're an Admin, pair up with an Owner. Throughout, "you" means you, the admin, and "staff" means everyone at your organization who uses Claude.

| Role | What they can do |
| --- | --- |
| Primary Owner | One per organization, usually whoever set up the account. Can do everything an Owner can do, plus an organization-wide data export. |
| Owner | Changes the organization settings in Phase 3. |
| Admin | Invites and removes people. Can't change Phase 3 settings. |
| User | Uses Claude. Sees only their own chats and what colleagues share. |

**Who you need.** **On Team:** mostly you. You'll still send three questions to staff in Phase 2, and whoever leads the organization signs the half-page policy at the end.

On Enterprise

Your signer (usually the Executive Director, sometimes the CIO) and whoever covers legal, if you have someone. They'll read Phase 1 and sign Phase 2. Name them now and bring them in early, so they buy into the approach.

**Setup time.** Team: about 30 minutes of your time, and a few days for staff to answer three questions.

On Enterprise

Enterprise: 60-90 minutes of your time across one week, and the time it takes to get leadership sign-off.

## Phase 1 - Understand how Claude handles your data[](#phase-1---understand-how-claude-handles-your-data)

Nonprofits ask us the same six questions about their data. Each is answered below in plain English, with a link to the public page behind it. This summarizes Anthropic's public documentation and isn't legal advice. If anything here differs from your organization's agreement with Anthropic (for most Team plans, the Commercial Terms you accepted at signup), the agreement governs.

Note your organization's answers as you go, as you will use them in Phase 2.

### Team vs Enterprise[](#team-vs-enterprise)

Default data handling is the same on both plans: no training on your data by default, same default privacy, same security certifications (SOC 2, ISO 27001, ISO 42001). Both plans have single sign-on (SSO), domain verification and just-in-time (JIT) provisioning (accounts created the first time someone signs in).

On Enterprise

Enterprise adds the controls you need once Claude is running across the whole organization. That means identity controls (SCIM to sync staff accounts automatically from your identity provider, such as Okta, Microsoft Entra ID or Google Workspace, and custom roles that decide which groups get which connectors and capabilities) and compliance controls (audit logs, the Compliance API, custom retention, and the ability to process health information under HIPAA).

### 1. What data goes into Claude?[](#1-what-data-goes-into-claude)

The data you already have. Claude works with what staff give it: what they type or paste, [files they upload(opens in new tab)](https://support.claude.com/en/articles/8241126-upload-files-to-claude) (spreadsheets, PDFs, documents), and, if you turn [connectors(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) on, what it can read from tools like Google Drive or Microsoft 365. It can't reach anything you haven't connected, and with connectors on, it pulls in only what's relevant to what someone asks.

In practice that looks like a development director uploading last year's gift spreadsheet and asking which lapsed donors to call first, or a program lead pasting in survey responses to find the themes. Start there: the spreadsheets, documents and notes staff already handle every day.

Most of this information is already covered by rules you have today.

What's new is the conversation history: what staff asked and what Claude answered. The next five questions cover it: whether it's used to train models, who can see it, how long it's kept and where, and what changes when you connect other tools.

What to put in your policy

Your confidentiality and data-handling rules for donor records, client files, financials and HR documents still apply when staff use Claude, and your AI policy should reflect that.

### 2. Is our data used to train Claude?[](#2-is-our-data-used-to-train-claude)

**No.** By default, Anthropic does not use conversations (including inputs and outputs), files or connected data from Team or Enterprise accounts to train its models. This is the same on both Team and Enterprise plans. Learn more at our [Privacy Center(opens in new tab)](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training) and in the [Commercial Terms of Service(opens in new tab)](https://www.anthropic.com/legal/commercial-terms).

The exception you control: when a staff member clicks thumbs-up or thumbs-down on a response, that conversation is submitted to Anthropic as feedback and may be used to improve Claude (see [Manage user feedback settings(opens in new tab)](https://support.claude.com/en/articles/10504844)). Owners can turn it on or off, so check how yours is set.

What to put in your policy

Decide which, and say so in your policy. Phase 3 comes back to this.

### 3. Who can see our conversations?[](#3-who-can-see-our-conversations)

* **Colleagues.** Other staff see a conversation only if the person who had it shares it with them. [Sharing a project(opens in new tab)](https://support.claude.com/en/articles/9519189) (a workspace with its own instructions, files and chats) shares its instructions and files, not the chats in it. Each person's chats stay private by default. Owners decide whether projects can be shared or made public (visible to everyone in your organization, not outside it) at all.
* **Owners and Admins** can't browse conversations in the app either. A few routes do reach content, and you decide who holds them. Both plans: the Primary Owner can run the organization-wide [data export(opens in new tab)](https://support.claude.com/en/articles/13346720) of all conversations.

On Enterprise

Enterprise adds two routes: the Primary Owner can turn on the [Compliance API(opens in new tab)](https://support.claude.com/en/articles/13015708), which exposes chat and file content to your compliance tools, and a [custom role(opens in new tab)](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans) with the Privacy permission set to Can manage can run exports. Enterprise Owners also get audit logs - who did what, no content.

* Memory, if you turn it on, is private to each person, though it's included in organization data exports. See [memory controls for Team and Enterprise plans(opens in new tab)](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context).
* **At Anthropic.** Anthropic may process data for [internal processes such as safety-related review, product support or incident response(opens in new tab)](https://privacy.claude.com/en/articles/7996890-where-are-your-servers-located-do-you-host-your-models-on-eu-servers). Review the [Data Processing Addendum(opens in new tab)](https://www.anthropic.com/legal/data-processing-addendum) for details.
* **Outside your organization.** People outside your organization can see only artifacts (something Claude built in a chat, like an interactive page or tool), and only if your settings allow it. Owners control outside sharing, by [email invitation(opens in new tab)](https://support.claude.com/en/articles/9547008-share-artifacts#:~:text=all%20three%20levels.-,Invite%20people%20by%20email,-Available%20in%20beta) and by link. Email invitations are on by default on Team and off on Enterprise; you'll set both in Phase 3. See [Share artifacts(opens in new tab)](https://support.claude.com/en/articles/9547008-share-artifacts).

What to put in your policy

Pick people you'd trust with your case files, and name who holds these roles in your policy. See [roles and permissions(opens in new tab)](https://support.claude.com/en/articles/9267276-roles-and-permissions).

### 4. How long is data kept, and can we delete it?[](#4-how-long-is-data-kept-and-can-we-delete-it)

* Conversations stay in your account until the staff member deletes them (or, on Enterprise, your retention period removes them). Once deleted, they leave that person's history immediately and Anthropic's back-end systems within 30 days, except where the law requires longer retention or as described below.
* Content that automated systems flag under Anthropic's [Usage Policy(opens in new tab)](https://www.anthropic.com/legal/aup) (Anthropic's own rules for what Claude may be used for, separate from your policy) can be kept for up to two years, and the classification itself (a score, not your content) for up to seven years. This applies to flagged content, not everyday conversations.
* On **Team**, there's no auto-delete: conversations stay until staff delete them.

On Enterprise

**Enterprise** Owners can set a [custom retention period(opens in new tab)](https://support.claude.com/en/articles/10440198-configure-custom-data-retention-controls-for-enterprise-plans) for the whole organization (minimum 30 days) so conversations auto-delete. Chats inside projects follow a separate project retention period, so set that too.

Learn more about [how long Anthropic stores your organization's data(opens in new tab)](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data).

### 5. Where does our data live, and who else handles it?[](#5-where-does-our-data-live-and-who-else-handles-it)

* Data is stored in the United States. By default, processing may route through data centers in the US, Europe, Asia and Australia (Enterprise plans on usage-based billing can restrict inference to the US). See [where Anthropic's servers are located(opens in new tab)](https://privacy.claude.com/en/articles/7996890-where-are-your-servers-located-do-you-host-your-models-on-eu-servers).
* Anthropic uses a published list of [sub-processors(opens in new tab)](https://trust.anthropic.com/subprocessors): cloud hosting, support, billing and similar vendors. Anthropic posts changes to the Trust Center and gives advance notice of new sub-processors under its [Data Processing Addendum(opens in new tab)](https://www.anthropic.com/legal/data-processing-addendum); you can subscribe to the Trust Center news feed.
* Anthropic holds SOC 2 Type II, ISO 27001:2022 and ISO/IEC 42001:2023 (AI management) certifications. Reports and certificates are available from the Trust Center, some on request. See [what certifications Anthropic has obtained(opens in new tab)](https://privacy.claude.com/en/articles/10015870-what-certifications-has-anthropic-obtained).

Review security details at the [Anthropic Trust Center(opens in new tab)](https://trust.anthropic.com/).

### 6. What happens when we connect Claude to our other systems, or use skills?[](#6-what-happens-when-we-connect-claude-to-our-other-systems-or-use-skills)

[**Connectors**(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) (Google Drive, Gmail, Microsoft 365, Slack, your CRM via a custom connector, and others) let Claude read from a system when it's relevant to what a staff member asks, and take actions in it if you allow them.

* In your connected systems, Claude only sees what the user has access to. Take Google Drive: if a staff member can't open a file in Drive, Claude can't open it for them either. Each person signs in to the connected tool with their own account. Two exceptions you'd set up on purpose: a [custom connector(opens in new tab)](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp) (one your IT team or a vendor builds) that uses one shared login reaches whatever that login can access, and with [enterprise-managed authorization(opens in new tab)](https://support.claude.com/en/articles/15537633-authorize-mcp-connectors-for-your-entire-organization) IT authorizes a connector once for everyone. Making a connector available doesn't hand Claude anyone's login.
* Claude retrieves what's relevant at the time of the request. Whatever it retrieves becomes part of that conversation and follows the same rules as questions 2-5: not used for training by default, visible to other staff only if the conversation is shared and to admins as described in question 3, same retention. The connected service itself still handles your data under its own terms. See [how the Google Workspace connectors handle your data(opens in new tab)](https://support.claude.com/en/articles/10166901).
* **Owners decide which connectors are available at all, what each may do (always allow, needs approval or blocked, per action) and, on Enterprise, which groups get which.** [Desktop extensions(opens in new tab)](https://support.claude.com/en/articles/12592343) in the Claude Desktop app are open by default until you turn on the allowlist. You'll set all of this in Phase 3.

[**Skills**(opens in new tab)](https://support.claude.com/en/articles/12512176-what-are-skills) are packaged instructions and reference files that teach Claude how your organization does a specific task, such as "draft a grant report in our format." **Anything you put in a skill is treated like anything else you give Claude:** not used for training by default, visible only where it's shared and to admins as described in question 3. Owners decide who can create, share and publish skills; see [provision and manage skills for your organization(opens in new tab)](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization).

What to put in your policy:

name the systems staff may connect, and the ones they can't connect until you've reviewed them. "Drive and email yes, the donor database not yet" is a fine first answer.

### What this means for donor, client and health data[](#what-this-means-for-donor-client-and-health-data)

* **Donor and client information**: most of it can go into your organization's Claude account within your policy.
  + Donor data such as names and giving history: yes, within your policy.
  + Client-identifying information such as names and case notes: also within your policy, and the Phase 2 template makes it an ask-first item.
  + Health and disability details: leave them out unless your organization has the HIPAA-ready version of Claude (Enterprise plans only); if protected health information (PHI) is central to the work you want help with, read "Covered by HIPAA?" below first.
  + Immigration status: handle it like health details.
* In every case, by default none of this is used for training, it's visible only to the staff it's shared with and to admins as described in question 3, and your organization is responsible for complying with the laws that apply to its data (see the [Commercial Terms(opens in new tab)](https://www.anthropic.com/legal/commercial-terms) and the [Data Processing Addendum(opens in new tab)](https://www.anthropic.com/legal/data-processing-addendum)).
* **Covered by HIPAA?** If you're a clinic or a health plan, or you handle health records for one, protected health information (PHI) needs a Business Associate Agreement (BAA) with Anthropic. That's available with the [HIPAA-ready configuration on Enterprise plans(opens in new tab)](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans), and not on Team. **On Team**, keep PHI out of Claude entirely and use it for everything else: grant writing, board reports, policies, de-identified program summaries. If PHI is central to the work you want help with, [contact our sales team(opens in new tab)](https://claude.com/solutions/nonprofits#pricing) about Enterprise.

On Enterprise

**On Enterprise**, you aren't covered automatically. Your Primary Owner turns on HIPAA under Organization settings > Data and privacy > HIPAA Compliance and accepts the BAA in that same flow - there's no separate document to sign. It can't be reversed from organization settings, so read the BAA and the Implementation Guide in the flow before accepting. Once it's on, the BAA covers chat, projects, artifacts and file creation (with limits), but not every feature: connectors and skills can be turned on but aren't covered, and memory is unavailable. Read the Implementation Guide for HIPAA Entities on the Trust Center (summarized in [Business Associate Agreements for commercial customers(opens in new tab)](https://privacy.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers)) before you follow the connector and settings steps in Phase 3.

* **Not sure whether HIPAA applies to you?** That depends on the services you provide and who you provide them for. Anthropic can't make that determination for you. Check with your legal counsel or compliance lead before client health details go in.
* **When in doubt, ask one question:** would I be comfortable if a colleague saw this in a shared project? If not, leave it out or strip the identifying details first. Staff can apply that test without legal training.

What to put in your policy

Your policy should ask staff to leave out names and identifiers where they can, and require that a person reviews anything before it goes out.

## Phase 2 - Write your AI use policy[](#phase-2---write-your-ai-use-policy)

If you don't have a written AI policy yet, that's normal. Write something short first and treat it as a living document. You're not starting from scratch: as Phase 1 said, your existing confidentiality rules still apply, and this policy mostly says how they carry over to Claude.

Don't try to cover every team and every scenario in one pass. Start where the need is clearest (one program team, one type of data, one connector) and add to it as staff bring you new use cases and as Claude changes. Holding out for one comprehensive policy is how organizations stall, and the next product update would reopen it anyway.

Step 1 asks staff before you draft anything, so the policy answers their real questions in their own words.

### Step 1. Run a three-question staff check-in (give people 3-4 days to answer)[](#step-1-run-a-three-question-staff-check-in-give-people-3-4-days-to-answer)

Before you write anything, find out what's already happening. Leadership and staff usually see AI use differently, and NTEN and The Bridgespan Group's [State of Nonprofit AI Adoption and Governance report (2026)(opens in new tab)](https://www.nten.org/publications/state-of-nonprofit-ai) describes the gap. A short check-in closes most of it and gives you raw material for the policy.

Send the questions below to all staff (Team) or through team leads (Enterprise), as an anonymous form:

We are in the process of putting together an AI use policy, and would like your input so that the policy reflects how you actually work and what you need to be successful. Please take a few minutes to answer these three questions - there are no wrong answers, and all responses are anonymous.

1. What are you already using AI for at work, if anything?

2. What would you want to use it for if you knew it was OK?

3. What type of data do you want to use with AI?

Anything else you'd like to share? (optional)

Copy prompt

### Step 2. Make six decisions[](#step-2-make-six-decisions)

Work through these with your signer. Each decision becomes a short section of the policy. Under each one is example text from a fictional organization, Riverbend Community Services, that you can adapt.

**1. Purpose - why we use AI.** Frame it around the time it gives staff back.

*Riverbend uses AI tools to give staff time back for the work only people can do. This policy exists so everyone knows what's encouraged, what's off-limits, and who to ask when something is unclear.*

Copy prompt

**2. What we encourage, what needs a conversation first, and what's off-limits.** The staff check-in answers go here (see Step 3). Lead with what you want staff to use Claude for, and keep the not-permitted list short. A long list of limits reads as a warning, and staff stop using the ask-first route.

***Encouraged.** Everyday work in your organization's Claude account, under two standing rules: a person reviews anything before it goes outside the organization, and staff leave out names and identifiers when the task doesn't need them. Examples include:*

* *Drafting and editing: grant proposals and reports, donor appeals and acknowledgements, newsletters, board memos, job postings*
* *Summarizing and analyzing: meeting notes, survey results, research and policy scans*
* *Donor and supporter information: names, contact details, giving history*
* *Program and client data in aggregate or with identifiers removed*
* *Internal operations: budgets and spreadsheets, process documentation, planning, translating materials*

***Ask first.** Some work is legitimate but higher-stakes, and usually only a few people or one team need it. Bring the use case to [policy owner] before you start; we'll agree on guardrails together and write the decision down so the next person doesn't have to ask again. Most asks end in "yes, and here's how."*

* *Client-identifying information: names, service history, assessments, case notes, anything about minors. For some programs, being identified as a client is itself sensitive, so [policy owner] decides once whether client names are ask-first or off-limits for us. Health and disability details stay out unless we have the HIPAA-ready version of Claude; treat immigration status the same way.*
* *Bulk donor exports, wealth screening or major-gift research on named individuals*
* *HR and personnel matters: hiring screens, performance write-ups, investigations*
* *Connecting Claude to a new system of record (CRM, case management, finance) through a connector*
* *Preparing filings or formal responses to a regulator, auditor or attorney*

***Not permitted.** A short list of hard lines that apply to everyone, with no exception process.*

* *Entering client health or disability records, unless we have the HIPAA-ready version of Claude*
* *Using Claude's output as the final decision on a client's eligibility, benefits or services*
* *Anything that impersonates a real person*
* *Using a personal Claude account, or any other AI tool, for work covered by this policy*

Copy prompt

**3. How Claude handles our data.** A few lines, lifted from Phase 1. Say whether feedback is on or off.

*Our Claude account is on Anthropic's [Team/Enterprise] plan. Under Anthropic's commercial terms, by default our conversations and files are not used to train AI models and aren't visible to colleagues unless we share them. Our Primary Owner can export all conversations[; on Enterprise: and our compliance tools can access them through the Compliance API]. Anthropic may process them for internal processes such as safety-related review, product support or incident response (see Anthropic's [Data Processing Addendum(opens in new tab)](https://www.anthropic.com/legal/data-processing-addendum)). They're covered by Anthropic's Commercial Terms of Service (or our organization's agreement with Anthropic) [link]. The feedback buttons are [on/off]; [if on: don't submit feedback on conversations that contain client or donor details].*

Copy prompt

**4. A person checks the output.** Every version of your policy needs this line. Checking well is a skill: the [AI Fluency for nonprofits course(opens in new tab)](https://academy.claude.com/courses/ai-fluency-for-nonprofits) teaches it as Discernment. Point staff there.

*A staff member reviews anything AI produces before it is sent externally, published, or used to make a decision about a person.*

*Staff who use AI complete the [AI Fluency for nonprofits course(opens in new tab)](https://academy.claude.com/courses/ai-fluency-for-nonprofits) in their first 30 days.*

Copy prompt

**5. Which tools.** Use the organization's account. Name the connectors and skills that are on and tell staff to use them: that's where most of the time savings are. Say whether memory is on.

*Use Riverbend's Claude account (you'll receive an invitation). Please don't use personal AI accounts for Riverbend work. Connected and encouraged: Google Drive, Gmail. Skills on: [your list] - start with [the one staff asked for most]. Not yet: Salesforce. Ask [policy owner] before connecting anything else. Memory: on. Switch it on under Settings > Memory so Claude keeps Riverbend's context between chats.*

Copy prompt

**6. Policy owner, Primary Owner, signer, review date.** Name the policy owner and the Primary Owner on the Claude account.

*Policy owner: [Name, title]. Claude account Primary Owner: [Name, title]. Approved by: [ED name], [date]. We'll revisit this in 90 days, or sooner if Anthropic changes how it handles data or we connect a new system that holds client information.*

Copy prompt

Open the [AI use policy template(opens in new tab)](https://claude.ai/artifact/4LwG7DfXLj9vnkhqLA7MzM?sk=Do1-n1X38SwETmNQ-YydGg). It opens in Claude, so you'll need a Claude account, and a free one works. No Claude account yet? Use the [Google Docs version(opens in new tab)](https://docs.google.com/document/d/1l9e-jTXj_fDTpljRsKT1sIpt7_v2FA6ptbwsVBg0wuY/edit) instead. To write your own policy, adapt the example text under the six decisions above and use the prompt in Step 3.

### Step 3. Let Claude draft decisions 2 and 5 from what staff said[](#step-3-let-claude-draft-decisions-2-and-5-from-what-staff-said)

Staff find a policy easier to recognize and follow when it uses their own words. You're an Owner and this is the account you govern, so it's fine to use it before the policy is signed. Open your organization's Claude account, paste in the staff check-in responses and run this prompt:

I'm writing a one-page AI use policy for a nonprofit. Below are anonymous staff answers to three questions: what they already use AI for, what they'd use it for if they knew it was OK, and what types of data they want to use with it.

Draft two sections for me:

(a) "What we encourage, what needs a conversation first, and what's off-limits." Group what staff already do and want to do into a short encouraged list. Sort the data types they named, plus these fixed rules [no client health or disability records; human review before anything external; no impersonation; no personal AI accounts for work], into a short ask-first list for higher-stakes work and a short not-permitted list. Use their language where you can.

(b) "Which tools and connected systems." Based on what they mention using, suggest which connectors we should approve first and which to hold.

Then write a three-sentence "you said, we decided" paragraph I can send to staff showing how their input shaped the policy. Plain language, warm, no jargon.

[paste staff responses here]

Open in Claude

**Review what comes back with your signer before it goes in the policy.**

### Step 4. Get it signed[](#step-4-get-it-signed)

Send your draft policy from Step 3, plus Phase 1 of this tutorial for the facts behind it, to your signer, and ask for a yes or comments by a specific date. If legal or your board wants the underlying documents, the claims in Phase 1 link to Anthropic's public pages.

For a starting point, use the [AI use policy template(opens in new tab)](https://claude.ai/artifact/4LwG7DfXLj9vnkhqLA7MzM?sk=Do1-n1X38SwETmNQ-YydGg) from Step 2. No Claude account yet? Use the [Google Docs version(opens in new tab)](https://docs.google.com/document/d/1l9e-jTXj_fDTpljRsKT1sIpt7_v2FA6ptbwsVBg0wuY/edit) instead. If you want a fuller policy document, NTEN's [AI for nonprofits resource hub(opens in new tab)](https://www.nten.org/learn/resource-hubs/artificial-intelligence) has two downloadable policy templates (NTEN's and ANB Advisory Group's) plus community examples. The [Integration lesson(opens in new tab)](https://academy.claude.com/courses/ai-fluency-for-nonprofits/integration) in AI Fluency for nonprofits walks you through drafting one step by step. Most organizations under 50 staff won't need more than one page. Larger ones usually start from one of the NTEN templates.

## Phase 3 - Roll it out and keep it current[](#phase-3---roll-it-out-and-keep-it-current)

You have a signed policy. Now set the handful of settings that enforce it, then tell staff.

### Step 1. Set the few settings that enforce the policy[](#step-1-set-the-few-settings-that-enforce-the-policy)

Most of these are under Organization settings.

| Setting | Where | What to do | On Enterprise |
| --- | --- | --- | --- |
| **Who's an Owner.** | Organization settings > Members | Keep Owners to one or two named people, and make one of them the policy owner from Phase 2. Organization settings > Members shows who holds each role, and the roles table under Before you start explains each one. See [roles and permissions(opens in new tab)](https://support.claude.com/en/articles/9267276-roles-and-permissions). | Enterprise can also add custom roles. |
| **Which connectors are on.** | Organization settings > Connectors Organization settings > Connectors > Desktop | Decide your day-one list and add only those. On both plans you can also restrict what each connector may do, organization-wide. On Team, a connector you add is available to all staff, so limiting who uses it is a policy rule. See [use connectors to extend Claude's capabilities(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities).  If staff use the Claude Desktop app, turn on the [desktop extension allowlist(opens in new tab)](https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist), then add the extensions you approve. Anything installed before that is removed and has to be reinstalled, so pick a quiet time. | On Enterprise it can be a setting: custom roles let you grant connectors (or individual actions within them) to specific groups. See [set up role-based permissions(opens in new tab)](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans). |
| **Whether projects can be shared and made public.** | Organization settings > Data and privacy | Project sharing and public projects are both allowed by default on both plans, so a staff member can make a project visible to everyone in the organization. That's fine for most organizations. Turn Public projects off if teams handle confidential casework. See [control project sharing for your organization(opens in new tab)](https://support.claude.com/en/articles/9927533-control-project-sharing-for-your-organization). |  |
| **Sharing outside the organization, and skill publishing.** | Organization settings > Artifacts Organization settings > Plugins & skills | In Organization settings > Artifacts, set outside sharing (email invitations and links) to match your human-review rule.  In Organization settings > Plugins & skills, check that Publishing is set to Requires review so an Owner approves a skill before everyone gets it. |  |
| **Memory.** | Organization settings > Capabilities | Turn [memory(opens in new tab)](https://support.claude.com/en/articles/11817273) on for the organization and ask staff to switch it on under Settings > Memory; it stays off for each person until they do. Deleting a chat doesn't delete what Claude remembered from it, though people can delete individual memories. Before you turn memory off for the organization later, check the [memory article(opens in new tab)](https://support.claude.com/en/articles/11817273) for what happens to saved memory. | Enterprise: settle retention before this step, since your retention setting affects memory. Memory isn't available with HIPAA or public-sector agreements; [check who can use memory(opens in new tab)](https://support.claude.com/en/articles/11817273). |
| **User feedback.** | the Rate chats setting under Organization settings > Data and privacy | On or off. Check how yours is set, pick one and note it in the policy (Phase 2, decision 3). See [manage user feedback settings(opens in new tab)](https://support.claude.com/en/articles/10504844-manage-user-feedback-settings-on-team-and-enterprise-plans). |  |

**The policy itself.** Let staff ask it. If your nonprofit is verified, the Claude for Nonprofits plugin is installed by default and includes an AI use policy lookup skill, so staff can ask Claude "can I use Claude for this?" and get an answer from your rules.

* Save the signed policy where staff can already reach it, such as a shared Drive folder or your intranet.
* The first time someone asks, Claude asks where the policy lives: they point it at the document through a connector or drop it into the chat, and if memory is on, Claude remembers it for next time.
* The plugin needs Skills and Cowork (the mode where you hand Claude a whole task and it works through it across your files and connected tools) turned on for your organization (see [Manage plugins for your organization(opens in new tab)](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization)).
* To save staff that first step, an Owner can add a line under Organization settings > Organization and access > Organization instructions, for example: "Our AI use policy is the document called AI use policy in the shared Policies folder".

**Both plans, if staff use Claude Code:** have developers [sign in to Claude Code with the organization's account(opens in new tab)](https://support.claude.com/en/articles/11845131), so the policy covers developers as well as chat. IT can restrict logins to your organization with [Claude Code managed settings(opens in new tab)](https://code.claude.com/docs/en/authentication#restrict-login-to-your-organization).

On Enterprise

On HIPAA-ready Enterprise plans, the BAA covers Claude Code only in specific setups, so keep PHI out of it until you've read [Use Claude Code and Claude Cowork (local mode) on a HIPAA-ready Enterprise plan(opens in new tab)](https://support.claude.com/en/articles/17318731-use-claude-code-local-mode-and-claude-cowork-local-mode-on-a-hipaa-ready-enterprise-plan).

**Enterprise only:** set the retention period from question 4 now if you haven't. Audit logs, the Compliance API, SCIM provisioning and custom roles can follow the invitations below. From here the [Claude Enterprise Administrator Guide(opens in new tab)](https://academy.claude.com/tutorials/claude-enterprise-administrator-guide) takes over, with links to the setup articles.

### Step 2. Tell staff[](#step-2-tell-staff)

**1. Invite everyone you have seats for**, not just the people who asked. The policy says "use our account, not personal ones," so everyone needs an invitation or that line is empty.

* Each invitation takes up a seat the moment you send it, so check your count under Organization settings > Organization and access (Total seats) first (see purchase and manage seats on [Team(opens in new tab)](https://support.claude.com/en/articles/12004354-purchase-and-manage-seats-on-team-plans) or [Enterprise(opens in new tab)](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans) plans, or on Enterprise ask your Anthropic contact).
* Fewer seats than staff? Invite in waves: start with the teams whose check-in answers showed the most use, tell everyone else when their turn comes, and keep the policy organization-wide from day one.
* For a structured pilot, the [launch section of the Enterprise Administrator Guide(opens in new tab)](https://academy.claude.com/tutorials/claude-enterprise-administrator-guide#phase-2-change-management-launch) covers champions and phased rollout.
* Send the invitations and the note today; the domain work below can follow when IT is ready.
* **Both plans:** two ways to add people, and they differ when seats run out.
  + By email (Organization settings > Members): each pending invitation uses one of your purchased seats.
  + By invite link (Organization settings > Organization and access; on by default on Team, off on Enterprise, not available with SSO) or organization discovery (staff on your domain are prompted to join when they sign up): once your purchased seats are used, each new joiner can add a paid seat automatically (see [Find and join a Team or Enterprise organization(opens in new tab)](https://support.claude.com/en/articles/13566435-find-and-join-a-team-or-enterprise-organization)).
  + To stay inside your count, invite by email. See [manage members on Team and Enterprise plans(opens in new tab)](https://support.claude.com/en/articles/13133750-manage-members-on-team-and-enterprise-plans).
  + Staff whose email is on another domain need that domain added to your allowed domains (the email domains permitted to join, in Organization settings) first.
* **Both plans, to stop new personal accounts on your domain:** [verify your email domain(opens in new tab)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso) (whoever manages your website domain adds one DNS record; it can take up to two days to show as verified) and turn on Restrict organization creation. After that, nobody can create a new personal Claude account with a work address; they join yours by invitation, invite link or organization discovery instead.

On Enterprise

**Enterprise, to fold in existing personal accounts:** once your domain is verified, SSO is enforced, JIT or SCIM provisioning is on and Restrict organization creation is on, you can [claim and migrate personal Claude accounts on your domain(opens in new tab)](https://support.claude.com/en/articles/14625619-claim-and-migrate-accounts-on-your-domain). It's one-way, and it isn't optional for staff: everyone on the domain gets 30 days to move over, and personal accounts left after that are deactivated. On HIPAA-ready plans people start fresh without their history.

**2. Communicate, more than once.** Send the note below today, then say it again at your next all-staff meeting, ask managers to raise it with their teams, and pin the policy where staff already look. To start, copy Riverbend's and swap the brackets (drop the ask-Claude line if the plugin isn't on for your organization):

Hi all - we now have an AI use policy, shaped by what you told us recently (thank you). Short version: [link to policy].

You'll get an invitation to [organization]'s Claude account today. Use it instead of personal AI tools for [organization] work.

[You said / we decided paragraph from Phase 2, Step 3.]

Questions about what's OK: ask [policy owner], or ask Claude "can I use Claude for this?" Something not working: [support route].

Want to learn how to use it well: the Claude for Nonprofits session for staff: A Staff Guide to Making Claude Useful on Day One.

Copy prompt

### Step 3. Keep it current[](#step-3-keep-it-current)

A week after the invitations go out, open Organization settings > Members: resend anything still pending, then open [Analytics(opens in new tab)](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans) from your user menu to see who has started. Then put a 90-day reminder in your calendar. Revisit sooner if:

* Anthropic changes how it handles data. Follow the [Help Center release notes(opens in new tab)](https://support.claude.com/en/articles/12138966-release-notes) and in-product notifications. For the source documents, click **Subscribe to updates** on the [Trust Center(opens in new tab)](https://trust.anthropic.com/), and keep an eye on the [Privacy Center(opens in new tab)](https://privacy.claude.com/en/) and the [Commercial Terms(opens in new tab)](https://www.anthropic.com/legal/commercial-terms).
* You want to connect a system that holds client or donor data
* Staff keep asking the policy owner the same question, and the policy doesn't answer it

## What's next[](#whats-next)

Enterprise admins: continue with the Claude Enterprise Administrator Guide for configuration in depth. Everyone: send staff the Claude for Nonprofits session for staff, [A Staff Guide to Making Claude Useful on Day One(opens in new tab)](https://claude.com/resources/webinars/claude-for-nonprofits-a-staff-guide-to-making-claude-useful-on-day-one), along with the note above. Questions after reading this: the session for admins, [An Admin's Guide to Data Handling and AI Use Policy(opens in new tab)](https://claude.com/resources/webinars/claude-for-nonprofits-admin-guide-to-data-handling-ai-policy), walks through this tutorial with live Q&A.

## Learn more[](#learn-more)

* [**Getting started with Claude for nonprofits**(opens in new tab)](https://academy.claude.com/tutorials/getting-started-with-claude-for-nonprofits): nonprofit pricing, verification and the nonprofit connectors, from Claude Academy.
* [**AI Fluency for nonprofits**(opens in new tab)](https://academy.claude.com/courses/ai-fluency-for-nonprofits): the full course from Anthropic and GivingTuesday. Its Integration lesson is the policy-drafting exercise referenced in Phase 2.
* [**Claude 101**(opens in new tab)](https://academy.claude.com/courses/claude-101): the self-paced introductory course on Claude Academy, for staff once they have their invitation.
* [**Is my data used for model training?**(opens in new tab)](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training) and [**How long do you store my organization's data?**(opens in new tab)](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data): the two Privacy Center articles to forward to whoever signs.
* [**Anthropic Trust Center**(opens in new tab)](https://trust.anthropic.com/) and the [**Data Processing Addendum**(opens in new tab)](https://www.anthropic.com/legal/data-processing-addendum): certifications, sub-processors, security documentation and the contractual data terms.

* [What you'll have at the end](#what-youll-have-at-the-end)
* [Before you start](#before-you-start)
* [Phase 1 - Understand how Claude handles your data](#phase-1---understand-how-claude-handles-your-data)
* [Phase 2 - Write your AI use policy](#phase-2---write-your-ai-use-policy)
* [Phase 3 - Roll it out and keep it current](#phase-3---roll-it-out-and-keep-it-current)
* [What's next](#whats-next)
* [Learn more](#learn-more)
