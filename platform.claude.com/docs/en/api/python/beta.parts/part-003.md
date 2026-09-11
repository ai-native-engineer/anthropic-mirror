<!-- source: https://platform.claude.com/docs/en/api/python/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/python/beta -->

<!-- chunk-start -->

  Lifetime in seconds for access tokens minted via this rule (60-86400). Defaults to 3600 (1h). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  maximum: 86400, minimum: 60

- `workspace_id: Optional[str]`

  Tagged ID of the workspace to enable this rule for. Required unless `applies_to_all_workspaces` is true. Additional workspaces can be added via the `/federation_rules/{federation_rule_id}/workspaces` sub-resource.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaFederationRule: …`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: Literal["federation_rule"]`

    default: federation_rule

  - `id: str`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: bool`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: Optional[datetime]`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: Optional[Dict[str, str]]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: datetime`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: Optional[str]`

    Optional free-text description.

  - `issuer_id: str`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: Optional[str]`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: Optional[str]`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: Optional[Dict[str, str]]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: Optional[str]`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: Optional[str]`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: str`

    Admin-chosen slug identifier.

  - `oauth_scope: str`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `type: Literal["service_account"]`

    - `service_account_id: str`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: Optional[str]`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: int`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `updated_at: datetime`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: Optional[str]`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: List[str]`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_federation_rule = client.beta.organization.federation.rules.create(
    issuer_id="issuer_id",
    match={},
    name="x",
    oauth_scope="x",
    target={
        "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
        "type": "service_account",
    },
)
print(beta_federation_rule.id)
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### List Federation Rules

`beta.organization.federation.rules.list(**kwargs)  -> SyncPageCursor[BetaFederationRule]`

**GET** `/v1/organizations/federation_rules`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List federation rules in your organization.

Optionally filter by issuer with `issuer_id`. Archived rules are excluded
unless `include_archived=true`.

#### Parameters

- `include_archived: Optional[bool]`

  Include archived resources. Defaults to false.

  default: false

- `issuer_id: Optional[str]`

  Filter to rules referencing this federation issuer.

- `limit: Optional[int]`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: Optional[str]`

  Opaque cursor from a previous response's `next_page`.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaFederationRule: …`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: Literal["federation_rule"]`

    default: federation_rule

  - `id: str`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: bool`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: Optional[datetime]`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: Optional[Dict[str, str]]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: datetime`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: Optional[str]`

    Optional free-text description.

  - `issuer_id: str`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: Optional[str]`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: Optional[str]`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: Optional[Dict[str, str]]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: Optional[str]`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: Optional[str]`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: str`

    Admin-chosen slug identifier.

  - `oauth_scope: str`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `type: Literal["service_account"]`

    - `service_account_id: str`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: Optional[str]`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: int`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `updated_at: datetime`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: Optional[str]`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: List[str]`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.organization.federation.rules.list()
page = page.data[0]
print(page.id)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
      "applies_to_all_workspaces": true,
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "attributes": {
        "foo": "string"
      },
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "issuer_id": "issuer_id",
      "issuer_name": "issuer_name",
      "match": {
        "audience": "audience",
        "claims": {
          "foo": "string"
        },
        "condition": "condition",
        "subject_prefix": "subject_prefix"
      },
      "name": "prod-deploy-pipeline",
      "oauth_scope": "oauth_scope",
      "target": {
        "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
        "type": "service_account",
        "service_account_name": "service_account_name"
      },
      "token_lifetime_seconds": 0,
      "type": "federation_rule",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id",
      "workspace_id": "workspace_id",
      "workspace_ids": [
        "string"
      ]
    }
  ],
  "next_page": "next_page"
}
```

### Get Federation Rule

`beta.organization.federation.rules.retrieve(federation_rule_id, **kwargs)  -> BetaFederationRule`

**GET** `/v1/organizations/federation_rules/{federation_rule_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a federation rule by its ID (`fdrl_...`).

#### Parameters

- `federation_rule_id: str`

  ID of the federation rule.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaFederationRule: …`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: Literal["federation_rule"]`

    default: federation_rule

  - `id: str`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: bool`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: Optional[datetime]`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: Optional[Dict[str, str]]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: datetime`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: Optional[str]`

    Optional free-text description.

  - `issuer_id: str`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: Optional[str]`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: Optional[str]`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: Optional[Dict[str, str]]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: Optional[str]`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: Optional[str]`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: str`

    Admin-chosen slug identifier.

  - `oauth_scope: str`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `type: Literal["service_account"]`

    - `service_account_id: str`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: Optional[str]`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: int`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `updated_at: datetime`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: Optional[str]`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: List[str]`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_federation_rule = client.beta.organization.federation.rules.retrieve(
    federation_rule_id="federation_rule_id",
)
print(beta_federation_rule.id)
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### Update Federation Rule

`beta.organization.federation.rules.update(federation_rule_id, **kwargs)  -> BetaFederationRule`

**POST** `/v1/organizations/federation_rules/{federation_rule_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Partially update a federation rule.

`issuer_id` is immutable. `match` and `target` are replaced as whole
objects when set. Referenced service accounts and workspaces must exist
in your organization; invalid references are rejected with a 400 error.
Archived rules cannot be updated; this returns 400. Create a new rule
instead. Rules on well-known shared issuers (GitHub Actions, GitLab,
Buildkite, Terraform Cloud, Google) must constrain tenant identity via
an identity-bearing claim, a tenant-pinning subject prefix (such as
`repo:YOUR_ORG/...`), or a CEL condition referencing one of those
identity claims (e.g. `claims.repository_owner`). On these issuers the
requirement is re-checked on every update; if an existing rule's stored
match does not yet constrain tenant identity, any update (even a rename
or description change) must also supply a conforming `match` in the same
request. OAuth callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Parameters

- `federation_rule_id: str`

  ID of the federation rule to update.

- `applies_to_all_workspaces: Optional[bool]`

  When true, enables this rule for every workspace in the org (including workspaces created later). Setting `false` is rejected with 400 if no workspace would remain enabled; a rule with only a legacy `workspace_id` binding continues to mint.

- `attributes: Optional[Dict[str, str]]`

  Replaces the CEL expressions `{name: expr}` extracting named values from claims. Send null to clear them. Not yet supported; any non-empty value is rejected with 400.

- `description: Optional[str]`

  Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

  maxLength: 2000

- `match: Optional[BetaFederationRuleMatchParam]`

  Does the incoming JWT qualify?

  All populated fields must pass; omitted fields are skipped. At least one
  of `subject_prefix` (other than a wildcard-only value like `*`), `claims`,
  or `condition` is required; `audience` alone is not sufficient.

  - `audience: Optional[str]`

    Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

    maxLength: 1024

  - `claims: Optional[Dict[str, str]]`

    Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

  - `condition: Optional[str]`

    CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

    maxLength: 4096

  - `subject_prefix: Optional[str]`

    Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

    maxLength: 1024

- `name: Optional[str]`

  Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `oauth_scope: Optional[str]`

  Replaces the space-separated OAuth scopes granted on minted tokens. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

  minLength: 1

- `target: Optional[BetaServiceAccountTargetParam]`

  Bind to a fixed service account by ID.

  - `type: Literal["service_account"]`

  - `service_account_id: str`

    Tagged ID of the service account to mint tokens for.

  - `service_account_name: Optional[str]`

    Service account's display name at read time. Ignored on writes.

- `token_lifetime_seconds: Optional[int]`

  Replaces the lifetime in seconds for access tokens minted via this rule (60-86400). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  maximum: 86400, minimum: 60

- `workspace_id: Optional[str]`

  Replaces the existing single workspace enablement (the previous one is removed). Rejected with 400 if the rule is enabled for more than one workspace; use the `/federation_rules/{federation_rule_id}/workspaces` sub-resource instead.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaFederationRule: …`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: Literal["federation_rule"]`

    default: federation_rule

  - `id: str`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: bool`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: Optional[datetime]`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: Optional[Dict[str, str]]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: datetime`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: Optional[str]`

    Optional free-text description.

  - `issuer_id: str`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: Optional[str]`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: Optional[str]`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: Optional[Dict[str, str]]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: Optional[str]`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: Optional[str]`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: str`

    Admin-chosen slug identifier.

  - `oauth_scope: str`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `type: Literal["service_account"]`

    - `service_account_id: str`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: Optional[str]`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: int`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `updated_at: datetime`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: Optional[str]`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: List[str]`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_federation_rule = client.beta.organization.federation.rules.update(
    federation_rule_id="federation_rule_id",
)
print(beta_federation_rule.id)
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### Archive Federation Rule

