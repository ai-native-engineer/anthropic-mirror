<!-- source: https://platform.claude.com/docs/en/api/models -->

# Models
##### [List Models](https://platform.claude.com/docs/en/api/models/list)
GET/v1/models
##### [Get a Model](https://platform.claude.com/docs/en/api/models/retrieve)
GET/v1/models/{model_id}
##### ModelsExpand Collapse 
CapabilitySupport object { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#capability_support.supported)
[](https://platform.claude.com/docs/en/api/models#capability_support)
ContextManagementCapability object { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported } 
Context management capability details.
clear_thinking_20251015: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#context_management_capability.clear_thinking_20251015%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#context_management_capability.clear_thinking_20251015)
clear_tool_uses_20250919: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#context_management_capability.clear_tool_uses_20250919%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#context_management_capability.clear_tool_uses_20250919)
compact_20260112: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#context_management_capability.compact_20260112%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#context_management_capability.compact_20260112)
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#context_management_capability.supported)
[](https://platform.claude.com/docs/en/api/models#context_management_capability)
EffortCapability object { high, low, max, 3 more } 
Effort (reasoning_effort) capability details.
high: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports high effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.high%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#effort_capability.high)
low: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports low effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.low%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#effort_capability.low)
max: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports max effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.max%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#effort_capability.max)
medium: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports medium effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.medium%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#effort_capability.medium)
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.supported)
xhigh: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.xhigh%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#effort_capability.xhigh)
[](https://platform.claude.com/docs/en/api/models#effort_capability)
ModelCapabilities object { batch, citations, code_execution, 6 more } 
Model capability information.
batch: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports the Batch API.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.batch%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.batch)
citations: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports citation generation.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.citations%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.citations)
code_execution: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports code execution tools.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.code_execution%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.code_execution)
context_management: [ContextManagementCapability](https://platform.claude.com/docs/en/api/models#context_management_capability) { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported } 
Context management support and available strategies.
clear_thinking_20251015: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#context_management_capability.clear_thinking_20251015%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.context_management%20%2B%20\(resource\)%20models.clear_thinking_20251015)
clear_tool_uses_20250919: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#context_management_capability.clear_tool_uses_20250919%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.context_management%20%2B%20\(resource\)%20models.clear_tool_uses_20250919)
compact_20260112: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#context_management_capability.compact_20260112%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.context_management%20%2B%20\(resource\)%20models.compact_20260112)
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.context_management%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.context_management)
effort: [EffortCapability](https://platform.claude.com/docs/en/api/models#effort_capability) { high, low, max, 3 more } 
Effort (reasoning_effort) support and available levels.
high: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports high effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.high%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.effort%20%2B%20\(resource\)%20models.high)
low: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports low effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.low%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.effort%20%2B%20\(resource\)%20models.low)
max: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports max effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.max%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.effort%20%2B%20\(resource\)%20models.max)
medium: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports medium effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.medium%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.effort%20%2B%20\(resource\)%20models.medium)
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.effort%20%2B%20\(resource\)%20models.supported)
xhigh: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.xhigh%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.effort%20%2B%20\(resource\)%20models.xhigh)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.effort)
image_input: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model accepts image content blocks.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.image_input%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.image_input)
pdf_input: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model accepts PDF content blocks.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.pdf_input%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.pdf_input)
structured_outputs: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports structured output / JSON mode / strict tool schemas.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.structured_outputs%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.structured_outputs)
thinking: [ThinkingCapability](https://platform.claude.com/docs/en/api/models#thinking_capability) { supported, types } 
Thinking capability and supported type configurations.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.thinking%20%2B%20\(resource\)%20models.supported)
types: [ThinkingTypes](https://platform.claude.com/docs/en/api/models#thinking_types) { adaptive, enabled } 
Supported thinking type configurations.
adaptive: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports thinking with type 'adaptive' (auto).
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#thinking_types.adaptive%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#thinking_capability.types%20%2B%20\(resource\)%20models.adaptive)
enabled: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports thinking with type 'enabled'.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#thinking_types.enabled%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#thinking_capability.types%20%2B%20\(resource\)%20models.enabled)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.thinking%20%2B%20\(resource\)%20models.types)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.thinking)
[](https://platform.claude.com/docs/en/api/models#model_capabilities)
ModelInfo object { id, capabilities, created_at, 4 more } 
Unique model identifier.
[](https://platform.claude.com/docs/en/api/models#model_info.id)
capabilities: [ModelCapabilities](https://platform.claude.com/docs/en/api/models#model_capabilities) { batch, citations, code_execution, 6 more } 
Model capability information.
batch: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports the Batch API.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.batch%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_info.capabilities%20%2B%20\(resource\)%20models.batch)
citations: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports citation generation.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.citations%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_info.capabilities%20%2B%20\(resource\)%20models.citations)
code_execution: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports code execution tools.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.code_execution%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_info.capabilities%20%2B%20\(resource\)%20models.code_execution)
context_management: [ContextManagementCapability](https://platform.claude.com/docs/en/api/models#context_management_capability) { clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported } 
Context management support and available strategies.
clear_thinking_20251015: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#context_management_capability.clear_thinking_20251015%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.context_management%20%2B%20\(resource\)%20models.clear_thinking_20251015)
clear_tool_uses_20250919: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#context_management_capability.clear_tool_uses_20250919%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.context_management%20%2B%20\(resource\)%20models.clear_tool_uses_20250919)
compact_20260112: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#context_management_capability.compact_20260112%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.context_management%20%2B%20\(resource\)%20models.compact_20260112)
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.context_management%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_info.capabilities%20%2B%20\(resource\)%20models.context_management)
effort: [EffortCapability](https://platform.claude.com/docs/en/api/models#effort_capability) { high, low, max, 3 more } 
Effort (reasoning_effort) support and available levels.
high: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports high effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.high%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.effort%20%2B%20\(resource\)%20models.high)
low: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports low effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.low%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.effort%20%2B%20\(resource\)%20models.low)
max: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports max effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.max%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.effort%20%2B%20\(resource\)%20models.max)
medium: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports medium effort level.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.medium%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.effort%20%2B%20\(resource\)%20models.medium)
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.effort%20%2B%20\(resource\)%20models.supported)
xhigh: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Indicates whether a capability is supported.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#effort_capability.xhigh%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.effort%20%2B%20\(resource\)%20models.xhigh)
[](https://platform.claude.com/docs/en/api/models#model_info.capabilities%20%2B%20\(resource\)%20models.effort)
image_input: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model accepts image content blocks.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.image_input%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_info.capabilities%20%2B%20\(resource\)%20models.image_input)
pdf_input: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model accepts PDF content blocks.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.pdf_input%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_info.capabilities%20%2B%20\(resource\)%20models.pdf_input)
structured_outputs: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports structured output / JSON mode / strict tool schemas.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.structured_outputs%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#model_info.capabilities%20%2B%20\(resource\)%20models.structured_outputs)
thinking: [ThinkingCapability](https://platform.claude.com/docs/en/api/models#thinking_capability) { supported, types } 
Thinking capability and supported type configurations.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#model_capabilities.thinking%20%2B%20\(resource\)%20models.supported)
types: [ThinkingTypes](https://platform.claude.com/docs/en/api/models#thinking_types) { adaptive, enabled } 
Supported thinking type configurations.
adaptive: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports thinking with type 'adaptive' (auto).
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#thinking_types.adaptive%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#thinking_capability.types%20%2B%20\(resource\)%20models.adaptive)
enabled: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports thinking with type 'enabled'.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#thinking_types.enabled%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#thinking_capability.types%20%2B%20\(resource\)%20models.enabled)
[](https://platform.claude.com/docs/en/api/models#model_capabilities.thinking%20%2B%20\(resource\)%20models.types)
[](https://platform.claude.com/docs/en/api/models#model_info.capabilities%20%2B%20\(resource\)%20models.thinking)
[](https://platform.claude.com/docs/en/api/models#model_info.capabilities)
created_at: string
RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.
[](https://platform.claude.com/docs/en/api/models#model_info.created_at)
display_name: string
A human-readable name for the model.
[](https://platform.claude.com/docs/en/api/models#model_info.display_name)
max_input_tokens: number
Maximum input context window size in tokens for this model.
[](https://platform.claude.com/docs/en/api/models#model_info.max_input_tokens)
max_tokens: number
Maximum value for the `max_tokens` parameter when using this model.
[](https://platform.claude.com/docs/en/api/models#model_info.max_tokens)
type: "model"
Object type.
For Models, this is always `"model"`.
[](https://platform.claude.com/docs/en/api/models#model_info.type)
[](https://platform.claude.com/docs/en/api/models#model_info)
ThinkingCapability object { supported, types } 
Thinking capability details.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#thinking_capability.supported)
types: [ThinkingTypes](https://platform.claude.com/docs/en/api/models#thinking_types) { adaptive, enabled } 
Supported thinking type configurations.
adaptive: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports thinking with type 'adaptive' (auto).
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#thinking_types.adaptive%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#thinking_capability.types%20%2B%20\(resource\)%20models.adaptive)
enabled: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports thinking with type 'enabled'.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#thinking_types.enabled%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#thinking_capability.types%20%2B%20\(resource\)%20models.enabled)
[](https://platform.claude.com/docs/en/api/models#thinking_capability.types)
[](https://platform.claude.com/docs/en/api/models#thinking_capability)
ThinkingTypes object { adaptive, enabled } 
Supported thinking type configurations.
adaptive: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports thinking with type 'adaptive' (auto).
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#thinking_types.adaptive%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#thinking_types.adaptive)
enabled: [CapabilitySupport](https://platform.claude.com/docs/en/api/models#capability_support) { supported } 
Whether the model supports thinking with type 'enabled'.
supported: boolean
Whether this capability is supported by the model.
[](https://platform.claude.com/docs/en/api/models#thinking_types.enabled%20%2B%20\(resource\)%20models.supported)
[](https://platform.claude.com/docs/en/api/models#thinking_types.enabled)
[](https://platform.claude.com/docs/en/api/models#thinking_types)
