<!-- source: https://claude.com/resources/tutorials/how-to-install-the-claude-for-small-business-plugin -->

# How to install and use the Claude for Small Business plugin

Install the plugin, see what's in it, customize it for your business, and run your first task. By the end, you'll have the plugin tailored to your business and a first task already done.

  Small Business
* Product

  Claude Cowork
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/how-to-install-the-claude-for-small-business-plugin

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The Small Business [plugin](https://claude.com/resources/tutorials/how-to-customize-plugins-in-cowork) in [Claude Cowork](https://claude.com/resources/tutorials/get-started-in-claude-cowork-in-three-steps) puts Claude to work across the tools you already use — your accounting, payments, CRM, design, contracts, email, files, and calendar. You describe the job in plain English, and Claude reads the data, does the work, and shows you the result before anything sends, posts, or pays.

> To learn more, see [Customize Claude Cowork](https://claude.com/resources/tutorials/customize-claude-cowork) and [Customizing plugins in Claude Cowork](https://claude.com/resources/tutorials/how-to-customize-plugins-in-cowork)

## Install and run the plugin

You'll need the [Claude desktop app](https://claude.com/download) on a Pro, Max, or Team plan.

1. Open **Cowork** and click **Customize** in the left sidebar.
2. Under **Plugins**, click **+**.
3. Find **Small Business** and click **Install**.

After installing the plugin, you'll have all of the [skills](https://claude.com/resources/tutorials/what-are-skills) listed below available. To tailor the plugin to your business and workflow, see the *Customize the plugin for your business* section of this guide.

#### To run a skill:

* Type `/` in the Cowork chat bar and pick it from the list, or
* Describe the job in plain English and Claude picks the skill that fits.

Either way, Claude follows the skill's instructions for that task. To learn more, see [What are skills](https://claude.com/resources/tutorials/what-are-skills) and [Use plugins in Claude Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork).

## What's in the plugin

A [plugin](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork) bundles a set of [skills](https://claude.com/resources/tutorials/what-are-skills) and the connectors they read from. Each skill is a set of instructions for a specific task. With the plugin installed, Claude already knows the steps for a range of tasks, so when you prompt for one it only has to be a few words.

Some skills in this plugin run a few of the others in sequence, asking for your decision between steps, so a bigger job is still one ask. The table lists each skill, what it does, and the tools it reads from

| Skill | What it does | Tools it uses |
| --- | --- | --- |
| Money and finance | | |
| /plan-payroll | Builds a 30-day cash forecast, ranks overdue invoices, and drafts a reminder for each one.Runs `cash-flow-snapshot` `invoice-chase` | [QuickBooks](https://claude.ai/cowork/connectors/quickbooks), [PayPal](https://claude.ai/cowork/connectors/paypal) |
| /month-heads-up | Reads the next 30 days of cash, finds your tightest week, and flags what to watch before month-end.Runs `cash-flow-snapshot` | [QuickBooks](https://claude.ai/cowork/connectors/quickbooks) |
| /close-month | Reconciles your books against your payment processor and writes the close packet for your accountant.Runs `month-end-prep` | [QuickBooks](https://claude.ai/cowork/connectors/quickbooks), [PayPal](https://claude.ai/cowork/connectors/paypal) |
| /price-check | Builds a margin-by-product table and pricing scenarios with break-even math.Runs `margin-analyzer` | [QuickBooks](https://claude.ai/cowork/connectors/quickbooks) |
| /tax-prep | Calculates quarterly estimated taxes or builds a year-end 1099 list, formatted for your accountant.Runs `tax-season-organizer` | [QuickBooks](https://claude.ai/cowork/connectors/quickbooks) |
| cash-flow-snapshot | Reads cash, invoices, bills, and incoming settlements and builds a 30/60/90-day forecast with the tight weeks flagged. | [QuickBooks](https://claude.ai/cowork/connectors/quickbooks), [PayPal](https://claude.ai/cowork/connectors/paypal) |
| invoice-chase | Ranks overdue invoices and drafts a reminder for each one, matched to how that customer has paid before. | [QuickBooks](https://claude.ai/cowork/connectors/quickbooks), [PayPal](https://claude.ai/cowork/connectors/paypal) |
| margin-analyzer | Builds a margin-by-product table and pricing scenarios with break-even math. Shows the numbers; you decide what to charge. | [QuickBooks](https://claude.ai/cowork/connectors/quickbooks), [PayPal](https://claude.ai/cowork/connectors/paypal) |
| month-end-prep | Reconciles your books against your payment processor, flags what's off, writes the close packet for your accountant. | [QuickBooks](https://claude.ai/cowork/connectors/quickbooks), [PayPal](https://claude.ai/cowork/connectors/paypal) |
| tax-season-organizer | Calculates quarterly estimated taxes or builds a year-end 1099 list, formatted for your accountant. | [QuickBooks](https://claude.ai/cowork/connectors/quickbooks), [PayPal](https://claude.ai/cowork/connectors/paypal) |
| Sales and marketing | | |
| /call-list | Scores your leads on engagement, fit, and urgency, and writes a call card for the top ones.Runs `lead-triage` | [HubSpot](https://claude.ai/cowork/connectors/hubspot) |
| /sales-brief | Ranks top and bottom sellers and drafts a content plan that pushes the winners.Runs `content-strategy` | [QuickBooks](https://claude.ai/cowork/connectors/quickbooks) or [PayPal](https://claude.ai/cowork/connectors/paypal) |
| /run-campaign | Reads your sales history, finds the slow stretch, drafts the offer, builds the assets, and stages the send.Runs `content-strategy` `canva-creator` `lead-triage` | [HubSpot](https://claude.ai/cowork/connectors/hubspot), [Canva](https://claude.ai/cowork/connectors/canva) |
| lead-triage | Scores your leads on engagement, fit, and urgency, and writes a call card for the top ones with talking points. | [HubSpot](https://claude.ai/cowork/connectors/hubspot) |
| content-strategy | Reads your sales data, finds what's selling and what isn't, and drafts a content plan that pushes the winners. | [QuickBooks](https://claude.ai/cowork/connectors/quickbooks) or [PayPal](https://claude.ai/cowork/connectors/paypal) |
| canva-creator | Builds the campaign from a brief: posting calendar, social designs, captions, and a staged email. | [Canva](https://claude.ai/cowork/connectors/canva), [HubSpot](https://claude.ai/cowork/connectors/hubspot) |
| Customers and operations | | |
| /handle-complaint | Reads a customer email, looks up their order and history, and drafts a reply matched to the situation.Runs `ticket-deflector` `customer-pulse` | [Gmail](https://claude.ai/cowork/connectors/gmail), [HubSpot](https://claude.ai/cowork/connectors/hubspot) |
| /customer-pulse-check | Reads disputes, tickets, emails, and reviews and groups them into themes with a draft response for each.Runs `customer-pulse` `ticket-deflector` | [PayPal](https://claude.ai/cowork/connectors/paypal) or [HubSpot](https://claude.ai/cowork/connectors/hubspot) |
| /crm-cleanup | Finds stale deals, duplicate contacts, and missing fields. Shows what it found before changing anything.Runs `crm-maintenance` | [HubSpot](https://claude.ai/cowork/connectors/hubspot) |
| /review-contract | Reads a contract and writes a plain-English summary, a red-flag list, and a marked-up redline.Runs `contract-review` | Uploaded file |
| ticket-deflector | Reads a customer email, looks up their order and history, and drafts a reply matched to the situation. | [PayPal](https://claude.ai/cowork/connectors/paypal), [HubSpot](https://claude.ai/cowork/connectors/hubspot), [Gmail](https://claude.ai/cowork/connectors/gmail) |
| customer-pulse | Reads disputes, tickets, emails, and reviews and groups them into themes with the most fixable problems first. | [PayPal](https://claude.ai/cowork/connectors/paypal) or [HubSpot](https://claude.ai/cowork/connectors/hubspot) |
| crm-maintenance | Finds stale deals, duplicate contacts, and missing fields. Shows what it found before changing anything. | [HubSpot](https://claude.ai/cowork/connectors/hubspot) |
| contract-review | Reads a contract and writes a plain-English summary, a red-flag list, and a marked-up redline. | Uploaded file; [Docusign](https://claude.ai/cowork/connectors/docusign) optional |
| Business intelligence | | |
| /monday-brief | One page to start the week: cash, sales trend, pipeline, this week's calendar, and what most needs you today.Runs `business-pulse` | Whatever's connected |
| /friday-brief | Revenue against last week, what sold, wins and watches.Runs `business-pulse` | [PayPal](https://claude.ai/cowork/connectors/paypal) or [HubSpot](https://claude.ai/cowork/connectors/hubspot) |
| /quarterly-review | Revenue and margin trends, customer health, opportunities, and risks, written as a narrative.Runs `business-pulse` | [QuickBooks](https://claude.ai/cowork/connectors/quickbooks) |
| business-pulse | One page: cash, sales trend, pipeline, this week's calendar, and the things that most need your attention. | Whatever's connected |
| Hiring and setup | | |
| job-post-builder | Writes a job post, a structured interview guide with a scoring rubric, and an offer letter template. | No connector required |
| smb-onboard | The setup skill. Asks about your business, helps you connect tools, and saves your context so every other skill knows it. | No connector required |

The tools listed are the defaults. When you customize the plugin, you can point a skill at the tools you actually use — a different payment processor, accounting tool, or CRM — and the skill reads from those instead.

## Customize the plugin for your business

The skills come with defaults written for a typical small business. There are two ways to make them yours.

In **Customize → Plugins**, open **Claude for Small Business** and click **Customize**. Or type the prompt yourself in the Cowork chat bar:

Customize the "smb-complete" plugin for me based on my company.

Copy

Claude asks about your business — what you do, who works with you, what's hardest right now — and rewrites the plugin's defaults to match. From then on, the skills carry your context: your industry, your team size, your priorities, the way you like things done.

As you do tasks with Claude that run these skills and see the output they produce, you can tell Claude to update any of them at any time — say what you'd like different and the change is saved. Over time the skills get more tailored to how you like things done and how you want the outputs to come out.

For the full pattern, see [How to customize plugins in Cowork](https://claude.com/resources/tutorials/how-to-customize-plugins-in-cowork).

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

For a step-by-step walkthrough of four of these — payroll, the month-end close, the Monday brief, and a campaign — see [Using Claude for your small business](https://claude.com/resources/tutorials/your-first-week-with-claude-for-small-business).

## Things to note

* **You approve before anything sends, posts, or pays** — skills draft, propose, and stage. Nothing goes out until you say so.
* **Your existing permissions hold** — Claude reads what your account in each tool can read. It can't see data you don't already have access to.
* **Anthropic doesn't train Claude on your business data** — and the permissions you've already set in your tools still apply. If an employee can't see something in QuickBooks today, they can't see it through Claude. The full policy is in the [Trust Center](https://trust.anthropic.com).
* **The big decisions stay with you** — Claude prepares the work and shows you what it found, but the calls that matter — what to charge, what to sign, what to send your accountant — are yours and your professionals' to make.
* **Some features depend on your plan in a connected tool** — generating designs or staging sends may need a higher tier in that tool. When something isn't available, the skill tells you and offers a workaround.

## Learn more

* [Introducing Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) — the launch announcement
* [Using Claude for your small business](https://claude.com/resources/tutorials/your-first-week-with-claude-for-small-business) — four workflows the plugin runs end to end
* [How to customize plugins in Cowork](https://claude.com/resources/tutorials/how-to-customize-plugins-in-cowork) — make the skills run from your context
* [What are skills](https://claude.com/resources/tutorials/what-are-skills) — how skills work in Claude
* [AI Fluency for Small Business](https://anthropic.skilljar.com/ai-fluency-for-small-businesses) — a free course on running a small business with AI

## Related tutorials

[Using Claude Cowork for your small business](/resources/tutorials/using-claude-for-your-small-business)Using Claude Cowork for your small business

Using Claude Cowork for your small business

Tutorial

[Tutorial](/resources/tutorials/using-claude-for-your-small-business)Tutorial
