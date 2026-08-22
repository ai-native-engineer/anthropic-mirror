<!-- source: https://platform.claude.com/docs/en/api/cli/beta/sessions -->
<!-- part of: https://platform.claude.com/docs/en/api/cli/beta/sessions -->

<!-- chunk-start -->

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object { type }`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object { type }`

                        Tool calls require user confirmation before execution.

                    - `type: "write"`

                  - `beta_managed_agents_glob_tool_config: object { enabled, name, permission_policy, type }`

                    Configuration for the glob tool.

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object { type }`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object { type }`

                        Tool calls require user confirmation before execution.

                    - `type: "glob"`

                  - `beta_managed_agents_grep_tool_config: object { enabled, name, permission_policy, type }`

                    Configuration for the grep tool.

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object { type }`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object { type }`

                        Tool calls require user confirmation before execution.

                    - `type: "grep"`

                  - `beta_managed_agents_web_fetch_tool_config: object { enabled, name, permission_policy, 4 more }`

                    Configuration for the web_fetch tool.

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object { type }`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object { type }`

                        Tool calls require user confirmation before execution.

                    - `type: "web_fetch"`

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `max_content_tokens: optional number`

                  - `beta_managed_agents_web_search_tool_config: object { enabled, name, permission_policy, 4 more }`

                    Configuration for the web_search tool.

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object { type }`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object { type }`

                        Tool calls require user confirmation before execution.

                    - `type: "web_search"`

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `user_location: optional object { type, city, country, 2 more }`

                      Approximate user location for search result localization.

                      - `type: "approximate"`

                        Location precision. Only "approximate" is supported.

                      - `city: optional string`

                        City name.

                      - `country: optional string`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: optional string`

                        Region or state name.

                      - `timezone: optional string`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                - `default_config: object { enabled, permission_policy }`

                  Resolved default configuration for agent tools.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object { type }`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object { type }`

                      Tool calls require user confirmation before execution.

                - `type: "agent_toolset_20260401"`

                  - `"agent_toolset_20260401"`

              - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

                - `configs: array of BetaManagedAgentsMCPToolConfig`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object { type }`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object { type }`

                      Tool calls require user confirmation before execution.

                - `default_config: object { enabled, permission_policy }`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object { type }`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object { type }`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: string`

                - `type: "mcp_toolset"`

                  - `"mcp_toolset"`

              - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

                A custom tool as returned in API responses.

                - `description: string`

                - `input_schema: object { type, properties, required }`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties: optional map[unknown]`

                  - `required: optional array of string`

                - `name: string`

                - `type: "custom"`

                  - `"custom"`

            - `type: "agent"`

              - `"agent"`

            - `version: number`

          - `beta_managed_agents_advisor: object { model, type }`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: string`

              The advisor model id.

            - `type: "advisor"`

              - `"advisor"`

        - `type: "coordinator"`

          - `"coordinator"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `beta_managed_agents_anthropic_skill: object { skill_id, type, version }`

          A resolved Anthropic-managed skill.

        - `beta_managed_agents_custom_skill: object { skill_id, type, version }`

          A resolved user-created custom skill.

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `beta_managed_agents_agent_toolset20260401: object { configs, default_config, type }`

        - `beta_managed_agents_mcp_toolset: object { configs, default_config, mcp_server_name, type }`

        - `beta_managed_agents_custom_tool: object { description, input_schema, name, type }`

          A custom tool as returned in API responses.

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `budget: optional object { max_list_cost, type }`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: object { amount, currency }`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: "USD"`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

          - `"USD"`

      - `type: "limit"`

        - `"limit"`

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string`

      The session's new title. Present only when the update changed it.

  - `beta_managed_agents_start_event: object { event, type }`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsAgentMessagePreview or BetaManagedAgentsAgentThinkingPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `beta_managed_agents_agent_message_preview: object { id, type }`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: "agent.message"`

          - `"agent.message"`

      - `beta_managed_agents_agent_thinking_preview: object { id, type }`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: "agent.thinking"`

          - `"agent.thinking"`

    - `type: "event_start"`

      - `"event_start"`

  - `beta_managed_agents_delta_event: object { delta, event_id, type }`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: object { content, type, index }`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

      - `type: "content_delta"`

        - `"content_delta"`

      - `index: optional number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: "event_delta"`

      - `"event_delta"`

  - `beta_managed_agents_system_message_event: object { id, content, type, processed_at }`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `type: "system.message"`

      - `"system.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

  - `beta_managed_agents_session_usage_event: object { id, processed_at, type, 2 more }`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

    - `type: "session.usage"`

      - `"session.usage"`

    - `usage: object { active_seconds, cache_creation, cache_read_input_tokens, 4 more }`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

      - `cache_creation: optional object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: optional number`

          Tokens used to create 1-hour ephemeral cache entries.

        - `ephemeral_5m_input_tokens: optional number`

          Tokens used to create 5-minute ephemeral cache entries.

      - `cache_read_input_tokens: optional number`

        Total tokens read from prompt cache.

      - `input_tokens: optional number`

        Total input tokens consumed across all turns.

      - `list_cost: optional object { amount, currency }`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: "USD"`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `output_tokens: optional number`

        Total output tokens generated across all turns.

      - `server_tool_use: optional object { web_fetch_requests, web_search_requests }`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: optional number`

          Number of server-executed web fetch requests.

        - `web_search_requests: optional number`

          Number of server-executed web search requests.

    - `budget: optional object { max_list_cost, type }`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: object { amount, currency }`

        A monetary amount in a specific currency.

      - `type: "limit"`

### Example

```cli
ant beta:sessions:threads:events stream \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --thread-id sthr_011CZkZVWa6oIjw0rgXZpnBt
```

#### Response

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```
