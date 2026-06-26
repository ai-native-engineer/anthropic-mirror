<!-- source: https://platform.claude.com/docs/en/api/beta/models/retrieve -->

# Get a Model
GET/v1/models/{model_id}
Get a specific model.
The Models API response can be used to determine information about a specific model or resolve a model alias to a model ID.
##### Path ParametersExpand Collapse 
model_id: string
Model identifier or alias.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#retrieve.model_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#retrieve.betas)
BetaModelInfo object { id, allowed_fallback_models, capabilities, 5 more } 
Unique model identifier.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.id)
allowed_fallback_models: array of string
Model IDs this model accepts as `fallbacks[i].model` on the Messages API. An empty list means the `fallbacks` parameter is not supported for this model as primary.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.allowed_fallback_models)
capabilities: [BetaModelCapabilities](https://platform.claude.com/docs/en/api/beta#beta_model_capabilities) { batch, citations, code_execution, 6 more } 
Model capability information.
batch: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Whether the model supports the Batch API.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.batch%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.capabilities%20%2B%20\(resource\)%20beta.models.batch)
citations: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Whether the model supports citation generation.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.citations%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.capabilities%20%2B%20\(resource\)%20beta.models.citations)
code_execution: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Whether the model supports code execution tools.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.code_execution%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.capabilities%20%2B%20\(resource\)%20beta.models.code_execution)
context_management: [BetaContextManagementCapability](https://platform.claude.com/docs/en/api/beta#beta_context_management_capability) { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported } 
Context management support and available strategies.
clear_thinking_20251015: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_context_management_capability.clear_thinking_20251015%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.context_management%20%2B%20\(resource\)%20beta.models.clear_thinking_20251015)
clear_tool_uses_20250919: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_context_management_capability.clear_tool_uses_20250919%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.context_management%20%2B%20\(resource\)%20beta.models.clear_tool_uses_20250919)
compact_20260112: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_context_management_capability.compact_20260112%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.context_management%20%2B%20\(resource\)%20beta.models.compact_20260112)
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.context_management%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.capabilities%20%2B%20\(resource\)%20beta.models.context_management)
effort: [BetaEffortCapability](https://platform.claude.com/docs/en/api/beta#beta_effort_capability) { high, low, max, 3 more } 
Effort (reasoning_effort) support and available levels.
high: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Whether the model supports high effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_effort_capability.high%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.effort%20%2B%20\(resource\)%20beta.models.high)
low: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Whether the model supports low effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_effort_capability.low%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.effort%20%2B%20\(resource\)%20beta.models.low)
max: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Whether the model supports max effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_effort_capability.max%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.effort%20%2B%20\(resource\)%20beta.models.max)
medium: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Whether the model supports medium effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_effort_capability.medium%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.effort%20%2B%20\(resource\)%20beta.models.medium)
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.effort%20%2B%20\(resource\)%20beta.models.supported)
xhigh: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_effort_capability.xhigh%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.effort%20%2B%20\(resource\)%20beta.models.xhigh)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.capabilities%20%2B%20\(resource\)%20beta.models.effort)
image_input: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Whether the model accepts image content blocks.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.image_input%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.capabilities%20%2B%20\(resource\)%20beta.models.image_input)
pdf_input: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Whether the model accepts PDF content blocks.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.pdf_input%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.capabilities%20%2B%20\(resource\)%20beta.models.pdf_input)
structured_outputs: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Whether the model supports structured output / JSON mode / strict tool schemas.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.structured_outputs%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.capabilities%20%2B%20\(resource\)%20beta.models.structured_outputs)
thinking: [BetaThinkingCapability](https://platform.claude.com/docs/en/api/beta#beta_thinking_capability) { supported, types } 
Thinking capability and supported type configurations.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.thinking%20%2B%20\(resource\)%20beta.models.supported)
types: [BetaThinkingTypes](https://platform.claude.com/docs/en/api/beta#beta_thinking_types) { adaptive, enabled } 
Supported thinking type configurations.
adaptive: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Whether the model supports thinking with type 'adaptive' (auto).
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_thinking_types.adaptive%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_thinking_capability.types%20%2B%20\(resource\)%20beta.models.adaptive)
enabled: [BetaCapabilitySupport](https://platform.claude.com/docs/en/api/beta#beta_capability_support) { supported } 
Whether the model supports thinking with type 'enabled'.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_thinking_types.enabled%20%2B%20\(resource\)%20beta.models.supported)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_thinking_capability.types%20%2B%20\(resource\)%20beta.models.enabled)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_capabilities.thinking%20%2B%20\(resource\)%20beta.models.types)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.capabilities%20%2B%20\(resource\)%20beta.models.thinking)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.capabilities)
created_at: string
RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.created_at)
display_name: string
A human-readable name for the model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.display_name)
max_input_tokens: number
Maximum input context window size in tokens for this model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.max_input_tokens)
max_tokens: number
Maximum value for the `max_tokens` parameter when using this model.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.max_tokens)
type: "model"
Object type.
For Models, this is always `"model"`.
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info.type)
[](https://platform.claude.com/docs/en/api/beta/models/retrieve#beta_model_info)
Get a Model
cURL

curl https://api.anthropic.com/v1/models/$MODEL_ID \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "id": "claude-opus-4-6",
  "allowed_fallback_models": [
    "string"
  ],
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

  "id": "claude-opus-4-6",
  "allowed_fallback_models": [
    "string"
  ],
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
