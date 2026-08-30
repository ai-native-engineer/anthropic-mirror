<!-- source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/prerequisites -->

Lesson 3 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutPrerequisites

3. /[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

# Prerequisites

Lesson 310 min

In this lessonBy the end, you’ll be able to

* Locate the three places you’ll work from as an admin and what you’ll do in each
* Identify the different roles in a Claude Enterprise organization
* Confirm the six prerequisites your group structure depends on, and which four are must-dos before setup

You’ve named the owners and stakeholders for each decision. Before you actually make the first one, you’ll cover three areas of groundwork, taking each in turn:

1. **Where you’ll be working:** the three places you’ll administer Claude Enterprise.
2. **Who can do what:** the roles that gate every action in your organization settings.
3. **The prerequisite check:** six items to confirm before you choose a group structure, including domain claiming.

Your identity team may already have much of this in place for other systems. Your task here is to know what still needs to be in place and who owns getting it there.

## Where you’ll be working[](#where-youll-be-working)

You administer Claude Enterprise from three places. Knowing which holds what keeps you from fruitlessly hunting for settings. A fourth, Claude Code’s managed settings, belongs to your platform lead (Lesson 6).

* **Organization settings**: most of the controls in this course — groups and roles, connectors, governance, spend, and visibility. You go here to change what a group is allowed to do.
* **Your identity provider (IdP), such as Okta, Microsoft Entra ID, or equivalent: group definitions and membership**, which Claude reads through the identity sync. You go here to change who is in a group.
* **Claude Console:** API keys and developer access, run as a separate organization with its own admin model. You go here to manage API access, which the settings above don’t govern.

A common mix-up is between the first two: if your groups sync, you change membership in your identity provider and permissions in Organization settings.

## Who can do what[](#who-can-do-what)

Every member holds a role, one of the four built-in roles (Primary Owner, Owner, Admin, User) or a custom role you define, and every action in your organization settings is gated by them. The exact capabilities that sit with each built-in role shift as the product evolves. See the [Roles and permissions(opens in new tab)](https://support.claude.com/en/articles/9267276-roles-and-permissions) article for the current capability matrix. Lesson 5 covers the full role picture of User, Admin, and custom roles as part of the group design. The admin side matters now, because it determines who can actually enact the decisions this course walks through.

## The prerequisite check[](#the-prerequisite-check)

The first decision that you’ll make is Structure & Identity. This is the decision that requires the most work to change later, so you want to make sure you’re adequately prepared for it. There are six prerequisites you should have in place before you choose a group structure. Four are must-dos: three block group setup outright, and one is your insurance against locking yourself out. The other two can run in parallel.

| **Prerequisite** | **Why it matters** | **Must-do before setup?** |
| --- | --- | --- |
| At least two members are assigned the Owner role directly, not through a group; if you use IdP role mappings, they are in the group mapped to Owner before you save it | Keeps a misconfigured group sync from locking your own team out of the settings that would fix it | Yes: your lockout insurance; do it before you configure single sign-on |
| The identity provider connection is configured and single sign-on is enforced | Claude reads groups from your IdP; no connection, no sync | Yes: blocks group setup |
| The provisioning app is set up in your identity provider | This is the IdP side of the sync; without it, groups don’t push | Yes: blocks group setup |
| Your domain is verified and claiming is on | Until claiming is on, members on your domain can sign up outside your organization, where none of your controls reach them | Yes: blocks group setup |
| You have a naming convention for the Claude groups you’ll create | Easy to agree on before groups exist; renaming later just needs a resync | No: can run in parallel |
| The billing owner is identified | Needed for the contract and for the spend decisions (Lessons 9 and 10) | No: not needed until the spend decisions |

## A closer look at two prerequisites[](#a-closer-look-at-two-prerequisites)

Two of these prerequisites deserve a closer look than the table gives them — your lockout insurance and domain claiming.

Regarding lockout insurance, you should give at least two members the Owner role. Without IdP role mappings, assign them directly by name, so a group-sync error can’t take admin access away. With IdP role mappings, put those same people in the group mapped to Owner before you save the mapping. Once mappings are on, a direct assignment alone won’t restore your access; only the Primary Owner, who is never auto-removed, can.

The Primary Owner deserves special attention because it holds actions no other role can perform, and a couple of them come back later in the course. Give each admin the least-powerful role that covers their job, and keep the Primary Owner out of day-to-day admin duty. If the Primary Owner isn’t you, find out now who should hold this role.

The other prerequisite that deserves its own explanation: domain claiming. People at your company may have already been using Claude on a non-Enterprise account that they signed up for using a work email before your organization existed in Claude. Until you claim your domain, those accounts sit outside your organization, as does everything the members do in them. Verifying the domain proves you own it; claiming is the separate step that routes everyone signing in with that domain’s address into your organization. Once implemented, every future sign-up on the domain lands inside your controls. The help center’s [domain-claiming(opens in new tab)](https://support.claude.com/en/articles/14625619-claim-and-migrate-accounts-on-your-domain) and [account-migration(opens in new tab)](https://support.claude.com/en/articles/9267400-move-your-personal-claude-account-to-a-team-or-enterprise-organization) articles carry the exact steps.

Domain claiming comes last among the four must-do prerequisites for a reason: turning it on requires the groundwork before it so that everyone on the domain has a way to sign in once their account moves:

* Your domain is verified
* Organization creation on it is restricted
* Single sign-on is enforced (not just configured)
* Provisioning is live

A few callouts to note before you turn claiming on:

* **It cannot be reversed.**
* Members who already hold a personal account on your domain get a 30-day migration window, starting when you initiate the claim.
* Each of them chooses between bringing their existing conversations and projects into a new account in your organization, or starting fresh. Either way, custom skills don’t transfer in a personal-account migration, so they should export any they want to keep before migrating. Connected-app authorizations are revoked, so each app is reconnected from the new organization account, and any custom connectors re-added there, subject to your organization’s policy. Skills are potentially recoverable, though: a whole-organization Team-to-Enterprise migration retains members’ skills, which reappear once an admin re-enables them. Anyone who hasn’t chosen when the window closes gets a fresh account by default.
* The original personal account is deactivated in every case.

Your role here is to make this transition as smooth as possible: forewarn those members before you initiate, so nobody discovers the change only after their old account is gone. Consider sharing the following:

| **Message** | **What to say** |
| --- | --- |
| **What’s happening** | On [date] we’re bringing accounts on the [company] email domain into the company’s Claude organization. From that date you have a 30-day window to move your account. |
| **The choice to make** | Bring your existing conversations and projects into your new organization account, or start fresh. Either way, custom skills and connected apps won’t carry over, so save anything you rely on first. |
| **The details of the transition** | When the 30-day window closes you get a fresh account by default, and your current personal account is deactivated. |
| **What to expect** | A reminder with your deadline arrives by email and in the product. |
| **Questions** | Contact [admin or help channel] for any questions. |

## Pluto’s prerequisites[](#plutos-prerequisites)

As Pluto’s deployment team worked through the prerequisites, domain claiming was their one real hurdle: about forty members, mostly engineers, were already using Claude on Pluto’s email domain — the IT lead sent the notice above two weeks before initiating the claim — and every one of them came under Pluto’s control once claiming was on. The identity team connected single sign-on in the first week, the admin roles sit with the IT lead, and the Primary Owner role stays with the CIO, deliberately out of daily use. The identity team also stood up the provisioning app. Two directly assigned Owners and the group naming convention sit with the IT lead, and the billing owner is the CFO’s delegate.

## Set up resources[](#set-up-resources)

These articles cover the groundwork above: SSO, provisioning, the roles matrix, and domain claiming, including what your members with personal accounts will see.

* **[Claim and migrate accounts on your domain(opens in new tab)](https://support.claude.com/en/articles/14625619-claim-and-migrate-accounts-on-your-domain)**: the steps to verify and claim your domain.
* **[Respond to an Enterprise domain claim on your Claude account(opens in new tab)](https://support.claude.com/en/articles/14625626-respond-to-an-enterprise-domain-claim-on-your-claude-account)**: what your members with personal accounts see, so you can forewarn them.
* **[Move your personal Claude account to a Team or Enterprise organization(opens in new tab)](https://support.claude.com/en/articles/9267400-move-your-personal-claude-account-to-a-team-or-enterprise-organization)**: what happens to a member’s skills, connected apps, and history when they migrate.
* **[Migrate your organization from Team to Enterprise(opens in new tab)](https://support.claude.com/en/articles/13779868-migrate-your-organization-from-team-to-enterprise)**: how a whole-organization migration keeps members’ skills.
* **[Roles and permissions(opens in new tab)](https://support.claude.com/en/articles/9267276-roles-and-permissions)**: the current capability matrix for each built-in role.
* **[Set up single sign-on (SSO)(opens in new tab)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)**: configuring SSO, the setup you must enforce, not just configure, before you claim your domain.
* **[Set up JIT or SCIM provisioning(opens in new tab)](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)**: the provisioning that has to be live so everyone on your domain has a way in.

## Lesson activity[](#lesson-activity)

The interactive widget below tracks the six prerequisites: mark each in place or not yet, and copy the result into your companion.

Run down the six prerequisites and, for each, answer two questions: What is its current status, and who at your company owns getting it done? Any hard block that isn’t in place, and any prerequisite with no owner, must be resolved before you begin deciding settings.

→ Record this in the work-along companion, section Lesson 3.

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

In the next module, you will decide how many Claude Enterprise organizations you run, and design your groups.

[Previous lessonOwners and intake](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/owners-and-intake)[Next lessonOne organization or many](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/one-organization-or-many)

Lesson 3 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutPrerequisites

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

* [Where you’ll be working](#where-youll-be-working)
* [Who can do what](#who-can-do-what)
* [The prerequisite check](#the-prerequisite-check)
* [A closer look at two prerequisites](#a-closer-look-at-two-prerequisites)
* [Pluto’s prerequisites](#plutos-prerequisites)
* [Set up resources](#set-up-resources)
* [Lesson activity](#lesson-activity)
* [What’s next](#whats-next)
