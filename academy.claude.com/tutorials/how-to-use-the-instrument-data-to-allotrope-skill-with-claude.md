<!-- source: https://academy.claude.com/tutorials/how-to-use-the-instrument-data-to-allotrope-skill-with-claude -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# How to use the Instrument Data to Allotrope Skill with Claude

How to use the Instrument Data to Allotrope Skill with Claude

3 minClaude

[Open Claude](https://claude.ai/new)

![](https://academy.claude.com/assets/v1/thumbnail.light-oyn2l3lg.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-miiqhla1.png)

## **What is the Instrument Data to Allotrope skill?**[](#what-is-the-instrument-data-to-allotrope-skill)

The instrument-to-allotrope skill converts raw laboratory instrument output files (CSVs, Excel, Txt, etc.) into standardized [Allotrope(opens in new tab)](https://www.allotrope.org/) Simple Model (ASM) JSON format or flattened 2D CSVs for easier integration with LIMS, ELNs, and data lakes. It auto-detects instrument types and when applicable, uses the [allotropy library(opens in new tab)](https://pypi.org/project/allotropy/) (authored by Benchling) to parse files. It also generates exportable Python parser code so data engineers can reliably replicate the conversion in production pipelines. Users may consider customizing the skill to use their specific data schemas or file output formats instead of the Allotrope standard.

## **Who should use the Instrument Data to Allotrope skill?**[](#who-should-use-the-instrument-data-to-allotrope-skill)

This skill is designed for lab scientists, data managers, and informatics teams working with laboratory instruments who need to standardize disparate instrument outputs (cell counters, plate readers, spectrophotometers, etc.) into a consistent format for downstream analysis, regulatory submissions, or integration with enterprise data systems without writing code from scratch.

## **How to access the skill in** [**Claude.ai**(opens in new tab)](http://claude.ai)[](#how-to-access-the-skill-in-claudeai)

**For Organization Owners (Team and Enterprise)**

1. Download the ZIP for the **instrument-data-to-allotrope** skill [here(opens in new tab)](https://github.com/anthropics/life-sciences/releases/download/v1.1.1/instrument-data-to-allotrope-v1.1.1.zip)
2. From [Claude.ai(opens in new tab)](http://claude.ai), navigate to Admin settings > Capabilities > Skills
3. Make sure Skills is activated for your organization
4. Click “Organization skills library”
5. Click “+Add”
6. Upload the skill zip file

Learn about [provisioning and managing skills for your organization(opens in new tab)](https://support.claude.com/en/articles/13119606-provisioning-and-managing-skills-for-your-organization)

**For Individual Claude Users**

1. Download the ZIP file for the **instrument-data-to-allotrope** skill [here(opens in new tab)](https://github.com/anthropics/life-sciences/releases/download/v1.1.1/instrument-data-to-allotrope-v1.1.1.zip)
2. From [Claude.ai(opens in new tab)](http://claude.ai), navigate to Settings > Capabilities > Skills (if Skills is not available, contact your team admin)
3. Click “Upload skill”
4. Upload the skill zip file

## **How to access the skills in Claude Code**[](#how-to-access-the-skills-in-claude-code)

1. Download the [ZIP file for the instrument-data-to-allotrope skill(opens in new tab)](https://github.com/anthropics/life-sciences/releases/download/v1.1.1/instrument-data-to-allotrope-v1.1.1.zip)
2. On your own computer, unzip it into a new folder named `instrument-data-to-allotrope` inside `~/.claude/skills/`, so that the skill's `SKILL.md` file is at `~/.claude/skills/instrument-data-to-allotrope/SKILL.md`
3. Start Claude Code and run `/skills` to check that **instrument-data-to-allotrope** is listed

Learn about [where Claude Code loads skills from(opens in new tab)](https://code.claude.com/docs/en/skills#where-skills-live).

* [What is the Instrument Data to Allotrope skill?](#what-is-the-instrument-data-to-allotrope-skill)
* [Who should use the Instrument Data to Allotrope skill?](#who-should-use-the-instrument-data-to-allotrope-skill)
* [How to access the skill in Claude.ai](#how-to-access-the-skill-in-claudeai)
* [How to access the skills in Claude Code](#how-to-access-the-skills-in-claude-code)
