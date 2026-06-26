<!-- source: https://platform.claude.com/docs/en/managed-agents/reference -->

# Reference
Event types, self-hosted worker CLI flags, supported MCP server types, rate limits, and branding guidelines for Claude Managed Agents.
This page collects reference material for Claude Managed Agents. For task-oriented guides, follow the links in each section. For the operations on the session resource, see [Session operations](https://platform.claude.com/docs/en/managed-agents/session-operations).
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Event types
Event type strings follow a `{domain}.{action}` naming convention. See [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) for sending, streaming, and listing events.
User events
User events
Agent events
Agent events
Session events
Session events
Span events
Span events
System events
System events  
| Type  | Description  |  
| --- | --- |  
| `user.message`  | A user message with text content.  |  
| `user.interrupt`  | Stop the agent mid-execution.  |  
| `user.custom_tool_result`  | Response to a custom tool call from the agent.  |  
| `user.tool_confirmation`  | Approve or deny an agent or MCP tool call when a permission policy requires confirmation.  |  
| `user.define_outcome`  | Define an [outcome](https://platform.claude.com/docs/en/managed-agents/define-outcomes) for the agent to work toward.  |  
| `user.tool_result`  | For sessions with `self_hosted` [environments](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) only, your integration is responsible for providing `agent_toolset` results. The SDK helpers and CLI do this automatically.  |  
Self-hosted worker
These are the `ant beta:worker` CLI flags for the pre-built worker that drives a `self_hosted` environment. See [Self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) for setting up the environment, running a worker, and the SDK helper options.  
| Flag  | Description  |  
| --- | --- |  
| `--environment-id`  | The environment to poll for work. Also reads from `ANTHROPIC_ENVIRONMENT_ID`.  |  
| `--environment-key`  | Authenticates the worker with this environment. Also reads from `ANTHROPIC_ENVIRONMENT_KEY`.  |  
| `--workdir`  | Directory where skills are downloaded and tools read and write files. Defaults to `.` (the current directory); the system default working directory is `/workspace`.  |  
| `--on-work`  | Script to call for each claimed work item instead of running tools in-process. Receives session details as environment variables.  |  
| `--unrestricted-paths`  | Allow tool calls to access paths outside `--workdir`.  |  
| `--max-idle`  | How long to wait after the session goes idle with an `end_turn` [stop reason](https://platform.claude.com/docs/en/api/handling-stop-reasons) before shutting down. Defaults to `60s`.  |  
| `--log-format`  | Log output format. Use `json` for structured log ingestion. Defaults to `text`.  |  
Supported MCP server types
Claude Managed Agents connects to [remote MCP servers](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers) that expose an HTTP endpoint, or to private MCP servers through [MCP tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview). The server must support the MCP protocol's streamable HTTP transport. See [MCP connector](https://platform.claude.com/docs/en/managed-agents/mcp-connector) for declaring servers on an agent.
For more information on MCP and building MCP servers, see the [MCP documentation](https://modelcontextprotocol.io).
Rate limits
Managed Agents endpoints are rate-limited per organization:  
| Operation  | Limit  |  
| --- | --- |  
| Create endpoints (such as agents, sessions, and environments)  | 300 requests per minute  |  
| Read endpoints (such as retrieve, list, and stream)  | 600 requests per minute  |  
Organization-level [spend limits and tier-based rate limits](https://platform.claude.com/docs/en/api/rate-limits) also apply.
Branding guidelines
For partners integrating Claude Managed Agents, use of Claude branding is optional. When referencing Claude in your product:
**Allowed:**
  * "Claude Agent" (preferred for dropdown menus)
  * "Claude" (when within a menu already labeled "Agents")
  * "{YourAgentName} Powered by Claude" (if you have an existing agent name)

**Not permitted:**
  * "Claude Code" or "Claude Code Agent"
  * "Claude Cowork" or "Claude Cowork Agent"
  * Claude Code-branded ASCII art or visual elements that mimic Claude Code

Your product should maintain its own branding and not appear to be Claude Code, Claude Cowork, or any other Anthropic product. For questions about branding compliance, contact the Anthropic [sales team](https://www.anthropic.com/contact-sales).
  * [Event types](https://platform.claude.com/docs/en/managed-agents/reference#event-types)
  * [Self-hosted worker](https://platform.claude.com/docs/en/managed-agents/reference#self-hosted-worker)
  * [Supported MCP server types](https://platform.claude.com/docs/en/managed-agents/reference#supported-mcp-server-types)
  * [Rate limits](https://platform.claude.com/docs/en/managed-agents/reference#rate-limits)
  * [Branding guidelines](https://platform.claude.com/docs/en/managed-agents/reference#branding-guidelines)

Managed Agents/Reference
# Reference
Event types, self-hosted worker CLI flags, supported MCP server types, rate limits, and branding guidelines for Claude Managed Agents.
This page collects reference material for Claude Managed Agents. For task-oriented guides, follow the links in each section. For the operations on the session resource, see [Session operations](https://platform.claude.com/docs/en/managed-agents/session-operations).
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Event types
Event type strings follow a `{domain}.{action}` naming convention. See [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) for sending, streaming, and listing events.
User events
User events
Agent events
Agent events
Session events
Session events
Span events
Span events
System events
System events  
| Type  | Description  |  
| --- | --- |  
| `user.message`  | A user message with text content.  |  
| `user.interrupt`  | Stop the agent mid-execution.  |  
| `user.custom_tool_result`  | Response to a custom tool call from the agent.  |  
| `user.tool_confirmation`  | Approve or deny an agent or MCP tool call when a permission policy requires confirmation.  |  
| `user.define_outcome`  | Define an [outcome](https://platform.claude.com/docs/en/managed-agents/define-outcomes) for the agent to work toward.  |  
| `user.tool_result`  | For sessions with `self_hosted` [environments](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) only, your integration is responsible for providing `agent_toolset` results. The SDK helpers and CLI do this automatically.  |  
Self-hosted worker
These are the `ant beta:worker` CLI flags for the pre-built worker that drives a `self_hosted` environment. See [Self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) for setting up the environment, running a worker, and the SDK helper options.  
| Flag  | Description  |  
| --- | --- |  
| `--environment-id`  | The environment to poll for work. Also reads from `ANTHROPIC_ENVIRONMENT_ID`.  |  
| `--environment-key`  | Authenticates the worker with this environment. Also reads from `ANTHROPIC_ENVIRONMENT_KEY`.  |  
| `--workdir`  | Directory where skills are downloaded and tools read and write files. Defaults to `.` (the current directory); the system default working directory is `/workspace`.  |  
| `--on-work`  | Script to call for each claimed work item instead of running tools in-process. Receives session details as environment variables.  |  
| `--unrestricted-paths`  | Allow tool calls to access paths outside `--workdir`.  |  
| `--max-idle`  | How long to wait after the session goes idle with an `end_turn` [stop reason](https://platform.claude.com/docs/en/api/handling-stop-reasons) before shutting down. Defaults to `60s`.  |  
| `--log-format`  | Log output format. Use `json` for structured log ingestion. Defaults to `text`.  |  
Supported MCP server types
Claude Managed Agents connects to [remote MCP servers](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers) that expose an HTTP endpoint, or to private MCP servers through [MCP tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview). The server must support the MCP protocol's streamable HTTP transport. See [MCP connector](https://platform.claude.com/docs/en/managed-agents/mcp-connector) for declaring servers on an agent.
For more information on MCP and building MCP servers, see the [MCP documentation](https://modelcontextprotocol.io).
Rate limits
Managed Agents endpoints are rate-limited per organization:  
| Operation  | Limit  |  
| --- | --- |  
| Create endpoints (such as agents, sessions, and environments)  | 300 requests per minute  |  
| Read endpoints (such as retrieve, list, and stream)  | 600 requests per minute  |  
Organization-level [spend limits and tier-based rate limits](https://platform.claude.com/docs/en/api/rate-limits) also apply.
Branding guidelines
For partners integrating Claude Managed Agents, use of Claude branding is optional. When referencing Claude in your product:
**Allowed:**
  * "Claude Agent" (preferred for dropdown menus)
  * "Claude" (when within a menu already labeled "Agents")
  * "{YourAgentName} Powered by Claude" (if you have an existing agent name)

**Not permitted:**
  * "Claude Code" or "Claude Code Agent"
  * "Claude Cowork" or "Claude Cowork Agent"
  * Claude Code-branded ASCII art or visual elements that mimic Claude Code

Your product should maintain its own branding and not appear to be Claude Code, Claude Cowork, or any other Anthropic product. For questions about branding compliance, contact the Anthropic [sales team](https://www.anthropic.com/contact-sales).
