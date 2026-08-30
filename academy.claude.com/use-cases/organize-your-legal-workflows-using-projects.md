<!-- source: https://academy.claude.com/use-cases/organize-your-legal-workflows-using-projects -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Organize your legal workflows using Projects

Stop explaining your review standards for every contract. Claude Projects let you upload your playbooks once and reference them automatically across hundreds of reviews.

15 minLegalClaude.ai

Try in ClaudeCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-l0eu13eo.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-bjr745ao.png)

![Organize your legal workflows using Projects result](https://academy.claude.com/assets/v1/organize-your-legal-workflows-using-projects-hkym4oh1.png)[Open artifact](https://claude.ai/public/artifacts/b405e6c9-608b-448a-b2b8-8c8982e582ff)

## 1. Describe the task[](#1-describe-the-task)

Contract reviews at scale demand consistency, but playbooks live in shared drives and tribal knowledge stays in senior associates' heads. Projects in Claude solve this by giving you persistent context. Upload your playbook, templates, and term lists once, and Claude references them automatically in every conversation within that Project. This prompt will help you create project instructions for your team.

I'm setting up a Project for NDA reviews at our firm. We handle about 30 NDAs a week and I want Claude to reference our standard terms, flag deviations, and maintain consistency in our review comments.

I've uploaded our NDA playbook, our standard mutual NDA template, and our list of unacceptable terms. **Analyze these documents** and create an NDA Review Standards Guide that captures our voice, tone, and structure we use throughout our writing. Make this a **professional reference document** I can upload to the Project knowledge, so Claude can reference it during every review.

Then help me craft optimized **project instructions** I can paste into the custom instructions field—instructions that tell Claude to reference the standards guide and apply our approach.

Open in Claude

## 2. Give Claude context[](#2-give-claude-context)

Add your documents or connect your document storage so Claude can access your playbooks, templates, and term lists directly. The more complete your reference materials, the more accurately Claude captures your firm's standards and approach.

### Required context[](#required-context)

Upload core reference materials: At minimum, provide your review playbook or guidelines, a standard template showing your preferred language, and any lists of prohibited or flagged terms.

### Optional context[](#optional-context)

Enable Google Drive integration: Claude can pull your playbooks, templates, and term lists directly from shared drives.

Other Document connectors. If you use other document storage, you can connect [Microsoft 365(opens in new tab)](https://claude.com/connectors/microsoft-365), [Notion(opens in new tab)](https://claude.com/connectors/notion), and [Box(opens in new tab)](https://claude.com/connectors/box) accounts, or use [other connectors(opens in new tab)](https://claude.com/connectors/) to access your documentation.

Sample redlines or review comments: If you have examples of completed reviews, these help Claude learn your commenting style and severity calibrations.

## 3. What Claude creates[](#3-what-claude-creates)

Claude analyzes your reference materials, identifies patterns in your review approach, and produces two files: a standards guide for your Project knowledge and ready-to-paste custom instructions.

I've analyzed your NDA playbook, mutual template, and unacceptable terms list. Here's what I found:

**Patterns in your review approach:**

Your firm uses a direct, business-impact focused tone that's solution-oriented rather than just flagging problems. Comments follow a consistent three-part structure: issue identification, risk level, and recommendation with alternative language. Severity indicators are calibrated to actual risk, and terminology stays consistent across documents.

I've created two files for your NDA Review Project:

**1. NDA Review Standards Guide** (Word document)

A 7-page professional reference document that captures Meridian's approach, including:

* Voice and tone principles with specific examples
* Three-part comment structure with sample markup
* Severity indicator definitions and usage guidelines
* Complete standard terms reference (confidential information definition, carve-outs, survival periods, return/destruction standards)
* Unacceptable terms tables organized by Critical and High risk
* Inappropriate scope expansion flags
* Escalation triggers
* Quality standards checklist

**2. Project Instructions** (Markdown file)

Ready-to-paste custom instructions that tell Claude to reference the Standards Guide for every review, apply the three-part comment structure consistently, use correct severity indicators, flag escalation triggers explicitly, and run a quality checklist before delivering.

[Project instructions .md]

**To set up your Project:**

1. Create a new Project in Claude
2. Upload the Standards Guide to Project knowledge
3. Paste the instructions from the markdown file into the custom instructions field
4. Optionally add your standard mutual NDA template for comparison reference

Each review will now reference your standards automatically.

## 4. Follow up prompts[](#4-follow-up-prompts)

Continue the conversation with Claude to refine, expand, or explore further.

### Test the setup with a real NDA in a Project[](#test-the-setup-with-a-real-nda-in-a-project)

Create a new Project, upload the Standards Guide to the knowledge base, and paste your custom instructions into the Project settings. Upload an NDA to see how Claude applies your standards, then refine any instructions that need adjustment.

Here's an NDA we received yesterday from a potential vendor. Review it against our standards guide and flag any deviations. Format your comments the way our associates would, with risk level and recommended alternative language for each issue.

Open in Claude

### Expand to other contract types[](#expand-to-other-contract-types)

Once your NDA workflow is running, replicate the approach for other high-volume agreements.

We also review about 15 MSAs per month. I'm uploading our MSA playbook and template. Create a separate standards guide for MSA reviews following the same structure as the NDA guide, and give me project instructions I can use for a new MSA Review Project.

Open in Claude

### Create a training resource for new associates[](#create-a-training-resource-for-new-associates)

Turn your systematized approach into onboarding material.

Based on the NDA standards guide, create a training document for new associates joining the contracts team. It should explain our review philosophy, walk through the workflow, and include 3-4 annotated examples showing how we'd handle common issues. Make it something they can reference during their first few weeks.

Open in Claude

## 5. Tricks, tips, and troubleshooting[](#5-tricks-tips-and-troubleshooting)

### Start with your best-documented process[](#start-with-your-best-documented-process)

If your playbook is thorough and your templates are up to date, Claude's standards guide will be stronger. If you're working from informal tribal knowledge, consider using this as an opportunity to formalize your approach first, then have Claude systematize it.

### Teams can share Projects and their configurations[](#teams-can-share-projects-and-their-configurations)

On Team and Enterprise plans, share the Project so colleagues get the same setup. Everyone reviews against identical standards without each person configuring their own approach. When standards change, update the knowledge base once, and the change propagates to all users.

### Test with real documents before going live[](#test-with-real-documents-before-going-live)

After setup, run 3-5 already reviewed NDAs through the Project and compare Claude's output to how your actual associates handled them. Note where Claude misses nuance or applies the wrong severity level, then refine your custom instructions. Ten minutes of calibration prevents hundreds of inconsistent reviews.

### Claude can work in your file formats[](#claude-can-work-in-your-file-formats)

Legal documents typically need to stay in .docx for redlining and collaboration. Claude can analyze Word documents and produce outputs in the same format, so deliverables slot directly into your existing workflow without conversion.

### This pattern extends beyond legal work[](#this-pattern-extends-beyond-legal-work)

Marketing teams can document brand voice. Finance teams can capture reporting standards. Research teams can codify methodology. The output becomes infrastructure for consistent AI-assisted work across any domain with established practices.

## 6. Ready to try for yourself?[](#6-ready-to-try-for-yourself)

Upload your NDA playbook and get started with your first Project. Once you've calibrated the workflow, you can expand to MSAs, vendor agreements, employee contracts, and build Projects for every high-volume legal process.

I'm setting up a Project for NDA reviews at our firm. We handle about 30 NDAs a week and I want Claude to reference our standard terms, flag deviations, and maintain consistency in our review comments.

I've uploaded our NDA playbook, our standard mutual NDA template, and our list of unacceptable terms. Analyze these documents and create an NDA Review Standards Guide that captures our voice, tone, and structure we use throughout our writing. Make this a professional reference document I can upload to the Project knowledge, so Claude can reference it during every review.

Then help me craft optimized project instructions I can paste into the custom instructions field—instructions that tell Claude to reference the standards guide and apply our approach.

Try in Claude

* [1. Describe the task](#1-describe-the-task)
* [2. Give Claude context](#2-give-claude-context)
* [3. What Claude creates](#3-what-claude-creates)
* [4. Follow up prompts](#4-follow-up-prompts)
* [5. Tricks, tips, and troubleshooting](#5-tricks-tips-and-troubleshooting)
* [6. Ready to try for yourself?](#6-ready-to-try-for-yourself)
