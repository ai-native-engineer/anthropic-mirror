<!-- source: https://academy.claude.com/tutorials/how-to-install-the-claude-for-small-business-plugin -->

The Small Business [plugin(opens in new tab)](https://academy.claude.com/tutorials/how-to-customize-plugins-in-cowork) in [Claude Cowork(opens in new tab)](https://academy.claude.com/tutorials/get-started-in-claude-cowork-in-three-steps) puts Claude to work across the tools you already use — your accounting, payments, CRM, design, contracts, email, files, and calendar. You describe the job in plain English, and Claude reads the data, does the work, and shows you the result before anything sends, posts, or pays.

Running the plugin well is an act of delegation, in two moves: you put the job into plain words so Claude picks the right skill for it, and you stay involved while the work happens, reading what Claude stages before anything goes out. Claude works as a collaborator you direct: it brings the capability, and the intent and the judgment calls stay with you.

## Install and run the plugin

You'll need the [Claude desktop app(opens in new tab)](https://claude.com/download) on a Pro, Max, Team, or Enterprise plan.

1. Open **Cowork** and click **Customize** in the left sidebar.
2. Under **Plugins**, click **+**.
3. Find **Small Business** and click **Install**.

After installing the plugin, you'll have all of the [skills(opens in new tab)](https://academy.claude.com/tutorials/what-are-skills) listed below available. To tailor the plugin to your business and workflow, see the *Customize the plugin for your business* section of this guide.

#### To run a skill:

* Type `/` in the Cowork chat bar and pick it from the list, or
* Describe the job in plain English and Claude picks the skill that fits.

Either way, Claude follows the skill's instructions for that task. To learn more, see [What are skills(opens in new tab)](https://academy.claude.com/tutorials/what-are-skills) and [Use plugins in Claude Cowork(opens in new tab)](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork).

## What's in the plugin

A [plugin(opens in new tab)](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork) bundles a set of [skills(opens in new tab)](https://academy.claude.com/tutorials/what-are-skills) and the connectors they read from. Each skill is a set of instructions for a specific task. With the plugin installed, Claude already knows the steps for a range of tasks, so when you prompt for one it only has to be a few words.

Some skills in this plugin run a few of the others in sequence, asking for your decision between steps, so a bigger job is still one ask. The table lists each skill, what it does, and the tools it reads from

| Skill | What it does | Tools it uses |
| --- | --- | --- |
| Money and finance | | |
| `/plan-payroll` | Builds a 30-day cash forecast, ranks overdue invoices, and drafts a reminder for each one.Runs `cash-flow-snapshot` `invoice-chase` | [QuickBooks(opens in new tab)](https://claude.ai/desktop/directory/quickbooks), [PayPal(opens in new tab)](https://claude.ai/desktop/directory/paypal) |
| `/month-heads-up` | Reads the next 30 days of cash, finds your tightest week, and flags what to watch before month-end.Runs `cash-flow-snapshot` | [QuickBooks(opens in new tab)](https://claude.ai/desktop/directory/quickbooks) |
| `/close-month` | Reconciles your books against your payment processor and writes the close packet for your accountant.Runs `month-end-prep` | [QuickBooks(opens in new tab)](https://claude.ai/desktop/directory/quickbooks), [PayPal(opens in new tab)](https://claude.ai/desktop/directory/paypal) |
| `/price-check` | Builds a margin-by-product table and pricing scenarios with break-even math.Runs `margin-analyzer` | [QuickBooks(opens in new tab)](https://claude.ai/desktop/directory/quickbooks) |
| `/tax-prep` | Calculates quarterly estimated taxes or builds a year-end 1099 list, formatted for your accountant.Runs `tax-season-organizer` | [QuickBooks(opens in new tab)](https://claude.ai/desktop/directory/quickbooks) |
| `cash-flow-snapshot` | Reads cash, invoices, bills, and incoming settlements and builds a 30/60/90-day forecast with the tight weeks flagged. | [QuickBooks(opens in new tab)](https://claude.ai/desktop/directory/quickbooks), [PayPal(opens in new tab)](https://claude.ai/desktop/directory/paypal) |
| `invoice-chase` | Ranks overdue invoices and drafts a reminder for each one, matched to how that customer has paid before. | [QuickBooks(opens in new tab)](https://claude.ai/desktop/directory/quickbooks), [PayPal(opens in new tab)](https://claude.ai/desktop/directory/paypal) |
| `margin-analyzer` | Builds a margin-by-product table and pricing scenarios with break-even math. Shows the numbers; you decide what to charge. | [QuickBooks(opens in new tab)](https://claude.ai/desktop/directory/quickbooks), [PayPal(opens in new tab)](https://claude.ai/desktop/directory/paypal) |
| `month-end-prep` | Reconciles your books against your payment processor, flags what's off, writes the close packet for your accountant. | [QuickBooks(opens in new tab)](https://claude.ai/desktop/directory/quickbooks), [PayPal(opens in new tab)](https://claude.ai/desktop/directory/paypal) |
| `tax-season-organizer` | Calculates quarterly estimated taxes or builds a year-end 1099 list, formatted for your accountant. | [QuickBooks(opens in new tab)](https://claude.ai/desktop/directory/quickbooks), [PayPal(opens in new tab)](https://claude.ai/desktop/directory/paypal) |
| Sales and marketing | | |
| `/call-list` | Scores your leads on engagement, fit, and urgency, and writes a call card for the top ones.Runs `lead-triage` | [HubSpot(opens in new tab)](https://claude.ai/desktop/directory/hubspot) |
| `/sales-brief` | Ranks top and bottom sellers and drafts a content plan that pushes the winners.Runs `content-strategy` | [QuickBooks(opens in new tab)](https://claude.ai/desktop/directory/quickbooks) or [PayPal(opens in new tab)](https://claude.ai/desktop/directory/paypal) |
| `/run-campaign` | Reads your sales history, finds the slow stretch, drafts the offer, builds the assets, and stages the send.Runs `content-strategy` `canva-creator` `lead-triage` | [HubSpot(opens in new tab)](https://claude.ai/desktop/directory/hubspot), [Canva(opens in new tab)](https://claude.ai/desktop/directory/canva) |
| `lead-triage` | Scores your leads on engagement, fit, and urgency, and writes a call card for the top ones with talking points. | [HubSpot(opens in new tab)](https://claude.ai/desktop/directory/hubspot) |
| `content-strategy` | Reads your sales data, finds what's selling and what isn't, and drafts a content plan that pushes the winners. | [QuickBooks(opens in new tab)](https://claude.ai/desktop/directory/quickbooks) or [PayPal(opens in new tab)](https://claude.ai/desktop/directory/paypal) |
| `canva-creator` | Builds the campaign from a brief: posting calendar, social designs, captions, and a staged email. | [Canva(opens in new tab)](https://claude.ai/desktop/directory/canva), [HubSpot(opens in new tab)](https://claude.ai/desktop/directory/hubspot) |
| Customers and operations | | |
| `/handle-complaint` | Reads a customer email, looks up their order and history, and drafts a reply matched to the situation.Runs `ticket-deflector` `customer-pulse` | [Gmail(opens in new tab)](https://claude.ai/desktop/directory/gmail-gmailmcp), [HubSpot(opens in new tab)](https://claude.ai/desktop/directory/hubspot) |
| `/customer-pulse-check` | Reads disputes, tickets, emails, and reviews and groups them into themes with a draft response for each.Runs `customer-pulse` `ticket-deflector` | [PayPal(opens in new tab)](https://claude.ai/desktop/directory/paypal) or [HubSpot(opens in new tab)](https://claude.ai/desktop/directory/hubspot) |
| `/crm-cleanup` | Finds stale deals, duplicate contacts, and missing fields. Shows what it found before changing anything.Runs `crm-maintenance` | [HubSpot(opens in new tab)](https://claude.ai/desktop/directory/hubspot) |
| `/review-contract` | Reads a contract and writes a plain-English summary, a red-flag list, and a marked-up redline.Runs `contract-review` | Uploaded file |
| `ticket-deflector` | Reads a customer email, looks up their order and history, and drafts a reply matched to the situation. | [PayPal(opens in new tab)](https://claude.ai/desktop/directory/paypal), [HubSpot(opens in new tab)](https://claude.ai/desktop/directory/hubspot), [Gmail(opens in new tab)](https://claude.ai/desktop/directory/gmail-gmailmcp) |
| `customer-pulse` | Reads disputes, tickets, emails, and reviews and groups them into themes with the most fixable problems first. | [PayPal(opens in new tab)](https://claude.ai/desktop/directory/paypal) or [HubSpot(opens in new tab)](https://claude.ai/desktop/directory/hubspot) |
| `crm-maintenance` | Finds stale deals, duplicate contacts, and missing fields. Shows what it found before changing anything. | [HubSpot(opens in new tab)](https://claude.ai/desktop/directory/hubspot) |
| `contract-review` | Reads a contract and writes a plain-English summary, a red-flag list, and a marked-up redline. | Uploaded file; [Docusign(opens in new tab)](https://claude.ai/desktop/directory/docusign) optional |
| Business intelligence | | |
| `/monday-brief` | One page to start the week: cash, sales trend, pipeline, this week's calendar, and what most needs you today.Runs `business-pulse` | Whatever's connected |
| `/friday-brief` | Revenue against last week, what sold, wins and watches.Runs `business-pulse` | [PayPal(opens in new tab)](https://claude.ai/desktop/directory/paypal) or [HubSpot(opens in new tab)](https://claude.ai/desktop/directory/hubspot) |
| `/quarterly-review` | Revenue and margin trends, customer health, opportunities, and risks, written as a narrative.Runs `business-pulse` | [QuickBooks(opens in new tab)](https://claude.ai/desktop/directory/quickbooks) |
| `business-pulse` | One page: cash, sales trend, pipeline, this week's calendar, and the things that most need your attention. | Whatever's connected |
| Hiring and setup | | |
| `job-post-builder` | Writes a job post, a structured interview guide with a scoring rubric, and an offer letter template. | No connector required |
| `smb-onboard` | The setup skill. Asks about your business, helps you connect tools, and saves your context so every other skill knows it. | No connector required |

The tools listed are the defaults. When you customize the plugin, you can point a skill at the tools you actually use — a different payment processor, accounting tool, or CRM — and the skill reads from those instead.

## Customize the plugin for your business

The skills come with defaults written for a typical small business. There are two ways to make them yours.

In **Customize → Plugins**, open **Claude for Small Business** and click **Customize**. Or type the prompt yourself in the Cowork chat bar:

Customize the "smb-complete" plugin for me based on my company.



Open in Cowork

Claude asks about your business — what you do, who works with you, what's hardest right now — and rewrites the plugin's defaults to match. From then on, the skills carry your context: your industry, your team size, your priorities, the way you like things done.

As you do tasks with Claude that run these skills and see the output they produce, you can tell Claude to update any of them at any time — say what you'd like different and the change is saved. Over time the skills get more tailored to how you like things done and how you want the outputs to come out.

For the full pattern, see [How to customize plugins in Cowork(opens in new tab)](https://academy.claude.com/tutorials/how-to-customize-plugins-in-cowork).

## Examples to try

Pick something that's on your list this week and describe it the way you'd describe it to someone you trust to handle it. Claude reads your prompt and runs the skill that fits.

### Money and finance

* *What does cash look like for the next 60 days?*
* *Which invoices are open and which ones should I follow up on?*
* *Help me close out April and reconcile the books.*
* *What are my margins on the catering side of the business?*
* *Get my Q2 estimated taxes ready for my accountant.*

### Sales and marketing

* *Who should I call first today?*
* *What's selling and what should I push this month?*
* *June is usually a quieter month — help me plan a promo to fill it.*

### Customers and operations

* *A customer wrote about a late shipment. Help me draft a reply.*
* *What are customers saying lately, and what should I act on?*
* *Tidy up the CRM and tell me what's worth a fresh look.*
* *Walk me through this NDA before I sign it.*

### Business intelligence and hiring

* *Give me my Monday brief.*
* *How'd we do this week?*
* *Write the QBR narrative for last quarter.*
* *Help me hire a part-time bookkeeper — write the post and the interview guide.*

For a step-by-step walkthrough of four of these — payroll, the month-end close, the Monday brief, and a campaign — see [Using Claude for your small business(opens in new tab)](https://academy.claude.com/tutorials/using-claude-for-your-small-business).

### Practice: run one skill yourself

Take one job from your week, one where you already know roughly what the answer should look like, and describe it in the Cowork chat bar the way you'd hand it to a person:

Which invoices are overdue, and which ones should I follow up on first?



Open in Cowork

Swap in your own job if invoices aren't the one on your mind this week, keeping the wording plain, with no skill name. Claude picks the skill that fits. If what comes back isn't the job you meant, type `/` and choose the skill yourself.

Before you approve anything, check the result against something you already know:

* **Confirm one line against your books.** Pick a customer you know offhand and check that what the draft reminder says about them matches your records.
* **Scan the list for anything that doesn't belong.** An invoice you know was settled showing up as open is your cue to stop and sort out the mismatch before anything goes out.

The habit to keep: describe the job, let Claude pick the skill, and check the result against something you know before you approve it. It works the same for every skill in this plugin.

## Things to note

* **You approve before anything sends, posts, or pays** — skills draft, propose, and stage. Nothing goes out until you say so.
* **Your existing permissions hold** — Claude reads what your account in each tool can read. It can't see data you don't already have access to.
* **Anthropic doesn't train Claude on your business data** — and the permissions you've already set in your tools still apply. If an employee can't see something in QuickBooks today, they can't see it through Claude. The full policy is in the [Trust Center(opens in new tab)](https://trust.anthropic.com).
* **The big decisions stay with you** — Claude prepares the work and shows you what it found, but the calls that matter — what to charge, what to sign, what to send your accountant — are yours and your professionals' to make.
* **Some features depend on your plan in a connected tool** — generating designs or staging sends may need a higher tier in that tool. When something isn't available, the skill tells you and offers a workaround.

## Learn more

* [Introducing Claude for Small Business(opens in new tab)](https://www.anthropic.com/news/claude-for-small-business) — the launch announcement
* [Using Claude for your small business(opens in new tab)](https://academy.claude.com/tutorials/using-claude-for-your-small-business) — four workflows the plugin runs end to end
* [How to customize plugins in Cowork(opens in new tab)](https://academy.claude.com/tutorials/how-to-customize-plugins-in-cowork) — make the skills run from your context
* [What are skills(opens in new tab)](https://academy.claude.com/tutorials/what-are-skills) — how skills work in Claude
