<!-- source: https://academy.claude.com/use-cases/update-your-financial-model-after-earnings -->

Loading

## 1. Describe the task

The print drops after hours and the stock is moving. You've got the model in a folder somewhere, the release open in one tab, the transcript in another, and a PM meeting in the morning.

In Cowork, Claude pulls the earnings release and call transcript through the S&P Global connector, reads your model from the attached folder, and tells you where your forecast was off — and which assumptions the transcript doesn't back up. You take that brief into Claude for Excel to make the cell changes, then open the deck in Claude for PowerPoint. The Excel-to-PowerPoint handoff carries the conversation, so Claude already knows which cells you changed when you build the page.

Claude handles the data pull and the cross-referencing; you make the call on what moves.

ACME just jumped 8% after hours — what's driving this? I need to update my model and build a page for tomorrow's PM meeting.

Steps:

* Pull the earnings release and call transcript from S&P
* Read my model in the folder and flag where my forecast was off
* Tell me which assumptions the transcript doesn't support
* Give me a brief I can take into Excel — cell refs, what to change, why

Show me the flags before I touch anything.



Open in Cowork

## 2. Give Claude context

Cowork pulls earnings data through the S&P Global connector and reads your model from the attached folder — that's where the cross-referencing happens. Cell edits happen in Claude for Excel with the workbook open, and the conversation carries into Claude for PowerPoint so the deck build picks up where you left off.

### Required context

Attach your portfolio folder with the model. Enable the S&P Global connector. Have Claude for Excel and PowerPoint add-in installed — that's where the cell edits and slide builds happen.

