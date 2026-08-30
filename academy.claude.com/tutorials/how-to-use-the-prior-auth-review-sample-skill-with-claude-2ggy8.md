<!-- source: https://academy.claude.com/tutorials/how-to-use-the-prior-auth-review-sample-skill-with-claude-2ggy8 -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# How to use the Prior Auth Review sample skill with Claude

How to use the Prior Auth Review sample skill with Claude

3 minClaude.ai

[Open Claude](https://claude.ai/new)

![](https://academy.claude.com/assets/v1/thumbnail.light-mjer1khs.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-hn3u7z1d.png)

## **What is the Prior Auth Review sample skill?**[](#what-is-the-prior-auth-review-sample-skill)

The Prior Authorization skill is a sample skill that digests request packet documentation and performs several initial checks to be verified by a human reviewer. These include:

* NPI Physician Registry
* ICD-10 Lookup
* CMS Coverage Database
* CPT Codes

It then extracts clinical data to summarize the argument for medical necessity and confirms all the required documentation is present.

This is a sample skill that gives you a starting point to customize for your own use cases. Be sure to review the [README.md(opens in new tab)](https://github.com/anthropics/healthcare/releases/download/v1.0.0/prior-auth-review-skill-v1.0.0.zip) file before using the skill.

## **Who should use the Prior Auth Review sample skill?**[](#who-should-use-the-prior-auth-review-sample-skill)

This skill is designed for payer clinical reviewers who need to significantly reduce the time to initial recommendation without writing code from scratch.

## **How to access the skill in** [**Claude.ai**(opens in new tab)](http://claude.ai)[](#how-to-access-the-skill-in-claudeai)

**For Organization Owners (Team and Enterprise)**

1. Download the ZIP for the **prior-auth-review-skill** [here(opens in new tab)](https://github.com/anthropics/healthcare/releases/download/v1.0.0/prior-auth-review-skill-v1.0.0.zip)
2. Review the sample skill thoroughly and make edits and adjustments to fit your organization’s workflows
3. From [Claude.ai(opens in new tab)](http://claude.ai), navigate to Admin settings > Capabilities > Skills
4. Make sure Skills is activated for your organization
5. Click “Organization skills library”
6. Click “+Add”
7. Upload the skill zip file

Learn about [provisioning and managing skills for your organization(opens in new tab)](https://support.claude.com/en/articles/13119606-provisioning-and-managing-skills-for-your-organization)

**For Individual Claude Users**

1. Download the ZIP file for the **prior-auth-review-skill** [here(opens in new tab)](https://github.com/anthropics/healthcare/releases/download/v1.0.0/prior-auth-review-skill-v1.0.0.zip)
2. Review the sample skill thoroughly and make edits and adjustments to fit your workflow
3. From [Claude.ai(opens in new tab)](http://claude.ai), navigate to Settings > Capabilities > Skills (if Skills is not available, contact your team admin)
4. Click “Upload skill”
5. Upload the skill zip file

## **How to access the skill in Claude Code**[](#how-to-access-the-skill-in-claude-code)

Command

`/plugin marketplace add anthropics/healthcare`

`/plugin install prior-auth-review@healthcare`

* [What is the Prior Auth Review sample skill?](#what-is-the-prior-auth-review-sample-skill)
* [Who should use the Prior Auth Review sample skill?](#who-should-use-the-prior-auth-review-sample-skill)
* [How to access the skill in Claude.ai](#how-to-access-the-skill-in-claudeai)
* [How to access the skill in Claude Code](#how-to-access-the-skill-in-claude-code)
