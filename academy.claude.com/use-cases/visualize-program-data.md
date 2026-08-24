<!-- source: https://academy.claude.com/use-cases/visualize-program-data -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Visualize program data

Transform spreadsheets of program statistics into presentation-ready charts, infographics, and dashboards that tell your impact story visually and help demonstrate program satisfaction to stakeholders.

15 minClaude.ai

Try in ClaudeCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-hed4429w.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-pdsn7leg.png)

![Visualize program data result](https://academy.claude.com/assets/v1/visualize-program-data-j89ybsd7.png)

## 1. Describe the task

Bring your data to life. Claude's ability to analyze patterns in your program data, combined with professional file creation tools, lets you transform raw statistics into visual stories that move stakeholders to action. Instead of presenting numbers in static spreadsheets, you can generate sophisticated dashboards, trend analyses, and impact visualizations that communicate program satisfaction and organizational performance at a glance.

The uploaded CSV contains quarterly metrics for six programs: Youth Nutrition Workshop, Adult Wellness Seminar, Senior Health Education, Community CPR Training, Mental Health First Aid, and Diabetes Prevention Program.

**The data includes:** participants enrolled and completed, completion rates, satisfaction scores (1-5 scale), Net Promoter Scores, pre/post-test averages, knowledge gains, repeat participants, referrals, volunteer hours, and cost per participant.

I need to create a **comprehensive visualization suite** for our board meeting next week. Create:

1. An Excel dashboard with multiple analysis sheets showing program satisfaction trends, learning outcomes, and quarterly comparisons. Use sophisticated formatting with professional color schemes, frozen headers, and clear data hierarchies. Include summary metrics and trend indicators.
2. A PowerPoint presentation (8-10 slides) that tells our impact story visually. Show satisfaction rankings, participation trends, knowledge gains by program, and key insights. Use premium design with charts that are immediately readable.

The board cares most about program satisfaction, completion rates, and demonstrable learning outcomes. They want to see which programs perform best and where we're improving quarter over quarter. Make the visualizations clear enough for quick comprehension but detailed enough to support strategic decisions.

Design these with consulting-firm quality and use colors that feel professional but warm (we're a health nonprofit, not a corporate consultancy).

Open in Claude

## 2. Give Claude context

Connect your data sources and enable key features. Provide your program data so Claude can identify patterns, calculate key metrics, and create visualizations that highlight your most important outcomes. Claude will identify missing values, inconsistent formats, and outliers, then suggest fixes before visualization.

Upload your program data as a XLSX or CSV file with columns for metrics you track. Include time periods (quarters, months, years), program names, and the specific measurements that matter to your stakeholders. The more complete your data, the richer Claude's analysis and visualizations.

### Required context

In addition to the raw data files containing the information you are looking to analyze and discuss, enable the [Google Drive integration(opens in new tab)](https://support.claude.com/en/articles/10166901-using-the-google-drive-integration) to provide Claude with more information.

Click the (+) button in the chat bar to browse files that contain additional information you may want to include:

* Context about your audience Board members? Funders? Staff? This shapes visualization complexity and emphasis
* Your key questions: What decisions will these visualizations inform? What patterns do you want to surface?

Enable [Extended Thinking(opens in new tab)](https://www.anthropic.com/news/visible-extended-thinking) to improves how Claude analyzes patterns across multiple programs and time periods, resulting in more sophisticated dashboard designs

Make sure code execution and file creation is enabled in [settings(opens in new tab)](https://claude.ai/settings/capabilities). This is essential for creating working Excel dashboards with formulas, charts, conditional formatting, and interactive elements.

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Google Drive

[Connect](https://claude.ai/directory/google-drive-drivemcp)

Browse all connectors[Open in Claude](https://claude.ai/customize/connectors)

![](https://academy.claude.com/surfaces/excel-icon.svg)

Program Data and Metrics 2024XLSX

![](data:image/svg+xml,%3csvg%20viewBox='0%200%2016%2016'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='m1.846%2012.624.64%201.104c.133.233.324.415.548.548l2.284-3.953H.75c0%20.258.066.515.199.748l.897%201.553Z'%20fill='%230066DA'/%3e%3cpath%20d='M8%205.672%205.716%201.72a1.54%201.54%200%200%200-.548.548L.949%209.576a1.53%201.53%200%200%200-.199.747h4.568L8%205.672Z'%20fill='%2300AC47'/%3e%3cpath%20d='M12.966%2014.276c.225-.133.415-.315.548-.548l.266-.457%201.27-2.2a1.5%201.5%200%200%200%20.2-.748h-4.568l.972%201.91%201.312%202.043Z'%20fill='%23EA4335'/%3e%3cpath%20d='M8%205.672%2010.284%201.72a1.5%201.5%200%200%200-.748-.2H6.464a1.5%201.5%200%200%200-.748.2L8%205.672Z'%20fill='%2300832D'/%3e%3cpath%20d='M10.682%2010.323H5.318l-2.284%203.953c.224.133.482.2.747.2h8.438c.265%200%20.523-.075.747-.2l-2.284-3.953Z'%20fill='%232684FC'/%3e%3cpath%20d='m12.941%205.922-2.11-3.655a1.54%201.54%200%200%200-.547-.548L8%205.672l2.682%204.651h4.56a1.5%201.5%200%200%200-.2-.747L12.94%205.922Z'%20fill='%23FFBA00'/%3e%3c/svg%3e)

Board Presentation Context and Audience NotesDOC

![](https://academy.claude.com/surfaces/excel-icon.svg)

Program Data and Metrics 2024XLSX

## 3. What Claude creates

Claude analyzes your program data to identify trends, calculate performance metrics, and create a comprehensive visualization suite tailored to your stakeholder needs.

Here's what I've created for your board presentation:

1. **Excel Dashboard:** Wellness\_Reach\_Program\_Visualization\_Suite.xlsx

* Executive Dashboard with annual key metrics and top performers
* Program Data sheet with all source data, frozen headers, and filters
* Satisfaction Analysis showing trends by program and quarter
* Learning Outcomes with pre/post test comparisons and effectiveness scores
* Quarterly Comparison with growth indicators and trend analysis

2. **PowerPoint Presentation:** Wellness\_Reach\_Impact\_Presentation.pptx

* Title slide and 2024 overview with key metrics
* Program satisfaction rankings (horizontal bar chart)
* Quarterly participation trends (line chart)
* Knowledge gains by program (clustered column chart)
* Top performers showcase with detailed metrics
* Key insights and recommendations slide

Key findings: Your programs achieved a 94% completion rate and 4.7/5.0 satisfaction score across 2,600+ participants. Senior Health Education and Diabetes Prevention Program lead in satisfaction (4.9/5.0). Community CPR Training shows the strongest growth trajectory with 24% enrollment increase from Q1 to Q3. Knowledge gains average 25+ points across all programs, demonstrating measurable learning impact.

## 4. Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Add demographic breakdowns

Understand which communities you're serving most effectively.

Create an additional analysis sheet showing how satisfaction and completion rates vary by participant age group and zip code. This will help us understand which communities we're serving most effectively.

Open in Claude

### Focus on specific programs

Generate a deep-dive analysis for a specific program.

Generate a deep-dive PowerPoint specifically for our Mental Health First Aid program. Show quarterly trends, participant testimonial themes, and compare our results to national certification standards.

Open in Claude

### Leverage Research to Understand Benchmarks

Use Research mode to find nonprofit sector benchmarks for comparison.

Use Research mode to find nonprofit sector benchmarks for our key metrics. I need comparison points for: donor retention rates for organizations in our budget range ($500K-$1M annual), average gift sizes for similar mission areas, and program satisfaction scores for workforce development nonprofits. Then add these benchmarks as reference lines on our existing charts.

Open in Claude

## 5. Tricks, tips, and troubleshooting

### Open the actual files to see full design quality

File previews in chat show basic structure but miss the details that make these outputs impressive. The Excel dashboard contains working formulas, conditional formatting with color scales, frozen header rows for easy navigation, and carefully selected typography that doesn't appear in previews. Download and open both files to experience the full professional quality and continue editing with complete fidelity.

### Treat your first version as a strong foundation, then refine iteratively

Claude's initial outputs establish excellent structure and professional design, but you'll spot opportunities for enhancement once you work with the real files. Request specific improvements: "Tighten the spacing on the trend analysis tab," "Add a chart showing donor acquisition cost over time," or "Include margin notes explaining what each metric means." Each round of targeted feedback produces increasingly polished results.

### Push beyond defaults with specific design direction

Claude defaults to professional but conservative aesthetics. When visual impact matters, request elevated design: "Choose a sophisticated color palette with unexpected combinations that still feel trustworthy," "Use premium typography with strong hierarchy—this should look expensive," or "Design like you're preparing this for a major foundation's investment committee." Including phrases like "consulting-grade quality" or "portfolio-worthy execution" in your prompts activates higher design standards.

### Consider which data stories matter most to different stakeholders

Board members want financial health and risk indicators. Major donors seek impact narratives and return on investment. Grant officers need evaluation data and sustainability metrics. Staff and volunteers respond to program performance and participant feedback. Before finalizing your visualizations, identify your primary audience and emphasize the metrics that resonate with their priorities.

### Build incremental visualization capacity rather than attempting everything at once

Start with a single dashboard covering your most important program or campaign. Get comfortable with regular updates. Let it become part of your quarterly routine. Once that feels effortless, expand to additional programs, more sophisticated analysis, or audience-specific reports. Organizations that try to visualize everything simultaneously often abandon the effort when it becomes overwhelming.

## 6. Ready to try for yourself?

Your program data already contains compelling impact stories. This visualization suite helps you surface those stories in formats that board members can understand at a glance, donors find inspiring, and funders see as evidence of your capacity. Start with the data you have today, see what patterns emerge, then build on that foundation.

The uploaded CSV contains quarterly metrics for six programs: Youth Nutrition Workshop, Adult Wellness Seminar, Senior Health Education, Community CPR Training, Mental Health First Aid, and Diabetes Prevention Program.

The data includes: participants enrolled and completed, completion rates, satisfaction scores (1-5 scale), Net Promoter Scores, pre/post-test averages, knowledge gains, repeat participants, referrals, volunteer hours, and cost per participant.

I need to create a comprehensive visualization suite for our board meeting next week. Create:

1. An Excel dashboard with multiple analysis sheets showing program satisfaction trends, learning outcomes, and quarterly comparisons. Use sophisticated formatting with professional color schemes, frozen headers, and clear data hierarchies. Include summary metrics and trend indicators.
2. A PowerPoint presentation (8-10 slides) that tells our impact story visually. Show satisfaction rankings, participation trends, knowledge gains by program, and key insights. Use premium design with charts that are immediately readable.

The board cares most about program satisfaction, completion rates, and demonstrable learning outcomes. They want to see which programs perform best and where we're improving quarter over quarter. Make the visualizations clear enough for quick comprehension but detailed enough to support strategic decisions.

Design these with consulting-firm quality and use colors that feel professional but warm (we're a health nonprofit, not a corporate consultancy).

Try in Claude

* [1. Describe the task](#1-describe-the-task)
* [2. Give Claude context](#2-give-claude-context)
* [3. What Claude creates](#3-what-claude-creates)
* [4. Follow up prompts](#4-follow-up-prompts)
* [5. Tricks, tips, and troubleshooting](#5-tricks-tips-and-troubleshooting)
* [6. Ready to try for yourself?](#6-ready-to-try-for-yourself)
