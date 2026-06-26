<!-- source: https://platform.claude.com/docs/en/api/admin/federation_rules -->

# Federation Rules
##### [Create Federation Rule](https://platform.claude.com/docs/en/api/admin/federation_rules/create)
POST/v1/organizations/federation_rules
##### [Get Federation Rule](https://platform.claude.com/docs/en/api/admin/federation_rules/retrieve)
GET/v1/organizations/federation_rules/{federation_rule_id}
##### [List Federation Rules](https://platform.claude.com/docs/en/api/admin/federation_rules/list)
GET/v1/organizations/federation_rules
##### [Update Federation Rule](https://platform.claude.com/docs/en/api/admin/federation_rules/update)
POST/v1/organizations/federation_rules/{federation_rule_id}
##### [Archive Federation Rule](https://platform.claude.com/docs/en/api/admin/federation_rules/archive)
POST/v1/organizations/federation_rules/{federation_rule_id}/archive
##### ModelsExpand Collapse 
FederationRule object { id, applies_to_all_workspaces, archived_at, 17 more } 
Authorization rule binding an external OIDC identity to Anthropic.
Evaluates the match conditions and mints an OAuth access token for the resolved target, scoped to a single workspace where the rule is enabled (chosen by the caller at exchange time when the rule is enabled for more than one). For rules enabled via `workspace_ids` or `applies_to_all_workspaces`, the target service account must be a member of that workspace (it is implicitly a member of the default workspace); rules carrying only the legacy `workspace_id` binding do not enforce this.
Tagged ID of the federation rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.id)
applies_to_all_workspaces: boolean
When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.applies_to_all_workspaces)
archived_at: string
If set, this rule is archived and rejects token exchange.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.archived_at)
archived_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that archived this rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.archived_by_actor_id)
attributes: map[string]
CEL expressions extracting named values from claims. Not yet supported; always null.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.attributes)
created_at: string
When this rule was created.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.created_at)
created_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that created this rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.created_by_actor_id)
description: string
Optional free-text description.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.description)
issuer_id: string
Tagged ID of the issuer whose tokens this rule accepts.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.issuer_id)
issuer_name: string
Issuer's display name at read time.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.issuer_name)
match: object { audience, claims, condition, subject_prefix } 
Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.
audience: optional string
Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.match.audience)
claims: optional map[string]
Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.match.claims)
condition: optional string
CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.match.condition)
subject_prefix: optional string
Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.match.subject_prefix)
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.match)
name: string
Admin-chosen slug identifier.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.name)
oauth_scope: string
Space-separated OAuth scopes granted on the minted token.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.oauth_scope)
target: object { service_account_id, type, service_account_name } 
Identity that tokens minted via this rule act as. Currently always a `service_account` target.
service_account_id: string
Tagged ID of the service account to mint tokens for.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.target.service_account_id)
type: "service_account"
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.target.type)
service_account_name: optional string
Service account's display name at read time. Ignored on writes.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.target.service_account_name)
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.target)
token_lifetime_seconds: number
Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.token_lifetime_seconds)
type: "federation_rule"
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.type)
updated_at: string
When this rule was last updated.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.updated_at)
updated_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.updated_by_actor_id)
workspace_id: string
Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.workspace_id)
workspace_ids: array of string
Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule.workspace_ids)
[](https://platform.claude.com/docs/en/api/admin/federation_rules#federation_rule)
####  Federation RulesWorkspaces
##### [List Federation Rule Workspaces](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/list)
GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces
##### [Add Federation Rule Workspace](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/create)
POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces
##### [Remove Federation Rule Workspace](https://platform.claude.com/docs/en/api/admin/federation_rules/workspaces/delete)
DELETE/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}
##### ModelsExpand Collapse 
WorkspaceListResponse object { created_at, created_by_actor_id, federation_rule_id, 3 more } 
created_at: string
When this workspace was enabled for the rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_list_response.created_at)
created_by_actor_id: string
Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_list_response.created_by_actor_id)
federation_rule_id: string
Tagged ID of the federation rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_list_response.federation_rule_id)
type: "federation_rule_workspace"
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_list_response.type)
workspace_id: string
Tagged ID of the workspace this rule is enabled for.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_list_response.workspace_id)
workspace_name: string
Workspace display name. Populated when listing; null in the enable response.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_list_response.workspace_name)
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_list_response)
WorkspaceCreateResponse object { created_at, created_by_actor_id, federation_rule_id, 3 more } 
created_at: string
When this workspace was enabled for the rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_create_response.created_at)
created_by_actor_id: string
Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_create_response.created_by_actor_id)
federation_rule_id: string
Tagged ID of the federation rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_create_response.federation_rule_id)
type: "federation_rule_workspace"
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_create_response.type)
workspace_id: string
Tagged ID of the workspace this rule is enabled for.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_create_response.workspace_id)
workspace_name: string
Workspace display name. Populated when listing; null in the enable response.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_create_response.workspace_name)
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_create_response)
WorkspaceDeleteResponse object { federation_rule_id, type, workspace_id } 
federation_rule_id: string
Tagged ID of the federation rule.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_delete_response.federation_rule_id)
type: "federation_rule_workspace_deleted"
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_delete_response.type)
workspace_id: string
Tagged ID of the workspace named in the delete request. Removal is idempotent.
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_delete_response.workspace_id)
[](https://platform.claude.com/docs/en/api/admin/federation_rules#workspace_delete_response)
