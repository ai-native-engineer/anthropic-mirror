<!-- source: https://claude.com/resources/use-cases/understand-and-extend-an-inherited-spreadsheet -->

Finance

Professional

Extended Thinking

# Understand and extend an inherited spreadsheet

Understand existing formulas and structure then add new data while preserving the original logic.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Finance
* Model

  Opus 4.5
* Features

  Extended Thinking
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/understand-and-extend-an-inherited-spreadsheet

1

## Describe the task

Inherited spreadsheets carry hidden complexity—formulas referencing other formulas, assumptions buried across tabs, calculations that cascade in undocumented ways. Before extending a model, you need to understand how it works.

Claude reads your spreadsheet's formulas and any existing documentation, then explains what it finds. Claude can annotate the spreadsheet itself, adding cell comments that explain complex formulas, documenting assumptions, and flagging logic that wasn't clear before. You get both an explanation and a marked-up file you can reference later.

Once you understand the structure, Claude extends the model following the original patterns and comments any new formulas it adds.

I inherited this SaaS revenue model when Marcus left. Finance needs Q1-Q3 2026 projections by Thursday. There's a Legend tab with some basics, and a few cell comments on formulas. Can you read through those, then help me understand the rest? Specifically:

* How the four tabs connect to each other
* What the seasonality adjustment and CAC Payback formulas are actually doing
* Anything important that isn't documented

Add some visual elements so I can see the trends at a glance—data bars on the margins, or a column showing growth from baseline. And add comments explaining any complex formulas. Then extend the model through Q3 2026, following Marcus's patterns.

‍

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

Upload the spreadsheet so Claude can read formulas and trace cell references directly.

‍

## Required context

Make sure [file creation](https://support.claude.com/en/articles/11722326-creating-and-editing-documents-spreadsheets-and-presentations) is enabled in settings so Claude can produce an extended version with working formulas.   
  
Click the (+) button in the chat bar to browse through your files or, alternatively, drag and drop the spreadsheet and any additional data files you want to analyze into the chat box area.

No items found.

Revenue Model

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

XSLX

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Revenue Model

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

XSLX

## Optional context

Turn on [Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking) for Claude to develop sophisticated layouts and logic during multi-step tasks.

Extended Thinking

3

## What Claude creates

Claude explains the tab structure and hidden logic, adds sparklines to surface trends and comments to explain formulas, then extends the model. The new spreadsheet matches the original conventions so the file stays coherent.

‍

From Claude

I've read Marcus's Legend tab and cell comments. Here's the full picture.

**The color coding (from Legend):**

* Blue = hardcoded inputs you can edit
* Black = formulas calculating within the same sheet
* Green = formulas pulling from other tabs (change the source, these update)
* Yellow highlight = key assumptions to review each quarter

**What the cell comments explain:**

*Seasonality adjustment* (Customer Metrics F4): Marcus's comment: "The division normalizes out last quarter's seasonality before applying this quarter's." The formula `=E4*1.1*B$24/B$27` takes prior quarter × growth × (current season ÷ prior season). This prevents double-counting when moving from Q4's 1.15 factor to Q1's 0.88.

*CAC Payback* (P&L B26): The comment flags an important caveat: "Uses total S&M, not just direct acquisition costs." If S&M includes brand marketing, this metric looks worse than a pure CAC calculation.

**What Marcus didn't document:**

* **Average customer revenue:** The formula (Beginning + Ending)/2 \* ARPU averages customer count because customers acquired mid-quarter generate partial revenue. Not explained anywhere.
* **Headcount lag:** Actual headcount in 2025 references the prior quarter's required number, modeling hiring delay. The comment mentions the lag but not why it matters for forecasting.
* **Tax edge case:** MAX(Operating Income, 0) prevents negative taxes on losses. Easy to miss.

**What I preserved:**

* All 348 original formulas and cross-sheet references
* Legend tab and existing cell comments
* Color coding conventions throughout

**What I added:**

* Q1 2026 through Q3 2026 in columns J through L across all tabs
* Sparklines in a "Trend" column showing patterns at a glance: Line sparklines for customer counts—you can see Q4 spikes and Q1 dips clearly; Column sparklines for revenue—the varying bar heights show seasonality; Line sparklines with high/low markers on margins—spots your best and worst quarters
* "vs Q1'24" column showing growth from baseline (Total customers +100%, revenue +96%)
* Cell comments explaining undocumented patterns (revenue averaging, Q1 slowdowns, CAC methodology)
* Comments on complex formulas I extended

The sparklines show seasonality patterns—Q4 spikes, Q1 dips—without you scanning numbers. Hover over cells with red corners to see the comments. Test the model: change Enterprise churn in Assumptions and watch it cascade through all tabs.

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Create a changelog for what you modified

When you extend or modify a model, documenting what changed makes future handoffs cleaner and protects you if questions arise.

Can you create a summary of every change made to this file? List what was added, what formulas were extended, and what assumptions I should call out as new.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Update with actuals and analyze variance

The quarter closed. Now you need to replace projections with actual results and understand where the forecast diverged from reality.

Q4 2025 closed at $8.2M revenue versus the $8.5M forecast. Update the model with actuals and break down the variance—how much came from customer count versus ARPU versus churn? I need to explain the miss to leadership.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Choose Opus for complex financial models

Sonnet handles simple spreadsheets well. But inherited models with cross-sheet dependencies—where changing one assumption cascades through four tabs—benefit from Opus 4.5's deeper reasoning. The extra time per response pays off in fewer formula errors, better pattern recognition, and polished output files with working formulas, formatting, and annotations intact.

### Ask Claude to annotate the file

Cell comments travel with the spreadsheet—unlike external docs that get separated and lost. Ask Claude to add comments explaining complex formulas directly in the file, so the explanation lives where you need it.

### Add features to visualize patterns

Ask Claude to add sparklines or embed charts next to key metrics to show clear trends. You'll instantly see which quarters spike, where margins dip, how segments compare. When you present the model, stakeholders grasp the story without scanning rows.

## Ready to try for yourself?

Work from previous financial models with clear understanding and logic. Upload inherited spreadsheets and ask Claude to show you how they work so you can extend with confidence.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6924b1c3f7f87a471d60e479_Screenshot%202025-11-24%20at%2011.27.36%E2%80%AFAM.png)

Open artifact in new window

[Open artifact in new window](#)Open artifact in new window

## Related use cases

[Draft a credit memo from spreads and statements with Claude for Excel](/resources/use-cases/draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel)Draft a credit memo from spreads and statements with Claude for Excel

Draft a credit memo from spreads and statements with Claude for Excel

Use case

[Use case](/resources/use-cases/draft-a-credit-memo-from-spreads-and-statements-with-claude-for-excel)Use case

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
