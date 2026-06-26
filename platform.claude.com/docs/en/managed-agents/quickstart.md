<!-- source: https://platform.claude.com/docs/en/managed-agents/quickstart -->

# Get started with Claude Managed Agents
Create your first autonomous agent.
This guide walks you through creating an agent, setting up an environment, starting a session, and streaming agent responses.

**Prefer an interactive walkthrough?** Run `/claude-api managed-agents-onboard` in the latest version of [Claude Code](https://claude.com/product/claude-code) for a guided setup and interactive question-answering.
Core concepts  
| Concept  | Description  |  
| --- | --- |  
| **Agent**  | The model, system prompt, tools, MCP servers, and skills  |  
| **Environment**  | Configuration for where sessions run: an Anthropic-managed cloud sandbox, or a self-hosted sandbox on your own infrastructure  |  
| **Session**  | A running agent instance within an environment, performing a specific task and generating outputs  |  
| **Events**  | Messages exchanged between your application and the agent (user turns, tool results, status updates)  |  
Prerequisites
  * An Anthropic [Console account](https://platform.claude.com)
  * An [API key](https://platform.claude.com/settings/keys)

Install the CLI
Homebrew (macOS)
Homebrew (macOS)
curl (Linux/WSL)
curl (Linux/WSL)
Go
Go

brew install anthropics/tap/ant

Check the installation:

ant --version

Install the SDK
Python
Python
TypeScript
TypeScript
Java
Java
Go
Go
C#
C#
Ruby
Ruby
PHP
PHP

pip install anthropic

Set your API key as an environment variable:

export ANTHROPIC_API_KEY="your-api-key-here"

Create your first session
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
  1. 1
Create an agent
Create an agent that defines the model, system prompt, and available tools.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create \
  --name "Coding Assistant" \
  --model '{id: claude-opus-4-8}' \
  --system "You are a helpful coding assistant. Write clean, well-documented code." \
  --tool '{type: agent_toolset_20260401}'

The `agent_toolset_20260401` tool type enables the full set of pre-built agent tools (bash, file operations, web search, and more). See [Tools](https://platform.claude.com/docs/en/managed-agents/tools) for the complete list and per-tool configuration options.
Save the returned `agent.id`. You'll reference it in every session you create.
  2. 2
Create an environment
An environment defines the sandbox where your agent runs.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:environments create \
  --name "quickstart-env" \
  --config '{type: cloud, networking: {type: unrestricted}}'

Save the returned `environment.id`. You'll reference it in every session you create.

To run the sandbox on your own infrastructure instead of a cloud sandbox, see [Self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes).
  3. 3
Start a session
Create a session that references your agent and environment.
curlPythonTypeScriptC#GoJavaPHPRuby

session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="Quickstart session",
)

print(f"Session ID: {session.id}")

  4. 4
Send a message and stream the response
Open a stream, send a user event, then process events as they arrive:
curlPythonTypeScriptC#GoJavaPHPRuby

with client.beta.sessions.events.stream(session.id) as stream:
    # Send the user message after the stream opens
    client.beta.sessions.events.send(
        session.id,
        events=[
                "type": "user.message",
                "content": [
                        "type": "text",
                        "text": "Create a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt",
                ],
        ],
    )

    # Process streaming events
    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    print(block.text, end="")
            case "agent.tool_use":
                print(f"\n[Using tool: {event.name}]")
            case "session.status_idle":
                print("\n\nAgent finished.")
                break

The agent writes a Python script, executes it in the sandbox, and verifies the output file was created. Your output looks similar to this:

I'll create a Python script that generates the first 20 Fibonacci numbers and saves them to a file.
[Using tool: write]
[Using tool: bash]
The script ran successfully. Let me verify the output file.
[Using tool: bash]
fibonacci.txt contains the first 20 Fibonacci numbers (0 through 4181).

Agent finished.

What's happening
When you send a user event, Claude Managed Agents:
  1. **Provisions a sandbox:** Your environment configuration determines how it's built.
  2. **Runs the agent loop:** Claude determines which tools to use based on your message.
  3. **Executes tools:** File writes, bash commands, and other tool calls run inside the sandbox.
  4. **Streams events:** You receive real-time updates as the agent works.
  5. **Goes idle:** The agent emits a `session.status_idle` event when it has nothing more to do.

Next steps
[ Define your agent Create reusable, versioned agent configurations ](https://platform.claude.com/docs/en/managed-agents/agent-setup)[  Configure environments Customize networking and sandbox settings ](https://platform.claude.com/docs/en/managed-agents/environments)[  Agent tools Enable specific tools for your agent ](https://platform.claude.com/docs/en/managed-agents/tools)[  Session event stream Handle events and steer the agent mid-execution ](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)
  * [Core concepts](https://platform.claude.com/docs/en/managed-agents/quickstart#core-concepts)
  * [Prerequisites](https://platform.claude.com/docs/en/managed-agents/quickstart#prerequisites)
  * [Install the CLI](https://platform.claude.com/docs/en/managed-agents/quickstart#install-the-cli)
  * [Install the SDK](https://platform.claude.com/docs/en/managed-agents/quickstart#install-the-sdk)
  * [Create your first session](https://platform.claude.com/docs/en/managed-agents/quickstart#create-your-first-session)
  * [What's happening](https://platform.claude.com/docs/en/managed-agents/quickstart#whats-happening)
  * [Next steps](https://platform.claude.com/docs/en/managed-agents/quickstart#next-steps)

Managed Agents/First steps
# Get started with Claude Managed Agents
Create your first autonomous agent.
This guide walks you through creating an agent, setting up an environment, starting a session, and streaming agent responses.

**Prefer an interactive walkthrough?** Run `/claude-api managed-agents-onboard` in the latest version of [Claude Code](https://claude.com/product/claude-code) for a guided setup and interactive question-answering.
Core concepts  
| Concept  | Description  |  
| --- | --- |  
| **Agent**  | The model, system prompt, tools, MCP servers, and skills  |  
| **Environment**  | Configuration for where sessions run: an Anthropic-managed cloud sandbox, or a self-hosted sandbox on your own infrastructure  |  
| **Session**  | A running agent instance within an environment, performing a specific task and generating outputs  |  
| **Events**  | Messages exchanged between your application and the agent (user turns, tool results, status updates)  |  
Prerequisites
  * An Anthropic [Console account](https://platform.claude.com)
  * An [API key](https://platform.claude.com/settings/keys)

Install the CLI
Homebrew (macOS)
Homebrew (macOS)
curl (Linux/WSL)
curl (Linux/WSL)
Go
Go

brew install anthropics/tap/ant

Check the installation:

ant --version

Install the SDK
Python
Python
TypeScript
TypeScript
Java
Java
Go
Go
C#
C#
Ruby
Ruby
PHP
PHP

pip install anthropic

Set your API key as an environment variable:

export ANTHROPIC_API_KEY="your-api-key-here"

Create your first session
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
  1. 1
Create an agent
Create an agent that defines the model, system prompt, and available tools.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:agents create \
  --name "Coding Assistant" \
  --model '{id: claude-opus-4-8}' \
  --system "You are a helpful coding assistant. Write clean, well-documented code." \
  --tool '{type: agent_toolset_20260401}'

The `agent_toolset_20260401` tool type enables the full set of pre-built agent tools (bash, file operations, web search, and more). See [Tools](https://platform.claude.com/docs/en/managed-agents/tools) for the complete list and per-tool configuration options.
Save the returned `agent.id`. You'll reference it in every session you create.
  2. 2
Create an environment
An environment defines the sandbox where your agent runs.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:environments create \
  --name "quickstart-env" \
  --config '{type: cloud, networking: {type: unrestricted}}'

Save the returned `environment.id`. You'll reference it in every session you create.

To run the sandbox on your own infrastructure instead of a cloud sandbox, see [Self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes).
  3. 3
Start a session
Create a session that references your agent and environment.
curlPythonTypeScriptC#GoJavaPHPRuby

session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    title="Quickstart session",
)

print(f"Session ID: {session.id}")

  4. 4
Send a message and stream the response
Open a stream, send a user event, then process events as they arrive:
curlPythonTypeScriptC#GoJavaPHPRuby

with client.beta.sessions.events.stream(session.id) as stream:
    # Send the user message after the stream opens
    client.beta.sessions.events.send(
        session.id,
        events=[
                "type": "user.message",
                "content": [
                        "type": "text",
                        "text": "Create a Python script that generates the first 20 Fibonacci numbers and saves them to fibonacci.txt",
                ],
        ],
    )

    # Process streaming events
    for event in stream:
        match event.type:
            case "agent.message":
                for block in event.content:
                    print(block.text, end="")
            case "agent.tool_use":
                print(f"\n[Using tool: {event.name}]")
            case "session.status_idle":
                print("\n\nAgent finished.")
                break

The agent writes a Python script, executes it in the sandbox, and verifies the output file was created. Your output looks similar to this:

I'll create a Python script that generates the first 20 Fibonacci numbers and saves them to a file.
[Using tool: write]
[Using tool: bash]
The script ran successfully. Let me verify the output file.
[Using tool: bash]
fibonacci.txt contains the first 20 Fibonacci numbers (0 through 4181).

Agent finished.

What's happening
When you send a user event, Claude Managed Agents:
  1. **Provisions a sandbox:** Your environment configuration determines how it's built.
  2. **Runs the agent loop:** Claude determines which tools to use based on your message.
  3. **Executes tools:** File writes, bash commands, and other tool calls run inside the sandbox.
  4. **Streams events:** You receive real-time updates as the agent works.
  5. **Goes idle:** The agent emits a `session.status_idle` event when it has nothing more to do.

Next steps
[ Define your agent Create reusable, versioned agent configurations ](https://platform.claude.com/docs/en/managed-agents/agent-setup)[  Configure environments Customize networking and sandbox settings ](https://platform.claude.com/docs/en/managed-agents/environments)[  Agent tools Enable specific tools for your agent ](https://platform.claude.com/docs/en/managed-agents/tools)[  Session event stream Handle events and steer the agent mid-execution ](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)
