<!-- source: https://claude.com/resources/use-cases/genomic-data-analysis -->

Life Sciences

Professional

Connectors

Extended Thinking

# Genomic data analysis

With Claude as your research partner, analyze gene expression data to identify patterns and form testable hypotheses about biological mechanisms, while Claude handles the computational heavy lifting of bioinformatics and literature synthesis.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Life Sciences
* Model

  Sonnet 4.5
* Features

  Connectors

  Extended Thinking
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/genomic-data-analysis

1

## Describe the task

Claude's ability to process large datasets and search scientific literature, combined with your domain expertise, lets you move from raw data to validated hypotheses in a fraction of the time it would take manually.

Share your genomic data with Claude and describe what you want to explore. Claude can analyze differential expression patterns, create visualizations, and search scientific databases to contextualize your findings.

My colleagues recently published the attached single-cell dataset that describes gene expression differences between adult and pediatric liver samples with a focus on the immune system. I would like to explore these samples but focus on the parenchymal cells and differences between adult and pediatric liver. Can you help me first go through the differentially expressed genes and create a heatmap and then also identify pathways or sets of genes that are enriched in each sample?

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

To help Claude analyze your genomic data effectively, you'll need to [provide your datasets](https://support.claude.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude) and optionally [connect to research databases.](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory)

## Required context

Upload CSV or TSV files containing differential expression results, normalized counts, or other quantitative genomics data. Click the (+) button in the chat bar to browse through your files, or alternatively, drag and drop files into the chat box area.

