<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool -->

# Web search tool
The web search tool gives Claude direct access to real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff. The response includes citations for sources drawn from search results.
The latest web search tool version (`web_search_20260318`) supports **dynamic filtering** with Claude Fable 5, Claude Opus 4.8, Claude Mythos 5, [Claude Mythos Preview](https://anthropic.com/glasswing), Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6. Claude can write and execute code to filter search results before they reach the context window, keeping only relevant information and discarding the rest. This leads to more accurate responses while reducing token consumption. `web_search_20260318` also adds [response inclusion](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#response-inclusion) control for agentic workflows. The previous versions (`web_search_20260209` for dynamic filtering only, `web_search_20250305` for basic search) remain available.
For [Claude Mythos Preview](https://anthropic.com/glasswing), web search is supported on the Claude API, Google Cloud, and Microsoft Foundry. Web search is not available for Mythos Preview on Amazon Bedrock or [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws).
For Zero Data Retention eligibility and the `allowed_callers` workaround, see [Server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools#zdr-and-allowed-callers).
For model support, see the [Tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference).
How web search works
When you add the web search tool to your API request:
  1. Claude decides when to search based on the prompt.
  2. The API executes the searches and provides Claude with the results. This process may repeat multiple times throughout a single request.
  3. At the end of its turn, Claude provides a final response with cited sources.

### 
When Claude searches
Claude searches when the request depends on information that is current, changing, or outside its training data:
  * Recent events, news, or announcements
  * Current prices, rates, scores, or statistics
  * Information about specific organizations, people, or products that might have changed
  * Explicit requests to search or look something up

Claude answers directly without searching when the request draws on stable knowledge:
  * Established facts, math, science fundamentals, or coding concepts
  * Creative writing or brainstorming
  * Analysis of content already provided in the conversation
  * Conversational turns and greetings

Triggering is steerable through your system prompt: you can encourage Claude to search more readily or to prefer answering directly. For a hard constraint, use `max_uses` to cap the number of searches for each request.
### 
Dynamic filtering
Web search is a token-intensive task. With basic web search, Claude needs to pull search results into context, fetch full HTML from multiple websites, and reason over all of it before arriving at an answer. Often, much of this content is irrelevant, which can degrade response quality.
With `web_search_20260209` or later, Claude can write and execute code to post-process query results. Instead of reasoning over full HTML files, Claude dynamically filters search results before loading them into context, keeping only what's relevant and discarding the rest.
Dynamic filtering is particularly effective for:
  * Searching through technical documentation
  * Literature review and citation verification
  * Technical research
  * Response grounding and verification

Dynamic filtering requires the [code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) to be enabled. The web search tool (with and without dynamic filtering) is available on the Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry). On Google Cloud, only the basic web search tool (without dynamic filtering) is available. Web search is not available on Amazon Bedrock.
To enable dynamic filtering, use `web_search_20260209` or any later version. The following examples use `web_search_20260209`:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.",
    ],
    tools=[{"type": "web_search_20260209", "name": "web_search"}],
)
print(response)

How to use web search
Your organization's administrator must enable web search in the [Claude Console](https://platform.claude.com/settings/privacy).
Provide the web search tool in your API request:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "What's the weather in NYC?"}],
    tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}],
)
print(response)

