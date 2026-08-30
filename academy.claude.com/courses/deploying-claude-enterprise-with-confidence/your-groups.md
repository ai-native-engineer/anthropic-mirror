<!-- source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/your-groups -->

Lesson 5 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutYour groups

3. /[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

# Your groups

Lesson 59 min

In this lessonBy the end, you’ll be able to

* Explain what a group is and how nearly every later control attaches to groups rather than to individual members
* Predict what a member gets when they belong to two groups, and how to restrict capabilities purposefully
* Choose the pattern your groups will follow, and know what it costs to change the mapping once members are working with Claude

This is still the first of the five decisions, Structure & Identity. You’ve set the organization boundary. Now you can move on to what goes into it: your groups and the roles they carry. Groups are the unit that nearly every later decision attaches to.

## Groups are the unit nearly every control attaches to[](#groups-are-the-unit-nearly-every-control-attaches-to)

Everything else in this module follows from what a group is and what it carries.

1. **A group is a named set of members.**

   Your identity provider already sorts your members into groups, and Claude reads them automatically from the SCIM sync. You may have anywhere from hundreds to tens of thousands of members, so configuring one member at a time doesn’t scale. Groups let you configure capabilities for many members at once instead of one at a time.
2. **One group structure spans every surface your contract covers.**

   You build a single group structure, not one per surface (e.g., Cowork or Claude Code). The role you attach to a group applies across each of Claude’s surfaces, so what that role grants in one product doesn’t have to be remade for the next.
3. **Almost every setting in the four decisions ahead attaches to a group:**

   Nearly everything you configure, you configure for a group; a handful of settings are organization-wide ceilings instead, and the lessons flag those where they come up.

If you later find yourself wanting to scope a control to a specific subset (“just these three members,” “everyone except contractors”), that’s likely the structure telling you your organization needs another group.

## How RBAC works: members, groups, roles[](#how-rbac-works-members-groups-roles)

Claude Enterprise uses role-based access control (RBAC). There are three parts to this:

* **Members:** your people.
* **Groups:** named sets of members, synced from your identity provider (IdP) over SCIM or, if you don’t sync, created by hand in Organization settings.
* **Roles:** sets of permissions you attach to a group. Every member on a custom role gets what the roles on their groups grant.

You set access by role, not member by member. To see what a member can do, review the roles on their groups. Change a role, and every member of that group changes at once.

There are three kinds of roles:

* **Admin roles (Primary Owner, Owner, Admin):** who can change settings, such as inviting members, editing caps, and viewing billing (the last two are Owner-and-above). An Admin can manage members but not billing; an Owner can take every admin action except granting or removing the Primary Owner role; the Primary Owner can take all of these actions.
* **User roles (User):** what members can do in Claude, including capabilities, model access, and which tools Claude may use on their behalf. Most of this course scopes these through custom roles (see below).
* **Custom roles:** a permission set you define when the built-in roles don’t fit. It can carry admin or user permissions.

A custom role sets four kinds of access, each of which it can hold differently from the organization-wide default:

* **Capabilities:** which features are on, for example Claude Code and Cowork.
* **Model access:** which Claude models the group can use.
* **Connector permissions:** which connectors the group reaches, and whether it can write through them.
* **Admin permissions:** for a custom admin role, which admin actions it may perform.

These take effect only for members on a custom role; members on a built-in role keep every surface, model, and connector enabled organization-wide. Setting the role to Custom, by hand or through your IdP role mapping, is part of this lesson’s hand-off.

When a member belongs to more than one group, their permissions are the union of every group’s role. If any group grants a capability, the member has it, and a narrower group cannot remove what a broader one grants. To hold a tighter boundary, put those members in their own group with its own role, and keep them out of the broad group that carries the sensitive permission.

## Pluto’s groups[](#plutos-groups)

Pluto’s group structure is the hybrid pattern: it mirrors its organization chart, one group per business unit plus a cross-unit Engineering group, everywhere except Payments & Trust, whose engineers would otherwise inherit Engineering’s broad connector access through the union. So Pluto added a dedicated payments-eng group with its own role, and its payments engineers sit there rather than in the broad Engineering group, ensuring they only obtain the permissions they need.

The interactive widget below puts one member in two of Pluto’s groups and shows what she actually gets under the union rule.

## 1 · Your decision[](#1-your-decision)

Which group pattern do your controls attach to: what are your groups, and which of the later controls (surfaces, connectors, governance, caps) does each carry?

## 2 · The choices you can make[](#2-the-choices-you-can-make)

| **The choice** | **When you’d choose it** | **What it means and the impact it has** |
| --- | --- | --- |
| **Mirror your company’s org chart** | Controls only need to vary by department rather than by risk. The shape typically already exists in your identity provider. | One Claude group per department or team. All later controls land on department lines. A risk boundary that cuts across departments has no group to attach to until you add one. |
| **Tier by risk** | A regulated function needs at least one control (usually connectors, governance, or visibility) tighter than its parent department — a boundary department groups alone can’t express. | A small number of groups that cut across departments by how sensitive the work is. Controls attach by sensitivity rather than department, so an everyday control that varies by department has no group shaped for it. |
| **Hybrid approach** | Everyday controls fit the department shape, but a boundary doesn’t fit inside any department. Companies that need a risk boundary typically end up here. | Department groups for the everyday controls, plus a dedicated group carved out where the boundary sits. Each control lands on a group shaped for it — just keep the carved-out members out of the broad group, since the union rule can’t take a permission away. |

## 3 · If you change this later[](#3-if-you-change-this-later)

The group structure itself is low stakes to change. You can add a group, rename one, or change the role attached to it. The mapping is what to treat with care: the rule that membership in an IdP group grants a role in Claude. Once a mapping is live, changing it changes access for every member it covers, and reversing it means a second mass change, not a simple undo.

## Set up resources[](#set-up-resources)

When you’ve made the call, groups and their role assignments live in Organization settings, while membership itself syncs from your identity provider.

* **[Manage groups and group spend limits on Enterprise plans(opens in new tab)](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)**: creating groups and attaching roles.
* **[Manage custom roles on Enterprise plans(opens in new tab)](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**: defining a role when the built-in ones don’t fit.
* **[Roles and permissions(opens in new tab)](https://support.claude.com/en/articles/9267276-roles-and-permissions)**: what each built-in role grants, so a group holds the role that matches the reach you intend.
* **[Set up role-based permissions on Enterprise plans(opens in new tab)](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans)**: attaching a role’s permissions to a group.
* **[How SCIM sync works for Enterprise organizations(opens in new tab)](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations)**: how synced directory groups keep membership current with no manual upkeep.

## Lesson activity[](#lesson-activity)

Sketch your groups against the union rule: list each group and what its role grants, then name the members or functions that must be tightly bounded and the dedicated group that bounds them. If you have a regulated function, confirm its members are correctly restricted.

**What to bring your identity team:** the pattern you chose, the rule that turns your IdP groups into Claude groups (plus any exception), any group whose role differs from your standard custom role, and which IdP group maps to the Custom role. If provisioning isn’t yours to run, this is the brief you hand them.

→ Record this in the work-along companion, section Lesson 5.

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

The next lesson covers which Claude surfaces you’ll grant to each group, along with how to phase that access and how the model defaults, organization-wide and per role, decide what each group runs on.

[Previous lessonOne organization or many](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/one-organization-or-many)[Next lessonSurfaces each group gets](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/surfaces-each-group-gets)

Lesson 5 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutYour groups

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

* [Groups are the unit nearly every control attaches to](#groups-are-the-unit-nearly-every-control-attaches-to)
* [How RBAC works: members, groups, roles](#how-rbac-works-members-groups-roles)
* [Pluto’s groups](#plutos-groups)
* [1 · Your decision](#1-your-decision)
* [2 · The choices you can make](#2-the-choices-you-can-make)
* [3 · If you change this later](#3-if-you-change-this-later)
* [Set up resources](#set-up-resources)
* [Lesson activity](#lesson-activity)
* [What’s next](#whats-next)
