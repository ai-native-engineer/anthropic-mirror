<!-- source: https://platform.claude.com/docs/en/api/csharp/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/csharp/beta -->

<!-- chunk-start -->

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaFederationRuleWorkspace:`

  - `required DateTimeOffset CreatedAt`

    When this workspace was enabled for the rule.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `required string FederationRuleID`

    Tagged ID of the federation rule.

  - `JsonElement Type = "federation_rule_workspace"`

  - `required string WorkspaceID`

    Tagged ID of the workspace this rule is enabled for.

  - `required string? WorkspaceName`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```csharp
WorkspaceListParams parameters = new()
{
    FederationRuleID = "federation_rule_id"
};

var page = await client.Beta.Organization.Federation.Rules.Workspaces.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`WorkspaceRemoveResponse Beta.Organization.Federation.Rules.Workspaces.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Disable a federation rule for a workspace.

Idempotent; succeeds even if the enablement was already removed. OAuth
callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Parameters

- `WorkspaceRemoveParams parameters`

  - `required string federationRuleID`

    Path param: ID of the federation rule.

  - `required string workspaceID`

    Path param: ID of the workspace to disable for.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class WorkspaceRemoveResponse:`

  - `required string FederationRuleID`

    Tagged ID of the federation rule.

  - `JsonElement Type = "federation_rule_workspace_deleted"`

  - `required string WorkspaceID`

    Tagged ID of the workspace named in the delete request. Removal is idempotent.

#### Example

```csharp
WorkspaceRemoveParams parameters = new()
{
    FederationRuleID = "federation_rule_id",
    WorkspaceID = "workspace_id",
};

var workspace = await client.Beta.Organization.Federation.Rules.Workspaces.Remove(parameters);

Console.WriteLine(workspace);
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

`BetaOrganizationInvite Beta.Organization.Invites.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/invites`

Invite a user to join the organization by email.

On plans that draw members from a finite pool of purchased seats, the invite automatically consumes a seat from the lowest tier with availability; there is no seat-tier parameter. When no seat is free the request fails with a 400 error rather than purchasing a seat.

#### Parameters

- `InviteCreateParams parameters`

  - `required string email`

    Email of the User.

    format: email

  - `required Role role`

    Role for the invited User.

    The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `User("user")`

  - `IReadOnlyList<string> rbacGroupIds`

    RBAC group IDs to assign to the User when the Invite is accepted. A non-empty array is accepted only for a Claude Enterprise organization with RBAC groups, and requires the key to carry the `write:rbac_groups` scope.

    maxItems: 100

#### Returns

- `class BetaOrganizationInvite:`

  - `required string ID`

    ID of the Invite.

  - `required DateTimeOffset? AcceptedAt`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `required string Email`

    Email of the User being invited.

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `required DateTimeOffset InvitedAt`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `required IReadOnlyList<string> RbacGroupIds`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin("admin")`

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `MembershipAdmin("membership_admin")`

    - `Owner("owner")`

    - `PrimaryOwner("primary_owner")`

    - `User("user")`

  - `required Status Status`

    Status of the Invite.

    - `Accepted("accepted")`

    - `Deleted("deleted")`

    - `Expired("expired")`

    - `Pending("pending")`

  - `JsonElement Type = "invite"`

    Object type.

    For Invites, this is always `"invite"`.

#### Example

