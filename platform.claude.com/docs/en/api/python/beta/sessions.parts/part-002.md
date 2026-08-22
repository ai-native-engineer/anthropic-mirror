<!-- source: https://platform.claude.com/docs/en/api/python/beta/sessions -->
<!-- part of: https://platform.claude.com/docs/en/api/python/beta/sessions -->

<!-- chunk-start -->

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["edit"]`

                      - `"edit"`

                  - `class BetaManagedAgentsReadToolConfig: …`

                    Configuration for the read tool.

                    - `enabled: bool`

                    - `name: Literal["read"]`

                      - `"read"`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["read"]`

                      - `"read"`

                  - `class BetaManagedAgentsWriteToolConfig: …`

                    Configuration for the write tool.

                    - `enabled: bool`

                    - `name: Literal["write"]`

                      - `"write"`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["write"]`

                      - `"write"`

                  - `class BetaManagedAgentsGlobToolConfig: …`

                    Configuration for the glob tool.

                    - `enabled: bool`

                    - `name: Literal["glob"]`

                      - `"glob"`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["glob"]`

                      - `"glob"`

                  - `class BetaManagedAgentsGrepToolConfig: …`

                    Configuration for the grep tool.

                    - `enabled: bool`

                    - `name: Literal["grep"]`

                      - `"grep"`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["grep"]`

                      - `"grep"`

                  - `class BetaManagedAgentsWebFetchToolConfig: …`

                    Configuration for the web_fetch tool.

                    - `enabled: bool`

                    - `name: Literal["web_fetch"]`

                      - `"web_fetch"`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["web_fetch"]`

                      - `"web_fetch"`

                    - `allowed_domains: Optional[List[str]]`

                    - `blocked_domains: Optional[List[str]]`

                    - `max_content_tokens: Optional[int]`

                  - `class BetaManagedAgentsWebSearchToolConfig: …`

                    Configuration for the web_search tool.

                    - `enabled: bool`

                    - `name: Literal["web_search"]`

                      - `"web_search"`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                    - `type: Literal["web_search"]`

                      - `"web_search"`

                    - `allowed_domains: Optional[List[str]]`

                    - `blocked_domains: Optional[List[str]]`

                    - `user_location: Optional[BetaManagedAgentsUserLocation]`

                      Approximate user location for search result localization.

                      - `type: Literal["approximate"]`

                        Location precision. Only "approximate" is supported.

                        - `"approximate"`

                      - `city: Optional[str]`

                        City name.

                      - `country: Optional[str]`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: Optional[str]`

                        Region or state name.

                      - `timezone: Optional[str]`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: bool`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                - `type: Literal["agent_toolset_20260401"]`

                  - `"agent_toolset_20260401"`

              - `class BetaManagedAgentsMCPToolset: …`

                - `configs: List[BetaManagedAgentsMCPToolConfig]`

                  - `enabled: bool`

                  - `name: str`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: bool`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: str`

                - `type: Literal["mcp_toolset"]`

                  - `"mcp_toolset"`

              - `class BetaManagedAgentsCustomTool: …`

                A custom tool as returned in API responses.

                - `description: str`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: Literal["object"]`

                    - `"object"`

                  - `properties: Optional[Dict[str, object]]`

                  - `required: Optional[List[str]]`

                - `name: str`

                - `type: Literal["custom"]`

                  - `"custom"`

            - `type: Literal["agent"]`

              - `"agent"`

            - `version: int`

          - `class BetaManagedAgentsAdvisor: …`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: str`

              The advisor model id.

            - `type: Literal["advisor"]`

              - `"advisor"`

        - `type: Literal["coordinator"]`

          - `"coordinator"`

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `type: Literal["agent"]`

        - `"agent"`

      - `version: int`

    - `budget: Optional[BetaManagedAgentsBudgetLimit]`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: str`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

          - `"USD"`

      - `type: Literal["limit"]`

        - `"limit"`

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent: …`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview: …`

        - `id: str`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: Literal["agent.message"]`

          - `"agent.message"`

      - `class BetaManagedAgentsAgentThinkingPreview: …`

        - `id: str`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: Literal["agent.thinking"]`

          - `"agent.thinking"`

    - `type: Literal["event_start"]`

      - `"event_start"`

  - `class BetaManagedAgentsDeltaEvent: …`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `type: Literal["content_delta"]`

        - `"content_delta"`

      - `index: Optional[int]`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: str`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: Literal["event_delta"]`

      - `"event_delta"`

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `text: str`

        The text content.

      - `type: Literal["text"]`

        - `"text"`

    - `type: Literal["system.message"]`

      - `"system.message"`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsSessionUsageEvent: …`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

    - `type: Literal["session.usage"]`

      - `"session.usage"`

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: Optional[float]`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

      - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: Optional[int]`

          Tokens used to create 1-hour ephemeral cache entries.

        - `ephemeral_5m_input_tokens: Optional[int]`

          Tokens used to create 5-minute ephemeral cache entries.

      - `cache_read_input_tokens: Optional[int]`

        Total tokens read from prompt cache.

      - `input_tokens: Optional[int]`

        Total input tokens consumed across all turns.

      - `list_cost: Optional[BetaMonetaryAmount]`

        A monetary amount in a specific currency.

      - `output_tokens: Optional[int]`

        Total output tokens generated across all turns.

      - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: Optional[int]`

          Number of server-executed web fetch requests.

        - `web_search_requests: Optional[int]`

          Number of server-executed web search requests.

    - `budget: Optional[BetaManagedAgentsBudgetLimit]`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
for event in client.beta.sessions.threads.events.stream(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
):
    print(event)
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
