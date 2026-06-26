<!-- source: https://claude.com/resources/tutorials/claude-for-financial-services-skills -->

# Six skills for financial service professionals

Introduction to six specialized AI skills for financial professionals including valuation modeling, competitive analysis, research reports, and due diligence.

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

  https://claude.com/resources/tutorials/claude-for-financial-services-skills

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Claude for Financial Services Skills are specialized tools designed to help financial services professionals with key workflows. These Skills provide Claude with targeted capabilities for common financial analysis, research, and document creation tasks, helping you work more efficiently and consistently.

These Skills are in research preview and available exclusively to Claude for Financial Services users who sign up on [our waitlist](https://docs.google.com/forms/d/1HuMMD2JnSXq0LvQ6Y-VUwAIZdNrg5sLXdCpF3CjmjUE/edit). We will periodically review this list and grant interested users access to this feature. If you have an Enterprise plan, you should contact your account manager to receive priority access.

This article provides an overview of six specialized Skills designed for financial services workflows. If you’re looking for information about Skills in general, see [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)

## Prerequisites

**For Enterprise plans:** Owners must first enable both **Code execution and file creation** and **Skills** in Admin settings > Capabilities. Once enabled, individual members can toggle on example skills and upload their own in [Settings > Capabilities](https://preview.claude.ai/settings/capabilities).

**How to enable Skills**

1. Navigate to [Settings > Capabilities](https://claude.ai/settings/capabilities).
2. Ensure that **Code execution and file creation** is enabled.
3. Scroll to the **Skills** section.
4. Toggle individual skills on or off as needed.

Read more about [using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

## Comps analysis with public/private peers

This Skill generates peer benchmarking tables with valuation multiples and operating metrics that auto-refresh with live data.

**What it does:** Creates comprehensive comparative analysis between a target company and selected peers using both public and private company data.

**Suggested data sources:**

* Public company fundamentals (FactSet/CapIQ/Daloopa)
* Private company fundamentals (PitchBook)
* M&A transactions data (PitchBook)

**Key outputs:**

* Excel spreadsheet with peer company financial data and valuation multiples
* Written analysis documenting peer selection rationale and key insights

## Discounted Cash Flow (DCF) modeling

This Skill builds discounted cash flow models with proper WACC calculations, scenario toggles, and sensitivity tables.

**What it does:** Constructs comprehensive DCF valuation models with detailed cash flow projections and scenario analysis.

**Suggested data sources:**

* Public company fundamentals (FactSet/CapIQ/Daloopa)
* Consensus estimates (FactSet)
* Broker research

**Key outputs:**

* Excel DCF model with detailed cash flow projections and valuation
* Sensitivity analysis showing impact of key assumptions
* Executive summary with valuation range and key drivers

## Initiating coverage research

This Skill helps conduct comprehensive company research for initiating coverage, including business model analysis, competitive positioning, and financial performance review.

**What it does:** Produces thorough research reports with investment recommendations, financial models, and valuation analysis for new coverage initiations.

**Suggest data sources:**

* Web search on key company developments
* SEC filings (EDGAR)
* Public company fundamentals (FactSet/CapIQ/Daloopa)
* Earnings transcripts (Aiera)

**Key outputs:**

* Comprehensive initiation report with investment recommendation and price target
* Detailed financial model with projections and valuation analysis
* Executive summary presentation for investment committee review

## Strip profile/business overview creation

This Skill creates concise 1-2 page company summaries for pitch books and buyer lists with key metrics and investment highlights.

**What it does:** Generates professional company profiles with executive summaries, business overviews, financial summaries, and supporting appendices.

**Suggested data sources:**

* Public company fundamentals (FactSet/CapIQ/Daloopa)
* Private company fundamentals & developments (Pitchbook)

**Key outputs:**

* Professional company profile presentation with executive summary
* Business overview document with key metrics and positioning
* Investment thesis summary with growth drivers and risks

## Due diligence data pack creation

This Skill processes data room documents into structured Excel data packs with financials, customer lists, and contract terms.

**What it does:** Extracts and organizes key information from CIMs, offering memorandums, and other due diligence materials into standardized formats.

**Suggested data sources:**

* Due diligence / CIM documents (SharePoint, Egnyte)

**Key outputs:**

* Standardized financial data pack with historical and projected financials
* Executive summary highlighting key investment metrics
* Normalized data for comps analysis and modeling

## Earnings Analysis

This Skill creates professional equity research earnings update reports analyzing quarterly results for companies already under coverage.

**What it does:** Creates fast-turnaround earnings analysis focusing on beat/miss analysis, key metrics, updated estimates, and revised thesis. Generates an 8-12 page document (3,000-5,000 words) including summary tables and charts.

**Suggested data sources:**

* Earnings call transcripts (Aiera)
* Investor presentations (Daloopa, Aiera)
* Public company fundamentals (FactSet/CapIQ/Daloopa)

## How to use these Skills

Claude for Financial Services Skills work automatically when relevant to your task. You don’t need to explicitly invoke them—Claude determines when each Skill is needed based on your request.

For example, if you ask Claude to “Create a DCF model for Company XYZ,” Claude will automatically use the DCF modeling Skill. Similarly, asking for “comps analysis for ABC Corp” will trigger the comps analysis Skill.

To guarantee Claude uses the skill, you are also welcome to explicitly instruct Claude to use the skill. For example, append “please use DCF skill” to the prompt.

## Best Practices

* **Be specific about your requirements:** Clearly state the company name, analysis type, and any specific parameters you need.**‍**
* **Provide context:** Share relevant details like industry, time period, or specific metrics you want to focus on.**‍**
* **Review and refine:** After Claude generates output using a Skill, you can ask for adjustments or additional analysis.**‍**
* **Leverage multiple Skills:** Many workflows benefit from using several Skills together—for example, using the research Skill to initiate coverage, then the DCF Skill for valuation.

## Learn more about Skills

* [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)[‍](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
* [Using Skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)[‍](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
* [How to create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

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
