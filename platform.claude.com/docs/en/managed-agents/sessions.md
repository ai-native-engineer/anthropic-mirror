<!-- source: https://platform.claude.com/docs/en/managed-agents/sessions -->

# Start a session
Create a session to run your agent and begin executing tasks.
A session is an agent instance within an environment. Each session references an [agent](https://platform.claude.com/docs/en/managed-agents/agent-setup) and an [environment](https://platform.claude.com/docs/en/managed-agents/environments) (both created separately), and maintains conversation history across multiple interactions. Sessions follow a two-step lifecycle: first [create the session](https://platform.claude.com/docs/en/managed-agents/sessions#creating-a-session) to provision its sandbox, then [send a user event](https://platform.claude.com/docs/en/managed-agents/sessions#starting-the-session) to start work.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Creating a session
A session requires an `agent` ID and an `environment` ID. Agents are versioned resources; passing in the `agent` ID as a string starts the session with the latest agent version.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID"

To pin a session to a specific agent version, pass an object. This lets you control exactly which version runs and stage rollouts of new versions independently.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions create <<YAML
agent:
  type: agent
  id: $AGENT_ID
  version: 1
environment_id: $ENVIRONMENT_ID
YAML


The agent defines how Claude behaves within the session, including the model, system prompt, tools, and MCP servers. See [Define your agent](https://platform.claude.com/docs/en/managed-agents/agent-setup) for details.
MCP authentication through vaults
If your agent uses MCP tools that require authentication, pass `vault_ids` at session creation to reference a vault containing stored OAuth credentials. Anthropic manages token refresh on your behalf. See [Authenticate with vaults](https://platform.claude.com/docs/en/managed-agents/vaults) for how to create vaults and register credentials.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions create <<YAML
agent: $AGENT_ID
environment_id: $ENVIRONMENT_ID
vault_ids:
  - $VAULT_ID
YAML

Starting the session
Creating a session provisions the environment's sandbox but does not start any work. To delegate a task, send events to the session using a [user event](https://platform.claude.com/docs/en/managed-agents/reference#event-types). The session acts as a state machine that tracks progress while events drive the actual execution.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions:events send \
  --session-id "$SESSION_ID" <<'YAML'
events:
  - type: user.message
    content:
      - type: text
        text: List the files in the working directory.
YAML

See [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) for how to stream the agent's responses and handle tool confirmations.
See [Session statuses](https://platform.claude.com/docs/en/managed-agents/session-operations#session-statuses) for the statuses a session moves through, and [Session operations](https://platform.claude.com/docs/en/managed-agents/session-operations) for retrieving, listing, updating, archiving, and deleting sessions.
  * [Creating a session](https://platform.claude.com/docs/en/managed-agents/sessions#creating-a-session)
  * [MCP authentication through vaults](https://platform.claude.com/docs/en/managed-agents/sessions#mcp-authentication-through-vaults)
  * [Starting the session](https://platform.claude.com/docs/en/managed-agents/sessions#starting-the-session)

Managed Agents/Delegate work to your agent
# Start a session
Create a session to run your agent and begin executing tasks.
A session is an agent instance within an environment. Each session references an [agent](https://platform.claude.com/docs/en/managed-agents/agent-setup) and an [environment](https://platform.claude.com/docs/en/managed-agents/environments) (both created separately), and maintains conversation history across multiple interactions. Sessions follow a two-step lifecycle: first [create the session](https://platform.claude.com/docs/en/managed-agents/sessions#creating-a-session) to provision its sandbox, then [send a user event](https://platform.claude.com/docs/en/managed-agents/sessions#starting-the-session) to start work.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Creating a session
A session requires an `agent` ID and an `environment` ID. Agents are versioned resources; passing in the `agent` ID as a string starts the session with the latest agent version.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions create \
  --agent "$AGENT_ID" \
  --environment-id "$ENVIRONMENT_ID"

To pin a session to a specific agent version, pass an object. This lets you control exactly which version runs and stage rollouts of new versions independently.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions create <<YAML
agent:
  type: agent
  id: $AGENT_ID
  version: 1
environment_id: $ENVIRONMENT_ID
YAML


The agent defines how Claude behaves within the session, including the model, system prompt, tools, and MCP servers. See [Define your agent](https://platform.claude.com/docs/en/managed-agents/agent-setup) for details.
MCP authentication through vaults
If your agent uses MCP tools that require authentication, pass `vault_ids` at session creation to reference a vault containing stored OAuth credentials. Anthropic manages token refresh on your behalf. See [Authenticate with vaults](https://platform.claude.com/docs/en/managed-agents/vaults) for how to create vaults and register credentials.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions create <<YAML
agent: $AGENT_ID
environment_id: $ENVIRONMENT_ID
vault_ids:
  - $VAULT_ID
YAML

Starting the session
Creating a session provisions the environment's sandbox but does not start any work. To delegate a task, send events to the session using a [user event](https://platform.claude.com/docs/en/managed-agents/reference#event-types). The session acts as a state machine that tracks progress while events drive the actual execution.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions:events send \
  --session-id "$SESSION_ID" <<'YAML'
events:
  - type: user.message
    content:
      - type: text
        text: List the files in the working directory.
YAML

See [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) for how to stream the agent's responses and handle tool confirmations.
See [Session statuses](https://platform.claude.com/docs/en/managed-agents/session-operations#session-statuses) for the statuses a session moves through, and [Session operations](https://platform.claude.com/docs/en/managed-agents/session-operations) for retrieving, listing, updating, archiving, and deleting sessions.
