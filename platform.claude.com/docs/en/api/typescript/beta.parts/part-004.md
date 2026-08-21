<!-- source: https://platform.claude.com/docs/en/api/typescript/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/typescript/beta -->

<!-- chunk-start -->

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnel`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string | null`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

    - `"tunnel"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnel = await client.beta.tunnels.archive("tunnel_id");

console.log(betaTunnel.id);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

## Reveal Tunnel Token

`client.beta.tunnels.revealToken(stringtunnelID, TunnelRevealTokenParamsparams?, RequestOptionsoptions?): BetaTunnelToken`

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `tunnelID: string`

- `params: TunnelRevealTokenParams`

  - `betas?: Array<AnthropicBeta>`

    Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnelToken`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

    - `"tunnel_token"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelToken = await client.beta.tunnels.revealToken("tunnel_id");

console.log(betaTunnelToken.id);
```

#### Response

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

## Rotate Tunnel Token

`client.beta.tunnels.rotateToken(stringtunnelID, TunnelRotateTokenParamsparams, RequestOptionsoptions?): BetaTunnelToken`

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `tunnelID: string`

- `params: TunnelRotateTokenParams`

  - `reason?: string | null`

    Body param: Optional free-text reason for the rotation, recorded for audit.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnelToken`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

    - `"tunnel_token"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelToken = await client.beta.tunnels.rotateToken("tunnel_id");

console.log(betaTunnelToken.id);
```

#### Response

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

## Domain Types

### Beta Tunnel

- `BetaTunnel`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string | null`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

    - `"tunnel"`

### Beta Tunnel Token

- `BetaTunnelToken`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

    - `"tunnel_token"`

# Certificates

## Create Tunnel Certificate

`client.beta.tunnels.certificates.create(stringtunnelID, CertificateCreateParamsparams, RequestOptionsoptions?): BetaTunnelCertificate`

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `tunnelID: string`

- `params: CertificateCreateParams`

  - `ca_certificate_pem: string`

    Body param: PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string | null`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelCertificate = await client.beta.tunnels.certificates.create("tunnel_id", {
  ca_certificate_pem: "ca_certificate_pem"
});

console.log(betaTunnelCertificate.id);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

## Get Tunnel Certificate

`client.beta.tunnels.certificates.retrieve(stringcertificateID, CertificateRetrieveParamsparams, RequestOptionsoptions?): BetaTunnelCertificate`

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `certificateID: string`

- `params: CertificateRetrieveParams`

  - `tunnel_id: string`

    Path param: Path parameter tunnel_id

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string | null`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelCertificate = await client.beta.tunnels.certificates.retrieve(
  "certificate_id",
  { tunnel_id: "tunnel_id" }
);

console.log(betaTunnelCertificate.id);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

## List Tunnel Certificates

`client.beta.tunnels.certificates.list(stringtunnelID, CertificateListParamsparams?, RequestOptionsoptions?): PageCursor<BetaTunnelCertificate>`

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `tunnelID: string`

- `params: CertificateListParams`

  - `include_archived?: boolean`

    Query param: Whether to include archived certificates in the results. Defaults to false.

  - `limit?: number`

    Query param: Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

  - `page?: string`

    Query param: Opaque pagination cursor from a previous `list_tunnel_certificates` response.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string | null`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaTunnelCertificate of client.beta.tunnels.certificates.list("tunnel_id")) {
  console.log(betaTunnelCertificate.id);
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "expires_at": "2019-12-27T18:11:19.117Z",
      "fingerprint": "fingerprint",
      "tunnel_id": "tunnel_id",
      "type": "tunnel_certificate"
    }
  ],
  "next_page": "next_page"
}
```

## Archive Tunnel Certificate

`client.beta.tunnels.certificates.archive(stringcertificateID, CertificateArchiveParamsparams, RequestOptionsoptions?): BetaTunnelCertificate`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `certificateID: string`

