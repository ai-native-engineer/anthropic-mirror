<!-- source: https://claude.com/resources/tutorials/using-the-cms-coverage-connector-in-claude -->

# Using the CMS Coverage Connector in Claude

  Healthcare
* Product
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/using-the-cms-coverage-connector-in-claude

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The CMS Coverage connector gives Claude access to the CMS Medicare Coverage Database, enabling searches and retrieval of National Coverage Determinations (NCDs), Local Coverage Determinations (LCDs), billing articles, and coverage policy updates for Medicare Part B services. This article explains how to set up and use the CMS Coverage integration with Claude to search Medicare Part B coverage policies instantly.

The CMS Coverage integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

This server may return data governed by third-party license agreements, including those available [here](https://api.coverage.cms.gov/v1/metadata/license-agreement/). By connecting to this server, you understand and agree to abide by any applicable agreements.

## **What this integration provides**

This integration connects to the CMS Coverage API v1, providing comprehensive access to the Medicare Coverage Database maintained by the Centers for Medicare & Medicaid Services. This connector enables users to search, retrieve, and monitor Medicare Part B coverage policies that determine whether and under what circumstances Medicare will pay for medical services, procedures, durable medical equipment (DME), laboratory tests, and injectable drugs administered in medical settings across the United States. It's important to note that this connector covers Part B coverage only — it does not include Medicare Part D prescription drug formularies or Part A inpatient hospital coverage.

The connector provides multiple tool categories for different coverage research needs:

* National coverage tools include:   
  + **search\_ncds** for finding official nationwide coverage policies,
  + **search\_nca\_cals** for tracking coverage analyses and letters
  + **search\_medcac\_meetings** for advisory committee discussions
  + **search\_technology\_assessments** for clinical evidence reviews.
* Local coverage tools include:   
  + **search\_lcds** for regional coverage policies by Medicare Administrative Contractors (MACs)
  + **search\_proposed\_lcds** for pending policy changes
  + **search\_articles** for detailed billing and coding guidance with CPT/HCPCS codes and ICD-10 requirements.

Detail retrieval tools like **get\_ncd**, **get\_nca**, and **get\_cal** fetch complete policy documents including coverage criteria, indications, limitations, effective dates, and documentation requirements. Helper tools include **get\_contractors** for identifying MACs by region, **whats\_new\_national** and **whats\_new\_local** for monitoring recent policy changes, and **sad\_exclusion\_list** for checking self-administered drug exclusions.

On the provider side, the connector accesses structured data from the CMS Medicare Coverage Database API, retrieving policy documents, contractor information, billing codes, medical necessity criteria, and revision histories directly from CMS's official repository. Data returned from these APIs may be governed by third-party license agreements, including those available [here](https://api.coverage.cms.gov/v1/metadata/license-agreement/).

## **Who should use the CMS Coverage integration**

* **Healthcare Providers & Physicians:** Verify coverage for procedures, understand medical necessity requirements, and ensure compliance with Medicare billing policies before providing services
* **Medical Coders & Billers:** Access detailed billing articles with CPT/HCPCS codes, ICD-10 diagnosis codes, modifiers, and documentation requirements for accurate claims submission
* **Healthcare Compliance Officers:** Monitor policy changes, track coverage updates, and ensure organizational adherence to Medicare coverage guidelines
* **Prior Authorization Specialists:** Research coverage criteria, medical necessity requirements, and documentation standards for authorization requests
* **Durable Medical Equipment (DME) Suppliers:** Look up LCD coverage policies for equipment like wheelchairs, oxygen systems, and CPAP devices by geographic region
* **Healthcare Policy Researchers:** Analyze coverage trends, compare regional LCD variations, and track national coverage decision-making processes
* **Medical Affairs & Market Access Teams:** Research coverage landscapes for medical devices, procedures, and treatments to inform commercialization strategies
* **Clinical Trial Investigators:** Verify Medicare coverage status for procedures and services used in clinical research protocols

## **Setting up the CMS Coverage integration**

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click “**CMS Coverage**”
4. Click “Add to your team”

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Find “**CMS Coverage**”
3. Click “Connect”

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

‍**For Claude Code Users**

1. Command: `/plugin marketplace add anthropics/healthcare`
2. Command: `/plugin install cms-coverage@healthcare`
3. Restart Claude Code
4. Verify that the server is connected with /mcp

## **Example use cases**

**Pre-Service Coverage Verification**

* Healthcare providers need to verify Medicare coverage before performing procedures or prescribing equipment to avoid claim denials and ensure patients understand their coverage.

* Sample Prompts:   
  + *"Does Medicare cover continuous glucose monitoring for type 2 diabetes patients?"*
  + *"What are the medical necessity criteria for home oxygen therapy in California?"*
  + *"Find the LCD for power wheelchairs in my region and tell me what documentation is required"*
  + *"Is sacral nerve stimulation covered by Medicare for urinary incontinence?"*

**Billing & Coding Compliance**

* Medical coders and billers need specific HCPCS codes, ICD-10 diagnosis codes, and billing requirements to submit clean claims and avoid denials.
* Sample Prompts:   
  + *"What are the covered ICD-10 codes for diabetes self-management training?"*
  + *"Find the billing article for home oxygen equipment and show me the required HCPCS codes"*
  + *"What modifiers are required for billing wheelchair accessories in Texas?"*
  + *"Show me the documentation requirements for billing cardiac rehabilitation services"*

**Policy Monitoring & Updates**

* Compliance officers and healthcare administrators need to stay current with coverage policy changes that affect their practice or organization.
* Sample Prompts:   
  + *"What Medicare coverage policies have changed in the last 30 days?"*
  + *"Show me recent LCD updates for my Medicare contractor"*
  + *"Have there been any new NCDs published for cardiovascular procedures this quarter?"*
  + *"Are there any proposed LCDs for laboratory testing that I should review?"*

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
