<!-- source: https://platform.claude.com/docs/en/managed-agents/skills -->

# Skills
Attach reusable, filesystem-based expertise to your agent for domain-specific workflows.
Skills are reusable, filesystem-based resources that give your agent domain-specific expertise: workflows, context, and best practices that turn a general-purpose agent into a specialist. Unlike prompts (conversation-level instructions for one-off tasks), skills load on demand, only impacting the context window when needed.
You can attach two types of skill. Both work the same way: your agent invokes them automatically when they are relevant to the task.
  * **Pre-built Anthropic skills:** Common document tasks such as PowerPoint, Excel, Word, and PDF handling.
  * **Custom skills:** Skills you author and upload to your workspace.

To learn how to author custom skills, see [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) and [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices). This page assumes you already have skills available in your workspace or are using Anthropic pre-built skills.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Attach skills to an agent
Attach skills when creating an agent. Each session supports up to 20 skills total, counted across every agent in the session (see [Multiagent sessions](https://platform.claude.com/docs/en/managed-agents/multi-agent)).
Each entry in the `skills` array uses the following fields:  
| Field  | Description  |  
| --- | --- |  
| `type`  | Either `anthropic` for pre-built skills or `custom` for workspace-authored skills.  |  
| `skill_id`  | The skill identifier. For Anthropic skills, use the short name (for example, `xlsx`). For custom skills, use the `skill_*` ID returned at creation.  |  
| `version`  | Custom skills only. Pin to a specific version or use `latest`.  |  
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create <<'YAML'
name: Financial Analyst
model: claude-opus-4-8
system: You are a financial analysis agent.
skills:
  - type: anthropic
    skill_id: xlsx
  - type: custom
    skill_id: skill_abc123
    version: latest
YAML

  * [Attach skills to an agent](https://platform.claude.com/docs/en/managed-agents/skills#attach-skills-to-an-agent)

Managed Agents/Define your agent
# Skills
Attach reusable, filesystem-based expertise to your agent for domain-specific workflows.
Skills are reusable, filesystem-based resources that give your agent domain-specific expertise: workflows, context, and best practices that turn a general-purpose agent into a specialist. Unlike prompts (conversation-level instructions for one-off tasks), skills load on demand, only impacting the context window when needed.
You can attach two types of skill. Both work the same way: your agent invokes them automatically when they are relevant to the task.
  * **Pre-built Anthropic skills:** Common document tasks such as PowerPoint, Excel, Word, and PDF handling.
  * **Custom skills:** Skills you author and upload to your workspace.

To learn how to author custom skills, see [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) and [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices). This page assumes you already have skills available in your workspace or are using Anthropic pre-built skills.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Attach skills to an agent
Attach skills when creating an agent. Each session supports up to 20 skills total, counted across every agent in the session (see [Multiagent sessions](https://platform.claude.com/docs/en/managed-agents/multi-agent)).
Each entry in the `skills` array uses the following fields:  
| Field  | Description  |  
| --- | --- |  
| `type`  | Either `anthropic` for pre-built skills or `custom` for workspace-authored skills.  |  
| `skill_id`  | The skill identifier. For Anthropic skills, use the short name (for example, `xlsx`). For custom skills, use the `skill_*` ID returned at creation.  |  
| `version`  | Custom skills only. Pin to a specific version or use `latest`.  |  
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create <<'YAML'
name: Financial Analyst
model: claude-opus-4-8
system: You are a financial analysis agent.
skills:
  - type: anthropic
    skill_id: xlsx
  - type: custom
    skill_id: skill_abc123
    version: latest
YAML
