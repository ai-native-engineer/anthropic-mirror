<!-- source: https://claude.com/resources/tutorials/using-the-icd-10-connector-in-claude -->

# Using the ICD-10 Connector in Claude

  Healthcare
* Product
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/using-the-icd-10-connector-in-claude

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

The ICD-10 connector gives Claude access to ICD-10-CM diagnosis codes and ICD-10-PCS procedure codes (2026 edition), enabling healthcare organizations to search, validate, and explore medical coding hierarchies required for HIPAA-compliant billing and clinical documentation. This article explains how to set up and use the ICD-10 integration with Claude to streamline medical coding and billing compliance workflows.

The ICD-10 integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

‍

## **What this integration provides**

This integration provides access to the 2026 International Classification of Diseases, 10th Revision code sets used in the United States healthcare system. ICD-10 is based on the World Health Organization (WHO) classification system, with ICD-10-CM (Clinical Modification) authorized by WHO and developed by the CDC's National Center for Health Statistics (NCHS) for diagnosis coding, and ICD-10-PCS (Procedure Coding System) developed by CMS for inpatient procedure coding. Both code sets are HIPAA-mandated standards that became effective October 1, 2015, and are updated annually. The FY 2026 release includes over 550 diagnosis code changes (487 additions, 28 deletions, 38 revisions) and became effective October 1, 2025, for patient encounters and discharges through September 30, 2026.

This connector provides nine primary tool calls that access ICD-10-CM and ICD-10-PCS codes.

* **search\_diagnosis\_by\_description** enables users to find diagnosis codes by disease name or medical terminology (e.g., "diabetes", "myocardial infarction", "breast cancer"), using case-insensitive text matching across code descriptions with automatic filtering for HIPAA-valid codes (excludes category headers that cannot be billed).
* **search\_diagnosis\_by\_code** finds diagnosis codes by exact code match or prefix search (e.g., "E11" returns all Type 2 diabetes codes), useful for exploring code families and related conditions.
* **search\_procedure\_by\_description** searches ICD-10-PCS procedure codes by anatomical terms and root operations (e.g., "appendix", "resection", "percutaneous endoscopic" for laparoscopic procedures), noting that PCS uses standardized terminology rather than common procedure names.
* **search\_procedure\_by\_code** finds procedure codes by exact match or prefix (e.g., "0DT" returns gastrointestinal resection procedures), enabling systematic exploration of procedure code families.
* **lookup\_code** retrieves complete details for a specific code when the exact code is known (e.g., "E11.65", "0DTJ4ZZ"), returning short and long descriptions plus HIPAA transaction validity status.
* **validate\_code** checks whether a code exists in the database and confirms its validity for HIPAA-covered transactions, distinguishing between billable codes and category headers.
* **get\_hierarchy** retrieves the full code family tree under a category prefix (e.g., "E11" returns all 117 Type 2 diabetes codes), showing parent-child relationships and complication progressions.
* **get\_by\_category** navigates diagnosis codes by chapter (single letter like "E" for Endocrine diseases) or 3-character category (e.g., "E11" for Type 2 Diabetes).
* **get\_by\_body\_system** retrieves ICD-10-PCS procedure codes for specific anatomical systems using the first character body system code (e.g., "0" for Central Nervous System, "D" for Gastrointestinal).

On the provider side, the connector accesses a locally stored database of the 2026 ICD-10-CM and ICD-10-PCS code sets published by CMS and CDC/NCHS. The database includes code structure (chapter, category, subcategory), short and long descriptions, and HIPAA transaction validity flags. ICD-10-CM codes are 3-7 alphanumeric characters documenting diagnoses; ICD-10-PCS codes are exactly 7 alphanumeric characters documenting inpatient procedures. Category header codes (shorter codes like "E11" or "E11.3") serve as organizational groupings and are NOT valid for billing—only fully specified codes with maximum detail are HIPAA-compliant.

‍

## **Who should use the ICD-10 integration**

