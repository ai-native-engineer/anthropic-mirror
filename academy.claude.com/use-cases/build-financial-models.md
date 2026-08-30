<!-- source: https://academy.claude.com/use-cases/build-financial-models -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Build financial models

Create investment analyses with complete financial models, scenario planning, and risk evaluation.

20 minFinanceClaude.ai

Try in ClaudeCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-kv9emaq4.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-oise4nkg.png)

## 1. Describe the task[](#1-describe-the-task)

Investment analysis means pulling data from research platforms, building financial models, and formatting to firm standards—work that can occupy analysts for days. Claude connects to your data sources and generates working models based on your deal parameters. You review the assumptions and edit directly in Excel with formulas intact, rather than building from scratch.

Tell Claude about your investment opportunity and what your partners need to see. Be specific about the deal parameters, key questions, and timeline.

I'm evaluating MediTech Solutions (healthcare SaaS) and need a complete investment analysis.

Deal structure: $75M growth equity stake at 3.6x ARR entry, exit at 7.0x in year 5. Current metrics are $50M ARR growing 35% with 18% EBITDA margin.

**Get the company financials from Daloopa** - search for MediTech Solutions and pull their historical revenue, EBITDA margins, customer metrics, and growth rates.

**Pull healthcare SaaS comparables from S&P Global** - find public companies in the sector and get their current trading multiples, growth rates, and margin profiles. I need this to validate our 7.0x exit assumption.

**Search the web for healthcare SaaS customer concentration benchmarks** - the company mentioned their top 3 customers represent about 40% of revenue and I need to know if that's typical or concerning for this sector. Also look up recent healthcare SaaS growth trends to stress-test the 35% growth assumption.

**Retrieve our IC template from Box** - search the "IC Templates" folder and use the private equity model format as the structure.

**Key questions to address**: How do returns look if growth slows to 25% or 20%? What does the customer concentration risk mean for our downside scenario? How does our 7.0x exit assumption compare to where public healthcare SaaS companies are trading today?

Create an Excel model with scenarios (base, upside, downside), sensitivity analysis on growth and exit multiple, risk assessment focusing on customer concentration, and a comps table showing where public companies trade. Use sophisticated private equity formatting with premium visual quality, an intentional color scheme, working formulas, frozen panes, and conditional formatting.

Open in Claude

## 2. Give Claude context[](#2-give-claude-context)

Connect your data platforms so Claude conducts research and analysis based on current data rather than requiring manual gathering from multiple sources.

### Required context[](#required-context)

