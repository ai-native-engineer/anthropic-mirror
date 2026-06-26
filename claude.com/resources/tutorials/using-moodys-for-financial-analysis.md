<!-- source: https://claude.com/resources/tutorials/using-moodys-for-financial-analysis -->

# Using Moody's for financial analysis

Use Moody's credit ratings connector with Claude for comprehensive financial analysis including credit ratings, outlooks, and research documents.

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

  https://claude.com/resources/tutorials/using-moodys-for-financial-analysis

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The Moody’s connector provides Claude with access to proprietary credit ratings, comprehensive entity intelligence, and analytical frameworks for risk assessment through the Model Context Protocol (MCP). This integration enables financial professionals to access Moody’s authoritative data directly within their AI workflows.

## What This Connector Provides

### Integration Capabilities

Through the Moody’s integration, Claude can access the following resources:

* **Entity Discovery:** Claude can search for entities covered by Moody’s using identifiers, company names, or related metadata. This returns Moody’s unique entity IDs that unlock access to comprehensive datasets.

* **Credit Ratings and Outlooks:** Retrieve current credit ratings, rating dates, and outlooks for specific entities, providing critical information for credit risk assessment and investment decisions.

* **Research Library Access:** Claude can search Moody’s proprietary research documents related to specific entities or topics, giving you access to expert analysis and insights.

* **Rating Driver Analysis:** Access the primary factors behind credit rating upgrades or downgrades, providing context for rating movements and enabling deeper risk analysis.

* **Rating Scorecards:** View detailed rating scorecards including factor weights, scoring components, and overall rating rationale to understand how Moody’s evaluates entity creditworthiness.

## How Claude Uses Moody’s Data

Claude applies Moody’s capabilities to support comprehensive financial analysis:

* **Integrated Risk Assessment:** Claude combines credit ratings, research insights, and rating drivers to provide holistic risk evaluations. For example, when analyzing a potential investment, Claude might retrieve the entity’s current rating, review recent research publications, and examine the factors that could trigger rating changes.

* **Contextual Analysis:** By accessing rating scorecards and upgrade/downgrade factors, Claude applies Moody’s analytical frameworks to understand credit quality. This ensures that risk assessments align with industry-standard methodologies.

* **Research-Backed Insights:** Claude can search through Moody’s extensive research library to find relevant analysis, sector trends, and comparable entity studies, providing evidence-based context for financial decisions.

* **Entity Intelligence:** Through entity mapping and discovery, Claude can identify relationships between entities, access comprehensive company intelligence, and retrieve relevant Moody’s data across different use cases.

## Setting up the Moody’s Connector

The Moody’s MCP server uses remote access via a simple URL endpoint and is compatible with any LLM that supports the MCP Standard Protocol.

* Authentication: The Moody’s connector implements OAuth authentication. When connecting, you’ll be redirected to a Moody’s authentication page where you’ll enter your authorized credentials. After successful authentication, you’ll be redirected back to Claude.

* Server URL: <https://api.moodys.com/genai-ready-data/m1/mcp>

### Adding the Connector as an Organization Owner

