<!-- source: https://claude.com/resources/tutorials/using-the-tooluniverse-extension-in-claude -->

# Using the ToolUniverse Extension in Claude

  Life Sciences
* Product
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/using-the-tooluniverse-extension-in-claude

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The ToolUniverse MCP gives Claude access to a library of 600+ vetted scientific tools to explore large hypothesis spaces, compare competing hypotheses, and iterate through fast-to-slow cycles of analysis. This article explains how to set up and use the ToolUniverse integration with Claude.

The ToolUniverse integration is available as a desktop extension in the Claude Desktop App ([download here](https://claude.ai/download)), and it relies upon Claude's ability to use [local connectors via a desktop extension](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop).

## **About the ToolUniverse integration**

ToolUniverse is an ecosystem for building AI scientists and AI agents for science that work with researchers to generate hypotheses, turn them into executable research plans, run scientific tools, and continually update analyses. It targets research at scale to reimagine scientific discovery: AI scientists explore large hypothesis spaces, compare competing hypotheses, and iterate through fast-to-slow cycles of analysis instead of producing one-off summaries.

ToolUniverse standardizes tool use. It lets AI scientists discover and execute tools via local Python functions and remote services served through MCP. This design makes every step inspectable: AI scientists compose end-to-end workflows that connect datasets, models, and analysis pipelines and record inputs and outputs before they choose the next action. In human-AI collaboration, ToolUniverse supports a continuous loop of hypothesis generation, information-seeking tool calls, execution of research objectives, and refinement of internal models as new experimental data arrive and insights are generated.

## **Data sets and services available in this integration**

**Disclaimer from ToolUniverse:** ToolUniverse provides access to third-party scientific databases and services. All copyrights and intellectual property rights for the data, content, and services listed below belong to their respective original sources and owners. ToolUniverse acts solely as an integration platform and bears no responsibility for the accuracy, completeness, or continued availability of these external resources.

ToolUniverse provides access to a comprehensive ecosystem of scientific resources:

**Biological Databases and Biological Foundation Models**

* UniProt - Complete protein knowledge database
* Ensembl - Genomic data and annotations
* RCSB PDB - Protein structure database
* ChEMBL - Bioactive molecules and drug discovery database
* NCBI databases - GenBank, RefSeq, SNP database
* Gene Ontology - Biological process, function, and location annotations
* ESM - Protein language models
* TranscriptFormer - Single-cell foundation models

**Chemical and Drug Databases**

* PubChem - Chemical structures and biological activities
* DrugBank - Drug and drug target database
* ChEMBL - Bioactive drug-like small molecules
* FDA databases - Drug approval, drug prescribing information, adverse events, drug indications and contraindications, drug interactions
* ClinicalTrials.gov - Clinical trial information

**Literature and Knowledge Bases**

* PubMed - Biomedical literature database
* Semantic Scholar - AI-powered literature analysis
* Europe PMC - Open access biomedical literature
* OpenAlex - Comprehensive scholarly works database
* Crossref - DOI registration and metadata
* OpenTargets - Insights for systematic drug target selection

**Genomic and Health Data**

* GTEx - Tissue-specific gene expression
* GWAS Catalog - Genome-wide association studies
* ClinVar - Genetic variation and disease relationships
* OMIM - Online Mendelian Inheritance in Man
* TCGA - Cancer genomics data

**Research Tools and APIs**

* OpenTargets - Target-disease associations
* STRING - Protein-protein interaction networks
* KEGG - Pathway and disease information
* Reactome - Biological pathway database
* InterPro - Protein families and domains

**AI Models, AI agents, Foundation and Generative Models, Visualizations and Scientific Workflows**

* AlphaFold - Protein structure prediction
* BLAST - Sequence similarity searching
* ADMET-AI - Drug property prediction models
* ChemTools - Chemical informatics utilities
* Visualization tools - Molecular and data visualization

‍

## **Who should use the ToolUniverse integration**

**Research Scientists and Academics**

Accelerate hypothesis generation, automate literature reviews, perform complex multi-database analyses, and scale research capabilities to emerging experimental and AI-human collaboration platforms.

**Pharmaceutical and Biotech Companies**

Streamline drug development pipelines, enhance target identification, improve compound design and optimization, virtual drug screening, and accelerate report generation and target assessment, de-risking and validation.

**Healthcare Organizations**

Power precision medicine initiatives, support clinical trial design and optimization with patient selection, facilitate pharmacogenomics research, and improve patient stratification strategies, extract prognostic and predictive biomarkers from multimodal healthcare datasets.

**Data Scientists, ML Engineers, Platform and Infrastructure Engineers**

Access to domain-specific tools without custom development, rapid prototyping of AI agents for science, and integration of scientific data into ML workflows.

**Government and Regulatory Agencies**

Enhanced regulatory decision-making, improved adverse event analysis, accelerated drug approval processes, and comprehensive safety monitoring.

## **Who can access the ToolUniverse integration**

ToolUniverse is open source under the Apache License 2.0, allowing free access to all features in ToolUniverse. The source code is available on [GitHub](https://github.com/mims-harvard/ToolUniverse).

More details on accessing the integration can be found in [ToolUniverse’s MCP Server Documentation](https://github.com/mims-harvard/ToolUniverse).

‍

## **Setting up the ToolUniverse integration**

The ToolUniverse integration is available as a desktop extension in the Claude Desktop App ([download here](https://claude.ai/download)). For Organization Owners (Team and Enterprise), setting up the integration involves making the extension available to your organization. For individual users, setting up the integration involves installing the extension from inside the Claude Desktop App.

‍

**For Organization Owners (Team and Enterprise)**

*If your organization uses the Desktop Extension Allowlist (i.e., restricts which Desktop Extensions users can access)…*

1. Navigate to Admin settings > Connectors
2. Click “Desktop” tab at the top
3. Confirm that “Allowlist” it toggled **on**
4. Click the “Browse” button
5. In the search field, type “**ToolUniverse**”
6. Click on ToolUniverse
7. Click “Add to your team”
8. Instruct your team to download the [Claude Desktop App](https://claude.ai/download) to access the integration by following the instructions below for Individual Claude Users

*If your organization does not use the Desktop Extension Allowlist (i.e., does not restrict which Desktop Extensions users can access)…*

1. Navigate to Admin settings > Connectors
2. Click “Desktop” tab at the top
3. Confirm that “Allowlist” it toggled **off**
4. If the Allowlist is toggled off, all users in your organization will already be able to access the Desktop Extension directory using the instructions below for Individual Claude Users

**For Individual Claude Users**

1. Download the [Claude Desktop App](https://claude.ai/download)
2. In the Claude Desktop App, navigate to Settings > Extensions
3. Click “Browse extensions”
4. Click “**ToolUniverse**”
5. Click “Install”

Learn about [installing desktop extensions from the directory](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop).

**For Claude Code Users**

1. Command: /plugin marketplace add anthropics/life-sciences
2. Command: /plugin install tool-universe@life-sciences
3. Restart Claude Code
4. Verify that the server is connected with /mcp

Technical details of the ToolUniverse integration can be found in [ToolUniverse’s MCP Server Documentation](https://github.com/mims-harvard/ToolUniverse).

‍

## **Example use cases**

**Drug Discovery and Therapeutic Development**

* Therapeutic discovery and target-to-candidate workflows
* **Sample Prompt:** “*Identify targets for hypercholesterolemia, prioritize one using evidence from OpenTargets and literature, then screen known drugs and close analogs, and rank candidates by predicted binding and ADMET tradeoffs. Provide intermediate evidence and a final shortlist.*”
* **Workflow:** ToolUniverse-powered AI scientists:   
  + Query disease-target associations using OpenTargets API
  + Retrieve protein structures from RCSB PDB
  + Analyze molecular interactions with ChEMBL compound data
  + Predict binding affinities using integrated ML models
  + Generate research hypotheses for therapeutic development

‍

**Human Genetics and Genomic Research**

* Human genetics to mechanism (variant-to-gene-to-pathway)
* **Sample Prompt:** “*From GWAS hits for type 2 diabetes, map variants to candidate genes, summarize functional annotations and tissue expression, and return enriched pathways with supporting references and links to primary sources.*”
* **Workflow:** ToolUniverse-powered AI scientists:   
  + Search GWAS catalog for disease-associated genetic variants
  + Map SNPs to genes using Ensembl and NCBI databases
  + Retrieve functional annotations from Gene Ontology
  + Analyze tissue-specific expression using GTEx data
  + Identify biological pathways using KEGG and Reactome

‍

**Literature and Multimodal Evidence Synthesis**

* **Sample Prompt:** “*Search PubMed and Europe PMC for recent CRISPR off-target detection methods, extract key experimental settings and reported failure modes, and produce a structured comparison table with citations.*”
* **Workflow:** ToolUniverse-powered AI scientists:   
  + Multi-database literature searches (PubMed, Europe PMC, bioRxiv)
  + Automated paper summarization and key finding extraction
  + Citation network analysis using Semantic Scholar
  + Trend identification through temporal analysis
  + Cross-referencing with clinical trial data from ClinicalTrials.gov

‍

**Chemical and Molecular Analysis**

* **Sample Prompt:** "*Using ToolUniverse's OpenFDA and ADMET-AI tools, analyze the molecular properties of FDA-approved drugs for hypertension, predict their ADMET profiles, and identify potential side effect patterns.*"
* Workflow: ToolUniverse-powered AI scientists:   
  + Query FDA drug databases for approved medications
  + Calculate molecular descriptors and properties
  + Predict pharmacokinetic profiles using ADMET-AI models
  + Analyze structure-activity relationships
  + Identify potential drug repurposing opportunities

‍

**Scientific Discovery and Automation for Multi-Tool Studies**

* **Sample Prompt:** "*Build a reusable workflow that runs multiple literature searches in parallel, consolidates results, and produces a reproducible report. Return the workflow as a composed tool with clear inputs and outputs. Using ToolUniverse's UniProt, PRIDE, and KEGG pathway tools, design a complete proteomics workflow: from protein identification using mass spectrometry data to functional analysis and pathway mapping.*"
* **Workflow:** ToolUniverse-powered AI scientists:   
  + Integrate multimodal proteomics databases (UniProt, PRIDE)
  + Automate data processing and quality control of proteomics readouts
  + Annotate protein functions and perform pathway analysis
  + Complete statistical analyses and generate interactive visualizations
  + Generate reports with summaries

‍

## **Demos and Documentation**

**Live Demonstrations**

* **Interactive Web Platform:** [AIScientist.Tools](https://aiscientist.tools) - Live tool discovery and execution interface for exploring 700+ scientific tools
* **Video Demonstrations:** Available on [YouTube](https://www.youtube.com/watch?v=fManSJlSs60)
* **GitHub Repository:** [ToolUniverse on GitHub](https://github.com/mims-harvard/ToolUniverse) - Complete source code, documentation, and community with 797+ stars

‍

**Documentation and Tutorials**

Documentation is available at [ToolUniverse Documentation](https://zitniklab.hms.harvard.edu/ToolUniverse/) covering installation, usage, and advanced features, including a quick start tutorial for 5-minute setup and immediate experimentation with scientific tools, and guides for integration with large language models, AI agents, and reasoning models.

‍

**Community Resources**

Access community resources through our [Slack Community](https://join.slack.com/t/tooluniversehq/shared_invite/zt-3dic3eoio-5xxoJch7TLNibNQn5_AREQ) for peer support and collaboration, and [GitHub Issues](https://github.com/mims-harvard/ToolUniverse/issues) for reporting bugs and requesting features.

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
