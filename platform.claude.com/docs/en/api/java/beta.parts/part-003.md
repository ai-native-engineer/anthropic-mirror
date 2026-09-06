<!-- source: https://platform.claude.com/docs/en/api/java/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/java/beta -->

<!-- chunk-start -->

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `Optional<Attributes> attributes`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `LocalDateTime createdAt`

    When this rule was created.

    format: date-time

  - `Optional<String> createdByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `Optional<String> description`

    Optional free-text description.

  - `String issuerId`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `Optional<String> issuerName`

    Issuer's display name at read time.

  - `BetaFederationRuleMatch match`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `Optional<String> audience`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `Optional<Claims> claims`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `Optional<String> condition`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `Optional<String> subjectPrefix`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `String name`

    Admin-chosen slug identifier.

  - `String oauthScope`

    Space-separated OAuth scopes granted on the minted token.

  - `BetaServiceAccountTarget target`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `String serviceAccountId`

      Tagged ID of the service account to mint tokens for.

    - `JsonValue type = "service_account"`

    - `Optional<String> serviceAccountName`

      Service account's display name at read time. Ignored on writes.

  - `long tokenLifetimeSeconds`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `JsonValue type = "federation_rule"`

  - `LocalDateTime updatedAt`

    When this rule was last updated.

    format: date-time

  - `Optional<String> updatedByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `Optional<String> workspaceId`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `List<String> workspaceIds`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.federation.rules.BetaFederationRule;
import com.anthropic.models.beta.organization.federation.rules.RuleUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaFederationRule betaFederationRule = client.beta().organization().federation().rules().update("federation_rule_id");
    }
}
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

`BetaFederationRule beta().organization().federation().rules().archive(params = RuleArchiveParams.none(), requestOptions = RequestOptions.none())`

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

- `RuleArchiveParams params`

  - `Optional<String> federationRuleId`

    ID of the federation rule to archive.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationRule:`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `String id`

    Tagged ID of the federation rule.

  - `boolean appliesToAllWorkspaces`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `Optional<LocalDateTime> archivedAt`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `Optional<String> archivedByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `Optional<Attributes> attributes`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `LocalDateTime createdAt`

    When this rule was created.

    format: date-time

  - `Optional<String> createdByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `Optional<String> description`

    Optional free-text description.

  - `String issuerId`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `Optional<String> issuerName`

    Issuer's display name at read time.

  - `BetaFederationRuleMatch match`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `Optional<String> audience`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `Optional<Claims> claims`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `Optional<String> condition`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `Optional<String> subjectPrefix`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `String name`

    Admin-chosen slug identifier.

  - `String oauthScope`

    Space-separated OAuth scopes granted on the minted token.

  - `BetaServiceAccountTarget target`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `String serviceAccountId`

      Tagged ID of the service account to mint tokens for.

    - `JsonValue type = "service_account"`

    - `Optional<String> serviceAccountName`

      Service account's display name at read time. Ignored on writes.

  - `long tokenLifetimeSeconds`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `JsonValue type = "federation_rule"`

  - `LocalDateTime updatedAt`

    When this rule was last updated.

    format: date-time

  - `Optional<String> updatedByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `Optional<String> workspaceId`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `List<String> workspaceIds`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.federation.rules.BetaFederationRule;
import com.anthropic.models.beta.organization.federation.rules.RuleArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaFederationRule betaFederationRule = client.beta().organization().federation().rules().archive("federation_rule_id");
    }
}
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

`BetaFederationRuleWorkspace beta().organization().federation().rules().workspaces().add(params, requestOptions = RequestOptions.none())`

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

- `WorkspaceAddParams params`

  - `Optional<String> federationRuleId`

    ID of the federation rule.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

  - `String workspaceId`

    Tagged ID of the workspace to enable this rule for.

#### Returns

- `class BetaFederationRuleWorkspace:`

  - `LocalDateTime createdAt`

    When this workspace was enabled for the rule.

    format: date-time

  - `Optional<String> createdByActorId`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `String federationRuleId`

    Tagged ID of the federation rule.

  - `JsonValue type = "federation_rule_workspace"`

  - `String workspaceId`

    Tagged ID of the workspace this rule is enabled for.

  - `Optional<String> workspaceName`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.federation.rules.BetaFederationRuleWorkspace;
import com.anthropic.models.beta.organization.federation.rules.workspaces.WorkspaceAddParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkspaceAddParams params = WorkspaceAddParams.builder()
            .federationRuleId("federation_rule_id")
            .workspaceId("workspace_id")
            .build();
        BetaFederationRuleWorkspace betaFederationRuleWorkspace = client.beta().organization().federation().rules().workspaces().add(params);
    }
}
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

`WorkspaceListPage beta().organization().federation().rules().workspaces().list(params = WorkspaceListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List workspaces where this federation rule is enabled.

Returns all workspace enablements in a single response; the `limit` and
`page` parameters are accepted but have no effect, and `next_page` is
always `null`. Returns explicit per-workspace enablements only; for
rules with `applies_to_all_workspaces` or a legacy single
`workspace_id`, check those fields on the rule itself.

#### Parameters

- `WorkspaceListParams params`

  - `Optional<String> federationRuleId`

    ID of the federation rule.

  - `Optional<Long> limit`

    Number of results per page.

    maximum: 100, minimum: 1

  - `Optional<String> page`

    Opaque cursor from a previous response's `next_page`.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationRuleWorkspace:`

  - `LocalDateTime createdAt`

    When this workspace was enabled for the rule.

    format: date-time

  - `Optional<String> createdByActorId`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `String federationRuleId`

    Tagged ID of the federation rule.

  - `JsonValue type = "federation_rule_workspace"`

  - `String workspaceId`

    Tagged ID of the workspace this rule is enabled for.

  - `Optional<String> workspaceName`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.federation.rules.workspaces.WorkspaceListPage;
import com.anthropic.models.beta.organization.federation.rules.workspaces.WorkspaceListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkspaceListPage page = client.beta().organization().federation().rules().workspaces().list("federation_rule_id");
    }
}
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

`WorkspaceRemoveResponse beta().organization().federation().rules().workspaces().remove(params, requestOptions = RequestOptions.none())`

**DELETE** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Disable a federation rule for a workspace.

Idempotent; succeeds even if the enablement was already removed. OAuth
callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Parameters

