<!-- source: https://platform.claude.com/docs/en/api/completions -->

# Completions
##### [Create a Text Completion](https://platform.claude.com/docs/en/api/completions/create)
POST/v1/complete
##### ModelsExpand Collapse 
Completion object { id, completion, model, 2 more } 
Unique object identifier.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/completions#completion.id)
completion: string
The resulting completion up to and excluding the stop sequences.
[](https://platform.claude.com/docs/en/api/completions#completion.completion)
model: [Model](https://platform.claude.com/docs/en/api/messages#model)
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more
The model that will complete your prompt.
See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.
"claude-fable-5"
Next generation of intelligence for the hardest knowledge work and coding problems
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B0%5D)
"claude-mythos-5"
Most capable model for cybersecurity and biology research
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B1%5D)
"claude-opus-4-8"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B2%5D)
"claude-opus-4-7"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B3%5D)
"claude-mythos-preview"
New class of intelligence, strongest in coding and cybersecurity
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B4%5D)
"claude-opus-4-6"
Frontier intelligence for long-running agents and coding
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B5%5D)
"claude-sonnet-4-6"
Best combination of speed and intelligence
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B6%5D)
"claude-haiku-4-5"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B7%5D)
"claude-haiku-4-5-20251001"
Fastest model with near-frontier intelligence
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B8%5D)
"claude-opus-4-5"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B9%5D)
"claude-opus-4-5-20251101"
Premium model combining maximum intelligence with practical performance
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B10%5D)
"claude-sonnet-4-5"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B11%5D)
"claude-sonnet-4-5-20250929"
High-performance model for agents and coding
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B12%5D)
"claude-opus-4-1"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B13%5D)
"claude-opus-4-1-20250805"
Exceptional model for specialized complex tasks
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D%5B14%5D)
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B0%5D)
string
[](https://platform.claude.com/docs/en/api/completions#completion.model%20%2B%20\(resource\)%20messages%5B1%5D)
[](https://platform.claude.com/docs/en/api/completions#completion.model)
stop_reason: string
The reason that we stopped.
This may be one the following values:
  * `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
  * `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

[](https://platform.claude.com/docs/en/api/completions#completion.stop_reason)
type: "completion"
Object type.
For Text Completions, this is always `"completion"`.
[](https://platform.claude.com/docs/en/api/completions#completion.type)
[](https://platform.claude.com/docs/en/api/completions#completion)
