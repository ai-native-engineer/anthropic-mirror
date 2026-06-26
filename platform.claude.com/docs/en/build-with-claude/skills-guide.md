<!-- source: https://platform.claude.com/docs/en/build-with-claude/skills-guide -->

# Using Agent Skills with the API
Learn how to use Agent Skills to extend Claude's capabilities through the API.
Agent Skills extend Claude's capabilities through organized folders of instructions, scripts, and resources. This guide shows you how to use both pre-built and custom Skills with the Claude API.
For complete API reference including request/response schemas and all parameters, see:
  * [Skill Management API Reference](https://platform.claude.com/docs/en/api/skills/list-skills) - CRUD operations for Skills
  * [Skill Versions API Reference](https://platform.claude.com/docs/en/api/skills/list-skill-versions) - Version management

This feature is **not** eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). Data is retained according to the feature's standard retention policy.
Quick links
[ Get started with Agent Skills Create your first Skill ](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)[ Create custom Skills Best practices for authoring Skills ](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
Overview
For a deep dive into the architecture and real-world applications of Agent Skills, read the engineering blog post: [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).
Skills integrate with the Messages API through the [code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool). Whether using pre-built Skills managed by Anthropic or custom Skills you've uploaded, the integration shape is identical: both require code execution and use the same `container` structure.
### 
Using Skills
Skills integrate identically in the Messages API regardless of source. You specify Skills in the `container` parameter with a `skill_id`, `type`, and optional `version`, and they execute in the code execution environment.
**You can use Skills from two sources:**  
| Aspect  | Anthropic Skills  | Custom Skills  |  
| --- | --- | --- |  
| **Type value**  | `anthropic`  | `custom`  |  
| **Skill IDs**  | Short names: `pptx`, `xlsx`, `docx`, `pdf`  | Generated: `skill_01AbCdEfGhIjKlMnOpQrStUv`  |  
| **Version format**  | Date-based: `20251013` or `latest`  | Epoch timestamp: `1759178010641129` or `latest`  |  
| **Management**  | Pre-built and maintained by Anthropic  | Upload and manage through the [Skills API](https://platform.claude.com/docs/en/api/skills/create-skill)  |  
| **Availability**  | Available to all users  | Private to your workspace  |  
Both skill sources are returned by the [List Skills endpoint](https://platform.claude.com/docs/en/api/skills/list-skills) (use the `source` parameter to filter). The integration shape and execution environment are identical. The only difference is where the Skills come from and how they're managed.
### 
Prerequisites
To use Skills, you need:
  1. **Claude API key** from the [Console](https://platform.claude.com/settings/keys)
  2. **Beta headers:**
     * `code-execution-2025-08-25` - Enables code execution (required for Skills)
     * `skills-2025-10-02` - Enables Skills API
     * `files-api-2025-04-14` - For uploading/downloading files to/from container
  3. **[Code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)** enabled in your requests

* * *
Using Skills in Messages
### 
Container parameter
Skills are specified using the `container` parameter in the Messages API. You can include up to 8 Skills per request.
The structure is identical for both Anthropic and custom Skills. Specify the required `type` and `skill_id`, and optionally include `version` to pin to a specific version:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]
    messages=[
        {"role": "user", "content": "Create a presentation about renewable energy"}
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

### 
Downloading generated files
When Skills create documents (Excel, PowerPoint, PDF, Word), they return `file_id` attributes in the response. You must use the Files API to download these files.
**How it works:**
  1. Skills create files during code execution
  2. Response includes `file_id` for each created file
  3. Use Files API to download the actual file content
  4. Save locally or process as needed

**Example: Creating and downloading an Excel file**
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

# Step 1: Use a Skill to create a file
response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    messages=[
            "role": "user",
            "content": "Create an Excel file with a simple budget spreadsheet",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Step 2: Extract file IDs from the response
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

# Step 3: Download the file using Files API
for file_id in extract_file_ids(response):
    file_metadata = client.beta.files.retrieve_metadata(file_id=file_id)
    file_content = client.beta.files.download(file_id=file_id)

    # Step 4: Save to disk
    file_content.write_to_file(file_metadata.filename)
    print(f"Downloaded: {file_metadata.filename}")

**Additional Files API operations:**
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()
file_id = "file_abc123"
# Get file metadata
file_info = client.beta.files.retrieve_metadata(file_id=file_id)
print(f"Filename: {file_info.filename}, Size: {file_info.size_bytes} bytes")

# List all files
files = client.beta.files.list()
for file in files.data:
    print(f"{file.filename} - {file.created_at}")

# Delete a file
client.beta.files.delete(file_id=file_id)

For complete details on the Files API, see the [Files API documentation](https://platform.claude.com/docs/en/api/files-content).
### 
Multi-turn conversations
Reuse the same container across multiple messages by specifying the container ID:
CLIPythonTypeScriptC#GoJavaPHPRuby

# First request creates container
response1 = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    messages=[{"role": "user", "content": "Analyze this sales data"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Continue conversation with same container
messages = [
    {"role": "user", "content": "Analyze this sales data"},
    {"role": "assistant", "content": response1.content},
    {"role": "user", "content": "What was the total revenue?"},
]

response2 = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "id": response1.container.id,  # Reuse container
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}],
    messages=messages,
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

### 
Long-running operations
Skills may perform operations that require multiple turns. Handle `pause_turn` stop reasons:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

messages = [{"role": "user", "content": "Process this large dataset"}]
max_retries = 10

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest",
        ]
    messages=messages,
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Handle pause_turn for long operations
for i in range(max_retries):
    if response.stop_reason != "pause_turn":
        break

    messages.append({"role": "assistant", "content": response.content})
    response = client.beta.messages.create(
        model="claude-opus-4-8",
        max_tokens=4096,
        betas=["code-execution-2025-08-25", "skills-2025-10-02"],
        container={
            "id": response.container.id,
            "skills": [
                    "type": "custom",
                    "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                    "version": "latest",
            ],
        messages=messages,
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    )

The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running Skill operation. You can provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you wish to interrupt the conversation and provide additional guidance.
### 
Using Multiple Skills
Combine multiple Skills in a single request to handle complex workflows:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "anthropic", "skill_id": "pptx", "version": "latest"},
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest",
        ]
    messages=[
        {"role": "user", "content": "Analyze sales data and create a presentation"}
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

* * *
Managing Custom Skills
### 
Creating a Skill
A Skill bundle is a directory containing a `SKILL.md` file at the top level with `name` and `description` YAML frontmatter, plus any supporting scripts or resources. See [Get started with Agent Skills in the API](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart) to author one, and the **Requirements** list following the examples for the full constraints.
Upload your custom Skill to make it available in your workspace. You can upload a zip archive or individual file objects; the Python SDK additionally provides a `files_from_dir` helper that accepts a directory path.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Option 1: Upload individual files (one --file flag per file)
ant beta:skills create \
  --display-title "Financial Analysis" \
  --file financial_skill/SKILL.md \
  --file financial_skill/analyze.py \
  --beta skills-2025-10-02

# Option 2: Upload a zip archive
ant beta:skills create \
  --display-title "Financial Analysis" \
  --file financial_analysis_skill.zip \
  --beta skills-2025-10-02

**Requirements:**
  * Must include a SKILL.md file at the top level
  * All files must specify a common root directory in their paths
  * Total upload size must be under 30 MB
  * YAML frontmatter requirements:
    * `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
    * `description`: Maximum 1024 characters, non-empty, no XML tags

For complete request/response schemas, see the [Create Skill API reference](https://platform.claude.com/docs/en/api/skills/create-skill).
### 
Listing Skills
Retrieve all Skills available to your workspace, including both Anthropic pre-built Skills and your custom Skills. Use the `source` parameter to filter by skill type:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# List all Skills
ant beta:skills list

# List only custom Skills
ant beta:skills list --source custom

See the [List Skills API reference](https://platform.claude.com/docs/en/api/skills/list-skills) for pagination and filtering options.
### 
Retrieving a Skill
Get details about a specific Skill:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:skills retrieve \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv

### 
Deleting a Skill
To delete a Skill, you must first delete all its versions:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Step 1: Delete all versions
ant beta:skills:versions list \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv \
  --transform version --raw-output \
  | while read -r VERSION; do
      ant beta:skills:versions delete \
        --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv \
        --version "$VERSION" >/dev/null
    done

# Step 2: Delete the Skill
ant beta:skills delete \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv >/dev/null

Attempting to delete a Skill with existing versions returns a 400 error.
### 
Versioning
Skills support versioning to manage updates safely:
**Anthropic Skills:**
  * Versions use date format: `20251013`
  * New versions released as updates are made
  * Specify exact versions for stability

**Custom Skills:**
  * Auto-generated epoch timestamps: `1759178010641129`
  * Use `"latest"` to always get the most recent version
  * Create new versions when updating Skill files

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Create a new version
VERSION_NUMBER=$(ant beta:skills:versions create \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv \
  --file updated_skill/SKILL.md \
  --transform version --raw-output)

# Use specific version
ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 <<YAML
model: claude-opus-4-8
max_tokens: 4096
container:
  skills:
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: $VERSION_NUMBER
messages:
  - role: user
    content: Use updated Skill
tools:
  - type: code_execution_20250825
    name: code_execution
YAML

# Use latest version
ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 <<'YAML'
model: claude-opus-4-8
max_tokens: 4096
container:
  skills:
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: latest
messages:
  - role: user
    content: Use latest Skill version
tools:
  - type: code_execution_20250825
    name: code_execution
YAML

See the [Create Skill Version API reference](https://platform.claude.com/docs/en/api/skills/create-skill-version) for complete details.
* * *
How Skills are loaded
When you specify Skills in a container:
  1. **Metadata Discovery:** Claude sees metadata for each Skill (name, description) in the system prompt
  2. **File Loading:** Skill files are copied into the container at `/skills/{directory}/`
  3. **Automatic Use:** Claude automatically loads and uses Skills when relevant to your request
  4. **Composition:** Multiple Skills compose together for complex workflows

The progressive disclosure architecture ensures efficient context usage: Claude only loads full Skill instructions when needed.
* * *
Use cases
### 
Organizational Skills
**Brand & Communications**
  * Apply company-specific formatting (colors, fonts, layouts) to documents
  * Generate communications following organizational templates
  * Ensure consistent brand guidelines across all outputs

**Project Management**
  * Structure notes with company-specific formats (OKRs, decision logs)
  * Generate tasks following team conventions
  * Create standardized meeting recaps and status updates

**Business Operations**
  * Create company-standard reports, proposals, and analyses
  * Execute company-specific analytical procedures
  * Generate financial models following organizational templates

### 
Personal Skills
**Content Creation**
  * Custom document templates
  * Specialized formatting and styling
  * Domain-specific content generation

**Data Analysis**
  * Custom data processing pipelines
  * Specialized visualization templates
  * Industry-specific analytical methods

**Development & Automation**
  * Code generation templates
  * Testing frameworks
  * Deployment workflows

### 
Example: financial modeling
Combine Excel and custom DCF analysis Skills:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Create custom DCF analysis Skill
from anthropic.lib import files_from_dir

dcf_skill = client.beta.skills.create(
    display_title="DCF Analysis",
    files=files_from_dir("/path/to/dcf_skill"),
)

# Use with Excel to create financial model
response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "custom", "skill_id": dcf_skill.id, "version": "latest"},
        ]
    messages=[
            "role": "user",
            "content": "Build a DCF valuation model for a SaaS company with the attached financials",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
print(response)

* * *
Limits and constraints
### 
Request limits
  * **Maximum Skills per request:** 8
  * **Maximum Skill upload size:** 30 MB (all files combined)
  * **YAML frontmatter requirements:**
    * `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
    * `description`: Maximum 1024 characters, non-empty, no XML tags

### 
Environment constraints
Skills run in the code execution container with these limitations:
  * **No network access:** Cannot make external API calls
  * **No runtime package installation:** Only pre-installed packages available
  * **Isolated environment:** Containers are isolated; a fresh container is created unless you specify an existing container ID

See [Code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) for available packages.
* * *
Best practices
### 
When to use multiple Skills
Combine Skills when tasks involve multiple document types or domains:
**Good use cases:**
  * Data analysis (Excel) + presentation creation (PowerPoint)
  * Report generation (Word) + export to PDF
  * Custom domain logic + document generation

**Avoid:**
  * Including unused Skills (impacts performance)

### 
Version management strategy
**For production:**

# Pin to specific versions for stability
container = {
    "skills": [
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "1759178010641129",  # Specific version
    ]

**For development:**

# Use latest for active development
container = {
    "skills": [
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "latest",  # Always get newest
    ]

### 
Prompt caching considerations
When using prompt caching, note that changing the Skills list in your container breaks the cache:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# First request creates cache
response1 = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
        "prompt-caching-2024-07-31",
    ],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    messages=[{"role": "user", "content": "Analyze sales data"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Adding/removing Skills breaks cache
response2 = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
        "prompt-caching-2024-07-31",
    ],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest",
            },  # Cache miss
        ]
    messages=[{"role": "user", "content": "Create a presentation"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

For best caching performance, keep your Skills list consistent across requests.
### 
Error handling
Handle Skill-related errors gracefully:
CLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

try:
    response = client.beta.messages.create(
        model="claude-opus-4-8",
        max_tokens=4096,
        betas=["code-execution-2025-08-25", "skills-2025-10-02"],
        container={
            "skills": [
                    "type": "custom",
                    "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                    "version": "latest",
            ]
        messages=[{"role": "user", "content": "Process data"}],
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    )
except anthropic.BadRequestError as e:
    if "skill" in str(e):
        print(f"Skill error: {e}")
        # Handle skill-specific errors
    else:
        raise

* * *
Data retention
Agent Skills are not covered by ZDR arrangements. Skill definitions and execution data are retained according to Anthropic's standard data retention policy.
For ZDR eligibility across all features, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention).
Next steps
[  API Reference Complete API reference with all endpoints ](https://platform.claude.com/docs/en/api/skills/create-skill)[  Authoring Guide Best practices for writing effective Skills ](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)[ Code Execution Tool Learn about the code execution environment ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)
  * [Quick links](https://platform.claude.com/docs/en/build-with-claude/skills-guide#quick-links)
  * [Overview](https://platform.claude.com/docs/en/build-with-claude/skills-guide#overview)
  * [Using Skills](https://platform.claude.com/docs/en/build-with-claude/skills-guide#using-skills)
  * [Prerequisites](https://platform.claude.com/docs/en/build-with-claude/skills-guide#prerequisites)
  * [Using Skills in Messages](https://platform.claude.com/docs/en/build-with-claude/skills-guide#using-skills-in-messages)
  * [Container parameter](https://platform.claude.com/docs/en/build-with-claude/skills-guide#container-parameter)
  * [Downloading generated files](https://platform.claude.com/docs/en/build-with-claude/skills-guide#downloading-generated-files)
  * [Multi-turn conversations](https://platform.claude.com/docs/en/build-with-claude/skills-guide#multi-turn-conversations)
  * [Long-running operations](https://platform.claude.com/docs/en/build-with-claude/skills-guide#long-running-operations)
  * [Using Multiple Skills](https://platform.claude.com/docs/en/build-with-claude/skills-guide#using-multiple-skills)
  * [Managing Custom Skills](https://platform.claude.com/docs/en/build-with-claude/skills-guide#managing-custom-skills)
  * [Creating a Skill](https://platform.claude.com/docs/en/build-with-claude/skills-guide#creating-a-skill)
  * [Listing Skills](https://platform.claude.com/docs/en/build-with-claude/skills-guide#listing-skills)
  * [Retrieving a Skill](https://platform.claude.com/docs/en/build-with-claude/skills-guide#retrieving-a-skill)
  * [Deleting a Skill](https://platform.claude.com/docs/en/build-with-claude/skills-guide#deleting-a-skill)
  * [Versioning](https://platform.claude.com/docs/en/build-with-claude/skills-guide#versioning)
  * [How Skills are loaded](https://platform.claude.com/docs/en/build-with-claude/skills-guide#how-skills-are-loaded)
  * [Use cases](https://platform.claude.com/docs/en/build-with-claude/skills-guide#use-cases)
  * [Organizational Skills](https://platform.claude.com/docs/en/build-with-claude/skills-guide#organizational-skills)
  * [Personal Skills](https://platform.claude.com/docs/en/build-with-claude/skills-guide#personal-skills)
  * [Example: financial modeling](https://platform.claude.com/docs/en/build-with-claude/skills-guide#example-financial-modeling)
  * [Limits and constraints](https://platform.claude.com/docs/en/build-with-claude/skills-guide#limits-and-constraints)
  * [Request limits](https://platform.claude.com/docs/en/build-with-claude/skills-guide#request-limits)
  * [Environment constraints](https://platform.claude.com/docs/en/build-with-claude/skills-guide#environment-constraints)
  * [Best practices](https://platform.claude.com/docs/en/build-with-claude/skills-guide#best-practices)
  * [When to use multiple Skills](https://platform.claude.com/docs/en/build-with-claude/skills-guide#when-to-use-multiple-skills)
  * [Version management strategy](https://platform.claude.com/docs/en/build-with-claude/skills-guide#version-management-strategy)
  * [Prompt caching considerations](https://platform.claude.com/docs/en/build-with-claude/skills-guide#prompt-caching-considerations)
  * [Error handling](https://platform.claude.com/docs/en/build-with-claude/skills-guide#error-handling)
  * [Data retention](https://platform.claude.com/docs/en/build-with-claude/skills-guide#data-retention)
  * [Next steps](https://platform.claude.com/docs/en/build-with-claude/skills-guide#next-steps)

Messages/Skills
# Using Agent Skills with the API
Learn how to use Agent Skills to extend Claude's capabilities through the API.
Agent Skills extend Claude's capabilities through organized folders of instructions, scripts, and resources. This guide shows you how to use both pre-built and custom Skills with the Claude API.
For complete API reference including request/response schemas and all parameters, see:
  * [Skill Management API Reference](https://platform.claude.com/docs/en/api/skills/list-skills) - CRUD operations for Skills
  * [Skill Versions API Reference](https://platform.claude.com/docs/en/api/skills/list-skill-versions) - Version management

This feature is **not** eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). Data is retained according to the feature's standard retention policy.
Quick links
[ Get started with Agent Skills Create your first Skill ](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)[ Create custom Skills Best practices for authoring Skills ](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
Overview
For a deep dive into the architecture and real-world applications of Agent Skills, read the engineering blog post: [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).
Skills integrate with the Messages API through the [code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool). Whether using pre-built Skills managed by Anthropic or custom Skills you've uploaded, the integration shape is identical: both require code execution and use the same `container` structure.
### 
Using Skills
Skills integrate identically in the Messages API regardless of source. You specify Skills in the `container` parameter with a `skill_id`, `type`, and optional `version`, and they execute in the code execution environment.
**You can use Skills from two sources:**  
| Aspect  | Anthropic Skills  | Custom Skills  |  
| --- | --- | --- |  
| **Type value**  | `anthropic`  | `custom`  |  
| **Skill IDs**  | Short names: `pptx`, `xlsx`, `docx`, `pdf`  | Generated: `skill_01AbCdEfGhIjKlMnOpQrStUv`  |  
| **Version format**  | Date-based: `20251013` or `latest`  | Epoch timestamp: `1759178010641129` or `latest`  |  
| **Management**  | Pre-built and maintained by Anthropic  | Upload and manage through the [Skills API](https://platform.claude.com/docs/en/api/skills/create-skill)  |  
| **Availability**  | Available to all users  | Private to your workspace  |  
Both skill sources are returned by the [List Skills endpoint](https://platform.claude.com/docs/en/api/skills/list-skills) (use the `source` parameter to filter). The integration shape and execution environment are identical. The only difference is where the Skills come from and how they're managed.
### 
Prerequisites
To use Skills, you need:
  1. **Claude API key** from the [Console](https://platform.claude.com/settings/keys)
  2. **Beta headers:**
     * `code-execution-2025-08-25` - Enables code execution (required for Skills)
     * `skills-2025-10-02` - Enables Skills API
     * `files-api-2025-04-14` - For uploading/downloading files to/from container
  3. **[Code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)** enabled in your requests

* * *
Using Skills in Messages
### 
Container parameter
Skills are specified using the `container` parameter in the Messages API. You can include up to 8 Skills per request.
The structure is identical for both Anthropic and custom Skills. Specify the required `type` and `skill_id`, and optionally include `version` to pin to a specific version:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]
    messages=[
        {"role": "user", "content": "Create a presentation about renewable energy"}
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

### 
Downloading generated files
When Skills create documents (Excel, PowerPoint, PDF, Word), they return `file_id` attributes in the response. You must use the Files API to download these files.
**How it works:**
  1. Skills create files during code execution
  2. Response includes `file_id` for each created file
  3. Use Files API to download the actual file content
  4. Save locally or process as needed

**Example: Creating and downloading an Excel file**
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

# Step 1: Use a Skill to create a file
response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    messages=[
            "role": "user",
            "content": "Create an Excel file with a simple budget spreadsheet",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Step 2: Extract file IDs from the response
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

# Step 3: Download the file using Files API
for file_id in extract_file_ids(response):
    file_metadata = client.beta.files.retrieve_metadata(file_id=file_id)
    file_content = client.beta.files.download(file_id=file_id)

    # Step 4: Save to disk
    file_content.write_to_file(file_metadata.filename)
    print(f"Downloaded: {file_metadata.filename}")

**Additional Files API operations:**
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()
file_id = "file_abc123"
# Get file metadata
file_info = client.beta.files.retrieve_metadata(file_id=file_id)
print(f"Filename: {file_info.filename}, Size: {file_info.size_bytes} bytes")

# List all files
files = client.beta.files.list()
for file in files.data:
    print(f"{file.filename} - {file.created_at}")

# Delete a file
client.beta.files.delete(file_id=file_id)

For complete details on the Files API, see the [Files API documentation](https://platform.claude.com/docs/en/api/files-content).
### 
Multi-turn conversations
Reuse the same container across multiple messages by specifying the container ID:
CLIPythonTypeScriptC#GoJavaPHPRuby

# First request creates container
response1 = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    messages=[{"role": "user", "content": "Analyze this sales data"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Continue conversation with same container
messages = [
    {"role": "user", "content": "Analyze this sales data"},
    {"role": "assistant", "content": response1.content},
    {"role": "user", "content": "What was the total revenue?"},
]

response2 = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "id": response1.container.id,  # Reuse container
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}],
    messages=messages,
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

### 
Long-running operations
Skills may perform operations that require multiple turns. Handle `pause_turn` stop reasons:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

messages = [{"role": "user", "content": "Process this large dataset"}]
max_retries = 10

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest",
        ]
    messages=messages,
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Handle pause_turn for long operations
for i in range(max_retries):
    if response.stop_reason != "pause_turn":
        break

    messages.append({"role": "assistant", "content": response.content})
    response = client.beta.messages.create(
        model="claude-opus-4-8",
        max_tokens=4096,
        betas=["code-execution-2025-08-25", "skills-2025-10-02"],
        container={
            "id": response.container.id,
            "skills": [
                    "type": "custom",
                    "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                    "version": "latest",
            ],
        messages=messages,
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    )

The response may include a `pause_turn` stop reason, which indicates that the API paused a long-running Skill operation. You can provide the response back as-is in a subsequent request to let Claude continue its turn, or modify the content if you wish to interrupt the conversation and provide additional guidance.
### 
Using Multiple Skills
Combine multiple Skills in a single request to handle complex workflows:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "anthropic", "skill_id": "pptx", "version": "latest"},
                "type": "custom",
                "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                "version": "latest",
        ]
    messages=[
        {"role": "user", "content": "Analyze sales data and create a presentation"}
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

* * *
Managing Custom Skills
### 
Creating a Skill
A Skill bundle is a directory containing a `SKILL.md` file at the top level with `name` and `description` YAML frontmatter, plus any supporting scripts or resources. See [Get started with Agent Skills in the API](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart) to author one, and the **Requirements** list following the examples for the full constraints.
Upload your custom Skill to make it available in your workspace. You can upload a zip archive or individual file objects; the Python SDK additionally provides a `files_from_dir` helper that accepts a directory path.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Option 1: Upload individual files (one --file flag per file)
ant beta:skills create \
  --display-title "Financial Analysis" \
  --file financial_skill/SKILL.md \
  --file financial_skill/analyze.py \
  --beta skills-2025-10-02

# Option 2: Upload a zip archive
ant beta:skills create \
  --display-title "Financial Analysis" \
  --file financial_analysis_skill.zip \
  --beta skills-2025-10-02

**Requirements:**
  * Must include a SKILL.md file at the top level
  * All files must specify a common root directory in their paths
  * Total upload size must be under 30 MB
  * YAML frontmatter requirements:
    * `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
    * `description`: Maximum 1024 characters, non-empty, no XML tags

For complete request/response schemas, see the [Create Skill API reference](https://platform.claude.com/docs/en/api/skills/create-skill).
### 
Listing Skills
Retrieve all Skills available to your workspace, including both Anthropic pre-built Skills and your custom Skills. Use the `source` parameter to filter by skill type:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# List all Skills
ant beta:skills list

# List only custom Skills
ant beta:skills list --source custom

See the [List Skills API reference](https://platform.claude.com/docs/en/api/skills/list-skills) for pagination and filtering options.
### 
Retrieving a Skill
Get details about a specific Skill:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:skills retrieve \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv

### 
Deleting a Skill
To delete a Skill, you must first delete all its versions:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Step 1: Delete all versions
ant beta:skills:versions list \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv \
  --transform version --raw-output \
  | while read -r VERSION; do
      ant beta:skills:versions delete \
        --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv \
        --version "$VERSION" >/dev/null
    done

# Step 2: Delete the Skill
ant beta:skills delete \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv >/dev/null

Attempting to delete a Skill with existing versions returns a 400 error.
### 
Versioning
Skills support versioning to manage updates safely:
**Anthropic Skills:**
  * Versions use date format: `20251013`
  * New versions released as updates are made
  * Specify exact versions for stability

**Custom Skills:**
  * Auto-generated epoch timestamps: `1759178010641129`
  * Use `"latest"` to always get the most recent version
  * Create new versions when updating Skill files

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Create a new version
VERSION_NUMBER=$(ant beta:skills:versions create \
  --skill-id skill_01AbCdEfGhIjKlMnOpQrStUv \
  --file updated_skill/SKILL.md \
  --transform version --raw-output)

# Use specific version
ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 <<YAML
model: claude-opus-4-8
max_tokens: 4096
container:
  skills:
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: $VERSION_NUMBER
messages:
  - role: user
    content: Use updated Skill
tools:
  - type: code_execution_20250825
    name: code_execution
YAML

# Use latest version
ant beta:messages create \
  --beta code-execution-2025-08-25 \
  --beta skills-2025-10-02 <<'YAML'
model: claude-opus-4-8
max_tokens: 4096
container:
  skills:
    - type: custom
      skill_id: skill_01AbCdEfGhIjKlMnOpQrStUv
      version: latest
messages:
  - role: user
    content: Use latest Skill version
tools:
  - type: code_execution_20250825
    name: code_execution
YAML

See the [Create Skill Version API reference](https://platform.claude.com/docs/en/api/skills/create-skill-version) for complete details.
* * *
How Skills are loaded
When you specify Skills in a container:
  1. **Metadata Discovery:** Claude sees metadata for each Skill (name, description) in the system prompt
  2. **File Loading:** Skill files are copied into the container at `/skills/{directory}/`
  3. **Automatic Use:** Claude automatically loads and uses Skills when relevant to your request
  4. **Composition:** Multiple Skills compose together for complex workflows

The progressive disclosure architecture ensures efficient context usage: Claude only loads full Skill instructions when needed.
* * *
Use cases
### 
Organizational Skills
**Brand & Communications**
  * Apply company-specific formatting (colors, fonts, layouts) to documents
  * Generate communications following organizational templates
  * Ensure consistent brand guidelines across all outputs

**Project Management**
  * Structure notes with company-specific formats (OKRs, decision logs)
  * Generate tasks following team conventions
  * Create standardized meeting recaps and status updates

**Business Operations**
  * Create company-standard reports, proposals, and analyses
  * Execute company-specific analytical procedures
  * Generate financial models following organizational templates

### 
Personal Skills
**Content Creation**
  * Custom document templates
  * Specialized formatting and styling
  * Domain-specific content generation

**Data Analysis**
  * Custom data processing pipelines
  * Specialized visualization templates
  * Industry-specific analytical methods

**Development & Automation**
  * Code generation templates
  * Testing frameworks
  * Deployment workflows

### 
Example: financial modeling
Combine Excel and custom DCF analysis Skills:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Create custom DCF analysis Skill
from anthropic.lib import files_from_dir

dcf_skill = client.beta.skills.create(
    display_title="DCF Analysis",
    files=files_from_dir("/path/to/dcf_skill"),
)

# Use with Excel to create financial model
response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
            {"type": "custom", "skill_id": dcf_skill.id, "version": "latest"},
        ]
    messages=[
            "role": "user",
            "content": "Build a DCF valuation model for a SaaS company with the attached financials",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)
print(response)

* * *
Limits and constraints
### 
Request limits
  * **Maximum Skills per request:** 8
  * **Maximum Skill upload size:** 30 MB (all files combined)
  * **YAML frontmatter requirements:**
    * `name`: Maximum 64 characters, lowercase letters/numbers/hyphens only, no XML tags, no reserved words ("anthropic", "claude")
    * `description`: Maximum 1024 characters, non-empty, no XML tags

### 
Environment constraints
Skills run in the code execution container with these limitations:
  * **No network access:** Cannot make external API calls
  * **No runtime package installation:** Only pre-installed packages available
  * **Isolated environment:** Containers are isolated; a fresh container is created unless you specify an existing container ID

See [Code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) for available packages.
* * *
Best practices
### 
When to use multiple Skills
Combine Skills when tasks involve multiple document types or domains:
**Good use cases:**
  * Data analysis (Excel) + presentation creation (PowerPoint)
  * Report generation (Word) + export to PDF
  * Custom domain logic + document generation

**Avoid:**
  * Including unused Skills (impacts performance)

### 
Version management strategy
**For production:**

# Pin to specific versions for stability
container = {
    "skills": [
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "1759178010641129",  # Specific version
    ]

**For development:**

# Use latest for active development
container = {
    "skills": [
            "type": "custom",
            "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
            "version": "latest",  # Always get newest
    ]

### 
Prompt caching considerations
When using prompt caching, note that changing the Skills list in your container breaks the cache:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# First request creates cache
response1 = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
        "prompt-caching-2024-07-31",
    ],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    messages=[{"role": "user", "content": "Analyze sales data"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

# Adding/removing Skills breaks cache
response2 = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=4096,
    betas=[
        "code-execution-2025-08-25",
        "skills-2025-10-02",
        "prompt-caching-2024-07-31",
    ],
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"},
                "type": "anthropic",
                "skill_id": "pptx",
                "version": "latest",
            },  # Cache miss
        ]
    messages=[{"role": "user", "content": "Create a presentation"}],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

For best caching performance, keep your Skills list consistent across requests.
### 
Error handling
Handle Skill-related errors gracefully:
CLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

try:
    response = client.beta.messages.create(
        model="claude-opus-4-8",
        max_tokens=4096,
        betas=["code-execution-2025-08-25", "skills-2025-10-02"],
        container={
            "skills": [
                    "type": "custom",
                    "skill_id": "skill_01AbCdEfGhIjKlMnOpQrStUv",
                    "version": "latest",
            ]
        messages=[{"role": "user", "content": "Process data"}],
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    )
except anthropic.BadRequestError as e:
    if "skill" in str(e):
        print(f"Skill error: {e}")
        # Handle skill-specific errors
    else:
        raise

* * *
Data retention
Agent Skills are not covered by ZDR arrangements. Skill definitions and execution data are retained according to Anthropic's standard data retention policy.
For ZDR eligibility across all features, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention).
Next steps
[  API Reference Complete API reference with all endpoints ](https://platform.claude.com/docs/en/api/skills/create-skill)[  Authoring Guide Best practices for writing effective Skills ](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)[ Code Execution Tool Learn about the code execution environment ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)
