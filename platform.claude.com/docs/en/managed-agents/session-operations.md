<!-- source: https://platform.claude.com/docs/en/managed-agents/session-operations -->

# Session operations
Retrieve, list, update, archive, and delete Claude Managed Agents sessions.
Once a session exists, use these operations to read, update, archive, or delete it. See [Start a session](https://platform.claude.com/docs/en/managed-agents/sessions) for creating a session and sending it work.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Session statuses
Sessions progress through these statuses. See [Start a session](https://platform.claude.com/docs/en/managed-agents/sessions) for the session lifecycle.  
| Status  | Description  |  
| --- | --- |  
| `idle`  | Agent is waiting for input, including user messages or tool confirmations. Sessions start in `idle`.  |  
| `running`  | Agent is actively executing.  |  
| `rescheduling`  | Transient error occurred, retrying automatically.  |  
| `terminated`  | Session has ended because of an unrecoverable error.  |  
Updating the agent configuration
You can update a session's `agent.tools` and `agent.mcp_servers`, including permission policies, mid-session without creating a new agent version. Updates are session-local and do not propagate back to the underlying agent.
The semantics of an update are full replacement: the provided array is the new value. To preserve existing entries, `GET` the session, modify the array, and `POST` it back.
The session must be `idle` to update the agent. [Interrupt](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#integrating-events) the session if you need to update the agent while it's running.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions update --session-id "$SESSION_ID" <<'YAML'
agent:
  tools:
    - type: agent_toolset_20260401
    - type: mcp_toolset
      mcp_server_name: linear
  mcp_servers:
    - type: url
      name: linear
      url: https://mcp.linear.app/sse
YAML

Retrieving a session
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions retrieve --session-id "$SESSION_ID"

Listing sessions
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions list --agent-id "$AGENT_ID"

Archiving a session
Archive a session to prevent new events from being sent while preserving its history. A `running` session cannot be archived; send an [interrupt event](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#integrating-events) if you need to archive it immediately.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions archive \
  --session-id "$SESSION_ID"

Deleting a session
Delete a session to permanently remove its record, events, and associated sandbox. A `running` session cannot be deleted; send an [interrupt event](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#integrating-events) if you need to delete it immediately.
Files, memory stores, vaults, skills, environments, and agents are independent resources and are not affected by session deletion.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions delete \
  --session-id "$SESSION_ID"

  * [Session statuses](https://platform.claude.com/docs/en/managed-agents/session-operations#session-statuses)
  * [Updating the agent configuration](https://platform.claude.com/docs/en/managed-agents/session-operations#updating-the-agent-configuration)
  * [Retrieving a session](https://platform.claude.com/docs/en/managed-agents/session-operations#retrieving-a-session)
  * [Listing sessions](https://platform.claude.com/docs/en/managed-agents/session-operations#listing-sessions)
  * [Archiving a session](https://platform.claude.com/docs/en/managed-agents/session-operations#archiving-a-session)
  * [Deleting a session](https://platform.claude.com/docs/en/managed-agents/session-operations#deleting-a-session)

Managed Agents/Delegate work to your agent
# Session operations
Retrieve, list, update, archive, and delete Claude Managed Agents sessions.
Once a session exists, use these operations to read, update, archive, or delete it. See [Start a session](https://platform.claude.com/docs/en/managed-agents/sessions) for creating a session and sending it work.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Session statuses
Sessions progress through these statuses. See [Start a session](https://platform.claude.com/docs/en/managed-agents/sessions) for the session lifecycle.  
| Status  | Description  |  
| --- | --- |  
| `idle`  | Agent is waiting for input, including user messages or tool confirmations. Sessions start in `idle`.  |  
| `running`  | Agent is actively executing.  |  
| `rescheduling`  | Transient error occurred, retrying automatically.  |  
| `terminated`  | Session has ended because of an unrecoverable error.  |  
Updating the agent configuration
You can update a session's `agent.tools` and `agent.mcp_servers`, including permission policies, mid-session without creating a new agent version. Updates are session-local and do not propagate back to the underlying agent.
The semantics of an update are full replacement: the provided array is the new value. To preserve existing entries, `GET` the session, modify the array, and `POST` it back.
The session must be `idle` to update the agent. [Interrupt](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#integrating-events) the session if you need to update the agent while it's running.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions update --session-id "$SESSION_ID" <<'YAML'
agent:
  tools:
    - type: agent_toolset_20260401
    - type: mcp_toolset
      mcp_server_name: linear
  mcp_servers:
    - type: url
      name: linear
      url: https://mcp.linear.app/sse
YAML

Retrieving a session
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions retrieve --session-id "$SESSION_ID"

Listing sessions
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions list --agent-id "$AGENT_ID"

Archiving a session
Archive a session to prevent new events from being sent while preserving its history. A `running` session cannot be archived; send an [interrupt event](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#integrating-events) if you need to archive it immediately.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions archive \
  --session-id "$SESSION_ID"

Deleting a session
Delete a session to permanently remove its record, events, and associated sandbox. A `running` session cannot be deleted; send an [interrupt event](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#integrating-events) if you need to delete it immediately.
Files, memory stores, vaults, skills, environments, and agents are independent resources and are not affected by session deletion.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:sessions delete \
  --session-id "$SESSION_ID"
