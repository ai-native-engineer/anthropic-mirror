<!-- source: https://claude.com/resources/tutorials/using-the-clinicaltrials-gov-connector-in-claude -->

# Using the ClinicalTrials.gov Connector in Claude

  Life Sciences
* Product
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/using-the-clinicaltrials-gov-connector-in-claude

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The ClinicalTrials.gov connector gives Claude access to the NIH/NLM registry of 500,000+ clinical studies to search trials, analyze endpoints, and support research operations. This article explains how to set up and use the ClinicalTrials.gov integration with Claude to power clinical, regulatory, and patient-supporting workflows.

The ClinicalTrials.gov integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

‍

## **What this integration provides**

The ClinicalTrials.gov connector gives Claude access to ClinicalTrials.gov API v2, the world's largest clinical trial registry managed by the National Library of Medicine (NLM) at the National Institutes of Health (NIH). With more than 1,200 studies, the database has grown to over 500,000 registered trials across 221 countries and territories, representing the most comprehensive source of clinical research information worldwide.

This connector provides six primary tool calls that access different dimensions of clinical trial data.

* **search\_trials** is the primary discovery tool, enabling users to find trials by condition (e.g., "diabetes", "lung cancer"), intervention (drug/treatment names), location (city, state, country), sponsor, recruitment status (RECRUITING, COMPLETED, etc.), and development phase (PHASE1-PHASE4), with support for Boolean operators and medical synonym expansion.
* **get\_trial\_details** retrieves comprehensive protocol information for specific trials using their NCT identifier, returning full eligibility criteria (inclusion/exclusion), detailed study design and methodology, primary and secondary endpoints with measurement timeframes, all study locations with contact information, sponsor details, enrollment targets, and links to published results.
* **search\_by\_sponsor** enables pharmaceutical pipeline analysis by finding all trials funded by specific companies or institutions (e.g., "Pfizer", "NIH", "Mayo Clinic"), supporting competitive intelligence and drug development tracking with filtering by condition and phase.
* **search\_investigators** identifies principal investigators and research sites conducting trials in specific therapeutic areas, returning investigator names, roles, institutional affiliations, facility locations, and associated trial information for site selection and investigator verification.
* **analyze\_endpoints** systematically compares outcome measures across trials, operating in two modes: single-trial analysis (returns all endpoints for one NCT ID) or aggregate analysis (identifies common endpoint patterns across multiple trials in a therapeutic area), essential for protocol design benchmarking and understanding standard measures in a disease area.
* **search\_by\_eligibility** enables clinical research coordinators to screen for trials matching specific demographic and clinical criteria (age, sex) with support for eligibility keyword searches in inclusion/exclusion criteria text  (e.g., "BRCA mutation", "HbA1c > 8%", "ECOG 0-1").

On the provider side, the connector queries ClinicalTrials.gov's RESTful API v2, which accesses a PostgreSQL database updated daily with trial registration data submitted by study sponsors. All interventional trials of FDA-regulated products must be registered before enrollment begins (per FDAAA 801), and results must be submitted within one year of study completion. The database includes structured data fields for conditions (using MeSH terminology), interventions, locations, eligibility criteria, outcome measures, and study design parameters.

‍

## **Who should use the ClinicalTrials.gov integration**

* **Clinical Research Coordinators & Study Recruiters:** Screen institutional patient populations for trial eligibility using demographic and clinical criteria, identify nearby recruiting studies for referral programs, verify detailed trial requirements and visit schedules, and coordinate with study sponsors to accelerate enrollment.
* **Pharmaceutical & Biotech Companies:** Conduct competitive intelligence on competitor pipelines, analyze clinical development strategies across therapeutic areas, identify partnership opportunities with active research sites, and benchmark study designs and endpoints against industry standards.
* **Principal Investigators & Site Coordinators:** Identify collaborating investigators at other institutions, understand which sites are most active in specific disease areas, verify investigator qualifications and track record, and discover trials for potential site participation.
* **Protocol Writers & Clinical Operations Teams:** Benchmark endpoint selection by analyzing outcome measures used in similar trials, design eligibility criteria based on prior study standards, identify common recruitment challenges in a therapeutic area, and estimate feasible enrollment timelines.
* **Regulatory Affairs Professionals:** Track clinical development programs for regulatory submissions, verify trial registration compliance for FDA-regulated products, analyze phase progression rates and development timelines, and identify precedent trials for regulatory strategy.
* **Clinical Trial Recruiters & Research Navigators:** Screen institutional patient populations for trial eligibility, identify appropriate trials for referral programs, coordinate with study sponsors for patient enrollment, and maintain databases of active trials at their healthcare system.
* **Medical Affairs & Health Economists:** Analyze trial completion rates and time-to-results, identify gaps in clinical evidence for specific indications, track real-world evidence studies and post-marketing trials, and support payer value dossiers with clinical trial data.

‍

## **Setting up the ClinicalTrials.gov integration**

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click “**ClinicalTrials.gov**”
4. Click “Add to your team”

‍

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Find “**ClinicalTrials.gov**”
3. Click “Connect”

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

‍

**For Claude Code Users**

1. Command: /plugin marketplace add anthropics/life-sciences
2. Command: /plugin install clinical-trials@life-sciences
3. Restart Claude Code
4. Verify that the server is connected with /mcp

‍

Technical details of the ClinicalTrials.gov integration can be found in the [ClinicalTrials.gov MCP Server Documentation](http://clinicaltrials.gov).

‍

## **Example use cases**

**Clinical Trial Recruitment & Eligibility Screening**

* Scenario: Research coordinators and recruitment professionals identifying eligible trial candidates from their institutional patient populations
* Sample Prompts:   
  + *"Find recruiting Phase 3 diabetes trials with HbA1c eligibility criteria between 7-10% for our Boston research site"*
  + *"What breast cancer trials are accepting BRCA-positive candidates at academic medical centers in California?"*
  + *"Search for Alzheimer's trials with MMSE score requirements that match our memory clinic population"*
  + *"Identify pediatric leukemia trials recruiting at major children's hospitals for our referral network"*

‍

**Competitive Intelligence & Pipeline Analysis**

* Scenario: Analyzing pharmaceutical company development programs and therapeutic landscapes
* Sample Prompts:   
  + *"What Phase 3 oncology trials is Pfizer currently running? Show their cancer pipeline"*
  + *"Find all GLP-1 agonist trials for obesity. Who are the main sponsors and what endpoints are they measuring?"*
  + *"Show me Moderna's active clinical trials and their development phases"*
  + *"What companies are developing drugs for Parkinson's disease? Analyze their trial endpoints"*

‍

**Systematic Protocol Design & Endpoint Benchmarking**

* Scenario: Designing new trial protocols based on industry standards and precedent studies
* Sample Prompts:   
  + *"What are the most common primary endpoints used in Phase 3 diabetes trials?"*
  + *"Analyze endpoints for completed heart failure trials - what timeframes do they use?"*
  + *"Find principal investigators at academic medical centers conducting immunotherapy trials"*
  + *"What eligibility criteria do Phase 2 NASH trials typically use? Show me HbA1c cutoffs"*

Learn more at How to use the Clinical Trial Protocol skill with Claude

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