![](data:image/svg+xml,%3csvg%20width='24'%20height='11'%20viewBox='0%200%2024%2011'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.55115%200.792969C5.06304%200.793105%206.9701%201.51652%206.9701%203.55469H5.4574C5.41357%203.09446%204.97109%202.17401%203.55115%202.17383C1.77581%202.17383%201.77576%203.35743%201.77576%203.55469C1.77583%203.75209%202.03857%204.67277%203.68201%204.67285C5.19434%204.67285%206.9701%205.13287%206.9701%207.30273C6.97007%208.02617%206.83743%2010.0645%203.68201%2010.0645C0.920312%2010.0643%20-0.0214425%208.0918%200.000369067%207.10547H1.64295C1.66526%207.65344%202.10464%208.74892%203.68201%208.74902C5.65388%208.74902%205.58828%207.76308%205.58826%207.30273C5.58826%206.84246%205.06332%206.05371%203.68201%206.05371C2.30072%206.05366%200.262138%205.52713%200.262088%203.55469C0.262088%201.58208%202.16996%200.792969%203.55115%200.792969ZM11.1781%200.792969C12.2301%200.793118%2013.676%201.46372%2013.6762%202.83105C13.6762%204.19842%2012.5372%205.11036%2011.9672%205.39551C12.3179%205.76815%2013.1245%206.63208%2013.5453%207.10547C13.8608%206.57946%2013.8518%205.4397%2013.808%204.93555H16.1097V6.05371H15.057C15.0043%207.15811%2014.6405%207.91617%2014.4652%208.15723L16.1097%209.86719H14.2025L13.5453%209.20898C13.2823%209.49389%2012.4404%2010.0643%2011.1781%2010.0645C9.00833%2010.0645%208.15279%208.61776%208.15271%207.30273C8.15271%206.25087%209.20472%205.28639%209.73084%204.93555C9.42394%204.69432%208.81092%203.93553%208.81092%202.83105C8.81109%201.45042%2010.1261%200.792969%2011.1781%200.792969ZM21.2377%200.924805C22.6185%200.924805%2023.9994%202.17419%2023.9994%203.68652C23.9992%205.39592%2022.7499%206.71094%2021.4349%206.71094H18.9369V9.86719H17.3588V0.924805H21.2377ZM10.5199%205.92188C10.1691%206.09741%209.46814%206.61915%209.46814%207.30273C9.46824%208.15745%2010.1919%208.88086%2011.1781%208.88086C11.967%208.88077%2012.559%208.44181%2012.7562%208.22266L10.5199%205.92188ZM18.9369%202.30566V5.26465H21.1068C21.8957%205.26455%2022.4875%204.6725%2022.4877%203.68652C22.4877%203.02903%2022.093%202.30576%2021.1068%202.30566H18.9369ZM11.1781%201.97656C10.9151%201.97656%2010.1254%202.2396%2010.1254%202.96289C10.1254%203.54151%2010.8274%204.16809%2011.1781%204.40918C11.5508%204.2337%2012.2953%203.6991%2012.2953%202.96289C12.2953%202.04264%2011.4414%201.9766%2011.1781%201.97656Z'%20fill='%23D7002B'/%3e%3c/svg%3e)

S&P Global

[Connect](https://claude.ai/desktop/directory/s-p-global)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

Portfolio folder

ACME valuation model

Prior PM deck

ACME valuation model

In Cowork’s chat bar:Portfolio folder

## 3. What Claude creates

A brief you can act on: what moved the stock, where your forecast was off, and the exact cells to look at when you open the workbook.

**What moved the stock — Q4 FY26**

* Revenue: $2.72B — beat $2.58B guide, $130M above your $2.61B forecast
* Adj. EPS: $2.05 — beat $1.90 Street
* Gross margin: 45.7% vs. your 42.4% implied — this is the driver

**1 assumption to review**

**Assumptions!C7 — FY28E gross margin at 43.0%**

Management didn't guide FY28 on the call. Baird asked about out-year margin durability; CFO said "2026 is an investment year, benefits build into 2027" — nothing past that. Your 60bp expansion in FY28E is your call, not theirs.

**In your Excel workbook**

With the Claude for Excel add-in installed, paste this into the sidebar with the workbook open:

Q4 print: rev $2.72B (beat), GM 45.7% vs my 42.4%.

Flag on Assumptions!C7 — FY28E GM at 43.0%, mgmt didn't guide past FY27. Walk me through C7, then build best/base/worst scenarios on the margin range.

Copy prompt

Once you've signed off on the cells, open the deck in Claude for PowerPoint. The conversation carries from Excel, so the page build already knows what changed.

## 4. Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Compare to your forecast

In Cowork, ask where the actual landed against what you had.

oh ok how does the actual number compare to what I had in my model?



Open in Cowork

### Check an assumption against the call

See if management said anything that should move a specific cell.

is my FY28 gross margin too aggressive? what did they actually say about out-year margins on the call



Open in Cowork

### Build scenarios in the workbook

In Claude for Excel, once you've signed off on the assumptions.

ok keep the 43% — build me best/base/worst around the margin range in a new Scenarios tab

Copy prompt

## 5. Tricks, tips, and troubleshooting

### Ask Cowork for the Excel-ready brief

End your Cowork session by asking for a one-paragraph brief with the cell refs — that's what you paste into the Claude for Excel sidebar. Tighter than scrolling back through the chat.

### Click the cell reference

When Claude flags Assumptions!C7 in the Excel sidebar, click it and Excel jumps to that cell. Check the number before you agree to change anything.

### Excel to PowerPoint carries the conversation

When you open the deck in Claude for PowerPoint, it already knows what you changed in Excel. You're not re-explaining the print or the thesis — just say "build me the page."

### Save it as a skill

Post-earnings is the same loop every quarter. Once the Cowork conversation works, save it as a skill so the next print starts one click in.

## 6. Ready to try for yourself?

Try it on your next earnings print. Attach your model folder in Cowork, ask what moved the stock, and review the flags before anything changes.

ACME just jumped 8% after hours — what's driving this? I need to update my model and build a page for tomorrow's PM meeting.

Steps:

* Pull the earnings release and call transcript from S&P
* Read my model in the folder and flag where my forecast was off
* Tell me which assumptions the transcript doesn't support
* Give me a brief I can take into Excel — cell refs, what to change, why

Show me the flags before I touch anything.

Try in Cowork