- `params: CertificateArchiveParams`

  - `tunnel_id: string`

    Path param: Path parameter tunnel_id

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

      - `"message-batches-2024-09-24"`

      - `"prompt-caching-2024-07-31"`

      - `"computer-use-2024-10-22"`

      - `"computer-use-2025-01-24"`

      - `"pdfs-2024-09-25"`

      - `"token-counting-2024-11-01"`

      - `"token-efficient-tools-2025-02-19"`

      - `"output-128k-2025-02-19"`

      - `"files-api-2025-04-14"`

      - `"mcp-client-2025-04-04"`

      - `"mcp-client-2025-11-20"`

      - `"dev-full-thinking-2025-05-14"`

      - `"interleaved-thinking-2025-05-14"`

      - `"code-execution-2025-05-22"`

      - `"extended-cache-ttl-2025-04-11"`

      - `"context-1m-2025-08-07"`

      - `"context-management-2025-06-27"`

      - `"model-context-window-exceeded-2025-08-26"`

      - `"skills-2025-10-02"`

      - `"fast-mode-2026-02-01"`

      - `"output-300k-2026-03-24"`

      - `"user-profiles-2026-03-24"`

      - `"user-profiles-2026-08-18"`

      - `"advisor-tool-2026-03-01"`

      - `"managed-agents-2026-04-01"`

      - `"cache-diagnosis-2026-04-07"`

      - `"dreaming-2026-04-21"`

      - `"thinking-token-count-2026-05-13"`

      - `"server-side-fallback-2026-06-01"`

      - `"server-side-fallback-2026-07-01"`

      - `"fallback-credit-2026-06-01"`

      - `"fallback-credit-2026-07-01"`

      - `"agent-memory-2026-07-22"`

      - `"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string | null`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaTunnelCertificate = await client.beta.tunnels.certificates.archive(
  "certificate_id",
  { tunnel_id: "tunnel_id" }
);

console.log(betaTunnelCertificate.id);
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

## Domain Types

### Beta Tunnel Certificate

- `BetaTunnelCertificate`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string | null`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

    - `"tunnel_certificate"`

# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `BetaWebhookAgentArchivedEventData`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.archived"`

    - `"agent.archived"`

  - `workspace_id: string`

### Beta Webhook Agent Created Event Data

- `BetaWebhookAgentCreatedEventData`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.created"`

    - `"agent.created"`

  - `workspace_id: string`

### Beta Webhook Agent Deleted Event Data

- `BetaWebhookAgentDeletedEventData`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.deleted"`

    - `"agent.deleted"`

  - `workspace_id: string`

### Beta Webhook Agent Updated Event Data

- `BetaWebhookAgentUpdatedEventData`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.updated"`

    - `"agent.updated"`

  - `workspace_id: string`

### Beta Webhook Deployment Archived Event Data

- `BetaWebhookDeploymentArchivedEventData`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.archived"`

    - `"deployment.archived"`

  - `workspace_id: string`

### Beta Webhook Deployment Created Event Data

- `BetaWebhookDeploymentCreatedEventData`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.created"`

    - `"deployment.created"`

  - `workspace_id: string`

### Beta Webhook Deployment Deleted Event Data

- `BetaWebhookDeploymentDeletedEventData`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.deleted"`

    - `"deployment.deleted"`

  - `workspace_id: string`

### Beta Webhook Deployment Paused Event Data

- `BetaWebhookDeploymentPausedEventData`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.paused"`

    - `"deployment.paused"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Failed Event Data

- `BetaWebhookDeploymentRunFailedEventData`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.failed"`

    - `"deployment_run.failed"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Started Event Data

- `BetaWebhookDeploymentRunStartedEventData`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.started"`

    - `"deployment_run.started"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Succeeded Event Data

- `BetaWebhookDeploymentRunSucceededEventData`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.succeeded"`

    - `"deployment_run.succeeded"`

  - `workspace_id: string`

### Beta Webhook Deployment Unpaused Event Data

- `BetaWebhookDeploymentUnpausedEventData`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.unpaused"`

    - `"deployment.unpaused"`

  - `workspace_id: string`

### Beta Webhook Deployment Updated Event Data

- `BetaWebhookDeploymentUpdatedEventData`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.updated"`

    - `"deployment.updated"`

  - `workspace_id: string`

### Beta Webhook Environment Archived Event Data

- `BetaWebhookEnvironmentArchivedEventData`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.archived"`

    - `"environment.archived"`

  - `workspace_id: string`

### Beta Webhook Environment Created Event Data

- `BetaWebhookEnvironmentCreatedEventData`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.created"`

    - `"environment.created"`

  - `workspace_id: string`

### Beta Webhook Environment Deleted Event Data

- `BetaWebhookEnvironmentDeletedEventData`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.deleted"`

    - `"environment.deleted"`

  - `workspace_id: string`

### Beta Webhook Environment Updated Event Data

- `BetaWebhookEnvironmentUpdatedEventData`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.updated"`

    - `"environment.updated"`

  - `workspace_id: string`

