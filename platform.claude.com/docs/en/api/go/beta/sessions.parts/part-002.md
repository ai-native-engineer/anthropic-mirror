<!-- source: https://platform.claude.com/docs/en/api/go/beta/sessions -->
<!-- part of: https://platform.claude.com/docs/en/api/go/beta/sessions -->

<!-- chunk-start -->

                  - `const BetaManagedAgentsAgentToolConfigNameBash BetaManagedAgentsAgentToolConfigName = "bash"`

                  - `const BetaManagedAgentsAgentToolConfigNameEdit BetaManagedAgentsAgentToolConfigName = "edit"`

                  - `const BetaManagedAgentsAgentToolConfigNameRead BetaManagedAgentsAgentToolConfigName = "read"`

                  - `const BetaManagedAgentsAgentToolConfigNameWrite BetaManagedAgentsAgentToolConfigName = "write"`

                  - `const BetaManagedAgentsAgentToolConfigNameGlob BetaManagedAgentsAgentToolConfigName = "glob"`

                  - `const BetaManagedAgentsAgentToolConfigNameGrep BetaManagedAgentsAgentToolConfigName = "grep"`

                  - `const BetaManagedAgentsAgentToolConfigNameWebFetch BetaManagedAgentsAgentToolConfigName = "web_fetch"`

                  - `const BetaManagedAgentsAgentToolConfigNameWebSearch BetaManagedAgentsAgentToolConfigName = "web_search"`

                - `PermissionPolicy BetaManagedAgentsAgentToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                    - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                      - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

                    - `Type BetaManagedAgentsAlwaysAskPolicyType`

                      - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

              - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAgentToolset20260401Type`

                - `const BetaManagedAgentsAgentToolset20260401TypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401Type = "agent_toolset_20260401"`

            - `type BetaManagedAgentsMCPToolset struct{…}`

              - `Configs []BetaManagedAgentsMCPToolConfig`

                - `Enabled bool`

                - `Name string`

                - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `MCPServerName string`

              - `Type BetaManagedAgentsMCPToolsetType`

                - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

            - `type BetaManagedAgentsCustomTool struct{…}`

              A custom tool as returned in API responses.

              - `Description string`

              - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `Type Object`

                  - `const ObjectObject Object = "object"`

                - `Properties map[string, any]`

                - `Required []string`

              - `Name string`

              - `Type BetaManagedAgentsCustomToolType`

                - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

          - `Type BetaManagedAgentsSessionThreadAgentType`

            - `const BetaManagedAgentsSessionThreadAgentTypeAgent BetaManagedAgentsSessionThreadAgentType = "agent"`

          - `Version int64`

        - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

          - `const BetaManagedAgentsSessionMultiagentCoordinatorTypeCoordinator BetaManagedAgentsSessionMultiagentCoordinatorType = "coordinator"`

      - `Name string`

      - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

        - `type BetaManagedAgentsAnthropicSkill struct{…}`

          A resolved Anthropic-managed skill.

        - `type BetaManagedAgentsCustomSkill struct{…}`

          A resolved user-created custom skill.

      - `System string`

      - `Tools []BetaManagedAgentsSessionAgentToolUnion`

        - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

        - `type BetaManagedAgentsMCPToolset struct{…}`

        - `type BetaManagedAgentsCustomTool struct{…}`

          A custom tool as returned in API responses.

      - `Type BetaManagedAgentsSessionAgentType`

        - `const BetaManagedAgentsSessionAgentTypeAgent BetaManagedAgentsSessionAgentType = "agent"`

      - `Version int64`

    - `Metadata map[string, string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Title string`

      The session's new title. Present only when the update changed it.

  - `type BetaManagedAgentsStartEvent struct{…}`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `Event BetaManagedAgentsStartEventPreviewUnion`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `type BetaManagedAgentsAgentMessagePreview struct{…}`

        - `ID string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `Type BetaManagedAgentsAgentMessagePreviewType`

          - `const BetaManagedAgentsAgentMessagePreviewTypeAgentMessage BetaManagedAgentsAgentMessagePreviewType = "agent.message"`

      - `type BetaManagedAgentsAgentThinkingPreview struct{…}`

        - `ID string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `Type BetaManagedAgentsAgentThinkingPreviewType`

          - `const BetaManagedAgentsAgentThinkingPreviewTypeAgentThinking BetaManagedAgentsAgentThinkingPreviewType = "agent.thinking"`

    - `Type BetaManagedAgentsStartEventType`

      - `const BetaManagedAgentsStartEventTypeEventStart BetaManagedAgentsStartEventType = "event_start"`

  - `type BetaManagedAgentsDeltaEvent struct{…}`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `Delta BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `Content BetaManagedAgentsTextBlock`

        Regular text content.

      - `Type BetaManagedAgentsDeltaContentType`

        - `const BetaManagedAgentsDeltaContentTypeContentDelta BetaManagedAgentsDeltaContentType = "content_delta"`

      - `Index int64`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `EventID string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `Type BetaManagedAgentsDeltaEventType`

      - `const BetaManagedAgentsDeltaEventTypeEventDelta BetaManagedAgentsDeltaEventType = "event_delta"`

  - `type BetaManagedAgentsSystemMessageEvent struct{…}`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `Text string`

        The text content.

      - `Type BetaManagedAgentsSystemContentBlockType`

        - `const BetaManagedAgentsSystemContentBlockTypeText BetaManagedAgentsSystemContentBlockType = "text"`

    - `Type BetaManagedAgentsSystemMessageEventType`

      - `const BetaManagedAgentsSystemMessageEventTypeSystemMessage BetaManagedAgentsSystemMessageEventType = "system.message"`

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	stream := client.Beta.Sessions.Threads.Events.StreamEvents(
		context.TODO(),
		"sthr_011CZkZVWa6oIjw0rgXZpnBt",
		anthropic.BetaSessionThreadEventStreamParams{
			SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
		},
	)
	for stream.Next() {
		fmt.Printf("%+v\n", stream.Current())
	}
	err := stream.Err()
	if err != nil {
		panic(err.Error())
	}
}
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
