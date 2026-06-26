<!-- source: https://claude.com/resources/tutorials/using-the-chembl-connector-in-claude -->

# Using the ChEMBL Connector in Claude

  Life Sciences
* Product
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/using-the-chembl-connector-in-claude

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The ChEMBL connector gives Claude access to EMBL-EBI's ChEMBL database, a manually curated repository of bioactive molecules with drug-like properties, their biological targets, and quantitative activity measurements. This article explains how to set up and use the ChEMBL integration with Claude to accelerate drug discovery through bioactive compound data.

The ChEMBL integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

‍

## **What this integration provides**

This integration connects Claude to the most recent version of ChEMBL, Europe's leading open-access drug discovery database maintained by the European Bioinformatics Institute (EMBL-EBI). ChEMBL contains over 2 million bioactive compounds, 15+ million activity measurements, and data from 76,000+ scientific publications, making it an essential resource for computational drug discovery, target identification, and pharmaceutical research.

This connector provides six primary tool calls that access different facets of the ChEMBL database.

* **compound\_search** enables users to find molecules by name, ChEMBL ID, or chemical structure (SMILES), returning comprehensive data including molecular properties, synonyms, approval status, and ATC classifications.
* **target\_search** queries biological targets (proteins, enzymes, receptors) by name, gene symbol, or organism, providing protein accessions, Gene Ontology annotations, and cross-references to UniProt and other databases.
* **get\_bioactivity** retrieves quantitative activity measurements (IC50, EC50, Ki, Kd values) for compound-target interactions, including assay descriptions, pChEMBL scores, confidence ratings, and literature references from peer-reviewed journals.
* **get\_mechanism** accesses manually curated mechanism of action data for approved drugs, detailing how compounds interact with their biological targets (e.g., "Cyclooxygenase inhibitor") with action types (INHIBITOR, AGONIST, ANTAGONIST) and supporting references.
* **drug\_search** finds approved drugs and clinical candidates by therapeutic indication using MeSH disease terminology, returning drugs with their development phase, approval dates, and safety warnings.
* **get\_admet** provides calculated molecular properties critical for drug-likeness assessment, including lipophilicity (ALogP), polar surface area, hydrogen bond donors/acceptors, Rule of Five violations, and QED drug-likeness scores.

On the provider side, the connector queries ChEMBL's RESTful API and SQL database containing standardized, manually curated data extracted from medicinal chemistry literature, clinical trials databases, and high-throughput screening campaigns. All bioactivity data includes confidence scores, data validity flags, and full provenance tracing back to original publications.

## **Who should use the ChEMBL integration**

* **Medicinal Chemists:** Design and optimize lead compounds by analyzing structure-activity relationships (SAR), checking molecular properties against drug-likeness criteria, and identifying structural analogs with improved potency or selectivity.
* **Pharmacologists:** Research drug mechanisms of action, identify polypharmacology risks, discover off-target effects, and validate therapeutic targets by examining bioactivity profiles across protein families.
* **Computational Biologists & Cheminformaticians:** Build machine learning models for activity prediction, perform virtual screening campaigns, train QSAR models, and conduct large-scale data mining across chemical space.
* **Drug Discovery Scientists:** Identify validated drug targets, find chemical starting points for hit-to-lead optimization, benchmark competitor compounds, and assess freedom-to-operate by analyzing approved drugs in therapeutic areas.
* **Academic Researchers:** Investigate drug repurposing opportunities, study evolutionary relationships between drug targets, analyze clinical development success rates, and validate findings against established bioactivity data.
* **Pharmaceutical Project Teams:** Conduct competitive intelligence on drug pipelines, analyze endpoints for clinical trial design, assess target tractability, and evaluate ADMET liabilities early in development.

## **Setting up the ChEMBL integration**

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click “**ChEMBL**”
4. Click “Add to your team”

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Find “**ChEMBL**”
3. Click “Connect”

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

‍**For Claude Code Users**

1. Command: `/plugin marketplace add anthropics/life-sciences`
2. Command: `/plugin install chembl@life-sciences`
3. Restart Claude Code
4. Verify that the server is connected with /mcp

‍

## **Example use cases**

**Target-Based Drug Discovery**

* *Scenario: Identifying validated compounds for a therapeutic target of interest*
* *Sample Prompts:*   
  + *“Find all approved kinase inhibitors that target EGFR with IC50 less than 100 nM”*
  + *“What compounds have been tested against the BCL2 protein? Show me the most potent ones with their bioactivity data”*
  + *“Search for GPCR agonists targeting the adenosine A2A receptor and show their mechanism of action”*

‍

**Compound Optimization & SAR Analysis**

* Scenario: Improving lead compound properties by studying structure-activity relationships
* Sample Prompts:

* *“Find structural analogs of imatinib with similarity > 85% and compare their target selectivity profiles”*
* *“What are the ADMET properties for aspirin? Does it pass Lipinski's Rule of Five?”  
  “Show me compounds similar to this SMILES structure: CC(=O)Oc1ccccc1C(=O)O, and compare their bioactivity against cyclooxygenase”*

‍

**Competitive Intelligence & Drug Repurposing**

* Scenario: Analyzing therapeutic landscapes and identifying repositioning opportunities
* Sample Prompts:   
  + *“What are all the approved drugs for treating hypertension? Show their mechanisms of action”*
  + *“Find the mechanism of action for pembrolizumab and identify all other compounds targeting the same protein”*
  + *“Search for approved oncology drugs that also show bioactivity against inflammatory disease targets”*

‍

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
