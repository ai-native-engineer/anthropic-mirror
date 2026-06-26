<!-- source: https://platform.claude.com/docs/en/managed-agents/environments -->

# Cloud environment setup
Customize cloud sandboxes for your sessions.
Environments define the sandbox configuration where your agent runs. You create an environment once, then reference its ID each time you start a session. Multiple sessions can share the same environment, but each session gets its own isolated sandbox (a fresh Linux container).
This page covers `type: cloud` environments. To run sandboxes on your own infrastructure, see [Self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes).
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Create an environment
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:environments create \
  --name "python-dev" \
  --config '{type: cloud, networking: {type: unrestricted}}'

The `name` must be unique within your organization and workspace.
Use the environment in a session
Pass the environment ID as a string when [creating a session](https://platform.claude.com/docs/en/managed-agents/sessions).
curlPythonTypeScriptC#GoJavaPHPRuby

session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
)

Configuration options
### 
Packages
The `packages` field pre-installs packages into the sandbox before the agent starts. Packages are installed by their respective package managers and cached across sessions that share the same environment. When multiple package managers are specified, they run in alphabetical order (apt, cargo, gem, go, npm, pip). You can optionally pin specific versions; the default is latest.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:environments create <<'YAML'
name: data-analysis
config:
  type: cloud
  packages:
    pip:
      - pandas
      - numpy
      - scikit-learn
    npm:
      - express
  networking:
    type: unrestricted
YAML

Supported package managers:  
| Field  | Package manager  | Example  |  
| --- | --- | --- |  
| `apt`  | System packages (apt-get)  | `"ffmpeg"`  |  
| `cargo`  | Rust (cargo)  | `"ripgrep@14.0.0"`  |  
| `gem`  | Ruby (gem)  | `"rails:7.1.0"`  |  
| `go`  | Go modules  | `"golang.org/x/tools/cmd/goimports@latest"`  |  
| `npm`  | Node.js (npm)  | `"express@4.18.0"`  |  
| `pip`  | Python (pip)  | `"pandas==2.2.0"`  |  
### 
Networking
The `networking` field controls the sandbox's outbound network access. It does not impact the `web_search` or `web_fetch` tools' allowed domains.  
| Mode  | Description  |  
| --- | --- |  
| `unrestricted`  | Full outbound network access, except for a general safety blocklist. This is the default.  |  
| `limited`  | Restricts sandbox network access to the `allowed_hosts` list. Further access is enabled through the `allow_package_managers` and `allow_mcp_servers` bool.  |  
curlPythonTypeScriptC#GoJavaPHPRuby