`beta.organization.federation.rules.archive(federation_rule_id, **kwargs)  -> BetaFederationRule`

**POST** `/v1/organizations/federation_rules/{federation_rule_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a federation rule.

Token exchange through this rule stops immediately. Idempotent;
re-archiving returns the rule with its original `archived_at`. Archiving
clears the rule's workspace targeting (`workspace_id` and
`workspace_ids` are emptied). Tokens already minted before archive
remain valid until they expire. OAuth callers may only manage rules
whose `oauth_scope` is `workspace:developer` or `workspace:inference`;
other scopes require a Console session.

#### Parameters

- `federation_rule_id: str`

  ID of the federation rule to archive.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaFederationRule: …`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `type: Literal["federation_rule"]`

    default: federation_rule

  - `id: str`

    Tagged ID of the federation rule.

  - `applies_to_all_workspaces: bool`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `archived_at: Optional[datetime]`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `archived_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `attributes: Optional[Dict[str, str]]`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `created_at: datetime`

    When this rule was created.

    format: date-time

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `description: Optional[str]`

    Optional free-text description.

  - `issuer_id: str`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `issuer_name: Optional[str]`

    Issuer's display name at read time.

  - `match: BetaFederationRuleMatch`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `audience: Optional[str]`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `claims: Optional[Dict[str, str]]`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `condition: Optional[str]`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `subject_prefix: Optional[str]`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `name: str`

    Admin-chosen slug identifier.

  - `oauth_scope: str`

    Space-separated OAuth scopes granted on the minted token.

  - `target: BetaServiceAccountTarget`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `type: Literal["service_account"]`

    - `service_account_id: str`

      Tagged ID of the service account to mint tokens for.

    - `service_account_name: Optional[str]`

      Service account's display name at read time. Ignored on writes.

  - `token_lifetime_seconds: int`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `updated_at: datetime`

    When this rule was last updated.

    format: date-time

  - `updated_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `workspace_id: Optional[str]`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `workspace_ids: List[str]`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_federation_rule = client.beta.organization.federation.rules.archive(
    federation_rule_id="federation_rule_id",
)
print(beta_federation_rule.id)
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

## Beta › Organization › Federation › Rules › Workspaces

### Add Federation Rule Workspace

`beta.organization.federation.rules.workspaces.add(federation_rule_id, **kwargs)  -> BetaFederationRuleWorkspace`

**POST** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Enable a federation rule for a workspace.

Idempotent; re-enabling returns the existing enablement. The rule and
workspace must both belong to your organization. Membership of the
rule's target service account in this workspace is not checked at
enablement: token exchange into this workspace is rejected unless the
target is a member (it is implicitly a member of the default workspace).
Archived rules are rejected with 400. OAuth callers may only manage rules
whose `oauth_scope` is `workspace:developer` or `workspace:inference`;
other scopes require a Console session.

#### Parameters

- `federation_rule_id: str`

  ID of the federation rule.

- `workspace_id: str`

  Tagged ID of the workspace to enable this rule for.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaFederationRuleWorkspace: …`

  - `type: Literal["federation_rule_workspace"]`

    default: federation_rule_workspace

  - `created_at: datetime`

    When this workspace was enabled for the rule.

    format: date-time

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: str`

    Tagged ID of the federation rule.

  - `workspace_id: str`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: Optional[str]`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_federation_rule_workspace = (
    client.beta.organization.federation.rules.workspaces.add(
        federation_rule_id="federation_rule_id",
        workspace_id="workspace_id",
    )
)
print(beta_federation_rule_workspace.created_by_actor_id)
```

##### Response (200)

```json
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace",
  "workspace_id": "workspace_id",
  "workspace_name": "workspace_name"
}
```

### List Federation Rule Workspaces

`beta.organization.federation.rules.workspaces.list(federation_rule_id, **kwargs)  -> SyncPageCursor[BetaFederationRuleWorkspace]`

**GET** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List workspaces where this federation rule is enabled.

Returns all workspace enablements in a single response; the `limit` and
`page` parameters are accepted but have no effect, and `next_page` is
always `null`. Returns explicit per-workspace enablements only; for
rules with `applies_to_all_workspaces` or a legacy single
`workspace_id`, check those fields on the rule itself.

#### Parameters

- `federation_rule_id: str`

  ID of the federation rule.

- `limit: Optional[int]`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: Optional[str]`

  Opaque cursor from a previous response's `next_page`.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaFederationRuleWorkspace: …`

  - `type: Literal["federation_rule_workspace"]`

    default: federation_rule_workspace

  - `created_at: datetime`

    When this workspace was enabled for the rule.

    format: date-time

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `federation_rule_id: str`

    Tagged ID of the federation rule.

  - `workspace_id: str`

    Tagged ID of the workspace this rule is enabled for.

  - `workspace_name: Optional[str]`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.organization.federation.rules.workspaces.list(
    federation_rule_id="federation_rule_id",
)
page = page.data[0]
print(page.created_by_actor_id)
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
    }
  ],
  "next_page": "next_page"
}
```

### Remove Federation Rule Workspace

`beta.organization.federation.rules.workspaces.remove(workspace_id, **kwargs)  -> WorkspaceRemoveResponse`

**DELETE** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Disable a federation rule for a workspace.

Idempotent; succeeds even if the enablement was already removed. OAuth
callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Parameters

- `federation_rule_id: str`

  ID of the federation rule.

- `workspace_id: str`

  ID of the workspace to disable for.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class WorkspaceRemoveResponse: …`

  - `type: Literal["federation_rule_workspace_deleted"]`

    default: federation_rule_workspace_deleted

  - `federation_rule_id: str`

    Tagged ID of the federation rule.

  - `workspace_id: str`

    Tagged ID of the workspace named in the delete request. Removal is idempotent.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
