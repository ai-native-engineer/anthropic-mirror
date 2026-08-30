<!-- source: https://academy.claude.com/use-cases/preclinical-study-analysis -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Preclinical study analysis

Build study reports by connecting to research platforms and compiling data across experiments.

10 minClaude.ai

Try in ClaudeCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-k3y0qtqk.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-kzqqf3fw.png)

## 1. Describe the task[](#1-describe-the-task)

Claude connects directly to research platforms like Benchling, allowing you to query complex experimental data as naturally as asking a colleague. It retrieves data from multiple notebook entries and sources, synthesizes comparisons, and creates polished reports, saving hours of tedious compilation work.

Start by telling Claude what studies you need to compare and what you want to understand about them.

Summarize the study designs for ST042 and ST043 and how they're different, including a table indicating key differences. Link all my notebook entries and sources.

Open in Claude

## 2. Give Claude context[](#2-give-claude-context)

To enable this workflow, you'll need Claude connected to your research data management system, like Benchling or other platforms.

### Required context[](#required-context)

To pull data directly from your Benchling workspace, use the [Benchling connector.(opens in new tab)](https://claude.ai/directory/benchling) This connector requires you to have [Claude for Desktop(opens in new tab)](https://www.claude.com/download).

After connecting, Claude will be able to access your electronic lab notebooks, experimental protocols, and study data.

Benchling

[Connect](https://claude.ai/directory/benchling)

Browse all connectors[Open in Claude](https://claude.ai/customize/connectors)

## 3. What Claude creates[](#3-what-claude-creates)

Claude connects to Benchling's agents to retrieve your study data, then synthesizes a comprehensive summary with key differences highlighted.

Perfect! The research is complete. Here's a comprehensive summary of studies ST042 and ST043:

**Study Overview**

Both ST042 and ST043 are preclinical validation studies evaluating the same LNP003-L006 therapeutic formulation for hepatic phosphoglycerate mutase (PGM) protein restoration. They were run in parallel with identical test articles and analytical methods but used different animal models and dose ranges.

**ST042: Restoring PGM Levels with LNP003**

* Study ID: bfi\_ZWJIMRJbt
* Duration: February 12, 2024 - March 6, 2025
* Animal Model: Apolipoprotein E knockout (Apoe−/−) mice (n=14)
* Study Context: Disease model for atherosclerosis/cardiovascular applications
* Principal Investigator: Cecilia Cheng

**ST043: Efficacy of PGM**

* Study ID: bfi\_1cQtyNuu
* Duration: January 8, 2024 - March 7, 2025
* Animal Model: C57BL/6 wild-type mice (n=12)
* Study Context: Standard efficacy assessment for baseline therapeutic evaluation
* Principal Investigator: Cecilia Cheng

**Key Differences Table**

**How They Differ**

**1. Animal Models**

ST042 used a disease model (Apoe−/− mice) with validated amyloid pathology to assess efficacy in a context relevant to atherosclerosis and cardiovascular translational applications. ST043 used standard wild-type mice to establish baseline therapeutic efficacy without disease confounders.

**2. Dosing Strategy**

ST043 explored higher dose ranges (0.75-1.5 mg/kg) compared to ST042 (0.5-1.0 mg/kg), providing dose-response data across an expanded therapeutic window.

**3. Tissue Collection Scope**

ST042 had more comprehensive tissue collection (64 samples from liver, blood, and spleen), while ST043 had focused collection (14 samples) with enhanced brain tissue analysis for potential neurological applications.

**4. Strategic Purpose**

ST042 validated efficacy in a disease-relevant model, while ST043 provided clean therapeutic signal data for establishing the baseline therapeutic window.

**Shared Elements**

Both studies used:

* Identical LNP003-L006 formulation (bfi\_nQkcz2Zb2)
* Same analytical methods (HPLC, ELISA, histology)
* Oral administration based on body weight
* Three-group design (control, low dose, high dose)
* Same sampling timepoints (D2 T0 and D7)

**Key Documentation**

**ST042 Notebook Entries**

* EXP25000831 - Primary study report
* EXP25000829 - IND application report
* EXP24000468 - HPLC analytical protocol

**ST043 Notebook Entries**

* EXP24000469 - HPLC analytical protocol

**Cross-Study Documentation**

* Comparative analysis template for ST041, ST042, and ST043

**Conclusion**

These complementary studies demonstrate that LNP003-L006 effectively restores hepatic PGM protein levels in both wild-type and disease models, with robust dose-dependent efficacy. ST042's 3.5-fold increase in protein levels between dose groups and peak response of 511 µg/mL validates therapeutic potential in a disease-relevant context, while ST043 confirms activity across higher dose ranges in standard models.

## 4. Follow up prompts[](#4-follow-up-prompts)

Continue the conversation with Claude to refine, expand, or explore further.

### Generate regulatory documentation[](#generate-regulatory-documentation)

After reviewing the study comparison, ask Claude to create a polished report.

From these results, generate a Study Report that I can include in my regulatory submission.

Open in Claude

## 5. Tricks, tips, and troubleshooting[](#5-tricks-tips-and-troubleshooting)

### Connects directly to your source data[](#connects-directly-to-your-source-data)

When you ask Claude to "link all my notebook entries," it queries Benchling's database and retrieves actual entry IDs with clickable links. This maintains full traceability back to raw experimental data, which is essential for regulatory compliance and internal validation.

### Open external links to verify and interact with content[](#open-external-links-to-verify-and-interact-with-content)

Claude provides Benchling notebook URLs (like benchling.com/entry/bfi\_ZWJIMRJbt) so you can click through to review the original experiment protocols, attachments, results, and visualizations. This gives you full context beyond what appears in the summary.

## 6. Ready to try for yourself?[](#6-ready-to-try-for-yourself)

What used to take days of compiling and validating across tools now happens in minutes. Connect Claude to your research platform and start querying your experimental data like you'd ask a colleague—with full traceability and regulatory-ready outputs.

Summarize the study designs for ST042 and ST043 and how they're different, including a table indicating key differences. Link all my notebook entries and sources.

Try in Claude

* [1. Describe the task](#1-describe-the-task)
* [2. Give Claude context](#2-give-claude-context)
* [3. What Claude creates](#3-what-claude-creates)
* [4. Follow up prompts](#4-follow-up-prompts)
* [5. Tricks, tips, and troubleshooting](#5-tricks-tips-and-troubleshooting)
* [6. Ready to try for yourself?](#6-ready-to-try-for-yourself)
