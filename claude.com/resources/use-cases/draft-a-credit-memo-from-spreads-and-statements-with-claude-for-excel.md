<!-- source: https://claude.com/resources/use-cases/draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel -->

Finance

Cowork

Connectors

# Draft a credit memo from spreads and statements with Claude for Excel

Cowork pulls the borrower's filings and spreads through the S&P Capital IQ connector and reads the underwriting workbook from your deal folder. You take the ratios and exceptions into Claude for Excel to update the model, then bring the writeup into Claude for Word for the credit memo.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Finance
* Model

  Sonnet 4.6
* Features

  Connectors
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel

1

## Describe the task

The deal goes to committee Thursday. You've got three years of statements in the deal folder, a half-built spread in Excel, a covenant package the relationship manager sent over Friday, and a borrower that doesn't quite look like the last one you underwrote.

In Cowork, Claude pulls the borrower's filings and peer spreads through the S&P Capital IQ connector, reads your underwriting workbook from the deal folder, and tells you where the ratios trip your policy thresholds — and which assumptions in the model don't square with what's in the statements. You take that brief into Claude for Excel to update the spread and run the covenants, then open the memo template in Claude for Word. The Excel-to-Word handoff carries the conversation, so Claude already knows which ratios moved when you draft the writeup.

Claude pulls the spreads and runs the ratios; you make the credit decision.

‍

### **Prompt**

Acme Manufacturing — $25M revolver renewal, committee Thursday. Walk me through the credit before I touch the spread.

Steps:

* Pull three years of financials and peer spreads from S&P Capital IQ
* Read the underwriting workbook in the deal folder and flag where ratios trip policy
* Tell me which assumptions in the model don't match what's in the statements
* Give me a brief I can take into Excel — cell refs, what to change, why

Show me the exceptions before I touch anything.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

Cowork pulls borrower data through the S&P Capital IQ connector and reads your spread from the deal folder — that's where the ratio analysis and policy check happen. Cell edits happen in Claude for Excel with the workbook open, and the conversation carries into Claude for Word so the memo draft picks up where you left off.

## Required context

Attach the deal folder with the underwriting workbook. Enable the S&P Capital IQ connector. Have the Claude for Excel and Claude for Word add-ins installed — that's where the spread updates and memo drafts happen.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690a4a6d8eea74be27d86ad5_s%26p.svg)

S&P Global

Acme spread workbook

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

XSLX

Credit memo template

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68eff599f02e8d84f204b878_google_doc.svg)

DOC

Acme spread workbook

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

XSLX

## Optional context

Claude can run the standard underwriting loop — ratio analysis, covenant compliance, risk rating recommendation, and the formal memo draft. The Financial Analysis plugin adds DCF, comps, and stress-testing skills if you need them for the downside cases.

No items found.

3

## What Claude creates

A brief you can act on: where the borrower stands against policy, which ratios moved since last review, and the exact cells to look at when you open the spread.

‍

From Claude

**Acme Manufacturing — $25M revolver renewal, FY25 review**

**Where it stands vs. policy**

* DSCR: 1.42x — passes 1.25x minimum, down from 1.68x last review
* Funded debt / EBITDA: 3.1x — passes 3.5x ceiling, up from 2.4x
* Fixed charge coverage: 1.18x — **fails 1.20x minimum**
* Current ratio: 1.35x — passes 1.20x minimum

**2 exceptions to flag for committee**

*FCCR!D14 — Fixed charge coverage at 1.18x* Tripping the covenant by 2bp. Driver is the new equipment lease ($840K annual) that started in March; rent is now in fixed charges but the lease wasn't in the FY24 base. If you add back one quarter of pre-lease run-rate, FCCR comes to 1.23x. Your call on whether that warrants a waiver request or a covenant reset.

*Assumptions!B22 — FY26E revenue growth at 8%* Borrower's own forward guidance in the Q4 commentary is "mid-single digits, 4-6%." Your 8% is above their own range. RM notes from the site visit mention a contract with their largest customer is up for rebid in Q2 — not in the model.

‍

**In your Excel workbook**

With the Claude for Excel add-in installed, paste this into the sidebar with the spread open:

FY25 spread done. FCCR at 1.18x fails 1.20x — driver is the equipment lease. Walk me through FCCR!D14, then build me a covenant cushion view at +/- 5% revenue and +/- 100bp on the lease assumption.

Also flag Assumptions!B22 — my 8% growth is above the 4-6% the borrower guided to. Show me what base/downside looks like at their range.

‍

Once you've signed off on the spread, open the memo template in Claude for Word. The conversation carries from Excel, so the memo draft already knows which ratios flipped and which exceptions need committee narrative.

‍

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Compare to last review

In Cowork, ask what's moved since the last credit cycle.

‍

what changed vs. the FY24 review — leverage, coverage, working capital

‍

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Pressure-test an assumption against the call

See if anything in the borrower's own commentary should move a cell.

is my 8% FY26 growth too rich? what did the borrower actually say about the pipeline in their Q4 narrative

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Build the downside case

In Claude for Excel, once you've signed off on the base.

‍

build me a downside scenario in a new tab — revenue down 10%, gross margin down 200bp, hold opex flat. show me where covenants break

‍

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Ask Cowork for the Excel-ready brief

End your Cowork session by asking for a one-paragraph brief with the cell refs and the policy exceptions — that's what you paste into the Claude for Excel sidebar. Tighter than scrolling back through the chat.

### Click the cell reference

When Claude flags FCCR!D14 in the Excel sidebar, click it and Excel jumps to that cell. Check the formula and the inputs before you agree to change anything.

### Excel to Word carries the conversation

When you open the memo template in Claude for Word, it already knows which ratios moved and which exceptions you decided to surface. You're not re-explaining the deal — just say "draft the credit summary and the exceptions section."

### Save it as a skill

Renewal underwriting is the same loop every cycle. Once the Cowork conversation works for one deal, save it as a skill so the next renewal in the portfolio starts one click in.

‍

## Ready to try for yourself?

Try it on your next renewal. Attach the deal folder in Cowork, ask where the borrower stands against policy, and review the exceptions before anything changes.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69deb4db4aa7783f5f10f101_Screenshot%202026-04-14%20at%202.18.08%E2%80%AFPM.png)

Open artifact in new window

[Open artifact in new window](#)Open artifact in new window

## Related use cases

[Validate reserves and draft filing narrative with Claude for Excel](/resources/use-cases/validate-reserves-and-draft-filing-narrative-with-claude-for-excel)Validate reserves and draft filing narrative with Claude for Excel

Validate reserves and draft filing narrative with Claude for Excel

Use case

[Use case](/resources/use-cases/validate-reserves-and-draft-filing-narrative-with-claude-for-excel)Use case

[Update your financial model after earnings](/resources/use-cases/update-your-financial-model-after-earnings)Update your financial model after earnings

Update your financial model after earnings

Use case

[Use case](/resources/use-cases/update-your-financial-model-after-earnings)Use case

[Reconcile transactions across your accounts](/resources/use-cases/reconcile-transactions-across-your-accounts)Reconcile transactions across your accounts

Reconcile transactions across your accounts

Use case

[Use case](/resources/use-cases/reconcile-transactions-across-your-accounts)Use case

[Understand and extend an inherited spreadsheet](/resources/use-cases/understand-and-extend-an-inherited-spreadsheet)Understand and extend an inherited spreadsheet

Understand and extend an inherited spreadsheet

Use case

[Use case](/resources/use-cases/understand-and-extend-an-inherited-spreadsheet)Use case