- `WorkspaceRemoveParams params`

  - `String federationRuleId`

    ID of the federation rule.

  - `Optional<String> workspaceId`

    ID of the workspace to disable for.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class WorkspaceRemoveResponse:`

  - `String federationRuleId`

    Tagged ID of the federation rule.

  - `JsonValue type = "federation_rule_workspace_deleted"`

  - `String workspaceId`

    Tagged ID of the workspace named in the delete request. Removal is idempotent.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.federation.rules.workspaces.WorkspaceRemoveParams;
import com.anthropic.models.beta.organization.federation.rules.workspaces.WorkspaceRemoveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkspaceRemoveParams params = WorkspaceRemoveParams.builder()
            .federationRuleId("federation_rule_id")
            .workspaceId("workspace_id")
            .build();
        WorkspaceRemoveResponse workspace = client.beta().organization().federation().rules().workspaces().remove(params);
    }
}
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

`BetaOrganizationInvite beta().organization().invites().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/organizations/invites`

Invite a user to join the organization by email.

On plans that draw members from a finite pool of purchased seats, the invite automatically consumes a seat from the lowest tier with availability; there is no seat-tier parameter. When no seat is free the request fails with a 400 error rather than purchasing a seat.

#### Parameters

- `InviteCreateParams params`

  - `String email`

    Email of the User.

    format: email

  - `Role role`

    Role for the invited User.

    The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

    - `BILLING("billing")`

    - `CLAUDE_CODE_USER("claude_code_user")`

    - `DEVELOPER("developer")`

    - `MANAGED("managed")`

    - `USER("user")`

  - `Optional<List<String>> rbacGroupIds`

    RBAC group IDs to assign to the User when the Invite is accepted. A non-empty array is accepted only for a Claude Enterprise organization with RBAC groups, and requires the key to carry the `write:rbac_groups` scope.

    maxItems: 100

#### Returns

- `class BetaOrganizationInvite:`

  - `String id`

    ID of the Invite.

  - `Optional<LocalDateTime> acceptedAt`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `String email`

    Email of the User being invited.

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `LocalDateTime invitedAt`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `List<String> rbacGroupIds`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `BetaOrganizationRole role`

    Organization role of the User.

    - `ADMIN("admin")`

    - `BILLING("billing")`

    - `CLAUDE_CODE_USER("claude_code_user")`

    - `DEVELOPER("developer")`

    - `MANAGED("managed")`

    - `MEMBERSHIP_ADMIN("membership_admin")`

    - `OWNER("owner")`

    - `PRIMARY_OWNER("primary_owner")`

    - `USER("user")`

  - `Status status`

    Status of the Invite.

    - `ACCEPTED("accepted")`

    - `DELETED("deleted")`

    - `EXPIRED("expired")`

    - `PENDING("pending")`

  - `JsonValue type = "invite"`

    Object type.

    For Invites, this is always `"invite"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.invites.BetaOrganizationInvite;
import com.anthropic.models.beta.organization.invites.InviteCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        InviteCreateParams params = InviteCreateParams.builder()
            .email("user@emaildomain.com")
            .role(InviteCreateParams.Role.USER)
            .build();
        BetaOrganizationInvite betaOrganizationInvite = client.beta().organization().invites().create(params);
    }
}
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

`InviteListPage beta().organization().invites().list(params = InviteListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/invites`

List the organization's invites.

#### Parameters

- `InviteListParams params`

  - `Optional<String> afterId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `Optional<String> beforeId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Optional<String> email`

    Filter by the email address the Invite was sent to. Matches the same way as the Users list's `email` filter (normalized, case-insensitive).

    format: email

  - `Optional<Long> limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `Optional<List<String>> roles`

    Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

    Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

  - `Optional<List<Status>> statuses`

    Filter by Invite status. Repeatable; values are OR'ed together. Omit to return `pending`, `accepted`, and `expired` Invites alike.

    - `ACCEPTED("accepted")`

    - `EXPIRED("expired")`

    - `PENDING("pending")`

#### Returns

- `class BetaOrganizationInvite:`

  - `String id`

    ID of the Invite.

  - `Optional<LocalDateTime> acceptedAt`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `String email`

    Email of the User being invited.

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `LocalDateTime invitedAt`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `List<String> rbacGroupIds`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `BetaOrganizationRole role`

    Organization role of the User.

    - `ADMIN("admin")`

    - `BILLING("billing")`

    - `CLAUDE_CODE_USER("claude_code_user")`

    - `DEVELOPER("developer")`

    - `MANAGED("managed")`

    - `MEMBERSHIP_ADMIN("membership_admin")`

    - `OWNER("owner")`

    - `PRIMARY_OWNER("primary_owner")`

    - `USER("user")`

  - `Status status`

    Status of the Invite.

    - `ACCEPTED("accepted")`

    - `DELETED("deleted")`

    - `EXPIRED("expired")`

    - `PENDING("pending")`

  - `JsonValue type = "invite"`

    Object type.

    For Invites, this is always `"invite"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.invites.InviteListPage;
import com.anthropic.models.beta.organization.invites.InviteListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        InviteListPage page = client.beta().organization().invites().list();
    }
}
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

`BetaOrganizationInvite beta().organization().invites().retrieve(params = InviteRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/invites/{invite_id}`

Retrieve an invite by ID.

#### Parameters

- `InviteRetrieveParams params`

  - `Optional<String> inviteId`

    ID of the Invite.

#### Returns

- `class BetaOrganizationInvite:`

  - `String id`

    ID of the Invite.

  - `Optional<LocalDateTime> acceptedAt`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `String email`

    Email of the User being invited.

  - `LocalDateTime expiresAt`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `LocalDateTime invitedAt`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `List<String> rbacGroupIds`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `BetaOrganizationRole role`

    Organization role of the User.

    - `ADMIN("admin")`

    - `BILLING("billing")`

    - `CLAUDE_CODE_USER("claude_code_user")`

    - `DEVELOPER("developer")`

    - `MANAGED("managed")`

    - `MEMBERSHIP_ADMIN("membership_admin")`

    - `OWNER("owner")`

    - `PRIMARY_OWNER("primary_owner")`

    - `USER("user")`

  - `Status status`

    Status of the Invite.

    - `ACCEPTED("accepted")`

    - `DELETED("deleted")`

    - `EXPIRED("expired")`

    - `PENDING("pending")`

  - `JsonValue type = "invite"`

    Object type.

    For Invites, this is always `"invite"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.invites.BetaOrganizationInvite;
import com.anthropic.models.beta.organization.invites.InviteRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaOrganizationInvite betaOrganizationInvite = client.beta().organization().invites().retrieve("invite_id");
    }
}
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

`InviteDeleteResponse beta().organization().invites().delete(params = InviteDeleteParams.none(), requestOptions = RequestOptions.none())`

**DELETE** `/v1/organizations/invites/{invite_id}`

Delete a pending invite.

#### Parameters

- `InviteDeleteParams params`

  - `Optional<String> inviteId`

    ID of the Invite.

#### Returns

