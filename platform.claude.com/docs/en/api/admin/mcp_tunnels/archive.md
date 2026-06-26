<!-- source: https://platform.claude.com/docs/en/api/admin/mcp_tunnels/archive -->

# Archive Tunnel
POST/v1/organizations/tunnels/{tunnel_id}/archive
Archive a tunnel. Archival is irreversible.
Every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.
##### Path ParametersExpand Collapse 
tunnel_id: string
ID of the Tunnel.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/archive#archive.tunnel_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": array of "mcp-tunnels-2026-05-19"
Required for all Tunnel endpoints.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/archive#archive.anthropic-beta)
ID of the Tunnel.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/archive#mcp_tunnel_archive_response.id)
archived_at: string
RFC 3339 datetime string indicating when the Tunnel was archived, or `null` if it is not archived.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/archive#mcp_tunnel_archive_response.archived_at)
created_at: string
RFC 3339 datetime string indicating when the Tunnel was created.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/archive#mcp_tunnel_archive_response.created_at)
display_name: string
Human-readable name for the Tunnel (1–255 characters), or `null` if unset.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/archive#mcp_tunnel_archive_response.display_name)
domain: string
Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a subdomain of this value are routed through the Tunnel. Globally unique and never reused, even after the Tunnel is archived.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/archive#mcp_tunnel_archive_response.domain)
type: "tunnel"
Object type. Always `tunnel` for Tunnels.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/archive#mcp_tunnel_archive_response.type)
workspace_id: string
ID of the Workspace this Tunnel belongs to, or `null` for the default Workspace. Immutable after creation.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/archive#mcp_tunnel_archive_response.workspace_id)
Archive Tunnel

curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/archive \
    -X POST \
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
