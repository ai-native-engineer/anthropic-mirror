<!-- source: https://claude.com/resources/tutorials/using-the-open-targets-connector-in-claude -->

# Using the Open Targets Connector in Claude

  Life Sciences
* Product
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/using-the-open-targets-connector-in-claude

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

This connector provides access to the Open Targets Platform for identifying and prioritizing therapeutic drug targets based on disease associations. This article explains how to set up and use the Open Targets integration with Claude to more quickly explore supporting data and prioritize drug targets and assess disease associations.

The Open Targets integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

‍

## **What this integration provides**

The Open Targets connector provides a purpose-built interface and instruction to access and interpret the data and analyses within the [Open Targets Platform](http://platform.opentargets.org).

The Open Targets Platform is a comprehensive tool that supports systematic identification and prioritization of potential therapeutic drug targets, integrating publicly available datasets to build and score target-disease associations. It also integrates relevant annotation information about targets, diseases/phenotypes, drugs, variants, GWAS and molecular QTL studies, and credible sets as well as their most relevant relationships.

This tool makes the Open Targets Platform GraphQL API accessible as read-only, and includes all sources listed in the [Open Targets Platform documentation](http://platform-docs.opentargets.org).

‍

## **Who should use the Open Targets integration**

* **Target Discovery Scientists:** Identifying novel therapeutic targets
* **Research Directors/Team or Project Leads/Portfolio Managers:** Strategic decision-making and portfolio management
* **Academic researchers at all levels:** contrasting their data against existing data, e.g. viewing associations evidence and prioritization analyses for a list of targets they have generated
* **Bioinformaticians/Data Engineers/Machine Learning Engineers/R&D IT teams:** Integrating Open Targets data with proprietary datasets, building internal data platforms and solutions, training models on biological data

‍

## **Who can access the Open Targets integration**

The Open Targets Platform data available through the connector is available for academic and commercial use. Open Targets Platform is marked with CC0 1.0; this dedicates the data to the public domain, allowing downstream users to consume the data without restriction. For more information, refer to the [Open Targets Platform licensing documentation.](https://platform-docs.opentargets.org/licence)

The connector code itself is licensed with Apache 2.0.

More details on accessing the integration can be found in [Open Targets’ MCP Server Documentation](https://github.com/opentargets/open-targets-platform-mcp).

‍

## **Setting up the Open Targets integration**

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click “**Open Targets**”
4. Click “Add to your team”

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Find “**Open Targets**”
3. Click “Connect”

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

**For Claude Code Users**

1. Command: `/plugin marketplace add anthropics/life-sciences`
2. Command: `/plugin install open-targets@life-sciences`
3. Restart Claude Code
4. Verify that the server is connected with /mcp

Technical details of the Open Targets integration can be found in [Open Targets’ MCP Server Documentation](https://github.com/opentargets/open-targets-platform-mcp).

‍

## **Example use cases**

* **Target Discovery Researcher Studying a Disease**   
  + A neuroscience researcher at a pharmaceutical company’s early discovery team, exploring novel therapeutic targets for Alzheimer’s disease. They need to assess which targets show the strongest evidence of association with the disease and understand the types of supporting evidence. They may then want to further prioritize targets based on the evidence.   
    - Example Prompt: *"What are the top five targets associated with Alzheimer disease?"*
  + The Platform provides a ranked list of targets based on overall association scores and a breakdown of the evidence across multiple data types. From there, they can ask further questions about the targets and the evidence.

* **Statistical Geneticist Browsing Studies**   
  + A statistical geneticist at an academic research institute is investigating genetic variants associated with early onset Alzheimer’s disease. They are reviewing existing genetic evidence for PSEN1 and need to understand what genome wide association studies (GWAS) have been conducted and the most likely causal variants, which populations were studied, and how these findings compare across studies.   
    - Example Prompt: *"Do you have any GWAS evidence for PSEN1? What studies are there?"*
  + The Platform can provide a list of studies and credible sets containing PSEN1 with variant-level information and study metadata, and links to original publications. The user can further query the information in these studies and credible sets.

* **Target Prioritisation Using Safety Data**   
  + A translational scientist on a target selection committee is evaluating potential drug targets for an anti-inflammatory programme. They need to understand the safety profile associated with targeting this protein to inform risk-benefit discussions, including known adverse events and safety issues, evidence from clinical trials, post-marketing surveillance, and genetic studies.    
    - Example Prompt: *"Are there known safety events associated with targeting PTGS2?"*
  + The Platform provides comprehensive safety information from multiple sources, which the user can explore in more detail, and compare information for different targets.

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
