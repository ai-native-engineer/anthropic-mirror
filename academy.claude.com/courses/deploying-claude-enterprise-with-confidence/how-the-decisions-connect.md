<!-- source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/how-the-decisions-connect -->

Lesson 13 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutHow the decisions connect

3. /[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

# How the decisions connect

Lesson 137 min

In this lessonBy the end, you’ll be able to

* Review how your five decisions relate to your rollout objective
* Predict how a change to one setting cascades across the other decisions
* Turn your completed companion into the rollout plan you walk your stakeholders through at kickoff

By now you should be well on your way to having concrete decisions for your Claude Enterprise deployment: they’ll either be made, or packaged and sitting with their owners. This lesson allows you to look at your decisions next to Pluto’s, consider what changing any one of them would set off, and reflect on how a regulated function’s answers hold together.

## Your five answers[](#your-five-answers)

If you recall, Pluto’s objective from Lesson 1 was to have every business unit using Claude in its daily work by the end of the quarter, measured as weekly active usage in each unit, without a single security escalation from Payments & Trust. The column on the right (“Tie to the objective”) reads each of Pluto’s answers against this objective.

Open your companion and review your entry for each decision as you go down the table. The table mirrors the companion’s decision record with Pluto’s answers filled in for comparison.

| **Decision** | **Pluto’s answer** | **Tie to the objective** |
| --- | --- | --- |
| **1 · Structure & Identity** Lessons 4 and 5 | • One organization • Groups aligned with the org chart, plus a cross-unit Engineering group • A dedicated payments-eng group | One organization keeps all five units in one rollout and one usage pool; the payments-eng group isolates the regulated function’s settings without a second organization. |
| **2 · Access** Lessons 6 and 7 | • Claude chat and Claude Cowork for every group • Claude Code for Engineering and Platform first (payments-eng waited until visibility reporting was in place) • Connectors scoped per group, read-only for payments-eng | Chat and Cowork everywhere puts Claude in every unit’s daily work; holding Claude Code and write-access connectors back for payments-eng protects the no-escalation constraint without significantly impacting adoption. |
| **3 · Governance** Lesson 8 | • Open build, reviewed spread for most groups • Approve-first for Payments & Trust | Open building lets the four ordinary units spread what works; approve-first review keeps Payments & Trust’s customizations from becoming the escalation. |
| **4 · Spend** Lessons 9 and 10 | • Organization ceiling • Group caps sized to typical usage • Per-member overrides for the handful of Platform engineers running well above the group, after the first usage review • A mid-range default model • Monthly review of spend caps and requests | Spend caps sized to typical usage keep members working instead of paused, so adoption isn’t throttled; the monthly review moves the settings, not just the caps, when spend climbs. |
| **5 · Visibility** Lessons 11 and 12 | • Compliance API into the existing security review • Telemetry to the observability stack • Organization-wide retention set to the shorter window Payments & Trust requires • Adoption read group by group | The record is on before members are in, so a Payments & Trust question gets evidence instead of an escalation; group-by-group reads show whether every unit is on track by quarter’s end. |

Where your answer differs from Pluto’s, that’s your organization’s unique characteristics showing through: trace the difference back to the rollout objective you wrote in Lesson 1. If you find it challenging to explain the decision, it’s worth a second look before you share with your stakeholders.

## Predict a cascade[](#predict-a-cascade)

Structure comes first, the other decisions attach their settings to the groups it defines, and Visibility reads across all of it. Now that you know what each setting is, the map has a second use: predicting what changes below a setting when you change it.

Add a group at Pluto, for instance, and it needs a surface grant (Lesson 6), a connector scope (Lesson 7), a cap (Lesson 9), and a dashboard filter (Lesson 12) before anyone in it goes live.

The interactive widget below runs one change through the decision map and shows what changes downstream, from where it starts to what it reaches.

## Regulated functions: one posture, not five exceptions[](#regulated-functions-one-posture-not-five-exceptions)

If you have a regulated function, this section is the check that its five answers form one posture rather than five separate exceptions; Pluto’s Payments & Trust is the worked example.

* **Structure**: its members sit in their own group, so the union rule gives them nothing broader than their own group’s role (Lesson 5).
* **Access**: the same surfaces as their neighbors, with Claude Code held until visibility reporting is in place (Lesson 6), and connectors read-only (Lesson 7).
* **Governance**: approve-first, while the rest of Pluto builds freely and shares within the group, with a reviewer for anything beyond it (Lesson 8).
* **Spend**: a group cap sized like any other group’s, with every increase request getting a look before it’s approved (Lesson 9).
* **Visibility**: they are the reason Pluto’s organization-wide retention window is the shorter one, with the Compliance API on and a named reader in the security review (Lesson 11).

Re-read those entries in your companion as a set. One group handled through the ordinary system, with no special machinery: that is why it holds. If your whole organization is regulated, that set is your baseline.

## Set up resources[](#set-up-resources)

When a decision needs a second look before the kickoff, the article behind every setting in this course lives in one of these two collections.

* **[Team and Enterprise plans(opens in new tab)](https://support.claude.com/en/collections/9387370-team-and-enterprise-plans)**: the full set of Team and Enterprise admin articles, for re-reading any one decision.
* **[Admin management(opens in new tab)](https://support.claude.com/en/collections/9811449-admin-management)**: the how-to articles behind the settings you now revisit.

## Lesson activity[](#lesson-activity)

Three more steps turn your companion into the rollout plan you bring to your stakeholder kickoff.

* **Review the hard-to-undo settings:** confirm each of the four (domain claiming, how many organizations, the group mapping, retention) on your companion’s Lesson 13 checklist is either decided, or on an owner’s desk with a decide-by date.
* **Close any open items:** for each decision still open, write what is blocking it, what it takes to unblock, and a decide-by date. An owner’s name alone is not a plan; an open item with none of these is where a rollout stalls.
* **Sequence the plan:** the companion lists the order (structure, then access, governance, spend, visibility on, then go-live by group); put an owner and a start date on each step.

→ Record this in the work-along companion, section Lesson 13.

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

The final lesson covers what happens when a new surface arrives: which of your answers carry over as they are, and which decisions you’ll run again.

[Previous lessonAdoption signals](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/adoption-signals)[Next lessonWhen a new product arrives](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/when-a-new-product-arrives)

Lesson 13 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutHow the decisions connect

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

* [Your five answers](#your-five-answers)
* [Predict a cascade](#predict-a-cascade)
* [Regulated functions: one posture, not five exceptions](#regulated-functions-one-posture-not-five-exceptions)
* [Set up resources](#set-up-resources)
* [Lesson activity](#lesson-activity)
* [What’s next](#whats-next)