- `class InviteDeleteResponse:`

  - `String id`

    ID of the Invite.

  - `JsonValue type = "invite_deleted"`

    Deleted object type.

    For Invites, this is always `"invite_deleted"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.invites.InviteDeleteParams;
import com.anthropic.models.beta.organization.invites.InviteDeleteResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        InviteDeleteResponse invite = client.beta().organization().invites().delete("invite_id");
    }
}
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

`BetaServiceAccount beta().organization().serviceAccounts().create(params, requestOptions = RequestOptions.none())`

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

- `ServiceAccountCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

  - `String name`

    Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

    maxLength: 255, minLength: 1

  - `Optional<String> description`

    Optional free-text description.

    maxLength: 2000

  - `Optional<OrganizationRole> organizationRole`

    Org-level role. Defaults to `developer`.

    - `ADMIN("admin")`

    - `DEVELOPER("developer")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `String id`

    Tagged ID of the service account.

  - `Optional<LocalDateTime> archivedAt`

    If set, this service account is archived.

    format: date-time

  - `Optional<String> archivedByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `LocalDateTime createdAt`

    When this service account was created.

    format: date-time

  - `Optional<String> createdByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `Optional<String> description`

    Optional free-text description.

  - `String name`

    Admin-chosen slug identifier.

  - `OrganizationRole organizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `ADMIN("admin")`

    - `DEVELOPER("developer")`

  - `JsonValue type = "service_account"`

  - `LocalDateTime updatedAt`

    When this service account was last updated.

    format: date-time

  - `Optional<String> updatedByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.serviceaccounts.BetaServiceAccount;
import com.anthropic.models.beta.organization.serviceaccounts.ServiceAccountCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ServiceAccountCreateParams params = ServiceAccountCreateParams.builder()
            .name("ci-deploy-bot")
            .build();
        BetaServiceAccount betaServiceAccount = client.beta().organization().serviceAccounts().create(params);
    }
}
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

`ServiceAccountListPage beta().organization().serviceAccounts().list(params = ServiceAccountListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List service accounts in the caller's organization.

Results are ordered by creation time, newest first. Use `limit` and the
`next_page` cursor to paginate; set `include_archived=true` to include
archived service accounts.

#### Parameters

- `ServiceAccountListParams params`

  - `Optional<Boolean> includeArchived`

    Include archived resources. Defaults to false.

  - `Optional<Long> limit`

    Number of results per page.

    maximum: 100, minimum: 1

  - `Optional<String> page`

    Opaque cursor from a previous response's `next_page`.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `String id`

    Tagged ID of the service account.

  - `Optional<LocalDateTime> archivedAt`

    If set, this service account is archived.

    format: date-time

  - `Optional<String> archivedByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `LocalDateTime createdAt`

    When this service account was created.

    format: date-time

  - `Optional<String> createdByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `Optional<String> description`

    Optional free-text description.

  - `String name`

    Admin-chosen slug identifier.

  - `OrganizationRole organizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `ADMIN("admin")`

    - `DEVELOPER("developer")`

  - `JsonValue type = "service_account"`

  - `LocalDateTime updatedAt`

    When this service account was last updated.

    format: date-time

  - `Optional<String> updatedByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.serviceaccounts.ServiceAccountListPage;
import com.anthropic.models.beta.organization.serviceaccounts.ServiceAccountListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ServiceAccountListPage page = client.beta().organization().serviceAccounts().list();
    }
}
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

`BetaServiceAccount beta().organization().serviceAccounts().retrieve(params = ServiceAccountRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a service account by its ID (`svac_...`).

#### Parameters

- `ServiceAccountRetrieveParams params`

  - `Optional<String> serviceAccountId`

    ID of the service account.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `String id`

    Tagged ID of the service account.

  - `Optional<LocalDateTime> archivedAt`

    If set, this service account is archived.

    format: date-time

  - `Optional<String> archivedByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `LocalDateTime createdAt`

    When this service account was created.

    format: date-time

  - `Optional<String> createdByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `Optional<String> description`

    Optional free-text description.

  - `String name`

    Admin-chosen slug identifier.

  - `OrganizationRole organizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `ADMIN("admin")`

    - `DEVELOPER("developer")`

  - `JsonValue type = "service_account"`

  - `LocalDateTime updatedAt`

    When this service account was last updated.

    format: date-time

  - `Optional<String> updatedByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.serviceaccounts.BetaServiceAccount;
import com.anthropic.models.beta.organization.serviceaccounts.ServiceAccountRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaServiceAccount betaServiceAccount = client.beta().organization().serviceAccounts().retrieve("service_account_id");
    }
}
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

`BetaServiceAccount beta().organization().serviceAccounts().update(params = ServiceAccountUpdateParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Update a service account.

Only `description` and `organization_role` are mutable; `name` cannot be
changed. Archived service accounts cannot be updated; this returns 400.
Setting `organization_role` to `admin` (even when unchanged) requires an
interactive credential (a user OAuth token or a Console session).

#### Parameters

- `ServiceAccountUpdateParams params`

  - `Optional<String> serviceAccountId`

    ID of the service account to update.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

  - `Optional<String> description`

    Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

    maxLength: 2000

  - `Optional<OrganizationRole> organizationRole`

    Replaces the org-level role. Omit or send `null` to leave unchanged.

    - `ADMIN("admin")`

    - `DEVELOPER("developer")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `String id`

    Tagged ID of the service account.

  - `Optional<LocalDateTime> archivedAt`

    If set, this service account is archived.

    format: date-time

  - `Optional<String> archivedByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `LocalDateTime createdAt`

    When this service account was created.

    format: date-time

  - `Optional<String> createdByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `Optional<String> description`

    Optional free-text description.

  - `String name`

    Admin-chosen slug identifier.

  - `OrganizationRole organizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `ADMIN("admin")`

    - `DEVELOPER("developer")`

  - `JsonValue type = "service_account"`

  - `LocalDateTime updatedAt`

    When this service account was last updated.

    format: date-time

  - `Optional<String> updatedByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.serviceaccounts.BetaServiceAccount;
import com.anthropic.models.beta.organization.serviceaccounts.ServiceAccountUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaServiceAccount betaServiceAccount = client.beta().organization().serviceAccounts().update("service_account_id");
    }
}
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

`BetaServiceAccount beta().organization().serviceAccounts().archive(params = ServiceAccountArchiveParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/organizations/service_accounts/{service_account_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a service account.

Idempotent; re-archiving returns the service account with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still targets this service account, same as issuer archival; archive
those rules first or change their target to another service account.

#### Parameters

- `ServiceAccountArchiveParams params`

  - `Optional<String> serviceAccountId`

    ID of the service account to archive.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `String id`

    Tagged ID of the service account.

  - `Optional<LocalDateTime> archivedAt`

    If set, this service account is archived.

    format: date-time

  - `Optional<String> archivedByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `LocalDateTime createdAt`

    When this service account was created.

    format: date-time

  - `Optional<String> createdByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `Optional<String> description`

    Optional free-text description.

  - `String name`

    Admin-chosen slug identifier.

  - `OrganizationRole organizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `ADMIN("admin")`

    - `DEVELOPER("developer")`

  - `JsonValue type = "service_account"`

  - `LocalDateTime updatedAt`

    When this service account was last updated.

    format: date-time

  - `Optional<String> updatedByActorId`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.serviceaccounts.BetaServiceAccount;
import com.anthropic.models.beta.organization.serviceaccounts.ServiceAccountArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaServiceAccount betaServiceAccount = client.beta().organization().serviceAccounts().archive("service_account_id");
    }
}
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

`BetaServiceAccountWorkspaceMember beta().organization().serviceAccounts().workspaces().add(params, requestOptions = RequestOptions.none())`

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

- `WorkspaceAddParams params`

  - `Optional<String> serviceAccountId`

    ID of the service account.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

  - `String workspaceId`

    Tagged workspace ID to add the service account to.

  - `BetaNoBillingWorkspaceRole workspaceRole`

    Role to assign to the service account in this workspace.

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `Optional<String> createdByActorId`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `Optional<Boolean> implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `String serviceAccountId`

    Tagged service account ID (`svac_...`).

  - `JsonValue type = "service_account_workspace_member"`

  - `String workspaceId`

    Tagged workspace ID (`wrkspc_...`).

  - `BetaWorkspaceRole workspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WORKSPACE_ADMIN("workspace_admin")`

    - `WORKSPACE_BILLING("workspace_billing")`

    - `WORKSPACE_DEVELOPER("workspace_developer")`

    - `WORKSPACE_RESTRICTED_DEVELOPER("workspace_restricted_developer")`

    - `WORKSPACE_USER("workspace_user")`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.serviceaccounts.BetaServiceAccountWorkspaceMember;
import com.anthropic.models.beta.organization.serviceaccounts.workspaces.WorkspaceAddParams;
import com.anthropic.models.beta.organization.workspaces.BetaNoBillingWorkspaceRole;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkspaceAddParams params = WorkspaceAddParams.builder()
            .serviceAccountId("service_account_id")
            .workspaceId("workspace_id")
            .workspaceRole(BetaNoBillingWorkspaceRole.WORKSPACE_ADMIN)
            .build();
        BetaServiceAccountWorkspaceMember betaServiceAccountWorkspaceMember = client.beta().organization().serviceAccounts().workspaces().add(params);
    }
}
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

`WorkspaceListPage beta().organization().serviceAccounts().workspaces().list(params = WorkspaceListParams.none(), requestOptions = RequestOptions.none())`

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

- `WorkspaceListParams params`

  - `Optional<String> serviceAccountId`

    ID of the service account.

  - `Optional<Long> limit`

    Number of results per page.

    maximum: 100, minimum: 1

  - `Optional<String> page`

    Opaque cursor from a previous response's `next_page`.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `Optional<String> createdByActorId`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `Optional<Boolean> implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `String serviceAccountId`

    Tagged service account ID (`svac_...`).

  - `JsonValue type = "service_account_workspace_member"`

  - `String workspaceId`

    Tagged workspace ID (`wrkspc_...`).

  - `BetaWorkspaceRole workspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WORKSPACE_ADMIN("workspace_admin")`

    - `WORKSPACE_BILLING("workspace_billing")`

    - `WORKSPACE_DEVELOPER("workspace_developer")`

    - `WORKSPACE_RESTRICTED_DEVELOPER("workspace_restricted_developer")`

    - `WORKSPACE_USER("workspace_user")`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.serviceaccounts.workspaces.WorkspaceListPage;
import com.anthropic.models.beta.organization.serviceaccounts.workspaces.WorkspaceListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkspaceListPage page = client.beta().organization().serviceAccounts().workspaces().list("service_account_id");
    }
}
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

