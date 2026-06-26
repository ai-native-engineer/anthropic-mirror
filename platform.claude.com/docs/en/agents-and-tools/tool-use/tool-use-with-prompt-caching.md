<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching -->

# Tool use with prompt caching
Cache tool definitions across turns and understand what invalidates your cache.
This page covers prompt caching for tool definitions: where to place `cache_control` breakpoints, how `defer_loading` preserves your cache, and what invalidates it. For general prompt caching, see [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).
cache_control on tool definitions
Place `cache_control: {"type": "ephemeral"}` on the last tool in your `tools` array. This caches the entire tool-definitions prefix, from the first tool through the marked breakpoint:

  "tools": [
      "name": "get_weather",
      "description": "Get the current weather in a given location",
      "input_schema": {
        "type": "object",
        "properties": {
          "location": { "type": "string" }
        "required": ["location"]
      "name": "get_time",
      "description": "Get the current time in a given time zone",
      "input_schema": {
        "type": "object",
        "properties": {
          "timezone": { "type": "string" }
        "required": ["timezone"]
      "cache_control": { "type": "ephemeral" }
  ]

For `mcp_toolset`, the `cache_control` breakpoint lands on the last tool in the set. You don't control tool order within an MCP toolset, so place the breakpoint on the `mcp_toolset` entry itself and the API applies it to the final expanded tool.
defer_loading and cache preservation
Deferred tools are not included in the system-prompt prefix. When the model discovers a deferred tool through [tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool), the definition is appended inline as a `tool_reference` block in the conversation history. The prefix is untouched, so prompt caching is preserved.
This means adding tools dynamically through tool search does not break your cache. You can start a conversation with a small set of always-loaded tools (cached), let the model discover additional tools as needed, and keep the same cache hit across every turn.
`defer_loading` also acts independently of grammar construction for [strict mode](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use). The grammar builds from the full toolset regardless of which tools are deferred, so prompt caching and grammar caching are both preserved when tools load dynamically.
What invalidates your cache
The cache follows a prefix hierarchy (`tools` → `system` → `messages`), so a change at one level invalidates that level and everything after it:  
| Change  | Invalidates  |  
| --- | --- |  
| Modifying tool definitions  | Entire cache (tools, system, messages)  |  
| Toggling web search or citations  | System and messages caches  |  
| Changing `tool_choice`  | Messages cache  |  
| Changing `disable_parallel_tool_use`  | Messages cache  |  
| Toggling images present/absent  | Messages cache  |  
| Changing thinking parameters  | Messages cache  |  
If you need to vary `tool_choice` mid-conversation, consider placing cache breakpoints before the variation point.
Server tool results are cached automatically
When your request has prompt caching enabled and Claude uses a [server tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools) such as web search, web fetch, or code execution, the API automatically places a cache breakpoint on the server tool result before running the next iteration of the agentic loop. This lets later iterations within the same request read the growing prefix from cache instead of reprocessing it.
This automatic breakpoint always uses the default 5-minute TTL, independent of any TTL you set on your own `cache_control` markers. In the response `usage`, these writes appear under `cache_creation.ephemeral_5m_input_tokens`, so you may see 5-minute cache writes even when every `cache_control` you set uses a 1-hour TTL.
This behavior only applies when your request already has at least one `cache_control` marker. Requests without prompt caching do not receive the automatic breakpoint.
Per-tool interaction table  
| Tool  | Caching considerations  |  
| --- | --- |  
| [Web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)  | Enabling or disabling invalidates the system and messages caches  |  
| [Web fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)  | Enabling or disabling invalidates the system and messages caches  |  
| [Code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)  | Container state is independent of prompt cache  |  
| [Tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)  | Discovered tools load as `tool_reference` blocks, preserving prefix cache  |  
| [Computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)  | Screenshot presence affects messages cache  |  
| [Text editor](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)  | Standard client tool, no special caching interaction  |  
| [Bash](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)  | Standard client tool, no special caching interaction  |  
| [Memory](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)  | Standard client tool, no special caching interaction  |  
Next steps
[ Prompt caching Learn the full prompt caching model, including TTLs and pricing. ](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)[ Tool search Load tools on demand without breaking your cache. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)[  Tool reference Browse all available tools and their parameters. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)
  * [cache_control on tool definitions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching#cache-control-on-tool-definitions)
  * [defer_loading and cache preservation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching#defer-loading-and-cache-preservation)
  * [What invalidates your cache](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching#what-invalidates-your-cache)
  * [Server tool results are cached automatically](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching#server-tool-results-are-cached-automatically)
  * [Per-tool interaction table](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching#per-tool-interaction-table)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching#next-steps)

Messages/Tools
# Tool use with prompt caching
Cache tool definitions across turns and understand what invalidates your cache.
This page covers prompt caching for tool definitions: where to place `cache_control` breakpoints, how `defer_loading` preserves your cache, and what invalidates it. For general prompt caching, see [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching).
cache_control on tool definitions
Place `cache_control: {"type": "ephemeral"}` on the last tool in your `tools` array. This caches the entire tool-definitions prefix, from the first tool through the marked breakpoint:

  "tools": [
      "name": "get_weather",
      "description": "Get the current weather in a given location",
      "input_schema": {
        "type": "object",
        "properties": {
          "location": { "type": "string" }
        "required": ["location"]
      "name": "get_time",
      "description": "Get the current time in a given time zone",
      "input_schema": {
        "type": "object",
        "properties": {
          "timezone": { "type": "string" }
        "required": ["timezone"]
      "cache_control": { "type": "ephemeral" }
  ]

For `mcp_toolset`, the `cache_control` breakpoint lands on the last tool in the set. You don't control tool order within an MCP toolset, so place the breakpoint on the `mcp_toolset` entry itself and the API applies it to the final expanded tool.
defer_loading and cache preservation
Deferred tools are not included in the system-prompt prefix. When the model discovers a deferred tool through [tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool), the definition is appended inline as a `tool_reference` block in the conversation history. The prefix is untouched, so prompt caching is preserved.
This means adding tools dynamically through tool search does not break your cache. You can start a conversation with a small set of always-loaded tools (cached), let the model discover additional tools as needed, and keep the same cache hit across every turn.
`defer_loading` also acts independently of grammar construction for [strict mode](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use). The grammar builds from the full toolset regardless of which tools are deferred, so prompt caching and grammar caching are both preserved when tools load dynamically.
What invalidates your cache
The cache follows a prefix hierarchy (`tools` → `system` → `messages`), so a change at one level invalidates that level and everything after it:  
| Change  | Invalidates  |  
| --- | --- |  
| Modifying tool definitions  | Entire cache (tools, system, messages)  |  
| Toggling web search or citations  | System and messages caches  |  
| Changing `tool_choice`  | Messages cache  |  
| Changing `disable_parallel_tool_use`  | Messages cache  |  
| Toggling images present/absent  | Messages cache  |  
| Changing thinking parameters  | Messages cache  |  
If you need to vary `tool_choice` mid-conversation, consider placing cache breakpoints before the variation point.
Server tool results are cached automatically
When your request has prompt caching enabled and Claude uses a [server tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools) such as web search, web fetch, or code execution, the API automatically places a cache breakpoint on the server tool result before running the next iteration of the agentic loop. This lets later iterations within the same request read the growing prefix from cache instead of reprocessing it.
This automatic breakpoint always uses the default 5-minute TTL, independent of any TTL you set on your own `cache_control` markers. In the response `usage`, these writes appear under `cache_creation.ephemeral_5m_input_tokens`, so you may see 5-minute cache writes even when every `cache_control` you set uses a 1-hour TTL.
This behavior only applies when your request already has at least one `cache_control` marker. Requests without prompt caching do not receive the automatic breakpoint.
Per-tool interaction table  
| Tool  | Caching considerations  |  
| --- | --- |  
| [Web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)  | Enabling or disabling invalidates the system and messages caches  |  
| [Web fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)  | Enabling or disabling invalidates the system and messages caches  |  
| [Code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)  | Container state is independent of prompt cache  |  
| [Tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)  | Discovered tools load as `tool_reference` blocks, preserving prefix cache  |  
| [Computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)  | Screenshot presence affects messages cache  |  
| [Text editor](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)  | Standard client tool, no special caching interaction  |  
| [Bash](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)  | Standard client tool, no special caching interaction  |  
| [Memory](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)  | Standard client tool, no special caching interaction  |  
Next steps
[ Prompt caching Learn the full prompt caching model, including TTLs and pricing. ](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)[ Tool search Load tools on demand without breaking your cache. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)[  Tool reference Browse all available tools and their parameters. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)
