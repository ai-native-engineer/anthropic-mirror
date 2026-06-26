<!-- source: https://claude.com/resources/use-cases/validate-reserves-and-draft-filing-narrative-with-claude-for-excel -->

Finance

Connectors

# Validate reserves and draft filing narrative with Claude for Excel

Cowork reads your reserve workbook from the valuation folder and pulls prior filings and bulletins through the NAIC connector. You take the formula flags and reserve walk into Claude for Excel to clean the workbook, then bring the narrative into Claude for Word for the filing memo.

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

  https://claude.com/resources/use-case/validate-reserves-and-draft-filing-narrative-with-claude-for-excel

1

## Describe the task

The valuation cutoff was last Friday. You’ve got the reserve workbook with five tabs of triangles, the prior-year filing memo open in another window, the appointed actuary asking about IBNR movement, and the state filing due in two weeks.

In Cowork, Claude reads your reserve workbook from the valuation folder, pulls your prior filings and the latest state bulletins through the NAIC connector, and tells you where the development factors look off — and which formulas reference the wrong roll-forward column. You take the flags into Claude for Excel to fix the workbook, then open the filing memo in Claude for Word. The Excel-to-Word handoff carries the conversation, so the narrative draft already knows which reserve segments moved and why.

Claude validates the formulas and flags the anomalies; you sign off on the reserves.

Q1 reserve review for Personal Auto BI — appointed actuary review next week, filing due in two. Walk me through the workbook before I lock the numbers.

Steps:

* Read the reserve workbook in the valuation folder and validate the formulas
* Pull the FY24 filing and any new bulletins from NAIC
* Flag development factors and tail assumptions that look off vs. prior
* Give me a brief I can take into Excel — sheet refs, what's broken, what's just a movement to explain

Show me the flags before I touch anything.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

Cowork reads the reserve workbook from the attached folder and pulls historical filings through the NAIC connector — that's where the formula validation and prior-period comparison happen. Workbook fixes happen in Claude for Excel with the file open, and the conversation carries into Claude for Word so the filing narrative picks up where you left off.

## Required context

Attach the valuation folder with the reserve workbook. Enable the NAIC connector. Have the Claude for Excel and Claude for Word add-ins installed — that's where the workbook fixes and filing narrative happen.

No items found.

Q1 reserve workbook (Personal Auto BI)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

XSLX

Prior-year filing memo

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68eff599f02e8d84f204b878_google_doc.svg)

DOC

Q1 reserve workbook (Personal Auto BI)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

XSLX

## Optional context

Claude can run the standard reserve validation loop — formula audit, link-checking across triangles and roll-forward, anomaly detection on development factors, and the filing narrative draft. The Financial Analysis plugin adds scenario and stress-testing skills if you need them for sensitivity exhibits.

No items found.

3

## What Claude creates

A brief you can act on: where the workbook is broken, where the reserves moved, and the exact cells to look at when you open the file.

From Claude

**Personal Auto BI — Q1 reserve review**

**Reserve walk vs. Q4 prior**

* Ultimate losses: $487.2M — up $6.4M from $480.8M
* Case reserves: $142.1M — down $3.2M
* IBNR: $89.6M — up $9.6M
* Paid-to-date: $255.5M — up $11.2M (in line with expected)

**3 formula issues to fix**

*Triangles!K47 — Hard-coded 0.987 development factor* The 24-36 month link ratio for AY 2022 is hard-coded. Every other cell in column K pulls from the LDF table on Methodology!B14. This was probably a one-time override that didn't get reverted. The driver-derived value is 1.024 — using 0.987 understates IBNR by ~$2.1M for that accident year.

‍

*Roll-forward!E22 — References wrong column* Q1 paid-to-date for AY 2023 is pulling from the AY 2022 column. Off by $890K. The pattern in the rest of the row is correct; just this one cell drifted.

‍

*BF Method!D38 — Tail factor not flowing through* The 120-month tail factor on the input tab updated to 1.015, but the BF calculation still uses the prior 1.012. Three references didn't get linked when the tail tab was rebuilt last quarter.

‍

**1 movement to explain in the narrative**

*IBNR up $9.6M (+12%) on Personal Auto BI* Drivers: claim count emergence on AY 2024 ran 8% above expected in Q1, and the LDF refresh added ~50bp to the 12-24 month link ratio. Both are real movements, not formula issues — they just need narrative in the filing.

‍

**In your Excel workbook**

With the Claude for Excel add-in installed, paste this into the sidebar with the workbook open:

Q1 reserve review — IBNR up $9.6M, ultimate up $6.4M.

‍

Three formula fixes: Triangles!K47 (hard-coded LDF), Roll-forward!E22 (wrong column ref), BF Method!D38 (tail not flowing). Walk me through each, show me the corrected number, then re-run the reserve walk so I can see the clean ultimate.

‍

Once you've signed off on the workbook, open the filing memo in Claude for Word. The conversation carries from Excel, so the narrative already knows the IBNR movement and the LDF refresh — you just need it to draft the reserve adequacy section and the methodology change disclosure.

‍

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Pressure-test the development factors

In Cowork, ask whether the LDFs look consistent with industry data.

are my 12-24 and 24-36 link ratios in line with the industry benchmarks NAIC published last quarter for Personal Auto BI?

‍

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Run a sensitivity on the tail

In Claude for Excel, once the workbook is clean.

rebuild the tail sensitivity — show ultimate at tail factors of 1.010, 1.015, 1.020, 1.025, hold everything else constant

‍

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Draft the methodology change disclosure

In Claude for Word, once the reserves are locked.

draft the methodology change section for the filing — we updated the tail factor and added one accident year to the LDF selection window. keep it ASOP 36 compliant

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Ask Cowork for the Excel-ready brief

End your Cowork session by asking for a one-paragraph brief with the sheet refs and the formula flags — that's what you paste into the Claude for Excel sidebar. Tighter than scrolling back through the chat.

### Click the sheet reference

When Claude flags Triangles!K47 in the Excel sidebar, click it and Excel jumps to that cell. Check the formula and the surrounding pattern before you agree to change anything.

### Excel to Word carries the conversation

When you open the filing memo in Claude for Word, it already knows which formulas you fixed and which movements need narrative. You're not re-explaining the reserve walk — just say "draft the reserve adequacy section and the methodology disclosure."

### Save it as a skill

Quarterly reserve review is the same loop every cycle. Once the Cowork conversation works for one segment, save it as a skill so the next quarter's review across all your lines starts one click in.

‍

## Ready to try for yourself?

Try it on your next reserve cycle. Attach the valuation folder in Cowork, ask where the workbook needs fixing, and review the flags before anything moves.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69deb4b8db0f7637606138a2_Screenshot%202026-04-14%20at%202.17.56%E2%80%AFPM.png)

Open artifact in new window

[Open artifact in new window](#)Open artifact in new window

## Related use cases

[Draft a credit memo from spreads and statements with Claude for Excel](/resources/use-cases/draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel)Draft a credit memo from spreads and statements with Claude for Excel

Draft a credit memo from spreads and statements with Claude for Excel

Use case

[Use case](/resources/use-cases/draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel)Use case

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