workspace = client.beta.organization.federation.rules.workspaces.remove(
    workspace_id="workspace_id",
    federation_rule_id="federation_rule_id",
)
print(workspace.federation_rule_id)
```

##### Response (200)

```json
{
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace_deleted",
  "workspace_id": "workspace_id"
}
```

## Beta › Organization › Invites

### Create Invite

`beta.organization.invites.create(**kwargs)  -> BetaOrganizationInvite`

**POST** `/v1/organizations/invites`

Invite a user to join the organization by email.

On plans that draw members from a finite pool of purchased seats, the invite automatically consumes a seat from the lowest tier with availability; there is no seat-tier parameter. When no seat is free the request fails with a 400 error rather than purchasing a seat.

#### Parameters

- `email: str`

  Email of the User.

  format: email

- `role: Literal["billing", "claude_code_user", "developer", 2 more]`

  Role for the invited User.

  The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

  - `"billing"`

  - `"claude_code_user"`

  - `"developer"`

  - `"managed"`

  - `"user"`

- `rbac_group_ids: Optional[Sequence[str]]`

  RBAC group IDs to assign to the User when the Invite is accepted. A non-empty array is accepted only for a Claude Enterprise organization with RBAC groups, and requires the key to carry the `write:rbac_groups` scope.

  maxItems: 100

#### Returns

- `class BetaOrganizationInvite: …`

  - `type: Literal["invite"]`

    Object type.

    For Invites, this is always `"invite"`.

    default: invite

  - `id: str`

    ID of the Invite.

  - `accepted_at: Optional[datetime]`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `email: str`

    Email of the User being invited.

  - `expires_at: datetime`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `invited_at: datetime`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `rbac_group_ids: List[str]`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

  - `status: Literal["accepted", "deleted", "expired", "pending"]`

    Status of the Invite.

    - `"accepted"`

    - `"deleted"`

    - `"expired"`

    - `"pending"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_organization_invite = client.beta.organization.invites.create(
    email="user@emaildomain.com",
    role="user",
)
print(beta_organization_invite.id)
```

##### Response (200)

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "accepted_at": "2019-12-27T18:11:19.117Z",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "rbac_group_ids": [
    "string"
  ],
  "role": "admin",
  "status": "pending",
  "type": "invite"
}
```

### List Invites

`beta.organization.invites.list(**kwargs)  -> SyncPage[BetaOrganizationInvite]`

**GET** `/v1/organizations/invites`

List the organization's invites.

#### Parameters

- `after_id: Optional[str]`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: Optional[str]`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `email: Optional[str]`

  Filter by the email address the Invite was sent to. Matches the same way as the Users list's `email` filter (normalized, case-insensitive).

  format: email

- `limit: Optional[int]`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, maximum: 1000, minimum: 1

- `roles: Optional[Sequence[str]]`

  Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

  Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

- `statuses: Optional[List[Literal["accepted", "expired", "pending"]]]`

  Filter by Invite status. Repeatable; values are OR'ed together. Omit to return `pending`, `accepted`, and `expired` Invites alike.

  - `"accepted"`

  - `"expired"`

  - `"pending"`

#### Returns

- `class BetaOrganizationInvite: …`

  - `type: Literal["invite"]`

    Object type.

    For Invites, this is always `"invite"`.

    default: invite

  - `id: str`

    ID of the Invite.

  - `accepted_at: Optional[datetime]`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `email: str`

    Email of the User being invited.

  - `expires_at: datetime`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `invited_at: datetime`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `rbac_group_ids: List[str]`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

  - `status: Literal["accepted", "deleted", "expired", "pending"]`

    Status of the Invite.

    - `"accepted"`

    - `"deleted"`

    - `"expired"`

    - `"pending"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.organization.invites.list()
page = page.data[0]
print(page.id)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
      "accepted_at": "2019-12-27T18:11:19.117Z",
      "email": "user@emaildomain.com",
      "expires_at": "2024-11-20T23:58:27.427722Z",
      "invited_at": "2024-10-30T23:58:27.427722Z",
      "rbac_group_ids": [
        "string"
      ],
      "role": "admin",
      "status": "pending",
      "type": "invite"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Get Invite

`beta.organization.invites.retrieve(invite_id)  -> BetaOrganizationInvite`

**GET** `/v1/organizations/invites/{invite_id}`

Retrieve an invite by ID.

#### Parameters

- `invite_id: str`

  ID of the Invite.

#### Returns

- `class BetaOrganizationInvite: …`

  - `type: Literal["invite"]`

    Object type.

    For Invites, this is always `"invite"`.

    default: invite

  - `id: str`

    ID of the Invite.

  - `accepted_at: Optional[datetime]`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `email: str`

    Email of the User being invited.

  - `expires_at: datetime`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `invited_at: datetime`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `rbac_group_ids: List[str]`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

  - `status: Literal["accepted", "deleted", "expired", "pending"]`

    Status of the Invite.

    - `"accepted"`

    - `"deleted"`

    - `"expired"`

    - `"pending"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_organization_invite = client.beta.organization.invites.retrieve(
    "invite_id",
)
print(beta_organization_invite.id)
```

##### Response (200)

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "accepted_at": "2019-12-27T18:11:19.117Z",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "rbac_group_ids": [
    "string"
  ],
  "role": "admin",
  "status": "pending",
  "type": "invite"
}
```

### Delete Invite

`beta.organization.invites.delete(invite_id)  -> InviteDeleteResponse`

**DELETE** `/v1/organizations/invites/{invite_id}`

Delete a pending invite.

#### Parameters

- `invite_id: str`

  ID of the Invite.

#### Returns

- `class InviteDeleteResponse: …`

  - `type: Literal["invite_deleted"]`

    Deleted object type.

    For Invites, this is always `"invite_deleted"`.

    default: invite_deleted

  - `id: str`

    ID of the Invite.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
invite = client.beta.organization.invites.delete(
    "invite_id",
)
print(invite.id)
```

##### Response (200)

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "type": "invite_deleted"
}
```

## Beta › Organization › Service Accounts

### Create Service Account

`beta.organization.service_accounts.create(**kwargs)  -> BetaServiceAccount`

**POST** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Create a service account.

A service account is a named workload identity that federation rules
target. `organization_role` is `developer` (default) or `admin`; a rule
may only be created or retargeted to grant `org:admin` scope when the
target's `organization_role` is `admin`. Creating an `admin`-role service
account requires an interactive credential (a user OAuth token or a
Console session) — a workload may only create `developer`-role service
accounts.

#### Parameters

- `name: str`

  Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

  maxLength: 255, minLength: 1

- `description: Optional[str]`

  Optional free-text description.

  maxLength: 2000

- `organization_role: Optional[Literal["admin", "developer"]]`

  Org-level role. Defaults to `developer`.

  - `"admin"`

  - `"developer"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccount: …`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: Literal["service_account"]`

    default: service_account

  - `id: str`

    Tagged ID of the service account.

  - `archived_at: Optional[datetime]`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: datetime`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: Optional[str]`

    Optional free-text description.

  - `name: str`

    Admin-chosen slug identifier.

  - `organization_role: Literal["admin", "developer"]`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `updated_at: datetime`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_service_account = client.beta.organization.service_accounts.create(
    name="ci-deploy-bot",
)
print(beta_service_account.id)
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### List Service Accounts

`beta.organization.service_accounts.list(**kwargs)  -> SyncPageCursor[BetaServiceAccount]`

**GET** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List service accounts in the caller's organization.

Results are ordered by creation time, newest first. Use `limit` and the
`next_page` cursor to paginate; set `include_archived=true` to include
archived service accounts.

#### Parameters

- `include_archived: Optional[bool]`

  Include archived resources. Defaults to false.

  default: false

- `limit: Optional[int]`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: Optional[str]`

  Opaque cursor from a previous response's `next_page`.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccount: …`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: Literal["service_account"]`

    default: service_account

  - `id: str`

    Tagged ID of the service account.

  - `archived_at: Optional[datetime]`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: datetime`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: Optional[str]`

    Optional free-text description.

  - `name: str`

    Admin-chosen slug identifier.

  - `organization_role: Literal["admin", "developer"]`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `updated_at: datetime`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.organization.service_accounts.list()
page = page.data[0]
print(page.id)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "name": "ci-deploy-bot",
      "organization_role": "admin",
      "type": "service_account",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```

### Get Service Account

`beta.organization.service_accounts.retrieve(service_account_id, **kwargs)  -> BetaServiceAccount`

**GET** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a service account by its ID (`svac_...`).

#### Parameters

