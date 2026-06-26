<!-- source: https://claude.com/resources/tutorials/using-databricks-for-data-analysis -->

# Using Databricks for Data Analysis

Integrate Claude with Databricks to access organizational data through Unity Catalog using custom functions, vector search, and natural language queries.

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

  https://claude.com/resources/tutorials/using-databricks-for-data-analysis

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The Databricks connector provides Claude with access to your organization's internal data through Unity Catalog, enabling analysis of your databases, running custom business logic, and accessing unstructured documents. Databricks provides three separate connectors: one for functions, one for vector search, and one for Genie, each accessing different capabilities within your Databricks workspace.

## Reminder on Databricks Components

Before exploring what Claude can do with Databricks, it's important to understand three core components that exist within your Databricks workspace:

1. **Unity Catalog Functions**: Custom Python or SQL functions your organization has created for specific calculations, data transformations, or API integrations. These might include proprietary scoring algorithms, normalized financial calculations, or business-specific data processing logic.**‍**
2. **Vector Search**: Semantic search indexes built on your organization's documents and datasets. These allow searching conceptually similar content even when exact keywords don't match.**‍**
3. **Genie**: A natural language interface that translates plain English questions into SQL queries against your data. Genie uses metadata about your tables and columns to understand business terminology and generate appropriate queries.

## What This Connector Provides

### Integration Capabilities

Through the Databricks integration, Claude can access resources in your workspace:

* **Execute Custom Functions**: Claude can run Unity Catalog functions defined by your organization. This includes executing complex business logic, applying calculations, or calling external APIs through functions your team has created. For example, if your organization has built a custom customer health score function, Claude can apply it consistently across analyses.**‍**
* **Semantic Search**: Using vector search indexes, Claude can find relevant documents and content based on meaning rather than just keywords. This is particularly useful for searching through contracts, research reports, customer feedback, or technical documentation where similar concepts might be expressed in different ways.**‍**
* **Natural Language Queries**: Through Genie, Claude can translate plain English questions into SQL queries. Instead of writing complex SQL, you can ask questions like "What was our revenue growth last quarter?" and Claude will use Genie to generate and execute the appropriate query.**‍**
* **Governed Access**: All data access through the connector respects your organization's Unity Catalog permissions and policies. Claude can only access data and execute functions that your user account has permission to use.

### How Claude Uses Databricks Data

Claude applies Databricks capabilities in several ways to support comprehensive data analysis:

* **Multi-Source Analysis**: Claude combines results from database queries, vector searches, and custom functions to provide comprehensive insights. For example, when validating an investment thesis, Claude might query historical financial performance from your portfolio database, search through past due diligence reports for similar sector investments, and apply your proprietary IRR calculation function to model expected returns.**‍**
* **Iterative Exploration**: Claude can query data, analyze initial results, and refine searches based on findings. This allows for analysis where insights from one query inform the next.**‍**
* **Custom Logic Application**: By executing Unity Catalog functions, Claude applies your organization's specific rules and calculations. This ensures that proprietary metrics, adjusted calculations, and company-specific logic are applied uniformly across all analyses.**‍**
* **Contextual Query Building**: When you ask questions in plain English, Claude uses Genie to translate them into appropriate SQL queries. This translation considers your table structures, column names, and relationships to generate accurate queries that match your database structure.**‍**
* **Pattern Recognition**: Through vector search, Claude can find patterns and similarities across documents and data. This helps in finding related issues, similar transactions, or comparable situations that might not be obvious through traditional keyword searches.

## Setting up the Databricks Connector

The Databricks integration consists of three separate connectors, each requiring separate setup:

1. **Functions Server:** Accesses Unity Catalog functions for calculations, business logic, and data transformations.**‍**
2. **Vector Search Server:** Enables semantic search across indexed documents and datasets.**‍**
3. **Genie Server:** Provides natural language to SQL query translation capabilities.