```csharp
InviteCreateParams parameters = new()
{
    Email = "user@emaildomain.com",
    Role = Role.User,
};

var betaOrganizationInvite = await client.Beta.Organization.Invites.Create(parameters);

Console.WriteLine(betaOrganizationInvite);
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

`InviteListPage Beta.Organization.Invites.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/invites`

List the organization's invites.

#### Parameters

- `InviteListParams parameters`

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `string email`

    Filter by the email address the Invite was sent to. Matches the same way as the Users list's `email` filter (normalized, case-insensitive).

    format: email

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `IReadOnlyList<string> roles`

    Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

    Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

  - `IReadOnlyList<Status> statuses`

    Filter by Invite status. Repeatable; values are OR'ed together. Omit to return `pending`, `accepted`, and `expired` Invites alike.

    - `Accepted("accepted")`

    - `Expired("expired")`

    - `Pending("pending")`

#### Returns

- `class BetaOrganizationInvite:`

  - `required string ID`

    ID of the Invite.

  - `required DateTimeOffset? AcceptedAt`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `required string Email`

    Email of the User being invited.

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `required DateTimeOffset InvitedAt`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `required IReadOnlyList<string> RbacGroupIds`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin("admin")`

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `MembershipAdmin("membership_admin")`

    - `Owner("owner")`

    - `PrimaryOwner("primary_owner")`

    - `User("user")`

  - `required Status Status`

    Status of the Invite.

    - `Accepted("accepted")`

    - `Deleted("deleted")`

    - `Expired("expired")`

    - `Pending("pending")`

  - `JsonElement Type = "invite"`

    Object type.

    For Invites, this is always `"invite"`.

#### Example

```csharp
InviteListParams parameters = new();

var page = await client.Beta.Organization.Invites.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaOrganizationInvite Beta.Organization.Invites.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/invites/{invite_id}`

Retrieve an invite by ID.

#### Parameters

- `InviteRetrieveParams parameters`

  - `required string inviteID`

    ID of the Invite.

#### Returns

- `class BetaOrganizationInvite:`

  - `required string ID`

    ID of the Invite.

  - `required DateTimeOffset? AcceptedAt`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `required string Email`

    Email of the User being invited.

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `required DateTimeOffset InvitedAt`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `required IReadOnlyList<string> RbacGroupIds`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin("admin")`

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `MembershipAdmin("membership_admin")`

    - `Owner("owner")`

    - `PrimaryOwner("primary_owner")`

    - `User("user")`

  - `required Status Status`

    Status of the Invite.

    - `Accepted("accepted")`

    - `Deleted("deleted")`

    - `Expired("expired")`

    - `Pending("pending")`

  - `JsonElement Type = "invite"`

    Object type.

    For Invites, this is always `"invite"`.

#### Example

```csharp
InviteRetrieveParams parameters = new() { InviteID = "invite_id" };

var betaOrganizationInvite = await client.Beta.Organization.Invites.Retrieve(parameters);

Console.WriteLine(betaOrganizationInvite);
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

`InviteDeleteResponse Beta.Organization.Invites.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/invites/{invite_id}`

Delete a pending invite.

#### Parameters

- `InviteDeleteParams parameters`

  - `required string inviteID`

    ID of the Invite.

#### Returns

- `class InviteDeleteResponse:`

  - `required string ID`

    ID of the Invite.

  - `JsonElement Type = "invite_deleted"`

    Deleted object type.

    For Invites, this is always `"invite_deleted"`.

#### Example

```csharp
InviteDeleteParams parameters = new() { InviteID = "invite_id" };

var invite = await client.Beta.Organization.Invites.Delete(parameters);

Console.WriteLine(invite);
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

`BetaServiceAccount Beta.Organization.ServiceAccounts.Create(parameters, cancellationToken = default)`

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

- `ServiceAccountCreateParams parameters`

  - `required string name`

    Body param: Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

    maxLength: 255, minLength: 1

  - `string? description`

    Body param: Optional free-text description.

    maxLength: 2000

  - `OrganizationRole organizationRole`

    Body param: Org-level role. Defaults to `developer`.

    - `Admin("admin")`

    - `Developer("developer")`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin("admin")`

    - `Developer("developer")`

  - `JsonElement Type = "service_account"`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountCreateParams parameters = new() { Name = "ci-deploy-bot" };

var betaServiceAccount = await client.Beta.Organization.ServiceAccounts.Create(parameters);

Console.WriteLine(betaServiceAccount);
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