`WorkspaceRemoveResponse beta().organization().serviceAccounts().workspaces().remove(params, requestOptions = RequestOptions.none())`

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

- `WorkspaceRemoveParams params`

  - `String serviceAccountId`

    ID of the service account.

  - `Optional<String> workspaceId`

    ID of the workspace.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class WorkspaceRemoveResponse:`

  - `String serviceAccountId`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `JsonValue type = "service_account_workspace_member_deleted"`

  - `String workspaceId`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.serviceaccounts.workspaces.WorkspaceRemoveParams;
import com.anthropic.models.beta.organization.serviceaccounts.workspaces.WorkspaceRemoveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkspaceRemoveParams params = WorkspaceRemoveParams.builder()
            .serviceAccountId("service_account_id")
            .workspaceId("workspace_id")
            .build();
        WorkspaceRemoveResponse workspace = client.beta().organization().serviceAccounts().workspaces().remove(params);
    }
}
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

`UserListPage beta().organization().users().list(params = UserListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/users`

List the organization's members.

#### Parameters

- `UserListParams params`

  - `Optional<String> afterId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `Optional<String> beforeId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Optional<String> email`

    Filter by user email.

    format: email

  - `Optional<Long> limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `Optional<List<String>> roles`

    Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

    Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

#### Returns

- `class BetaOrganizationUser:`

  - `String id`

    ID of the User.

  - `LocalDateTime addedAt`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `String email`

    Email of the User.

  - `String name`

    Name of the User.

  - `BetaOrganizationRole role`

    Organization role of the User.

    - `ADMIN("admin")`

    - `BILLING("billing")`

    - `CLAUDE_CODE_USER("claude_code_user")`

    - `DEVELOPER("developer")`

    - `MANAGED("managed")`

    - `MEMBERSHIP_ADMIN("membership_admin")`

    - `OWNER("owner")`

    - `PRIMARY_OWNER("primary_owner")`

    - `USER("user")`

  - `JsonValue type = "user"`

    Object type.

    For Users, this is always `"user"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.users.UserListPage;
import com.anthropic.models.beta.organization.users.UserListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        UserListPage page = client.beta().organization().users().list();
    }
}
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

`BetaOrganizationUser beta().organization().users().retrieve(params = UserRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/users/{user_id}`

Retrieve a member of the organization by user ID.

#### Parameters

- `UserRetrieveParams params`

  - `Optional<String> userId`

    ID of the User.

#### Returns

- `class BetaOrganizationUser:`

  - `String id`

    ID of the User.

  - `LocalDateTime addedAt`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `String email`

    Email of the User.

  - `String name`

    Name of the User.

  - `BetaOrganizationRole role`

    Organization role of the User.

    - `ADMIN("admin")`

    - `BILLING("billing")`

    - `CLAUDE_CODE_USER("claude_code_user")`

    - `DEVELOPER("developer")`

    - `MANAGED("managed")`

    - `MEMBERSHIP_ADMIN("membership_admin")`

    - `OWNER("owner")`

    - `PRIMARY_OWNER("primary_owner")`

    - `USER("user")`

  - `JsonValue type = "user"`

    Object type.

    For Users, this is always `"user"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.users.BetaOrganizationUser;
import com.anthropic.models.beta.organization.users.UserRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaOrganizationUser betaOrganizationUser = client.beta().organization().users().retrieve("user_id");
    }
}
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

`BetaOrganizationUser beta().organization().users().update(params, requestOptions = RequestOptions.none())`

**POST** `/v1/organizations/users/{user_id}`

Update a member's organization role.

#### Parameters

- `UserUpdateParams params`

  - `Optional<String> userId`

    ID of the User.

  - `Role role`

    New role for the User.

    The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

    - `BILLING("billing")`

    - `CLAUDE_CODE_USER("claude_code_user")`

    - `DEVELOPER("developer")`

    - `MANAGED("managed")`

    - `USER("user")`

#### Returns

- `class BetaOrganizationUser:`

  - `String id`

    ID of the User.

  - `LocalDateTime addedAt`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `String email`

    Email of the User.

  - `String name`

    Name of the User.

  - `BetaOrganizationRole role`

    Organization role of the User.

    - `ADMIN("admin")`

    - `BILLING("billing")`

    - `CLAUDE_CODE_USER("claude_code_user")`

    - `DEVELOPER("developer")`

    - `MANAGED("managed")`

    - `MEMBERSHIP_ADMIN("membership_admin")`

    - `OWNER("owner")`

    - `PRIMARY_OWNER("primary_owner")`

    - `USER("user")`

  - `JsonValue type = "user"`

    Object type.

    For Users, this is always `"user"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.users.BetaOrganizationUser;
