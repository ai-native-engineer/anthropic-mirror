<!-- source: https://claude.com/resources/tutorials/using-factset-for-comprehensive-financial-research -->

# Using FactSet for comprehensive financial research

Set up and use Claude's FactSet integration for institutional-grade financial analysis including pricing, fundamentals, estimates, M&A data, and ownership.

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

  https://claude.com/resources/tutorials/using-factset-for-comprehensive-financial-research

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The FactSet integration is currently in early access; contact the FactSet team for additional details.

The FactSet integration provides Claude with access to institutional-grade financial data and analytics used by investment professionals worldwide. This article explains how to set up and use FactSet data for financial analysis, including global pricing data, fundamental financials, analyst estimates, M&A transactions, ownership data, and executive information.

## What This Integration Provides

### Capabilities

The FactSet integration enables Claude to access multiple categories of financial and market data:

* **Global Market Data**: End-of-day pricing, OHLC, volume, and returns for global equities, ADRs, and ETFs from 2006 onwards, including corporate actions and dividend adjustments.**‍**
* **Comprehensive Fundamentals**: Standardized financial statements, segment breakdowns, and ratios from company filings across annual, quarterly, and interim periods.**‍**
* **Analyst Consensus and Estimates**: Forward-looking earnings estimates, analyst ratings, and earnings surprise data comparing actual results to expectations.**‍**
* **M&A and Deal Intelligence**: Transaction data including deal values, terms, parties, and status for both public and private deals.**‍**
* **Supply Chain Relationships**: Business network mapping of competitors, customers, suppliers, and partners from regulatory filings.**‍**
* **Ownership and Insider Activity**: Institutional holdings, fund positions, and insider transactions (with quarterly filing lags).**‍**
* **Executive and Board Information**: Leadership profiles, compensation data, employment history, and governance statistics.**‍**
* **Corporate Events Calendar**: Earnings announcements, investor conferences, and other scheduled corporate events.

## How Claude Uses FactSet Data

Claude applies FactSet's data to support comprehensive analysis:

* **Integrated Company Analysis**: Combines pricing, fundamentals, estimates, and ownership data to build complete company profiles.**‍**
* **Cross-Dataset Validation**: Verifies information across data types, such as comparing earnings surprises to insider trading patterns.**‍**
* **Timeline Construction**:Builds chronological narratives combining M&A events, corporate actions, and management changes.**‍**
* **Network Mapping**: Creates relationship maps showing competitive dynamics and ownership structures.**‍**
* **Multi-Period Comparisons**: Retrieves standardized metrics across companies for accurate peer analysis.

## Setting up the FactSet integration

### For Organization Owners

1. Navigate to [Admin settings > Connectors](https://claude.ai/admin-settings/connectors).
2. Scroll down and click “Add custom connector" at the bottom of the list.
3. Enter the FactSet integration URL (provided by your FactSet representative)
4. Name the integration (e.g., "FactSet")
5. Click "Add"

### For Individual Users

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## Common Use Cases

### Comprehensive Equity Research

`Using FactSet, create a complete analysis of Apple (AAPL) including 5-year price performance with total returns, latest quarterly fundamentals versus prior year, consensus estimates for next fiscal year, and recent insider transaction activity. Compare key metrics to Microsoft and Google as peer benchmarks.`

This request uses multiple FactSet datasets to build a complete equity research report. Claude retrieves historical pricing to show performance trends, pulls standardized fundamentals for year-over-year comparisons, incorporates forward-looking consensus estimates, and adds governance context through insider activity. The peer comparison ensures relative valuation context using FactSet's standardized metrics.

**When to use**: Building investment research reports or preparing for investment committee presentations.

**Tip**: FactSet's standardized fundamentals enable true apples-to-apples comparisons across companies, even when they use different accounting presentations.

### M&A Activity Analysis

Retrieve all M&A deals in the software sector over the past 24 months where deal value exceeded $1 billion. Include buyer, target, deal value, and completion status. Then identify which acquirers have been most active and their typical deal sizes.

M&A analysis through FactSet shows consolidation patterns and strategic priorities in specific sectors. Claude retrieves transaction data filtered by industry, size, and time period, then analyzes patterns to identify serial acquirers, typical valuations, and preferred deal structures.

**When to use**: Understanding consolidation trends or identifying potential acquirers and targets.

**Note**: Deal data includes both completed and pending transactions, with status indicators showing which deals closed successfully versus those that were terminated.

### Earnings Surprise Analysis

For the last 8 quarters, show me Netflix's reported EPS versus consensus estimates, calculating the surprise percentage and direction. Include the stock's price reaction in the 3 days following each announcement to understand how the market responded to surprises.

Earnings surprise analysis combines FactSet's expectations data with actual reported results and subsequent price movements. Claude can identify whether companies beat or missed expectations and calculate the magnitude of the surprise. The integration provides historical earnings performance data alongside corresponding stock price changes, enabling analysis of earnings sensitivity patterns.

**When to use**: Evaluating management credibility and understanding market expectations.

**Key benefit**: Combines estimate data with price reactions for complete surprise impact analysis, showing not just the surprise but how the market interpreted it.

### Ownership and Insider Tracking

Show me the top 20 institutional holders of Tesla, their current positions, and changes over the last quarter. Also pull any insider transactions over $1 million in the past 6 months, noting whether executives were buying or selling.

Claude retrieves institutional holdings data showing position sizes and changes by investment managers, mutual funds, and other institutional investors. The integration also tracks insider transactions, documenting when executives and directors buy or sell shares in their companies. These datasets show ownership changes over time, though institutional data typically reflects quarterly filing cycles rather than current positions.

**When to use**: Understanding investor sentiment and management confidence.

**Note**: Ownership data typically has a quarterly lag due to filing requirements, so positions shown may not reflect current holdings.

### Supply Chain Risk Assessment

Map NVIDIA's key suppliers, customers, and partners from FactSet's relationship data. Identify any concentration risks where a single relationship represents significant revenue exposure. Cross-reference with recent 10-K risk disclosures.

Supply chain analysis through FactSet can show dependencies that may not be apparent from financial statements. This analysis can highlight risks, potential supply disruptions, and customer dependencies that could impact future performance.

**When to use**: Operational due diligence or supply chain risk analysis.

**Key consideration**: Relationship data comes from disclosed sources and may not capture all partnerships, particularly those below materiality thresholds.

## Tips for Using FactSet

* Specify exact data types needed to avoid overwhelming results

* Use date ranges to manage data volume, especially for daily pricing data

* Note that some data has reporting lags—ownership is quarterly, insider transactions have filing delays

* For complex analyses, start with a subset of companies before expanding scope

* Be aware that relationship and ownership data reflects disclosed information and may not be complete

‍

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
