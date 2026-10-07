<!-- source: https://claude.com/resources/guides/the-complete-guide-to-building-skills-for-claude/resources-and-references -->

Chapter 074 min read

# Resources and references

4 min read

4 min remaining

If you're building your first skill, start with the Best Practices Guide, then reference the API docs as needed.

## Official documentation

#### Anthropic resources

* [Best Practices Guide (opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
* [Skills Documentation (opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
* [API Reference (opens in new tab)](https://platform.claude.com/docs/en/api/overview)
* [MCP Documentation (opens in new tab)](https://modelcontextprotocol.io)

#### Blog posts

* [Introducing Agent Skills (opens in new tab)](https://claude.com/resources/articles/skills)
* [Engineering Blog: Equipping Agents for the Real World (opens in new tab)](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
* [Skills Explained (opens in new tab)](https://claude.com/resources/articles/skills-explained)
* [How to Create Skills for Claude (opens in new tab)](https://claude.com/resources/articles/how-to-create-skills-key-steps-limitations-and-examples)
* [Building Skills for Claude Code (opens in new tab)](https://www.claude.com/blog/building-skills-for-claude-code)
* [Improving Frontend Design through Skills (opens in new tab)](https://claude.com/resources/articles/improving-frontend-design-through-skills)

## Example skills

#### Public skills repository

* GitHub: [anthropics/skills (opens in new tab)](https://github.com/anthropics/skills)
* Contains Anthropic-created skills you can customize

## Tools and utilities

#### skill-creator skill

* Built into Claude.ai and available for Claude Code
* Can generate skills from descriptions
* Reviews and provides recommendations
* Use: "Help me build a skill using skill-creator"

#### Validation

* skill-creator can assess your skills
* Ask: "Review this skill and suggest improvements"

## Getting support

#### For technical questions

* General questions: Community forums at the [Claude Developers Discord (opens in new tab)](https://discord.com/invite/6PPFFzqPDZ)

#### For bug reports

* GitHub Issues: [anthropics/skills/issues (opens in new tab)](https://github.com/anthropics/skills/issues)
* Include: Skill name, error message, steps to reproduce

## Reference A: Quick checklist

Use this checklist to validate your skill before and after upload. If you want a faster start, use the skill-creator skill to generate your first draft, then run through this list to make sure you haven't missed anything.

### Before you start

* Identified 2-3 concrete use cases
* Tools identified (built-in or MCP)
* Reviewed this guide and example skills
* Planned folder structure

### During development

* Folder named in kebab-case
* SKILL.md file exists (exact spelling)
* YAML frontmatter has --- delimiters
* name field: kebab-case, no spaces, no capitals
* description includes WHAT and WHEN
* No XML tags (< >) anywhere
* Instructions are clear and actionable
* Error handling included
* Examples provided
* References clearly linked

### Before upload

* Tested triggering on obvious tasks
* Tested triggering on paraphrased requests
* Verified doesn't trigger on unrelated topics
* Functional tests pass
* Tool integration works (if applicable)
* Compressed as .zip file

### After upload

* Test in real conversations
* Monitor for under/over-triggering
* Collect user feedback
* Iterate on description and instructions
* Update version in metadata

## Reference B: YAML frontmatter

### Required fields

Copy

```
---
name: skill-name-in-kebab-case
description: What it does and when to use it. Include specific trigger phrases.
---
```

### All optional fields

Copy

```
name: skill-name
description: [required description]
license: MIT # Optional: License for open-source
allowed-tools: "Bash(python:*) Bash(npm:*) WebFetch" # Optional: Restrict tool access
metadata: # Optional: Custom fields
  author: Company Name
  version: 1.0.0
  mcp-server: server-name
  category: productivity
  tags: [project-management, automation]
  documentation: https://example.com/docs
  support: support@example.com
```

### Security notes

#### Allowed

* Any standard YAML types (strings, numbers, booleans, lists, objects)
* Custom metadata fields
* Long descriptions (up to 1024 characters)

#### Forbidden

* XML angle brackets (< >) - security restriction
* Code execution in YAML (uses safe YAML parsing)
* Skills named with "claude" or "anthropic" prefix (reserved)

## Reference C: Complete skill examples

For full, production-ready skills demonstrating the patterns in this guide:

* Document Skills - [PDF (opens in new tab)](https://github.com/anthropics/skills/tree/main/skills/pdf), [DOCX (opens in new tab)](https://github.com/anthropics/skills/tree/main/skills/docx), [PPTX (opens in new tab)](https://github.com/anthropics/skills/tree/main/skills/pptx), [XLSX (opens in new tab)](https://github.com/anthropics/skills/tree/main/skills/xlsx) creation
* [Example Skills (opens in new tab)](https://github.com/anthropics/skills/tree/main/skills) - Various workflow patterns
* [Partner Skills Directory (opens in new tab)](https://www.claude.com/connectors) - View skills from various partners such as Asana, Atlassian, Canva, Figma, Sentry, Zapier, and more

These repositories stay up-to-date and include additional examples beyond what's covered here. Clone them, modify them for your use case, and use them as templates.

## Enjoyed the guide?

Take it with you or get in touch with us.

[Download now (opens in new tab)](https://assets.claude.com/3678ba816db40b2e13bd5f00af201fc9e4b95b12.pdf?dl=)[Contact sales](https://claude.com/contact-sales)

Resources and references - The complete guide to building Skills for Claude | Claude by Anthropic
