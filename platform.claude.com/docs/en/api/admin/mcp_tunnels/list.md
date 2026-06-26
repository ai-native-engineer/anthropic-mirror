<!-- source: https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list -->

# List Tunnels
GET/v1/organizations/tunnels
List the organization's tunnels.
Results span the caller's organization, ordered by creation time (newest first). Use `workspace_id` to filter to a single workspace; archived tunnels are excluded unless `include_archived` is set.
##### Query ParametersExpand Collapse 
include_archived: optional boolean
Include archived tunnels in the results. Archived tunnels are excluded by default.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#list.include_archived)
limit: optional number
Maximum number of tunnels to return in a single page.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#list.limit)
page: optional string
Opaque pagination cursor from a previous response's `next_page`. Omit to fetch the first page.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#list.page)
workspace_id: optional string
Return only tunnels in this Workspace. Accepts a `wrkspc_`-prefixed Workspace ID; omit to list tunnels across all Workspaces.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#list.workspace_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": array of "mcp-tunnels-2026-05-19"
Required for all Tunnel endpoints.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#list.anthropic-beta)
data: array of object { id, archived_at, created_at, 4 more } 
ID of the Tunnel.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#mcp_tunnel_list_response.id)
archived_at: string
RFC 3339 datetime string indicating when the Tunnel was archived, or `null` if it is not archived.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#mcp_tunnel_list_response.archived_at)
created_at: string
RFC 3339 datetime string indicating when the Tunnel was created.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#mcp_tunnel_list_response.created_at)
display_name: string
Human-readable name for the Tunnel (1–255 characters), or `null` if unset.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#mcp_tunnel_list_response.display_name)
domain: string
Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a subdomain of this value are routed through the Tunnel. Globally unique and never reused, even after the Tunnel is archived.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#mcp_tunnel_list_response.domain)
type: "tunnel"
Object type. Always `tunnel` for Tunnels.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#mcp_tunnel_list_response.type)
workspace_id: string
ID of the Workspace this Tunnel belongs to, or `null` for the default Workspace. Immutable after creation.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#mcp_tunnel_list_response.workspace_id)
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#list)
next_page: string
Opaque cursor for the next page, or `null` if there are no more results.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/list#list)
List Tunnels

curl https://api.anthropic.com/v1/organizations/tunnels \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "Production",
      "domain": "a1b2c3d4.tunnel.anthropic.com",
      "type": "tunnel",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="

  "data": [
      "id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "Production",
      "domain": "a1b2c3d4.tunnel.anthropic.com",
      "type": "tunnel",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
