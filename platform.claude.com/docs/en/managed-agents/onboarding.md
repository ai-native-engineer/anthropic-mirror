<!-- source: https://platform.claude.com/docs/en/managed-agents/onboarding -->

# Prototype in Console
Create and test agents visually in Console without writing API calls.
[Console](https://platform.claude.com/workspaces/default/agent-quickstart/) provides a visual interface for creating and configuring agents. It lets you iterate on configuration interactively before writing code.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
How to build an agent
The [visual interface](https://platform.claude.com/workspaces/default/agent-quickstart/) walks you through each field of an agent definition:
  * **Model and system prompt:** Pick a model and write the system prompt in a full-width editor.
  * **MCP servers:** Add remote MCP servers by URL and authenticate your agent to take action on your behalf.
  * **Tools:** Extend your agent's capabilities using a pre-built agent toolset and MCP tools.
  * **Skills:** Attach Anthropic or custom skills from your organization's library.

As you configure, Console shows the equivalent API request so you can copy it into your code once you're satisfied.
Testing an agent
Console includes an inline session runner. After configuring your agent, you can start a test session directly, send messages, and watch the event stream without leaving the page. This is the fastest way to check that your system prompt and tool selection produce the behavior you expect.
From prototype to code
Once your agent works as expected:
  1. Copy the agent ID and [environment ID](https://platform.claude.com/docs/en/managed-agents/environments) from Console.
  2. Reference them in your code when [creating sessions](https://platform.claude.com/docs/en/managed-agents/sessions):

curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions create \
  --agent agent_01J8XkN5uT3vHpLqRfWdY2 \
  --environment-id env_01K2mPsT7hNwR4jXuLvCqD8 \
  --title "My first session"

  * [How to build an agent](https://platform.claude.com/docs/en/managed-agents/onboarding#how-to-build-an-agent)
  * [Testing an agent](https://platform.claude.com/docs/en/managed-agents/onboarding#testing-an-agent)
  * [From prototype to code](https://platform.claude.com/docs/en/managed-agents/onboarding#from-prototype-to-code)

Managed Agents/First steps
# Prototype in Console
Create and test agents visually in Console without writing API calls.
[Console](https://platform.claude.com/workspaces/default/agent-quickstart/) provides a visual interface for creating and configuring agents. It lets you iterate on configuration interactively before writing code.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
How to build an agent
The [visual interface](https://platform.claude.com/workspaces/default/agent-quickstart/) walks you through each field of an agent definition:
  * **Model and system prompt:** Pick a model and write the system prompt in a full-width editor.
  * **MCP servers:** Add remote MCP servers by URL and authenticate your agent to take action on your behalf.
  * **Tools:** Extend your agent's capabilities using a pre-built agent toolset and MCP tools.
  * **Skills:** Attach Anthropic or custom skills from your organization's library.

As you configure, Console shows the equivalent API request so you can copy it into your code once you're satisfied.
Testing an agent
Console includes an inline session runner. After configuring your agent, you can start a test session directly, send messages, and watch the event stream without leaving the page. This is the fastest way to check that your system prompt and tool selection produce the behavior you expect.
From prototype to code
Once your agent works as expected:
  1. Copy the agent ID and [environment ID](https://platform.claude.com/docs/en/managed-agents/environments) from Console.
  2. Reference them in your code when [creating sessions](https://platform.claude.com/docs/en/managed-agents/sessions):

curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions create \
  --agent agent_01J8XkN5uT3vHpLqRfWdY2 \
  --environment-id env_01K2mPsT7hNwR4jXuLvCqD8 \
  --title "My first session"
