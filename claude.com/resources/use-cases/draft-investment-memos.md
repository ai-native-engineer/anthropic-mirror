<!-- source: https://claude.com/resources/use-cases/draft-investment-memos -->

Professional

Finance

Extended Thinking

Web Search

Connectors

# Draft investment memos

Generate investment memos from platform data, formatted to match your firm's structure and requirements.

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

  https://claude.com/resources/use-case/draft-investment-memos

1

## Describe the task

Claude can connect directly to your financial tools, letting you query using natural language and receive analysis with source citations. Instead of opening multiple browser tabs to gather data, copying metrics into spreadsheets, and then formatting a Word document from scratch, you can request the complete workflow in one conversation.

Tell Claude which company you're evaluating, what metrics drive your investment decision, and what deliverable format you need.

I'm evaluating CloudBridge Technologies (ticker: CLDG) for a potential equity investment and need an initial memo for our IC meeting next week.

**Pull the data I need:** Using Daloopa, get CloudBridge's revenue, operating margins, and free cash flow for the last 12 quarters, plus their segment revenue breakdowns. Using Kensho, identify who CloudBridge lists as competitors in their SEC filings and pull revenue growth and margins for those competitors. Also get CloudBridge's key business relationships and major customers.

**Analyze this:** Calculate cloud platform segment growth versus overall company growth. Determine free cash flow conversion rate. Compare margins year-over-year. Benchmark CloudBridge against the competitors we identified. Flag customer concentration risks.

**Create a professional investment memo in Word format:** executive summary with recommendation, business overview with segment analysis, financial performance highlighting trends, competitive positioning, valuation assessment, and key risks. Use IC-ready formatting.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

Connect your data platforms so Claude produces memos with current data rather than requiring manual metric gathering from multiple sources.

## Required context

Use [connectors](https://claude.com/blog/integrations) to give Claude access to financial data providers. Browse through the connector library in your [settings](https://claude.ai/settings/connectors) to find tools from [trusted financial partners](https://claude.com/partners/mcp).

Set up connections to [Daloopa](https://claude.ai/directory/67e0ebd7-f7c3-4917-b8f9-dc8c8cdcce13) for SEC filings and fundamental data, and [S&P Global](https://claude.ai/directory/d965405c-3467-4046-b5b3-e8fb8ed235eb) for market intelligence and competitor analysis.

This workflow uses capabilities available to [Claude for Enterprise](https://claude.com/blog/claude-for-enterprise) customers. Financial data connectors may require existing subscriptions or licenses with the underlying providers.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690a4cbdf84c69c7e54ba46c_daloopa.svg)

Daloopa

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690a4a6d8eea74be27d86ad5_s%26p.svg)

S&P Global

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

## Optional context

In the chat settings, make sure  [Web Search](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search) is turned on for additional context on the company you are evaluating.

Enable [Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking) for better synthesis when combining data from multiple platforms and creating higher-quality document outputs.

Web Search

Extended Thinking

3

## What Claude creates

Claude pulls data from Daloopa and S&P Global, calculates growth rates and margins, compares performance across competitors, and generates a professional Word document ready for investment committee review.

From Claude

Perfect! I've retrieved the financial data and created your investment memo:

**Data Retrieved:**

* CloudBridge quarterly data: Revenue grew from $1.8B to $2.8B over 12 quarters, operating margins expanded from 37.5% to 41.2%, free cash flow increased from $610M to $915M
* Segment breakdown: Cloud Platform Services (58% of revenue, 34% growth), Developer Tools (28%, 18% growth), Professional Services (14%, 12% growth)
* Competitors from SEC filings: DataFlow Inc. and SkyLink Corp.
* Competitive data: DataFlow growing 19% at 36% margins, SkyLink growing 15% at 28% margins
* Business relationships: 8 major customers totaling 22% of cloud revenue, largest customer at 5%

**Analysis:**

* Cloud Platform segment growing 34% versus 27% overall company growth—driving mix improvement
* Free cash flow conversion at 33% margin demonstrates capital efficiency
* Margins expanded 380 basis points YoY, outpacing peers by 5-13 percentage points
* CloudBridge maintains strongest growth and margin profile among enterprise infrastructure competitors
* Customer concentration moderate and declining—no single-customer dependency risk

**Investment Memo:**

View your memo

The document includes executive summary with BUY recommendation and $165 target (28% upside), business overview analyzing segment performance, financial highlights showing margin expansion and cash generation, competitive benchmarking table, valuation using three methodologies, and risk assessment with mitigating factors. Formatted for IC presentation with professional typography and clear visual hierarchy.

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Show source citations for verification

Get specific platform references and data points for every claim in the memo. Claude can trace every number and claim back to its source, showing you exactly where each piece of information came from.

Cite the exact source for each metric—I need to see platform name, date pulled, and which filing or transcript. Show me where the Q3 revenue number came from, which analyst report supports the margin expansion claim, and the specific competitor data points.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Expand on the valuation methodology

Add detailed calculations and assumptions to support your price target. Claude shows the underlying math and how your valuation changes under different scenarios.

Show me the DCF math step-by-step: revenue assumptions, margin projections, discount rate, terminal value. Then create a sensitivity table showing how the target price changes if growth rates or margins differ from base case by 5 percentage points.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Transform into presentation format

Convert your written memo into slides for your committee meeting. Claude restructures your content and creates charts to illustrate key findings.

Convert this analysis into a 6-slide PowerPoint: title slide with recommendation, business model overview, competitive comparison with charts, financial performance trends, valuation summary, and investment thesis. Visualize trends with visual elements, like graphs and charts.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Use specific and clear instructions

Claude has access to vast amounts of financial data when connected to multiple tools and sources. Without specific references in your prompt, you may receive more data than needed or miss specific, critical metrics. Provide clear direction to ensure Claude returns the information required for your analysis, saving time and improving accuracy.

### Download the actual memo, not just the preview

The in-chat preview may not show the final typography, spacing hierarchy, and formatted tables that the document has. Open the file to see—and continue editing—the complete output.

### Match model to task complexity

This example uses Claude Sonnet 4.5, the Claude model best suited for a balance of intelligence, speed, and cost for most use cases. If you need faster iteration (like rapid brainstorming or simple formatting), consider switching to Haiku 4.5, the fastest Claude model with near-frontier intelligence. To learn more about various models, visit our [Model Report](https://www.anthropic.com/transparency/model-report).

### Unlock specialized capabilities

In addition to the ability to connect to financial data tools, [Claude for Financial Services](https://claude.com/solutions/financial-services) adds expanded services. In addition to financial data connections, receive specialized Skills for institutional-grade analysis and frameworks, such as those for financial analysis or valuation. Also receive expert implementation support through tailored onboarding, training, and best practices.

## Ready to try for yourself?

Financial workflows that once required hours of data gathering and manual document formatting now collapse into focused conversations. Test the approach with one company evaluation to calibrate how Claude handles your specific analytical needs.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690b0f6f22640e561aab082e_Screenshot%202025-11-05%20at%2012.21.00%E2%80%AFAM.png)

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