config = {
    "type": "cloud",
    "networking": {
        "type": "limited",
        "allowed_hosts": ["api.example.com"],
        "allow_mcp_servers": True,
        "allow_package_managers": True,

For production deployments, use `limited` networking with an explicit `allowed_hosts` list. Follow the principle of least privilege by granting only the minimum network access your agent requires, and regularly audit your allowed domains.
When using `limited` networking:
  * `allowed_hosts` specifies domains the sandbox can reach. Specify bare hostnames or wildcard patterns (such as `*.example.com`); do not include a URL scheme.
  * `allow_mcp_servers` permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.
  * `allow_package_managers` permits outbound access to public package registries (such as PyPI and npm) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Environment lifecycle
  * Environments persist until explicitly archived or deleted.
  * Multiple sessions can reference the same environment.
  * Each session gets its own sandbox instance. Sessions do not share file system state.
  * Environments are not versioned. If you frequently update your environments, you may want to log these updates on your side, to map environment state with sessions.

Manage environments
curlCLIPythonTypeScriptC#GoJavaPHPRuby

# List environments
ant beta:environments list

# Retrieve a specific environment
ant beta:environments retrieve --environment-id "$ENVIRONMENT_ID"

# Archive an environment (read-only, existing sessions continue)
ant beta:environments archive --environment-id "$ENVIRONMENT_ID"

# Delete an environment (only if no sessions reference it)
ant beta:environments delete --environment-id "$ENVIRONMENT_ID"

Pre-installed runtimes
Cloud sandboxes include common runtimes out of the box. See [Sandbox reference](https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference) for the full list of pre-installed languages, databases, and utilities.
  * [Create an environment](https://platform.claude.com/docs/en/managed-agents/environments#create-an-environment)
  * [Use the environment in a session](https://platform.claude.com/docs/en/managed-agents/environments#use-the-environment-in-a-session)
  * [Configuration options](https://platform.claude.com/docs/en/managed-agents/environments#configuration-options)
  * [Packages](https://platform.claude.com/docs/en/managed-agents/environments#packages)
  * [Networking](https://platform.claude.com/docs/en/managed-agents/environments#networking)
  * [Environment lifecycle](https://platform.claude.com/docs/en/managed-agents/environments#environment-lifecycle)
  * [Manage environments](https://platform.claude.com/docs/en/managed-agents/environments#manage-environments)
  * [Pre-installed runtimes](https://platform.claude.com/docs/en/managed-agents/environments#pre-installed-runtimes)

Managed Agents/Configure agent environment
# Cloud environment setup
Customize cloud sandboxes for your sessions.
Environments define the sandbox configuration where your agent runs. You create an environment once, then reference its ID each time you start a session. Multiple sessions can share the same environment, but each session gets its own isolated sandbox (a fresh Linux container).
This page covers `type: cloud` environments. To run sandboxes on your own infrastructure, see [Self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes).
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.
Create an environment
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:environments create \
  --name "python-dev" \
  --config '{type: cloud, networking: {type: unrestricted}}'

The `name` must be unique within your organization and workspace.
Use the environment in a session
Pass the environment ID as a string when [creating a session](https://platform.claude.com/docs/en/managed-agents/sessions).
curlPythonTypeScriptC#GoJavaPHPRuby

session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
)

Configuration options
### 
Packages
The `packages` field pre-installs packages into the sandbox before the agent starts. Packages are installed by their respective package managers and cached across sessions that share the same environment. When multiple package managers are specified, they run in alphabetical order (apt, cargo, gem, go, npm, pip). You can optionally pin specific versions; the default is latest.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

ant beta:environments create <<'YAML'
name: data-analysis
config:
  type: cloud
  packages:
    pip:
      - pandas
      - numpy
      - scikit-learn
    npm:
      - express
  networking:
    type: unrestricted
YAML

Supported package managers:  
| Field  | Package manager  | Example  |  
| --- | --- | --- |  
| `apt`  | System packages (apt-get)  | `"ffmpeg"`  |  
| `cargo`  | Rust (cargo)  | `"ripgrep@14.0.0"`  |  
| `gem`  | Ruby (gem)  | `"rails:7.1.0"`  |  
| `go`  | Go modules  | `"golang.org/x/tools/cmd/goimports@latest"`  |  
| `npm`  | Node.js (npm)  | `"express@4.18.0"`  |  
| `pip`  | Python (pip)  | `"pandas==2.2.0"`  |  
### 
Networking
The `networking` field controls the sandbox's outbound network access. It does not impact the `web_search` or `web_fetch` tools' allowed domains.  
| Mode  | Description  |  
| --- | --- |  
| `unrestricted`  | Full outbound network access, except for a general safety blocklist. This is the default.  |  
| `limited`  | Restricts sandbox network access to the `allowed_hosts` list. Further access is enabled through the `allow_package_managers` and `allow_mcp_servers` bool.  |  
curlPythonTypeScriptC#GoJavaPHPRuby

config = {
    "type": "cloud",
    "networking": {
        "type": "limited",
        "allowed_hosts": ["api.example.com"],
        "allow_mcp_servers": True,
        "allow_package_managers": True,

For production deployments, use `limited` networking with an explicit `allowed_hosts` list. Follow the principle of least privilege by granting only the minimum network access your agent requires, and regularly audit your allowed domains.
When using `limited` networking:
  * `allowed_hosts` specifies domains the sandbox can reach. Specify bare hostnames or wildcard patterns (such as `*.example.com`); do not include a URL scheme.
  * `allow_mcp_servers` permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.
  * `allow_package_managers` permits outbound access to public package registries (such as PyPI and npm) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

Environment lifecycle
  * Environments persist until explicitly archived or deleted.
  * Multiple sessions can reference the same environment.
  * Each session gets its own sandbox instance. Sessions do not share file system state.
  * Environments are not versioned. If you frequently update your environments, you may want to log these updates on your side, to map environment state with sessions.

Manage environments
curlCLIPythonTypeScriptC#GoJavaPHPRuby

# List environments
ant beta:environments list

# Retrieve a specific environment
ant beta:environments retrieve --environment-id "$ENVIRONMENT_ID"

# Archive an environment (read-only, existing sessions continue)
ant beta:environments archive --environment-id "$ENVIRONMENT_ID"

# Delete an environment (only if no sessions reference it)
ant beta:environments delete --environment-id "$ENVIRONMENT_ID"

Pre-installed runtimes
Cloud sandboxes include common runtimes out of the box. See [Sandbox reference](https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference) for the full list of pre-installed languages, databases, and utilities.
