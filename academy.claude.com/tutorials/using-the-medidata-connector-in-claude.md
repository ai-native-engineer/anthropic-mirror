<!-- source: https://academy.claude.com/tutorials/using-the-medidata-connector-in-claude -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# Using the Medidata Connector in Claude

Set up and use the Medidata integration with Claude to streamline platform support and optimize site selection for clinical trials.

3 minClaude.ai

[Open Claude](https://claude.ai/new)

![](https://academy.claude.com/assets/v1/thumbnail.light-cwnmszwx.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-g8rfr2po.png)

Medidata is a leading provider of clinical trial solutions to the life sciences industry. This article explains how to set up and use the Medidata integration with Claude to streamline platform support and optimize site selection.

The Medidata integration relies upon Claude's ability to [use remote connectors(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities).

## **What this integration provides**

This connector gives Medidata customers the ability to connect Claude to their Medidata platform data. Today, the connector supports two key use cases, and Medidata will continue to add more functionality regularly:

* **Site Ranking:** Allows Medidata's Intelligent Trials customers to predict which sites align with their enrollment goals during their protocol/study planning process. This service gives Claude access to aggregated historical operational enrollment data, population/country data, and standardized site data. This service takes various inputs on the planned phase, indication, etc., and ranks sites based on predicted enrollment rate to help inform the site selection strategy for a disease area of interest or a planned study. Users can then use the predicted sites to perform deeper analysis using Claude.
* **Platform Help:** This service gives Claude access to Medidata’s Knowledge Hub documentation (i.e. documentation and FAQs on Medidata’s products) around how to use the various products available in the Medidata platform. Claude users will be able to ask and query to find the answers to their questions about the platform, and integrate that information with their own internal documents/policies.

## **Who should use the Medidata integration**

* **Clinical Feasibility Lead / Strategist:** Define global site criteria and analyze historical data to determine optimal patient access. Craft the initial feasibility survey instruments and validate that the proposed site list aligns with specific recruitment goals and protocol requirements.
* **Study Manager:** Review final site recommendations to ensure the geographic footprint remains balanced and cost-effective. Act as the final decision-maker for site approvals by weighing scientific prestige against potential regulatory startup delays to maintain the global enrollment timeline.
* **Site Selection Manager/Specialist:** Lead data-mining activities by synthesizing information from internal databases and public registries to build preliminary site and investigator lists. Manage the distribution and analysis of feasibility surveys to transform site responses into ranked selection packs for sponsor review.
* **Country Manager:** Validate proposed site lists by leveraging local networks to vet investigator interest and current workload. Oversee local Site Qualification Visits and confirm that facilities possess the physical infrastructure and staff capacity required for protocol execution.

## **Who can access the Medidata integration**

All Medidata platform users can access the Platform Help service. Access to Site Ranking service is limited to subscribed customers of Medidata’s Intelligent Trials/Study Feasibility application, and their subscription access must match any queries.

More details on accessing the integration can be found in Medidata’s MCP Server Documentation [link].

## **Setting up the Medidata integration**

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click “**Medidata**”
4. Click “Add to your team”

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Find “**Medidata**”
3. Click “Connect”
4. Follow the instructions to describe authentication process

Learn about [finding and connecting tools(opens in new tab)](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory) in Claude.

**For Claude Code Users**

1. Command: `/plugin marketplace add anthropics/life-sciences`
2. Command: `/plugin install medidata@life-sciences`
3. Restart Claude Code
4. Verify that the server is connected with /mcp

Technical details of the Medidata integration can be found in Medidata’s MCP Server Documentation [link].

## **Example use cases**

**Site Ranking use cases:**

* “What are the top ‘n’ predicted high performing sites for my core criteria i.e. within phase & indication of interest?”
* “What are the top ‘n’ predicted high performing sites based on more granular study criteria i.e. including age & eligibility, no. of study arms, etc.”
* “Which sites rank in the top 25% for predicted performance based on my specified criteria?”
* “What is the physical address of the top performing site(s) in indication X?”
* “Which sites are located in the country (s) of interest?”
* “What is the geographical distribution (no. of sites by countries or regions) of the top performing sites?”
* “Can you research which sites have access to advanced neuroimaging equipment like tau PET and the capability to perform lumbar punctures?”

**Platform Help use cases:**

* “How do I create a derived dataset in Data Connect?”
* “How do I configure edit checks for Rave EDC?”
* “When is the last release of Clinical Data Studio and what features did it include?”
* “We need to import external lab data into Data Connect. How do I do this and ensure alignment with our SOPs?”

* [What this integration provides](#what-this-integration-provides)
* [Who should use the Medidata integration](#who-should-use-the-medidata-integration)
* [Who can access the Medidata integration](#who-can-access-the-medidata-integration)
* [Setting up the Medidata integration](#setting-up-the-medidata-integration)
* [Example use cases](#example-use-cases)