import com.anthropic.models.beta.organization.users.UserUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        UserUpdateParams params = UserUpdateParams.builder()
            .userId("user_id")
            .role(UserUpdateParams.Role.USER)
            .build();
        BetaOrganizationUser betaOrganizationUser = client.beta().organization().users().update(params);
    }
}
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

`UserRemoveResponse beta().organization().users().remove(params = UserRemoveParams.none(), requestOptions = RequestOptions.none())`

**DELETE** `/v1/organizations/users/{user_id}`

Remove a member from the organization.

#### Parameters

- `UserRemoveParams params`

  - `Optional<String> userId`

    ID of the User.

#### Returns

- `class UserRemoveResponse:`

  - `String id`

    ID of the User.

  - `JsonValue type = "user_deleted"`

    Deleted object type.

    For Users, this is always `"user_deleted"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.users.UserRemoveParams;
import com.anthropic.models.beta.organization.users.UserRemoveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        UserRemoveResponse user = client.beta().organization().users().remove("user_id");
    }
}
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

`WorkspaceListPage beta().organization().workspaces().list(params = WorkspaceListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/workspaces`

List Workspaces

#### Parameters

- `WorkspaceListParams params`

  - `Optional<String> afterId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `Optional<String> beforeId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Optional<Boolean> includeArchived`

    Whether to include Workspaces that have been archived in the response

  - `Optional<Long> limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

#### Returns

- `class BetaWorkspace:`

  - `String id`

    ID of the Workspace.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `String compartmentId`

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

  - `LocalDateTime createdAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `BetaDataResidency dataResidency`

    Data residency configuration.

    - `AllowedInferenceGeos allowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `List<String>`

      - `JsonValue`

    - `String defaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `String workspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `String displayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `Optional<String> externalKeyId`

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

  - `String name`

    Name of the Workspace.

  - `Tags tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonValue type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.workspaces.WorkspaceListPage;
import com.anthropic.models.beta.organization.workspaces.WorkspaceListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkspaceListPage page = client.beta().organization().workspaces().list();
    }
}
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

`BetaWorkspace beta().organization().workspaces().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/organizations/workspaces`

Create Workspace

#### Parameters

- `WorkspaceCreateParams params`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

  - `String name`

    Name of the Workspace.

    maxLength: 40, minLength: 1

  - `Optional<BetaDataResidencyCreateConfig> dataResidency`

    Data residency configuration for the workspace. If omitted, defaults to `workspace_geo: "us"`, `allowed_inference_geos: "unrestricted"`, and `default_inference_geo: "global"`.

  - `Optional<String> displayColor`

    Hex color code representing the Workspace in the Anthropic Console.

    maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

  - `Optional<String> externalKeyId`

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

  - `Optional<Tags> tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Returns

- `class BetaWorkspace:`

  - `String id`

    ID of the Workspace.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `String compartmentId`

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

  - `LocalDateTime createdAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `BetaDataResidency dataResidency`

    Data residency configuration.

    - `AllowedInferenceGeos allowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `List<String>`

      - `JsonValue`

    - `String defaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `String workspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `String displayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `Optional<String> externalKeyId`

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

  - `String name`

    Name of the Workspace.

  - `Tags tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonValue type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.workspaces.BetaWorkspace;
import com.anthropic.models.beta.organization.workspaces.WorkspaceCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkspaceCreateParams params = WorkspaceCreateParams.builder()
            .name("x")
            .build();
        BetaWorkspace betaWorkspace = client.beta().organization().workspaces().create(params);
    }
}
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

`BetaWorkspace beta().organization().workspaces().retrieve(params = WorkspaceRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

#### Parameters

- `WorkspaceRetrieveParams params`

  - `Optional<String> workspaceId`

    ID of the Workspace.

#### Returns

- `class BetaWorkspace:`

  - `String id`

    ID of the Workspace.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `String compartmentId`

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

  - `LocalDateTime createdAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `BetaDataResidency dataResidency`

    Data residency configuration.

    - `AllowedInferenceGeos allowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `List<String>`

      - `JsonValue`

    - `String defaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `String workspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `String displayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `Optional<String> externalKeyId`

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

  - `String name`

    Name of the Workspace.

  - `Tags tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonValue type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.workspaces.BetaWorkspace;
import com.anthropic.models.beta.organization.workspaces.WorkspaceRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaWorkspace betaWorkspace = client.beta().organization().workspaces().retrieve("workspace_id");
    }
}
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

`BetaWorkspace beta().organization().workspaces().update(params = WorkspaceUpdateParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/organizations/workspaces/{workspace_id}`

Update Workspace

#### Parameters

- `WorkspaceUpdateParams params`

  - `Optional<String> workspaceId`

  - `Optional<BetaDataResidencyUpdateConfig> dataResidency`

    Data residency configuration for the workspace.

  - `Optional<String> displayColor`

    Hex color code representing the Workspace in the Anthropic Console.

    maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

  - `Optional<String> externalKeyId`

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

  - `Optional<String> name`

    Name of the Workspace.

    maxLength: 40, minLength: 1

  - `Optional<Tags> tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Returns

- `class BetaWorkspace:`

  - `String id`

    ID of the Workspace.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `String compartmentId`

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

  - `LocalDateTime createdAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `BetaDataResidency dataResidency`

    Data residency configuration.

    - `AllowedInferenceGeos allowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `List<String>`

      - `JsonValue`

    - `String defaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `String workspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `String displayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `Optional<String> externalKeyId`

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

  - `String name`

    Name of the Workspace.

  - `Tags tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonValue type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.workspaces.BetaWorkspace;
import com.anthropic.models.beta.organization.workspaces.WorkspaceUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaWorkspace betaWorkspace = client.beta().organization().workspaces().update("workspace_id");
    }
}
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

`BetaWorkspace beta().organization().workspaces().archive(params = WorkspaceArchiveParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/organizations/workspaces/{workspace_id}/archive`

Archive Workspace

#### Parameters

- `WorkspaceArchiveParams params`

  - `Optional<String> workspaceId`

