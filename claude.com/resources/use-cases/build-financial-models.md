<!-- source: https://claude.com/resources/use-cases/build-financial-models -->

Finance

Extended Thinking

Web Search

Connectors

# Build financial models

Create investment analyses with complete financial models, scenario planning, and risk evaluation.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Finance
* Model

  Sonnet 4.5
* Features

  Extended Thinking

  Web Search

  Connectors
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/build-financial-models

1

## Describe the task

Investment analysis means pulling data from research platforms, building financial models, and formatting to firm standards—work that can occupy analysts for days. Claude connects to your data sources and generates working models based on your deal parameters. You review the assumptions and edit directly in Excel with formulas intact, rather than building from scratch.

Tell Claude about your investment opportunity and what your partners need to see. Be specific about the deal parameters, key questions, and timeline.

I'm evaluating MediTech Solutions (healthcare SaaS) and need a complete investment analysis.

Deal structure: $75M growth equity stake at 3.6x ARR entry, exit at 7.0x in year 5. Current metrics are $50M ARR growing 35% with 18% EBITDA margin.

**Get the company financials from Daloopa** - search for MediTech Solutions and pull their historical revenue, EBITDA margins, customer metrics, and growth rates.

**Pull healthcare SaaS comparables from S&P Global** - find public companies in the sector and get their current trading multiples, growth rates, and margin profiles. I need this to validate our 7.0x exit assumption.

**Search the web for healthcare SaaS customer concentration benchmarks** - the company mentioned their top 3 customers represent about 40% of revenue and I need to know if that's typical or concerning for this sector. Also look up recent healthcare SaaS growth trends to stress-test the 35% growth assumption.

**Retrieve our IC template from Box** - search the "IC Templates" folder and use the private equity model format as the structure.

**Key questions to address**: How do returns look if growth slows to 25% or 20%? What does the customer concentration risk mean for our downside scenario? How does our 7.0x exit assumption compare to where public healthcare SaaS companies are trading today?

Create an Excel model with scenarios (base, upside, downside), sensitivity analysis on growth and exit multiple, risk assessment focusing on customer concentration, and a comps table showing where public companies trade. Use sophisticated private equity formatting with premium visual quality, an intentional color scheme, working formulas, frozen panes, and conditional formatting.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

Connect your data platforms so Claude conducts research and analysis based on current data rather than requiring manual gathering from multiple sources.

## Required context

Use [connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) to give Claude access to financial data providers. Browse through the connector library in your settings to find tools from [trusted financial partners](https://claude.com/partners/mcp).

Enable connections to [S&P Global](https://support.claude.com/en/articles/12220135-using-s-p-global-data-for-financial-analysis), [Daloopa](https://support.claude.com/en/articles/12220011-using-daloopa-for-financial-analysis), and [Box](https://claude.ai/directory/a5380429-c773-4180-b642-301418240c8c) so Claude can access your financial research stack.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690a4cbdf84c69c7e54ba46c_daloopa.svg)

Daloopa

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690a4dac0ead54d36d26dc68_box.svg)

Box

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690a4a6d8eea74be27d86ad5_s%26p.svg)

S&P Global

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

## Optional context

Turn on [Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking) for complex multi-position analysis and to produce higher-quality  workbooks with working formulas and charts.

Make sure [Web Search](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search) is enabled so Claude can incorporate current market context and historical scenario precedents.

Extended Thinking

Web Search

3

## What Claude creates

Claude pulled financials from Daloopa, analyzed healthcare SaaS comparables from S&P Capital IQ, built three-scenario projections with sensitivity analysis, and formatted the multi-sheet model to match your IC template standards.

From Claude

I've created your investment analysis model.

**Data sources used:**

* Pulled MediTech's financial history from Daloopa (verified the $50M ARR, 35% growth rate, 18% EBITDA margin)
* Retrieved 7 healthcare SaaS comparables from S&P Global (Veeva, Doximity, Health Catalyst, Phreesia, Certify, NextGen, HealthStream)
* Searched web for healthcare SaaS customer concentration norms - found 40-45% concentration in top 3 customers is common for companies at this scale, though concentration typically decreases as ARR crosses $100M
* Used the "Growth Equity Model Template v3" from your IC Templates folder in Drive