- `service_account_id: str`

  ID of the service account.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccount: …`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: Literal["service_account"]`

    default: service_account

  - `id: str`

    Tagged ID of the service account.

  - `archived_at: Optional[datetime]`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: datetime`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: Optional[str]`

    Optional free-text description.

  - `name: str`

    Admin-chosen slug identifier.

  - `organization_role: Literal["admin", "developer"]`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `updated_at: datetime`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_service_account = client.beta.organization.service_accounts.retrieve(
    service_account_id="service_account_id",
)
print(beta_service_account.id)
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Update Service Account

`beta.organization.service_accounts.update(service_account_id, **kwargs)  -> BetaServiceAccount`

**POST** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Update a service account.

Only `description` and `organization_role` are mutable; `name` cannot be
changed. Archived service accounts cannot be updated; this returns 400.
Setting `organization_role` to `admin` (even when unchanged) requires an
interactive credential (a user OAuth token or a Console session).

#### Parameters

- `service_account_id: str`

  ID of the service account to update.

- `description: Optional[str]`

  Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

  maxLength: 2000

- `organization_role: Optional[Literal["admin", "developer"]]`

  Replaces the org-level role. Omit or send `null` to leave unchanged.

  - `"admin"`

  - `"developer"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccount: …`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: Literal["service_account"]`

    default: service_account

  - `id: str`

    Tagged ID of the service account.

  - `archived_at: Optional[datetime]`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: datetime`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: Optional[str]`

    Optional free-text description.

  - `name: str`

    Admin-chosen slug identifier.

  - `organization_role: Literal["admin", "developer"]`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `updated_at: datetime`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_service_account = client.beta.organization.service_accounts.update(
    service_account_id="service_account_id",
)
print(beta_service_account.id)
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Archive Service Account

`beta.organization.service_accounts.archive(service_account_id, **kwargs)  -> BetaServiceAccount`

**POST** `/v1/organizations/service_accounts/{service_account_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a service account.

Idempotent; re-archiving returns the service account with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still targets this service account, same as issuer archival; archive
those rules first or change their target to another service account.

#### Parameters

- `service_account_id: str`

  ID of the service account to archive.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccount: …`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: Literal["service_account"]`

    default: service_account

  - `id: str`

    Tagged ID of the service account.

  - `archived_at: Optional[datetime]`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: datetime`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: Optional[str]`

    Optional free-text description.

  - `name: str`

    Admin-chosen slug identifier.

  - `organization_role: Literal["admin", "developer"]`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `"admin"`

    - `"developer"`

  - `updated_at: datetime`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: Optional[str]`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_service_account = client.beta.organization.service_accounts.archive(
    service_account_id="service_account_id",
)
print(beta_service_account.id)
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## Beta › Organization › Service Accounts › Workspaces

### Add Workspace To Service Account

`beta.organization.service_accounts.workspaces.add(service_account_id, **kwargs)  -> BetaServiceAccountWorkspaceMember`

**POST** `/v1/organizations/service_accounts/{service_account_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Add a service account to a workspace with the given `workspace_role`.

Mirror of `POST /workspaces/{workspace_id}/service_accounts`, addressed
from the service-account side; both create the same membership. If the
service account is already an explicit member of the workspace, its
`workspace_role` is replaced with the value supplied here. Archived
workspaces return 400. Archived service accounts cannot be added and are
rejected.

#### Parameters

- `service_account_id: str`

  ID of the service account.

- `workspace_id: str`

  Tagged workspace ID to add the service account to.

- `workspace_role: BetaNoBillingWorkspaceRole`

  Role to assign to the service account in this workspace.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccountWorkspaceMember: …`

  - `type: Literal["service_account_workspace_member"]`

    default: service_account_workspace_member

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: Optional[bool]`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: str`

    Tagged service account ID (`svac_...`).

  - `workspace_id: str`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_service_account_workspace_member = (
    client.beta.organization.service_accounts.workspaces.add(
        service_account_id="service_account_id",
        workspace_id="workspace_id",
        workspace_role="workspace_admin",
    )
)
print(beta_service_account_workspace_member.created_by_actor_id)
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### List Workspaces For Service Account

`beta.organization.service_accounts.workspaces.list(service_account_id, **kwargs)  -> SyncPageCursor[BetaServiceAccountWorkspaceMember]`

**GET** `/v1/organizations/service_accounts/{service_account_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List the workspaces a service account is a member of.

Each entry includes the service account's `workspace_role` in that
workspace. Use `limit` and the `next_page` cursor to paginate. When the
service account has no explicit default-workspace membership, the
implicit (`implicit: true`) membership is returned as the first entry on
the first page; with `limit=1` the first page may return up to 2 entries
(the implicit entry plus one explicit membership) so a pagination cursor
can be derived. Memberships are returned only while
the service account is active. Without a `page` cursor, an archived
service account returns an empty list. A `page` cursor that does not
match an active membership returns a 400 invalid-request error. A cursor
stops matching when the membership is removed, the workspace is deleted,
or the service account is archived. Restart pagination from the first
page to recover.

#### Parameters

- `service_account_id: str`

  ID of the service account.

- `limit: Optional[int]`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: Optional[str]`

  Opaque cursor from a previous response's `next_page`.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccountWorkspaceMember: …`

  - `type: Literal["service_account_workspace_member"]`

    default: service_account_workspace_member

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: Optional[bool]`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: str`

    Tagged service account ID (`svac_...`).

  - `workspace_id: str`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.organization.service_accounts.workspaces.list(
    service_account_id="service_account_id",
)
page = page.data[0]
print(page.created_by_actor_id)
```

##### Response (200)

```json
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
    }
  ],
  "next_page": "next_page"
}
```

### Remove Workspace From Service Account

`beta.organization.service_accounts.workspaces.remove(workspace_id, **kwargs)  -> WorkspaceRemoveResponse`

**DELETE** `/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Mirror of `DELETE /workspaces/{workspace_id}/service_accounts/{service_account_id}`,
addressed from the service-account side. Removal is idempotent (returns
200 even if the membership was already removed). A DELETE against the
implicit default-workspace membership returns 200 but is a no-op and the
membership persists; deleting an explicit default-workspace row reverts
to the implicit `workspace_user` membership. Archived workspaces return
400.

#### Parameters

- `service_account_id: str`

  ID of the service account.

- `workspace_id: str`

  ID of the workspace.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class WorkspaceRemoveResponse: …`

  - `type: Literal["service_account_workspace_member_deleted"]`

    default: service_account_workspace_member_deleted

  - `service_account_id: str`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `workspace_id: str`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
workspace = client.beta.organization.service_accounts.workspaces.remove(
    workspace_id="workspace_id",
    service_account_id="service_account_id",
)
print(workspace.service_account_id)
```

##### Response (200)

```json
{
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
}
```

## Beta › Organization › Users

### List Users

`beta.organization.users.list(**kwargs)  -> SyncPage[BetaOrganizationUser]`

**GET** `/v1/organizations/users`

List the organization's members.

#### Parameters

- `after_id: Optional[str]`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: Optional[str]`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `email: Optional[str]`

  Filter by user email.

  format: email

- `limit: Optional[int]`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, maximum: 1000, minimum: 1

- `roles: Optional[Sequence[str]]`

  Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

  Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

#### Returns

- `class BetaOrganizationUser: …`

  - `type: Literal["user"]`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `id: str`

    ID of the User.

  - `added_at: datetime`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: str`

    Email of the User.

  - `name: str`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.organization.users.list()
page = page.data[0]
print(page.id)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "added_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "name": "Jane Doe",
      "role": "admin",
      "type": "user"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Get User

`beta.organization.users.retrieve(user_id)  -> BetaOrganizationUser`

**GET** `/v1/organizations/users/{user_id}`

