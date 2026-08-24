<!-- source: https://academy.claude.com/tutorials/using-the-benchling-connector-in-claude -->

The Benchling integration connects Claude to Benchling R&D platform data, enabling scientists to ask questions and receive clear summaries with links back to source experiments, notebooks, and structured records—all while maintaining existing access permissions. This article explains how to set up and use the Benchling integration with Claude to advance your R&D workflows.

The Benchling integration relies upon Claude's ability to [use remote connectors(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities).

## **What this integration provides**

When Claude sends a query to Benchling, it can search across the full breadth of a customer’s Benchling environment. This covers experimental results and study data, notebook content such as text and attachments, and structured records like registry items, inventory, and templates. The Benchling integration brings these different data types together to provide a unified answer, saving scientists from having to manually piece information across entries or projects. You can also choose to pull in public literature sources, combining internal and external knowledge in one place. All results follow the same access permissions already set in Benchling, ensuring people only see the data they are meant to.

## **Who should use the Benchling integration**

* **Bench Scientists & Research Associates** - want to quickly find and summarize the right data, whether from Benchling or external sources, and use it to decide on next steps in their experiments.
* **Team Leads & Project Managers** - need concise summaries of ongoing work and alignment with external findings to guide project planning.
* **Computational Biologists & Informatics Teams** - want to ask governance questions and assemble curated datasets from Benchling that can be used for deeper analysis or shared across teams.
* **Program Leads** - need automatically generated reports that combine Benchling study results with external context or public data, giving them a clear view of progress and next steps.
* **R&D Leaders & Executives** - require portfolio-level insights to spot trends across programs and benchmark against public industry data.

## **Who can access the Benchling integration**

Benchling customers who meet the following criteria:

* Benchling AI (Deep Research) enabled in your tenant
* API access (V3 APIs, including AI Agents endpoint)
* Benchling remote MCP enabled for your tenant

No additional setup is required beyond connecting Claude to the Benchling connector and authenticating with your Benchling login credentials.

More details on accessing the integration can be found in [Benchling’s MCP Server Documentation(opens in new tab)](https://help.benchling.com/hc/en-us/articles/40342713479437-Benchling-MCP).

## **Setting up the Benchling integration**

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click “**Benchling**”
4. Click “Add to your team”
5. Get a Server URL from Benchling by clicking the link provided
6. Paste the Server URL into field provided
7. Click “Continue”

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Click “Connect”
3. Follow the instructions to authenticate with your Benchling account

Learn about [finding and connecting tools(opens in new tab)](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory) in Claude.

Technical details of the Benchling integration can be found in [Benchling’s MCP Server Documentation(opens in new tab)](https://help.benchling.com/hc/en-us/articles/40342713479437-Benchling-MCP).

## **Example use cases**

**Cross-Source Comparison:**

Compare the IC50 results from my last two Benchling experiments with recent PubMed articles on AAV stability.



Open in Claude

**Insight Summarization:**

Summarize the key findings from Benchling experiments and highlight how they align with external literature trends.



Open in Claude

**Recommendations:**

Based on our last three in vivo results in Benchling and recent FDA guidance, what should we test next?



Open in Claude

**Portfolio Insights:**

Aggregate results from our top five Benchling programs and highlight which ones are showing the strongest early efficacy signals compared with industry benchmarks.



Open in Claude
