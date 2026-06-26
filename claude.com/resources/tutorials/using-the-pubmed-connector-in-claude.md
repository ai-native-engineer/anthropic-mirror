<!-- source: https://claude.com/resources/tutorials/using-the-pubmed-connector-in-claude -->

# Using the PubMed Connector in Claude

Set up and use Claude's PubMed integration for access to millions of biomedical research articles and clinical studies.

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

  https://claude.com/resources/tutorials/using-the-pubmed-connector-in-claude

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The PubMed integration provides access to millions of biomedical research articles and clinical studies, allowing Claude to access abstracts and full papers to clarify experimental approaches, identify key findings, determine novelty and applicability, and surface specific papers for deeper exploration. This article explains how to set up and use the PubMed integration with Claude to accelerate your research workflows.

The PubMed integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## What this integration provides

The PubMed integration connects Claude directly to the PubMed database maintained by the U.S. National Library of Medicine. With over 36 million citations for biomedical literature, PubMed is the premier resource for medical research, scientific studies, and health information.

This integration allows you to:

* Search for research articles using keywords, authors, journals, or advanced query syntax
* Get complete article metadata including abstracts, authors, publication dates, citations, and links to the full article
* Access full-text articles from PubMed Central (PMC) when available
* Find related articles across NCBI databases
* Match citations to PubMed IDs for verification and referencing
* Convert between ID formats (PMID, PMC ID, DOI)

## Setting up the PubMed integration

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click "**PubMed**"
4. Click "Add to your team"

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Find "PubMed"
3. Click "Connect"

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

**For Claude Code Users**

1. Command: `/plugin marketplace add anthropics/life-sciences`
2. Command: `/plugin install pubmed@life-sciences`
3. Restart Claude Code
4. Verify that the server is connected with `/mcp`

## Using the PubMed MCP with the Messages API

Developers can connect to the PubMed integration directly through Claude's Messages API using the MCP connector. This allows you to build applications that leverage PubMed search capabilities programmatically.

### Requirements

**An Anthropic API key**

The beta header: `anthropic-beta: mcp-client-2025-11-20`

### Setup

> 1. Add the PubMed MCP server to your API request's `mcp_servers` array  
> 2. Reference the server in your `tools` array using an `mcp_toolset` entry  
> 3. Include the required beta header

### Example Request

`import anthropic client = anthropic.Anthropic() response = client.beta.messages.create( model="claude-sonnet-4-5", max_tokens=1000, messages=[{"role": "user", "content": "Find recent papers on CRISPR gene editing in cancer treatment"}], mcp_servers=[{"type": "url", "url": "https://pubmed.mcp.claude.com/mcp", "name": "pubmed"}], tools=[{"type": "mcp_toolset", "mcp_server_name": "pubmed"}], betas=["mcp-client-2025-11-20"] )`

## Common use cases

**Search for Research Articles**

Ask Claude to find articles on biomedical or scientific topics of interest. Example prompts:

* `"Find recent studies about immunotherapy for melanoma"`
* `"Show me research on CRISPR gene editing from the last month"`
* `"Find literature related to a proposal or gene that I am working on"`

**Get Article Details and Metadata**

Retrieve comprehensive information about specific articles. Example prompts:

* `"What are the most cited papers on this topic?"`
* `"Find the most recent papers on this topic and summarize new contributions to the field?"`
* `"Who were the authors for that study?"`
* `"When was that paper published?"`

**Access Full-Text Articles**

For articles available in PubMed Central, retrieve the complete text of the articles to help with your research. Example prompts:

* `"Compare the methods of these two papers"`
* `"What were the shared conclusions across these papers, and where did they differ?"`
* `"Read these papers and help me identify the most important conclusions for my hypothesis"`

**Note:** Only articles in PubMed Central (PMC) have full text available. PubMed might only have access to abstracts of other articles.

**Find Related Articles**

Discover similar research across NCBI databases. Example prompts:

* `"Find similar studies to this one"`
* `"Compare the findings of this study to others in the field"`

**Match Citations to PubMed IDs**

Verify citations and find PubMed IDs from journal references. Example prompts:

* `"Look up this citation: Smith J, Nature 2020, vol 52, page 811"`
* `"Find the PubMed entry for this reference from my bibliography"`
* `"I have a citation from a paper, can you find it in PubMed?"`
* `"I would like to have a discussion about the paper associated with this PMID"`

## Frequently asked questions

**Is the PubMed integration free to use?**

Yes! The integration is free for all Claude users. PubMed is a free public resource provided by the U.S. National Library of Medicine.

**Can I access full-text articles for any paper?**

PubMed only makes the full text of articles available if they are in PubMed Central (PMC). PubMed contains over 36 million citations with abstracts, but PMC contains approximately 8 million full-text articles. Where the full text of an article is not available, Claude can provide relevant metadata (title, authors, abstract) if available, and can also supply a link to the full article for your review.

**How current is the data?**

PubMed is updated daily with new research. The integration provides real-time access to the latest available data from the NCBI databases.

**Does this work with other NCBI databases?**

The integration primarily accesses PubMed and PubMed Central. However, you can discover related data from other NCBI databases (like Gene, Protein, and Nucleotide databases) by asking Claude to find connections. For example:

* `"Find genes associated with this article"`
* `"Show me protein sequences referenced in this paper"`
* `"Are there any nucleotide sequences linked to this study?"`

**Are there any rate limits I should know about?**

Yes, the server has rate limits to comply with NCBI guidelines. If you receive a rate limit message, wait briefly and try again.

**Where does the data come from?**

All data comes from official NCBI sources, but may not reflect the most current/accurate data available from NLM: PubMed (the National Library of Medicine's MEDLINE database), PubMed Central (free full-text archive of biomedical literature), and the NCBI E-utilities API (official programmatic access to NCBI databases).

## Privacy and Data Usage

* The PubMed integration only accesses publicly available research articles
* No personal health information or patient data is accessible through the integration
* Your search queries are used only to retrieve relevant articles
* All data comes from official NCBI sources

## Additional Resources

* PubMed Advanced Search Builder: <https://pubmed.ncbi.nlm.nih.gov/advanced/>
* MeSH Database: <https://www.ncbi.nlm.nih.gov/mesh>
* NCBI E-utilities Documentation: <https://www.ncbi.nlm.nih.gov/books/NBK25501/>

## Need More Help?

If you're experiencing issues with the PubMed integration or have questions not covered here, please [contact Claude support](https://support.claude.com/en/articles/9015913-how-to-get-support) or visit our help center for additional troubleshooting guides.

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
