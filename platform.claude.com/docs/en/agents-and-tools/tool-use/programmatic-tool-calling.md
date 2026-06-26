<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling -->

# Programmatic tool calling
Programmatic tool calling allows Claude to write code that calls your tools programmatically within a [code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) container, rather than requiring round trips through the model for each tool invocation. This reduces latency for multi-tool workflows and decreases token consumption by allowing Claude to filter or process data before it reaches the model's context window. On agentic search benchmarks like [BrowseComp](https://arxiv.org/abs/2504.12516) and [DeepSearchQA](https://github.com/google-deepmind/deepsearchqa), which test multi-step web research and complex information retrieval, adding programmatic tool calling on top of basic search tools improved performance by an average of 11% while using 24% fewer input tokens (see [Improved web search with dynamic filtering](https://claude.com/blog/improved-web-search-with-dynamic-filtering)).
The difference compounds fast in real workflows. Consider checking budget compliance across 20 employees: the traditional approach requires 20 separate model round-trips, pulling thousands of expense line items into the context along the way. With programmatic tool calling, a single script runs all 20 lookups, filters the results, and returns only the employees who exceeded their limits, shrinking what Claude needs to reason over from hundreds of kilobytes down to a handful of lines.

For a deeper look at the inference and context costs that programmatic tool calling addresses, see [Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use).
This feature requires the code execution tool to be enabled.
This feature is **not** eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). Data is retained according to the feature's standard retention policy.
Model compatibility
Programmatic tool calling requires `code_execution_20260120` or later, which is supported on the following models:  
| Model |  
| --- |  
| Claude Fable 5 (claude-fable-5) |  
| Claude Mythos 5 (claude-mythos-5) |  
| Claude Opus 4.8 (claude-opus-4-8) |  
| Claude Opus 4.7 (claude-opus-4-7) |  
| Claude Opus 4.6 (claude-opus-4-6) |  
| Claude Sonnet 4.6 (claude-sonnet-4-6) |  
| Claude Opus 4.5 (claude-opus-4-5-20251101) |  
| Claude Sonnet 4.5 (claude-sonnet-4-5-20250929) |  
For the full code execution tool version matrix, see the [code execution tool model compatibility table](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#model-compatibility). Programmatic tool calling is available on the Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry). It is not currently available on Amazon Bedrock or Google Cloud.
Quick start
Here's an example where Claude programmatically queries a database multiple times and aggregates results:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": "Query sales data for the West, East, and Central regions, then tell me which region had the highest revenue",
    ],
    tools=[
        {"type": "code_execution_20260120", "name": "code_execution"},
            "name": "query_database",
            "description": "Execute a SQL query against the sales database. Returns a list of rows as JSON objects.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "sql": {"type": "string", "description": "SQL query to execute"}
                "required": ["sql"],
            "allowed_callers": ["code_execution_20260120"],
    ],
)

print(response)