Use [connectors(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) to give Claude access to financial data providers. Browse through the connector library in your settings to find tools from [trusted financial partners(opens in new tab)](https://claude.com/partners/mcp).

Enable connections to [S&P Global(opens in new tab)](https://support.claude.com/en/articles/12220135-using-s-p-global-data-for-financial-analysis), [Daloopa(opens in new tab)](https://support.claude.com/en/articles/12220011-using-daloopa-for-financial-analysis), and [Box(opens in new tab)](https://claude.ai/directory/box) so Claude can access your financial research stack.

![](images/10305e6c71037c9c.svg)

Daloopa

[Connect](https://claude.ai/directory/daloopa)

![](images/890b21cc280f11a8.svg)'%3e%3cmask%20id='mask0_181_11527'%20style='mask-type:luminance'%20maskUnits='userSpaceOnUse'%20x='0'%20y='0'%20width='24'%20height='25'%3e%3cpath%20d='M19.2%200.855469H4.8C2.14903%200.855469%200%203.0045%200%205.65547V20.0555C0%2022.7064%202.14903%2024.8555%204.8%2024.8555H19.2C21.851%2024.8555%2024%2022.7064%2024%2020.0555V5.65547C24%203.0045%2021.851%200.855469%2019.2%200.855469Z'%20fill='white'/%3e%3c/mask%3e%3cg%20mask='url(%23mask0_181_11527)'%3e%3cpath%20d='M24%200.855469H0V24.8555H24V0.855469Z'%20fill='url(%23paint0_linear_181_11527)'/%3e%3cpath%20fill-rule='evenodd'%20clip-rule='evenodd'%20d='M12.1582%2014.6759C11.2427%2014.6759%2010.458%2013.8913%2010.458%2012.9322C10.458%2011.9732%2011.1991%2011.1885%2012.1582%2011.1885C13.0735%2011.1885%2013.8582%2011.9732%2013.8582%2012.9322C13.8582%2013.8913%2013.1172%2014.6759%2012.1582%2014.6759ZM7.1886%2014.6759C6.27316%2014.6759%205.48849%2013.8913%205.48849%2012.9322C5.48849%2011.9732%206.22956%2011.1885%207.1886%2011.1885C8.10405%2011.1885%208.8887%2011.9732%208.8887%2012.9322C8.8887%2013.8913%208.14763%2014.6759%207.1886%2014.6759ZM18.5226%2010.3602C18.7407%2010.0987%2019.1329%2010.0551%2019.3945%2010.273C19.656%2010.4474%2019.7433%2010.8397%2019.5253%2011.1013L17.956%2013.063L19.5253%2015.0247C19.7433%2015.2861%2019.656%2015.635%2019.3945%2015.8529C19.1329%2016.0273%2018.7407%2015.9837%2018.5226%2015.7657L17.1713%2014.1092L15.82%2015.7657C15.6019%2016.0273%2015.2097%2016.0708%2014.9481%2015.8529C14.6865%2015.6785%2014.5993%2015.2861%2014.8173%2015.0247L16.3866%2013.063L14.8609%2011.0577C14.6429%2010.7962%2014.7301%2010.4474%2014.9916%2010.2295C15.2532%2010.0551%2015.6455%2010.0987%2015.8635%2010.3166L17.2149%2012.0168L18.5226%2010.3602ZM4.96538%207.57031C5.27052%207.57031%205.53209%207.83186%205.53209%208.13701V10.6218C6.0116%2010.273%206.57831%2010.0551%207.23219%2010.0551C8.322%2010.0551%209.23745%2010.6654%209.71697%2011.6244C10.1965%2010.709%2011.1119%2010.0551%2012.2017%2010.0551C13.7711%2010.0551%2014.9916%2011.3629%2014.9916%2012.9758C14.9916%2014.5887%2013.7274%2015.8965%2012.2017%2015.8965C11.1119%2015.8965%2010.1965%2015.2861%209.71697%2014.3271C9.23745%2015.2426%208.322%2015.8965%207.23219%2015.8965C5.70645%2015.8965%204.44227%2014.6323%204.44227%2013.0193V8.13701C4.39868%207.83186%204.66023%207.57031%204.96538%207.57031Z'%20fill='white'/%3e%3c/g%3e%3c/g%3e%3cdefs%3e%3clinearGradient%20id='paint0_linear_181_11527'%20x1='12'%20y1='0.855469'%20x2='12'%20y2='24.8555'%20gradientUnits='userSpaceOnUse'%3e%3cstop%20stop-color='%232486FC'/%3e%3cstop%20offset='1'%20stop-color='%230061D5'/%3e%3c/linearGradient%3e%3cclipPath%20id='clip0_181_11527'%3e%3crect%20width='24'%20height='24'%20fill='white'%20transform='translate(0%200.855469)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e)

Box

[Connect](https://claude.ai/directory/box)

![](images/28e67c02d4071cfa.svg)

S&P Global

[Connect](https://claude.ai/directory/s-p-global)

Browse all connectors[Open in Claude](https://claude.ai/customize/connectors)

### Optional context[](#optional-context)

Make sure [Web Search(opens in new tab)](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search) is enabled so Claude can incorporate current market context and historical scenario precedents.

[

Web Search](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search)

## 3. What Claude creates[](#3-what-claude-creates)

Claude pulled financials from Daloopa, analyzed healthcare SaaS comparables from S&P Capital IQ, built three-scenario projections with sensitivity analysis, and formatted the multi-sheet model to match your IC template standards.

I've created your investment analysis model.

**Data sources used:**

* Pulled MediTech's financial history from Daloopa (verified the $50M ARR, 35% growth rate, 18% EBITDA margin)
* Retrieved 7 healthcare SaaS comparables from S&P Global (Veeva, Doximity, Health Catalyst, Phreesia, Certify, NextGen, HealthStream)
* Searched web for healthcare SaaS customer concentration norms - found 40-45% concentration in top 3 customers is common for companies at this scale, though concentration typically decreases as ARR crosses $100M
* Used the "Growth Equity Model Template v3" from your IC Templates folder in Drive

**Model structure:**

* Executive Summary - Deal parameters, three-scenario returns (Bear: 2.2x/17% IRR, Base: 3.0x/25% IRR, Bull: 4.1x/33% IRR), investment thesis, and risk overview
* Financial Model - 5-year projections with blue-text assumption cells, automatic calculations through P&L and cash flows, exit valuation at 7.0x ($225M EV, $146M cash return on $75M invested)
* Scenario Analysis - Three scenarios varying growth (25-45% range), margin expansion (18-24% EBITDA), and exit multiples (5.5-8.5x), plus IRR sensitivity table across 25 combinations
* Risk Assessment - Seven risks mapped: customer concentration (42% in top 3), CMS reimbursement changes, Epic/Cerner competition, platform scalability, key person risk, data security compliance, and market saturation. Each includes likelihood, impact, and mitigation approach
* Comps & Valuation - Public healthcare SaaS companies trading at 4.5x median ARR multiple vs. MediTech's 3.6x entry. MediTech shows 35% growth vs. peer median of 18% and Rule of 40 score of 53 vs. peer median of 28

**Customer concentration finding:** The 42% concentration matches sector norms at this revenue scale. Web research shows similar-sized healthcare SaaS companies typically see this decrease to 25-30% as they cross $100M ARR through customer base expansion.

**Exit multiple assumption:** The 7.0x exit sits above current public comps (4.5x median) but below where faster-growing peers traded 18 months ago (8-10x range). Assumes market multiples recover partially and MediTech's growth premium commands a valuation spread.

All formulas are functional. Color coding follows PE standards (blue inputs, black calculations, green cross-sheet references).

**View your financial model**

## 4. Follow up prompts[](#4-follow-up-prompts)

Continue the conversation with Claude to refine, expand, or explore further.

### Create the IC memo[](#create-the-ic-memo)

Turn your financial model into a written investment recommendation. Claude converts the numbers and analysis into a narrative memo that explains the returns, risks, and why this deal makes sense.

Take the key insights from this model and create an investment memo. Use our standard IC template from Drive. Structure it with these sections: Deal Overview, Investment Thesis, Returns Summary, Key Risks, Recommendation.

Open in Claude

### Validate the growth assumptions[](#validate-the-growth-assumptions)

Check if your projections match reality. Claude researches how similar companies actually grew at this stage and tells you if your forecast is reasonable or too optimistic.

These growth numbers feel optimistic. Pull actual growth trajectories from similar healthcare SaaS companies—either from our portfolio or public comps. Show me year-over-year growth rates for companies that started at $50M ARR. Does our path match reality or are we being too aggressive?

Open in Claude

### Research recent exit multiples[](#research-recent-exit-multiples)

Use [Research(opens in new tab)](https://support.claude.com/en/articles/11088861-using-research-on-claude) to find current transaction data across multiple sources. Research takes a few minutes but delivers a thorough report with verified citations. With financial data connectors enabled, Claude can cross-reference your internal knowledge with external market data.

Find healthcare SaaS exit transactions in the last 18 months for companies in the $50-100M ARR range. What multiples did they actually achieve? How does our 7.0x exit assumption compare to recent deals, not just public trading multiples?

Open in Claude

## 5. Tricks, tips, and troubleshooting[](#5-tricks-tips-and-troubleshooting)

### Keep comps fresh with connected data[](#keep-comps-fresh-with-connected-data)

Once you connect S&P Capital IQ or Daloopa, refresh comparable company multiples without manual updates. Say: "Pull latest healthcare SaaS comps and update the valuation sheet." Your benchmarking stays current as public market multiples shift.

### Work directly in your spreadsheet with Claude[](#work-directly-in-your-spreadsheet-with-claude)

Once Claude creates your financial model, download and open the file in Excel. With [Claude for Excel(opens in new tab)](http://claude.com/claude-for-excel), you can get instant explanations of any formula, test scenarios without breaking dependencies, or trace errors to their source. Claude provides cell-level citations for every calculation. Claude for Excel is currently in beta as a research preview. [Join the waitlist(opens in new tab)](https://www.claude.com/claude-for-excel) to get access.

### Unlock further capabilities[](#unlock-further-capabilities)

In addition to the ability to connect to financial data tools, [Claude for Financial Services(opens in new tab)](https://claude.com/solutions/financial-services) adds expanded services. In addition to financial data connections, receive specialized Skills for institutional-grade analysis and frameworks, such as those for financial analysis or valuation. Also receive expert implementation support through tailored onboarding, training, and best practices.

## 6. Ready to try for yourself?[](#6-ready-to-try-for-yourself)

Connect Claude to your data platforms, point to the deal you're evaluating, and receive working spreadsheets for financial analyses.

I'm evaluating MediTech Solutions (healthcare SaaS) and need a complete investment analysis.

Deal structure: $75M growth equity stake at 3.6x ARR entry, exit at 7.0x in year 5. Current metrics are $50M ARR growing 35% with 18% EBITDA margin.

Get the company financials from Daloopa - search for MediTech Solutions and pull their historical revenue, EBITDA margins, customer metrics, and growth rates.

Pull healthcare SaaS comparables from S&P Global - find public companies in the sector and get their current trading multiples, growth rates, and margin profiles. I need this to validate our 7.0x exit assumption.

Search the web for healthcare SaaS customer concentration benchmarks - the company mentioned their top 3 customers represent about 40% of revenue and I need to know if that's typical or concerning for this sector. Also look up recent healthcare SaaS growth trends to stress-test the 35% growth assumption.

Retrieve our IC template from Box - search the "IC Templates" folder and use the private equity model format as the structure.

Key questions to address: How do returns look if growth slows to 25% or 20%? What does the customer concentration risk mean for our downside scenario? How does our 7.0x exit assumption compare to where public healthcare SaaS companies are trading today?

Create an Excel model with scenarios (base, upside, downside), sensitivity analysis on growth and exit multiple, risk assessment focusing on customer concentration, and a comps table showing where public companies trade. Use sophisticated private equity formatting with premium visual quality, an intentional color scheme, working formulas, frozen panes, and conditional formatting.

Try in Claude

* [1. Describe the task](#1-describe-the-task)
* [2. Give Claude context](#2-give-claude-context)
* [3. What Claude creates](#3-what-claude-creates)
* [4. Follow up prompts](#4-follow-up-prompts)
* [5. Tricks, tips, and troubleshooting](#5-tricks-tips-and-troubleshooting)
* [6. Ready to try for yourself?](#6-ready-to-try-for-yourself)
