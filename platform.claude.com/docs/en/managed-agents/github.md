<!-- source: https://platform.claude.com/docs/en/managed-agents/github -->

# Accessing GitHub
Connect your agent to GitHub repositories for cloning, reading, and creating pull requests.
You can mount a GitHub repository to your session sandbox and connect to the GitHub MCP for making pull requests.
GitHub repositories are cached, so future sessions that use the same repository start faster.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
GitHub MCP and session resources
First, create an agent that declares the GitHub MCP server. The agent definition holds the server URL but no auth token:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

AGENT_ID=$(ant beta:agents create \
  --name "Code Reviewer" \
  --model '{id: claude-opus-4-8}' \
  --system "You are a code review assistant with access to GitHub." \
  --mcp-server '{type: url, name: github, url: https://api.githubcopilot.com/mcp/}' \
  --tool '{type: agent_toolset_20260401}' \
  --tool '{type: mcp_toolset, mcp_server_name: github}' \
  --transform id --raw-output)

Then create a session that mounts the GitHub repository:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    resources=[
            "type": "github_repository",
            "url": "https://github.com/org/repo",
            "mount_path": "/workspace/repo",
            "authorization_token": "ghp_your_github_token",
    ],
)

The `resources[].authorization_token` authenticates the repository clone operation and is not echoed in API responses.
Token permissions
When providing a GitHub token, use the minimum required permissions:  
| Action  | Required scopes  |  
| --- | --- |  
| Clone private repos  | `repo`  |  
| Create PRs  | `repo`  |  
| Read issues  |  `repo` (private) or `public_repo`  |  
| Create issues  |  `repo` (private) or `public_repo`  |  

Use fine-grained personal access tokens with minimum required permissions. Avoid using tokens with broad access to your GitHub account.
Multiple repositories
Mount multiple repositories by adding entries to the `resources` array:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

resources = [
        "type": "github_repository",
        "url": "https://github.com/org/frontend",
        "mount_path": "/workspace/frontend",
        "authorization_token": "ghp_your_github_token",
        "type": "github_repository",
        "url": "https://github.com/org/backend",
        "mount_path": "/workspace/backend",
        "authorization_token": "ghp_your_github_token",
]

Managing repositories on a running session
After a session is created, you can list its repository resources and rotate their authorization tokens. Each resource has an `id` returned at session creation time (or through `resources.list`) that you use for updates. Repositories are attached for the lifetime of the session; to change which repositories are mounted, create a new session.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

# List resources on the session
listed = client.beta.sessions.resources.list(session.id)
repo_resource_id = listed.data[0].id
print(repo_resource_id)  # "sesrsc_01ABC..."

# Rotate the authorization token
client.beta.sessions.resources.update(
    repo_resource_id,
    session_id=session.id,
    authorization_token="ghp_your_new_github_token",
)

Creating pull requests
With the GitHub MCP server, the agent can create branches, commit changes, and push them:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

client.beta.sessions.events.send(
    session.id,
    events=[
            "type": "user.message",
            "content": [
                    "type": "text",
                    "text": "Fix the type error in src/utils.ts, commit it to a new branch, and push it.",
            ],
    ],
)

Next steps
[  Session event stream Stream events and steer the agent while it opens the pull request ](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)[  MCP connector Connect more MCP servers to give the agent additional tools ](https://platform.claude.com/docs/en/managed-agents/mcp-connector)[  Adding files Mount files in the sandbox alongside your repositories ](https://platform.claude.com/docs/en/managed-agents/files)
  * [GitHub MCP and session resources](https://platform.claude.com/docs/en/managed-agents/github#git-hub-mcp-and-session-resources)
  * [Token permissions](https://platform.claude.com/docs/en/managed-agents/github#token-permissions)
  * [Multiple repositories](https://platform.claude.com/docs/en/managed-agents/github#multiple-repositories)
  * [Managing repositories on a running session](https://platform.claude.com/docs/en/managed-agents/github#managing-repositories-on-a-running-session)
  * [Creating pull requests](https://platform.claude.com/docs/en/managed-agents/github#creating-pull-requests)
  * [Next steps](https://platform.claude.com/docs/en/managed-agents/github#next-steps)

Managed Agents/Manage agent context
# Accessing GitHub
Connect your agent to GitHub repositories for cloning, reading, and creating pull requests.
You can mount a GitHub repository to your session sandbox and connect to the GitHub MCP for making pull requests.
GitHub repositories are cached, so future sessions that use the same repository start faster.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
GitHub MCP and session resources
First, create an agent that declares the GitHub MCP server. The agent definition holds the server URL but no auth token:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

AGENT_ID=$(ant beta:agents create \
  --name "Code Reviewer" \
  --model '{id: claude-opus-4-8}' \
  --system "You are a code review assistant with access to GitHub." \
  --mcp-server '{type: url, name: github, url: https://api.githubcopilot.com/mcp/}' \
  --tool '{type: agent_toolset_20260401}' \
  --tool '{type: mcp_toolset, mcp_server_name: github}' \
  --transform id --raw-output)

Then create a session that mounts the GitHub repository:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    resources=[
            "type": "github_repository",
            "url": "https://github.com/org/repo",
            "mount_path": "/workspace/repo",
            "authorization_token": "ghp_your_github_token",
    ],
)

The `resources[].authorization_token` authenticates the repository clone operation and is not echoed in API responses.
Token permissions
When providing a GitHub token, use the minimum required permissions:  
| Action  | Required scopes  |  
| --- | --- |  
| Clone private repos  | `repo`  |  
| Create PRs  | `repo`  |  
| Read issues  |  `repo` (private) or `public_repo`  |  
| Create issues  |  `repo` (private) or `public_repo`  |  

Use fine-grained personal access tokens with minimum required permissions. Avoid using tokens with broad access to your GitHub account.
Multiple repositories
Mount multiple repositories by adding entries to the `resources` array:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

resources = [
        "type": "github_repository",
        "url": "https://github.com/org/frontend",
        "mount_path": "/workspace/frontend",
        "authorization_token": "ghp_your_github_token",
        "type": "github_repository",
        "url": "https://github.com/org/backend",
        "mount_path": "/workspace/backend",
        "authorization_token": "ghp_your_github_token",
]

Managing repositories on a running session
After a session is created, you can list its repository resources and rotate their authorization tokens. Each resource has an `id` returned at session creation time (or through `resources.list`) that you use for updates. Repositories are attached for the lifetime of the session; to change which repositories are mounted, create a new session.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

# List resources on the session
listed = client.beta.sessions.resources.list(session.id)
repo_resource_id = listed.data[0].id
print(repo_resource_id)  # "sesrsc_01ABC..."

# Rotate the authorization token
client.beta.sessions.resources.update(
    repo_resource_id,
    session_id=session.id,
    authorization_token="ghp_your_new_github_token",
)

Creating pull requests
With the GitHub MCP server, the agent can create branches, commit changes, and push them:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

client.beta.sessions.events.send(
    session.id,
    events=[
            "type": "user.message",
            "content": [
                    "type": "text",
                    "text": "Fix the type error in src/utils.ts, commit it to a new branch, and push it.",
            ],
    ],
)

Next steps
[  Session event stream Stream events and steer the agent while it opens the pull request ](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)[  MCP connector Connect more MCP servers to give the agent additional tools ](https://platform.claude.com/docs/en/managed-agents/mcp-connector)[  Adding files Mount files in the sandbox alongside your repositories ](https://platform.claude.com/docs/en/managed-agents/files)