How programmatic tool calling works
When you configure a tool to be callable from code execution and Claude decides to use that tool:
  1. Claude writes Python code that invokes the tool as a function, potentially including multiple tool calls and pre/post-processing logic
  2. Claude runs this code in a sandboxed container through code execution
  3. When a tool function is called, code execution pauses and the API returns a `tool_use` block
  4. You provide the tool result, and code execution continues (intermediate results are not loaded into Claude's context window)
  5. Once all code execution completes, Claude receives the final output and continues working on the task

This approach is particularly useful for:
  * **Large data processing:** Filter or aggregate tool results before they reach Claude's context
  * **Multi-step workflows:** Save tokens and latency by calling tools serially or in a loop without sampling Claude in-between tool calls
  * **Conditional logic:** Make decisions based on intermediate tool results

Custom tools are converted to async Python functions to support parallel tool calling. When Claude writes code that calls your tools, it uses `await` (for example, `result = await query_database("<sql>")`) and automatically includes the appropriate async wrapper function.
The async wrapper is omitted from code examples in this documentation for clarity.
Core concepts
### 
The `allowed_callers` field
The `allowed_callers` field specifies which contexts can invoke a tool:

  "name": "query_database",
  "description": "Execute a SQL query against the database",
  "input_schema": {
    // ...
  "allowed_callers": ["code_execution_20260120"]

**Possible values:**
  * `["direct"]` - Claude is guided to call this tool directly (default if omitted)
  * `["code_execution_20260120"]` - Claude is guided to call this tool only from within code execution
  * `["direct", "code_execution_20260120"]` - Claude may call this tool directly or from within code execution


Choose either `["direct"]` or `["code_execution_20260120"]` for each tool rather than enabling both, as this provides clearer guidance to Claude for how best to use the tool.
`allowed_callers` controls how the tool is presented to Claude and is validated against `tool_choice`, but it is not a hard API-level block on direct invocation. Claude is strongly guided to respect it, but your client should still be prepared to handle a direct `tool_use` for any tool it defines. Do not rely on `allowed_callers` as a security boundary.
### 
The `caller` field in responses
Every tool use block includes a `caller` field indicating how it was invoked:
**Direct invocation (traditional tool use):**

  "type": "tool_use",
  "id": "toolu_abc123",
  "name": "query_database",
  "input": { "sql": "<sql>" },
  "caller": { "type": "direct" }

**Programmatic invocation:**

  "type": "tool_use",
  "id": "toolu_xyz789",
  "name": "query_database",
  "input": { "sql": "<sql>" },
  "caller": {
    "type": "code_execution_20260120",
    "tool_id": "srvtoolu_abc123"

The `tool_id` references the code execution tool that made the programmatic call.
### 
Container lifecycle
Programmatic tool calling uses the same containers as code execution:
  * **Container creation:** A new container is created for each request unless you reuse an existing one
  * **Expiration:** Containers have a 30-day maximum lifetime and are cleaned up after 4.5 minutes of idle time
  * **Container ID:** Returned in responses in the `container` field
  * **Reuse:** Pass the container ID to maintain state across requests


When a tool is called programmatically and the container is waiting for your tool result, you must respond before the container expires. Monitor the `expires_at` field. If the container expires, Claude may treat the tool call as timed out and retry it.
Example workflow
Here's how a complete programmatic tool calling flow works:
### 
Step 1: Initial request
Send a request with code execution and a tool that allows programmatic calling. To enable programmatic calling, add the `allowed_callers` field to your tool definition.
Provide detailed descriptions of your tool's output format in the tool description. If you specify that the tool returns JSON, Claude attempts to deserialize and process the result in code. The more detail you provide about the output schema, the better Claude can handle the response programmatically.
The request shape is identical to the [Quick start](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#quick-start) example: include `code_execution` in your tools list, add `allowed_callers: ["code_execution_20260120"]` to any tool you want Claude to invoke from code, and send your user message. The remaining steps in this workflow use the user message `"Query customer purchase history from the last quarter and identify our top 5 customers by revenue"`.
### 
Step 2: API response with tool call
Claude writes code that calls your tool. The API pauses and returns:
Output

  "role": "assistant",
  "content": [
      "type": "text",
      "text": "I'll query the purchase history and analyze the results."
      "type": "server_tool_use",
      "id": "srvtoolu_abc123",
      "name": "code_execution",
      "input": {
        "code": "results = await query_database('<sql>')\ntop_customers = sorted(results, key=lambda x: x['revenue'], reverse=True)[:5]\nprint(f'Top 5 customers: {top_customers}')"
      "type": "tool_use",
      "id": "toolu_def456",
      "name": "query_database",
      "input": { "sql": "<sql>" },
      "caller": {
        "type": "code_execution_20260120",
        "tool_id": "srvtoolu_abc123"
  ],
  "container": {
    "id": "container_xyz789",
    "expires_at": "2026-01-20T14:30:00Z"
  "stop_reason": "tool_use"

### 
Step 3: Provide tool result
Include the full conversation history plus your tool result:
CLIPythonTypeScriptC#GoJavaPHPRuby

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    container="container_xyz789",  # Reuse the container
    messages=[
            "role": "user",
            "content": "Query customer purchase history from the last quarter and identify our top 5 customers by revenue",
            "role": "assistant",
            "content": [
                    "type": "text",
                    "text": "I'll query the purchase history and analyze the results.",
                    "type": "server_tool_use",
                    "id": "srvtoolu_abc123",
                    "name": "code_execution",
                    "input": {"code": "..."},
                    "type": "tool_use",
                    "id": "toolu_def456",
                    "name": "query_database",
                    "input": {"sql": "<sql>"},
                    "caller": {
                        "type": "code_execution_20260120",
                        "tool_id": "srvtoolu_abc123",
            ],
            "role": "user",
            "content": [
                    "type": "tool_result",
                    "tool_use_id": "toolu_def456",
                    "content": '[{"customer_id": "C1", "revenue": 45000}, {"customer_id": "C2", "revenue": 38000}, ...]',
            ],
    ],
    tools=[...],
)

print(response)

### 
Step 4: Next tool call or completion
The code execution continues and processes the results. If additional tool calls are needed, repeat Step 3 until all tool calls are satisfied.
### 
Step 5: Final response
Once the code execution completes, Claude provides the final response:
Output

  "content": [
      "type": "code_execution_tool_result",
      "tool_use_id": "srvtoolu_abc123",
      "content": {
        "type": "code_execution_result",
        "stdout": "Top 5 customers: [{'customer_id': 'C1', 'revenue': 45000}, {'customer_id': 'C2', 'revenue': 38000}, {'customer_id': 'C5', 'revenue': 32000}, {'customer_id': 'C8', 'revenue': 28500}, {'customer_id': 'C3', 'revenue': 24000}]",
        "stderr": "",
        "return_code": 0,
        "content": []
      "type": "text",
      "text": "I've analyzed the purchase history from last quarter. Your top 5 customers generated $167,500 in total revenue, with Customer C1 leading at $45,000."
  ],
  "stop_reason": "end_turn"

Advanced patterns
### 
Batch processing with loops
Claude can write code that processes multiple items efficiently:

async def _claude_code():
    regions = ["West", "East", "Central", "North", "South"]
    results = {}
    for region in regions:
        data = await query_database(f"<sql for {region}>")
        results[region] = sum(row["revenue"] for row in data)

    # Process results programmatically
    top_region = max(results.items(), key=lambda x: x[1])
    print(f"Top region: {top_region[0]} with ${top_region[1]:,} in revenue")

This pattern:
  * Reduces model round-trips from N (one per region) to 1
  * Processes large result sets programmatically before returning to Claude
  * Saves tokens by only returning aggregated conclusions instead of raw data

### 
Early termination
Claude can stop processing as soon as success criteria are met:

async def _claude_code():
    endpoints = ["us-east", "eu-west", "apac"]
    for endpoint in endpoints:
        status = await check_health(endpoint)
        if status == "healthy":
            print(f"Found healthy endpoint: {endpoint}")
            break  # Stop early, don't check remaining

### 
Conditional tool selection

async def _claude_code():
    file_info = await get_file_info(path)
    if file_info["size"] < 10000:
        content = await read_full_file(path)
    else:
        content = await read_file_summary(path)
    print(content)

### 
Data filtering

async def _claude_code():
    logs = await fetch_logs(server_id)
    errors = [log for log in logs if "ERROR" in log]
    print(f"Found {len(errors)} errors")
    for error in errors[-10:]:  # Only return last 10 errors
        print(error)

Response format
### 
Programmatic tool call
When code execution calls a tool:

  "type": "tool_use",
  "id": "toolu_abc123",
  "name": "query_database",
  "input": { "sql": "<sql>" },
  "caller": {
    "type": "code_execution_20260120",
    "tool_id": "srvtoolu_xyz789"

### 
Tool result handling
Your tool result is passed back to the running code:

  "role": "user",
  "content": [
      "type": "tool_result",
      "tool_use_id": "toolu_abc123",
      "content": "[{\"customer_id\": \"C1\", \"revenue\": 45000, \"orders\": 23}, {\"customer_id\": \"C2\", \"revenue\": 38000, \"orders\": 18}, ...]"
  ]

### 
Code execution completion
When all tool calls are satisfied and code completes:

  "type": "code_execution_tool_result",
  "tool_use_id": "srvtoolu_xyz789",
  "content": {
    "type": "code_execution_result",
    "stdout": "Analysis complete. Top 5 customers identified from 847 total records.",
    "stderr": "",
    "return_code": 0,
    "content": []

Error handling
### 
Common errors  
| Error  | Description  | Solution  |  
| --- | --- | --- |  
| `invalid_tool_input`  | Tool input doesn't match schema  | Validate your tool's input_schema  |  
|  `invalid_request_error` (on `tool_choice`)  |  `tool_choice` names a tool whose `allowed_callers` does not include `"direct"`  | Either add `"direct"` to that tool's `allowed_callers`, or remove the tool from `tool_choice` and let Claude invoke it from code  |  
### 
Container expiration during tool call
If your tool takes too long to respond, the code execution receives a `TimeoutError`. Claude sees this in stderr and typically retries:

  "type": "code_execution_tool_result",
  "tool_use_id": "srvtoolu_abc123",
  "content": {
    "type": "code_execution_result",
    "stdout": "",
    "stderr": "TimeoutError: Calling tool ['query_database'] timed out.",
    "return_code": 0,
    "content": []

To prevent timeouts:
  * Monitor the `expires_at` field in responses
  * Implement timeouts for your tool execution
  * Consider breaking long operations into smaller chunks

### 
Tool execution errors
If your tool returns an error:

  "type": "tool_result",
  "tool_use_id": "toolu_abc123",
  "content": "Error: Query timeout - table lock exceeded 30 seconds"

Claude's code receives this error and can handle it appropriately.
Constraints and limitations
### 
Feature incompatibilities
  * **Structured outputs:** Tools with `strict: true` are not supported with programmatic calling
  * **Tool choice:** You cannot force programmatic calling of a specific tool through `tool_choice`
  * **Parallel tool use:** `disable_parallel_tool_use: true` is not supported with programmatic calling

### 
Tool restrictions
The following tools cannot be called programmatically:
  * Tools provided by an [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)

### 
Message formatting restrictions
When responding to programmatic tool calls, there are strict formatting requirements:
**Tool result only responses:** If there are pending programmatic tool calls waiting for results, your response message must contain **only** `tool_result` blocks. You cannot include any text content, even after the tool results.
Invalid - Cannot include text when responding to programmatic tool calls:

  "role": "user",
  "content": [
      "type": "tool_result",
      "tool_use_id": "toolu_01",
      "content": "[{\"customer_id\": \"C1\", \"revenue\": 45000}]"
    { "type": "text", "text": "What should I do next?" }
  ]

Valid - Only tool results when responding to programmatic tool calls:

  "role": "user",
  "content": [
      "type": "tool_result",
      "tool_use_id": "toolu_01",
      "content": "[{\"customer_id\": \"C1\", \"revenue\": 45000}]"
  ]

This restriction only applies when responding to programmatic (code execution) tool calls. For regular client-side tool calls, you can include text content after tool results.
### 
Rate limits
Programmatic tool calls are subject to the same rate limits as regular tool calls. Each tool call from code execution counts as a separate invocation.
### 
Validate tool results before use
When implementing user-defined tools that will be called programmatically:
  * **Tool results are returned as strings:** They can contain any content, including code snippets or executable commands that may be processed by the execution environment.
  * **Validate external tool results:** If your tool returns data from external sources or accepts user input, be aware of code injection risks if the output will be interpreted or executed as code.

Token efficiency
Programmatic tool calling can significantly reduce token consumption:
  * **Tool results from programmatic calls are not added to Claude's context** - only the final code output is
  * **Intermediate processing happens in code** - filtering, aggregation, and other transformations don't consume model tokens
  * **Multiple tool calls in one code execution** - reduces overhead compared to separate model turns

For example, calling 10 tools directly uses ~10x the tokens of calling them programmatically and returning a summary.
In Anthropic's internal evaluations on a production Claude model:
  * On a 75-tool project-management agent benchmark, enabling programmatic tool calling reduced billed input tokens by roughly 38% with no change in task accuracy.
  * On [τ²-bench](https://arxiv.org/abs/2506.07982) (airline, retail, and telecom domains), where each turn makes one or two sequential tool calls, programmatic tool calling left scores unchanged and cost roughly 8% more. Sequential single-call workflows do not benefit.
  * Across production API traffic, requests whose `tools` array contains 10 to 49 tool definitions see typical token savings of 20% to 40% with programmatic tool calling enabled.

Actual savings vary with workload shape; see [When to use programmatic calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#when-to-use-programmatic-calling).
Usage and pricing
Programmatic tool calling uses the same pricing as code execution. See the [code execution pricing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#usage-and-pricing) for details.
Token counting for programmatic tool calls: Tool results from programmatic invocations do not count toward your input/output token usage. Only the final code execution result and Claude's response count.
Best practices
### 
Tool design
  * **Provide detailed output descriptions:** Because Claude deserializes tool results in code, clearly document the format (JSON structure and field types)
  * **Return structured data:** JSON or other easily parseable formats work best for programmatic processing
  * **Keep responses concise:** Return only necessary data to minimize processing overhead

### 
When to use programmatic calling
Programmatic tool calling trades a small fixed overhead (container startup, script generation) for large savings on tool-result tokens and model round-trips. Whether that trade pays off depends on workload shape.
**Strong fit:**
  * Fan-out or parallel operations across many items (for example, checking 50 endpoints or looking up 20 records)
  * Large tool results that can be filtered, aggregated, or summarized before reaching Claude's context
  * Agentic search and retrieval, where iterative querying and result filtering dominate the workflow

**Weak fit:**
  * Strictly sequential workflows where each call depends on Claude reasoning over the previous result, because the script cannot skip the model round-trip in that case
  * A small number of tool calls with small responses, especially on the first turn of a conversation, where container and script overhead can exceed the savings
  * Tools that require immediate user feedback between calls

If you are unsure, measure billed input tokens with and without `allowed_callers` on a representative sample of your traffic before enabling it broadly.
### 
Performance optimization
  * **Reuse containers** when making multiple related requests to maintain state
  * **Batch similar operations** in a single code execution when possible

Troubleshooting
### 
Common issues
**`invalid_request_error`when setting`tool_choice`**
  * `tool_choice` cannot name a tool whose `allowed_callers` omits `"direct"`. Either add `"direct"` to that tool's `allowed_callers`, or remove the tool from `tool_choice` and let Claude invoke it from code.

**Container expiration**
  * Ensure you respond to tool calls before the container idles out (4.5 minutes of inactivity; 30-day hard maximum)
  * Monitor the `expires_at` field in responses
  * Consider implementing faster tool execution

**Tool result not parsed correctly**
  * Ensure your tool returns string data that Claude can deserialize
  * Provide clear output format documentation in your tool description

### 
Debugging tips
  1. **Log all tool calls and results** to track the flow
  2. **Check the`caller` field** to confirm programmatic invocation
  3. **Monitor container IDs** to ensure proper reuse
  4. **Test tools independently** before enabling programmatic calling

Why programmatic tool calling works
Claude's training includes extensive exposure to code, making it effective at reasoning through and chaining function calls. When tools are presented as callable functions within a code execution environment, Claude can leverage this strength to:
  * **Reason naturally about tool composition:** Chain operations and handle dependencies as naturally as writing any Python code
  * **Process large results efficiently:** Filter down large tool outputs, extract only relevant data, or write intermediate results to files before returning summaries to the context window
  * **Reduce latency significantly:** Eliminate the overhead of re-sampling Claude between each tool call in multi-step workflows

This approach enables workflows that would be impractical with traditional tool use (such as processing files over 1M tokens) by allowing Claude to work with data programmatically rather than loading everything into the conversation context.
Alternative implementations
Programmatic tool calling is a generalizable pattern that can also be implemented on your own infrastructure. Here's how the approaches compare:
### 
Client-side direct execution
Provide Claude with a code execution tool and describe what functions are available in that environment. When Claude invokes the tool with code, your application executes it locally where those functions are defined.
**Advantages:**
  * Simple to implement with minimal re-architecting
  * Full control over the environment and instructions

**Disadvantages:**
  * Executes untrusted code outside of a sandbox
  * Tool invocations can be vectors for code injection

**Use when:** Your application can safely execute arbitrary code, you want a simple solution, and Anthropic's managed offering doesn't fit your needs.
### 
Self-managed sandboxed execution
Same approach from Claude's perspective, but code runs in a sandboxed container with security restrictions (for example, no network egress). If your tools require external resources, you'll need a protocol for executing tool calls outside the sandbox.
**Advantages:**
  * Safe programmatic tool calling on your own infrastructure
  * Full control over the execution environment

**Disadvantages:**
  * Complex to build and maintain
  * Requires managing both infrastructure and inter-process communication

**Use when:** Security is critical and Anthropic's managed solution doesn't fit your requirements.
### 
Anthropic-managed execution
Anthropic's programmatic tool calling is a managed version of sandboxed execution with an opinionated Python environment tuned for Claude. Anthropic handles container management, code execution, and secure tool invocation communication.
**Advantages:**
  * Safe and secure by default
  * Easy to enable with minimal configuration
  * Environment and instructions optimized for Claude

Consider using Anthropic's managed solution if you're using the Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), or [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry).
Data retention
Programmatic tool calling is built on the code execution infrastructure and uses the same sandbox containers. Container data, including execution artifacts and outputs, is retained for up to 30 days.
For ZDR eligibility across all features, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention).
Related features
[  Code execution tool Learn about the underlying code execution capability that powers programmatic tool calling. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)[  Tool use with Claude Understand the fundamentals of tool use with Claude. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)[ Define tools Step-by-step guide for defining tools. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
  * [Model compatibility](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#model-compatibility)
  * [Quick start](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#quick-start)
  * [How programmatic tool calling works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#how-programmatic-tool-calling-works)
  * [Core concepts](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#core-concepts)
  * [The allowed_callers field](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#the-allowed-callers-field)
  * [The caller field in responses](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#the-caller-field-in-responses)
  * [Container lifecycle](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#container-lifecycle)
  * [Example workflow](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#example-workflow)
  * [Step 1: Initial request](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#step-1-initial-request)
  * [Step 2: API response with tool call](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#step-2-api-response-with-tool-call)
  * [Step 3: Provide tool result](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#step-3-provide-tool-result)
  * [Step 4: Next tool call or completion](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#step-4-next-tool-call-or-completion)
  * [Step 5: Final response](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#step-5-final-response)
  * [Advanced patterns](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#advanced-patterns)
  * [Batch processing with loops](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#batch-processing-with-loops)
  * [Early termination](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#early-termination)
  * [Conditional tool selection](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#conditional-tool-selection)
  * [Data filtering](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#data-filtering)
  * [Response format](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#response-format)
  * [Programmatic tool call](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#programmatic-tool-call)
  * [Tool result handling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#tool-result-handling)
  * [Code execution completion](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#code-execution-completion)
  * [Error handling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#error-handling)
  * [Common errors](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#common-errors)
  * [Container expiration during tool call](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#container-expiration-during-tool-call)
  * [Tool execution errors](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#tool-execution-errors)
  * [Constraints and limitations](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#constraints-and-limitations)
  * [Feature incompatibilities](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#feature-incompatibilities)
  * [Tool restrictions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#tool-restrictions)
  * [Message formatting restrictions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#message-formatting-restrictions)
  * [Rate limits](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#rate-limits)
  * [Validate tool results before use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#validate-tool-results-before-use)
  * [Token efficiency](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#token-efficiency)
  * [Usage and pricing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#usage-and-pricing)
  * [Best practices](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#best-practices)
  * [Tool design](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#tool-design)
  * [When to use programmatic calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#when-to-use-programmatic-calling)
  * [Performance optimization](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#performance-optimization)
  * [Troubleshooting](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#troubleshooting)
  * [Common issues](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#common-issues)
  * [Debugging tips](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#debugging-tips)
  * [Why programmatic tool calling works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#why-programmatic-tool-calling-works)
  * [Alternative implementations](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#alternative-implementations)
  * [Client-side direct execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#client-side-direct-execution)
  * [Self-managed sandboxed execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#self-managed-sandboxed-execution)
  * [Anthropic-managed execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#anthropic-managed-execution)
  * [Data retention](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#data-retention)
  * [Related features](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#related-features)

Messages/Tool infrastructure
# Programmatic tool calling
Programmatic tool calling allows Claude to write code that calls your tools programmatically within a [code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) container, rather than requiring round trips through the model for each tool invocation. This reduces latency for multi-tool workflows and decreases token consumption by allowing Claude to filter or process data before it reaches the model's context window. On agentic search benchmarks like [BrowseComp](https://arxiv.org/abs/2504.12516) and [DeepSearchQA](https://github.com/google-deepmind/deepsearchqa), which test multi-step web research and complex information retrieval, adding programmatic tool calling on top of basic search tools improved performance by an average of 11% while using 24% fewer input tokens (see [Improved web search with dynamic filtering](https://claude.com/blog/improved-web-search-with-dynamic-filtering)).
The difference compounds fast in real workflows. Consider checking budget compliance across 20 employees: the traditional approach requires 20 separate model round-trips, pulling thousands of expense line items into the context along the way. With programmatic tool calling, a single script runs all 20 lookups, filters the results, and returns only the employees who exceeded their limits, shrinking what Claude needs to reason over from hundreds of kilobytes down to a handful of lines.

For a deeper look at the inference and context costs that programmatic tool calling addresses, see [Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use).
This feature requires the code execution tool to be enabled.
This feature is **not** eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). Data is retained according to the feature's standard retention policy.
Model compatibility
Programmatic tool calling requires `code_execution_20260120` or later, which is supported on the following models:  
| Model |  
| --- |  
| Claude Fable 5 (claude-fable-5) |  
| Claude Mythos 5 (claude-mythos-5) |  
| Claude Opus 4.8 (claude-opus-4-8) |  
| Claude Opus 4.7 (claude-opus-4-7) |  
| Claude Opus 4.6 (claude-opus-4-6) |  
| Claude Sonnet 4.6 (claude-sonnet-4-6) |  
| Claude Opus 4.5 (claude-opus-4-5-20251101) |  
| Claude Sonnet 4.5 (claude-sonnet-4-5-20250929) |  
For the full code execution tool version matrix, see the [code execution tool model compatibility table](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#model-compatibility). Programmatic tool calling is available on the Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), and [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry). It is not currently available on Amazon Bedrock or Google Cloud.
Quick start
Here's an example where Claude programmatically queries a database multiple times and aggregates results:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": "Query sales data for the West, East, and Central regions, then tell me which region had the highest revenue",
    ],
    tools=[
        {"type": "code_execution_20260120", "name": "code_execution"},
            "name": "query_database",
            "description": "Execute a SQL query against the sales database. Returns a list of rows as JSON objects.",
            "input_schema": {
                "type": "object",
                "properties": {
                    "sql": {"type": "string", "description": "SQL query to execute"}
                "required": ["sql"],
            "allowed_callers": ["code_execution_20260120"],
    ],
)

print(response)

How programmatic tool calling works
When you configure a tool to be callable from code execution and Claude decides to use that tool:
  1. Claude writes Python code that invokes the tool as a function, potentially including multiple tool calls and pre/post-processing logic
  2. Claude runs this code in a sandboxed container through code execution
  3. When a tool function is called, code execution pauses and the API returns a `tool_use` block
  4. You provide the tool result, and code execution continues (intermediate results are not loaded into Claude's context window)
  5. Once all code execution completes, Claude receives the final output and continues working on the task

This approach is particularly useful for:
  * **Large data processing:** Filter or aggregate tool results before they reach Claude's context
  * **Multi-step workflows:** Save tokens and latency by calling tools serially or in a loop without sampling Claude in-between tool calls
  * **Conditional logic:** Make decisions based on intermediate tool results

Custom tools are converted to async Python functions to support parallel tool calling. When Claude writes code that calls your tools, it uses `await` (for example, `result = await query_database("<sql>")`) and automatically includes the appropriate async wrapper function.
The async wrapper is omitted from code examples in this documentation for clarity.
Core concepts
### 
The `allowed_callers` field
The `allowed_callers` field specifies which contexts can invoke a tool:

  "name": "query_database",
  "description": "Execute a SQL query against the database",
  "input_schema": {
    // ...
  "allowed_callers": ["code_execution_20260120"]

**Possible values:**
  * `["direct"]` - Claude is guided to call this tool directly (default if omitted)
  * `["code_execution_20260120"]` - Claude is guided to call this tool only from within code execution
  * `["direct", "code_execution_20260120"]` - Claude may call this tool directly or from within code execution


Choose either `["direct"]` or `["code_execution_20260120"]` for each tool rather than enabling both, as this provides clearer guidance to Claude for how best to use the tool.
`allowed_callers` controls how the tool is presented to Claude and is validated against `tool_choice`, but it is not a hard API-level block on direct invocation. Claude is strongly guided to respect it, but your client should still be prepared to handle a direct `tool_use` for any tool it defines. Do not rely on `allowed_callers` as a security boundary.
### 
The `caller` field in responses
Every tool use block includes a `caller` field indicating how it was invoked:
**Direct invocation (traditional tool use):**

  "type": "tool_use",
  "id": "toolu_abc123",
  "name": "query_database",
  "input": { "sql": "<sql>" },
  "caller": { "type": "direct" }

**Programmatic invocation:**

  "type": "tool_use",
  "id": "toolu_xyz789",
  "name": "query_database",
  "input": { "sql": "<sql>" },
  "caller": {
    "type": "code_execution_20260120",
    "tool_id": "srvtoolu_abc123"

The `tool_id` references the code execution tool that made the programmatic call.
### 
Container lifecycle
Programmatic tool calling uses the same containers as code execution:
  * **Container creation:** A new container is created for each request unless you reuse an existing one
  * **Expiration:** Containers have a 30-day maximum lifetime and are cleaned up after 4.5 minutes of idle time
  * **Container ID:** Returned in responses in the `container` field
  * **Reuse:** Pass the container ID to maintain state across requests


When a tool is called programmatically and the container is waiting for your tool result, you must respond before the container expires. Monitor the `expires_at` field. If the container expires, Claude may treat the tool call as timed out and retry it.
Example workflow
Here's how a complete programmatic tool calling flow works:
### 
Step 1: Initial request
Send a request with code execution and a tool that allows programmatic calling. To enable programmatic calling, add the `allowed_callers` field to your tool definition.
Provide detailed descriptions of your tool's output format in the tool description. If you specify that the tool returns JSON, Claude attempts to deserialize and process the result in code. The more detail you provide about the output schema, the better Claude can handle the response programmatically.
The request shape is identical to the [Quick start](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#quick-start) example: include `code_execution` in your tools list, add `allowed_callers: ["code_execution_20260120"]` to any tool you want Claude to invoke from code, and send your user message. The remaining steps in this workflow use the user message `"Query customer purchase history from the last quarter and identify our top 5 customers by revenue"`.
### 
Step 2: API response with tool call
Claude writes code that calls your tool. The API pauses and returns:
Output

  "role": "assistant",
  "content": [
      "type": "text",
      "text": "I'll query the purchase history and analyze the results."
      "type": "server_tool_use",
      "id": "srvtoolu_abc123",
      "name": "code_execution",
      "input": {
        "code": "results = await query_database('<sql>')\ntop_customers = sorted(results, key=lambda x: x['revenue'], reverse=True)[:5]\nprint(f'Top 5 customers: {top_customers}')"
      "type": "tool_use",
      "id": "toolu_def456",
      "name": "query_database",
      "input": { "sql": "<sql>" },
      "caller": {
        "type": "code_execution_20260120",
        "tool_id": "srvtoolu_abc123"
  ],
  "container": {
    "id": "container_xyz789",
    "expires_at": "2026-01-20T14:30:00Z"
  "stop_reason": "tool_use"

### 
Step 3: Provide tool result
Include the full conversation history plus your tool result:
CLIPythonTypeScriptC#GoJavaPHPRuby

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    container="container_xyz789",  # Reuse the container
    messages=[
            "role": "user",
            "content": "Query customer purchase history from the last quarter and identify our top 5 customers by revenue",
            "role": "assistant",
            "content": [
                    "type": "text",
                    "text": "I'll query the purchase history and analyze the results.",
                    "type": "server_tool_use",
                    "id": "srvtoolu_abc123",
                    "name": "code_execution",
                    "input": {"code": "..."},
                    "type": "tool_use",
                    "id": "toolu_def456",
                    "name": "query_database",
                    "input": {"sql": "<sql>"},
                    "caller": {
                        "type": "code_execution_20260120",
                        "tool_id": "srvtoolu_abc123",
            ],
            "role": "user",
            "content": [
                    "type": "tool_result",
                    "tool_use_id": "toolu_def456",
                    "content": '[{"customer_id": "C1", "revenue": 45000}, {"customer_id": "C2", "revenue": 38000}, ...]',
            ],
    ],
    tools=[...],
)

print(response)

### 
Step 4: Next tool call or completion
The code execution continues and processes the results. If additional tool calls are needed, repeat Step 3 until all tool calls are satisfied.
### 
Step 5: Final response
Once the code execution completes, Claude provides the final response:
Output

  "content": [
      "type": "code_execution_tool_result",
      "tool_use_id": "srvtoolu_abc123",
      "content": {
        "type": "code_execution_result",
        "stdout": "Top 5 customers: [{'customer_id': 'C1', 'revenue': 45000}, {'customer_id': 'C2', 'revenue': 38000}, {'customer_id': 'C5', 'revenue': 32000}, {'customer_id': 'C8', 'revenue': 28500}, {'customer_id': 'C3', 'revenue': 24000}]",
        "stderr": "",
        "return_code": 0,
        "content": []
      "type": "text",
      "text": "I've analyzed the purchase history from last quarter. Your top 5 customers generated $167,500 in total revenue, with Customer C1 leading at $45,000."
  ],
  "stop_reason": "end_turn"

Advanced patterns
### 
Batch processing with loops
Claude can write code that processes multiple items efficiently:

async def _claude_code():
    regions = ["West", "East", "Central", "North", "South"]
    results = {}
    for region in regions:
        data = await query_database(f"<sql for {region}>")
        results[region] = sum(row["revenue"] for row in data)

    # Process results programmatically
    top_region = max(results.items(), key=lambda x: x[1])
    print(f"Top region: {top_region[0]} with ${top_region[1]:,} in revenue")

This pattern:
  * Reduces model round-trips from N (one per region) to 1
  * Processes large result sets programmatically before returning to Claude
  * Saves tokens by only returning aggregated conclusions instead of raw data

### 
Early termination
Claude can stop processing as soon as success criteria are met:

async def _claude_code():
    endpoints = ["us-east", "eu-west", "apac"]
    for endpoint in endpoints:
        status = await check_health(endpoint)
        if status == "healthy":
            print(f"Found healthy endpoint: {endpoint}")
            break  # Stop early, don't check remaining

### 
Conditional tool selection

async def _claude_code():
    file_info = await get_file_info(path)
    if file_info["size"] < 10000:
        content = await read_full_file(path)
    else:
        content = await read_file_summary(path)
    print(content)

### 
Data filtering

async def _claude_code():
    logs = await fetch_logs(server_id)
    errors = [log for log in logs if "ERROR" in log]
    print(f"Found {len(errors)} errors")
    for error in errors[-10:]:  # Only return last 10 errors
        print(error)

Response format
### 
Programmatic tool call
When code execution calls a tool:

  "type": "tool_use",
  "id": "toolu_abc123",
  "name": "query_database",
  "input": { "sql": "<sql>" },
  "caller": {
    "type": "code_execution_20260120",
    "tool_id": "srvtoolu_xyz789"

### 
Tool result handling
Your tool result is passed back to the running code:

  "role": "user",
  "content": [
      "type": "tool_result",
      "tool_use_id": "toolu_abc123",
      "content": "[{\"customer_id\": \"C1\", \"revenue\": 45000, \"orders\": 23}, {\"customer_id\": \"C2\", \"revenue\": 38000, \"orders\": 18}, ...]"
  ]

### 
Code execution completion
When all tool calls are satisfied and code completes:

  "type": "code_execution_tool_result",
  "tool_use_id": "srvtoolu_xyz789",
  "content": {
    "type": "code_execution_result",
    "stdout": "Analysis complete. Top 5 customers identified from 847 total records.",
    "stderr": "",
    "return_code": 0,
    "content": []

Error handling
### 
Common errors  
| Error  | Description  | Solution  |  
| --- | --- | --- |  
| `invalid_tool_input`  | Tool input doesn't match schema  | Validate your tool's input_schema  |  
|  `invalid_request_error` (on `tool_choice`)  |  `tool_choice` names a tool whose `allowed_callers` does not include `"direct"`  | Either add `"direct"` to that tool's `allowed_callers`, or remove the tool from `tool_choice` and let Claude invoke it from code  |  
### 
Container expiration during tool call
If your tool takes too long to respond, the code execution receives a `TimeoutError`. Claude sees this in stderr and typically retries:

  "type": "code_execution_tool_result",
  "tool_use_id": "srvtoolu_abc123",
  "content": {
    "type": "code_execution_result",
    "stdout": "",
    "stderr": "TimeoutError: Calling tool ['query_database'] timed out.",
    "return_code": 0,
    "content": []

To prevent timeouts:
  * Monitor the `expires_at` field in responses
  * Implement timeouts for your tool execution
  * Consider breaking long operations into smaller chunks

### 
Tool execution errors
If your tool returns an error:

  "type": "tool_result",
  "tool_use_id": "toolu_abc123",
  "content": "Error: Query timeout - table lock exceeded 30 seconds"

Claude's code receives this error and can handle it appropriately.
Constraints and limitations
### 
Feature incompatibilities
  * **Structured outputs:** Tools with `strict: true` are not supported with programmatic calling
  * **Tool choice:** You cannot force programmatic calling of a specific tool through `tool_choice`
  * **Parallel tool use:** `disable_parallel_tool_use: true` is not supported with programmatic calling

### 
Tool restrictions
The following tools cannot be called programmatically:
  * Tools provided by an [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)

### 
Message formatting restrictions
When responding to programmatic tool calls, there are strict formatting requirements:
**Tool result only responses:** If there are pending programmatic tool calls waiting for results, your response message must contain **only** `tool_result` blocks. You cannot include any text content, even after the tool results.
Invalid - Cannot include text when responding to programmatic tool calls:

  "role": "user",
  "content": [
      "type": "tool_result",
      "tool_use_id": "toolu_01",
      "content": "[{\"customer_id\": \"C1\", \"revenue\": 45000}]"
    { "type": "text", "text": "What should I do next?" }
  ]

Valid - Only tool results when responding to programmatic tool calls:

  "role": "user",
  "content": [
      "type": "tool_result",
      "tool_use_id": "toolu_01",
      "content": "[{\"customer_id\": \"C1\", \"revenue\": 45000}]"
  ]

This restriction only applies when responding to programmatic (code execution) tool calls. For regular client-side tool calls, you can include text content after tool results.
### 
Rate limits
Programmatic tool calls are subject to the same rate limits as regular tool calls. Each tool call from code execution counts as a separate invocation.
### 
Validate tool results before use
When implementing user-defined tools that will be called programmatically:
  * **Tool results are returned as strings:** They can contain any content, including code snippets or executable commands that may be processed by the execution environment.
  * **Validate external tool results:** If your tool returns data from external sources or accepts user input, be aware of code injection risks if the output will be interpreted or executed as code.

Token efficiency
Programmatic tool calling can significantly reduce token consumption:
  * **Tool results from programmatic calls are not added to Claude's context** - only the final code output is
  * **Intermediate processing happens in code** - filtering, aggregation, and other transformations don't consume model tokens
  * **Multiple tool calls in one code execution** - reduces overhead compared to separate model turns

For example, calling 10 tools directly uses ~10x the tokens of calling them programmatically and returning a summary.
In Anthropic's internal evaluations on a production Claude model:
  * On a 75-tool project-management agent benchmark, enabling programmatic tool calling reduced billed input tokens by roughly 38% with no change in task accuracy.
  * On [τ²-bench](https://arxiv.org/abs/2506.07982) (airline, retail, and telecom domains), where each turn makes one or two sequential tool calls, programmatic tool calling left scores unchanged and cost roughly 8% more. Sequential single-call workflows do not benefit.
  * Across production API traffic, requests whose `tools` array contains 10 to 49 tool definitions see typical token savings of 20% to 40% with programmatic tool calling enabled.

Actual savings vary with workload shape; see [When to use programmatic calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling#when-to-use-programmatic-calling).
Usage and pricing
Programmatic tool calling uses the same pricing as code execution. See the [code execution pricing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#usage-and-pricing) for details.
Token counting for programmatic tool calls: Tool results from programmatic invocations do not count toward your input/output token usage. Only the final code execution result and Claude's response count.
Best practices
### 
Tool design
  * **Provide detailed output descriptions:** Because Claude deserializes tool results in code, clearly document the format (JSON structure and field types)
  * **Return structured data:** JSON or other easily parseable formats work best for programmatic processing
  * **Keep responses concise:** Return only necessary data to minimize processing overhead

### 
When to use programmatic calling
Programmatic tool calling trades a small fixed overhead (container startup, script generation) for large savings on tool-result tokens and model round-trips. Whether that trade pays off depends on workload shape.
**Strong fit:**
  * Fan-out or parallel operations across many items (for example, checking 50 endpoints or looking up 20 records)
  * Large tool results that can be filtered, aggregated, or summarized before reaching Claude's context
  * Agentic search and retrieval, where iterative querying and result filtering dominate the workflow

**Weak fit:**
  * Strictly sequential workflows where each call depends on Claude reasoning over the previous result, because the script cannot skip the model round-trip in that case
  * A small number of tool calls with small responses, especially on the first turn of a conversation, where container and script overhead can exceed the savings
  * Tools that require immediate user feedback between calls

If you are unsure, measure billed input tokens with and without `allowed_callers` on a representative sample of your traffic before enabling it broadly.
### 
Performance optimization
  * **Reuse containers** when making multiple related requests to maintain state
  * **Batch similar operations** in a single code execution when possible

Troubleshooting
### 
Common issues
**`invalid_request_error`when setting`tool_choice`**
  * `tool_choice` cannot name a tool whose `allowed_callers` omits `"direct"`. Either add `"direct"` to that tool's `allowed_callers`, or remove the tool from `tool_choice` and let Claude invoke it from code.

**Container expiration**
  * Ensure you respond to tool calls before the container idles out (4.5 minutes of inactivity; 30-day hard maximum)
  * Monitor the `expires_at` field in responses
  * Consider implementing faster tool execution

**Tool result not parsed correctly**
  * Ensure your tool returns string data that Claude can deserialize
  * Provide clear output format documentation in your tool description

### 
Debugging tips
  1. **Log all tool calls and results** to track the flow
  2. **Check the`caller` field** to confirm programmatic invocation
  3. **Monitor container IDs** to ensure proper reuse
  4. **Test tools independently** before enabling programmatic calling

Why programmatic tool calling works
Claude's training includes extensive exposure to code, making it effective at reasoning through and chaining function calls. When tools are presented as callable functions within a code execution environment, Claude can leverage this strength to:
  * **Reason naturally about tool composition:** Chain operations and handle dependencies as naturally as writing any Python code
  * **Process large results efficiently:** Filter down large tool outputs, extract only relevant data, or write intermediate results to files before returning summaries to the context window
  * **Reduce latency significantly:** Eliminate the overhead of re-sampling Claude between each tool call in multi-step workflows

This approach enables workflows that would be impractical with traditional tool use (such as processing files over 1M tokens) by allowing Claude to work with data programmatically rather than loading everything into the conversation context.
Alternative implementations
Programmatic tool calling is a generalizable pattern that can also be implemented on your own infrastructure. Here's how the approaches compare:
### 
Client-side direct execution
Provide Claude with a code execution tool and describe what functions are available in that environment. When Claude invokes the tool with code, your application executes it locally where those functions are defined.
**Advantages:**
  * Simple to implement with minimal re-architecting
  * Full control over the environment and instructions

**Disadvantages:**
  * Executes untrusted code outside of a sandbox
  * Tool invocations can be vectors for code injection

**Use when:** Your application can safely execute arbitrary code, you want a simple solution, and Anthropic's managed offering doesn't fit your needs.
### 
Self-managed sandboxed execution
Same approach from Claude's perspective, but code runs in a sandboxed container with security restrictions (for example, no network egress). If your tools require external resources, you'll need a protocol for executing tool calls outside the sandbox.
**Advantages:**
  * Safe programmatic tool calling on your own infrastructure
  * Full control over the execution environment

**Disadvantages:**
  * Complex to build and maintain
  * Requires managing both infrastructure and inter-process communication

**Use when:** Security is critical and Anthropic's managed solution doesn't fit your requirements.
### 
Anthropic-managed execution
Anthropic's programmatic tool calling is a managed version of sandboxed execution with an opinionated Python environment tuned for Claude. Anthropic handles container management, code execution, and secure tool invocation communication.
**Advantages:**
  * Safe and secure by default
  * Easy to enable with minimal configuration
  * Environment and instructions optimized for Claude

Consider using Anthropic's managed solution if you're using the Claude API, [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), or [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry).
Data retention
Programmatic tool calling is built on the code execution infrastructure and uses the same sandbox containers. Container data, including execution artifacts and outputs, is retained for up to 30 days.
For ZDR eligibility across all features, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention).
Related features
[  Code execution tool Learn about the underlying code execution capability that powers programmatic tool calling. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)[  Tool use with Claude Understand the fundamentals of tool use with Claude. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)[ Define tools Step-by-step guide for defining tools. ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
