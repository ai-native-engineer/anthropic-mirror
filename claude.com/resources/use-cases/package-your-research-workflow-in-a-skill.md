<!-- source: https://claude.com/resources/use-cases/package-your-research-workflow-in-a-skill -->

Professional

Skills

# Package your research workflow using skills

Package your research process into a skill that creates reports without re-explaining your standards every time.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Professional
* Model

  Sonnet 4.5
* Features

  Skills
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/package-your-research-workflow-in-a-skill

1

## Describe the task

Monthly research reports often involve repeatedly explaining the same details: which sources to use for each section, how to write a specific way, specific formatting rules. Skills streamlines your entire research workflow—from sources and formatting to visual elements—ensuring every report consistently meets your standards without the need for constant re-explanation.

Creating this skill takes one conversation. Walk through your report structure section by section, including the sources and formatting to use. Claude packages everything into a skill that triggers automatically whenever you mention research reports.

I want to create a skill for my monthly competitive intelligence reports. These reports follow a specific template with different requirements for each section.

I'm uploading my report template showing the exact structure and spacing. Here's what each section needs:

Section 1 - Executive Summary: Pull from recent web articles about competitors. Format as 4-5 concise bullet points, each under 20 words. Bold key metrics.

Section 2 - Market Landscape: Use web search for analyst reports and industry trends. Write in prose paragraphs, 2-3 pages, professional but accessible tone.

Section 3 - Competitive Analysis: Pull fromuploaded competitor data files. Present as comparison tables with our company highlighted. Include 3-4 key differentiators.

Section 4 - Recommendations: Based on all above sections. Format as numbered list (1-5 items), each with brief rationale. Direct, actionable language.

**Formatting specifics:**

