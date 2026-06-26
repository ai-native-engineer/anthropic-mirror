<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool -->

# Bash tool
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
The bash tool enables Claude to execute shell commands in a persistent bash session, allowing system operations, script execution, and command-line automation. Shell access is a foundational agent capability. On [Terminal-Bench 2.0](https://github.com/terminal-bench/terminal-bench), a benchmark that evaluates real-world terminal tasks using shell-only validation, Claude shows strong performance gains with access to a persistent bash session.
Overview
The bash tool provides Claude with:
  * Persistent bash session that maintains state
  * Ability to run any shell command
  * Access to environment variables and working directory
  * Command chaining and scripting capabilities

For model support, see the [Tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference).
Use cases
  * **Development workflows:** Run build commands, tests, and development tools
  * **System automation:** Execute scripts, manage files, automate tasks
  * **Data processing:** Process files, run analysis scripts, manage datasets
  * **Environment setup:** Install packages, configure environments

Quick start
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[{"type": "bash_20250124", "name": "bash"}],
    messages=[
        {"role": "user", "content": "List all Python files in the current directory."}
    ],
)

print(response)

How it works
The bash tool maintains a persistent session:
  1. Claude determines what command to run
  2. You execute the command in a bash shell
  3. Return the output (stdout and stderr) to Claude
  4. Session state persists between commands (environment variables, working directory)

Parameters  
| Parameter  | Required  | Description  |  
| --- | --- | --- |  
| `command`  | Yes*  | The bash command to run  |  
| `restart`  | No  | Set to `true` to restart the bash session  |  
*Required unless using `restart`
### Example usage
Example: Multi-step automation
Claude can chain commands to complete complex tasks:

User request:
"Install the requests library and create a simple Python script that
fetches a joke from an API, then run it."

Claude's tool uses:
1. Install package
   {"command": "pip install requests"}

2. Create script
   {"command": "cat > fetch_joke.py << 'EOF'\nimport requests\nresponse = requests.get('https://official-joke-api.appspot.com/random_joke')\njoke = response.json()\nprint(f\"Setup: {joke['setup']}\")\nprint(f\"Punchline: {joke['punchline']}\")\nEOF"}

3. Run script
   {"command": "python fetch_joke.py"}

The session maintains state between commands, so files created in step 2 are available in step 3.
Implement the bash tool
The bash tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.
  1. 1
Set up a bash environment
Create a persistent bash session that Claude can interact with:

import subprocess
import threading
import queue