Retrieve a member of the organization by user ID.

#### Parameters

- `user_id: str`

  ID of the User.

#### Returns

- `class BetaOrganizationUser: …`

  - `type: Literal["user"]`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `id: str`

    ID of the User.

  - `added_at: datetime`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: str`

    Email of the User.

  - `name: str`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_organization_user = client.beta.organization.users.retrieve(
    "user_id",
)
print(beta_organization_user.id)
```

##### Response (200)

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "admin",
  "type": "user"
}
```

### Update User

`beta.organization.users.update(user_id, **kwargs)  -> BetaOrganizationUser`

**POST** `/v1/organizations/users/{user_id}`

Update a member's organization role.

#### Parameters

- `user_id: str`

  ID of the User.

- `role: Literal["billing", "claude_code_user", "developer", 2 more]`

  New role for the User.

  The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

  - `"billing"`

  - `"claude_code_user"`

  - `"developer"`

  - `"managed"`

  - `"user"`

#### Returns

- `class BetaOrganizationUser: …`

  - `type: Literal["user"]`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `id: str`

    ID of the User.

  - `added_at: datetime`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: str`

    Email of the User.

  - `name: str`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_organization_user = client.beta.organization.users.update(
    user_id="user_id",
    role="user",
)
print(beta_organization_user.id)
```

##### Response (200)

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "admin",
  "type": "user"
}
```

### Remove User

`beta.organization.users.remove(user_id)  -> UserRemoveResponse`

**DELETE** `/v1/organizations/users/{user_id}`

Remove a member from the organization.

#### Parameters

- `user_id: str`

  ID of the User.

#### Returns

- `class UserRemoveResponse: …`

  - `type: Literal["user_deleted"]`

    Deleted object type.

    For Users, this is always `"user_deleted"`.

    default: user_deleted

  - `id: str`

    ID of the User.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
user = client.beta.organization.users.remove(
    "user_id",
)
print(user.id)
```

##### Response (200)

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "type": "user_deleted"
}
```

## Beta › Organization › Workspaces

### List Workspaces

`beta.organization.workspaces.list(**kwargs)  -> SyncPage[BetaWorkspace]`

**GET** `/v1/organizations/workspaces`

List Workspaces

#### Parameters

- `after_id: Optional[str]`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: Optional[str]`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `include_archived: Optional[bool]`

  Whether to include Workspaces that have been archived in the response

  default: false

- `limit: Optional[int]`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, maximum: 1000, minimum: 1

#### Returns

- `class BetaWorkspace: …`

  - `type: Literal["workspace"]`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `id: str`

    ID of the Workspace.

  - `archived_at: Optional[datetime]`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: str`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK
    integration guide for the required key configuration; unless your organization
    is on Claude Platform on AWS, it includes a separate value used during key
    validation. On Claude Platform on AWS there is no separate validation value:
    the key is validated against this Workspace's own value when it is attached, so
    if your key policy uses the compartment condition, add this value to it before
    attaching the key.

  - `created_at: datetime`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Union[List[str], Literal["unrestricted"]]`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `List[str]`

      - `Literal["unrestricted"]`

    - `default_inference_geo: str`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: str`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: str`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: Optional[str]`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
    single-Region key in the same AWS account and Region as the Workspace. On that
    platform the key is validated against this Workspace when it is attached, so a
    key-policy problem is reported as an error on this request. This field is write-once:
    once a key is attached to a Workspace it cannot be detached or replaced. To
    rotate key material, rotate the underlying key on your cloud KMS; the
    `external_key_id` stays the same.

  - `name: str`

    Name of the Workspace.

  - `tags: Dict[str, str]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.organization.workspaces.list()
page = page.data[0]
print(page.id)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "data_residency": {
        "allowed_inference_geos": "unrestricted",
        "default_inference_geo": "default_inference_geo",
        "workspace_geo": "workspace_geo"
      },
      "display_color": "#6C5BB9",
      "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "name": "Workspace Name",
      "tags": {
        "env": "prod",
        "team": "platform"
      },
      "type": "workspace"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Create Workspace

`beta.organization.workspaces.create(**kwargs)  -> BetaWorkspace`

**POST** `/v1/organizations/workspaces`

Create Workspace

#### Parameters

- `name: str`

  Name of the Workspace.

  maxLength: 40, minLength: 1

- `data_residency: Optional[BetaDataResidencyCreateConfigParam]`

  Data residency configuration for the workspace. If omitted, defaults to `workspace_geo: "us"`, `allowed_inference_geos: "unrestricted"`, and `default_inference_geo: "global"`.

  - `allowed_inference_geos: Optional[Union[List[BetaAllowedInferenceGeo], Literal["unrestricted"], null]]`

    Permitted inference geo values. Defaults to 'unrestricted' if omitted, which allows all geos. Use the string 'unrestricted' to allow all geos, or a list of specific geos.

    - `List[BetaAllowedInferenceGeo]`

      - `"global"`

      - `"us"`

    - `Literal["unrestricted"]`

  - `default_inference_geo: Optional[Literal["global", "us"]]`

    Default inference geo applied when requests omit the parameter. Defaults to 'global' if omitted. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

    - `"global"`

    - `"us"`

  - `workspace_geo: Optional[Literal["us"]]`

    Geographic region for workspace data storage. Immutable after creation. Defaults to 'us' if omitted.

- `display_color: Optional[str]`

  Hex color code representing the Workspace in the Anthropic Console.

  maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

- `external_key_id: Optional[str]`

  ID of the customer-managed encryption key (CMEK) configuration to use for this
  Workspace. Setting this field requires CMEK to be enabled for your
  organization. When set, data stored for this Workspace is encrypted with the
  referenced key. Create key configurations with the External Keys API. On
  Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
  single-Region key in the same AWS account and Region as the Workspace. On that
  platform the key is validated against this Workspace when it is attached, so a
  key-policy problem is reported as an error on this request. This field is write-once:
  once a key is attached to a Workspace it cannot be detached or replaced. To
  rotate key material, rotate the underlying key on your cloud KMS; the
  `external_key_id` stays the same.

- `tags: Optional[Dict[str, str]]`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaWorkspace: …`

  - `type: Literal["workspace"]`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `id: str`

    ID of the Workspace.

  - `archived_at: Optional[datetime]`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: str`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK
    integration guide for the required key configuration; unless your organization
    is on Claude Platform on AWS, it includes a separate value used during key
    validation. On Claude Platform on AWS there is no separate validation value:
    the key is validated against this Workspace's own value when it is attached, so
    if your key policy uses the compartment condition, add this value to it before
    attaching the key.

  - `created_at: datetime`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Union[List[str], Literal["unrestricted"]]`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `List[str]`

      - `Literal["unrestricted"]`

    - `default_inference_geo: str`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: str`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: str`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: Optional[str]`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
    single-Region key in the same AWS account and Region as the Workspace. On that
    platform the key is validated against this Workspace when it is attached, so a
    key-policy problem is reported as an error on this request. This field is write-once:
    once a key is attached to a Workspace it cannot be detached or replaced. To
    rotate key material, rotate the underlying key on your cloud KMS; the
    `external_key_id` stays the same.

  - `name: str`

    Name of the Workspace.

  - `tags: Dict[str, str]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_workspace = client.beta.organization.workspaces.create(
    name="x",
)
print(beta_workspace.id)
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

### Get Workspace

`beta.organization.workspaces.retrieve(workspace_id)  -> BetaWorkspace`

**GET** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

#### Parameters

- `workspace_id: str`

  ID of the Workspace.

#### Returns

