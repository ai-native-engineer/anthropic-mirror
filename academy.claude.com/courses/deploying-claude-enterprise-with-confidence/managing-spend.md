<!-- source: https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/managing-spend -->

Lesson 10 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutManaging spend

3. /[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

[Deploying Claude Enterprise with Confidence: The five decisions that shape your rollout](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence)

# Managing spend

Lesson 1010 min

In this lessonBy the end, you’ll be able to

* Explain how Claude Enterprise bills
* Use the levers that move spend without adjusting a cap
* Set your spend-governance posture: your defaults, your review cadence, and your rule for approving increases

This is still the fourth of the five decisions, Spend. You’ve set the three cap levels. Now you put them to use. Managing spend has three parts: how you’re billed, the settings that move spend before any cap is reached, and the review habit that tells you which to change. The aim is that a cap-increase request becomes a prompt to look, not an automatic yes.

## How you’re billed[](#how-youre-billed)

Under a typical Enterprise agreement, you pay a per-member platform fee plus pooled consumption measured in tokens. You can check your contract for your company’s source of truth. [Tokens(opens in new tab)](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) are the small chunks of text that Claude counts as it reads your input and writes its response. Longer prompts and longer conversations tend to cost more, and surfaces vary; agentic surfaces (Cowork and Claude Code, where Claude takes many steps on its own) do more behind the scenes than a single chat exchange, so they tend to consume more per task. If your contract is sales-assisted, that consumption bills monthly in arrears; if you’re on self-serve Enterprise, you prepay credits and usage pauses when they run out. See the help center to learn more about [how Enterprise plans are billed(opens in new tab)](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan) or Claude Academy to learn more about [tokens and embeddings(opens in new tab)](https://academy.claude.com/tutorials/tokens-and-embeddings).

What matters for this lesson: consumption, not just headcount, drives the bill, and the pool is organization-wide, so one group’s heavy month draws from everyone’s pool. Whether a group can actually run the pool down is up to the caps you set (Lesson 9): none are mandatory, and any level left uncapped is simply unlimited.

## The settings that move spend[](#the-settings-that-move-spend)

Spend caps set ceilings; these settings decide how fast your groups approach them.

* **The model default and the effort level:** Lesson 6 covered where these settings live; the spend consequence matters here. Most members never touch the picker, so if that default is the most capable model at a high effort level, it’s your most expensive configuration and the one most of your usage will run on. Setting a mid-range model as the default (organization-wide, or per role, as Lesson 6 set up) and capping the effort level a role can use for its routine work moves more spend than most cap changes.
* **Organization instructions as guidance at the point of use:** your organization instructions reach members inside the conversation, at the moment cost is incurred, rather than in a document they’d have to find. A few instructions that can help with consumption: keep answers to the short version unless the member asks for more; work from the files the task needs rather than everything attached; reserve the highest effort for work that needs it. This is soft steering that can shape Claude’s output, not a hard limit.
* **Customizations as a reuse lever:** a skill loads only when a task calls for it, which is less token-intensive than re-sharing the prompt every time, and more consistent. Projects offer something similar: their instructions and files persist for everyone the project is shared with, though that context is present in each project conversation rather than loaded on demand.
* **Member agentic usage habits:** with agentic work, a task started and left running keeps drawing from the pool even if its owner no longer manages the task. In Cowork, for example, scheduled tasks keep consuming on their cadence whether or not anyone is watching. There’s no dedicated admin control for this today. The fix is a member habit: scope the task, point it at the files that matter, and regularly review your scheduled tasks and delete the ones you no longer need — the same way you’d stop compiling a recurring report nobody reads.

## Reviewing before you raise[](#reviewing-before-you-raise)

Three habits keep spend managed instead of merely capped.

1. **Question every increase:** before you approve a request, ensure that the extra spend is justified rather than a symptom.
2. **Question every repeat, too:** a repeated raise on the same group’s cap can mean usage is growing, or it can mean the cap was set below what members actually need, which blocks real work rather than reducing underlying spend. The review’s job is to ask which is happening: adjust the settings when usage is the symptom and re-base the cap when the cap is.
3. **Review the caps on a cadence, in both directions:** which members and groups are reaching their caps, and which are underutilizing, so you can pre-empt requests instead of reacting to them and make adjustments that better balance spend across the organization.

## Reading your spend[](#reading-your-spend)

Three surfaces answer three kinds of questions, so use the one that fits.

| **Surface** | **What it answers** | **Use it for** |
| --- | --- | --- |
| The analytics dashboard | Adoption and spend trends: spend by model, top consumers, where usage is climbing | Your regular review |
| Analytics chat | Ad-hoc questions in plain language (“who spent the most this month, and on which model?”) | A one-off question that doesn’t need a report |
| The Analytics API | The same usage and cost data, pulled programmatically into your own finance tooling | Reconciliation and chargeback; a Primary Owner generates the key |

For a group-by-group read, the Analytics API breaks usage and cost down by group, and the dashboard’s Skills view filters by group; the spend CSV is per member, so join it to your group mapping for a group view of anything else. One scope note so you reach for the right tool when automating: the Analytics API reads usage, while the Spend Limits API (Lesson 9) sets per-member caps.

## Pluto’s spend governance[](#plutos-spend-governance)

Pluto set a mid-range model as the organization default and reviews the dashboard monthly. In month two, Platform hit its cap and an increase request landed; the review showed most of that spend was the most capable model running routine pull-request summaries, so Pluto lowered the default model on the Engineering role that Platform’s members hold and left the cap where it was. The next month, Platform ran under its cap with the same volume of work.

The interactive widget below plays Pluto’s month two forward: you choose the setting Pluto changes (raise the cap, change the default, or set an effort cap) and watch the next month’s spend and the cap respond.

## 1 · Your decision[](#1-your-decision)

What is your spend-governance posture: where the defaults sit, how often you review, and what happens before a cap moves?

## 2 · The choices you can make[](#2-the-choices-you-can-make)

This decision is a judgment call, not a list of options. Two calls make it: how often you review, and whether any group’s spend needs its own review on top.

1. **How often you review:** start monthly, because once the defaults are set, spend moves slowly, and a monthly pass over the analytics dashboard is enough to catch a trend while you still have levers to pull. Tighten to weekly or biweekly while the picture is still forming (e.g., during the first months of a rollout, a new surface or group coming online, a budget with no headroom, etc.) and stretch back out when the need for changes begins to plateau.
2. **Whether a regulated group needs its own review:** a regulated group whose spend needs separate oversight should have its own review and its own owners, on top of whichever cadence the rest of the organization runs.

## 3 · If you change this later[](#3-if-you-change-this-later)

The default model, the effort caps, and the review cadence are all settings you adjust as data comes in; each change applies from that point.

## Set up resources[](#set-up-resources)

When you’ve made the call, the default and effort caps live in your organization settings, the organization instructions live where you set them in Lesson 8, and the review runs off the analytics dashboard.

* **[Claude Enterprise consumption guide(opens in new tab)](https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide)**: how usage is metered, plus Analytics chat, the Analytics API, and organization instructions: the reading behind every spend review.
* **[How am I billed for my Enterprise plan?(opens in new tab)](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)**: how the bill is calculated, so a raise or a cut lands where you expect.
* **[Manage model access for your organization(opens in new tab)](https://support.claude.com/en/articles/15694740-manage-model-access-for-your-organization)**: per-role model access and effort caps, the lever behind the model-mix habit.
* **[Manage usage credits for Team and seat-based Enterprise plans(opens in new tab)](https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans)**: buying, tracking, and topping up the credit pool.

## Lesson activity[](#lesson-activity)

Write down your organization-wide default model, plus the default model and effort cap for any custom role that needs a different one, then set your organization-wide review cadence, put the first review on the calendar, and note the first three checks you’ll run when an increase request comes in. Draft the three lines you’ll add to your organization instructions, and write the member guidance, in your own voice, as the note you’ll send at rollout.

**What to bring your budget owner:** the defaults you’re proposing, the review cadence and who runs it, and the rule you’ll apply before approving any increase.

→ Record this in the work-along companion, section Lesson 10.

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

The next module, Visibility, covers what you can measure and how long conversation data is kept: the record you produce when someone asks what happened.

[Previous lessonSpend caps](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/spend-caps)[Next lessonVisibility: what you can measure](https://academy.claude.com/courses/deploying-claude-enterprise-with-confidence/visibility-what-you-can-measure)

Lesson 10 of 14 · Deploying Claude Enterprise with Confidence: The five decisions that shape your rolloutManaging spend

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

* [How you’re billed](#how-youre-billed)
* [The settings that move spend](#the-settings-that-move-spend)
* [Reviewing before you raise](#reviewing-before-you-raise)
* [Reading your spend](#reading-your-spend)
* [Pluto’s spend governance](#plutos-spend-governance)
* [1 · Your decision](#1-your-decision)
* [2 · The choices you can make](#2-the-choices-you-can-make)
* [3 · If you change this later](#3-if-you-change-this-later)
* [Set up resources](#set-up-resources)
* [Lesson activity](#lesson-activity)
* [What’s next](#whats-next)