* Headings: Bold, 14pt, dark blue (#1B4F72)
* Body text: 11pt, regular weight, black
* Tables: Light gray headers, alternating row colors
* Add our company logo in the header (I'm uploading the PNG)
* Add my signature image at the bottom of the last page

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

This workflow leverages Claude's [skills](https://www.anthropic.com/news/skills) system. In [Settings > Capabilities > Skills](https://claude.ai/settings/capabilities), make sure code execution and file creation is turned on so you have the ability to create skills.

## Required context

Upload files or past work to serve as examples, templates, or references that Claude can integrate into or reference within the skill. Claude can work with diverse file types, such as those listed [here](https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude).

No items found.

research-brief-reference

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

PDF

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

research-brief-reference

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

PDF

## Optional context

Enable [Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking) in the chat bar for deeper strategic thinking about gathering sources, structuring information and meeting quality standards.

Extended Thinking

3

## What Claude creates

Claude walks you through building the skill, asking questions to capture all the different requirements for each section. After Claude creates your skill package, upload it through chat or in [Settings > Capabilities > Skills](https://claude.ai/settings/capabilities) to make sure it is enabled. The skill activates automatically when you mention competitive intelligence or research reports.

From Claude

I'll help you create a comprehensive skill for your monthly competitive intelligence reports. Let me start by reading the skill creation guide to ensure we follow best practices.

*Reading the skill creator guide to understand best practices for creating this brand guideline…*

### Your Competitive Intelligence Skill is Ready!

I've created a comprehensive skill for generating your monthly competitive intelligence reports with exact formatting and structure. Here's what you're getting:

### **Main Deliverable**

***competitive-intelligence.skill - Install this skill file in Claude***

**Documentation & Examples**

* User Guide - How to use the skill with examples
* Package Summary - Complete overview of what's included
* Sample Report - Example output showing the formatting

#### **What This Skill Does**

The skill generates professional competitive intelligence reports with:

**Four standardized sections:**

* Executive Summary (4-5 bullets, under 20 words each, bold metrics)
* Market Landscape (2-3 pages of prose, analyst reports, trends)
* Competitive Analysis (comparison tables + 3-4 differentiators)
* Recommendations (numbered list with rationale)

**Automated research:**

Web searches for competitor news and industry trends

Google Drive integration for your internal competitor data

Analyst report fetching and synthesis

**Professional formatting:**

* Exact typography (14pt headings, 11pt body, dark blue #1B4F72)
* Styled comparison tables with your company highlighted in yellow
* Company logo in header, signature at bottom
* Proper spacing, colors, and layout

#### **Quick Start**

After installing the skill, just say: "Create my December 2025 competitive intelligence report"

Claude will research, structure, and generate a publication-ready DOCX in ~5-7 minutes.

**Customization**

The skill includes synthetic placeholder assets:

* company\_logo.png - Replace with your actual logo
* signature.png - Replace with your signature

All formatting specs are in references/template.md if you need to adjust the template.

**Key Features**

* Token-efficient - Clean, focused SKILL.md under 500 lines
* Progressive disclosure - Detailed formatting specs in reference files
* Tested scripts - Python DOCX generator works perfectly
* Real research - Integrates web search and Google Drive

**Publication-ready - Professional formatting automatically applied**

The skill follows all best practices from the skill creator guide including workflow-based structure, concrete examples, and proper resource organization.

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Test the skill

Create a new report by simply mentioning the skill to trigger it naturally, all the tedious formatting and source-gathering automated.

I need to begin drafting my October competitive intelligence report. The focus on AI coding assistants.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Update the skill

Adjust formatting for a specific section

The Executive Summary bullets are too long. Update the skill, to make sure to tighten each to under 15 words and make them punchier. Use em dashes for sub-points instead of nested bullets.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Integrate your connectors

Simply tell Claude which tools need to be used in your workflow. Skills can include tools by integrating with any MCP connectors you have connected.

Update my competitive intelligence skill. Pull team insights from #competitive-intel channel slack and reference past reports in Drive for trend comparisons.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### **Inspect the skill files**

Download the ZIP and open SKILL.md. A skill at its core is just a group of files, with the main instructions written in plain markdown showing: which sources go where, formatting rules per section, logo placement. You can have Claude help you make edits or just edit directly if something's wrong.

### **If it doesn't trigger automatically**

If you are having trouble with the skill activating automatically, explicitly mention the skill in your prompt. You can also edit the SKILL.md file to include more context for when the skill should be triggered.

### **Test with a past report first**

Test the skill by having it create an output for a task you've already completed. Compare Claude's output with your own to surface any gaps that you can use to update the skill.

## Ready to try for yourself?

Chat with Claude to easily package your processes and expertise into skills. Start with a workflow you repeat often, and easily invoke the skill at any time, anywhere in Claude.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690b2e2d415e52e8ead346c0_Frame%201430106300.png)

Open artifact in new window

[Open artifact in new window](#)Open artifact in new window

## Related use cases

[Source insights from your tools to build a deck](/resources/use-cases/source-insights-from-your-tools-to-build-a-deck)Source insights from your tools to build a deck

Source insights from your tools to build a deck

Use case

[Use case](/resources/use-cases/source-insights-from-your-tools-to-build-a-deck)Use case

[Evaluate a company from the science to the balance sheet](/resources/use-cases/evaluate-a-company-from-the-science-to-the-balance-sheet)Evaluate a company from the science to the balance sheet

Evaluate a company from the science to the balance sheet

Use case

[Use case](/resources/use-cases/evaluate-a-company-from-the-science-to-the-balance-sheet)Use case

[Build analysis from browser charts and folder data](/resources/use-cases/build-analysis-from-browser-charts-and-folder-data)Build analysis from browser charts and folder data

Build analysis from browser charts and folder data

Use case

[Use case](/resources/use-cases/build-analysis-from-browser-charts-and-folder-data)Use case

[Build a daily briefing across your tools](/resources/use-cases/build-a-daily-briefing-across-your-tools)Build a daily briefing across your tools

Build a daily briefing across your tools

Use case

[Use case](/resources/use-cases/build-a-daily-briefing-across-your-tools)Use case