class BashSession:
    def __init__(self):
        self.process = subprocess.Popen(
            ["/bin/bash"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=0,
        )
        self.output_queue = queue.Queue()
        self.error_queue = queue.Queue()
        self._start_readers()

  2. 2
Handle command execution
Create a function to execute commands and capture output:

def execute_command(self, command):
    # Send command to bash
    self.process.stdin.write(command + "\n")
    self.process.stdin.flush()

    # Capture output with timeout
    output = self._read_output(timeout=10)
    return output

  3. 3
Process Claude's tool calls
Extract and execute commands from Claude's responses:

for content in response.content:
    if content.type == "tool_use" and content.name == "bash":
        if content.input.get("restart"):
            bash_session.restart()
            result = "Bash session restarted"
        else:
            command = content.input.get("command")
            result = bash_session.execute_command(command)

        # Return result to Claude
        tool_result = {
            "type": "tool_result",
            "tool_use_id": content.id,
            "content": result,

  4. 4
Implement safety measures
Add validation and restrictions. Use an allowlist rather than a blocklist, since blocklists are easy to bypass. Reject shell operators so chained commands can't slip past the allowlist:

import shlex

ALLOWED_COMMANDS = {"ls", "cat", "echo", "pwd", "grep", "find", "wc", "head", "tail"}
SHELL_OPERATORS = {"&&", "||", "|", ";", "&", ">", "<", ">>"}

def validate_command(command):
    # Allow only commands from an explicit allowlist
    try:
        tokens = shlex.split(command)
    except ValueError:
        return False, "Could not parse command"

    if not tokens:
        return False, "Empty command"

    executable = tokens[0]
    if executable not in ALLOWED_COMMANDS:
        return False, f"Command '{executable}' is not in the allowlist"

    # Reject shell operators that would chain additional commands
    for token in tokens[1:]:
        if token in SHELL_OPERATORS or token.startswith(("$", "`")):
            return False, f"Shell operator '{token}' is not allowed"

    return True, None

This check is a first line of defense. For stronger isolation, run validated commands with `shell=False` and pass `shlex.split(command)` as the argument list, so the shell never interprets the string.

### 
Handle errors
When implementing the bash tool, handle various error scenarios:
### Command execution timeout
### Command not found
### Permission denied
### 
Follow implementation best practices
### Use command timeouts
### Maintain session state
### Handle large outputs
### Log all commands
### Sanitize outputs
Security

The bash tool provides direct system access. Implement these essential safety measures:
  * Running in isolated environments (Docker/VM)
  * Implementing command filtering and allowlists
  * Setting resource limits (CPU, memory, disk)
  * Logging all executed commands

### 
Key recommendations
  * Use `ulimit` to set resource constraints
  * Filter dangerous commands (`sudo`, `rm -rf`, etc.)
  * Run with minimal user permissions
  * Monitor and log all command execution

Pricing
The bash tool adds **245 input tokens** to your API calls.
Additional tokens are consumed by:
  * Command outputs (stdout/stderr)
  * Error messages
  * Large file contents

See [tool use pricing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview#pricing) for complete pricing details.
Common patterns
### 
Development workflows
  * Running tests: `pytest && coverage report`
  * Building projects: `npm install && npm run build`
  * Git operations: `git status && git add . && git commit -m "message"`

#### 
Git-based checkpointing
Git serves as a structured recovery mechanism in long-running agent workflows, not just a way to save changes:
  * **Capture a baseline:** Before any agent work begins, commit the current state. This is the known-good starting point.
  * **Commit per feature:** Each completed feature gets its own commit. These serve as rollback points if something goes wrong later.
  * **Reconstruct state at session start:** Read `git log` alongside a progress file to understand what has already been done and what comes next.
  * **Revert on failure:** If work goes sideways, `git checkout` reverts to the last good commit instead of trying to debug a broken state.

### 
File operations
  * Processing data: `wc -l *.csv && ls -lh *.csv`
  * Searching files: `find . -name "*.py" | xargs grep "pattern"`
  * Creating backups: `tar -czf backup.tar.gz ./data`

### 
System tasks
  * Checking resources: `df -h && free -m`
  * Process management: `ps aux | grep python`
  * Environment setup: `export PATH=$PATH:/new/path && echo $PATH`

Limitations
  * **No interactive commands:** Cannot handle `vim`, `less`, or password prompts
  * **No GUI applications:** Command-line only
  * **Session scope:** Bash session state is client-side. The API is stateless. Your application is responsible for maintaining the shell session between turns.
  * **Output limits:** Large outputs may be truncated
  * **No streaming:** Results returned after completion

Combining with other tools
The bash tool is most powerful when combined with the [text editor](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool) and other tools.
If you're also using the [code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool), Claude has access to two separate execution environments: your local bash session and Anthropic's sandboxed container. State is not shared between them. See [Using code execution with other execution tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#using-code-execution-with-other-execution-tools) for guidance on prompting Claude to distinguish between environments.
Next steps
[  Tool use overview Learn about tool use with Claude ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)[  Text editor tool View and edit text files with Claude ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)
  * [Overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#overview)
  * [Use cases](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#use-cases)
  * [Quick start](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#quick-start)
  * [How it works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#how-it-works)
  * [Parameters](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#parameters)
  * [Example: Multi-step automation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#example-multi-step-automation)
  * [Implement the bash tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#implement-the-bash-tool)
  * [Handle errors](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#handle-errors)
  * [Follow implementation best practices](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#follow-implementation-best-practices)
  * [Security](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#security)
  * [Key recommendations](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#key-recommendations)
  * [Pricing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#pricing)
  * [Common patterns](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#common-patterns)
  * [Development workflows](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#development-workflows)
  * [File operations](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#file-operations)
  * [System tasks](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#system-tasks)
  * [Limitations](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#limitations)
  * [Combining with other tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#combining-with-other-tools)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#next-steps)

Messages/Tools
# Bash tool
This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.
The bash tool enables Claude to execute shell commands in a persistent bash session, allowing system operations, script execution, and command-line automation. Shell access is a foundational agent capability. On [Terminal-Bench 2.0](https://github.com/terminal-bench/terminal-bench), a benchmark that evaluates real-world terminal tasks using shell-only validation, Claude shows strong performance gains with access to a persistent bash session.
Overview
The bash tool provides Claude with:
  * Persistent bash session that maintains state
  * Ability to run any shell command
  * Access to environment variables and working directory
  * Command chaining and scripting capabilities

For model support, see the [Tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference).
Use cases
  * **Development workflows:** Run build commands, tests, and development tools
  * **System automation:** Execute scripts, manage files, automate tasks
  * **Data processing:** Process files, run analysis scripts, manage datasets
  * **Environment setup:** Install packages, configure environments

Quick start
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[{"type": "bash_20250124", "name": "bash"}],
    messages=[
        {"role": "user", "content": "List all Python files in the current directory."}
    ],
)

print(response)

How it works
The bash tool maintains a persistent session:
  1. Claude determines what command to run
  2. You execute the command in a bash shell
  3. Return the output (stdout and stderr) to Claude
  4. Session state persists between commands (environment variables, working directory)

Parameters  
| Parameter  | Required  | Description  |  
| --- | --- | --- |  
| `command`  | Yes*  | The bash command to run  |  
| `restart`  | No  | Set to `true` to restart the bash session  |  
*Required unless using `restart`
### Example usage
Example: Multi-step automation
Claude can chain commands to complete complex tasks:

User request:
"Install the requests library and create a simple Python script that
fetches a joke from an API, then run it."

Claude's tool uses:
1. Install package
   {"command": "pip install requests"}

2. Create script
   {"command": "cat > fetch_joke.py << 'EOF'\nimport requests\nresponse = requests.get('https://official-joke-api.appspot.com/random_joke')\njoke = response.json()\nprint(f\"Setup: {joke['setup']}\")\nprint(f\"Punchline: {joke['punchline']}\")\nEOF"}

3. Run script
   {"command": "python fetch_joke.py"}

The session maintains state between commands, so files created in step 2 are available in step 3.
Implement the bash tool
The bash tool is implemented as a schema-less tool. When using this tool, you don't need to provide an input schema as with other tools; the schema is built into Claude's model and can't be modified.
  1. 1
Set up a bash environment
Create a persistent bash session that Claude can interact with:

import subprocess
import threading
import queue

class BashSession:
    def __init__(self):
        self.process = subprocess.Popen(
            ["/bin/bash"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=0,
        )
        self.output_queue = queue.Queue()
        self.error_queue = queue.Queue()
        self._start_readers()

  2. 2
Handle command execution
Create a function to execute commands and capture output:

def execute_command(self, command):
    # Send command to bash
    self.process.stdin.write(command + "\n")
    self.process.stdin.flush()

    # Capture output with timeout
    output = self._read_output(timeout=10)
    return output

  3. 3
Process Claude's tool calls
Extract and execute commands from Claude's responses:

for content in response.content:
    if content.type == "tool_use" and content.name == "bash":
        if content.input.get("restart"):
            bash_session.restart()
            result = "Bash session restarted"
        else:
            command = content.input.get("command")
            result = bash_session.execute_command(command)

        # Return result to Claude
        tool_result = {
            "type": "tool_result",
            "tool_use_id": content.id,
            "content": result,

  4. 4
Implement safety measures
Add validation and restrictions. Use an allowlist rather than a blocklist, since blocklists are easy to bypass. Reject shell operators so chained commands can't slip past the allowlist:

import shlex

ALLOWED_COMMANDS = {"ls", "cat", "echo", "pwd", "grep", "find", "wc", "head", "tail"}
SHELL_OPERATORS = {"&&", "||", "|", ";", "&", ">", "<", ">>"}

def validate_command(command):
    # Allow only commands from an explicit allowlist
    try:
        tokens = shlex.split(command)
    except ValueError:
        return False, "Could not parse command"

    if not tokens:
        return False, "Empty command"

    executable = tokens[0]
    if executable not in ALLOWED_COMMANDS:
        return False, f"Command '{executable}' is not in the allowlist"

    # Reject shell operators that would chain additional commands
    for token in tokens[1:]:
        if token in SHELL_OPERATORS or token.startswith(("$", "`")):
            return False, f"Shell operator '{token}' is not allowed"

    return True, None

This check is a first line of defense. For stronger isolation, run validated commands with `shell=False` and pass `shlex.split(command)` as the argument list, so the shell never interprets the string.

### 
Handle errors
When implementing the bash tool, handle various error scenarios:
### Command execution timeout
### Command not found
### Permission denied
### 
Follow implementation best practices
### Use command timeouts
### Maintain session state
### Handle large outputs
### Log all commands
### Sanitize outputs
Security

The bash tool provides direct system access. Implement these essential safety measures:
  * Running in isolated environments (Docker/VM)
  * Implementing command filtering and allowlists
  * Setting resource limits (CPU, memory, disk)
  * Logging all executed commands

### 
Key recommendations
  * Use `ulimit` to set resource constraints
  * Filter dangerous commands (`sudo`, `rm -rf`, etc.)
  * Run with minimal user permissions
  * Monitor and log all command execution

Pricing
The bash tool adds **245 input tokens** to your API calls.
Additional tokens are consumed by:
  * Command outputs (stdout/stderr)
  * Error messages
  * Large file contents

See [tool use pricing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview#pricing) for complete pricing details.
Common patterns
### 
Development workflows
  * Running tests: `pytest && coverage report`
  * Building projects: `npm install && npm run build`
  * Git operations: `git status && git add . && git commit -m "message"`

#### 
Git-based checkpointing
Git serves as a structured recovery mechanism in long-running agent workflows, not just a way to save changes:
  * **Capture a baseline:** Before any agent work begins, commit the current state. This is the known-good starting point.
  * **Commit per feature:** Each completed feature gets its own commit. These serve as rollback points if something goes wrong later.
  * **Reconstruct state at session start:** Read `git log` alongside a progress file to understand what has already been done and what comes next.
  * **Revert on failure:** If work goes sideways, `git checkout` reverts to the last good commit instead of trying to debug a broken state.

### 
File operations
  * Processing data: `wc -l *.csv && ls -lh *.csv`
  * Searching files: `find . -name "*.py" | xargs grep "pattern"`
  * Creating backups: `tar -czf backup.tar.gz ./data`

### 
System tasks
  * Checking resources: `df -h && free -m`
  * Process management: `ps aux | grep python`
  * Environment setup: `export PATH=$PATH:/new/path && echo $PATH`

Limitations
  * **No interactive commands:** Cannot handle `vim`, `less`, or password prompts
  * **No GUI applications:** Command-line only
  * **Session scope:** Bash session state is client-side. The API is stateless. Your application is responsible for maintaining the shell session between turns.
  * **Output limits:** Large outputs may be truncated
  * **No streaming:** Results returned after completion

Combining with other tools
The bash tool is most powerful when combined with the [text editor](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool) and other tools.
If you're also using the [code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool), Claude has access to two separate execution environments: your local bash session and Anthropic's sandboxed container. State is not shared between them. See [Using code execution with other execution tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool#using-code-execution-with-other-execution-tools) for guidance on prompting Claude to distinguish between environments.
Next steps
[  Tool use overview Learn about tool use with Claude ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)[  Text editor tool View and edit text files with Claude ](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)
