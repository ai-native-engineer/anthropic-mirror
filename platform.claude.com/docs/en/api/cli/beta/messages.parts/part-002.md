<!-- source: https://platform.claude.com/docs/en/api/cli/beta/messages -->
<!-- part of: https://platform.claude.com/docs/en/api/cli/beta/messages -->

<!-- chunk-start -->
            prefix is permitted but yields no additional credit.

            `null` when the refused model isn't eligible for a fallback credit.

          - `fallback_has_prefill_claim: boolean`

            Whether the accompanying `fallback_credit_token` may be redeemed with the
            appended-assistant retry form. Only set when `fallback_credit_token` is
            present.

            `true`: retry by resending the same request body plus one appended
            `assistant` message whose content is this response's `content` with any
            trailing whitespace stripped from the final text block and unpaired
            `tool_use` blocks omitted (the same appended-turn shape described on
            `fallback_credit_token`), with the token attached. `false`: retry by
            resending the original request body unchanged, with the token attached —
            the appended-assistant form is not available for this refusal (no
            continuable partial content, or the request uses `output_format` or a
            `tool_choice` that forces tool use). One exception: when the request used
            `output_format` or a forced `tool_choice` and the refusal arrived after
            server tools (including MCP connector tools) had already executed, the
            token may not be redeemable by either retry form; if the exact-body retry
            is then rejected with a 400 saying the token must be redeemed by
            continuing the partial response, discard the token and retry without it.

            Advisory: if an appended-assistant retry is rejected with a 400 despite
            `true`, fall back to resending the original request body with the token.

          - `recommended_model: string`

            The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

          - `type: "refusal"`

        - `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 5 more`

          The reason that we stopped.

          This may be one the following values:

          * `"end_turn"`: the model reached a natural stopping point
          * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
          * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
          * `"tool_use"`: the model invoked one or more tools
          * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
          * `"refusal"`: when streaming classifiers intervene to handle potential policy violations
          * `"model_context_window_exceeded"`: we exceeded the model's context window

          In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

          - `"end_turn"`

          - `"max_tokens"`

          - `"stop_sequence"`

          - `"tool_use"`

          - `"pause_turn"`

          - `"compaction"`

          - `"refusal"`

          - `"model_context_window_exceeded"`

        - `stop_sequence: string`

          Which custom stop sequence was generated, if any.

          This value will be a non-null string if one of your custom stop sequences was generated.

        - `type: "message"`

          Object type.

          For Messages, this is always `"message"`.

        - `usage: object`

          Billing and rate-limit usage.

          Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

          Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

          For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

          Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

          - `cache_creation: object`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

              minimum: 0

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

              minimum: 0

          - `cache_creation_input_tokens: number`

            The number of input tokens used to create the cache entry.

            minimum: 0

          - `cache_read_input_tokens: number`

            The number of input tokens read from the cache.

            minimum: 0

          - `fallback_credit: object`

            Outcome of the `fallback_credit_token` presented on this request.

            - `status: BetaFallbackCreditRedeemed or BetaFallbackCreditNotApplied`

              Whether the fallback-credit reprice was applied to this response's billing.

              A union discriminated on `type`. `redeemed`: the retry is billed as if
              the conversation had been on the retry model all along — including when the
              resulting shift is zero because there was nothing to move. `not_applied`:
              no reprice was applied; the arm's `reason` says why.

              - `beta_fallback_credit_redeemed: object`

                The reprice was applied: the retry is billed as if the conversation
                had been on the retry model all along.

                - `type: "redeemed"`

              - `beta_fallback_credit_not_applied: object`

                No reprice was applied; `reason` says why.

                - `reason: "body_mismatch" or "continuation_excluded" or "continuation_only" or 9 more`

                  Why the reprice was not applied.

                  A closed enum; additions to the redemption-check vocabulary arrive as
                  deliberate schema updates.

                  - `"body_mismatch"`

                  - `"continuation_excluded"`

                  - `"continuation_only"`

                  - `"expired"`

                  - `"invalid_target_model"`

                  - `"not_enabled"`

                  - `"reprice_unavailable"`

                  - `"temporarily_unavailable"`

                  - `"variant_fields_present"`

                  - `"wrong_organization"`

                  - `"wrong_platform"`

                  - `"wrong_workspace"`

                - `type: "not_applied"`

                - `remove_to_redeem: optional array of string`

                  Request fields to remove before retrying, so the retry can redeem this
                  token.

                  Present exactly when `reason` is `variant_fields_present` — never null,
                  never an empty array; absent otherwise. Fields are named only from your own request, and only after
                  the sealed variant hash matched. A served best-effort retry has already
                  been billed at normal price; nothing redeems retroactively, but a corrected
                  re-send inside the token's five-minute window can still redeem.

          - `inference_geo: string`

            The geographic region where inference was performed for this request.

          - `input_tokens: number`

            The number of input tokens which were used.

            minimum: 0

          - `iterations: array of BetaMessageIterationUsage or BetaCompactionIterationUsage or BetaAdvisorMessageIterationUsage or BetaFallbackMessageIterationUsage`

            Per-iteration token usage breakdown.

            Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

            - Determine which iterations exceeded long context thresholds (>=200k tokens)
            - Calculate the context window size from the last `message` entry
            - Understand token accumulation across server-side tool use loops

            A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

            - `beta_message_iteration_usage: object`

              Token usage for a sampling iteration.

              - `cache_creation: object`

                Breakdown of cached tokens by TTL

                - `ephemeral_1h_input_tokens: number`

                  The number of input tokens used to create the 1 hour cache entry.

                  minimum: 0

                - `ephemeral_5m_input_tokens: number`

                  The number of input tokens used to create the 5 minute cache entry.

                  minimum: 0

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

                minimum: 0

              - `input_tokens: number`

                The number of input tokens which were used.

                minimum: 0

              - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `"claude-fable-5-1"`

                  Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

                - `"claude-mythos-5-1"`

                  Our most capable model for cybersecurity and biology research, available through trusted access programs

                - `"claude-sonnet-5"`

                  High-performance model for coding and agents

                - `"claude-fable-5"`

                  Next generation of intelligence for the hardest knowledge work and coding problems

                - `"claude-mythos-5"`

                  Most capable model for cybersecurity and biology research

                - `"claude-opus-5"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-opus-4-8"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-opus-4-7"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-mythos-preview"`

                  New class of intelligence, strongest in coding and cybersecurity

                - `"claude-opus-4-6"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-sonnet-4-6"`

                  Best combination of speed and intelligence

                - `"claude-haiku-4-5"`

                  Fastest model with near-frontier intelligence

                - `"claude-haiku-4-5-20251001"`

                  Fastest model with near-frontier intelligence

                - `"claude-opus-4-5"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-opus-4-5-20251101"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-sonnet-4-5"`

                  High-performance model for agents and coding

                - `"claude-sonnet-4-5-20250929"`

                  High-performance model for agents and coding

              - `output_tokens: number`

                The number of output tokens which were used.

                minimum: 0

              - `type: "message"`

                Usage for a sampling iteration

            - `beta_compaction_iteration_usage: object`

              Token usage for a compaction iteration.

              - `cache_creation: object`

                Breakdown of cached tokens by TTL

                - `ephemeral_1h_input_tokens: number`

                  The number of input tokens used to create the 1 hour cache entry.

                  minimum: 0

                - `ephemeral_5m_input_tokens: number`

                  The number of input tokens used to create the 5 minute cache entry.

                  minimum: 0

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

                minimum: 0

              - `input_tokens: number`

                The number of input tokens which were used.

                minimum: 0

              - `output_tokens: number`

                The number of output tokens which were used.

                minimum: 0

              - `type: "compaction"`

                Usage for a compaction iteration

            - `beta_advisor_message_iteration_usage: object`

              Token usage for an advisor sub-inference iteration.

              - `cache_creation: object`

                Breakdown of cached tokens by TTL

                - `ephemeral_1h_input_tokens: number`

                  The number of input tokens used to create the 1 hour cache entry.

                  minimum: 0

                - `ephemeral_5m_input_tokens: number`

                  The number of input tokens used to create the 5 minute cache entry.

                  minimum: 0

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

                minimum: 0

              - `input_tokens: number`

                The number of input tokens which were used.

                minimum: 0

              - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `"claude-fable-5-1"`

                  Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

                - `"claude-mythos-5-1"`

                  Our most capable model for cybersecurity and biology research, available through trusted access programs

                - `"claude-sonnet-5"`

                  High-performance model for coding and agents

                - `"claude-fable-5"`

                  Next generation of intelligence for the hardest knowledge work and coding problems

                - `"claude-mythos-5"`

                  Most capable model for cybersecurity and biology research

                - `"claude-opus-5"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-opus-4-8"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-opus-4-7"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-mythos-preview"`

                  New class of intelligence, strongest in coding and cybersecurity

                - `"claude-opus-4-6"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-sonnet-4-6"`

                  Best combination of speed and intelligence

                - `"claude-haiku-4-5"`

                  Fastest model with near-frontier intelligence

                - `"claude-haiku-4-5-20251001"`

                  Fastest model with near-frontier intelligence

                - `"claude-opus-4-5"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-opus-4-5-20251101"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-sonnet-4-5"`

                  High-performance model for agents and coding

                - `"claude-sonnet-4-5-20250929"`

                  High-performance model for agents and coding

              - `output_tokens: number`

                The number of output tokens which were used.

                minimum: 0

              - `type: "advisor_message"`

                Usage for an advisor sub-inference iteration

            - `beta_fallback_message_iteration_usage: object`

              Token usage for the fallback-model attempt of a server-side fallback request.

              Produced in place of a `message` entry for whichever hop served the
              response. A declined hop produces the existing `message` entry. Whether
              a fallback model served the response is signalled by the presence of this
              entry in `usage.iterations`.

              - `cache_creation: object`

                Breakdown of cached tokens by TTL

                - `ephemeral_1h_input_tokens: number`

                  The number of input tokens used to create the 1 hour cache entry.

                  minimum: 0

                - `ephemeral_5m_input_tokens: number`

                  The number of input tokens used to create the 5 minute cache entry.

                  minimum: 0

              - `cache_creation_input_tokens: number`

                The number of input tokens used to create the cache entry.

                minimum: 0

              - `cache_read_input_tokens: number`

                The number of input tokens read from the cache.

                minimum: 0

              - `input_tokens: number`

                The number of input tokens which were used.

                minimum: 0

              - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

                The model that will complete your prompt.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `"claude-fable-5-1"`

                  Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

                - `"claude-mythos-5-1"`

                  Our most capable model for cybersecurity and biology research, available through trusted access programs

                - `"claude-sonnet-5"`

                  High-performance model for coding and agents

                - `"claude-fable-5"`

                  Next generation of intelligence for the hardest knowledge work and coding problems

                - `"claude-mythos-5"`

                  Most capable model for cybersecurity and biology research

                - `"claude-opus-5"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-opus-4-8"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-opus-4-7"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-mythos-preview"`

                  New class of intelligence, strongest in coding and cybersecurity

                - `"claude-opus-4-6"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-sonnet-4-6"`

                  Best combination of speed and intelligence

                - `"claude-haiku-4-5"`

                  Fastest model with near-frontier intelligence

                - `"claude-haiku-4-5-20251001"`

                  Fastest model with near-frontier intelligence

                - `"claude-opus-4-5"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-opus-4-5-20251101"`

                  Powerful intelligence for long-running agents and coding

                - `"claude-sonnet-4-5"`

                  High-performance model for agents and coding

                - `"claude-sonnet-4-5-20250929"`

                  High-performance model for agents and coding

              - `output_tokens: number`

                The number of output tokens which were used.

                minimum: 0

              - `type: "fallback_message"`

                Usage for the fallback-model attempt that served the response

          - `output_tokens: number`

            The number of output tokens which were used.

            minimum: 0

          - `output_tokens_details: object`

            Breakdown of output tokens by category.

            `output_tokens` remains the inclusive, authoritative total used for billing.
            This object provides a read-only decomposition for observability — for example,
            how many of the billed output tokens were spent on internal reasoning that may
            have been summarized before being returned to you.

            - `thinking_tokens: number`

              Number of output tokens the model generated as internal reasoning, including
              the thinking-block delimiter tokens.

              Reflects the raw reasoning the model produced, not the (possibly shorter)
              summarized thinking text returned in the response body. Computed by
              re-tokenizing the raw reasoning text, so it may differ from the model's exact
              generation count by a small number of tokens. Always ≤ `output_tokens`;
              `output_tokens - thinking_tokens` approximates the non-reasoning output.

              minimum: 0

          - `server_tool_use: object`

            The number of server tool requests.

            - `web_fetch_requests: number`

              The number of web fetch tool requests.

              minimum: 0

            - `web_search_requests: number`

              The number of web search tool requests.

              minimum: 0

          - `service_tier: "standard" or "priority" or "batch"`

            If the request used the priority, standard, or batch tier.

            - `"standard"`

            - `"priority"`

            - `"batch"`

          - `speed: "standard" or "fast"`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `"standard"`

            - `"fast"`

        - `input_transformations: optional array of BetaThinkingDroppedInputTransformation`

          Changes the API made to the request's input before showing it to the model:
          one entry per change, in request order. Today the only entry type is
          `thinking_dropped` — a `thinking`, `redacted_thinking` or `connector_text`
          block from the request's `messages` that was removed from the prompt instead
          of being shown to the model because it failed a binding check. More entry
          types may be added over time; ignore types you do not recognize.

          Requires `anthropic-beta: thinking-binding-controls-2026-08-01`. Present on
          every such response from a model that supports extended thinking, as `[]`
          when nothing was changed; without the beta, blocks are removed all the same
          but nothing is reported. Removed blocks contribute nothing to
          `usage.input_tokens`. When streaming, the array is final in `message_start`;
          the final `message_delta` event carries it only when a server-side model
          fallback happened mid-stream, in which case it holds the serving model's
          entries and replaces the one in `message_start`.

          - `path: string`

            Where the removed block was in your request, as `messages.{i}.content.{j}`:
            `i` indexes the `messages` array you sent and `j` that message's `content`
            array — the same form error messages use.

          - `reason: "model_binding_mismatch" or "prefix_binding_mismatch" or "organization_binding_mismatch" or "end_user_binding_mismatch"`

            Which binding check removed the block: `model_binding_mismatch` — it was
            created by a model whose reasoning the requested model may not read;
            `prefix_binding_mismatch` — the conversation before it differs from the
            conversation it was created in (the rest of that turn's consecutive thinking
            blocks are removed with it, each with this reason);
            `organization_binding_mismatch` — it was created under a different
            organization (an Anthropic organization, AWS account or Google Cloud project)
            and this organization is not one of its additional organizations;
            `end_user_binding_mismatch` — it was created for a different end user, or
            was removed by the consumer-organization binding. A block that would fail
            several checks reports one reason, in this order of precedence:
            `organization_binding_mismatch`, `end_user_binding_mismatch`,
            `model_binding_mismatch`, `prefix_binding_mismatch`.

            - `"model_binding_mismatch"`

            - `"prefix_binding_mismatch"`

            - `"organization_binding_mismatch"`

            - `"end_user_binding_mismatch"`

          - `type: "thinking_dropped"`

            Always `thinking_dropped` for this entry type.

      - `type: "succeeded"`

    - `beta_message_batch_errored_result: object`

      - `error: object`

        - `error: BetaInvalidRequestError or BetaAuthenticationError or BetaBillingError or 6 more`

          - `beta_invalid_request_error: object`

            - `message: string`

            - `type: "invalid_request_error"`

          - `beta_authentication_error: object`

            - `message: string`

            - `type: "authentication_error"`

          - `beta_billing_error: object`

            - `message: string`

            - `type: "billing_error"`

          - `beta_permission_error: object`

            - `message: string`

            - `type: "permission_error"`

          - `beta_not_found_error: object`

            - `message: string`

            - `type: "not_found_error"`

          - `beta_rate_limit_error: object`

            - `message: string`

            - `type: "rate_limit_error"`

          - `beta_gateway_timeout_error: object`

            - `message: string`

            - `type: "timeout_error"`

          - `beta_api_error: object`

            - `message: string`

            - `type: "api_error"`

          - `beta_overloaded_error: object`

            - `message: string`

            - `type: "overloaded_error"`

        - `request_id: string`

        - `type: "error"`

      - `type: "errored"`

    - `beta_message_batch_canceled_result: object`

      - `type: "canceled"`

    - `beta_message_batch_expired_result: object`

      - `type: "expired"`

#### Example

```bash
ant beta:messages:batches results \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```
