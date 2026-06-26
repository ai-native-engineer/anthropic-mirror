<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool -->

# Code execution tool
Run Python and bash code in a sandboxed container to analyze data, generate files, and iterate on solutions.
Claude can analyze data, create visualizations, perform complex calculations, run system commands, create and edit files, and process uploaded files directly within the API conversation. The code execution tool allows Claude to run Bash commands and manipulate files, including writing code, in a secure, sandboxed environment.
**Code execution is free when used with web search or web fetch.** When `web_search_20260209` (or later) or `web_fetch_20260209` (or later) is included in your request, there are no additional charges for code execution tool calls beyond the standard input and output token costs. Standard code execution charges apply when these tools are not included.
Code execution is a core primitive for building high-performance agents. It enables dynamic filtering in web search and web fetch tools, allowing Claude to process results before they reach the context window, improving accuracy while reducing token consumption.
Reach out through the [feedback form](https://forms.gle/LTAU6Xn2puCJMi1n6) to share your feedback on this feature.
This feature is **not** eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). Data is retained according to the feature's standard retention policy.
Model compatibility
The code execution tool is available on the following models:  
| Model  | Tool versions  |  
| --- | --- |  
| Claude Fable 5 (claude-fable-5)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Mythos 5 (claude-mythos-5)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Opus 4.8 (claude-opus-4-8)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Opus 4.7 (claude-opus-4-7)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Opus 4.6 (claude-opus-4-6)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Sonnet 4.6 (claude-sonnet-4-6)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Opus 4.5 (claude-opus-4-5-20251101)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Haiku 4.5 (claude-haiku-4-5-20251001)  | `code_execution_20250825`  |  
| Claude Opus 4.1 (claude-opus-4-1-20250805) ([deprecated](https://platform.claude.com/docs/en/about-claude/model-deprecations))  | `code_execution_20250825`  |  
`code_execution_20250825` supports Bash commands and file operations and is available on every model in the table. `code_execution_20260120` adds REPL state persistence and [programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) from within the sandbox, and is available on Claude Fable 5, Claude Mythos 5, Opus 4.5+, and Sonnet 4.5+ only. `code_execution_20260521` is the same runtime as `_20260120` with the per-cell execution time limit disclosed in the tool description, so Claude can budget long-running cells accordingly. Each cell has a 90-second wall-clock time limit; code that exceeds it returns a `detection_timeout` result. If you're still using the legacy `code_execution_20250522` (Python only), see [Upgrade to latest tool version](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#upgrade-to-latest-tool-version) to migrate from it.

Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.
Platform availability
Code execution is available on:
  * **Claude API** (Anthropic)
  * **[Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)**
  * **[Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)**

Code execution is not currently available on Amazon Bedrock or Google Cloud.
For [Claude Mythos Preview](https://anthropic.com/glasswing), code execution is supported on the Claude API and Microsoft Foundry only. It is not available for Mythos Preview on Amazon Bedrock, Google Cloud, or Claude Platform on AWS.
Quick start
Here's a simple example that asks Claude to perform a calculation:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

print(response)

How code execution works
When you add the code execution tool to your API request:
  1. Claude evaluates whether code execution would help answer your question
  2. The tool automatically provides Claude with the following capabilities:
     * **Bash commands** : Execute shell commands for system operations and package management
     * **File operations** : Create, view, and edit files directly, including writing code
  3. Claude can use any combination of these capabilities in a single request
  4. All operations run in a secure sandbox environment
  5. Claude provides results with any generated charts, calculations, or analysis

### 
When Claude runs code
Claude runs code when the request benefits from computation or file handling:
  * Non-trivial math (large numbers, many steps, precision-sensitive results)
  * Data analysis, file parsing, or visualization
  * Algorithm execution or simulation
  * Explicit requests to "run", "compute", or "execute"

Claude answers directly without running code for:
  * Simple arithmetic and well-known math facts
  * Factual, conversational, or creative requests
  * Simple unit conversions or translations

If you want Claude to run code for a borderline request, ask explicitly (for example, "run code to verify this").
Using code execution with other execution tools
When you provide code execution alongside client-provided tools that also run code (such as a [bash tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool) or custom REPL), Claude is operating in a multi-computer environment. The code execution tool runs in Anthropic's sandboxed container, while your client-provided tools run in a separate environment that you control. Claude can sometimes confuse these environments, attempting to use the wrong tool or assuming state is shared between them.
To avoid this, add instructions to your system prompt that clarify the distinction:

When multiple code execution environments are available, be aware that:
- Variables, files, and state do NOT persist between different execution environments
- Use the code_execution tool for general-purpose computation in Anthropic's sandboxed environment
- Use client-provided execution tools (e.g., bash) when you need access to the user's local system, files, or data
- If you need to pass results between environments, explicitly include outputs in subsequent tool calls rather than assuming shared state

This is especially important when combining code execution with [web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) or [web fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool), which enable code execution automatically. If your application already provides a client-side shell tool, the automatic code execution creates a second execution environment that Claude needs to distinguish between.
How to use the tool
### 
Upload and analyze your own files
To analyze your own data files (such as CSV, Excel, or images), upload them through the Files API and reference them in your request:
Using the Files API with Code Execution requires the Files API beta header: `"anthropic-beta": "files-api-2025-04-14"`
The Python environment can process various file types uploaded through the Files API, including:
  * CSV
  * Excel (.xlsx, .xls)
  * JSON
  * XML
  * Images (JPEG, PNG, GIF, WebP)
  * Text files (.txt, .md, .py, and others)

#### 
Upload and analyze files
  1. **Upload your file** using the [Files API](https://platform.claude.com/docs/en/build-with-claude/files)
  2. **Reference the file** in your message using a `container_upload` content block
  3. **Include the code execution tool** in your API request

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

# Upload a file
file_object = client.beta.files.upload(
    file=open("data.csv", "rb"),
)

# Use the file_id with code execution
response = client.beta.messages.create(
    model="claude-opus-4-8",
    betas=["files-api-2025-04-14"],
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": [
                {"type": "text", "text": "Analyze this CSV data"},
                {"type": "container_upload", "file_id": file_object.id},
            ],
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

print(response)

### 
Retrieve generated files
When Claude creates files during code execution, you can retrieve these files using the Files API:
CLIPythonTypeScriptC#GoJavaPHPRuby

# Initialize the client
client = Anthropic()

# Request code execution that creates files
response = client.beta.messages.create(
    model="claude-opus-4-8",
    betas=["files-api-2025-04-14"],
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": "Create a matplotlib visualization and save it as output.png",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Extract file IDs from the response
def extract_file_ids(response):
    file_ids = []
    for item in response.content:
        if item.type == "bash_code_execution_tool_result":
            content_item = item.content
            if content_item.type == "bash_code_execution_result":
                # concrete-typed list: List[BashCodeExecutionOutputBlock]
                for file in content_item.content:
                    file_ids.append(file.file_id)
    return file_ids

# Download the created files
for file_id in extract_file_ids(response):
    file_metadata = client.beta.files.retrieve_metadata(file_id)
    file_content = client.beta.files.download(file_id)
    file_content.write_to_file(file_metadata.filename)
    print(f"Downloaded: {file_metadata.filename}")

Tool definition
The code execution tool requires no additional parameters:
JSON

  "type": "code_execution_20250825",
  "name": "code_execution"

When this tool is provided, Claude automatically gains access to two sub-tools:
  * `bash_code_execution`: Run shell commands
  * `text_editor_code_execution`: View, create, and edit files, including writing code

Response format
The code execution tool can return two types of results depending on the operation:
### 
Bash command response
Output

  "type": "server_tool_use",
  "id": "srvtoolu_01B3C4D5E6F7G8H9I0J1K2L3",
  "name": "bash_code_execution",
  "input": {
    "command": "ls -la | head -5"
  "type": "bash_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01B3C4D5E6F7G8H9I0J1K2L3",
  "content": {
    "type": "bash_code_execution_result",
    "stdout": "total 24\ndrwxr-xr-x 2 user user 4096 Jan 1 12:00 .\ndrwxr-xr-x 3 user user 4096 Jan 1 11:00 ..\n-rw-r--r-- 1 user user  220 Jan 1 12:00 data.csv\n-rw-r--r-- 1 user user  180 Jan 1 12:00 config.json",
    "stderr": "",
    "return_code": 0

### 
File operation responses
**View file:**
Output

  "type": "server_tool_use",
  "id": "srvtoolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "name": "text_editor_code_execution",
  "input": {
    "command": "view",
    "path": "config.json"
  "type": "text_editor_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "content": {
    "type": "text_editor_code_execution_result",
    "file_type": "text",
    "content": "{\n  \"setting\": \"value\",\n  \"debug\": true\n}",
    "numLines": 4,
    "startLine": 1,
    "totalLines": 4

**Create file:**
Output

  "type": "server_tool_use",
  "id": "srvtoolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "name": "text_editor_code_execution",
  "input": {
    "command": "create",
    "path": "new_file.txt",
    "file_text": "Hello, World!"
  "type": "text_editor_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "content": {
    "type": "text_editor_code_execution_result",
    "is_file_update": false

**Edit file (str_replace):**
Output

  "type": "server_tool_use",
  "id": "srvtoolu_01E6F7G8H9I0J1K2L3M4N5O6",
  "name": "text_editor_code_execution",
  "input": {
    "command": "str_replace",
    "path": "config.json",
    "old_str": "\"debug\": true",
    "new_str": "\"debug\": false"
  "type": "text_editor_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01E6F7G8H9I0J1K2L3M4N5O6",
  "content": {
    "type": "text_editor_code_execution_result",
    "oldStart": 3,
    "oldLines": 1,
    "newStart": 3,
    "newLines": 1,
    "lines": ["-  \"debug\": true", "+  \"debug\": false"]

### 
Results
All execution results include:
  * `stdout`: Output from successful execution
  * `stderr`: Error messages if execution fails
  * `return_code`: 0 for success, non-zero for failure

Additional fields for file operations:
  * **View** : `file_type`, `content`, `numLines`, `startLine`, `totalLines`
  * **Create** : `is_file_update` (whether file already existed)
  * **Edit** : `oldStart`, `oldLines`, `newStart`, `newLines`, `lines` (diff format)

### 
Errors
Each tool type can return specific errors:
**Common errors (all tools):**
Output

  "type": "bash_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01VfmxgZ46TiHbmXgy928hQR",
  "content": {
    "type": "bash_code_execution_tool_result_error",
    "error_code": "unavailable"

**Error codes by tool type:**  
| Tool  | Error Code  | Description  |  
| --- | --- | --- |  
| All tools  | `unavailable`  | The tool is temporarily unavailable  |  
| All tools  | `execution_time_exceeded`  | Execution exceeded maximum time limit  |  
| All tools  | `container_expired`  | Container expired and is no longer available  |  
| All tools  | `invalid_tool_input`  | Invalid parameters provided to the tool  |  
| All tools  | `too_many_requests`  | Rate limit exceeded for tool usage  |  
| bash  | `output_file_too_large`  | Command output exceeded the maximum size  |  
| text_editor  | `file_not_found`  | File doesn't exist (for view/edit operations)  |  
| text_editor  | `string_not_found`  | The `old_str` not found in file (for str_replace)  |  
#### 
`pause_turn` stop reason
The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running turn. You may provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you wish to interrupt the conversation.
Containers
The code execution tool runs in a secure, containerized environment designed specifically for code execution, with a higher focus on Python.
### 
Runtime environment
  * **Python version** : 3.11.12
  * **Operating system** : Linux-based container
  * **Architecture** : x86_64 (AMD64)

### 
Resource limits
  * **Memory** : 5GiB RAM
  * **Disk space** : 5GiB workspace storage
  * **CPU** : 1 CPU

### 
Networking and security
  * **Internet access** : Completely disabled for security
  * **External connections** : No outbound network requests permitted
  * **Sandbox isolation** : Full isolation from host system and other containers
  * **File access** : Limited to workspace directory only
  * **Workspace scoping** : Like [Files](https://platform.claude.com/docs/en/build-with-claude/files), containers are scoped to the workspace of the API key
  * **Expiration** : Containers expire 30 days after creation

### 
Pre-installed libraries
The sandboxed Python environment includes these commonly used libraries:
  * **Data Science** : pandas, numpy, scipy, scikit-learn, statsmodels
  * **Visualization** : matplotlib, seaborn
  * **File Processing** : pyarrow, openpyxl, xlsxwriter, xlrd, pillow, python-pptx, python-docx, pypdf, pdfplumber, pypdfium2, pdf2image, pdfkit, tabula-py, reportlab[pycairo], Img2pdf
  * **Math & Computing**: sympy, mpmath
  * **Utilities** : tqdm, python-dateutil, pytz, joblib, unzip, unrar, 7zip, bc, rg (ripgrep), fd, sqlite

Container reuse
You can reuse an existing container across multiple API requests by providing the container ID from a previous response. This allows you to maintain created files between requests.
### 
Example
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# First request: Create a file with a random number
response1 = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": "Write a file with a random number and save it to '/tmp/number.txt'",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Extract the container ID from the first response
container_id = response1.container.id

# Second request: Reuse the container to read the file
response2 = client.messages.create(
    container=container_id,  # Reuse the same container
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": "Read the number from '/tmp/number.txt' and calculate its square",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

print(response2)

Streaming
With streaming enabled, you'll receive code execution events as they occur:

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "code_execution"}}

// Code execution streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"code\":\"import pandas as pd\\ndf = pd.read_csv('data.csv')\\nprint(df.head())\"}"}}

// Pause while code executes

// Execution results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "code_execution_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": {"stdout": "   A  B  C\n0  1  2  3\n1  4  5  6", "stderr": ""}}}

Batch requests
You can include the code execution tool in the [Messages Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing). Code execution tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.
Usage and pricing
**Code execution is free when used with web search or web fetch.** When `web_search_20260209` (or later) or `web_fetch_20260209` (or later) is included in your API request, there are no additional charges for code execution tool calls beyond the standard input and output token costs.
When used without these tools, code execution is billed by execution time, tracked separately from token usage:
  * Execution time has a minimum of 5 minutes
  * Each organization receives **1,550 free hours** of usage per month
  * Additional usage beyond 1,550 hours is billed at **$0.05 per hour, per container**
  * If files are included in the request, execution time is billed even if the tool is not invoked, due to files being preloaded onto the container

Code execution usage is tracked in the response:

  "usage": {
    "input_tokens": 105,
    "output_tokens": 239,
    "server_tool_use": {
      "code_execution_requests": 1

Upgrade to latest tool version
By upgrading to `code-execution-2025-08-25`, you get access to file manipulation and Bash capabilities, including code in multiple languages. There is no price difference.
### 
What's changed  
| Component  | Legacy  | Current  |  
| --- | --- | --- |  
| Beta header  | `code-execution-2025-05-22`  | `code-execution-2025-08-25`  |  
| Tool type  | `code_execution_20250522`  | `code_execution_20250825`  |  
| Capabilities  | Python only  | Bash commands, file operations  |  
| Response types  | `code_execution_result`  |  `bash_code_execution_result`, `text_editor_code_execution_result`  |  
### 
Backward compatibility
  * All existing Python code execution continues to work exactly as before
  * No changes required to existing Python-only workflows

### 
Upgrade steps
To upgrade, update the tool type in your API requests:

- "type": "code_execution_20250522"
+ "type": "code_execution_20250825"

**Review response handling** (if parsing responses programmatically):
  * The previous blocks for Python execution responses will no longer be sent
  * Instead, new response types for Bash and file operations will be sent (see Response Format section)

Programmatic tool calling
For running tools inside the code execution container, see [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling).
Data retention
Code execution runs in server-side sandbox containers. Container data, including execution artifacts, uploaded files, and outputs, is retained for up to 30 days. This retention applies to all data processed within the container environment. Files that code execution creates in the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) (retrievable via `client.beta.files.download()`) persist until explicitly deleted.
For ZDR eligibility across all features, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention).
Using code execution with Agent Skills
The code execution tool enables Claude to use [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). Skills are modular capabilities consisting of instructions, scripts, and resources that extend Claude's functionality.
Learn more in [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) and [Using Agent Skills with the API](https://platform.claude.com/docs/en/build-with-claude/skills-guide).
  * [Model compatibility](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#model-compatibility)
  * [Platform availability](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#platform-availability)
  * [Quick start](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#quick-start)
  * [How code execution works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#how-code-execution-works)
  * [When Claude runs code](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#when-claude-runs-code)
  * [Using code execution with other execution tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#using-code-execution-with-other-execution-tools)
  * [How to use the tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#how-to-use-the-tool)
  * [Upload and analyze your own files](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#upload-and-analyze-your-own-files)
  * [Retrieve generated files](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#retrieve-generated-files)
  * [Tool definition](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#tool-definition)
  * [Response format](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#response-format)
  * [Bash command response](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#bash-command-response)
  * [File operation responses](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#file-operation-responses)
  * [Results](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#results)
  * [Errors](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#errors)
  * [Containers](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#containers)
  * [Runtime environment](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#runtime-environment)
  * [Resource limits](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#resource-limits)
  * [Networking and security](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#networking-and-security)
  * [Pre-installed libraries](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#pre-installed-libraries)
  * [Container reuse](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#container-reuse)
  * [Example](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#example)
  * [Streaming](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#streaming)
  * [Batch requests](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#batch-requests)
  * [Usage and pricing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#usage-and-pricing)
  * [Upgrade to latest tool version](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#upgrade-to-latest-tool-version)
  * [What's changed](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#whats-changed)
  * [Backward compatibility](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#backward-compatibility)
  * [Upgrade steps](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#upgrade-steps)
  * [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#programmatic-tool-calling)
  * [Data retention](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#data-retention)
  * [Using code execution with Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#using-code-execution-with-agent-skills)

Messages/Tools
# Code execution tool
Run Python and bash code in a sandboxed container to analyze data, generate files, and iterate on solutions.
Claude can analyze data, create visualizations, perform complex calculations, run system commands, create and edit files, and process uploaded files directly within the API conversation. The code execution tool allows Claude to run Bash commands and manipulate files, including writing code, in a secure, sandboxed environment.
**Code execution is free when used with web search or web fetch.** When `web_search_20260209` (or later) or `web_fetch_20260209` (or later) is included in your request, there are no additional charges for code execution tool calls beyond the standard input and output token costs. Standard code execution charges apply when these tools are not included.
Code execution is a core primitive for building high-performance agents. It enables dynamic filtering in web search and web fetch tools, allowing Claude to process results before they reach the context window, improving accuracy while reducing token consumption.
Reach out through the [feedback form](https://forms.gle/LTAU6Xn2puCJMi1n6) to share your feedback on this feature.
This feature is **not** eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). Data is retained according to the feature's standard retention policy.
Model compatibility
The code execution tool is available on the following models:  
| Model  | Tool versions  |  
| --- | --- |  
| Claude Fable 5 (claude-fable-5)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Mythos 5 (claude-mythos-5)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Opus 4.8 (claude-opus-4-8)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Opus 4.7 (claude-opus-4-7)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Opus 4.6 (claude-opus-4-6)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Sonnet 4.6 (claude-sonnet-4-6)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Opus 4.5 (claude-opus-4-5-20251101)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Sonnet 4.5 (claude-sonnet-4-5-20250929)  |  `code_execution_20250825`, `code_execution_20260120`, `code_execution_20260521`  |  
| Claude Haiku 4.5 (claude-haiku-4-5-20251001)  | `code_execution_20250825`  |  
| Claude Opus 4.1 (claude-opus-4-1-20250805) ([deprecated](https://platform.claude.com/docs/en/about-claude/model-deprecations))  | `code_execution_20250825`  |  
`code_execution_20250825` supports Bash commands and file operations and is available on every model in the table. `code_execution_20260120` adds REPL state persistence and [programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) from within the sandbox, and is available on Claude Fable 5, Claude Mythos 5, Opus 4.5+, and Sonnet 4.5+ only. `code_execution_20260521` is the same runtime as `_20260120` with the per-cell execution time limit disclosed in the tool description, so Claude can budget long-running cells accordingly. Each cell has a 90-second wall-clock time limit; code that exceeds it returns a `detection_timeout` result. If you're still using the legacy `code_execution_20250522` (Python only), see [Upgrade to latest tool version](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#upgrade-to-latest-tool-version) to migrate from it.

Older tool versions are not guaranteed to be backwards-compatible with newer models. Always use the tool version that corresponds to your model version.
Platform availability
Code execution is available on:
  * **Claude API** (Anthropic)
  * **[Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)**
  * **[Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)**

Code execution is not currently available on Amazon Bedrock or Google Cloud.
For [Claude Mythos Preview](https://anthropic.com/glasswing), code execution is supported on the Claude API and Microsoft Foundry only. It is not available for Mythos Preview on Amazon Bedrock, Google Cloud, or Claude Platform on AWS.
Quick start
Here's a simple example that asks Claude to perform a calculation:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

print(response)

How code execution works
When you add the code execution tool to your API request:
  1. Claude evaluates whether code execution would help answer your question
  2. The tool automatically provides Claude with the following capabilities:
     * **Bash commands** : Execute shell commands for system operations and package management
     * **File operations** : Create, view, and edit files directly, including writing code
  3. Claude can use any combination of these capabilities in a single request
  4. All operations run in a secure sandbox environment
  5. Claude provides results with any generated charts, calculations, or analysis

### 
When Claude runs code
Claude runs code when the request benefits from computation or file handling:
  * Non-trivial math (large numbers, many steps, precision-sensitive results)
  * Data analysis, file parsing, or visualization
  * Algorithm execution or simulation
  * Explicit requests to "run", "compute", or "execute"

Claude answers directly without running code for:
  * Simple arithmetic and well-known math facts
  * Factual, conversational, or creative requests
  * Simple unit conversions or translations

If you want Claude to run code for a borderline request, ask explicitly (for example, "run code to verify this").
Using code execution with other execution tools
When you provide code execution alongside client-provided tools that also run code (such as a [bash tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool) or custom REPL), Claude is operating in a multi-computer environment. The code execution tool runs in Anthropic's sandboxed container, while your client-provided tools run in a separate environment that you control. Claude can sometimes confuse these environments, attempting to use the wrong tool or assuming state is shared between them.
To avoid this, add instructions to your system prompt that clarify the distinction:

When multiple code execution environments are available, be aware that:
- Variables, files, and state do NOT persist between different execution environments
- Use the code_execution tool for general-purpose computation in Anthropic's sandboxed environment
- Use client-provided execution tools (e.g., bash) when you need access to the user's local system, files, or data
- If you need to pass results between environments, explicitly include outputs in subsequent tool calls rather than assuming shared state

This is especially important when combining code execution with [web search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) or [web fetch](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool), which enable code execution automatically. If your application already provides a client-side shell tool, the automatic code execution creates a second execution environment that Claude needs to distinguish between.
How to use the tool
### 
Upload and analyze your own files
To analyze your own data files (such as CSV, Excel, or images), upload them through the Files API and reference them in your request:
Using the Files API with Code Execution requires the Files API beta header: `"anthropic-beta": "files-api-2025-04-14"`
The Python environment can process various file types uploaded through the Files API, including:
  * CSV
  * Excel (.xlsx, .xls)
  * JSON
  * XML
  * Images (JPEG, PNG, GIF, WebP)
  * Text files (.txt, .md, .py, and others)

#### 
Upload and analyze files
  1. **Upload your file** using the [Files API](https://platform.claude.com/docs/en/build-with-claude/files)
  2. **Reference the file** in your message using a `container_upload` content block
  3. **Include the code execution tool** in your API request

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

# Upload a file
file_object = client.beta.files.upload(
    file=open("data.csv", "rb"),
)

# Use the file_id with code execution
response = client.beta.messages.create(
    model="claude-opus-4-8",
    betas=["files-api-2025-04-14"],
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": [
                {"type": "text", "text": "Analyze this CSV data"},
                {"type": "container_upload", "file_id": file_object.id},
            ],
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

print(response)

### 
Retrieve generated files
When Claude creates files during code execution, you can retrieve these files using the Files API:
CLIPythonTypeScriptC#GoJavaPHPRuby

# Initialize the client
client = Anthropic()

# Request code execution that creates files
response = client.beta.messages.create(
    model="claude-opus-4-8",
    betas=["files-api-2025-04-14"],
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": "Create a matplotlib visualization and save it as output.png",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Extract file IDs from the response
def extract_file_ids(response):
    file_ids = []
    for item in response.content:
        if item.type == "bash_code_execution_tool_result":
            content_item = item.content
            if content_item.type == "bash_code_execution_result":
                # concrete-typed list: List[BashCodeExecutionOutputBlock]
                for file in content_item.content:
                    file_ids.append(file.file_id)
    return file_ids

# Download the created files
for file_id in extract_file_ids(response):
    file_metadata = client.beta.files.retrieve_metadata(file_id)
    file_content = client.beta.files.download(file_id)
    file_content.write_to_file(file_metadata.filename)
    print(f"Downloaded: {file_metadata.filename}")

Tool definition
The code execution tool requires no additional parameters:
JSON

  "type": "code_execution_20250825",
  "name": "code_execution"

When this tool is provided, Claude automatically gains access to two sub-tools:
  * `bash_code_execution`: Run shell commands
  * `text_editor_code_execution`: View, create, and edit files, including writing code

Response format
The code execution tool can return two types of results depending on the operation:
### 
Bash command response
Output

  "type": "server_tool_use",
  "id": "srvtoolu_01B3C4D5E6F7G8H9I0J1K2L3",
  "name": "bash_code_execution",
  "input": {
    "command": "ls -la | head -5"
  "type": "bash_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01B3C4D5E6F7G8H9I0J1K2L3",
  "content": {
    "type": "bash_code_execution_result",
    "stdout": "total 24\ndrwxr-xr-x 2 user user 4096 Jan 1 12:00 .\ndrwxr-xr-x 3 user user 4096 Jan 1 11:00 ..\n-rw-r--r-- 1 user user  220 Jan 1 12:00 data.csv\n-rw-r--r-- 1 user user  180 Jan 1 12:00 config.json",
    "stderr": "",
    "return_code": 0

### 
File operation responses
**View file:**
Output

  "type": "server_tool_use",
  "id": "srvtoolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "name": "text_editor_code_execution",
  "input": {
    "command": "view",
    "path": "config.json"
  "type": "text_editor_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01C4D5E6F7G8H9I0J1K2L3M4",
  "content": {
    "type": "text_editor_code_execution_result",
    "file_type": "text",
    "content": "{\n  \"setting\": \"value\",\n  \"debug\": true\n}",
    "numLines": 4,
    "startLine": 1,
    "totalLines": 4

**Create file:**
Output

  "type": "server_tool_use",
  "id": "srvtoolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "name": "text_editor_code_execution",
  "input": {
    "command": "create",
    "path": "new_file.txt",
    "file_text": "Hello, World!"
  "type": "text_editor_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01D5E6F7G8H9I0J1K2L3M4N5",
  "content": {
    "type": "text_editor_code_execution_result",
    "is_file_update": false

**Edit file (str_replace):**
Output

  "type": "server_tool_use",
  "id": "srvtoolu_01E6F7G8H9I0J1K2L3M4N5O6",
  "name": "text_editor_code_execution",
  "input": {
    "command": "str_replace",
    "path": "config.json",
    "old_str": "\"debug\": true",
    "new_str": "\"debug\": false"
  "type": "text_editor_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01E6F7G8H9I0J1K2L3M4N5O6",
  "content": {
    "type": "text_editor_code_execution_result",
    "oldStart": 3,
    "oldLines": 1,
    "newStart": 3,
    "newLines": 1,
    "lines": ["-  \"debug\": true", "+  \"debug\": false"]

### 
Results
All execution results include:
  * `stdout`: Output from successful execution
  * `stderr`: Error messages if execution fails
  * `return_code`: 0 for success, non-zero for failure

Additional fields for file operations:
  * **View** : `file_type`, `content`, `numLines`, `startLine`, `totalLines`
  * **Create** : `is_file_update` (whether file already existed)
  * **Edit** : `oldStart`, `oldLines`, `newStart`, `newLines`, `lines` (diff format)

### 
Errors
Each tool type can return specific errors:
**Common errors (all tools):**
Output

  "type": "bash_code_execution_tool_result",
  "tool_use_id": "srvtoolu_01VfmxgZ46TiHbmXgy928hQR",
  "content": {
    "type": "bash_code_execution_tool_result_error",
    "error_code": "unavailable"

**Error codes by tool type:**  
| Tool  | Error Code  | Description  |  
| --- | --- | --- |  
| All tools  | `unavailable`  | The tool is temporarily unavailable  |  
| All tools  | `execution_time_exceeded`  | Execution exceeded maximum time limit  |  
| All tools  | `container_expired`  | Container expired and is no longer available  |  
| All tools  | `invalid_tool_input`  | Invalid parameters provided to the tool  |  
| All tools  | `too_many_requests`  | Rate limit exceeded for tool usage  |  
| bash  | `output_file_too_large`  | Command output exceeded the maximum size  |  
| text_editor  | `file_not_found`  | File doesn't exist (for view/edit operations)  |  
| text_editor  | `string_not_found`  | The `old_str` not found in file (for str_replace)  |  
#### 
`pause_turn` stop reason
The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running turn. You may provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you wish to interrupt the conversation.
Containers
The code execution tool runs in a secure, containerized environment designed specifically for code execution, with a higher focus on Python.
### 
Runtime environment
  * **Python version** : 3.11.12
  * **Operating system** : Linux-based container
  * **Architecture** : x86_64 (AMD64)

### 
Resource limits
  * **Memory** : 5GiB RAM
  * **Disk space** : 5GiB workspace storage
  * **CPU** : 1 CPU

### 
Networking and security
  * **Internet access** : Completely disabled for security
  * **External connections** : No outbound network requests permitted
  * **Sandbox isolation** : Full isolation from host system and other containers
  * **File access** : Limited to workspace directory only
  * **Workspace scoping** : Like [Files](https://platform.claude.com/docs/en/build-with-claude/files), containers are scoped to the workspace of the API key
  * **Expiration** : Containers expire 30 days after creation

### 
Pre-installed libraries
The sandboxed Python environment includes these commonly used libraries:
  * **Data Science** : pandas, numpy, scipy, scikit-learn, statsmodels
  * **Visualization** : matplotlib, seaborn
  * **File Processing** : pyarrow, openpyxl, xlsxwriter, xlrd, pillow, python-pptx, python-docx, pypdf, pdfplumber, pypdfium2, pdf2image, pdfkit, tabula-py, reportlab[pycairo], Img2pdf
  * **Math & Computing**: sympy, mpmath
  * **Utilities** : tqdm, python-dateutil, pytz, joblib, unzip, unrar, 7zip, bc, rg (ripgrep), fd, sqlite

Container reuse
You can reuse an existing container across multiple API requests by providing the container ID from a previous response. This allows you to maintain created files between requests.
### 
Example
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# First request: Create a file with a random number
response1 = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": "Write a file with a random number and save it to '/tmp/number.txt'",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Extract the container ID from the first response
container_id = response1.container.id

# Second request: Reuse the container to read the file
response2 = client.messages.create(
    container=container_id,  # Reuse the same container
    model="claude-opus-4-8",
    max_tokens=4096,
    messages=[
            "role": "user",
            "content": "Read the number from '/tmp/number.txt' and calculate its square",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

print(response2)

Streaming
With streaming enabled, you'll receive code execution events as they occur:

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "server_tool_use", "id": "srvtoolu_xyz789", "name": "code_execution"}}

// Code execution streamed
event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "input_json_delta", "partial_json": "{\"code\":\"import pandas as pd\\ndf = pd.read_csv('data.csv')\\nprint(df.head())\"}"}}

// Pause while code executes

// Execution results streamed
event: content_block_start
data: {"type": "content_block_start", "index": 2, "content_block": {"type": "code_execution_tool_result", "tool_use_id": "srvtoolu_xyz789", "content": {"stdout": "   A  B  C\n0  1  2  3\n1  4  5  6", "stderr": ""}}}

Batch requests
You can include the code execution tool in the [Messages Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing). Code execution tool calls through the Messages Batches API are priced the same as those in regular Messages API requests.
Usage and pricing
**Code execution is free when used with web search or web fetch.** When `web_search_20260209` (or later) or `web_fetch_20260209` (or later) is included in your API request, there are no additional charges for code execution tool calls beyond the standard input and output token costs.
When used without these tools, code execution is billed by execution time, tracked separately from token usage:
  * Execution time has a minimum of 5 minutes
  * Each organization receives **1,550 free hours** of usage per month
  * Additional usage beyond 1,550 hours is billed at **$0.05 per hour, per container**
  * If files are included in the request, execution time is billed even if the tool is not invoked, due to files being preloaded onto the container

Code execution usage is tracked in the response:

  "usage": {
    "input_tokens": 105,
    "output_tokens": 239,
    "server_tool_use": {
      "code_execution_requests": 1

Upgrade to latest tool version
By upgrading to `code-execution-2025-08-25`, you get access to file manipulation and Bash capabilities, including code in multiple languages. There is no price difference.
### 
What's changed  
| Component  | Legacy  | Current  |  
| --- | --- | --- |  
| Beta header  | `code-execution-2025-05-22`  | `code-execution-2025-08-25`  |  
| Tool type  | `code_execution_20250522`  | `code_execution_20250825`  |  
| Capabilities  | Python only  | Bash commands, file operations  |  
| Response types  | `code_execution_result`  |  `bash_code_execution_result`, `text_editor_code_execution_result`  |  
### 
Backward compatibility
  * All existing Python code execution continues to work exactly as before
  * No changes required to existing Python-only workflows

### 
Upgrade steps
To upgrade, update the tool type in your API requests:

- "type": "code_execution_20250522"
+ "type": "code_execution_20250825"

**Review response handling** (if parsing responses programmatically):
  * The previous blocks for Python execution responses will no longer be sent
  * Instead, new response types for Bash and file operations will be sent (see Response Format section)

Programmatic tool calling
For running tools inside the code execution container, see [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling).
Data retention
Code execution runs in server-side sandbox containers. Container data, including execution artifacts, uploaded files, and outputs, is retained for up to 30 days. This retention applies to all data processed within the container environment. Files that code execution creates in the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) (retrievable via `client.beta.files.download()`) persist until explicitly deleted.
For ZDR eligibility across all features, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention).
Using code execution with Agent Skills
The code execution tool enables Claude to use [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). Skills are modular capabilities consisting of instructions, scripts, and resources that extend Claude's functionality.
Learn more in [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) and [Using Agent Skills with the API](https://platform.claude.com/docs/en/build-with-claude/skills-guide).