Technical details of the Databricks connectors can be found in Databricks's [MCP Server Documentation](https://docs.databricks.com/aws/en/generative-ai/mcp/managed-mcp). Authentication with Databrick's connectors is handled via [OAuth](https://docs.databricks.com/aws/en/generative-ai/mcp/connect-external-services#connect-claude-connectors-using-oauth) (for [Claude.ai](http://claude.ai/) and Claude Desktop) or via a [Databricks Personal Access Token](https://docs.databricks.com/aws/en/generative-ai/mcp/connect-external-services#connect-claude-desktop-using-pat) (for Claude Desktop only).

### Adding the Connector as an Organization Owner

1. Navigate to [Admin settings > Connectors](https://claude.ai/admin-settings/connectors).
2. Scroll down and click “Add custom connector" at the bottom of the list.
3. Enter integration URL for [your Databricks workspace](https://docs.databricks.com/aws/en/generative-ai/mcp/managed-mcp)‍
4. Name the integration. Remember that there are three separate Databricks servers, so consider naming each uniquely (e.g., "Databricks UC", "Databricks Genie", "Databricks Search")
5. Click "Add"

### For Individual Users

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## Common Use Cases

### Available Resources Example

To illustrate how these capabilities work together, consider a private equity firm with the following Databricks resources configured:

### Tables in this scenario

1. **portfolio\_companies:** Company details, acquisition information, current valuations, and debt levels**‍**
2. **financial\_statements:** Period financials including revenue, EBITDA with adjustments, and operational metrics like customer count and churn**‍**
3. **market\_comparables:** Sector comparable companies with valuation multiples and growth rates**‍**
4. **due\_diligence\_docs:** Repository of due diligence reports, analysis documents, and deal memos

### Unity Catalog Functions in this scenario

1. **calculate\_normalized\_ebitda():** Applies standard private equity adjustments to reported EBITDA, removing one-time costs and normalizing owner compensation**‍**
2. **compute\_portfolio\_irr():** Calculates internal rate of return and money-on-invested-capital based on cash flows and holding periods**‍**
3. **estimate\_debt\_capacity():** Models maximum leverage capacity with covenant compliance stress testing under various scenarios

### Vector Search Index in this scenario

1. **due\_diligence\_index:** Semantic search across all due diligence documents, deal memos, and analysis reports

## Portfolio Exit Readiness Analysis

Example input prompt:

Which portfolio companies are ready for exit? Show valuation ranges and expected returns based on current market multiples.

For this analysis, Claude might use the different UC Functions and Genie in the following steps:

1. **Genie**: Identify portfolio companies held >3 years and retrieve their latest financials.**‍**
2. **UC Function**: Call `calculate_normalized_ebitda()` for each company to apply PE adjustments.**‍**
3. **UC Function**: Execute `compute_portfolio_irr()` to calculate IRR and MOIC for each company.**‍**
4. **Genie**: Query market comparables and apply sector multiples to normalized EBITDA for valuation ranges.

Claude might then report its results in a summary showing exit-ready companies with IRR, MOIC, and valuation ranges based on current market multiples.

## New Deal Valuation

Example input prompt:

We're evaluating TechCorp acquisition (SaaS, $45M revenue, $12M EBITDA).What's a fair valuation and how much debt can we support? Include previous due diligence records in your analysis.

To complete this request, Claude might follow this workflow:

1. **Genie**: Query market comparables for similar-sized companies in target's sector to establish valuation benchmarks.**‍**
2. **UC Function**: Call `estimate_debt_capacity()` with target metrics to model leverage scenarios and stress-test covenant compliance.**‍**
3. **Vector Search**: Search due diligence index for relevant value creation playbooks and precedent transactions.**‍**
4. **Synthesis**: Combine results to generate valuation range, recommended capital structure, and relevant precedents.

Ideally, Claude would then respond with a report on the valuation range and a recommended offer price, while citing sources that lead to its recommendation.

## Covenant Breach Risk Assessment

Example input prompt:

If we see a 15-25% EBITDA decline across the portfolio, which companies risk covenant breaches? What actions should we take?

For this task, Claude might use the following resources:

1. **Genie**: Identify portfolio companies with debt, focusing on those with leverage >4x.**‍**
2. **UC Function**: Call calculate\_normalized\_ebitda() for each high-leverage company to establish baseline.**‍**
3. **UC Function**: Run estimate\_debt\_capacity() with 15%, 20%, and 25% decline scenarios for each company.**‍**
4. **Genie**: Query historical financials to identify companies with deteriorating working capital trends.

Claude might then respond with a breach risk analysis, organized by company and scenario.

## Tips for Using Databricks

* Be specific about what data you are looking for.
  + Example: Instead of "Analyze customers", try "Show me our top 20 customers by…"
* Use "find similar" language for pattern matching
  + Example: "Find feedback that mentions issues like this complaint."

* Remember that all data access permissions follow your Unity Catalog permissions. Claude can only access the data that you can access.
* Custom functions provide consistent calculations. Consider adding UC Functions for calculating standardized metrics.
* Complex analyses may require multiple steps. Ask for a plan first and review Claude's proposed approach.

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
