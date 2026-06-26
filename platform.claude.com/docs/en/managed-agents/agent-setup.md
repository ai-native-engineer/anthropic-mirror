<!-- source: https://platform.claude.com/docs/en/managed-agents/agent-setup -->

# Define your agent
Create a reusable, versioned agent configuration.
An agent is a reusable, versioned configuration that defines persona and capabilities. It bundles the model, system prompt, tools, MCP servers, and skills that shape how Claude behaves during a session.
Create the agent once as a reusable resource and reference it by ID each time you [start a session](https://platform.claude.com/docs/en/managed-agents/sessions). Agents are versioned and easier to manage across many sessions.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Agent configuration fields  
| Field  | Description  |  
| --- | --- |  
| `name`  | Required. A human-readable name for the agent.  |  
| `model`  | Required. The Claude [model](https://platform.claude.com/docs/en/about-claude/models/overview) that powers the agent. Accepts a model ID string or an object, for example `{"id": "claude-opus-4-8"}`. All Claude 4.5-family and later models are supported.  |  
| `system`  | A [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role) that defines the agent's behavior and persona. The system prompt is distinct from [user messages](https://platform.claude.com/docs/en/managed-agents/reference#event-types), which should describe the work to be done.  |  
| `tools`  | The tools available to the agent. Combines [pre-built agent tools](https://platform.claude.com/docs/en/managed-agents/tools), [MCP tools](https://platform.claude.com/docs/en/managed-agents/mcp-connector), and [custom tools](https://platform.claude.com/docs/en/managed-agents/tools#custom-tools).  |  
| `mcp_servers`  |  [MCP servers](https://platform.claude.com/docs/en/managed-agents/mcp-connector) that provide standardized third-party capabilities.  |  
| `skills`  |  [Skills](https://platform.claude.com/docs/en/managed-agents/skills) that supply domain-specific context with progressive disclosure.  |  
| `multiagent`  | A coordinator declaration listing the agents this agent can delegate to. See [Multiagent sessions](https://platform.claude.com/docs/en/managed-agents/multi-agent).  |  
| `description`  | A description of what the agent does.  |  
| `metadata`  | Arbitrary key-value pairs for your own tracking.  |  
Create an agent
The following example defines a coding agent that uses Claude Opus 4.8 with access to the pre-built agent toolset. The toolset lets the agent write code, read files, search the web, and more. See the [agent tools reference](https://platform.claude.com/docs/en/managed-agents/tools) for the full list of supported tools.
The examples use curl, the `ant` CLI, or one of the SDKs. If you haven't set one up, the [quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart#install-the-cli) covers installation and client setup.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

agent=$(ant beta:agents create \
  --name "Coding Assistant" \
  --model '{id: claude-opus-4-8}' \
  --system "You are a helpful coding agent." \
  --tool '{type: agent_toolset_20260401}' \
  --format json)

AGENT_ID=$(jq -r '.id' <<< "$agent")
AGENT_VERSION=$(jq -r '.version' <<< "$agent")


To use Claude Opus 4.8, Claude Opus 4.7, or Claude Opus 4.6 with [fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode), pass `model` as an object, for example: `{"id": "claude-opus-4-8", "speed": "fast"}`.
The response echoes your configuration and adds `id`, `type`, `version`, `created_at`, `updated_at`, and `archived_at` fields. The `version` starts at 1 and increments each time an update changes the agent.

  "id": "agent_01HqR2k7vXbZ9mNpL3wYcT8f",
  "type": "agent",
  "name": "Coding Assistant",
  "model": {
    "id": "claude-opus-4-8",
    "speed": "standard"
  "system": "You are a helpful coding agent.",
  "description": null,
  "tools": [
      "type": "agent_toolset_20260401",
      "default_config": {
        "permission_policy": { "type": "always_allow" }
  ],
  "skills": [],
  "mcp_servers": [],
  "metadata": {},
  "version": 1,
  "created_at": "2026-04-03T18:24:10.412Z",
  "updated_at": "2026-04-03T18:24:10.412Z",
  "archived_at": null

The `default_config` on the toolset shows its default [permission policy](https://platform.claude.com/docs/en/managed-agents/permission-policies), `always_allow`, which applies unless you configure one.
Update an agent
Updating an agent generates a new version when the configuration changes. The `version` field is required and must match the agent's current version, so you always update from a known state. A version mismatch returns a 409, and updates to archived agents are rejected.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents update \
  --agent-id "$AGENT_ID" \
  --version "$AGENT_VERSION" \
  --system "You are a helpful coding agent. Always write tests."

### 
Update semantics
  * **Omitted fields are preserved.** You only need to include the fields you want to change.
  * **Scalar fields** (`model`, `system`, `name`, `description`) are replaced with the new value. `system` and `description` can be cleared by passing `null`. `model` and `name` are mandatory and cannot be cleared.
  * **Array fields** (`tools`, `mcp_servers`, `skills`) are fully replaced by the new array. To clear an array field entirely, pass `null` or an empty array.
  * **`multiagent`**is replaced as a whole, including its`agents` roster. Pass `null` to clear it.
  * **Metadata** is merged at the key level. Keys you provide are added or updated. Keys you omit are preserved. To delete a specific key, set its value to `null`.
  * **No-op detection.** If the update produces no change relative to the current version, no new version is created and the existing version is returned.
  * **Coordinator rosters are not updated.** Coordinators that reference this agent in their `multiagent.agents` roster keep the version that was pinned when the coordinator was created or last updated, even if the reference omits `version`. To delegate to the new version, [update the coordinator](https://platform.claude.com/docs/en/managed-agents/multi-agent#configure-the-coordinator) so its roster references it.

Agent lifecycle  
| Operation  | Behavior  |  
| --- | --- |  
| **Update**  | Generates a new agent version when the configuration changes.  |  
| **List versions**  | Returns the full version history so you can track changes over time.  |  
| **Archive**  | Makes the agent read-only. New sessions cannot reference it, but existing sessions continue to run.  |  
### 
List versions
Fetch the full version history to track how an agent has changed over time. Results are paginated, and the SDK examples fetch every page automatically.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents:versions list --agent-id "$AGENT_ID"

### 
Archive an agent
Archiving makes the agent read-only and cannot be undone. Existing sessions continue to run, but new sessions cannot reference the agent. The response sets `archived_at` to the archive timestamp.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents archive --agent-id "$AGENT_ID"

Next steps
[  Tools Configure tools available to your agent. ](https://platform.claude.com/docs/en/managed-agents/tools)[  Skills Attach reusable, filesystem-based expertise to your agent for domain-specific workflows. ](https://platform.claude.com/docs/en/managed-agents/skills)[  Start a session Create a session to run your agent and begin executing tasks. ](https://platform.claude.com/docs/en/managed-agents/sessions)[  Reference Event types, self-hosted worker CLI flags, supported MCP server types, rate limits, and branding guidelines for Claude Managed Agents. ](https://platform.claude.com/docs/en/managed-agents/reference)
  * [Agent configuration fields](https://platform.claude.com/docs/en/managed-agents/agent-setup#agent-configuration-fields)
  * [Create an agent](https://platform.claude.com/docs/en/managed-agents/agent-setup#create-an-agent)
  * [Update an agent](https://platform.claude.com/docs/en/managed-agents/agent-setup#update-an-agent)
  * [Update semantics](https://platform.claude.com/docs/en/managed-agents/agent-setup#update-semantics)
  * [Agent lifecycle](https://platform.claude.com/docs/en/managed-agents/agent-setup#agent-lifecycle)
  * [List versions](https://platform.claude.com/docs/en/managed-agents/agent-setup#list-versions)
  * [Archive an agent](https://platform.claude.com/docs/en/managed-agents/agent-setup#archive-an-agent)
  * [Next steps](https://platform.claude.com/docs/en/managed-agents/agent-setup#next-steps)

Managed Agents/Define your agent
# Define your agent
Create a reusable, versioned agent configuration.
An agent is a reusable, versioned configuration that defines persona and capabilities. It bundles the model, system prompt, tools, MCP servers, and skills that shape how Claude behaves during a session.
Create the agent once as a reusable resource and reference it by ID each time you [start a session](https://platform.claude.com/docs/en/managed-agents/sessions). Agents are versioned and easier to manage across many sessions.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Agent configuration fields  
| Field  | Description  |  
| --- | --- |  
| `name`  | Required. A human-readable name for the agent.  |  
| `model`  | Required. The Claude [model](https://platform.claude.com/docs/en/about-claude/models/overview) that powers the agent. Accepts a model ID string or an object, for example `{"id": "claude-opus-4-8"}`. All Claude 4.5-family and later models are supported.  |  
| `system`  | A [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role) that defines the agent's behavior and persona. The system prompt is distinct from [user messages](https://platform.claude.com/docs/en/managed-agents/reference#event-types), which should describe the work to be done.  |  
| `tools`  | The tools available to the agent. Combines [pre-built agent tools](https://platform.claude.com/docs/en/managed-agents/tools), [MCP tools](https://platform.claude.com/docs/en/managed-agents/mcp-connector), and [custom tools](https://platform.claude.com/docs/en/managed-agents/tools#custom-tools).  |  
| `mcp_servers`  |  [MCP servers](https://platform.claude.com/docs/en/managed-agents/mcp-connector) that provide standardized third-party capabilities.  |  
| `skills`  |  [Skills](https://platform.claude.com/docs/en/managed-agents/skills) that supply domain-specific context with progressive disclosure.  |  
| `multiagent`  | A coordinator declaration listing the agents this agent can delegate to. See [Multiagent sessions](https://platform.claude.com/docs/en/managed-agents/multi-agent).  |  
| `description`  | A description of what the agent does.  |  
| `metadata`  | Arbitrary key-value pairs for your own tracking.  |  
Create an agent
The following example defines a coding agent that uses Claude Opus 4.8 with access to the pre-built agent toolset. The toolset lets the agent write code, read files, search the web, and more. See the [agent tools reference](https://platform.claude.com/docs/en/managed-agents/tools) for the full list of supported tools.
The examples use curl, the `ant` CLI, or one of the SDKs. If you haven't set one up, the [quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart#install-the-cli) covers installation and client setup.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

agent=$(ant beta:agents create \
  --name "Coding Assistant" \
  --model '{id: claude-opus-4-8}' \
  --system "You are a helpful coding agent." \
  --tool '{type: agent_toolset_20260401}' \
  --format json)

AGENT_ID=$(jq -r '.id' <<< "$agent")
AGENT_VERSION=$(jq -r '.version' <<< "$agent")


To use Claude Opus 4.8, Claude Opus 4.7, or Claude Opus 4.6 with [fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode), pass `model` as an object, for example: `{"id": "claude-opus-4-8", "speed": "fast"}`.
The response echoes your configuration and adds `id`, `type`, `version`, `created_at`, `updated_at`, and `archived_at` fields. The `version` starts at 1 and increments each time an update changes the agent.

  "id": "agent_01HqR2k7vXbZ9mNpL3wYcT8f",
  "type": "agent",
  "name": "Coding Assistant",
  "model": {
    "id": "claude-opus-4-8",
    "speed": "standard"
  "system": "You are a helpful coding agent.",
  "description": null,
  "tools": [
      "type": "agent_toolset_20260401",
      "default_config": {
        "permission_policy": { "type": "always_allow" }
  ],
  "skills": [],
  "mcp_servers": [],
  "metadata": {},
  "version": 1,
  "created_at": "2026-04-03T18:24:10.412Z",
  "updated_at": "2026-04-03T18:24:10.412Z",
  "archived_at": null

The `default_config` on the toolset shows its default [permission policy](https://platform.claude.com/docs/en/managed-agents/permission-policies), `always_allow`, which applies unless you configure one.
Update an agent
Updating an agent generates a new version when the configuration changes. The `version` field is required and must match the agent's current version, so you always update from a known state. A version mismatch returns a 409, and updates to archived agents are rejected.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents update \
  --agent-id "$AGENT_ID" \
  --version "$AGENT_VERSION" \
  --system "You are a helpful coding agent. Always write tests."

### 
Update semantics
  * **Omitted fields are preserved.** You only need to include the fields you want to change.
  * **Scalar fields** (`model`, `system`, `name`, `description`) are replaced with the new value. `system` and `description` can be cleared by passing `null`. `model` and `name` are mandatory and cannot be cleared.
  * **Array fields** (`tools`, `mcp_servers`, `skills`) are fully replaced by the new array. To clear an array field entirely, pass `null` or an empty array.
  * **`multiagent`**is replaced as a whole, including its`agents` roster. Pass `null` to clear it.
  * **Metadata** is merged at the key level. Keys you provide are added or updated. Keys you omit are preserved. To delete a specific key, set its value to `null`.
  * **No-op detection.** If the update produces no change relative to the current version, no new version is created and the existing version is returned.
  * **Coordinator rosters are not updated.** Coordinators that reference this agent in their `multiagent.agents` roster keep the version that was pinned when the coordinator was created or last updated, even if the reference omits `version`. To delegate to the new version, [update the coordinator](https://platform.claude.com/docs/en/managed-agents/multi-agent#configure-the-coordinator) so its roster references it.

Agent lifecycle  
| Operation  | Behavior  |  
| --- | --- |  
| **Update**  | Generates a new agent version when the configuration changes.  |  
| **List versions**  | Returns the full version history so you can track changes over time.  |  
| **Archive**  | Makes the agent read-only. New sessions cannot reference it, but existing sessions continue to run.  |  
### 
List versions
Fetch the full version history to track how an agent has changed over time. Results are paginated, and the SDK examples fetch every page automatically.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents:versions list --agent-id "$AGENT_ID"

### 
Archive an agent
Archiving makes the agent read-only and cannot be undone. Existing sessions continue to run, but new sessions cannot reference the agent. The response sets `archived_at` to the archive timestamp.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents archive --agent-id "$AGENT_ID"

Next steps
[  Tools Configure tools available to your agent. ](https://platform.claude.com/docs/en/managed-agents/tools)[  Skills Attach reusable, filesystem-based expertise to your agent for domain-specific workflows. ](https://platform.claude.com/docs/en/managed-agents/skills)[  Start a session Create a session to run your agent and begin executing tasks. ](https://platform.claude.com/docs/en/managed-agents/sessions)[  Reference Event types, self-hosted worker CLI flags, supported MCP server types, rate limits, and branding guidelines for Claude Managed Agents. ](https://platform.claude.com/docs/en/managed-agents/reference)