Tool definition
The web search tool supports the following parameters:
JSON

  "type": "web_search_20250305",
  "name": "web_search",

  // Optional: Limit the number of searches per request
  "max_uses": 5,

  // Optional: Only include results from these domains
  "allowed_domains": ["example.com", "trusteddomain.org"],

  // Optional: Never include results from these domains
  "blocked_domains": ["untrustedsource.com"],

  // Optional: Localize search results
  "user_location": {
    "type": "approximate",
    "city": "San Francisco",
    "region": "California",
    "country": "US",
    "timezone": "America/Los_Angeles"

### 
Max uses
The `max_uses` parameter limits the number of searches performed. If Claude attempts more searches than allowed, the `web_search_tool_result` is an error with the `max_uses_exceeded` error code.
Simple factual queries typically use 1–3 searches; comparative or multi-entity research can use 10 or more. For latency-sensitive lookups, `max_uses: 3` bounds cost while rarely truncating. For research agents, set `max_uses` to 15–20 or omit it entirely.
### 
Domain filtering
For domain filtering with `allowed_domains` and `blocked_domains`, see [Server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools#domain-filtering).
### 
Localization
The `user_location` parameter allows you to localize search results based on a user's location.
  * `type`: The type of location (must be `approximate`)
  * `city`: The city name
  * `region`: The region or state
  * `country`: The country
  * `timezone`: The [IANA timezone ID](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

### 
Response inclusion
Requires `web_search_20260318` or later.
The `response_inclusion` parameter controls how search result blocks appear in the API response when the result was consumed by a completed [code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) call in the same turn. Set `"response_inclusion": "excluded"` to drop those nested `server_tool_use` and result block pairs entirely from the response, reducing output token costs for agentic workflows that don't need to echo raw search content back to the client. The default is `"full"`. Results from direct calls, or from code execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

  "tools": [
      "type": "web_search_20260318",
      "name": "web_search",
      "response_inclusion": "excluded"
  ]

Response
Here's an example response structure:
Output

  "role": "assistant",
  "content": [
    // 1. Claude's decision to search
      "type": "text",
      "text": "I'll search for when Claude Shannon was born."
    // 2. The search query used
      "type": "server_tool_use",
      "id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
      "name": "web_search",
      "input": {
        "query": "claude shannon birth date"
    // 3. Search results
      "type": "web_search_tool_result",
      "tool_use_id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
      "content": [
          "type": "web_search_result",
          "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
          "title": "Claude Shannon - Wikipedia",
          "encrypted_content": "EqgfCioIARgBIiQ3YTAwMjY1Mi1mZjM5LTQ1NGUtODgxNC1kNjNjNTk1ZWI3Y...",
          "page_age": "April 30, 2025"
      ]
      "text": "Based on the search results, ",
      "type": "text"
    // 4. Claude's response with citations
      "text": "Claude Shannon was born on April 30, 1916, in Petoskey, Michigan",
      "type": "text",
      "citations": [
          "type": "web_search_result_location",
          "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
          "title": "Claude Shannon - Wikipedia",
          "encrypted_index": "Eo8BCioIAhgBIiQyYjQ0OWJmZi1lNm..",
          "cited_text": "Claude Elwood Shannon (April 30, 1916 – February 24, 2001) was an American mathematician, electrical engineer, computer scientist, cryptographer and i..."
      ]
  ],
  "id": "msg_a930390d3a",
  "usage": {
    "input_tokens": 6039,
    "output_tokens": 931,
    "server_tool_use": {
      "web_search_requests": 1
  "stop_reason": "end_turn"

### 
Search results
Search results include:
  * `url`: The URL of the source page
  * `title`: The title of the source page
  * `page_age`: When the site was last updated
  * `encrypted_content`: Encrypted content that must be passed back in multi-turn conversations for citations

### 
Citations
Citations are always enabled for web search, and each `web_search_result_location` includes:
  * `url`: The URL of the cited source
  * `title`: The title of the cited source
  * `encrypted_index`: A reference that must be passed back for multi-turn conversations.
  * `cited_text`: Up to 150 characters of the cited content

The web search citation fields `cited_text`, `title`, and `url` do not count towards input or output token usage.
When displaying API outputs directly to end users, citations must be included to the original source. If you are making modifications to API outputs, including by reprocessing and/or combining them with your own material before displaying them to end users, display citations as appropriate based on consultation with your legal team.
### 
Errors
When the web search tool encounters an error (such as hitting rate limits), the Claude API still returns a 200 (success) response. The error is represented within the response body using the following structure:
Output

  "type": "web_search_tool_result",
  "tool_use_id": "srvtoolu_a93jad",
  "content": {
    "type": "web_search_tool_result_error",
    "error_code": "max_uses_exceeded"

These are the possible error codes:
  * `too_many_requests`: Rate limit exceeded
  * `invalid_input`: Invalid search query parameter
  * `max_uses_exceeded`: Maximum web search tool uses exceeded
  * `query_too_long`: Query exceeds maximum length
  * `unavailable`: An internal error occurred

### 
`pause_turn` stop reason
For continuing after a `pause_turn` stop reason, see [Server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools#the-server-side-loop-and-pause-turn).
Prompt caching
For caching tool definitions across turns, see [Tool use with prompt caching](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching).
Streaming
With streaming enabled, you'll receive search events as part of the stream. There will be a pause while the search executes:
Output

event: message_start
data: {"type": "message_start", "message": {"id": "msg_abc123", "type": "message"}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}

// Claude's decision to search

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "web_search"}}

// Search query streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"query\":\"latest quantum computing breakthroughs 2025\"}"}}

// Pause while search executes

// Search results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "web_search_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": [{"type": "web_search_result", "title": "Quantum Computing Breakthroughs in 2025", "url": "https://example.com"}]}}

// Claude's response with citations (omitted in this example)

Batch requests
You can include the web search tool in the [Messages Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing). Web search tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.
To protect shared capacity, the Batches API throttles web search requests per organization, so large batches with many searches might take longer to complete. You can see your organization's web search rate limit on the [Limits](https://platform.claude.com/settings/limits) page in the Claude Console; contact sales from that page to request a higher limit. Typical batch web-search workloads include enriching records with current web data, researching a large list of entities, and grounding or checking a corpus of content against live sources.
Usage and pricing
Web search usage is charged in addition to token usage:

  "usage": {
    "input_tokens": 105,
    "output_tokens": 6039,
    "cache_read_input_tokens": 7123,
    "cache_creation_input_tokens": 7345,
    "server_tool_use": {
      "web_search_requests": 1

Web search is available on the Claude API for **$10 per 1,000 searches** , plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations executed during a single turn and in subsequent conversation turns.
Each web search counts as one use, regardless of the number of results returned. If an error occurs during web search, the web search will not be billed.
Next steps
[ Server tools Shared mechanics for Anthropic-executed tools. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools)[ Tool reference Directory of all Anthropic-provided tools. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)
  * [How web search works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#how-web-search-works)
  * [When Claude searches](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#when-claude-searches)
  * [Dynamic filtering](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#dynamic-filtering)
  * [How to use web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#how-to-use-web-search)
  * [Tool definition](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#tool-definition)
  * [Max uses](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#max-uses)
  * [Domain filtering](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#domain-filtering)
  * [Localization](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#localization)
  * [Response inclusion](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#response-inclusion)
  * [Response](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#response)
  * [Search results](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#search-results)
  * [Citations](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#citations)
  * [Errors](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#errors)
  * [pause_turn stop reason](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#pause-turn-stop-reason)
  * [Prompt caching](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#prompt-caching)
  * [Streaming](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#streaming)
  * [Batch requests](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#batch-requests)
  * [Usage and pricing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#usage-and-pricing)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#next-steps)

Messages/Tools
# Web search tool
The web search tool gives Claude direct access to real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff. The response includes citations for sources drawn from search results.
The latest web search tool version (`web_search_20260318`) supports **dynamic filtering** with Claude Fable 5, Claude Opus 4.8, Claude Mythos 5, [Claude Mythos Preview](https://anthropic.com/glasswing), Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6. Claude can write and execute code to filter search results before they reach the context window, keeping only relevant information and discarding the rest. This leads to more accurate responses while reducing token consumption. `web_search_20260318` also adds [response inclusion](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool#response-inclusion) control for agentic workflows. The previous versions (`web_search_20260209` for dynamic filtering only, `web_search_20250305` for basic search) remain available.
For [Claude Mythos Preview](https://anthropic.com/glasswing), web search is supported on the Claude API, Google Cloud, and Microsoft Foundry. Web search is not available for Mythos Preview on Amazon Bedrock or [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws).
For Zero Data Retention eligibility and the `allowed_callers` workaround, see [Server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools#zdr-and-allowed-callers).
For model support, see the [Tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference).
How web search works
When you add the web search tool to your API request:
  1. Claude decides when to search based on the prompt.
  2. The API executes the searches and provides Claude with the results. This process may repeat multiple times throughout a single request.
  3. At the end of its turn, Claude provides a final response with cited sources.

### 
When Claude searches
Claude searches when the request depends on information that is current, changing, or outside its training data:
  * Recent events, news, or announcements
  * Current prices, rates, scores, or statistics
  * Information about specific organizations, people, or products that might have changed
  * Explicit requests to search or look something up

Claude answers directly without searching when the request draws on stable knowledge:
  * Established facts, math, science fundamentals, or coding concepts
  * Creative writing or brainstorming
  * Analysis of content already provided in the conversation
  * Conversational turns and greetings

Triggering is steerable through your system prompt: you can encourage Claude to search more readily or to prefer answering directly. For a hard constraint, use `max_uses` to cap the number of searches for each request.
### 
Dynamic filtering
Web search is a token-intensive task. With basic web search, Claude needs to pull search results into context, fetch full HTML from multiple websites, and reason over all of it before arriving at an answer. Often, much of this content is irrelevant, which can degrade response quality.
With `web_search_20260209` or later, Claude can write and execute code to post-process query results. Instead of reasoning over full HTML files, Claude dynamically filters search results before loading them into context, keeping only what's relevant and discarding the rest.
Dynamic filtering is particularly effective for:
  * Searching through technical documentation
  * Literature review and citation verification
  * Technical research
  * Response grounding and verification

Dynamic filtering requires the [code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) to be enabled. The web search tool (with and without dynamic filtering) is available on the Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry). On Google Cloud, only the basic web search tool (without dynamic filtering) is available. Web search is not available on Amazon Bedrock.
To enable dynamic filtering, use `web_search_20260209` or any later version. The following examples use `web_search_20260209`:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio.",
    ],
    tools=[{"type": "web_search_20260209", "name": "web_search"}],
)
print(response)

How to use web search
Your organization's administrator must enable web search in the [Claude Console](https://platform.claude.com/settings/privacy).
Provide the web search tool in your API request:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "What's the weather in NYC?"}],
    tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}],
)
print(response)

Tool definition
The web search tool supports the following parameters:
JSON

  "type": "web_search_20250305",
  "name": "web_search",

  // Optional: Limit the number of searches per request
  "max_uses": 5,

  // Optional: Only include results from these domains
  "allowed_domains": ["example.com", "trusteddomain.org"],

  // Optional: Never include results from these domains
  "blocked_domains": ["untrustedsource.com"],

  // Optional: Localize search results
  "user_location": {
    "type": "approximate",
    "city": "San Francisco",
    "region": "California",
    "country": "US",
    "timezone": "America/Los_Angeles"

### 
Max uses
The `max_uses` parameter limits the number of searches performed. If Claude attempts more searches than allowed, the `web_search_tool_result` is an error with the `max_uses_exceeded` error code.
Simple factual queries typically use 1–3 searches; comparative or multi-entity research can use 10 or more. For latency-sensitive lookups, `max_uses: 3` bounds cost while rarely truncating. For research agents, set `max_uses` to 15–20 or omit it entirely.
### 
Domain filtering
For domain filtering with `allowed_domains` and `blocked_domains`, see [Server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools#domain-filtering).
### 
Localization
The `user_location` parameter allows you to localize search results based on a user's location.
  * `type`: The type of location (must be `approximate`)
  * `city`: The city name
  * `region`: The region or state
  * `country`: The country
  * `timezone`: The [IANA timezone ID](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

### 
Response inclusion
Requires `web_search_20260318` or later.
The `response_inclusion` parameter controls how search result blocks appear in the API response when the result was consumed by a completed [code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) call in the same turn. Set `"response_inclusion": "excluded"` to drop those nested `server_tool_use` and result block pairs entirely from the response, reducing output token costs for agentic workflows that don't need to echo raw search content back to the client. The default is `"full"`. Results from direct calls, or from code execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

  "tools": [
      "type": "web_search_20260318",
      "name": "web_search",
      "response_inclusion": "excluded"
  ]

Response
Here's an example response structure:
Output

  "role": "assistant",
  "content": [
    // 1. Claude's decision to search
      "type": "text",
      "text": "I'll search for when Claude Shannon was born."
    // 2. The search query used
      "type": "server_tool_use",
      "id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
      "name": "web_search",
      "input": {
        "query": "claude shannon birth date"
    // 3. Search results
      "type": "web_search_tool_result",
      "tool_use_id": "srvtoolu_01WYG3ziw53XMcoyKL4XcZmE",
      "content": [
          "type": "web_search_result",
          "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
          "title": "Claude Shannon - Wikipedia",
          "encrypted_content": "EqgfCioIARgBIiQ3YTAwMjY1Mi1mZjM5LTQ1NGUtODgxNC1kNjNjNTk1ZWI3Y...",
          "page_age": "April 30, 2025"
      ]
      "text": "Based on the search results, ",
      "type": "text"
    // 4. Claude's response with citations
      "text": "Claude Shannon was born on April 30, 1916, in Petoskey, Michigan",
      "type": "text",
      "citations": [
          "type": "web_search_result_location",
          "url": "https://en.wikipedia.org/wiki/Claude_Shannon",
          "title": "Claude Shannon - Wikipedia",
          "encrypted_index": "Eo8BCioIAhgBIiQyYjQ0OWJmZi1lNm..",
          "cited_text": "Claude Elwood Shannon (April 30, 1916 – February 24, 2001) was an American mathematician, electrical engineer, computer scientist, cryptographer and i..."
      ]
  ],
  "id": "msg_a930390d3a",
  "usage": {
    "input_tokens": 6039,
    "output_tokens": 931,
    "server_tool_use": {
      "web_search_requests": 1
  "stop_reason": "end_turn"

### 
Search results
Search results include:
  * `url`: The URL of the source page
  * `title`: The title of the source page
  * `page_age`: When the site was last updated
  * `encrypted_content`: Encrypted content that must be passed back in multi-turn conversations for citations

### 
Citations
Citations are always enabled for web search, and each `web_search_result_location` includes:
  * `url`: The URL of the cited source
  * `title`: The title of the cited source
  * `encrypted_index`: A reference that must be passed back for multi-turn conversations.
  * `cited_text`: Up to 150 characters of the cited content

The web search citation fields `cited_text`, `title`, and `url` do not count towards input or output token usage.
When displaying API outputs directly to end users, citations must be included to the original source. If you are making modifications to API outputs, including by reprocessing and/or combining them with your own material before displaying them to end users, display citations as appropriate based on consultation with your legal team.
### 
Errors
When the web search tool encounters an error (such as hitting rate limits), the Claude API still returns a 200 (success) response. The error is represented within the response body using the following structure:
Output

  "type": "web_search_tool_result",
  "tool_use_id": "srvtoolu_a93jad",
  "content": {
    "type": "web_search_tool_result_error",
    "error_code": "max_uses_exceeded"

These are the possible error codes:
  * `too_many_requests`: Rate limit exceeded
  * `invalid_input`: Invalid search query parameter
  * `max_uses_exceeded`: Maximum web search tool uses exceeded
  * `query_too_long`: Query exceeds maximum length
  * `unavailable`: An internal error occurred

### 
`pause_turn` stop reason
For continuing after a `pause_turn` stop reason, see [Server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools#the-server-side-loop-and-pause-turn).
Prompt caching
For caching tool definitions across turns, see [Tool use with prompt caching](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching).
Streaming
With streaming enabled, you'll receive search events as part of the stream. There will be a pause while the search executes:
Output

event: message_start
data: {"type": "message_start", "message": {"id": "msg_abc123", "type": "message"}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "text", "text": ""}}

// Claude's decision to search

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "web_search"}}

// Search query streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"query\":\"latest quantum computing breakthroughs 2025\"}"}}

// Pause while search executes

// Search results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "web_search_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": [{"type": "web_search_result", "title": "Quantum Computing Breakthroughs in 2025", "url": "https://example.com"}]}}

// Claude's response with citations (omitted in this example)

Batch requests
You can include the web search tool in the [Messages Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing). Web search tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.
To protect shared capacity, the Batches API throttles web search requests per organization, so large batches with many searches might take longer to complete. You can see your organization's web search rate limit on the [Limits](https://platform.claude.com/settings/limits) page in the Claude Console; contact sales from that page to request a higher limit. Typical batch web-search workloads include enriching records with current web data, researching a large list of entities, and grounding or checking a corpus of content against live sources.
Usage and pricing
Web search usage is charged in addition to token usage:

  "usage": {
    "input_tokens": 105,
    "output_tokens": 6039,
    "cache_read_input_tokens": 7123,
    "cache_creation_input_tokens": 7345,
    "server_tool_use": {
      "web_search_requests": 1

Web search is available on the Claude API for **$10 per 1,000 searches** , plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations executed during a single turn and in subsequent conversation turns.
Each web search counts as one use, regardless of the number of results returned. If an error occurs during web search, the web search will not be billed.
Next steps
[ Server tools Shared mechanics for Anthropic-executed tools. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools)[ Tool reference Directory of all Anthropic-provided tools. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)
