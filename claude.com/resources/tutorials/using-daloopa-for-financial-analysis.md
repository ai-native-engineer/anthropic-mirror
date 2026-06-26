<!-- source: https://claude.com/resources/tutorials/using-daloopa-for-financial-analysis -->

# Using Daloopa for financial analysis

Set up and use the Daloopa integration with Claude for accessing financial data from public company filings covering 3,500+ companies.

  Finance
* Product

  Claude.ai
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/using-daloopa-for-financial-analysis

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The Daloopa integration provides Claude with access to a financial data extraction service that covers public company filings and metrics. This article explains how to set up and use Daloopa to retrieve financial data for your analysis.

The Daloopa integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## What This Integration Provides

### Capabilities

The Daloopa integration enables Claude to access comprehensive financial data from public company filings.

* **Company Discovery and Identification:** Search for companies using ticker symbols or company names across Daloopa's database of 3,500+ public companies. The search handles name variations and automatically matches to the correct entity.**‍**
* **Financial Metric Discovery:** Explore all available data series for any company, including standard financial statements and company-specific KPIs like subscriber counts for streaming services or wafer shipments for semiconductors. This reveals unique operational metrics beyond standard line items.**‍**
* **Historical Data Retrieval:** Access specific financial fundamentals across custom time periods, with most companies having 10+ years of data. Request individual quarters, full years, or any combination for flexible analysis.**‍**
* **Source-Linked Data Points:** Every financial value includes a hyperlink to its exact location in SEC filings or investor materials, providing complete transparency and audit trails.**‍**
* **Flexible Period Selection:** Request data for any combination of quarters or years to enable quarter-over-quarter comparisons, year-over-year analyses, or custom period selections matching your analytical needs.**‍**
* **Granular Metric Access:** Access specific line items like segment revenue breakdowns or working capital components without retrieving entire financial statements.

## How Claude Uses Daloopa Data

Claude applies Daloopa's financial data to support your analysis.

* **Multi-Company Comparisons:** Retrieves metrics for multiple companies and builds comparative tables showing revenue growth, margins, and other KPIs side by side to identify relative performance.**‍**
* **Trend Analysis Construction:** Pulls data across multiple periods to calculate growth rates and identify patterns, highlighting periods of acceleration or deceleration in company performance.**‍**
* **Custom Metric Calculations:** Computes derived metrics like free cash flow conversion or return on invested capital using raw financial data, creating calculations tailored to your analytical framework.**‍**
* **Data Quality Verification:** Uses source links to reference specific filing locations, helping verify unusual figures or reconcile discrepancies with explanations from the original documents.**‍**
* **Earnings Analysis Automation:** Following releases, pulls latest results and compares to prior periods, calculating variances and presenting structured analysis of key changes.**‍**
* **Metric Discovery for Unfamiliar Companies:** First explores available metrics for new companies, then retrieves the most relevant KPIs, particularly useful when analyzing unfamiliar sectors with different performance indicators.

## Setting Up Daloopa Integration

Technical details of the Daloopa Integration can be found in Daloopa's [MCP Server Documentation](https://docs.daloopa.com/docs/daloopa-mcp). You will need to contact Daloopa to get access to the MCP server.

### For Organization Owners

