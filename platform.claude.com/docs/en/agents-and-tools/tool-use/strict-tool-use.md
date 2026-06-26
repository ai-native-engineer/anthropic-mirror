<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use -->

# Strict tool use
Enforce JSON Schema compliance on Claude's tool inputs with grammar-constrained sampling.
Setting `strict: true` on a tool definition guarantees Claude's tool inputs match your JSON Schema by constraining the model's token sampling to schema-valid outputs (a technique called grammar-constrained sampling). This page covers why strict mode matters for agents, how to enable it, and common use cases. For the supported JSON Schema subset, see [JSON Schema limitations](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#json-schema-limitations). For non-strict schema guidance, see [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools).
Strict tool use validates tool parameters, ensuring Claude calls your functions with correctly-typed arguments. Use strict tool use when you need to:
  * Validate tool parameters
  * Build agentic workflows
  * Ensure type-safe function calls
  * Handle complex tools with nested properties

Why strict tool use matters for agents
Building reliable agentic systems requires guaranteed schema conformance. Without strict mode, Claude might return incompatible types (`"2"` instead of `2`) or omit required fields, breaking your functions and causing runtime errors.
Strict tool use guarantees type-safe parameters:
  * Functions receive correctly-typed arguments every time
  * No need to validate and retry tool calls
  * Production-ready agents that work consistently at scale

For example, suppose a booking system needs `passengers: int`. Without strict mode, Claude might provide `passengers: "two"` or `passengers: "2"`. With `strict: true`, the response always contains `passengers: 2`.
Quick start
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
    tools=[
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "strict": True,  # Enable strict mode
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The unit of temperature, either 'celsius' or 'fahrenheit'",
                "required": ["location"],
                "additionalProperties": False,
    ],
)
print(response.content)

**Response format:** Tool use blocks with validated inputs in `response.content[x].input`
Output

  "type": "tool_use",
  "name": "get_weather",
  "input": {
    "location": "San Francisco, CA"

**Guarantees:**
  * Tool `input` strictly follows the `input_schema`
  * Tool `name` is always valid (from provided tools or server tools)

How it works
  1. 1
Define your tool schema
Create a JSON schema for your tool's `input_schema`. The schema uses standard JSON Schema format with some limitations (see [JSON Schema limitations](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#json-schema-limitations)).
  2. 2
Add strict: true
Set `"strict": true` as a top-level property in your tool definition, alongside `name`, `description`, and `input_schema`.
  3. 3
Handle tool calls
When Claude uses the tool, the `input` field in the tool_use block strictly follows your `input_schema`, and the `name` is always valid.

Common use cases
### Validated tool inputs
### Agentic workflow with multiple validated tools
Data retention
Strict tool use compiles tool `input_schema` definitions into grammars using the same pipeline as [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs). Tool schemas are temporarily cached for up to 24 hours since last use. Prompts and responses are not retained beyond the API response.
Strict tool use is HIPAA eligible, but **PHI must not be included in tool schema definitions**. The API caches compiled schemas separately from message content, and these cached schemas do not receive the same PHI protections as prompts and responses. Do not include PHI in `input_schema` property names, `enum` values, `const` values, or `pattern` regular expressions. PHI should only appear in message content (prompts and responses), where it is protected under HIPAA safeguards.
For ZDR and HIPAA eligibility across all features, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention).
Next steps
[  Web fetch tool Fetch and read content from specific URLs to bring live web content into Claude's context. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)[ Tool use with prompt caching Cache tool definitions across turns to reduce cost and latency. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[  Structured outputs Get validated JSON responses using the same grammar-constrained sampling. ](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)[ Define tools Specify tool schemas, write effective descriptions, and control when Claude calls your tools. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
  * [Why strict tool use matters for agents](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use#why-strict-tool-use-matters-for-agents)
  * [Quick start](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use#quick-start)
  * [How it works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use#how-it-works)
  * [Common use cases](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use#common-use-cases)
  * [Data retention](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use#data-retention)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use#next-steps)

Messages/Tools
# Strict tool use
Enforce JSON Schema compliance on Claude's tool inputs with grammar-constrained sampling.
Setting `strict: true` on a tool definition guarantees Claude's tool inputs match your JSON Schema by constraining the model's token sampling to schema-valid outputs (a technique called grammar-constrained sampling). This page covers why strict mode matters for agents, how to enable it, and common use cases. For the supported JSON Schema subset, see [JSON Schema limitations](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#json-schema-limitations). For non-strict schema guidance, see [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools).
Strict tool use validates tool parameters, ensuring Claude calls your functions with correctly-typed arguments. Use strict tool use when you need to:
  * Validate tool parameters
  * Build agentic workflows
  * Ensure type-safe function calls
  * Handle complex tools with nested properties

Why strict tool use matters for agents
Building reliable agentic systems requires guaranteed schema conformance. Without strict mode, Claude might return incompatible types (`"2"` instead of `2`) or omit required fields, breaking your functions and causing runtime errors.
Strict tool use guarantees type-safe parameters:
  * Functions receive correctly-typed arguments every time
  * No need to validate and retry tool calls
  * Production-ready agents that work consistently at scale

For example, suppose a booking system needs `passengers: int`. Without strict mode, Claude might provide `passengers: "two"` or `passengers: "2"`. With `strict: true`, the response always contains `passengers: 2`.
Quick start
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "What's the weather like in San Francisco?"}],
    tools=[
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "strict": True,  # Enable strict mode
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The unit of temperature, either 'celsius' or 'fahrenheit'",
                "required": ["location"],
                "additionalProperties": False,
    ],
)
print(response.content)

**Response format:** Tool use blocks with validated inputs in `response.content[x].input`
Output

  "type": "tool_use",
  "name": "get_weather",
  "input": {
    "location": "San Francisco, CA"

**Guarantees:**
  * Tool `input` strictly follows the `input_schema`
  * Tool `name` is always valid (from provided tools or server tools)

How it works
  1. 1
Define your tool schema
Create a JSON schema for your tool's `input_schema`. The schema uses standard JSON Schema format with some limitations (see [JSON Schema limitations](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#json-schema-limitations)).
  2. 2
Add strict: true
Set `"strict": true` as a top-level property in your tool definition, alongside `name`, `description`, and `input_schema`.
  3. 3
Handle tool calls
When Claude uses the tool, the `input` field in the tool_use block strictly follows your `input_schema`, and the `name` is always valid.

Common use cases
### Validated tool inputs
### Agentic workflow with multiple validated tools
Data retention
Strict tool use compiles tool `input_schema` definitions into grammars using the same pipeline as [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs). Tool schemas are temporarily cached for up to 24 hours since last use. Prompts and responses are not retained beyond the API response.
Strict tool use is HIPAA eligible, but **PHI must not be included in tool schema definitions**. The API caches compiled schemas separately from message content, and these cached schemas do not receive the same PHI protections as prompts and responses. Do not include PHI in `input_schema` property names, `enum` values, `const` values, or `pattern` regular expressions. PHI should only appear in message content (prompts and responses), where it is protected under HIPAA safeguards.
For ZDR and HIPAA eligibility across all features, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention).
Next steps
[  Web fetch tool Fetch and read content from specific URLs to bring live web content into Claude's context. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)[ Tool use with prompt caching Cache tool definitions across turns to reduce cost and latency. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[  Structured outputs Get validated JSON responses using the same grammar-constrained sampling. ](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)[ Define tools Specify tool schemas, write effective descriptions, and control when Claude calls your tools. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
