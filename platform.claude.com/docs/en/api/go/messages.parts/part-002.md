<!-- source: https://platform.claude.com/docs/en/api/go/messages -->
<!-- part of: https://platform.claude.com/docs/en/api/go/messages -->

<!-- chunk-start -->
          * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
          * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
          * `"tool_use"`: the model invoked one or more tools
          * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
          * `"refusal"`: when streaming classifiers intervene to handle potential policy violations
          * `"model_context_window_exceeded"`: we exceeded the model's context window

          In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

          - `const StopReasonEndTurn StopReason = "end_turn"`

          - `const StopReasonMaxTokens StopReason = "max_tokens"`

          - `const StopReasonStopSequence StopReason = "stop_sequence"`

          - `const StopReasonToolUse StopReason = "tool_use"`

          - `const StopReasonPauseTurn StopReason = "pause_turn"`

          - `const StopReasonRefusal StopReason = "refusal"`

          - `const StopReasonModelContextWindowExceeded StopReason = "model_context_window_exceeded"`

        - `StopSequence string`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `Type Message`

          Object type.

          For Messages, this is always `"message"`.

          default: message

        - `Usage Usage`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `CacheCreation CacheCreation`

            Breakdown of cached tokens by TTL

            - `Ephemeral1hInputTokens int64`

              The number of input tokens used to create the 1 hour cache entry.

              default: 0, minimum: 0

            - `Ephemeral5mInputTokens int64`

              The number of input tokens used to create the 5 minute cache entry.

              default: 0, minimum: 0

          - `CacheCreationInputTokens int64`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `CacheReadInputTokens int64`

            The number of input tokens read from the cache.

            minimum: 0

          - `InferenceGeo string`

            The geographic region where inference was performed for this request.

          - `InputTokens int64`

            The number of input tokens which were used.

            minimum: 0

          - `OutputTokens int64`

            The number of output tokens which were used.

            minimum: 0

          - `OutputTokensDetails OutputTokensDetails`

            Breakdown of output tokens by category.

            `output_tokens` remains the inclusive, authoritative total used for billing.
            This object provides a read-only decomposition for observability — for example,
            how many of the billed output tokens were spent on internal reasoning that may
            have been summarized before being returned to you.

            - `ThinkingTokens int64`

              Number of output tokens the model generated as internal reasoning, including
              the thinking-block delimiter tokens.

              Reflects the raw reasoning the model produced, not the (possibly shorter)
              summarized thinking text returned in the response body. Computed by
              re-tokenizing the raw reasoning text, so it may differ from the model's exact
              generation count by a small number of tokens. Always ≤ `output_tokens`;
              `output_tokens - thinking_tokens` approximates the non-reasoning output.

              default: 0, minimum: 0

          - `ServerToolUse ServerToolUsage`

            The number of server tool requests.

            - `WebFetchRequests int64`

              The number of web fetch tool requests.

              default: 0, minimum: 0

            - `WebSearchRequests int64`

              The number of web search tool requests.

              default: 0, minimum: 0

          - `ServiceTier UsageServiceTier`

            If the request used the priority, standard, or batch tier.

            - `const UsageServiceTierStandard UsageServiceTier = "standard"`

            - `const UsageServiceTierPriority UsageServiceTier = "priority"`

            - `const UsageServiceTierBatch UsageServiceTier = "batch"`

      - `Type Succeeded`

        default: succeeded

    - `type MessageBatchErroredResult struct{…}`

      - `Error ErrorResponse`

        - `Error ErrorObjectUnion`

          - `type InvalidRequestError struct{…}`

            - `Message string`

              default: Invalid request

            - `Type InvalidRequestError`

              default: invalid_request_error

          - `type AuthenticationError struct{…}`

            - `Message string`

              default: Authentication error

            - `Type AuthenticationError`

              default: authentication_error

          - `type BillingError struct{…}`

            - `Message string`

              default: Billing error

            - `Type BillingError`

              default: billing_error

          - `type PermissionError struct{…}`

            - `Message string`

              default: Permission denied

            - `Type PermissionError`

              default: permission_error

          - `type NotFoundError struct{…}`

            - `Message string`

              default: Not found

            - `Type NotFoundError`

              default: not_found_error

          - `type RateLimitError struct{…}`

            - `Message string`

              default: Rate limited

            - `Type RateLimitError`

              default: rate_limit_error

          - `type GatewayTimeoutError struct{…}`

            - `Message string`

              default: Request timeout

            - `Type TimeoutError`

              default: timeout_error

          - `type APIErrorObject struct{…}`

            - `Message string`

              default: Internal server error

            - `Type APIError`

              default: api_error

          - `type OverloadedError struct{…}`

            - `Message string`

              default: Overloaded

            - `Type OverloadedError`

              default: overloaded_error

        - `RequestID string`

        - `Type Error`

          default: error

      - `Type Errored`

        default: errored

    - `type MessageBatchCanceledResult struct{…}`

      - `Type Canceled`

        default: canceled

    - `type MessageBatchExpiredResult struct{…}`

      - `Type Expired`

        default: expired

#### Example

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
	stream := client.Messages.Batches.ResultsStreaming(context.TODO(), "message_batch_id")
	for stream.Next() {
		fmt.Printf("%+v\n", stream.Current())
	}
	err := stream.Err()
	if err != nil {
		panic(err.Error())
	}
}
```
