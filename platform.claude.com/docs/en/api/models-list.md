<!-- source: https://platform.claude.com/docs/en/api/models-list -->

# List Models
GET/v1/models
List available models.
The Models API response can be used to determine which models are available for use in the API. More recently released models are listed first.
##### Query ParametersExpand Collapse 
after_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.
[](https://platform.claude.com/docs/en/api/models/list#list.after_id)
before_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.
[](https://platform.claude.com/docs/en/api/models/list#list.before_id)
limit: optional number
Number of items to return per page.
Defaults to `20`. Ranges from `1` to `1000`.
maximum1000
minimum1
[](https://platform.claude.com/docs/en/api/models/list#list.limit)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/models/list#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/models/list#list.betas)
data: array of [ModelInfo](https://platform.claude.com/docs/en/api/models#model_info) { id, capabilities, created_at, 4 more } 
Unique model identifier.
[](https://platform.claude.com/docs/en/api/models/list#model_info.id)
capabilities: [ModelCapabilities](https://platform.claude.com/docs/en/api/models#model_capabilities) { batch, citations, code_execution, 6 more } 
Model capability information.
batch: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports the Batch API.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.batch%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_info.capabilities%20%2B%20\(resource\)%20models.batch)
citations: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports citation generation.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.citations%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_info.capabilities%20%2B%20\(resource\)%20models.citations)
code_execution: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports code execution tools.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.code_execution%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_info.capabilities%20%2B%20\(resource\)%20models.code_execution)
context_management: [ContextManagementCapability](https://platform.claude.com/docs/en/api/models#context_management_capability) { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported } 
Context management support and available strategies.
clear_thinking_20251015: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#context_management_capability.clear_thinking_20251015%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.context_management%20%2B%20\(resource\)%20models.clear_thinking_20251015)
clear_tool_uses_20250919: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#context_management_capability.clear_tool_uses_20250919%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.context_management%20%2B%20\(resource\)%20models.clear_tool_uses_20250919)
compact_20260112: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#context_management_capability.compact_20260112%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.context_management%20%2B%20\(resource\)%20models.compact_20260112)
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.context_management%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_info.capabilities%20%2B%20\(resource\)%20models.context_management)
effort: [EffortCapability](https://platform.claude.com/docs/en/api/models#effort_capability) { high, low, max, 3 more } 
Effort (reasoning_effort) support and available levels.
high: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports high effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#effort_capability.high%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.effort%20%2B%20\(resource\)%20models.high)
low: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports low effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#effort_capability.low%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.effort%20%2B%20\(resource\)%20models.low)
max: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports max effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#effort_capability.max%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.effort%20%2B%20\(resource\)%20models.max)
medium: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports medium effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#effort_capability.medium%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.effort%20%2B%20\(resource\)%20models.medium)
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.effort%20%2B%20\(resource\)%20models.supported)
xhigh: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#effort_capability.xhigh%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.effort%20%2B%20\(resource\)%20models.xhigh)
[](https://platform.claude.com/docs/en/api/models/list#model_info.capabilities%20%2B%20\(resource\)%20models.effort)
image_input: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model accepts image content blocks.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.image_input%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_info.capabilities%20%2B%20\(resource\)%20models.image_input)
pdf_input: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model accepts PDF content blocks.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.pdf_input%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_info.capabilities%20%2B%20\(resource\)%20models.pdf_input)
structured_outputs: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports structured output / JSON mode / strict tool schemas.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.structured_outputs%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#model_info.capabilities%20%2B%20\(resource\)%20models.structured_outputs)
thinking: [ThinkingCapability](https://platform.claude.com/docs/en/api/models#thinking_capability) { supported, types } 
Thinking capability and supported type configurations.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.thinking%20%2B%20\(resource\)%20models.supported)
types: [ThinkingTypes](https://platform.claude.com/docs/en/api/models#thinking_types) { adaptive, enabled } 
Supported thinking type configurations.
adaptive: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports thinking with type 'adaptive' (auto).
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#thinking_types.adaptive%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#thinking_capability.types%20%2B%20\(resource\)%20models.adaptive)
enabled: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports thinking with type 'enabled'.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models/list#thinking_types.enabled%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models/list#thinking_capability.types%20%2B%20\(resource\)%20models.enabled)
[](https://platform.claude.com/docs/en/api/models/list#model_capabilities.thinking%20%2B%20\(resource\)%20models.types)
[](https://platform.claude.com/docs/en/api/models/list#model_info.capabilities%20%2B%20\(resource\)%20models.thinking)
[](https://platform.claude.com/docs/en/api/models/list#model_info.capabilities)
created_at: string
RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.
[](https://platform.claude.com/docs/en/api/models/list#model_info.created_at)
display_name: string
A human-readable name for the model.
[](https://platform.claude.com/docs/en/api/models/list#model_info.display_name)
max_input_tokens: number
Maximum input context window size in tokens for this model.
[](https://platform.claude.com/docs/en/api/models/list#model_info.max_input_tokens)
max_tokens: number
Maximum value for the `max_tokens` parameter when using this model.
[](https://platform.claude.com/docs/en/api/models/list#model_info.max_tokens)
type: "model"
Object type.
For Models, this is always `"model"`.
[](https://platform.claude.com/docs/en/api/models/list#model_info.type)
[](https://platform.claude.com/docs/en/api/models/list#list)
first_id: string
First ID in the `data` list. Can be used as the `before_id` for the previous page.
[](https://platform.claude.com/docs/en/api/models/list#list)
has_more: boolean
Indicates if there are more results in the requested page direction.
[](https://platform.claude.com/docs/en/api/models/list#list)
last_id: string
Last ID in the `data` list. Can be used as the `after_id` for the next page.
[](https://platform.claude.com/docs/en/api/models/list#list)
List Models
cURL

curl https://api.anthropic.com/v1/models \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "data": [
      "id": "claude-opus-4-6",
      "capabilities": {
        "batch": {
          "supported": true
        "citations": {
          "supported": true
        "code_execution": {
          "supported": true
        "context_management": {
          "clear_thinking_20251015": {
            "supported": true
          "clear_tool_uses_20250919": {
            "supported": true
          "compact_20260112": {
            "supported": true
          "supported": true
        "effort": {
          "high": {
            "supported": true
          "low": {
            "supported": true
          "max": {
            "supported": true
          "medium": {
            "supported": true
          "supported": true,
          "xhigh": {
            "supported": true
        "image_input": {
          "supported": true
        "pdf_input": {
          "supported": true
        "structured_outputs": {
          "supported": true
        "thinking": {
          "supported": true,
          "types": {
            "adaptive": {
              "supported": true
            "enabled": {
              "supported": true
      "created_at": "2026-02-04T00:00:00Z",
      "display_name": "Claude Opus 4.6",
      "max_input_tokens": 0,
      "max_tokens": 0,
      "type": "model"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"

  "data": [
      "id": "claude-opus-4-6",
      "capabilities": {
        "batch": {
          "supported": true
        "citations": {
          "supported": true
        "code_execution": {
          "supported": true
        "context_management": {
          "clear_thinking_20251015": {
            "supported": true
          "clear_tool_uses_20250919": {
            "supported": true
          "compact_20260112": {
            "supported": true
          "supported": true
        "effort": {
          "high": {
            "supported": true
          "low": {
            "supported": true
          "max": {
            "supported": true
          "medium": {
            "supported": true
          "supported": true,
          "xhigh": {
            "supported": true
        "image_input": {
          "supported": true
        "pdf_input": {
          "supported": true
        "structured_outputs": {
          "supported": true
        "thinking": {
          "supported": true,
          "types": {
            "adaptive": {
              "supported": true
            "enabled": {
              "supported": true
      "created_at": "2026-02-04T00:00:00Z",
      "display_name": "Claude Opus 4.6",
      "max_input_tokens": 0,
      "max_tokens": 0,
      "type": "model"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
