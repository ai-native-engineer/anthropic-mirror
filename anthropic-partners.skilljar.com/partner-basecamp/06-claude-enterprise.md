<!-- https://anthropic-partners.skilljar.com/partner-basecamp/465965 -->
<!-- scorm-content: https://anthropic-partners.skilljar.com/content/wp/4hdejjwplbrm/qq3fuvpkhoai/module-04-claude-enterprise.html -->

# Claude Enterprise

Module 4 of 6

# Claude Enterprise

Before you can recommend Claude Enterprise to a client, you need to know exactly what it is, who buys it, and which five features close the conversation.

Partner Basecamp
~18 min
SET B - DAY 2 PREP
2 practice scenarios

What you'll walk away with

## Three things you'll be able to *do*

This module covers the full Claude Enterprise surface area. Not just what it is, but who buys it, what actually closes the deal, and how to position it against competitors.

1

Describe Claude Enterprise to any stakeholder

Walk any audience through the product, its surfaces, its billing model, and its position in Anthropic's portfolio. No product sheet required.

2

Map a customer's words to the right feature

When a VP of Clinical Ops says "patient data compliance," you'll know the answer before she finishes the sentence. Same instinct applies across every role and vertical.

3

Know the five features that close the upgrade

SSO won't move a deal from Team to Enterprise anymore. You'll know which five features do, and how to use them in a positioning conversation.

The product

## What Claude Enterprise *actually is*

Definition

Claude Enterprise is Anthropic's business-grade plan, designed for organizations that need Claude deployed securely across teams at scale. It gives every employee access to Claude through an interface built for their job, with the governance controls IT and legal actually need.

Billing model (new orgs)

Usage-based

Base seat fee plus actual token consumption. No session caps. Existing orgs may still be on legacy seat-based pricing.

Strategic position

Employees work smarter

Anthropic's vehicle for making every person in an organization more productive with AI. Success examples include Cognizant, Disney, Travelers, and Eli Lilly. Your account rep can share relevant case studies for your specific vertical.

Three product surfaces

🌐

Claude.ai (Web)

Full interface with SSO, SCIM, RBAC, and audit logs built in

💻

Claude Desktop

Home for Cowork and local file access. Enterprise-managed deployment on macOS and Windows

📱

Claude Mobile

iOS and Android for on-the-go access

The buyer

## Claude Enterprise isn't a *developer tool*

Every function in an enterprise has a use case. The frame for any call: what does this person do all day? Work backward from their most time-consuming, repetitive task.

By Team
By Vertical

Marketing

* Analyzing market trends and audience behavior
* Drafting content at scale
* Developing campaign strategies and briefs
* Building performance reports

Sales

* Analyzing call transcripts and planning accounts
* Preparing objection handling and talk tracks
* Developing pitch decks and proposals
* Tracking metrics and KPI analysis

Product

* Drafting product vision and objectives
* Creating specs and requirements docs
* Analyzing user feedback and usage data
* Building roadmaps and prioritization frameworks

HR

* Writing job descriptions and recruiting materials
* Creating training modules and documentation
* Developing employee growth and review plans
* Analyzing engagement and retention data

Legal

* Drafting and redlining commercial agreements
* Summarizing laws and regulatory changes
* Streamlining compliance review processes
* Supporting litigation research and prep

Financial Services

* Building financial models (DCF, comps, 3-statement)
* Generating investment research and pitchbooks
* Ingesting full 10K filings in a single context window

Healthcare

* Integrating with EHR systems for clinical workflows
* Automating prior authorization and documentation
* Summarizing patient records and care plans

Life Sciences

* Accelerating R&D with literature and data review
* Querying clinical trial databases
* Streamlining drug development pipelines

Cybersecurity

* Investigating SOC alerts and triaging threats
* Generating and tuning detection rules
* Automating incident response workflows

Telecom

* Managing identity verification and fraud detection
* Optimizing network performance and troubleshooting
* Scaling AI-powered customer service

