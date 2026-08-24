<!-- source: https://academy.claude.com/use-cases/draft-investment-memos -->

Loading

## 1. Describe the task

Claude can connect directly to your financial tools, letting you query using natural language and receive analysis with source citations. Instead of opening multiple browser tabs to gather data, copying metrics into spreadsheets, and then formatting a Word document from scratch, you can request the complete workflow in one conversation.

Tell Claude which company you're evaluating, what metrics drive your investment decision, and what deliverable format you need.

I'm evaluating CloudBridge Technologies (ticker: CLDG) for a potential equity investment and need an initial memo for our IC meeting next week.

**Pull the data I need:** Using Daloopa, get CloudBridge's revenue, operating margins, and free cash flow for the last 12 quarters, plus their segment revenue breakdowns. Using Kensho, identify who CloudBridge lists as competitors in their SEC filings and pull revenue growth and margins for those competitors. Also get CloudBridge's key business relationships and major customers.

**Analyze this:** Calculate cloud platform segment growth versus overall company growth. Determine free cash flow conversion rate. Compare margins year-over-year. Benchmark CloudBridge against the competitors we identified. Flag customer concentration risks.

**Create a professional investment memo in Word format:** executive summary with recommendation, business overview with segment analysis, financial performance highlighting trends, competitive positioning, valuation assessment, and key risks. Use IC-ready formatting.



Open in Claude

## 2. Give Claude context

Connect your data platforms so Claude produces memos with current data rather than requiring manual metric gathering from multiple sources.

### Required context