`ServiceAccountListPage Beta.Organization.ServiceAccounts.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List service accounts in the caller's organization.

Results are ordered by creation time, newest first. Use `limit` and the
`next_page` cursor to paginate; set `include_archived=true` to include
archived service accounts.

#### Parameters

- `ServiceAccountListParams parameters`

  - `bool includeArchived`

    Query param: Include archived resources. Defaults to false.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin("admin")`

    - `Developer("developer")`

  - `JsonElement Type = "service_account"`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountListParams parameters = new();

var page = await client.Beta.Organization.ServiceAccounts.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaServiceAccount Beta.Organization.ServiceAccounts.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a service account by its ID (`svac_...`).

#### Parameters

- `ServiceAccountRetrieveParams parameters`

  - `required string serviceAccountID`

    ID of the service account.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin("admin")`

    - `Developer("developer")`

  - `JsonElement Type = "service_account"`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountRetrieveParams parameters = new()
{
    ServiceAccountID = "service_account_id"
};

var betaServiceAccount = await client.Beta.Organization.ServiceAccounts.Retrieve(parameters);

Console.WriteLine(betaServiceAccount);
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

`BetaServiceAccount Beta.Organization.ServiceAccounts.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Update a service account.

Only `description` and `organization_role` are mutable; `name` cannot be
changed. Archived service accounts cannot be updated; this returns 400.
Setting `organization_role` to `admin` (even when unchanged) requires an
interactive credential (a user OAuth token or a Console session).

#### Parameters

