<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool -->

# Tool search tool
The tool search tool enables Claude to work with hundreds or thousands of tools by dynamically discovering and loading them on-demand. Instead of loading all tool definitions into the context window upfront, Claude searches your tool catalog (including tool names, descriptions, argument names, and argument descriptions) and loads only the tools it needs.
This approach solves two problems that compound quickly as tool libraries scale:
  * **Context bloat:** Tool definitions eat into your context budget fast. A typical multi-server setup (GitHub, Slack, Sentry, Grafana, Splunk) can consume ~55k tokens in definitions before Claude does any actual work. Tool search typically reduces this by over 85%, loading only the 3–5 tools Claude actually needs for a given request.
  * **Tool selection accuracy:** Claude's ability to correctly pick the right tool degrades significantly once you exceed 30–50 available tools. By surfacing a focused set of relevant tools on demand, tool search keeps selection accuracy high even across thousands of tools.


For background on the scaling challenges that tool search solves, see [Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use). Tool search's on-demand loading is also an instance of the broader just-in-time retrieval principle described in [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
Although this is provided as a server-side tool, you can also implement your own client-side tool search functionality. See [Custom tool search implementation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#custom-tool-search-implementation) for details.
Share feedback on this feature through the [feedback form](https://forms.gle/MhcGFFwLxuwnWTkYA).
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.

On Amazon Bedrock, server-side tool search is available only through the [InvokeModel API](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModel_AnthropicClaude_section.html), not the Converse API.
On [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), server-side tool search works identically to the Claude API. Claude Platform on AWS uses the Anthropic Messages API directly, so there is no InvokeModel or Converse distinction.
How tool search works
There are two tool search variants:
  * **Regex** (`tool_search_tool_regex_20251119`): Claude constructs regex patterns to search for tools
  * **BM25** (`tool_search_tool_bm25_20251119`): Claude uses natural language queries to search for tools

When you enable the tool search tool:
  1. You include a tool search tool (for example, `tool_search_tool_regex_20251119` or `tool_search_tool_bm25_20251119`) in your tools list.
  2. You provide all tool definitions with `defer_loading: true` for tools that shouldn't be loaded immediately.
  3. Claude sees only the tool search tool and any non-deferred tools initially.
  4. When Claude needs additional tools, it searches using a tool search tool.
  5. The API returns 3-5 most relevant `tool_reference` blocks.
  6. These references are automatically expanded into full tool definitions.
  7. Claude selects from the discovered tools and calls them.

This keeps your context window efficient while maintaining high tool selection accuracy.
Quick start
Here's a simple example with deferred tools:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=2048,
    messages=[{"role": "user", "content": "What is the weather in San Francisco?"}],
    tools=[
        {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
            "name": "get_weather",
            "description": "Get the weather at a specific location",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                "required": ["location"],
            "defer_loading": True,
            "name": "search_files",
            "description": "Search through files in the workspace",
            "input_schema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "file_types": {"type": "array", "items": {"type": "string"}},
                "required": ["query"],
            "defer_loading": True,
    ],
)

print(response)

Tool definition
The tool search tool has two variants:
JSON

  "type": "tool_search_tool_regex_20251119",
  "name": "tool_search_tool_regex"

JSON

  "type": "tool_search_tool_bm25_20251119",
  "name": "tool_search_tool_bm25"


**Regex variant query format: Python regex, NOT natural language**
When using `tool_search_tool_regex_20251119`, Claude constructs regex patterns using Python's `re.search()` syntax, not natural language queries. Common patterns:
  * `"weather"` - matches tool names/descriptions containing "weather"
  * `"get_.*_data"` - matches tools like `get_user_data`, `get_weather_data`
  * `"database.*query|query.*database"` - OR patterns for flexibility
  * `"(?i)slack"` - case-insensitive search

Maximum query length: 200 characters
**BM25 variant query format: Natural language**
When using `tool_search_tool_bm25_20251119`, Claude uses natural language queries to search for tools.
### 
Deferred tool loading
Mark tools for on-demand loading by adding `defer_loading: true`:
JSON

  "name": "get_weather",
  "description": "Get current weather for a location",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": { "type": "string" },
      "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
    "required": ["location"]
  "defer_loading": true

**Key points:**
  * Tools without `defer_loading` are loaded into context immediately
  * Tools with `defer_loading: true` are only loaded when Claude discovers them through search
  * The tool search tool itself should **never** have `defer_loading: true`
  * Keep your 3-5 most frequently used tools as non-deferred for optimal performance

Both tool search variants (`regex` and `bm25`) search tool names, descriptions, argument names, and argument descriptions.
**How deferral works internally:** Deferred tools are not included in the system-prompt prefix. When the model discovers a deferred tool through tool search, the API appends a `tool_reference` block inline in the conversation, then expands it into the full tool definition before passing it to Claude. The prefix is untouched, so prompt caching is preserved. The grammar for [strict mode](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) (the rules that constrain tool-call output to match your schemas) builds from the full toolset, so `defer_loading` and strict mode compose without grammar recompilation.
Response format
When Claude uses the tool search tool, the response includes new block types:
JSON

  "role": "assistant",
  "content": [
      "type": "text",
      "text": "I'll search for tools to help with the weather information."
      "type": "server_tool_use",
      "id": "srvtoolu_01ABC123",
      "name": "tool_search_tool_regex",
      "input": {
        "query": "weather"
      "type": "tool_search_tool_result",
      "tool_use_id": "srvtoolu_01ABC123",
      "content": {
        "type": "tool_search_tool_search_result",
        "tool_references": [{ "type": "tool_reference", "tool_name": "get_weather" }]
      "type": "text",
      "text": "I found a weather tool. Let me get the weather for San Francisco."
      "type": "tool_use",
      "id": "toolu_01XYZ789",
      "name": "get_weather",
      "input": { "location": "San Francisco", "unit": "fahrenheit" }
  ],
  "stop_reason": "tool_use"

### 
Understanding the response
  * **`server_tool_use`:** Indicates Claude is calling the tool search tool
  * **`tool_search_tool_result`:** Contains the search results with a nested `tool_search_tool_search_result` object
  * **`tool_references`:** Array of `tool_reference` objects pointing to discovered tools
  * **`tool_use`:** Claude calling the discovered tool

The `tool_reference` blocks are automatically expanded into full tool definitions before being shown to Claude. You don't need to handle this expansion yourself. It happens automatically in the API as long as you provide all matching tool definitions in the `tools` parameter.
MCP integration
For configuring `mcp_toolset` with `defer_loading`, see [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector).
Custom tool search implementation
You can implement your own tool search logic (for example, using embeddings or semantic search) by returning `tool_reference` blocks from a custom tool. When Claude calls your custom search tool, return a standard `tool_result` with `tool_reference` blocks in the content array:
JSON

  "type": "tool_result",
  "tool_use_id": "toolu_your_tool_id",
  "content": [{ "type": "tool_reference", "tool_name": "discovered_tool_name" }]

Every tool referenced must have a corresponding tool definition in the top-level `tools` parameter with `defer_loading: true`. This approach lets you use more sophisticated search algorithms while maintaining compatibility with the tool search system.
The `tool_search_tool_result` format shown in the [Response format](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#response-format) section is the server-side format used internally by Anthropic's built-in tool search. For custom client-side implementations, always use the standard `tool_result` format with `tool_reference` content blocks as shown in the preceding example.
For a complete example using embeddings, see the [tool search with embeddings cookbook](https://platform.claude.com/cookbooks/tool_use).
Error handling
The tool search tool is not compatible with [tool use examples](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#providing-tool-use-examples). If you need to provide examples of tool usage, use standard tool calling without tool search.
### 
HTTP errors (400 status)
These errors prevent the request from being processed:
**All tools deferred:**

  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "All tools have defer_loading set. At least one tool must be non-deferred."

**Missing tool definition:**

  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Tool reference 'unknown_tool' has no corresponding tool definition"

### 
Tool result errors (200 status)
Errors during tool execution return a 200 response with error information in the body:
JSON

  "type": "tool_search_tool_result",
  "tool_use_id": "srvtoolu_01ABC123",
  "content": {
    "type": "tool_search_tool_result_error",
    "error_code": "invalid_pattern"

**Error codes:**
  * `too_many_requests`: Rate limit exceeded for tool search operations
  * `invalid_pattern`: Malformed regex pattern
  * `pattern_too_long`: Pattern exceeds 200 character limit
  * `unavailable`: Tool search service temporarily unavailable

### 
Common mistakes
### 400 Error: All tools are deferred
### 400 Error: Missing tool definition
### Claude doesn't find expected tools
Prompt caching
For how `defer_loading` preserves prompt caching, see [Tool use with prompt caching](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching).
The system automatically expands `tool_reference` blocks throughout the entire conversation history, so Claude can reuse discovered tools in subsequent turns without re-searching.
Streaming
With streaming enabled, you'll receive tool search events as part of the stream:

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "tool_search_tool_regex"}}

// Search query streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"query\":\"weather\"}"}}

// Pause while search executes

// Search results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "tool_search_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": {"type": "tool_search_tool_search_result", "tool_references": [{"type": "tool_reference", "tool_name": "get_weather"}]}}}

// Claude continues with discovered tools

Batch requests
You can include the tool search tool in the [Messages Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing). Tool search operations through the Messages Batches API are priced the same as those in regular Messages API requests.
Limits and best practices
### 
Limits
  * **Maximum tools:** 10,000 tools in your catalog
  * **Search results:** Returns 3-5 most relevant tools per search
  * **Pattern length:** Maximum 200 characters for regex patterns
  * **Model support:** Claude Fable 5, Claude Mythos 5, [Claude Mythos Preview](https://anthropic.com/glasswing), Sonnet 4.0+, Opus 4.0+, Haiku 4.5+

### 
When to use tool search
**Good use cases:**
  * 10+ tools available in your system
  * Tool definitions consuming >10k tokens
  * Experiencing tool selection accuracy issues with large tool sets
  * Building MCP-powered systems with multiple servers (200+ tools)
  * Tool library growing over time

**When traditional tool calling might be better:**
  * Less than 10 tools total
  * All tools are frequently used in every request
  * Very small tool definitions (<100 tokens total)

### 
Optimization tips
  * Keep 3-5 most frequently used tools as non-deferred
  * Write clear, descriptive tool names and descriptions
  * Use consistent namespacing in tool names: prefix by service or resource (for example, `github_`, `slack_`) so that search queries naturally surface the right tool group
  * Use semantic keywords in descriptions that match how users describe tasks
  * Add a system prompt section describing available tool categories: "You can search for tools to interact with Slack, GitHub, and Jira"
  * Monitor which tools Claude discovers to refine descriptions

Usage
Tool search tool usage is tracked in the response usage object:
JSON

  "usage": {
    "input_tokens": 1024,
    "output_tokens": 256,
    "server_tool_use": {
      "tool_search_requests": 2

Next steps
[ Tool reference Full tool catalog with model compatibility and parameters. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)[ MCP connector Configure MCP toolsets with deferred loading. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)[  Prompt caching Combine tool search with cached tool definitions. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[ Define tools Step-by-step guide for defining tools. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
  * [How tool search works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#how-tool-search-works)
  * [Quick start](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#quick-start)
  * [Tool definition](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#tool-definition)
  * [Deferred tool loading](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#deferred-tool-loading)
  * [Response format](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#response-format)
  * [Understanding the response](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#understanding-the-response)
  * [MCP integration](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#mcp-integration)
  * [Custom tool search implementation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#custom-tool-search-implementation)
  * [Error handling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#error-handling)
  * [HTTP errors (400 status)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#http-errors-400-status)
  * [Tool result errors (200 status)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#tool-result-errors-200-status)
  * [Common mistakes](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#common-mistakes)
  * [Prompt caching](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#prompt-caching)
  * [Streaming](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#streaming)
  * [Batch requests](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#batch-requests)
  * [Limits and best practices](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#limits-and-best-practices)
  * [Limits](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#limits)
  * [When to use tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#when-to-use-tool-search)
  * [Optimization tips](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#optimization-tips)
  * [Usage](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#usage)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#next-steps)

Messages/Tool infrastructure
# Tool search tool
The tool search tool enables Claude to work with hundreds or thousands of tools by dynamically discovering and loading them on-demand. Instead of loading all tool definitions into the context window upfront, Claude searches your tool catalog (including tool names, descriptions, argument names, and argument descriptions) and loads only the tools it needs.
This approach solves two problems that compound quickly as tool libraries scale:
  * **Context bloat:** Tool definitions eat into your context budget fast. A typical multi-server setup (GitHub, Slack, Sentry, Grafana, Splunk) can consume ~55k tokens in definitions before Claude does any actual work. Tool search typically reduces this by over 85%, loading only the 3–5 tools Claude actually needs for a given request.
  * **Tool selection accuracy:** Claude's ability to correctly pick the right tool degrades significantly once you exceed 30–50 available tools. By surfacing a focused set of relevant tools on demand, tool search keeps selection accuracy high even across thousands of tools.


For background on the scaling challenges that tool search solves, see [Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use). Tool search's on-demand loading is also an instance of the broader just-in-time retrieval principle described in [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
Although this is provided as a server-side tool, you can also implement your own client-side tool search functionality. See [Custom tool search implementation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#custom-tool-search-implementation) for details.
Share feedback on this feature through the [feedback form](https://forms.gle/MhcGFFwLxuwnWTkYA).
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.

On Amazon Bedrock, server-side tool search is available only through the [InvokeModel API](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModel_AnthropicClaude_section.html), not the Converse API.
On [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), server-side tool search works identically to the Claude API. Claude Platform on AWS uses the Anthropic Messages API directly, so there is no InvokeModel or Converse distinction.
How tool search works
There are two tool search variants:
  * **Regex** (`tool_search_tool_regex_20251119`): Claude constructs regex patterns to search for tools
  * **BM25** (`tool_search_tool_bm25_20251119`): Claude uses natural language queries to search for tools

When you enable the tool search tool:
  1. You include a tool search tool (for example, `tool_search_tool_regex_20251119` or `tool_search_tool_bm25_20251119`) in your tools list.
  2. You provide all tool definitions with `defer_loading: true` for tools that shouldn't be loaded immediately.
  3. Claude sees only the tool search tool and any non-deferred tools initially.
  4. When Claude needs additional tools, it searches using a tool search tool.
  5. The API returns 3-5 most relevant `tool_reference` blocks.
  6. These references are automatically expanded into full tool definitions.
  7. Claude selects from the discovered tools and calls them.

This keeps your context window efficient while maintaining high tool selection accuracy.
Quick start
Here's a simple example with deferred tools:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=2048,
    messages=[{"role": "user", "content": "What is the weather in San Francisco?"}],
    tools=[
        {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
            "name": "get_weather",
            "description": "Get the weather at a specific location",
            "input_schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                "required": ["location"],
            "defer_loading": True,
            "name": "search_files",
            "description": "Search through files in the workspace",
            "input_schema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "file_types": {"type": "array", "items": {"type": "string"}},
                "required": ["query"],
            "defer_loading": True,
    ],
)

print(response)

Tool definition
The tool search tool has two variants:
JSON

  "type": "tool_search_tool_regex_20251119",
  "name": "tool_search_tool_regex"

JSON

  "type": "tool_search_tool_bm25_20251119",
  "name": "tool_search_tool_bm25"


**Regex variant query format: Python regex, NOT natural language**
When using `tool_search_tool_regex_20251119`, Claude constructs regex patterns using Python's `re.search()` syntax, not natural language queries. Common patterns:
  * `"weather"` - matches tool names/descriptions containing "weather"
  * `"get_.*_data"` - matches tools like `get_user_data`, `get_weather_data`
  * `"database.*query|query.*database"` - OR patterns for flexibility
  * `"(?i)slack"` - case-insensitive search

Maximum query length: 200 characters
**BM25 variant query format: Natural language**
When using `tool_search_tool_bm25_20251119`, Claude uses natural language queries to search for tools.
### 
Deferred tool loading
Mark tools for on-demand loading by adding `defer_loading: true`:
JSON

  "name": "get_weather",
  "description": "Get current weather for a location",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": { "type": "string" },
      "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
    "required": ["location"]
  "defer_loading": true

**Key points:**
  * Tools without `defer_loading` are loaded into context immediately
  * Tools with `defer_loading: true` are only loaded when Claude discovers them through search
  * The tool search tool itself should **never** have `defer_loading: true`
  * Keep your 3-5 most frequently used tools as non-deferred for optimal performance

Both tool search variants (`regex` and `bm25`) search tool names, descriptions, argument names, and argument descriptions.
**How deferral works internally:** Deferred tools are not included in the system-prompt prefix. When the model discovers a deferred tool through tool search, the API appends a `tool_reference` block inline in the conversation, then expands it into the full tool definition before passing it to Claude. The prefix is untouched, so prompt caching is preserved. The grammar for [strict mode](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use) (the rules that constrain tool-call output to match your schemas) builds from the full toolset, so `defer_loading` and strict mode compose without grammar recompilation.
Response format
When Claude uses the tool search tool, the response includes new block types:
JSON

  "role": "assistant",
  "content": [
      "type": "text",
      "text": "I'll search for tools to help with the weather information."
      "type": "server_tool_use",
      "id": "srvtoolu_01ABC123",
      "name": "tool_search_tool_regex",
      "input": {
        "query": "weather"
      "type": "tool_search_tool_result",
      "tool_use_id": "srvtoolu_01ABC123",
      "content": {
        "type": "tool_search_tool_search_result",
        "tool_references": [{ "type": "tool_reference", "tool_name": "get_weather" }]
      "type": "text",
      "text": "I found a weather tool. Let me get the weather for San Francisco."
      "type": "tool_use",
      "id": "toolu_01XYZ789",
      "name": "get_weather",
      "input": { "location": "San Francisco", "unit": "fahrenheit" }
  ],
  "stop_reason": "tool_use"

### 
Understanding the response
  * **`server_tool_use`:** Indicates Claude is calling the tool search tool
  * **`tool_search_tool_result`:** Contains the search results with a nested `tool_search_tool_search_result` object
  * **`tool_references`:** Array of `tool_reference` objects pointing to discovered tools
  * **`tool_use`:** Claude calling the discovered tool

The `tool_reference` blocks are automatically expanded into full tool definitions before being shown to Claude. You don't need to handle this expansion yourself. It happens automatically in the API as long as you provide all matching tool definitions in the `tools` parameter.
MCP integration
For configuring `mcp_toolset` with `defer_loading`, see [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector).
Custom tool search implementation
You can implement your own tool search logic (for example, using embeddings or semantic search) by returning `tool_reference` blocks from a custom tool. When Claude calls your custom search tool, return a standard `tool_result` with `tool_reference` blocks in the content array:
JSON

  "type": "tool_result",
  "tool_use_id": "toolu_your_tool_id",
  "content": [{ "type": "tool_reference", "tool_name": "discovered_tool_name" }]

Every tool referenced must have a corresponding tool definition in the top-level `tools` parameter with `defer_loading: true`. This approach lets you use more sophisticated search algorithms while maintaining compatibility with the tool search system.
The `tool_search_tool_result` format shown in the [Response format](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool#response-format) section is the server-side format used internally by Anthropic's built-in tool search. For custom client-side implementations, always use the standard `tool_result` format with `tool_reference` content blocks as shown in the preceding example.
For a complete example using embeddings, see the [tool search with embeddings cookbook](https://platform.claude.com/cookbooks/tool_use).
Error handling
The tool search tool is not compatible with [tool use examples](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#providing-tool-use-examples). If you need to provide examples of tool usage, use standard tool calling without tool search.
### 
HTTP errors (400 status)
These errors prevent the request from being processed:
**All tools deferred:**

  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "All tools have defer_loading set. At least one tool must be non-deferred."

**Missing tool definition:**

  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Tool reference 'unknown_tool' has no corresponding tool definition"

### 
Tool result errors (200 status)
Errors during tool execution return a 200 response with error information in the body:
JSON

  "type": "tool_search_tool_result",
  "tool_use_id": "srvtoolu_01ABC123",
  "content": {
    "type": "tool_search_tool_result_error",
    "error_code": "invalid_pattern"

**Error codes:**
  * `too_many_requests`: Rate limit exceeded for tool search operations
  * `invalid_pattern`: Malformed regex pattern
  * `pattern_too_long`: Pattern exceeds 200 character limit
  * `unavailable`: Tool search service temporarily unavailable

### 
Common mistakes
### 400 Error: All tools are deferred
### 400 Error: Missing tool definition
### Claude doesn't find expected tools
Prompt caching
For how `defer_loading` preserves prompt caching, see [Tool use with prompt caching](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching).
The system automatically expands `tool_reference` blocks throughout the entire conversation history, so Claude can reuse discovered tools in subsequent turns without re-searching.
Streaming
With streaming enabled, you'll receive tool search events as part of the stream:

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "tool_search_tool_regex"}}

// Search query streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"query\":\"weather\"}"}}

// Pause while search executes

// Search results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "tool_search_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": {"type": "tool_search_tool_search_result", "tool_references": [{"type": "tool_reference", "tool_name": "get_weather"}]}}}

// Claude continues with discovered tools

Batch requests
You can include the tool search tool in the [Messages Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing). Tool search operations through the Messages Batches API are priced the same as those in regular Messages API requests.
Limits and best practices
### 
Limits
  * **Maximum tools:** 10,000 tools in your catalog
  * **Search results:** Returns 3-5 most relevant tools per search
  * **Pattern length:** Maximum 200 characters for regex patterns
  * **Model support:** Claude Fable 5, Claude Mythos 5, [Claude Mythos Preview](https://anthropic.com/glasswing), Sonnet 4.0+, Opus 4.0+, Haiku 4.5+

### 
When to use tool search
**Good use cases:**
  * 10+ tools available in your system
  * Tool definitions consuming >10k tokens
  * Experiencing tool selection accuracy issues with large tool sets
  * Building MCP-powered systems with multiple servers (200+ tools)
  * Tool library growing over time

**When traditional tool calling might be better:**
  * Less than 10 tools total
  * All tools are frequently used in every request
  * Very small tool definitions (<100 tokens total)

### 
Optimization tips
  * Keep 3-5 most frequently used tools as non-deferred
  * Write clear, descriptive tool names and descriptions
  * Use consistent namespacing in tool names: prefix by service or resource (for example, `github_`, `slack_`) so that search queries naturally surface the right tool group
  * Use semantic keywords in descriptions that match how users describe tasks
  * Add a system prompt section describing available tool categories: "You can search for tools to interact with Slack, GitHub, and Jira"
  * Monitor which tools Claude discovers to refine descriptions

Usage
Tool search tool usage is tracked in the response usage object:
JSON

  "usage": {
    "input_tokens": 1024,
    "output_tokens": 256,
    "server_tool_use": {
      "tool_search_requests": 2

Next steps
[ Tool reference Full tool catalog with model compatibility and parameters. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)[ MCP connector Configure MCP toolsets with deferred loading. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)[  Prompt caching Combine tool search with cached tool definitions. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[ Define tools Step-by-step guide for defining tools. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
