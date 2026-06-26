<!-- source: https://claude.com/resources/tutorials/using-the-synapse-org-connector-in-claude -->

# Using the Synapse.org Connector in Claude

Set up and use the Synapse.org integration with Claude to discover biomedical data and explore project structures across the Synapse platform.

  Life Sciences
* Product

  Claude.ai
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/using-the-synapse-org-connector-in-claude

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The Synapse.org integration by Sage Bionetworks allows researchers to discover biomedical data across all of Synapse, see the structure of projects, and retrieve information on their data assets for authorized users. This article explains how to set up and use the Synapse.org integration with Claude to advance your research and analysis workflows.

The Synapse.org integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## What this integration provides

Services include search and (meta)data retrieval services. Data access will be governed by the access controls defined for each project. Some data are publicly available, while others require approval from Synapse’s governance team prior to access.

## Who can access the Synapse.org integration

* Individuals who have a registered Synapse account ([register for free](https://accounts.synapse.org/register1?appId=synapse.org))
* Data access may be subject to use restriction from contributors

More details on accessing the integration can be found in [Synapse’s MCP Server Documentation](https://github.com/susheel/synapse-mcp?tab=readme-ov-file#synapse-mcp-server).

## Setting up the Synapse.org integration

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click “**Synapse.org**”
4. Click “Add to your team”

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Click “Connect”
3. Follow the instructions to authenticate with your Synapse.org account

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

**For Claude Code Users**

1. Command: `/plugin marketplace add anthropics/life-sciences`‍
2. Command: `/plugin install synapse@life-sciences`‍
3. Restart Claude Code
4. Verify that the server is connected with `/mcp`

Technical details of the Synapse.org integration can be found in [Synapse’s MCP Server Documentation](https://github.com/susheel/synapse-mcp?tab=readme-ov-file#synapse-mcp-server).

## Common use cases

* Search for reusable scientific data across all of the Synapse.org platform
  + *“Find RNA-seq datasets related to Alzheimer's disease in Synapse”*
  + *“Search Synapse for single-cell transcriptomics datasets”*
  + *"Find genomic sequencing data for plexiform neurofibromas in the NF Data Portal”*
* Authorized users can see hierarchy of folders, files, tables, datasets within projects to help organize and monitor data assets
  + *“Explain the files and folders in the public AACR Project GENIE project”*
  + *“Give me a quick overview of the data assets in the SEA-AD challenge project with agentic track (syn66496696)?”*
* Get custom metadata of entities in Synapse
  + *“What are the annotations and metadata for file syn4553239?”*
  + *“Show me the custom metadata fields for dataset syn66364675”*
* Get provenance information for entities in Synapse to help understand past data processing
  + *“What's the processing history for file syn51543273?”*
  + *“Show me the data lineage and upstream dependencies for the dataset syn68719289”*

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
