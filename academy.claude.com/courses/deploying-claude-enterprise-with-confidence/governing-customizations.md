<!-- source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/governing-customizations -->

Lesson 8 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutGoverning customizations

3. /[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

# Governing customizations

Lesson 810 min

In this lessonBy the end, you’ll be able to

* Describe the customizations you govern (skills and plugins, projects, and organization instructions)
* Explain why customizations need governance and how the settings that enforce a posture work together
* Choose your governance posture, including whether one posture covers the whole organization, and recognize the signals that it doesn’t fit

This is the third of the five decisions, Governance. You’ve decided what Claude can reach. Now you’ll learn about the customizations that change how Claude works, and how those changes can cascade across your organization. Skills, shared setups, and the always-on guidance your organization gives Claude all sit here because they answer one question at different layers: how much of what one member sets up can reach others?

## User customizations and organization instructions[](#user-customizations-and-organization-instructions)

This lesson focuses on three types of customizations. The sections below unpack each one, then take up the posture (your organization’s rule for who may create, share, and scale them) that governs how far they spread.

1. **Skills and plugins**

   A [skill(opens in new tab)](https://support.claude.com/en/articles/12512176-what-are-skills) is a folder of instructions, scripts, and resources that Claude loads when a task calls for it. In practice it packages a workflow so Claude runs it the same way every time: a first-pass contract reviewer your legal team runs against its own playbook, a summary formatter that writes in your voice, or an incident postmortem in your template. With a skill, Claude already knows your conventions, so nobody re-explains them in every conversation.

   A [plugin(opens in new tab)](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) bundles skills with other components (connectors, sub-agents) so a whole toolkit installs at once; the same posture covers skills and plugins, so the rest of this lesson says “customizations” for the family. A plugin can’t give a member a connector or capability their groups don’t include; it works with what’s already there.
2. **Projects**

   A [project(opens in new tab)](https://support.claude.com/en/articles/9517075-what-are-projects) is a workspace with its own context and files, which persist for everyone working in it. Projects sharing decides whether a project one member builds can be shared with others in your organization, and how widely. Turning Public projects off keeps projects invite-only; sharing with named people or groups continues. Group-level sharing controls are in beta, so the granularity you see may differ from another organization’s; the setting itself is the posture choice.
3. **Organization instructions**

   [Organization instructions(opens in new tab)](https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide) are a block of guidance included in your members’ conversations with Claude on the surfaces that support it: your organization’s always-on context. Use it to give Claude standing facts and standing instructions: who your organization is and how it’s structured, the tone for customer-facing writing, or a rule for every session, such as citing the source document whenever Claude quotes internal material. Pluto’s version appears later in this lesson.

## Why customizations need governance[](#why-customizations-need-governance)

The ability to share customization adds real value to members’ experience of working with Claude. A skill one member builds can codify a workflow a team already runs, so it spreads in a form that is more uniform and often faster and higher quality. Members can also build workflows that didn’t exist before Claude and scale those across your organization.

The flip side is sprawl: left ungoverned, your organization could end up with tens of near-duplicate skills, untested workflows spreading to teams that assume they were reviewed, or sensitive data made accessible by sharing a project organization-wide. Governance is how you keep the spread deliberate, and deciding who you allow to make and scale customizations is the heart of it.

Governance comes down to three questions:

1. What customizations are allowed to do when they run?
2. Who can create them, and who can use them?
3. How do they move from the member who built them to everyone else?

## What customizations can do when they run[](#what-customizations-can-do-when-they-run)

What a skill is allowed to do when it runs depends on capabilities: some skills run code, some search the web, some read files. A skill only runs when the capability it needs is on, so when you enable a capability, check both toggles together: the capability and the skills your teams will rely on that need it. Skills require code execution: in Organization settings you turn on the Code execution and file creation setting as well as Skills before members can use a skill at all. Leave a capability a skill depends on switched off organization-wide and the skill your finance team wants (say, a research summarizer) won’t be available at all.

## Who can create and use them[](#who-can-create-and-use-them)

Whether members can create and use skills is an organization-wide setting. It’s one of the handful of settings that sit above your groups rather than attaching to one, though a custom role’s Create skills capability decides who can build. Distribution can attach to a group, though: a skill bundled into a plugin can be assigned to a specific group, so only that group sees it.

## How they move to everyone else[](#how-they-move-to-everyone-else)

How a skill spreads is governed by four separate distribution controls, which make up your posture:

1. **Owner provisioning**: an Owner uploads a skill and it reaches every member’s skills list, enabled by default (members can toggle it off for themselves). Only Owners can add or remove these.
2. **Skill sharing (on by default unless your organization has set a skills preference)**: members share a skill directly with specific colleagues, who can use it but not edit it.
3. **Share with groups (off by default)**: members share a skill with an entire group that has Share resources with this group on.
4. **Share with organization (off by default)**: members publish a skill to the organization directory, where anyone can find and install it. There is no in-product review step: with this on, a member can publish without review, so a reviewed-spread posture is a process you run (a reviewer approves, then an Owner provisions), not a toggle you set.

## Pluto’s governance[](#plutos-governance)

Pluto runs a split posture: members in most groups build freely and share within their group, and anything headed beyond the group goes through a named reviewer in that group; Payments & Trust runs tighter, so nothing built there is shared at all until it’s approved (approve-first), a rule Pluto enforces through its reviewer and its policy, since the sharing toggles themselves are organization-wide. Pluto’s organization instructions name Pluto, its five business units, and its house style for customer-facing writing. They read: “You are assisting Pluto, a fintech with five business units: Retail, B2B, Payments & Trust, Platform, and Ops. Customer-facing writing is plain and short, in Pluto’s house style.”

The interactive widget below follows one skill through the build-review-publish loop: switch between the postures — Pluto’s open build with reviewed spread for most groups, approve-first for Payments & Trust — and watch where the review gate sits.

## 1 · Your decision[](#1-your-decision)

Your customization posture: how freely do members create and share skills, plugins, and projects, and does one posture cover the whole organization?

## 2 · The choices you can make[](#2-the-choices-you-can-make)

There isn’t a single posture most companies share here; the posture tracks how your company already handles the tools its own people build. Three postures cover most cases:

| **The choice** | **When you’d choose it** | **What it means and the impact it has** |
| --- | --- | --- |
| **Open build, reviewed spread** | You want members to experiment and build freely, and you have a CoE or champions group that can vet what spreads beyond the builder. | Anyone can build customizations for themselves, but promoting one to the whole organization goes through a review first. Members keep experimenting freely, and with organization-wide sharing left off, nothing spreads organization-wide unreviewed. **Settings**: Skill sharing on, Share with organization off; reviewed skills go out by Owner provisioning. |
| **Centralized** | A staffed central team already owns how the tools your people build get made and scaled, and you want Claude customizations to run through it. | A staffed team builds and vets everything; members install from what is published to the organization. Everything in use meets your standards; the trade is slower spread. **Settings**: Skill sharing and Share with organization off; Owner provisioning only. |
| **Fully open** | A small or high-trust organization where members would sanity-check each other’s work anyway and formal review would only slow them down. | Anyone builds, shares, and installs; vetting is social rather than procedural. Nothing gates the spread. **Settings**: all sharing on. |

## 3 · If you change this later[](#3-if-you-change-this-later)

Posture toggles are freely reversible: change one and it applies from that point, with no undo work. The two directions aren’t equal, though. Loosening is free — allow more building and sharing, and members gain room. Tightening is the direction to be deliberate about: move to a stricter posture after members have built under a looser one, and the skills they already rely on stop spreading until each is reviewed under the new rule, so re-review the ones in heavy use first.

## Set up resources[](#set-up-resources)

When you’ve made the call, the create-and-share settings, code execution, projects sharing, and organization instructions live in Organization settings.

* **[What are skills?(opens in new tab)](https://support.claude.com/en/articles/12512176-what-are-skills)**: what a skill is and does from the member side, before you set the posture that governs them.
* **[Provision and manage skills for your organization(opens in new tab)](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization)**: creating, enabling, and governing skills, including the organization-wide toggles you turn on here.
* **[What are projects?(opens in new tab)](https://support.claude.com/en/articles/9517075-what-are-projects)**: what a project is and holds, so you can decide how far it should share.
* **[Manage project visibility and sharing(opens in new tab)](https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing)**: the project-sharing settings that live in Organization settings.
* **[Set organization instructions(opens in new tab)](https://support.claude.com/en/articles/14546867-set-organization-instructions)**: where the instructions live, who can set them, and the character limit.
* **[Claude Enterprise consumption guide(opens in new tab)](https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide)**: the organization instructions section: the standing guidance every conversation carries.
* **[Scaling workflows with Claude Cowork at your organization(opens in new tab)](https://academy.claude.com/tutorials/scaling-workflows-with-claude-cowork-at-your-organization)**: what scaled sharing looks like in practice, from the Claude tutorial library.

## Lesson activity[](#lesson-activity)

**What to bring your governance owner and your security lead**: the posture you chose, the reviewer for customizations before they spread organization-wide and for which groups, and whether code execution stays on and for whom. If the posture isn’t yours alone to set, this is the brief for them.

Before you record a posture, check it against three questions you can already answer:

1. Which of the three postures matches how your company handles the tools its own people build today, and does any regulated group need a tighter posture than the rest?
2. If your posture has a review gate, who is the reviewer, and for which groups?
3. What should your organization instructions say: the two or three lines every conversation should carry about who you are and the standards Claude should follow?

→ Record this in the work-along companion, section Lesson 8.

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

Members can now build and share within the bounds you set. The next module, Spend, turns to what that activity costs: where spend caps sit across your organization, and who owns each one when a member reaches it.

[Previous lessonConnectors](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/connectors)[Next lessonSpend caps](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/spend-caps)

Lesson 8 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutGoverning customizations

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

* [User customizations and organization instructions](#user-customizations-and-organization-instructions)
* [Why customizations need governance](#why-customizations-need-governance)
* [What customizations can do when they run](#what-customizations-can-do-when-they-run)
* [Who can create and use them](#who-can-create-and-use-them)
* [How they move to everyone else](#how-they-move-to-everyone-else)
* [Pluto’s governance](#plutos-governance)
* [1 · Your decision](#1-your-decision)
* [2 · The choices you can make](#2-the-choices-you-can-make)
* [3 · If you change this later](#3-if-you-change-this-later)
* [Set up resources](#set-up-resources)
* [Lesson activity](#lesson-activity)
* [What’s next](#whats-next)
