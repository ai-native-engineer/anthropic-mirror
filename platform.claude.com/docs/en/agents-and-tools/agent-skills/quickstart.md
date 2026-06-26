<!-- source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart -->

# Get started with Agent Skills in the API
Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.
This tutorial shows you how to use Agent Skills to create a PowerPoint presentation. You'll learn how to enable Skills, make a simple request, and access the generated file.
Prerequisites
  * [Claude API key](https://platform.claude.com/settings/keys)
  * Python 3.7+ or curl installed
  * Basic familiarity with making API requests

Agent Skills overview
Pre-built Agent Skills extend Claude's capabilities with specialized expertise for tasks like creating documents, analyzing data, and processing files. Anthropic provides the following pre-built Agent Skills in the API:
  * **PowerPoint (pptx):** Create and edit presentations
  * **Excel (xlsx):** Create and analyze spreadsheets
  * **Word (docx):** Create and edit documents
  * **PDF (pdf):** Generate PDF documents

**Want to create custom Skills?** See the [Agent Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction) for examples of building your own Skills with domain-specific expertise.
Step 1: List available Skills
First, check what Skills are available. Use the Skills API to list all Anthropic-managed Skills:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# List Anthropic-managed Skills
ant beta:skills list --source anthropic

You see the following Skills: `pptx`, `xlsx`, `docx`, and `pdf`.
This API returns each Skill's metadata: its name and description. Claude loads this metadata at startup to know what Skills are available. This is the first level of **progressive disclosure** , where Claude discovers Skills without loading their full instructions yet.
Step 2: Create a presentation
Now use the PowerPoint Skill to create a presentation about renewable energy. Specify Skills using the `container` parameter in the Messages API:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Create a message with the PowerPoint Skill
response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]
    messages=[
            "role": "user",
            "content": "Create a presentation about renewable energy with 5 slides",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

print(f"stop_reason={response.stop_reason}, blocks={len(response.content)}")

Let's break down what each part does:
  * **`container.skills`:** Specifies which Skills Claude can use
  * **`type: "anthropic"`:** Indicates this is an Anthropic-managed Skill
  * **`skill_id: "pptx"`:** The PowerPoint Skill identifier
  * **`version: "latest"`:** The Skill version set to the most recently published
  * **`tools`:** Enables code execution (required for Skills)
  * **Beta headers:** `code-execution-2025-08-25` and `skills-2025-10-02`

The examples here use the `code_execution_20250825` tool version with its matching `code-execution-2025-08-25` beta header. Skills also work with the newer [code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) revisions (`code_execution_20260120` and later); any code execution tool version satisfies the Skills requirement. Whichever version you use, keep its tool `type` and beta header consistent with the code execution tool page, and always include `skills-2025-10-02`.
When you make this request, Claude automatically matches your task to the relevant Skill. Since you asked for a presentation, Claude determines the PowerPoint Skill is relevant and loads its full instructions: the second level of progressive disclosure. Then Claude executes the Skill's code to create your presentation.
Step 3: Download the created file
The presentation was created in the code execution container and saved as a file. The response includes a file reference with a file ID. Extract the file ID and download it using the Files API:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Extract file ID from the code-execution tool result. The Skill might run
# its work through either the Python or bash code-execution tool, so check
# both result types.
file_id = None
for block in response.content:
    if block.type == "code_execution_tool_result":
        if block.content.type == "code_execution_result":
            for output in block.content.content:
                file_id = output.file_id
    elif block.type == "bash_code_execution_tool_result":
        if block.content.type == "bash_code_execution_result":
            for output in block.content.content:
                file_id = output.file_id

if file_id:
    # Download the file and save it
    output_path = Path(tempfile.gettempdir()) / "renewable_energy.pptx"
    file_content = client.beta.files.download(file_id=file_id)
    file_content.write_to_file(output_path)
    print(f"Presentation saved to {output_path}")

For complete details on working with generated files, see the [code execution tool documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#retrieve-generated-files).
Try more examples
Now that you've created your first document with Skills, try these variations:
### 
Create a spreadsheet
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    messages=[
            "role": "user",
            "content": "Create a quarterly sales tracking spreadsheet with sample data",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

### 
Create a Word document
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "docx", "version": "latest"}]
    messages=[
            "role": "user",
            "content": "Write a 2-page report on the benefits of renewable energy",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

### 
Generate a PDF
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "pdf", "version": "latest"}]
    messages=[
            "role": "user",
            "content": "Generate a PDF invoice template",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

Next steps
Now that you've used pre-built Agent Skills, you can:
[  API Guide Use Skills with the Claude API ](https://platform.claude.com/docs/en/build-with-claude/skills-guide)[  Create Custom Skills Upload your own Skills for specialized tasks ](https://platform.claude.com/docs/en/api/skills/create-skill)[  Authoring Guide Learn best practices for writing effective Skills ](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)[ Use Skills in Claude Code  Learn about Skills in Claude Code ](https://code.claude.com/docs/en/skills)[  Agent Skills Cookbook  Explore example Skills and implementation patterns ](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)
  * [Prerequisites](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart#prerequisites)
  * [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart#agent-skills-overview)
  * [Step 1: List available Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart#step-1-list-available-skills)
  * [Step 2: Create a presentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart#step-2-create-a-presentation)
  * [Step 3: Download the created file](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart#step-3-download-the-created-file)
  * [Try more examples](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart#try-more-examples)
  * [Create a spreadsheet](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart#create-a-spreadsheet)
  * [Create a Word document](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart#create-a-word-document)
  * [Generate a PDF](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart#generate-a-pdf)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart#next-steps)

Messages/Skills
# Get started with Agent Skills in the API
Learn how to use Agent Skills to create documents with the Claude API in under 10 minutes.
This tutorial shows you how to use Agent Skills to create a PowerPoint presentation. You'll learn how to enable Skills, make a simple request, and access the generated file.
Prerequisites
  * [Claude API key](https://platform.claude.com/settings/keys)
  * Python 3.7+ or curl installed
  * Basic familiarity with making API requests

Agent Skills overview
Pre-built Agent Skills extend Claude's capabilities with specialized expertise for tasks like creating documents, analyzing data, and processing files. Anthropic provides the following pre-built Agent Skills in the API:
  * **PowerPoint (pptx):** Create and edit presentations
  * **Excel (xlsx):** Create and analyze spreadsheets
  * **Word (docx):** Create and edit documents
  * **PDF (pdf):** Generate PDF documents

**Want to create custom Skills?** See the [Agent Skills Cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction) for examples of building your own Skills with domain-specific expertise.
Step 1: List available Skills
First, check what Skills are available. Use the Skills API to list all Anthropic-managed Skills:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# List Anthropic-managed Skills
ant beta:skills list --source anthropic

You see the following Skills: `pptx`, `xlsx`, `docx`, and `pdf`.
This API returns each Skill's metadata: its name and description. Claude loads this metadata at startup to know what Skills are available. This is the first level of **progressive disclosure** , where Claude discovers Skills without loading their full instructions yet.
Step 2: Create a presentation
Now use the PowerPoint Skill to create a presentation about renewable energy. Specify Skills using the `container` parameter in the Messages API:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Create a message with the PowerPoint Skill
response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]
    messages=[
            "role": "user",
            "content": "Create a presentation about renewable energy with 5 slides",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

print(f"stop_reason={response.stop_reason}, blocks={len(response.content)}")

Let's break down what each part does:
  * **`container.skills`:** Specifies which Skills Claude can use
  * **`type: "anthropic"`:** Indicates this is an Anthropic-managed Skill
  * **`skill_id: "pptx"`:** The PowerPoint Skill identifier
  * **`version: "latest"`:** The Skill version set to the most recently published
  * **`tools`:** Enables code execution (required for Skills)
  * **Beta headers:** `code-execution-2025-08-25` and `skills-2025-10-02`

The examples here use the `code_execution_20250825` tool version with its matching `code-execution-2025-08-25` beta header. Skills also work with the newer [code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) revisions (`code_execution_20260120` and later); any code execution tool version satisfies the Skills requirement. Whichever version you use, keep its tool `type` and beta header consistent with the code execution tool page, and always include `skills-2025-10-02`.
When you make this request, Claude automatically matches your task to the relevant Skill. Since you asked for a presentation, Claude determines the PowerPoint Skill is relevant and loads its full instructions: the second level of progressive disclosure. Then Claude executes the Skill's code to create your presentation.
Step 3: Download the created file
The presentation was created in the code execution container and saved as a file. The response includes a file reference with a file ID. Extract the file ID and download it using the Files API:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

# Extract file ID from the code-execution tool result. The Skill might run
# its work through either the Python or bash code-execution tool, so check
# both result types.
file_id = None
for block in response.content:
    if block.type == "code_execution_tool_result":
        if block.content.type == "code_execution_result":
            for output in block.content.content:
                file_id = output.file_id
    elif block.type == "bash_code_execution_tool_result":
        if block.content.type == "bash_code_execution_result":
            for output in block.content.content:
                file_id = output.file_id

if file_id:
    # Download the file and save it
    output_path = Path(tempfile.gettempdir()) / "renewable_energy.pptx"
    file_content = client.beta.files.download(file_id=file_id)
    file_content.write_to_file(output_path)
    print(f"Presentation saved to {output_path}")

For complete details on working with generated files, see the [code execution tool documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#retrieve-generated-files).
Try more examples
Now that you've created your first document with Skills, try these variations:
### 
Create a spreadsheet
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "xlsx", "version": "latest"}]
    messages=[
            "role": "user",
            "content": "Create a quarterly sales tracking spreadsheet with sample data",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

### 
Create a Word document
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "docx", "version": "latest"}]
    messages=[
            "role": "user",
            "content": "Write a 2-page report on the benefits of renewable energy",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

### 
Generate a PDF
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=16000,
    betas=["code-execution-2025-08-25", "skills-2025-10-02"],
    container={
        "skills": [{"type": "anthropic", "skill_id": "pdf", "version": "latest"}]
    messages=[
            "role": "user",
            "content": "Generate a PDF invoice template",
    ],
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
)

Next steps
Now that you've used pre-built Agent Skills, you can:
[  API Guide Use Skills with the Claude API ](https://platform.claude.com/docs/en/build-with-claude/skills-guide)[  Create Custom Skills Upload your own Skills for specialized tasks ](https://platform.claude.com/docs/en/api/skills/create-skill)[  Authoring Guide Learn best practices for writing effective Skills ](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)[ Use Skills in Claude Code  Learn about Skills in Claude Code ](https://code.claude.com/docs/en/skills)[  Agent Skills Cookbook  Explore example Skills and implementation patterns ](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)