Use [connectors(opens in new tab)](https://claude.com/blog/integrations) to give Claude access to financial data providers. Browse through the connector library in your [settings(opens in new tab)](https://claude.ai/customize/connectors) to find tools from [trusted financial partners(opens in new tab)](https://claude.com/partners/mcp).

Set up connections to [Daloopa(opens in new tab)](https://claude.ai/directory/daloopa) for SEC filings and fundamental data, and [S&P Global(opens in new tab)](https://claude.ai/directory/s-p-global) for market intelligence and competitor analysis.

This workflow uses capabilities available to [Claude for Enterprise(opens in new tab)](https://claude.com/blog/claude-for-enterprise) customers. Financial data connectors may require existing subscriptions or licenses with the underlying providers.

![](data:image/svg+xml,%3csvg%20width='24'%20height='25'%20viewBox='0%200%2024%2025'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3crect%20y='0.855469'%20width='24'%20height='24'%20fill='%23012060'/%3e%3cpath%20fill-rule='evenodd'%20clip-rule='evenodd'%20d='M12.7708%203.85547C14.7289%203.85547%2016.6078%204.77652%2017.2919%205.27652V7.17126H16.1077C15.8445%206.43441%2014.8129%204.96073%2012.7919%204.96073C10.5814%204.96076%2010.3552%206.47427%2010.5814%207.01336C11.6081%209.46073%2017.766%2011.5923%2017.766%2016.8818C17.766%2022.1713%2013.7397%2022.8028%2011.9239%2022.8028C10.1081%2022.8028%206.47656%2021.5397%206.47656%2016.8818C6.55551%2012.9344%209.7134%2011.3555%2011.2134%2010.8028C10.1871%209.85547%208.60814%208.51336%208.60814%207.01336C8.60814%205.27653%2010.323%203.85548%2012.7708%203.85547ZM12.2397%2011.6713C10.4239%2012.3818%208.84498%2014.1186%208.84498%2016.8818C8.84498%2019.487%209.79235%2021.7765%2011.9239%2021.7765C13.9766%2021.7765%2015.3187%2020.0397%2015.3187%2016.8818C15.3187%2014.3555%2013.266%2012.3555%2012.2397%2011.6713Z'%20fill='white'/%3e%3c/svg%3e)

Daloopa

[Connect](https://claude.ai/directory/daloopa)

![](data:image/svg+xml,%3csvg%20width='24'%20height='11'%20viewBox='0%200%2024%2011'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.55115%200.792969C5.06304%200.793105%206.9701%201.51652%206.9701%203.55469H5.4574C5.41357%203.09446%204.97109%202.17401%203.55115%202.17383C1.77581%202.17383%201.77576%203.35743%201.77576%203.55469C1.77583%203.75209%202.03857%204.67277%203.68201%204.67285C5.19434%204.67285%206.9701%205.13287%206.9701%207.30273C6.97007%208.02617%206.83743%2010.0645%203.68201%2010.0645C0.920312%2010.0643%20-0.0214425%208.0918%200.000369067%207.10547H1.64295C1.66526%207.65344%202.10464%208.74892%203.68201%208.74902C5.65388%208.74902%205.58828%207.76308%205.58826%207.30273C5.58826%206.84246%205.06332%206.05371%203.68201%206.05371C2.30072%206.05366%200.262138%205.52713%200.262088%203.55469C0.262088%201.58208%202.16996%200.792969%203.55115%200.792969ZM11.1781%200.792969C12.2301%200.793118%2013.676%201.46372%2013.6762%202.83105C13.6762%204.19842%2012.5372%205.11036%2011.9672%205.39551C12.3179%205.76815%2013.1245%206.63208%2013.5453%207.10547C13.8608%206.57946%2013.8518%205.4397%2013.808%204.93555H16.1097V6.05371H15.057C15.0043%207.15811%2014.6405%207.91617%2014.4652%208.15723L16.1097%209.86719H14.2025L13.5453%209.20898C13.2823%209.49389%2012.4404%2010.0643%2011.1781%2010.0645C9.00833%2010.0645%208.15279%208.61776%208.15271%207.30273C8.15271%206.25087%209.20472%205.28639%209.73084%204.93555C9.42394%204.69432%208.81092%203.93553%208.81092%202.83105C8.81109%201.45042%2010.1261%200.792969%2011.1781%200.792969ZM21.2377%200.924805C22.6185%200.924805%2023.9994%202.17419%2023.9994%203.68652C23.9992%205.39592%2022.7499%206.71094%2021.4349%206.71094H18.9369V9.86719H17.3588V0.924805H21.2377ZM10.5199%205.92188C10.1691%206.09741%209.46814%206.61915%209.46814%207.30273C9.46824%208.15745%2010.1919%208.88086%2011.1781%208.88086C11.967%208.88077%2012.559%208.44181%2012.7562%208.22266L10.5199%205.92188ZM18.9369%202.30566V5.26465H21.1068C21.8957%205.26455%2022.4875%204.6725%2022.4877%203.68652C22.4877%203.02903%2022.093%202.30576%2021.1068%202.30566H18.9369ZM11.1781%201.97656C10.9151%201.97656%2010.1254%202.2396%2010.1254%202.96289C10.1254%203.54151%2010.8274%204.16809%2011.1781%204.40918C11.5508%204.2337%2012.2953%203.6991%2012.2953%202.96289C12.2953%202.04264%2011.4414%201.9766%2011.1781%201.97656Z'%20fill='%23D7002B'/%3e%3c/svg%3e)

S&P Global

[Connect](https://claude.ai/directory/s-p-global)

Browse all connectors[Open in Claude](https://claude.ai/customize/connectors)

### Optional context

In the chat settings, make sure [Web Search(opens in new tab)](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search) is turned on for additional context on the company you are evaluating.

Enable [Extended Thinking(opens in new tab)](https://support.claude.com/en/articles/10574485-using-extended-thinking) for better synthesis when combining data from multiple platforms and creating higher-quality document outputs.

[

Web Search](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search)[

Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking)

## 3. What Claude creates

Claude pulls data from Daloopa and S&P Global, calculates growth rates and margins, compares performance across competitors, and generates a professional Word document ready for investment committee review.

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

## 4. Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Show source citations for verification

Get specific platform references and data points for every claim in the memo. Claude can trace every number and claim back to its source, showing you exactly where each piece of information came from.

Cite the exact source for each metric—I need to see platform name, date pulled, and which filing or transcript. Show me where the Q3 revenue number came from, which analyst report supports the margin expansion claim, and the specific competitor data points.



Open in Claude

### Expand on the valuation methodology

Add detailed calculations and assumptions to support your price target. Claude shows the underlying math and how your valuation changes under different scenarios.

Show me the DCF math step-by-step: revenue assumptions, margin projections, discount rate, terminal value. Then create a sensitivity table showing how the target price changes if growth rates or margins differ from base case by 5 percentage points.



Open in Claude

### Transform into presentation format

Convert your written memo into slides for your committee meeting. Claude restructures your content and creates charts to illustrate key findings.

Convert this analysis into a 6-slide PowerPoint: title slide with recommendation, business model overview, competitive comparison with charts, financial performance trends, valuation summary, and investment thesis. Visualize trends with visual elements, like graphs and charts.



Open in Claude

## 5. Tricks, tips, and troubleshooting

### Use specific and clear instructions

Claude has access to vast amounts of financial data when connected to multiple tools and sources. Without specific references in your prompt, you may receive more data than needed or miss specific, critical metrics. Provide clear direction to ensure Claude returns the information required for your analysis, saving time and improving accuracy.

### Download the actual memo, not just the preview

The in-chat preview may not show the final typography, spacing hierarchy, and formatted tables that the document has. Open the file to see—and continue editing—the complete output.

### Match model to task complexity

This example uses Claude Sonnet 4.5, the Claude model best suited for a balance of intelligence, speed, and cost for most use cases. If you need faster iteration (like rapid brainstorming or simple formatting), consider switching to Haiku 4.5, the fastest Claude model with near-frontier intelligence. To learn more about various models, visit our [Model Report(opens in new tab)](https://www.anthropic.com/transparency/model-report).

### Unlock specialized capabilities

In addition to the ability to connect to financial data tools, [Claude for Financial Services(opens in new tab)](https://claude.com/solutions/financial-services) adds expanded services. In addition to financial data connections, receive specialized Skills for institutional-grade analysis and frameworks, such as those for financial analysis or valuation. Also receive expert implementation support through tailored onboarding, training, and best practices.

## 6. Ready to try for yourself?

Financial workflows that once required hours of data gathering and manual document formatting now collapse into focused conversations. Test the approach with one company evaluation to calibrate how Claude handles your specific analytical needs.

I'm evaluating CloudBridge Technologies (ticker: CLDG) for a potential equity investment and need an initial memo for our IC meeting next week.

Pull the data I need: Using Daloopa, get CloudBridge's revenue, operating margins, and free cash flow for the last 12 quarters, plus their segment revenue breakdowns. Using Kensho, identify who CloudBridge lists as competitors in their SEC filings and pull revenue growth and margins for those competitors. Also get CloudBridge's key business relationships and major customers.

Analyze this: Calculate cloud platform segment growth versus overall company growth. Determine free cash flow conversion rate. Compare margins year-over-year. Benchmark CloudBridge against the competitors we identified. Flag customer concentration risks.

Create a professional investment memo in Word format: executive summary with recommendation, business overview with segment analysis, financial performance highlighting trends, competitive positioning, valuation assessment, and key risks. Use IC-ready formatting.

Try in Claude
