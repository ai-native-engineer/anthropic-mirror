<!-- source: https://claude.com/resources/tutorials/prompting-strategies-for-financial-analysis -->

# Prompting strategies for financial analysis

Learn how to write effective prompts for Claude's financial analysis capabilities focusing on clarity, specificity, and data management.

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

  https://claude.com/resources/tutorials/prompting-strategies-for-financial-analysis

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Effective prompting helps you use Claude's financial analysis capabilities efficiently and accurately. This guide provides strategies for writing clear, specific prompts that produce the results you need while avoiding common issues that can lead to incomplete or overwhelming outputs.

## Discovering What Data Claude Can Access

Before starting any financial analysis, it's essential to understand which data sources Claude has available. Different integrations provide different types of data—Daloopa focuses on SEC filings and fundamentals and Kensho offers comprehensive S&P Global market data and business relationships. Knowing what's accessible prevents wasted time requesting unavailable data.

Start your analysis sessions by confirming data availability:

* "*What S&P Global financial data can you access through Kensho?*"

* "*Can you retrieve segment data through Daloopa?*"

This preliminary step prevents requesting analyses that require unavailable data and helps you understand which integration to specify for different types of analysis.

## Core Prompting Principles

### Be Specific and Clear

Claude has access to vast amounts of financial data through multiple sources. Without specific instructions, you may receive more data than needed or miss critical metrics. Clear specifications ensure you get exactly what your analysis requires, saving time and improving accuracy.

Consider these contrasting examples:

# Bad prompt

`Claude, please Analyze Microsoft`

This vague request could trigger retrieval of hundreds of data points across multiple years, making it difficult to identify relevant insights. Claude won't know whether you want valuation metrics, operational performance, or competitive positioning.

# Good prompt

`Using Daloopa, retrieve Microsoft's (MSFT) revenue, operating margin, and free cash flow for Q1 2023 through Q4 2024, then calculate year-over-year growth rates`

This specific request identifies the data source, company ticker, exact metrics, time period, and desired calculations. Claude knows precisely what to retrieve and how to process it. Your prompts should include company tickers, exact metric names, specific time periods, and the desired output format.

### Request Only Relevant Information

Financial integrations can pull extensive datasets covering hundreds of metrics across many years. Requesting everything available wastes time, increases processing complexity, and makes it harder to focus on what matters for your specific analysis. Targeted requests produce cleaner, more actionable results.

# Bad prompt

`Pull all financial data for Tesla, Ford, and GM`

This request could return thousands of data points including irrelevant metrics, making it difficult to conduct focused analysis.

# Good prompt

`For Tesla (TSLA), Ford (F), and GM, retrieve only automotive revenue and gross margins for the last 4 quarters to compare operational efficiency`

This focused request retrieves only the metrics needed for operational comparison. When crafting prompts, think about your analytical objective first, then request only the data that directly supports that analysis. This approach produces more manageable outputs and clearer insights.

### Control Data Volume

Large data requests can slow down analysis and produce overwhelming outputs that are difficult to interpret. Managing scope ensures Claude can process requests efficiently and present results in digestible formats. This is particularly important when working with multiple companies or extended time periods.

# Bad prompt

`Get all available historical data for the entire S&P 500`

This request is likely to fail or produce unusable results due to the sheer volume of data involved.

# Good prompt

`Retrieve the last 8 quarters of revenue and EBITDA margin for these 5 software companies: CRM, NOW, WDAY, TEAM, and ZM`

This manageable request focuses on a specific peer group with defined metrics and a reasonable time frame. As a general guideline, limit requests to 3-5 companies for detailed analysis, request specific line items rather than entire financial statements, and use date ranges that match your analytical needs rather than requesting all available history.

## Structuring Complex Analyses

### Request Analysis Plans First

Complex financial analyses involve multiple steps, data sources, and assumptions. Having Claude outline the approach first lets you catch potential issues before time is spent on calculations. This is especially valuable for valuations, modeling, or multi-company comparisons where methodology choices significantly impact results. A clear plan also ensures alignment between your expectations and Claude's intended approach.

# Bad prompt

`Do a complete valuation analysis of Netflix`

