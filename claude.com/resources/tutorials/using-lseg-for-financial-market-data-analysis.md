<!-- source: https://claude.com/resources/tutorials/using-lseg-for-financial-market-data-analysis -->

# Using LSEG for financial market data analysis

Set up and use LSEG's financial market data integration with Claude for real-time pricing, analytics, and valuation tools across asset classes.

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

  https://claude.com/resources/tutorials/using-lseg-for-financial-market-data-analysis

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The LSEG integration provides Claude with access to LSEG’s comprehensive financial market data ecosystem, spanning across asset classes and domains. This article explains how to set up and use LSEG to retrieve real-time market data, analytics, and perform complex financial calculations. The LSEG integration relies upon Claude’s ability to use remote connectors.

## What This Integration Provides

### Capabilities

The LSEG integration enables Claude to access institutional-grade market data, analytics, and valuation tools directly into conversational AI workflows.

* **FX Spot Price Calculation:** Get the latest FX spot rates for currency pairs, enabling real-time foreign exchange analysis and multi-currency calculations.**‍**
* **FX Forward Price Calculation:** Compute tenor FX forward rates for currency pairs and display FX forward points between currency pairs for different tenors, supporting hedging strategies and forward contract analysis.**‍**
* **Interest Rate Curve Analysis:** Calculate interest rate curves for specific curve references and access comprehensive lists of all interest rate curves maintained by LSEG for yield curve construction and rate projections.**‍**
* **FX Forward Curve Points:** Calculate FX forward curve points using LSEG-defined forward curves with specific valuation dates, providing detailed term structure analysis for currency derivatives.**‍**
* **Bond Pricing:** Price bonds using ISIN codes to retrieve current market valuations, yield calculations, and spread measures for fixed income analysis.**‍**
* **Comprehensive Asset Class Coverage:** Access data and analytics across equities, fixed income, FX, commodities, and other asset classes through LSEG’s extensive database.

## How Claude Uses LSEG Data

Claude applies LSEG’s market data to support your financial analysis.

* Real-Time FX Analysis: Retrieves current spot rates and forward prices for currency pairs to analyze exchange rate movements, calculate cross-rates, and evaluate currency exposures.
* Yield Curve Construction: Pulls interest rate curve data to build term structures, calculate forward rates, and analyze the shape of yield curves for interest rate forecasting.
* Fixed Income Valuation: Uses bond pricing tools to value securities, compare yields across issuers, and assess credit spreads for portfolio management and trading decisions.
* Cross-Asset Analysis: Combines data from multiple asset classes to identify relationships, correlations, and trading opportunities across markets.
* Hedging Strategy Development: Leverages forward curve data to structure currency hedges, evaluate hedge effectiveness, and optimize hedging costs.
* Market Data Validation: Provides authoritative pricing and reference data to verify quotes, reconcile positions, and ensure data accuracy.

## Setting Up LSEG Integration

Technical details of the LSEG Integration can be found in LSEG’s MCP Server Documentation (available soon on LSEG portal). You will need to contact LSEG to get access to the MCP server.

### For Organization Owners

1. Navigate to [Admin settings > Connectors](https://claude.ai/admin-settings/connectors).
2. Scroll down and click “Add custom connector” at the bottom of the list.
3. Enter integration URL: <https://api.analytics.lseg.com/lfa/mcp>‍
4. Name the integration (e.g., “LSEG MCP”)
5. Click “Add”

### For Individual Users

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## Common Use Cases

### Currency Exchange Rate Analysis

Example input prompt:

`What’s the current USD/EUR spot rate, and what are the 3-month and 6-month forward rates? Calculate the implied forward points for each tenor.`

**When to use:** Evaluating currency positions, pricing FX forwards, or analyzing currency basis.

**Tip:** Compare spot vs. forward rates to understand market expectations for currency movements.

### Interest Rate Curve Comparison

Example input prompt:

`Show me the USD SOFR swap curve. Plot the curve and identify any unusual shapes or inflection points.`

**When to use:** Assessing interest rate risk, pricing swaps, or understanding monetary policy expectations.

**Typical analysis:** Compare curves across different currencies or time periods to identify relative value opportunities.

### Multi-Currency Bond Analysis

Example input prompt:

`Price the following bonds using their ISIN codes: FR0014012I5 (French government bond) and US91282CNT44 (US Treasury). Compare their yields and calculate the spread.`

**When to use:** Portfolio construction, relative value analysis, or credit assessment across sovereign issuers.

**Note:** Ensure proper currency conversion when comparing international bonds.

### FX Forward Curve Construction

Example input prompt:

`For AUD/USD, show me the complete forward curve using AONIA and SOFR conventions. Display the forward points and implied forward rates for standard tenors.`

**When to use:** Structuring FX derivatives, pricing swaps, or analyzing currency carry strategies.

**Works well with:** Custom valuation dates to assess forward pricing at specific points in time.

### Cross-Asset Correlation Analysis

Example input prompt:

`Get the USD SOFR curve and EUR ESTR curve, then analyze how they’ve moved relative to each other. Are there any divergences that suggest trading opportunities?`

**When to use:** Identifying cross-currency basis trades or understanding global rate relationships.

**Key benefit:** LSEG provides consistent data across asset classes for reliable correlation analysis.

### Real-Time Market Data for Trading

Example input prompt:

`I’m looking at pricing a currency swap. Get me the current EUR/USD spot rate and the EUR ESTR and USD SOFR curves for accurate valuation.`

**When to use:** Pre-trade analysis, pricing verification, or mark-to-market calculations.

**Why it matters:** Real-time access ensures your analysis reflects current market conditions.

## Tips for Using LSEG

* Use specific currency pair conventions (USD/EUR, GBP/USD)
* Specify tenors clearly for forward rates (3M, 6M, 1Y)
* Reference bonds by ISIN codes for accurate pricing
* Define valuation dates when working with forward curves
* Understand curve conventions (SOFR, ESTR, AONIA) for different currencies
* Cross-reference data across tools to validate analysis

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