#### Returns

- `class BetaWorkspace:`

  - `String id`

    ID of the Workspace.

  - `Optional<LocalDateTime> archivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `String compartmentId`

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

  - `LocalDateTime createdAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `BetaDataResidency dataResidency`

    Data residency configuration.

    - `AllowedInferenceGeos allowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `List<String>`

      - `JsonValue`

    - `String defaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `String workspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `String displayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `Optional<String> externalKeyId`

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

  - `String name`

    Name of the Workspace.

  - `Tags tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonValue type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.workspaces.BetaWorkspace;
import com.anthropic.models.beta.organization.workspaces.WorkspaceArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaWorkspace betaWorkspace = client.beta().organization().workspaces().archive("workspace_id");
    }
}
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

`RateLimitListPage beta().organization().workspaces().rateLimits().list(params = RateLimitListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/workspaces/{workspace_id}/rate_limits`

List rate-limit overrides configured for a workspace.

Returns only the groups and limiter types that have a workspace-level
override. Groups without overrides inherit the organization limits and
are not listed; use `GET /v1/organizations/rate_limits` to see those.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `RateLimitListParams params`

  - `Optional<String> workspaceId`

    The ID of the workspace.

  - `Optional<GroupType> groupType`

    Filter by group type.

    - `BATCH("batch")`

    - `FILES("files")`

    - `MODEL_GROUP("model_group")`

    - `SKILLS("skills")`

    - `TOKEN_COUNT("token_count")`

    - `WEB_SEARCH("web_search")`

  - `Optional<Long> limit`

    Maximum number of items to return per page. Ranges from `1` to `1000`.

    When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

    maximum: 1000, minimum: 1

  - `Optional<String> page`

    Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaWorkspaceRateLimit:`

  - `GroupType groupType`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `BATCH("batch")`

    - `FILES("files")`

    - `MODEL_GROUP("model_group")`

    - `SKILLS("skills")`

    - `TOKEN_COUNT("token_count")`

    - `WEB_SEARCH("web_search")`

  - `List<BetaWorkspaceRateLimitValue> limits`

    The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

    - `Optional<Long> orgLimit`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `String type`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `long value`

      The workspace-level override value for this limiter type.

  - `Optional<List<String>> models`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `String rateLimitId`

    The `id` of the RateLimit group this override applies to.

  - `JsonValue type = "workspace_rate_limit"`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

  - `String workspaceId`

    ID of the Workspace this override applies to.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.workspaces.ratelimits.RateLimitListPage;
import com.anthropic.models.beta.organization.workspaces.ratelimits.RateLimitListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        RateLimitListPage page = client.beta().organization().workspaces().rateLimits().list("workspace_id");
    }
}
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

`MemberListPage beta().organization().workspaces().members().list(params = MemberListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/workspaces/{workspace_id}/members`

List Workspace Members

#### Parameters

- `MemberListParams params`

  - `Optional<String> workspaceId`

    ID of the Workspace.

  - `Optional<String> afterId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `Optional<String> beforeId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Optional<Long> limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonValue type = "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `String userId`

    ID of the User.

  - `String workspaceId`

    ID of the Workspace.

  - `BetaWorkspaceRole workspaceRole`

    Role of the Workspace Member.

    - `WORKSPACE_ADMIN("workspace_admin")`

    - `WORKSPACE_BILLING("workspace_billing")`

    - `WORKSPACE_DEVELOPER("workspace_developer")`

    - `WORKSPACE_RESTRICTED_DEVELOPER("workspace_restricted_developer")`

    - `WORKSPACE_USER("workspace_user")`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.workspaces.members.MemberListPage;
import com.anthropic.models.beta.organization.workspaces.members.MemberListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemberListPage page = client.beta().organization().workspaces().members().list("workspace_id");
    }
}
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

`BetaWorkspaceMember beta().organization().workspaces().members().add(params, requestOptions = RequestOptions.none())`

**POST** `/v1/organizations/workspaces/{workspace_id}/members`

Create Workspace Member

#### Parameters

- `MemberAddParams params`

  - `Optional<String> workspaceId`

    ID of the Workspace.

  - `String userId`

    ID of the User.

  - `BetaNoBillingWorkspaceRole workspaceRole`

    Role of the new Workspace Member. Cannot be `workspace_billing`.

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonValue type = "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `String userId`

    ID of the User.

  - `String workspaceId`

    ID of the Workspace.

  - `BetaWorkspaceRole workspaceRole`

    Role of the Workspace Member.

    - `WORKSPACE_ADMIN("workspace_admin")`

    - `WORKSPACE_BILLING("workspace_billing")`

    - `WORKSPACE_DEVELOPER("workspace_developer")`

    - `WORKSPACE_RESTRICTED_DEVELOPER("workspace_restricted_developer")`

    - `WORKSPACE_USER("workspace_user")`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.workspaces.BetaNoBillingWorkspaceRole;
import com.anthropic.models.beta.organization.workspaces.BetaWorkspaceMember;
import com.anthropic.models.beta.organization.workspaces.members.MemberAddParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemberAddParams params = MemberAddParams.builder()
            .workspaceId("workspace_id")
            .userId("user_01WCz1FkmYMm4gnmykNKUu3Q")
            .workspaceRole(BetaNoBillingWorkspaceRole.WORKSPACE_ADMIN)
            .build();
        BetaWorkspaceMember betaWorkspaceMember = client.beta().organization().workspaces().members().add(params);
    }
}
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

