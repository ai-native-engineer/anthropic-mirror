<!-- source: https://platform.claude.com/docs/en/api/cli/beta/messages -->
<!-- part of: https://platform.claude.com/docs/en/api/cli/beta/messages -->

<!-- chunk-start -->

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

      - `iterations: array of BetaMessageIterationUsage or BetaCompactionIterationUsage or BetaAdvisorMessageIterationUsage or BetaFallbackMessageIterationUsage`

        Per-iteration token usage breakdown.

        Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

        - Determine which iterations exceeded long context thresholds (>=200k tokens)
        - Calculate the true context window size from the last iteration
        - Understand token accumulation across server-side tool use loops

        - `beta_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

          Token usage for a sampling iteration.

          - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

          - `cache_creation_input_tokens: number`

            The number of input tokens used to create the cache entry.

          - `cache_read_input_tokens: number`

            The number of input tokens read from the cache.

          - `input_tokens: number`

            The number of input tokens which were used.

          - `model: "claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 12 more or string`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `type: "message"`

            Usage for a sampling iteration

        - `beta_compaction_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 3 more }`

          Token usage for a compaction iteration.

          - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

          - `cache_creation_input_tokens: number`

            The number of input tokens used to create the cache entry.

          - `cache_read_input_tokens: number`

            The number of input tokens read from the cache.

          - `input_tokens: number`

            The number of input tokens which were used.

          - `output_tokens: number`

            The number of output tokens which were used.

          - `type: "compaction"`

            Usage for a compaction iteration

        - `beta_advisor_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

          Token usage for an advisor sub-inference iteration.

          - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

          - `cache_creation_input_tokens: number`

            The number of input tokens used to create the cache entry.

          - `cache_read_input_tokens: number`

            The number of input tokens read from the cache.

          - `input_tokens: number`

            The number of input tokens which were used.

          - `model: "claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 12 more or string`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `type: "advisor_message"`

            Usage for an advisor sub-inference iteration

        - `beta_fallback_message_iteration_usage: object { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 4 more }`

          Token usage for the fallback-model attempt of a server-side fallback request.

          Produced in place of a `message` entry for whichever hop served the
          response. A declined hop produces the existing `message` entry. Whether
          a fallback model served the response is signalled by the presence of this
          entry in `usage.iterations`.

          - `cache_creation: object { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }`

            Breakdown of cached tokens by TTL

            - `ephemeral_1h_input_tokens: number`

              The number of input tokens used to create the 1 hour cache entry.

            - `ephemeral_5m_input_tokens: number`

              The number of input tokens used to create the 5 minute cache entry.

          - `cache_creation_input_tokens: number`

            The number of input tokens used to create the cache entry.

          - `cache_read_input_tokens: number`

            The number of input tokens read from the cache.

          - `input_tokens: number`

            The number of input tokens which were used.

          - `model: "claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 12 more or string`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `type: "fallback_message"`

            Usage for the fallback-model attempt that served the response

      - `output_tokens: number`

        The number of output tokens which were used.

      - `output_tokens_details: object { thinking_tokens }`

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

      - `server_tool_use: object { web_fetch_requests, web_search_requests }`

        The number of server tool requests.

        - `web_fetch_requests: number`

          The number of web fetch tool requests.

        - `web_search_requests: number`

          The number of web search tool requests.

      - `service_tier: "standard" or "priority" or "batch"`

        If the request used the priority, standard, or batch tier.

        - `"standard"`

        - `"priority"`

        - `"batch"`

      - `speed: "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `type: "succeeded"`
