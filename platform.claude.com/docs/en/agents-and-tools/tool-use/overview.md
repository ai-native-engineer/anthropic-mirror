<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview -->

# Tool use with Claude
Connect Claude to external tools and APIs. Learn where tools execute and how the agentic loop works.
Tool use lets Claude call functions you define or that Anthropic provides. Claude decides when to call a tool based on the user's request and the tool's description, then returns a structured call that your application executes (client tools) or that Anthropic executes (server tools).
Here's the simplest example using a server tool, where Anthropic handles execution:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[{"type": "web_search_20260209", "name": "web_search"}],
    messages=[{"role": "user", "content": "What's the latest on the Mars rover?"}],
)
print(response.content)

* * *
How tool use works
Tools differ primarily by where the code executes. **Client tools** (including user-defined tools and Anthropic-schema tools like bash and text_editor) run in your application: Claude responds with `stop_reason: "tool_use"` and one or more `tool_use` blocks, your code executes the operation, and you send back a `tool_result`. **Server tools** (web_search, code_execution, web_fetch, tool_search) run on Anthropic's infrastructure: you see the results directly without handling execution.
For the full conceptual model including the agentic loop and when to choose each approach, see [How tool use works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works).
For connecting to MCP servers, see the [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector). For building your own MCP client, see [modelcontextprotocol.io](https://modelcontextprotocol.io/docs/develop/build-client).

**Guarantee schema conformance with strict tool use**
Add `strict: true` to your tool definitions to ensure Claude's tool calls always match your schema exactly. See [Strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use).
Tool access is one of the most effective capabilities you can give an agent. On benchmarks like [LAB-Bench FigQA](https://lab-bench.org/) (scientific figure interpretation) and [SWE-bench](https://www.swebench.com/) (real-world software engineering), adding even basic tools produces large gains, often surpassing human expert baselines.
* * *
When Claude uses tools
With the default `tool_choice` of `{"type": "auto"}`, Claude decides on each turn whether to call a tool or respond directly. It calls a tool when the request maps to that tool's described capability and the answer isn't already in context. It responds directly for stable knowledge, creative tasks, and conversational turns.
This boundary is steerable through your system prompt. If Claude isn't calling tools when you expect, a light instruction like `"Use the tools to investigate before responding."` measurably increases tool use. A stronger form like `"Always call a tool first before responding."` pushes further. Conversely, `"Use your judgment about whether to call a tool or respond directly."` keeps triggering behavior conservative.
For a hard guarantee rather than a nudge, use [`tool_choice`](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#forcing-tool-use).
Each server tool's page describes its own trigger boundary in more detail. See for example [the web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) or [the code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool).
* * *
Tool use examples
For a complete hands-on walkthrough, see the [tutorial](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent). For reference examples of individual concepts, see [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) and [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).
### What happens when Claude needs more information
* * *
Pricing
Tool use requests are priced based on:
  1. The total number of input tokens sent to the model (including in the `tools` parameter)
  2. The number of output tokens generated
  3. For server-side tools, additional usage-based pricing (e.g., web search charges per search performed)

Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage.
The additional tokens from tool use come from:
  * The `tools` parameter in API requests (tool names, descriptions, and schemas)
  * `tool_use` content blocks in API requests and responses
  * `tool_result` content blocks in API requests

When you use `tools`, the API also automatically includes a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no `tools` are provided, then a tool choice of `none` uses 0 additional system prompt tokens.  
| Model  | Tool choice  | Tool use system prompt token count  |  
| --- | --- | --- |  
| Claude Opus 4.8  |  `auto`, `none`
* * *
`any`, `tool`  | 290 tokens
* * *
410 tokens  |  
| Claude Opus 4.7  |  `auto`, `none`
* * *
`any`, `tool`  | 675 tokens
* * *
804 tokens  |  
| Claude Opus 4.6  |  `auto`, `none`
* * *
`any`, `tool`  | 497 tokens
* * *
589 tokens  |  
| Claude Opus 4.5  |  `auto`, `none`
* * *
`any`, `tool`  | 496 tokens
* * *
588 tokens  |  
| Claude Opus 4.1 ([deprecated](https://platform.claude.com/docs/en/about-claude/model-deprecations))  |  `auto`, `none`
* * *
`any`, `tool`  | 313 tokens
* * *
315 tokens  |  
| Claude Opus 4 ([retired, except on Google Cloud](https://platform.claude.com/docs/en/about-claude/model-deprecations))  |  `auto`, `none`
* * *
`any`, `tool`  | 313 tokens
* * *
315 tokens  |  
| Claude Sonnet 4.6  |  `auto`, `none`
* * *
`any`, `tool`  | 497 tokens
* * *
589 tokens  |  
| Claude Sonnet 4.5  |  `auto`, `none`
* * *
`any`, `tool`  | 496 tokens
* * *
588 tokens  |  
| Claude Sonnet 4 ([retired, except on Bedrock and Google Cloud](https://platform.claude.com/docs/en/about-claude/model-deprecations))  |  `auto`, `none`
* * *
`any`, `tool`  | 313 tokens
* * *
315 tokens  |  
| Claude Haiku 4.5  |  `auto`, `none`
* * *
`any`, `tool`  | 496 tokens
* * *
588 tokens  |  
| Claude Haiku 3.5 ([retired, except on Bedrock and Google Cloud](https://platform.claude.com/docs/en/about-claude/model-deprecations))  |  `auto`, `none`
* * *
`any`, `tool`  | 264 tokens
* * *
355 tokens  |  
These token counts are added to your normal input and output tokens to calculate the total cost of a request.
Refer to the [models overview table](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison) for current per-model prices.
When you send a tool use prompt, like any other API request, the response includes both input and output token counts in the reported `usage` metrics.
* * *
Next steps
[ How tool use works Understand the tool use loop, where tools execute, and when to use tools instead of prose. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)[  Tutorial: Build a tool-using agent A guided walkthrough from a single tool call to a production-ready agentic loop. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[  Tool reference Directory of Anthropic-provided tools and reference for optional tool definition properties. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)
  * [How tool use works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview#how-tool-use-works)
  * [When Claude uses tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview#when-claude-uses-tools)
  * [Tool use examples](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview#tool-use-examples)
  * [Pricing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview#pricing)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview#next-steps)

Messages/Tools
# Tool use with Claude
Connect Claude to external tools and APIs. Learn where tools execute and how the agentic loop works.
Tool use lets Claude call functions you define or that Anthropic provides. Claude decides when to call a tool based on the user's request and the tool's description, then returns a structured call that your application executes (client tools) or that Anthropic executes (server tools).
Here's the simplest example using a server tool, where Anthropic handles execution:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[{"type": "web_search_20260209", "name": "web_search"}],
    messages=[{"role": "user", "content": "What's the latest on the Mars rover?"}],
)
print(response.content)

* * *
How tool use works
Tools differ primarily by where the code executes. **Client tools** (including user-defined tools and Anthropic-schema tools like bash and text_editor) run in your application: Claude responds with `stop_reason: "tool_use"` and one or more `tool_use` blocks, your code executes the operation, and you send back a `tool_result`. **Server tools** (web_search, code_execution, web_fetch, tool_search) run on Anthropic's infrastructure: you see the results directly without handling execution.
For the full conceptual model including the agentic loop and when to choose each approach, see [How tool use works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works).
For connecting to MCP servers, see the [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector). For building your own MCP client, see [modelcontextprotocol.io](https://modelcontextprotocol.io/docs/develop/build-client).

**Guarantee schema conformance with strict tool use**
Add `strict: true` to your tool definitions to ensure Claude's tool calls always match your schema exactly. See [Strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use).
Tool access is one of the most effective capabilities you can give an agent. On benchmarks like [LAB-Bench FigQA](https://lab-bench.org/) (scientific figure interpretation) and [SWE-bench](https://www.swebench.com/) (real-world software engineering), adding even basic tools produces large gains, often surpassing human expert baselines.
* * *
When Claude uses tools
With the default `tool_choice` of `{"type": "auto"}`, Claude decides on each turn whether to call a tool or respond directly. It calls a tool when the request maps to that tool's described capability and the answer isn't already in context. It responds directly for stable knowledge, creative tasks, and conversational turns.
This boundary is steerable through your system prompt. If Claude isn't calling tools when you expect, a light instruction like `"Use the tools to investigate before responding."` measurably increases tool use. A stronger form like `"Always call a tool first before responding."` pushes further. Conversely, `"Use your judgment about whether to call a tool or respond directly."` keeps triggering behavior conservative.
For a hard guarantee rather than a nudge, use [`tool_choice`](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#forcing-tool-use).
Each server tool's page describes its own trigger boundary in more detail. See for example [the web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) or [the code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool).
* * *
Tool use examples
For a complete hands-on walkthrough, see the [tutorial](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent). For reference examples of individual concepts, see [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools) and [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).
### What happens when Claude needs more information
* * *
Pricing
Tool use requests are priced based on:
  1. The total number of input tokens sent to the model (including in the `tools` parameter)
  2. The number of output tokens generated
  3. For server-side tools, additional usage-based pricing (e.g., web search charges per search performed)

Client-side tools are priced the same as any other Claude API request, while server-side tools may incur additional charges based on their specific usage.
The additional tokens from tool use come from:
  * The `tools` parameter in API requests (tool names, descriptions, and schemas)
  * `tool_use` content blocks in API requests and responses
  * `tool_result` content blocks in API requests

When you use `tools`, the API also automatically includes a special system prompt for the model which enables tool use. The number of tool use tokens required for each model are listed below (excluding the additional tokens listed above). Note that the table assumes at least 1 tool is provided. If no `tools` are provided, then a tool choice of `none` uses 0 additional system prompt tokens.  
| Model  | Tool choice  | Tool use system prompt token count  |  
| --- | --- | --- |  
| Claude Opus 4.8  |  `auto`, `none`
* * *
`any`, `tool`  | 290 tokens
* * *
410 tokens  |  
| Claude Opus 4.7  |  `auto`, `none`
* * *
`any`, `tool`  | 675 tokens
* * *
804 tokens  |  
| Claude Opus 4.6  |  `auto`, `none`
* * *
`any`, `tool`  | 497 tokens
* * *
589 tokens  |  
| Claude Opus 4.5  |  `auto`, `none`
* * *
`any`, `tool`  | 496 tokens
* * *
588 tokens  |  
| Claude Opus 4.1 ([deprecated](https://platform.claude.com/docs/en/about-claude/model-deprecations))  |  `auto`, `none`
* * *
`any`, `tool`  | 313 tokens
* * *
315 tokens  |  
| Claude Opus 4 ([retired, except on Google Cloud](https://platform.claude.com/docs/en/about-claude/model-deprecations))  |  `auto`, `none`
* * *
`any`, `tool`  | 313 tokens
* * *
315 tokens  |  
| Claude Sonnet 4.6  |  `auto`, `none`
* * *
`any`, `tool`  | 497 tokens
* * *
589 tokens  |  
| Claude Sonnet 4.5  |  `auto`, `none`
* * *
`any`, `tool`  | 496 tokens
* * *
588 tokens  |  
| Claude Sonnet 4 ([retired, except on Bedrock and Google Cloud](https://platform.claude.com/docs/en/about-claude/model-deprecations))  |  `auto`, `none`
* * *
`any`, `tool`  | 313 tokens
* * *
315 tokens  |  
| Claude Haiku 4.5  |  `auto`, `none`
* * *
`any`, `tool`  | 496 tokens
* * *
588 tokens  |  
| Claude Haiku 3.5 ([retired, except on Bedrock and Google Cloud](https://platform.claude.com/docs/en/about-claude/model-deprecations))  |  `auto`, `none`
* * *
`any`, `tool`  | 264 tokens
* * *
355 tokens  |  
These token counts are added to your normal input and output tokens to calculate the total cost of a request.
Refer to the [models overview table](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison) for current per-model prices.
When you send a tool use prompt, like any other API request, the response includes both input and output token counts in the reported `usage` metrics.
* * *
Next steps
[ How tool use works Understand the tool use loop, where tools execute, and when to use tools instead of prose. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)[  Tutorial: Build a tool-using agent A guided walkthrough from a single tool call to a production-ready agentic loop. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[  Tool reference Directory of Anthropic-provided tools and reference for optional tool definition properties. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)
