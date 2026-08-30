<!-- source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/surfaces-each-group-gets -->

Lesson 6 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutSurfaces each group gets

3. /[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

# Surfaces each group gets

Lesson 610 min

In this lessonBy the end, you’ll be able to

* Set the model defaults, organization-wide and per role, and the effort caps a role can use
* Grant a surface to a group through its roles
* Decide which surfaces each group gets, and when to phase them in

This is the second of the five decisions, Access. You’ve created your groups. Now you grant them access to different Claude surfaces. A surface is a place your members use Claude, and your Claude Enterprise contract can include several (e.g., Claude chat, Claude Cowork, Claude Code, Claude for Microsoft 365).

Under most Claude Enterprise contracts, every surface the contract covers is available for your organization to switch on. Who can then use it depends on their role: members on the built-in roles get every surface that is on; a Custom-role member gets a surface only when you grant it. The work is deciding who gets which, and when, so that a surface reaches a group when your rollout strategy calls for it, rather than switching everything on at once. Two mechanics come before that decision: how a grant reaches a group, and the models these surfaces run on.

## How access is granted[](#how-access-is-granted)

Two layers decide whether a group can use a surface, and both must allow it.

* **The organization-wide toggle is the ceiling:** each surface has an on/off switch for the whole organization. Off means nobody has it, regardless of what their role allows.
* **The role grant decides who has access under that ceiling:** once a surface is on organization-wide, you grant it to the roles attached to the groups that should have it. Attach the surface to a group’s role, and every Custom-role member of the group gets it (Lesson 5); leave it off the role, and that group doesn’t gain access to the surface.

The interactive widget below shows the chain end to end: members land in a group, and the role applied to the group is what turns their access on.

Claude Code takes the same grant as any other surface: on for the organization, then attached to the roles of the groups that use it. Because it runs inside your engineering environment, it also carries a boundary configuration the other surfaces don’t have.

Those boundaries live in Claude Code’s managed settings, usually written by the platform or engineering lead who knows each team’s repositories, not by you. So when you grant Claude Code to a group, you decide which groups get it, and your platform lead configures which files, commands, and network destinations it can reach for each. Those managed settings can also pin Claude Code’s default model, though the models available to it stay governed on the Models page in your organization settings.

## Models: what a group’s conversations run on[](#models-what-a-groups-conversations-run-on)

Every new conversation starts on a default model, on every surface that supports it, and you control that default. Out of the box it adheres to Anthropic’s default, which updates as models are released and retired. Where your chosen model isn’t available in a product, that product falls back to the recommendation.

To set the default yourself, choose an organization default:

* It holds through model releases until you change it. An Owner, Primary Owner, or a custom role with the Identity & Access permission can set it.
* Members can still switch models in their own conversations. That choice carries to their next one until you change the organization default, which resets those selections.
* A custom role can carry its own default model, overriding the organization default for its members.

You can also limit which models a role reaches. These model-access and effort limits are set per role and apply only to Custom roles (Lesson 5). Effort is how much work the model puts into a response; higher effort costs more tokens. Give a custom role a subset of models and its members see only those in the picker (e.g., Haiku is always available), and the same settings cap the highest effort level they can pick on each model. You can find resources on [choosing between models(opens in new tab)](https://academy.claude.com/tutorials/choosing-the-right-claude-model) and [model effort(opens in new tab)](https://academy.claude.com/tutorials/how-to-select-the-right-effort-setting-for-claude-cowork-and-chat) on Claude Academy.

There are two main reasons to update the model default or restrict models for your organization:

* **Spend:** Models use tokens differently, so they cost different amounts to run. The most capable model is usually the most expensive place for routine work to happen. The help center’s article on [how usage and length limits work(opens in new tab)](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) covers how those limits differ by plan and model. Because most members run the model they see when they start a new task, the default steers most of your spend, and a model restriction caps what a group can spend per interaction. Lesson 10 goes into more detail on both as spend levers.
* **Task fit:** Coding teams, for example, may get more out of the most capable model as their starting point, while a team doing routine drafting may not need that level of capability. The default is set by role, so each group starts on the model that fits its work, and a restriction keeps a costly model out of the picker for a group that won’t gain significant benefit from it.

## Pluto’s surfaces[](#plutos-surfaces)

Pluto gives Claude chat and Claude Cowork to every group, because its objective is broad daily use. Claude Code goes to Engineering and Platform, whose daily work is writing code. Payments-eng waits for Claude Code until Pluto’s visibility reporting is in place, which keeps Pluto’s constraint — no security escalation from Payments & Trust — intact. The remaining surfaces phase in group by group as the work calls for them.

The interactive widget below fills Pluto’s grid step by step (broad surfaces first, then the specialized ones) and stops at the one grant that can’t turn on yet, with the reason.

## 1 · Your decision[](#1-your-decision)

Which surfaces does each group get, and when do you phase them in?

## 2 · The choices you can make[](#2-the-choices-you-can-make)

This decision is a judgment call rather than a mechanical rule. There are two main considerations:

* **Whether the surface changes the group’s daily work:** grant on what the group needs and will use, not on what your contract happens to cover.
* **Whether your rollout objective calls for holding a surface back:** piloting Claude with one team before giving members access, or waiting on a review before a group gets a surface.

| **The choice** | **When you’d choose it** | **What it means and the impact it has** |
| --- | --- | --- |
| **Broad first, specialized where needed** | Your rollout objective doesn’t call for holding a surface back, and only some groups’ daily work calls for the specialized surfaces. | Grant the general-purpose surfaces where most members get their first value; holding specialized ones back keeps you from configuring boundaries for groups that would never use them. |
| **Pilot, then widen** | Your rollout objective calls for testing Claude with one team before giving members access. | Grant the surfaces to the pilot group alone and widen from there. What you learn from the pilot shapes the broad rollout; the other groups wait until your objective says widen. |
| **Phased in behind a review** | A constraint (the second half of your rollout objective) means a group must wait for a surface until a review clears. | The grant simply phases in after the review clears; the group gets the surface then — the constraint stays intact while the group waits. |

## 3 · If you change this later[](#3-if-you-change-this-later)

Granting a surface later is cheap: it’s a role setting you can add any time. The expensive direction is taking one away: a group that has built its workflows on a surface loses a tool it relies on, mid-work, and revoking it is a change you’ll have to manage with those members.

## Set up resources[](#set-up-resources)

When you’ve made the call, you’ll grant each surface through your organization’s roles. For any group getting Claude Code, loop in your platform lead at the same time, so the boundary configuration is ready when access is.

* **[Set up role-based permissions on Enterprise plans(opens in new tab)](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans)**: granting a surface to a group through its role.
* **[Manage model access for your organization(opens in new tab)](https://support.claude.com/en/articles/15694740-manage-model-access-for-your-organization)**: the organization-wide default model, per-role defaults, and per-role model access and effort caps, including which surfaces those settings cover.
* **[Set a default model for your organization(opens in new tab)](https://support.claude.com/en/articles/15330088-set-a-default-model-for-your-organization)**: the organization default and per-role defaults, and how the same default can resolve to different models by surface.
* **[Choosing between models(opens in new tab)](https://academy.claude.com/tutorials/choosing-the-right-claude-model)**: guidance on model selection, from Claude Academy.
* **[Model effort(opens in new tab)](https://academy.claude.com/tutorials/how-to-select-the-right-effort-setting-for-claude-cowork-and-chat)**: guidance on effort levels, from Claude Academy.
* **[How usage and length limits work(opens in new tab)](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)**: how limits differ by plan and model.
* **[Claude Code managed settings(opens in new tab)](https://code.claude.com/docs/en/managed-settings)**: the boundary configuration your platform lead owns.

## Lesson activity[](#lesson-activity)

For each of your groups, mark the surfaces it gets on day one and the ones you’ll phase in later, and why. List separately every group getting Claude Code: that grant travels with a boundary-configuration task for your platform lead.

**What to bring your platform lead and budget owner:** for your platform lead, the list of groups getting Claude Code and what each group’s code touches; for the budget owner, a heads-up if you’re setting per-role default models, since that’s where the spend settings (Lesson 10) begin.

→ Record this in the work-along companion, section Lesson 6.

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

Your groups can reach their surfaces. The next question is what Claude can reach on their behalf: the connectors that let it read from and act on your organization’s tools. The next lesson covers the three gates that decide whether a connector works for a member, and the one control worth deciding tool by tool: read-only or read-write.

[Previous lessonYour groups](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/your-groups)[Next lessonConnectors](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/connectors)

Lesson 6 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutSurfaces each group gets

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

* [How access is granted](#how-access-is-granted)
* [Models: what a group’s conversations run on](#models-what-a-groups-conversations-run-on)
* [Pluto’s surfaces](#plutos-surfaces)
* [1 · Your decision](#1-your-decision)
* [2 · The choices you can make](#2-the-choices-you-can-make)
* [3 · If you change this later](#3-if-you-change-this-later)
* [Set up resources](#set-up-resources)
* [Lesson activity](#lesson-activity)
* [What’s next](#whats-next)
