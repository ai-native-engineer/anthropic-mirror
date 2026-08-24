<!-- source: https://academy.claude.com/tutorials/using-chronograph-for-portfolio-monitoring -->

The Chronograph integration provides Claude with access to a portfolio monitoring platform that enables investment analysis and tracking. This article explains how to set up and use Chronograph to access portfolio data and investment insights. The Chronograph integration relies upon Claude’s ability to use remote connectors.

## What This Integration Provides

### Capabilities

The Chronograph integration enables Claude to access comprehensive portfolio and investment data.

* **Entity Search and Discovery:** Search for companies, funds, groups, and general partners via substring similarity search. The search helps you quickly locate relevant investment entities across Chronograph’s database.
* **Core Entity Information:** Retrieve detailed information about entities including their identifiers, core details, and filter options. This provides fundamental data needed for investment analysis.
* **Portfolio Exposure Tracking:** List your top company exposures by investment status (Invested, Realized, or Unrealized), along with detailed company information for portfolio monitoring and risk assessment.
* **Commitment History Analysis:** Calculate aggregate values for key metrics including NAV, Called, Distributed, Unfunded, Net IRR, Net MOIC, and Commitment Amount across your portfolio’s commitment history.
* **Investment Metrics Calculator:** Calculate individual metrics across specific investments, useful for aggregating and tracking performance. The calculator helps enumerate available metric options before running detailed queries.
* **Help Center Integration:** Access Chronograph’s help documentation directly through Claude. Search for relevant articles or retrieve complete article content to answer platform-specific questions.

## How Claude Uses Chronograph Data

Claude applies Chronograph’s portfolio data to support your investment analysis.

* Portfolio Performance Review: Retrieves commitment history data and calculates key metrics like IRR and MOIC to assess portfolio performance over time.
* Exposure Analysis: Pulls top company exposures to identify concentration risks and diversification opportunities across your portfolio.
* Entity Research: Searches for and retrieves detailed information about companies, funds, or partners to support due diligence and investment decisions.
* Metric Calculations: Computes custom investment metrics across your holdings to create tailored performance reports matching your analytical needs.
* Documentation Access: Searches Chronograph’s help center to answer questions about platform features, workflows, and best practices.

## Setting Up Chronograph Integration

You will need to contact Chronograph to get access to the MCP server.

### For Organization Owners

1. Navigate to [Admin settings > Connectors(opens in new tab)](https://claude.ai/admin-settings/connectors).
2. Scroll down and click “Add custom connector” at the bottom of the list.
3. Enter the integration details provided by Chronograph.
4. Name the integration (e.g., “Chronograph MCP”)
5. Click “Add”

### For Individual Users

1. Navigate to Settings > Connectors.
2. Find Chronograph in the list and click Connect.
3. In the new browser tab that appears, log in to your Chronograph account.
4. A confirmation will appear to indicate successful authentication, at which point you can close the tab and begin interacting with your Chronograph data via Claude.

## Common Use Cases

### Portfolio Performance Summary

Example input prompt:

Show me my portfolio’s overall performance metrics including Net IRR, Net MOIC, and total commitments across all investments.



Open in Claude

**When to use:** Regular portfolio reviews, investor reporting, or board presentations.

**Tip:** Specify time periods or commitment types for more focused analysis.

### Exposure Analysis

Example input prompt:

What are my top 10 company exposures by unrealized value? Include company details and current investment amounts.



Open in Claude

**When to use:** Risk management, concentration monitoring, or rebalancing decisions.

**Note:** Use different status filters (Invested, Realized, Unrealized) to analyze different portfolio segments.

### Entity Due Diligence

Example input prompt:

Search for information about [Company/Fund Name] and provide all available details including identifiers and key metrics.



Open in Claude

**When to use:** Initial research on potential investments or updating information on existing holdings.

**Works well with:** Combining entity search with exposure tracking for comprehensive analysis.

### Custom Metric Tracking

Example input prompt:

Calculate [specific metric] across my active investments in the technology sector.



Open in Claude

**When to use:** Sector-specific analysis, tracking specialized KPIs, or custom performance reporting.

**Key benefit:** First use the calculator with query: {help: true} to see available options and required parameters.

### Platform Guidance

Example input prompt:

Search Chronograph’s help center for articles about [topic] or How do I [perform specific task] in Chronograph?



Open in Claude

**When to use:** Learning platform features, troubleshooting workflows, or discovering capabilities.

**Tip:** Be specific with search terms to find the most relevant documentation.

## Tips for Using Chronograph

* Use specific entity names or identifiers when possible for accurate results
* For metric calculations, first call the Investment Metrics Calculator with query: {help: true} to see available options
* Specify investment status filters (Invested, Realized, Unrealized) to focus your analysis
* Search the help center for platform-specific guidance before asking general questions

**Note:** Claude currently cannot access documents, custom fields, or metrics that require a Primary Metric Type label.
