<!-- source: https://platform.claude.com/docs/en/managed-agents/permission-policies -->

# Permission policies
Control when agent and MCP tools execute.
Permission policies control whether server-executed tools (the pre-built agent toolset and MCP toolset) run automatically or wait for your approval. Custom tools are executed by your application and controlled by you, so they are not governed by permission policies.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Permission policy types  
| Policy  | Behavior  |  
| --- | --- |  
| `always_allow`  | The tool executes automatically with no confirmation.  |  
| `always_ask`  | The session pauses and waits for your approval before executing. See [Respond to confirmation requests](https://platform.claude.com/docs/en/managed-agents/permission-policies#respond-to-confirmation-requests) for the event flow.  |  
Each toolset kind has its own default: the agent toolset defaults to `always_allow`, and MCP toolsets default to `always_ask`.
A permission policy controls when an enabled tool runs. To remove a tool from the agent entirely, disable it instead. See [Disabling specific tools](https://platform.claude.com/docs/en/managed-agents/tools#disabling-specific-tools).
Set a policy for a toolset
You set permission policies in the agent's `tools` configuration when you create the agent, and you can change them later by [updating the agent](https://platform.claude.com/docs/en/managed-agents/agent-setup#update-an-agent). Running sessions keep the toolset configuration they were created with. Updates apply to sessions created afterward.
### 
Agent toolset permissions
When creating an agent, you can apply a policy to every tool in `agent_toolset_20260401` using `default_config.permission_policy`:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create <<'YAML'
name: Coding Assistant
model: claude-opus-4-8
tools:
  - type: agent_toolset_20260401
    default_config:
      permission_policy:
        type: always_ask
YAML

`default_config` is optional. If you omit it, the agent toolset is enabled with the default permission policy, `always_allow`.
### 
MCP toolset permissions
MCP toolsets default to `always_ask`. This ensures that new tools added to an MCP server do not execute in your application without approval. To auto-approve tools from a trusted MCP server, set `default_config.permission_policy` on the `mcp_toolset` entry.
The `mcp_server_name` must match the `name` of a server in the `mcp_servers` array.
This example connects a GitHub MCP server and allows its tools to run without confirmation:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create <<'YAML'
name: Dev Assistant
model: claude-opus-4-8
mcp_servers:
  - type: url
    name: github
    url: https://mcp.example.com/github
tools:
  - type: agent_toolset_20260401
  - type: mcp_toolset
    mcp_server_name: github
    default_config:
      permission_policy:
        type: always_allow
YAML

Override an individual tool policy
Use the `configs` array to override the default for individual tools. The `name` values for the agent toolset are listed in [Available tools](https://platform.claude.com/docs/en/managed-agents/tools#available-tools). This example allows the full agent toolset by default but requires confirmation before any bash command runs:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create <<'YAML'
name: Coding Assistant
model: claude-opus-4-8
tools:
  - type: agent_toolset_20260401
    default_config:
      permission_policy:
        type: always_allow
    configs:
      - name: bash
        permission_policy:
          type: always_ask
YAML

Pass this `tools` configuration in the agent create request (the CLI tab shows the complete command). MCP toolsets support the same per-tool overrides, with `name` set to the tool name reported by the MCP server. See [Configure which MCP tools are available](https://platform.claude.com/docs/en/managed-agents/mcp-connector#configure-which-mcp-tools-are-available).
Respond to confirmation requests
When the agent invokes a tool with an `always_ask` policy:
  1. The session emits an `agent.tool_use` or `agent.mcp_tool_use` event.
  2. The session pauses with a `session.status_idle` event whose `stop_reason.type` is `requires_action`. The blocking event IDs are in the `stop_reason.event_ids` array. The session waits indefinitely for a response.
  3. Send a `user.tool_confirmation` event for each blocking event, passing the event ID in the `tool_use_id` parameter. Set `result` to `"allow"` or `"deny"`. Use `deny_message` to explain a denial. You can send several confirmations in a single `events` request.
  4. Once all blocking events are resolved, the session transitions back to `running`. Allowed tools execute. Denied tools do not run, and the agent receives a tool result saying the call was rejected, including your `deny_message`.

In the following examples, the tool-use event IDs come from the `stop_reason.event_ids` array of the `session.status_idle` event. Learn more about receiving events in the [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#integrating-events) guide, or [subscribe to webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks) to be notified when a session pauses for input.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

# Allow the tool to execute
ant beta:sessions:events send \
  --session-id "$SESSION_ID" \
  --event "{type: user.tool_confirmation, tool_use_id: $AGENT_TOOL_USE_EVENT_ID, result: allow}"

# Or deny it with an explanation
ant beta:sessions:events send \
  --session-id "$SESSION_ID" \
  --event "{type: user.tool_confirmation, tool_use_id: $MCP_TOOL_USE_EVENT_ID, result: deny,
    deny_message: Don't create issues in the production project. Use the staging project.}"

Custom tools
Permission policies do not apply to custom tools. When the agent invokes a custom tool, your application receives an `agent.custom_tool_use` event and is responsible for deciding whether to execute it before sending back a `user.custom_tool_result`. See [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#handling-custom-tool-calls) for the full flow.
Next steps
[ Skills Attach reusable, filesystem-based expertise to your agent for domain-specific workflows. ](https://platform.claude.com/docs/en/managed-agents/skills)[  Session event stream Send events, stream responses, and interrupt or redirect your session mid-execution. ](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)
  * [Permission policy types](https://platform.claude.com/docs/en/managed-agents/permission-policies#permission-policy-types)
  * [Set a policy for a toolset](https://platform.claude.com/docs/en/managed-agents/permission-policies#set-a-policy-for-a-toolset)
  * [Agent toolset permissions](https://platform.claude.com/docs/en/managed-agents/permission-policies#agent-toolset-permissions)
  * [MCP toolset permissions](https://platform.claude.com/docs/en/managed-agents/permission-policies#mcp-toolset-permissions)
  * [Override an individual tool policy](https://platform.claude.com/docs/en/managed-agents/permission-policies#override-an-individual-tool-policy)
  * [Respond to confirmation requests](https://platform.claude.com/docs/en/managed-agents/permission-policies#respond-to-confirmation-requests)
  * [Custom tools](https://platform.claude.com/docs/en/managed-agents/permission-policies#custom-tools)
  * [Next steps](https://platform.claude.com/docs/en/managed-agents/permission-policies#next-steps)

Managed Agents/Define your agent
# Permission policies
Control when agent and MCP tools execute.
Permission policies control whether server-executed tools (the pre-built agent toolset and MCP toolset) run automatically or wait for your approval. Custom tools are executed by your application and controlled by you, so they are not governed by permission policies.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Permission policy types  
| Policy  | Behavior  |  
| --- | --- |  
| `always_allow`  | The tool executes automatically with no confirmation.  |  
| `always_ask`  | The session pauses and waits for your approval before executing. See [Respond to confirmation requests](https://platform.claude.com/docs/en/managed-agents/permission-policies#respond-to-confirmation-requests) for the event flow.  |  
Each toolset kind has its own default: the agent toolset defaults to `always_allow`, and MCP toolsets default to `always_ask`.
A permission policy controls when an enabled tool runs. To remove a tool from the agent entirely, disable it instead. See [Disabling specific tools](https://platform.claude.com/docs/en/managed-agents/tools#disabling-specific-tools).
Set a policy for a toolset
You set permission policies in the agent's `tools` configuration when you create the agent, and you can change them later by [updating the agent](https://platform.claude.com/docs/en/managed-agents/agent-setup#update-an-agent). Running sessions keep the toolset configuration they were created with. Updates apply to sessions created afterward.
### 
Agent toolset permissions
When creating an agent, you can apply a policy to every tool in `agent_toolset_20260401` using `default_config.permission_policy`:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create <<'YAML'
name: Coding Assistant
model: claude-opus-4-8
tools:
  - type: agent_toolset_20260401
    default_config:
      permission_policy:
        type: always_ask
YAML

`default_config` is optional. If you omit it, the agent toolset is enabled with the default permission policy, `always_allow`.
### 
MCP toolset permissions
MCP toolsets default to `always_ask`. This ensures that new tools added to an MCP server do not execute in your application without approval. To auto-approve tools from a trusted MCP server, set `default_config.permission_policy` on the `mcp_toolset` entry.
The `mcp_server_name` must match the `name` of a server in the `mcp_servers` array.
This example connects a GitHub MCP server and allows its tools to run without confirmation:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create <<'YAML'
name: Dev Assistant
model: claude-opus-4-8
mcp_servers:
  - type: url
    name: github
    url: https://mcp.example.com/github
tools:
  - type: agent_toolset_20260401
  - type: mcp_toolset
    mcp_server_name: github
    default_config:
      permission_policy:
        type: always_allow
YAML

Override an individual tool policy
Use the `configs` array to override the default for individual tools. The `name` values for the agent toolset are listed in [Available tools](https://platform.claude.com/docs/en/managed-agents/tools#available-tools). This example allows the full agent toolset by default but requires confirmation before any bash command runs:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create <<'YAML'
name: Coding Assistant
model: claude-opus-4-8
tools:
  - type: agent_toolset_20260401
    default_config:
      permission_policy:
        type: always_allow
    configs:
      - name: bash
        permission_policy:
          type: always_ask
YAML

Pass this `tools` configuration in the agent create request (the CLI tab shows the complete command). MCP toolsets support the same per-tool overrides, with `name` set to the tool name reported by the MCP server. See [Configure which MCP tools are available](https://platform.claude.com/docs/en/managed-agents/mcp-connector#configure-which-mcp-tools-are-available).
Respond to confirmation requests
When the agent invokes a tool with an `always_ask` policy:
  1. The session emits an `agent.tool_use` or `agent.mcp_tool_use` event.
  2. The session pauses with a `session.status_idle` event whose `stop_reason.type` is `requires_action`. The blocking event IDs are in the `stop_reason.event_ids` array. The session waits indefinitely for a response.
  3. Send a `user.tool_confirmation` event for each blocking event, passing the event ID in the `tool_use_id` parameter. Set `result` to `"allow"` or `"deny"`. Use `deny_message` to explain a denial. You can send several confirmations in a single `events` request.
  4. Once all blocking events are resolved, the session transitions back to `running`. Allowed tools execute. Denied tools do not run, and the agent receives a tool result saying the call was rejected, including your `deny_message`.

In the following examples, the tool-use event IDs come from the `stop_reason.event_ids` array of the `session.status_idle` event. Learn more about receiving events in the [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#integrating-events) guide, or [subscribe to webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks) to be notified when a session pauses for input.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

# Allow the tool to execute
ant beta:sessions:events send \
  --session-id "$SESSION_ID" \
  --event "{type: user.tool_confirmation, tool_use_id: $AGENT_TOOL_USE_EVENT_ID, result: allow}"

# Or deny it with an explanation
ant beta:sessions:events send \
  --session-id "$SESSION_ID" \
  --event "{type: user.tool_confirmation, tool_use_id: $MCP_TOOL_USE_EVENT_ID, result: deny,
    deny_message: Don't create issues in the production project. Use the staging project.}"

Custom tools
Permission policies do not apply to custom tools. When the agent invokes a custom tool, your application receives an `agent.custom_tool_use` event and is responsible for deciding whether to execute it before sending back a `user.custom_tool_result`. See [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#handling-custom-tool-calls) for the full flow.
Next steps
[ Skills Attach reusable, filesystem-based expertise to your agent for domain-specific workflows. ](https://platform.claude.com/docs/en/managed-agents/skills)[  Session event stream Send events, stream responses, and interrupt or redirect your session mid-execution. ](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)