`BetaWorkspaceMember beta().organization().workspaces().members().retrieve(params, requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Get Workspace Member

#### Parameters

- `MemberRetrieveParams params`

  - `String workspaceId`

    ID of the Workspace.

  - `Optional<String> userId`

    ID of the User.

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonValue type = "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `String userId`

    ID of the User.

  - `String workspaceId`

    ID of the Workspace.

  - `BetaWorkspaceRole workspaceRole`

    Role of the Workspace Member.

    - `WORKSPACE_ADMIN("workspace_admin")`

    - `WORKSPACE_BILLING("workspace_billing")`

    - `WORKSPACE_DEVELOPER("workspace_developer")`

    - `WORKSPACE_RESTRICTED_DEVELOPER("workspace_restricted_developer")`

    - `WORKSPACE_USER("workspace_user")`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.workspaces.BetaWorkspaceMember;
import com.anthropic.models.beta.organization.workspaces.members.MemberRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemberRetrieveParams params = MemberRetrieveParams.builder()
            .workspaceId("workspace_id")
            .userId("user_id")
            .build();
        BetaWorkspaceMember betaWorkspaceMember = client.beta().organization().workspaces().members().retrieve(params);
    }
}
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

`BetaWorkspaceMember beta().organization().workspaces().members().update(params, requestOptions = RequestOptions.none())`

**POST** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Update Workspace Member

#### Parameters

- `MemberUpdateParams params`

  - `String workspaceId`

    ID of the Workspace.

  - `Optional<String> userId`

    ID of the User.

  - `BetaWorkspaceRole workspaceRole`

    New workspace role for the User.

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonValue type = "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `String userId`

    ID of the User.

  - `String workspaceId`

    ID of the Workspace.

  - `BetaWorkspaceRole workspaceRole`

    Role of the Workspace Member.

    - `WORKSPACE_ADMIN("workspace_admin")`

    - `WORKSPACE_BILLING("workspace_billing")`

    - `WORKSPACE_DEVELOPER("workspace_developer")`

    - `WORKSPACE_RESTRICTED_DEVELOPER("workspace_restricted_developer")`

    - `WORKSPACE_USER("workspace_user")`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.workspaces.BetaWorkspaceMember;
import com.anthropic.models.beta.organization.workspaces.BetaWorkspaceRole;
import com.anthropic.models.beta.organization.workspaces.members.MemberUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemberUpdateParams params = MemberUpdateParams.builder()
            .workspaceId("workspace_id")
            .userId("user_id")
            .workspaceRole(BetaWorkspaceRole.WORKSPACE_ADMIN)
            .build();
        BetaWorkspaceMember betaWorkspaceMember = client.beta().organization().workspaces().members().update(params);
    }
}
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

`MemberRemoveResponse beta().organization().workspaces().members().remove(params, requestOptions = RequestOptions.none())`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Delete Workspace Member

#### Parameters

- `MemberRemoveParams params`

  - `String workspaceId`

    ID of the Workspace.

  - `Optional<String> userId`

    ID of the User.

#### Returns

- `class MemberRemoveResponse:`

  - `JsonValue type = "workspace_member_deleted"`

    Deleted object type.

    For Workspace Members, this is always `"workspace_member_deleted"`.

  - `String userId`

    ID of the User.

  - `String workspaceId`

    ID of the Workspace.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.workspaces.members.MemberRemoveParams;
import com.anthropic.models.beta.organization.workspaces.members.MemberRemoveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemberRemoveParams params = MemberRemoveParams.builder()
            .workspaceId("workspace_id")
            .userId("user_id")
            .build();
        MemberRemoveResponse member = client.beta().organization().workspaces().members().remove(params);
    }
}
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

`ServiceAccountListPage beta().organization().workspaces().serviceAccounts().list(params = ServiceAccountListParams.none(), requestOptions = RequestOptions.none())`

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

- `ServiceAccountListParams params`

  - `Optional<String> workspaceId`

    ID of the workspace.

  - `Optional<Long> limit`

    Number of results per page.

    maximum: 100, minimum: 1

  - `Optional<String> page`

    Opaque cursor from a previous response's `next_page`.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `Optional<String> createdByActorId`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `Optional<Boolean> implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `String serviceAccountId`

    Tagged service account ID (`svac_...`).

  - `JsonValue type = "service_account_workspace_member"`

  - `String workspaceId`

    Tagged workspace ID (`wrkspc_...`).

  - `BetaWorkspaceRole workspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WORKSPACE_ADMIN("workspace_admin")`

    - `WORKSPACE_BILLING("workspace_billing")`

    - `WORKSPACE_DEVELOPER("workspace_developer")`

    - `WORKSPACE_RESTRICTED_DEVELOPER("workspace_restricted_developer")`

    - `WORKSPACE_USER("workspace_user")`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.workspaces.serviceaccounts.ServiceAccountListPage;
import com.anthropic.models.beta.organization.workspaces.serviceaccounts.ServiceAccountListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ServiceAccountListPage page = client.beta().organization().workspaces().serviceAccounts().list("workspace_id");
    }
}
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

`BetaServiceAccountWorkspaceMember beta().organization().workspaces().serviceAccounts().add(params, requestOptions = RequestOptions.none())`

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

- `ServiceAccountAddParams params`

  - `Optional<String> workspaceId`

    ID of the workspace.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

  - `String serviceAccountId`

    Tagged service account ID to add.

  - `BetaNoBillingWorkspaceRole workspaceRole`

    Role to assign to the service account in this workspace.

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `Optional<String> createdByActorId`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `Optional<Boolean> implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `String serviceAccountId`

    Tagged service account ID (`svac_...`).

  - `JsonValue type = "service_account_workspace_member"`

  - `String workspaceId`

    Tagged workspace ID (`wrkspc_...`).

  - `BetaWorkspaceRole workspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WORKSPACE_ADMIN("workspace_admin")`

    - `WORKSPACE_BILLING("workspace_billing")`

    - `WORKSPACE_DEVELOPER("workspace_developer")`

    - `WORKSPACE_RESTRICTED_DEVELOPER("workspace_restricted_developer")`

    - `WORKSPACE_USER("workspace_user")`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.serviceaccounts.BetaServiceAccountWorkspaceMember;
import com.anthropic.models.beta.organization.workspaces.BetaNoBillingWorkspaceRole;
import com.anthropic.models.beta.organization.workspaces.serviceaccounts.ServiceAccountAddParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ServiceAccountAddParams params = ServiceAccountAddParams.builder()
            .workspaceId("workspace_id")
            .serviceAccountId("service_account_id")
            .workspaceRole(BetaNoBillingWorkspaceRole.WORKSPACE_ADMIN)
            .build();
        BetaServiceAccountWorkspaceMember betaServiceAccountWorkspaceMember = client.beta().organization().workspaces().serviceAccounts().add(params);
    }
}
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

`BetaServiceAccountWorkspaceMember beta().organization().workspaces().serviceAccounts().retrieve(params, requestOptions = RequestOptions.none())`

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

- `ServiceAccountRetrieveParams params`

  - `String workspaceId`

    ID of the workspace.

  - `Optional<String> serviceAccountId`

    ID of the service account.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `Optional<String> createdByActorId`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `Optional<Boolean> implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `String serviceAccountId`

    Tagged service account ID (`svac_...`).

  - `JsonValue type = "service_account_workspace_member"`

  - `String workspaceId`

    Tagged workspace ID (`wrkspc_...`).

  - `BetaWorkspaceRole workspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WORKSPACE_ADMIN("workspace_admin")`

    - `WORKSPACE_BILLING("workspace_billing")`

    - `WORKSPACE_DEVELOPER("workspace_developer")`

    - `WORKSPACE_RESTRICTED_DEVELOPER("workspace_restricted_developer")`

    - `WORKSPACE_USER("workspace_user")`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.serviceaccounts.BetaServiceAccountWorkspaceMember;
import com.anthropic.models.beta.organization.workspaces.serviceaccounts.ServiceAccountRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ServiceAccountRetrieveParams params = ServiceAccountRetrieveParams.builder()
            .workspaceId("workspace_id")
            .serviceAccountId("service_account_id")
            .build();
        BetaServiceAccountWorkspaceMember betaServiceAccountWorkspaceMember = client.beta().organization().workspaces().serviceAccounts().retrieve(params);
    }
}
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

`BetaServiceAccountWorkspaceMember beta().organization().workspaces().serviceAccounts().update(params, requestOptions = RequestOptions.none())`

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

