<!-- source: https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list -->

# List Tunnel Certificates
GET/v1/organizations/tunnels/{tunnel_id}/certificates
List the certificates registered on a tunnel.
Archived certificates are excluded unless `include_archived` is set.
##### Path ParametersExpand Collapse 
tunnel_id: string
ID of the Tunnel.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#list.tunnel_id)
##### Query ParametersExpand Collapse 
include_archived: optional boolean
Include archived certificates in the results. Archived certificates are excluded by default.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#list.include_archived)
limit: optional number
Maximum number of certificates to return.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#list.limit)
page: optional string
A tunnel has at most two active certificates, so this list is not paginated.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#list.page)
##### Header ParametersExpand Collapse 
"anthropic-beta": array of "mcp-tunnels-2026-05-19"
Required for all Tunnel endpoints.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#list.anthropic-beta)
data: array of object { id, archived_at, created_at, 4 more } 
ID of the Tunnel Certificate.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#tunnel_certificate_list_response.id)
archived_at: string
RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#tunnel_certificate_list_response.archived_at)
created_at: string
RFC 3339 datetime string indicating when the certificate was registered.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#tunnel_certificate_list_response.created_at)
expires_at: string
RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#tunnel_certificate_list_response.expires_at)
fingerprint: string
The certificate's SHA-256 fingerprint, as a lowercase hex string.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#tunnel_certificate_list_response.fingerprint)
tunnel_id: string
ID of the Tunnel this certificate is registered against.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#tunnel_certificate_list_response.tunnel_id)
type: "tunnel_certificate"
Object type. Always `tunnel_certificate` for Tunnel Certificates.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#tunnel_certificate_list_response.type)
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#list)
next_page: string
Opaque cursor for the next page, or `null` if there are no more results.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/list#list)
List Tunnel Certificates

curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "data": [
      "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
      "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
      "type": "tunnel_certificate"
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="

  "data": [
      "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
      "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
      "type": "tunnel_certificate"
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