Retail

* Automating operational workflows and analytics
* Orchestrating multi-agent commerce systems
* Generating brand and product content at scale

Lead with relevance

Before any discovery call, identify the customer's vertical and their most document-heavy or repetitive workflow. That's where Claude Enterprise earns the conversation.

The feature set

## Three clusters. Every deal maps to *at least one*.

Claude Enterprise's capabilities fall into three areas. When a customer describes a pain, your job is to locate it in one of these clusters and name the specific feature that solves it.

Data and Connectivity

Native Connectors

First-party integrations with Google Drive, Gmail, Google Calendar, GitHub, Microsoft 365, and Slack. No custom setup required.

Custom Connectors (MCP)

Open standard for connecting Claude to any external app, internal database, or legacy system. Growing ecosystem of pre-built connectors.

File Handling

Upload PDFs, Excel, Word documents, images, and more. 30MB per file. Claude reads and reasons across all of it.

Shared Workspace

Projects (500K context)

Persistent workspaces with files, custom instructions, and a 500K token context window. Every conversation starts warm. Teams share one context instead of starting from scratch.

Workflows and Output

Skills

Package custom capabilities for repetitive workflows so any team member can trigger them, consistently.

Artifacts

Rich interactive outputs: documents, code, charts, React components. Deliverables that live in a shareable workspace.

Enhanced Context (up to 1M tokens)

Ingest hundreds of transcripts, dozens of long documents, or 100K lines of code in a single context. 500K standard context window. Up to 1M tokens is available for customers with specific compliance or data processing requirements.

Make the 500K window concrete

The number alone won't land. Try this: "500K tokens means loading three months of customer call transcripts and asking Claude to identify every objection pattern across all of them."

Practice

## Hear the customer. Name the *feature*.

You're in a discovery call with a 2,000-person health system. The VP of Clinical Ops, CMO, and compliance team each raise a concern. Match each one to the Claude Enterprise feature that answers it.

Health system discovery call: 4 customer statements

Statement 1 of 4

VP of Clinical Ops

"We want to deploy AI across our clinical research and back-office teams (about 800 seats). Our biggest concern is patient data compliance."

SCIM Provisioning
HIPAA-ready offering + Business Associate Agreement
Custom Data Retention Controls

**HIPAA + BAA.** This is the first filter in any healthcare conversation. Before you discuss features, capabilities, or pricing: confirm HIPAA compliance and a BAA. As of January 2026, Anthropic offers a HIPAA-ready Claude Enterprise with a signed BAA. That's your lead.

Next statement

IT Director

"We use Okta. When someone joins, they need access the same day. When they leave, access revoked immediately. No lag."

SSO (SAML)
IP Allowlisting
SCIM Provisioning

**SCIM provisioning.** SAML SSO handles authentication, but it doesn't manage user lifecycle. SCIM syncs your identity provider (Okta, Azure AD, etc.) directly with Claude Enterprise, so provisioning and deprovisioning is automatic. For an 800-seat rollout, manual user management is a security risk and an ops burden. SCIM solves both.

Next statement

Chief Compliance Officer

"We need a full audit trail: who used Claude, what they asked, what data was accessed. And it has to pipe into our SIEM."

Custom Data Retention Controls
Audit Logs + Compliance API
RBAC

**Audit Logs + Compliance API.** Audit Logs capture 180 days of every prompt, response, and file access, all queryable. The Compliance API is the SIEM integration path: programmatic access to activity logs, chat histories, and file content. Note: the Compliance API docs aren't public. Customers access them through their account rep via the Trust Center under NDA.

Final statement

CISO

"Access needs to be restricted to our corporate VPN only. Researchers get full capabilities. Admin staff should have limited access."

SCIM + Compliance API
IP Allowlisting + RBAC
Audit Logs + Tenant Restrictions

