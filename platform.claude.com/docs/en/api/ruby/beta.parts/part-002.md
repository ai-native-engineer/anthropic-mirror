<!-- source: https://platform.claude.com/docs/en/api/ruby/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/ruby/beta -->

<!-- chunk-start -->

    - `type: :"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that started running.

    - `type: :"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: :"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that terminated.

    - `type: :"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: String`

      Unique identifier for this event.

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that is retrying.

    - `type: :"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.updated"`

    - `agent: BetaManagedAgentsSessionAgent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: String`

      - `description: String`

      - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

        - `name: String`

        - `type: :url`

        - `url: String`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `:"claude-sonnet-5"`

              High-performance model for coding and agents

            - `:"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `:"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `:"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `:"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `:"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `:"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `String = String`

        - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow`

            Low effort. Favors latency over reasoning depth.

            - `type: :low`

          - `class BetaManagedAgentsEffortMedium`

            Medium effort. Balances latency and reasoning depth.

            - `type: :medium`

          - `class BetaManagedAgentsEffortHigh`

            High effort. Favors reasoning depth.

            - `type: :high`

          - `class BetaManagedAgentsEffortXhigh`

            Extra-high effort. Not all models accept this level.

            - `type: :xhigh`

          - `class BetaManagedAgentsEffortMax`

            Maximum effort. Favors reasoning depth over latency.

            - `type: :max`

        - `inference_geo: String`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: :standard | :fast`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `:standard`

          - `:fast`

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: Array[BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: String`

            - `description: String`

            - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

              - `name: String`

              - `type: :url`

              - `url: String`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: String`

            - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

              - `class BetaManagedAgentsAnthropicSkill`

                A resolved Anthropic-managed skill.

                - `skill_id: String`

                - `type: :anthropic`

                - `version: String`

              - `class BetaManagedAgentsCustomSkill`

                A resolved user-created custom skill.

                - `skill_id: String`

                - `type: :custom`

                - `version: String`

            - `system_: String`

            - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

              - `class BetaManagedAgentsAgentToolset20260401`

                - `configs: Array[BetaManagedAgentsAgentToolConfig]`

                  - `class BetaManagedAgentsBashToolConfig`

                    Configuration for the bash tool.

                    - `enabled: bool`

                    - `name: :bash`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                        - `type: :always_allow`

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                        - `type: :always_ask`

                    - `type: :bash`

                  - `class BetaManagedAgentsEditToolConfig`

                    Configuration for the edit tool.

                    - `enabled: bool`

                    - `name: :edit`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :edit`

                  - `class BetaManagedAgentsReadToolConfig`

                    Configuration for the read tool.

                    - `enabled: bool`

                    - `name: :read`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :read`

                  - `class BetaManagedAgentsWriteToolConfig`

                    Configuration for the write tool.

                    - `enabled: bool`

                    - `name: :write`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :write`

                  - `class BetaManagedAgentsGlobToolConfig`

                    Configuration for the glob tool.

                    - `enabled: bool`

                    - `name: :glob`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :glob`

                  - `class BetaManagedAgentsGrepToolConfig`

                    Configuration for the grep tool.

                    - `enabled: bool`

                    - `name: :grep`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :grep`

                  - `class BetaManagedAgentsWebFetchToolConfig`

                    Configuration for the web_fetch tool.

                    - `enabled: bool`

                    - `name: :web_fetch`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :web_fetch`

                    - `allowed_domains: Array[String]`

                    - `blocked_domains: Array[String]`

                    - `max_content_tokens: Integer`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig`

                    Configuration for the web_search tool.

                    - `enabled: bool`

                    - `name: :web_search`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :web_search`

                    - `allowed_domains: Array[String]`

                    - `blocked_domains: Array[String]`

                    - `user_location: BetaManagedAgentsUserLocation`

                      Approximate user location for search result localization.

                      - `type: :approximate`

                        Location precision. Only "approximate" is supported.

                      - `city: String`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country: String`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: String`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone: String`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: bool`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `type: :agent_toolset_20260401`

              - `class BetaManagedAgentsMCPToolset`

                - `configs: Array[BetaManagedAgentsMCPToolConfig]`

                  - `enabled: bool`

                  - `name: String`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: bool`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: String`

                - `type: :mcp_toolset`

              - `class BetaManagedAgentsCustomTool`

                A custom tool as returned in API responses.

                - `description: String`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: :object`

                  - `properties: Hash[Symbol, untyped]`

                  - `required: Array[String]`

                - `name: String`

                - `type: :custom`

            - `type: :agent`

            - `version: Integer`

              format: int32

          - `class BetaManagedAgentsAdvisor`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: String`

              The advisor model id.

            - `type: :advisor`

        - `type: :coordinator`

      - `name: String`

      - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

        - `class BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

      - `system_: String`

      - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

        - `class BetaManagedAgentsAgentToolset20260401`

        - `class BetaManagedAgentsMCPToolset`

        - `class BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

      - `type: :agent`

      - `version: Integer`

        format: int32

    - `budget: BetaManagedAgentsBudgetLimit`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: String`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: :limit`

    - `metadata: Hash[Symbol, String]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: String`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview`

        - `id: String`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: :"agent.message"`

      - `class BetaManagedAgentsAgentThinkingPreview`

        - `id: String`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: :"agent.thinking"`

    - `type: :event_start`

  - `class BetaManagedAgentsDeltaEvent`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: :content_delta`

      - `index: Integer`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: String`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: :event_delta`

  - `class BetaManagedAgentsSystemMessageEvent`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: String`

        The text content.

        minLength: 1

      - `type: :text`

    - `type: :"system.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.usage"`

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: Float`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: BetaManagedAgentsCacheCreationUsage`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: Integer`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: Integer`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: Integer`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: Integer`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

      - `output_tokens: Integer`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: BetaManagedAgentsServerToolUsage`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: Integer`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: Integer`

          Number of server-executed web search requests.

          format: int32

    - `budget: BetaManagedAgentsBudgetLimit`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `BetaManagedAgentsStreamSessionEvents = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 34 more`

  Server-sent event in the session stream.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_stream_session_events = anthropic.beta.sessions.events.stream("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(beta_managed_agents_stream_session_events)
```

##### Response (200)

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

## Beta › Sessions › Resources

### Add Session Resource

`beta.sessions.resources.add(session_id, **kwargs) -> BetaManagedAgentsFileResource`

**POST** `/v1/sessions/{session_id}/resources`

Add Session Resource

#### Parameters

- `session_id: String`

- `file_id: String`

  ID of a previously uploaded file.

  minLength: 1, maxLength: 128

- `type: :file`

- `mount_path: String`

  Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  minLength: 1, maxLength: 4096

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsFileResource`

  - `id: String`

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `file_id: String`

  - `mount_path: String`

  - `type: :file`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_file_resource = anthropic.beta.sessions.resources.add(
  "sesn_011CZkZAtmR3yMPDzynEDxu7",
  file_id: "file_011CNha8iCJcU1wXNR6q4V8w",
  type: :file
)

puts(beta_managed_agents_file_resource)
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "created_at": "2026-03-15T10:00:00Z",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "mount_path": "/uploads/receipt.pdf",
  "type": "file",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

### List Session Resources

`beta.sessions.resources.list(session_id, **kwargs) -> PageCursor<BetaManagedAgentsSessionResource>`

**GET** `/v1/sessions/{session_id}/resources`

List Session Resources

#### Parameters

- `session_id: String`

- `limit: Integer`

  Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

  format: int32

- `page: String`

  Opaque cursor from a previous response's next_page field.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `BetaManagedAgentsSessionResource = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource | BetaManagedAgentsMemoryStoreResource`

  A memory store attached to an agent session.

  - `class BetaManagedAgentsGitHubRepositoryResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: String`

    - `type: :github_repository`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: String`

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: :branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: :commit`

  - `class BetaManagedAgentsFileResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: String`

    - `mount_path: String`

    - `type: :file`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource`

    A memory store attached to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `description: String`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: String`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: String`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.sessions.resources.list("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Session Resource

`beta.sessions.resources.retrieve(resource_id, **kwargs) -> ResourceRetrieveResponse`

**GET** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

#### Parameters

- `session_id: String`

- `resource_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `ResourceRetrieveResponse = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource | BetaManagedAgentsMemoryStoreResource`

  The requested session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: String`

    - `type: :github_repository`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: String`

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: :branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: :commit`

  - `class BetaManagedAgentsFileResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: String`

    - `mount_path: String`

    - `type: :file`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource`

    A memory store attached to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `description: String`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: String`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: String`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

resource = anthropic.beta.sessions.resources.retrieve(
  "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
)

puts(resource)
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

### Update Session Resource

`beta.sessions.resources.update(resource_id, **kwargs) -> ResourceUpdateResponse`

**POST** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

#### Parameters

- `session_id: String`

- `resource_id: String`

- `authorization_token: String`

  New authorization token for the resource. Currently only `github_repository` resources support token rotation.

  minLength: 1, maxLength: 4096

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `ResourceUpdateResponse = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource | BetaManagedAgentsMemoryStoreResource`

  The updated session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: String`

    - `type: :github_repository`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: String`

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: :branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: :commit`

  - `class BetaManagedAgentsFileResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: String`

    - `mount_path: String`

    - `type: :file`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource`

    A memory store attached to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `description: String`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: String`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: String`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

resource = anthropic.beta.sessions.resources.update(
  "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7",
  authorization_token: "ghp_exampletoken"
)

puts(resource)
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

### Delete Session Resource

`beta.sessions.resources.delete(resource_id, **kwargs) -> BetaManagedAgentsDeleteSessionResource`

**DELETE** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

#### Parameters

- `session_id: String`

- `resource_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeleteSessionResource`

  Confirmation of resource deletion.

  - `id: String`

  - `type: :session_resource_deleted`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_delete_session_resource = anthropic.beta.sessions.resources.delete(
  "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
)

puts(beta_managed_agents_delete_session_resource)
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

## Beta › Sessions › Threads

### List Session Threads

`beta.sessions.threads.list(session_id, **kwargs) -> PageCursor<BetaManagedAgentsSessionThread>`

**GET** `/v1/sessions/{session_id}/threads`

List Session Threads

#### Parameters

- `session_id: String`

- `limit: Integer`

  Maximum results per page. Defaults to 1000.

  format: int32

- `page: String`

  Opaque pagination cursor from a previous response's next_page. Forward-only.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsSessionThread`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: String`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor`

    A session-resolved multiagent roster entry.

    - `class BetaManagedAgentsSessionThreadAgent`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `id: String`

      - `description: String`

      - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

        - `name: String`

        - `type: :url`

        - `url: String`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `:"claude-sonnet-5"`

              High-performance model for coding and agents

            - `:"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `:"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `:"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `:"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `:"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `:"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `String = String`

        - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow`

            Low effort. Favors latency over reasoning depth.

            - `type: :low`

          - `class BetaManagedAgentsEffortMedium`

            Medium effort. Balances latency and reasoning depth.

            - `type: :medium`

          - `class BetaManagedAgentsEffortHigh`

            High effort. Favors reasoning depth.

            - `type: :high`

          - `class BetaManagedAgentsEffortXhigh`

            Extra-high effort. Not all models accept this level.

            - `type: :xhigh`

          - `class BetaManagedAgentsEffortMax`

            Maximum effort. Favors reasoning depth over latency.

            - `type: :max`

        - `inference_geo: String`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: :standard | :fast`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `:standard`

          - `:fast`

      - `name: String`

      - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

        - `class BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

          - `skill_id: String`

          - `type: :anthropic`

          - `version: String`

        - `class BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

          - `skill_id: String`

          - `type: :custom`

          - `version: String`

      - `system_: String`

      - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

        - `class BetaManagedAgentsAgentToolset20260401`

          - `configs: Array[BetaManagedAgentsAgentToolConfig]`

            - `class BetaManagedAgentsBashToolConfig`

              Configuration for the bash tool.

              - `enabled: bool`

              - `name: :bash`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                  - `type: :always_allow`

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

                  - `type: :always_ask`

              - `type: :bash`

            - `class BetaManagedAgentsEditToolConfig`

              Configuration for the edit tool.

              - `enabled: bool`

              - `name: :edit`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :edit`

            - `class BetaManagedAgentsReadToolConfig`

              Configuration for the read tool.

              - `enabled: bool`

              - `name: :read`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :read`

            - `class BetaManagedAgentsWriteToolConfig`

              Configuration for the write tool.

              - `enabled: bool`

              - `name: :write`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :write`

            - `class BetaManagedAgentsGlobToolConfig`

              Configuration for the glob tool.

              - `enabled: bool`

              - `name: :glob`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :glob`

            - `class BetaManagedAgentsGrepToolConfig`

              Configuration for the grep tool.

              - `enabled: bool`

              - `name: :grep`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :grep`

            - `class BetaManagedAgentsWebFetchToolConfig`

              Configuration for the web_fetch tool.

              - `enabled: bool`

              - `name: :web_fetch`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :web_fetch`

              - `allowed_domains: Array[String]`

              - `blocked_domains: Array[String]`

              - `max_content_tokens: Integer`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig`

              Configuration for the web_search tool.

              - `enabled: bool`

              - `name: :web_search`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :web_search`

              - `allowed_domains: Array[String]`

              - `blocked_domains: Array[String]`

              - `user_location: BetaManagedAgentsUserLocation`

                Approximate user location for search result localization.

                - `type: :approximate`

                  Location precision. Only "approximate" is supported.

                - `city: String`

                  City name.

                  minLength: 1, maxLength: 255

                - `country: String`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `region: String`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `timezone: String`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

            Resolved default configuration for agent tools.

            - `enabled: bool`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `type: :agent_toolset_20260401`

        - `class BetaManagedAgentsMCPToolset`

          - `configs: Array[BetaManagedAgentsMCPToolConfig]`

            - `enabled: bool`

            - `name: String`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: bool`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `mcp_server_name: String`

          - `type: :mcp_toolset`

        - `class BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

          - `description: String`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: :object`

            - `properties: Hash[Symbol, untyped]`

            - `required: Array[String]`

          - `name: String`

          - `type: :custom`

      - `type: :agent`

      - `version: Integer`

        format: int32

    - `class BetaManagedAgentsAdvisor`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: String`

        The advisor model id.

      - `type: :advisor`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `parent_thread_id: String`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: String`

    The session this thread belongs to.

  - `stats: BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `active_seconds: Float`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds: Float`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds: Float`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `:running`

    - `:idle`

    - `:rescheduling`

    - `:terminated`

  - `type: :session_thread`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds: Float`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Integer`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: Integer`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Integer`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: String`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: Integer`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: BetaManagedAgentsServerToolUsage`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Integer`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: Integer`

        Number of server-executed web search requests.

        format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.sessions.threads.list("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "description": "A focused research subagent.",
        "mcp_servers": [
          {
            "name": "example-mcp",
            "type": "url",
            "url": "https://example-server.modelcontextprotocol.io/sse"
          }
        ],
        "model": {
          "id": "claude-opus-5",
          "effort": {
            "type": "low"
          },
          "inference_geo": "inference_geo",
          "speed": "standard"
        },
        "name": "Researcher",
        "skills": [
          {
            "skill_id": "xlsx",
            "type": "anthropic",
            "version": "1"
          }
        ],
        "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
        "tools": [
          {
            "configs": [
              {
                "enabled": true,
                "name": "bash",
                "permission_policy": {
                  "type": "always_allow"
                },
                "type": "bash"
              }
            ],
            "default_config": {
              "enabled": true,
              "permission_policy": {
                "type": "always_ask"
              }
            },
            "type": "agent_toolset_20260401"
          }
        ],
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "parent_thread_id": null,
      "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
      "stats": {
        "active_seconds": 0,
        "duration_seconds": 0,
        "startup_seconds": 0
      },
      "status": "idle",
      "type": "session_thread",
      "updated_at": "2026-03-15T10:00:00Z",
      "usage": {
        "active_seconds": 0,
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "list_cost": {
          "amount": "2500",
          "currency": "USD"
        },
        "output_tokens": 0,
        "server_tool_use": {
          "web_fetch_requests": 0,
          "web_search_requests": 3
        }
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Session Thread

`beta.sessions.threads.retrieve(thread_id, **kwargs) -> BetaManagedAgentsSessionThread`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

#### Parameters

- `session_id: String`

- `thread_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsSessionThread`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: String`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor`

    A session-resolved multiagent roster entry.

    - `class BetaManagedAgentsSessionThreadAgent`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `id: String`

      - `description: String`

      - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

        - `name: String`

        - `type: :url`

        - `url: String`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `:"claude-sonnet-5"`

              High-performance model for coding and agents

            - `:"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `:"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `:"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `:"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `:"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `:"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `String = String`

        - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow`

            Low effort. Favors latency over reasoning depth.

            - `type: :low`

          - `class BetaManagedAgentsEffortMedium`

            Medium effort. Balances latency and reasoning depth.

            - `type: :medium`

          - `class BetaManagedAgentsEffortHigh`

            High effort. Favors reasoning depth.

            - `type: :high`

          - `class BetaManagedAgentsEffortXhigh`

            Extra-high effort. Not all models accept this level.

            - `type: :xhigh`

          - `class BetaManagedAgentsEffortMax`

            Maximum effort. Favors reasoning depth over latency.

            - `type: :max`

        - `inference_geo: String`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: :standard | :fast`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `:standard`

          - `:fast`

      - `name: String`

      - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

        - `class BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

          - `skill_id: String`

          - `type: :anthropic`

          - `version: String`

        - `class BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

          - `skill_id: String`

          - `type: :custom`

          - `version: String`

      - `system_: String`

      - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

        - `class BetaManagedAgentsAgentToolset20260401`

          - `configs: Array[BetaManagedAgentsAgentToolConfig]`

            - `class BetaManagedAgentsBashToolConfig`

              Configuration for the bash tool.

              - `enabled: bool`

              - `name: :bash`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                  - `type: :always_allow`

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

                  - `type: :always_ask`

              - `type: :bash`

            - `class BetaManagedAgentsEditToolConfig`

              Configuration for the edit tool.

              - `enabled: bool`

              - `name: :edit`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :edit`

            - `class BetaManagedAgentsReadToolConfig`

              Configuration for the read tool.

              - `enabled: bool`

              - `name: :read`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :read`

            - `class BetaManagedAgentsWriteToolConfig`

              Configuration for the write tool.

              - `enabled: bool`

              - `name: :write`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :write`

            - `class BetaManagedAgentsGlobToolConfig`

              Configuration for the glob tool.

              - `enabled: bool`

              - `name: :glob`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :glob`

            - `class BetaManagedAgentsGrepToolConfig`

              Configuration for the grep tool.

              - `enabled: bool`

              - `name: :grep`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :grep`

            - `class BetaManagedAgentsWebFetchToolConfig`

              Configuration for the web_fetch tool.

              - `enabled: bool`

              - `name: :web_fetch`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :web_fetch`

              - `allowed_domains: Array[String]`

              - `blocked_domains: Array[String]`

              - `max_content_tokens: Integer`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig`

              Configuration for the web_search tool.

              - `enabled: bool`

              - `name: :web_search`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :web_search`

              - `allowed_domains: Array[String]`

              - `blocked_domains: Array[String]`

              - `user_location: BetaManagedAgentsUserLocation`

                Approximate user location for search result localization.

                - `type: :approximate`

                  Location precision. Only "approximate" is supported.

                - `city: String`

                  City name.

                  minLength: 1, maxLength: 255

                - `country: String`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `region: String`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `timezone: String`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

            Resolved default configuration for agent tools.

            - `enabled: bool`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `type: :agent_toolset_20260401`

        - `class BetaManagedAgentsMCPToolset`

          - `configs: Array[BetaManagedAgentsMCPToolConfig]`

            - `enabled: bool`

            - `name: String`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: bool`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `mcp_server_name: String`

          - `type: :mcp_toolset`

        - `class BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

          - `description: String`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: :object`

            - `properties: Hash[Symbol, untyped]`

            - `required: Array[String]`

          - `name: String`

          - `type: :custom`

      - `type: :agent`

      - `version: Integer`

        format: int32

    - `class BetaManagedAgentsAdvisor`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: String`

        The advisor model id.

      - `type: :advisor`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `parent_thread_id: String`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: String`

    The session this thread belongs to.

  - `stats: BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `active_seconds: Float`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds: Float`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds: Float`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `:running`

    - `:idle`

    - `:rescheduling`

    - `:terminated`

  - `type: :session_thread`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds: Float`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Integer`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: Integer`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Integer`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: String`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: Integer`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: BetaManagedAgentsServerToolUsage`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Integer`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: Integer`

        Number of server-executed web search requests.

        format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_session_thread = anthropic.beta.sessions.threads.retrieve(
  "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
)

puts(beta_managed_agents_session_thread)
```

##### Response (200)

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  }
}
```

### Archive Session Thread

`beta.sessions.threads.archive(thread_id, **kwargs) -> BetaManagedAgentsSessionThread`

**POST** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

#### Parameters

- `session_id: String`

- `thread_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsSessionThread`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: String`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor`

    A session-resolved multiagent roster entry.

    - `class BetaManagedAgentsSessionThreadAgent`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `id: String`

      - `description: String`

      - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

        - `name: String`

        - `type: :url`

        - `url: String`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `:"claude-sonnet-5"`

              High-performance model for coding and agents

            - `:"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `:"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `:"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `:"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `:"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `:"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `String = String`

        - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow`

            Low effort. Favors latency over reasoning depth.

            - `type: :low`

          - `class BetaManagedAgentsEffortMedium`

            Medium effort. Balances latency and reasoning depth.

            - `type: :medium`

          - `class BetaManagedAgentsEffortHigh`

            High effort. Favors reasoning depth.

            - `type: :high`

          - `class BetaManagedAgentsEffortXhigh`

            Extra-high effort. Not all models accept this level.

            - `type: :xhigh`

          - `class BetaManagedAgentsEffortMax`

            Maximum effort. Favors reasoning depth over latency.

            - `type: :max`

        - `inference_geo: String`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: :standard | :fast`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `:standard`

          - `:fast`

      - `name: String`

      - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

        - `class BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

          - `skill_id: String`

          - `type: :anthropic`

          - `version: String`

        - `class BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

          - `skill_id: String`

          - `type: :custom`

          - `version: String`

      - `system_: String`

      - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

        - `class BetaManagedAgentsAgentToolset20260401`

          - `configs: Array[BetaManagedAgentsAgentToolConfig]`

            - `class BetaManagedAgentsBashToolConfig`

              Configuration for the bash tool.

              - `enabled: bool`

              - `name: :bash`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                  - `type: :always_allow`

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

                  - `type: :always_ask`

              - `type: :bash`

            - `class BetaManagedAgentsEditToolConfig`

              Configuration for the edit tool.

              - `enabled: bool`

              - `name: :edit`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :edit`

            - `class BetaManagedAgentsReadToolConfig`

              Configuration for the read tool.

              - `enabled: bool`

              - `name: :read`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :read`

            - `class BetaManagedAgentsWriteToolConfig`

              Configuration for the write tool.

              - `enabled: bool`

              - `name: :write`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :write`

            - `class BetaManagedAgentsGlobToolConfig`

              Configuration for the glob tool.

              - `enabled: bool`

              - `name: :glob`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :glob`

            - `class BetaManagedAgentsGrepToolConfig`

              Configuration for the grep tool.

              - `enabled: bool`

              - `name: :grep`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :grep`

            - `class BetaManagedAgentsWebFetchToolConfig`

              Configuration for the web_fetch tool.

              - `enabled: bool`

              - `name: :web_fetch`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :web_fetch`

              - `allowed_domains: Array[String]`

              - `blocked_domains: Array[String]`

              - `max_content_tokens: Integer`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig`

              Configuration for the web_search tool.

              - `enabled: bool`

              - `name: :web_search`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy`

                  Tool calls require user confirmation before execution.

              - `type: :web_search`

              - `allowed_domains: Array[String]`

              - `blocked_domains: Array[String]`

              - `user_location: BetaManagedAgentsUserLocation`

                Approximate user location for search result localization.

                - `type: :approximate`

                  Location precision. Only "approximate" is supported.

                - `city: String`

                  City name.

                  minLength: 1, maxLength: 255

                - `country: String`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `region: String`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `timezone: String`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

            Resolved default configuration for agent tools.

            - `enabled: bool`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `type: :agent_toolset_20260401`

        - `class BetaManagedAgentsMCPToolset`

          - `configs: Array[BetaManagedAgentsMCPToolConfig]`

            - `enabled: bool`

            - `name: String`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: bool`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

          - `mcp_server_name: String`

          - `type: :mcp_toolset`

        - `class BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

          - `description: String`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: :object`

            - `properties: Hash[Symbol, untyped]`

            - `required: Array[String]`

          - `name: String`

          - `type: :custom`

      - `type: :agent`

      - `version: Integer`

        format: int32

    - `class BetaManagedAgentsAdvisor`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: String`

        The advisor model id.

      - `type: :advisor`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `parent_thread_id: String`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: String`

    The session this thread belongs to.

  - `stats: BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `active_seconds: Float`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds: Float`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds: Float`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `:running`

    - `:idle`

    - `:rescheduling`

    - `:terminated`

  - `type: :session_thread`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds: Float`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Integer`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: Integer`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Integer`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: String`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: Integer`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: BetaManagedAgentsServerToolUsage`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Integer`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: Integer`

        Number of server-executed web search requests.

        format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_session_thread = anthropic.beta.sessions.threads.archive(
  "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
)

puts(beta_managed_agents_session_thread)
```

##### Response (200)

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  }
}
```

## Beta › Sessions › Threads › Events

### List Session Thread Events

`beta.sessions.threads.events.list(thread_id, **kwargs) -> PageCursor<BetaManagedAgentsSessionEvent>`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

#### Parameters

- `session_id: String`

- `thread_id: String`

- `limit: Integer`

  Query parameter for limit

  format: int32

- `page: String`

  Query parameter for page

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `BetaManagedAgentsSessionEvent = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 32 more`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

          minLength: 1

        - `type: :text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

              minLength: 1

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: :base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

            - `url: String`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

              minLength: 1

            - `type: :file`

        - `type: :image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

              minLength: 1

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: :base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

              minLength: 1

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: :text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

            - `url: String`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

              minLength: 1

            - `type: :file`

        - `type: :document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: :redacted`

    - `type: :"user.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: String`

      Unique identifier for this event.

    - `type: :"user.interrupt"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: String`

      Unique identifier for this event.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: String`

      Unique identifier for this event.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: Array[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: String`

            The text content.

            minLength: 1

          - `type: :text`

        - `source: String`

          The URL source of the search result.

          minLength: 1

        - `title: String`

          The title of the search result.

          minLength: 1

        - `type: :search_result`

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the custom tool being called.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.custom_tool_use"`

    - `session_thread_id: String`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsRedactedBlock]`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `mcp_server_name: String`

      Name of the MCP server providing the tool.

    - `name: String`

      Name of the MCP tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.mcp_tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

    - `session_thread_id: String`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: String`

      Unique identifier for this event.

    - `mcp_tool_use_id: String`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.mcp_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the agent tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

    - `session_thread_id: String`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: :"agent.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: String`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.thread_message_received"`

    - `from_agent_name: String`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: String`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: :"agent.thread_message_sent"`

    - `to_agent_name: String`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: String`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

        - `type: :unknown_error`

      - `class BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :model_overloaded_error`

      - `class BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :model_rate_limited_error`

      - `class BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :model_request_failed_error`

      - `class BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: String`

          Name of the MCP server that failed to connect.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :mcp_connection_failed_error`

      - `class BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: String`

          Name of the MCP server that failed authentication.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :mcp_authentication_failed_error`

      - `class BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :billing_error`

      - `class BetaManagedAgentsCredentialHostUnreachableError`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: String`

          ID of the affected credential.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :credential_host_unreachable_error`

        - `vault_id: String`

          ID of the vault containing the affected credential.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: :end_turn`

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array[String]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: :requires_action`

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: :retries_exhausted`

      - `class BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: :budget_reached`

    - `type: :"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the callable agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public `sthr_` ID of the newly created thread.

    - `type: :"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent`

    Emitted when an outcome evaluation cycle begins.

    - `id: String`

      Unique identifier for this event.

    - `iteration: Integer`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: String`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: String`

      Unique identifier for this event.

    - `explanation: String`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: Integer`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: String`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: String`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: String`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: :"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: Integer`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: Integer`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: Integer`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: Integer`

        Output tokens generated by this request.

        format: int32

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

  - `class BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: String`

      Unique identifier for this event.

    - `is_error: bool`

      Whether the model request resulted in an error.

    - `model_request_start_id: String`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: String`

      Unique identifier for this event.

    - `iteration: Integer`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: String`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: String`

      Unique identifier for this event.

    - `description: String`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Integer`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: String`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: String`

          ID of the rubric file.

        - `type: :file`

      - `class BetaManagedAgentsTextRubric`

        Rubric content provided inline as text.

        - `content: String`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: :text`

    - `type: :"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that started running.

    - `type: :"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: :"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that terminated.

    - `type: :"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: String`

      Unique identifier for this event.

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that is retrying.

    - `type: :"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.updated"`

    - `agent: BetaManagedAgentsSessionAgent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: String`

      - `description: String`

      - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

        - `name: String`

        - `type: :url`

        - `url: String`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `:"claude-sonnet-5"`

              High-performance model for coding and agents

            - `:"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `:"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `:"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `:"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `:"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `:"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `String = String`

        - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow`

            Low effort. Favors latency over reasoning depth.

            - `type: :low`

          - `class BetaManagedAgentsEffortMedium`

            Medium effort. Balances latency and reasoning depth.

            - `type: :medium`

          - `class BetaManagedAgentsEffortHigh`

            High effort. Favors reasoning depth.

            - `type: :high`

          - `class BetaManagedAgentsEffortXhigh`

            Extra-high effort. Not all models accept this level.

            - `type: :xhigh`

          - `class BetaManagedAgentsEffortMax`

            Maximum effort. Favors reasoning depth over latency.

            - `type: :max`

        - `inference_geo: String`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: :standard | :fast`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `:standard`

          - `:fast`

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: Array[BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: String`

            - `description: String`

            - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

              - `name: String`

              - `type: :url`

              - `url: String`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: String`

            - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

              - `class BetaManagedAgentsAnthropicSkill`

                A resolved Anthropic-managed skill.

                - `skill_id: String`

                - `type: :anthropic`

                - `version: String`

              - `class BetaManagedAgentsCustomSkill`

                A resolved user-created custom skill.

                - `skill_id: String`

                - `type: :custom`

                - `version: String`

            - `system_: String`

            - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

              - `class BetaManagedAgentsAgentToolset20260401`

                - `configs: Array[BetaManagedAgentsAgentToolConfig]`

                  - `class BetaManagedAgentsBashToolConfig`

                    Configuration for the bash tool.

                    - `enabled: bool`

                    - `name: :bash`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                        - `type: :always_allow`

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                        - `type: :always_ask`

                    - `type: :bash`

                  - `class BetaManagedAgentsEditToolConfig`

                    Configuration for the edit tool.

                    - `enabled: bool`

                    - `name: :edit`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :edit`

                  - `class BetaManagedAgentsReadToolConfig`

                    Configuration for the read tool.

                    - `enabled: bool`

                    - `name: :read`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :read`

                  - `class BetaManagedAgentsWriteToolConfig`

                    Configuration for the write tool.

                    - `enabled: bool`

                    - `name: :write`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :write`

                  - `class BetaManagedAgentsGlobToolConfig`

                    Configuration for the glob tool.

                    - `enabled: bool`

                    - `name: :glob`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :glob`

                  - `class BetaManagedAgentsGrepToolConfig`

                    Configuration for the grep tool.

                    - `enabled: bool`

                    - `name: :grep`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :grep`

                  - `class BetaManagedAgentsWebFetchToolConfig`

                    Configuration for the web_fetch tool.

                    - `enabled: bool`

                    - `name: :web_fetch`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :web_fetch`

                    - `allowed_domains: Array[String]`

                    - `blocked_domains: Array[String]`

                    - `max_content_tokens: Integer`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig`

                    Configuration for the web_search tool.

                    - `enabled: bool`

                    - `name: :web_search`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :web_search`

                    - `allowed_domains: Array[String]`

                    - `blocked_domains: Array[String]`

                    - `user_location: BetaManagedAgentsUserLocation`

                      Approximate user location for search result localization.

                      - `type: :approximate`

                        Location precision. Only "approximate" is supported.

                      - `city: String`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country: String`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: String`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone: String`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: bool`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `type: :agent_toolset_20260401`

              - `class BetaManagedAgentsMCPToolset`

                - `configs: Array[BetaManagedAgentsMCPToolConfig]`

                  - `enabled: bool`

                  - `name: String`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: bool`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: String`

                - `type: :mcp_toolset`

              - `class BetaManagedAgentsCustomTool`

                A custom tool as returned in API responses.

                - `description: String`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: :object`

                  - `properties: Hash[Symbol, untyped]`

                  - `required: Array[String]`

                - `name: String`

                - `type: :custom`

            - `type: :agent`

            - `version: Integer`

              format: int32

          - `class BetaManagedAgentsAdvisor`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: String`

              The advisor model id.

            - `type: :advisor`

        - `type: :coordinator`

      - `name: String`

      - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

        - `class BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

      - `system_: String`

      - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

        - `class BetaManagedAgentsAgentToolset20260401`

        - `class BetaManagedAgentsMCPToolset`

        - `class BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

      - `type: :agent`

      - `version: Integer`

        format: int32

    - `budget: BetaManagedAgentsBudgetLimit`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: String`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: :limit`

    - `metadata: Hash[Symbol, String]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: String`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: String`

        The text content.

        minLength: 1

      - `type: :text`

    - `type: :"system.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.usage"`

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: Float`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: BetaManagedAgentsCacheCreationUsage`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: Integer`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: Integer`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: Integer`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: Integer`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

      - `output_tokens: Integer`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: BetaManagedAgentsServerToolUsage`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: Integer`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: Integer`

          Number of server-executed web search requests.

          format: int32

    - `budget: BetaManagedAgentsBudgetLimit`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.sessions.threads.events.list(
  "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
)

puts(page)
```

##### Response (200)

```json
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

### Stream Session Thread Events

`beta.sessions.threads.events.stream(thread_id, **kwargs) -> BetaManagedAgentsStreamSessionThreadEvents`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

#### Parameters

- `session_id: String`

- `thread_id: String`

- `event_deltas: Array[BetaManagedAgentsDeltaType]`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

  - `:"agent.message"`

  - `:"agent.thinking"`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `BetaManagedAgentsStreamSessionThreadEvents = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 34 more`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent`

    A user message event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

          minLength: 1

        - `type: :text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

              minLength: 1

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: :base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

            - `url: String`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

              minLength: 1

            - `type: :file`

        - `type: :image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

              minLength: 1

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: :base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

              minLength: 1

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: :text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

            - `url: String`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

              minLength: 1

            - `type: :file`

        - `type: :document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: :redacted`

    - `type: :"user.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: String`

      Unique identifier for this event.

    - `type: :"user.interrupt"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: String`

      Unique identifier for this event.

    - `result: :allow | :deny`

      UserToolConfirmationResult enum

      - `:allow`

      - `:deny`

    - `tool_use_id: String`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_confirmation"`

    - `deny_message: String`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent`

    Event sent by the client providing the result of a custom tool execution.

    - `id: String`

      Unique identifier for this event.

    - `custom_tool_use_id: String`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.custom_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: Array[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `text: String`

            The text content.

            minLength: 1

          - `type: :text`

        - `source: String`

          The URL source of the search result.

          minLength: 1

        - `title: String`

          The title of the search result.

          minLength: 1

        - `type: :search_result`

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the custom tool being called.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.custom_tool_use"`

    - `session_thread_id: String`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent`

    An agent response event in the session conversation.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsRedactedBlock]`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.message"`

  - `class BetaManagedAgentsAgentThinkingEvent`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.thinking"`

  - `class BetaManagedAgentsAgentMCPToolUseEvent`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `mcp_server_name: String`

      Name of the MCP server providing the tool.

    - `name: String`

      Name of the MCP tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.mcp_tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

    - `session_thread_id: String`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent`

    Event representing the result of an MCP tool execution.

    - `id: String`

      Unique identifier for this event.

    - `mcp_tool_use_id: String`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.mcp_tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: String`

      Unique identifier for this event.

    - `input: Hash[Symbol, untyped]`

      Input parameters for the tool call.

    - `name: String`

      Name of the agent tool being used.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.tool_use"`

    - `evaluated_permission: :allow | :ask | :deny`

      AgentEvaluatedPermission enum

      - `:allow`

      - `:ask`

      - `:deny`

    - `session_thread_id: String`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent`

    Event representing the result of an agent tool execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: :"agent.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: String`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.thread_message_received"`

    - `from_agent_name: String`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: String`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: :"agent.thread_message_sent"`

    - `to_agent_name: String`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"agent.thread_context_compacted"`

  - `class BetaManagedAgentsSessionErrorEvent`

    An error event indicating a problem occurred during session execution.

    - `id: String`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: :retrying`

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: :exhausted`

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: :terminal`

        - `type: :unknown_error`

      - `class BetaManagedAgentsModelOverloadedError`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :model_overloaded_error`

      - `class BetaManagedAgentsModelRateLimitedError`

        The model request was rate-limited.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :model_rate_limited_error`

      - `class BetaManagedAgentsModelRequestFailedError`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :model_request_failed_error`

      - `class BetaManagedAgentsMCPConnectionFailedError`

        Failed to connect to an MCP server.

        - `mcp_server_name: String`

          Name of the MCP server that failed to connect.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :mcp_connection_failed_error`

      - `class BetaManagedAgentsMCPAuthenticationFailedError`

        Authentication to an MCP server failed.

        - `mcp_server_name: String`

          Name of the MCP server that failed authentication.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :mcp_authentication_failed_error`

      - `class BetaManagedAgentsBillingError`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :billing_error`

      - `class BetaManagedAgentsCredentialHostUnreachableError`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: String`

          ID of the affected credential.

        - `message: String`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: :credential_host_unreachable_error`

        - `vault_id: String`

          ID of the vault containing the affected credential.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.error"`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.status_rescheduled"`

  - `class BetaManagedAgentsSessionStatusRunningEvent`

    Indicates the session is actively running and the agent is working.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.status_running"`

  - `class BetaManagedAgentsSessionStatusIdleEvent`

    Indicates the agent has paused and is awaiting user input.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: :end_turn`

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: Array[String]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: :requires_action`

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: :retries_exhausted`

      - `class BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: :budget_reached`

    - `type: :"session.status_idle"`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent`

    Indicates the session has terminated, either due to an error or completion.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.status_terminated"`

  - `class BetaManagedAgentsSessionThreadCreatedEvent`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the callable agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public `sthr_` ID of the newly created thread.

    - `type: :"session.thread_created"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent`

    Emitted when an outcome evaluation cycle begins.

    - `id: String`

      Unique identifier for this event.

    - `iteration: Integer`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: String`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"span.outcome_evaluation_start"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: String`

      Unique identifier for this event.

    - `explanation: String`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: Integer`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: String`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: String`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: String`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: :"span.outcome_evaluation_end"`

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: Integer`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: Integer`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: Integer`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: Integer`

        Output tokens generated by this request.

        format: int32

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

  - `class BetaManagedAgentsSpanModelRequestStartEvent`

    Emitted when a model request is initiated by the agent.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"span.model_request_start"`

  - `class BetaManagedAgentsSpanModelRequestEndEvent`

    Emitted when a model request completes.

    - `id: String`

      Unique identifier for this event.

    - `is_error: bool`

      Whether the model request resulted in an error.

    - `model_request_start_id: String`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"span.model_request_end"`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: String`

      Unique identifier for this event.

    - `iteration: Integer`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: String`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"span.outcome_evaluation_ongoing"`

  - `class BetaManagedAgentsUserDefineOutcomeEvent`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: String`

      Unique identifier for this event.

    - `description: String`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Integer`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: String`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: String`

          ID of the rubric file.

        - `type: :file`

      - `class BetaManagedAgentsTextRubric`

        Rubric content provided inline as text.

        - `content: String`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: :text`

    - `type: :"user.define_outcome"`

  - `class BetaManagedAgentsSessionDeletedEvent`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.deleted"`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that started running.

    - `type: :"session.thread_status_running"`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: :"session.thread_status_idle"`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that terminated.

    - `type: :"session.thread_status_terminated"`

  - `class BetaManagedAgentsUserToolResultEvent`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: String`

      Unique identifier for this event.

    - `tool_use_id: String`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: :"user.tool_result"`

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock`

        A block containing a web search result.

    - `is_error: bool`

      Whether the tool execution resulted in an error.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: String`

      Unique identifier for this event.

    - `agent_name: String`

      Name of the agent the thread runs.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: String`

      Public sthr_ ID of the thread that is retrying.

    - `type: :"session.thread_status_rescheduled"`

  - `class BetaManagedAgentsSessionUpdatedEvent`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.updated"`

    - `agent: BetaManagedAgentsSessionAgent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: String`

      - `description: String`

      - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

        - `name: String`

        - `type: :url`

        - `url: String`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `:"claude-sonnet-5"`

              High-performance model for coding and agents

            - `:"claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `:"claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `:"claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `:"claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `:"claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `:"claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `:"claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `String = String`

        - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow`

            Low effort. Favors latency over reasoning depth.

            - `type: :low`

          - `class BetaManagedAgentsEffortMedium`

            Medium effort. Balances latency and reasoning depth.

            - `type: :medium`

          - `class BetaManagedAgentsEffortHigh`

            High effort. Favors reasoning depth.

            - `type: :high`

          - `class BetaManagedAgentsEffortXhigh`

            Extra-high effort. Not all models accept this level.

            - `type: :xhigh`

          - `class BetaManagedAgentsEffortMax`

            Maximum effort. Favors reasoning depth over latency.

            - `type: :max`

        - `inference_geo: String`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: :standard | :fast`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `:standard`

          - `:fast`

      - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: Array[BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: String`

            - `description: String`

            - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

              - `name: String`

              - `type: :url`

              - `url: String`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: String`

            - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

              - `class BetaManagedAgentsAnthropicSkill`

                A resolved Anthropic-managed skill.

                - `skill_id: String`

                - `type: :anthropic`

                - `version: String`

              - `class BetaManagedAgentsCustomSkill`

                A resolved user-created custom skill.

                - `skill_id: String`

                - `type: :custom`

                - `version: String`

            - `system_: String`

            - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

              - `class BetaManagedAgentsAgentToolset20260401`

                - `configs: Array[BetaManagedAgentsAgentToolConfig]`

                  - `class BetaManagedAgentsBashToolConfig`

                    Configuration for the bash tool.

                    - `enabled: bool`

                    - `name: :bash`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                        - `type: :always_allow`

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                        - `type: :always_ask`

                    - `type: :bash`

                  - `class BetaManagedAgentsEditToolConfig`

                    Configuration for the edit tool.

                    - `enabled: bool`

                    - `name: :edit`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :edit`

                  - `class BetaManagedAgentsReadToolConfig`

                    Configuration for the read tool.

                    - `enabled: bool`

                    - `name: :read`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :read`

                  - `class BetaManagedAgentsWriteToolConfig`

                    Configuration for the write tool.

                    - `enabled: bool`

                    - `name: :write`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :write`

                  - `class BetaManagedAgentsGlobToolConfig`

                    Configuration for the glob tool.

                    - `enabled: bool`

                    - `name: :glob`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :glob`

                  - `class BetaManagedAgentsGrepToolConfig`

                    Configuration for the grep tool.

                    - `enabled: bool`

                    - `name: :grep`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :grep`

                  - `class BetaManagedAgentsWebFetchToolConfig`

                    Configuration for the web_fetch tool.

                    - `enabled: bool`

                    - `name: :web_fetch`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :web_fetch`

                    - `allowed_domains: Array[String]`

                    - `blocked_domains: Array[String]`

                    - `max_content_tokens: Integer`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig`

                    Configuration for the web_search tool.

                    - `enabled: bool`

                    - `name: :web_search`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy`

                        Tool calls require user confirmation before execution.

                    - `type: :web_search`

                    - `allowed_domains: Array[String]`

                    - `blocked_domains: Array[String]`

                    - `user_location: BetaManagedAgentsUserLocation`

                      Approximate user location for search result localization.

                      - `type: :approximate`

                        Location precision. Only "approximate" is supported.

                      - `city: String`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country: String`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: String`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone: String`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: bool`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `type: :agent_toolset_20260401`

              - `class BetaManagedAgentsMCPToolset`

                - `configs: Array[BetaManagedAgentsMCPToolConfig]`

                  - `enabled: bool`

                  - `name: String`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: bool`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: String`

                - `type: :mcp_toolset`

              - `class BetaManagedAgentsCustomTool`

                A custom tool as returned in API responses.

                - `description: String`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: :object`

                  - `properties: Hash[Symbol, untyped]`

                  - `required: Array[String]`

                - `name: String`

                - `type: :custom`

            - `type: :agent`

            - `version: Integer`

              format: int32

          - `class BetaManagedAgentsAdvisor`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: String`

              The advisor model id.

            - `type: :advisor`

        - `type: :coordinator`

      - `name: String`

      - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

        - `class BetaManagedAgentsAnthropicSkill`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill`

          A resolved user-created custom skill.

      - `system_: String`

      - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

        - `class BetaManagedAgentsAgentToolset20260401`

        - `class BetaManagedAgentsMCPToolset`

        - `class BetaManagedAgentsCustomTool`

          A custom tool as returned in API responses.

      - `type: :agent`

      - `version: Integer`

        format: int32

    - `budget: BetaManagedAgentsBudgetLimit`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: String`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: :limit`

    - `metadata: Hash[Symbol, String]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: String`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview`

        - `id: String`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: :"agent.message"`

      - `class BetaManagedAgentsAgentThinkingPreview`

        - `id: String`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: :"agent.thinking"`

    - `type: :event_start`

  - `class BetaManagedAgentsDeltaEvent`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: :content_delta`

      - `index: Integer`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: String`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: :event_delta`

  - `class BetaManagedAgentsSystemMessageEvent`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: String`

      Unique identifier for this event.

    - `content: Array[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: String`

        The text content.

        minLength: 1

      - `type: :text`

    - `type: :"system.message"`

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: String`

      Unique identifier for this event.

    - `processed_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: :"session.usage"`

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: Float`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: BetaManagedAgentsCacheCreationUsage`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: Integer`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: Integer`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: Integer`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: Integer`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

      - `output_tokens: Integer`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: BetaManagedAgentsServerToolUsage`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: Integer`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: Integer`

          Number of server-executed web search requests.

          format: int32

    - `budget: BetaManagedAgentsBudgetLimit`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `BetaManagedAgentsStreamSessionThreadEvents = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | 34 more`

  Server-sent event in a single thread's stream.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_stream_session_thread_events = anthropic.beta.sessions.threads.events.stream(
  "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
)

puts(beta_managed_agents_stream_session_thread_events)
```

##### Response (200)

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

## Beta › Deployments

### Create Deployment

`beta.deployments.create(**kwargs) -> BetaManagedAgentsDeployment`

**POST** `/v1/deployments`

Create Deployment

#### Parameters

- `agent: String | BetaManagedAgentsAgentParams`

  Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

  - `String = String`

  - `class BetaManagedAgentsAgentParams`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: String`

      The `agent` ID.

      minLength: 1, maxLength: 128

    - `type: :agent`

    - `version: Integer`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

      format: int32

- `environment_id: String`

  ID of the `environment` defining the container configuration for sessions created from this deployment.

  minLength: 1, maxLength: 128

- `initial_events: Array[BetaManagedAgentsDeploymentInitialEventParams]`

  Events to send to each session immediately after creation. At least 1, maximum 50.

  - `class BetaManagedAgentsUserMessageEventParams`

    Parameters for sending a user message to the session.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

          minLength: 1

        - `type: :text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

              minLength: 1

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: :base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

            - `url: String`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

              minLength: 1

            - `type: :file`

        - `type: :image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

              minLength: 1

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: :base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

              minLength: 1

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: :text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

            - `url: String`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

              minLength: 1

            - `type: :file`

        - `type: :document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: :redacted`

    - `type: :"user.message"`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: String`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams | BetaManagedAgentsTextRubricParams`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: String`

          ID of the rubric file.

        - `type: :file`

      - `class BetaManagedAgentsTextRubricParams`

        Rubric content provided inline as text.

        - `content: String`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

        - `type: :text`

    - `type: :"user.define_outcome"`

    - `max_iterations: Integer`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `class BetaManagedAgentsSystemMessageEventParams`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: Array[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `text: String`

        The text content.

        minLength: 1

      - `type: :text`

    - `type: :"system.message"`

- `name: String`

  Human-readable name for the deployment.

  minLength: 1, maxLength: 256

- `budget: BetaManagedAgentsBudgetLimit`

  A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `max_list_cost: BetaMonetaryAmount`

    A monetary amount in a specific currency.

    - `amount: String`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `type: :limit`

- `description: String`

  Description of what the deployment does.

  maxLength: 2048

- `metadata: Hash[Symbol, String]`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources: Array[BetaManagedAgentsGitHubRepositoryResourceParams | BetaManagedAgentsFileResourceParams | BetaManagedAgentsMemoryStoreResourceParam]`

  Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

  - `class BetaManagedAgentsGitHubRepositoryResourceParams`

    Mount a GitHub repository into the session's container.

    - `authorization_token: String`

      GitHub authorization token used to clone the repository.

      minLength: 1, maxLength: 4096

    - `type: :github_repository`

    - `url: String`

      Github URL of the repository

      minLength: 1, maxLength: 2048

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: :branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: :commit`

    - `mount_path: String`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

      minLength: 1, maxLength: 4096

  - `class BetaManagedAgentsFileResourceParams`

    Mount a file uploaded via the Files API into the session.

    - `file_id: String`

      ID of a previously uploaded file.

      minLength: 1, maxLength: 128

    - `type: :file`

    - `mount_path: String`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

      minLength: 1, maxLength: 4096

  - `class BetaManagedAgentsMemoryStoreResourceParam`

    Parameters for attaching a memory store to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

- `schedule: BetaManagedAgentsScheduleParams`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: String`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `timezone: String`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

    minLength: 1

  - `type: :cron`

- `vault_ids: Array[String]`

  Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: String`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: String`

    - `type: :agent`

    - `version: Integer`

      format: int32

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

    Description of what the deployment does.

  - `environment_id: String`

    ID of the `environment` where sessions run.

  - `initial_events: Array[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

            minLength: 1

          - `type: :text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

                minLength: 1

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

                minLength: 1

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

                minLength: 1

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: :text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: :redacted`

      - `type: :"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: String`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: String`

            ID of the rubric file.

          - `type: :file`

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: String`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: :text`

      - `type: :"user.define_outcome"`

      - `max_iterations: Integer`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: String`

          The text content.

          minLength: 1

        - `type: :text`

      - `type: :"system.message"`

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: String`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: :manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: :environment_archived_error`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: :agent_archived_error`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: :environment_not_found_error`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: :vault_not_found_error`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: :file_not_found_error`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: :session_resource_not_found_error`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: :workspace_archived_error`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: :organization_disabled_error`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: :memory_store_archived_error`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: :skill_not_found_error`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: :vault_archived_error`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: :unknown_error`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: :self_hosted_resources_unsupported_error`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: :mcp_egress_blocked_error`

      - `type: :error`

  - `resources: Array[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: :github_repository`

      - `url: String`

        Github URL of the repository

      - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `name: String`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: :branch`

        - `class BetaManagedAgentsCommitCheckout`

          - `sha: String`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: :commit`

      - `mount_path: String`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: String`

        ID of a previously uploaded file.

      - `type: :file`

      - `mount_path: String`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: String`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: :memory_store`

      - `access: :read_write | :read_only`

        Access mode for an attached memory store.

        - `:read_write`

        - `:read_only`

      - `instructions: String`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: String`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: String`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: :cron`

    - `last_run_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: Array[Time]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `:active`

    - `:paused`

  - `type: :deployment`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: Array[String]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: String`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: :limit`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deployment = anthropic.beta.deployments.create(
  agent: "string",
  environment_id: "x",
  initial_events: [{content: [{text: "Where is my order #1234?", type: :text}], type: :"user.message"}],
  name: "x"
)

puts(beta_managed_agents_deployment)
```

##### Response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

### List Deployments

`beta.deployments.list(**kwargs) -> PageCursor<BetaManagedAgentsDeployment>`

**GET** `/v1/deployments`

List Deployments

#### Parameters

- `agent_id: String`

  Filter by agent ID.

- `created_at_gte: Time`

  Return deployments created at or after this time (inclusive).

  format: date-time

- `created_at_lte: Time`

  Return deployments created at or before this time (inclusive).

  format: date-time

- `include_archived: bool`

  When true, includes archived deployments. Default: false (exclude archived).

- `limit: Integer`

  Maximum results per page. Default 20, maximum 100.

  format: int32

- `page: String`

  Opaque pagination cursor.

- `status: BetaManagedAgentsDeploymentStatus`

  Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

  - `:active`

  - `:paused`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: String`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: String`

    - `type: :agent`

    - `version: Integer`

      format: int32

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

    Description of what the deployment does.

  - `environment_id: String`

    ID of the `environment` where sessions run.

  - `initial_events: Array[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

            minLength: 1

          - `type: :text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

                minLength: 1

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

                minLength: 1

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

                minLength: 1

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: :text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: :redacted`

      - `type: :"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: String`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: String`

            ID of the rubric file.

          - `type: :file`

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: String`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: :text`

      - `type: :"user.define_outcome"`

      - `max_iterations: Integer`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: String`

          The text content.

          minLength: 1

        - `type: :text`

      - `type: :"system.message"`

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: String`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: :manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: :environment_archived_error`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: :agent_archived_error`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: :environment_not_found_error`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: :vault_not_found_error`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: :file_not_found_error`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: :session_resource_not_found_error`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: :workspace_archived_error`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: :organization_disabled_error`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: :memory_store_archived_error`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: :skill_not_found_error`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: :vault_archived_error`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: :unknown_error`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: :self_hosted_resources_unsupported_error`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: :mcp_egress_blocked_error`

      - `type: :error`

  - `resources: Array[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: :github_repository`

      - `url: String`

        Github URL of the repository

      - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `name: String`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: :branch`

        - `class BetaManagedAgentsCommitCheckout`

          - `sha: String`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: :commit`

      - `mount_path: String`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: String`

        ID of a previously uploaded file.

      - `type: :file`

      - `mount_path: String`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: String`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: :memory_store`

      - `access: :read_write | :read_only`

        Access mode for an attached memory store.

        - `:read_write`

        - `:read_only`

      - `instructions: String`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: String`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: String`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: :cron`

    - `last_run_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: Array[Time]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `:active`

    - `:paused`

  - `type: :deployment`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: Array[String]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: String`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: :limit`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.deployments.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Compiles yesterday's orders into a report every weekday morning.",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "initial_events": [
        {
          "content": [
            {
              "text": "Compile yesterday's orders into report.md.",
              "type": "text"
            }
          ],
          "type": "user.message"
        }
      ],
      "metadata": {},
      "name": "Daily order report",
      "paused_reason": {
        "type": "manual"
      },
      "resources": [
        {
          "type": "github_repository",
          "url": "url",
          "checkout": {
            "name": "main",
            "type": "branch"
          },
          "mount_path": "mount_path"
        }
      ],
      "schedule": {
        "expression": "0 9 * * 1-5",
        "timezone": "America/Los_Angeles",
        "type": "cron",
        "last_run_at": "2026-03-16T16:00:09Z",
        "upcoming_runs_at": [
          "2026-03-17T16:00:00Z",
          "2026-03-18T16:00:00Z"
        ]
      },
      "status": "active",
      "type": "deployment",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ],
      "budget": {
        "max_list_cost": {
          "amount": "2500",
          "currency": "USD"
        },
        "type": "limit"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Deployment

`beta.deployments.retrieve(deployment_id, **kwargs) -> BetaManagedAgentsDeployment`

**GET** `/v1/deployments/{deployment_id}`

Get Deployment

#### Parameters

- `deployment_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: String`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: String`

    - `type: :agent`

    - `version: Integer`

      format: int32

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

    Description of what the deployment does.

  - `environment_id: String`

    ID of the `environment` where sessions run.

  - `initial_events: Array[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

            minLength: 1

          - `type: :text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

                minLength: 1

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

                minLength: 1

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

                minLength: 1

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: :text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: :redacted`

      - `type: :"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: String`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: String`

            ID of the rubric file.

          - `type: :file`

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: String`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: :text`

      - `type: :"user.define_outcome"`

      - `max_iterations: Integer`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: String`

          The text content.

          minLength: 1

        - `type: :text`

      - `type: :"system.message"`

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: String`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: :manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: :environment_archived_error`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: :agent_archived_error`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: :environment_not_found_error`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: :vault_not_found_error`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: :file_not_found_error`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: :session_resource_not_found_error`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: :workspace_archived_error`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: :organization_disabled_error`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: :memory_store_archived_error`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: :skill_not_found_error`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: :vault_archived_error`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: :unknown_error`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: :self_hosted_resources_unsupported_error`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: :mcp_egress_blocked_error`

      - `type: :error`

  - `resources: Array[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: :github_repository`

      - `url: String`

        Github URL of the repository

      - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `name: String`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: :branch`

        - `class BetaManagedAgentsCommitCheckout`

          - `sha: String`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: :commit`

      - `mount_path: String`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: String`

        ID of a previously uploaded file.

      - `type: :file`

      - `mount_path: String`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: String`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: :memory_store`

      - `access: :read_write | :read_only`

        Access mode for an attached memory store.

        - `:read_write`

        - `:read_only`

      - `instructions: String`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: String`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: String`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: :cron`

    - `last_run_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: Array[Time]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `:active`

    - `:paused`

  - `type: :deployment`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: Array[String]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: String`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: :limit`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deployment = anthropic.beta.deployments.retrieve("depl_011CZkZcDH3vPqd7xnEfwTai")

puts(beta_managed_agents_deployment)
```

##### Response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

### Update Deployment

`beta.deployments.update(deployment_id, **kwargs) -> BetaManagedAgentsDeployment`

**POST** `/v1/deployments/{deployment_id}`

Update Deployment

#### Parameters

- `deployment_id: String`

- `agent: String | BetaManagedAgentsAgentParams`

  Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

  - `String = String`

  - `class BetaManagedAgentsAgentParams`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: String`

      The `agent` ID.

      minLength: 1, maxLength: 128

    - `type: :agent`

    - `version: Integer`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

      format: int32

- `budget: BetaManagedAgentsBudgetLimit`

  A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `max_list_cost: BetaMonetaryAmount`

    A monetary amount in a specific currency.

    - `amount: String`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `type: :limit`

- `description: String`

  Description. Omit to preserve; send empty string or null to clear.

  maxLength: 2048

- `environment_id: String`

  ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

  maxLength: 128

- `initial_events: Array[BetaManagedAgentsDeploymentInitialEventParams]`

  Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

  - `class BetaManagedAgentsUserMessageEventParams`

    Parameters for sending a user message to the session.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

          minLength: 1

        - `type: :text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

              minLength: 1

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: :base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

            - `url: String`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

              minLength: 1

            - `type: :file`

        - `type: :image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

              minLength: 1

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: :base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

              minLength: 1

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: :text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

            - `url: String`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

              minLength: 1

            - `type: :file`

        - `type: :document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: :redacted`

    - `type: :"user.message"`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: String`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams | BetaManagedAgentsTextRubricParams`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: String`

          ID of the rubric file.

        - `type: :file`

      - `class BetaManagedAgentsTextRubricParams`

        Rubric content provided inline as text.

        - `content: String`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

        - `type: :text`

    - `type: :"user.define_outcome"`

    - `max_iterations: Integer`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `class BetaManagedAgentsSystemMessageEventParams`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: Array[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `text: String`

        The text content.

        minLength: 1

      - `type: :text`

    - `type: :"system.message"`

- `metadata: Hash[Symbol, String]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name: String`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

  maxLength: 256

- `resources: Array[BetaManagedAgentsGitHubRepositoryResourceParams | BetaManagedAgentsFileResourceParams | BetaManagedAgentsMemoryStoreResourceParam]`

  Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

  - `class BetaManagedAgentsGitHubRepositoryResourceParams`

    Mount a GitHub repository into the session's container.

    - `authorization_token: String`

      GitHub authorization token used to clone the repository.

      minLength: 1, maxLength: 4096

    - `type: :github_repository`

    - `url: String`

      Github URL of the repository

      minLength: 1, maxLength: 2048

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: :branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: :commit`

    - `mount_path: String`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

      minLength: 1, maxLength: 4096

  - `class BetaManagedAgentsFileResourceParams`

    Mount a file uploaded via the Files API into the session.

    - `file_id: String`

      ID of a previously uploaded file.

      minLength: 1, maxLength: 128

    - `type: :file`

    - `mount_path: String`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

      minLength: 1, maxLength: 4096

  - `class BetaManagedAgentsMemoryStoreResourceParam`

    Parameters for attaching a memory store to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

- `schedule: BetaManagedAgentsScheduleParams`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: String`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    minLength: 1, maxLength: 256

  - `timezone: String`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

    minLength: 1

  - `type: :cron`

- `vault_ids: Array[String]`

  Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: String`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: String`

    - `type: :agent`

    - `version: Integer`

      format: int32

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

    Description of what the deployment does.

  - `environment_id: String`

    ID of the `environment` where sessions run.

  - `initial_events: Array[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

            minLength: 1

          - `type: :text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

                minLength: 1

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

                minLength: 1

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

                minLength: 1

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: :text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: :redacted`

      - `type: :"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: String`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: String`

            ID of the rubric file.

          - `type: :file`

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: String`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: :text`

      - `type: :"user.define_outcome"`

      - `max_iterations: Integer`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: String`

          The text content.

          minLength: 1

        - `type: :text`

      - `type: :"system.message"`

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: String`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: :manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: :environment_archived_error`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: :agent_archived_error`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: :environment_not_found_error`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: :vault_not_found_error`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: :file_not_found_error`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: :session_resource_not_found_error`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: :workspace_archived_error`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: :organization_disabled_error`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: :memory_store_archived_error`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: :skill_not_found_error`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: :vault_archived_error`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: :unknown_error`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: :self_hosted_resources_unsupported_error`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: :mcp_egress_blocked_error`

      - `type: :error`

  - `resources: Array[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: :github_repository`

      - `url: String`

        Github URL of the repository

      - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `name: String`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: :branch`

        - `class BetaManagedAgentsCommitCheckout`

          - `sha: String`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: :commit`

      - `mount_path: String`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: String`

        ID of a previously uploaded file.

      - `type: :file`

      - `mount_path: String`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: String`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: :memory_store`

      - `access: :read_write | :read_only`

        Access mode for an attached memory store.

        - `:read_write`

        - `:read_only`

      - `instructions: String`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: String`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: String`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: :cron`

    - `last_run_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: Array[Time]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `:active`

    - `:paused`

  - `type: :deployment`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: Array[String]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: String`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: :limit`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deployment = anthropic.beta.deployments.update("depl_011CZkZcDH3vPqd7xnEfwTai")

puts(beta_managed_agents_deployment)
```

##### Response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

### Archive Deployment

`beta.deployments.archive(deployment_id, **kwargs) -> BetaManagedAgentsDeployment`

**POST** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

#### Parameters

- `deployment_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: String`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: String`

    - `type: :agent`

    - `version: Integer`

      format: int32

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

    Description of what the deployment does.

  - `environment_id: String`

    ID of the `environment` where sessions run.

  - `initial_events: Array[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

            minLength: 1

          - `type: :text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

                minLength: 1

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

                minLength: 1

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

                minLength: 1

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: :text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: :redacted`

      - `type: :"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: String`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: String`

            ID of the rubric file.

          - `type: :file`

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: String`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: :text`

      - `type: :"user.define_outcome"`

      - `max_iterations: Integer`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: String`

          The text content.

          minLength: 1

        - `type: :text`

      - `type: :"system.message"`

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: String`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: :manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: :environment_archived_error`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: :agent_archived_error`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: :environment_not_found_error`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: :vault_not_found_error`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: :file_not_found_error`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: :session_resource_not_found_error`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: :workspace_archived_error`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: :organization_disabled_error`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: :memory_store_archived_error`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: :skill_not_found_error`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: :vault_archived_error`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: :unknown_error`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: :self_hosted_resources_unsupported_error`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: :mcp_egress_blocked_error`

      - `type: :error`

  - `resources: Array[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: :github_repository`

      - `url: String`

        Github URL of the repository

      - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `name: String`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: :branch`

        - `class BetaManagedAgentsCommitCheckout`

          - `sha: String`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: :commit`

      - `mount_path: String`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: String`

        ID of a previously uploaded file.

      - `type: :file`

      - `mount_path: String`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: String`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: :memory_store`

      - `access: :read_write | :read_only`

        Access mode for an attached memory store.

        - `:read_write`

        - `:read_only`

      - `instructions: String`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: String`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: String`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: :cron`

    - `last_run_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: Array[Time]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `:active`

    - `:paused`

  - `type: :deployment`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: Array[String]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: String`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: :limit`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deployment = anthropic.beta.deployments.archive("depl_011CZkZcDH3vPqd7xnEfwTai")

puts(beta_managed_agents_deployment)
```

##### Response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

### Run Deployment Now

`beta.deployments.run(deployment_id, **kwargs) -> BetaManagedAgentsDeploymentRun`

**POST** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

#### Parameters

- `deployment_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeploymentRun`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: String`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: String`

    - `type: :agent`

    - `version: Integer`

      format: int32

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `deployment_id: String`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError | BetaManagedAgentsAgentArchivedRunError | BetaManagedAgentsEnvironmentNotFoundRunError | 13 more`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError`

      The deployment's environment was archived.

      - `message: String`

        Human-readable error description.

      - `type: :environment_archived_error`

    - `class BetaManagedAgentsAgentArchivedRunError`

      The deployment's agent was archived.

      - `message: String`

        Human-readable error description.

      - `type: :agent_archived_error`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError`

      The deployment's environment no longer exists.

      - `message: String`

        Human-readable error description.

      - `type: :environment_not_found_error`

    - `class BetaManagedAgentsVaultNotFoundRunError`

      A vault referenced by the deployment no longer exists.

      - `message: String`

        Human-readable error description.

      - `type: :vault_not_found_error`

    - `class BetaManagedAgentsVaultArchivedRunError`

      A vault referenced by the deployment is archived.

      - `message: String`

        Human-readable error description.

      - `type: :vault_archived_error`

    - `class BetaManagedAgentsFileNotFoundRunError`

      A file resource referenced by the deployment no longer exists.

      - `message: String`

        Human-readable error description.

      - `type: :file_not_found_error`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError`

      A memory store referenced by the deployment is archived.

      - `message: String`

        Human-readable error description.

      - `type: :memory_store_archived_error`

    - `class BetaManagedAgentsSkillNotFoundRunError`

      A skill referenced by the deployment's agent no longer exists.

      - `message: String`

        Human-readable error description.

      - `type: :skill_not_found_error`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError`

      A referenced resource no longer exists and its kind was not reported.

      - `message: String`

        Human-readable error description.

      - `type: :session_resource_not_found_error`

    - `class BetaManagedAgentsWorkspaceArchivedRunError`

      The deployment's workspace was archived.

      - `message: String`

        Human-readable error description.

      - `type: :workspace_archived_error`

    - `class BetaManagedAgentsOrganizationDisabledRunError`

      The deployment's organization is disabled.

      - `message: String`

        Human-readable error description.

      - `type: :organization_disabled_error`

    - `class BetaManagedAgentsSessionRateLimitedRunError`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: String`

        Human-readable error description.

      - `type: :session_rate_limited_error`

    - `class BetaManagedAgentsSessionCreationRejectedRunError`

      The session create request was rejected with a non-retryable validation error.

      - `message: String`

        Human-readable error description.

      - `type: :session_creation_rejected_error`

    - `class BetaManagedAgentsUnknownRunError`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: String`

        Human-readable error description.

      - `type: :unknown_error`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: String`

        Human-readable error description.

      - `type: :self_hosted_resources_unsupported_error`

    - `class BetaManagedAgentsMCPEgressBlockedRunError`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: String`

        Human-readable error description.

      - `type: :mcp_egress_blocked_error`

  - `session_id: String`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: :schedule`

    - `class BetaManagedAgentsManualTriggerContext`

      The run was started manually by creating a session directly against the deployment.

      - `type: :manual`

  - `type: :deployment_run`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deployment_run = anthropic.beta.deployments.run("depl_011CZkZcDH3vPqd7xnEfwTai")

puts(beta_managed_agents_deployment_run)
```

##### Response (200)

```json
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
}
```

### Pause Deployment

`beta.deployments.pause(deployment_id, **kwargs) -> BetaManagedAgentsDeployment`

**POST** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

#### Parameters

- `deployment_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: String`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: String`

    - `type: :agent`

    - `version: Integer`

      format: int32

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

    Description of what the deployment does.

  - `environment_id: String`

    ID of the `environment` where sessions run.

  - `initial_events: Array[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

            minLength: 1

          - `type: :text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

                minLength: 1

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

                minLength: 1

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

                minLength: 1

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: :text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: :redacted`

      - `type: :"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: String`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: String`

            ID of the rubric file.

          - `type: :file`

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: String`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: :text`

      - `type: :"user.define_outcome"`

      - `max_iterations: Integer`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: String`

          The text content.

          minLength: 1

        - `type: :text`

      - `type: :"system.message"`

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: String`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: :manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: :environment_archived_error`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: :agent_archived_error`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: :environment_not_found_error`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: :vault_not_found_error`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: :file_not_found_error`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: :session_resource_not_found_error`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: :workspace_archived_error`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: :organization_disabled_error`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: :memory_store_archived_error`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: :skill_not_found_error`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: :vault_archived_error`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: :unknown_error`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: :self_hosted_resources_unsupported_error`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: :mcp_egress_blocked_error`

      - `type: :error`

  - `resources: Array[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: :github_repository`

      - `url: String`

        Github URL of the repository

      - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `name: String`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: :branch`

        - `class BetaManagedAgentsCommitCheckout`

          - `sha: String`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: :commit`

      - `mount_path: String`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: String`

        ID of a previously uploaded file.

      - `type: :file`

      - `mount_path: String`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: String`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: :memory_store`

      - `access: :read_write | :read_only`

        Access mode for an attached memory store.

        - `:read_write`

        - `:read_only`

      - `instructions: String`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: String`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: String`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: :cron`

    - `last_run_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: Array[Time]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `:active`

    - `:paused`

  - `type: :deployment`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: Array[String]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: String`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: :limit`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deployment = anthropic.beta.deployments.pause("depl_011CZkZcDH3vPqd7xnEfwTai")

puts(beta_managed_agents_deployment)
```

##### Response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

### Unpause Deployment

`beta.deployments.unpause(deployment_id, **kwargs) -> BetaManagedAgentsDeployment`

**POST** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

#### Parameters

- `deployment_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeployment`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: String`

    Unique identifier for this deployment.

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: String`

    - `type: :agent`

    - `version: Integer`

      format: int32

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

    Description of what the deployment does.

  - `environment_id: String`

    ID of the `environment` where sessions run.

  - `initial_events: Array[BetaManagedAgentsDeploymentInitialEvent]`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent`

      A user message sent to the session.

      - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock`

          Regular text content.

          - `text: String`

            The text content.

            minLength: 1

          - `type: :text`

        - `class BetaManagedAgentsImageBlock`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource`

              Base64-encoded image data.

              - `data: String`

                Base64-encoded image data.

                minLength: 1

              - `media_type: String`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsURLImageSource`

              Image referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource`

              Image referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :image`

        - `class BetaManagedAgentsDocumentBlock`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource`

              Base64-encoded document data.

              - `data: String`

                Base64-encoded document data.

                minLength: 1

              - `media_type: String`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: :base64`

            - `class BetaManagedAgentsPlainTextDocumentSource`

              Plain text document content.

              - `data: String`

                The plain text content.

                minLength: 1

              - `media_type: :"text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: :text`

            - `class BetaManagedAgentsURLDocumentSource`

              Document referenced by URL.

              - `type: :url`

              - `url: String`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource`

              Document referenced by file ID.

              - `file_id: String`

                ID of a previously uploaded file.

                minLength: 1

              - `type: :file`

          - `type: :document`

          - `context: String`

            Additional context about the document for the model.

          - `title: String`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock`

          Placeholder for content withheld by Anthropic model policy.

          - `type: :redacted`

      - `type: :"user.message"`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: String`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: String`

            ID of the rubric file.

          - `type: :file`

        - `class BetaManagedAgentsTextRubric`

          Rubric content provided inline as text.

          - `content: String`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: :text`

      - `type: :"user.define_outcome"`

      - `max_iterations: Integer`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: Array[BetaManagedAgentsSystemContentBlock]`

        System content blocks to append. Text-only.

        - `text: String`

          The text content.

          minLength: 1

        - `type: :text`

      - `type: :"system.message"`

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: String`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason`

      The caller invoked the pause endpoint on the deployment.

      - `type: :manual`

    - `class BetaManagedAgentsErrorDeploymentPausedReason`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsDeploymentPausedReasonError`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError`

          The deployment's environment was archived.

          - `type: :environment_archived_error`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError`

          The deployment's agent was archived.

          - `type: :agent_archived_error`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError`

          The deployment's environment no longer exists.

          - `type: :environment_not_found_error`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError`

          A vault referenced by the deployment no longer exists.

          - `type: :vault_not_found_error`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError`

          A file resource referenced by the deployment no longer exists.

          - `type: :file_not_found_error`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError`

          A referenced resource no longer exists and its kind was not reported.

          - `type: :session_resource_not_found_error`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError`

          The deployment's workspace was archived.

          - `type: :workspace_archived_error`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError`

          The deployment's organization is disabled.

          - `type: :organization_disabled_error`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError`

          A memory store referenced by the deployment is archived.

          - `type: :memory_store_archived_error`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError`

          A skill referenced by the deployment's agent no longer exists.

          - `type: :skill_not_found_error`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError`

          A vault referenced by the deployment is archived.

          - `type: :vault_archived_error`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: :unknown_error`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: :self_hosted_resources_unsupported_error`

        - `class BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: :mcp_egress_blocked_error`

      - `type: :error`

  - `resources: Array[BetaManagedAgentsSessionResourceConfig]`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: :github_repository`

      - `url: String`

        Github URL of the repository

      - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout`

          - `name: String`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: :branch`

        - `class BetaManagedAgentsCommitCheckout`

          - `sha: String`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: :commit`

      - `mount_path: String`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig`

      A file mounted into each session's container.

      - `file_id: String`

        ID of a previously uploaded file.

      - `type: :file`

      - `mount_path: String`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: String`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: :memory_store`

      - `access: :read_write | :read_only`

        Access mode for an attached memory store.

        - `:read_write`

        - `:read_only`

      - `instructions: String`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: BetaManagedAgentsSchedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: String`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `timezone: String`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `type: :cron`

    - `last_run_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `upcoming_runs_at: Array[Time]`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `:active`

    - `:paused`

  - `type: :deployment`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_ids: Array[String]`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `budget: BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: String`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: :limit`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deployment = anthropic.beta.deployments.unpause("depl_011CZkZcDH3vPqd7xnEfwTai")

puts(beta_managed_agents_deployment)
```

##### Response (200)

```json
{
  "id": "depl_011CZkZcDH3vPqd7xnEfwTai",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Compiles yesterday's orders into a report every weekday morning.",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "initial_events": [
    {
      "content": [
        {
          "text": "Compile yesterday's orders into report.md.",
          "type": "text"
        }
      ],
      "type": "user.message"
    }
  ],
  "metadata": {},
  "name": "Daily order report",
  "paused_reason": {
    "type": "manual"
  },
  "resources": [
    {
      "type": "github_repository",
      "url": "url",
      "checkout": {
        "name": "main",
        "type": "branch"
      },
      "mount_path": "mount_path"
    }
  ],
  "schedule": {
    "expression": "0 9 * * 1-5",
    "timezone": "America/Los_Angeles",
    "type": "cron",
    "last_run_at": "2026-03-16T16:00:09Z",
    "upcoming_runs_at": [
      "2026-03-17T16:00:00Z",
      "2026-03-18T16:00:00Z"
    ]
  },
  "status": "active",
  "type": "deployment",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  }
}
```

## Beta › Deployment Runs

### List Deployment Runs

`beta.deployment_runs.list(**kwargs) -> PageCursor<BetaManagedAgentsDeploymentRun>`

**GET** `/v1/deployment_runs`

List Deployment Runs

#### Parameters

- `created_at_gt: Time`

  Return runs created strictly after this time (exclusive).

  format: date-time

- `created_at_gte: Time`

  Return runs created at or after this time (inclusive).

  format: date-time

- `created_at_lt: Time`

  Return runs created strictly before this time (exclusive).

  format: date-time

- `created_at_lte: Time`

  Return runs created at or before this time (inclusive).

  format: date-time

- `deployment_id: String`

  Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment_id returns 200 with empty data.

- `has_error: bool`

  Filter: true for runs with non-null error, false for runs with non-null session_id. Omit for all.

- `limit: Integer`

  Maximum results per page. Default 20, maximum 1000.

  format: int32

- `page: String`

  Opaque pagination cursor. Pass next_page from the previous response. Invalid or expired cursors return 400.

- `trigger_type: BetaManagedAgentsTriggerType`

  Filter runs by what triggered them. Omit to return all runs.

  - `:schedule`

  - `:manual`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeploymentRun`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: String`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: String`

    - `type: :agent`

    - `version: Integer`

      format: int32

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `deployment_id: String`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError | BetaManagedAgentsAgentArchivedRunError | BetaManagedAgentsEnvironmentNotFoundRunError | 13 more`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError`

      The deployment's environment was archived.

      - `message: String`

        Human-readable error description.

      - `type: :environment_archived_error`

    - `class BetaManagedAgentsAgentArchivedRunError`

      The deployment's agent was archived.

      - `message: String`

        Human-readable error description.

      - `type: :agent_archived_error`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError`

      The deployment's environment no longer exists.

      - `message: String`

        Human-readable error description.

      - `type: :environment_not_found_error`

    - `class BetaManagedAgentsVaultNotFoundRunError`

      A vault referenced by the deployment no longer exists.

      - `message: String`

        Human-readable error description.

      - `type: :vault_not_found_error`

    - `class BetaManagedAgentsVaultArchivedRunError`

      A vault referenced by the deployment is archived.

      - `message: String`

        Human-readable error description.

      - `type: :vault_archived_error`

    - `class BetaManagedAgentsFileNotFoundRunError`

      A file resource referenced by the deployment no longer exists.

      - `message: String`

        Human-readable error description.

      - `type: :file_not_found_error`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError`

      A memory store referenced by the deployment is archived.

      - `message: String`

        Human-readable error description.

      - `type: :memory_store_archived_error`

    - `class BetaManagedAgentsSkillNotFoundRunError`

      A skill referenced by the deployment's agent no longer exists.

      - `message: String`

        Human-readable error description.

      - `type: :skill_not_found_error`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError`

      A referenced resource no longer exists and its kind was not reported.

      - `message: String`

        Human-readable error description.

      - `type: :session_resource_not_found_error`

    - `class BetaManagedAgentsWorkspaceArchivedRunError`

      The deployment's workspace was archived.

      - `message: String`

        Human-readable error description.

      - `type: :workspace_archived_error`

    - `class BetaManagedAgentsOrganizationDisabledRunError`

      The deployment's organization is disabled.

      - `message: String`

        Human-readable error description.

      - `type: :organization_disabled_error`

    - `class BetaManagedAgentsSessionRateLimitedRunError`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: String`

        Human-readable error description.

      - `type: :session_rate_limited_error`

    - `class BetaManagedAgentsSessionCreationRejectedRunError`

      The session create request was rejected with a non-retryable validation error.

      - `message: String`

        Human-readable error description.

      - `type: :session_creation_rejected_error`

    - `class BetaManagedAgentsUnknownRunError`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: String`

        Human-readable error description.

      - `type: :unknown_error`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: String`

        Human-readable error description.

      - `type: :self_hosted_resources_unsupported_error`

    - `class BetaManagedAgentsMCPEgressBlockedRunError`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: String`

        Human-readable error description.

      - `type: :mcp_egress_blocked_error`

  - `session_id: String`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: :schedule`

    - `class BetaManagedAgentsManualTriggerContext`

      The run was started manually by creating a session directly against the deployment.

      - `type: :manual`

  - `type: :deployment_run`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.deployment_runs.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "type": "agent",
        "version": 1
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "deployment_id": "deployment_id",
      "error": {
        "message": "message",
        "type": "environment_archived_error"
      },
      "session_id": "session_id",
      "trigger_context": {
        "scheduled_at": "2019-12-27T18:11:19.117Z",
        "type": "schedule"
      },
      "type": "deployment_run"
    }
  ],
  "next_page": "next_page"
}
```

### Get Deployment Run

`beta.deployment_runs.retrieve(deployment_run_id, **kwargs) -> BetaManagedAgentsDeploymentRun`

**GET** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

#### Parameters

- `deployment_run_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeploymentRun`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: String`

    Unique identifier for this run (`drun_...`).

  - `agent: BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `id: String`

    - `type: :agent`

    - `version: Integer`

      format: int32

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `deployment_id: String`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError | BetaManagedAgentsAgentArchivedRunError | BetaManagedAgentsEnvironmentNotFoundRunError | 13 more`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError`

      The deployment's environment was archived.

      - `message: String`

        Human-readable error description.

      - `type: :environment_archived_error`

    - `class BetaManagedAgentsAgentArchivedRunError`

      The deployment's agent was archived.

      - `message: String`

        Human-readable error description.

      - `type: :agent_archived_error`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError`

      The deployment's environment no longer exists.

      - `message: String`

        Human-readable error description.

      - `type: :environment_not_found_error`

    - `class BetaManagedAgentsVaultNotFoundRunError`

      A vault referenced by the deployment no longer exists.

      - `message: String`

        Human-readable error description.

      - `type: :vault_not_found_error`

    - `class BetaManagedAgentsVaultArchivedRunError`

      A vault referenced by the deployment is archived.

      - `message: String`

        Human-readable error description.

      - `type: :vault_archived_error`

    - `class BetaManagedAgentsFileNotFoundRunError`

      A file resource referenced by the deployment no longer exists.

      - `message: String`

        Human-readable error description.

      - `type: :file_not_found_error`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError`

      A memory store referenced by the deployment is archived.

      - `message: String`

        Human-readable error description.

      - `type: :memory_store_archived_error`

    - `class BetaManagedAgentsSkillNotFoundRunError`

      A skill referenced by the deployment's agent no longer exists.

      - `message: String`

        Human-readable error description.

      - `type: :skill_not_found_error`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError`

      A referenced resource no longer exists and its kind was not reported.

      - `message: String`

        Human-readable error description.

      - `type: :session_resource_not_found_error`

    - `class BetaManagedAgentsWorkspaceArchivedRunError`

      The deployment's workspace was archived.

      - `message: String`

        Human-readable error description.

      - `type: :workspace_archived_error`

    - `class BetaManagedAgentsOrganizationDisabledRunError`

      The deployment's organization is disabled.

      - `message: String`

        Human-readable error description.

      - `type: :organization_disabled_error`

    - `class BetaManagedAgentsSessionRateLimitedRunError`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: String`

        Human-readable error description.

      - `type: :session_rate_limited_error`

    - `class BetaManagedAgentsSessionCreationRejectedRunError`

      The session create request was rejected with a non-retryable validation error.

      - `message: String`

        Human-readable error description.

      - `type: :session_creation_rejected_error`

    - `class BetaManagedAgentsUnknownRunError`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: String`

        Human-readable error description.

      - `type: :unknown_error`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: String`

        Human-readable error description.

      - `type: :self_hosted_resources_unsupported_error`

    - `class BetaManagedAgentsMCPEgressBlockedRunError`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: String`

        Human-readable error description.

      - `type: :mcp_egress_blocked_error`

  - `session_id: String`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: :schedule`

    - `class BetaManagedAgentsManualTriggerContext`

      The run was started manually by creating a session directly against the deployment.

      - `type: :manual`

  - `type: :deployment_run`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deployment_run = anthropic.beta.deployment_runs.retrieve("deployment_run_id")

puts(beta_managed_agents_deployment_run)
```

##### Response (200)

```json
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
}
```

## Beta › Vaults

### Create Vault

`beta.vaults.create(**kwargs) -> BetaManagedAgentsVault`

**POST** `/v1/vaults`

Create Vault

#### Parameters

- `display_name: String`

  Human-readable name for the vault. 1-255 characters.

  minLength: 1, maxLength: 255

- `metadata: Hash[Symbol, String]`

  Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `id: String`

    Unique identifier for the vault.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the vault.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the vault.

  - `type: :vault`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_vault = anthropic.beta.vaults.create(display_name: "Example vault")

puts(beta_managed_agents_vault)
```

##### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

### List Vaults

`beta.vaults.list(**kwargs) -> PageCursor<BetaManagedAgentsVault>`

**GET** `/v1/vaults`

List Vaults

#### Parameters

- `include_archived: bool`

  Whether to include archived vaults in the results.

- `limit: Integer`

  Maximum number of vaults to return per page. Defaults to 20, maximum 100.

  format: int32

- `page: String`

  Opaque pagination token from a previous `list_vaults` response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `id: String`

    Unique identifier for the vault.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the vault.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the vault.

  - `type: :vault`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.vaults.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Vault

`beta.vaults.retrieve(vault_id, **kwargs) -> BetaManagedAgentsVault`

**GET** `/v1/vaults/{vault_id}`

Get Vault

#### Parameters

- `vault_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `id: String`

    Unique identifier for the vault.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the vault.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the vault.

  - `type: :vault`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_vault = anthropic.beta.vaults.retrieve("vlt_011CZkZDLs7fYzm1hXNPeRjv")

puts(beta_managed_agents_vault)
```

##### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

### Update Vault

`beta.vaults.update(vault_id, **kwargs) -> BetaManagedAgentsVault`

**POST** `/v1/vaults/{vault_id}`

Update Vault

#### Parameters

- `vault_id: String`

- `display_name: String`

  Updated human-readable name for the vault. 1-255 characters.

  minLength: 1, maxLength: 255

- `metadata: Hash[Symbol, String]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `id: String`

    Unique identifier for the vault.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the vault.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the vault.

  - `type: :vault`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_vault = anthropic.beta.vaults.update("vlt_011CZkZDLs7fYzm1hXNPeRjv")

puts(beta_managed_agents_vault)
```

##### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

### Delete Vault

`beta.vaults.delete(vault_id, **kwargs) -> BetaManagedAgentsDeletedVault`

**DELETE** `/v1/vaults/{vault_id}`

Delete Vault

#### Parameters

- `vault_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeletedVault`

  Confirmation of a deleted vault.

  - `id: String`

    Unique identifier of the deleted vault.

  - `type: :vault_deleted`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_vault = anthropic.beta.vaults.delete("vlt_011CZkZDLs7fYzm1hXNPeRjv")

puts(beta_managed_agents_deleted_vault)
```

##### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

### Archive Vault

`beta.vaults.archive(vault_id, **kwargs) -> BetaManagedAgentsVault`

**POST** `/v1/vaults/{vault_id}/archive`

Archive Vault

#### Parameters

- `vault_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `id: String`

    Unique identifier for the vault.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the vault.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the vault.

  - `type: :vault`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_vault = anthropic.beta.vaults.archive("vlt_011CZkZDLs7fYzm1hXNPeRjv")

puts(beta_managed_agents_vault)
```

##### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Beta › Vaults › Credentials

### Create Credential

`beta.vaults.credentials.create(vault_id, **kwargs) -> BetaManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials`

Create Credential

#### Parameters

- `vault_id: String`

- `auth: BetaManagedAgentsMCPOAuthCreateParams | BetaManagedAgentsStaticBearerCreateParams | BetaManagedAgentsEnvironmentVariableCreateParams`

  Authentication details for creating a credential.

  - `class BetaManagedAgentsMCPOAuthCreateParams`

    Parameters for creating an MCP OAuth credential.

    - `access_token: String`

      OAuth access token.

      minLength: 1, maxLength: 8192

    - `mcp_server_url: String`

      URL of the MCP server this credential authenticates against.

      minLength: 1, maxLength: 2047

    - `type: :mcp_oauth`

    - `expires_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `refresh: BetaManagedAgentsMCPOAuthRefreshParams`

      OAuth refresh token parameters for creating a credential with refresh support.

      - `client_id: String`

        OAuth client ID.

        minLength: 1, maxLength: 1024

      - `refresh_token: String`

        OAuth refresh token.

        minLength: 1, maxLength: 4096

      - `token_endpoint: String`

        Token endpoint URL used to refresh the access token.

        minLength: 1, maxLength: 2047

      - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam | BetaManagedAgentsTokenEndpointAuthBasicParam | BetaManagedAgentsTokenEndpointAuthPostParam`

        Token endpoint requires no client authentication.

        - `class BetaManagedAgentsTokenEndpointAuthNoneParam`

          Token endpoint requires no client authentication.

          - `type: :none`

        - `class BetaManagedAgentsTokenEndpointAuthBasicParam`

          Token endpoint uses HTTP Basic authentication with client credentials.

          - `client_secret: String`

            OAuth client secret.

            minLength: 1, maxLength: 512

          - `type: :client_secret_basic`

        - `class BetaManagedAgentsTokenEndpointAuthPostParam`

          Token endpoint uses POST body authentication with client credentials.

          - `client_secret: String`

            OAuth client secret.

            minLength: 1, maxLength: 512

          - `type: :client_secret_post`

      - `resource: String`

        OAuth resource indicator.

        minLength: 1, maxLength: 2047

      - `scope: String`

        OAuth scope for the refresh request.

        minLength: 1, maxLength: 8192

  - `class BetaManagedAgentsStaticBearerCreateParams`

    Parameters for creating a static bearer token credential.

    - `token: String`

      Static bearer token value.

      minLength: 1, maxLength: 8192

    - `mcp_server_url: String`

      URL of the MCP server this credential authenticates against.

      minLength: 1, maxLength: 2047

    - `type: :static_bearer`

  - `class BetaManagedAgentsEnvironmentVariableCreateParams`

    Parameters for creating an environment variable credential.

    - `networking: BetaManagedAgentsCredentialNetworkingParams`

      Outbound hosts the secret value is substituted on.

      - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

        Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

        - `type: :unrestricted`

      - `class BetaManagedAgentsLimitedCredentialNetworkingParams`

        Substitute the secret only on requests to the listed hosts.

        - `allowed_hosts: Array[String]`

          Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

        - `type: :limited`

    - `secret_name: String`

      Name of the environment variable. Immutable after create.

      minLength: 1, maxLength: 255

    - `secret_value: String`

      Secret value. Write-only; never returned in responses.

      minLength: 1, maxLength: 4096

    - `type: :environment_variable`

    - `injection_location: BetaManagedAgentsInjectionLocationParams`

      Where in the outbound request the secret value may be substituted.

      - `body: bool`

        Substitute when the placeholder appears in the request body.

      - `header: bool`

        Substitute when the placeholder appears in a request header value.

- `display_name: String`

  Human-readable name for the credential. Up to 255 characters.

  maxLength: 255

- `metadata: Hash[Symbol, String]`

  Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: String`

    Unique identifier for the credential.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `type: :mcp_oauth`

      - `expires_at: Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `refresh: BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: String`

          OAuth client ID.

        - `token_endpoint: String`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: :none`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: :client_secret_basic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: :client_secret_post`

        - `resource: String`

          OAuth resource indicator.

        - `scope: String`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `type: :static_bearer`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: :unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: Array[String]`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: :limited`

      - `secret_name: String`

        Name of the environment variable.

      - `type: :environment_variable`

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the credential.

  - `type: :vault_credential`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: String`

    Identifier of the vault this credential belongs to.

  - `display_name: String`

    Human-readable name for the credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential = anthropic.beta.vaults.credentials.create(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  auth: {
    token: "bearer_exampletoken",
    mcp_server_url: "https://example-server.modelcontextprotocol.io/sse",
    type: :static_bearer
  }
)

puts(beta_managed_agents_credential)
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### List Credentials

`beta.vaults.credentials.list(vault_id, **kwargs) -> PageCursor<BetaManagedAgentsCredential>`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

#### Parameters

- `vault_id: String`

- `include_archived: bool`

  Whether to include archived credentials in the results.

- `limit: Integer`

  Maximum number of credentials to return per page. Defaults to 20, maximum 100.

  format: int32

- `page: String`

  Opaque pagination token from a previous `list_credentials` response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: String`

    Unique identifier for the credential.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `type: :mcp_oauth`

      - `expires_at: Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `refresh: BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: String`

          OAuth client ID.

        - `token_endpoint: String`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: :none`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: :client_secret_basic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: :client_secret_post`

        - `resource: String`

          OAuth resource indicator.

        - `scope: String`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `type: :static_bearer`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: :unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: Array[String]`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: :limited`

      - `secret_name: String`

        Name of the environment variable.

      - `type: :environment_variable`

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the credential.

  - `type: :vault_credential`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: String`

    Identifier of the vault this credential belongs to.

  - `display_name: String`

    Human-readable name for the credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.vaults.credentials.list("vlt_011CZkZDLs7fYzm1hXNPeRjv")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
      "archived_at": null,
      "auth": {
        "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
        "type": "static_bearer"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {
        "environment": "production"
      },
      "type": "vault_credential",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "display_name": "Example credential"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Credential

`beta.vaults.credentials.retrieve(credential_id, **kwargs) -> BetaManagedAgentsCredential`

**GET** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

#### Parameters

- `vault_id: String`

- `credential_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: String`

    Unique identifier for the credential.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `type: :mcp_oauth`

      - `expires_at: Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `refresh: BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: String`

          OAuth client ID.

        - `token_endpoint: String`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: :none`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: :client_secret_basic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: :client_secret_post`

        - `resource: String`

          OAuth resource indicator.

        - `scope: String`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `type: :static_bearer`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: :unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: Array[String]`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: :limited`

      - `secret_name: String`

        Name of the environment variable.

      - `type: :environment_variable`

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the credential.

  - `type: :vault_credential`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: String`

    Identifier of the vault this credential belongs to.

  - `display_name: String`

    Human-readable name for the credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential = anthropic.beta.vaults.credentials.retrieve(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_credential)
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### Update Credential

`beta.vaults.credentials.update(credential_id, **kwargs) -> BetaManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

#### Parameters

- `vault_id: String`

- `credential_id: String`

- `auth: BetaManagedAgentsMCPOAuthUpdateParams | BetaManagedAgentsStaticBearerUpdateParams | BetaManagedAgentsEnvironmentVariableUpdateParams`

  Updated authentication details for a credential.

  - `class BetaManagedAgentsMCPOAuthUpdateParams`

    Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

    - `type: :mcp_oauth`

    - `access_token: String`

      Updated OAuth access token.

      minLength: 1, maxLength: 8192

    - `expires_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `refresh: BetaManagedAgentsMCPOAuthRefreshUpdateParams`

      Parameters for updating OAuth refresh token configuration.

      - `refresh_token: String`

        Updated OAuth refresh token.

        minLength: 1, maxLength: 4096

      - `scope: String`

        Updated OAuth scope for the refresh request.

        maxLength: 8192

      - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthBasicUpdateParam | BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `type: :client_secret_basic`

          - `client_secret: String`

            Updated OAuth client secret.

            minLength: 1, maxLength: 512

        - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

          Updated POST body authentication parameters for the token endpoint.

          - `type: :client_secret_post`

          - `client_secret: String`

            Updated OAuth client secret.

            minLength: 1, maxLength: 512

  - `class BetaManagedAgentsStaticBearerUpdateParams`

    Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

    - `type: :static_bearer`

    - `token: String`

      Updated static bearer token value.

      minLength: 1, maxLength: 8192

  - `class BetaManagedAgentsEnvironmentVariableUpdateParams`

    Parameters for updating an environment variable credential. `secret_name` is immutable.

    - `type: :environment_variable`

    - `injection_location: BetaManagedAgentsInjectionLocationUpdateParams`

      Updated injection location.

      - `body: bool`

        Substitute when the placeholder appears in the request body.

      - `header: bool`

        Substitute when the placeholder appears in a request header value.

    - `networking: BetaManagedAgentsCredentialNetworkingParams`

      Updated networking scope. Full replacement.

      - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

        Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

        - `type: :unrestricted`

      - `class BetaManagedAgentsLimitedCredentialNetworkingParams`

        Substitute the secret only on requests to the listed hosts.

        - `allowed_hosts: Array[String]`

          Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

        - `type: :limited`

    - `secret_value: String`

      Updated secret value.

      minLength: 1, maxLength: 4096

- `display_name: String`

  Updated human-readable name for the credential. 1-255 characters.

  minLength: 1, maxLength: 255

- `metadata: Hash[Symbol, String]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: String`

    Unique identifier for the credential.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `type: :mcp_oauth`

      - `expires_at: Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `refresh: BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: String`

          OAuth client ID.

        - `token_endpoint: String`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: :none`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: :client_secret_basic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: :client_secret_post`

        - `resource: String`

          OAuth resource indicator.

        - `scope: String`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `type: :static_bearer`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: :unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: Array[String]`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: :limited`

      - `secret_name: String`

        Name of the environment variable.

      - `type: :environment_variable`

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the credential.

  - `type: :vault_credential`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: String`

    Identifier of the vault this credential belongs to.

  - `display_name: String`

    Human-readable name for the credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential = anthropic.beta.vaults.credentials.update(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_credential)
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### Delete Credential

`beta.vaults.credentials.delete(credential_id, **kwargs) -> BetaManagedAgentsDeletedCredential`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

#### Parameters

- `vault_id: String`

- `credential_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeletedCredential`

  Confirmation of a deleted credential.

  - `id: String`

    Unique identifier of the deleted credential.

  - `type: :vault_credential_deleted`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_credential = anthropic.beta.vaults.credentials.delete(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_deleted_credential)
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

### Archive Credential

`beta.vaults.credentials.archive(credential_id, **kwargs) -> BetaManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

#### Parameters

- `vault_id: String`

- `credential_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: String`

    Unique identifier for the credential.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `type: :mcp_oauth`

      - `expires_at: Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `refresh: BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: String`

          OAuth client ID.

        - `token_endpoint: String`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: :none`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: :client_secret_basic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: :client_secret_post`

        - `resource: String`

          OAuth resource indicator.

        - `scope: String`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `type: :static_bearer`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: :unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: Array[String]`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: :limited`

      - `secret_name: String`

        Name of the environment variable.

      - `type: :environment_variable`

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the credential.

  - `type: :vault_credential`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: String`

    Identifier of the vault this credential belongs to.

  - `display_name: String`

    Human-readable name for the credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential = anthropic.beta.vaults.credentials.archive(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_credential)
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### Validate Credential

`beta.vaults.credentials.mcp_oauth_validate(credential_id, **kwargs) -> BetaManagedAgentsCredentialValidation`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

#### Parameters

- `vault_id: String`

- `credential_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsCredentialValidation`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: String`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: bool`

    Whether the credential has a refresh token configured.

  - `mcp_probe: BetaManagedAgentsMCPProbe`

    The failing step of an MCP validation probe.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

      - `body: String`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: bool`

        Whether `body` was truncated.

      - `content_type: String`

        Value of the `Content-Type` response header.

      - `status_code: Integer`

        HTTP status code.

        format: int32

    - `method_: String`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: BetaManagedAgentsRefreshObject`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

    - `status: :succeeded | :failed | :connect_error | :no_refresh_token`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `:succeeded`

      - `:failed`

      - `:connect_error`

      - `:no_refresh_token`

  - `status: BetaManagedAgentsCredentialValidationStatus`

    Overall verdict of a credential validation probe.

    - `:valid`

    - `:invalid`

    - `:unknown`

  - `type: :vault_credential_validation`

  - `validated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: String`

    Identifier of the vault containing the credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential_validation = anthropic.beta.vaults.credentials.mcp_oauth_validate(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_credential_validation)
```

##### Response (200)

```json
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```

## Beta › Memory Stores

### Create a memory store

`beta.memory_stores.create(**kwargs) -> BetaManagedAgentsMemoryStore`

**POST** `/v1/memory_stores`

Create a memory store

#### Parameters

- `name: String`

  Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

  minLength: 1, maxLength: 255

- `description: String`

  Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

  maxLength: 1024

- `metadata: Hash[Symbol, String]`

  Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: String`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `name: String`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: :memory_store`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_store = anthropic.beta.memory_stores.create(name: "x")

puts(beta_managed_agents_memory_store)
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

### List memory stores

`beta.memory_stores.list(**kwargs) -> PageCursor<BetaManagedAgentsMemoryStore>`

**GET** `/v1/memory_stores`

List memory stores

#### Parameters

- `created_at_gte: Time`

  Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

  format: date-time

- `created_at_lte: Time`

  Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

  format: date-time

- `include_archived: bool`

  When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

- `limit: Integer`

  Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

  format: int32

- `page: String`

  Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: String`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `name: String`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: :memory_store`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.memory_stores.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "name": "name",
      "type": "memory_store",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "metadata": {
        "foo": "string"
      }
    }
  ],
  "next_page": "next_page"
}
```

### Retrieve a memory store

`beta.memory_stores.retrieve(memory_store_id, **kwargs) -> BetaManagedAgentsMemoryStore`

**GET** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

#### Parameters

- `memory_store_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: String`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `name: String`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: :memory_store`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_store = anthropic.beta.memory_stores.retrieve("memory_store_id")

puts(beta_managed_agents_memory_store)
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

### Update a memory store

`beta.memory_stores.update(memory_store_id, **kwargs) -> BetaManagedAgentsMemoryStore`

**POST** `/v1/memory_stores/{memory_store_id}`

Update a memory store

#### Parameters

- `memory_store_id: String`

- `description: String`

  New description for the store, up to 1024 characters. Pass an empty string to clear it.

  maxLength: 1024

- `metadata: Hash[Symbol, String]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `name: String`

  New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

  minLength: 1, maxLength: 255

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: String`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `name: String`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: :memory_store`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_store = anthropic.beta.memory_stores.update("memory_store_id")

puts(beta_managed_agents_memory_store)
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

### Delete a memory store

`beta.memory_stores.delete(memory_store_id, **kwargs) -> BetaManagedAgentsDeletedMemoryStore`

**DELETE** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

#### Parameters

- `memory_store_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeletedMemoryStore`

  Confirmation that a `memory_store` was deleted.

  - `id: String`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `type: :memory_store_deleted`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_memory_store = anthropic.beta.memory_stores.delete("memory_store_id")

puts(beta_managed_agents_deleted_memory_store)
```

##### Response (200)

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

### Archive a memory store

`beta.memory_stores.archive(memory_store_id, **kwargs) -> BetaManagedAgentsMemoryStore`

**POST** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

#### Parameters

- `memory_store_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsMemoryStore`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: String`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `name: String`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: :memory_store`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_store = anthropic.beta.memory_stores.archive("memory_store_id")

puts(beta_managed_agents_memory_store)
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  }
}
```

## Beta › Memory Stores › Memories

### Create a memory

`beta.memory_stores.memories.create(memory_store_id, **kwargs) -> BetaManagedAgentsMemory`

**POST** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

#### Parameters

- `memory_store_id: String`

- `content: String`

  UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

- `path: String`

  Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

  minLength: 2, maxLength: 1024

- `view: BetaManagedAgentsMemoryView`

  Query parameter for view

  - `:basic`

  - `:full`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsMemory`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: String`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: Integer`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    format: int32

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `memory_store_id: String`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: String`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: String`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: :memory`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `content: String`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory = anthropic.beta.memory_stores.memories.create("memory_store_id", content: "content", path: "xx")

puts(beta_managed_agents_memory)
```

##### Response (200)

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

### List memories

`beta.memory_stores.memories.list(memory_store_id, **kwargs) -> PageCursor<BetaManagedAgentsMemoryListItem>`

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List memories

#### Parameters

- `memory_store_id: String`

- `depth: Integer`

  `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

  format: int32

- `limit: Integer`

  Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

  format: int32

- `page: String`

  Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `path_prefix: String`

  Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

- `view: BetaManagedAgentsMemoryView`

  Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

  - `:basic`

  - `:full`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `BetaManagedAgentsMemoryListItem = BetaManagedAgentsMemory | BetaManagedAgentsMemoryPrefix`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `class BetaManagedAgentsMemory`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `id: String`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `content_sha256: String`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `content_size_bytes: Integer`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

      format: int32

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `memory_store_id: String`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `memory_version_id: String`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `path: String`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `type: :memory`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `content: String`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `path: String`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `type: :memory_prefix`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.memory_stores.memories.list("memory_store_id")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_store_id": "memory_store_id",
      "memory_version_id": "memory_version_id",
      "path": "path",
      "type": "memory",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "content": "content"
    }
  ],
  "next_page": "next_page"
}
```

### Retrieve a memory

`beta.memory_stores.memories.retrieve(memory_id, **kwargs) -> BetaManagedAgentsMemory`

**GET** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

#### Parameters

- `memory_store_id: String`

- `memory_id: String`

- `view: BetaManagedAgentsMemoryView`

  Query parameter for view

  - `:basic`

  - `:full`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsMemory`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: String`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: Integer`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    format: int32

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `memory_store_id: String`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: String`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: String`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: :memory`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `content: String`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory = anthropic.beta.memory_stores.memories.retrieve("memory_id", memory_store_id: "memory_store_id")

puts(beta_managed_agents_memory)
```

##### Response (200)

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

### Update a memory

`beta.memory_stores.memories.update(memory_id, **kwargs) -> BetaManagedAgentsMemory`

**POST** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

#### Parameters

- `memory_store_id: String`

- `memory_id: String`

- `view: BetaManagedAgentsMemoryView`

  Query parameter for view

  - `:basic`

  - `:full`

- `content: String`

  New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

- `path: String`

  New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

  minLength: 2, maxLength: 1024

- `precondition: BetaManagedAgentsPrecondition`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: :content_sha256`

  - `content_sha256: String`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsMemory`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: String`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: Integer`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    format: int32

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `memory_store_id: String`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: String`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: String`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: :memory`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `content: String`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory = anthropic.beta.memory_stores.memories.update("memory_id", memory_store_id: "memory_store_id")

puts(beta_managed_agents_memory)
```

##### Response (200)

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

### Delete a memory

`beta.memory_stores.memories.delete(memory_id, **kwargs) -> BetaManagedAgentsDeletedMemory`

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

#### Parameters

- `memory_store_id: String`

- `memory_id: String`

- `expected_content_sha256: String`

  Query parameter for expected_content_sha256

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsDeletedMemory`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `id: String`

    ID of the deleted memory (a `mem_...` value).

  - `type: :memory_deleted`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_memory = anthropic.beta.memory_stores.memories.delete("memory_id", memory_store_id: "memory_store_id")

puts(beta_managed_agents_deleted_memory)
```

##### Response (200)

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

## Beta › Memory Stores › Memory Versions

### List memory versions

`beta.memory_stores.memory_versions.list(memory_store_id, **kwargs) -> PageCursor<BetaManagedAgentsMemoryVersion>`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

#### Parameters

- `memory_store_id: String`

- `api_key_id: String`

  Query parameter for api_key_id

- `created_at_gte: Time`

  Return versions created at or after this time (inclusive).

  format: date-time

- `created_at_lte: Time`

  Return versions created at or before this time (inclusive).

  format: date-time

- `limit: Integer`

  Query parameter for limit

  format: int32

- `memory_id: String`

  Query parameter for memory_id

- `operation: BetaManagedAgentsMemoryVersionOperation`

  Query parameter for operation

  - `:created`

  - `:modified`

  - `:deleted`

- `page: String`

  Query parameter for page

- `service_account_id: String`

  Query parameter for service_account_id

- `session_id: String`

  Query parameter for session_id

- `view: BetaManagedAgentsMemoryView`

  Query parameter for view

  - `:basic`

  - `:full`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsMemoryVersion`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: String`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `memory_id: String`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: String`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `:created`

    - `:modified`

    - `:deleted`

  - `type: :memory_version`

  - `content: String`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: Integer`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `created_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: String`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        minLength: 1

      - `type: :session_actor`

    - `class BetaManagedAgentsAPIActor`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: String`

        ID of the API key that performed the write. This identifies the key, not the secret.

        minLength: 1

      - `type: :api_actor`

    - `class BetaManagedAgentsUserActor`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: :user_actor`

      - `user_id: String`

        ID of the user who performed the write (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: String`

        ID of the service account that performed the write (a `svac_...` value).

        minLength: 1

      - `type: :service_account_actor`

  - `path: String`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `redacted_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.memory_stores.memory_versions.list("memory_store_id")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "next_page"
}
```

### Retrieve a memory version

`beta.memory_stores.memory_versions.retrieve(memory_version_id, **kwargs) -> BetaManagedAgentsMemoryVersion`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

#### Parameters

- `memory_store_id: String`

- `memory_version_id: String`

- `view: BetaManagedAgentsMemoryView`

  Query parameter for view

  - `:basic`

  - `:full`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsMemoryVersion`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: String`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `memory_id: String`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: String`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `:created`

    - `:modified`

    - `:deleted`

  - `type: :memory_version`

  - `content: String`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: Integer`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `created_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: String`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        minLength: 1

      - `type: :session_actor`

    - `class BetaManagedAgentsAPIActor`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: String`

        ID of the API key that performed the write. This identifies the key, not the secret.

        minLength: 1

      - `type: :api_actor`

    - `class BetaManagedAgentsUserActor`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: :user_actor`

      - `user_id: String`

        ID of the user who performed the write (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: String`

        ID of the service account that performed the write (a `svac_...` value).

        minLength: 1

      - `type: :service_account_actor`

  - `path: String`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `redacted_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_version = anthropic.beta.memory_stores.memory_versions.retrieve(
  "memory_version_id",
  memory_store_id: "memory_store_id"
)

puts(beta_managed_agents_memory_version)
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

### Redact a memory version

`beta.memory_stores.memory_versions.redact(memory_version_id, **kwargs) -> BetaManagedAgentsMemoryVersion`

**POST** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

#### Parameters

- `memory_store_id: String`

- `memory_version_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaManagedAgentsMemoryVersion`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: String`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `memory_id: String`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: String`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `:created`

    - `:modified`

    - `:deleted`

  - `type: :memory_version`

  - `content: String`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: String`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: Integer`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `created_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: String`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        minLength: 1

      - `type: :session_actor`

    - `class BetaManagedAgentsAPIActor`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: String`

        ID of the API key that performed the write. This identifies the key, not the secret.

        minLength: 1

      - `type: :api_actor`

    - `class BetaManagedAgentsUserActor`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: :user_actor`

      - `user_id: String`

        ID of the user who performed the write (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `service_account_id: String`

        ID of the service account that performed the write (a `svac_...` value).

        minLength: 1

      - `type: :service_account_actor`

  - `path: String`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `redacted_by: BetaManagedAgentsActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_memory_version = anthropic.beta.memory_stores.memory_versions.redact(
  "memory_version_id",
  memory_store_id: "memory_store_id"
)

puts(beta_managed_agents_memory_version)
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

## Beta › Files

### Upload File

`beta.files.upload(**kwargs) -> BetaFileMetadata`

**POST** `/v1/files`

Upload File

#### Parameters

- `file: String`

  The file to upload

  format: binary

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaFileMetadata`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `mime_type: String`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

    - `type: :session`

      The type of scope (e.g., `"session"`).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_file_metadata = anthropic.beta.files.upload(file: StringIO.new("Example data"))

puts(beta_file_metadata)
```

##### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

### List Files

`beta.files.list(**kwargs) -> Page<BetaFileMetadata>`

**GET** `/v1/files`

List Files

#### Parameters

- `after_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

- `scope_id: String`

  Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaFileMetadata`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `mime_type: String`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

    - `type: :session`

      The type of scope (e.g., `"session"`).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.files.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "created_at": "2025-04-15T18:37:24.100435Z",
      "filename": "document.pdf",
      "mime_type": "application/pdf",
      "size_bytes": 102400,
      "type": "file",
      "downloadable": false,
      "scope": {
        "id": "id",
        "type": "session"
      }
    }
  ],
  "first_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "has_more": true,
  "last_id": "file_013Zva2CMHLNnXjNJJKqJ2EF"
}
```

### Download File

`beta.files.download(file_id, **kwargs) -> StringIO`

**GET** `/v1/files/{file_id}/content`

Download File

#### Parameters

- `file_id: String`

  ID of the File.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `StringIO`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

response = anthropic.beta.files.download("file_id")

puts(response)
```

### Get File Metadata

`beta.files.retrieve_metadata(file_id, **kwargs) -> BetaFileMetadata`

**GET** `/v1/files/{file_id}`

Get File Metadata

#### Parameters

- `file_id: String`

  ID of the File.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaFileMetadata`

  - `id: String`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: Time`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `filename: String`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `mime_type: String`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `size_bytes: Integer`

    Size of the file in bytes.

    minimum: 0

  - `type: :file`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: bool`

    Whether the file can be downloaded.

  - `scope: BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: String`

      The ID of the scoping resource (e.g., the session ID).

    - `type: :session`

      The type of scope (e.g., `"session"`).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_file_metadata = anthropic.beta.files.retrieve_metadata("file_id")

puts(beta_file_metadata)
```

##### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

### Delete File

`beta.files.delete(file_id, **kwargs) -> BetaDeletedFile`

**DELETE** `/v1/files/{file_id}`

Delete File

#### Parameters

- `file_id: String`

  ID of the File.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaDeletedFile`

  - `id: String`

    ID of the deleted file.

  - `type: :file_deleted`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_deleted_file = anthropic.beta.files.delete("file_id")

puts(beta_deleted_file)
```

##### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

## Beta › Skills

### Create Skill

`beta.skills.create(**kwargs) -> SkillCreateResponse`

**POST** `/v1/skills`

Create Skill

#### Parameters

- `files: Array[String]`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `display_title: String`

  Display title for the skill.

  This is a human-readable label that is not included in the prompt sent to the model.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class SkillCreateResponse`

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: String`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: String`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: String`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: String`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: String`

    ISO 8601 timestamp of when the skill was last updated.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

skill = anthropic.beta.skills.create(files: [StringIO.new("Example data")])

puts(skill)
```

##### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### List Skills

`beta.skills.list(**kwargs) -> PageCursor<SkillListResponse>`

**GET** `/v1/skills`

List Skills

#### Parameters

- `limit: Integer`

  Number of results to return per page.

  Maximum value is 100. Defaults to 20.

- `page: String`

  Pagination token for fetching a specific page of results.

  Pass the value from a previous response's `next_page` field to get the next page of results.

- `source: String`

  Filter skills by source.

  If provided, only skills from the specified source will be returned:

  * `"custom"`: only return user-created skills
  * `"anthropic"`: only return Anthropic-created skills

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class SkillListResponse`

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: String`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: String`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: String`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: String`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: String`

    ISO 8601 timestamp of when the skill was last updated.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.skills.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_title": "My Custom Skill",
      "latest_version": "1759178010641129",
      "source": "custom",
      "type": "type",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Skill

`beta.skills.retrieve(skill_id, **kwargs) -> SkillRetrieveResponse`

**GET** `/v1/skills/{skill_id}`

Get Skill

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class SkillRetrieveResponse`

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: String`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: String`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: String`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: String`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: String`

    ISO 8601 timestamp of when the skill was last updated.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

skill = anthropic.beta.skills.retrieve("skill_id")

puts(skill)
```

##### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Delete Skill

`beta.skills.delete(skill_id, **kwargs) -> SkillDeleteResponse`

**DELETE** `/v1/skills/{skill_id}`

Delete Skill

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class SkillDeleteResponse`

  - `id: String`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: String`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

skill = anthropic.beta.skills.delete("skill_id")

puts(skill)
```

##### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

## Beta › Skills › Versions

### Create Skill Version

`beta.skills.versions.create(skill_id, **kwargs) -> VersionCreateResponse`

**POST** `/v1/skills/{skill_id}/versions`

Create Skill Version

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `files: Array[String]`

  Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class VersionCreateResponse`

  - `id: String`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill version was created.

  - `description: String`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: String`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: String`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: String`

    Identifier for the skill that this version belongs to.

  - `type: String`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: String`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

version = anthropic.beta.skills.versions.create("skill_id", files: [StringIO.new("Example data")])

puts(version)
```

##### Response (200)

```json
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

### List Skill Versions

`beta.skills.versions.list(skill_id, **kwargs) -> PageCursor<VersionListResponse>`

**GET** `/v1/skills/{skill_id}/versions`

List Skill Versions

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `page: String`

  Optionally set to the `next_page` token from the previous response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class VersionListResponse`

  - `id: String`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill version was created.

  - `description: String`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: String`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: String`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: String`

    Identifier for the skill that this version belongs to.

  - `type: String`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: String`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.skills.versions.list("skill_id")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "skillver_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "A custom skill for doing something useful",
      "directory": "my-skill",
      "name": "my-skill",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "type",
      "version": "1759178010641129"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Download Skill Version Content

`beta.skills.versions.download(version, **kwargs) -> StringIO`

**GET** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: String`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `StringIO`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

response = anthropic.beta.skills.versions.download("version", skill_id: "skill_id")

puts(response)
```

### Get Skill Version

`beta.skills.versions.retrieve(version, **kwargs) -> VersionRetrieveResponse`

**GET** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: String`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class VersionRetrieveResponse`

  - `id: String`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: String`

    ISO 8601 timestamp of when the skill version was created.

  - `description: String`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: String`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: String`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: String`

    Identifier for the skill that this version belongs to.

  - `type: String`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: String`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

version = anthropic.beta.skills.versions.retrieve("version", skill_id: "skill_id")

puts(version)
```

##### Response (200)

```json
{
  "id": "skillver_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "A custom skill for doing something useful",
  "directory": "my-skill",
  "name": "my-skill",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type",
  "version": "1759178010641129"
}
```

### Delete Skill Version

`beta.skills.versions.delete(version, **kwargs) -> VersionDeleteResponse`

**DELETE** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

#### Parameters

- `skill_id: String`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `version: String`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class VersionDeleteResponse`

  - `id: String`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `type: String`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

version = anthropic.beta.skills.versions.delete("version", skill_id: "skill_id")

puts(version)
```

##### Response (200)

```json
{
  "id": "1759178010641129",
  "type": "type"
}
```

## Beta › Webhooks

### Unwrap

`beta.webhooks.unwrap() -> void`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

result = anthropic.beta.webhooks.unwrap

puts(result)
```

## Beta › User Profiles

### Create User Profile

`beta.user_profiles.create(**kwargs) -> BetaUserProfile`

**POST** `/v1/user_profiles`

Create User Profile

#### Parameters

- `access_type: :application | :passthrough`

  How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

  - `:application`

  - `:passthrough`

- `external_id: String`

  Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

  minLength: 1, maxLength: 255

- `metadata: Hash[Symbol, String]`

  Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

- `name: String`

  Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a resold-to company (`relationship` `resold` / `access_type` `passthrough`), that company's name where known. Maximum 255 characters.

  minLength: 1, maxLength: 255

- `relationship: :external | :resold | :internal`

  How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `:external`

  - `:resold`

  - `:internal`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaUserProfile`

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `type: :user_profile`

    Object type. Always `user_profile`.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `access_type: :application | :passthrough`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `:application`

    - `:passthrough`

  - `external_id: String`

    Platform's own identifier for this user. Not enforced unique.

  - `name: String`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: :external | :resold | :internal`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `:external`

    - `:resold`

    - `:internal`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_user_profile = anthropic.beta.user_profiles.create

puts(beta_user_profile)
```

##### Response (200)

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "access_type": "application",
  "external_id": "user_12345",
  "name": "Example User",
  "relationship": "external"
}
```

### List User Profiles

`beta.user_profiles.list(**kwargs) -> PageCursor<BetaUserProfile>`

**GET** `/v1/user_profiles`

List User Profiles

#### Parameters

- `limit: Integer`

  Query parameter for limit

  format: int32

- `order: :asc | :desc`

  Query parameter for order

  - `:asc`

  - `:desc`

- `page: String`

  Query parameter for page

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaUserProfile`

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `type: :user_profile`

    Object type. Always `user_profile`.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `access_type: :application | :passthrough`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `:application`

    - `:passthrough`

  - `external_id: String`

    Platform's own identifier for this user. Not enforced unique.

  - `name: String`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: :external | :resold | :internal`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `:external`

    - `:resold`

    - `:internal`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.user_profiles.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {},
      "trust_grants": {
        "cyber": {
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z",
      "access_type": "application",
      "external_id": "user_12345",
      "name": "Example User",
      "relationship": "external"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get User Profile

`beta.user_profiles.retrieve(user_profile_id, **kwargs) -> BetaUserProfile`

**GET** `/v1/user_profiles/{user_profile_id}`

Get User Profile

#### Parameters

- `user_profile_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaUserProfile`

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `type: :user_profile`

    Object type. Always `user_profile`.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `access_type: :application | :passthrough`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `:application`

    - `:passthrough`

  - `external_id: String`

    Platform's own identifier for this user. Not enforced unique.

  - `name: String`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: :external | :resold | :internal`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `:external`

    - `:resold`

    - `:internal`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_user_profile = anthropic.beta.user_profiles.retrieve("uprof_011CZkZCu8hGbp5mYRQgUmz9")

puts(beta_user_profile)
```

##### Response (200)

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "access_type": "application",
  "external_id": "user_12345",
  "name": "Example User",
  "relationship": "external"
}
```

### Update User Profile

`beta.user_profiles.update(user_profile_id, **kwargs) -> BetaUserProfile`

**POST** `/v1/user_profiles/{user_profile_id}`

Update User Profile

#### Parameters

- `user_profile_id: String`

- `access_type: :application | :passthrough`

  How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

  - `:application`

  - `:passthrough`

- `external_id: String`

  If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

  minLength: 1, maxLength: 255

- `metadata: Hash[Symbol, String]`

  Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `name: String`

  If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

  minLength: 1, maxLength: 255

- `relationship: :external | :resold | :internal`

  How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `:external`

  - `:resold`

  - `:internal`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaUserProfile`

  - `id: String`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Hash[Symbol, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: :active | :pending | :rejected`

      Status of the trust grant.

      - `:active`

      - `:pending`

      - `:rejected`

  - `type: :user_profile`

    Object type. Always `user_profile`.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `access_type: :application | :passthrough`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `:application`

    - `:passthrough`

  - `external_id: String`

    Platform's own identifier for this user. Not enforced unique.

  - `name: String`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: :external | :resold | :internal`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `:external`

    - `:resold`

    - `:internal`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_user_profile = anthropic.beta.user_profiles.update("uprof_011CZkZCu8hGbp5mYRQgUmz9")

puts(beta_user_profile)
```

##### Response (200)

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "access_type": "application",
  "external_id": "user_12345",
  "name": "Example User",
  "relationship": "external"
}
```

### Create Enrollment URL

`beta.user_profiles.create_enrollment_url(user_profile_id, **kwargs) -> BetaUserProfileEnrollmentURL`

**POST** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

#### Parameters

- `user_profile_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaUserProfileEnrollmentURL`

  - `expires_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: :enrollment_url`

    Object type. Always `enrollment_url`.

  - `url: String`

    Enrollment URL to send to the end user. Valid until `expires_at`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_user_profile_enrollment_url = anthropic.beta.user_profiles.create_enrollment_url("uprof_011CZkZCu8hGbp5mYRQgUmz9")

puts(beta_user_profile_enrollment_url)
```

##### Response (200)

```json
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

## Beta › Dreams

### Create a Dream

`beta.dreams.create(**kwargs) -> BetaDream`

**POST** `/v1/dreams`

Create a Dream

#### Parameters

- `inputs: Array[BetaDreamInput]`

  - `class BetaDreamMemoryStoreInput`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `memory_store_id: String`

      minLength: 1

    - `type: :memory_store`

  - `class BetaDreamSessionsInput`

    Input session transcripts the dream reads.

    - `session_ids: Array[String]`

    - `type: :sessions`

- `model: String | BetaDreamModelConfigParam`

  Model identifier and configuration applied to every pipeline stage.

  - `String = String`

  - `class BetaDreamModelConfigParam`

    Model identifier and configuration applied to every pipeline stage.

    - `id: String`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

- `instructions: String`

  minLength: 1, maxLength: 4096

- `output_behavior: BetaOutputBehavior`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `class BetaOutputBehaviorCreateNew`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type: :create_new`

  - `class BetaOutputBehaviorUpdateExisting`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `memory_store_id: String`

      minLength: 1

    - `type: :update_existing`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: String`

    - `type: String`

  - `inputs: Array[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: String`

        minLength: 1

      - `type: :memory_store`

    - `class BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array[String]`

      - `type: :sessions`

  - `instructions: String`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: String`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: :create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: String`

        minLength: 1

      - `type: :update_existing`

  - `outputs: Array[BetaDreamOutput]`

    - `memory_store_id: String`

    - `type: :memory_store`

  - `session_id: String`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `:pending`

    - `:running`

    - `:completed`

    - `:failed`

    - `:canceled`

  - `type: :dream`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: Integer`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Integer`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: Integer`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_dream = anthropic.beta.dreams.create(inputs: [{memory_store_id: "x", type: :memory_store}], model: "string")

puts(beta_dream)
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

### List Dreams

`beta.dreams.list(**kwargs) -> PageCursor<BetaDream>`

**GET** `/v1/dreams`

List Dreams

#### Parameters

- `created_at_gt: Time`

  Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

  format: date-time

- `created_at_lt: Time`

  Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

  format: date-time

- `include_archived: bool`

  Query parameter for include_archived

- `limit: Integer`

  Query parameter for limit

  format: int32

- `page: String`

  Query parameter for page

- `statuses: Array[BetaDreamStatus]`

  Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

  - `:pending`

  - `:running`

  - `:completed`

  - `:failed`

  - `:canceled`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: String`

    - `type: String`

  - `inputs: Array[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: String`

        minLength: 1

      - `type: :memory_store`

    - `class BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array[String]`

      - `type: :sessions`

  - `instructions: String`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: String`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: :create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: String`

        minLength: 1

      - `type: :update_existing`

  - `outputs: Array[BetaDreamOutput]`

    - `memory_store_id: String`

    - `type: :memory_store`

  - `session_id: String`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `:pending`

    - `:running`

    - `:completed`

    - `:failed`

    - `:canceled`

  - `type: :dream`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: Integer`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Integer`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: Integer`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.dreams.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "ended_at": "2019-12-27T18:11:19.117Z",
      "error": {
        "message": "message",
        "type": "type"
      },
      "inputs": [
        {
          "memory_store_id": "x",
          "type": "memory_store"
        }
      ],
      "instructions": "instructions",
      "model": {
        "id": "x",
        "speed": "standard"
      },
      "output_behavior": {
        "type": "create_new"
      },
      "outputs": [
        {
          "memory_store_id": "memory_store_id",
          "type": "memory_store"
        }
      ],
      "session_id": "session_id",
      "status": "pending",
      "type": "dream",
      "usage": {
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
      }
    }
  ],
  "next_page": "next_page"
}
```

### Get a Dream

`beta.dreams.retrieve(dream_id, **kwargs) -> BetaDream`

**GET** `/v1/dreams/{dream_id}`

Get a Dream

#### Parameters

- `dream_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: String`

    - `type: String`

  - `inputs: Array[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: String`

        minLength: 1

      - `type: :memory_store`

    - `class BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array[String]`

      - `type: :sessions`

  - `instructions: String`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: String`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: :create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: String`

        minLength: 1

      - `type: :update_existing`

  - `outputs: Array[BetaDreamOutput]`

    - `memory_store_id: String`

    - `type: :memory_store`

  - `session_id: String`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `:pending`

    - `:running`

    - `:completed`

    - `:failed`

    - `:canceled`

  - `type: :dream`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: Integer`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Integer`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: Integer`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_dream = anthropic.beta.dreams.retrieve("dream_id")

puts(beta_dream)
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

### Cancel a Dream

`beta.dreams.cancel(dream_id, **kwargs) -> BetaDream`

**POST** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

#### Parameters

- `dream_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: String`

    - `type: String`

  - `inputs: Array[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: String`

        minLength: 1

      - `type: :memory_store`

    - `class BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array[String]`

      - `type: :sessions`

  - `instructions: String`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: String`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: :create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: String`

        minLength: 1

      - `type: :update_existing`

  - `outputs: Array[BetaDreamOutput]`

    - `memory_store_id: String`

    - `type: :memory_store`

  - `session_id: String`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `:pending`

    - `:running`

    - `:completed`

    - `:failed`

    - `:canceled`

  - `type: :dream`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: Integer`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Integer`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: Integer`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_dream = anthropic.beta.dreams.cancel("dream_id")

puts(beta_dream)
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

### Archive a Dream

`beta.dreams.archive(dream_id, **kwargs) -> BetaDream`

**POST** `/v1/dreams/{dream_id}/archive`

Archive a Dream

#### Parameters

- `dream_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaDream`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: String`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `ended_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `error: BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: String`

    - `type: String`

  - `inputs: Array[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: String`

        minLength: 1

      - `type: :memory_store`

    - `class BetaDreamSessionsInput`

      Input session transcripts the dream reads.

      - `session_ids: Array[String]`

      - `type: :sessions`

  - `instructions: String`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: String`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `speed: :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: :create_new`

    - `class BetaOutputBehaviorUpdateExisting`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: String`

        minLength: 1

      - `type: :update_existing`

  - `outputs: Array[BetaDreamOutput]`

    - `memory_store_id: String`

    - `type: :memory_store`

  - `session_id: String`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `:pending`

    - `:running`

    - `:completed`

    - `:failed`

    - `:canceled`

  - `type: :dream`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: Integer`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Integer`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `output_tokens: Integer`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_dream = anthropic.beta.dreams.archive("dream_id")

puts(beta_dream)
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Beta › Tunnels

### Create Tunnel

`beta.tunnels.create(**kwargs) -> BetaTunnel`

**POST** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

#### Parameters

- `display_name: String`

  Optional human-readable name for the tunnel (1-255 characters).

  minLength: 1, maxLength: 255

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaTunnel`

  An MCP tunnel.

  - `id: String`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: String`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: :tunnel`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel = anthropic.beta.tunnels.create

puts(beta_tunnel)
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

### Get Tunnel

`beta.tunnels.retrieve(tunnel_id, **kwargs) -> BetaTunnel`

**GET** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

#### Parameters

- `tunnel_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaTunnel`

  An MCP tunnel.

  - `id: String`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: String`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: :tunnel`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel = anthropic.beta.tunnels.retrieve("tunnel_id")

puts(beta_tunnel)
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

### List Tunnels

`beta.tunnels.list(**kwargs) -> PageCursor<BetaTunnel>`

**GET** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

#### Parameters

- `include_archived: bool`

  Whether to include archived tunnels in the results. Defaults to false.

- `limit: Integer`

  Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

  format: int32

- `page: String`

  Opaque pagination cursor from a previous `list_tunnels` response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaTunnel`

  An MCP tunnel.

  - `id: String`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: String`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: :tunnel`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.tunnels.list

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "display_name": "display_name",
      "domain": "domain",
      "type": "tunnel"
    }
  ],
  "next_page": "next_page"
}
```

### Archive Tunnel

`beta.tunnels.archive(tunnel_id, **kwargs) -> BetaTunnel`

**POST** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

#### Parameters

- `tunnel_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaTunnel`

  An MCP tunnel.

  - `id: String`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: String`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: :tunnel`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel = anthropic.beta.tunnels.archive("tunnel_id")

puts(beta_tunnel)
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

### Reveal Tunnel Token

`beta.tunnels.reveal_token(tunnel_id, **kwargs) -> BetaTunnelToken`

**POST** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

#### Parameters

- `tunnel_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaTunnelToken`

  A tunnel's connector token.

  - `id: String`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: String`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: :tunnel_token`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_token = anthropic.beta.tunnels.reveal_token("tunnel_id")

puts(beta_tunnel_token)
```

##### Response (200)

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

### Rotate Tunnel Token

`beta.tunnels.rotate_token(tunnel_id, **kwargs) -> BetaTunnelToken`

**POST** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

#### Parameters

- `tunnel_id: String`

- `reason: String`

  Optional free-text reason for the rotation, recorded for audit.

  maxLength: 1024

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaTunnelToken`

  A tunnel's connector token.

  - `id: String`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: String`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: :tunnel_token`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_token = anthropic.beta.tunnels.rotate_token("tunnel_id")

puts(beta_tunnel_token)
```

##### Response (200)

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

## Beta › Tunnels › Certificates

### Create Tunnel Certificate

`beta.tunnels.certificates.create(tunnel_id, **kwargs) -> BetaTunnelCertificate`

**POST** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

#### Parameters

- `tunnel_id: String`

- `ca_certificate_pem: String`

  PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

  maxLength: 8192

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: String`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `expires_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `fingerprint: String`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: String`

    ID of the tunnel the certificate is registered against.

  - `type: :tunnel_certificate`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_certificate = anthropic.beta.tunnels.certificates.create("tunnel_id", ca_certificate_pem: "ca_certificate_pem")

puts(beta_tunnel_certificate)
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

### Get Tunnel Certificate

`beta.tunnels.certificates.retrieve(certificate_id, **kwargs) -> BetaTunnelCertificate`

**GET** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

#### Parameters

- `tunnel_id: String`

- `certificate_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: String`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `expires_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `fingerprint: String`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: String`

    ID of the tunnel the certificate is registered against.

  - `type: :tunnel_certificate`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_certificate = anthropic.beta.tunnels.certificates.retrieve("certificate_id", tunnel_id: "tunnel_id")

puts(beta_tunnel_certificate)
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

### List Tunnel Certificates

`beta.tunnels.certificates.list(tunnel_id, **kwargs) -> PageCursor<BetaTunnelCertificate>`

**GET** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

#### Parameters

- `tunnel_id: String`

- `include_archived: bool`

  Whether to include archived certificates in the results. Defaults to false.

- `limit: Integer`

  Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

  format: int32

- `page: String`

  Opaque pagination cursor from a previous `list_tunnel_certificates` response.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: String`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `expires_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `fingerprint: String`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: String`

    ID of the tunnel the certificate is registered against.

  - `type: :tunnel_certificate`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.tunnels.certificates.list("tunnel_id")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "expires_at": "2019-12-27T18:11:19.117Z",
      "fingerprint": "fingerprint",
      "tunnel_id": "tunnel_id",
      "type": "tunnel_certificate"
    }
  ],
  "next_page": "next_page"
}
```

### Archive Tunnel Certificate

`beta.tunnels.certificates.archive(certificate_id, **kwargs) -> BetaTunnelCertificate`

**POST** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

#### Parameters

- `tunnel_id: String`

- `certificate_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

#### Returns

- `class BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: String`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `expires_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `fingerprint: String`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: String`

    ID of the tunnel the certificate is registered against.

  - `type: :tunnel_certificate`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_tunnel_certificate = anthropic.beta.tunnels.certificates.archive("certificate_id", tunnel_id: "tunnel_id")

puts(beta_tunnel_certificate)
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```