- `ServiceAccountUpdateParams params`

  - `String workspaceId`

    ID of the workspace.

  - `Optional<String> serviceAccountId`

    ID of the service account.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

  - `BetaNoBillingWorkspaceRole workspaceRole`

    New role for the service account in this workspace.

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `Optional<String> createdByActorId`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `Optional<Boolean> implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `String serviceAccountId`

    Tagged service account ID (`svac_...`).

  - `JsonValue type = "service_account_workspace_member"`

  - `String workspaceId`

    Tagged workspace ID (`wrkspc_...`).

  - `BetaWorkspaceRole workspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WORKSPACE_ADMIN("workspace_admin")`

    - `WORKSPACE_BILLING("workspace_billing")`

    - `WORKSPACE_DEVELOPER("workspace_developer")`

    - `WORKSPACE_RESTRICTED_DEVELOPER("workspace_restricted_developer")`

    - `WORKSPACE_USER("workspace_user")`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.serviceaccounts.BetaServiceAccountWorkspaceMember;
import com.anthropic.models.beta.organization.workspaces.BetaNoBillingWorkspaceRole;
import com.anthropic.models.beta.organization.workspaces.serviceaccounts.ServiceAccountUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ServiceAccountUpdateParams params = ServiceAccountUpdateParams.builder()
            .workspaceId("workspace_id")
            .serviceAccountId("service_account_id")
            .workspaceRole(BetaNoBillingWorkspaceRole.WORKSPACE_ADMIN)
            .build();
        BetaServiceAccountWorkspaceMember betaServiceAccountWorkspaceMember = client.beta().organization().workspaces().serviceAccounts().update(params);
    }
}
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

`ServiceAccountRemoveResponse beta().organization().workspaces().serviceAccounts().remove(params, requestOptions = RequestOptions.none())`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Removal is idempotent (returns 200 even if the membership was already
removed). A DELETE against the implicit default-workspace membership
returns 200 but is a no-op and the membership persists; deleting an
explicit default-workspace row reverts to the implicit `workspace_user`
membership. Archived workspaces return 400.

#### Parameters

- `ServiceAccountRemoveParams params`

  - `String workspaceId`

    ID of the workspace.

  - `Optional<String> serviceAccountId`

    ID of the service account.

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class ServiceAccountRemoveResponse:`

  - `String serviceAccountId`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `JsonValue type = "service_account_workspace_member_deleted"`

  - `String workspaceId`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.workspaces.serviceaccounts.ServiceAccountRemoveParams;
import com.anthropic.models.beta.organization.workspaces.serviceaccounts.ServiceAccountRemoveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ServiceAccountRemoveParams params = ServiceAccountRemoveParams.builder()
            .workspaceId("workspace_id")
            .serviceAccountId("service_account_id")
            .build();
        ServiceAccountRemoveResponse serviceAccount = client.beta().organization().workspaces().serviceAccounts().remove(params);
    }
}
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

`RateLimitListPage beta().organization().rateLimits().list(params = RateLimitListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/rate_limits`

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `RateLimitListParams params`

  - `Optional<GroupType> groupType`

    Filter by group type.

    - `BATCH("batch")`

    - `FILES("files")`

    - `MODEL_GROUP("model_group")`

    - `SKILLS("skills")`

    - `TOKEN_COUNT("token_count")`

    - `WEB_SEARCH("web_search")`

  - `Optional<Long> limit`

    Maximum number of items to return per page. Ranges from `1` to `1000`.

    When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

    maximum: 1000, minimum: 1

  - `Optional<String> model`

    Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

  - `Optional<String> page`

    Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaOrganizationRateLimit:`

  - `String id`

    Stable identifier for this rate-limit group within the organization.

  - `GroupType groupType`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `BATCH("batch")`

    - `FILES("files")`

    - `MODEL_GROUP("model_group")`

    - `SKILLS("skills")`

    - `TOKEN_COUNT("token_count")`

    - `WEB_SEARCH("web_search")`

  - `List<BetaOrganizationRateLimitValue> limits`

    The limiter values that apply to this group.

    - `String type`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `long value`

      The configured limit value for this limiter type.

  - `Optional<List<String>> models`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `JsonValue type = "rate_limit"`

    Object type. Always `rate_limit` for organization rate-limit entries.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.ratelimits.RateLimitListPage;
import com.anthropic.models.beta.organization.ratelimits.RateLimitListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        RateLimitListPage page = client.beta().organization().rateLimits().list();
    }
}
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

`BetaComplianceSettings beta().organization().complianceSettings().retrieve(params = ComplianceSettingRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/organizations/compliance_settings`

Retrieve your organization's Compliance Settings.

Compliance Settings is a singleton resource: there is exactly one per
organization, addressed without an identifier. The `state` field reflects
whether the Compliance API is enabled. An organization with a parent
organization reads the state inherited from the parent's configuration.

#### Parameters

- `ComplianceSettingRetrieveParams params`

#### Returns

- `class BetaComplianceSettings:`

  - `State state`

    Whether the Compliance API is enabled for this organization.

    - `class BetaComplianceSettingsStateEnabled:`

      - `JsonValue type = "enabled"`

    - `class BetaComplianceSettingsStateDisabled:`

      - `JsonValue type = "disabled"`

  - `JsonValue type = "compliance_settings"`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.compliancesettings.BetaComplianceSettings;
import com.anthropic.models.beta.organization.compliancesettings.ComplianceSettingRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaComplianceSettings betaComplianceSettings = client.beta().organization().complianceSettings().retrieve();
    }
}
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

`BetaComplianceSettings beta().organization().complianceSettings().update(params, requestOptions = RequestOptions.none())`

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

- `ComplianceSettingUpdateParams params`

  - `State state`

    Desired state. Accepts the string shorthand "enabled" or "disabled" in place of the object form; the response always returns the canonical object form.

    - `class BetaComplianceSettingsStateEnabledParam:`

      - `JsonValue type = "enabled"`

    - `class BetaComplianceSettingsStateDisabledParam:`

      - `JsonValue type = "disabled"`

#### Returns

- `class BetaComplianceSettings:`

  - `State state`

    Whether the Compliance API is enabled for this organization.

    - `class BetaComplianceSettingsStateEnabled:`

      - `JsonValue type = "enabled"`

    - `class BetaComplianceSettingsStateDisabled:`

      - `JsonValue type = "disabled"`

  - `JsonValue type = "compliance_settings"`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.organization.compliancesettings.BetaComplianceSettings;
import com.anthropic.models.beta.organization.compliancesettings.BetaComplianceSettingsStateEnabledParam;
import com.anthropic.models.beta.organization.compliancesettings.ComplianceSettingUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ComplianceSettingUpdateParams params = ComplianceSettingUpdateParams.builder()
            .state(BetaComplianceSettingsStateEnabledParam.builder().build())
            .build();
        BetaComplianceSettings betaComplianceSettings = client.beta().organization().complianceSettings().update(params);
    }
}
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
