<!-- source: https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive -->

# Archive Tunnel Certificate
POST/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive
Archive a certificate, removing it from the set Anthropic trusts for this tunnel.
The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.
##### Path ParametersExpand Collapse 
tunnel_id: string
ID of the Tunnel.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive#archive.tunnel_id)
certificate_id: string
ID of the Tunnel Certificate.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive#archive.certificate_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": array of "mcp-tunnels-2026-05-19"
Required for all Tunnel endpoints.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive#archive.anthropic-beta)
ID of the Tunnel Certificate.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive#tunnel_certificate_archive_response.id)
archived_at: string
RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive#tunnel_certificate_archive_response.archived_at)
created_at: string
RFC 3339 datetime string indicating when the certificate was registered.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive#tunnel_certificate_archive_response.created_at)
expires_at: string
RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive#tunnel_certificate_archive_response.expires_at)
fingerprint: string
The certificate's SHA-256 fingerprint, as a lowercase hex string.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive#tunnel_certificate_archive_response.fingerprint)
tunnel_id: string
ID of the Tunnel this certificate is registered against.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive#tunnel_certificate_archive_response.tunnel_id)
type: "tunnel_certificate"
Object type. Always `tunnel_certificate` for Tunnel Certificates.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/archive#tunnel_certificate_archive_response.type)
Archive Tunnel Certificate

curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates/$CERTIFICATE_ID/archive \
    -X POST \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "type": "tunnel_certificate"

  "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "type": "tunnel_certificate"
