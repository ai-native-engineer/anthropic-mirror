<!-- source: https://claude.com/resources/tutorials/using-the-benchling-connector-in-claude -->

# Using the Benchling connector in Claude

Set up and use the Benchling integration with Claude to connect to Benchling R&D platform data for experiments, notebooks, and structured records.

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

  https://claude.com/resources/tutorials/using-the-benchling-connector-in-claude

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The Benchling integration connects Claude to Benchling R&D platform data, enabling scientists to ask questions and receive clear summaries with links back to source experiments, notebooks, and structured records—all while maintaining existing access permissions. This article explains how to set up and use the Benchling integration with Claude to advance your R&D workflows.

The Benchling integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

‍

## **What this integration provides**

When Claude sends a query to Benchling, it can search across the full breadth of a customer’s Benchling environment. This covers experimental results and study data, notebook content such as text and attachments, and structured records like registry items, inventory, and templates. The Benchling integration brings these different data types together to provide a unified answer, saving scientists from having to manually piece information across entries or projects. You can also choose to pull in public literature sources, combining internal and external knowledge in one place. All results follow the same access permissions already set in Benchling, ensuring people only see the data they are meant to.

‍

## **Who should use the Benchling integration**

* **Bench Scientists & Research Associates** - want to quickly find and summarize the right data, whether from Benchling or external sources, and use it to decide on next steps in their experiments.
* **Team Leads & Project Managers** - need concise summaries of ongoing work and alignment with external findings to guide project planning.
* **Computational Biologists & Informatics Teams** - want to ask governance questions and assemble curated datasets from Benchling that can be used for deeper analysis or shared across teams.
* **Program Leads** - need automatically generated reports that combine Benchling study results with external context or public data, giving them a clear view of progress and next steps.
* **R&D Leaders & Executives** - require portfolio-level insights to spot trends across programs and benchmark against public industry data.

‍

## **Who can access the Benchling integration**

Benchling customers who meet the following criteria:

* Benchling AI (Deep Research) enabled in your tenant
* API access (V3 APIs, including AI Agents endpoint)
* Benchling remote MCP enabled for your tenant

No additional setup is required beyond connecting Claude to the Benchling connector and authenticating with your Benchling login credentials.

More details on accessing the integration can be found in [Benchling’s MCP Server Documentation](https://help.benchling.com/hc/en-us/articles/40342713479437-Benchling-MCP).

‍

## **Setting up the Benchling integration**

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click “**Benchling**”
4. Click “Add to your team”
5. Get a Server URL from Benchling by clicking the link provided
6. Paste the Server URL into field provided
7. Click “Continue”

‍

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Click “Connect”
3. Follow the instructions to authenticate with your Benchling account

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

Technical details of the Benchling integration can be found in [Benchling’s MCP Server Documentation](https://help.benchling.com/hc/en-us/articles/40342713479437-Benchling-MCP).

## **Example use cases**

* **Cross-Source Comparison:** *“Compare the IC50 results from my last two Benchling experiments with recent PubMed articles on AAV stability.”*
* **Insight Summarization:** *“Summarize the key findings from Benchling experiments and highlight how they align with external literature trends.”*
* **Recommendations:** *“Based on our last three in vivo results in Benchling and recent FDA guidance, what should we test next?”*
* **Portfolio Insights:** *“Aggregate results from our top five Benchling programs and highlight which ones are showing the strongest early efficacy signals compared with industry benchmarks.”*

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
