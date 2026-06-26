<!-- source: https://claude.com/resources/tutorials/using-the-npi-registry-connector-in-claude -->

# Using the NPI Registry Connector in Claude

  Healthcare
* Product
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/using-the-npi-registry-connector-in-claude

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The NPI Registry connector gives Claude access to the CMS National Plan and Provider Enumeration System (NPPES) to validate, look up, and search healthcare providers in the United States by their National Provider Identifier (NPI). This article explains how to set up and use the NPI Registry integration with Claude to search and verify US healthcare provider credentials.

The NPI Registry integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

## **What this integration provides**

The NPI Registry connector provides programmatic access to the Centers for Medicare & Medicaid Services (CMS) NPPES NPI Registry API v2.1. The National Provider Identifier (NPI) is a unique 10-digit identification number required under HIPAA for covered healthcare providers in the United States. This connector enables users to validate NPI numbers, retrieve comprehensive provider information, and search the registry containing millions of individual providers (NPI-1) and organizations (NPI-2) including physicians, nurses, therapists, hospitals, clinics, and pharmacies.

The connector provides three core tools that access different NPPES endpoints:

* **npi\_validate** performs instant local validation of NPI format and Luhn check digit without making an API call
* **npi\_lookup** retrieves complete provider records by NPI number including credentials (MD, DO, RN, PA-C, etc.), primary specialty/taxonomy codes, state license numbers, practice addresses, phone numbers, and enumeration status
* **npi\_search** enables discovery of providers through flexible queries combining first/last name, organization name, location (city/state/ZIP), specialty/taxonomy descriptions, and supports wildcards and name alias expansion. The provider-side data accessed includes self-reported information from NPPES enrollment records such as legal business names, practice locations, NUCC healthcare provider taxonomy classifications, state licensing information, mailing addresses, and optional health information exchange endpoints.

## **Who should use the NPI Registry integration**

* **Healthcare Administrators:** Verify provider credentials, validate billing information, and maintain accurate provider directories for insurance networks and health systems
* **Clinical Research Coordinators:** Validate US-based clinical trial investigators' credentials and verify their medical specialties and practice locations
* **Healthcare IT Developers:** Build provider lookup features, validate NPI numbers in EHR systems, and integrate provider verification into healthcare applications
* **Medical Affairs Teams:** Identify and locate key opinion leaders, build physician networks, and conduct competitive intelligence on provider affiliations
* **Compliance Officers:** Verify provider licensing status, validate NPIs for regulatory submissions, and audit provider enrollment data
* **Healthcare Recruiters:** Find providers by specialty and location, identify practice affiliations, and verify credentials during candidate screening
* **Health Services Researchers:** Analyze provider distribution patterns, study specialty availability by geographic region, and access provider taxonomy data

## **Setting up the NPI Registry integration**

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click “**NPI Registry**”
4. Click “Add to your team”
5. ‍

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Find “**NPI Registry**”
3. Click “Connect”

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

**For Claude Code Users**

1. Command: /plugin marketplace add anthropics/healthcare
2. Command: /plugin install npi-registry@healthcare
3. Restart Claude Code
4. Verify that the server is connected with /mcp

## **Example use cases**

**Provider Credential Verification**

* Validate the credentials, specialty, and practice location of a healthcare provider before onboarding, contracting, or referral.
* Sample Prompts:   
  + *"Validate NPI 1043248818 and show me their credentials and specialty"*
  + *"Look up the provider with NPI 1679576722 and tell me if they're actively licensed"*
  + *"Check if NPI 1234567893 is valid and what type of provider it belongs to"*

**Provider Discovery by Specialty and Location**

* Find healthcare providers in specific geographic areas by their medical specialty to build networks, identify referral partners, or analyze provider availability.
* Sample Prompts:   
  + *"Find all cardiologists practicing in Boston, Massachusetts"*
  + *"Search for nurse practitioners in ZIP code 90210"*
  + *"Show me orthopedic surgeons in California with their practice addresses"*
  + *"Find all general acute care hospitals in New York"*

**Clinical Trial Investigator Verification**

* Verify that clinical trial investigators are legitimate US healthcare providers with appropriate credentials and active status.
* Sample Prompts:   
  + *"I have a clinical trial investigator named Dr. Sarah Johnson in Minnesota. Can you find her NPI and verify her credentials?"*
  + *"Verify that the principal investigator John Smith, MD is a licensed oncologist in Texas"*
  + *"Find the NPI and specialty for Dr. Robert Chen who lists Mayo Clinic as his affiliation"*

## Related tutorials

[How to use the Prior Auth Review sample skill with Claude](/resources/tutorials/how-to-use-the-prior-auth-review-sample-skill-with-claude-2ggy8)How to use the Prior Auth Review sample skill with Claude

How to use the Prior Auth Review sample skill with Claude

Tutorial

[Tutorial](/resources/tutorials/how-to-use-the-prior-auth-review-sample-skill-with-claude-2ggy8)Tutorial

[Using the Function Connector in Claude](/resources/tutorials/using-the-function-connector-in-claude)Using the Function Connector in Claude

Using the Function Connector in Claude

Tutorial

[Tutorial](/resources/tutorials/using-the-function-connector-in-claude)Tutorial

[Using the HealthEx Connector in Claude](/resources/tutorials/using-the-healthex-connector-in-claude)Using the HealthEx Connector in Claude

Using the HealthEx Connector in Claude

Tutorial

[Tutorial](/resources/tutorials/using-the-healthex-connector-in-claude)Tutorial

[How to use the FHIR Developer agent skill with Claude Code](/resources/tutorials/how-to-use-the-fhir-developer-agent-skill-with-claude-code)How to use the FHIR Developer agent skill with Claude Code

How to use the FHIR Developer agent skill with Claude Code

Tutorial

[Tutorial](/resources/tutorials/how-to-use-the-fhir-developer-agent-skill-with-claude-code)Tutorial