**IP Allowlisting + RBAC.** Two separate problems, two specific features. IP Allowlisting restricts Claude access to your corporate network or VPN. Users off-network simply can't reach it. RBAC (Role-Based Access Control) handles the internal permission layer: different roles get different capabilities. For an IT leader, name both explicitly rather than bundling them.

See results

🎯

#### The goal is to read the room

Every pain in that discovery call maps to a specific feature. That instinct (hear a concern, name the capability) is what separates a qualifying conversation from a forgettable one. Continue to see the governance picture in full.

Governance and security

## Identity, access, and *control*

Enterprise procurement decisions are often made by IT and security, not the business buyer. This is the layer they scrutinize. Know it cold.

| Feature | Free | Team | Enterprise |
| --- | --- | --- | --- |
| SAML SSO | ✕ | ✓ | ✓ |
| **SCIM Provisioning** | ✕ | ✕ | ✓ |
| **IP Allowlisting** | ✕ | ✕ | ✓ |
| **Tenant Restrictions** | ✕ | ✕ | ✓ |

Common mistake

SSO is available on **Team and Enterprise**. Do not use it as a reason to upgrade. If a customer is already on Team and asks why they should move to Enterprise, SSO is not your answer.

Current RBAC (Role-Based Access Control) roles

User

Base access: chats and projects

Admin

Member management and usage analytics

Owner

SSO, integrations, data controls, audit logs

Primary Owner

Seats, billing, data exports. One per org.

Enterprise-only security

## Four features that exist *nowhere else* in the stack

These don't exist on Free or Team. In regulated industries, they're often what turns a proof of concept into a signed contract.

1

Audit Logs

180-day retention for user actions, system events, and data access. Every prompt, every response, every file access logged and queryable.

Enterprise only

2

Compliance API

Programmatic access to activity logs, chat histories, and file content. The SIEM integration path. Docs available via the Trust Center under NDA through account reps.

Enterprise only

3

Compliance Frameworks

HIPAA-BAA (healthcare). FERPA (education, via school official exemption). FedRAMP (U.S. government agencies, through Claude for Public Sector). GDPR (EU and international, via Data Processing Agreements).

Enterprise only

4

Custom Data Retention

Configure retention periods for chats and projects. Minimum 30 days, deletion at midnight UTC. Critical for organizations with data residency requirements or legal holds.

Enterprise only

The competitive frame

vs.

ChatGPT Enterprise

"ChatGPT was built for consumers and extended to enterprise. Claude Enterprise was built for enterprise *from the start.*"

vs.

Microsoft Copilot

"Copilot works great if you live entirely in M365. Claude Enterprise works across M365, Google, Slack, GitHub, and your custom data sources *simultaneously.*"

vs.

Google Gemini

"If you're all-in on Google, Gemini is fine. The moment you need to touch Slack or GitHub, *you're patching it together.*"

Tier comparison

## How Claude Enterprise stacks up against *Team and Free*

The five features that move a deal from Team to Enterprise are not the ones you might expect. One important item dropped off the list entirely.

The upgrade triggers that actually work

Lead with these five: **500K context window, SCIM provisioning, Compliance API, Audit Logs, HIPAA-ready.** SSO is on Team too. It no longer moves deals.

| Feature | Free | Team | Enterprise |
| --- | --- | --- | --- |
| Core capabilities | | | |
| **Context window** | 200K | 200K | **500K** |
| Seats | 1 | 5–75 | Unlimited |
| Claude Code and Cowork | ✕ | ✓ | ✓ |
| Native 1P Connectors (M365, Slack, etc.) | ✕ | ✓ | ✓ |
| SSO and Domain Capture | ✕ | ✓ | ✓ |
| No model training on content | ✕ | ✓ | ✓ |
| Enterprise only | | | |
| **SCIM Provisioning** | ✕ | ✕ | ✓ |
| **RBAC** | ✕ | ✕ | ✓ |
| **Audit Logs (180-day)** | ✕ | ✕ | ✓ |
| **Compliance API** | ✕ | ✕ | ✓ |
| **Custom Data Retention** | ✕ | ✕ | ✓ |
| **IP Allowlisting** | ✕ | ✕ | ✓ |
| **HIPAA-ready** | ✕ | ✕ | ✓ |

