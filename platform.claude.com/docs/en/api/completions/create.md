<!-- source: https://platform.claude.com/docs/en/api/completions/create -->

# Create a Text Completion
POST/v1/complete
[Legacy] Create a Text Completion.
The Text Completions API is a legacy API. We recommend using the [Messages API](https://docs.claude.com/en/api/messages) going forward.
Future models and features will not be compatible with Text Completions. See our [migration guide](https://docs.claude.com/en/api/migrating-from-text-completions-to-messages) for guidance in migrating from Text Completions to Messages.
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/completions/create#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/completions/create#create.betas)
#####  Body ParametersJSONExpand Collapse 
max_tokens_to_sample: number
The maximum number of tokens to generate before stopping.
Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.
minimum1
[](https://platform.claude.com/docs/en/api/completions/create#create.max_tokens_to_sample)
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/completions/create#create.model%5B1%5D)
[](https://platform.claude.com/docs/en/api/completions/create#create.model)
prompt: string
The prompt that you want Claude to complete.
For proper response generation you will need to format your prompt using alternating `
Human:`and`
Assistant:` conversational turns. For example:

"

Human: {userQuestion}

Assistant:"

See [prompt validation](https://docs.claude.com/en/api/prompt-validation) and our guide to [prompt design](https://docs.claude.com/en/docs/intro-to-prompting) for more details.
minLength1
[](https://platform.claude.com/docs/en/api/completions/create#create.prompt)
metadata: optional [Metadata](https://platform.claude.com/docs/en/api/messages#metadata) { user_id } 
An object describing metadata about the request.
user_id: optional string
An external identifier for the user who is associated with the request.
This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.
maxLength512
[](https://platform.claude.com/docs/en/api/completions/create#create.metadata.user_id)
[](https://platform.claude.com/docs/en/api/completions/create#create.metadata)
stop_sequences: optional array of string
Sequences that will cause the model to stop generating.
Our models stop on `"
Human:"`, and may include additional built-in stop sequences in the future. By providing the stop_sequences parameter, you may include additional strings that will cause the model to stop generating.
[](https://platform.claude.com/docs/en/api/completions/create#create.stop_sequences)
stream: optional boolean
Whether to incrementally stream the response using server-sent events.
See [streaming](https://docs.claude.com/en/api/streaming) for details.
[](https://platform.claude.com/docs/en/api/completions/create#create.stream)
Deprecatedtemperature: optional number
Amount of randomness injected into the response.
Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.
Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.
Note that even with `temperature` of `0.0`, the results will not be fully deterministic.
maximum1
minimum0
[](https://platform.claude.com/docs/en/api/completions/create#create.temperature)
Deprecatedtop_k: optional number
Only sample from the top K options for each subsequent token.
Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.
Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).
Recommended for advanced use cases only.
minimum0
[](https://platform.claude.com/docs/en/api/completions/create#create.top_k)
Deprecatedtop_p: optional number
Use nucleus sampling.
Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.
In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.
Recommended for advanced use cases only.
maximum1
minimum0
[](https://platform.claude.com/docs/en/api/completions/create#create.top_p)
Completion object { id, completion, model, 2 more } 
Unique object identifier.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/completions/create#completion.id)
completion: string
The resulting completion up to and excluding the stop sequences.
[](https://platform.claude.com/docs/en/api/completions/create#completion.completion)
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/completions/create#completion.model)
stop_reason: string
The reason that we stopped.
This may be one the following values:
  * `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
  * `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

[](https://platform.claude.com/docs/en/api/completions/create#completion.stop_reason)
type: "completion"
Object type.
For Text Completions, this is always `"completion"`.
[](https://platform.claude.com/docs/en/api/completions/create#completion.type)
[](https://platform.claude.com/docs/en/api/completions/create#completion)
Completion object { id, completion, model, 2 more } 
Unique object identifier.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/completions/create#completion.id)
completion: string
The resulting completion up to and excluding the stop sequences.
[](https://platform.claude.com/docs/en/api/completions/create#completion.completion)
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/completions/create#completion.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/completions/create#completion.model)
stop_reason: string
The reason that we stopped.
This may be one the following values:
  * `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
  * `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

[](https://platform.claude.com/docs/en/api/completions/create#completion.stop_reason)
type: "completion"
Object type.
For Text Completions, this is always `"completion"`.
[](https://platform.claude.com/docs/en/api/completions/create#completion.type)
[](https://platform.claude.com/docs/en/api/completions/create#completion)
Create a Text Completion
cURL

curl https://api.anthropic.com/v1/complete \
    -H 'Content-Type: application/json' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    --max-time 600 \
    -d '{
          "max_tokens_to_sample": 256,
          "model": "claude-2.1",
          "prompt": "\\n\\nHuman: Hello, world!\\n\\nAssistant:",
          "temperature": 1,
          "top_k": 5,
          "top_p": 0.7
        }'

  "id": "compl_018CKm6gsux7P8yMcwZbeCPw",
  "completion": " Hello! My name is Claude.",
  "model": "claude-2.1",
  "stop_reason": "stop_sequence",
  "type": "completion"

  "id": "compl_018CKm6gsux7P8yMcwZbeCPw",
  "completion": " Hello! My name is Claude.",
  "model": "claude-2.1",
  "stop_reason": "stop_sequence",
  "type": "completion"