* **Medical Coders & Health Information Management Professionals:** Search and validate diagnosis and procedure codes for accurate medical record documentation, ensure code specificity meets billing requirements, verify HIPAA transaction validity, and explore code hierarchies to select the most appropriate codes.
* **Revenue Cycle Management Teams & Billing Specialists:** Validate code accuracy before claim submission to reduce denials, verify codes are valid for the current fiscal year (FY 2026), identify codes requiring additional documentation specificity, and ensure compliance with payer coding requirements.
* **Clinical Documentation Improvement (CDI) Specialists:** Query physicians for more specific documentation when codes lack required detail, identify incomplete or non-specific codes that may result in claim denials, ensure documentation supports the most accurate and specific ICD-10 codes, and track code hierarchy relationships for comorbidity and complication coding.
* **Healthcare IT & EHR Integration Teams:** Build and maintain code validation logic in electronic health record systems, implement automated code suggestion features based on clinical documentation, create coding reference tools integrated into clinical workflows, and ensure coding databases are updated with annual ICD-10 revisions.
* **Medical Auditors & Compliance Officers:** Audit coded medical records for accuracy and specificity, identify patterns of coding errors or undercoding, verify compliance with CMS coding guidelines and HIPAA standards, and conduct retrospective reviews of diagnosis and procedure coding quality.
* **Healthcare Data Analysts & Population Health Teams:** Analyze disease prevalence and treatment patterns using standardized ICD-10 codes, track diagnosis trends across patient populations, conduct outcomes research using procedure codes, and support quality reporting and value-based care initiatives with accurate coded data.

‍

## **Setting up the ICD-10 integration**

**For Organization Owners (Team and Enterprise)**

1. Navigate to Admin settings > Connectors
2. Click "Browse connectors"
3. Click “**ICD-10**”
4. Click “Add to your team”

**For Individual Claude Users**

1. Navigate to Settings > Connectors
2. Find “**ICD-10**”
3. Click “Connect”

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

**For Claude Code Users**

1. Command: `/plugin marketplace add anthropics/healthcare`
2. Command: `/plugin install /plugin install icd10-codes@healthcare`
3. Restart Claude Code
4. Verify that the server is connected with /mcp

‍

## **Example use cases**

**Medical Coding & Documentation Accuracy**

* Scenario: Coders and CDI specialists ensuring accurate, specific code selection for billing and documentation
* Sample Prompts:   
  + *"Find all ICD-10 codes for Type 2 diabetes with complications. Show me the complete hierarchy"*
  + *"Validate code E11.65 for HIPAA billing. Is this code specific enough or is it a category header?"*
  + *"Search for diagnosis codes related to hypertension with chronic kidney disease"*
  + *"What ICD-10-PCS codes exist for laparoscopic appendectomy? Search procedures for 'appendix' and 'percutaneous endoscopic'"*

**Billing Compliance & Claims Processing**

* Scenario: Revenue cycle teams validating codes before claim submission to prevent denials
* Sample Prompts:   
  + *"Is E11.9 valid for HIPAA transactions? What's the full description?"*
  + *"Search for all myocardial infarction diagnosis codes that are valid for billing"*
  + *"Find procedure codes for coronary artery bypass graft by searching code prefix '021'"*
  + *"Validate this procedure code 0DTJ4ZZ - is it valid for inpatient hospital billing?"*

**Clinical Documentation Improvement & Audit**

* Scenario: CDI specialists and auditors reviewing documentation specificity and code appropriateness
* Sample Prompts:   
  + *"Show me the hierarchy of breast cancer diagnosis codes to identify if we're using the most specific code"*
  + *"Search for diabetes codes with retinopathy complications - which codes distinguish between severity levels?"*
  + *"What ICD-10 codes exist in the category E08 for diabetes due to underlying condition?"*
  + *"Find all gastrointestinal resection procedures by body system. Are we coding to the appropriate specificity level?"*

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
