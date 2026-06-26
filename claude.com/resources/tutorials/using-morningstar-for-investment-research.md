<!-- source: https://claude.com/resources/tutorials/using-morningstar-for-investment-research -->

# Using Morningstar for investment research

Integrate Morningstar's investment research capabilities into Claude for financial metrics, analyst research, and thematic investment analysis.

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

  https://claude.com/resources/tutorials/using-morningstar-for-investment-research

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The Morningstar integration provides Claude with access to investment research services and proprietary analytical metrics. This article explains how to set up and use Morningstar data for investment analysis, including fair value estimates, economic moat ratings, and star ratings.

The Morningstar integration relies upon Claude's ability to use [remote connectors](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp).

## What This Integration Provides

### Capabilities

The Morningstar integration enables Claude to access investment data and research:

* **Individual Security Metrics:** Retrieve specific data points for individual securities including fair value estimates, economic moat ratings, star ratings, market cap, EPS, and NAV. Data is accessed one security at a time for each stock, fund, or bond.**‍**
* **Analyst Research on Specific Securities:** Access Morningstar analyst opinions on stocks, ETFs, bonds, and mutual funds. Focus on specific aspects like risk factors, performance drivers, or competitive positioning based on fundamental analysis.**‍**
* **Thematic Investment Research:** Explore editorial content on broader investment themes including investment strategies, sustainable investing, retirement planning, and market trends for top-down approaches and asset allocation.**‍**
* **Multi-Asset Class Coverage:** Analyze equities, mutual funds, ETFs, and bonds through a unified interface with consistent metrics and research approaches across all asset types.

### How Claude Uses Morningstar Data

Claude applies Morningstar data to support your analysis:

* **Comparative Analysis:** Gathers data across multiple securities (one at a time) to build comparison tables and identify relative value, such as ranking portfolio holdings by discount to fair value.**‍**
* **Contextual Interpretation:** Combines quantitative metrics with qualitative research to explain both what ratings mean and why, like detailing the competitive advantages behind a "wide moat" rating.**‍**
* **Risk-Reward Assessment:** Evaluates whether returns justify risks by comparing uncertainty ratings and return data across securities.**‍**
* **Narrative Synthesis:** Merges data points with analyst commentary to create comprehensive security overviews that tell the complete investment story.**‍**
* **Screening and Filtering:** Systematically checks multiple securities against your criteria, such as finding wide-moat healthcare companies trading below fair value.

## Setting Up Morningstar Integration

Technical details of the Morningstar Integration can be found in the [Morningstar Integration MCP Server Documentation](https://developer.morningstar.com/direct-web-services/documentation/mcp-server/morningstar-mcp-server). If your account does not have access to the MCP server, you will need to contact Morningstar to get access to the MCP server.

### For Organization Owners

1. Navigate to [Admin settings > Connectors](https://claude.ai/admin-settings/connectors).
2. Scroll down and click “Add custom connector" at the bottom of the list.
3. Enter integration URL: <https://mcp.morningstar.com/mcp>
4. Name the connector (e.g., "Morningstar")
5. Click "Add"

### For Individual Users

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## Common Use Cases

### Valuation Analysis

`What is Microsoft's fair value estimate and economic moat rating compared to other mega-cap tech stocks? Include Apple, Google, and Amazon, showing their fair value ratios and whether they're trading above or below Morningstar's estimates.`

This type of analysis helps identify potentially undervalued securities by comparing current market prices to Morningstar's fair value estimates. The fair value methodology incorporates competitive advantages, growth prospects, and long-term earnings potential. When comparing multiple companies, Claude retrieves data for each individually and then presents the compiled results, making it easy to spot relative value opportunities within a peer group.

**When to use:** Screening for potentially undervalued securities or validating your own valuation models against Morningstar's independent analysis.

### Sector Research

`Provide Morningstar's outlook on renewable energy investments and key valuation metrics for clean energy ETFs. Include their analysis on regulatory tailwinds and which subsectors they view most favorably.`

Sector research combines thematic analysis with specific investment opportunities. Claude accesses Morningstar's editorial content on investment themes while also retrieving metrics for relevant funds and securities. This dual approach provides both the macro perspective on sector trends and specific vehicles for gaining exposure to those trends.

**When to use:** Understanding thematic investment opportunities, evaluating sector rotation strategies, or identifying funds that align with specific investment themes.

### Company Analysis

`Get Morningstar analysis of Apple including fair value, moat rating, and uncertainty rating. Also provide their view on key risks and competitive positioning versus Android ecosystem players.`

Individual company analysis combines Morningstar's quantitative metrics with qualitative analyst insights. Claude retrieves both the numerical ratings and the reasoning behind them, providing a complete picture of Morningstar's view on a security. This includes their assessment of competitive advantages, management quality, and industry dynamics.

**When to use:** Conducting deep dives on individual companies before making investment decisions or reviewing existing holdings.

### Portfolio Analysis

`Show Morningstar ratings and fair value ratios for my technology holdings: MSFT, AAPL, NVDA, and GOOGL. Identify which are trading at the biggest discount to fair value and have the widest economic moats.`

Portfolio analysis involves retrieving Morningstar data for each holding to identify rebalancing opportunities. Claude gathers metrics for each security individually, then synthesizes the information to highlight which positions might be overvalued or undervalued according to Morningstar's analysis. This systematic review helps maintain portfolio discipline and identify when market prices diverge significantly from fundamental values.

**Tip:** Claude retrieves data for each holding individually to build the complete analysis. For large portfolios, consider focusing on core positions or those with recent price movements.

### Risk-Focused Security Analysis

`Analyze Tesla from a risk perspective using Morningstar research. Focus on their assessment of execution risk, competition from traditional automakers, and regulatory challenges. Include their uncertainty rating and any concerns about valuation sustainability.`

Risk-focused analysis uses Morningstar's research capabilities to understand potential downside scenarios and investment risks. By requesting analysis focused on specific risk factors, Claude can provide Morningstar's view on what could go wrong with an investment. This includes both systematic risks affecting the entire sector and idiosyncratic risks specific to the company. The uncertainty rating provides a quantitative measure of how confident Morningstar is in their fair value estimate.

**When to use:** Evaluating high-volatility stocks, understanding the bear case for a position, or assessing whether potential returns adequately compensate for risks.

### Sustainable Investing Research

`What is Morningstar's perspective on ESG investing strategies and their performance versus traditional approaches? Include their recommendations for sustainable funds and whether they see ESG as a source of alpha or risk mitigation.`

Sustainable investing research taps into Morningstar's thematic content on ESG strategies and sustainable investment approaches. Claude can access both Morningstar's philosophical framework for sustainable investing and their practical recommendations for specific funds and strategies. This includes performance comparisons between ESG-focused and traditional investments, helping you understand the potential trade-offs and benefits of sustainable investing approaches.

**Why it matters:** Morningstar provides both conceptual frameworks and specific fund recommendations, helping bridge the gap between sustainable investing theory and practical implementation.

## Tips for Using Morningstar

* Combine Morningstar's qualitative insights with quantitative data for comprehensive analysis.
* Use fair value estimates as one input in your investment process, not the sole decision factor.
* Consider economic moat ratings when evaluating long-term investment quality.
* Request individual security data separately for accurate results.
* Note that research content reflects Morningstar's analytical views, not real-time market consensus.
* Be aware that data is retrieved one security at a time, so complex portfolio analyses may take multiple steps.
* Remember that Morningstar's ratings and estimates are based on fundamental analysis and may differ from market sentiment.

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