- `class BetaWorkspace: …`

  - `type: Literal["workspace"]`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `id: str`

    ID of the Workspace.

  - `archived_at: Optional[datetime]`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: str`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK
    integration guide for the required key configuration; unless your organization
    is on Claude Platform on AWS, it includes a separate value used during key
    validation. On Claude Platform on AWS there is no separate validation value:
    the key is validated against this Workspace's own value when it is attached, so
    if your key policy uses the compartment condition, add this value to it before
    attaching the key.

  - `created_at: datetime`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Union[List[str], Literal["unrestricted"]]`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `List[str]`

      - `Literal["unrestricted"]`

    - `default_inference_geo: str`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: str`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: str`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: Optional[str]`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
    single-Region key in the same AWS account and Region as the Workspace. On that
    platform the key is validated against this Workspace when it is attached, so a
    key-policy problem is reported as an error on this request. This field is write-once:
    once a key is attached to a Workspace it cannot be detached or replaced. To
    rotate key material, rotate the underlying key on your cloud KMS; the
    `external_key_id` stays the same.

  - `name: str`

    Name of the Workspace.

  - `tags: Dict[str, str]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_workspace = client.beta.organization.workspaces.retrieve(
    "workspace_id",
)
print(beta_workspace.id)
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

### Update Workspace

`beta.organization.workspaces.update(workspace_id, **kwargs)  -> BetaWorkspace`

**POST** `/v1/organizations/workspaces/{workspace_id}`

Update Workspace

#### Parameters

- `workspace_id: str`

- `data_residency: Optional[BetaDataResidencyUpdateConfigParam]`

  Data residency configuration for the workspace.

  - `allowed_inference_geos: Optional[Union[List[BetaAllowedInferenceGeo], Literal["unrestricted"], null]]`

    Permitted inference geo values. Use 'unrestricted' to allow all geos, or a list of specific geos.

    - `List[BetaAllowedInferenceGeo]`

      - `"global"`

      - `"us"`

    - `Literal["unrestricted"]`

  - `default_inference_geo: Optional[Literal["global", "us"]]`

    Default inference geo applied when requests omit the parameter. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

    - `"global"`

    - `"us"`

- `display_color: Optional[str]`

  Hex color code representing the Workspace in the Anthropic Console.

  maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

- `external_key_id: Optional[str]`

  ID of the customer-managed encryption key (CMEK) configuration to use for this
  Workspace. Setting this field requires CMEK to be enabled for your
  organization. When set, data stored for this Workspace is encrypted with the
  referenced key. Create key configurations with the External Keys API. On
  Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
  single-Region key in the same AWS account and Region as the Workspace. On that
  platform the key is validated against this Workspace when it is attached, so a
  key-policy problem is reported as an error on this request. This field is write-once:
  once a key is attached to a Workspace it cannot be detached or replaced. To
  rotate key material, rotate the underlying key on your cloud KMS; the
  `external_key_id` stays the same.

- `name: Optional[str]`

  Name of the Workspace.

  maxLength: 40, minLength: 1

- `tags: Optional[Dict[str, Optional[str]]]`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Returns

- `class BetaWorkspace: …`

  - `type: Literal["workspace"]`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `id: str`

    ID of the Workspace.

  - `archived_at: Optional[datetime]`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: str`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK
    integration guide for the required key configuration; unless your organization
    is on Claude Platform on AWS, it includes a separate value used during key
    validation. On Claude Platform on AWS there is no separate validation value:
    the key is validated against this Workspace's own value when it is attached, so
    if your key policy uses the compartment condition, add this value to it before
    attaching the key.

  - `created_at: datetime`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Union[List[str], Literal["unrestricted"]]`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `List[str]`

      - `Literal["unrestricted"]`

    - `default_inference_geo: str`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: str`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: str`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: Optional[str]`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
    single-Region key in the same AWS account and Region as the Workspace. On that
    platform the key is validated against this Workspace when it is attached, so a
    key-policy problem is reported as an error on this request. This field is write-once:
    once a key is attached to a Workspace it cannot be detached or replaced. To
    rotate key material, rotate the underlying key on your cloud KMS; the
    `external_key_id` stays the same.

  - `name: str`

    Name of the Workspace.

  - `tags: Dict[str, str]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_workspace = client.beta.organization.workspaces.update(
    workspace_id="workspace_id",
)
print(beta_workspace.id)
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

### Archive Workspace

`beta.organization.workspaces.archive(workspace_id)  -> BetaWorkspace`

**POST** `/v1/organizations/workspaces/{workspace_id}/archive`

Archive Workspace

#### Parameters

- `workspace_id: str`

#### Returns

- `class BetaWorkspace: …`

  - `type: Literal["workspace"]`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `id: str`

    ID of the Workspace.

  - `archived_at: Optional[datetime]`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: str`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK
    integration guide for the required key configuration; unless your organization
    is on Claude Platform on AWS, it includes a separate value used during key
    validation. On Claude Platform on AWS there is no separate validation value:
    the key is validated against this Workspace's own value when it is attached, so
    if your key policy uses the compartment condition, add this value to it before
    attaching the key.

  - `created_at: datetime`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Union[List[str], Literal["unrestricted"]]`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `List[str]`

      - `Literal["unrestricted"]`

    - `default_inference_geo: str`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: str`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: str`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: Optional[str]`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. On
    Claude Platform on AWS the value is the AWS KMS key ARN, and the key must be a
    single-Region key in the same AWS account and Region as the Workspace. On that
    platform the key is validated against this Workspace when it is attached, so a
    key-policy problem is reported as an error on this request. This field is write-once:
    once a key is attached to a Workspace it cannot be detached or replaced. To
    rotate key material, rotate the underlying key on your cloud KMS; the
    `external_key_id` stays the same.

  - `name: str`

    Name of the Workspace.

  - `tags: Dict[str, str]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_workspace = client.beta.organization.workspaces.archive(
    "workspace_id",
)
print(beta_workspace.id)
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

## Beta › Organization › Workspaces › Rate Limits

### List Workspace Rate Limits

`beta.organization.workspaces.rate_limits.list(workspace_id, **kwargs)  -> SyncPageCursor[BetaWorkspaceRateLimit]`

**GET** `/v1/organizations/workspaces/{workspace_id}/rate_limits`

List rate-limit overrides configured for a workspace.

Returns only the groups and limiter types that have a workspace-level
override. Groups without overrides inherit the organization limits and
are not listed; use `GET /v1/organizations/rate_limits` to see those.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `workspace_id: str`

  The ID of the workspace.

- `group_type: Optional[Literal["batch", "files", "model_group", 3 more]]`

  Filter by group type.

  - `"batch"`

  - `"files"`

  - `"model_group"`

  - `"skills"`

  - `"token_count"`

  - `"web_search"`

- `limit: Optional[int]`

  Maximum number of items to return per page. Ranges from `1` to `1000`.

  When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

  maximum: 1000, minimum: 1

- `page: Optional[str]`

  Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaWorkspaceRateLimit: …`

  - `type: Literal["workspace_rate_limit"]`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

    default: workspace_rate_limit

  - `group_type: Literal["batch", "files", "model_group", 3 more]`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `"batch"`

    - `"files"`

    - `"model_group"`

    - `"skills"`

    - `"token_count"`

    - `"web_search"`

  - `limits: List[BetaWorkspaceRateLimitValue]`

    The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

    - `type: str`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `org_limit: Optional[int]`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `value: int`

      The workspace-level override value for this limiter type.

  - `models: Optional[List[str]]`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `rate_limit_id: str`

    The `id` of the RateLimit group this override applies to.

  - `workspace_id: str`

    ID of the Workspace this override applies to.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.organization.workspaces.rate_limits.list(
    workspace_id="workspace_id",
)
page = page.data[0]
print(page.rate_limit_id)
```

