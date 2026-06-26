<!-- source: https://claude.com/resources/tutorials/using-the-biorxiv-and-medrxiv-connector-in-claude -->

# Using the bioRxiv and medRxiv Connector in Claude

  Life Sciences
* Product
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/using-the-biorxiv-and-medrxiv-connector-in-claude

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The bioRxiv connector gives Claude access to bioRxiv and medRxiv preprint servers, enabling researchers to search, retrieve, and summarize preprints. This article explains how to set up and use the bioRxiv integration with Claude to track emerging research before peer review publication.

The bioRxiv integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

‍

## **What this integration provides**

This connector gives Claude direct access to bioRxiv and medRxiv, the leading preprint servers for biological and health sciences operated by openRxiv. bioRxiv focuses on basic research across more than 25 life science disciplines, while medRxiv specializes in clinical and health research. These platforms enable scientists to share unpublished manuscripts rapidly, with bioRxiv now hosting over 310,000 preprints. The connector provides early access to cutting-edge research months before traditional peer-reviewed publication.

‍

The connector provides nine primary tool calls that access different aspects of the preprint ecosystem.

* **search\_preprints** enables users to discover preprints by date range, subject category (neuroscience, genomics, immunology, etc.), or recent submissions, returning DOIs, titles, authors, abstracts, and categories for each result.
* **get\_preprint** retrieves comprehensive metadata for specific preprints including full abstracts, corresponding author contact information, funding details, license information, PDF URLs, and whether the preprint has been published in a peer-reviewed journal.
* **get\_categories** lists all 27 bioRxiv subject categories for filtering searches across disciplines from animal behavior to systems biology.
* **search\_published\_articles** tracks preprints that have successfully transitioned to peer-reviewed publication, returning both the original preprint DOI and the published journal DOI with publication dates for analyzing preprint-to-publication timelines.
* **search\_biorxiv\_publications** provides simplified tracking of bioRxiv-specific publication outcomes (excludes medRxiv).
* **search\_publisher\_articles** filters published preprints by specific journals or publishers using DOI prefixes, enabling competitive analysis of which journals publish from the preprint pool.
* **search\_by\_funder** discovers research funded by specific organizations using ROR IDs (e.g., NIH, NSF, European Commission), essential for tracking grant-funded research output.
* **get\_content\_statistics** and **get\_usage\_statistics** provide platform-wide metrics on submission volumes, cumulative growth, abstract views, full-text views, and PDF downloads over time.

On the provider side, the connector queries the official bioRxiv/medRxiv RESTful API, accessing metadata stored in their PostgreSQL database. All preprints undergo basic screening for plagiarism and non-scientific content but are NOT peer-reviewed. Preprints receive DOIs for citability and version control tracks revisions over time.

‍

## **Who should use the bioRxiv integration**

* **Academic Researchers:** Monitor emerging research in their field before formal publication, identify collaboration opportunities, track competitor labs' preprints, and stay current with fast-moving areas where preprints provide 3-12 month publication lead time.
* **Grant Reviewers & Funding Officers:** Track research outputs from funded grants using ROR-based funder searches, assess productivity of research programs, and monitor which preprints from funded work achieve peer-reviewed publication.
* **Journal Editors & Publishers:** Discover high-quality preprints for solicitation, analyze which preprints attract reader attention through usage statistics, and understand publication patterns across therapeutic areas or disciplines.
* **Pharmaceutical & Biotech Scientists:** Monitor early-stage research relevant to drug targets, track academic publications before patent filings become public, identify emerging therapeutic modalities, and discover potential academic collaboration partners.
* **Science Journalists & Communicators:** Find breaking research stories, verify preprint status before reporting, track which preprints generate public interest through download metrics, and identify high-impact studies transitioning to peer-review.
* **Meta-Researchers & Bibliometricians:** Analyze preprint-to-publication rates, study time-to-publication across disciplines, investigate funder impacts on research dissemination, and track platform growth trends in open science.
* **PhD Students & Postdocs:** Stay current with latest methodologies before publication, find recent work for literature reviews, identify active research groups in their area, and discover which labs are productively publishing in their field.

‍

## **Setting up the bioRxiv integration**

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click “**bioRxiv**”
4. Click “Add to your team”

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Find “**bioRxiv**”
3. Click “Connect”

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

**For Claude Code Users**

1. Command: `/plugin marketplace add anthropics/life-sciences`
2. Command: `/plugin install biorxiv@life-sciences`
3. Restart Claude Code
4. Verify that the server is connected with /mcp

‍

## **Example use cases**

**Literature Monitoring & Early Research Discovery**

* Scenario: Staying current with rapidly evolving research areas before formal publication
* Sample Prompts:   
  + *"Find all neuroscience preprints posted in the last 30 days related to Alzheimer's disease"*
  + *"Search medRxiv for recent COVID-19 clinical trial preprints from the past week"*
  + *"Show me the latest CRISPR gene editing preprints in the molecular biology category"*
  + *"What are the most recent cancer immunotherapy preprints on bioRxiv?"*

‍

**Publication Tracking & Impact Analysis**

* Scenario: Analyzing which preprints successfully transition to peer-reviewed journals
* Sample Prompts:   
  + *"Which bioRxiv preprints have been published in Nature journals in the past 6 months?"*
  + *"Track preprints that were published in high-impact journals with DOI prefix 10.1126 (Science)"*
  + *"Show me recent genomics preprints that have been formally published and compare preprint vs publication dates"*
  + *"Find preprints from 2024 that successfully made it into peer-reviewed journals"*

‍

**Funding Agency Research Output Monitoring**

* Scenario: Tracking research productivity and outputs from specific funding organizations
* Sample Prompts:   
  + *"Find all preprints funded by the NIH (ROR ID: 021nxhr62) in the past year"*
  + *"What research has the European Commission (ROR: 02mhbdp94) funded that's been posted as preprints?"*
  + *"Show me bioRxiv preprints funded by the Wellcome Trust and track their publication outcomes"*
  + *"Analyze preprint submission trends and usage statistics for platform growth over time"*

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
