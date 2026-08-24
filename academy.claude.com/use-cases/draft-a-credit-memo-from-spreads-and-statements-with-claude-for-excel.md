<!-- source: https://academy.claude.com/use-cases/draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel -->

![Draft a credit memo from spreads and statements with Claude for Excel result](https://academy.claude.com/assets/v1/draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel-n3ph4xl2.png)

## 1. Describe the task

The deal goes to committee Thursday. You've got three years of statements in the deal folder, a half-built spread in Excel, a covenant package the relationship manager sent over Friday, and a borrower that doesn't quite look like the last one you underwrote.

In Cowork, Claude pulls the borrower's filings and peer spreads through the S&P Global connector, reads your underwriting workbook from the deal folder, and tells you where the ratios trip your policy thresholds — and which assumptions in the model don't square with what's in the statements. You take that brief into Claude for Excel to update the spread and run the covenants, then open the memo template in Claude for Word. The Excel-to-Word handoff carries the conversation, so Claude already knows which ratios moved when you draft the writeup.

Claude pulls the spreads and runs the ratios; you make the credit decision.

Acme Manufacturing — $25M revolver renewal, committee Thursday. Walk me through the credit before I touch the spread.

Steps:

* Pull three years of financials and peer spreads from S&P Global
* Read the underwriting workbook in the deal folder and flag where ratios trip policy
* Tell me which assumptions in the model don't match what's in the statements
* Give me a brief I can take into Excel — cell refs, what to change, why

Show me the exceptions before I touch anything.



Open in Cowork

## 2. Give Claude context

Cowork pulls borrower data through the S&P Global connector and reads your spread from the deal folder — that's where the ratio analysis and policy check happen. Cell edits happen in Claude for Excel with the workbook open, and the conversation carries into Claude for Word so the memo draft picks up where you left off.

### Required context

Attach the deal folder with the underwriting workbook. Enable the S&P Global connector. Have the Claude for Excel and Claude for Word add-ins installed — that's where the spread updates and memo drafts happen.

![](data:image/svg+xml,%3csvg%20width='24'%20height='11'%20viewBox='0%200%2024%2011'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.55115%200.792969C5.06304%200.793105%206.9701%201.51652%206.9701%203.55469H5.4574C5.41357%203.09446%204.97109%202.17401%203.55115%202.17383C1.77581%202.17383%201.77576%203.35743%201.77576%203.55469C1.77583%203.75209%202.03857%204.67277%203.68201%204.67285C5.19434%204.67285%206.9701%205.13287%206.9701%207.30273C6.97007%208.02617%206.83743%2010.0645%203.68201%2010.0645C0.920312%2010.0643%20-0.0214425%208.0918%200.000369067%207.10547H1.64295C1.66526%207.65344%202.10464%208.74892%203.68201%208.74902C5.65388%208.74902%205.58828%207.76308%205.58826%207.30273C5.58826%206.84246%205.06332%206.05371%203.68201%206.05371C2.30072%206.05366%200.262138%205.52713%200.262088%203.55469C0.262088%201.58208%202.16996%200.792969%203.55115%200.792969ZM11.1781%200.792969C12.2301%200.793118%2013.676%201.46372%2013.6762%202.83105C13.6762%204.19842%2012.5372%205.11036%2011.9672%205.39551C12.3179%205.76815%2013.1245%206.63208%2013.5453%207.10547C13.8608%206.57946%2013.8518%205.4397%2013.808%204.93555H16.1097V6.05371H15.057C15.0043%207.15811%2014.6405%207.91617%2014.4652%208.15723L16.1097%209.86719H14.2025L13.5453%209.20898C13.2823%209.49389%2012.4404%2010.0643%2011.1781%2010.0645C9.00833%2010.0645%208.15279%208.61776%208.15271%207.30273C8.15271%206.25087%209.20472%205.28639%209.73084%204.93555C9.42394%204.69432%208.81092%203.93553%208.81092%202.83105C8.81109%201.45042%2010.1261%200.792969%2011.1781%200.792969ZM21.2377%200.924805C22.6185%200.924805%2023.9994%202.17419%2023.9994%203.68652C23.9992%205.39592%2022.7499%206.71094%2021.4349%206.71094H18.9369V9.86719H17.3588V0.924805H21.2377ZM10.5199%205.92188C10.1691%206.09741%209.46814%206.61915%209.46814%207.30273C9.46824%208.15745%2010.1919%208.88086%2011.1781%208.88086C11.967%208.88077%2012.559%208.44181%2012.7562%208.22266L10.5199%205.92188ZM18.9369%202.30566V5.26465H21.1068C21.8957%205.26455%2022.4875%204.6725%2022.4877%203.68652C22.4877%203.02903%2022.093%202.30576%2021.1068%202.30566H18.9369ZM11.1781%201.97656C10.9151%201.97656%2010.1254%202.2396%2010.1254%202.96289C10.1254%203.54151%2010.8274%204.16809%2011.1781%204.40918C11.5508%204.2337%2012.2953%203.6991%2012.2953%202.96289C12.2953%202.04264%2011.4414%201.9766%2011.1781%201.97656Z'%20fill='%23D7002B'/%3e%3c/svg%3e)

S&P Global

[Connect](https://claude.ai/desktop/directory/s-p-global)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

Deal folder

Acme spread workbook

Credit memo template

In Cowork’s chat bar:Deal folder

## 3. What Claude creates

A brief you can act on: where the borrower stands against policy, which ratios moved since last review, and the exact cells to look at when you open the spread.

**Acme Manufacturing — $25M revolver renewal, FY25 review**

**Where it stands vs. policy**

* DSCR: 1.42x — passes 1.25x minimum, down from 1.68x last review
* Funded debt / EBITDA: 3.1x — passes 3.5x ceiling, up from 2.4x
* Fixed charge coverage: 1.18x — **fails 1.20x minimum**
* Current ratio: 1.35x — passes 1.20x minimum

**2 exceptions to flag for committee**

*FCCR!D14 — Fixed charge coverage at 1.18x* Tripping the covenant by 2bp. Driver is the new equipment lease ($840K annual) that started in March; rent is now in fixed charges but the lease wasn't in the FY24 base. If you add back one quarter of pre-lease run-rate, FCCR comes to 1.23x. Your call on whether that warrants a waiver request or a covenant reset.

*Assumptions!B22 — FY26E revenue growth at 8%* Borrower's own forward guidance in the Q4 commentary is "mid-single digits, 4-6%." Your 8% is above their own range. RM notes from the site visit mention a contract with their largest customer is up for rebid in Q2 — not in the model.

**In your Excel workbook**

With the Claude for Excel add-in installed, paste this into the sidebar with the spread open:

FY25 spread done. FCCR at 1.18x fails 1.20x — driver is the equipment lease. Walk me through FCCR!D14, then build me a covenant cushion view at +/- 5% revenue and +/- 100bp on the lease assumption.

Also flag Assumptions!B22 — my 8% growth is above the 4-6% the borrower guided to. Show me what base/downside looks like at their range.

Copy prompt

Once you've signed off on the spread, open the memo template in Claude for Word. The conversation carries from Excel, so the memo draft already knows which ratios flipped and which exceptions need committee narrative.

## 4. Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Compare to last review

In Cowork, ask what's moved since the last credit cycle.

what changed vs. the FY24 review — leverage, coverage, working capital



Open in Cowork

### Pressure-test an assumption against the call

See if anything in the borrower's own commentary should move a cell.

is my 8% FY26 growth too rich? what did the borrower actually say about the pipeline in their Q4 narrative



Open in Cowork

### Build the downside case

In Claude for Excel, once you've signed off on the base.

build me a downside scenario in a new tab — revenue down 10%, gross margin down 200bp, hold opex flat. show me where covenants break

Copy prompt

## 5. Tricks, tips, and troubleshooting

### Ask Cowork for the Excel-ready brief

End your Cowork session by asking for a one-paragraph brief with the cell refs and the policy exceptions — that's what you paste into the Claude for Excel sidebar. Tighter than scrolling back through the chat.

### Click the cell reference

When Claude flags FCCR!D14 in the Excel sidebar, click it and Excel jumps to that cell. Check the formula and the inputs before you agree to change anything.

### Excel to Word carries the conversation

When you open the memo template in Claude for Word, it already knows which ratios moved and which exceptions you decided to surface. You're not re-explaining the deal — just say "draft the credit summary and the exceptions section."

### Save it as a skill

Renewal underwriting is the same loop every cycle. Once the Cowork conversation works for one deal, save it as a skill so the next renewal in the portfolio starts one click in.

## 6. Ready to try for yourself?

Try it on your next renewal. Attach the deal folder in Cowork, ask where the borrower stands against policy, and review the exceptions before anything changes.

Acme Manufacturing — $25M revolver renewal, committee Thursday. Walk me through the credit before I touch the spread.

Steps:

* Pull three years of financials and peer spreads from S&P Global
* Read the underwriting workbook in the deal folder and flag where ratios trip policy
* Tell me which assumptions in the model don't match what's in the statements
* Give me a brief I can take into Excel — cell refs, what to change, why

Show me the exceptions before I touch anything.

Try in Cowork
