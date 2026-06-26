<!-- source: https://claude.com/resources/tutorials/using-the-owkin-connector-in-claude -->

# Using the Owkin Connector in Claude

  Life Sciences
* Product
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/using-the-owkin-connector-in-claude

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The Owkin connector powers Pathology Explorer, an Owkin AI agent that transforms H&E pathology slides into queryable insights for drug discovery and development and clinical research. This article explains how to set up and use the Owkin integration with Claude to accelerate pathology-driven research.

The Owkin integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

‍

## **What this integration provides**

Owkin builds AI agents for biology to accelerate drug discovery, de-risk and accelerate clinical trials. The Owkin connector gives Claude access to Pathology Explorer, an Owkin agent that transforms H&E slides from the TCGA database into granular, queryable insights. Researchers can use it to automatically detect cell types from pathology images, spatially analyze tumor micro-environments, and validate hypotheses through cohort-level survival analysis, accelerating and de-risking drug discovery and development.

The Pathology Explorer offers a range of capabilities, allowing Claude to analyze histopathological slides. Below is an extended description of the slide-level features provided by the model.

‍

**Count and density features**

For each cell type (lymphocytes, neutrophils, plasmocytes, fibroblasts, eosinophils, cancer cell), the model provides:

* count\_{cell\_type}: The total number of cells of the specified type detected in the slide.
* global\_density\_{cell\_type}: The density of the specified cell type per unit area of the tissue.

**Morphological features of the nucleus**

For each cell type, the model provides:

* mean\_area\_{cell\_type}: The average area of the nuclei of the specified cell type in the slides.
* mean\_circularity\_{cell\_type}: The average circularity of the nuclei of the specified cell type in the slides.
* mean\_perimeter\_{cell\_type}: The average perimeter of the nuclei of the specified cell type in the slides.

**Spatial organization features**

For three types of regions (tumor, tumor core and tumor core stroma), the model provides for each cell type:

* density\_{cell\_type}\_in\_{region}: The density of the specified cell type within the specified region.

For each region, the model also provides:

* area\_{region}: The area of the specified region in the slide.

In addition, for a selection of biologically relevant cell-cell interactions, the model provides:

* average\_co\_occurrence\_{cell\_type}\_{cell\_type2}\_rad\_20.0um: The average co-occurrence of the two specified cell types nuclei within a radius of 20 micrometers.

The model also computes the tils\_diffusivity, a metric for quantifying the tumor-infiltrating lymphocytes diffusivity for the slide.

‍

**Available cohorts from the dataset**

The features are available on the following TCGA cohorts:

* TCGA\_ACC
* TCGA\_BLCA
* TCGA\_BRCA
* TCGA\_CESC
* TCGA\_CHOL
* TCGA\_COAD
* TCGA\_DLBC
* TCGA\_ESCA
* TCGA\_HNSC
* TCGA\_KICH
* TCGA\_KIRC
* TCGA\_KIRP
* TCGA\_LIHC
* TCGA\_LUAD
* TCGA\_LUSC
* TCGA\_MESO
* TCGA\_OV
* TCGA\_PAAD
* TCGA\_PRAD
* TCGA\_READ
* TCGA\_SARC
* TCGA\_STAD
* TCGA\_THCA
* TCGA\_THYM
* TCGA\_UCEC
* TCGA\_UCS

‍

## **Who should use the Owkin integration**

Pharma researchers and healthcare providers (Research Use Only), for example:

* Translational and immuno-oncology researchers
* Novel drug discovery teams
* Drug development and biomarker discovery teams
* Digital pathology research groups
* Companion diagnostic development groups

## **Who can access the Owkin integration**

Prerequisites to access the connector are:

