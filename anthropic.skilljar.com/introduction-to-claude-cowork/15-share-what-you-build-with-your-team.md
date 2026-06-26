<!-- https://anthropic.skilljar.com/introduction-to-claude-cowork/485950 -->

**Estimated time:** 7 minutes

### Learning objectives

By the end of this lesson you'll be able to:

* Explain how plugins get distributed across an Enterprise organization
* Apply a few good habits for keeping a shared plugin healthy over time

---

### Scaling workflows across your team

By this point, your team has a handful of skills that have earned their place. They started as someone's personal way of working, they've been run through evals, and they hold up on more than one person's use cases.

When you want to scale those across the whole team efficiently, you bundle them into a plugin — you covered how in Lesson 8. This lesson is about the next step: getting that plugin to everyone who needs it.

### Distributing a plugin in your organization

Inside a larger company, the recommended way to share a plugin is through your organization's private marketplace — a catalog of company-approved plugins that an admin manages.

In practice, distribution is a hand-off. You bring the plugin to whoever owns the marketplace for your org — that might be a team lead, an enablement or operations owner, or IT — and they publish it. When they do, they choose how it lands for everyone else:

* Available — it appears in the company Directory and people can install it if they want it.
* Installed by default — it's already there when people open Cowork; they can turn it off.
* Required — it's installed and stays on; useful for things like compliance checks that everyone needs to run the same way.

From your teammates' seat, the plugin simply shows up in their Directory labeled as coming from your company, alongside the public Anthropic ones. They can use it and turn it off (unless it's required), but they can't edit it — updates flow from whoever maintains it.

What this looks like for *you* depends on what your admin has set up. Some organizations have a marketplace running and a clear owner to hand things to; others haven't switched it on yet. Use the interactive below to find your situation and the right next step.

Distribution paths

When you go to share your plugin in Cowork, **what you see depends on how your org has set things up**. Pick the one that matches:

It's there — I know the owner
hand-off

I'm not sure it exists yet
discovery

I'm the admin
setup

Path A

### The marketplace exists and you know who runs it

The path is already paved. Your job is a hand-off, not a setup.

Your next step

Bring your plugin to the **marketplace owner** — team lead, enablement, or IT. Tell them who it's for and how it should land. They'll pick one of the install levels below when they publish.

Available

In the Directory for anyone who wants it. Right for most team plugins.

Installed by default

Already on when teammates open Cowork; they can switch it off.

Required

On and stays on. Reserve for compliance or must-run-the-same-way work.

Hidden

In the marketplace but not shown in the Directory — for staging or restricted rollouts.

Once it's published, your teammates see it in their Directory labeled as coming from your company. **Your updates flow to them automatically.**

Path B

### You're not sure the marketplace is set up

Common in orgs that just rolled out Cowork — the marketplace is an admin switch, and someone has to flip it.

Your next step

Find out **who manages Claude for your organization** — usually IT, an enablement lead, or whoever owns software tools. Ask them whether a private plugin marketplace is turned on, and who you'd hand a plugin to.

The ask, in one line: *“We've built a Cowork plugin our team wants to share — is the org marketplace turned on, and who owns it?”*  
  
Until it's live, you can still **export the plugin folder and hand it to a teammate directly** — it's just manual.

Path C

### You're the admin

Then you're the person everyone else in this lesson is looking for.

Your next step

Head to **Organization settings → Plugins** to create your private marketplace — upload a plugin directly, or connect a GitHub repo so updates sync automatically. Then set each plugin's install preference — **Available**, **Installed by default**, **Required**, or **Hidden** — org-wide or per group.

The full admin walkthrough lives in the help center: *Manage Claude Cowork plugins for your organization*. Group-level targeting, share-event audit logs, and the rest of the admin controls are beyond what an individual contributor needs in this course.

Whichever path applies, the goal is the same: a skill that started on one laptop becomes something a teammate can install and run.

Match what you see in your org to the distribution path that fits — and who to talk to if the marketplace isn't live yet.

### Habits worth keeping

A short set of practices that prevent a shared plugin from quietly going stale:

* **One owner.** Every shared plugin has a named person who reviews changes, runs the evals after edits, and decides when to update or retire it.
* **Evals before every publish.** Treat the eval loop as the gate — if the cases you care about don't hold up after a change, don't push it to everyone.
* **Name skills and plugins specifically.** "meeting-prep" may collide with three other meeting-prep skills across your organization's plugins directory. "sales-customer-renewal-prep" won't.
* **Set a review rhythm.** Quarterly is a reasonable starting point to look at what's installed, what's actually getting used, and what's gone stale. Retire what nobody runs and make amendments where people have identified opportunities for improvement.

### Lesson reflection

Think about the skills you and your immediate teammates rely on most in Cowork today.

* Which two or three would be the first candidates to bundle into a team plugin?
* Who in your organization is the person you'd bring that plugin to — the one who could get it onto the marketplace?

If you don't know the answer to the second question yet, that's your real next step.

### What’s next

In the final lesson, you'll get a quick recap of the arc you've just been through and the next moves to keep the momentum going.

#### Feedback

As you progress through the course, we'd love to hear how you're using concepts from it in your work, plus any feedback you may have. Share your feedback [here](https://docs.google.com/forms/d/e/1FAIpQLScol7ZPi1cxhXy40g0AQieFbhTNQoVNm1Bvvs2gD1giMzOXHQ/viewform).

#### Acknowledgments and license

*Copyright 2026 Anthropic. All rights reserved.*