##### Response (200)

```json
{
  "data": [
    {
      "group_type": "batch",
      "limits": [
        {
          "org_limit": 0,
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "rate_limit_id": "rate_limit_id",
      "type": "workspace_rate_limit",
      "workspace_id": "workspace_id"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Workspaces › Members

### List Workspace Members

`beta.organization.workspaces.members.list(workspace_id, **kwargs)  -> SyncPage[BetaWorkspaceMember]`

**GET** `/v1/organizations/workspaces/{workspace_id}/members`

List Workspace Members

#### Parameters

- `workspace_id: str`

  ID of the Workspace.

- `after_id: Optional[str]`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: Optional[str]`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit: Optional[int]`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20, maximum: 1000, minimum: 1

#### Returns

- `class BetaWorkspaceMember: …`

  - `type: Literal["workspace_member"]`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `user_id: str`

    ID of the User.

  - `workspace_id: str`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.organization.workspaces.members.list(
    workspace_id="workspace_id",
)
page = page.data[0]
print(page.user_id)
```

##### Response (200)

```json
{
  "data": [
    {
      "type": "workspace_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "workspace_role": "workspace_admin"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Create Workspace Member

`beta.organization.workspaces.members.add(workspace_id, **kwargs)  -> BetaWorkspaceMember`

**POST** `/v1/organizations/workspaces/{workspace_id}/members`

Create Workspace Member

#### Parameters

- `workspace_id: str`

  ID of the Workspace.

- `user_id: str`

  ID of the User.

- `workspace_role: BetaNoBillingWorkspaceRole`

  Role of the new Workspace Member. Cannot be `workspace_billing`.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

#### Returns

- `class BetaWorkspaceMember: …`

  - `type: Literal["workspace_member"]`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `user_id: str`

    ID of the User.

  - `workspace_id: str`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_workspace_member = client.beta.organization.workspaces.members.add(
    workspace_id="workspace_id",
    user_id="user_01WCz1FkmYMm4gnmykNKUu3Q",
    workspace_role="workspace_admin",
)
print(beta_workspace_member.user_id)
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
}
```

### Get Workspace Member

`beta.organization.workspaces.members.retrieve(user_id, **kwargs)  -> BetaWorkspaceMember`

**GET** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Get Workspace Member

#### Parameters

- `workspace_id: str`

  ID of the Workspace.

- `user_id: str`

  ID of the User.

#### Returns

- `class BetaWorkspaceMember: …`

  - `type: Literal["workspace_member"]`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `user_id: str`

    ID of the User.

  - `workspace_id: str`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_workspace_member = client.beta.organization.workspaces.members.retrieve(
    user_id="user_id",
    workspace_id="workspace_id",
)
print(beta_workspace_member.user_id)
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
}
```

### Update Workspace Member

`beta.organization.workspaces.members.update(user_id, **kwargs)  -> BetaWorkspaceMember`

**POST** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Update Workspace Member

#### Parameters

- `workspace_id: str`

  ID of the Workspace.

- `user_id: str`

  ID of the User.

- `workspace_role: BetaWorkspaceRole`

  New workspace role for the User.

  - `"workspace_admin"`

  - `"workspace_billing"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

#### Returns

- `class BetaWorkspaceMember: …`

  - `type: Literal["workspace_member"]`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `user_id: str`

    ID of the User.

  - `workspace_id: str`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_workspace_member = client.beta.organization.workspaces.members.update(
    user_id="user_id",
    workspace_id="workspace_id",
    workspace_role="workspace_admin",
)
print(beta_workspace_member.user_id)
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
}
```

### Delete Workspace Member

`beta.organization.workspaces.members.remove(user_id, **kwargs)  -> MemberRemoveResponse`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Delete Workspace Member

#### Parameters

- `workspace_id: str`

  ID of the Workspace.

- `user_id: str`

  ID of the User.

#### Returns

- `class MemberRemoveResponse: …`

  - `type: Literal["workspace_member_deleted"]`

    Deleted object type.

    For Workspace Members, this is always `"workspace_member_deleted"`.

    default: workspace_member_deleted

  - `user_id: str`

    ID of the User.

  - `workspace_id: str`

    ID of the Workspace.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
member = client.beta.organization.workspaces.members.remove(
    user_id="user_id",
    workspace_id="workspace_id",
)
print(member.user_id)
```

##### Response (200)

```json
{
  "type": "workspace_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## Beta › Organization › Workspaces › Service Accounts

### List Service Account Workspace Members

`beta.organization.workspaces.service_accounts.list(workspace_id, **kwargs)  -> SyncPageCursor[BetaServiceAccountWorkspaceMember]`

**GET** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List the service accounts that are members of a workspace.

Each entry includes the service account's `workspace_role`. Use `limit`
and the `next_page` cursor to paginate. Archived workspaces return 400;
use `GET /service_accounts/{id}/workspaces` to audit memberships of an
archived workspace. The implicit default-workspace membership is not
included in this list. Memberships of archived service accounts are
omitted from the results.

#### Parameters

- `workspace_id: str`

  ID of the workspace.

- `limit: Optional[int]`

  Number of results per page.

  default: 20, maximum: 100, minimum: 1

- `page: Optional[str]`

  Opaque cursor from a previous response's `next_page`.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccountWorkspaceMember: …`

  - `type: Literal["service_account_workspace_member"]`

    default: service_account_workspace_member

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: Optional[bool]`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: str`

    Tagged service account ID (`svac_...`).

  - `workspace_id: str`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.organization.workspaces.service_accounts.list(
    workspace_id="workspace_id",
)
page = page.data[0]
print(page.created_by_actor_id)
```

##### Response (200)

```json
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
    }
  ],
  "next_page": "next_page"
}
```

### Create Service Account Workspace Member

`beta.organization.workspaces.service_accounts.add(workspace_id, **kwargs)  -> BetaServiceAccountWorkspaceMember`

**POST** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Add a service account to a workspace with the given `workspace_role`.

The role determines what the service account can do in the workspace and
which workspace-scoped permissions it can be granted when authenticating
through federation. Every service account is already an implicit
`workspace_user` member of the default workspace; adding it explicitly
assigns a chosen role. If the service account is already an explicit
member of the workspace, its `workspace_role` is replaced with the
value supplied here. Archived workspaces return 400. Archived service
accounts cannot be added and are rejected.

#### Parameters

- `workspace_id: str`

  ID of the workspace.

- `service_account_id: str`

  Tagged service account ID to add.

- `workspace_role: BetaNoBillingWorkspaceRole`

  Role to assign to the service account in this workspace.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccountWorkspaceMember: …`

  - `type: Literal["service_account_workspace_member"]`

    default: service_account_workspace_member

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: Optional[bool]`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: str`

    Tagged service account ID (`svac_...`).

  - `workspace_id: str`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_service_account_workspace_member = (
    client.beta.organization.workspaces.service_accounts.add(
        workspace_id="workspace_id",
        service_account_id="service_account_id",
        workspace_role="workspace_admin",
    )
)
print(beta_service_account_workspace_member.created_by_actor_id)
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### Get Service Account Workspace Member

`beta.organization.workspaces.service_accounts.retrieve(service_account_id, **kwargs)  -> BetaServiceAccountWorkspaceMember`

**GET** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a service account's membership in a workspace.

Returns the membership record, including the service account's
`workspace_role` in this workspace. Archived workspaces return 400. For
the default workspace, returns the implicit (`implicit: true`)
membership when no explicit membership exists; an explicitly added
membership is returned with its assigned role. An archived service
account returns 404.

#### Parameters

- `workspace_id: str`

  ID of the workspace.