### Beta Webhook Event

- `BetaWebhookEvent`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

        - `"session.created"`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

        - `"session.pending"`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

        - `"session.running"`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

        - `"session.idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

        - `"session.requires_action"`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

        - `"session.archived"`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

        - `"session.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRescheduledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

        - `"session.status_rescheduled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

        - `"session.status_run_started"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

        - `"session.status_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_created"`

        - `"session.thread_created"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_idled"`

        - `"session.thread_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_terminated"`

        - `"session.thread_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

        - `"vault.created"`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

        - `"vault.archived"`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

        - `"vault.deleted"`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

        - `"vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

        - `"vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

        - `"vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

        - `"vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookSessionUpdatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.updated"`

        - `"session.updated"`

      - `workspace_id: string`

    - `BetaWebhookAgentCreatedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.created"`

        - `"agent.created"`

      - `workspace_id: string`

    - `BetaWebhookAgentArchivedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.archived"`

        - `"agent.archived"`

      - `workspace_id: string`

    - `BetaWebhookAgentDeletedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.deleted"`

        - `"agent.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentPausedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.paused"`

        - `"deployment.paused"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunFailedEventData`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.failed"`

        - `"deployment_run.failed"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentCreatedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.created"`

        - `"deployment.created"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUpdatedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.updated"`

        - `"deployment.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUnpausedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.unpaused"`

        - `"deployment.unpaused"`

      - `workspace_id: string`

    - `BetaWebhookAgentUpdatedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.updated"`

        - `"agent.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentArchivedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.archived"`

        - `"deployment.archived"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunStartedEventData`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.started"`

        - `"deployment_run.started"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentDeletedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.deleted"`

        - `"deployment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunSucceededEventData`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.succeeded"`

        - `"deployment_run.succeeded"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentCreatedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.created"`

        - `"environment.created"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentUpdatedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.updated"`

        - `"environment.updated"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentArchivedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.archived"`

        - `"environment.archived"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentDeletedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.deleted"`

        - `"environment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreCreatedEventData`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.created"`

        - `"memory_store.created"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreArchivedEventData`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.archived"`

        - `"memory_store.archived"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreDeletedEventData`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.deleted"`

        - `"memory_store.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionBudgetReachedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.budget_reached"`

        - `"session.budget_reached"`

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

    - `"event"`

### Beta Webhook Event Data

