<!-- source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/one-organization-or-many -->

Lesson 4 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutOne organization or many

3. /[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

# One organization or many

Lesson 47 min

In this lessonBy the end, you’ll be able to

* Explain what a Claude organization is and what lives inside its boundary
* Decide how many organizations your company runs
* Weigh what it would cost to split or merge organizations once members are working
* Explain how members arrive in the organization you land on, through just-in-time provisioning or directory sync

This is the first of the five decisions, Structure & Identity. You’ve confirmed your prerequisites. Now you are ready to make that decision, the one every other decision sits inside: how many Claude organizations you run. First you’ll pin down what an organization is in Claude Enterprise, then you’ll actually make the call, then you’ll set up provisioning, which is how members actually arrive in the organization you land on.

## What an organization is[](#what-an-organization-is)

In Claude Enterprise, an organization is the boundary around your members, groups, settings, and data, and each contract with Anthropic creates at least one. Organizations don’t share content: projects, conversations, artifacts, and custom skills made in one aren’t reachable from another, and organization settings in one don’t apply in another. Very large deployments can run a linked parent/child structure that softens parts of this. See [the parent/child organization note(opens in new tab)](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning) for more.

From here on, “organization” refers to that boundary in Claude. The company you work for is “your company.”

## Pluto’s topology[](#plutos-topology)

Pluto has five business units but one Anthropic contract, one identity provider, and no need to keep any unit, even the regulated Payments & Trust, from the others’ data, so it runs one organization. Payments & Trust needs tighter controls than the rest, and Pluto meets that with groups and permissions inside the one organization rather than splitting it into an organization of its own.

The interactive widget below lets you set the three inputs to your company’s answers and shows how changing any one of them moves the recommendation between one organization and several.

## 1 · Your decision[](#1-your-decision)

How many Claude organizations does your company run: one, or more than one?

## 2 · The choices you can make[](#2-the-choices-you-can-make)

| **The choice** | **When you’d choose it** | **What it means and the impact it has** |
| --- | --- | --- |
| **One Claude Enterprise organization** | If none of the three situations below is true of your company. | Your controls live in one place, your groups do the internal separation, and every later decision gets made once instead of once per organization. Separate spend caps, connector settings, or a stricter posture for one unit are group-and-role work inside the one organization — not reasons to split. |
| **Several organizations, split along contract lines** | Business units need separate contracts with Anthropic, not just separate cost centers on one bill. | Run one organization per separate contract, and treat each as its own rollout: the five decisions repeat per organization. |
| **Several organizations, split along identity lines** | You run distinct identity providers (e.g., one unit on Okta and another on Microsoft Entra ID) that can’t be joined into one shared sign-in. | Same as above: one organization per identity boundary, each configured on its own. |
| **Several organizations, split along a data-isolation line** | One part of the company must be walled off from another’s data, by regulation or contract. | Same as above, with the boundary drawn where the isolation requirement is, once your compliance owner confirms an organization boundary satisfies it. |

## 3 · If you change this later[](#3-if-you-change-this-later)

Merging or splitting two organizations requires a full rebuild. Because nothing crosses the organization boundary, splitting one organization into two means standing up a second organization, sorting out domain verification across both, and re-provisioning the members who move. Merging two organizations into one runs into the same wall from the other side. Both are disruptive for the people affected, so weigh this before you commit to the change.

Adding a separate second organization later is cheaper than pulling apart one organization you consolidated too much.

## Set up resources[](#set-up-resources)

With your organization boundary set, you determine the preferred way to provision members at your organization. Both paths run through the identity provider you set up as a prerequisite. Just-in-time (JIT) provisioning creates a member the first time they sign in. Directory sync (SCIM) pushes members, and their group memberships, from your directory ahead of time. With JIT alone, groups don’t sync; you create and maintain them by hand, and the group decision in Lesson 5 reads the same either way.

Directory sync automates the group structure and provisioning, so when people change teams in the directory, Claude follows. That matters for everything after this lesson: a control is only as accurate as the membership list underneath it. If your directory is already accurate, sync keeps your Claude groups matched to it with no manual upkeep.

* **[Important considerations before enabling SSO and JIT/SCIM provisioning(opens in new tab)](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)**: what to check before you turn provisioning on, including the parent/child structure note.
* **[How SCIM sync works for Enterprise organizations(opens in new tab)](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations)**: how directory sync carries members and their group memberships into the organization.
* **[Set up JIT or SCIM provisioning(opens in new tab)](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)**: the steps for both provisioning paths.
* **[Set up single sign-on (SSO)(opens in new tab)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)**: the SSO configuration each organization needs in place before provisioning turns on.

## Lesson activity[](#lesson-activity)

Use the interactive above as your workspace: set each of the three inputs to your company’s answer and read the recommendation. Then decide your count: one organization or many, and, if many, which input draws each wall and where it goes.

If the decision isn’t yours alone (a subsidiary’s counsel, a data-residency ruling, an identity team that owns your directory), the companion section doubles as the brief you hand the owner: the three inputs above, plus where you landed, and why.

→ Record this in the work-along companion, section Lesson 4.

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

The next lesson covers what a group is, what a member gets when they belong to two groups (the union rule), and how to choose the pattern your groups follow.

[Previous lessonPrerequisites](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/prerequisites)[Next lessonYour groups](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/your-groups)

Lesson 4 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutOne organization or many

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

* [What an organization is](#what-an-organization-is)
* [Pluto’s topology](#plutos-topology)
* [1 · Your decision](#1-your-decision)
* [2 · The choices you can make](#2-the-choices-you-can-make)
* [3 · If you change this later](#3-if-you-change-this-later)
* [Set up resources](#set-up-resources)
* [Lesson activity](#lesson-activity)
* [What’s next](#whats-next)
