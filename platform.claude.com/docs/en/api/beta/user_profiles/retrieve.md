<!-- source: https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve -->

# Get User Profile
GET/v1/user_profiles/{user_profile_id}
Get User Profile
##### Path ParametersExpand Collapse 
user_profile_id: string
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#retrieve.user_profile_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#retrieve.betas)
BetaUserProfile object { id, created_at, metadata, 6 more } 
Unique identifier for this user profile, prefixed `uprof_`.
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile.id)
created_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile.created_at)
metadata: map[string]
Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile.metadata)
relationship: "external" or "resold" or "internal"
How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.
"external"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile.relationship%5B0%5D)
"resold"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile.relationship%5B1%5D)
"internal"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile.relationship%5B2%5D)
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile.relationship)
trust_grants: map[[BetaUserProfileTrustGrant](https://platform.claude.com/docs/en/api/beta#beta_user_profile_trust_grant) { status } ]
Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.
status: "active" or "pending" or "rejected"
Status of the trust grant.
"active"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile_trust_grant.status%5B0%5D)
"pending"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile_trust_grant.status%5B1%5D)
"rejected"
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile_trust_grant.status%5B2%5D)
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile_trust_grant.status)
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile.trust_grants)
type: "user_profile"
Object type. Always `user_profile`.
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile.type)
updated_at: string
A timestamp in RFC 3339 format
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile.updated_at)
external_id: optional string
Platform's own identifier for this user. Not enforced unique.
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile.external_id)
name: optional string
Display name of the entity this profile represents. For `resold` this is the resold-to company's name.
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile.name)
[](https://platform.claude.com/docs/en/api/beta/user_profiles/retrieve#beta_user_profile)
Get User Profile
cURL

curl https://api.anthropic.com/v1/user_profiles/$USER_PROFILE_ID \
    -H 'anthropic-beta: user-profiles-2026-03-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"

  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
