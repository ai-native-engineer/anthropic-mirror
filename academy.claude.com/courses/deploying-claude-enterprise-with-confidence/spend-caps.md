<!-- source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/spend-caps -->

Lesson 9 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutSpend caps

3. /[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

# Spend caps

Lesson 99 min

In this lessonBy the end, you’ll be able to

* Describe the three spend cap levels and predict which one applies to a given member
* Explain what a member experiences at a cap and how their request reaches an Owner
* Decide where caps sit for your organization and who owns the escalation

This is the fourth of the five decisions, Spend. You’ve set the rules for what members build. This lesson covers spend caps: the three levels they sit at, what happens when a member hits one, and who owns the escalation.

## What caps are and where they sit[](#what-caps-are-and-where-they-sit)

Spend caps come in three levels, from widest to narrowest:

1. **The organization ceiling:** the total your organization can draw in a given month; no group cap or per-member override lets anyone draw beyond it.
2. **Group caps: per-member limits that every member of a group inherits, sized to that group’s typical usage.**
3. **Per-member overrides**: a specific member’s own limit, set individually, above or below their group’s number.

Under the group caps sits a seat default limit, set under Spending defaults — the number a member gets before setting any group cap or override. When a member belongs to two groups that both carry a cap, one organization-wide setting (Multi-group spend limit, under Spending defaults) decides which applies, and you choose whether the higher or the lower group cap wins. Set it deliberately, because unlike the permissions union rule from Lesson 5, where the broader grant always wins, here the decision is yours.

## How caps work in practice[](#how-caps-work-in-practice)

When a member hits their cap, their usage is paused. A pause is not an outage, and no work is queued to run later. The member can’t use Claude beyond the cap until their limit resets with the new month, or until an approved request lifts it. The member also sees an in-app prompt to request more, and the request routes to your Admins and Owners to approve or deny.

One thing to watch for at scale: approvals sit with your Owners, but the budget usually sits with someone else. This dynamic means that in-product requests can sometimes wait days for a decision. Large organizations commonly route cap increase requests through their own ticketing instead — the Spend Limits API can list, approve, and deny requests as well as set limits.

Rather than setting caps one member at a time, use the group cap as your scale mechanism: size it to the group’s typical usage and let membership do the assignment. A group cap is not a pooled budget the group shares, and it is not necessarily proportional to headcount — it answers “how much does one member of this group typically need?” Overrides are for specific exceptions, such as the analyst who runs a heavy monthly data analysis job with Claude Code. This gives the analyst what they need without raising the cap for the entire group that contains them.

Where per-member overrides multiply, the Spend Limits API, part of the Claude Enterprise Admin API (in public beta), sets them programmatically, so a platform team doesn’t have to set each one by hand. Group caps stay in your organization settings. If the list of overrides keeps growing, treat that as a signal that those members need a group of their own, not a longer exception list.

## Pluto’s caps[](#plutos-caps)

Pluto set an organization ceiling from the budget owner’s number and group caps sized to each unit’s typical member. After the first month’s usage review, the handful of Platform engineers whose Claude Code work ran well above the group’s typical usage got per-member overrides rather than a higher Platform cap. Raising the group cap would have lifted the ceiling for every engineer, including the ones already well within it, so the overrides target just the outliers who need the extra room. Payments & Trust reviews every request that touches its group.

The interactive widget below shows how a group cap and a per-member override combine for one member, and which cap your Multi-group spend limit setting applies when she belongs to two groups.

## 1 · Your decision[](#1-your-decision)

Where do caps sit for your organization (the ceiling, the group caps, any day-one overrides), and who owns the escalation when a member hits one?

## 2 · The choices you can make[](#2-the-choices-you-can-make)

This decision is a judgment call, not a toggle. You have to make the call on both how you set your caps and who owns the escalation once they’re set. Weigh the considerations under each together.

You can lean on the [Claude Enterprise consumption guide(opens in new tab)](https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide)’s tier structure rather than inventing your own. It recommends defining consumption tiers by role type before rollout (light, standard, and power) so caps are assigned and adjusted consistently; chat is the lighter surface, and Claude Code and Cowork consume more per session.

Put a number on each tier from your own usage history or your account team’s sizing guidance if you have one, record the date you set it, and treat it as the opening number you adjust against your own usage rather than a target. Two things bound the number you land on: the organization ceiling your budget owner holds, and the surfaces each group actually gets from Lesson 6.

Setting a cap comes down to three considerations, plus one constraint if you prepay, each weighed against how much usage history you have and the shape of the group’s work:

1. **Sized to typical usage:** the typical fit. Group caps sized to each group’s typical member, with membership doing the assignment.
2. **Tight, raised on evidence:** when usage is genuinely unknown (no history, new surfaces), start tight and treat each request as the usage evidence you need to rightsize the budget. Raising on evidence means re-basing a group’s cap to observed usage once the first month backs it up, rather than approving small increments repeatedly.
3. **Planned room for spiky work:** a group with month-end analyses or seasonal load gets a higher cap or overrides you set for the spike and remove afterward, instead of repeated emergency approvals.
4. **If you prepay usage credits:** the ceiling is your remaining prepaid credit. At zero, usage pauses organization-wide until credits are added, so the budget owner is on every ceiling change.

Decide the escalation split when you set the caps, not after the first request lands. Name the Owner who approves routine requests and agree on the approval range with the budget owner up front; anything that would move a group cap or the ceiling is the budget owner’s call, with your usage story attached. Members knowing the loop exists matters more than the exact split.

## 3 · If you change this later[](#3-if-you-change-this-later)

Caps can be changed freely; each change applies from that point.

## Set up resources[](#set-up-resources)

When you’ve made the call, you’ll set the ceiling, group caps, and any overrides in your organization settings.

* **[Manage groups and group spend limits on Enterprise plans(opens in new tab)](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)**: setting a cap on a group, and where that cap sits.
* **[Manage usage credits for Team and seat-based Enterprise plans(opens in new tab)](https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans)**: the organization-wide credit pool your caps draw against if you prepay credits.
* **[How usage and length limits work(opens in new tab)](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)**: the model- and plan-level limits that sit under any cap you set.

## Lesson activity[](#lesson-activity)

In many organizations the budget owner commits these numbers; if that’s your case, the companion section doubles as the brief you hand the budget owner. In your companion, draft:

* The cap table: the ceiling, the per-group numbers, and the tier you picked for each group, with why that tier.
* The members, if any, you already expect will need overrides.
* The escalation split: what you approve same-day, what goes to the budget owner.
* Which cap wins when a member is in two capped groups.
* Your organization’s usage history (if available), shared alongside the table so the reasoning behind each cap arrives with the ask.

**What to bring your budget owner**: the cap table, the overrides you expect, the escalation split, and the usage history behind them.

→ Record this in the work-along companion, section Lesson 9.

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

The next lesson covers how you’re billed and the settings that move spend without touching a single cap, so that when a request lands, raising the number is your last option instead of your first.

[Previous lessonGoverning customizations](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/governing-customizations)[Next lessonManaging spend](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/managing-spend)

Lesson 9 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutSpend caps

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

* [What caps are and where they sit](#what-caps-are-and-where-they-sit)
* [How caps work in practice](#how-caps-work-in-practice)
* [Pluto’s caps](#plutos-caps)
* [1 · Your decision](#1-your-decision)
* [2 · The choices you can make](#2-the-choices-you-can-make)
* [3 · If you change this later](#3-if-you-change-this-later)
* [Set up resources](#set-up-resources)
* [Lesson activity](#lesson-activity)
* [What’s next](#whats-next)
