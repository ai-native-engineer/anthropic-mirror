<!-- source: https://platform.claude.com/docs/en/api/beta/environments/retrieve -->

# Get Environment
GET/v1/environments/{environment_id}
Retrieve a specific environment by ID.
##### Path ParametersExpand Collapse 
environment_id: string
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#retrieve.environment_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#retrieve.betas)
BetaEnvironment object { id, archived_at, config, 7 more } 
Unified Environment resource for both cloud and self-hosted environments.
Environment identifier (e.g., 'env_...')
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_environment.id)
archived_at: string
RFC 3339 timestamp when environment was archived, or null if not archived
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_environment.archived_at)
config: [BetaCloudConfig](https://platform.claude.com/docs/en/api/beta#beta_cloud_config) { networking, packages, type }  or [BetaSelfHostedConfig](https://platform.claude.com/docs/en/api/beta#beta_self_hosted_config) { type } 
Environment configuration (either Anthropic Cloud or self-hosted)
BetaCloudConfig object { networking, packages, type } 
`cloud` environment configuration.
networking: [BetaUnrestrictedNetwork](https://platform.claude.com/docs/en/api/beta#beta_unrestricted_network) { type }  or [BetaLimitedNetwork](https://platform.claude.com/docs/en/api/beta#beta_limited_network) { allow_mcp_servers, allow_package_managers, allowed_hosts, type } 
Network configuration policy.
BetaUnrestrictedNetwork object { type } 
Unrestricted network access.
type: "unrestricted"
Network policy type
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_unrestricted_network.type)
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_unrestricted_network)
BetaLimitedNetwork object { allow_mcp_servers, allow_package_managers, allowed_hosts, type } 
Limited network access.
allow_mcp_servers: boolean
Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_limited_network.allow_mcp_servers)
allow_package_managers: boolean
Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_limited_network.allow_package_managers)
allowed_hosts: array of string
Specifies domains the container can reach.
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_limited_network.allowed_hosts)
type: "limited"
Network policy type
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_limited_network.type)
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_limited_network)
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_cloud_config.networking)
packages: [BetaPackages](https://platform.claude.com/docs/en/api/beta#beta_packages) { apt, cargo, gem, 4 more } 
Package manager configuration.
apt: array of string
Ubuntu/Debian packages to install
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_cloud_config.packages%20%2B%20\(resource\)%20beta.environments.apt)
cargo: array of string
Rust packages to install
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_cloud_config.packages%20%2B%20\(resource\)%20beta.environments.cargo)
gem: array of string
Ruby packages to install
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_cloud_config.packages%20%2B%20\(resource\)%20beta.environments.gem)
go: array of string
Go packages to install
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_cloud_config.packages%20%2B%20\(resource\)%20beta.environments.go)
npm: array of string
Node.js packages to install
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_cloud_config.packages%20%2B%20\(resource\)%20beta.environments.npm)
pip: array of string
Python packages to install
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_cloud_config.packages%20%2B%20\(resource\)%20beta.environments.pip)
type: optional "packages"
Package configuration type
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_cloud_config.packages%20%2B%20\(resource\)%20beta.environments.type)
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_cloud_config.packages)
type: "cloud"
Environment type
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_cloud_config.type)
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_cloud_config)
BetaSelfHostedConfig object { type } 
Configuration for self-hosted environments.
type: "self_hosted"
Environment type
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_self_hosted_config.type)
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_self_hosted_config)
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_environment.config)
created_at: string
RFC 3339 timestamp when environment was created
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_environment.created_at)
description: string
User-provided description for the environment
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_environment.description)
metadata: map[string]
User-provided metadata key-value pairs
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_environment.metadata)
name: string
Human-readable name for the environment
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_environment.name)
type: "environment"
The type of object (always 'environment')
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_environment.type)
updated_at: string
RFC 3339 timestamp when environment was last updated
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_environment.updated_at)
scope: optional "organization" or "account"
The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.
"organization"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_environment.scope%5B0%5D)
"account"
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_environment.scope%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_environment.scope)
[](https://platform.claude.com/docs/en/api/beta/environments/retrieve#beta_environment)
Get Environment
cURL

curl https://api.anthropic.com/v1/environments/$ENVIRONMENT_ID \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    "type": "cloud"
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"

  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    "type": "cloud"
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
