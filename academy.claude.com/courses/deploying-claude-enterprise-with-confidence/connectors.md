<!-- source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/connectors -->

Lesson 7 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutConnectors

3. /[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

# Connectors

Lesson 710 min

In this lessonBy the end, you’ll be able to

* Name the three gates that allow connector usage and understand how to configure what you have control over
* Explain how enterprise-managed authorization (EMA) lets you provision connector access centrally
* Explain read versus write access, and decide which connectors each group gets and at what depth

This is still the second of the five decisions, Access. You’ve decided which product surfaces and capabilities your groups can access; now you decide which tools and data sources Claude can reach.

## What a connector is[](#what-a-connector-is)

A connector gives Claude access to another application (your drive, your wiki, your ticket tracker) so members can bring their live work context into a conversation instead of pasting or uploading it in. That reach is the value and the risk at once, so connector access is controlled at three separate gates. It is also what can drive early adoption: a team that connects a tool early has live context to work with from day one, so enabling a first connector for a group is one of the higher-leverage moves in a rollout.

## The three gates[](#the-three-gates)

Between any connector and a member actually using it there are three gates, and all three must be open for Claude to be able to access the connector’s data.

| **Gate** | **What it controls** | **Set by** | **If it’s closed** |
| --- | --- | --- | --- |
| **Organization gate** | Whether the connector is available in your organization at all | An Owner or Primary Owner | Nobody sees the connector, regardless of role |
| **Role gate** | Whether a group’s role includes the connector | An Owner or Primary Owner | Some groups have the connector; this member’s group doesn’t |
| **Member gate** | Whether this member has connected their own account, authorizing Claude to act as them | The member | The connector is granted, but not usable until this member connects their account |

## What you control[](#what-you-control)

Within your two gates you hold three controls:

1. The connectors you add to your organization.
2. Per-group scoping: which groups get each one.
3. Where a connector offers it, the access depth: read-only or read-write. In the product, a connector’s write and delete tools are each set to Always allow, Needs approval, or Blocked, so blocking them holds it read-only.

When accessing a connector, Claude inherits the member’s own permissions from the connected service: if a member can’t access a specific file, channel, or record in the source system, that permission boundary carries through the connector too.

Claude Code’s network reach, the allowed domains your platform lead sets in its managed settings (Lesson 6), is the same question applied to the network, so raise it in the same conversation as the connector list.

## Enterprise-managed authorization[](#enterprise-managed-authorization)

By default, the third gate belongs to the member: they connect their own account, and you cannot do it for them. For most organizations that works, but it means you cannot guarantee a connector is actually live for the group you scoped it to.

Enterprise-managed authorization (EMA) closes that gap. Instead of each member connecting their own account, you provision access centrally through your organization’s identity provider: once a connector is enabled, everyone in scope gets it automatically on their first login, with permissions inherited from their existing IdP groups and roles. Offboarding runs through the IdP either way. EMA is available only for connectors whose provider has built support for it, so some connectors on your list will still go through the member gate. [Authorize MCP connectors for your entire organization(opens in new tab)](https://support.claude.com/en/articles/15537633-authorize-mcp-connectors-for-your-entire-organization) covers what EMA does, which connectors and identity providers support it, and how to set it up (MCP is the open standard connectors are built on).

## Read and write access[](#read-and-write-access)

Connector access comes in two levels, and they carry different amounts of risk. Read access, the lower-risk of the two, lets Claude see the system: fetch the doc, search the tracker, read the dashboard, etc. Write access lets Claude change it: file the ticket, edit the page, create a new entry, etc. Giving Claude write access means that Claude, acting as the member, can change or overwrite information (in Cowork, a member still confirms each write unless Allow “Always allow” for connector tools is on) in the connected application. That’s why write access should get a different level of sign-off: consider having the data-risk owner you named in Lesson 2 approve write grants, so the risk is managed by the person who owns it.

Connectors are the most visible change you will turn on: members notice the moment Claude can suddenly access data directly. Announce each connector as it is made available, and be clear about what does and doesn’t change for members: the connector is now available to them, but each member still chooses whether to turn it on. Route requests for new connectors through the access owner you named in Lesson 2.

## Pluto’s connectors[](#plutos-connectors)

Pluto added its drive and its wiki for every group, read-only, and added the ticket tracker read-write for Engineering, whose workflow files tickets all day, with the risk owner’s sign-off on the write grant. Payments-eng (kept out of Engineering in Lesson 5) stays read-only, and a connector whose data sits outside its remit is left off that group entirely — the tighter posture Payments & Trust takes throughout.

The interactive widget below runs Pluto’s three gates for a single connector: open or close any gate and watch who controls it and what each member experiences.

## 1 · Your decision[](#1-your-decision)

Which connectors does each group get, and at what depth: read-only or read-write, per tool?

## 2 · The choices you can make[](#2-the-choices-you-can-make)

Connector access is ultimately a judgment call about risk: for each connector, ask which group’s work needs write access every week.

| **The choice** | **When you’d choose it** | **What it means and the impact it has** |
| --- | --- | --- |
| **Read-only, scoped to the groups whose work lives in that system** | Most organizations land here unless the situation below applies. | Read access is immediately useful: fetch and search create real value on their own. This avoids the question of what Claude is allowed to change in your systems while your organization learns what members actually do with the reach. The common pattern is that write comes later, once a workflow has demonstrated the need and the risk owner has signed off. |
| **Write, phased in with sign-off** | A group’s workflow clearly needs Claude writing into the system (filing tickets, updating pages), and its risk owner is comfortable with it. | The group starts read-only like everyone else, then gets write once the need has shown itself and the risk owner has signed off. Claude can then change that system on members’ behalf, with the risk sitting with the owner who accepted it. |

## 3 · If you change this later[](#3-if-you-change-this-later)

Connector settings are freely reversible: the connectors you’ve added, each group’s scoping, and read-only versus read-write all move in your organization settings. Widening costs members nothing. Narrowing, however, ought to be handled with care: revoking write access or removing a connector breaks the workflows members built on it. It is best practice to announce any access changes so members are aware of them.

## Set up resources[](#set-up-resources)

When you’ve made the call, set up your organization’s connectors. The connectors you add and each group’s connector scoping live with your groups and their role assignments in Organization settings, and, where you use EMA, that is where the member gate becomes yours to stand up centrally as well.

* **[Use connectors to extend Claude’s capabilities(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)**: what a connector is and does from the member side: the thing you are gating.
* **[Get started with custom connectors using remote MCP(opens in new tab)](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)**: how a custom connector is built and added, so you know what you are approving.
* **[Authorize MCP connectors for your entire organization(opens in new tab)](https://support.claude.com/en/articles/15537633-authorize-mcp-connectors-for-your-entire-organization)**: enterprise-managed authorization — what it does, which connectors and identity providers support it, and how to set it up.
* **[Enterprise-managed authorization (MCP documentation)(opens in new tab)](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization)**: the standard behind EMA.
* **[Configure the sandboxed Bash tool(opens in new tab)](https://code.claude.com/docs/en/sandboxing)**: Claude Code’s network reach: the sandbox’s allowed domains in its managed settings, which your platform lead owns.

## Lesson activity[](#lesson-activity)

Fill the connector table in your companion: connector, who gets it, and depth (read-only or read-write).

**What to bring your risk owner:** every row with write access: the workflow that needs it, the group that carries it, and the read-versus-write risk framing from the section above.

→ Record this in the work-along companion, section Lesson 7.

## Downloads

*

  ### Work-along companion (Word)

  The editable Word version of the rollout plan you fill in lesson by lesson.

  [Download](https://academy.claude.com/assets/v1/work-along-companion-bk4suxux.docx)
*

  ### Work-along companion (PDF)

  The same rollout plan as a fillable PDF.

  [Download](https://academy.claude.com/assets/v1/work-along-companion-c5lkvz0n.pdf)

## What’s next[](#whats-next)

The next module, Governance, turns inward to how freely members customize Claude itself: the skills they build, how those skills are shared, and the organization instructions that shape Claude for everyone, along with the governance posture that covers all three.

[Previous lessonSurfaces each group gets](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/surfaces-each-group-gets)[Next lessonGoverning customizations](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/governing-customizations)

Lesson 7 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutConnectors

The plan

* [Five decisions and the frame](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/five-decisions-and-the-frame)
* [Owners and intake](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/owners-and-intake)
* [Prerequisites](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/prerequisites)

Structure & Identity

* [One organization or many](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/one-organization-or-many)
* [Your groups](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/your-groups)

Access

* [Surfaces each group gets](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/surfaces-each-group-gets)
* [Connectors](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/connectors)

Governance

* [Governing customizations](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/governing-customizations)

Spend

* [Spend caps](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/spend-caps)
* [Managing spend](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/managing-spend)

Visibility

* [Visibility: what you can measure](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/visibility-what-you-can-measure)
* [Adoption signals](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/adoption-signals)

Your rollout

* [How the decisions connect](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/how-the-decisions-connect)
* [When a new product arrives](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/when-a-new-product-arrives)
* [Certificate quizQuiz](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/certificate-quiz)

* [Completion badge](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/badge)

* [What a connector is](#what-a-connector-is)
* [The three gates](#the-three-gates)
* [What you control](#what-you-control)
* [Enterprise-managed authorization](#enterprise-managed-authorization)
* [Read and write access](#read-and-write-access)
* [Pluto’s connectors](#plutos-connectors)
* [1 · Your decision](#1-your-decision)
* [2 · The choices you can make](#2-the-choices-you-can-make)
* [3 · If you change this later](#3-if-you-change-this-later)
* [Set up resources](#set-up-resources)
* [Lesson activity](#lesson-activity)
* [What’s next](#whats-next)