**Model structure:**

* Executive Summary - Deal parameters, three-scenario returns (Bear: 2.2x/17% IRR, Base: 3.0x/25% IRR, Bull: 4.1x/33% IRR), investment thesis, and risk overview
* Financial Model - 5-year projections with blue-text assumption cells, automatic calculations through P&L and cash flows, exit valuation at 7.0x ($225M EV, $146M cash return on $75M invested)
* Scenario Analysis - Three scenarios varying growth (25-45% range), margin expansion (18-24% EBITDA), and exit multiples (5.5-8.5x), plus IRR sensitivity table across 25 combinations
* Risk Assessment - Seven risks mapped: customer concentration (42% in top 3), CMS reimbursement changes, Epic/Cerner competition, platform scalability, key person risk, data security compliance, and market saturation. Each includes likelihood, impact, and mitigation approach
* Comps & Valuation - Public healthcare SaaS companies trading at 4.5x median ARR multiple vs. MediTech's 3.6x entry. MediTech shows 35% growth vs. peer median of 18% and Rule of 40 score of 53 vs. peer median of 28

**Customer concentration finding:** The 42% concentration matches sector norms at this revenue scale. Web research shows similar-sized healthcare SaaS companies typically see this decrease to 25-30% as they cross $100M ARR through customer base expansion.

**Exit multiple assumption:** The 7.0x exit sits above current public comps (4.5x median) but below where faster-growing peers traded 18 months ago (8-10x range). Assumes market multiples recover partially and MediTech's growth premium commands a valuation spread.

All formulas are functional. Color coding follows PE standards (blue inputs, black calculations, green cross-sheet references).

**View your financial model**

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Create the IC memo

Turn your financial model into a written investment recommendation. Claude converts the numbers and analysis into a narrative memo that explains the returns, risks, and why this deal makes sense.

Take the key insights from this model and create an investment memo. Use our standard IC template from Drive. Structure it with these sections: Deal Overview, Investment Thesis, Returns Summary, Key Risks, Recommendation.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Validate the growth assumptions

Check if your projections match reality. Claude researches how similar companies actually grew at this stage and tells you if your forecast is reasonable or too optimistic.

These growth numbers feel optimistic. Pull actual growth trajectories from similar healthcare SaaS companies—either from our portfolio or public comps. Show me year-over-year growth rates for companies that started at $50M ARR. Does our path match reality or are we being too aggressive?

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Research recent exit multiples

Use [Research](https://support.claude.com/en/articles/11088861-using-research-on-claude) to find current transaction data across multiple sources. Research takes a few minutes but delivers a thorough report with verified citations. With financial data connectors enabled, Claude can cross-reference your internal knowledge with external market data.

Find healthcare SaaS exit transactions in the last 18 months for companies in the $50-100M ARR range. What multiples did they actually achieve? How does our 7.0x exit assumption compare to recent deals, not just public trading multiples?

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Keep comps fresh with connected data

Once you connect S&P Capital IQ or Daloopa, refresh comparable company multiples without manual updates. Say: "Pull latest healthcare SaaS comps and update the valuation sheet." Your benchmarking stays current as public market multiples shift.

### Work directly in your spreadsheet with Claude

Once Claude creates your financial model, download and open the file in Excel. With [Claude for Excel](http://claude.com/claude-for-excel), you can get instant explanations of any formula, test scenarios without breaking dependencies, or trace errors to their source. Claude provides cell-level citations for every calculation.Claude for Excel is currently in beta as a research preview. [Join the waitlis](https://www.claude.com/claude-for-excel)[t](https://www.claude.com/claude-for-excel) to get access.

### **Unlock further capabilities**

In addition to the ability to connect to financial data tools, [Claude for Financial Services](https://claude.com/solutions/financial-services) adds expanded services. In addition to financial data connections, receive specialized Skills for institutional-grade analysis and frameworks, such as those for financial analysis or valuation. Also receive expert implementation support through tailored onboarding, training, and best practices.

## Ready to try for yourself?

Connect Claude to your data platforms, point to the deal you're evaluating, and receive working spreadsheets for financial analyses.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690b0cf995f40a50d10d33b8_Screenshot%202025-11-05%20at%2012.22.50%E2%80%AFAM.png)

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
