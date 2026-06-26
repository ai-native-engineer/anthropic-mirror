<!-- source: https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create -->

# Create Tunnel Certificate
POST/v1/organizations/tunnels/{tunnel_id}/certificates
Register a public CA certificate for the tunnel.
Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. The PEM body must contain exactly one X.509 certificate and no private-key material. A tunnel holds at most two non-archived certificates.
##### Path ParametersExpand Collapse 
tunnel_id: string
ID of the Tunnel.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create#create.tunnel_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": array of "mcp-tunnels-2026-05-19"
Required for all Tunnel endpoints.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create#create.anthropic-beta)
#####  Body ParametersJSONExpand Collapse 
ca_certificate_pem: string
PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create#create.ca_certificate_pem)
ID of the Tunnel Certificate.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create#tunnel_certificate_create_response.id)
archived_at: string
RFC 3339 datetime string indicating when the certificate was archived, or `null` if it is not archived.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create#tunnel_certificate_create_response.archived_at)
created_at: string
RFC 3339 datetime string indicating when the certificate was registered.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create#tunnel_certificate_create_response.created_at)
expires_at: string
RFC 3339 datetime string indicating when the certificate expires, or `null` if it does not expire.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create#tunnel_certificate_create_response.expires_at)
fingerprint: string
The certificate's SHA-256 fingerprint, as a lowercase hex string.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create#tunnel_certificate_create_response.fingerprint)
tunnel_id: string
ID of the Tunnel this certificate is registered against.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create#tunnel_certificate_create_response.tunnel_id)
type: "tunnel_certificate"
Object type. Always `tunnel_certificate` for Tunnel Certificates.
[](https://platform.claude.com/docs/en/api/admin/mcp_tunnels/tunnel_certificates/create#tunnel_certificate_create_response.type)
Create Tunnel Certificate

curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "ca_certificate_pem": "-----BEGIN CERTIFICATE-----\\nMIIBexampleEXAMPLEexampleEXAMPLEexampleEXAMPLEexampleEXAMPLEexa\\n...illustrative placeholder, not a real certificate...\\n-----END CERTIFICATE-----\\n"
        }'

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