This open-ended request leaves too many decisions to Claude, potentially resulting in an analysis that doesn't match your requirements or uses inappropriate assumptions.

# Good prompt

`Create a plan for valuing Netflix (NFLX) using DCF methodology. List the data you'll need, calculations you'll perform, and assumptions you'll make. Let me review before you proceed.`

This approach gives you visibility into the planned methodology before execution begins. You can review the data sources Claude intends to use, verify that key assumptions are reasonable, identify any missing components, and adjust the approach before investing time in detailed calculations. This preliminary review often catches issues that would be costly to fix after the analysis is complete.

### Use Step-by-Step Approaches

Breaking complex analyses into discrete steps provides transparency into Claude's process and allows for course correction. You can verify data accuracy, check calculations, and adjust methodology between steps rather than discovering issues only in final results. This approach is particularly valuable when working with multiple data sources or when calculations build upon each other.

# Bad prompt

`Compare these 5 companies and tell me which is best`

This request produces a black-box analysis where you can't verify the underlying data or logic.

# Good prompt

`Let's analyze these companies step by step. First, pull their P/E ratios. Show me the results before proceeding to the next metric.`

This incremental approach allows you to catch errors early, adjust the analysis based on initial findings, understand Claude's reasoning at each stage, and verify data accuracy before it's used in calculations. Each step becomes a checkpoint where you can ensure the analysis remains on track.

### Build Incrementally

Starting with data retrieval before moving to analysis ensures you're working with accurate, complete information. This approach prevents wasted effort on calculations using incomplete data and helps identify data gaps before they affect conclusions. It also allows you to adjust your analysis based on what data is actually available.

A typical incremental workflow might look like this:

First, retrieve Amazon's segment revenue for the last 8 quarters and show me what's available

Now calculate the growth rate for AWS specifically

Finally, compare AWS growth to Azure's growth over the same period

Each step builds on the previous one, ensuring that you have the necessary foundation before proceeding. This method is particularly useful when exploring unfamiliar companies or sectors where you may not know exactly what data is available until you start the analysis.

## Common Issues and Solutions

### Data Availability Challenges

**Issue:** Requesting data that doesn't exist or isn't available through current integrations can derail your analysis.

**Solution:** Start by asking what's available. For example: "*What operational metrics does Daloopa have for Spotify?*" This preliminary check prevents building analyses around unavailable data.

Different companies report different metrics, and not all historical data may be available. Confirming availability upfront saves time and allows you to adjust your analytical approach based on what data is actually accessible.

### Scope Management

**Issue:** Requesting analysis of 50+ companies at once can produce overwhelming results or cause the analysis to fail entirely.

**Solution:** Break large analyses into smaller groups of 5-10 companies, then combine the results.

For example, instead of "*Analyze all REITs,*" try being more specific: "*Analyze these 5 industrial REITs first: PLD, DRE, FR, TRNO, STAG.*" After reviewing the initial results, you can proceed with additional groups. This approach ensures each batch receives thorough analysis and allows you to refine your criteria based on initial findings.

### Ambiguous Requests

**Issue:** Terms like "good companies" or "strong performance" mean different things to different analysts and can lead to results that don't match your criteria.

**Solution:** Define your criteria explicitly using quantitative thresholds.

Here's an example:

# Bad prompt

`Find me good value stocks`

# Good prompt

`Find companies with P/E below 15, positive free cash flow, and revenue growth above 5%`

The specific criteria ensure Claude identifies companies that match your investment philosophy and screening parameters. This precision is particularly important when building screens or identifying investment candidates.

## Tips for Efficient Prompting

* State your end goal upfront so Claude can suggest appropriate approaches.
* Use consistent terminology throughout your analysis.
* Save successful prompt templates for recurring analyses.
* Start with smaller test requests before scaling up.
* Name the specific data source in your prompts (Daloopa, Kensho/S&P Global).
* Consider data freshness - specify if you need latest available or specific historical data.
* Include output format preferences (table, bullet points, narrative).
* Request source citations when accuracy is critical.
* For recurring analyses, establish a consistent prompt structure you can reuse.

These strategies help you get the most value from Claude's financial analysis capabilities while avoiding common pitfalls. As you develop experience with the system, you'll identify prompt patterns that work well for your specific analytical needs.

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
