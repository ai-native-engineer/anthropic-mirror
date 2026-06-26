<!-- source: https://platform.claude.com/docs/en/api/admin/mcp_tunnels/rotate_token -->

# Rotate Tunnel Token
POST/v1/organizations/tunnels/{tunnel_id}/rotate_token
Invalidate the tunnel's current token for new connections and return a fresh value.
Established connections are not severed by rotation; a connector restarted after rotation must use the new value. An optional `reason` is captured for operational context.
##### Path ParametersExpand Collapse 
tunnel_id: string
ID of the Tunnel.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/rotate_token#rotate_token.tunnel_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": array of "mcp-tunnels-2026-05-19"
Required for all Tunnel endpoints.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/rotate_token#rotate_token.anthropic-beta)
#####  Body ParametersJSONExpand Collapse 
reason: optional string
Optional free-text reason for the rotation, recorded for audit.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/rotate_token#rotate_token.reason)
Stable identifier for the current token value. Changes when the token is rotated.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/rotate_token#mcp_tunnel_rotate_token_response.id)
tunnel_token: string
The tunnel's connection token.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/rotate_token#mcp_tunnel_rotate_token_response.tunnel_token)
type: "tunnel_token"
Object type. Always `tunnel_token` for Tunnel Tokens.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/rotate_token#mcp_tunnel_rotate_token_response.type)
Rotate Tunnel Token

curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/rotate_token \
    -X POST \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "id": "ttkn_bb97000eaec162831399ca9b6684a4fdf5be49ace5683057b017aab5c87e19e0",
  "tunnel_token": "eyJhIjoiRVhBTVBMRSIsInQiOiJFWEFNUExFIiwicyI6IkVYQU1QTEUifQ==",
  "type": "tunnel_token"

  "id": "ttkn_bb97000eaec162831399ca9b6684a4fdf5be49ace5683057b017aab5c87e19e0",
  "tunnel_token": "eyJhIjoiRVhBTVBMRSIsInQiOiJFWEFNUExFIiwicyI6IkVYQU1QTEUifQ==",
  "type": "tunnel_token"
