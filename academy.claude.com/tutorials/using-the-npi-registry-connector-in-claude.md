<!-- source: https://academy.claude.com/tutorials/using-the-npi-registry-connector-in-claude -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# Using the NPI Registry Connector in Claude

Set up and use the NPI Registry integration with Claude to validate, look up, and search US healthcare provider credentials in the CMS NPPES registry.

15 minClaude.ai

[Open Claude](https://claude.ai/new)

![](https://academy.claude.com/assets/v1/thumbnail.light-lhfk8yng.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-c5j7rv4s.png)

The NPI Registry connector gives Claude access to the CMS National Plan and Provider Enumeration System (NPPES) to validate, look up, and search healthcare providers in the United States by their National Provider Identifier (NPI). This article explains how to set up and use the NPI Registry integration with Claude to search and verify US healthcare provider credentials.

The NPI Registry integration relies upon Claude's ability to [use remote connectors(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities).

## What this integration provides[](#what-this-integration-provides)

The NPI Registry connector provides programmatic access to the Centers for Medicare & Medicaid Services (CMS) NPPES NPI Registry API v2.1. The National Provider Identifier (NPI) is a unique 10-digit identification number required under HIPAA for covered healthcare providers in the United States. This connector enables users to validate NPI numbers, retrieve comprehensive provider information, and search the registry containing millions of individual providers (NPI-1) and organizations (NPI-2) including physicians, nurses, therapists, hospitals, clinics, and pharmacies.

The connector provides three core tools that access different NPPES endpoints:

* **npi\_validate** performs instant local validation of NPI format and Luhn check digit without making an API call
* **npi\_lookup** retrieves complete provider records by NPI number including credentials (MD, DO, RN, PA-C, etc.), primary specialty/taxonomy codes, state license numbers, practice addresses, phone numbers, and enumeration status
* **npi\_search** enables discovery of providers through flexible queries combining first/last name, organization name, location (city/state/ZIP), specialty/taxonomy descriptions, and supports wildcards and name alias expansion. The provider-side data accessed includes self-reported information from NPPES enrollment records such as legal business names, practice locations, NUCC healthcare provider taxonomy classifications, state licensing information, mailing addresses, and optional health information exchange endpoints.

## Who should use the NPI Registry integration[](#who-should-use-the-npi-registry-integration)

* **Healthcare Administrators:** Verify provider credentials, validate billing information, and maintain accurate provider directories for insurance networks and health systems
* **Clinical Research Coordinators:** Validate US-based clinical trial investigators' credentials and verify their medical specialties and practice locations
* **Healthcare IT Developers:** Build provider lookup features, validate NPI numbers in EHR systems, and integrate provider verification into healthcare applications
* **Medical Affairs Teams:** Identify and locate key opinion leaders, build physician networks, and conduct competitive intelligence on provider affiliations
* **Compliance Officers:** Verify provider licensing status, validate NPIs for regulatory submissions, and audit provider enrollment data
* **Healthcare Recruiters:** Find providers by specialty and location, identify practice affiliations, and verify credentials during candidate screening
* **Health Services Researchers:** Analyze provider distribution patterns, study specialty availability by geographic region, and access provider taxonomy data

## Setting up the NPI Registry integration[](#setting-up-the-npi-registry-integration)

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click “**NPI Registry**”
4. Click “Add to your team”

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Find “**NPI Registry**”
3. Click “Connect”

Learn about [finding and connecting tools(opens in new tab)](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory) in Claude.

**For Claude Code Users**

1. Command: `/plugin marketplace add anthropics/healthcare`
2. Command: `/plugin install npi-registry@healthcare`
3. Restart Claude Code
4. Verify that the server is connected with /mcp

## Example use cases[](#example-use-cases)

**Provider Credential Verification**

* Validate the credentials, specialty, and practice location of a healthcare provider before onboarding, contracting, or referral.
* Sample Prompts:

Validate NPI 1043248818 and show me their credentials and specialty

Open in Claude

Look up the provider with NPI 1679576722 and tell me if they're actively licensed

Open in Claude

Check if NPI 1234567893 is valid and what type of provider it belongs to

Open in Claude

**Provider Discovery by Specialty and Location**

* Find healthcare providers in specific geographic areas by their medical specialty to build networks, identify referral partners, or analyze provider availability.
* Sample Prompts:

Find all cardiologists practicing in Boston, Massachusetts

Open in Claude

Search for nurse practitioners in ZIP code 90210

Open in Claude

Show me orthopedic surgeons in California with their practice addresses

Open in Claude

Find all general acute care hospitals in New York

Open in Claude

**Clinical Trial Investigator Verification**

* Verify that clinical trial investigators are legitimate US healthcare providers with appropriate credentials and active status.
* Sample Prompts:

I have a clinical trial investigator named Dr. Sarah Johnson in Minnesota. Can you find her NPI and verify her credentials?

Open in Claude

Verify that the principal investigator John Smith, MD is a licensed oncologist in Texas

Open in Claude

Find the NPI and specialty for Dr. Robert Chen who lists Mayo Clinic as his affiliation

Open in Claude

* [What this integration provides](#what-this-integration-provides)
* [Who should use the NPI Registry integration](#who-should-use-the-npi-registry-integration)
* [Setting up the NPI Registry integration](#setting-up-the-npi-registry-integration)
* [Example use cases](#example-use-cases)
