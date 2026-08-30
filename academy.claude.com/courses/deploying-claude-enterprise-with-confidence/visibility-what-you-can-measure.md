<!-- source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/visibility-what-you-can-measure -->

Lesson 11 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutVisibility: what you can measure

3. /[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

# Visibility: what you can measure

Lesson 1110 min

In this lessonBy the end, you’ll be able to

* Explain what the Compliance API records, what it doesn’t, and how it differs from audit logs and full data exports
* Decide whether to route OpenTelemetry export to your observability stack as an operational complement to the Compliance API
* Choose a retention window matched to your existing data policy and propose inference hooks for content that shouldn’t reach Claude at all

This is the fifth of the five decisions, Visibility. You’ve set what your rollout costs. This lesson covers visibility: the three pieces (the Compliance API, OpenTelemetry, and retention) and the one decision among them that’s hard to walk back.

## What visibility is for[](#what-visibility-is-for)

The first four decisions you made configure what Claude does. Visibility is how you determine whether they’re working. Visibility also lets you answer specific after-the-fact questions with evidence: Which members touched a particular account? What did Claude produce in a sensitive conversation? How long is that conversation kept? These answers can only come from records you were already keeping.

That’s why you set visibility up before members get access, not after: the stretch between first access and the day you turn recording on is time with no content record behind it. Three pieces give you the coverage: the Compliance API (conversation content, plus audit log events), OpenTelemetry (how the surfaces are running), and retention (how long content is kept).

## The Compliance API: your record of conversation content[](#the-compliance-api-your-record-of-conversation-content)

The Compliance API is the content-carrying record. It is generally available for Claude chat on Enterprise plans, excluding Public Sector organizations, and for Claude Platform customers. Coverage extends to Cowork — through Claude, Claude Desktop, and Claude Mobile — and to Claude Code through the CLI and Claude Desktop, generally available for Enterprise customers; both run on your organization’s existing Compliance Access Key and settings, so there is nothing extra to integrate. The help center’s [Compliance API article(opens in new tab)](https://support.claude.com/en/articles/13015708-access-the-compliance-api) links the setup documentation on Claude Platform Docs. It carries activity feed events, chat data, and file content, so it can answer “what was said” and “what was shared,” not just “who logged in when.” Whether it meets a specific legal or regulatory requirement is your legal and compliance owners’ call. Integrate it with the CASB, DLP, eDiscovery, and SIEM tools you already run — many of those vendors have built integrations on the Compliance API, listed in [Get started with Claude Compliance API integrations(opens in new tab)](https://support.claude.com/en/articles/15167101-get-started-with-claude-compliance-api-integrations).

The Compliance API is easy to confuse with two other records:

* **Audit logs are metadata-only.** They record events (who did what when: admin and member actions) with no prompts and no completions. The Compliance API now includes audit log events too, so one record carries both, but the distinction still matters: when someone asks for content, metadata alone is the wrong answer.
* **Full data exports are a separate Primary Owner capability**, for pulling your organization’s data wholesale rather than reviewing it case by case.

The Primary Owner enables the Compliance API. Access keys are scoped when they’re created: a Primary Owner key can cover every organization under the parent, while an Owner key covers that Owner’s organization only. A Primary Owner can also create a key scoped to a single organization (a child of the parent), not only a parent-wide one — scope is a per-key choice at creation, not fixed by role. The decision that matters after that is who reads it: a record no one reviews isn’t actually a control. Many companies already have a place where security logs go (a SIEM or your security tooling’s central collection point) with an owner who reviews them. Route the Compliance API there, and Claude becomes one more source in a review process that already exists.

## OpenTelemetry: how the surfaces are running[](#opentelemetry-how-the-surfaces-are-running)

OpenTelemetry export sends operational telemetry to your observability stack: usage patterns and performance, and on some surfaces conversation content. Claude Code has a documented opt-in for logging prompts if your engineering team turns it on; by default its telemetry is operational data. Cowork’s export includes prompt content by default, so filter it in your collector if your policy requires. Treat OpenTelemetry as “how it’s running,” complementary to the Compliance API’s “what was said,” and optional: the Compliance API, not telemetry, is the record to rely on for content. If your platform team already runs an observability stack, this is a routing task for them.

## Retention: how long content is kept[](#retention-how-long-content-is-kept)

Retention is how long conversation content is kept before deletion. Left at the default, content is kept indefinitely until you or your members delete it. If you set a custom retention window instead, content is deleted automatically on your schedule: the clock runs from a chat’s last message and from a project’s last update, and for a chat kept inside a project, the project’s window applies instead of the chat’s. The shortest custom window is 30 days. This setting has no zero-retention option.

Data reached through the Compliance API follows its own retention model:

* Activity feed and remote session transcripts (sessions run on Anthropic’s servers, not on a member’s machine): six years regardless of the window you set.
* Local session transcripts from Cowork and Claude Code: your custom window when you set a finite one, or six years when you don’t.

So a short window limits what members keep, not what the compliance record holds.

Retention is an organization-wide setting, so choose it against the data-governance policy your company already has for this class of content, and involve whoever owns that policy, so the number is approved before you set it. If a regulated function needs a shorter window than the rest of your organization would like, the shorter window is what everyone gets, so name that trade-off to the affected teams so they’re aware.

One proposal to bring to that conversation is inference hooks: every prompt from Claude chat, Cowork, and Claude Code goes to a server your security team or their vendor operates for an allow-or-deny decision before Claude answers, so content that shouldn’t reach Claude at all is blocked at the door rather than governed by retention after the fact. The help center’s [Inference hooks overview(opens in new tab)](https://support.claude.com/en/articles/16059458-inference-hooks-overview) covers what they are and who can turn them on.

The interactive widget below shows how each of these decisions affects your ability to answer questions about your data after the fact.

## Pluto’s visibility[](#plutos-visibility)

Pluto’s Primary Owner enabled the Compliance API before general rollout and routed it into the security review Pluto already runs, so a named reviewer reads it as part of an existing process. Cowork and Claude Code sessions fall under the Compliance API’s coverage, and their operational telemetry exports to the observability stack that Platform already runs. And because Payments & Trust required a shorter window than the other units would have chosen, the risk owner set the organization-wide retention to that shorter number.

## 1 · Your decision[](#1-your-decision)

What retention window do you set, and is the Compliance API on and routed to a reviewer?

## 2 · The choices you can make[](#2-the-choices-you-can-make)

| **The choice** | **When you’d choose it** | **What it means and the impact it has** |
| --- | --- | --- |
| **Match your existing data policy, Compliance API on** | The default. You have a data-governance policy for this class of content and a security/compliance review process a named reviewer already runs. | Retention set to whatever your data-governance policy already says for this class of content. Compliance API on and routed to the review you already run. |
| **Regulated posture, Compliance API expected** | You handle regulated data. | Compliance API moves from optional to expected. The retention window is typically set organization-wide against your regulatory and contractual obligations rather than your general data policy — that call sits with your risk owner. The whole organization gets the regulated group’s number. |
| **Compliance API off, condition documented** | No review process exists and none is planned. | Leave the Compliance API off for now and write down the condition that turns it on. Note that until it’s on, questions about that period have no content record to draw on. |

If part of your company’s data must be fully separated from the rest, that isn’t a retention setting: it’s the separate-organization question from Lesson 4, so route it back there rather than trying to solve it here.

## 3 · If you change this later[](#3-if-you-change-this-later)

The Compliance API and OpenTelemetry are toggles and destinations you can change any time. Retention is different in kind: the setting moves freely, but the content it deletes doesn’t come back. Shortening the window later erases history your members had built up under the old one. So agree on the window once, before members accumulate work under a number you’ll want to change.

## Set up resources[](#set-up-resources)

When you’ve made the call, retention and the Compliance API are set in Organization settings, and the Primary Owner turns the Compliance API on.

* **[Configure custom data retention controls for Enterprise plans(opens in new tab)](https://support.claude.com/en/articles/10440198-configure-custom-data-retention-controls-for-enterprise-plans)**: setting your organization-wide retention window.
* **[Access the Compliance API(opens in new tab)](https://support.claude.com/en/articles/13015708-access-the-compliance-api)**: enabling the record and routing it into the review you already run.
* **[Access audit logs(opens in new tab)](https://support.claude.com/en/articles/9970975-access-audit-logs)**: the record of admin and member actions, which you pull through the Compliance API alongside the conversation record.
* **[View usage analytics for Team and Enterprise plans(opens in new tab)](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans)**: the adoption read (Lesson 12).
* **[Monitor Claude Cowork activity with OpenTelemetry(opens in new tab)](https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry)**: Cowork’s export, which includes prompt content by default.
* **[Monitoring(opens in new tab)](https://code.claude.com/docs/en/monitoring-usage)**: enabling and configuring OpenTelemetry export for Claude Code.
* **[Inference hooks overview(opens in new tab)](https://support.claude.com/en/articles/16059458-inference-hooks-overview)**: proposing a pre-answer allow-or-deny gate for content that shouldn’t reach Claude at all.
* **[Get started with Claude Compliance API integrations(opens in new tab)](https://support.claude.com/en/articles/15167101-get-started-with-claude-compliance-api-integrations)**: the CASB, DLP, eDiscovery, and SIEM integrations vendors have built on the Compliance API.

## Lesson activity[](#lesson-activity)

This is one of the two decisions that usually escalates, so the companion section doubles as the brief you hand the visibility owner from Lesson 2. The risk lead makes the call for this one. Assemble it in four parts:

1. The three pieces (conversation content, operational telemetry, retention), the process at your company it plugs into, and the person who owns that process. Any piece with no existing process is one where you’d be building a review process from scratch. Flag it before rollout, because those take the longest to stand up.
2. Your recommended retention window and the existing policy it matches.
3. Your Compliance API recommendation, with the name of whoever would read it.
4. Where telemetry lands.

**What to bring your visibility owner**: the three pieces, your retention recommendation, your Compliance API recommendation and who would read it, and where telemetry lands. Hand it to the visibility owner you named in Lesson 2, and record their call when it comes back.

→ Record this in the work-along companion, section Lesson 11.

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

You can now prove what happened. Whether the rollout is *working* is a different question with a different answer: the adoption signals your analytics report, read against the rollout objective you set in Lesson 1. The next lesson shows you how to read them, where they can mislead you, and how to set the pace goal that gives your objective a timeline.

[Previous lessonManaging spend](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/managing-spend)[Next lessonAdoption signals](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/adoption-signals)

Lesson 11 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutVisibility: what you can measure

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

* [What visibility is for](#what-visibility-is-for)
* [The Compliance API: your record of conversation content](#the-compliance-api-your-record-of-conversation-content)
* [OpenTelemetry: how the surfaces are running](#opentelemetry-how-the-surfaces-are-running)
* [Retention: how long content is kept](#retention-how-long-content-is-kept)
* [Pluto’s visibility](#plutos-visibility)
* [1 · Your decision](#1-your-decision)
* [2 · The choices you can make](#2-the-choices-you-can-make)
* [3 · If you change this later](#3-if-you-change-this-later)
* [Set up resources](#set-up-resources)
* [Lesson activity](#lesson-activity)
* [What’s next](#whats-next)