- `BetaWebhookEventData = BetaWebhookSessionCreatedEventData | BetaWebhookSessionPendingEventData | BetaWebhookSessionRunningEventData | 41 more`

  - `BetaWebhookSessionCreatedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.created"`

      - `"session.created"`

    - `workspace_id: string`

  - `BetaWebhookSessionPendingEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.pending"`

      - `"session.pending"`

    - `workspace_id: string`

  - `BetaWebhookSessionRunningEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.running"`

      - `"session.running"`

    - `workspace_id: string`

  - `BetaWebhookSessionIdledEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.idled"`

      - `"session.idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionRequiresActionEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.requires_action"`

      - `"session.requires_action"`

    - `workspace_id: string`

  - `BetaWebhookSessionArchivedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.archived"`

      - `"session.archived"`

    - `workspace_id: string`

  - `BetaWebhookSessionDeletedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.deleted"`

      - `"session.deleted"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRescheduledEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_rescheduled"`

      - `"session.status_rescheduled"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRunStartedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_run_started"`

      - `"session.status_run_started"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusIdledEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_idled"`

      - `"session.status_idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusTerminatedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_terminated"`

      - `"session.status_terminated"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadCreatedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_created"`

      - `"session.thread_created"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadIdledEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_idled"`

      - `"session.thread_idled"`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadTerminatedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_terminated"`

      - `"session.thread_terminated"`

    - `workspace_id: string`

  - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.outcome_evaluation_ended"`

      - `"session.outcome_evaluation_ended"`

    - `workspace_id: string`

  - `BetaWebhookVaultCreatedEventData`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.created"`

      - `"vault.created"`

    - `workspace_id: string`

  - `BetaWebhookVaultArchivedEventData`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.archived"`

      - `"vault.archived"`

    - `workspace_id: string`

  - `BetaWebhookVaultDeletedEventData`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.deleted"`

      - `"vault.deleted"`

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialCreatedEventData`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.created"`

      - `"vault_credential.created"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialArchivedEventData`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.archived"`

      - `"vault_credential.archived"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialDeletedEventData`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.deleted"`

      - `"vault_credential.deleted"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialRefreshFailedEventData`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.refresh_failed"`

      - `"vault_credential.refresh_failed"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookSessionUpdatedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.updated"`

      - `"session.updated"`

    - `workspace_id: string`

  - `BetaWebhookAgentCreatedEventData`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.created"`

      - `"agent.created"`

    - `workspace_id: string`

  - `BetaWebhookAgentArchivedEventData`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.archived"`

      - `"agent.archived"`

    - `workspace_id: string`

  - `BetaWebhookAgentDeletedEventData`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.deleted"`

      - `"agent.deleted"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentPausedEventData`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.paused"`

      - `"deployment.paused"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunFailedEventData`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.failed"`

      - `"deployment_run.failed"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentCreatedEventData`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.created"`

      - `"deployment.created"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentUpdatedEventData`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.updated"`

      - `"deployment.updated"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentUnpausedEventData`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.unpaused"`

      - `"deployment.unpaused"`

    - `workspace_id: string`

  - `BetaWebhookAgentUpdatedEventData`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.updated"`

      - `"agent.updated"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentArchivedEventData`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.archived"`

      - `"deployment.archived"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunStartedEventData`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.started"`

      - `"deployment_run.started"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentDeletedEventData`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.deleted"`

      - `"deployment.deleted"`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunSucceededEventData`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.succeeded"`

      - `"deployment_run.succeeded"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentCreatedEventData`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.created"`

      - `"environment.created"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentUpdatedEventData`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.updated"`

      - `"environment.updated"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentArchivedEventData`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.archived"`

      - `"environment.archived"`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentDeletedEventData`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.deleted"`

      - `"environment.deleted"`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreCreatedEventData`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.created"`

      - `"memory_store.created"`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreArchivedEventData`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.archived"`

      - `"memory_store.archived"`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreDeletedEventData`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.deleted"`

      - `"memory_store.deleted"`

    - `workspace_id: string`

  - `BetaWebhookSessionBudgetReachedEventData`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.budget_reached"`

      - `"session.budget_reached"`

    - `workspace_id: string`

### Beta Webhook Memory Store Archived Event Data

- `BetaWebhookMemoryStoreArchivedEventData`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.archived"`

    - `"memory_store.archived"`

  - `workspace_id: string`

### Beta Webhook Memory Store Created Event Data

- `BetaWebhookMemoryStoreCreatedEventData`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.created"`

    - `"memory_store.created"`

  - `workspace_id: string`

### Beta Webhook Memory Store Deleted Event Data

- `BetaWebhookMemoryStoreDeletedEventData`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.deleted"`

    - `"memory_store.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Archived Event Data

- `BetaWebhookSessionArchivedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.archived"`

    - `"session.archived"`

  - `workspace_id: string`

### Beta Webhook Session Budget Reached Event Data

- `BetaWebhookSessionBudgetReachedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.budget_reached"`

    - `"session.budget_reached"`

  - `workspace_id: string`

### Beta Webhook Session Created Event Data

- `BetaWebhookSessionCreatedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.created"`

    - `"session.created"`

  - `workspace_id: string`

### Beta Webhook Session Deleted Event Data

- `BetaWebhookSessionDeletedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.deleted"`

    - `"session.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Idled Event Data

- `BetaWebhookSessionIdledEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.idled"`

    - `"session.idled"`

  - `workspace_id: string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.outcome_evaluation_ended"`

    - `"session.outcome_evaluation_ended"`

  - `workspace_id: string`

### Beta Webhook Session Pending Event Data

- `BetaWebhookSessionPendingEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.pending"`

    - `"session.pending"`

  - `workspace_id: string`

### Beta Webhook Session Requires Action Event Data

- `BetaWebhookSessionRequiresActionEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.requires_action"`

    - `"session.requires_action"`

  - `workspace_id: string`

### Beta Webhook Session Running Event Data

- `BetaWebhookSessionRunningEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.running"`

    - `"session.running"`

  - `workspace_id: string`

### Beta Webhook Session Status Idled Event Data

- `BetaWebhookSessionStatusIdledEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_idled"`

    - `"session.status_idled"`

  - `workspace_id: string`

### Beta Webhook Session Status Rescheduled Event Data

- `BetaWebhookSessionStatusRescheduledEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_rescheduled"`

    - `"session.status_rescheduled"`

  - `workspace_id: string`