* An account with access to the K Pro platform ([product page](https://www.owkin.com/k-os/k-pro), [signup page](https://k.owkin.com/auth/signin?utm_source=k-nav-page&utm_medium=owkin-website&utm_campaign=k-nav-acquisition&next=%2Fchat))
* Access to Claude.ai or Claude Desktop

More details on accessing the integration can be found in [Owkin’s MCP Server Documentation](https://docs.owkin.com/mcp-tools-documentation/introduction).

## **Setting up the Owkin integration**

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click “**Owkin**”
4. Click “Add to your team”

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Find “**Owkin**”
3. Click “Connect”
4. Follow the instructions to enter your Owkin credentials to authenticate

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

**For Claude Code Users**

1. Command: `/plugin marketplace add anthropics/life-sciences`
2. Command: `/plugin install owkin@life-sciences`
3. Restart Claude Code
4. Verify that the server is connected with /mcp

Technical details of the Owkin integration can be found in [Owkin’s MCP Server Documentation](https://docs.owkin.com/mcp-tools-documentation/introduction).

## **Example use cases**

* **Refine patient stratification.** Identify patient subgroups that generalist models miss through granular profiling of 6 distinct cell types (including understudied populations like neutrophils and eosinophils). Leverage spatial organization analysis to characterize TME structures and phenotypes beyond simple counts.   
  + Example prompt: *"I'm looking for Lung Adenocarcinoma patients that might be resistant to immunotherapy. Are there cases with low immune infiltration in the TCGA cohort?"*
* **Visualize whole-slide images.** Build confidence in the model output by retrieving whole-slide images directly within the chat interface.   
  + Example prompt: *"Find the slide the most enriched in eosinophils from cohort TCGA\_BRCA and plot it."*
* **Assess prognostic value of H&E based markers.** Test clinical hypotheses by performing survival analysis on your cohorts, by splitting patients based on features such as specific cell densities or spatial scores.   
  + Example prompt: *"Is the density of plasmocytes associated with overall survival in bladder carcinoma?"*
* **Extract quantitative evidence for reproducibility.** Build trust in AI-generated insights by retrieving the underlying raw data for independent verification or downstream analysis.   
  + Example prompt: *"Export the breakdown of all cell types for patient TCGA-A2-A0YI-01Z-00-DX1.1CF2EC2D-C722-467F-8832-409B823E8D8F.svs in parquet format, so I can reproduce this analysis."*
* **Understand Owkin’s Pathology Explorer capabilities and context.** Gain transparency into the model by querying its technical specifications directly. Learn about the supported cell types, the pan-cancer training dataset and more, to ensure the model is appropriate for your research question.

Example prompt: *"Can you provide an overview of Owkin’s Pathology Explorer model and its capabilities?"*

## Related tutorials

[How to use the Nextflow Deployment agent skill with Claude Code](/resources/tutorials/how-to-use-the-nextflow-deployment-agent-skill-with-claude-code)How to use the Nextflow Deployment agent skill with Claude Code

How to use the Nextflow Deployment agent skill with Claude Code

Tutorial

[Tutorial](/resources/tutorials/how-to-use-the-nextflow-deployment-agent-skill-with-claude-code)Tutorial

[How to use the Instrument Data to Allotrope Skill with Claude](/resources/tutorials/how-to-use-the-instrument-data-to-allotrope-skill-with-claude)How to use the Instrument Data to Allotrope Skill with Claude

How to use the Instrument Data to Allotrope Skill with Claude

Tutorial

[Tutorial](/resources/tutorials/how-to-use-the-instrument-data-to-allotrope-skill-with-claude)Tutorial

[How to use the Scientific Problem Selection Skill with Claude](/resources/tutorials/how-to-use-the-scientific-problem-selection-skill-with-claude)How to use the Scientific Problem Selection Skill with Claude

How to use the Scientific Problem Selection Skill with Claude

Tutorial

[Tutorial](/resources/tutorials/how-to-use-the-scientific-problem-selection-skill-with-claude)Tutorial

[How to use the scVI-Tools bioinformatics skill bundle with Claude](/resources/tutorials/how-to-use-the-scvi-tools-bioinformatics-skill-bundle-with-claude)How to use the scVI-Tools bioinformatics skill bundle with Claude

How to use the scVI-Tools bioinformatics skill bundle with Claude

Tutorial

[Tutorial](/resources/tutorials/how-to-use-the-scvi-tools-bioinformatics-skill-bundle-with-claude)Tutorial