- `ServiceAccountUpdateParams parameters`

  - `required string serviceAccountID`

    Path param: ID of the service account to update.

  - `string? description`

    Body param: Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

    maxLength: 2000

  - `OrganizationRole? organizationRole`

    Body param: Replaces the org-level role. Omit or send `null` to leave unchanged.

    - `Admin("admin")`

    - `Developer("developer")`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin("admin")`

    - `Developer("developer")`

  - `JsonElement Type = "service_account"`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountUpdateParams parameters = new()
{
    ServiceAccountID = "service_account_id"
};

var betaServiceAccount = await client.Beta.Organization.ServiceAccounts.Update(parameters);

Console.WriteLine(betaServiceAccount);
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

`BetaServiceAccount Beta.Organization.ServiceAccounts.Archive(parameters, cancellationToken = default)`

**POST** `/v1/organizations/service_accounts/{service_account_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a service account.

Idempotent; re-archiving returns the service account with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still targets this service account, same as issuer archival; archive
those rules first or change their target to another service account.

#### Parameters

- `ServiceAccountArchiveParams parameters`

  - `required string serviceAccountID`

    ID of the service account to archive.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin("admin")`

    - `Developer("developer")`

  - `JsonElement Type = "service_account"`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountArchiveParams parameters = new()
{
    ServiceAccountID = "service_account_id"
};

var betaServiceAccount = await client.Beta.Organization.ServiceAccounts.Archive(parameters);

Console.WriteLine(betaServiceAccount);
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

`BetaServiceAccountWorkspaceMember Beta.Organization.ServiceAccounts.Workspaces.Add(parameters, cancellationToken = default)`

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

- `WorkspaceAddParams parameters`

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `required string workspaceID`

    Body param: Tagged workspace ID to add the service account to.

  - `required BetaNoBillingWorkspaceRole workspaceRole`

    Body param: Role to assign to the service account in this workspace.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `JsonElement Type = "service_account_workspace_member"`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
WorkspaceAddParams parameters = new()
{
    ServiceAccountID = "service_account_id",
    WorkspaceID = "workspace_id",
    WorkspaceRole = BetaNoBillingWorkspaceRole.WorkspaceAdmin,
};

var betaServiceAccountWorkspaceMember = await client.Beta.Organization.ServiceAccounts.Workspaces.Add(parameters);

Console.WriteLine(betaServiceAccountWorkspaceMember);
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

`WorkspaceListPage Beta.Organization.ServiceAccounts.Workspaces.List(parameters, cancellationToken = default)`

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

- `WorkspaceListParams parameters`

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `JsonElement Type = "service_account_workspace_member"`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
WorkspaceListParams parameters = new()
{
    ServiceAccountID = "service_account_id"
};

var page = await client.Beta.Organization.ServiceAccounts.Workspaces.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`WorkspaceRemoveResponse Beta.Organization.ServiceAccounts.Workspaces.Remove(parameters, cancellationToken = default)`

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

- `WorkspaceRemoveParams parameters`

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class WorkspaceRemoveResponse:`

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `JsonElement Type = "service_account_workspace_member_deleted"`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```csharp
WorkspaceRemoveParams parameters = new()
{
    ServiceAccountID = "service_account_id",
    WorkspaceID = "workspace_id",
};

var workspace = await client.Beta.Organization.ServiceAccounts.Workspaces.Remove(parameters);

Console.WriteLine(workspace);
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

`UserListPage Beta.Organization.Users.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/users`

List the organization's members.

#### Parameters

- `UserListParams parameters`

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `string email`

    Filter by user email.

    format: email

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `IReadOnlyList<string> roles`

    Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

    Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

#### Returns

- `class BetaOrganizationUser:`

  - `required string ID`

    ID of the User.

  - `required DateTimeOffset AddedAt`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `required string Email`

    Email of the User.

  - `required string Name`

    Name of the User.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin("admin")`

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `MembershipAdmin("membership_admin")`

    - `Owner("owner")`

    - `PrimaryOwner("primary_owner")`

    - `User("user")`

  - `JsonElement Type = "user"`

    Object type.

    For Users, this is always `"user"`.

#### Example

```csharp
UserListParams parameters = new();

var page = await client.Beta.Organization.Users.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaOrganizationUser Beta.Organization.Users.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/users/{user_id}`

Retrieve a member of the organization by user ID.

#### Parameters

- `UserRetrieveParams parameters`

  - `required string userID`

    ID of the User.

#### Returns

- `class BetaOrganizationUser:`

  - `required string ID`

    ID of the User.

  - `required DateTimeOffset AddedAt`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `required string Email`

    Email of the User.

  - `required string Name`

    Name of the User.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin("admin")`

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `MembershipAdmin("membership_admin")`

    - `Owner("owner")`

    - `PrimaryOwner("primary_owner")`

    - `User("user")`

  - `JsonElement Type = "user"`

    Object type.

    For Users, this is always `"user"`.

#### Example

```csharp
UserRetrieveParams parameters = new() { UserID = "user_id" };

var betaOrganizationUser = await client.Beta.Organization.Users.Retrieve(parameters);

Console.WriteLine(betaOrganizationUser);
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

`BetaOrganizationUser Beta.Organization.Users.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/users/{user_id}`

Update a member's organization role.

#### Parameters

- `UserUpdateParams parameters`

  - `required string userID`

    ID of the User.

  - `required Role role`

    New role for the User.

    The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `User("user")`

#### Returns

- `class BetaOrganizationUser:`

  - `required string ID`

    ID of the User.

  - `required DateTimeOffset AddedAt`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `required string Email`

    Email of the User.

  - `required string Name`

    Name of the User.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin("admin")`

    - `Billing("billing")`

    - `ClaudeCodeUser("claude_code_user")`

    - `Developer("developer")`

    - `Managed("managed")`

    - `MembershipAdmin("membership_admin")`

    - `Owner("owner")`

    - `PrimaryOwner("primary_owner")`

    - `User("user")`

  - `JsonElement Type = "user"`

    Object type.

    For Users, this is always `"user"`.

#### Example

```csharp
UserUpdateParams parameters = new()
{
    UserID = "user_id",
    Role = Role.User,
};

var betaOrganizationUser = await client.Beta.Organization.Users.Update(parameters);

Console.WriteLine(betaOrganizationUser);
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

`UserRemoveResponse Beta.Organization.Users.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/users/{user_id}`

Remove a member from the organization.

#### Parameters

- `UserRemoveParams parameters`

  - `required string userID`

    ID of the User.

#### Returns

- `class UserRemoveResponse:`

  - `required string ID`

    ID of the User.

  - `JsonElement Type = "user_deleted"`

    Deleted object type.

    For Users, this is always `"user_deleted"`.

#### Example

```csharp
UserRemoveParams parameters = new() { UserID = "user_id" };

var user = await client.Beta.Organization.Users.Remove(parameters);

Console.WriteLine(user);
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

`WorkspaceListPage Beta.Organization.Workspaces.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces`

List Workspaces

#### Parameters

- `WorkspaceListParams parameters`

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `bool includeArchived`

    Whether to include Workspaces that have been archived in the response

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

#### Returns

- `class BetaWorkspace:`

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

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

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

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

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonElement Type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```csharp
WorkspaceListParams parameters = new();

var page = await client.Beta.Organization.Workspaces.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaWorkspace Beta.Organization.Workspaces.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces`

Create Workspace

#### Parameters

- `WorkspaceCreateParams parameters`

  - `required string name`

    Body param: Name of the Workspace.

    maxLength: 40, minLength: 1

  - `BetaDataResidencyCreateConfig? dataResidency`

    Body param: Data residency configuration for the workspace. If omitted, defaults to `workspace_geo: "us"`, `allowed_inference_geos: "unrestricted"`, and `default_inference_geo: "global"`.

  - `string? displayColor`

    Body param: Hex color code representing the Workspace in the Anthropic Console.

    maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

  - `string? externalKeyID`

    Body param: ID of the customer-managed encryption key (CMEK) configuration to use for this
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

  - `IReadOnlyDictionary<string, string>? tags`

    Body param: User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaWorkspace:`

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

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

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

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

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonElement Type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```csharp
WorkspaceCreateParams parameters = new() { Name = "x" };

var betaWorkspace = await client.Beta.Organization.Workspaces.Create(parameters);

Console.WriteLine(betaWorkspace);
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

`BetaWorkspace Beta.Organization.Workspaces.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

#### Parameters

- `WorkspaceRetrieveParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

#### Returns

- `class BetaWorkspace:`

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

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

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

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

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonElement Type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```csharp
WorkspaceRetrieveParams parameters = new() { WorkspaceID = "workspace_id" };

var betaWorkspace = await client.Beta.Organization.Workspaces.Retrieve(parameters);

Console.WriteLine(betaWorkspace);
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

`BetaWorkspace Beta.Organization.Workspaces.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}`

Update Workspace

#### Parameters

- `WorkspaceUpdateParams parameters`

  - `required string workspaceID`

  - `BetaDataResidencyUpdateConfig? dataResidency`

    Data residency configuration for the workspace.

  - `string displayColor`

    Hex color code representing the Workspace in the Anthropic Console.

    maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

  - `string externalKeyID`

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

  - `string name`

    Name of the Workspace.

    maxLength: 40, minLength: 1

  - `IReadOnlyDictionary<string, string>? tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Returns

- `class BetaWorkspace:`

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

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

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

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

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonElement Type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```csharp
WorkspaceUpdateParams parameters = new() { WorkspaceID = "workspace_id" };

var betaWorkspace = await client.Beta.Organization.Workspaces.Update(parameters);

Console.WriteLine(betaWorkspace);
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

`BetaWorkspace Beta.Organization.Workspaces.Archive(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}/archive`

Archive Workspace

#### Parameters

- `WorkspaceArchiveParams parameters`

  - `required string workspaceID`

#### Returns

- `class BetaWorkspace:`

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

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

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

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

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonElement Type = "workspace"`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```csharp
WorkspaceArchiveParams parameters = new() { WorkspaceID = "workspace_id" };

var betaWorkspace = await client.Beta.Organization.Workspaces.Archive(parameters);

Console.WriteLine(betaWorkspace);
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

`RateLimitListPage Beta.Organization.Workspaces.RateLimits.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}/rate_limits`

List rate-limit overrides configured for a workspace.

Returns only the groups and limiter types that have a workspace-level
override. Groups without overrides inherit the organization limits and
are not listed; use `GET /v1/organizations/rate_limits` to see those.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `RateLimitListParams parameters`

  - `required string workspaceID`

    The ID of the workspace.

  - `GroupType? groupType`

    Filter by group type.

    - `Batch("batch")`

    - `Files("files")`

    - `ModelGroup("model_group")`

    - `Skills("skills")`

    - `TokenCount("token_count")`

    - `WebSearch("web_search")`

  - `long? limit`

    Maximum number of items to return per page. Ranges from `1` to `1000`.

    When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

    maximum: 1000, minimum: 1

  - `string? page`

    Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaWorkspaceRateLimit:`

  - `required GroupType GroupType`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `Batch("batch")`

    - `Files("files")`

    - `ModelGroup("model_group")`

    - `Skills("skills")`

    - `TokenCount("token_count")`

    - `WebSearch("web_search")`

  - `required IReadOnlyList<BetaWorkspaceRateLimitValue> Limits`

    The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

    - `required long? OrgLimit`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `required string Type`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `required long Value`

      The workspace-level override value for this limiter type.

  - `required IReadOnlyList<string>? Models`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `required string RateLimitID`

    The `id` of the RateLimit group this override applies to.

  - `JsonElement Type = "workspace_rate_limit"`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

  - `required string WorkspaceID`

    ID of the Workspace this override applies to.

#### Example

```csharp
RateLimitListParams parameters = new() { WorkspaceID = "workspace_id" };

var page = await client.Beta.Organization.Workspaces.RateLimits.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`MemberListPage Beta.Organization.Workspaces.Members.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}/members`

List Workspace Members

#### Parameters

- `MemberListParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonElement Type = "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the Workspace Member.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
MemberListParams parameters = new() { WorkspaceID = "workspace_id" };

var page = await client.Beta.Organization.Workspaces.Members.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaWorkspaceMember Beta.Organization.Workspaces.Members.Add(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}/members`

Create Workspace Member

#### Parameters

- `MemberAddParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

  - `required string userID`

    ID of the User.

  - `required BetaNoBillingWorkspaceRole workspaceRole`

    Role of the new Workspace Member. Cannot be `workspace_billing`.

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonElement Type = "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the Workspace Member.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
MemberAddParams parameters = new()
{
    WorkspaceID = "workspace_id",
    UserID = "user_01WCz1FkmYMm4gnmykNKUu3Q",
    WorkspaceRole = BetaNoBillingWorkspaceRole.WorkspaceAdmin,
};

var betaWorkspaceMember = await client.Beta.Organization.Workspaces.Members.Add(parameters);

Console.WriteLine(betaWorkspaceMember);
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

`BetaWorkspaceMember Beta.Organization.Workspaces.Members.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Get Workspace Member

#### Parameters

- `MemberRetrieveParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

  - `required string userID`

    ID of the User.

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonElement Type = "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the Workspace Member.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
MemberRetrieveParams parameters = new()
{
    WorkspaceID = "workspace_id",
    UserID = "user_id",
};

var betaWorkspaceMember = await client.Beta.Organization.Workspaces.Members.Retrieve(parameters);

Console.WriteLine(betaWorkspaceMember);
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

`BetaWorkspaceMember Beta.Organization.Workspaces.Members.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Update Workspace Member

#### Parameters

- `MemberUpdateParams parameters`

  - `required string workspaceID`

    Path param: ID of the Workspace.

  - `required string userID`

    Path param: ID of the User.

  - `required BetaWorkspaceRole workspaceRole`

    Body param: New workspace role for the User.

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonElement Type = "workspace_member"`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the Workspace Member.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
MemberUpdateParams parameters = new()
{
    WorkspaceID = "workspace_id",
    UserID = "user_id",
    WorkspaceRole = BetaWorkspaceRole.WorkspaceAdmin,
};

var betaWorkspaceMember = await client.Beta.Organization.Workspaces.Members.Update(parameters);

Console.WriteLine(betaWorkspaceMember);
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

`MemberRemoveResponse Beta.Organization.Workspaces.Members.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Delete Workspace Member

#### Parameters

- `MemberRemoveParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

  - `required string userID`

    ID of the User.

#### Returns

- `class MemberRemoveResponse:`

  - `JsonElement Type = "workspace_member_deleted"`

    Deleted object type.

    For Workspace Members, this is always `"workspace_member_deleted"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

#### Example

```csharp
MemberRemoveParams parameters = new()
{
    WorkspaceID = "workspace_id",
    UserID = "user_id",
};

var member = await client.Beta.Organization.Workspaces.Members.Remove(parameters);

Console.WriteLine(member);
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

`ServiceAccountListPage Beta.Organization.Workspaces.ServiceAccounts.List(parameters, cancellationToken = default)`

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

- `ServiceAccountListParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `JsonElement Type = "service_account_workspace_member"`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
ServiceAccountListParams parameters = new() { WorkspaceID = "workspace_id" };

var page = await client.Beta.Organization.Workspaces.ServiceAccounts.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaServiceAccountWorkspaceMember Beta.Organization.Workspaces.ServiceAccounts.Add(parameters, cancellationToken = default)`

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

- `ServiceAccountAddParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `required string serviceAccountID`

    Body param: Tagged service account ID to add.

  - `required BetaNoBillingWorkspaceRole workspaceRole`

    Body param: Role to assign to the service account in this workspace.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `JsonElement Type = "service_account_workspace_member"`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
ServiceAccountAddParams parameters = new()
{
    WorkspaceID = "workspace_id",
    ServiceAccountID = "service_account_id",
    WorkspaceRole = BetaNoBillingWorkspaceRole.WorkspaceAdmin,
};

var betaServiceAccountWorkspaceMember = await client.Beta.Organization.Workspaces.ServiceAccounts.Add(parameters);

Console.WriteLine(betaServiceAccountWorkspaceMember);
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

`BetaServiceAccountWorkspaceMember Beta.Organization.Workspaces.ServiceAccounts.Retrieve(parameters, cancellationToken = default)`

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

- `ServiceAccountRetrieveParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `JsonElement Type = "service_account_workspace_member"`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
ServiceAccountRetrieveParams parameters = new()
{
    WorkspaceID = "workspace_id",
    ServiceAccountID = "service_account_id",
};

var betaServiceAccountWorkspaceMember = await client.Beta.Organization.Workspaces.ServiceAccounts.Retrieve(parameters);

Console.WriteLine(betaServiceAccountWorkspaceMember);
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

`BetaServiceAccountWorkspaceMember Beta.Organization.Workspaces.ServiceAccounts.Update(parameters, cancellationToken = default)`

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

- `ServiceAccountUpdateParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `required BetaNoBillingWorkspaceRole workspaceRole`

    Body param: New role for the service account in this workspace.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `JsonElement Type = "service_account_workspace_member"`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin("workspace_admin")`

    - `WorkspaceBilling("workspace_billing")`

    - `WorkspaceDeveloper("workspace_developer")`

    - `WorkspaceRestrictedDeveloper("workspace_restricted_developer")`

    - `WorkspaceUser("workspace_user")`

#### Example

```csharp
ServiceAccountUpdateParams parameters = new()
{
    WorkspaceID = "workspace_id",
    ServiceAccountID = "service_account_id",
    WorkspaceRole = BetaNoBillingWorkspaceRole.WorkspaceAdmin,
};

var betaServiceAccountWorkspaceMember = await client.Beta.Organization.Workspaces.ServiceAccounts.Update(parameters);

Console.WriteLine(betaServiceAccountWorkspaceMember);
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

`ServiceAccountRemoveResponse Beta.Organization.Workspaces.ServiceAccounts.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Removal is idempotent (returns 200 even if the membership was already
removed). A DELETE against the implicit default-workspace membership
returns 200 but is a no-op and the membership persists; deleting an
explicit default-workspace row reverts to the implicit `workspace_user`
membership. Archived workspaces return 400.

#### Parameters

- `ServiceAccountRemoveParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

#### Returns

- `class ServiceAccountRemoveResponse:`

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `JsonElement Type = "service_account_workspace_member_deleted"`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```csharp
ServiceAccountRemoveParams parameters = new()
{
    WorkspaceID = "workspace_id",
    ServiceAccountID = "service_account_id",
};

var serviceAccount = await client.Beta.Organization.Workspaces.ServiceAccounts.Remove(parameters);

Console.WriteLine(serviceAccount);
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

`RateLimitListPage Beta.Organization.RateLimits.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/rate_limits`

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `RateLimitListParams parameters`

  - `GroupType? groupType`

    Filter by group type.

    - `Batch("batch")`

    - `Files("files")`

    - `ModelGroup("model_group")`

    - `Skills("skills")`

    - `TokenCount("token_count")`

    - `WebSearch("web_search")`

  - `long? limit`

    Maximum number of items to return per page. Ranges from `1` to `1000`.

    When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

    maximum: 1000, minimum: 1

  - `string? model`

    Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

  - `string? page`

    Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaOrganizationRateLimit:`

  - `required string ID`

    Stable identifier for this rate-limit group within the organization.

  - `required GroupType GroupType`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `Batch("batch")`

    - `Files("files")`

    - `ModelGroup("model_group")`

    - `Skills("skills")`

    - `TokenCount("token_count")`

    - `WebSearch("web_search")`

  - `required IReadOnlyList<BetaOrganizationRateLimitValue> Limits`

    The limiter values that apply to this group.

    - `required string Type`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `required long Value`

      The configured limit value for this limiter type.

  - `required IReadOnlyList<string>? Models`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `JsonElement Type = "rate_limit"`

    Object type. Always `rate_limit` for organization rate-limit entries.

#### Example

```csharp
RateLimitListParams parameters = new();

var page = await client.Beta.Organization.RateLimits.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaComplianceSettings Beta.Organization.ComplianceSettings.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/compliance_settings`

Retrieve your organization's Compliance Settings.

Compliance Settings is a singleton resource: there is exactly one per
organization, addressed without an identifier. The `state` field reflects
whether the Compliance API is enabled. An organization with a parent
organization reads the state inherited from the parent's configuration.

#### Parameters

- `ComplianceSettingRetrieveParams parameters`

#### Returns

- `class BetaComplianceSettings:`

  - `required State State`

    Whether the Compliance API is enabled for this organization.

    - `class BetaComplianceSettingsStateEnabled:`

      - `JsonElement Type = "enabled"`

    - `class BetaComplianceSettingsStateDisabled:`

      - `JsonElement Type = "disabled"`

  - `JsonElement Type = "compliance_settings"`

#### Example

```csharp
ComplianceSettingRetrieveParams parameters = new();

var betaComplianceSettings = await client.Beta.Organization.ComplianceSettings.Retrieve(parameters);

Console.WriteLine(betaComplianceSettings);
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

`BetaComplianceSettings Beta.Organization.ComplianceSettings.Update(parameters, cancellationToken = default)`

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

- `ComplianceSettingUpdateParams parameters`

  - `required State state`

    Desired state. Accepts the string shorthand "enabled" or "disabled" in place of the object form; the response always returns the canonical object form.

    - `class BetaComplianceSettingsStateEnabledParam:`

      - `JsonElement Type = "enabled"`

    - `class BetaComplianceSettingsStateDisabledParam:`

      - `JsonElement Type = "disabled"`

#### Returns

- `class BetaComplianceSettings:`

  - `required State State`

    Whether the Compliance API is enabled for this organization.

    - `class BetaComplianceSettingsStateEnabled:`

      - `JsonElement Type = "enabled"`

    - `class BetaComplianceSettingsStateDisabled:`

      - `JsonElement Type = "disabled"`

  - `JsonElement Type = "compliance_settings"`

#### Example

```csharp
ComplianceSettingUpdateParams parameters = new()
{
    State = new BetaComplianceSettingsStateEnabledParam()
};

var betaComplianceSettings = await client.Beta.Organization.ComplianceSettings.Update(parameters);

Console.WriteLine(betaComplianceSettings);
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