- `service_account_id: str`

  ID of the service account.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccountWorkspaceMember: …`

  - `type: Literal["service_account_workspace_member"]`

    default: service_account_workspace_member

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: Optional[bool]`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: str`

    Tagged service account ID (`svac_...`).

  - `workspace_id: str`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_service_account_workspace_member = (
    client.beta.organization.workspaces.service_accounts.retrieve(
        service_account_id="service_account_id",
        workspace_id="workspace_id",
    )
)
print(beta_service_account_workspace_member.created_by_actor_id)
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### Update Service Account Workspace Member

`beta.organization.workspaces.service_accounts.update(service_account_id, **kwargs)  -> BetaServiceAccountWorkspaceMember`

**POST** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Change a service account's role in a workspace.

The new `workspace_role` replaces the current one. Only explicit
memberships can be updated; to set a role on the implicit
default-workspace membership, add the service account explicitly with
`POST /workspaces/{workspace_id}/service_accounts`. Archived workspaces
return 400. Archived service accounts cannot be updated and are
rejected.

#### Parameters

- `workspace_id: str`

  ID of the workspace.

- `service_account_id: str`

  ID of the service account.

- `workspace_role: BetaNoBillingWorkspaceRole`

  New role for the service account in this workspace.

  - `"workspace_admin"`

  - `"workspace_developer"`

  - `"workspace_restricted_developer"`

  - `"workspace_user"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccountWorkspaceMember: …`

  - `type: Literal["service_account_workspace_member"]`

    default: service_account_workspace_member

  - `created_by_actor_id: Optional[str]`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: Optional[bool]`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: str`

    Tagged service account ID (`svac_...`).

  - `workspace_id: str`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `"workspace_admin"`

    - `"workspace_billing"`

    - `"workspace_developer"`

    - `"workspace_restricted_developer"`

    - `"workspace_user"`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_service_account_workspace_member = (
    client.beta.organization.workspaces.service_accounts.update(
        service_account_id="service_account_id",
        workspace_id="workspace_id",
        workspace_role="workspace_admin",
    )
)
print(beta_service_account_workspace_member.created_by_actor_id)
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### Delete Service Account Workspace Member

`beta.organization.workspaces.service_accounts.remove(service_account_id, **kwargs)  -> ServiceAccountRemoveResponse`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Removal is idempotent (returns 200 even if the membership was already
removed). A DELETE against the implicit default-workspace membership
returns 200 but is a no-op and the membership persists; deleting an
explicit default-workspace row reverts to the implicit `workspace_user`
membership. Archived workspaces return 400.

#### Parameters

- `workspace_id: str`

  ID of the workspace.

- `service_account_id: str`

  ID of the service account.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

    - `"user-profiles-2026-09-04"`

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

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class ServiceAccountRemoveResponse: …`

  - `type: Literal["service_account_workspace_member_deleted"]`

    default: service_account_workspace_member_deleted

  - `service_account_id: str`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `workspace_id: str`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
service_account = client.beta.organization.workspaces.service_accounts.remove(
    service_account_id="service_account_id",
    workspace_id="workspace_id",
)
print(service_account.service_account_id)
```

##### Response (200)

```json
{
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
}
```

## Beta › Organization › Rate Limits

### List Organization Rate Limits

`beta.organization.rate_limits.list(**kwargs)  -> SyncPageCursor[BetaOrganizationRateLimit]`

**GET** `/v1/organizations/rate_limits`

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `group_type: Optional[Literal["batch", "files", "model_group", 3 more]]`

  Filter by group type.

  - `"batch"`

  - `"files"`

  - `"model_group"`

  - `"skills"`

  - `"token_count"`

  - `"web_search"`

- `limit: Optional[int]`

  Maximum number of items to return per page. Ranges from `1` to `1000`.

  When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

  maximum: 1000, minimum: 1

- `model: Optional[str]`

  Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

- `page: Optional[str]`

  Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaOrganizationRateLimit: …`

  - `type: Literal["rate_limit"]`

    Object type. Always `rate_limit` for organization rate-limit entries.

    default: rate_limit

  - `id: str`

    Stable identifier for this rate-limit group within the organization.

  - `group_type: Literal["batch", "files", "model_group", 3 more]`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `"batch"`

    - `"files"`

    - `"model_group"`

    - `"skills"`

    - `"token_count"`

    - `"web_search"`

  - `limits: List[BetaOrganizationRateLimitValue]`

    The limiter values that apply to this group.

    - `type: str`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `value: int`

      The configured limit value for this limiter type.

  - `models: Optional[List[str]]`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.organization.rate_limits.list()
page = page.data[0]
print(page.id)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "group_type": "batch",
      "limits": [
        {
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "type": "rate_limit"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Compliance Settings

### Get Compliance Settings

`beta.organization.compliance_settings.retrieve()  -> BetaComplianceSettings`

**GET** `/v1/organizations/compliance_settings`

Retrieve your organization's Compliance Settings.

Compliance Settings is a singleton resource: there is exactly one per
organization, addressed without an identifier. The `state` field reflects
whether the Compliance API is enabled. An organization with a parent
organization reads the state inherited from the parent's configuration.

#### Returns

- `class BetaComplianceSettings: …`

  - `type: Literal["compliance_settings"]`

    default: compliance_settings

  - `state: BetaComplianceSettingsState`

    Whether the Compliance API is enabled for this organization.

    - `class BetaComplianceSettingsStateEnabled: …`

      - `type: Literal["enabled"]`

        default: enabled

    - `class BetaComplianceSettingsStateDisabled: …`

      - `type: Literal["disabled"]`

        default: disabled

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_compliance_settings = client.beta.organization.compliance_settings.retrieve()
print(beta_compliance_settings.state)
```

##### Response (200)

```json
{
  "state": {
    "type": "enabled"
  },
  "type": "compliance_settings"
}
```

### Update Compliance Settings

`beta.organization.compliance_settings.update(**kwargs)  -> BetaComplianceSettings`

**POST** `/v1/organizations/compliance_settings`

Update your organization's Compliance Settings.

Setting `state` to `enabled` turns on the Compliance API and begins
capturing organization activity events. Setting it to `disabled` turns
both off. `state` reflects whether the Compliance API is enabled.

A request that sets `state` to its current value succeeds and leaves the
resource unchanged. A `disabled` request stays in effect until a later
`enabled` request or the organization's next provisioning action that
enables Access Transparency: enabling Access Transparency also enables
the Compliance API, which serves its activity events, so such
provisioning (including re-runs) re-enables the Compliance API even
after a `disabled` request. Automated provisioning never disables
compliance settings.

#### Parameters

- `state: BetaComplianceSettingsStateParam`

  Desired state. Accepts the string shorthand "enabled" or "disabled" in place of the object form; the response always returns the canonical object form.

  - `class BetaComplianceSettingsStateEnabledParam: …`

    - `type: Literal["enabled"]`

  - `class BetaComplianceSettingsStateDisabledParam: …`

    - `type: Literal["disabled"]`

#### Returns

- `class BetaComplianceSettings: …`

  - `type: Literal["compliance_settings"]`

    default: compliance_settings

  - `state: BetaComplianceSettingsState`

    Whether the Compliance API is enabled for this organization.

    - `class BetaComplianceSettingsStateEnabled: …`

      - `type: Literal["enabled"]`

        default: enabled

    - `class BetaComplianceSettingsStateDisabled: …`

      - `type: Literal["disabled"]`

        default: disabled

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_compliance_settings = client.beta.organization.compliance_settings.update(
    state={"type": "enabled"},
)
print(beta_compliance_settings.state)
```

##### Response (200)

```json
{
  "state": {
    "type": "enabled"
  },
  "type": "compliance_settings"
}
```
