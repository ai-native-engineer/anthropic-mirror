<!-- source: https://platform.claude.com/docs/en/api/admin/federation_rules/create -->

# Create Federation Rule
POST/v1/organizations/federation_rules
Create a federation rule owned by your organization.
The referenced issuer and the target service account must already exist in the same organization; invalid references are rejected with a 400 error. The workspace reference is validated. Membership is not checked at rule creation: token exchange resolves a single enabled workspace per call and is rejected unless the target service account is a member of that workspace (it is implicitly a member of the default workspace). Rules on well-known shared issuers (GitHub Actions, GitLab, Buildkite, Terraform Cloud, Google) must constrain tenant identity via an identity-bearing claim, a tenant-pinning subject prefix (such as `repo:YOUR_ORG/...`), or a CEL condition referencing one of those identity claims (e.g. `claims.repository_owner`). OAuth callers may only manage rules whose `oauth_scope` is `workspace:developer` or `workspace:inference`; other scopes require a Console session. Admin API keys are not accepted.
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of string
Optional header to specify the beta version(s) you want to use.
To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.anthropic-beta)
#####  Body ParametersJSONExpand Collapse 
issuer_id: string
Tagged ID of the federation issuer.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.issuer_id)
match: object { audience, claims, condition, subject_prefix } 
Conditions the verified JWT must satisfy for this rule to apply. At least one of `subject_prefix` (other than a wildcard-only value like `*`), `claims`, or `condition` is required; `audience` alone is not sufficient.
audience: optional string
Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.match.audience)
claims: optional map[string]
Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.match.claims)
condition: optional string
CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.match.condition)
subject_prefix: optional string
Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.match.subject_prefix)
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.match)
name: string
Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.name)
oauth_scope: string
Space-separated OAuth scopes. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.oauth_scope)
target: object { service_account_id, type, service_account_name } 
Identity that tokens minted via this rule act as. Currently always a `service_account` target.
service_account_id: string
Tagged ID of the service account to mint tokens for.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.target.service_account_id)
type: "service_account"
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.target.type)
service_account_name: optional string
Service account's display name at read time. Ignored on writes.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.target.service_account_name)
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.target)
applies_to_all_workspaces: optional boolean
When true, enable this rule for every workspace in the org (including workspaces created later).
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.applies_to_all_workspaces)
attributes: optional map[string]
CEL expressions `{name: expr}` extracting named values from claims. Not yet supported; any non-empty value is rejected with 400.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.attributes)
description: optional string
Optional free-text description.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.description)
token_lifetime_seconds: optional number
Lifetime in seconds for access tokens minted via this rule (60-86400). Defaults to 3600 (1h). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.token_lifetime_seconds)
workspace_id: optional string
Tagged ID of the workspace to enable this rule for. Required unless `applies_to_all_workspaces` is true. Additional workspaces can be added via the `/federation_rules/{federation_rule_id}/workspaces` sub-resource.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#create.workspace_id)
FederationRule object { id, applies_to_all_workspaces, archived_at, 17 more } 
Authorization rule binding an external OIDC identity to Anthropic.
Evaluates the match conditions and mints an OAuth access token for the resolved target, scoped to a single workspace where the rule is enabled (chosen by the caller at exchange time when the rule is enabled for more than one). For rules enabled via `workspace_ids` or `applies_to_all_workspaces`, the target service account must be a member of that workspace (it is implicitly a member of the default workspace); rules carrying only the legacy `workspace_id` binding do not enforce this.
Tagged ID of the federation rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.id)
applies_to_all_workspaces: boolean
When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.applies_to_all_workspaces)
archived_at: string
If set, this rule is archived and rejects token exchange.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.archived_at)
archived_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that archived this rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.archived_by_actor_id)
attributes: map[string]
CEL expressions extracting named values from claims. Not yet supported; always null.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.attributes)
created_at: string
When this rule was created.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.created_at)
created_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that created this rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.created_by_actor_id)
description: string
Optional free-text description.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.description)
issuer_id: string
Tagged ID of the issuer whose tokens this rule accepts.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.issuer_id)
issuer_name: string
Issuer's display name at read time.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.issuer_name)
match: object { audience, claims, condition, subject_prefix } 
Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.
audience: optional string
Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.match.audience)
claims: optional map[string]
Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.match.claims)
condition: optional string
CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.match.condition)
subject_prefix: optional string
Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.match.subject_prefix)
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.match)
name: string
Admin-chosen slug identifier.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.name)
oauth_scope: string
Space-separated OAuth scopes granted on the minted token.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.oauth_scope)
target: object { service_account_id, type, service_account_name } 
Identity that tokens minted via this rule act as. Currently always a `service_account` target.
service_account_id: string
Tagged ID of the service account to mint tokens for.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.target.service_account_id)
type: "service_account"
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.target.type)
service_account_name: optional string
Service account's display name at read time. Ignored on writes.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.target.service_account_name)
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.target)
token_lifetime_seconds: number
Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.token_lifetime_seconds)
type: "federation_rule"
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.type)
updated_at: string
When this rule was last updated.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.updated_at)
updated_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.updated_by_actor_id)
workspace_id: string
Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.workspace_id)
workspace_ids: array of string
Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule.workspace_ids)
[](https://platform.claude.com/docs/en/api/admin/federation_rules/create#federation_rule)
Create Federation Rule

curl https://api.anthropic.com/v1/organizations/federation_rules \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "issuer_id": "issuer_id",
          "match": {},
          "name": "x",
          "oauth_scope": "x",
          "target": {
            "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
            "type": "service_account"
        }'

  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]

  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
