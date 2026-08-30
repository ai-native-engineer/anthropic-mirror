<!-- source: https://academy.claude.com/use-cases/audit-a-folder-of-visual-assets-against-your-guidelines -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Audit a folder of visual assets against your guidelines

In Claude Cowork, Claude Opus 5 can read a large folder of image exports at high resolution to spot off-brand colors, outdated logos, and missing legal copy. Point Claude at your assets folder and your brand guidelines, and get back a categorized list of violations with a confidence rating on each one.

15 minMarketingClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-dk9zo6ae.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-e548vu0j.png)

![Audit a folder of visual assets against your guidelines result](https://academy.claude.com/assets/v1/audit-a-folder-of-visual-assets-against-your-guidelines-jt2onlse.png)

## 1. Describe the task[](#1-describe-the-task)

With Claude Opus 5, any folder of images can be checked against a written set of rules — brand guidelines for marketing assets, accessibility rules for UI screenshots, a style guide for a batch of design exports.

Opus 5 reads images at high resolution (up to 2,576 pixels on the long edge), so the small details that decide a match — a hex value, a logo version, a line of legal text — come through clearly. It can hold the rules document and the images together and check one against the other across the whole folder.

Here, a folder of live marketing assets gets checked against a brand-guidelines PDF and a legal-compliance sheet.

Audit every PNG and JPG in this folder against **brand-meridian-2025-q2.pdf** and **legal-required-copy.txt**.

Flag:

* the old **2024 logo**
* off-brand hex codes (**#0052B3** instead of #004B9F, **#D4AF37** instead of #C9A961)
* missing or undersized **legal copy**

Group by violation type. For each one give me **filename, issue, guideline value, asset value, and confidence**. End with how many assets passed all checks.

Open in Cowork

## 2. Give Claude context[](#2-give-claude-context)

In Claude Cowork, [point your project at the folder(opens in new tab)](https://support.claude.com/en/articles/13345190-get-started-with-cowork) that holds the brand-guidelines PDF, the legal sheet, and the asset exports.

Opus 5's high-resolution vision helps while reading small text in the guide and matching it against the same detail across hundreds of images.

### Required context[](#required-context)

* A Claude Cowork project pointed at the folder holding the brand-guidelines PDF, legal sheet, and asset exports (PNG/JPEG)

## 3. What Claude creates[](#3-what-claude-creates)

Claude reads the guide and the legal sheet, then checks every asset in the folder against them. You get a grouped violation list (filename, issue, guideline vs asset value, confidence per item), a compliant count, and a short "less certain" block for the items worth opening yourself.

Audited 200 PNG/JPG files against **brand-meridian-2025-q2.pdf** and **legal-required-copy.txt**.

**Logo & lockup** — 3 violations

* q1-social-tile-14.png · 2024 logo still in use · high
* partner-onepager-emea.pdf · clear space 8px (min is 20px) · high
* product-hero.png · tagline reads "Better Decisions" (approved: "Always On") · high

**Color** — 2 violations

* email-header-march.png · banner is #0052B3 (guide: #004B9F) · high
* social-tile-feb.png · gold reads close to #D4AF37 (guide: #C9A961) · medium — estimated from tone, not a printed hex

**Typography** — 2 violations

* case-study-onepager.pdf · body is Helvetica (guide: Manrope) · high
* q2-email-template.html · H1 at 16pt (guide: 18pt+) · high

**Required legal copy** — 3 violations

* partner-onepager-emea.pdf · footer at 7pt (min 8pt) · high
* event-banner-sf.png · "© 2024" (should be 2025) · high
* webinar-promo-9.png · footer missing · high

**Unapproved claims** — 1 violation

* product-comparison.png · "3× faster" not in approved-claims list · high

**Compliant:** 189 assets pass all checks.

**Less certain:** the gold on social-tile-feb.png may be a JPG compression shift rather than the old hex; partner-deck-asia.pptx uses a green not in the guide, possibly an approved regional variant.

Want me to file the 10 high-confidence items as Asana tasks, or save the full report to the folder?

## 4. Follow up prompts[](#4-follow-up-prompts)

Continue the conversation with Claude to refine, expand, or explore further.

### Check the live pages where these assets appear[](#check-the-live-pages-where-these-assets-appear)

The exports are one step removed from what customers see. With [Claude in Chrome(opens in new tab)](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome), Claude can open the live pages and run the same checks against what's rendering there — catching cases where the file was fixed but the page still shows the old version.

For each high-confidence violation, open the live page listed in asset-urls.csv in Chrome and tell me whether the published version has the same issue or has already been corrected.

Open in Cowork

### File each high-confidence violation as a task[](#file-each-high-confidence-violation-as-a-task)

With [Asana(opens in new tab)](https://claude.com/connectors/asana) or [Linear(opens in new tab)](https://claude.com/connectors/linear) connected, Claude turns each finding into a task with the filename, the rule, and the fix, so the audit ends in your tracker instead of a chat.

Create an Asana task in the Brand Compliance project for every high-confidence violation, assigned to the asset owner, with the filename, the guideline, and the corrected value in the description.

Open in Cowork

### Save the audit as a skill and put it on a schedule[](#save-the-audit-as-a-skill-and-put-it-on-a-schedule)

When the rules and grouping are right, save them as a [skill(opens in new tab)](https://support.claude.com/en/articles/12512176-use-skills-in-cowork) so the check is one line. Then set that skill as a [scheduled task(opens in new tab)](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork) in Claude Cowork — every Friday, Claude runs the same audit on whatever is new in the folder and posts the result to Slack, with the rules already written down.

Save this as a skill called brand-compliance-audit, then schedule it to run every Friday at 2pm and post the summary to #brand-ops.

Open in Cowork

## 5. Tricks, tips, and troubleshooting[](#5-tricks-tips-and-troubleshooting)

### Name the deliverable and the grouping in your prompt[](#name-the-deliverable-and-the-grouping-in-your-prompt)

Tell Claude how to group the findings (Logo, Color, Legal, Claims) and what to return per item (filename, issue, guideline value, asset value, confidence). Opus 5 follows a format instruction like that closely, so you get a structured list you can act on rather than prose.

### Opus 5 reads images at high resolution; Claude Cowork is what lets it work through the whole folder[](#opus-5-reads-images-at-high-resolution-claude-cowork-is-what-lets-it-work-through-the-whole-folder)

The high-resolution reading is a property of the model. Claude Cowork is what gives the model the entire folder — assets and reference documents together — and the working context to process all 200 in one task. You'd get the same reading quality on a handful of uploads in a [claude.ai(opens in new tab)](https://claude.ai) chat with Opus 5 selected; Claude Cowork is what makes it practical at folder scale and lets you schedule it.

### Tell Claude which rules are mandatory and which are tolerable[](#tell-claude-which-rules-are-mandatory-and-which-are-tolerable)

If legal copy is non-negotiable but a hex within a few points is acceptable, say so in the prompt or the project instructions. Opus 5 will weight legal violations as high priority and near-miss colors as lower, and your output will already be sorted the way you'd triage it.

## 6. Ready to try for yourself?[](#6-ready-to-try-for-yourself)

Audit at the scale and pace your team can act on: high-confidence violations go to Asana, the items worth a second look stay in the folder, and the summary lands in Slack — from one prompt in Claude Cowork.

Audit every PNG and JPG in this folder against brand-meridian-2025-q2.pdf and legal-required-copy.txt.

Flag:

• the old 2024 logo
• off-brand hex codes (#0052B3 instead of #004B9F, #D4AF37 instead of #C9A961)
• missing or undersized legal copy

Group by violation type. For each one give me filename, issue, guideline value, asset value, and confidence. End with how many assets passed all checks.

Try in Cowork

* [1. Describe the task](#1-describe-the-task)
* [2. Give Claude context](#2-give-claude-context)
* [3. What Claude creates](#3-what-claude-creates)
* [4. Follow up prompts](#4-follow-up-prompts)
* [5. Tricks, tips, and troubleshooting](#5-tricks-tips-and-troubleshooting)
* [6. Ready to try for yourself?](#6-ready-to-try-for-yourself)
