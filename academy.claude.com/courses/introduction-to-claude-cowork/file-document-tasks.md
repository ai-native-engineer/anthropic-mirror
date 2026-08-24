<!-- source: https://academy.claude.com/courses/introduction-to-claude-cowork/file-document-tasks -->

Lesson 7 of 14 · Introduction to Claude CoworkSkills: Teach Claude Cowork your way

## What a skill actually is

Loading

A skill is a reusable playbook — a folder of files and resources — that teaches Claude how to do a specific kind of work the way you'd want it done. When you start a task that matches the skill, Claude loads the playbook and follows it.

Skills are automatically used during the task right when you need them. You don't have to invoke them by name; Claude notices when a task matches a skill you have installed and loads it automatically. You can also be explicit (*"use the board memo drafting skill"*) when you want to.

## What’s inside a skill

A skill is more than a long instruction. The four kinds of files a skill can include — and how they work together — are how you encode a real process well enough that Claude can run it like your team would:

* **Instructions** (the SKILL.md file). The brief that tells Claude what the skill does, when to use it, and how to do it. Write it the way you'd write a runbook for a new colleague — specific enough that they can do the work.
* **Assets.** Logos, brand templates, slide masters, fonts. The raw materials the skill uses to produce real-looking output.
* **References.** Examples of good output, style guides, clause libraries, the past work you'd hand a new teammate as the bar to match. References are how Claude learns what "good" looks like for this kind of work.
* **Scripts.** Small pieces of code Claude can run for the parts of the process that should happen the same way every time — a variance calculation, a structured comparison, a chart formatter, a doc reformatter.

A skill can use any combination of these. Some skills are just a SKILL.md file with instructions, and that's perfectly fine for some processes. Others have a SKILL.md plus a brand asset folder. Others have all four. The mix follows the work: include what needs to be included, nothing more.

Below are three examples of skills. Click through each to get a sense for their application and makeup.

Loading

This is what makes skills so useful for codifying how your team works. Cowork is a coworker that can act on your behalf — and skills are how you get it to do the work the way it should be done. The instructions tell it what to do; the assets give it the raw materials; the references show it what good looks like; the scripts let it run the repeatable parts the same way every time.

## Build a skill with Claude

The fastest way to build a skill is with Claude.

Start a new conversation in Cowork and say something like:

I want to build a skill for [the recurring process you're tired of re-explaining]. Walk me through what you need to know.



Open in Cowork

Claude will ask a few questions: what the skill should do, when it should trigger, what good output looks like, what resources it should use to inform the skill. Answer as specifically as you can — point at real examples of the work, real templates, real prior outputs. The output is a skill folder with the SKILL.md and any assets, references, and scripts the skill needs, ready to install.

Once it's installed, you can find the skill in **Customize**. If you want to make any changes to the skill, you can just provide Claude with the correction and ask it to update the skill. *"Add a step that flags any deal over $100K that slipped two stages — that always matters."* Claude updates the skill in place.

Skills work the same way inside any conversation, including conversations inside a project. So a skill you build for variance analysis will show up whenever variance analysis is the task — whether you're working in your default Cowork session or inside a specific finance project.

## Lesson reflection

Think of one process you repeat — a report you run, a format you always use, a checklist you follow. Jot it down. That's your first skill candidate. You don't need to build it now. Come back and build it with Claude when you have time.

## What’s next

Skills package your specific workflows so anyone on your team can run them and get the same quality result. Plugins bundle several skills and connectors into one installable package built around a job. That's the next lesson.
