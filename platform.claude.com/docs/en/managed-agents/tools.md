<!-- source: https://platform.claude.com/docs/en/managed-agents/tools -->

# Tools
Configure tools available to your agent.
Claude Managed Agents provides a set of built-in tools that Claude can use autonomously within a [session](https://platform.claude.com/docs/en/managed-agents/sessions). You control which tools are available by specifying them in the agent configuration.
Claude Managed Agents also supports custom, user-defined tools. Your application executes these tools separately and returns the results to Claude, which uses them to continue the task. To give the agent tools from an MCP server, use the [MCP connector](https://platform.claude.com/docs/en/managed-agents/mcp-connector) instead.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Available tools
The agent toolset includes the following tools. All are enabled by default when you include the toolset in your agent configuration. Use the values in the Name column to reference tools in the `configs` array.  
| Tool  | Name  | Description  |  
| --- | --- | --- |  
| Bash  | `bash`  | Execute bash commands in a shell session  |  
| Read  | `read`  | Read a file from the sandbox filesystem  |  
| Write  | `write`  | Write a file to the sandbox filesystem  |  
| Edit  | `edit`  | Perform string replacement in a file  |  
| Glob  | `glob`  | Fast file pattern matching using glob patterns  |  
| Grep  | `grep`  | Text search using regex patterns  |  
| Web fetch  | `web_fetch`  | Fetch content from a URL  |  
| Web search  | `web_search`  | Search the web for information  |  
When a tool output exceeds 100,000 tokens, it is automatically written to a file in the [sandbox](https://platform.claude.com/docs/en/managed-agents/environments). The model receives a truncated preview with the file path and can read the full content from there.
Configuring the toolset
Enable the full toolset with `agent_toolset_20260401` when creating an agent. Use the `configs` array to disable specific tools or override their settings. Each config entry can also set a `permission_policy` that controls whether the tool's calls are auto-approved or require confirmation. See [Permission policies](https://platform.claude.com/docs/en/managed-agents/permission-policies) for the available policy types.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create <<'YAML'
name: Coding Assistant
model: claude-opus-4-8
tools:
  - type: agent_toolset_20260401
    configs:
      - name: web_fetch
        enabled: false
YAML

### 
Disabling specific tools
To disable a tool, set `enabled: false` in its config entry in the toolset object of your agent's `tools` array:

  "type": "agent_toolset_20260401",
  "configs": [
    { "name": "web_fetch", "enabled": false },
    { "name": "web_search", "enabled": false }
  ]

### 
Enabling only specific tools
The `default_config` object sets the baseline for every tool in the set, and per-tool `configs` entries override it. To start with everything off and enable only what you need, set `default_config.enabled` to `false`:

  "type": "agent_toolset_20260401",
  "default_config": { "enabled": false },
  "configs": [
    { "name": "bash", "enabled": true },
    { "name": "read", "enabled": true },
    { "name": "write", "enabled": true }
  ]

Custom tools
In addition to built-in tools, you can define custom tools. Custom tools are analogous to [user-defined client tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works#user-defined-tools-client-executed) in the Messages API.
Each custom tool defines a contract: you specify what operations are available and what they return, and Claude determines when and how to call them. The model never executes anything on its own. It emits a structured request, your code runs the operation, and the result flows back into the conversation. See [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#handling-custom-tool-calls) for how to receive custom tool calls and return results during a session.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create <<'YAML'
name: Weather Agent
model: claude-opus-4-8
tools:
  - type: agent_toolset_20260401
  - type: custom
    name: get_weather
    description: Get current weather for a location
    input_schema:
      type: object
      properties:
        location:
          type: string
          description: City name
      required:
        - location
YAML

Once you've defined custom tools on the agent, the agent invokes them during a session.
### 
Best practices for custom tool definitions
  * **Provide extremely detailed descriptions.** This is by far the most important factor in tool performance. Your descriptions should explain what the tool does and when to use it (and when not to). Explain what each parameter means and how it affects the tool's behavior. Call out any important caveats or limitations. The more context you can give Claude about your tools, the better it is at determining when and how to use them. Aim for three to four sentences for each tool description, more if the tool is complex.
  * **Consolidate related operations into fewer tools.** Rather than creating a separate tool for every action (`create_pr`, `review_pr`, `merge_pr`), group them into a single tool with an `action` parameter. Fewer, more capable tools reduce selection ambiguity and make your tool surface easier for Claude to navigate.
  * **Use meaningful namespacing in tool names.** When your tools span multiple services or resources, prefix names with the resource (for example, `db_query` or `storage_read`). This makes tool selection unambiguous as your library grows.
  * **Design tool responses to return only high-signal information.** Return semantic, stable identifiers (for example, slugs or UUIDs) rather than opaque internal references, and include only the fields Claude needs to determine its next step. Bloated responses waste context and make it harder for Claude to extract what matters.

Next steps
[  MCP connector Connect MCP servers to your agents for access to external tools and data sources. ](https://platform.claude.com/docs/en/managed-agents/mcp-connector)[  Permission policies Control when agent and MCP tools execute. ](https://platform.claude.com/docs/en/managed-agents/permission-policies)[  Session event stream Send events, stream responses, and interrupt or redirect your session mid-execution. ](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)
  * [Available tools](https://platform.claude.com/docs/en/managed-agents/tools#available-tools)
  * [Configuring the toolset](https://platform.claude.com/docs/en/managed-agents/tools#configuring-the-toolset)
  * [Disabling specific tools](https://platform.claude.com/docs/en/managed-agents/tools#disabling-specific-tools)
  * [Enabling only specific tools](https://platform.claude.com/docs/en/managed-agents/tools#enabling-only-specific-tools)
  * [Custom tools](https://platform.claude.com/docs/en/managed-agents/tools#custom-tools)
  * [Best practices for custom tool definitions](https://platform.claude.com/docs/en/managed-agents/tools#best-practices-for-custom-tool-definitions)
  * [Next steps](https://platform.claude.com/docs/en/managed-agents/tools#next-steps)

Managed Agents/Define your agent
# Tools
Configure tools available to your agent.
Claude Managed Agents provides a set of built-in tools that Claude can use autonomously within a [session](https://platform.claude.com/docs/en/managed-agents/sessions). You control which tools are available by specifying them in the agent configuration.
Claude Managed Agents also supports custom, user-defined tools. Your application executes these tools separately and returns the results to Claude, which uses them to continue the task. To give the agent tools from an MCP server, use the [MCP connector](https://platform.claude.com/docs/en/managed-agents/mcp-connector) instead.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Available tools
The agent toolset includes the following tools. All are enabled by default when you include the toolset in your agent configuration. Use the values in the Name column to reference tools in the `configs` array.  
| Tool  | Name  | Description  |  
| --- | --- | --- |  
| Bash  | `bash`  | Execute bash commands in a shell session  |  
| Read  | `read`  | Read a file from the sandbox filesystem  |  
| Write  | `write`  | Write a file to the sandbox filesystem  |  
| Edit  | `edit`  | Perform string replacement in a file  |  
| Glob  | `glob`  | Fast file pattern matching using glob patterns  |  
| Grep  | `grep`  | Text search using regex patterns  |  
| Web fetch  | `web_fetch`  | Fetch content from a URL  |  
| Web search  | `web_search`  | Search the web for information  |  
When a tool output exceeds 100,000 tokens, it is automatically written to a file in the [sandbox](https://platform.claude.com/docs/en/managed-agents/environments). The model receives a truncated preview with the file path and can read the full content from there.
Configuring the toolset
Enable the full toolset with `agent_toolset_20260401` when creating an agent. Use the `configs` array to disable specific tools or override their settings. Each config entry can also set a `permission_policy` that controls whether the tool's calls are auto-approved or require confirmation. See [Permission policies](https://platform.claude.com/docs/en/managed-agents/permission-policies) for the available policy types.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create <<'YAML'
name: Coding Assistant
model: claude-opus-4-8
tools:
  - type: agent_toolset_20260401
    configs:
      - name: web_fetch
        enabled: false
YAML

### 
Disabling specific tools
To disable a tool, set `enabled: false` in its config entry in the toolset object of your agent's `tools` array:

  "type": "agent_toolset_20260401",
  "configs": [
    { "name": "web_fetch", "enabled": false },
    { "name": "web_search", "enabled": false }
  ]

### 
Enabling only specific tools
The `default_config` object sets the baseline for every tool in the set, and per-tool `configs` entries override it. To start with everything off and enable only what you need, set `default_config.enabled` to `false`:

  "type": "agent_toolset_20260401",
  "default_config": { "enabled": false },
  "configs": [
    { "name": "bash", "enabled": true },
    { "name": "read", "enabled": true },
    { "name": "write", "enabled": true }
  ]

Custom tools
In addition to built-in tools, you can define custom tools. Custom tools are analogous to [user-defined client tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works#user-defined-tools-client-executed) in the Messages API.
Each custom tool defines a contract: you specify what operations are available and what they return, and Claude determines when and how to call them. The model never executes anything on its own. It emits a structured request, your code runs the operation, and the result flows back into the conversation. See [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#handling-custom-tool-calls) for how to receive custom tool calls and return results during a session.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create <<'YAML'
name: Weather Agent
model: claude-opus-4-8
tools:
  - type: agent_toolset_20260401
  - type: custom
    name: get_weather
    description: Get current weather for a location
    input_schema:
      type: object
      properties:
        location:
          type: string
          description: City name
      required:
        - location
YAML

Once you've defined custom tools on the agent, the agent invokes them during a session.
### 
Best practices for custom tool definitions
  * **Provide extremely detailed descriptions.** This is by far the most important factor in tool performance. Your descriptions should explain what the tool does and when to use it (and when not to). Explain what each parameter means and how it affects the tool's behavior. Call out any important caveats or limitations. The more context you can give Claude about your tools, the better it is at determining when and how to use them. Aim for three to four sentences for each tool description, more if the tool is complex.
  * **Consolidate related operations into fewer tools.** Rather than creating a separate tool for every action (`create_pr`, `review_pr`, `merge_pr`), group them into a single tool with an `action` parameter. Fewer, more capable tools reduce selection ambiguity and make your tool surface easier for Claude to navigate.
  * **Use meaningful namespacing in tool names.** When your tools span multiple services or resources, prefix names with the resource (for example, `db_query` or `storage_read`). This makes tool selection unambiguous as your library grows.
  * **Design tool responses to return only high-signal information.** Return semantic, stable identifiers (for example, slugs or UUIDs) rather than opaque internal references, and include only the fields Claude needs to determine its next step. Bloated responses waste context and make it harder for Claude to extract what matters.

Next steps
[  MCP connector Connect MCP servers to your agents for access to external tools and data sources. ](https://platform.claude.com/docs/en/managed-agents/mcp-connector)[  Permission policies Control when agent and MCP tools execute. ](https://platform.claude.com/docs/en/managed-agents/permission-policies)[  Session event stream Send events, stream responses, and interrupt or redirect your session mid-execution. ](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)
