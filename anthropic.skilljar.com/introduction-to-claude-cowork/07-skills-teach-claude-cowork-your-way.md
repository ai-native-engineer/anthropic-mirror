<!-- https://anthropic.skilljar.com/introduction-to-claude-cowork/444170 -->

**Estimated time:** 12 minutes

### Learning objectives

By the end of this lesson you'll be able to:

* Define a skill and explain how Claude uses one
* Recognize the four building blocks a skill can include
* Build a skill from one of your own recurring processes

---

### What a skill actually is

A skill is a reusable playbook — a folder of files and resources — that teaches Claude how to do a specific kind of work the way you'd want it done. When you start a task that matches the skill, Claude loads the playbook and follows it.

Skills are automatically used during the task right when you need them. You don't have to invoke them by name; Claude notices when a task matches a skill you have installed and loads it automatically. You can also be explicit (*"use the board memo drafting skill"*) when you want to.

### What’s inside a skill

A skill is more than a long instruction. The four kinds of files a skill can include — and how they work together — are how you encode a real process well enough that Claude can run it like your team would:

* **Instructions** (the SKILL.md file). The brief that tells Claude what the skill does, when to use it, and how to do it. Write it the way you'd write a runbook for a new colleague — specific enough that they can do the work.
* **Assets.** Logos, brand templates, slide masters, fonts. The raw materials the skill uses to produce real-looking output.
* **References.** Examples of good output, style guides, clause libraries, the past work you'd hand a new teammate as the bar to match. References are how Claude learns what "good" looks like for this kind of work.
* **Scripts.** Small pieces of code Claude can run for the parts of the process that should happen the same way every time — a variance calculation, a structured comparison, a chart formatter, a doc reformatter.

A skill can use any combination of these. Some skills are just a SKILL.md file with instructions, and that's perfectly fine for some processes. Others have a SKILL.md plus a brand asset folder. Others have all four. The mix follows the work: include what needs to be included, nothing more.

Below are three examples of skills. Click through each to get a sense for their application and makeup.

Inside a skill

A skill is a folder. **What goes inside depends on the process.** Switch between three examples:

meeting-recap

board-memo

variance-analysis

meeting-recap/

SKILL.md

board-memo/

SKILL.md


assets/

brand-template.pptx

references/

2025-Q4-board-memo.docx

2026-Q1-board-memo.docx

variance-analysis/

SKILL.md


scripts/

variance.py

Click SKILL.md in the meeting-recap folder to see what it does.

meeting-recap SKILL.md The brief

The simplest skill is just this one file — the instructions, with nothing else attached.

--- name: meeting-recap description: Write a recap after any meeting with action items ---
# Meeting recap
## When to use
After any meeting with action items.
## Format
- Decisions
- Action items (owner + date)
- Open questions
## Length
Under 150 words.

What you'd use it for Lock in the recap format once. No template, no script, no examples needed — just the rules.

board-memo SKILL.md The brief

Tells Cowork what this skill does and how to do it — written like a runbook for a new colleague.

--- name: board-memo description: Draft the monthly board memo in our house format ---
# Board memo
## When to use
Monthly close. Quarterly board prep.
## Process
1. Pull variance from the close folder 2. Section order: Variance → Forecast → Risks → Asks 3. Lead with churn-adjusted ARR

What you'd use it for Codify the unwritten rules — the section order, the question that always comes up — so Cowork doesn't have to be told them every month.

board-memo assets/ Templates & brand

The actual files Cowork reaches for — templates, brand kits, anything the deliverable needs to look like.

brand-template.pptx

What you'd use it for Put your team's slide template here and decks Cowork builds with this skill can match it.

board-memo references/ Prior work

Your two best past memos — finished work Cowork reads to match the tone, length, and structure.

2025-Q4-board-memo.docx

2026-Q1-board-memo.docx

What you'd use it for When the easiest way to describe the bar is to show it, not write it down.

variance-analysis SKILL.md The brief

Tells Cowork where the inputs live, what counts as material, and which script to run before writing it up.

--- name: variance-analysis description: Compare actuals vs plan and write up material variances ---
# Variance analysis
## Sources
Actuals: Finance/close/{YYYY-MM}/ Plan: Finance/plan/{YYYY}-plan.xlsx
## What counts as material
>5% AND >$50K. Both, not either.
## Run
1. Call scripts/variance.py 2. One paragraph per material line

What you'd use it for Put the team's definition of “material” and the write-up format here once. Every month, Cowork applies them without being re-told.

variance-analysis scripts/ Repeatable calculation

A small Python script that does the same calculation, the same way, every time. Say “run variance for May” — Cowork pulls the right files, runs the script, produces the write-up.

# scripts/variance.py
# Same calculation every month, no rounding drift.
def variance(month): actuals = read\_close(month) plan = read\_plan(month) rows = [] for line in actuals.lines: delta\_pct = (line.actual - plan[line.id]) / plan[line.id] delta\_abs = line.actual - plan[line.id] if abs(delta\_pct) > 0.05 and abs(delta\_abs) > 50\_000: rows.append((line.name, delta\_pct, delta\_abs)) return rows

What you'd use it for Pin the calculation you don't want re-derived — same numbers, same shape, every run. The write-up is the part Cowork drafts; the math is the part the script owns.

This is what makes skills so useful for codifying how your team works. Cowork is a coworker that can act on your behalf — and skills are how you get it to do the work the way it should be done. The instructions tell it what to do; the assets give it the raw materials; the references show it what good looks like; the scripts let it run the repeatable parts the same way every time.

### Build a skill with Claude

The fastest way to build a skill is with Claude.

Start a new conversation in Cowork and say something like:

> *I want to build a skill for [the recurring process you're tired of re-explaining]. Walk me through what you need to know.*

Claude will ask a few questions: what the skill should do, when it should trigger, what good output looks like, what resources it should use to inform the skill. Answer as specifically as you can — point at real examples of the work, real templates, real prior outputs. The output is a skill folder with the SKILL.md and any assets, references, and scripts the skill needs, ready to install.

Once it's installed, you can find the skill in **Customize**. If you want to make any changes to the skill, you can just provide Claude with the correction and ask it to update the skill. *"Add a step that flags any deal over $100K that slipped two stages — that always matters."* Claude updates the skill in place.

Skills work the same way inside any conversation, including conversations inside a project. So a skill you build for variance analysis will show up whenever variance analysis is the task — whether you're working in your default Cowork session or inside a specific finance project.

### Lesson reflection

Think of one process you repeat — a report you run, a format you always use, a checklist you follow. Jot it down. That's your first skill candidate. You don't need to build it now. Come back and build it with Claude when you have time.

### What’s next

Skills package your specific workflows so anyone on your team can run them and get the same quality result. Plugins bundle several skills and connectors into one installable package built around a job. That's the next lesson.

#### Feedback

As you progress through the course, we'd love to hear how you're using concepts from it in your work, plus any feedback you may have. Share your feedback [here](https://docs.google.com/forms/d/e/1FAIpQLScol7ZPi1cxhXy40g0AQieFbhTNQoVNm1Bvvs2gD1giMzOXHQ/viewform).

#### Acknowledgments and license

*Copyright 2026 Anthropic. All rights reserved.*