### Beta Webhook Session Status Run Started Event Data

- `BetaWebhookSessionStatusRunStartedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_run_started"`

    - `"session.status_run_started"`

  - `workspace_id: string`

### Beta Webhook Session Status Terminated Event Data

- `BetaWebhookSessionStatusTerminatedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_terminated"`

    - `"session.status_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Thread Created Event Data

- `BetaWebhookSessionThreadCreatedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_created"`

    - `"session.thread_created"`

  - `workspace_id: string`

### Beta Webhook Session Thread Idled Event Data

- `BetaWebhookSessionThreadIdledEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_idled"`

    - `"session.thread_idled"`

  - `workspace_id: string`

### Beta Webhook Session Thread Terminated Event Data

- `BetaWebhookSessionThreadTerminatedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_terminated"`

    - `"session.thread_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Updated Event Data

- `BetaWebhookSessionUpdatedEventData`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.updated"`

    - `"session.updated"`

  - `workspace_id: string`

### Beta Webhook Vault Archived Event Data

- `BetaWebhookVaultArchivedEventData`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.archived"`

    - `"vault.archived"`

  - `workspace_id: string`

### Beta Webhook Vault Created Event Data

- `BetaWebhookVaultCreatedEventData`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.created"`

    - `"vault.created"`

  - `workspace_id: string`

### Beta Webhook Vault Credential Archived Event Data

- `BetaWebhookVaultCredentialArchivedEventData`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.archived"`

    - `"vault_credential.archived"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Created Event Data

- `BetaWebhookVaultCredentialCreatedEventData`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.created"`

    - `"vault_credential.created"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Deleted Event Data

- `BetaWebhookVaultCredentialDeletedEventData`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.deleted"`

    - `"vault_credential.deleted"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `BetaWebhookVaultCredentialRefreshFailedEventData`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.refresh_failed"`

    - `"vault_credential.refresh_failed"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Deleted Event Data

- `BetaWebhookVaultDeletedEventData`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.deleted"`

    - `"vault.deleted"`

  - `workspace_id: string`

### Unwrap Webhook Event

- `UnwrapWebhookEvent`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

        - `"session.created"`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

        - `"session.pending"`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

        - `"session.running"`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

        - `"session.idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

        - `"session.requires_action"`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

        - `"session.archived"`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

        - `"session.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRescheduledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

        - `"session.status_rescheduled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

        - `"session.status_run_started"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

        - `"session.status_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

        - `"session.status_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_created"`

        - `"session.thread_created"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_idled"`

        - `"session.thread_idled"`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_terminated"`

        - `"session.thread_terminated"`

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

        - `"vault.created"`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

        - `"vault.archived"`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

        - `"vault.deleted"`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

        - `"vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

        - `"vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

        - `"vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

        - `"vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookSessionUpdatedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.updated"`

        - `"session.updated"`

      - `workspace_id: string`

    - `BetaWebhookAgentCreatedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.created"`

        - `"agent.created"`

      - `workspace_id: string`

    - `BetaWebhookAgentArchivedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.archived"`

        - `"agent.archived"`

      - `workspace_id: string`

    - `BetaWebhookAgentDeletedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.deleted"`

        - `"agent.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentPausedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.paused"`

        - `"deployment.paused"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunFailedEventData`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.failed"`

        - `"deployment_run.failed"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentCreatedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.created"`

        - `"deployment.created"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUpdatedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.updated"`

        - `"deployment.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUnpausedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.unpaused"`

        - `"deployment.unpaused"`

      - `workspace_id: string`

    - `BetaWebhookAgentUpdatedEventData`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.updated"`

        - `"agent.updated"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentArchivedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.archived"`

        - `"deployment.archived"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunStartedEventData`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.started"`

        - `"deployment_run.started"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentDeletedEventData`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.deleted"`

        - `"deployment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunSucceededEventData`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.succeeded"`

        - `"deployment_run.succeeded"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentCreatedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.created"`

        - `"environment.created"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentUpdatedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.updated"`

        - `"environment.updated"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentArchivedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.archived"`

        - `"environment.archived"`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentDeletedEventData`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.deleted"`

        - `"environment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreCreatedEventData`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.created"`

        - `"memory_store.created"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreArchivedEventData`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.archived"`

        - `"memory_store.archived"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreDeletedEventData`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.deleted"`

        - `"memory_store.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionBudgetReachedEventData`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.budget_reached"`

        - `"session.budget_reached"`

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

    - `"event"`
