<!-- source: https://platform.claude.com/cookbook/claude-agent-sdk-02-the-observability-agent -->

python

```
import os
import shutil
import subprocess
from typing import Any

from dotenv import load_dotenv
from IPython.display import Markdown, display
from utils.agent_visualizer import (
    display_agent_response,
    print_activity,
    reset_activity_context,
    visualize_conversation,
)

from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient
```

# 02 - The Observability Agent

In the previous notebooks we have built a basic research agent and a Chief of Staff multi-agent framework. While the agents we have built are already powerful, they were still limited in what they could do: the web search agent is limited to searching the internet and our Chief of Staff agent was limited to interacting with its own filesystem.

This is a serious constraint: real-world agents often need to interact with other systems like databases, APIs, file systems, and other specialized services. [MCP (Model Context Protocol)](https://modelcontextprotocol.io/docs/getting-started/intro) is an open-source standard for AI-tool integrations that allows for an easy connection between our agents and these external systems. In this notebook, we will explore how to connect MCP servers to our agent.

**Need more details on MCP?** For comprehensive setup instructions, configuration best practices, and troubleshooting tips, see the [Claude Code MCP documentation](https://docs.claude.com/en/docs/claude-code/mcp).

## Introduction to the MCP Server

### 1. The Git MCP server

Let's first give our agent the ability to understand and work with Git repositories. By adding the [Git MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/git) to our agent, it gains access to 13 Git-specific tools that let it examine commit history, check file changes, create branches, and even make commits. This transforms our agent from a passive observer into an active participant in your development workflow. In this example, we'll configure the agent to explore a repository's history using only Git tools. This is pretty simple, but knowing this, it is not difficult to imagine agents that can automatically create pull requests, analyze code evolution patterns, or help manage complex Git workflows across multiple repositories.

python

```
# Get the git repository root (mcp_server_git requires a valid git repo path)
# os.getcwd() may return a subdirectory, so we find the actual repo root
git_executable = shutil.which("git")
if git_executable is None:
    raise RuntimeError("Git executable not found in PATH")

git_repo_root = subprocess.run(  # noqa: S603
    [git_executable, "rev-parse", "--show-toplevel"],
    capture_output=True,
    text=True,
    check=True,
).stdout.strip()

# Define our git MCP server (installed via uv sync from pyproject.toml)
git_mcp: dict[str, Any] = {
    "git": {
        "command": "uv",
        "args": ["run", "python", "-m", "mcp_server_git", "--repository", git_repo_root],
    }
}
```

python

```
messages = []
async with ClaudeSDKClient(
    options=ClaudeAgentOptions(
        model="claude-opus-4-6",
        mcp_servers=git_mcp,
        allowed_tools=["mcp__git"],
        # disallowed_tools ensures the agent ONLY uses MCP tools, not Bash with git commands
        disallowed_tools=["Bash", "Task", "WebSearch", "WebFetch"],
        permission_mode="acceptEdits",
    )
) as agent:
    await agent.query(
        "Explore this repo's git history and provide a brief summary of recent activity."
    )
    async for msg in agent.receive_response():
        print_activity(msg)
        messages.append(msg)
```

```
🤖 Using: mcp__git__git_log()
🤖 Using: mcp__git__git_status()
🤖 Using: mcp__git__git_branch()
✓ Tool completed
✓ Tool completed
✓ Tool completed
🤖 Thinking...
🤖 Using: mcp__git__git_log()
🤖 Using: mcp__git__git_status()
🤖 Using: mcp__git__git_branch()
✓ Tool completed
✓ Tool completed
✓ Tool completed
🤖 Thinking...
```

python

```
display(Markdown(f"\nResult:\n{messages[-1].result}"))
```

```
<IPython.core.display.Markdown object>
```

### 2. The GitHub MCP server

Now let's level up from local Git operations to full GitHub platform integration. By switching to the [official GitHub MCP server](https://github.com/github/github-mcp-server/tree/main), our agent gains access to over 100 tools that interact with GitHub's entire ecosystem – from managing issues and pull requests to monitoring CI/CD workflows and analyzing code security alerts. This server can work with both public and private repositories, giving your agent the ability to automate complex GitHub workflows that would typically require multiple manual steps.

#### Step 1: Set up your GitHub Token

You need a GitHub Personal Access Token. Get one [here](https://github.com/settings/personal-access-tokens/new) and put in the .env file as `GITHUB_TOKEN="<token>"`

> Note: When getting your token, select "Fine-grained" token with the default options (i.e., public repos, no account permissions), that'll be the easiest way to get this demo working.

Also, for this example you will have to have [Docker](https://www.docker.com/products/docker-desktop/) running on your machine. Docker is required because the GitHub MCP server runs in a containerized environment for security and isolation.

**Docker Quick Setup:**

* Install Docker Desktop from [docker.com](https://www.docker.com/products/docker-desktop/)
* Ensure Docker is running (you'll see the Docker icon in your system tray)
* Verify with `docker --version` in your terminal
* **Troubleshooting:** If Docker won't start, check that virtualization is enabled in your BIOS. For detailed setup instructions, see the [Docker documentation](https://docs.docker.com/get-docker/)

#### Step 2: Define the mcp server and start the agent loop!

python

```
# define our github mcp server
load_dotenv(override=True)
github_mcp: dict[str, Any] = {
    "github": {
        "command": "docker",
        "args": [
            "run",
            "-i",
            "--rm",
            "-e",
            "GITHUB_PERSONAL_ACCESS_TOKEN",
            "ghcr.io/github/github-mcp-server",
        ],
        "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": os.environ.get("GITHUB_TOKEN")},
    }
}
```

python

```
# run our agent
messages = []
async with ClaudeSDKClient(
    options=ClaudeAgentOptions(
        model="claude-opus-4-6",
        mcp_servers=github_mcp,
        allowed_tools=["mcp__github"],
        # disallowed_tools ensures the agent ONLY uses MCP tools, not Bash with gh CLI
        disallowed_tools=["Bash", "Task", "WebSearch", "WebFetch"],
        permission_mode="acceptEdits",
    )
) as agent:
    await agent.query(
        "Search for the anthropics/claude-agent-sdk-python repository and give me a few key facts about it."
    )
    async for msg in agent.receive_response():
        print_activity(msg)
        messages.append(msg)
```

```
🤖 Using: mcp__github__search_repositories()
✓ Tool completed
🤖 Thinking...
```

python

```
display(Markdown(f"\nResult:\n{messages[-1].result}"))
```

```
<IPython.core.display.Markdown object>
```

## Real use case: An observability agent

Now, with such simple setup we can already have an agent acting as self-healing software system!

python

```
load_dotenv(override=True)

prompt = """Analyze the CI health for facebook/react repository.

Examine the most recent runs of the 'CI' workflow and provide:
1. Current status and what triggered the run (push, PR, schedule, etc.)
2. If failing: identify the specific failing jobs/tests and assess severity
3. If passing: note any concerning patterns (long duration, flaky history)
4. Recommended actions with priority (critical/high/medium/low)

Provide a concise operational summary suitable for an on-call engineer.
Do not create issues or PRs - this is a read-only analysis."""

github_mcp: dict[str, Any] = {
    "github": {
        "command": "docker",
        "args": [
            "run",
            "-i",
            "--rm",
            "-e",
            "GITHUB_PERSONAL_ACCESS_TOKEN",
            "ghcr.io/github/github-mcp-server",
        ],
        "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": os.environ.get("GITHUB_TOKEN")},
    }
}

messages = []
async with ClaudeSDKClient(
    options=ClaudeAgentOptions(
        model="claude-opus-4-6",
        mcp_servers=github_mcp,
        allowed_tools=["mcp__github"],
        # IMPORTANT: disallowed_tools is required to actually RESTRICT tool usage.
        # Without this, allowed_tools only controls permission prompting, not availability.
        # The agent would still have access to Bash (and could use `gh` CLI instead of MCP).
        disallowed_tools=["Bash", "Task", "WebSearch", "WebFetch"],
        permission_mode="acceptEdits",
    )
) as agent:
    await agent.query(prompt)
    async for msg in agent.receive_response():
        print_activity(msg)
        messages.append(msg)
```

```
🤖 Using: mcp__github__get_file_contents()
🤖 Using: mcp__github__list_commits()
✓ Tool completed
✓ Tool completed
🤖 Thinking...
🤖 Using: mcp__github__get_file_contents()
🤖 Using: mcp__github__get_file_contents()
🤖 Using: mcp__github__list_pull_requests()
✓ Tool completed
✓ Tool completed
✓ Tool completed
🤖 Thinking...
🤖 Using: mcp__github__get_commit()
🤖 Using: mcp__github__get_commit()
🤖 Using: mcp__github__get_commit()
🤖 Using: mcp__github__pull_request_read()
🤖 Using: mcp__github__pull_request_read()
🤖 Using: mcp__github__pull_request_read()
✓ Tool completed
✓ Tool completed
✓ Tool completed
✓ Tool completed
✓ Tool completed
✓ Tool completed
🤖 Thinking...
🤖 Using: mcp__github__pull_request_read()
🤖 Using: mcp__github__pull_request_read()
🤖 Using: mcp__github__pull_request_read()
🤖 Using: mcp__github__pull_request_read()
🤖 Using: mcp__github__pull_request_read()
✓ Tool completed
✓ Tool completed
✓ Tool completed
✓ Tool completed
✓ Tool completed
🤖 Thinking...
🤖 Using: mcp__github__search_issues()
🤖 Using: mcp__github__search_issues()
✓ Tool completed
✓ Tool completed
🤖 Thinking...
```

python

```
display(Markdown(f"\nResult:\n{messages[-1].result}"))
```

```
<IPython.core.display.Markdown object>
```

python

```
reset_activity_context()
visualize_conversation(messages)
```

```
<IPython.core.display.HTML object>
```

python

```
reset_activity_context()
display_agent_response(messages)
```

```
<IPython.core.display.HTML object>
```

### Observability Agent as Module

The `observability_agent/agent.py` module wraps the observability pattern into a reusable `send_query` function. It imports and uses the shared visualization utilities from `utils.agent_visualizer` internally:

* **`reset_activity_context()`**: Called automatically at the start of each query
* **`print_activity()`**: Provides real-time feedback during execution
* **`display_agent_response()`**: Renders the final result (controlled by `display_result` parameter)

This means you can use the module with minimal code:

python

```
# Reload the module to pick up any changes (useful during development)
from observability_agent.agent import send_query

# The module handles activity display, context reset, and result visualization internally
result = await send_query(
    "Check the CI status for the last 2 runs in anthropics/claude-agent-sdk-python. Just do 3 tool calls, be efficient."
)
```

```
🤖 Using: mcp__github__list_commits()
✓ Tool completed
🤖 Using: mcp__github__get_commit()
🤖 Using: mcp__github__get_commit()
✓ Tool completed
✓ Tool completed
🤖 Thinking...

<IPython.core.display.HTML object>
```

Multi-turn conversations work seamlessly - just pass `continue_conversation=True`:

python

```
# Example 2: Multi-turn conversation for deeper monitoring
result1 = await send_query("What's the current CI status for facebook/react?")
```

```
🤖 Using: mcp__github__list_pull_requests()
🤖 Using: mcp__github__list_commits()
✓ Tool completed
✓ Tool completed
🤖 Thinking...
🤖 Using: mcp__github__pull_request_read()
🤖 Using: mcp__github__pull_request_read()
🤖 Using: mcp__github__pull_request_read()
🤖 Using: mcp__github__get_commit()
✓ Tool completed
✓ Tool completed
✓ Tool completed
✓ Tool completed
🤖 Thinking...

<IPython.core.display.HTML object>
```

python

```
# Continue the conversation to dig deeper
result2 = await send_query(
    "Are there any flaky tests in the recent failures? You can only make one tool call.",
    continue_conversation=True,
)
```

```
🤖 Using: mcp__github__search_issues()
✓ Tool completed
🤖 Thinking...

<IPython.core.display.HTML object>
```

## Conclusion

We've demonstrated how the Claude Code SDK enables seamless integration with external systems through the Model Context Protocol (MCP). Starting with local Git operations through the Git MCP server, we progressively expanded to full GitHub platform integration with access to over 100 GitHub-specific tools. This transformed our agent from a local assistant into a powerful observability system capable of monitoring workflows, analyzing CI/CD failures, and providing actionable insights for production systems.

By connecting MCP servers to our agent, we created an autonomous observability system that monitors GitHub Actions workflows, distinguishes between real failures and security restrictions, and provides detailed analysis of test failures. The system demonstrates how agents can actively participate in your DevOps workflow, moving from passive monitoring to intelligent incident response.

This concludes, for now, our journey through the Claude Code SDK tutorial series. We've progressed from simple research agents to sophisticated multi-agent orchestration, and finally to external system integration through MCP. Together, these patterns provide the foundation for building production-ready agentic systems that can handle real-world complexity while maintaining governance, compliance, and observability.

### What You've Learned Across All Notebooks

**From Notebook 00 (Research Agent)**

* Core SDK fundamentals with `query()` and `ClaudeSDKClient`
* Basic tool usage with WebSearch and Read
* Simple agent loops and conversation management

**From Notebook 01 (Chief of Staff)**

* Advanced features: memory, output styles, planning mode
* Multi-agent coordination through subagents
* Governance through hooks and custom commands
* Enterprise-ready agent architectures

**From Notebook 02 (Observability Agent)**

* External system integration via MCP servers
* Real-time monitoring and incident response
* Production workflow automation
* Scalable agent deployment patterns

The complete implementations for all three agents are available in their respective directories (`research_agent/`, `chief_of_staff_agent/`, `observability_agent/`), ready to serve as inspiration for integrations into your production systems.