1. Navigate to [Admin settings > Connectors](https://claude.ai/admin-settings/connectors)

1. Click “Add custom connector”

1. Enter the Moody’s MCP server URL: <https://api.moodys.com/genai-ready-data/m1/mcp>

1. Name the integration (e.g., “Moody’s Credit Intelligence”)

1. Click “Add”

### For Individual Users

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## Common Use Cases

### Available Tools Example

To illustrate how these tools work together, consider a financial services firm with access to the following Moody’s MCP tools:

Entity Tools:

* findEntity: Search for companies, financial institutions, or governmental entities covered by Moody’s

* - getEntityRatings: Retrieve current ratings and outlooks

* - getEntityRatingDrivers: Access upgrade/downgrade factors

* - getEntityScorecard: View detailed rating methodology and scoring

Research Tools:

* searchEntityDocuments: Access Moody’s proprietary research library

### Credit Analysis for Portfolio Management

Example input prompt:

Analyze the credit profile of XYZ Corporation. What’s their current rating, what factors could trigger a downgrade, and are there any recent research reports I should review?

For this analysis, Claude might use the following workflow:

1. **Entity Discovery:** Use findEntity to locate XYZ Corporation and retrieve its unique Moody’s entity ID.

1. **Rating Retrieval:** Call getEntityRatings to retrieve the current credit rating, outlook, and rating date.

1. **Risk Factor Analysis:** Execute getEntityRatingDrivers to identify the key factors that could lead to rating upgrades or downgrades.

1. **Rating Methodology:** Use getEntityScorecard to view the detailed scorecard showing how Moody’s evaluates this entity across different factors.

1. **Research Review:** Call searchEntityDocuments to find recent research reports, sector analyses, or rating action commentaries.

Claude might then provide a comprehensive credit analysis including the current rating, key risk factors to monitor, and relevant insights from Moody’s research.

### M&A Due Diligence

Example input prompt:

We’re evaluating an acquisition of ABC Manufacturing. What’s their credit standing, and how does it compare to their sector peers? Include relevant research on industry trends.

To complete this request, Claude might follow this workflow:

1. **Target Analysis:** Use findEntity and getEntityRatings to establish the target’s creditworthiness.

1. **Rating Factors:** Call getEntityScorecard and getEntityRatingDrivers to understand the underlying credit fundamentals and potential risks.

1. **Sector Context:** Execute searchEntityDocuments with sector-specific queries to find research on industry trends, peer comparisons, and market outlook.

1. **Synthesis:** Combine ratings, scorecard metrics, and research insights to provide a comprehensive view of the target’s credit profile and sector positioning.

Claude would then respond with a due diligence summary including credit ratings, key risk factors, sector positioning, and relevant research findings.

### Investment Portfolio Monitoring

Example input prompt:

Monitor my portfolio holdings for any rating changes or negative rating drivers. My holdings include: Company A, Company B, and Company C.

For this task, Claude might use the following approach:

1. **Entity Identification:** Use findEntity to locate each portfolio company in Moody’s database.

1. **Rating Status:** Call getEntityRatings for each holding to check current ratings and outlooks.

1. **Risk Assessment:** Execute getEntityRatingDrivers for holdings with negative outlooks or recent rating changes to identify specific risk factors.

1. **Research Updates:** Use searchEntityDocuments to find any recent research publications or rating action commentaries for companies showing credit stress.

Claude might then respond with a portfolio monitoring report highlighting any rating changes, companies on negative watch, and key risk factors requiring attention.

### Counterparty Risk Assessment

Example input prompt:

We’re entering a large trade with DEF Bank. Assess their credit quality and identify any factors that could impact their creditworthiness over the next 12 months.

For this assessment, Claude might follow these steps:

1. **Entity Lookup:** Use findEntity to locate DEF Bank in Moody’s coverage universe.

1. **Credit Profile:** Call getEntityRatings to retrieve current ratings and outlook.

1. **Rating Analysis:** Execute getEntityScorecard to review the bank’s financial strength across key metrics like capital adequacy, asset quality, and liquidity.

1. **Forward-Looking Factors:** Use getEntityRatingDrivers to identify specific factors that could trigger rating changes.

1. **Research Context:** Call searchEntityDocuments to find sector research on banking industry trends and systemic risks.

Claude would then provide a counterparty risk assessment including current credit standing, key vulnerabilities, and forward-looking risk factors.

## Tips for Using Moody’s

* Be specific about entities: When searching for entities, include relevant identifiers like ticker symbols, full legal names, or location information for more accurate results.
  + Example: Instead of “Apple”, try “Apple Inc. (AAPL)”
* Leverage rating drivers for forward-looking analysis: The rating upgrade/downgrade factors provide valuable insights into what could change an entity’s credit profile.
  + Example: “What factors would lead to a downgrade of Company X’s rating?”

* Combine tools for comprehensive analysis: Use multiple tools together to build complete credit profiles. Start with ratings, then examine scorecards and drivers, and supplement with research.

* Access is governed by your Moody’s subscription: Claude can only access data and research that your Moody’s account has permission to view. The connector respects your subscription entitlements.
* Use research search for sector insights: The document search isn’t limited to individual entities. Search by sector, theme, or risk type to find broader market analysis.
  + Example: “Find Moody’s research on renewable energy sector credit trends”

* Rating scorecards provide methodology transparency: Review scorecards to understand how Moody’s weighs different factors in their rating assessment, which can inform your own credit analysis framework.

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