Claude for Education

Claude Enterprise with higher-ed enhancements: EDU MCP integrations (Panopto, Wiley), LTI integration in Canvas LMS, Socratic Learning Mode, school-specific project templates, and dedicated onboarding with train-the-trainer support. Also available via AWS Marketplace private offers.

Cowork

## Not a replacement. A *different capability entirely*.

The question comes up constantly: is claude.ai being replaced by Cowork? No. They serve different jobs. Getting this clear matters because customers will ask, and you need a confident, accurate answer.

Claude.ai

A conversational interface. Fast, accessible, great for chat-first tasks: drafting, summarizing, answering questions. Works in any browser. No local file access.

Cowork

An agentic product for multi-step work involving local files, browser automation, document creation, and sustained working context across a session. Runs in a sandboxed VM inside Claude Desktop.

Important

Cowork is **included in every Claude Enterprise seat**. Not an add-on. Not a separate SKU. Built on the same Agent SDK as Claude Code, packaged for non-developers who need agentic capabilities.

Six things Cowork does that claude.ai can't

Browser Use

Chrome extension lets Claude navigate legacy portals (Salesforce, government tools), fill forms, and extract data.

Agentic Architecture

Sub-agent orchestration breaks complex work into tracked sub-tasks with a visible progress UI.

Local File System

Reads, edits, and creates files locally. Takes raw data to finished deliverables: financial models, PPTX, reports.

Plugins

Role-specific specialization and enterprise workflow automation. Admins can standardize them org-wide.

Progress UI

Multiple-choice discovery before work starts, then a right-panel TODO tracker showing live progress and completed artifacts.

Skills and MCP Connectors

Pre-packaged capabilities and external tool integrations. Build once, deploy across the org.

Practice

## Which upgrade trigger do you *lead with?*

Three customer situations. In each one, pick the strongest Claude Enterprise response. Some options sound plausible. One is clearly right.

Scenario 1 of 3

Scenario 1

A CFO at a 600-person financial firm says: "We need to make sure only employees on our internal network can access Claude. No access from home, no access on personal devices."

SCIM Provisioning
IP Allowlisting
SSO (SAML)
Tenant Restrictions

Next scenario

Scenario 2

A legal ops director says: "We have hundreds of contracts and we need to analyze all of them against our updated risk framework simultaneously. Can Claude actually handle that volume?"

Audit Logs
500K context window
Native Connectors
HIPAA-ready offering

Final scenario

Scenario 3

Your contact is on Claude Team and happy with it. Their IT director asks: "We already have SSO through Okta on Team. What would we actually gain by moving to Enterprise?"

"SSO works even better integrated at the Enterprise tier."
"You'd get 500K context, SCIM, Audit Logs, Compliance API, and HIPAA. Those are the five things Team can't give you."
"Team is probably enough for most organizations your size."
"Enterprise gives you access to more advanced Claude models."

See results

🎯

#### Aim for the right positioning

Know which features close deals, and know which ones don't move needles anymore. That's the difference between a product walk-through and a conversation that leads somewhere.

Module 4 of 6 Complete

## The conversation that closes isn't about features. It's about *fit*.

You can now describe **Claude Enterprise** to any stakeholder, map a customer's words to a specific capability, and name the five features that justify the upgrade from Team. The next module takes you inside the tool that extends Claude's reach beyond the browser and into your client's actual workflow.

Next up: Module 5

Claude Cowork

You've positioned Cowork as part of Enterprise. Now you need to show what it actually does. What can it accomplish that claude.ai can't? And how do you demo it in a way that lands with a non-technical buyer?

Mark module as complete



Begin
