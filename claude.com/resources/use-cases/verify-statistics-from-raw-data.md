<!-- source: https://claude.com/resources/use-cases/verify-statistics-from-raw-data -->

Professional

Research

Extended Thinking

# Verify statistics from raw data

Learn to evaluate published statistics by checking them against raw data.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Research
* Model

  Sonnet 4.5
* Features

  Extended Thinking
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/verify-statistics-from-raw-data

1

## Describe the task

Claude's ability to parse manuscripts while simultaneously running statistical analyses on raw data helps you develop a deeper understanding of how to assess research methods and build critical reading skills you'll use throughout your career.

Ask Claude to examine a paper by extracting every statistical claim and rerunning each analysis on the provided data files. This hands-on verification teaches you what to watch for and helps you understand whether the study's conclusions are supported by its data.

I'm reading this paper that's central to my literature review, and I want to understand it more deeply before citing it extensively. I've got the published manuscript and their supplementary data files.

Can you help me verify their statistical claims? Go through the paper systematically and pull out every p-value, mean, standard error, sample size, and test result they report. Then run each analysis yourself using their actual data.

For each statistical claim, show me three things: what the paper states, what you calculated from their data, and whether these match. Flag any problems you notice - things like using wrong tests for the data type, sample sizes that don't add up, or p-values that seem mathematically questionable.

Then build me a detailed Excel workbook where I can see your complete verification. Create separate sheets for each analysis showing your calculations step by step, plus a summary sheet highlighting any issues I should understand before relying on this work.

Make the spreadsheet well-designed and easy to navigate - professional formatting, frozen headers, filtered columns, and clear notes explaining what you found.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

Provide the published manuscript and its underlying raw data so Claude can verify every statistical claim and help you understand how thoroughly the analysis supports the conclusions.

## Required context

Click the (+) button in the chat bar to browse through your files or, alternatively, drag and drop the manuscript and any additional data files you want to analyze into the chat box area.

No items found.

Manuscript

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

PDF

Data files

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

XSLX

Manuscript

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

PDF

## Optional context

For more thorough statistical verification and high quality outputs, enable [Extended Thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking)**.**

‍

Extended Thinking

3

## What Claude creates

Claude creates a comprehensive audit workbook documenting every statistical check, showing you exactly what to watch for and building your ability to critically evaluate research methods.

From Claude

**Statistical Reproducibility Check Complete**

I've verified the statistical claims in "Effects of Chronic Sleep Deprivation on Spatial Memory and Anxiety-like Behavior in C57BL/6 Mice" against the experimental data. Here's what I found:

**Verification Summary:**

* 31 statistical claims checked
* ✓ 22 verified correctly
* ⚠ 3 minor discrepancies
* ✗ 6 require attention

**Critical Issues to Understand:**

**1. Sample Size Discrepancy (throughout manuscript)**

* Manuscript states: n=12 per group
* Data shows: n=11 for control group
* Implication: This affects the statistical power and validity of all control group comparisons. The paper should have explained any subject exclusions.

**2. Unit Conversion Error (Open Field - Total Distance)**

* Manuscript reports: 2456 ± 234 cm (control), 1834 ± 187 cm (SD)
* Data shows: 24.43 ± 1.8 meters (control), 18.38 ± 1.1 meters (SD)
* Issue: Values off by factor of 100 - data stored in meters but reported as centimeters
* Why this matters: This type of error suggests inadequate data checking, which raises questions about other results

**3. Inappropriate Statistical Test (Corticosterone)**

* Issue: Used unpaired t-test for before/after measurements from same mice
* Should use: Paired t-test accounting for baseline values
* Manuscript p-value: 0.003
* Correct paired test: p<0.001
* Implication: The effect is actually stronger than reported, but the methodological choice shows limited statistical understanding

**4. P-value Precision Errors**

* Target quadrant time: Reports p=0.004, actual p=0.0001
* Day 5 latency: Reports p=0.02, actual p=0.026
* Why this matters: Exact p-values matter for meta-analyses and understanding effect strength

**5. Methods Description Inconsistency**

* Methods state "unpaired t-tests for between-group comparisons"
* Problem: Corticosterone data are paired samples (baseline and final from same mice)
* This suggests either unclear writing or misunderstanding of their own analysis

**View your statistical audit workbook**

‍

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Go beyond numbers and check the figures

Verify that visual representations match the underlying data. Claude compares graphs, charts, and tables to raw data values to catch misrepresentations or errors.

Check that all bar heights, error bars, and data points in Figure 2 match the actual data values. Show me any discrepancies.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Learn what to watch for next time

Claude can explain which red flags are worth investigating when you're reading papers without access to raw data - like methodological inconsistencies, suspiciously round numbers, or statistical choices that don't match study designs.

Based on what we found here, teach me what warning signs I should look for when reading other papers in my field. What patterns suggest I should be skeptical, even when I can't verify the raw data?

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Draft reviewer comments

Frame statistical or methodological issues constructively so authors understand what needs fixing without getting defensive. Claude can help balance specificity with encouragement.

Turn these statistical problems into helpful reviewer comments that are clear about what needs correcting but encouraging about how to fix it.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Start where you already have domain expertise

You'll quickly grasp the best practices for working with Claude by verifying papers in your field, as your expertise will help you discern what is plausible. When Claude flags an issue, your domain knowledge helps you judge whether it's a real error or a misunderstanding of field-specific practice. Conversely, when Claude says everything checks out, you can assess whether it tested the right assumptions.

### Open the actual Excel file

The preview in chat shows structure, but the real workbook contains working formulas, conditional formatting that highlights issues, dropdown filters for exploring results, and detailed calculation notes. Download and open the file to see how verification works and to learn techniques you can apply when checking other papers.

## Ready to try for yourself?

Upload any paper with its supplementary data files, describe why you're examining it ("I'm considering citing this extensively" or "these results seem surprising and I want to understand them better"), and let Claude help you build the critical analysis skills that strengthen your research.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690a7cc0f2944881ea09581a_Screenshot%202025-11-04%20at%202.22.53%E2%80%AFPM.png)

Open artifact in new window

[Open artifact in new window](#)Open artifact in new window

## Related use cases

[Surface themes from all your feedback channels](/resources/use-cases/surface-themes-from-all-your-feedback-channels)Surface themes from all your feedback channels

Surface themes from all your feedback channels

Use case

[Use case](/resources/use-cases/surface-themes-from-all-your-feedback-channels)Use case

[Turn transit time into research time](/resources/use-cases/turn-transit-time-into-research-time)Turn transit time into research time

Turn transit time into research time

Use case

[Use case](/resources/use-cases/turn-transit-time-into-research-time)Use case

[Plan your literature review](/resources/use-cases/plan-your-literature-review)Plan your literature review

Plan your literature review

Use case

[Use case](/resources/use-cases/plan-your-literature-review)Use case