Use connectors to give Claude access to research databases. You can browse through a [variety of tools](https://claude.com/partners/mcp) from trusted partners, built for Model Context Protocol, or [add custom ones](https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp). Keep in mind, some connectors are only available using [Claude for Desktop](https://www.claude.com/download).

Claude can then use your genomic data files to perform computational analysis and generate visualizations.

No items found.

Differential expression data files

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

CSV

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

Differential expression data files

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

CSV

## Optional context

Enable [Extended thinking](https://www.anthropic.com/news/visible-extended-thinking) for Claude to think through more complex tasks, like creating analysis reports and visualizations.

Extended Thinking

3

## What Claude creates

Claude examines your datasets, performs pathway enrichment analysis, creates visual representations of gene expression patterns, and identifies key biological processes enriched in each condition.

From Claude

I'd be happy to help you analyze these differentially expressed genes between adult and pediatric liver parenchymal cells! Let me start by examining the datasets you've uploaded.

Perfect! I can see we have two datasets:

Pediatric-enriched genes: 2000 genes with positive log fold changes  
Adult-enriched genes: 818 genes with positive log fold changes

Now let me create a comprehensive analysis including:

1. A heatmap visualization of top differentially expressed genes
2. Pathway enrichment analysis for both conditions

Excellent! I've completed a comprehensive analysis of the differentially expressed genes between adult and pediatric liver parenchymal cells. Here's what I found:

**Key Findings:**

**Dataset Overview:**

* Pediatric-enriched: 1,999 genes with significantly higher expression
* Adult-enriched: 817 genes with significantly higher expression

**Top Pediatric-Enriched Genes:**

The most striking pediatric markers show extremely high fold changes (15-25 log2FC):

* KCNA5 (voltage-gated potassium channel) - 24.9 log2FC
* HSPB7 (heat shock protein) - 24.7 log2FC
* MYOZ1 (muscle development) - 24.3 log2FC
* HAPLN2 (ECM proteoglycan) - 8.7 log2FC
* CASQ2 (cardiac calcium sequestration) - 8.1 log2FC

**Top Adult-Enriched Genes:**

Adult liver shows moderate enrichment (4-5 log2FC) in mature metabolic functions:

* APOA4 (lipid metabolism) - 5.3 log2FC
* CYP2A7 (drug metabolism) - 4.6 log2FC
* CHI3L1 (inflammatory marker) - 4.4 log2FC
* F9 (coagulation factor IX) - 4.1 log2FC
* CYP3A4 (primary drug metabolizing enzyme) - 3.6 log2FC

**Pathway Enrichment Analysis:**

**Strongly Pediatric-Biased (>75%):**

* Cardiac/Smooth Muscle (89% pediatric) - developmental contractile machinery
* Muscle/Contractile proteins (86%) - cytoskeletal maturation
* Extracellular Matrix (85%) - tissue remodeling
* Chemokines/Cytokines (81%) - immune recruitment
* Heat Shock Proteins (80%) - stress response/development
* Coagulation/Blood (78%) - hemostasis development

**Strongly Adult-Biased (>75%):**

* CYP450/Drug Metabolism (87% adult) - mature xenobiotic processing
* Secreted Proteins (83%) - hepatic synthetic function
* Lipid Metabolism (80%) - mature lipid homeostasis
* Glucose Metabolism (67%) - gluconeogenesis capacity
* Ion Channels/Transport (65%) - mature hepatocyte function

**Biological Insights:**

**Pediatric liver is characterized by:**

* Strong developmental programs (muscle, ECM, contractile proteins)
* Active tissue remodeling and growth
* Elevated stress response (HSPs)
* Immune system recruitment signatures
* Immature metabolic capacity

**Adult liver demonstrates:**

* Mature metabolic specialization (CYP450s, lipid/glucose metabolism)
* Established synthetic functions (coagulation factors, complement)
* Reduced developmental signaling
* Functional hepatocyte differentiation

**Files Generated:**

* View heatmap - Top 50 genes from each group
* View pathway analysis - Pathway enrichment comparison
* View detailed summary - Gene statistics
* View full pathway analysis - Complete pathway details
* View pathway summary table - Summary statistics

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Literature validation

Claude can search [PubMed](https://claude.ai/directory/81cc5080-a204-4aa1-a694-fa868a3c8721) to distinguish which of your findings are well-documented in literature versus novel discoveries, helping you identify the most promising avenues for further research.

I'd like to focus on the extracellular matrix and its remodeling or function in the pediatric liver. I want to understand what is expected in these findings vs. what is new. Can you look at the ECM and remodeling proteins and explore the literature in PubMed to clarify citations of well-understood matrix proteins in the pediatric liver v. ECM components that do not currently have known functions in developmental or pediatric liver?

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Connect [PubMed](https://claude.ai/directory/81cc5080-a204-4aa1-a694-fa868a3c8721) for real-time literature integration

When Claude is connected to PubMed, it can access actual papers, extract specific experimental details, and find citations you might miss. This turns literature review from a multi-day task into a conversation. Claude provides reference links to all the articles it mentions, including identifying specific sections that you can deep dive on your own for further review.

### Build your analysis incrementally

Start with exploratory data analysis and visualization, review the patterns, then dive deeper into specific pathways. This checkpoint approach lets you steer the analysis toward the most interesting findings rather than trying to do everything at once.

### Ask Claude to show its computational methods

Request "show me the code" or "explain your analytical approach" to verify Claude is using appropriate statistical methods for your data type. This builds confidence in results and helps you explain your analysis to reviewers.

### Continue working in your files

The files Claude creates are fully editable. Download the heat maps, pathway comparisons, and summary documents to continue working in your preferred tools.

## Ready to try for yourself?

Whether you're exploring differential expression, validating findings against literature, or designing follow-up experiments, Claude can handle the computational heavy lifting while you focus on the creative work of scientific discovery.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69161dc3e1f05e75f279107b_Screenshot%202025-11-13%20at%2010.03.54%E2%80%AFAM.png)

Open artifact in new window

[Open artifact in new window](#)Open artifact in new window

## Related use cases

[Preclinical study analysis](/resources/use-cases/preclinical-study-analysis)Preclinical study analysis

Preclinical study analysis

Use case

[Use case](/resources/use-cases/preclinical-study-analysis)Use case
