<!-- source: https://claude.com/resources/tutorials/how-to-use-the-prior-auth-review-sample-skill-with-claude-2ggy8 -->

# How to use the Prior Auth Review sample skill with Claude

  Healthcare
* Product
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/how-to-use-the-prior-auth-review-sample-skill-with-claude-2ggy8

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

## **What is the Prior Auth Review sample skill?**

The Prior Authorization skill is a sample skill that digests request packet documentation and performs several initial checks to be verified by a human reviewer.  These include:

* NPI Physician Registry
* ICD-10 Lookup
* CMS Coverage Database
* CPT Codes

It then extracts clinical data to summarize the argument for medical necessity and confirms all the required documentation is present.

This is a sample skill that gives you a starting point to customize for your own use cases. Be sure to review the [README.md](https://github.com/anthropics/healthcare/releases/download/v1.0.0/prior-auth-review-skill-v1.0.0.zip) file before using the skill.

## **Who should use the Prior Auth Review sample skill?**

This skill is designed for payer clinical reviewers who need to significantly reduce the time to initial recommendation without writing code from scratch.

## **How to access the skill in** [**Claude.ai**](http://claude.ai)

**For Organization Owners (Team and Enterprise)**

1. Download the ZIP for the **prior-auth-review-skill** [here](https://github.com/anthropics/healthcare/releases/download/v1.0.0/prior-auth-review-skill-v1.0.0.zip)
2. Review the sample skill thoroughly and make edits and adjustments to fit your organization’s workflows
3. From [Claude.ai](http://claude.ai), navigate to Admin settings > Capabilities > Skills
4. Make sure Skills is activated for your organization
5. Click “Organization skills library”
6. Click “+Add”
7. Upload the skill zip file

Learn about [provisioning and managing skills for your organization](https://support.claude.com/en/articles/13119606-provisioning-and-managing-skills-for-your-organization)

**For Individual Claude Users**

1. Download the ZIP file for the **prior-auth-review-skill** [here](https://github.com/anthropics/healthcare/releases/download/v1.0.0/prior-auth-review-skill-v1.0.0.zip)
2. Review the sample skill thoroughly and make edits and adjustments to fit your workflow
3. From [Claude.ai](http://claude.ai), navigate to Settings > Capabilities > Skills (if Skills is not available, contact your team admin)
4. Click “Upload skill”
5. Upload the skill zip file

## **How to access the skill in Claude Code**

Command

`/plugin marketplace add anthropics/healthcare`

`/plugin install prior-auth-review@healthcare`

## Related tutorials

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

[Using the NPI Registry Connector in Claude](/resources/tutorials/using-the-npi-registry-connector-in-claude)Using the NPI Registry Connector in Claude

Using the NPI Registry Connector in Claude

Tutorial

[Tutorial](/resources/tutorials/using-the-npi-registry-connector-in-claude)Tutorial
