<!-- source: https://platform.claude.com/docs/en/api/admin/federation_issuers/archive -->

# Archive Federation Issuer
POST/v1/organizations/federation_issuers/{federation_issuer_id}/archive
Archive a federation issuer.
Idempotent; re-archiving returns the issuer with its original `archived_at`. Rejected with 400 if any live (non-archived) federation rule still references the issuer; archive those rules first (a rule's issuer cannot be changed), or recreate them against another issuer.
Requires an OAuth bearer or Console session; Admin API keys are not accepted.
##### Path ParametersExpand Collapse 
federation_issuer_id: string
ID of the federation issuer to archive.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#archive.federation_issuer_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of string
Optional header to specify the beta version(s) you want to use.
To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#archive.anthropic-beta)
FederationIssuer object { id, archived_at, archived_by_actor_id, 12 more } 
Registered external OIDC identity provider.
Records an external IdP the organization trusts for the RFC 7523 jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.
Tagged ID of the federation issuer.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.id)
archived_at: string
If set, all rules referencing this issuer reject token exchange.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.archived_at)
archived_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.archived_by_actor_id)
check_jti: boolean
Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.check_jti)
created_at: string
When this issuer was created.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.created_at)
created_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that created this issuer.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.created_by_actor_id)
issuer_url: string
The `iss` claim value. Incoming JWTs must match exactly.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.issuer_url)
jwks: object { type, ca_cert_pem, discovery_base }  or object { type, url, ca_cert_pem }  or object { keys, type } 
How signing keys are obtained for signature verification.
Discovery object { type, ca_cert_pem, discovery_base } 
JWKS via the issuer's OIDC discovery document.
type: "discovery"
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.jwks%5B0%5D.type)
ca_cert_pem: optional string
Optional custom CA (PEM) for TLS verification of the JWKS fetch.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.jwks%5B0%5D.ca_cert_pem)
discovery_base: optional string
Set when the discovery URL differs from `issuer_url`.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.jwks%5B0%5D.discovery_base)
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.jwks%5B0%5D)
ExplicitURL object { type, url, ca_cert_pem } 
JWKS fetched from a fixed endpoint.
type: "explicit_url"
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.jwks%5B1%5D.type)
url: string
JWKS endpoint.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.jwks%5B1%5D.url)
ca_cert_pem: optional string
Optional custom CA (PEM) for TLS verification of the JWKS fetch.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.jwks%5B1%5D.ca_cert_pem)
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.jwks%5B1%5D)
Inline object { keys, type } 
JWKS supplied directly; no network fetch.
keys: array of map[unknown]
Inline JWK objects.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.jwks%5B2%5D.keys)
type: "inline"
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.jwks%5B2%5D.type)
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.jwks%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.jwks)
jwks_polling_disabled_at: string
If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.jwks_polling_disabled_at)
max_jwt_lifetime_seconds: number
Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.max_jwt_lifetime_seconds)
name: string
Admin-chosen slug identifier.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.name)
poll_status: object { consecutive_failures, last_fetched_at, next_poll_at } 
Status of automatic JWKS polling for a federation issuer.
Anthropic periodically fetches the issuer's signing keys in the background. These fields summarize the most recent fetches so the health of the JWKS endpoint can be monitored.
consecutive_failures: number
Consecutive fetch failures since the last success.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.poll_status.consecutive_failures)
last_fetched_at: string
When the last successful fetch completed.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.poll_status.last_fetched_at)
next_poll_at: string
When the next fetch is scheduled. Null if paused.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.poll_status.next_poll_at)
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.poll_status)
type: "federation_issuer"
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.type)
updated_at: string
When this issuer was last updated.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.updated_at)
updated_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer.updated_by_actor_id)
[](https://platform.claude.com/docs/en/api/admin/federation_issuers/archive#federation_issuer)
Archive Federation Issuer

curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID/archive \
    -X POST \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"

  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