1. Navigate to [Admin settings > Connectors](https://claude.ai/admin-settings/connectors).
2. Scroll down and click “Add custom connector" at the bottom of the list.
3. Enter integration URL: <https://mcp.daloopa.com/server/mcp>‍
4. Name the integration (e.g., "Daloopa MCP")
5. Click "Add"

### For Individual Users

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## Common Use Cases

### Multi-Company Benchmarking

`Using Daloopa, compare cash-on-cash returns for CAVA, SHAK, and CMG over the last 8 quarters. Include both the absolute values and quarter-over quarter growth rates to identify which company is improving operational efficiency fastest.`

**When to use:** Evaluating relative performance across peer companies for investment decisions or competitive analysis.

**Tip:** Specify 3-10 companies with clear metrics for manageable output that fits well in tables or charts.

### Time Series Analysis

`Pull revenue and gross margin trends for MSFT from Q1 2023 to Q1 2025. Show both the quarterly values and calculate the year-over-year growth rates for each quarter.`

**When to use:** Tracking company performance over time to identify trends, seasonality, or inflection points.

**Typical timeframe:** 4-24 quarters provides good trend visibility without overwhelming detail.

## Operational KPI Analysis

`Show me non-GAAP gross margins for top analog semiconductor companies. Focus on AMD, NVDA, INTC, AVGO, and QCOM to understand margin profiles in the sector.`

**When to use:** Comparing operational efficiency metrics across companies in the same industry.

**Note:** Focus on 2-5 specific KPIs at a time for clarity in analysis.

## Quarter-over-Quarter Analysis

`What changed most materially in Apple's latest quarter versus prior quarter? Focus on revenue, operating margin, and free cash flow changes.`

**When to use:** Understanding momentum and recent changes in company performance, particularly useful right after earnings releases.

**Works well with:** Recent 2-4 reporting periods for focused analysis.

## Post-Earnings Analysis

`Microsoft just reported earnings yesterday - pull their Q4 2024 results and compare them to both the prior quarter (Q3 2024) and year-ago quarter (Q4 2023). Include revenue by segment, operating margins, and any operational metrics like Azure growth or Office 365 subscribers that are available.`

**When to use:** Immediately after a company reports earnings to quickly assess performance against multiple comparison periods.

**Key benefit:** Rapidly generate earnings summaries with quantified deltas and growth rates while the market is still digesting the results.

**Note:** Request specific segments or metrics mentioned in the earnings call for deeper insight into business drivers.

## Discovering Available Metrics

`I'm analyzing Spotify (SPOT) and need to understand their key business metrics beyond standard financials. Search Daloopa for all available metrics related to subscribers, ARPU, content costs, and any other operational KPIs they report for the last 8 quarters.`

**When to use:** Beginning analysis on an unfamiliar company or sector where you need to understand what unique metrics are tracked.

**Why it matters:** Many companies report industry-specific KPIs (like Spotify's Premium subscribers or Netflix's content amortization) that aren't in standard financial statements.

**Tip:** Start broad to discover available metrics, then narrow your request to the most relevant ones for detailed analysis.

## Tips for Using Daloopa

* Use specific company tickers (MSFT, AAPL)
* Define clear time periods (Q1 2024, 2023FY)
* Request specific metrics rather than general categories
* Limit scope to reasonable number of companies for clear comparisons
* Consider data freshness - Daloopa updates after earnings releases but may not have real-time intraday data

## Related tutorials

[Install financial services plugins for Claude Cowork](/resources/tutorials/install-financial-services-plugins-for-cowork)Install financial services plugins for Claude Cowork

Install financial services plugins for Claude Cowork

Tutorial

[Tutorial](/resources/tutorials/install-financial-services-plugins-for-cowork)Tutorial

[How to build a plugin from scratch in Claude Cowork](/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork)How to build a plugin from scratch in Claude Cowork

How to build a plugin from scratch in Claude Cowork

Tutorial

[Tutorial](/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork)Tutorial

[Getting started with Claude in Excel](/resources/tutorials/getting-started-with-claude-in-excel)Getting started with Claude in Excel

Getting started with Claude in Excel

Tutorial

[Tutorial](/resources/tutorials/getting-started-with-claude-in-excel)Tutorial

[How to use Claude in Excel for accounting: Revenue model validation](/resources/tutorials/how-to-use-claude-in-excel-for-accounting-revenue-model-validation)How to use Claude in Excel for accounting: Revenue model validation

How to use Claude in Excel for accounting: Revenue model validation

Tutorial

[Tutorial](/resources/tutorials/how-to-use-claude-in-excel-for-accounting-revenue-model-validation)Tutorial
