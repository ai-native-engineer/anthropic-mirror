<!-- source: https://platform.claude.com/docs/en/api/cli/beta/environments -->

# Environments
##### [Create Environment](https://platform.claude.com/docs/en/api/beta/environments/create)
$ ant beta:environments create
POST/v1/environments
##### [List Environments](https://platform.claude.com/docs/en/api/beta/environments/list)
$ ant beta:environments list
GET/v1/environments
##### [Get Environment](https://platform.claude.com/docs/en/api/beta/environments/retrieve)
$ ant beta:environments retrieve
GET/v1/environments/{environment_id}
##### [Update Environment](https://platform.claude.com/docs/en/api/beta/environments/update)
$ ant beta:environments update
POST/v1/environments/{environment_id}
##### [Delete Environment](https://platform.claude.com/docs/en/api/beta/environments/delete)
$ ant beta:environments delete
DELETE/v1/environments/{environment_id}
##### [Archive Environment](https://platform.claude.com/docs/en/api/beta/environments/archive)
$ ant beta:environments archive
POST/v1/environments/{environment_id}/archive
##### ModelsExpand Collapse 
beta_cloud_config: object { networking, packages, type } 
`cloud` environment configuration.
networking: [BetaUnrestrictedNetwork](https://platform.claude.com/docs/en/api/beta#beta_unrestricted_network) { type }  or [BetaLimitedNetwork](https://platform.claude.com/docs/en/api/beta#beta_limited_network) { allow_mcp_servers, allow_package_managers, allowed_hosts, type } 
Network configuration policy.
beta_unrestricted_network: object { type } 
Unrestricted network access.
type: "unrestricted"
Network policy type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_unrestricted_network.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_unrestricted_network)
beta_limited_network: object { allow_mcp_servers, allow_package_managers, allowed_hosts, type } 
Limited network access.
allow_mcp_servers: boolean
Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network.allow_mcp_servers)
allow_package_managers: boolean
Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network.allow_package_managers)
allowed_hosts: array of string
Specifies domains the container can reach.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network.allowed_hosts)
type: "limited"
Network policy type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_cloud_config.networking)
packages: object { apt, cargo, gem, 4 more } 
Package manager configuration.
apt: array of string
Ubuntu/Debian packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.apt)
cargo: array of string
Rust packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.cargo)
gem: array of string
Ruby packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.gem)
go: array of string
Go packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.go)
npm: array of string
Node.js packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.npm)
pip: array of string
Python packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.pip)
type: optional "packages"
Package configuration type
"packages"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.type%5B0%5D)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_cloud_config.packages)
type: "cloud"
Environment type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_cloud_config.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_cloud_config)
beta_cloud_config_params: object { type, networking, packages } 
Request params for `cloud` environment configuration.
Fields default to null; on update, omitted fields preserve the existing value.
type: "cloud"
Environment type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_cloud_config_params.type)
networking: optional [BetaUnrestrictedNetwork](https://platform.claude.com/docs/en/api/beta#beta_unrestricted_network) { type }  or [BetaLimitedNetworkParams](https://platform.claude.com/docs/en/api/beta#beta_limited_network_params) { type, allow_mcp_servers, allow_package_managers, allowed_hosts } 
Network configuration policy. Omit on update to preserve the existing value.
beta_unrestricted_network: object { type } 
Unrestricted network access.
type: "unrestricted"
Network policy type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_unrestricted_network.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_unrestricted_network)
beta_limited_network_params: object { type, allow_mcp_servers, allow_package_managers, allowed_hosts } 
Limited network request params.
Fields default to null; on update, omitted fields preserve the existing value.
type: "limited"
Network policy type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network_params.type)
allow_mcp_servers: optional boolean
Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network_params.allow_mcp_servers)
allow_package_managers: optional boolean
Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network_params.allow_package_managers)
allowed_hosts: optional array of string
Specifies domains the container can reach.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network_params.allowed_hosts)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network_params)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_cloud_config_params.networking)
packages: optional object { apt, cargo, gem, 4 more } 
Specify packages (and optionally their versions) available in this environment.
When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.
apt: optional array of string
Ubuntu/Debian packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.apt)
cargo: optional array of string
Rust packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.cargo)
gem: optional array of string
Ruby packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.gem)
go: optional array of string
Go packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.go)
npm: optional array of string
Node.js packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.npm)
pip: optional array of string
Python packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.pip)
type: optional "packages"
Package configuration type
"packages"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.type%5B0%5D)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_cloud_config_params.packages)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_cloud_config_params)
beta_environment: object { id, archived_at, config, 7 more } 
Unified Environment resource for both cloud and self-hosted environments.
Environment identifier (e.g., 'env_...')
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment.id)
archived_at: string
RFC 3339 timestamp when environment was archived, or null if not archived
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment.archived_at)
config: [BetaCloudConfig](https://platform.claude.com/docs/en/api/beta#beta_cloud_config) { networking, packages, type }  or [BetaSelfHostedConfig](https://platform.claude.com/docs/en/api/beta#beta_self_hosted_config) { type } 
Environment configuration (either Anthropic Cloud or self-hosted)
beta_cloud_config: object { networking, packages, type } 
`cloud` environment configuration.
networking: [BetaUnrestrictedNetwork](https://platform.claude.com/docs/en/api/beta#beta_unrestricted_network) { type }  or [BetaLimitedNetwork](https://platform.claude.com/docs/en/api/beta#beta_limited_network) { allow_mcp_servers, allow_package_managers, allowed_hosts, type } 
Network configuration policy.
beta_unrestricted_network: object { type } 
Unrestricted network access.
type: "unrestricted"
Network policy type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_unrestricted_network.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_unrestricted_network)
beta_limited_network: object { allow_mcp_servers, allow_package_managers, allowed_hosts, type } 
Limited network access.
allow_mcp_servers: boolean
Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network.allow_mcp_servers)
allow_package_managers: boolean
Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network.allow_package_managers)
allowed_hosts: array of string
Specifies domains the container can reach.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network.allowed_hosts)
type: "limited"
Network policy type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_cloud_config.networking)
packages: object { apt, cargo, gem, 4 more } 
Package manager configuration.
apt: array of string
Ubuntu/Debian packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.apt)
cargo: array of string
Rust packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.cargo)
gem: array of string
Ruby packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.gem)
go: array of string
Go packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.go)
npm: array of string
Node.js packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.npm)
pip: array of string
Python packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.pip)
type: optional "packages"
Package configuration type
"packages"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.type%5B0%5D)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_cloud_config.packages)
type: "cloud"
Environment type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_cloud_config.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_cloud_config)
beta_self_hosted_config: object { type } 
Configuration for self-hosted environments.
type: "self_hosted"
Environment type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_config.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_config)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment.config)
created_at: string
RFC 3339 timestamp when environment was created
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment.created_at)
description: string
User-provided description for the environment
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment.description)
metadata: map[string]
User-provided metadata key-value pairs
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment.metadata)
name: string
Human-readable name for the environment
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment.name)
type: "environment"
The type of object (always 'environment')
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment.type)
updated_at: string
RFC 3339 timestamp when environment was last updated
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment.updated_at)
scope: optional "organization" or "account"
The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.
"organization"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment.scope%5B0%5D)
"account"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment.scope%5B1%5D)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment.scope)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment)
beta_environment_delete_response: object { id, type } 
Response after deleting an environment.
Environment identifier
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment_delete_response.id)
type: "environment_deleted"
The type of response
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment_delete_response.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_environment_delete_response)
beta_limited_network: object { allow_mcp_servers, allow_package_managers, allowed_hosts, type } 
Limited network access.
allow_mcp_servers: boolean
Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network.allow_mcp_servers)
allow_package_managers: boolean
Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network.allow_package_managers)
allowed_hosts: array of string
Specifies domains the container can reach.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network.allowed_hosts)
type: "limited"
Network policy type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network)
beta_limited_network_params: object { type, allow_mcp_servers, allow_package_managers, allowed_hosts } 
Limited network request params.
Fields default to null; on update, omitted fields preserve the existing value.
type: "limited"
Network policy type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network_params.type)
allow_mcp_servers: optional boolean
Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network_params.allow_mcp_servers)
allow_package_managers: optional boolean
Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network_params.allow_package_managers)
allowed_hosts: optional array of string
Specifies domains the container can reach.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network_params.allowed_hosts)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_limited_network_params)
beta_packages: object { apt, cargo, gem, 4 more } 
Packages (and their versions) available in this environment.
apt: array of string
Ubuntu/Debian packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.apt)
cargo: array of string
Rust packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.cargo)
gem: array of string
Ruby packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.gem)
go: array of string
Go packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.go)
npm: array of string
Node.js packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.npm)
pip: array of string
Python packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.pip)
type: optional "packages"
Package configuration type
"packages"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.type%5B0%5D)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages)
beta_packages_params: object { apt, cargo, gem, 4 more } 
Specify packages (and optionally their versions) available in this environment.
When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.
apt: optional array of string
Ubuntu/Debian packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.apt)
cargo: optional array of string
Rust packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.cargo)
gem: optional array of string
Ruby packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.gem)
go: optional array of string
Go packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.go)
npm: optional array of string
Node.js packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.npm)
pip: optional array of string
Python packages to install
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.pip)
type: optional "packages"
Package configuration type
"packages"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.type%5B0%5D)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_packages_params)
beta_self_hosted_config: object { type } 
Configuration for self-hosted environments.
type: "self_hosted"
Environment type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_config.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_config)
beta_self_hosted_config_params: object { type } 
Request params for `self_hosted` environment configuration.
type: "self_hosted"
Environment type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_config_params.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_config_params)
beta_unrestricted_network: object { type } 
Unrestricted network access.
type: "unrestricted"
Network policy type
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_unrestricted_network.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_unrestricted_network)
####  EnvironmentsWork
##### [Get Work Item](https://platform.claude.com/docs/en/api/beta/environments/work/retrieve)
$ ant beta:environments:work retrieve
GET/v1/environments/{environment_id}/work/{work_id}
##### [Poll for Work](https://platform.claude.com/docs/en/api/beta/environments/work/poll)
$ ant beta:environments:work poll
GET/v1/environments/{environment_id}/work/poll
##### [Acknowledge Work](https://platform.claude.com/docs/en/api/beta/environments/work/ack)
$ ant beta:environments:work ack
POST/v1/environments/{environment_id}/work/{work_id}/ack
##### [Record Heartbeat](https://platform.claude.com/docs/en/api/beta/environments/work/heartbeat)
$ ant beta:environments:work heartbeat
POST/v1/environments/{environment_id}/work/{work_id}/heartbeat
##### [Stop Work](https://platform.claude.com/docs/en/api/beta/environments/work/stop)
$ ant beta:environments:work stop
POST/v1/environments/{environment_id}/work/{work_id}/stop
##### [List Work Items](https://platform.claude.com/docs/en/api/beta/environments/work/list)
$ ant beta:environments:work list
GET/v1/environments/{environment_id}/work
##### [Update Work Item](https://platform.claude.com/docs/en/api/beta/environments/work/update)
$ ant beta:environments:work update
POST/v1/environments/{environment_id}/work/{work_id}
##### [Get Queue Statistics](https://platform.claude.com/docs/en/api/beta/environments/work/stats)
$ ant beta:environments:work stats
GET/v1/environments/{environment_id}/work/stats
##### ModelsExpand Collapse 
beta_self_hosted_work: object { id, acknowledged_at, created_at, 9 more } 
Work resource representing a unit of work in a self-hosted environment.
Work items are queued when sessions are created or when long-dormant sessions receive new messages. The environment worker polls for work to execute in a self-hosted sandbox.
Work identifier (e.g., 'work_...')
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.id)
acknowledged_at: string
RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.acknowledged_at)
created_at: string
RFC 3339 timestamp when work was created
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.created_at)
data: object { id, type } 
The actual work to be performed
Session identifier (e.g., 'session_...')
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_session_work_data.id)
type: "session"
Type of work data
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_session_work_data.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.data)
environment_id: string
Environment identifier this work belongs to (e.g., `env_...`)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.environment_id)
latest_heartbeat_at: string
RFC 3339 timestamp of the most recent heartbeat
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.latest_heartbeat_at)
metadata: map[string]
User-provided metadata key-value pairs associated with this work item
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.metadata)
started_at: string
RFC 3339 timestamp when work execution started
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.started_at)
state: "queued" or "starting" or "active" or 2 more
Current state of the work item
"queued"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.state%5B0%5D)
"starting"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.state%5B1%5D)
"active"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.state%5B2%5D)
"stopping"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.state%5B3%5D)
"stopped"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.state%5B4%5D)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.state)
stop_requested_at: string
RFC 3339 timestamp when stop was requested
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.stop_requested_at)
stopped_at: string
RFC 3339 timestamp when work execution stopped
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.stopped_at)
type: "work"
The type of object (always 'work')
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work)
beta_self_hosted_work_heartbeat_response: object { last_heartbeat, lease_extended, state, 2 more } 
Response after recording a heartbeat for a work item.
last_heartbeat: string
RFC 3339 timestamp of the actual heartbeat from DB
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_heartbeat_response.last_heartbeat)
lease_extended: boolean
Whether the heartbeat succeeded in extending the lease
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_heartbeat_response.lease_extended)
state: "queued" or "starting" or "active" or 2 more
Current state of the work item (active/stopping/stopped)
"queued"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_heartbeat_response.state%5B0%5D)
"starting"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_heartbeat_response.state%5B1%5D)
"active"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_heartbeat_response.state%5B2%5D)
"stopping"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_heartbeat_response.state%5B3%5D)
"stopped"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_heartbeat_response.state%5B4%5D)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_heartbeat_response.state)
ttl_seconds: number
Effective TTL applied to the lease
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_heartbeat_response.ttl_seconds)
type: "work_heartbeat"
The type of response
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_heartbeat_response.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_heartbeat_response)
beta_self_hosted_work_list_response: object { data, next_page } 
Response when listing work items with cursor-based pagination.
data: array of [BetaSelfHostedWork](https://platform.claude.com/docs/en/api/beta#beta_self_hosted_work) { id, acknowledged_at, created_at, 9 more } 
List of work items
Work identifier (e.g., 'work_...')
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.id)
acknowledged_at: string
RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.acknowledged_at)
created_at: string
RFC 3339 timestamp when work was created
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.created_at)
data: object { id, type } 
The actual work to be performed
Session identifier (e.g., 'session_...')
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_session_work_data.id)
type: "session"
Type of work data
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_session_work_data.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.data)
environment_id: string
Environment identifier this work belongs to (e.g., `env_...`)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.environment_id)
latest_heartbeat_at: string
RFC 3339 timestamp of the most recent heartbeat
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.latest_heartbeat_at)
metadata: map[string]
User-provided metadata key-value pairs associated with this work item
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.metadata)
started_at: string
RFC 3339 timestamp when work execution started
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.started_at)
state: "queued" or "starting" or "active" or 2 more
Current state of the work item
"queued"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.state%5B0%5D)
"starting"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.state%5B1%5D)
"active"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.state%5B2%5D)
"stopping"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.state%5B3%5D)
"stopped"
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.state%5B4%5D)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.state)
stop_requested_at: string
RFC 3339 timestamp when stop was requested
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.stop_requested_at)
stopped_at: string
RFC 3339 timestamp when work execution stopped
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.stopped_at)
type: "work"
The type of object (always 'work')
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_list_response.data)
next_page: string
Opaque cursor for fetching the next page of results
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_list_response.next_page)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_list_response)
beta_self_hosted_work_queue_stats: object { depth, oldest_queued_at, pending, 2 more } 
Statistics about the work queue for an environment.
Uses Redis Stream consumer group metrics for O(1) queries.
depth: number
Number of work items waiting to be picked up (lag from consumer group)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_queue_stats.depth)
oldest_queued_at: string
RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_queue_stats.oldest_queued_at)
pending: number
Number of work items being processed (polled but not acknowledged)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_queue_stats.pending)
type: "work_queue_stats"
The type of object
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_queue_stats.type)
workers_polling: number
Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_queue_stats.workers_polling)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_queue_stats)
beta_self_hosted_work_stop_request: object { force } 
Request to stop a work item.
force: optional boolean
If true, immediately stop work without graceful shutdown
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_stop_request.force)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_stop_request)
beta_self_hosted_work_update_request: object { metadata } 
Request to update work item metadata.
metadata: map[string]
Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve existing metadata.
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_update_request.metadata)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_self_hosted_work_update_request)
beta_session_work_data: object { id, type } 
Work data for session work items.
This resource type is used when work represents a session that needs to be executed in a self-hosted environment.
Session identifier (e.g., 'session_...')
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_session_work_data.id)
type: "session"
Type of work data
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_session_work_data.type)
[](https://platform.claude.com/docs/en/api/cli/beta/environments#beta_session_work_data)
