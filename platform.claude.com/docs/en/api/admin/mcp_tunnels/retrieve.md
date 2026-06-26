<!-- source: https://platform.claude.com/docs/en/api/admin/mcp_tunnels/retrieve -->

# Get Tunnel
GET/v1/organizations/tunnels/{tunnel_id}
Retrieve a single tunnel in the caller's organization by ID.
##### Path ParametersExpand Collapse 
tunnel_id: string
ID of the Tunnel.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/retrieve#retrieve.tunnel_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": array of "mcp-tunnels-2026-05-19"
Required for all Tunnel endpoints.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/retrieve#retrieve.anthropic-beta)
ID of the Tunnel.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/retrieve#mcp_tunnel_retrieve_response.id)
archived_at: string
RFC 3339 datetime string indicating when the Tunnel was archived, or `null` if it is not archived.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/retrieve#mcp_tunnel_retrieve_response.archived_at)
created_at: string
RFC 3339 datetime string indicating when the Tunnel was created.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/retrieve#mcp_tunnel_retrieve_response.created_at)
display_name: string
Human-readable name for the Tunnel (1–255 characters), or `null` if unset.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/retrieve#mcp_tunnel_retrieve_response.display_name)
domain: string
Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a subdomain of this value are routed through the Tunnel. Globally unique and never reused, even after the Tunnel is archived.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/retrieve#mcp_tunnel_retrieve_response.domain)
type: "tunnel"
Object type. Always `tunnel` for Tunnels.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/retrieve#mcp_tunnel_retrieve_response.type)
workspace_id: string
ID of the Workspace this Tunnel belongs to, or `null` for the default Workspace. Immutable after creation.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/retrieve#mcp_tunnel_retrieve_response.workspace_id)
Get Tunnel

curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "Production",
  "domain": "a1b2c3d4.tunnel.anthropic.com",
  "type": "tunnel",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"

  "id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "Production",
  "domain": "a1b2c3d4.tunnel.anthropic.com",
  "type": "tunnel",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
