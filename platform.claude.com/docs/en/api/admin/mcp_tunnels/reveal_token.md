<!-- source: https://platform.claude.com/docs/en/api/admin/mcp_tunnels/reveal_token -->

# Reveal Tunnel Token
POST/v1/organizations/tunnels/{tunnel_id}/reveal_token
Return the tunnel's current connection token.
The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as `POST` so the token does not appear in intermediary access logs.
##### Path ParametersExpand Collapse 
tunnel_id: string
ID of the Tunnel.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/reveal_token#reveal_token.tunnel_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": array of "mcp-tunnels-2026-05-19"
Required for all Tunnel endpoints.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/reveal_token#reveal_token.anthropic-beta)
Stable identifier for the current token value. Changes when the token is rotated.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/reveal_token#mcp_tunnel_reveal_token_response.id)
tunnel_token: string
The tunnel's connection token.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/reveal_token#mcp_tunnel_reveal_token_response.tunnel_token)
type: "tunnel_token"
Object type. Always `tunnel_token` for Tunnel Tokens.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/reveal_token#mcp_tunnel_reveal_token_response.type)
Reveal Tunnel Token

curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/reveal_token \
    -X POST \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "id": "ttkn_bb97000eaec162831399ca9b6684a4fdf5be49ace5683057b017aab5c87e19e0",
  "tunnel_token": "eyJhIjoiRVhBTVBMRSIsInQiOiJFWEFNUExFIiwicyI6IkVYQU1QTEUifQ==",
  "type": "tunnel_token"

  "id": "ttkn_bb97000eaec162831399ca9b6684a4fdf5be49ace5683057b017aab5c87e19e0",
  "tunnel_token": "eyJhIjoiRVhBTVBMRSIsInQiOiJFWEFNUExFIiwicyI6IkVYQU1QTEUifQ==",
  "type": "tunnel_token"
