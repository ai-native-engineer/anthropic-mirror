<!-- source: https://platform.claude.com/docs/en/api/go/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/go/beta -->

<!-- chunk-start -->

- `serviceAccountID string`

  ID of the service account.

- `params BetaOrganizationServiceAccountWorkspaceListParams`

  - `Limit param.Field[int64] Optional`

    Query param: Number of results per page.

    minimum: 1, maximum: 100

  - `Page param.Field[string] Optional`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaServiceAccountWorkspaceMember`

  - `Type ServiceAccountWorkspaceMember`

    default: service_account_workspace_member

  - `CreatedByActorID string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `Implicit bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `ServiceAccountID string`

    Tagged service account ID (`svac_...`).

  - `WorkspaceID string`

    Tagged workspace ID (`wrkspc_...`).

  - `WorkspaceRole BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `const BetaWorkspaceRoleWorkspaceAdmin BetaWorkspaceRole = "workspace_admin"`

    - `const BetaWorkspaceRoleWorkspaceBilling BetaWorkspaceRole = "workspace_billing"`

    - `const BetaWorkspaceRoleWorkspaceDeveloper BetaWorkspaceRole = "workspace_developer"`

    - `const BetaWorkspaceRoleWorkspaceRestrictedDeveloper BetaWorkspaceRole = "workspace_restricted_developer"`

    - `const BetaWorkspaceRoleWorkspaceUser BetaWorkspaceRole = "workspace_user"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.ServiceAccounts.Workspaces.List(
		context.TODO(),
		"service_account_id",
		anthropic.BetaOrganizationServiceAccountWorkspaceListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
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

`client.Beta.Organization.ServiceAccounts.Workspaces.Remove(ctx, workspaceID, params) (*BetaOrganizationServiceAccountWorkspaceRemoveResponse, error)`

**DELETE** `/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Mirror of `DELETE /workspaces/{workspace_id}/service_accounts/{service_account_id}`,
addressed from the service-account side. Removal is idempotent (returns
200 even if the membership was already removed). A DELETE against the
implicit default-workspace membership returns 200 but is a no-op and the
membership persists; deleting an explicit default-workspace row reverts
to the implicit `workspace_user` membership. Archived workspaces return
400.

#### Parameters

- `workspaceID string`

  ID of the workspace.

- `params BetaOrganizationServiceAccountWorkspaceRemoveParams`

  - `ServiceAccountID param.Field[string]`

    Path param: ID of the service account.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaOrganizationServiceAccountWorkspaceRemoveResponse`

  - `Type ServiceAccountWorkspaceMemberDeleted`

    default: service_account_workspace_member_deleted

  - `ServiceAccountID string`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `WorkspaceID string`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	workspace, err := client.Beta.Organization.ServiceAccounts.Workspaces.Remove(
		context.TODO(),
		"workspace_id",
		anthropic.BetaOrganizationServiceAccountWorkspaceRemoveParams{
			ServiceAccountID: "service_account_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", workspace.ServiceAccountID)
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

`client.Beta.Organization.Users.List(ctx, query) (*Page[BetaOrganizationUser], error)`

**GET** `/v1/organizations/users`

List the organization's members.

#### Parameters

- `query BetaOrganizationUserListParams`

  - `AfterID param.Field[string] Optional`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `BeforeID param.Field[string] Optional`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Email param.Field[string] Optional`

    Filter by user email.

    format: email

  - `Limit param.Field[int64] Optional`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    minimum: 1, maximum: 1000

  - `Roles param.Field[[]string] Optional`

    Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

    Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

#### Returns

- `type BetaOrganizationUser`

  - `Type User`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `ID string`

    ID of the User.

  - `AddedAt Time`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `Email string`

    Email of the User.

  - `Name string`

    Name of the User.

  - `Role BetaOrganizationRole`

    Organization role of the User.

    - `const BetaOrganizationRoleAdmin BetaOrganizationRole = "admin"`

    - `const BetaOrganizationRoleBilling BetaOrganizationRole = "billing"`

    - `const BetaOrganizationRoleClaudeCodeUser BetaOrganizationRole = "claude_code_user"`

    - `const BetaOrganizationRoleDeveloper BetaOrganizationRole = "developer"`

    - `const BetaOrganizationRoleManaged BetaOrganizationRole = "managed"`

    - `const BetaOrganizationRoleMembershipAdmin BetaOrganizationRole = "membership_admin"`

    - `const BetaOrganizationRoleOwner BetaOrganizationRole = "owner"`

    - `const BetaOrganizationRolePrimaryOwner BetaOrganizationRole = "primary_owner"`

    - `const BetaOrganizationRoleUser BetaOrganizationRole = "user"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Users.List(context.TODO(), anthropic.BetaOrganizationUserListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
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

`client.Beta.Organization.Users.Get(ctx, userID) (*BetaOrganizationUser, error)`

**GET** `/v1/organizations/users/{user_id}`

Retrieve a member of the organization by user ID.

#### Parameters

- `userID string`

  ID of the User.

#### Returns

- `type BetaOrganizationUser`

  - `Type User`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `ID string`

    ID of the User.

  - `AddedAt Time`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `Email string`

    Email of the User.

  - `Name string`

    Name of the User.

  - `Role BetaOrganizationRole`

    Organization role of the User.

    - `const BetaOrganizationRoleAdmin BetaOrganizationRole = "admin"`

    - `const BetaOrganizationRoleBilling BetaOrganizationRole = "billing"`

    - `const BetaOrganizationRoleClaudeCodeUser BetaOrganizationRole = "claude_code_user"`

    - `const BetaOrganizationRoleDeveloper BetaOrganizationRole = "developer"`

    - `const BetaOrganizationRoleManaged BetaOrganizationRole = "managed"`

    - `const BetaOrganizationRoleMembershipAdmin BetaOrganizationRole = "membership_admin"`

    - `const BetaOrganizationRoleOwner BetaOrganizationRole = "owner"`

    - `const BetaOrganizationRolePrimaryOwner BetaOrganizationRole = "primary_owner"`

    - `const BetaOrganizationRoleUser BetaOrganizationRole = "user"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaOrganizationUser, err := client.Beta.Organization.Users.Get(context.TODO(), "user_id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaOrganizationUser.ID)
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

`client.Beta.Organization.Users.Update(ctx, userID, body) (*BetaOrganizationUser, error)`

**POST** `/v1/organizations/users/{user_id}`

Update a member's organization role.

#### Parameters

- `userID string`

  ID of the User.

- `body BetaOrganizationUserUpdateParams`

  - `Role param.Field[BetaOrganizationUserUpdateParamsRole]`

    New role for the User.

    The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

    - `const BetaOrganizationUserUpdateParamsRoleBilling BetaOrganizationUserUpdateParamsRole = "billing"`

    - `const BetaOrganizationUserUpdateParamsRoleClaudeCodeUser BetaOrganizationUserUpdateParamsRole = "claude_code_user"`

    - `const BetaOrganizationUserUpdateParamsRoleDeveloper BetaOrganizationUserUpdateParamsRole = "developer"`

    - `const BetaOrganizationUserUpdateParamsRoleManaged BetaOrganizationUserUpdateParamsRole = "managed"`

    - `const BetaOrganizationUserUpdateParamsRoleUser BetaOrganizationUserUpdateParamsRole = "user"`

#### Returns

- `type BetaOrganizationUser`

  - `Type User`

    Object type.

    For Users, this is always `"user"`.

    default: user

  - `ID string`

    ID of the User.

  - `AddedAt Time`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `Email string`

    Email of the User.

  - `Name string`

    Name of the User.

  - `Role BetaOrganizationRole`

    Organization role of the User.

    - `const BetaOrganizationRoleAdmin BetaOrganizationRole = "admin"`

    - `const BetaOrganizationRoleBilling BetaOrganizationRole = "billing"`

    - `const BetaOrganizationRoleClaudeCodeUser BetaOrganizationRole = "claude_code_user"`

    - `const BetaOrganizationRoleDeveloper BetaOrganizationRole = "developer"`

    - `const BetaOrganizationRoleManaged BetaOrganizationRole = "managed"`

    - `const BetaOrganizationRoleMembershipAdmin BetaOrganizationRole = "membership_admin"`

    - `const BetaOrganizationRoleOwner BetaOrganizationRole = "owner"`

    - `const BetaOrganizationRolePrimaryOwner BetaOrganizationRole = "primary_owner"`

    - `const BetaOrganizationRoleUser BetaOrganizationRole = "user"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaOrganizationUser, err := client.Beta.Organization.Users.Update(
		context.TODO(),
		"user_id",
		anthropic.BetaOrganizationUserUpdateParams{
			Role: anthropic.BetaOrganizationUserUpdateParamsRoleUser,
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaOrganizationUser.ID)
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

`client.Beta.Organization.Users.Remove(ctx, userID) (*BetaOrganizationUserRemoveResponse, error)`

**DELETE** `/v1/organizations/users/{user_id}`

Remove a member from the organization.

#### Parameters

- `userID string`

  ID of the User.

#### Returns

- `type BetaOrganizationUserRemoveResponse`

  - `Type UserDeleted`

    Deleted object type.

    For Users, this is always `"user_deleted"`.

    default: user_deleted

  - `ID string`

    ID of the User.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	user, err := client.Beta.Organization.Users.Remove(context.TODO(), "user_id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", user.ID)
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

`client.Beta.Organization.Workspaces.List(ctx, query) (*Page[BetaWorkspace], error)`

**GET** `/v1/organizations/workspaces`

List Workspaces

#### Parameters

- `query BetaOrganizationWorkspaceListParams`

  - `AfterID param.Field[string] Optional`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `BeforeID param.Field[string] Optional`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `IncludeArchived param.Field[bool] Optional`

    Whether to include Workspaces that have been archived in the response

  - `IncludeDefault param.Field[bool] Optional`

    Whether to include the organization's default Workspace in the response

  - `Limit param.Field[int64] Optional`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    minimum: 1, maximum: 1000

#### Returns

- `type BetaWorkspace`

  - `Type Workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `ID string`

    ID of the Workspace.

  - `ArchivedAt Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `CompartmentID string`

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

  - `CreatedAt Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `DataResidency BetaDataResidency`

    Data residency configuration.

    - `AllowedInferenceGeos BetaDataResidencyAllowedInferenceGeosUnion`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `type BetaDataResidencyAllowedInferenceGeosGeos []BetaAllowedInferenceGeo`

        - `const BetaAllowedInferenceGeoGlobal BetaAllowedInferenceGeo = "global"`

        - `const BetaAllowedInferenceGeoUs BetaAllowedInferenceGeo = "us"`

      - `type Unrestricted string`

    - `DefaultInferenceGeo BetaDataResidencyDefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

      - `const BetaDataResidencyDefaultInferenceGeoGlobal BetaDataResidencyDefaultInferenceGeo = "global"`

      - `const BetaDataResidencyDefaultInferenceGeoUs BetaDataResidencyDefaultInferenceGeo = "us"`

    - `WorkspaceGeo BetaDataResidencyWorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `DisplayColor string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `ExternalKeyID string`

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

  - `Name string`

    Name of the Workspace.

  - `Tags map[string, string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Workspaces.List(context.TODO(), anthropic.BetaOrganizationWorkspaceListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
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
        "default_inference_geo": "global",
        "workspace_geo": "us"
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

`client.Beta.Organization.Workspaces.New(ctx, params) (*BetaWorkspace, error)`

**POST** `/v1/organizations/workspaces`

Create Workspace

#### Parameters

- `params BetaOrganizationWorkspaceNewParams`

  - `Name param.Field[string]`

    Body param: Name of the Workspace.

    minLength: 1, maxLength: 40

  - `DataResidency param.Field[BetaDataResidencyCreateConfig] Optional`

    Body param: Data residency configuration for the workspace. If omitted, defaults to `workspace_geo: "us"`, `allowed_inference_geos: "unrestricted"`, and `default_inference_geo: "global"`.

  - `DisplayColor param.Field[string] Optional`

    Body param: Hex color code representing the Workspace in the Anthropic Console.

    maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

  - `ExternalKeyID param.Field[string] Optional`

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

  - `Tags param.Field[map[string, string]] Optional`

    Body param: User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaWorkspace`

  - `Type Workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `ID string`

    ID of the Workspace.

  - `ArchivedAt Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `CompartmentID string`

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

  - `CreatedAt Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `DataResidency BetaDataResidency`

    Data residency configuration.

    - `AllowedInferenceGeos BetaDataResidencyAllowedInferenceGeosUnion`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `type BetaDataResidencyAllowedInferenceGeosGeos []BetaAllowedInferenceGeo`

        - `const BetaAllowedInferenceGeoGlobal BetaAllowedInferenceGeo = "global"`

        - `const BetaAllowedInferenceGeoUs BetaAllowedInferenceGeo = "us"`

      - `type Unrestricted string`

    - `DefaultInferenceGeo BetaDataResidencyDefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

      - `const BetaDataResidencyDefaultInferenceGeoGlobal BetaDataResidencyDefaultInferenceGeo = "global"`

      - `const BetaDataResidencyDefaultInferenceGeoUs BetaDataResidencyDefaultInferenceGeo = "us"`

    - `WorkspaceGeo BetaDataResidencyWorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `DisplayColor string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `ExternalKeyID string`

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

  - `Name string`

    Name of the Workspace.

  - `Tags map[string, string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaWorkspace, err := client.Beta.Organization.Workspaces.New(context.TODO(), anthropic.BetaOrganizationWorkspaceNewParams{
		Name: "x",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaWorkspace.ID)
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
    "default_inference_geo": "global",
    "workspace_geo": "us"
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

`client.Beta.Organization.Workspaces.Get(ctx, workspaceID) (*BetaWorkspace, error)`

**GET** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

#### Parameters

- `workspaceID string`

  ID of the Workspace.

#### Returns

- `type BetaWorkspace`

  - `Type Workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `ID string`

    ID of the Workspace.

  - `ArchivedAt Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `CompartmentID string`

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

  - `CreatedAt Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `DataResidency BetaDataResidency`

    Data residency configuration.

    - `AllowedInferenceGeos BetaDataResidencyAllowedInferenceGeosUnion`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `type BetaDataResidencyAllowedInferenceGeosGeos []BetaAllowedInferenceGeo`

        - `const BetaAllowedInferenceGeoGlobal BetaAllowedInferenceGeo = "global"`

        - `const BetaAllowedInferenceGeoUs BetaAllowedInferenceGeo = "us"`

      - `type Unrestricted string`

    - `DefaultInferenceGeo BetaDataResidencyDefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

      - `const BetaDataResidencyDefaultInferenceGeoGlobal BetaDataResidencyDefaultInferenceGeo = "global"`

      - `const BetaDataResidencyDefaultInferenceGeoUs BetaDataResidencyDefaultInferenceGeo = "us"`

    - `WorkspaceGeo BetaDataResidencyWorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `DisplayColor string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `ExternalKeyID string`

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

  - `Name string`

    Name of the Workspace.

  - `Tags map[string, string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaWorkspace, err := client.Beta.Organization.Workspaces.Get(context.TODO(), "workspace_id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaWorkspace.ID)
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
    "default_inference_geo": "global",
    "workspace_geo": "us"
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

`client.Beta.Organization.Workspaces.Update(ctx, workspaceID, body) (*BetaWorkspace, error)`

**POST** `/v1/organizations/workspaces/{workspace_id}`

Update Workspace

#### Parameters

- `workspaceID string`

- `body BetaOrganizationWorkspaceUpdateParams`

  - `DataResidency param.Field[BetaDataResidencyUpdateConfig] Optional`

    Data residency configuration for the workspace.

  - `DisplayColor param.Field[string] Optional`

    Hex color code representing the Workspace in the Anthropic Console.

    maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

  - `ExternalKeyID param.Field[string] Optional`

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

  - `Name param.Field[string] Optional`

    Name of the Workspace.

    minLength: 1, maxLength: 40

  - `Tags param.Field[map[string, string]] Optional`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Returns

- `type BetaWorkspace`

  - `Type Workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `ID string`

    ID of the Workspace.

  - `ArchivedAt Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `CompartmentID string`

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

  - `CreatedAt Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `DataResidency BetaDataResidency`

    Data residency configuration.

    - `AllowedInferenceGeos BetaDataResidencyAllowedInferenceGeosUnion`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `type BetaDataResidencyAllowedInferenceGeosGeos []BetaAllowedInferenceGeo`

        - `const BetaAllowedInferenceGeoGlobal BetaAllowedInferenceGeo = "global"`

        - `const BetaAllowedInferenceGeoUs BetaAllowedInferenceGeo = "us"`

      - `type Unrestricted string`

    - `DefaultInferenceGeo BetaDataResidencyDefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

      - `const BetaDataResidencyDefaultInferenceGeoGlobal BetaDataResidencyDefaultInferenceGeo = "global"`

      - `const BetaDataResidencyDefaultInferenceGeoUs BetaDataResidencyDefaultInferenceGeo = "us"`

    - `WorkspaceGeo BetaDataResidencyWorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `DisplayColor string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `ExternalKeyID string`

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

  - `Name string`

    Name of the Workspace.

  - `Tags map[string, string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaWorkspace, err := client.Beta.Organization.Workspaces.Update(
		context.TODO(),
		"workspace_id",
		anthropic.BetaOrganizationWorkspaceUpdateParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaWorkspace.ID)
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
    "default_inference_geo": "global",
    "workspace_geo": "us"
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

`client.Beta.Organization.Workspaces.Archive(ctx, workspaceID) (*BetaWorkspace, error)`

**POST** `/v1/organizations/workspaces/{workspace_id}/archive`

Archive Workspace

#### Parameters

- `workspaceID string`

#### Returns

- `type BetaWorkspace`

  - `Type Workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

    default: workspace

  - `ID string`

    ID of the Workspace.

  - `ArchivedAt Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `CompartmentID string`

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

  - `CreatedAt Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `DataResidency BetaDataResidency`

    Data residency configuration.

    - `AllowedInferenceGeos BetaDataResidencyAllowedInferenceGeosUnion`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `type BetaDataResidencyAllowedInferenceGeosGeos []BetaAllowedInferenceGeo`

        - `const BetaAllowedInferenceGeoGlobal BetaAllowedInferenceGeo = "global"`

        - `const BetaAllowedInferenceGeoUs BetaAllowedInferenceGeo = "us"`

      - `type Unrestricted string`

    - `DefaultInferenceGeo BetaDataResidencyDefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

      - `const BetaDataResidencyDefaultInferenceGeoGlobal BetaDataResidencyDefaultInferenceGeo = "global"`

      - `const BetaDataResidencyDefaultInferenceGeoUs BetaDataResidencyDefaultInferenceGeo = "us"`

    - `WorkspaceGeo BetaDataResidencyWorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `DisplayColor string`

    Hex color code representing the Workspace in the Anthropic Console.

  - `ExternalKeyID string`

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

  - `Name string`

    Name of the Workspace.

  - `Tags map[string, string]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaWorkspace, err := client.Beta.Organization.Workspaces.Archive(context.TODO(), "workspace_id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaWorkspace.ID)
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
    "default_inference_geo": "global",
    "workspace_geo": "us"
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

`client.Beta.Organization.Workspaces.RateLimits.List(ctx, workspaceID, query) (*PageCursor[BetaWorkspaceRateLimit], error)`

**GET** `/v1/organizations/workspaces/{workspace_id}/rate_limits`

List a workspace's rate limits.

By default, returns only the groups and limiter types that have a
workspace-level override. With `include_inherited=true`, returns every
group with organization-level limits the workspace can see, listing for
each the values it inherits from the organization as well as its own
overrides. Each value's `source` says which it is.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `workspaceID string`

  The ID of the workspace.

- `query BetaOrganizationWorkspaceRateLimitListParams`

  - `GroupType param.Field[BetaOrganizationWorkspaceRateLimitListParamsGroupType] Optional`

    Filter by group type.

    - `const BetaOrganizationWorkspaceRateLimitListParamsGroupTypeBatch BetaOrganizationWorkspaceRateLimitListParamsGroupType = "batch"`

    - `const BetaOrganizationWorkspaceRateLimitListParamsGroupTypeFiles BetaOrganizationWorkspaceRateLimitListParamsGroupType = "files"`

    - `const BetaOrganizationWorkspaceRateLimitListParamsGroupTypeModelGroup BetaOrganizationWorkspaceRateLimitListParamsGroupType = "model_group"`

    - `const BetaOrganizationWorkspaceRateLimitListParamsGroupTypeSkills BetaOrganizationWorkspaceRateLimitListParamsGroupType = "skills"`

    - `const BetaOrganizationWorkspaceRateLimitListParamsGroupTypeTokenCount BetaOrganizationWorkspaceRateLimitListParamsGroupType = "token_count"`

    - `const BetaOrganizationWorkspaceRateLimitListParamsGroupTypeWebSearch BetaOrganizationWorkspaceRateLimitListParamsGroupType = "web_search"`

  - `IncludeInherited param.Field[bool] Optional`

    Also list the limiter values the workspace inherits from the organization, including groups with no workspace-level override.

  - `Limit param.Field[int64] Optional`

    Maximum number of items to return per page. Ranges from `1` to `1000`.

    When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

    minimum: 1, maximum: 1000

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page`.

#### Returns

- `type BetaWorkspaceRateLimit`

  - `Type WorkspaceRateLimit`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

    default: workspace_rate_limit

  - `Group BetaWorkspaceRateLimitGroupUnion`

    The rate-limit group this entry's limits apply to. Its `type` equals `group_type`.

    - `type BetaOrganizationRateLimitModelGroup`

      - `Type ModelGroup`

        Always `model_group`: a family of models.

        default: model_group

      - `ID string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

      - `DisplayName string`

        Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.

    - `type BetaOrganizationRateLimitBatchGroup`

      - `Type Batch`

        Always `batch`: the Message Batches API.

        default: batch

      - `ID string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `type BetaOrganizationRateLimitTokenCountGroup`

      - `Type TokenCount`

        Always `token_count`: the Token Count API.

        default: token_count

      - `ID string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `type BetaOrganizationRateLimitFilesGroup`

      - `Type Files`

        Always `files`: the Files API.

        default: files

      - `ID string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `type BetaOrganizationRateLimitSkillsGroup`

      - `Type Skills`

        Always `skills`: the Skills API.

        default: skills

      - `ID string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `type BetaOrganizationRateLimitWebSearchGroup`

      - `Type WebSearch`

        Always `web_search`: the Messages API web search tool.

        default: web_search

      - `ID string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

  - `Limits []BetaWorkspaceRateLimitValue`

    The workspace's limiter values for this group. By default only the limiter types with a workspace-level override are listed. With `include_inherited` set to `true`, the limiter types the workspace inherits from the organization are listed too, each marked by `source`.

    - `Type string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `OrgLimit int64`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `Source BetaWorkspaceRateLimitValueSourceUnion`

      Where `value` comes from. `organization` values are listed only when `include_inherited` is `true`, and then `value` equals `org_limit`.

      - `type BetaWorkspaceRateLimitWorkspaceSource`

        - `Type Workspace`

          Always `workspace`: a workspace-level override is stored.

          default: workspace

      - `type BetaWorkspaceRateLimitOrganizationSource`

        - `Type Organization`

          Always `organization`: no workspace-level override is stored, so the organization's value applies.

          default: organization

    - `Value int64`

      The workspace's value for this limiter type: the workspace-level override when `source.type` is `workspace`, otherwise the organization's value.

  - `Models []string`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `RateLimitID string`

    The `id` of the organization's RateLimit entry this entry applies to.

  - `WorkspaceID string`

    ID of the Workspace this entry applies to.

  - `GroupType BetaWorkspaceRateLimitGroupType`

    **Deprecated**: Use `group.type` instead. `group_type` is still returned and always equals `group.type`.

    Deprecated: use `group.type` instead. The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`. Always equal to `group.type`.

    - `const BetaWorkspaceRateLimitGroupTypeBatch BetaWorkspaceRateLimitGroupType = "batch"`

    - `const BetaWorkspaceRateLimitGroupTypeFiles BetaWorkspaceRateLimitGroupType = "files"`

    - `const BetaWorkspaceRateLimitGroupTypeModelGroup BetaWorkspaceRateLimitGroupType = "model_group"`

    - `const BetaWorkspaceRateLimitGroupTypeSkills BetaWorkspaceRateLimitGroupType = "skills"`

    - `const BetaWorkspaceRateLimitGroupTypeTokenCount BetaWorkspaceRateLimitGroupType = "token_count"`

    - `const BetaWorkspaceRateLimitGroupTypeWebSearch BetaWorkspaceRateLimitGroupType = "web_search"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Workspaces.RateLimits.List(
		context.TODO(),
		"workspace_id",
		anthropic.BetaOrganizationWorkspaceRateLimitListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "group": {
        "id": "id",
        "display_name": "display_name",
        "type": "model_group"
      },
      "group_type": "batch",
      "limits": [
        {
          "org_limit": 0,
          "source": {
            "type": "workspace"
          },
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

`client.Beta.Organization.Workspaces.Members.List(ctx, workspaceID, query) (*Page[BetaWorkspaceMember], error)`

**GET** `/v1/organizations/workspaces/{workspace_id}/members`

List Workspace Members

#### Parameters

- `workspaceID string`

  ID of the Workspace.

- `query BetaOrganizationWorkspaceMemberListParams`

  - `AfterID param.Field[string] Optional`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `BeforeID param.Field[string] Optional`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Limit param.Field[int64] Optional`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    minimum: 1, maximum: 1000

#### Returns

- `type BetaWorkspaceMember`

  - `Type WorkspaceMember`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `UserID string`

    ID of the User.

  - `WorkspaceID string`

    ID of the Workspace.

  - `WorkspaceRole BetaWorkspaceRole`

    Role of the Workspace Member.

    - `const BetaWorkspaceRoleWorkspaceAdmin BetaWorkspaceRole = "workspace_admin"`

    - `const BetaWorkspaceRoleWorkspaceBilling BetaWorkspaceRole = "workspace_billing"`

    - `const BetaWorkspaceRoleWorkspaceDeveloper BetaWorkspaceRole = "workspace_developer"`

    - `const BetaWorkspaceRoleWorkspaceRestrictedDeveloper BetaWorkspaceRole = "workspace_restricted_developer"`

    - `const BetaWorkspaceRoleWorkspaceUser BetaWorkspaceRole = "workspace_user"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Workspaces.Members.List(
		context.TODO(),
		"workspace_id",
		anthropic.BetaOrganizationWorkspaceMemberListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
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

`client.Beta.Organization.Workspaces.Members.Add(ctx, workspaceID, body) (*BetaWorkspaceMember, error)`

**POST** `/v1/organizations/workspaces/{workspace_id}/members`

Create Workspace Member

#### Parameters

- `workspaceID string`

  ID of the Workspace.

- `body BetaOrganizationWorkspaceMemberAddParams`

  - `UserID param.Field[string]`

    ID of the User.

  - `WorkspaceRole param.Field[BetaNoBillingWorkspaceRole]`

    Role of the new Workspace Member. Cannot be `workspace_billing`.

#### Returns

- `type BetaWorkspaceMember`

  - `Type WorkspaceMember`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `UserID string`

    ID of the User.

  - `WorkspaceID string`

    ID of the Workspace.

  - `WorkspaceRole BetaWorkspaceRole`

    Role of the Workspace Member.

    - `const BetaWorkspaceRoleWorkspaceAdmin BetaWorkspaceRole = "workspace_admin"`

    - `const BetaWorkspaceRoleWorkspaceBilling BetaWorkspaceRole = "workspace_billing"`

    - `const BetaWorkspaceRoleWorkspaceDeveloper BetaWorkspaceRole = "workspace_developer"`

    - `const BetaWorkspaceRoleWorkspaceRestrictedDeveloper BetaWorkspaceRole = "workspace_restricted_developer"`

    - `const BetaWorkspaceRoleWorkspaceUser BetaWorkspaceRole = "workspace_user"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaWorkspaceMember, err := client.Beta.Organization.Workspaces.Members.Add(
		context.TODO(),
		"workspace_id",
		anthropic.BetaOrganizationWorkspaceMemberAddParams{
			UserID:        "user_01WCz1FkmYMm4gnmykNKUu3Q",
			WorkspaceRole: anthropic.BetaNoBillingWorkspaceRoleWorkspaceAdmin,
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaWorkspaceMember.UserID)
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

`client.Beta.Organization.Workspaces.Members.Get(ctx, userID, query) (*BetaWorkspaceMember, error)`

**GET** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Get Workspace Member

#### Parameters

- `userID string`

  ID of the User.

- `query BetaOrganizationWorkspaceMemberGetParams`

  - `WorkspaceID param.Field[string]`

    ID of the Workspace.

#### Returns

- `type BetaWorkspaceMember`

  - `Type WorkspaceMember`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `UserID string`

    ID of the User.

  - `WorkspaceID string`

    ID of the Workspace.

  - `WorkspaceRole BetaWorkspaceRole`

    Role of the Workspace Member.

    - `const BetaWorkspaceRoleWorkspaceAdmin BetaWorkspaceRole = "workspace_admin"`

    - `const BetaWorkspaceRoleWorkspaceBilling BetaWorkspaceRole = "workspace_billing"`

    - `const BetaWorkspaceRoleWorkspaceDeveloper BetaWorkspaceRole = "workspace_developer"`

    - `const BetaWorkspaceRoleWorkspaceRestrictedDeveloper BetaWorkspaceRole = "workspace_restricted_developer"`

    - `const BetaWorkspaceRoleWorkspaceUser BetaWorkspaceRole = "workspace_user"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaWorkspaceMember, err := client.Beta.Organization.Workspaces.Members.Get(
		context.TODO(),
		"user_id",
		anthropic.BetaOrganizationWorkspaceMemberGetParams{
			WorkspaceID: "workspace_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaWorkspaceMember.UserID)
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

`client.Beta.Organization.Workspaces.Members.Update(ctx, userID, params) (*BetaWorkspaceMember, error)`

**POST** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Update Workspace Member

#### Parameters

- `userID string`

  ID of the User.

- `params BetaOrganizationWorkspaceMemberUpdateParams`

  - `WorkspaceID param.Field[string]`

    Path param: ID of the Workspace.

  - `WorkspaceRole param.Field[BetaWorkspaceRole]`

    Body param: New workspace role for the User.

#### Returns

- `type BetaWorkspaceMember`

  - `Type WorkspaceMember`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

    default: workspace_member

  - `UserID string`

    ID of the User.

  - `WorkspaceID string`

    ID of the Workspace.

  - `WorkspaceRole BetaWorkspaceRole`

    Role of the Workspace Member.

    - `const BetaWorkspaceRoleWorkspaceAdmin BetaWorkspaceRole = "workspace_admin"`

    - `const BetaWorkspaceRoleWorkspaceBilling BetaWorkspaceRole = "workspace_billing"`

    - `const BetaWorkspaceRoleWorkspaceDeveloper BetaWorkspaceRole = "workspace_developer"`

    - `const BetaWorkspaceRoleWorkspaceRestrictedDeveloper BetaWorkspaceRole = "workspace_restricted_developer"`

    - `const BetaWorkspaceRoleWorkspaceUser BetaWorkspaceRole = "workspace_user"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaWorkspaceMember, err := client.Beta.Organization.Workspaces.Members.Update(
		context.TODO(),
		"user_id",
		anthropic.BetaOrganizationWorkspaceMemberUpdateParams{
			WorkspaceID:   "workspace_id",
			WorkspaceRole: anthropic.BetaWorkspaceRoleWorkspaceAdmin,
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaWorkspaceMember.UserID)
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

`client.Beta.Organization.Workspaces.Members.Remove(ctx, userID, body) (*BetaOrganizationWorkspaceMemberRemoveResponse, error)`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Delete Workspace Member

#### Parameters

- `userID string`

  ID of the User.

- `body BetaOrganizationWorkspaceMemberRemoveParams`

  - `WorkspaceID param.Field[string]`

    ID of the Workspace.

#### Returns

- `type BetaOrganizationWorkspaceMemberRemoveResponse`

  - `Type WorkspaceMemberDeleted`

    Deleted object type.

    For Workspace Members, this is always `"workspace_member_deleted"`.

    default: workspace_member_deleted

  - `UserID string`

    ID of the User.

  - `WorkspaceID string`

    ID of the Workspace.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	member, err := client.Beta.Organization.Workspaces.Members.Remove(
		context.TODO(),
		"user_id",
		anthropic.BetaOrganizationWorkspaceMemberRemoveParams{
			WorkspaceID: "workspace_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", member.UserID)
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

`client.Beta.Organization.Workspaces.ServiceAccounts.List(ctx, workspaceID, params) (*PageCursor[BetaServiceAccountWorkspaceMember], error)`

**GET** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

List the service accounts that are members of a workspace.

Each entry includes the service account's `workspace_role`. Use `limit`
and the `next_page` cursor to paginate. Archived workspaces return 400;
use `GET /service_accounts/{id}/workspaces` to audit memberships of an
archived workspace. The implicit default-workspace membership is not
included in this list. Memberships of archived service accounts are
omitted from the results.

#### Parameters

- `workspaceID string`

  ID of the workspace.

- `params BetaOrganizationWorkspaceServiceAccountListParams`

  - `Limit param.Field[int64] Optional`

    Query param: Number of results per page.

    minimum: 1, maximum: 100

  - `Page param.Field[string] Optional`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaServiceAccountWorkspaceMember`

  - `Type ServiceAccountWorkspaceMember`

    default: service_account_workspace_member

  - `CreatedByActorID string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `Implicit bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `ServiceAccountID string`

    Tagged service account ID (`svac_...`).

  - `WorkspaceID string`

    Tagged workspace ID (`wrkspc_...`).

  - `WorkspaceRole BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `const BetaWorkspaceRoleWorkspaceAdmin BetaWorkspaceRole = "workspace_admin"`

    - `const BetaWorkspaceRoleWorkspaceBilling BetaWorkspaceRole = "workspace_billing"`

    - `const BetaWorkspaceRoleWorkspaceDeveloper BetaWorkspaceRole = "workspace_developer"`

    - `const BetaWorkspaceRoleWorkspaceRestrictedDeveloper BetaWorkspaceRole = "workspace_restricted_developer"`

    - `const BetaWorkspaceRoleWorkspaceUser BetaWorkspaceRole = "workspace_user"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Workspaces.ServiceAccounts.List(
		context.TODO(),
		"workspace_id",
		anthropic.BetaOrganizationWorkspaceServiceAccountListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
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

`client.Beta.Organization.Workspaces.ServiceAccounts.Add(ctx, workspaceID, params) (*BetaServiceAccountWorkspaceMember, error)`

**POST** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

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

- `workspaceID string`

  ID of the workspace.

- `params BetaOrganizationWorkspaceServiceAccountAddParams`

  - `ServiceAccountID param.Field[string]`

    Body param: Tagged service account ID to add.

  - `WorkspaceRole param.Field[BetaNoBillingWorkspaceRole]`

    Body param: Role to assign to the service account in this workspace.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaServiceAccountWorkspaceMember`

  - `Type ServiceAccountWorkspaceMember`

    default: service_account_workspace_member

  - `CreatedByActorID string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `Implicit bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `ServiceAccountID string`

    Tagged service account ID (`svac_...`).

  - `WorkspaceID string`

    Tagged workspace ID (`wrkspc_...`).

  - `WorkspaceRole BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `const BetaWorkspaceRoleWorkspaceAdmin BetaWorkspaceRole = "workspace_admin"`

    - `const BetaWorkspaceRoleWorkspaceBilling BetaWorkspaceRole = "workspace_billing"`

    - `const BetaWorkspaceRoleWorkspaceDeveloper BetaWorkspaceRole = "workspace_developer"`

    - `const BetaWorkspaceRoleWorkspaceRestrictedDeveloper BetaWorkspaceRole = "workspace_restricted_developer"`

    - `const BetaWorkspaceRoleWorkspaceUser BetaWorkspaceRole = "workspace_user"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaServiceAccountWorkspaceMember, err := client.Beta.Organization.Workspaces.ServiceAccounts.Add(
		context.TODO(),
		"workspace_id",
		anthropic.BetaOrganizationWorkspaceServiceAccountAddParams{
			ServiceAccountID: "service_account_id",
			WorkspaceRole:    anthropic.BetaNoBillingWorkspaceRoleWorkspaceAdmin,
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaServiceAccountWorkspaceMember.CreatedByActorID)
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

`client.Beta.Organization.Workspaces.ServiceAccounts.Get(ctx, serviceAccountID, params) (*BetaServiceAccountWorkspaceMember, error)`

**GET** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Retrieve a service account's membership in a workspace.

Returns the membership record, including the service account's
`workspace_role` in this workspace. Archived workspaces return 400. For
the default workspace, returns the implicit (`implicit: true`)
membership when no explicit membership exists; an explicitly added
membership is returned with its assigned role. An archived service
account returns 404.

#### Parameters

- `serviceAccountID string`

  ID of the service account.

- `params BetaOrganizationWorkspaceServiceAccountGetParams`

  - `WorkspaceID param.Field[string]`

    Path param: ID of the workspace.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaServiceAccountWorkspaceMember`

  - `Type ServiceAccountWorkspaceMember`

    default: service_account_workspace_member

  - `CreatedByActorID string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `Implicit bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `ServiceAccountID string`

    Tagged service account ID (`svac_...`).

  - `WorkspaceID string`

    Tagged workspace ID (`wrkspc_...`).

  - `WorkspaceRole BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `const BetaWorkspaceRoleWorkspaceAdmin BetaWorkspaceRole = "workspace_admin"`

    - `const BetaWorkspaceRoleWorkspaceBilling BetaWorkspaceRole = "workspace_billing"`

    - `const BetaWorkspaceRoleWorkspaceDeveloper BetaWorkspaceRole = "workspace_developer"`

    - `const BetaWorkspaceRoleWorkspaceRestrictedDeveloper BetaWorkspaceRole = "workspace_restricted_developer"`

    - `const BetaWorkspaceRoleWorkspaceUser BetaWorkspaceRole = "workspace_user"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaServiceAccountWorkspaceMember, err := client.Beta.Organization.Workspaces.ServiceAccounts.Get(
		context.TODO(),
		"service_account_id",
		anthropic.BetaOrganizationWorkspaceServiceAccountGetParams{
			WorkspaceID: "workspace_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaServiceAccountWorkspaceMember.CreatedByActorID)
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

`client.Beta.Organization.Workspaces.ServiceAccounts.Update(ctx, serviceAccountID, params) (*BetaServiceAccountWorkspaceMember, error)`

**POST** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Change a service account's role in a workspace.

The new `workspace_role` replaces the current one. Only explicit
memberships can be updated; to set a role on the implicit
default-workspace membership, add the service account explicitly with
`POST /workspaces/{workspace_id}/service_accounts`. Archived workspaces
return 400. Archived service accounts cannot be updated and are
rejected.

#### Parameters

- `serviceAccountID string`

  ID of the service account.

- `params BetaOrganizationWorkspaceServiceAccountUpdateParams`

  - `WorkspaceID param.Field[string]`

    Path param: ID of the workspace.

  - `WorkspaceRole param.Field[BetaNoBillingWorkspaceRole]`

    Body param: New role for the service account in this workspace.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaServiceAccountWorkspaceMember`

  - `Type ServiceAccountWorkspaceMember`

    default: service_account_workspace_member

  - `CreatedByActorID string`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `Implicit bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `ServiceAccountID string`

    Tagged service account ID (`svac_...`).

  - `WorkspaceID string`

    Tagged workspace ID (`wrkspc_...`).

  - `WorkspaceRole BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `const BetaWorkspaceRoleWorkspaceAdmin BetaWorkspaceRole = "workspace_admin"`

    - `const BetaWorkspaceRoleWorkspaceBilling BetaWorkspaceRole = "workspace_billing"`

    - `const BetaWorkspaceRoleWorkspaceDeveloper BetaWorkspaceRole = "workspace_developer"`

    - `const BetaWorkspaceRoleWorkspaceRestrictedDeveloper BetaWorkspaceRole = "workspace_restricted_developer"`

    - `const BetaWorkspaceRoleWorkspaceUser BetaWorkspaceRole = "workspace_user"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaServiceAccountWorkspaceMember, err := client.Beta.Organization.Workspaces.ServiceAccounts.Update(
		context.TODO(),
		"service_account_id",
		anthropic.BetaOrganizationWorkspaceServiceAccountUpdateParams{
			WorkspaceID:   "workspace_id",
			WorkspaceRole: anthropic.BetaNoBillingWorkspaceRoleWorkspaceAdmin,
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaServiceAccountWorkspaceMember.CreatedByActorID)
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

`client.Beta.Organization.Workspaces.ServiceAccounts.Remove(ctx, serviceAccountID, params) (*BetaOrganizationWorkspaceServiceAccountRemoveResponse, error)`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Removal is idempotent (returns 200 even if the membership was already
removed). A DELETE against the implicit default-workspace membership
returns 200 but is a no-op and the membership persists; deleting an
explicit default-workspace row reverts to the implicit `workspace_user`
membership. Archived workspaces return 400.

#### Parameters

- `serviceAccountID string`

  ID of the service account.

- `params BetaOrganizationWorkspaceServiceAccountRemoveParams`

  - `WorkspaceID param.Field[string]`

    Path param: ID of the workspace.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaOrganizationWorkspaceServiceAccountRemoveResponse`

  - `Type ServiceAccountWorkspaceMemberDeleted`

    default: service_account_workspace_member_deleted

  - `ServiceAccountID string`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `WorkspaceID string`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	serviceAccount, err := client.Beta.Organization.Workspaces.ServiceAccounts.Remove(
		context.TODO(),
		"service_account_id",
		anthropic.BetaOrganizationWorkspaceServiceAccountRemoveParams{
			WorkspaceID: "workspace_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", serviceAccount.ServiceAccountID)
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

`client.Beta.Organization.RateLimits.List(ctx, query) (*PageCursor[BetaOrganizationRateLimit], error)`

**GET** `/v1/organizations/rate_limits`

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Message Batches API or the web
search tool) and contains the set of limiter values that apply to it.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `query BetaOrganizationRateLimitListParams`

  - `GroupType param.Field[BetaOrganizationRateLimitListParamsGroupType] Optional`

    Filter by group type.

    - `const BetaOrganizationRateLimitListParamsGroupTypeBatch BetaOrganizationRateLimitListParamsGroupType = "batch"`

    - `const BetaOrganizationRateLimitListParamsGroupTypeFiles BetaOrganizationRateLimitListParamsGroupType = "files"`

    - `const BetaOrganizationRateLimitListParamsGroupTypeModelGroup BetaOrganizationRateLimitListParamsGroupType = "model_group"`

    - `const BetaOrganizationRateLimitListParamsGroupTypeSkills BetaOrganizationRateLimitListParamsGroupType = "skills"`

    - `const BetaOrganizationRateLimitListParamsGroupTypeTokenCount BetaOrganizationRateLimitListParamsGroupType = "token_count"`

    - `const BetaOrganizationRateLimitListParamsGroupTypeWebSearch BetaOrganizationRateLimitListParamsGroupType = "web_search"`

  - `Limit param.Field[int64] Optional`

    Maximum number of items to return per page. Ranges from `1` to `1000`.

    When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

    minimum: 1, maximum: 1000

  - `Model param.Field[string] Optional`

    Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page`.

#### Returns

- `type BetaOrganizationRateLimit`

  - `Type RateLimit`

    Object type. Always `rate_limit` for organization rate-limit entries.

    default: rate_limit

  - `ID string`

    Identifier of this rate-limit entry. It is stable within the organization and differs between organizations; the group's own identifier is `group.id`.

  - `Group BetaOrganizationRateLimitGroupUnion`

    The rate-limit group this entry's limits apply to. Its `type` equals `group_type`.

    - `type BetaOrganizationRateLimitModelGroup`

      - `Type ModelGroup`

        Always `model_group`: a family of models.

        default: model_group

      - `ID string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

      - `DisplayName string`

        Human-readable name of the model group (for example, `Claude Sonnet 4.x`). For display only; it may change.

    - `type BetaOrganizationRateLimitBatchGroup`

      - `Type Batch`

        Always `batch`: the Message Batches API.

        default: batch

      - `ID string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `type BetaOrganizationRateLimitTokenCountGroup`

      - `Type TokenCount`

        Always `token_count`: the Token Count API.

        default: token_count

      - `ID string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `type BetaOrganizationRateLimitFilesGroup`

      - `Type Files`

        Always `files`: the Files API.

        default: files

      - `ID string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `type BetaOrganizationRateLimitSkillsGroup`

      - `Type Skills`

        Always `skills`: the Skills API.

        default: skills

      - `ID string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

    - `type BetaOrganizationRateLimitWebSearchGroup`

      - `Type WebSearch`

        Always `web_search`: the Messages API web search tool.

        default: web_search

      - `ID string`

        Opaque identifier of the rate-limit group (for example, `rlg_01VPTCmyiu5ZLsWkcxYG2pY8`). It is the same in every organization and never changes, unlike the entry's own identifier, which differs per organization.

  - `Limits []BetaOrganizationRateLimitValue`

    The limiter values that apply to this group.

    - `Type string`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `Value int64`

      The configured limit value for this limiter type.

  - `Models []string`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `GroupType BetaOrganizationRateLimitGroupType`

    **Deprecated**: Use `group.type` instead. `group_type` is still returned and always equals `group.type`.

    Deprecated: use `group.type` instead. The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`. Always equal to `group.type`.

    - `const BetaOrganizationRateLimitGroupTypeBatch BetaOrganizationRateLimitGroupType = "batch"`

    - `const BetaOrganizationRateLimitGroupTypeFiles BetaOrganizationRateLimitGroupType = "files"`

    - `const BetaOrganizationRateLimitGroupTypeModelGroup BetaOrganizationRateLimitGroupType = "model_group"`

    - `const BetaOrganizationRateLimitGroupTypeSkills BetaOrganizationRateLimitGroupType = "skills"`

    - `const BetaOrganizationRateLimitGroupTypeTokenCount BetaOrganizationRateLimitGroupType = "token_count"`

    - `const BetaOrganizationRateLimitGroupTypeWebSearch BetaOrganizationRateLimitGroupType = "web_search"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.RateLimits.List(context.TODO(), anthropic.BetaOrganizationRateLimitListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "group": {
        "id": "id",
        "display_name": "display_name",
        "type": "model_group"
      },
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

`client.Beta.Organization.ComplianceSettings.Get(ctx) (*BetaComplianceSettings, error)`

**GET** `/v1/organizations/compliance_settings`

Retrieve your organization's Compliance Settings.

Compliance Settings is a singleton resource: there is exactly one per
organization, addressed without an identifier. The `state` field reflects
whether the Compliance API is enabled. An organization with a parent
organization reads the state inherited from the parent's configuration.

#### Returns

- `type BetaComplianceSettings`

  - `Type ComplianceSettings`

    default: compliance_settings

  - `State BetaComplianceSettingsStateUnion`

    Whether the Compliance API is enabled for this organization.

    - `type BetaComplianceSettingsStateEnabled`

      - `Type Enabled`

        default: enabled

    - `type BetaComplianceSettingsStateDisabled`

      - `Type Disabled`

        default: disabled

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaComplianceSettings, err := client.Beta.Organization.ComplianceSettings.Get(context.TODO())
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaComplianceSettings.State)
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

`client.Beta.Organization.ComplianceSettings.Update(ctx, body) (*BetaComplianceSettings, error)`

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

- `body BetaOrganizationComplianceSettingUpdateParams`

  - `State param.Field[BetaComplianceSettingsStateParamUnionResp]`

    Desired state. Accepts the string shorthand "enabled" or "disabled" in place of the object form; the response always returns the canonical object form.

#### Returns

- `type BetaComplianceSettings`

  - `Type ComplianceSettings`

    default: compliance_settings

  - `State BetaComplianceSettingsStateUnion`

    Whether the Compliance API is enabled for this organization.

    - `type BetaComplianceSettingsStateEnabled`

      - `Type Enabled`

        default: enabled

    - `type BetaComplianceSettingsStateDisabled`

      - `Type Disabled`

        default: disabled

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaComplianceSettings, err := client.Beta.Organization.ComplianceSettings.Update(context.TODO(), anthropic.BetaOrganizationComplianceSettingUpdateParams{
		State: anthropic.BetaComplianceSettingsStateParamUnion{
			OfEnabled: &anthropic.BetaComplianceSettingsStateEnabledParam{},
		},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaComplianceSettings.State)
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

## Beta › Organization › Analytics › Summaries

### Get Activity Summaries

`client.Beta.Organization.Analytics.Summaries.List(ctx, query) (*PageCursor[BetaAnalyticsSingleDayActivitySummary], error)`

**GET** `/v1/organizations/analytics/summaries`

Get organization-wide activity summaries for a date range.

Returns one entry per day from `starting_date` (inclusive) to `ending_date`
(exclusive) in `data`, the same `data` / `next_page` envelope as the other
analytics list endpoints; the series is currently returned in full, so
`next_page` is always null (`summaries` is a deprecated alias of `data`).
Data is typically available with a 1-day lag and may be revised by a few
percent over the following days: when `ending_date` is omitted it
defaults to the most recent available day + 1, so the last entry covers
the most recent available day. The series can be scoped to an RBAC group
via `filter[]=rbac_group_id:{id}`. Available to organizations on a Claude
Enterprise plan. Requires an API key with the `read:analytics` scope.

#### Parameters

- `query BetaOrganizationAnalyticsSummaryListParams`

  - `StartingDate param.Field[Time]`

    UTC date in YYYY-MM-DD format. Start of the date range (inclusive). Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

    format: date

  - `EndingDate param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. End of the date range (exclusive). Data is typically available with a 1-day lag, so this can be at most today — which is also the default when omitted, making the last entry cover the most recent available day. Data may be revised by a few percent over the following days. The range may span at most 366 days.

    format: date

  - `Filter param.Field[[]string] Optional`

    Filters as `dimension:value`. Only `rbac_group_id` is supported (e.g. `filter[]=rbac_group_id:{id}`); repeat the param to OR across groups. Scopes the whole day series to members of the matching group(s), re-aggregated from member-level activity — org-wide seat/invite fields and the adoption rates derived from them are null on scoped rows. `rbac_group_id` accepts the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each UTC day (time-of-usage attribution). At most 100 entries.

    maxItems: 100

  - `Limit param.Field[int64] Optional`

    Number of results per page (1-1000, default 100). The day series (at most 366 entries) is currently returned in full in a single page, so `limit` does not yet shorten it.

    minimum: 1, maximum: 1000

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page` field. `next_page` is currently always null, so there is never a cursor to send.

#### Returns

- `type BetaAnalyticsSingleDayActivitySummary`

  Per-day entry in the /summaries response.

  - `AssignedSeatCount int64`

    Number of seats currently assigned to members. Null when the response is scoped to an RBAC group — seat assignment is org-wide and has no per-group analogue.

  - `CoworkDailyActiveUserCount int64`

    Number of users with Cowork activity on the requested day

  - `CoworkMonthlyActiveUserCount int64`

    Number of users with Cowork activity in the 30-day rolling window

  - `CoworkWeeklyActiveUserCount int64`

    Number of users with Cowork activity in the 7-day rolling window

  - `DailyActiveUserCount int64`

    Number of users with token consumption on the requested day

  - `DailyAdoptionRate float64`

    Percentage of assigned seats with activity on the requested day (`DAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `EndingAt Time`

    End of the aggregation period (exclusive), UTC midnight in RFC 3339 format (e.g. `2026-01-16T00:00:00Z`).

    format: date-time

  - `MonthlyActiveUserCount int64`

    Number of users with token consumption in the 30-day rolling window

  - `MonthlyAdoptionRate float64`

    Percentage of assigned seats with activity in the 30-day rolling window (`MAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `PendingInviteCount int64`

    Number of pending invitations to join the organization. Null when the response is scoped to an RBAC group.

  - `StartingAt Time`

    Start of the aggregation period (inclusive), UTC midnight in RFC 3339 format (e.g. `2026-01-15T00:00:00Z`).

    format: date-time

  - `WeeklyActiveUserCount int64`

    Number of users with token consumption in the 7-day rolling window

  - `WeeklyAdoptionRate float64`

    Percentage of assigned seats with activity in the 7-day rolling window (`WAU / assigned_seat_count * 100`). Null when the response is scoped to an RBAC group.

  - `ChatDailyActiveUserCount int64 Optional`

    Number of users with claude.ai (chat) activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `ChatMonthlyActiveUserCount int64 Optional`

    Number of users with claude.ai (chat) activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `ChatWeeklyActiveUserCount int64 Optional`

    Number of users with claude.ai (chat) activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `ClaudeCodeDailyActiveUserCount int64 Optional`

    Number of users with Claude Code activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `ClaudeCodeMonthlyActiveUserCount int64 Optional`

    Number of users with Claude Code activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `ClaudeCodeWeeklyActiveUserCount int64 Optional`

    Number of users with Claude Code activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `ClaudeDesignDailyActiveUserCount int64 Optional`

    Number of users with Claude Design activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `ClaudeDesignMonthlyActiveUserCount int64 Optional`

    Number of users with Claude Design activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `ClaudeDesignWeeklyActiveUserCount int64 Optional`

    Number of users with Claude Design activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `OfficeAgentDailyActiveUserCount int64 Optional`

    Number of users with Claude in Office activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `OfficeAgentMonthlyActiveUserCount int64 Optional`

    Number of users with Claude in Office activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `OfficeAgentWeeklyActiveUserCount int64 Optional`

    Number of users with Claude in Office activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `ScienceDailyActiveUserCount int64 Optional`

    Number of users with Claude Science activity on the requested day. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `ScienceEntitledUserCount int64 Optional`

    Number of users with a Claude Science seat entitlement (per-seat RBAC) at the time of the daily snapshot. The funnel top; independent of the org-level Claude Science toggle. Null when the response is scoped to an RBAC group — entitlement is org-wide and has no per-group analogue. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `ScienceMonthlyActiveUserCount int64 Optional`

    Number of users with Claude Science activity in the 30-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

  - `ScienceWeeklyActiveUserCount int64 Optional`

    Number of users with Claude Science activity in the 7-day rolling window. Omitted from the response while the per-product breakdown is not enabled for this organization.

#### Example

```go
package main

import (
	"context"
	"fmt"
	"time"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Analytics.Summaries.List(context.TODO(), anthropic.BetaOrganizationAnalyticsSummaryListParams{
		StartingDate: time.Now(),
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "2019-12-27T18:11:19.117Z",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "2019-12-27T18:11:19.117Z",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0,
      "chat_daily_active_user_count": 0,
      "chat_monthly_active_user_count": 0,
      "chat_weekly_active_user_count": 0,
      "claude_code_daily_active_user_count": 0,
      "claude_code_monthly_active_user_count": 0,
      "claude_code_weekly_active_user_count": 0,
      "claude_design_daily_active_user_count": 0,
      "claude_design_monthly_active_user_count": 0,
      "claude_design_weekly_active_user_count": 0,
      "office_agent_daily_active_user_count": 0,
      "office_agent_monthly_active_user_count": 0,
      "office_agent_weekly_active_user_count": 0,
      "science_daily_active_user_count": 0,
      "science_entitled_user_count": 0,
      "science_monthly_active_user_count": 0,
      "science_weekly_active_user_count": 0
    }
  ],
  "next_page": "next_page",
  "summaries": [
    {
      "assigned_seat_count": 0,
      "cowork_daily_active_user_count": 0,
      "cowork_monthly_active_user_count": 0,
      "cowork_weekly_active_user_count": 0,
      "daily_active_user_count": 0,
      "daily_adoption_rate": 0,
      "ending_at": "2019-12-27T18:11:19.117Z",
      "monthly_active_user_count": 0,
      "monthly_adoption_rate": 0,
      "pending_invite_count": 0,
      "starting_at": "2019-12-27T18:11:19.117Z",
      "weekly_active_user_count": 0,
      "weekly_adoption_rate": 0,
      "chat_daily_active_user_count": 0,
      "chat_monthly_active_user_count": 0,
      "chat_weekly_active_user_count": 0,
      "claude_code_daily_active_user_count": 0,
      "claude_code_monthly_active_user_count": 0,
      "claude_code_weekly_active_user_count": 0,
      "claude_design_daily_active_user_count": 0,
      "claude_design_monthly_active_user_count": 0,
      "claude_design_weekly_active_user_count": 0,
      "office_agent_daily_active_user_count": 0,
      "office_agent_monthly_active_user_count": 0,
      "office_agent_weekly_active_user_count": 0,
      "science_daily_active_user_count": 0,
      "science_entitled_user_count": 0,
      "science_monthly_active_user_count": 0,
      "science_weekly_active_user_count": 0
    }
  ]
}
```

## Beta › Organization › Analytics › Users

### List User Activity

`client.Beta.Organization.Analytics.Users.List(ctx, query) (*PageCursor[BetaAnalyticsUserActivity], error)`

**GET** `/v1/organizations/analytics/users`

Get per-user activity for a given day, with cursor-based pagination.

Returns activity metrics for each user in the organization, sorted by email
address. Use `group_by[]` for per-RBAC-group aggregates, or `filter[]` to
scope results to specific members, groups, or a chat project. Available
to organizations on a Claude Enterprise plan. Requires an API key with
the `read:analytics` scope.

#### Parameters

- `query BetaOrganizationAnalyticsUserListParams`

  - `Date param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. The day to get user activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

    format: date

  - `EndingDate param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

    format: date

  - `Filter param.Field[[]string] Optional`

    Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `project_id`, `rbac_group_id`, `user_id`. Value forms: `project_id` takes a tagged project id (`claude_proj_...`) and scopes each member's row to their claude.ai chat activity within that project (it cannot be combined with `group_by[]` or an `rbac_group_id` filter); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

    maxItems: 100

  - `GroupBy param.Field[[]string] Optional`

    Dimensions to break results out by (e.g. `group_by[]=rbac_group_id`). Supported on this endpoint: `rbac_group_id`. Rows are already per-member, so the one supported grouping aggregates them per RBAC group instead. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

    maxItems: 100

    - `const BetaOrganizationAnalyticsUserListParamsGroupByRBACGroupID BetaOrganizationAnalyticsUserListParamsGroupBy = "rbac_group_id"`

  - `Limit param.Field[int64] Optional`

    Number of results per page (1-1000, default 100).

    minimum: 1, maximum: 1000

  - `Order param.Field[BetaOrganizationAnalyticsUserListParamsOrder] Optional`

    Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

    - `const BetaOrganizationAnalyticsUserListParamsOrderAsc BetaOrganizationAnalyticsUserListParamsOrder = "asc"`

    - `const BetaOrganizationAnalyticsUserListParamsOrderDesc BetaOrganizationAnalyticsUserListParamsOrder = "desc"`

  - `OrderBy param.Field[string] Optional`

    Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page` field.

  - `StartingDate param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

    format: date

#### Returns

- `type BetaAnalyticsUserActivity`

  Per-user activity data for a given day.

  - `ChatMetrics BetaAnalyticsChatMetrics`

    Claude.ai activity metrics for a single user on a given day.

    - `ConnectorsUsedCount int64`

      Number of MCP connector invocations.

    - `DistinctArtifactsCreatedCount int64`

      Number of distinct artifacts created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `DistinctConnectorsUsedCount int64`

      Distinct claude.ai connectors this user used. Excludes calls whose connector could not be identified and all calls from organizations with zero data retention. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `DistinctConversationCount int64`

      Number of distinct conversations the user participated in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `DistinctFilesUploadedCount int64`

      Number of distinct files uploaded. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `DistinctProjectsCreatedCount int64`

      Number of distinct projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `DistinctProjectsUsedCount int64`

      Number of distinct projects used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `DistinctSharedArtifactsViewedCount int64`

      Number of distinct shared artifacts the user viewed. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `DistinctSkillsUsedCount int64`

      Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `MessageCount int64`

      Number of messages sent

    - `SharedConversationsViewedCount int64`

      Number of times the user opened a shared conversation in a project

    - `ThinkingMessageCount int64`

      Number of messages that used extended thinking

  - `ClaudeCodeMetrics BetaAnalyticsClaudeCodeMetrics`

    Claude Code activity metrics for a single user on a given day.

    - `CoreMetrics BetaAnalyticsCoreCodeMetrics`

      Core Claude Code activity metrics for a single user on a given day.

      - `ArtifactsCreatedCount int64`

        Number of artifacts created in Claude Code sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

      - `CommitCount int64`

        Number of commits made via Claude Code

      - `DistinctSessionCount int64`

        Number of distinct Claude Code sessions. On aggregated rows and in date-range mode: summed per-day distinct counts. A session essentially never spans a UTC day, so the sum is in practice the true distinct count.

      - `LinesOfCode BetaAnalyticsLinesOfCode`

        Lines of code added and removed via Claude Code.

        - `AddedCount int64`

          Lines of code added

        - `RemovedCount int64`

          Lines of code removed

      - `PullRequestCount int64`

        Number of pull requests created via Claude Code

    - `ToolActions BetaAnalyticsToolActions`

      Per-tool accepted/rejected counts for Claude Code file modification tools.

      - `EditTool BetaAnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

        - `AcceptedCount int64`

          Number of tool proposals accepted

        - `RejectedCount int64`

          Number of tool proposals rejected

      - `MultiEditTool BetaAnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

      - `NotebookEditTool BetaAnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

      - `WriteTool BetaAnalyticsToolActionCounts`

        Accepted/rejected counts for a single Claude Code tool type.

  - `CoworkMetrics BetaAnalyticsCoworkMetrics`

    Cowork activity metrics for a single user on a given day.

    - `ActionCount int64`

      Number of tool actions completed in Cowork sessions

    - `ArtifactsCreatedCount int64`

      Number of artifacts created in Cowork sessions: an artifact counts once, on the day a session first saves it. Counted from 2026-08-17; 0 on earlier days. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `ConnectorsUsedCount int64`

      Total number of connector invocations in Cowork sessions

    - `DispatchTurnCount int64`

      Number of Dispatch (background agent) turns completed

    - `DistinctConnectorsUsedCount int64`

      Number of distinct connectors used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `DistinctSessionCount int64`

      Number of distinct Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `DistinctSkillsUsedCount int64`

      Number of distinct skills used in Cowork sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `MessageCount int64`

      Number of messages sent in Cowork sessions

    - `SkillsUsedCount int64`

      Total number of skill invocations in Cowork sessions

    - `DistinctPluginsUsedCount int64 Optional`

      Number of distinct plugins used in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `EditToolCount int64 Optional`

      Number of successful Edit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `FileEditCount int64 Optional`

      Number of successful file-edit tool calls (Edit, MultiEdit, Write, NotebookEdit) in Cowork sessions. Null, never 0, while the file-edit metrics are not enabled for this organization.

    - `MultiEditToolCount int64 Optional`

      Number of successful MultiEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `NotebookEditToolCount int64 Optional`

      Number of successful NotebookEdit tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

    - `PluginsUsedCount int64 Optional`

      Total number of plugin invocations in Cowork sessions. Null while Cowork plugin-use metrics are not enabled for this organization.

    - `SessionsWithFileEditsCount int64 Optional`

      Number of distinct Cowork sessions with at least one successful file-edit tool call. Null while the file-edit metrics are not enabled for this organization. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `WriteToolCount int64 Optional`

      Number of successful Write tool calls in Cowork sessions. Null while the file-edit metrics are not enabled for this organization.

  - `DesignMetrics BetaAnalyticsDesignMetrics`

    Claude Design activity metrics for a single user on a given day.

    - `DistinctProjectsCreatedCount int64`

      Number of distinct Claude Design projects created. Exact in date-range mode: a creation belongs to exactly one day, so the per-day counts never overlap and their sum over the window is the exact count of distinct creations in it.

    - `DistinctProjectsUsedCount int64`

      Number of distinct Claude Design projects the user worked in. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `DistinctSessionCount int64`

      Number of distinct Claude Design sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `MessageCount int64`

      Number of messages sent in Claude Design sessions

  - `OfficeMetrics BetaAnalyticsOfficeMetrics`

    Office Agent activity metrics for a single user on a given day, broken out by Office product.

    - `Excel BetaAnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

      - `ConnectorsUsedCount int64`

        Number of MCP connector invocations

      - `DistinctConnectorsUsedCount int64`

        Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `DistinctSessionCount int64`

        Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `DistinctSkillsUsedCount int64`

        Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

      - `MessageCount int64`

        Number of messages sent

      - `SkillsUsedCount int64`

        Number of skill invocations

    - `Outlook BetaAnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

    - `Powerpoint BetaAnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

    - `Word BetaAnalyticsOfficeProductMetrics`

      Office Agent activity metrics for a single user on a given day within one Office product.

  - `ScienceMetrics BetaAnalyticsScienceMetrics`

    Claude Science activity metrics for a single user on a given day.

    - `DelegationCount int64`

      Number of delegations (handoffs to a specialized agent) in Claude Science sessions

    - `DistinctSessionCount int64`

      Number of distinct Claude Science sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `MessageCount int64`

      Number of messages sent in Claude Science sessions

    - `RemoteComputeJobCount int64`

      Number of remote compute jobs launched from Claude Science sessions

    - `SkillsUsedCount int64`

      Total number of skill invocations in Claude Science sessions

  - `WebSearchCount int64`

    Number of web searches performed

  - `DistinctUserCount int64 Optional`

    Number of distinct active users represented by this row. Only set for grouped rollups (`group_by[]`); null for per-user rows. In date-range mode, recomputed as an exact distinct count of the group's active members over the requested window, never a sum of per-day values.

  - `LastActivityDate Time Optional`

    Most recent UTC day (YYYY-MM-DD) on which the user had any counted activity, within the requested window: equal to the requested `date` in single-day mode, and to the latest active day from `starting_date` (inclusive) to `ending_date` (exclusive) in date-range rollup mode — never a day earlier than the window start. On filtered requests (`filter[]`) only days matching the filter count: with `filter[]=rbac_group_id:{id}` it is the last day the user was active while a member of that group, consistent with the row's other metrics. On grouped (`group_by[]`) rows it is the latest day any member of the group was active (the requested `date` in single-day mode). Omitted from the response while last-activity reporting is not enabled for this organization.

    format: date

  - `RBACGroupID string Optional`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `RBACGroupName string Optional`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `User BetaAnalyticsUser Optional`

    The user this row describes. Null on rows aggregated across users.

    - `Type User`

      Object type. Always `user`.

      default: user

    - `ID string`

      Tagged user identifier (e.g. `user_...`)

    - `EmailAddress string`

      Email address of the user

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Analytics.Users.List(context.TODO(), anthropic.BetaOrganizationAnalyticsUserListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "chat_metrics": {
        "connectors_used_count": 0,
        "distinct_artifacts_created_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_conversation_count": 0,
        "distinct_files_uploaded_count": 0,
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_shared_artifacts_viewed_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "shared_conversations_viewed_count": 0,
        "thinking_message_count": 0
      },
      "claude_code_metrics": {
        "core_metrics": {
          "artifacts_created_count": 0,
          "commit_count": 0,
          "distinct_session_count": 0,
          "lines_of_code": {
            "added_count": 0,
            "removed_count": 0
          },
          "pull_request_count": 0
        },
        "tool_actions": {
          "edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "multi_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "notebook_edit_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          },
          "write_tool": {
            "accepted_count": 0,
            "rejected_count": 0
          }
        }
      },
      "cowork_metrics": {
        "action_count": 0,
        "artifacts_created_count": 0,
        "connectors_used_count": 0,
        "dispatch_turn_count": 0,
        "distinct_connectors_used_count": 0,
        "distinct_session_count": 0,
        "distinct_skills_used_count": 0,
        "message_count": 0,
        "skills_used_count": 0,
        "distinct_plugins_used_count": 0,
        "edit_tool_count": 0,
        "file_edit_count": 0,
        "multi_edit_tool_count": 0,
        "notebook_edit_tool_count": 0,
        "plugins_used_count": 0,
        "sessions_with_file_edits_count": 0,
        "write_tool_count": 0
      },
      "design_metrics": {
        "distinct_projects_created_count": 0,
        "distinct_projects_used_count": 0,
        "distinct_session_count": 0,
        "message_count": 0
      },
      "office_metrics": {
        "excel": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "outlook": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "powerpoint": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        },
        "word": {
          "connectors_used_count": 0,
          "distinct_connectors_used_count": 0,
          "distinct_session_count": 0,
          "distinct_skills_used_count": 0,
          "message_count": 0,
          "skills_used_count": 0
        }
      },
      "science_metrics": {
        "delegation_count": 0,
        "distinct_session_count": 0,
        "message_count": 0,
        "remote_compute_job_count": 0,
        "skills_used_count": 0
      },
      "web_search_count": 0,
      "distinct_user_count": 0,
      "last_activity_date": "2019-12-27",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user": {
        "id": "id",
        "email_address": "email_address",
        "type": "user"
      }
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Analytics › Apps › Chat › Projects

### Get Chat Project Usage

`client.Beta.Organization.Analytics.Apps.Chat.Projects.List(ctx, query) (*PageCursor[BetaAnalyticsProjectActivity], error)`

**GET** `/v1/organizations/analytics/apps/chat/projects`

Get per-project activity for a given day, with cursor-based pagination.

Returns activity metrics for each project in the organization, sorted by
project ID. Use `group_by[]` to break projects out per member or per RBAC
group, and `filter[]` to scope results; the parameter descriptions list the
supported dimensions. Available to organizations on a Claude Enterprise
plan. Requires an API key with the `read:analytics` scope.

#### Parameters

- `query BetaOrganizationAnalyticsAppChatProjectListParams`

  - `Date param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. The day to get project activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

    format: date

  - `EndingDate param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

    format: date

  - `Filter param.Field[[]string] Optional`

    Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `project_id`, `rbac_group_id`, `user_id`. Value forms: `project_id` takes a tagged project id (`claude_proj_...`); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

    maxItems: 100

  - `GroupBy param.Field[[]string] Optional`

    Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `rbac_group_id`, `user_id`. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

    maxItems: 100

    - `const BetaOrganizationAnalyticsAppChatProjectListParamsGroupByRBACGroupID BetaOrganizationAnalyticsAppChatProjectListParamsGroupBy = "rbac_group_id"`

    - `const BetaOrganizationAnalyticsAppChatProjectListParamsGroupByUserID BetaOrganizationAnalyticsAppChatProjectListParamsGroupBy = "user_id"`

  - `Limit param.Field[int64] Optional`

    Number of results per page (1-1000, default 100).

    minimum: 1, maximum: 1000

  - `Order param.Field[BetaOrganizationAnalyticsAppChatProjectListParamsOrder] Optional`

    Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

    - `const BetaOrganizationAnalyticsAppChatProjectListParamsOrderAsc BetaOrganizationAnalyticsAppChatProjectListParamsOrder = "asc"`

    - `const BetaOrganizationAnalyticsAppChatProjectListParamsOrderDesc BetaOrganizationAnalyticsAppChatProjectListParamsOrder = "desc"`

  - `OrderBy param.Field[string] Optional`

    Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page` field.

  - `StartingDate param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

    format: date

#### Returns

- `type BetaAnalyticsProjectActivity`

  Per-project activity data for a given day.

  - `DistinctUserCount int64`

    Number of distinct users who used the project on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `MessageCount int64`

    Number of messages sent in the project on the requested day

  - `ProjectID string`

    Tagged project identifier (e.g. `claude_proj_...`)

  - `ProjectName string`

    Name of the project

  - `CreatedAt Time Optional`

    Project creation timestamp in RFC 3339 format. Null if the project was deleted before attribution was recorded.

    format: date-time

  - `CreatedBy BetaAnalyticsUser Optional`

    User who created the project. Null if the project was deleted before attribution was recorded, or if the creator's account no longer exists.

    - `Type User`

      Object type. Always `user`.

      default: user

    - `ID string`

      Tagged user identifier (e.g. `user_...`)

    - `EmailAddress string`

      Email address of the user

  - `DistinctConversationCount int64 Optional`

    Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

  - `Product string Optional`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, or `office_agent` (the canonical Cost & Usage product naming; an `office_agent` row's per-surface breakdown is in its `office_metrics`). On `/plugins` only `cowork` and `claude_code` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, and `cowork` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `RBACGroupID string Optional`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `RBACGroupName string Optional`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `UserID string Optional`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Analytics.Apps.Chat.Projects.List(context.TODO(), anthropic.BetaOrganizationAnalyticsAppChatProjectListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by": {
        "id": "id",
        "email_address": "email_address",
        "type": "user"
      },
      "distinct_conversation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Analytics › Connectors

### Get Connector Usage

`client.Beta.Organization.Analytics.Connectors.List(ctx, query) (*PageCursor[BetaAnalyticsConnectorActivity], error)`

**GET** `/v1/organizations/analytics/connectors`

Get per-connector usage for a given day, with cursor-based pagination.

Returns connector usage metrics for the organization, sorted by connector
name. Connector names are normalized from their various sources — for
example, "Atlassian MCP server" and "mcp-atlassian" both appear as
"atlassian". Use `group_by[]` to break usage out per member, per RBAC
group, or per product surface, and `filter[]` to scope results; the
parameter descriptions list the supported dimensions. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

#### Parameters

- `query BetaOrganizationAnalyticsConnectorListParams`

  - `Date param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. The day to get connector usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

    format: date

  - `EndingDate param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

    format: date

  - `Filter param.Field[[]string] Optional`

    Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `connector_name`, `product`, `rbac_group_id`, `user_id`. Value forms: `connector_name` matches case-insensitively, a display name such as 'GitHub MCP' also matches its normalized stored form ('github'), and for rows whose `connector_name` is an opaque connector id the connector's display name (`connector_display_name`) also matches; `product` is one of `chat`, `claude_code`, `cowork`, or `office_agent`; `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

    maxItems: 100

  - `GroupBy param.Field[[]string] Optional`

    Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `product`, `rbac_group_id`, `user_id`. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

    maxItems: 100

    - `const BetaOrganizationAnalyticsConnectorListParamsGroupByProduct BetaOrganizationAnalyticsConnectorListParamsGroupBy = "product"`

    - `const BetaOrganizationAnalyticsConnectorListParamsGroupByRBACGroupID BetaOrganizationAnalyticsConnectorListParamsGroupBy = "rbac_group_id"`

    - `const BetaOrganizationAnalyticsConnectorListParamsGroupByUserID BetaOrganizationAnalyticsConnectorListParamsGroupBy = "user_id"`

  - `Limit param.Field[int64] Optional`

    Number of results per page (1-1000, default 100).

    minimum: 1, maximum: 1000

  - `Order param.Field[BetaOrganizationAnalyticsConnectorListParamsOrder] Optional`

    Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

    - `const BetaOrganizationAnalyticsConnectorListParamsOrderAsc BetaOrganizationAnalyticsConnectorListParamsOrder = "asc"`

    - `const BetaOrganizationAnalyticsConnectorListParamsOrderDesc BetaOrganizationAnalyticsConnectorListParamsOrder = "desc"`

  - `OrderBy param.Field[string] Optional`

    Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page` field.

  - `StartingDate param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

    format: date

#### Returns

- `type BetaAnalyticsConnectorActivity`

  Per-connector activity data for a given day.

  - `ChatMetrics BetaAnalyticsConnectorChatMetrics`

    Claude.ai activity metrics for a single connector on a given day.

    - `DistinctConversationConnectorUsedCount int64`

      Number of distinct conversations in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `ClaudeCodeMetrics BetaAnalyticsConnectorClaudeCodeMetrics`

    Claude Code activity metrics for a single connector on a given day.

    - `DistinctSessionConnectorUsedCount int64`

      Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `ConnectorName string`

    Name of the connector. Some rows carry an opaque connector id here instead of a readable name; `connector_display_name` holds the resolved name for those rows.

  - `CoworkMetrics BetaAnalyticsConnectorCoworkMetrics`

    Cowork activity metrics for a single connector on a given day.

    - `DistinctSessionConnectorUsedCount int64`

      Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `DistinctUserCount int64`

    Number of distinct users who used the connector on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `OfficeMetrics BetaAnalyticsConnectorOfficeMetrics`

    Office Agent activity metrics for a single connector on a given day, broken out by Office product.

    - `Excel BetaAnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

      - `DistinctSessionConnectorUsedCount int64`

        Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `Outlook BetaAnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

    - `Powerpoint BetaAnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

    - `Word BetaAnalyticsConnectorOfficeProductMetrics`

      Office Agent activity metrics for a single connector on a given day within one Office product.

  - `ConnectorDisplayName string Optional`

    Human-readable display name for rows whose `connector_name` is an opaque connector id rather than a readable name, resolved at request time from the organization's connectors (including connectors that have since been removed). `connector_name` remains the row's stable key for sorting and pagination, and `filter[]=connector_name:{value}` also matches these rows by display name. Display names are not unique, and the same connector's claude.ai usage can appear under a separate row with a readable `connector_name`. Null when `connector_name` is already a readable name, when the id cannot be resolved to one of the organization's connectors, or when display-name resolution is not enabled for this organization.

  - `IndividualAuthDistinctUserCount int64 Optional`

    Number of distinct users whose use of this connector on the requested day ran on their own individual credential, connected through their own consent flow. Companion bucket to `managed_auth_distinct_user_count`, which carries the measurement, attribution, and null rules. Users whose requests used no stored credential count in neither bucket.

  - `ManagedAuthDistinctUserCount int64 Optional`

    Number of distinct users whose use of this connector on the requested day ran on Enterprise Managed Auth (an organization-managed credential provisioned through the organization's identity provider), read from the token record each request used. Null, never 0, when managed-auth reporting is not enabled for the organization, the value cannot be attributed to the row, no credentialed requests and no managed-token mint events (a managed credential being provisioned for a user's use of the connector) were observed that day, or the day predates 2026-07-01, the first day the backing data exists (forward-only data, no backfill). When credentialed requests or mint events were observed and attributed, both managed-auth fields populate, reporting 0 for a bucket with no users; the two counts are independent, not a partition — a user whose requests that day used both kinds of credential counts in both. Mint events carry user but not surface attribution, so they count as observed auth activity on `user_id` and `rbac_group_id` cuts — attributed to the user the credential was provisioned for — but never on a cut that references `product` (group or filter). Date-range rollup mode (`starting_date`/`ending_date`) computes both fields exactly over the window — distinct users with at least one qualifying day — when the whole window starts on or after 2026-07-01, with the null-versus-0 and mint-event rules applying with the window in place of the day; a range starting earlier reports every managed-auth field as null, never a partial-window value.

  - `Product string Optional`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, or `office_agent` (the canonical Cost & Usage product naming; an `office_agent` row's per-surface breakdown is in its `office_metrics`). On `/plugins` only `cowork` and `claude_code` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, and `cowork` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `RBACGroupID string Optional`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `RBACGroupName string Optional`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `ReadCallCount int64 Optional`

    Number of connector tool calls on the requested day whose trusted read-only annotation marked them read-only. Call count, not distinct users. Every call recorded on a classified surface lands in exactly one of `read_call_count`, `write_call_count`, or `unclassified_call_count`, so the three sum to the day's classified calls. Classification is forward-only per surface: claude.ai from 2026-06-01, Claude Code from 2026-05-30, Claude in Office from 2026-05-29, Cowork from 2026-06-02 (Cowork clients predating annotation forwarding land in `unclassified_call_count`). Null, never 0, when the value cannot be stated: the read/write split is not enabled for this organization, or the day predates 2026-05-29. For a date-range total, sum the per-day values, but treat a window that extends before 2026-05-29 as null rather than summing only its covered days — date-range rollup mode (`starting_date`/`ending_date`) applies both rules server-side.

  - `UnclassifiedCallCount int64 Optional`

    Number of connector tool calls on the requested day with no trusted read-only annotation — the annotation is optional in the MCP spec and is discarded when connector access controls are active, so unclassified calls are common. This field shows how much of the day's classified activity the read/write split actually covers. Call count, not distinct users. One of the three call-classification buckets; see `read_call_count` for the per-surface data-start dates, null conditions, and date-range guidance.

  - `UserID string Optional`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

  - `WriteCallCount int64 Optional`

    Number of connector tool calls on the requested day whose trusted read-only annotation marked them not read-only. Call count, not distinct users. One of the three call-classification buckets; see `read_call_count` for the per-surface data-start dates, null conditions, and date-range guidance.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Analytics.Connectors.List(context.TODO(), anthropic.BetaOrganizationAnalyticsConnectorListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "chat_metrics": {
        "distinct_conversation_connector_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "connector_name": "connector_name",
      "cowork_metrics": {
        "distinct_session_connector_used_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_connector_used_count": 0
        },
        "outlook": {
          "distinct_session_connector_used_count": 0
        },
        "powerpoint": {
          "distinct_session_connector_used_count": 0
        },
        "word": {
          "distinct_session_connector_used_count": 0
        }
      },
      "connector_display_name": "connector_display_name",
      "individual_auth_distinct_user_count": 0,
      "managed_auth_distinct_user_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "read_call_count": 0,
      "unclassified_call_count": 0,
      "user_id": "user_id",
      "write_call_count": 0
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Analytics › Plugins

### Get Plugin Usage

`client.Beta.Organization.Analytics.Plugins.List(ctx, query) (*PageCursor[BetaAnalyticsPluginActivity], error)`

**GET** `/v1/organizations/analytics/plugins`

Get per-plugin install + invocation usage for a given day, with pagination.

Returns plugin usage metrics for the organization across Cowork and Claude
Code, sorted by plugin name. The `plugin_name` value `third-party` is
an aggregate bucket, not a plugin: it collects plugin activity, from
either surface, for which the reporting client did not provide a plugin
name — so an organization's own plugins can contribute both to their own
named rows and to this bucket. Use `group_by[]` to break usage out per
member, per RBAC group, or per product surface (Cowork / Claude Code),
and `filter[]` to scope results; the parameter descriptions list the
supported dimensions. Requires an API key with the
`read:analytics` scope. `starting_date` / `ending_date` select
range-rollup mode like `/skills`.

#### Parameters

- `query BetaOrganizationAnalyticsPluginListParams`

  - `Date param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. The day to get plugin usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

    format: date

  - `EndingDate param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

    format: date

  - `Filter param.Field[[]string] Optional`

    Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `plugin_name`, `product`, `rbac_group_id`, `user_id`. Value forms: `plugin_name` matches case-insensitively; `product` is `claude_code` or `cowork` (the only surfaces with plugin attribution); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

    maxItems: 100

  - `GroupBy param.Field[[]string] Optional`

    Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `product`, `rbac_group_id`, `user_id`. On this endpoint `product` takes the values `claude_code` or `cowork` only (the surfaces with plugin attribution). Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

    maxItems: 100

    - `const BetaOrganizationAnalyticsPluginListParamsGroupByProduct BetaOrganizationAnalyticsPluginListParamsGroupBy = "product"`

    - `const BetaOrganizationAnalyticsPluginListParamsGroupByRBACGroupID BetaOrganizationAnalyticsPluginListParamsGroupBy = "rbac_group_id"`

    - `const BetaOrganizationAnalyticsPluginListParamsGroupByUserID BetaOrganizationAnalyticsPluginListParamsGroupBy = "user_id"`

  - `Limit param.Field[int64] Optional`

    Number of results per page (1-1000, default 100).

    minimum: 1, maximum: 1000

  - `Order param.Field[BetaOrganizationAnalyticsPluginListParamsOrder] Optional`

    Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

    - `const BetaOrganizationAnalyticsPluginListParamsOrderAsc BetaOrganizationAnalyticsPluginListParamsOrder = "asc"`

    - `const BetaOrganizationAnalyticsPluginListParamsOrderDesc BetaOrganizationAnalyticsPluginListParamsOrder = "desc"`

  - `OrderBy param.Field[string] Optional`

    Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page` field.

  - `StartingDate param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

    format: date

#### Returns

- `type BetaAnalyticsPluginActivity`

  Per-plugin install + invocation activity for a given day.

  With `group_by[]=user_id` / `rbac_group_id` / `product` (`cowork` /
  `claude_code` only on this endpoint) each row is one (plugin, user),
  (plugin, group), or (plugin, product) cut: the flat `user_id` /
  `rbac_group_id` / `product` keys carry the cut and the counts are
  scoped to it.

  - `ClaudeCodeMetrics BetaAnalyticsPluginClaudeCodeMetrics`

    Claude Code activity metrics for a single plugin on a given day.

    - `DistinctSessionPluginUsedCount int64`

      Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

  - `CoworkMetrics BetaAnalyticsPluginCoworkMetrics`

    Cowork activity metrics for a single plugin on a given day.

    - `DistinctSessionPluginUsedCount int64`

      Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

  - `DistinctUserCount int64`

    Number of distinct users with recorded install or invocation activity for the plugin on the requested day (install-only users count), or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `InstallCount int64`

    Number of distinct users who installed the plugin on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

  - `InvocationCount int64`

    Number of plugin invocations on the requested day

  - `PluginName string`

    Name of the plugin

  - `PluginID string Optional`

    Stable plugin identifier when available (e.g. `serena@claude-plugins-official`). Null for third-party Claude Code plugins (redacted at the source) and Cowork slash commands that carry only a hashed id.

  - `Product string Optional`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, or `office_agent` (the canonical Cost & Usage product naming; an `office_agent` row's per-surface breakdown is in its `office_metrics`). On `/plugins` only `cowork` and `claude_code` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, and `cowork` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `RBACGroupID string Optional`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `RBACGroupName string Optional`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `UserID string Optional`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Analytics.Plugins.List(context.TODO(), anthropic.BetaOrganizationAnalyticsPluginListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "claude_code_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_plugin_used_count": 0
      },
      "distinct_user_count": 0,
      "install_count": 0,
      "invocation_count": 0,
      "plugin_name": "plugin_name",
      "plugin_id": "plugin_id",
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Analytics › Skills

### Get Skill Usage

`client.Beta.Organization.Analytics.Skills.List(ctx, query) (*PageCursor[BetaAnalyticsSkillActivity], error)`

**GET** `/v1/organizations/analytics/skills`

Get per-skill usage for a given day, with cursor-based pagination.

Returns skill usage metrics for the organization, sorted by skill name.
Use `group_by[]` to break usage out per member, per RBAC group, or per
product surface, and `filter[]` to scope results; the parameter
descriptions list the supported dimensions. Available to organizations
on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

#### Parameters

- `query BetaOrganizationAnalyticsSkillListParams`

  - `Date param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. The day to get skill usage for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

    format: date

  - `EndingDate param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. End of the date range (exclusive); only valid with `starting_date`. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day), so this can be at most today — which is also the default when omitted, resolved once when the first page is served and reused for the rest of the pagination sequence. At most 366 days after `starting_date`.

    format: date

  - `Filter param.Field[[]string] Optional`

    Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `product`, `rbac_group_id`, `share_status`, `skill_name`, `user_id`. Value forms: `product` is one of `chat`, `claude_code`, `cowork`, or `office_agent`; `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `share_status` is one of `organization`, `private`, or `public`; `skill_name` matches case-insensitively; `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

    maxItems: 100

  - `GroupBy param.Field[[]string] Optional`

    Dimensions to break results out by (e.g. `group_by[]=user_id`). Supported on this endpoint: `product`, `rbac_group_id`, `user_id`. Grouped rows carry the requested dimension values as additional fields and paginate like ungrouped responses via `next_page`; an unsupported dimension returns 400. `rbac_group_id` attributes a user to every group they held at any point during each covered UTC day, so grouped rows are not an exclusive partition and can sum above org-level totals. At most 100 entries.

    maxItems: 100

    - `const BetaOrganizationAnalyticsSkillListParamsGroupByProduct BetaOrganizationAnalyticsSkillListParamsGroupBy = "product"`

    - `const BetaOrganizationAnalyticsSkillListParamsGroupByRBACGroupID BetaOrganizationAnalyticsSkillListParamsGroupBy = "rbac_group_id"`

    - `const BetaOrganizationAnalyticsSkillListParamsGroupByUserID BetaOrganizationAnalyticsSkillListParamsGroupBy = "user_id"`

  - `Limit param.Field[int64] Optional`

    Number of results per page (1-1000, default 100).

    minimum: 1, maximum: 1000

  - `Order param.Field[BetaOrganizationAnalyticsSkillListParamsOrder] Optional`

    Sort direction: `asc` or `desc`. Defaults to `asc` for the endpoint's sort column and to `desc` when `order_by` names a metric (a top-N ranking). Applies to `order_by`, or to the endpoint's default sort field when `order_by` is omitted.

    - `const BetaOrganizationAnalyticsSkillListParamsOrderAsc BetaOrganizationAnalyticsSkillListParamsOrder = "asc"`

    - `const BetaOrganizationAnalyticsSkillListParamsOrderDesc BetaOrganizationAnalyticsSkillListParamsOrder = "desc"`

  - `OrderBy param.Field[string] Optional`

    Sort field. Restricted to the endpoint's sort column plus its rankable metrics (metrics default to descending; a few metrics rank in date-range mode only, per the endpoint's documented orderable set).

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page` field.

  - `StartingDate param.Field[Time] Optional`

    UTC date in YYYY-MM-DD format. Start of a date range (inclusive). Enables rollup mode: one row per entity aggregated over the whole range — addable counters are summed across days, and a distinct count is never summed where summing could double-count (a field's range value is recomputed exactly over the window, approximate via HLL with typical error under 2%, null, or — for the creation-event counts, whose per-day values cannot overlap — a per-day sum that is itself exact; each field's own description says which). Use either `date` or `starting_date`, not both. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

    format: date

#### Returns

- `type BetaAnalyticsSkillActivity`

  Per-skill activity data for a given day.

  - `ChatMetrics BetaAnalyticsSkillChatMetrics`

    Claude.ai activity metrics for a single skill on a given day.

    - `DistinctConversationSkillUsedCount int64`

      Number of distinct conversations in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `ClaudeCodeMetrics BetaAnalyticsSkillClaudeCodeMetrics`

    Claude Code activity metrics for a single skill on a given day.

    - `DistinctSessionSkillUsedCount int64`

      Number of distinct Claude Code sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `CoworkMetrics BetaAnalyticsSkillCoworkMetrics`

    Cowork activity metrics for a single skill on a given day.

    - `DistinctSessionSkillUsedCount int64`

      Number of distinct Cowork sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

  - `DistinctUserCount int64`

    Number of distinct users who used the skill on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted.

  - `OfficeMetrics BetaAnalyticsSkillOfficeMetrics`

    Office Agent activity metrics for a single skill on a given day, broken out by Office product.

    - `Excel BetaAnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

      - `DistinctSessionSkillUsedCount int64`

        Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

    - `Outlook BetaAnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

    - `Powerpoint BetaAnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

    - `Word BetaAnalyticsSkillOfficeProductMetrics`

      Office Agent activity metrics for a single skill on a given day within one Office product.

  - `SkillName string`

    Name of the skill

  - `AttributedListPrice string Optional`

    List-price (rate-card) value of the member requests attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD), from Claude Code, Cowork, and Office Agent request-level attribution — the value of requests that involved the skill, not the skill's incremental cost. Unlike `estimated_overage_spend` this reflects usage value regardless of how it was funded — seat-covered usage counts — but it is undiscounted and does not tie to billed spend or the organization's spend reporting. claude.ai chat usage carries no request-level attribution and contributes nothing: the field is null on `chat` product rows and on `office_agent` product cuts dated before 2026-06-18 (the Office Agent attribution data-start), and on ungrouped rows it covers the Claude Code + Cowork + Office Agent share only (null when no attributable usage exists). Also null under the same conditions as `estimated_overage_spend` (spend reporting not enabled for this organization, `office_agent` product cuts before the 2026-06-18 data-start). "0" means attributable usage existed but none was attributed to this skill. Addable across days: date-range rollup mode returns the window's sum. On `group_by[]` and `filter[]` shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

  - `Currency string Optional`

    Currency for this row's monetary fields (`estimated_overage_spend` and `attributed_list_price`), as an uppercase ISO-4217 code. Always "USD" when either amount is populated; null whenever both amounts are null.

  - `EnableCount int64 Optional`

    Distinct accounts that enabled this skill on the requested day (claude.ai only — the skill analog of plugin `install_count`). The count is org-wide: null when enable reporting is not enabled for this organization, or when the request scopes to `user_id` / `rbac_group_id` / `product` via `group_by[]` or `filter[]` (an org-wide count would be misleading on per-cut rows). A distinct count, not an event count: summing across days double-counts members who enable the skill on more than one day, so it is also null in date-range rollup mode (`starting_date`/`ending_date`).

  - `EstimatedOverageSpend string Optional`

    Estimated overage spend attributed to this skill, as a decimal string in the minor unit of `currency` (cents for USD; "1250" is $12.50, fractional cents possible) — an allocation of each member's daily post-discount, pre-credit metered overage spend (the same cost basis as the organization's spend reporting and the Cost & Usage API, so per-skill figures are directly comparable; spend with no skill attribution — including any member-day without skill invocations — is not represented, so skill rows sum to at most those totals) across the skills the member used. Overage only: usage covered by included seat allowances bills nothing and allocates $0 here — see `attributed_list_price` for the funding-independent usage-value companion. Claude Code, Cowork, and Office Agent spend use request-level skill attribution; claude.ai chat spend is approximated proportionally to skill-invoking messages. An estimate, not a billing number — and the cost of the requests/messages that involved the skill, not the skill's incremental cost (the same request would still have cost something without the skill active). "0" means no overage spend was attributed; null when spend reporting is not enabled for this organization, on `office_agent` product cuts dated before 2026-06-18 (the Office Agent attribution data-start). Addable across days: date-range rollup mode (`starting_date`/`ending_date`) returns the window's sum. With `group_by[]=user_id` each row carries the user's own attributed spend. On `group_by[]` and `filter[]` shapes both amounts can total below the ungrouped value for the same skill over the same date or range: spend attributed to a member–skill pair with no counted usage on that day is excluded from those cuts.

  - `InvocationCount int64 Optional`

    Total number of times this skill was invoked on the requested day (the skill analog of plugin `invocation_count`). Unlike `distinct_user_count` — which answers '\# of users' — this is the true '# of uses'. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Null when invocation reporting is not enabled for this organization. Sum across a date range for total uses in the window — date-range rollup mode (`starting_date`/`ending_date`) returns this sum directly.

  - `Product string Optional`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, or `office_agent` (the canonical Cost & Usage product naming; an `office_agent` row's per-surface breakdown is in its `office_metrics`). On `/plugins` only `cowork` and `claude_code` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, and `cowork` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `RBACGroupID string Optional`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `RBACGroupName string Optional`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `ShareStatus BetaAnalyticsSkillActivityShareStatus Optional`

    Skill share status (claude.ai only): one of `private`, `organization`, or `public`. Null for skills used only in Claude Code or Office (no per-skill share-status concept) and when share-status reporting is not yet available for the organization. Filterable via `filter[]=share_status:{value}`.

    - `const BetaAnalyticsSkillActivityShareStatusOrganization BetaAnalyticsSkillActivityShareStatus = "organization"`

    - `const BetaAnalyticsSkillActivityShareStatusPrivate BetaAnalyticsSkillActivityShareStatus = "private"`

    - `const BetaAnalyticsSkillActivityShareStatusPublic BetaAnalyticsSkillActivityShareStatus = "public"`

  - `SkillDisplayName string Optional`

    Human-readable display name for rows whose `skill_name` is an opaque skill id (user/organization skill types and plugin-delivered skills, whose user-defined names usage reports generally withhold). Organization-shared skills and skills delivered by the organization's own plugins (its plugin marketplaces and its library) resolve; plugin skill names are shown without their 'plugin:' prefix. The literal 'unknown' bucket row gets a fixed 'Unknown skill' label. For a member's own skill (private or personal-plugin) it is null, except when the skill's owner used it from Claude Code or Cowork in the requested period: then it shows the name that client reported at the time. Apart from that, the names of members' own skills are not disclosed to analytics-key holders. Also null for Anthropic-provided plugin skills (not resolved), for an organization skill or plugin whose name can no longer be found (for example, one since deleted), when `skill_name` is already a display name, or when display-name resolution is not enabled for this organization.

  - `UserID string Optional`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Analytics.Skills.List(context.TODO(), anthropic.BetaOrganizationAnalyticsSkillListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "chat_metrics": {
        "distinct_conversation_skill_used_count": 0
      },
      "claude_code_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "cowork_metrics": {
        "distinct_session_skill_used_count": 0
      },
      "distinct_user_count": 0,
      "office_metrics": {
        "excel": {
          "distinct_session_skill_used_count": 0
        },
        "outlook": {
          "distinct_session_skill_used_count": 0
        },
        "powerpoint": {
          "distinct_session_skill_used_count": 0
        },
        "word": {
          "distinct_session_skill_used_count": 0
        }
      },
      "skill_name": "skill_name",
      "attributed_list_price": "attributed_list_price",
      "currency": "currency",
      "enable_count": 0,
      "estimated_overage_spend": "estimated_overage_spend",
      "invocation_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "share_status": "organization",
      "skill_display_name": "skill_display_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Analytics › Artifacts

### Get Artifact Activity

`client.Beta.Organization.Analytics.Artifacts.List(ctx, query) (*PageCursor[BetaAnalyticsArtifactActivity], error)`

**GET** `/v1/organizations/analytics/artifacts`

Get artifact-creation activity for a given day, broken out by MIME type.

Returns the full (`artifact_type`, `is_shared`) cube for the organization;
`next_page` is null except for grouped queries, which paginate. The cube
can be broken out per product, per member, or per RBAC group via
`group_by[]`, and scoped via `filter[]`. Requires an API key with the
`read:analytics` scope.

#### Parameters

- `query BetaOrganizationAnalyticsArtifactListParams`

  - `Date param.Field[Time]`

    UTC date in YYYY-MM-DD format. The day to get artifact activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

    format: date

  - `Filter param.Field[[]string] Optional`

    Filters as `dimension:value`, e.g. `filter[]=rbac_group_id:{id}`. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: `artifact_type`, `is_shared`, `product`, `rbac_group_id`, `user_id`. Value forms: `artifact_type` is a canonical artifact MIME type (e.g. `text/markdown`) or `other`; `is_shared` is `true` or `false`; `product` is `chat`, `claude_code`, or `cowork` (the surfaces that create artifacts); `rbac_group_id` takes the tagged id (`rbac_group_...`, as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); `user_id` takes a tagged user id (`user_...`), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

    maxItems: 100

  - `GroupBy param.Field[[]string] Optional`

    Dimensions to break results out by: `product`, `user_id` and/or `rbac_group_id`. The ungrouped artifact-type cube is finite and returned in full; grouped queries multiply the cube and paginate via `next_page`. `product` takes the values `chat`, `claude_code`, or `cowork` (the surfaces that create artifacts). `rbac_group_id` attributes a user to every group they held at any point during the requested UTC day, so grouped rows are not an exclusive partition. At most 100 entries.

    maxItems: 100

    - `const BetaOrganizationAnalyticsArtifactListParamsGroupByProduct BetaOrganizationAnalyticsArtifactListParamsGroupBy = "product"`

    - `const BetaOrganizationAnalyticsArtifactListParamsGroupByRBACGroupID BetaOrganizationAnalyticsArtifactListParamsGroupBy = "rbac_group_id"`

    - `const BetaOrganizationAnalyticsArtifactListParamsGroupByUserID BetaOrganizationAnalyticsArtifactListParamsGroupBy = "user_id"`

  - `Limit param.Field[int64] Optional`

    Maximum rows to return (1-1000, default 100). The ungrouped artifact-type cube is finite and returned in full; `limit` is the page size only when `group_by[]` multiplies the cube.

    minimum: 1, maximum: 1000

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page` field. Only valid with `group_by[]` — the ungrouped cube is never paginated.

#### Returns

- `type BetaAnalyticsArtifactActivity`

  Artifact-creation activity for one (`artifact_type`, `is_shared`) bucket
  on a given day.

  Artifacts form a small finite cube — the canonical MIME type (8 values incl.
  `other`) crossed with shared-vs-private — so the response is the full set of
  non-empty buckets, not a ranked/paginated list. Claude Code and Cowork
  artifacts report under `text/html` and are counted from 2026-08-17
  onward; earlier days contain claude.ai chat artifacts only. With
  `group_by[]=product` / `user_id` / `rbac_group_id` each row is further
  split by the flat group keys and counts are scoped to that cut.

  - `ArtifactType string`

    Canonical artifact MIME type (e.g. `text/markdown`, `application/vnd.ant.react`, `image/svg+xml`), or `other`. Claude Code and Cowork artifacts report as `text/html`.

  - `ArtifactsCreatedCount int64`

    Number of artifacts created in this bucket on the requested day

  - `DistinctUserCount int64`

    Number of distinct users who created artifacts in this bucket on the requested day

  - `IsShared bool`

    Whether the artifacts in this bucket have ever been shared (a Claude Code / Cowork artifact is shared once anyone beyond its creator may open it: named members, the whole organization, or anyone with the link).

  - `PublishedArtifactsCreatedCount int64`

    Number of those artifacts that have been published (for Claude Code / Cowork artifacts: open to anyone with the link); never exceeds `artifacts_created_count`

  - `Product string Optional`

    Product that produced this row's activity: one of `chat`, `claude_code`, `cowork`, or `office_agent` (the canonical Cost & Usage product naming; an `office_agent` row's per-surface breakdown is in its `office_metrics`). On `/plugins` only `cowork` and `claude_code` occur (the only surfaces with plugin attribution); on `/artifacts` only `chat`, `claude_code`, and `cowork` occur (the surfaces that create artifacts); `/apps/chat/projects` does not support the product dimension (a `product` entry in `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by `product`.

  - `RBACGroupID string Optional`

    Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

  - `RBACGroupName string Optional`

    Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

  - `UserID string Optional`

    Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

#### Example

```go
package main

import (
	"context"
	"fmt"
	"time"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Analytics.Artifacts.List(context.TODO(), anthropic.BetaOrganizationAnalyticsArtifactListParams{
		Date: time.Now(),
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "artifact_type": "artifact_type",
      "artifacts_created_count": 0,
      "distinct_user_count": 0,
      "is_shared": true,
      "published_artifacts_created_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Analytics › Usage Report

### Get Token Usage Over Time

`client.Beta.Organization.Analytics.UsageReport.List(ctx, query) (*PageCursor[BetaAnalyticsUsageReportTimeBucket], error)`

**GET** `/v1/organizations/analytics/usage_report`

Get token usage over time across a date range.

Returns token usage bucketed by minute, hour, or day, optionally broken
down by product, model, context window, inference region, or speed.
Available to organizations on a Claude Enterprise plan. Requires an API
key with the `read:analytics` scope.

#### Parameters

- `query BetaOrganizationAnalyticsUsageReportListParams`

  - `StartingAt param.Field[Time]`

    Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

    format: date-time

  - `BucketWidth param.Field[BetaOrganizationAnalyticsUsageReportListParamsBucketWidth] Optional`

    Time bucket granularity.

    - `const BetaOrganizationAnalyticsUsageReportListParamsBucketWidthDay BetaOrganizationAnalyticsUsageReportListParamsBucketWidth = "1d"`

    - `const BetaOrganizationAnalyticsUsageReportListParamsBucketWidthHour BetaOrganizationAnalyticsUsageReportListParamsBucketWidth = "1h"`

    - `const BetaOrganizationAnalyticsUsageReportListParamsBucketWidthMinute BetaOrganizationAnalyticsUsageReportListParamsBucketWidth = "1m"`

  - `ClaudeTagCategories param.Field[[]BetaAnalyticsClaudeTagCategory] Optional`

    Filter to Claude Tag (Claude in Slack) usage in specific spend categories. Usage with no category never matches. `dm` usage is reported under the user's product rather than `claude-tag`, so combining this filter with `products[]=claude-tag` excludes it. Use `group_by[]=claude_tag_category` to break out per-category values.

    maxItems: 100

    - `const BetaAnalyticsClaudeTagCategoryDm BetaAnalyticsClaudeTagCategory = "dm"`

    - `const BetaAnalyticsClaudeTagCategoryEngaged BetaAnalyticsClaudeTagCategory = "engaged"`

    - `const BetaAnalyticsClaudeTagCategoryMonitoring BetaAnalyticsClaudeTagCategory = "monitoring"`

    - `const BetaAnalyticsClaudeTagCategoryProactive BetaAnalyticsClaudeTagCategory = "proactive"`

    - `const BetaAnalyticsClaudeTagCategoryScheduled BetaAnalyticsClaudeTagCategory = "scheduled"`

  - `ClaudeTagUserIDs param.Field[[]string] Optional`

    Filter to Claude Tag (Claude in Slack) usage attributed to specific Slack users, by Slack user ID (for example `U0123ABCDEF`), not claude.ai user ID. Usage that is not Claude Tag, and Claude Tag usage not attributed to a single user, never matches. Use `group_by[]=claude_tag_user_id` to break out per-user values.

    maxItems: 100

  - `ContextWindows param.Field[[]BetaAnalyticsContextWindow] Optional`

    Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

    maxItems: 100

    - `const BetaAnalyticsContextWindowFrom0To200k BetaAnalyticsContextWindow = "0-200k"`

    - `const BetaAnalyticsContextWindowFrom200kTo1M BetaAnalyticsContextWindow = "200k-1M"`

  - `EndingAt param.Field[Time] Optional`

    End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

    format: date-time

  - `GroupBy param.Field[[]string] Optional`

    Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket). Each bucket reports at most its top 100 groups; a group beyond that cap has no row in that bucket (there is no remainder row), so grouped buckets are not exhaustive when a dimension has more than 100 distinct values.

    maxItems: 100

    - `const BetaOrganizationAnalyticsUsageReportListParamsGroupByClaudeTagCategory BetaOrganizationAnalyticsUsageReportListParamsGroupBy = "claude_tag_category"`

    - `const BetaOrganizationAnalyticsUsageReportListParamsGroupByClaudeTagUserID BetaOrganizationAnalyticsUsageReportListParamsGroupBy = "claude_tag_user_id"`

    - `const BetaOrganizationAnalyticsUsageReportListParamsGroupByContextWindow BetaOrganizationAnalyticsUsageReportListParamsGroupBy = "context_window"`

    - `const BetaOrganizationAnalyticsUsageReportListParamsGroupByInferenceGeo BetaOrganizationAnalyticsUsageReportListParamsGroupBy = "inference_geo"`

    - `const BetaOrganizationAnalyticsUsageReportListParamsGroupByModel BetaOrganizationAnalyticsUsageReportListParamsGroupBy = "model"`

    - `const BetaOrganizationAnalyticsUsageReportListParamsGroupByProduct BetaOrganizationAnalyticsUsageReportListParamsGroupBy = "product"`

    - `const BetaOrganizationAnalyticsUsageReportListParamsGroupByRBACGroupID BetaOrganizationAnalyticsUsageReportListParamsGroupBy = "rbac_group_id"`

    - `const BetaOrganizationAnalyticsUsageReportListParamsGroupBySlackChannelID BetaOrganizationAnalyticsUsageReportListParamsGroupBy = "slack_channel_id"`

    - `const BetaOrganizationAnalyticsUsageReportListParamsGroupBySpeed BetaOrganizationAnalyticsUsageReportListParamsGroupBy = "speed"`

  - `InferenceGeos param.Field[[]BetaAnalyticsInferenceGeoFilter] Optional`

    Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

    maxItems: 100

    - `const BetaAnalyticsInferenceGeoFilterGlobal BetaAnalyticsInferenceGeoFilter = "global"`

    - `const BetaAnalyticsInferenceGeoFilterNotAvailable BetaAnalyticsInferenceGeoFilter = "not_available"`

    - `const BetaAnalyticsInferenceGeoFilterUs BetaAnalyticsInferenceGeoFilter = "us"`

  - `Limit param.Field[int64] Optional`

    Maximum number of time buckets per page. Defaults and caps vary by `bucket_width` (`1d`: default 7, max 31; `1h`: default 24, max 168; `1m`: default 60, max 256).

    minimum: 1

  - `Models param.Field[[]string] Optional`

    Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

    maxItems: 100

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page` field.

  - `Products param.Field[[]BetaAnalyticsProductFilter] Optional`

    Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values.

    maxItems: 100

    - `const BetaAnalyticsProductFilterChat BetaAnalyticsProductFilter = "chat"`

    - `const BetaAnalyticsProductFilterClaudeTag BetaAnalyticsProductFilter = "claude-tag"`

    - `const BetaAnalyticsProductFilterClaudeCode BetaAnalyticsProductFilter = "claude_code"`

    - `const BetaAnalyticsProductFilterClaudeDesign BetaAnalyticsProductFilter = "claude_design"`

    - `const BetaAnalyticsProductFilterClaudeInChrome BetaAnalyticsProductFilter = "claude_in_chrome"`

    - `const BetaAnalyticsProductFilterCowork BetaAnalyticsProductFilter = "cowork"`

    - `const BetaAnalyticsProductFilterOfficeAgent BetaAnalyticsProductFilter = "office_agent"`

  - `RBACGroupIDs param.Field[[]string] Optional`

    Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

    maxItems: 100

  - `SlackChannelIDs param.Field[[]string] Optional`

    Filter to usage originating from specific Slack channels. Use `group_by[]=slack_channel_id` to break out per-channel values.

    maxItems: 100

  - `Speeds param.Field[[]string] Optional`

    Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

    maxItems: 100

    - `const BetaOrganizationAnalyticsUsageReportListParamsSpeedFast BetaOrganizationAnalyticsUsageReportListParamsSpeed = "fast"`

    - `const BetaOrganizationAnalyticsUsageReportListParamsSpeedStandard BetaOrganizationAnalyticsUsageReportListParamsSpeed = "standard"`

  - `UserIDs param.Field[[]string] Optional`

    Filter to specific users by tagged user ID.

    maxItems: 100

#### Returns

- `type BetaAnalyticsUsageReportTimeBucket`

  - `EndingAt Time`

    End of the time bucket (exclusive) in RFC 3339 format.

    format: date-time

  - `Results []BetaAnalyticsUsageBucketedResult`

    Rows for this time bucket. Empty when the bucket has no data; otherwise a single combined row when `group_by[]` is omitted, or one row per group (subject to the per-bucket group cap described on the `group_by[]` parameter).

    - `CacheCreation BetaCacheCreation`

      The number of input tokens for cache creation.

      - `Ephemeral1hInputTokens int64`

        The number of input tokens used to create the 1 hour cache entry.

        default: 0, minimum: 0

      - `Ephemeral5mInputTokens int64`

        The number of input tokens used to create the 5 minute cache entry.

        default: 0, minimum: 0

    - `CacheReadInputTokens int64`

      The number of input tokens read from the cache.

    - `ClaudeTagCategory BetaAnalyticsClaudeTagCategory`

      Claude Tag (Claude in Slack) spend category: `engaged` (a person addressed Claude in a channel or thread), `proactive` (Claude responded without being addressed), `scheduled` (a scheduled routine ran), `monitoring` (Claude watching a channel it was asked to monitor), or `dm` (direct messages with Claude). Populated only when `claude_tag_category` is in `group_by[]`; null for usage that is not Claude Tag. Direct-message usage is billed to the individual user and is reported under that user's product, not under `claude-tag`. New categories may be added over time.

      - `const BetaAnalyticsClaudeTagCategoryDm BetaAnalyticsClaudeTagCategory = "dm"`

      - `const BetaAnalyticsClaudeTagCategoryEngaged BetaAnalyticsClaudeTagCategory = "engaged"`

      - `const BetaAnalyticsClaudeTagCategoryMonitoring BetaAnalyticsClaudeTagCategory = "monitoring"`

      - `const BetaAnalyticsClaudeTagCategoryProactive BetaAnalyticsClaudeTagCategory = "proactive"`

      - `const BetaAnalyticsClaudeTagCategoryScheduled BetaAnalyticsClaudeTagCategory = "scheduled"`

    - `ClaudeTagUserID string`

      Slack user ID (for example `U0123ABCDEF`) of the member the Claude Tag (Claude in Slack) usage is attributed to, not a claude.ai user ID. Populated only when `claude_tag_user_id` is in `group_by[]`; null for usage that is not Claude Tag and for Claude Tag usage that is not attributed to a single user (for example `monitoring`, and `proactive` usage Claude initiated), so per-user rows can sum to less than the Claude Tag total. Cannot be combined with `group_by[]=rbac_group_id` or the `rbac_group_ids[]` filter.

    - `ContextWindow BetaAnalyticsContextWindow`

      Context-window pricing tier of the usage or cost. Null unless `context_window` is in `group_by[]`; it can also be null on grouped rows with no context-window tier, such as code execution.

      - `const BetaAnalyticsContextWindowFrom0To200k BetaAnalyticsContextWindow = "0-200k"`

      - `const BetaAnalyticsContextWindowFrom200kTo1M BetaAnalyticsContextWindow = "200k-1M"`

    - `InferenceGeo BetaAnalyticsUsageBucketedResultInferenceGeo`

      Inference region of the usage or cost. Null unless `inference_geo` is in `group_by[]`; it can also be null on grouped rows where the region is not set (the rows that `inference_geos[]=not_available` matches).

      - `const BetaAnalyticsUsageBucketedResultInferenceGeoGlobal BetaAnalyticsUsageBucketedResultInferenceGeo = "global"`

      - `const BetaAnalyticsUsageBucketedResultInferenceGeoUs BetaAnalyticsUsageBucketedResultInferenceGeo = "us"`

    - `Model string`

      Model that produced the usage or cost, as a model name in the form the `models[]` filter accepts (for example, `claude-opus-5`). Null unless `model` is in `group_by[]`; it can also be null on grouped rows whose usage or cost is not attributed to a specific model, such as code execution.

    - `OutputTokens int64`

      The number of output tokens generated.

    - `Product string`

      Product surface that produced the usage or cost. Null unless product is in `group_by[]`; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include `chat`, `claude_code`, `cowork`, `office_agent`, `claude_in_chrome`, `claude_design`, and `claude-tag`. `claude-tag` is Claude Tag, the Claude product in Slack. Some unattributed usage is reported as "other".

    - `RBACGroupID string`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has one id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query without `group_by[]`.

    - `Requests int64`

      Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `ServerToolUse BetaAnalyticsServerToolUse`

      Server-side tool usage metrics.

      - `WebSearchRequests int64`

        The number of web search requests made.

    - `SlackChannelID string`

      Slack channel the usage originated from. Populated only when `slack_channel_id` is in `group_by[]`; null for usage outside Slack (and for rows recorded before channel attribution was enabled).

    - `Speed BetaAnalyticsUsageBucketedResultSpeed`

      Inference speed mode of the usage or cost: `fast` or `standard`. Null unless `speed` is in `group_by[]`.

      - `const BetaAnalyticsUsageBucketedResultSpeedFast BetaAnalyticsUsageBucketedResultSpeed = "fast"`

      - `const BetaAnalyticsUsageBucketedResultSpeedStandard BetaAnalyticsUsageBucketedResultSpeed = "standard"`

    - `UncachedInputTokens int64`

      The number of uncached input tokens processed.

  - `StartingAt Time`

    Start of the time bucket (inclusive) in RFC 3339 format.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"
	"time"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Analytics.UsageReport.List(context.TODO(), anthropic.BetaOrganizationAnalyticsUsageReportListParams{
		StartingAt: time.Now(),
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
        {
          "cache_creation": {
            "ephemeral_1h_input_tokens": 0,
            "ephemeral_5m_input_tokens": 0
          },
          "cache_read_input_tokens": 0,
          "claude_tag_category": "dm",
          "claude_tag_user_id": "U0123ABCDEF",
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-5",
          "output_tokens": 0,
          "product": "chat",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "slack_channel_id": "C0123ABCDEF",
          "speed": "fast",
          "uncached_input_tokens": 0
        }
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Beta › Organization › Analytics › User Usage Report

### Get Per-User Token Usage

`client.Beta.Organization.Analytics.UserUsageReport.List(ctx, query) (*PageCursor[BetaAnalyticsUsageUsersItem], error)`

**GET** `/v1/organizations/analytics/user_usage_report`

Get per-user token usage across a date range.

Returns one row per user, ranked by the chosen token metric. Use this to
see which users consume the most tokens. Only usage attributable to a
seat user is included; for organization-wide totals including direct
API-key and automation traffic, use the bucketed
`/v1/organizations/analytics/usage_report` endpoint. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

#### Parameters

- `query BetaOrganizationAnalyticsUserUsageReportListParams`

  - `StartingAt param.Field[Time]`

    Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

    format: date-time

  - `BucketWidth param.Field[BetaOrganizationAnalyticsUserUsageReportListParamsBucketWidth] Optional`

    Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsBucketWidthDay BetaOrganizationAnalyticsUserUsageReportListParamsBucketWidth = "1d"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsBucketWidthHour BetaOrganizationAnalyticsUserUsageReportListParamsBucketWidth = "1h"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsBucketWidthMinute BetaOrganizationAnalyticsUserUsageReportListParamsBucketWidth = "1m"`

  - `ClaudeTagCategories param.Field[[]BetaAnalyticsClaudeTagCategory] Optional`

    Filter to Claude Tag (Claude in Slack) usage in specific spend categories. Usage with no category never matches. `dm` usage is reported under the user's product rather than `claude-tag`, so combining this filter with `products[]=claude-tag` excludes it. Use `group_by[]=claude_tag_category` to break out per-category values.

    maxItems: 100

    - `const BetaAnalyticsClaudeTagCategoryDm BetaAnalyticsClaudeTagCategory = "dm"`

    - `const BetaAnalyticsClaudeTagCategoryEngaged BetaAnalyticsClaudeTagCategory = "engaged"`

    - `const BetaAnalyticsClaudeTagCategoryMonitoring BetaAnalyticsClaudeTagCategory = "monitoring"`

    - `const BetaAnalyticsClaudeTagCategoryProactive BetaAnalyticsClaudeTagCategory = "proactive"`

    - `const BetaAnalyticsClaudeTagCategoryScheduled BetaAnalyticsClaudeTagCategory = "scheduled"`

  - `ClaudeTagUserIDs param.Field[[]string] Optional`

    Filter to Claude Tag (Claude in Slack) usage attributed to specific Slack users, by Slack user ID (for example `U0123ABCDEF`), not claude.ai user ID. Usage that is not Claude Tag, and Claude Tag usage not attributed to a single user, never matches. Use `group_by[]=claude_tag_user_id` to break out per-user values.

    maxItems: 100

  - `ContextWindows param.Field[[]BetaAnalyticsContextWindow] Optional`

    Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

    maxItems: 100

    - `const BetaAnalyticsContextWindowFrom0To200k BetaAnalyticsContextWindow = "0-200k"`

    - `const BetaAnalyticsContextWindowFrom200kTo1M BetaAnalyticsContextWindow = "200k-1M"`

  - `EndingAt param.Field[Time] Optional`

    End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

    format: date-time

  - `ExcludeDeletedUsers param.Field[bool] Optional`

    If true, omit rows for users who are deleted (`deleted: true`). A page may contain fewer than `limit` rows; use `has_more` and `next_page` to paginate as usual.

  - `GroupBy param.Field[[]string] Optional`

    Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/usage_report` endpoint. `limit` bounds (actor × time bucket × dimension) rows — with dimensions or `bucket_width` present, one actor may span several rows.

    maxItems: 100

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsGroupByClaudeTagCategory BetaOrganizationAnalyticsUserUsageReportListParamsGroupBy = "claude_tag_category"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsGroupByClaudeTagUserID BetaOrganizationAnalyticsUserUsageReportListParamsGroupBy = "claude_tag_user_id"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsGroupByContextWindow BetaOrganizationAnalyticsUserUsageReportListParamsGroupBy = "context_window"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsGroupByInferenceGeo BetaOrganizationAnalyticsUserUsageReportListParamsGroupBy = "inference_geo"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsGroupByModel BetaOrganizationAnalyticsUserUsageReportListParamsGroupBy = "model"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsGroupByProduct BetaOrganizationAnalyticsUserUsageReportListParamsGroupBy = "product"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsGroupByRBACGroupID BetaOrganizationAnalyticsUserUsageReportListParamsGroupBy = "rbac_group_id"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsGroupBySlackChannelID BetaOrganizationAnalyticsUserUsageReportListParamsGroupBy = "slack_channel_id"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsGroupBySpeed BetaOrganizationAnalyticsUserUsageReportListParamsGroupBy = "speed"`

  - `InferenceGeos param.Field[[]BetaAnalyticsInferenceGeoFilter] Optional`

    Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

    maxItems: 100

    - `const BetaAnalyticsInferenceGeoFilterGlobal BetaAnalyticsInferenceGeoFilter = "global"`

    - `const BetaAnalyticsInferenceGeoFilterNotAvailable BetaAnalyticsInferenceGeoFilter = "not_available"`

    - `const BetaAnalyticsInferenceGeoFilterUs BetaAnalyticsInferenceGeoFilter = "us"`

  - `Limit param.Field[int64] Optional`

    Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

    minimum: 1, maximum: 1000

  - `Models param.Field[[]string] Optional`

    Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

    maxItems: 100

  - `Order param.Field[BetaOrganizationAnalyticsUserUsageReportListParamsOrder] Optional`

    Sort direction. Defaults to `desc`.

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsOrderAsc BetaOrganizationAnalyticsUserUsageReportListParamsOrder = "asc"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsOrderDesc BetaOrganizationAnalyticsUserUsageReportListParamsOrder = "desc"`

  - `OrderBy param.Field[BetaOrganizationAnalyticsUserUsageReportListParamsOrderBy] Optional`

    Metric to rank actors by. Defaults to `total_tokens`.

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsOrderByOutputTokens BetaOrganizationAnalyticsUserUsageReportListParamsOrderBy = "output_tokens"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsOrderByRequests BetaOrganizationAnalyticsUserUsageReportListParamsOrderBy = "requests"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsOrderByTotalTokens BetaOrganizationAnalyticsUserUsageReportListParamsOrderBy = "total_tokens"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsOrderByUncachedInputTokens BetaOrganizationAnalyticsUserUsageReportListParamsOrderBy = "uncached_input_tokens"`

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page` field.

  - `Products param.Field[[]BetaAnalyticsProductFilter] Optional`

    Product surfaces to include. Defaults to all products.

    maxItems: 100

    - `const BetaAnalyticsProductFilterChat BetaAnalyticsProductFilter = "chat"`

    - `const BetaAnalyticsProductFilterClaudeTag BetaAnalyticsProductFilter = "claude-tag"`

    - `const BetaAnalyticsProductFilterClaudeCode BetaAnalyticsProductFilter = "claude_code"`

    - `const BetaAnalyticsProductFilterClaudeDesign BetaAnalyticsProductFilter = "claude_design"`

    - `const BetaAnalyticsProductFilterClaudeInChrome BetaAnalyticsProductFilter = "claude_in_chrome"`

    - `const BetaAnalyticsProductFilterCowork BetaAnalyticsProductFilter = "cowork"`

    - `const BetaAnalyticsProductFilterOfficeAgent BetaAnalyticsProductFilter = "office_agent"`

  - `RBACGroupIDs param.Field[[]string] Optional`

    Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

    maxItems: 100

  - `SlackChannelIDs param.Field[[]string] Optional`

    Filter to usage originating from specific Slack channels. Use `group_by[]=slack_channel_id` to break out per-channel values.

    maxItems: 100

  - `Speeds param.Field[[]string] Optional`

    Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

    maxItems: 100

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsSpeedFast BetaOrganizationAnalyticsUserUsageReportListParamsSpeed = "fast"`

    - `const BetaOrganizationAnalyticsUserUsageReportListParamsSpeedStandard BetaOrganizationAnalyticsUserUsageReportListParamsSpeed = "standard"`

  - `UserIDs param.Field[[]string] Optional`

    Filter to specific users by tagged user ID.

    maxItems: 100

#### Returns

- `type BetaAnalyticsUsageUsersItem`

  - `Actor BetaAnalyticsUserActor`

    The user this row's usage or cost is attributed to. Always a `user_actor`.

    - `Type UserActor`

      Actor type. Always `"user_actor"`.

    - `Deleted bool`

      True when the account has been deleted, or when the user is no longer a member of the organization or its associated organizations (for example, their membership was removed or they were deprovisioned via your identity provider). `email_address` stays populated for removed users and is null when the account has been deleted. `name` follows the rules described on that field. The `user_id` is still populated for reconciliation.

    - `EmailAddress string`

      The user's email address, including for users who are no longer members of the organization or its associated organizations. Null when the account has been deleted (check `deleted`) and for system-minted service accounts, which have no person's mailbox behind them (check `name`).

    - `Name string`

      The user's full name. Null when the user has not set a name. Returns `"Deleted User"` when the account itself has been deleted, or when the user is no longer a member of the organization or its associated organizations and the organization has chosen to hide the names of removed users. Otherwise, the name stays populated for removed users. Rows for system-minted service accounts render the service name (for example, `"Claude Security"` for usage by Anthropic's security-patching service) or null.

    - `UserID string`

      Tagged user ID.

  - `CacheCreation BetaCacheCreation`

    The number of input tokens for cache creation.

    - `Ephemeral1hInputTokens int64`

      The number of input tokens used to create the 1 hour cache entry.

      default: 0, minimum: 0

    - `Ephemeral5mInputTokens int64`

      The number of input tokens used to create the 5 minute cache entry.

      default: 0, minimum: 0

  - `CacheReadInputTokens int64`

    The number of input tokens read from the cache.

  - `ClaudeTagCategory BetaAnalyticsClaudeTagCategory`

    Claude Tag (Claude in Slack) spend category: `engaged` (a person addressed Claude in a channel or thread), `proactive` (Claude responded without being addressed), `scheduled` (a scheduled routine ran), `monitoring` (Claude watching a channel it was asked to monitor), or `dm` (direct messages with Claude). Populated only when `claude_tag_category` is in `group_by[]`; null for usage that is not Claude Tag. Direct-message usage is billed to the individual user and is reported under that user's product, not under `claude-tag`. New categories may be added over time.

    - `const BetaAnalyticsClaudeTagCategoryDm BetaAnalyticsClaudeTagCategory = "dm"`

    - `const BetaAnalyticsClaudeTagCategoryEngaged BetaAnalyticsClaudeTagCategory = "engaged"`

    - `const BetaAnalyticsClaudeTagCategoryMonitoring BetaAnalyticsClaudeTagCategory = "monitoring"`

    - `const BetaAnalyticsClaudeTagCategoryProactive BetaAnalyticsClaudeTagCategory = "proactive"`

    - `const BetaAnalyticsClaudeTagCategoryScheduled BetaAnalyticsClaudeTagCategory = "scheduled"`

  - `ClaudeTagUserID string`

    Slack user ID (for example `U0123ABCDEF`) of the member the Claude Tag (Claude in Slack) usage is attributed to, not a claude.ai user ID. Populated only when `claude_tag_user_id` is in `group_by[]`; null for usage that is not Claude Tag and for Claude Tag usage that is not attributed to a single user (for example `monitoring`, and `proactive` usage Claude initiated), so per-user rows can sum to less than the Claude Tag total. Cannot be combined with `group_by[]=rbac_group_id` or the `rbac_group_ids[]` filter.

  - `ContextWindow BetaAnalyticsContextWindow`

    Context-window pricing tier of the usage or cost. Null unless `context_window` is in `group_by[]`; it can also be null on grouped rows with no context-window tier, such as code execution.

    - `const BetaAnalyticsContextWindowFrom0To200k BetaAnalyticsContextWindow = "0-200k"`

    - `const BetaAnalyticsContextWindowFrom200kTo1M BetaAnalyticsContextWindow = "200k-1M"`

  - `EndingAt Time`

    End of the row's UTC time bucket (exclusive), as an RFC 3339 timestamp; equal to `starting_at` plus one `bucket_width`. Null unless `bucket_width` is set.

    format: date-time

  - `InferenceGeo BetaAnalyticsUsageUsersItemInferenceGeo`

    Inference region of the usage or cost. Null unless `inference_geo` is in `group_by[]`; it can also be null on grouped rows where the region is not set (the rows that `inference_geos[]=not_available` matches).

    - `const BetaAnalyticsUsageUsersItemInferenceGeoGlobal BetaAnalyticsUsageUsersItemInferenceGeo = "global"`

    - `const BetaAnalyticsUsageUsersItemInferenceGeoUs BetaAnalyticsUsageUsersItemInferenceGeo = "us"`

  - `Model string`

    Model that produced the usage or cost, as a model name in the form the `models[]` filter accepts (for example, `claude-opus-5`). Null unless `model` is in `group_by[]`; it can also be null on grouped rows whose usage or cost is not attributed to a specific model, such as code execution.

  - `OutputTokens int64`

    The number of output tokens generated.

  - `Product string`

    Product surface that produced the usage or cost. Null unless product is in `group_by[]`; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include `chat`, `claude_code`, `cowork`, `office_agent`, `claude_in_chrome`, `claude_design`, and `claude-tag`. `claude-tag` is Claude Tag, the Claude product in Slack. Some unattributed usage is reported as "other".

  - `RBACGroupID string`

    RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has one id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query without `group_by[]`.

  - `Requests int64`

    Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

  - `ServerToolUse BetaAnalyticsServerToolUse`

    Server-side tool usage metrics.

    - `WebSearchRequests int64`

      The number of web search requests made.

  - `SlackChannelID string`

    Slack channel the usage originated from. Populated only when `slack_channel_id` is in `group_by[]`; null for usage outside Slack (and for rows recorded before channel attribution was enabled).

  - `Speed BetaAnalyticsUsageUsersItemSpeed`

    Inference speed mode of the usage or cost: `fast` or `standard`. Null unless `speed` is in `group_by[]`.

    - `const BetaAnalyticsUsageUsersItemSpeedFast BetaAnalyticsUsageUsersItemSpeed = "fast"`

    - `const BetaAnalyticsUsageUsersItemSpeedStandard BetaAnalyticsUsageUsersItemSpeed = "standard"`

  - `StartingAt Time`

    Start of the row's UTC time bucket (inclusive), as an RFC 3339 timestamp. Null unless `bucket_width` is set; without `bucket_width`, each row aggregates the full requested range.

    format: date-time

  - `TotalTokens int64`

    Total token count across all token types. This is the value the default `order_by` (`total_tokens`) sorts on.

  - `UncachedInputTokens int64`

    The number of uncached input tokens processed.

#### Example

```go
package main

import (
	"context"
	"fmt"
	"time"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Analytics.UserUsageReport.List(context.TODO(), anthropic.BetaOrganizationAnalyticsUserUsageReportListParams{
		StartingAt: time.Now(),
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "actor": {
        "deleted": true,
        "email": "jane@example.com",
        "email_address": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor",
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt"
      },
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "cache_read_input_tokens": 3200000,
      "claude_tag_category": "dm",
      "claude_tag_user_id": "U0123ABCDEF",
      "context_window": "0-200k",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "model": "claude-opus-5",
      "output_tokens": 891000,
      "product": "chat",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "server_tool_use": {
        "web_search_requests": 10
      },
      "slack_channel_id": "C0123ABCDEF",
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "total_tokens": 5377000,
      "uncached_input_tokens": 1284500
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Beta › Organization › Analytics › Cost Report

### Get Cost Over Time

`client.Beta.Organization.Analytics.CostReport.List(ctx, query) (*PageCursor[BetaAnalyticsCostReportTimeBucket], error)`

**GET** `/v1/organizations/analytics/cost_report`

Get cost in USD over time across a date range.

Returns cost bucketed by minute, hour, or day, optionally broken down by
product, model, context window, inference region, speed, cost type, or
token type. Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

#### Parameters

- `query BetaOrganizationAnalyticsCostReportListParams`

  - `StartingAt param.Field[Time]`

    Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

    format: date-time

  - `BucketWidth param.Field[BetaOrganizationAnalyticsCostReportListParamsBucketWidth] Optional`

    Time bucket granularity.

    - `const BetaOrganizationAnalyticsCostReportListParamsBucketWidthDay BetaOrganizationAnalyticsCostReportListParamsBucketWidth = "1d"`

    - `const BetaOrganizationAnalyticsCostReportListParamsBucketWidthHour BetaOrganizationAnalyticsCostReportListParamsBucketWidth = "1h"`

    - `const BetaOrganizationAnalyticsCostReportListParamsBucketWidthMinute BetaOrganizationAnalyticsCostReportListParamsBucketWidth = "1m"`

  - `ClaudeTagCategories param.Field[[]BetaAnalyticsClaudeTagCategory] Optional`

    Filter to Claude Tag (Claude in Slack) usage in specific spend categories. Usage with no category never matches. `dm` usage is reported under the user's product rather than `claude-tag`, so combining this filter with `products[]=claude-tag` excludes it. Use `group_by[]=claude_tag_category` to break out per-category values.

    maxItems: 100

    - `const BetaAnalyticsClaudeTagCategoryDm BetaAnalyticsClaudeTagCategory = "dm"`

    - `const BetaAnalyticsClaudeTagCategoryEngaged BetaAnalyticsClaudeTagCategory = "engaged"`

    - `const BetaAnalyticsClaudeTagCategoryMonitoring BetaAnalyticsClaudeTagCategory = "monitoring"`

    - `const BetaAnalyticsClaudeTagCategoryProactive BetaAnalyticsClaudeTagCategory = "proactive"`

    - `const BetaAnalyticsClaudeTagCategoryScheduled BetaAnalyticsClaudeTagCategory = "scheduled"`

  - `ClaudeTagUserIDs param.Field[[]string] Optional`

    Filter to Claude Tag (Claude in Slack) usage attributed to specific Slack users, by Slack user ID (for example `U0123ABCDEF`), not claude.ai user ID. Usage that is not Claude Tag, and Claude Tag usage not attributed to a single user, never matches. Use `group_by[]=claude_tag_user_id` to break out per-user values.

    maxItems: 100

  - `ContextWindows param.Field[[]BetaAnalyticsContextWindow] Optional`

    Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

    maxItems: 100

    - `const BetaAnalyticsContextWindowFrom0To200k BetaAnalyticsContextWindow = "0-200k"`

    - `const BetaAnalyticsContextWindowFrom200kTo1M BetaAnalyticsContextWindow = "200k-1M"`

  - `EndingAt param.Field[Time] Optional`

    End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

    format: date-time

  - `GroupBy param.Field[[]string] Optional`

    Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket). Each bucket reports at most its top 100 groups; a group beyond that cap has no row in that bucket (there is no remainder row), so grouped buckets are not exhaustive when a dimension has more than 100 distinct values.

    maxItems: 100

    - `const BetaOrganizationAnalyticsCostReportListParamsGroupByClaudeTagCategory BetaOrganizationAnalyticsCostReportListParamsGroupBy = "claude_tag_category"`

    - `const BetaOrganizationAnalyticsCostReportListParamsGroupByClaudeTagUserID BetaOrganizationAnalyticsCostReportListParamsGroupBy = "claude_tag_user_id"`

    - `const BetaOrganizationAnalyticsCostReportListParamsGroupByContextWindow BetaOrganizationAnalyticsCostReportListParamsGroupBy = "context_window"`

    - `const BetaOrganizationAnalyticsCostReportListParamsGroupByCostType BetaOrganizationAnalyticsCostReportListParamsGroupBy = "cost_type"`

    - `const BetaOrganizationAnalyticsCostReportListParamsGroupByInferenceGeo BetaOrganizationAnalyticsCostReportListParamsGroupBy = "inference_geo"`

    - `const BetaOrganizationAnalyticsCostReportListParamsGroupByModel BetaOrganizationAnalyticsCostReportListParamsGroupBy = "model"`

    - `const BetaOrganizationAnalyticsCostReportListParamsGroupByProduct BetaOrganizationAnalyticsCostReportListParamsGroupBy = "product"`

    - `const BetaOrganizationAnalyticsCostReportListParamsGroupByRBACGroupID BetaOrganizationAnalyticsCostReportListParamsGroupBy = "rbac_group_id"`

    - `const BetaOrganizationAnalyticsCostReportListParamsGroupBySlackChannelID BetaOrganizationAnalyticsCostReportListParamsGroupBy = "slack_channel_id"`

    - `const BetaOrganizationAnalyticsCostReportListParamsGroupBySpeed BetaOrganizationAnalyticsCostReportListParamsGroupBy = "speed"`

    - `const BetaOrganizationAnalyticsCostReportListParamsGroupByTokenType BetaOrganizationAnalyticsCostReportListParamsGroupBy = "token_type"`

  - `InferenceGeos param.Field[[]BetaAnalyticsInferenceGeoFilter] Optional`

    Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

    maxItems: 100

    - `const BetaAnalyticsInferenceGeoFilterGlobal BetaAnalyticsInferenceGeoFilter = "global"`

    - `const BetaAnalyticsInferenceGeoFilterNotAvailable BetaAnalyticsInferenceGeoFilter = "not_available"`

    - `const BetaAnalyticsInferenceGeoFilterUs BetaAnalyticsInferenceGeoFilter = "us"`

  - `Limit param.Field[int64] Optional`

    Maximum number of time buckets per page. Defaults and caps vary by `bucket_width` (`1d`: default 7, max 31; `1h`: default 24, max 168; `1m`: default 60, max 256).

    minimum: 1

  - `Models param.Field[[]string] Optional`

    Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

    maxItems: 100

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page` field.

  - `Products param.Field[[]BetaAnalyticsProductFilter] Optional`

    Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values.

    maxItems: 100

    - `const BetaAnalyticsProductFilterChat BetaAnalyticsProductFilter = "chat"`

    - `const BetaAnalyticsProductFilterClaudeTag BetaAnalyticsProductFilter = "claude-tag"`

    - `const BetaAnalyticsProductFilterClaudeCode BetaAnalyticsProductFilter = "claude_code"`

    - `const BetaAnalyticsProductFilterClaudeDesign BetaAnalyticsProductFilter = "claude_design"`

    - `const BetaAnalyticsProductFilterClaudeInChrome BetaAnalyticsProductFilter = "claude_in_chrome"`

    - `const BetaAnalyticsProductFilterCowork BetaAnalyticsProductFilter = "cowork"`

    - `const BetaAnalyticsProductFilterOfficeAgent BetaAnalyticsProductFilter = "office_agent"`

  - `RBACGroupIDs param.Field[[]string] Optional`

    Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

    maxItems: 100

  - `SlackChannelIDs param.Field[[]string] Optional`

    Filter to usage originating from specific Slack channels. Use `group_by[]=slack_channel_id` to break out per-channel values.

    maxItems: 100

  - `Speeds param.Field[[]string] Optional`

    Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

    maxItems: 100

    - `const BetaOrganizationAnalyticsCostReportListParamsSpeedFast BetaOrganizationAnalyticsCostReportListParamsSpeed = "fast"`

    - `const BetaOrganizationAnalyticsCostReportListParamsSpeedStandard BetaOrganizationAnalyticsCostReportListParamsSpeed = "standard"`

  - `UserIDs param.Field[[]string] Optional`

    Filter to specific users by tagged user ID.

    maxItems: 100

#### Returns

- `type BetaAnalyticsCostReportTimeBucket`

  - `EndingAt Time`

    End of the time bucket (exclusive) in RFC 3339 format.

    format: date-time

  - `Results []BetaAnalyticsCostBucketedResult`

    Rows for this time bucket. Empty when the bucket has no data; otherwise a single combined row when `group_by[]` is omitted, or one row per group (subject to the per-bucket group cap described on the `group_by[]` parameter).

    - `Amount string`

      Amount (post-discount, pre-credit) in fractional cents.

    - `ClaudeTagCategory BetaAnalyticsClaudeTagCategory`

      Claude Tag (Claude in Slack) spend category: `engaged` (a person addressed Claude in a channel or thread), `proactive` (Claude responded without being addressed), `scheduled` (a scheduled routine ran), `monitoring` (Claude watching a channel it was asked to monitor), or `dm` (direct messages with Claude). Populated only when `claude_tag_category` is in `group_by[]`; null for usage that is not Claude Tag. Direct-message usage is billed to the individual user and is reported under that user's product, not under `claude-tag`. New categories may be added over time.

      - `const BetaAnalyticsClaudeTagCategoryDm BetaAnalyticsClaudeTagCategory = "dm"`

      - `const BetaAnalyticsClaudeTagCategoryEngaged BetaAnalyticsClaudeTagCategory = "engaged"`

      - `const BetaAnalyticsClaudeTagCategoryMonitoring BetaAnalyticsClaudeTagCategory = "monitoring"`

      - `const BetaAnalyticsClaudeTagCategoryProactive BetaAnalyticsClaudeTagCategory = "proactive"`

      - `const BetaAnalyticsClaudeTagCategoryScheduled BetaAnalyticsClaudeTagCategory = "scheduled"`

    - `ClaudeTagUserID string`

      Slack user ID (for example `U0123ABCDEF`) of the member the Claude Tag (Claude in Slack) usage is attributed to, not a claude.ai user ID. Populated only when `claude_tag_user_id` is in `group_by[]`; null for usage that is not Claude Tag and for Claude Tag usage that is not attributed to a single user (for example `monitoring`, and `proactive` usage Claude initiated), so per-user rows can sum to less than the Claude Tag total. Cannot be combined with `group_by[]=rbac_group_id` or the `rbac_group_ids[]` filter.

    - `ContextWindow BetaAnalyticsContextWindow`

      Context-window pricing tier of the usage or cost. Null unless `context_window` is in `group_by[]`; it can also be null on grouped rows with no context-window tier, such as code execution.

      - `const BetaAnalyticsContextWindowFrom0To200k BetaAnalyticsContextWindow = "0-200k"`

      - `const BetaAnalyticsContextWindowFrom200kTo1M BetaAnalyticsContextWindow = "200k-1M"`

    - `CostType BetaAnalyticsCostType`

      Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).

      - `const BetaAnalyticsCostTypeCodeExecution BetaAnalyticsCostType = "code_execution"`

      - `const BetaAnalyticsCostTypeTokens BetaAnalyticsCostType = "tokens"`

      - `const BetaAnalyticsCostTypeWebSearch BetaAnalyticsCostType = "web_search"`

    - `Currency string`

      Currency code for the cost amount. Currently always `"USD"`.

      default: USD

    - `InferenceGeo BetaAnalyticsCostBucketedResultInferenceGeo`

      Inference region of the usage or cost. Null unless `inference_geo` is in `group_by[]`; it can also be null on grouped rows where the region is not set (the rows that `inference_geos[]=not_available` matches).

      - `const BetaAnalyticsCostBucketedResultInferenceGeoGlobal BetaAnalyticsCostBucketedResultInferenceGeo = "global"`

      - `const BetaAnalyticsCostBucketedResultInferenceGeoUs BetaAnalyticsCostBucketedResultInferenceGeo = "us"`

    - `ListAmount string`

      List-price amount (pre-discount) in fractional cents.

    - `Model string`

      Model that produced the usage or cost, as a model name in the form the `models[]` filter accepts (for example, `claude-opus-5`). Null unless `model` is in `group_by[]`; it can also be null on grouped rows whose usage or cost is not attributed to a specific model, such as code execution.

    - `Product string`

      Product surface that produced the usage or cost. Null unless product is in `group_by[]`; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include `chat`, `claude_code`, `cowork`, `office_agent`, `claude_in_chrome`, `claude_design`, and `claude-tag`. `claude-tag` is Claude Tag, the Claude product in Slack. Some unattributed usage is reported as "other".

    - `RBACGroupID string`

      RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has one id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query without `group_by[]`.

    - `Requests int64`

      Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

    - `SlackChannelID string`

      Slack channel the usage originated from. Populated only when `slack_channel_id` is in `group_by[]`; null for usage outside Slack (and for rows recorded before channel attribution was enabled).

    - `Speed BetaAnalyticsCostBucketedResultSpeed`

      Inference speed mode of the usage or cost: `fast` or `standard`. Null unless `speed` is in `group_by[]`.

      - `const BetaAnalyticsCostBucketedResultSpeedFast BetaAnalyticsCostBucketedResultSpeed = "fast"`

      - `const BetaAnalyticsCostBucketedResultSpeedStandard BetaAnalyticsCostBucketedResultSpeed = "standard"`

    - `TokenType BetaAnalyticsTokenType`

      Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.

      - `const BetaAnalyticsTokenTypeCacheCreationEphemeral1hInputTokens BetaAnalyticsTokenType = "cache_creation.ephemeral_1h_input_tokens"`

      - `const BetaAnalyticsTokenTypeCacheCreationEphemeral5mInputTokens BetaAnalyticsTokenType = "cache_creation.ephemeral_5m_input_tokens"`

      - `const BetaAnalyticsTokenTypeCacheReadInputTokens BetaAnalyticsTokenType = "cache_read_input_tokens"`

      - `const BetaAnalyticsTokenTypeOutputTokens BetaAnalyticsTokenType = "output_tokens"`

      - `const BetaAnalyticsTokenTypeUncachedInputTokens BetaAnalyticsTokenType = "uncached_input_tokens"`

  - `StartingAt Time`

    Start of the time bucket (inclusive) in RFC 3339 format.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"
	"time"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Analytics.CostReport.List(context.TODO(), anthropic.BetaOrganizationAnalyticsCostReportListParams{
		StartingAt: time.Now(),
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
        {
          "amount": "amount",
          "claude_tag_category": "dm",
          "claude_tag_user_id": "U0123ABCDEF",
          "context_window": "0-200k",
          "cost_type": "code_execution",
          "currency": "USD",
          "inference_geo": "global",
          "list_amount": "list_amount",
          "model": "claude-opus-5",
          "product": "chat",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "slack_channel_id": "C0123ABCDEF",
          "speed": "fast",
          "token_type": "cache_creation.ephemeral_1h_input_tokens"
        }
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Beta › Organization › Analytics › User Cost Report

### Get Per-User Cost

`client.Beta.Organization.Analytics.UserCostReport.List(ctx, query) (*PageCursor[BetaAnalyticsCostUsersItem], error)`

**GET** `/v1/organizations/analytics/user_cost_report`

Get per-user cost in USD across a date range.

Returns one row per user, ranked by spend. Use this to see which users
account for the most cost. Only cost attributable to a seat user is
included; for organization-wide totals including direct API-key and
automation traffic, use the bucketed
`/v1/organizations/analytics/cost_report` endpoint. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

#### Parameters

- `query BetaOrganizationAnalyticsUserCostReportListParams`

  - `StartingAt param.Field[Time]`

    Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

    format: date-time

  - `BucketWidth param.Field[BetaOrganizationAnalyticsUserCostReportListParamsBucketWidth] Optional`

    Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

    - `const BetaOrganizationAnalyticsUserCostReportListParamsBucketWidthDay BetaOrganizationAnalyticsUserCostReportListParamsBucketWidth = "1d"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsBucketWidthHour BetaOrganizationAnalyticsUserCostReportListParamsBucketWidth = "1h"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsBucketWidthMinute BetaOrganizationAnalyticsUserCostReportListParamsBucketWidth = "1m"`

  - `ClaudeTagCategories param.Field[[]BetaAnalyticsClaudeTagCategory] Optional`

    Filter to Claude Tag (Claude in Slack) usage in specific spend categories. Usage with no category never matches. `dm` usage is reported under the user's product rather than `claude-tag`, so combining this filter with `products[]=claude-tag` excludes it. Use `group_by[]=claude_tag_category` to break out per-category values.

    maxItems: 100

    - `const BetaAnalyticsClaudeTagCategoryDm BetaAnalyticsClaudeTagCategory = "dm"`

    - `const BetaAnalyticsClaudeTagCategoryEngaged BetaAnalyticsClaudeTagCategory = "engaged"`

    - `const BetaAnalyticsClaudeTagCategoryMonitoring BetaAnalyticsClaudeTagCategory = "monitoring"`

    - `const BetaAnalyticsClaudeTagCategoryProactive BetaAnalyticsClaudeTagCategory = "proactive"`

    - `const BetaAnalyticsClaudeTagCategoryScheduled BetaAnalyticsClaudeTagCategory = "scheduled"`

  - `ClaudeTagUserIDs param.Field[[]string] Optional`

    Filter to Claude Tag (Claude in Slack) usage attributed to specific Slack users, by Slack user ID (for example `U0123ABCDEF`), not claude.ai user ID. Usage that is not Claude Tag, and Claude Tag usage not attributed to a single user, never matches. Use `group_by[]=claude_tag_user_id` to break out per-user values.

    maxItems: 100

  - `ContextWindows param.Field[[]BetaAnalyticsContextWindow] Optional`

    Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

    maxItems: 100

    - `const BetaAnalyticsContextWindowFrom0To200k BetaAnalyticsContextWindow = "0-200k"`

    - `const BetaAnalyticsContextWindowFrom200kTo1M BetaAnalyticsContextWindow = "200k-1M"`

  - `EndingAt param.Field[Time] Optional`

    End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

    format: date-time

  - `ExcludeDeletedUsers param.Field[bool] Optional`

    If true, omit rows for users who are deleted (`deleted: true`). A page may contain fewer than `limit` rows; use `has_more` and `next_page` to paginate as usual.

  - `GroupBy param.Field[[]string] Optional`

    Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/cost_report` endpoint. The `product`, `model`, `context_window`, `inference_geo`, and `speed` dimensions — and the time bucket, when `bucket_width` is set — count toward `limit`. `cost_type` and `token_type` do not: `cost_type` returns one row per cost component (tokens, web search, code execution); `token_type` returns one row per token type, each with `cost_type: "tokens"`; combining both returns the per-token-type rows plus the web-search and code-execution rows. A page can therefore contain more rows than `limit` when `cost_type` or `token_type` is requested.

    maxItems: 100

    - `const BetaOrganizationAnalyticsUserCostReportListParamsGroupByClaudeTagCategory BetaOrganizationAnalyticsUserCostReportListParamsGroupBy = "claude_tag_category"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsGroupByClaudeTagUserID BetaOrganizationAnalyticsUserCostReportListParamsGroupBy = "claude_tag_user_id"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsGroupByContextWindow BetaOrganizationAnalyticsUserCostReportListParamsGroupBy = "context_window"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsGroupByCostType BetaOrganizationAnalyticsUserCostReportListParamsGroupBy = "cost_type"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsGroupByInferenceGeo BetaOrganizationAnalyticsUserCostReportListParamsGroupBy = "inference_geo"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsGroupByModel BetaOrganizationAnalyticsUserCostReportListParamsGroupBy = "model"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsGroupByProduct BetaOrganizationAnalyticsUserCostReportListParamsGroupBy = "product"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsGroupByRBACGroupID BetaOrganizationAnalyticsUserCostReportListParamsGroupBy = "rbac_group_id"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsGroupBySlackChannelID BetaOrganizationAnalyticsUserCostReportListParamsGroupBy = "slack_channel_id"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsGroupBySpeed BetaOrganizationAnalyticsUserCostReportListParamsGroupBy = "speed"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsGroupByTokenType BetaOrganizationAnalyticsUserCostReportListParamsGroupBy = "token_type"`

  - `InferenceGeos param.Field[[]BetaAnalyticsInferenceGeoFilter] Optional`

    Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

    maxItems: 100

    - `const BetaAnalyticsInferenceGeoFilterGlobal BetaAnalyticsInferenceGeoFilter = "global"`

    - `const BetaAnalyticsInferenceGeoFilterNotAvailable BetaAnalyticsInferenceGeoFilter = "not_available"`

    - `const BetaAnalyticsInferenceGeoFilterUs BetaAnalyticsInferenceGeoFilter = "us"`

  - `Limit param.Field[int64] Optional`

    Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

    minimum: 1, maximum: 1000

  - `Models param.Field[[]string] Optional`

    Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

    maxItems: 100

  - `Order param.Field[BetaOrganizationAnalyticsUserCostReportListParamsOrder] Optional`

    Sort direction. Defaults to `desc`.

    - `const BetaOrganizationAnalyticsUserCostReportListParamsOrderAsc BetaOrganizationAnalyticsUserCostReportListParamsOrder = "asc"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsOrderDesc BetaOrganizationAnalyticsUserCostReportListParamsOrder = "desc"`

  - `OrderBy param.Field[BetaOrganizationAnalyticsUserCostReportListParamsOrderBy] Optional`

    Metric to rank actors by. Defaults to `amount`.

    - `const BetaOrganizationAnalyticsUserCostReportListParamsOrderByAmount BetaOrganizationAnalyticsUserCostReportListParamsOrderBy = "amount"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsOrderByListAmount BetaOrganizationAnalyticsUserCostReportListParamsOrderBy = "list_amount"`

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page` field.

  - `Products param.Field[[]BetaAnalyticsProductFilter] Optional`

    Product surfaces to include. Defaults to all products.

    maxItems: 100

    - `const BetaAnalyticsProductFilterChat BetaAnalyticsProductFilter = "chat"`

    - `const BetaAnalyticsProductFilterClaudeTag BetaAnalyticsProductFilter = "claude-tag"`

    - `const BetaAnalyticsProductFilterClaudeCode BetaAnalyticsProductFilter = "claude_code"`

    - `const BetaAnalyticsProductFilterClaudeDesign BetaAnalyticsProductFilter = "claude_design"`

    - `const BetaAnalyticsProductFilterClaudeInChrome BetaAnalyticsProductFilter = "claude_in_chrome"`

    - `const BetaAnalyticsProductFilterCowork BetaAnalyticsProductFilter = "cowork"`

    - `const BetaAnalyticsProductFilterOfficeAgent BetaAnalyticsProductFilter = "office_agent"`

  - `RBACGroupIDs param.Field[[]string] Optional`

    Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

    maxItems: 100

  - `SlackChannelIDs param.Field[[]string] Optional`

    Filter to usage originating from specific Slack channels. Use `group_by[]=slack_channel_id` to break out per-channel values.

    maxItems: 100

  - `Speeds param.Field[[]string] Optional`

    Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

    maxItems: 100

    - `const BetaOrganizationAnalyticsUserCostReportListParamsSpeedFast BetaOrganizationAnalyticsUserCostReportListParamsSpeed = "fast"`

    - `const BetaOrganizationAnalyticsUserCostReportListParamsSpeedStandard BetaOrganizationAnalyticsUserCostReportListParamsSpeed = "standard"`

  - `UserIDs param.Field[[]string] Optional`

    Filter to specific users by tagged user ID.

    maxItems: 100

#### Returns

- `type BetaAnalyticsCostUsersItem`

  - `Actor BetaAnalyticsUserActor`

    The user this row's usage or cost is attributed to. Always a `user_actor`.

    - `Type UserActor`

      Actor type. Always `"user_actor"`.

    - `Deleted bool`

      True when the account has been deleted, or when the user is no longer a member of the organization or its associated organizations (for example, their membership was removed or they were deprovisioned via your identity provider). `email_address` stays populated for removed users and is null when the account has been deleted. `name` follows the rules described on that field. The `user_id` is still populated for reconciliation.

    - `EmailAddress string`

      The user's email address, including for users who are no longer members of the organization or its associated organizations. Null when the account has been deleted (check `deleted`) and for system-minted service accounts, which have no person's mailbox behind them (check `name`).

    - `Name string`

      The user's full name. Null when the user has not set a name. Returns `"Deleted User"` when the account itself has been deleted, or when the user is no longer a member of the organization or its associated organizations and the organization has chosen to hide the names of removed users. Otherwise, the name stays populated for removed users. Rows for system-minted service accounts render the service name (for example, `"Claude Security"` for usage by Anthropic's security-patching service) or null.

    - `UserID string`

      Tagged user ID.

  - `Amount string`

    Amount (post-discount, pre-credit) in fractional cents (minor units).

  - `ClaudeTagCategory BetaAnalyticsClaudeTagCategory`

    Claude Tag (Claude in Slack) spend category: `engaged` (a person addressed Claude in a channel or thread), `proactive` (Claude responded without being addressed), `scheduled` (a scheduled routine ran), `monitoring` (Claude watching a channel it was asked to monitor), or `dm` (direct messages with Claude). Populated only when `claude_tag_category` is in `group_by[]`; null for usage that is not Claude Tag. Direct-message usage is billed to the individual user and is reported under that user's product, not under `claude-tag`. New categories may be added over time.

    - `const BetaAnalyticsClaudeTagCategoryDm BetaAnalyticsClaudeTagCategory = "dm"`

    - `const BetaAnalyticsClaudeTagCategoryEngaged BetaAnalyticsClaudeTagCategory = "engaged"`

    - `const BetaAnalyticsClaudeTagCategoryMonitoring BetaAnalyticsClaudeTagCategory = "monitoring"`

    - `const BetaAnalyticsClaudeTagCategoryProactive BetaAnalyticsClaudeTagCategory = "proactive"`

    - `const BetaAnalyticsClaudeTagCategoryScheduled BetaAnalyticsClaudeTagCategory = "scheduled"`

  - `ClaudeTagUserID string`

    Slack user ID (for example `U0123ABCDEF`) of the member the Claude Tag (Claude in Slack) usage is attributed to, not a claude.ai user ID. Populated only when `claude_tag_user_id` is in `group_by[]`; null for usage that is not Claude Tag and for Claude Tag usage that is not attributed to a single user (for example `monitoring`, and `proactive` usage Claude initiated), so per-user rows can sum to less than the Claude Tag total. Cannot be combined with `group_by[]=rbac_group_id` or the `rbac_group_ids[]` filter.

  - `ContextWindow BetaAnalyticsContextWindow`

    Context-window pricing tier of the usage or cost. Null unless `context_window` is in `group_by[]`; it can also be null on grouped rows with no context-window tier, such as code execution.

    - `const BetaAnalyticsContextWindowFrom0To200k BetaAnalyticsContextWindow = "0-200k"`

    - `const BetaAnalyticsContextWindowFrom200kTo1M BetaAnalyticsContextWindow = "200k-1M"`

  - `CostType BetaAnalyticsCostType`

    Cost component breakdown; null when returning the combined total.

    - `const BetaAnalyticsCostTypeCodeExecution BetaAnalyticsCostType = "code_execution"`

    - `const BetaAnalyticsCostTypeTokens BetaAnalyticsCostType = "tokens"`

    - `const BetaAnalyticsCostTypeWebSearch BetaAnalyticsCostType = "web_search"`

  - `Currency string`

    Currency code for the cost amount. Currently always `"USD"`.

    default: USD

  - `EndingAt Time`

    End of the row's UTC time bucket (exclusive), as an RFC 3339 timestamp; equal to `starting_at` plus one `bucket_width`. Null unless `bucket_width` is set.

    format: date-time

  - `InferenceGeo BetaAnalyticsCostUsersItemInferenceGeo`

    Inference region of the usage or cost. Null unless `inference_geo` is in `group_by[]`; it can also be null on grouped rows where the region is not set (the rows that `inference_geos[]=not_available` matches).

    - `const BetaAnalyticsCostUsersItemInferenceGeoGlobal BetaAnalyticsCostUsersItemInferenceGeo = "global"`

    - `const BetaAnalyticsCostUsersItemInferenceGeoUs BetaAnalyticsCostUsersItemInferenceGeo = "us"`

  - `ListAmount string`

    List-price amount (pre-discount) in fractional cents.

  - `Model string`

    Model that produced the usage or cost, as a model name in the form the `models[]` filter accepts (for example, `claude-opus-5`). Null unless `model` is in `group_by[]`; it can also be null on grouped rows whose usage or cost is not attributed to a specific model, such as code execution.

  - `Product string`

    Product surface that produced the usage or cost. Null unless product is in `group_by[]`; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include `chat`, `claude_code`, `cowork`, `office_agent`, `claude_in_chrome`, `claude_design`, and `claude-tag`. `claude-tag` is Claude Tag, the Claude product in Slack. Some unattributed usage is reported as "other".

  - `RBACGroupID string`

    RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has one id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query without `group_by[]`.

  - `Requests int64`

    Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).

  - `SlackChannelID string`

    Slack channel the usage originated from. Populated only when `slack_channel_id` is in `group_by[]`; null for usage outside Slack (and for rows recorded before channel attribution was enabled).

  - `Speed BetaAnalyticsCostUsersItemSpeed`

    Inference speed mode of the usage or cost: `fast` or `standard`. Null unless `speed` is in `group_by[]`.

    - `const BetaAnalyticsCostUsersItemSpeedFast BetaAnalyticsCostUsersItemSpeed = "fast"`

    - `const BetaAnalyticsCostUsersItemSpeedStandard BetaAnalyticsCostUsersItemSpeed = "standard"`

  - `StartingAt Time`

    Start of the row's UTC time bucket (inclusive), as an RFC 3339 timestamp. Null unless `bucket_width` is set; without `bucket_width`, each row aggregates the full requested range.

    format: date-time

  - `TokenType BetaAnalyticsTokenType`

    Token type when `cost_type` is `tokens`; null otherwise.

    - `const BetaAnalyticsTokenTypeCacheCreationEphemeral1hInputTokens BetaAnalyticsTokenType = "cache_creation.ephemeral_1h_input_tokens"`

    - `const BetaAnalyticsTokenTypeCacheCreationEphemeral5mInputTokens BetaAnalyticsTokenType = "cache_creation.ephemeral_5m_input_tokens"`

    - `const BetaAnalyticsTokenTypeCacheReadInputTokens BetaAnalyticsTokenType = "cache_read_input_tokens"`

    - `const BetaAnalyticsTokenTypeOutputTokens BetaAnalyticsTokenType = "output_tokens"`

    - `const BetaAnalyticsTokenTypeUncachedInputTokens BetaAnalyticsTokenType = "uncached_input_tokens"`

#### Example

```go
package main

import (
	"context"
	"fmt"
	"time"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Analytics.UserCostReport.List(context.TODO(), anthropic.BetaOrganizationAnalyticsUserCostReportListParams{
		StartingAt: time.Now(),
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "actor": {
        "deleted": true,
        "email": "jane@example.com",
        "email_address": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor",
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt"
      },
      "amount": "41280.000000",
      "claude_tag_category": "dm",
      "claude_tag_user_id": "U0123ABCDEF",
      "context_window": "0-200k",
      "cost_type": "code_execution",
      "currency": "USD",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "list_amount": "51600.000000",
      "model": "claude-opus-5",
      "product": "chat",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "slack_channel_id": "C0123ABCDEF",
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "token_type": "cache_creation.ephemeral_1h_input_tokens"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

## Beta › Organization › Spend Limits

### Set Spend Limit

`client.Beta.Organization.SpendLimits.Set(ctx, body) (*BetaSpendLimit, error)`

**POST** `/v1/organizations/spend_limits`

Set a spend limit.

Upsert keyed on (scope, period): setting a limit that already exists
overwrites it in place. A Claude Enterprise organization sets `user`
limits. Its seat-tier, group, and organization-level defaults are configured
in claude.ai. A Claude Console organization sets `organization` and
`workspace` limits, which are monthly and always carry an amount. Setting those
limits is in an early access preview. To request access, contact your
Anthropic account team.

#### Parameters

- `body BetaOrganizationSpendLimitSetParams`

  - `Amount param.Field[string]`

    Limit amount as a non-negative integer decimal string in the minor unit of the organization's billing currency (cents for USD): "50000" is $500.00. `null` sets an explicit no-limit override for this scope and `period` only — each period resolves independently, so caps for other periods still apply.

  - `Scope param.Field[BetaOrganizationSpendLimitSetParamsScopeUnion]`

    What the limit applies to. Claude Enterprise organizations set `user` limits. Claude Console organizations set `organization` and `workspace` limits. Any other combination returns 400. Setting `organization` and `workspace` limits through the API is in an early access preview. To request access, contact your Anthropic account team.

    - `type BetaSpendLimitUserScope`

      Scope selecting a single member of the organization.

      - `Type User`

        Scope type. Always `user` for this scope.

        default: user

      - `UserID string`

        Tagged ID of the member the spend limit applies to.

    - `type BetaSpendLimitOrganizationScope`

      - `Type Organization`

        default: organization

    - `type BetaSpendLimitWorkspaceScope`

      Scope selecting one workspace of a Claude Console organization.

      - `Type Workspace`

        Scope type. Always `workspace` for this scope.

        default: workspace

      - `WorkspaceID string`

        Tagged ID of the workspace the spend limit applies to.

  - `Period param.Field[BetaSpendLimitPeriod] Optional`

#### Returns

- `type BetaSpendLimit`

  A configured spend limit: a cap on metered spend for one scope and period.

  - `Type SpendLimit`

    Object type. Always `spend_limit`.

    default: spend_limit

  - `ID string`

    Unique tagged ID of the spend limit (`spl_...`).

  - `Amount string`

    Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

  - `CreatedAt Time`

    RFC 3339 datetime at which the spend limit was created.

    format: date-time

  - `Currency string`

    ISO 4217 code of the organization's billing currency; the unit for `amount`.

  - `IsEnabled bool`

    Read-only. `false` when extra usage is switched off for this organization (`organization` limit) or for this member (`user` limit); `amount` is kept and applies again when it's switched back on. Always `true` for other limits.

  - `Period BetaSpendLimitPeriod`

    Length of the window the limit resets over. `amount` caps spend within each period.

    - `const BetaSpendLimitPeriodDaily BetaSpendLimitPeriod = "daily"`

    - `const BetaSpendLimitPeriodMonthly BetaSpendLimitPeriod = "monthly"`

    - `const BetaSpendLimitPeriodWeekly BetaSpendLimitPeriod = "weekly"`

  - `Scope BetaSpendLimitScopeUnion`

    What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

    - `type BetaSpendLimitUserScope`

      Scope selecting a single member of the organization.

      - `Type User`

        Scope type. Always `user` for this scope.

        default: user

      - `UserID string`

        Tagged ID of the member the spend limit applies to.

    - `type BetaSpendLimitSeatTierScope`

      - `Type SeatTier`

        default: seat_tier

      - `SeatTier string`

    - `type BetaSpendLimitRBACGroupScope`

      - `Type RBACGroup`

        default: rbac_group

      - `RBACGroupID string`

    - `type BetaSpendLimitOrganizationServiceScope`

      - `Type OrganizationService`

        default: organization_service

      - `Service string`

    - `type BetaSpendLimitOrganizationScope`

      - `Type Organization`

        default: organization

    - `type BetaSpendLimitWorkspaceScope`

      Scope selecting one workspace of a Claude Console organization.

      - `Type Workspace`

        Scope type. Always `workspace` for this scope.

        default: workspace

      - `WorkspaceID string`

        Tagged ID of the workspace the spend limit applies to.

  - `UpdatedAt Time`

    RFC 3339 datetime at which the spend limit was last modified.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaSpendLimit, err := client.Beta.Organization.SpendLimits.Set(context.TODO(), anthropic.BetaOrganizationSpendLimitSetParams{
		Amount: anthropic.String("50000"),
		Scope: anthropic.BetaOrganizationSpendLimitSetParamsScopeUnion{
			OfUser: &anthropic.BetaSpendLimitUserScopeParam{
				UserID: "user_01WCz1FkmYMm4gnmykNKUu3Q",
			},
		},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaSpendLimit.ID)
}
```

##### Response (200)

```json
{
  "id": "id",
  "amount": "50000",
  "created_at": "2019-12-27T18:11:19.117Z",
  "currency": "USD",
  "is_enabled": true,
  "period": "daily",
  "scope": {
    "type": "user",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "type": "spend_limit",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

### Get Spend Limit

`client.Beta.Organization.SpendLimits.Get(ctx, spendLimitID) (*BetaSpendLimit, error)`

**GET** `/v1/organizations/spend_limits/{spend_limit_id}`

Retrieve a spend limit by ID.

#### Parameters

- `spendLimitID string`

  ID of the Spend Limit.

#### Returns

- `type BetaSpendLimit`

  A configured spend limit: a cap on metered spend for one scope and period.

  - `Type SpendLimit`

    Object type. Always `spend_limit`.

    default: spend_limit

  - `ID string`

    Unique tagged ID of the spend limit (`spl_...`).

  - `Amount string`

    Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

  - `CreatedAt Time`

    RFC 3339 datetime at which the spend limit was created.

    format: date-time

  - `Currency string`

    ISO 4217 code of the organization's billing currency; the unit for `amount`.

  - `IsEnabled bool`

    Read-only. `false` when extra usage is switched off for this organization (`organization` limit) or for this member (`user` limit); `amount` is kept and applies again when it's switched back on. Always `true` for other limits.

  - `Period BetaSpendLimitPeriod`

    Length of the window the limit resets over. `amount` caps spend within each period.

    - `const BetaSpendLimitPeriodDaily BetaSpendLimitPeriod = "daily"`

    - `const BetaSpendLimitPeriodMonthly BetaSpendLimitPeriod = "monthly"`

    - `const BetaSpendLimitPeriodWeekly BetaSpendLimitPeriod = "weekly"`

  - `Scope BetaSpendLimitScopeUnion`

    What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

    - `type BetaSpendLimitUserScope`

      Scope selecting a single member of the organization.

      - `Type User`

        Scope type. Always `user` for this scope.

        default: user

      - `UserID string`

        Tagged ID of the member the spend limit applies to.

    - `type BetaSpendLimitSeatTierScope`

      - `Type SeatTier`

        default: seat_tier

      - `SeatTier string`

    - `type BetaSpendLimitRBACGroupScope`

      - `Type RBACGroup`

        default: rbac_group

      - `RBACGroupID string`

    - `type BetaSpendLimitOrganizationServiceScope`

      - `Type OrganizationService`

        default: organization_service

      - `Service string`

    - `type BetaSpendLimitOrganizationScope`

      - `Type Organization`

        default: organization

    - `type BetaSpendLimitWorkspaceScope`

      Scope selecting one workspace of a Claude Console organization.

      - `Type Workspace`

        Scope type. Always `workspace` for this scope.

        default: workspace

      - `WorkspaceID string`

        Tagged ID of the workspace the spend limit applies to.

  - `UpdatedAt Time`

    RFC 3339 datetime at which the spend limit was last modified.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaSpendLimit, err := client.Beta.Organization.SpendLimits.Get(context.TODO(), "spend_limit_id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaSpendLimit.ID)
}
```

##### Response (200)

```json
{
  "id": "id",
  "amount": "50000",
  "created_at": "2019-12-27T18:11:19.117Z",
  "currency": "USD",
  "is_enabled": true,
  "period": "daily",
  "scope": {
    "type": "user",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "type": "spend_limit",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

### Delete Spend Limit

`client.Beta.Organization.SpendLimits.Delete(ctx, spendLimitID) (*BetaOrganizationSpendLimitDeleteResponse, error)`

**DELETE** `/v1/organizations/spend_limits/{spend_limit_id}`

Delete a spend limit.

For a Claude Enterprise organization, this deletes a per-user override, and
the member falls back to any inherited spend limit at that period. Its
seat-tier, group, and organization-level rows cannot be deleted via this
endpoint. A Claude Console organization deletes its organization and
workspace limits. Deleting them through the API is in an early access preview.

#### Parameters

- `spendLimitID string`

  ID of the Spend Limit.

#### Returns

- `type BetaOrganizationSpendLimitDeleteResponse`

  - `Type SpendLimitDeleted`

    default: spend_limit_deleted

  - `ID string`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	spendLimit, err := client.Beta.Organization.SpendLimits.Delete(context.TODO(), "spend_limit_id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", spendLimit.ID)
}
```

##### Response (200)

```json
{
  "id": "id",
  "type": "spend_limit_deleted"
}
```

### List Spend Limits

`client.Beta.Organization.SpendLimits.List(ctx, params) (*PageCursor[BetaSpendLimit], error)`

**GET** `/v1/organizations/spend_limits`

List the organization's spend limits.

A Claude Console organization's limits come in an order that is stable across
pages. A Claude Enterprise organization's are grouped by scope type,
in the order `organization`, `seat_tier`, `rbac_group`,
`organization_service`, `user`; within a type they come in a fixed order that
is not creation order.

#### Parameters

- `params BetaOrganizationSpendLimitListParams`

  - `Limit param.Field[int64] Optional`

    Query param: Maximum number of limits per page. Defaults to `20`.

    minimum: 1, maximum: 1000

  - `Page param.Field[string] Optional`

    Query param: Opaque cursor from a previous response's `next_page` field.

  - `ScopeType param.Field[[]string] Optional`

    Query param: Return only limits with these scope types. A Claude Console organization has `organization` and `workspace` limits; a Claude Enterprise organization has `organization`, `seat_tier`, `rbac_group`, `organization_service` and `user` limits. Omit for all.

    maxItems: 6

    - `const BetaOrganizationSpendLimitListParamsScopeTypeOrganization BetaOrganizationSpendLimitListParamsScopeType = "organization"`

    - `const BetaOrganizationSpendLimitListParamsScopeTypeOrganizationService BetaOrganizationSpendLimitListParamsScopeType = "organization_service"`

    - `const BetaOrganizationSpendLimitListParamsScopeTypeRBACGroup BetaOrganizationSpendLimitListParamsScopeType = "rbac_group"`

    - `const BetaOrganizationSpendLimitListParamsScopeTypeSeatTier BetaOrganizationSpendLimitListParamsScopeType = "seat_tier"`

    - `const BetaOrganizationSpendLimitListParamsScopeTypeUser BetaOrganizationSpendLimitListParamsScopeType = "user"`

    - `const BetaOrganizationSpendLimitListParamsScopeTypeWorkspace BetaOrganizationSpendLimitListParamsScopeType = "workspace"`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `spend-limit-reads-2026-09-26` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaSpendLimit`

  A configured spend limit: a cap on metered spend for one scope and period.

  - `Type SpendLimit`

    Object type. Always `spend_limit`.

    default: spend_limit

  - `ID string`

    Unique tagged ID of the spend limit (`spl_...`).

  - `Amount string`

    Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

  - `CreatedAt Time`

    RFC 3339 datetime at which the spend limit was created.

    format: date-time

  - `Currency string`

    ISO 4217 code of the organization's billing currency; the unit for `amount`.

  - `IsEnabled bool`

    Read-only. `false` when extra usage is switched off for this organization (`organization` limit) or for this member (`user` limit); `amount` is kept and applies again when it's switched back on. Always `true` for other limits.

  - `Period BetaSpendLimitPeriod`

    Length of the window the limit resets over. `amount` caps spend within each period.

    - `const BetaSpendLimitPeriodDaily BetaSpendLimitPeriod = "daily"`

    - `const BetaSpendLimitPeriodMonthly BetaSpendLimitPeriod = "monthly"`

    - `const BetaSpendLimitPeriodWeekly BetaSpendLimitPeriod = "weekly"`

  - `Scope BetaSpendLimitScopeUnion`

    What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

    - `type BetaSpendLimitUserScope`

      Scope selecting a single member of the organization.

      - `Type User`

        Scope type. Always `user` for this scope.

        default: user

      - `UserID string`

        Tagged ID of the member the spend limit applies to.

    - `type BetaSpendLimitSeatTierScope`

      - `Type SeatTier`

        default: seat_tier

      - `SeatTier string`

    - `type BetaSpendLimitRBACGroupScope`

      - `Type RBACGroup`

        default: rbac_group

      - `RBACGroupID string`

    - `type BetaSpendLimitOrganizationServiceScope`

      - `Type OrganizationService`

        default: organization_service

      - `Service string`

    - `type BetaSpendLimitOrganizationScope`

      - `Type Organization`

        default: organization

    - `type BetaSpendLimitWorkspaceScope`

      Scope selecting one workspace of a Claude Console organization.

      - `Type Workspace`

        Scope type. Always `workspace` for this scope.

        default: workspace

      - `WorkspaceID string`

        Tagged ID of the workspace the spend limit applies to.

  - `UpdatedAt Time`

    RFC 3339 datetime at which the spend limit was last modified.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.SpendLimits.List(context.TODO(), anthropic.BetaOrganizationSpendLimitListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "amount": "50000",
      "created_at": "2019-12-27T18:11:19.117Z",
      "currency": "USD",
      "is_enabled": true,
      "period": "daily",
      "scope": {
        "type": "user",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "type": "spend_limit",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Spend Limits › Effective

### List Effective Spend Limits

`client.Beta.Organization.SpendLimits.Effective.List(ctx, query) (*PageCursor[BetaSpendSummary], error)`

**GET** `/v1/organizations/spend_limits/effective`

List each member's effective spend limit and period-to-date spend.

Returns one row per (member, period) the member resolves a spend limit
for, with the `source` scope the spend limit was inherited from.
Paginates by member, so a member's periods never split across pages.

#### Parameters

- `query BetaOrganizationSpendLimitEffectiveListParams`

  - `Limit param.Field[int64] Optional`

    Maximum number of members per page. A member's period rows never split across pages, so a page may carry more rows than this. Defaults to `20`.

    minimum: 1, maximum: 1000

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page` field.

  - `Period param.Field[[]string] Optional`

    Restrict the report to these limit periods. Omit to return one row per period each member resolves a spend limit for.

    maxItems: 3

    - `const BetaOrganizationSpendLimitEffectiveListParamsPeriodDaily BetaOrganizationSpendLimitEffectiveListParamsPeriod = "daily"`

    - `const BetaOrganizationSpendLimitEffectiveListParamsPeriodMonthly BetaOrganizationSpendLimitEffectiveListParamsPeriod = "monthly"`

    - `const BetaOrganizationSpendLimitEffectiveListParamsPeriodWeekly BetaOrganizationSpendLimitEffectiveListParamsPeriod = "weekly"`

  - `UserIDs param.Field[[]string] Optional`

    Restrict the report to these members, by tagged user ID (`user_...`). At most 100 entries.

    maxItems: 100

#### Returns

- `type BetaSpendSummary`

  Per-member effective-limit report row (`GET /spend_limits/effective`).

  - `Actor BetaSpendSummaryActorUnion`

    - `type BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `Type UserActor`

        Actor type. Always `user_actor`.

        default: user_actor

      - `Deleted bool`

        True only when the underlying account has been deleted.

        default: false

      - `EmailAddress string`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `Name string`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `UserID string`

        Tagged ID of the user.

    - `type BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

      - `Type ScopedAPIKeyActor`

        default: scoped_api_key_actor

      - `ScopedAPIKeyID string`

  - `Amount string`

    Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

  - `Currency string`

    ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

  - `Period BetaSpendLimitPeriod`

    Period this row's effective limit and spend are reported for.

    - `const BetaSpendLimitPeriodDaily BetaSpendLimitPeriod = "daily"`

    - `const BetaSpendLimitPeriodMonthly BetaSpendLimitPeriod = "monthly"`

    - `const BetaSpendLimitPeriodWeekly BetaSpendLimitPeriod = "weekly"`

  - `PeriodToDateSpend string`

    The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

  - `Scope BetaSpendSummaryScopeUnion`

    - `type BetaSpendLimitUserScope`

      Scope selecting a single member of the organization.

      - `Type User`

        Scope type. Always `user` for this scope.

        default: user

      - `UserID string`

        Tagged ID of the member the spend limit applies to.

    - `type BetaSpendLimitSeatTierScope`

      - `Type SeatTier`

        default: seat_tier

      - `SeatTier string`

    - `type BetaSpendLimitRBACGroupScope`

      - `Type RBACGroup`

        default: rbac_group

      - `RBACGroupID string`

    - `type BetaSpendLimitOrganizationServiceScope`

      - `Type OrganizationService`

        default: organization_service

      - `Service string`

    - `type BetaSpendLimitOrganizationScope`

      - `Type Organization`

        default: organization

    - `type BetaSpendLimitWorkspaceScope`

      Scope selecting one workspace of a Claude Console organization.

      - `Type Workspace`

        Scope type. Always `workspace` for this scope.

        default: workspace

      - `WorkspaceID string`

        Tagged ID of the workspace the spend limit applies to.

  - `Source BetaSpendSummarySourceUnion`

    - `type BetaSpendLimitUserScope`

      Scope selecting a single member of the organization.

    - `type BetaSpendLimitSeatTierScope`

    - `type BetaSpendLimitRBACGroupScope`

    - `type BetaSpendLimitOrganizationServiceScope`

    - `type BetaSpendLimitOrganizationScope`

    - `type BetaSpendLimitWorkspaceScope`

      Scope selecting one workspace of a Claude Console organization.

  - `SpendLimitID string`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.SpendLimits.Effective.List(context.TODO(), anthropic.BetaOrganizationSpendLimitEffectiveListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "amount": "50000",
      "currency": "USD",
      "period": "daily",
      "period_to_date_spend": "12050.5",
      "scope": {
        "type": "user",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "source": {
        "type": "user",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "spend_limit_id": "spend_limit_id"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Spend Limits › Increase Requests

### List Spend Limit Increase Requests

`client.Beta.Organization.SpendLimits.IncreaseRequests.List(ctx, query) (*PageCursor[BetaSpendLimitIncreaseRequest], error)`

**GET** `/v1/organizations/spend_limit_increase_requests`

List spend limit increase requests, most recent first.

Pending requests include a live `spend_summary` for the requester.
Requests whose requester is no longer a member are excluded.

#### Parameters

- `query BetaOrganizationSpendLimitIncreaseRequestListParams`

  - `ActorIDs param.Field[[]string] Optional`

    Filter by requester, as `user_...` tagged IDs.

  - `Limit param.Field[int64] Optional`

    minimum: 1, maximum: 1000

  - `Page param.Field[string] Optional`

    Opaque cursor from a previous response's `next_page`.

  - `Status param.Field[[]BetaSpendLimitIncreaseRequestStatus] Optional`

    Filter by status. Omit to return all.

    - `const BetaSpendLimitIncreaseRequestStatusApproved BetaSpendLimitIncreaseRequestStatus = "approved"`

    - `const BetaSpendLimitIncreaseRequestStatusDenied BetaSpendLimitIncreaseRequestStatus = "denied"`

    - `const BetaSpendLimitIncreaseRequestStatusPending BetaSpendLimitIncreaseRequestStatus = "pending"`

#### Returns

- `type BetaSpendLimitIncreaseRequest`

  - `Type SpendLimitIncreaseRequest`

    default: spend_limit_increase_request

  - `ID string`

  - `Actor BetaSpendLimitIncreaseRequestActorUnion`

    - `type BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `Type UserActor`

        Actor type. Always `user_actor`.

        default: user_actor

      - `Deleted bool`

        True only when the underlying account has been deleted.

        default: false

      - `EmailAddress string`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `Name string`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `UserID string`

        Tagged ID of the user.

    - `type BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

      - `Type ScopedAPIKeyActor`

        default: scoped_api_key_actor

      - `ScopedAPIKeyID string`

  - `CreatedAt Time`

    format: date-time

  - `Period BetaSpendLimitPeriod`

    - `const BetaSpendLimitPeriodDaily BetaSpendLimitPeriod = "daily"`

    - `const BetaSpendLimitPeriodMonthly BetaSpendLimitPeriod = "monthly"`

    - `const BetaSpendLimitPeriodWeekly BetaSpendLimitPeriod = "weekly"`

  - `ResolvedAt Time`

    format: date-time

  - `ResolvedBy BetaSpendLimitIncreaseRequestResolvedByUnion`

    - `type BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `type BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

  - `SpendSummary BetaSpendSummary`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `Actor BetaSpendSummaryActorUnion`

      - `type BetaSpendLimitUserActor`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `type BetaSpendLimitScopedAPIKeyActor`

        A scoped Admin API key acting on behalf of the organization.

    - `Amount string`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `Currency string`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `Period BetaSpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `PeriodToDateSpend string`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `Scope BetaSpendSummaryScopeUnion`

      - `type BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

        - `Type User`

          Scope type. Always `user` for this scope.

          default: user

        - `UserID string`

          Tagged ID of the member the spend limit applies to.

      - `type BetaSpendLimitSeatTierScope`

        - `Type SeatTier`

          default: seat_tier

        - `SeatTier string`

      - `type BetaSpendLimitRBACGroupScope`

        - `Type RBACGroup`

          default: rbac_group

        - `RBACGroupID string`

      - `type BetaSpendLimitOrganizationServiceScope`

        - `Type OrganizationService`

          default: organization_service

        - `Service string`

      - `type BetaSpendLimitOrganizationScope`

        - `Type Organization`

          default: organization

      - `type BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

        - `Type Workspace`

          Scope type. Always `workspace` for this scope.

          default: workspace

        - `WorkspaceID string`

          Tagged ID of the workspace the spend limit applies to.

    - `Source BetaSpendSummarySourceUnion`

      - `type BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

      - `type BetaSpendLimitSeatTierScope`

      - `type BetaSpendLimitRBACGroupScope`

      - `type BetaSpendLimitOrganizationServiceScope`

      - `type BetaSpendLimitOrganizationScope`

      - `type BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

    - `SpendLimitID string`

  - `Status BetaSpendLimitIncreaseRequestStatus`

    - `const BetaSpendLimitIncreaseRequestStatusApproved BetaSpendLimitIncreaseRequestStatus = "approved"`

    - `const BetaSpendLimitIncreaseRequestStatusDenied BetaSpendLimitIncreaseRequestStatus = "denied"`

    - `const BetaSpendLimitIncreaseRequestStatusPending BetaSpendLimitIncreaseRequestStatus = "pending"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.SpendLimits.IncreaseRequests.List(context.TODO(), anthropic.BetaOrganizationSpendLimitIncreaseRequestListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "actor": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "created_at": "2019-12-27T18:11:19.117Z",
      "period": "daily",
      "resolved_at": "2019-12-27T18:11:19.117Z",
      "resolved_by": {
        "deleted": true,
        "email_address": "email_address",
        "name": "name",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "spend_summary": {
        "actor": {
          "deleted": true,
          "email_address": "email_address",
          "name": "name",
          "type": "user_actor",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "amount": "50000",
        "currency": "USD",
        "period": "daily",
        "period_to_date_spend": "12050.5",
        "scope": {
          "type": "user",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "source": {
          "type": "user",
          "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
        },
        "spend_limit_id": "spend_limit_id"
      },
      "status": "approved",
      "type": "spend_limit_increase_request"
    }
  ],
  "next_page": "next_page"
}
```

### Get Spend Limit Increase Request

`client.Beta.Organization.SpendLimits.IncreaseRequests.Get(ctx, spendLimitIncreaseRequestID) (*BetaSpendLimitIncreaseRequest, error)`

**GET** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}`

Retrieve a spend limit increase request.

While `pending`, the response includes a live `spend_summary` for the
requester at the request's period.

#### Parameters

- `spendLimitIncreaseRequestID string`

  ID of the spend limit increase request.

#### Returns

- `type BetaSpendLimitIncreaseRequest`

  - `Type SpendLimitIncreaseRequest`

    default: spend_limit_increase_request

  - `ID string`

  - `Actor BetaSpendLimitIncreaseRequestActorUnion`

    - `type BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `Type UserActor`

        Actor type. Always `user_actor`.

        default: user_actor

      - `Deleted bool`

        True only when the underlying account has been deleted.

        default: false

      - `EmailAddress string`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `Name string`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `UserID string`

        Tagged ID of the user.

    - `type BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

      - `Type ScopedAPIKeyActor`

        default: scoped_api_key_actor

      - `ScopedAPIKeyID string`

  - `CreatedAt Time`

    format: date-time

  - `Period BetaSpendLimitPeriod`

    - `const BetaSpendLimitPeriodDaily BetaSpendLimitPeriod = "daily"`

    - `const BetaSpendLimitPeriodMonthly BetaSpendLimitPeriod = "monthly"`

    - `const BetaSpendLimitPeriodWeekly BetaSpendLimitPeriod = "weekly"`

  - `ResolvedAt Time`

    format: date-time

  - `ResolvedBy BetaSpendLimitIncreaseRequestResolvedByUnion`

    - `type BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `type BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

  - `SpendSummary BetaSpendSummary`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `Actor BetaSpendSummaryActorUnion`

      - `type BetaSpendLimitUserActor`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `type BetaSpendLimitScopedAPIKeyActor`

        A scoped Admin API key acting on behalf of the organization.

    - `Amount string`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `Currency string`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `Period BetaSpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `PeriodToDateSpend string`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `Scope BetaSpendSummaryScopeUnion`

      - `type BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

        - `Type User`

          Scope type. Always `user` for this scope.

          default: user

        - `UserID string`

          Tagged ID of the member the spend limit applies to.

      - `type BetaSpendLimitSeatTierScope`

        - `Type SeatTier`

          default: seat_tier

        - `SeatTier string`

      - `type BetaSpendLimitRBACGroupScope`

        - `Type RBACGroup`

          default: rbac_group

        - `RBACGroupID string`

      - `type BetaSpendLimitOrganizationServiceScope`

        - `Type OrganizationService`

          default: organization_service

        - `Service string`

      - `type BetaSpendLimitOrganizationScope`

        - `Type Organization`

          default: organization

      - `type BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

        - `Type Workspace`

          Scope type. Always `workspace` for this scope.

          default: workspace

        - `WorkspaceID string`

          Tagged ID of the workspace the spend limit applies to.

    - `Source BetaSpendSummarySourceUnion`

      - `type BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

      - `type BetaSpendLimitSeatTierScope`

      - `type BetaSpendLimitRBACGroupScope`

      - `type BetaSpendLimitOrganizationServiceScope`

      - `type BetaSpendLimitOrganizationScope`

      - `type BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

    - `SpendLimitID string`

  - `Status BetaSpendLimitIncreaseRequestStatus`

    - `const BetaSpendLimitIncreaseRequestStatusApproved BetaSpendLimitIncreaseRequestStatus = "approved"`

    - `const BetaSpendLimitIncreaseRequestStatusDenied BetaSpendLimitIncreaseRequestStatus = "denied"`

    - `const BetaSpendLimitIncreaseRequestStatusPending BetaSpendLimitIncreaseRequestStatus = "pending"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaSpendLimitIncreaseRequest, err := client.Beta.Organization.SpendLimits.IncreaseRequests.Get(context.TODO(), "spend_limit_increase_request_id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaSpendLimitIncreaseRequest.ID)
}
```

##### Response (200)

```json
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "daily",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

### Approve Spend Limit Increase Request

`client.Beta.Organization.SpendLimits.IncreaseRequests.Approve(ctx, spendLimitIncreaseRequestID, body) (*BetaOrganizationSpendLimitIncreaseRequestApproveResponse, error)`

**POST** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/approve`

Approve a pending spend limit increase request.

Writes a per-user spend limit at `amount` for the requester and
transitions the request to `approved`. `period` defaults to the period
the member was blocked on. Anthropic emails the requester unless
`suppress_notification` is set.

#### Parameters

- `spendLimitIncreaseRequestID string`

  ID of the spend limit increase request.

- `body BetaOrganizationSpendLimitIncreaseRequestApproveParams`

  - `Amount param.Field[string]`

    New per-user spend limit as a non-negative integer decimal string (minor units).

  - `Period param.Field[BetaSpendLimitPeriod] Optional`

  - `SuppressNotification param.Field[bool] Optional`

#### Returns

- `type BetaOrganizationSpendLimitIncreaseRequestApproveResponse`

  - `Type SpendLimitIncreaseRequest`

    default: spend_limit_increase_request

  - `ID string`

  - `Actor BetaOrganizationSpendLimitIncreaseRequestApproveResponseActorUnion`

    - `type BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `Type UserActor`

        Actor type. Always `user_actor`.

        default: user_actor

      - `Deleted bool`

        True only when the underlying account has been deleted.

        default: false

      - `EmailAddress string`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `Name string`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `UserID string`

        Tagged ID of the user.

    - `type BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

      - `Type ScopedAPIKeyActor`

        default: scoped_api_key_actor

      - `ScopedAPIKeyID string`

  - `CreatedAt Time`

    format: date-time

  - `Period BetaSpendLimitPeriod`

    - `const BetaSpendLimitPeriodDaily BetaSpendLimitPeriod = "daily"`

    - `const BetaSpendLimitPeriodMonthly BetaSpendLimitPeriod = "monthly"`

    - `const BetaSpendLimitPeriodWeekly BetaSpendLimitPeriod = "weekly"`

  - `ResolvedAt Time`

    format: date-time

  - `ResolvedBy BetaOrganizationSpendLimitIncreaseRequestApproveResponseResolvedByUnion`

    - `type BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `type BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

  - `SpendLimit BetaSpendLimit`

    A configured spend limit: a cap on metered spend for one scope and period.

    - `Type SpendLimit`

      Object type. Always `spend_limit`.

      default: spend_limit

    - `ID string`

      Unique tagged ID of the spend limit (`spl_...`).

    - `Amount string`

      Limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD): "50000" is $500.00. `null` means no numeric cap is configured at this scope — see the effective report for whether a limit applies.

    - `CreatedAt Time`

      RFC 3339 datetime at which the spend limit was created.

      format: date-time

    - `Currency string`

      ISO 4217 code of the organization's billing currency; the unit for `amount`.

    - `IsEnabled bool`

      Read-only. `false` when extra usage is switched off for this organization (`organization` limit) or for this member (`user` limit); `amount` is kept and applies again when it's switched back on. Always `true` for other limits.

    - `Period BetaSpendLimitPeriod`

      Length of the window the limit resets over. `amount` caps spend within each period.

    - `Scope BetaSpendLimitScopeUnion`

      What the limit applies to. A tagged union on `type`; each variant carries the identifier for its scope.

      - `type BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

        - `Type User`

          Scope type. Always `user` for this scope.

          default: user

        - `UserID string`

          Tagged ID of the member the spend limit applies to.

      - `type BetaSpendLimitSeatTierScope`

        - `Type SeatTier`

          default: seat_tier

        - `SeatTier string`

      - `type BetaSpendLimitRBACGroupScope`

        - `Type RBACGroup`

          default: rbac_group

        - `RBACGroupID string`

      - `type BetaSpendLimitOrganizationServiceScope`

        - `Type OrganizationService`

          default: organization_service

        - `Service string`

      - `type BetaSpendLimitOrganizationScope`

        - `Type Organization`

          default: organization

      - `type BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

        - `Type Workspace`

          Scope type. Always `workspace` for this scope.

          default: workspace

        - `WorkspaceID string`

          Tagged ID of the workspace the spend limit applies to.

    - `UpdatedAt Time`

      RFC 3339 datetime at which the spend limit was last modified.

      format: date-time

  - `SpendSummary BetaSpendSummary`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `Actor BetaSpendSummaryActorUnion`

      - `type BetaSpendLimitUserActor`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `type BetaSpendLimitScopedAPIKeyActor`

        A scoped Admin API key acting on behalf of the organization.

    - `Amount string`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `Currency string`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `Period BetaSpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `PeriodToDateSpend string`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `Scope BetaSpendSummaryScopeUnion`

      - `type BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

      - `type BetaSpendLimitSeatTierScope`

      - `type BetaSpendLimitRBACGroupScope`

      - `type BetaSpendLimitOrganizationServiceScope`

      - `type BetaSpendLimitOrganizationScope`

      - `type BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

    - `Source BetaSpendSummarySourceUnion`

      - `type BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

      - `type BetaSpendLimitSeatTierScope`

      - `type BetaSpendLimitRBACGroupScope`

      - `type BetaSpendLimitOrganizationServiceScope`

      - `type BetaSpendLimitOrganizationScope`

      - `type BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

    - `SpendLimitID string`

  - `Status BetaSpendLimitIncreaseRequestStatus`

    - `const BetaSpendLimitIncreaseRequestStatusApproved BetaSpendLimitIncreaseRequestStatus = "approved"`

    - `const BetaSpendLimitIncreaseRequestStatusDenied BetaSpendLimitIncreaseRequestStatus = "denied"`

    - `const BetaSpendLimitIncreaseRequestStatusPending BetaSpendLimitIncreaseRequestStatus = "pending"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	response, err := client.Beta.Organization.SpendLimits.IncreaseRequests.Approve(
		context.TODO(),
		"spend_limit_increase_request_id",
		anthropic.BetaOrganizationSpendLimitIncreaseRequestApproveParams{
			Amount: "50000",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response.ID)
}
```

##### Response (200)

```json
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "spend_limit": {
    "id": "id",
    "amount": "50000",
    "created_at": "2019-12-27T18:11:19.117Z",
    "currency": "USD",
    "is_enabled": true,
    "period": "daily",
    "scope": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "type": "spend_limit",
    "updated_at": "2019-12-27T18:11:19.117Z"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "daily",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

### Deny Spend Limit Increase Request

`client.Beta.Organization.SpendLimits.IncreaseRequests.Deny(ctx, spendLimitIncreaseRequestID, body) (*BetaSpendLimitIncreaseRequest, error)`

**POST** `/v1/organizations/spend_limit_increase_requests/{spend_limit_increase_request_id}/deny`

Deny a pending spend limit increase request.

Idempotent on `denied`; denying an already-`approved` request returns
400. Anthropic emails the requester unless `suppress_notification` is set.

#### Parameters

- `spendLimitIncreaseRequestID string`

  ID of the spend limit increase request.

- `body BetaOrganizationSpendLimitIncreaseRequestDenyParams`

  - `SuppressNotification param.Field[bool] Optional`

#### Returns

- `type BetaSpendLimitIncreaseRequest`

  - `Type SpendLimitIncreaseRequest`

    default: spend_limit_increase_request

  - `ID string`

  - `Actor BetaSpendLimitIncreaseRequestActorUnion`

    - `type BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

      - `Type UserActor`

        Actor type. Always `user_actor`.

        default: user_actor

      - `Deleted bool`

        True only when the underlying account has been deleted.

        default: false

      - `EmailAddress string`

        The user's email address. Null when the account is unavailable or has been deleted.

      - `Name string`

        The user's current display name. Null when the account is unavailable, has been deleted, or has no name set.

      - `UserID string`

        Tagged ID of the user.

    - `type BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

      - `Type ScopedAPIKeyActor`

        default: scoped_api_key_actor

      - `ScopedAPIKeyID string`

  - `CreatedAt Time`

    format: date-time

  - `Period BetaSpendLimitPeriod`

    - `const BetaSpendLimitPeriodDaily BetaSpendLimitPeriod = "daily"`

    - `const BetaSpendLimitPeriodMonthly BetaSpendLimitPeriod = "monthly"`

    - `const BetaSpendLimitPeriodWeekly BetaSpendLimitPeriod = "weekly"`

  - `ResolvedAt Time`

    format: date-time

  - `ResolvedBy BetaSpendLimitIncreaseRequestResolvedByUnion`

    - `type BetaSpendLimitUserActor`

      A user within the organization. `name` and `email_address` are
      null when the underlying account is unavailable or has been deleted;
      `deleted` is true only for deleted accounts.

    - `type BetaSpendLimitScopedAPIKeyActor`

      A scoped Admin API key acting on behalf of the organization.

  - `SpendSummary BetaSpendSummary`

    Per-member effective-limit report row (`GET /spend_limits/effective`).

    - `Actor BetaSpendSummaryActorUnion`

      - `type BetaSpendLimitUserActor`

        A user within the organization. `name` and `email_address` are
        null when the underlying account is unavailable or has been deleted;
        `deleted` is true only for deleted accounts.

      - `type BetaSpendLimitScopedAPIKeyActor`

        A scoped Admin API key acting on behalf of the organization.

    - `Amount string`

      Effective limit amount as a non-negative integer decimal string in the minor unit of `currency` (cents for USD). `null` means no limit applies for this row's `period` — each period resolves independently, so another period may still cap this member.

    - `Currency string`

      ISO 4217 code of the organization's billing currency; the unit for `amount` and `period_to_date_spend`.

    - `Period BetaSpendLimitPeriod`

      Period this row's effective limit and spend are reported for.

    - `PeriodToDateSpend string`

      The member's spend so far in the current period, as a non-negative decimal string in the minor unit of `currency` (cents for USD). May carry fractional minor units up to three decimal places (e.g. `"12050.5"`) — metered usage is not rounded to whole cents. Reads as `"0"` when the spend reading is temporarily unavailable.

    - `Scope BetaSpendSummaryScopeUnion`

      - `type BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

        - `Type User`

          Scope type. Always `user` for this scope.

          default: user

        - `UserID string`

          Tagged ID of the member the spend limit applies to.

      - `type BetaSpendLimitSeatTierScope`

        - `Type SeatTier`

          default: seat_tier

        - `SeatTier string`

      - `type BetaSpendLimitRBACGroupScope`

        - `Type RBACGroup`

          default: rbac_group

        - `RBACGroupID string`

      - `type BetaSpendLimitOrganizationServiceScope`

        - `Type OrganizationService`

          default: organization_service

        - `Service string`

      - `type BetaSpendLimitOrganizationScope`

        - `Type Organization`

          default: organization

      - `type BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

        - `Type Workspace`

          Scope type. Always `workspace` for this scope.

          default: workspace

        - `WorkspaceID string`

          Tagged ID of the workspace the spend limit applies to.

    - `Source BetaSpendSummarySourceUnion`

      - `type BetaSpendLimitUserScope`

        Scope selecting a single member of the organization.

      - `type BetaSpendLimitSeatTierScope`

      - `type BetaSpendLimitRBACGroupScope`

      - `type BetaSpendLimitOrganizationServiceScope`

      - `type BetaSpendLimitOrganizationScope`

      - `type BetaSpendLimitWorkspaceScope`

        Scope selecting one workspace of a Claude Console organization.

    - `SpendLimitID string`

  - `Status BetaSpendLimitIncreaseRequestStatus`

    - `const BetaSpendLimitIncreaseRequestStatusApproved BetaSpendLimitIncreaseRequestStatus = "approved"`

    - `const BetaSpendLimitIncreaseRequestStatusDenied BetaSpendLimitIncreaseRequestStatus = "denied"`

    - `const BetaSpendLimitIncreaseRequestStatusPending BetaSpendLimitIncreaseRequestStatus = "pending"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaSpendLimitIncreaseRequest, err := client.Beta.Organization.SpendLimits.IncreaseRequests.Deny(
		context.TODO(),
		"spend_limit_increase_request_id",
		anthropic.BetaOrganizationSpendLimitIncreaseRequestDenyParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaSpendLimitIncreaseRequest.ID)
}
```

##### Response (200)

```json
{
  "id": "id",
  "actor": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "period": "daily",
  "resolved_at": "2019-12-27T18:11:19.117Z",
  "resolved_by": {
    "deleted": true,
    "email_address": "email_address",
    "name": "name",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "spend_summary": {
    "actor": {
      "deleted": true,
      "email_address": "email_address",
      "name": "name",
      "type": "user_actor",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "amount": "50000",
    "currency": "USD",
    "period": "daily",
    "period_to_date_spend": "12050.5",
    "scope": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "source": {
      "type": "user",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    },
    "spend_limit_id": "spend_limit_id"
  },
  "status": "approved",
  "type": "spend_limit_increase_request"
}
```

## Beta › Organization › RBAC Groups

### Create RBAC Group

`client.Beta.Organization.RBACGroups.New(ctx, body) (*BetaRBACGroup, error)`

**POST** `/v1/organizations/rbac_groups`

Create an RBAC Group in the Claude Enterprise tenant. Groups created via the API have source type `"direct"`.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `body BetaOrganizationRBACGroupNewParams`

  - `Name param.Field[string]`

    Name of the RBAC Group. Not uniqueness-enforced.

    minLength: 1, maxLength: 255

#### Returns

- `type BetaRBACGroup`

  - `Type RBACGroup`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

    default: rbac_group

  - `ID string`

    ID of the RBAC Group.

  - `CreatedAt Time`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `Name string`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `RoleIDs []string`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `SourceType BetaRBACGroupSourceType`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `const BetaRBACGroupSourceTypeDirect BetaRBACGroupSourceType = "direct"`

    - `const BetaRBACGroupSourceTypeSCIM BetaRBACGroupSourceType = "scim"`

  - `UpdatedAt Time`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaRBACGroup, err := client.Beta.Organization.RBACGroups.New(context.TODO(), anthropic.BetaOrganizationRBACGroupNewParams{
		Name: "Engineering",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaRBACGroup.ID)
}
```

##### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Engineering",
  "role_ids": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "roles": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "source_type": "direct",
  "type": "rbac_group",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### List RBAC Groups

`client.Beta.Organization.RBACGroups.List(ctx, query) (*PageCursor[BetaRBACGroup], error)`

**GET** `/v1/organizations/rbac_groups`

List RBAC Groups in the Claude Enterprise tenant.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `query BetaOrganizationRBACGroupListParams`

  - `Limit param.Field[int64] Optional`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    minimum: 1, maximum: 1000

  - `Page param.Field[string] Optional`

    Optionally set to the `next_page` token from the previous response.

#### Returns

- `type BetaRBACGroup`

  - `Type RBACGroup`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

    default: rbac_group

  - `ID string`

    ID of the RBAC Group.

  - `CreatedAt Time`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `Name string`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `RoleIDs []string`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `SourceType BetaRBACGroupSourceType`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `const BetaRBACGroupSourceTypeDirect BetaRBACGroupSourceType = "direct"`

    - `const BetaRBACGroupSourceTypeSCIM BetaRBACGroupSourceType = "scim"`

  - `UpdatedAt Time`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.RBACGroups.List(context.TODO(), anthropic.BetaOrganizationRBACGroupListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "name": "Engineering",
      "role_ids": [
        "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
      ],
      "roles": [
        "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
      ],
      "source_type": "direct",
      "type": "rbac_group",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

### Get RBAC Group

`client.Beta.Organization.RBACGroups.Get(ctx, rbacGroupID) (*BetaRBACGroup, error)`

**GET** `/v1/organizations/rbac_groups/{rbac_group_id}`

Retrieve an RBAC Group by ID.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `rbacGroupID string`

  ID of the RBAC Group.

#### Returns

- `type BetaRBACGroup`

  - `Type RBACGroup`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

    default: rbac_group

  - `ID string`

    ID of the RBAC Group.

  - `CreatedAt Time`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `Name string`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `RoleIDs []string`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `SourceType BetaRBACGroupSourceType`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `const BetaRBACGroupSourceTypeDirect BetaRBACGroupSourceType = "direct"`

    - `const BetaRBACGroupSourceTypeSCIM BetaRBACGroupSourceType = "scim"`

  - `UpdatedAt Time`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaRBACGroup, err := client.Beta.Organization.RBACGroups.Get(context.TODO(), "rbac_group_id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaRBACGroup.ID)
}
```

##### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Engineering",
  "role_ids": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "roles": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "source_type": "direct",
  "type": "rbac_group",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Update RBAC Group

`client.Beta.Organization.RBACGroups.Update(ctx, rbacGroupID, body) (*BetaRBACGroup, error)`

**POST** `/v1/organizations/rbac_groups/{rbac_group_id}`

Update an RBAC Group's name. Groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `rbacGroupID string`

  ID of the RBAC Group.

- `body BetaOrganizationRBACGroupUpdateParams`

  - `Name param.Field[string] Optional`

    Name of the RBAC Group. Not uniqueness-enforced.

    minLength: 1, maxLength: 255

#### Returns

- `type BetaRBACGroup`

  - `Type RBACGroup`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

    default: rbac_group

  - `ID string`

    ID of the RBAC Group.

  - `CreatedAt Time`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `Name string`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `RoleIDs []string`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `SourceType BetaRBACGroupSourceType`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `const BetaRBACGroupSourceTypeDirect BetaRBACGroupSourceType = "direct"`

    - `const BetaRBACGroupSourceTypeSCIM BetaRBACGroupSourceType = "scim"`

  - `UpdatedAt Time`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaRBACGroup, err := client.Beta.Organization.RBACGroups.Update(
		context.TODO(),
		"rbac_group_id",
		anthropic.BetaOrganizationRBACGroupUpdateParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaRBACGroup.ID)
}
```

##### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "name": "Engineering",
  "role_ids": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "roles": [
    "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s"
  ],
  "source_type": "direct",
  "type": "rbac_group",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Delete RBAC Group

`client.Beta.Organization.RBACGroups.Delete(ctx, rbacGroupID) (*BetaOrganizationRBACGroupDeleteResponse, error)`

**DELETE** `/v1/organizations/rbac_groups/{rbac_group_id}`

Delete an RBAC Group. Groups provisioned by an identity provider (source type `"scim"`) cannot be deleted via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `rbacGroupID string`

  ID of the RBAC Group.

#### Returns

- `type BetaOrganizationRBACGroupDeleteResponse`

  - `Type RBACGroupDeleted`

    Deleted object type.

    For RBAC Groups, this is always `"rbac_group_deleted"`.

    default: rbac_group_deleted

  - `ID string`

    ID of the RBAC Group.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	rbacGroup, err := client.Beta.Organization.RBACGroups.Delete(context.TODO(), "rbac_group_id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", rbacGroup.ID)
}
```

##### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_deleted"
}
```

## Beta › Organization › RBAC Groups › Members

### List RBAC Group Members

`client.Beta.Organization.RBACGroups.Members.List(ctx, rbacGroupID, query) (*PageCursor[BetaRBACGroupMember], error)`

**GET** `/v1/organizations/rbac_groups/{rbac_group_id}/members`

List members of an RBAC Group.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `rbacGroupID string`

  ID of the RBAC Group.

- `query BetaOrganizationRBACGroupMemberListParams`

  - `Limit param.Field[int64] Optional`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    minimum: 1, maximum: 1000

  - `Page param.Field[string] Optional`

    Optionally set to the `next_page` token from the previous response.

#### Returns

- `type BetaRBACGroupMember`

  - `Type RBACGroupMember`

    Object type.

    For RBAC Group Members, this is always `"rbac_group_member"`.

    default: rbac_group_member

  - `CreatedAt Time`

    RFC 3339 timestamp of when the User was added to the RBAC Group.

    format: date-time

  - `Email string`

    Email of the User.

  - `RBACGroupID string`

    ID of the RBAC Group.

  - `UserID string`

    ID of the User.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.RBACGroups.Members.List(
		context.TODO(),
		"rbac_group_id",
		anthropic.BetaOrganizationRBACGroupMemberListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "type": "rbac_group_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    }
  ],
  "has_more": false,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19ncm91cF8wMSJ9"
}
```

### Add RBAC Group Member

`client.Beta.Organization.RBACGroups.Members.Add(ctx, rbacGroupID, body) (*BetaRBACGroupMember, error)`

**POST** `/v1/organizations/rbac_groups/{rbac_group_id}/members`

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `rbacGroupID string`

  ID of the RBAC Group.

- `body BetaOrganizationRBACGroupMemberAddParams`

  - `UserID param.Field[string]`

    ID of the User.

#### Returns

- `type BetaRBACGroupMember`

  - `Type RBACGroupMember`

    Object type.

    For RBAC Group Members, this is always `"rbac_group_member"`.

    default: rbac_group_member

  - `CreatedAt Time`

    RFC 3339 timestamp of when the User was added to the RBAC Group.

    format: date-time

  - `Email string`

    Email of the User.

  - `RBACGroupID string`

    ID of the RBAC Group.

  - `UserID string`

    ID of the User.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaRBACGroupMember, err := client.Beta.Organization.RBACGroups.Members.Add(
		context.TODO(),
		"rbac_group_id",
		anthropic.BetaOrganizationRBACGroupMemberAddParams{
			UserID: "user_01WCz1FkmYMm4gnmykNKUu3Q",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaRBACGroupMember.RBACGroupID)
}
```

##### Response (200)

```json
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
}
```

### Remove RBAC Group Member

`client.Beta.Organization.RBACGroups.Members.Remove(ctx, userID, body) (*BetaOrganizationRBACGroupMemberRemoveResponse, error)`

**DELETE** `/v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}`

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `userID string`

  ID of the User.

- `body BetaOrganizationRBACGroupMemberRemoveParams`

  - `RBACGroupID param.Field[string]`

    ID of the RBAC Group.

#### Returns

- `type BetaOrganizationRBACGroupMemberRemoveResponse`

  - `Type RBACGroupMemberDeleted`

    Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

    default: rbac_group_member_deleted

  - `RBACGroupID string`

    ID of the RBAC Group.

  - `UserID string`

    ID of the User.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	member, err := client.Beta.Organization.RBACGroups.Members.Remove(
		context.TODO(),
		"user_id",
		anthropic.BetaOrganizationRBACGroupMemberRemoveParams{
			RBACGroupID: "rbac_group_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", member.RBACGroupID)
}
```

##### Response (200)

```json
{
  "group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "type": "rbac_group_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
}
```

## Beta › Organization › RBAC Roles

### List RBAC Roles

`client.Beta.Organization.RBACRoles.List(ctx, query) (*PageCursor[BetaRBACRole], error)`

**GET** `/v1/organizations/rbac_roles`

List RBAC Roles in the organization.

The RBAC Roles API is available to Claude Enterprise organizations only.

#### Parameters

- `query BetaOrganizationRBACRoleListParams`

  - `Limit param.Field[int64] Optional`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    minimum: 1, maximum: 1000

  - `Page param.Field[string] Optional`

    Optionally set to the `next_page` token from the previous response.

#### Returns

- `type BetaRBACRole`

  - `Type RBACRole`

    Object type.

    For RBAC Roles, this is always `"rbac_role"`.

    default: rbac_role

  - `ID string`

    ID of the RBAC Role.

  - `CreatedAt Time`

    RFC 3339 datetime string indicating when the RBAC Role was created.

    format: date-time

  - `DisplayName string`

    Name of the RBAC Role. For a role created by Anthropic, this name can differ from the label claude.ai shows, and Anthropic may change the name. To keep a lasting reference to a role, store its `id`.

  - `UpdatedAt Time`

    RFC 3339 datetime string indicating when the RBAC Role was last updated.

    format: date-time

  - `Name string`

    **Deprecated**: Use `display_name` instead; `name` always has the same value.

    Deprecated: use `display_name` instead. Name of the RBAC Role; always the same value as `display_name`.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.RBACRoles.List(context.TODO(), anthropic.BetaOrganizationRBACRoleListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "Project Editor",
      "name": "Project Editor",
      "type": "rbac_role",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
}
```

### Get RBAC Role

`client.Beta.Organization.RBACRoles.Get(ctx, rbacRoleID) (*BetaRBACRole, error)`

**GET** `/v1/organizations/rbac_roles/{rbac_role_id}`

Retrieve an RBAC Role by ID.

The RBAC Roles API is available to Claude Enterprise organizations only.

#### Parameters

- `rbacRoleID string`

  ID of the RBAC Role.

#### Returns

- `type BetaRBACRole`

  - `Type RBACRole`

    Object type.

    For RBAC Roles, this is always `"rbac_role"`.

    default: rbac_role

  - `ID string`

    ID of the RBAC Role.

  - `CreatedAt Time`

    RFC 3339 datetime string indicating when the RBAC Role was created.

    format: date-time

  - `DisplayName string`

    Name of the RBAC Role. For a role created by Anthropic, this name can differ from the label claude.ai shows, and Anthropic may change the name. To keep a lasting reference to a role, store its `id`.

  - `UpdatedAt Time`

    RFC 3339 datetime string indicating when the RBAC Role was last updated.

    format: date-time

  - `Name string`

    **Deprecated**: Use `display_name` instead; `name` always has the same value.

    Deprecated: use `display_name` instead. Name of the RBAC Role; always the same value as `display_name`.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaRBACRole, err := client.Beta.Organization.RBACRoles.Get(context.TODO(), "rbac_role_id")
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaRBACRole.ID)
}
```

##### Response (200)

```json
{
  "id": "rbac_role_016J8xVtKpDq3Wy9ZmN2hR4s",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "Project Editor",
  "name": "Project Editor",
  "type": "rbac_role",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

## Beta › Organization › RBAC Roles › Permissions

### List RBAC Role Permissions

`client.Beta.Organization.RBACRoles.Permissions.List(ctx, rbacRoleID, query) (*PageCursor[BetaRBACRolePermission], error)`

**GET** `/v1/organizations/rbac_roles/{rbac_role_id}/permissions`

List the permissions an RBAC Role grants.

The RBAC Roles API is available to Claude Enterprise organizations only.

#### Parameters

- `rbacRoleID string`

  ID of the RBAC Role.

- `query BetaOrganizationRBACRolePermissionListParams`

  - `Limit param.Field[int64] Optional`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    minimum: 1, maximum: 1000

  - `Page param.Field[string] Optional`

    Optionally set to the `next_page` token from the previous response.

#### Returns

- `type BetaRBACRolePermission`

  - `Type RBACRolePermission`

    Object type.

    For RBAC Role Permissions, this is always `"rbac_role_permission"`.

    default: rbac_role_permission

  - `Action string`

    Action the permission grants on the resource.

    The vocabulary follows the resource: an `organization` grant carries a
    product-feature entitlement (for example `chat`), an admin-panel
    permission entitlement (`permission_*`), or a blanket capability-access
    mode — `capability_access_all` grants every product-feature entitlement,
    and `capability_access_all_ga` grants the generally-available subset as
    it stands at permission-check time; neither mode grants model-access
    entitlements. A consumer enumerating a role's per-feature grants should
    treat a blanket row as granting every product-feature entitlement it
    covers, or it will under-report the role's effective access. A `connector_tool` grant carries
    a tool-access action (`use` or `always_allow`); a `connector_scope` grant
    carries the scope action `grant` (the role may receive the named OAuth
    scope when tokens are minted for the connector); `connector` and
    `all_connectors` grants carry a tool-access action, the scope action, or
    an authentication-method action (`interactive` or `managed`).

  - `Resource BetaRBACRolePermissionResourceUnion`

    What the permission applies to.

    A tagged union: `type` names the kind of resource and determines which
    identifier fields are present.

    - `type BetaRBACOrganizationPermissionResource`

      - `Type Organization`

        Kind of resource the permission applies to.

        default: organization

      - `OrganizationID string`

        UUID of the organization the permission applies to.

    - `type BetaRBACConnectorToolPermissionResource`

      - `Type ConnectorTool`

        Kind of resource the permission applies to.

        default: connector_tool

      - `ConnectorID string`

        ID of the connector the permission applies to.

      - `ToolName string`

        Published name of the connector tool the permission applies to.

        When the published name contains characters outside `[a-zA-Z0-9_-]` (or
        collides with a reserved form), it is server-encoded into a stable
        `{prefix}_{32-hex}` form — a shortened readable prefix of the name plus
        a hash — from which the published name is not recoverable.

    - `type BetaRBACConnectorScopePermissionResource`

      - `Type ConnectorScope`

        Kind of resource the permission applies to.

        default: connector_scope

      - `ConnectorID string`

        ID of the connector the permission applies to.

      - `Scope string`

        OAuth scope the permission names — the role may receive this scope when
        tokens are minted for the connector.

        Subject to the same encoding rule as `tool_name`: a scope containing
        characters outside `[a-zA-Z0-9_-]` (or colliding with a reserved form)
        appears server-encoded in a stable `{prefix}_{32-hex}` form. OAuth
        scopes routinely contain `:` and `/`, so most appear encoded.

    - `type BetaRBACConnectorPermissionResource`

      - `Type Connector`

        Kind of resource the permission applies to.

        default: connector

      - `ConnectorID string`

        ID of the connector the permission applies to.

    - `type BetaRBACAllConnectorsPermissionResource`

      - `Type AllConnectors`

        Kind of resource the permission applies to.

        default: all_connectors

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.RBACRoles.Permissions.List(
		context.TODO(),
		"rbac_role_id",
		anthropic.BetaOrganizationRBACRolePermissionListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "action": "use",
      "resource": {
        "organization_id": "3c4f5e6d-7a8b-49c0-9d1e-2f3a4b5c6d7e",
        "type": "organization"
      },
      "type": "rbac_role_permission"
    }
  ],
  "has_more": true,
  "next_page": "eyJjdXJzb3IiOiAicmJhY19yb2xlXzAxIn0"
}
```

## Beta › Organization › Plugins

### Create Plugin

`client.Beta.Organization.Plugins.New(ctx, params) (*BetaPlugin, error)`

**POST** `/v1/organizations/plugins`

Create an organization-owned Plugin and its first version by uploading the
version's files.

The upload is `multipart/form-data`: the version's files (`files`, each part sent
as `files[]`), with an optional `marketplace_id` and `release_notes`. The manifest's `name` becomes the
Plugin's `name`, and `display_name`, `description` and `manifest_version` come
from the manifest too.

`name` may contain lowercase letters (from any alphabet), digits, and hyphens, up
to 64 characters. Uppercase letters, spaces, underscores, and other punctuation are
rejected.

The `name` must be unique within the marketplace: a name already taken
returns a 409 with `error_code` `plugin_name_taken` and, when a Plugin holds it,
that Plugin's ID in `details.plugin_id`. A Plugin going into the organization's
library marketplace is also refused with a 409 when one of its skills has the name of
an organization skill (a skill an administrator uploaded for the whole organization
in claude.ai): `error_code` `skill_name_taken`, with that name in
`details.skill_name`; rename the skill, or remove the organization skill in
claude.ai. A 503 with `error_code`
`registration_pending` means the Plugin and its version were stored (their IDs are
in `details`) but are not yet usable in claude.ai: do not retry the create (the
retry would return `plugin_name_taken`); create a version on the stored Plugin
instead, which completes it.

For a worked example, see [Create a plugin](https://platform.claude.com/docs/en/manage-claude/plugins-api#create-a-plugin)
in the Plugins API guide.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `params BetaOrganizationPluginNewParams`

  - `Files param.Field[[]Reader]`

    Body param: The version's files: one part per file, the part's filename being the file's path within the Plugin (for example `skills/review-pr/SKILL.md`), or a single `.zip` or `.plugin` archive holding them all. On the wire each part is named `files[]`, and a part named plain `files` is not read; with cURL, `-F 'files[]=@SKILL.md;filename=skills/review-pr/SKILL.md'`. The files must include the manifest, `.claude-plugin/plugin.json`.

  - `MarketplaceID param.Field[string] Optional`

    Body param: ID of the organization-owned plugin marketplace to create the Plugin in (prefixed `marketplace_`). It must be a `manual` marketplace, one whose Plugins are uploaded rather than synchronized from a repository. When omitted, the Plugin is created in the organization's library marketplace, an organization-owned `manual` marketplace created on first use.

  - `ReleaseNotes param.Field[string] Optional`

    Body param: Release notes stored with the version and shown in its version history in claude.ai; up to 5,000 characters.

    maxLength: 5000

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPlugin`

  - `Type Plugin`

    Always `plugin`.

    default: plugin

  - `ID string`

    The Plugin's ID.

  - `Components []BetaPluginComponent`

    What the served version contains; null when not enumerated.

    - `Type BetaPluginComponentType`

      The kind of component.

      - `const BetaPluginComponentTypeAgent BetaPluginComponentType = "agent"`

      - `const BetaPluginComponentTypeCli BetaPluginComponentType = "cli"`

      - `const BetaPluginComponentTypeCommand BetaPluginComponentType = "command"`

      - `const BetaPluginComponentTypeHook BetaPluginComponentType = "hook"`

      - `const BetaPluginComponentTypeMCPServer BetaPluginComponentType = "mcp_server"`

      - `const BetaPluginComponentTypeSkill BetaPluginComponentType = "skill"`

    - `Description string`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `Name string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `ContentScan BetaPluginContentScan`

    The served version's content scan; null when it has not been scanned.

    - `Assessment BetaPluginContentScanAssessment`

      The scan's verdict; set only when `status` is `completed`.

      - `const BetaPluginContentScanAssessmentFail BetaPluginContentScanAssessment = "fail"`

      - `const BetaPluginContentScanAssessmentPass BetaPluginContentScanAssessment = "pass"`

      - `const BetaPluginContentScanAssessmentUnknown BetaPluginContentScanAssessment = "unknown"`

      - `const BetaPluginContentScanAssessmentWarn BetaPluginContentScanAssessment = "warn"`

    - `Reason string`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `Status BetaPluginContentScanStatus`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `const BetaPluginContentScanStatusCompleted BetaPluginContentScanStatus = "completed"`

      - `const BetaPluginContentScanStatusErrored BetaPluginContentScanStatus = "errored"`

      - `const BetaPluginContentScanStatusProcessing BetaPluginContentScanStatus = "processing"`

  - `CreatedAt Time`

    RFC 3339.

    format: date-time

  - `CreatedBy BetaPluginCreatedByUnion`

    Who created the Plugin; null when no creator is recorded.

    - `type BetaPluginUserActor`

      - `Type UserActor`

        A member of the organization.

        default: user_actor

      - `EmailAddress string`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `UserID string`

        The member's User ID.

    - `type BetaPluginAPIActor`

      - `Type APIActor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `APIKeyID string`

        The key's ID.

  - `Description string`

    The served version's description.

  - `DisplayName string`

    The served version's display name.

  - `LatestVersionID string`

    The newest version.

  - `ManifestVersion string`

    The version string the served version's manifest declares.

  - `MarketplaceID string`

    The ID of the plugin marketplace the Plugin lives in.

  - `Name string`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `OrganizationInstallationPreference BetaPluginOrganizationInstallationPreference`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `const BetaPluginOrganizationInstallationPreferenceAutoInstall BetaPluginOrganizationInstallationPreference = "auto_install"`

    - `const BetaPluginOrganizationInstallationPreferenceAvailable BetaPluginOrganizationInstallationPreference = "available"`

    - `const BetaPluginOrganizationInstallationPreferenceNotAvailable BetaPluginOrganizationInstallationPreference = "not_available"`

    - `const BetaPluginOrganizationInstallationPreferenceRequired BetaPluginOrganizationInstallationPreference = "required"`

  - `OrganizationInstallationPreferenceInherited bool`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `Owner BetaPluginOwnerUnion`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `type BetaPluginOwnerOrganization`

      - `Type Organization`

        The Plugin lives in a plugin marketplace the organization owns.

        default: organization

    - `type BetaPluginOwnerUser`

      - `Type User`

        The Plugin lives in one member's personal plugin marketplace.

        default: user

      - `UserID string`

        The member's User ID.

  - `Reach BetaPluginReach`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `const BetaPluginReachContained BetaPluginReach = "contained"`

    - `const BetaPluginReachPrivileged BetaPluginReach = "privileged"`

    - `const BetaPluginReachRemote BetaPluginReach = "remote"`

  - `ServedVersionID string`

    The version claude.ai serves to members.

  - `ServedVersionPinned bool`

    False while the served version follows each new version; true once it has been pinned to one.

  - `UpdatedAt Time`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

#### Example

```go
package main

import (
	"bytes"
	"context"
	"fmt"
	"io"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaPlugin, err := client.Beta.Organization.Plugins.New(context.TODO(), anthropic.BetaOrganizationPluginNewParams{
		Files: []io.Reader{io.Reader(bytes.NewBuffer([]byte("Example data")))},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaPlugin.ID)
}
```

##### Response (200)

```json
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "manifest_version": "1.2.0",
  "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "name": "code-review-helper",
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "owner": {
    "type": "organization"
  },
  "reach": "contained",
  "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
  "served_version_pinned": true,
  "type": "plugin",
  "updated_at": "2026-03-14T09:26:53.589793Z"
}
```

### Get Plugin

`client.Beta.Organization.Plugins.Get(ctx, pluginID, params) (*BetaPlugin, error)`

**GET** `/v1/organizations/plugins/{plugin_id}`

Retrieve a Plugin by ID.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `pluginID string`

  ID of the Plugin (prefixed `plugin_`).

- `params BetaOrganizationPluginGetParams`

  - `OrganizationID param.Field[string] Optional`

    Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPlugin`

  - `Type Plugin`

    Always `plugin`.

    default: plugin

  - `ID string`

    The Plugin's ID.

  - `Components []BetaPluginComponent`

    What the served version contains; null when not enumerated.

    - `Type BetaPluginComponentType`

      The kind of component.

      - `const BetaPluginComponentTypeAgent BetaPluginComponentType = "agent"`

      - `const BetaPluginComponentTypeCli BetaPluginComponentType = "cli"`

      - `const BetaPluginComponentTypeCommand BetaPluginComponentType = "command"`

      - `const BetaPluginComponentTypeHook BetaPluginComponentType = "hook"`

      - `const BetaPluginComponentTypeMCPServer BetaPluginComponentType = "mcp_server"`

      - `const BetaPluginComponentTypeSkill BetaPluginComponentType = "skill"`

    - `Description string`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `Name string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `ContentScan BetaPluginContentScan`

    The served version's content scan; null when it has not been scanned.

    - `Assessment BetaPluginContentScanAssessment`

      The scan's verdict; set only when `status` is `completed`.

      - `const BetaPluginContentScanAssessmentFail BetaPluginContentScanAssessment = "fail"`

      - `const BetaPluginContentScanAssessmentPass BetaPluginContentScanAssessment = "pass"`

      - `const BetaPluginContentScanAssessmentUnknown BetaPluginContentScanAssessment = "unknown"`

      - `const BetaPluginContentScanAssessmentWarn BetaPluginContentScanAssessment = "warn"`

    - `Reason string`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `Status BetaPluginContentScanStatus`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `const BetaPluginContentScanStatusCompleted BetaPluginContentScanStatus = "completed"`

      - `const BetaPluginContentScanStatusErrored BetaPluginContentScanStatus = "errored"`

      - `const BetaPluginContentScanStatusProcessing BetaPluginContentScanStatus = "processing"`

  - `CreatedAt Time`

    RFC 3339.

    format: date-time

  - `CreatedBy BetaPluginCreatedByUnion`

    Who created the Plugin; null when no creator is recorded.

    - `type BetaPluginUserActor`

      - `Type UserActor`

        A member of the organization.

        default: user_actor

      - `EmailAddress string`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `UserID string`

        The member's User ID.

    - `type BetaPluginAPIActor`

      - `Type APIActor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `APIKeyID string`

        The key's ID.

  - `Description string`

    The served version's description.

  - `DisplayName string`

    The served version's display name.

  - `LatestVersionID string`

    The newest version.

  - `ManifestVersion string`

    The version string the served version's manifest declares.

  - `MarketplaceID string`

    The ID of the plugin marketplace the Plugin lives in.

  - `Name string`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `OrganizationInstallationPreference BetaPluginOrganizationInstallationPreference`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `const BetaPluginOrganizationInstallationPreferenceAutoInstall BetaPluginOrganizationInstallationPreference = "auto_install"`

    - `const BetaPluginOrganizationInstallationPreferenceAvailable BetaPluginOrganizationInstallationPreference = "available"`

    - `const BetaPluginOrganizationInstallationPreferenceNotAvailable BetaPluginOrganizationInstallationPreference = "not_available"`

    - `const BetaPluginOrganizationInstallationPreferenceRequired BetaPluginOrganizationInstallationPreference = "required"`

  - `OrganizationInstallationPreferenceInherited bool`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `Owner BetaPluginOwnerUnion`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `type BetaPluginOwnerOrganization`

      - `Type Organization`

        The Plugin lives in a plugin marketplace the organization owns.

        default: organization

    - `type BetaPluginOwnerUser`

      - `Type User`

        The Plugin lives in one member's personal plugin marketplace.

        default: user

      - `UserID string`

        The member's User ID.

  - `Reach BetaPluginReach`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `const BetaPluginReachContained BetaPluginReach = "contained"`

    - `const BetaPluginReachPrivileged BetaPluginReach = "privileged"`

    - `const BetaPluginReachRemote BetaPluginReach = "remote"`

  - `ServedVersionID string`

    The version claude.ai serves to members.

  - `ServedVersionPinned bool`

    False while the served version follows each new version; true once it has been pinned to one.

  - `UpdatedAt Time`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaPlugin, err := client.Beta.Organization.Plugins.Get(
		context.TODO(),
		"plugin_id",
		anthropic.BetaOrganizationPluginGetParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaPlugin.ID)
}
```

##### Response (200)

```json
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "manifest_version": "1.2.0",
  "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "name": "code-review-helper",
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "owner": {
    "type": "organization"
  },
  "reach": "contained",
  "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
  "served_version_pinned": true,
  "type": "plugin",
  "updated_at": "2026-03-14T09:26:53.589793Z"
}
```

### Update Plugin

`client.Beta.Organization.Plugins.Update(ctx, pluginID, params) (*BetaPlugin, error)`

**POST** `/v1/organizations/plugins/{plugin_id}`

Change which stored version of an organization-owned Plugin is served to members,
for example to roll back to an earlier one. This pins the served version: later
uploads are stored but no longer change what is served, and pinning cannot currently
be undone, here or in claude.ai.

Pass the version as `served_version_id`: an earlier one to roll back, a later one to
start serving a version that was stored without being served, or the one already
served to pin it without changing what is served. No new version is created.

When the organization has content scanning enabled, a version whose scan is still
running is refused with a 409 (`error_code` `scan_pending`; retry once the scan
finishes) and one whose scan failed, errored or reached no verdict with a 400
(`scan_failed`; a `warn` is accepted). When the Plugin is in the organization's
library marketplace, a version other than the one served is also refused with a 409
when one of its skills has a name that an organization skill (one an administrator
uploaded for the whole organization in claude.ai) has since taken: `error_code`
`skill_name_taken`, with that name in `details.skill_name`. A member-owned Plugin
cannot be updated here (403).

This endpoint does not write installation settings; they are written at
`/v1/organizations/plugins/{plugin_id}/installation_settings/{target}`.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `pluginID string`

  ID of the Plugin (prefixed `plugin_`).

- `params BetaOrganizationPluginUpdateParams`

  - `ServedVersionID param.Field[string]`

    Body param: Serve this version of the Plugin (prefixed `pluginver_`) and pin the served version to it; `latest` is not accepted.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPlugin`

  - `Type Plugin`

    Always `plugin`.

    default: plugin

  - `ID string`

    The Plugin's ID.

  - `Components []BetaPluginComponent`

    What the served version contains; null when not enumerated.

    - `Type BetaPluginComponentType`

      The kind of component.

      - `const BetaPluginComponentTypeAgent BetaPluginComponentType = "agent"`

      - `const BetaPluginComponentTypeCli BetaPluginComponentType = "cli"`

      - `const BetaPluginComponentTypeCommand BetaPluginComponentType = "command"`

      - `const BetaPluginComponentTypeHook BetaPluginComponentType = "hook"`

      - `const BetaPluginComponentTypeMCPServer BetaPluginComponentType = "mcp_server"`

      - `const BetaPluginComponentTypeSkill BetaPluginComponentType = "skill"`

    - `Description string`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `Name string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `ContentScan BetaPluginContentScan`

    The served version's content scan; null when it has not been scanned.

    - `Assessment BetaPluginContentScanAssessment`

      The scan's verdict; set only when `status` is `completed`.

      - `const BetaPluginContentScanAssessmentFail BetaPluginContentScanAssessment = "fail"`

      - `const BetaPluginContentScanAssessmentPass BetaPluginContentScanAssessment = "pass"`

      - `const BetaPluginContentScanAssessmentUnknown BetaPluginContentScanAssessment = "unknown"`

      - `const BetaPluginContentScanAssessmentWarn BetaPluginContentScanAssessment = "warn"`

    - `Reason string`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `Status BetaPluginContentScanStatus`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `const BetaPluginContentScanStatusCompleted BetaPluginContentScanStatus = "completed"`

      - `const BetaPluginContentScanStatusErrored BetaPluginContentScanStatus = "errored"`

      - `const BetaPluginContentScanStatusProcessing BetaPluginContentScanStatus = "processing"`

  - `CreatedAt Time`

    RFC 3339.

    format: date-time

  - `CreatedBy BetaPluginCreatedByUnion`

    Who created the Plugin; null when no creator is recorded.

    - `type BetaPluginUserActor`

      - `Type UserActor`

        A member of the organization.

        default: user_actor

      - `EmailAddress string`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `UserID string`

        The member's User ID.

    - `type BetaPluginAPIActor`

      - `Type APIActor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `APIKeyID string`

        The key's ID.

  - `Description string`

    The served version's description.

  - `DisplayName string`

    The served version's display name.

  - `LatestVersionID string`

    The newest version.

  - `ManifestVersion string`

    The version string the served version's manifest declares.

  - `MarketplaceID string`

    The ID of the plugin marketplace the Plugin lives in.

  - `Name string`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `OrganizationInstallationPreference BetaPluginOrganizationInstallationPreference`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `const BetaPluginOrganizationInstallationPreferenceAutoInstall BetaPluginOrganizationInstallationPreference = "auto_install"`

    - `const BetaPluginOrganizationInstallationPreferenceAvailable BetaPluginOrganizationInstallationPreference = "available"`

    - `const BetaPluginOrganizationInstallationPreferenceNotAvailable BetaPluginOrganizationInstallationPreference = "not_available"`

    - `const BetaPluginOrganizationInstallationPreferenceRequired BetaPluginOrganizationInstallationPreference = "required"`

  - `OrganizationInstallationPreferenceInherited bool`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `Owner BetaPluginOwnerUnion`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `type BetaPluginOwnerOrganization`

      - `Type Organization`

        The Plugin lives in a plugin marketplace the organization owns.

        default: organization

    - `type BetaPluginOwnerUser`

      - `Type User`

        The Plugin lives in one member's personal plugin marketplace.

        default: user

      - `UserID string`

        The member's User ID.

  - `Reach BetaPluginReach`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `const BetaPluginReachContained BetaPluginReach = "contained"`

    - `const BetaPluginReachPrivileged BetaPluginReach = "privileged"`

    - `const BetaPluginReachRemote BetaPluginReach = "remote"`

  - `ServedVersionID string`

    The version claude.ai serves to members.

  - `ServedVersionPinned bool`

    False while the served version follows each new version; true once it has been pinned to one.

  - `UpdatedAt Time`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaPlugin, err := client.Beta.Organization.Plugins.Update(
		context.TODO(),
		"plugin_id",
		anthropic.BetaOrganizationPluginUpdateParams{
			ServedVersionID: "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaPlugin.ID)
}
```

##### Response (200)

```json
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "manifest_version": "1.2.0",
  "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "name": "code-review-helper",
  "organization_installation_preference": "available",
  "organization_installation_preference_inherited": true,
  "owner": {
    "type": "organization"
  },
  "reach": "contained",
  "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
  "served_version_pinned": true,
  "type": "plugin",
  "updated_at": "2026-03-14T09:26:53.589793Z"
}
```

### List Plugins

`client.Beta.Organization.Plugins.List(ctx, params) (*PageCursor[BetaPlugin], error)`

**GET** `/v1/organizations/plugins`

List the Plugins created under the organization, newest first: those in the
organization's own plugin marketplaces and those in members' personal plugin
marketplaces.

Plugins in members' personal marketplaces are listed with the same detail as the
organization's own, and their files can be downloaded through the version archive
endpoint, which records each such download on the Compliance API activity feed.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `params BetaOrganizationPluginListParams`

  - `CreatedAtGt param.Field[Time] Optional`

    Query param: RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

    format: date-time

  - `CreatedAtGte param.Field[Time] Optional`

    Query param: RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

    format: date-time

  - `CreatedAtLt param.Field[Time] Optional`

    Query param: RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

    format: date-time

  - `CreatedAtLte param.Field[Time] Optional`

    Query param: RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

    format: date-time

  - `Limit param.Field[int64] Optional`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `100`.

    minimum: 1, maximum: 100

  - `MarketplaceID param.Field[string] Optional`

    Query param: Only Plugins in this plugin marketplace (prefixed `marketplace_`).

  - `OrganizationID param.Field[string] Optional`

    Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

  - `OwnerType param.Field[BetaOrganizationPluginListParamsOwnerType] Optional`

    Query param: `organization` for Plugins in the organization's plugin marketplaces, `user` for Plugins in members' personal plugin marketplaces.

    - `const BetaOrganizationPluginListParamsOwnerTypeOrganization BetaOrganizationPluginListParamsOwnerType = "organization"`

    - `const BetaOrganizationPluginListParamsOwnerTypeUser BetaOrganizationPluginListParamsOwnerType = "user"`

  - `OwnerUserID param.Field[string] Optional`

    Query param: Only Plugins in this member's personal plugin marketplaces (prefixed `user_`); a removed member's ID is accepted.

  - `Page param.Field[string] Optional`

    Query param: Optionally set to the `next_page` token from the previous response.

    maxLength: 2048

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPlugin`

  - `Type Plugin`

    Always `plugin`.

    default: plugin

  - `ID string`

    The Plugin's ID.

  - `Components []BetaPluginComponent`

    What the served version contains; null when not enumerated.

    - `Type BetaPluginComponentType`

      The kind of component.

      - `const BetaPluginComponentTypeAgent BetaPluginComponentType = "agent"`

      - `const BetaPluginComponentTypeCli BetaPluginComponentType = "cli"`

      - `const BetaPluginComponentTypeCommand BetaPluginComponentType = "command"`

      - `const BetaPluginComponentTypeHook BetaPluginComponentType = "hook"`

      - `const BetaPluginComponentTypeMCPServer BetaPluginComponentType = "mcp_server"`

      - `const BetaPluginComponentTypeSkill BetaPluginComponentType = "skill"`

    - `Description string`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `Name string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `ContentScan BetaPluginContentScan`

    The served version's content scan; null when it has not been scanned.

    - `Assessment BetaPluginContentScanAssessment`

      The scan's verdict; set only when `status` is `completed`.

      - `const BetaPluginContentScanAssessmentFail BetaPluginContentScanAssessment = "fail"`

      - `const BetaPluginContentScanAssessmentPass BetaPluginContentScanAssessment = "pass"`

      - `const BetaPluginContentScanAssessmentUnknown BetaPluginContentScanAssessment = "unknown"`

      - `const BetaPluginContentScanAssessmentWarn BetaPluginContentScanAssessment = "warn"`

    - `Reason string`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `Status BetaPluginContentScanStatus`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `const BetaPluginContentScanStatusCompleted BetaPluginContentScanStatus = "completed"`

      - `const BetaPluginContentScanStatusErrored BetaPluginContentScanStatus = "errored"`

      - `const BetaPluginContentScanStatusProcessing BetaPluginContentScanStatus = "processing"`

  - `CreatedAt Time`

    RFC 3339.

    format: date-time

  - `CreatedBy BetaPluginCreatedByUnion`

    Who created the Plugin; null when no creator is recorded.

    - `type BetaPluginUserActor`

      - `Type UserActor`

        A member of the organization.

        default: user_actor

      - `EmailAddress string`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `UserID string`

        The member's User ID.

    - `type BetaPluginAPIActor`

      - `Type APIActor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `APIKeyID string`

        The key's ID.

  - `Description string`

    The served version's description.

  - `DisplayName string`

    The served version's display name.

  - `LatestVersionID string`

    The newest version.

  - `ManifestVersion string`

    The version string the served version's manifest declares.

  - `MarketplaceID string`

    The ID of the plugin marketplace the Plugin lives in.

  - `Name string`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `OrganizationInstallationPreference BetaPluginOrganizationInstallationPreference`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `const BetaPluginOrganizationInstallationPreferenceAutoInstall BetaPluginOrganizationInstallationPreference = "auto_install"`

    - `const BetaPluginOrganizationInstallationPreferenceAvailable BetaPluginOrganizationInstallationPreference = "available"`

    - `const BetaPluginOrganizationInstallationPreferenceNotAvailable BetaPluginOrganizationInstallationPreference = "not_available"`

    - `const BetaPluginOrganizationInstallationPreferenceRequired BetaPluginOrganizationInstallationPreference = "required"`

  - `OrganizationInstallationPreferenceInherited bool`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `Owner BetaPluginOwnerUnion`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `type BetaPluginOwnerOrganization`

      - `Type Organization`

        The Plugin lives in a plugin marketplace the organization owns.

        default: organization

    - `type BetaPluginOwnerUser`

      - `Type User`

        The Plugin lives in one member's personal plugin marketplace.

        default: user

      - `UserID string`

        The member's User ID.

  - `Reach BetaPluginReach`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `const BetaPluginReachContained BetaPluginReach = "contained"`

    - `const BetaPluginReachPrivileged BetaPluginReach = "privileged"`

    - `const BetaPluginReachRemote BetaPluginReach = "remote"`

  - `ServedVersionID string`

    The version claude.ai serves to members.

  - `ServedVersionPinned bool`

    False while the served version follows each new version; true once it has been pinned to one.

  - `UpdatedAt Time`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Plugins.List(context.TODO(), anthropic.BetaOrganizationPluginListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "components": [
        {
          "description": "description",
          "name": "review-pr",
          "type": "skill"
        }
      ],
      "content_scan": {
        "assessment": "warn",
        "reason": "credential-exposure",
        "status": "completed"
      },
      "created_at": "2026-03-14T09:26:53.589793Z",
      "created_by": {
        "email_address": "user@example.com",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "description": "Reviews pull requests against your team's conventions.",
      "display_name": "Code Review Helper",
      "latest_version_id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
      "manifest_version": "1.2.0",
      "marketplace_id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
      "name": "code-review-helper",
      "organization_installation_preference": "available",
      "organization_installation_preference_inherited": true,
      "owner": {
        "type": "organization"
      },
      "reach": "contained",
      "served_version_id": "pluginver_01K9wPcHd4Rm2Tx8Vq6Ln3Sb",
      "served_version_pinned": true,
      "type": "plugin",
      "updated_at": "2026-03-14T09:26:53.589793Z"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

### Delete Plugin

`client.Beta.Organization.Plugins.Delete(ctx, pluginID, body) (*BetaDeletedPlugin, error)`

**DELETE** `/v1/organizations/plugins/{plugin_id}`

Permanently delete a Plugin and every version it holds, exactly as when an
administrator deletes it in claude.ai. The Plugin may belong to the organization or
to a member, including a member who has since left the organization.

An organization-owned Plugin's installation settings go with it; a member-owned
Plugin's shares are withdrawn and its owner no longer has it.

To take an organization-owned Plugin out of use reversibly, set its
organization-wide installation setting to `not_available` instead (and
remove or change any group settings, which override it for their members). Only a
Plugin in a `manual` marketplace can be deleted here; one synchronized from a
repository is removed by removing it from the repository (400).

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `pluginID string`

  ID of the Plugin (prefixed `plugin_`).

- `body BetaOrganizationPluginDeleteParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaDeletedPlugin`

  - `Type PluginDeleted`

    Always `plugin_deleted`.

    default: plugin_deleted

  - `ID string`

    The deleted Plugin's ID.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaDeletedPlugin, err := client.Beta.Organization.Plugins.Delete(
		context.TODO(),
		"plugin_id",
		anthropic.BetaOrganizationPluginDeleteParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaDeletedPlugin.ID)
}
```

##### Response (200)

```json
{
  "id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "type": "plugin_deleted"
}
```

## Beta › Organization › Plugins › Versions

### Create Plugin Version

`client.Beta.Organization.Plugins.Versions.New(ctx, pluginID, params) (*BetaPluginVersion, error)`

**POST** `/v1/organizations/plugins/{plugin_id}/versions`

Add a version to an organization-owned Plugin by uploading the new version's
files; it becomes the version served to members unless the Plugin's served version
has been pinned.

The upload is the same `multipart/form-data` as creating a Plugin: the version's
files (`files`, each part sent as `files[]`) and optional `release_notes`. The uploaded manifest's `name`
must equal the Plugin's `name`. Returns the stored version; read the Plugin back to
see which version it serves.

Only a Plugin in a `manual` marketplace takes uploads; a Plugin synchronized from
a repository gets its versions from the repository. When the Plugin is in the
organization's library marketplace, a version that adds a skill with the name of an
organization skill (a skill an administrator uploaded for the whole organization in
claude.ai) is refused with a 409: `error_code` `skill_name_taken`, with that name in
`details.skill_name`. A 503 with `error_code`
`registration_pending` means the version was stored but is not yet usable; a later
version create on the Plugin completes it.

For a worked example, see [Create a version](https://platform.claude.com/docs/en/manage-claude/plugins-api#create-a-version)
in the Plugins API guide.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `pluginID string`

  ID of the Plugin (prefixed `plugin_`).

- `params BetaOrganizationPluginVersionNewParams`

  - `Files param.Field[[]Reader]`

    Body param: The version's files: one part per file, the part's filename being the file's path within the Plugin (for example `skills/review-pr/SKILL.md`), or a single `.zip` or `.plugin` archive holding them all. On the wire each part is named `files[]`, and a part named plain `files` is not read; with cURL, `-F 'files[]=@SKILL.md;filename=skills/review-pr/SKILL.md'`. The files must include the manifest, `.claude-plugin/plugin.json`.

  - `ReleaseNotes param.Field[string] Optional`

    Body param: Release notes stored with the version and shown in its version history in claude.ai; up to 5,000 characters.

    maxLength: 5000

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPluginVersion`

  - `Type PluginVersion`

    Always `plugin_version`.

    default: plugin_version

  - `ID string`

    The version's ID.

  - `Components []BetaPluginComponent`

    What the version contains; null when not enumerated.

    - `Type BetaPluginComponentType`

      The kind of component.

      - `const BetaPluginComponentTypeAgent BetaPluginComponentType = "agent"`

      - `const BetaPluginComponentTypeCli BetaPluginComponentType = "cli"`

      - `const BetaPluginComponentTypeCommand BetaPluginComponentType = "command"`

      - `const BetaPluginComponentTypeHook BetaPluginComponentType = "hook"`

      - `const BetaPluginComponentTypeMCPServer BetaPluginComponentType = "mcp_server"`

      - `const BetaPluginComponentTypeSkill BetaPluginComponentType = "skill"`

    - `Description string`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `Name string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `ContentScan BetaPluginContentScan`

    This version's content scan; null when it has not been scanned.

    - `Assessment BetaPluginContentScanAssessment`

      The scan's verdict; set only when `status` is `completed`.

      - `const BetaPluginContentScanAssessmentFail BetaPluginContentScanAssessment = "fail"`

      - `const BetaPluginContentScanAssessmentPass BetaPluginContentScanAssessment = "pass"`

      - `const BetaPluginContentScanAssessmentUnknown BetaPluginContentScanAssessment = "unknown"`

      - `const BetaPluginContentScanAssessmentWarn BetaPluginContentScanAssessment = "warn"`

    - `Reason string`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `Status BetaPluginContentScanStatus`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `const BetaPluginContentScanStatusCompleted BetaPluginContentScanStatus = "completed"`

      - `const BetaPluginContentScanStatusErrored BetaPluginContentScanStatus = "errored"`

      - `const BetaPluginContentScanStatusProcessing BetaPluginContentScanStatus = "processing"`

  - `CreatedAt Time`

    RFC 3339.

    format: date-time

  - `CreatedBy BetaPluginVersionCreatedByUnion`

    Who uploaded this version; null when not recorded.

    - `type BetaPluginUserActor`

      - `Type UserActor`

        A member of the organization.

        default: user_actor

      - `EmailAddress string`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `UserID string`

        The member's User ID.

    - `type BetaPluginAPIActor`

      - `Type APIActor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `APIKeyID string`

        The key's ID.

  - `Description string`

    The manifest's description; null when it declares none.

  - `DisplayName string`

    The manifest's display name; null when it declares none.

  - `ManifestVersion string`

    The version string the manifest declares; null when it declares none.

  - `PluginID string`

    The Plugin's ID.

  - `Reach BetaPluginVersionReach`

    How far the version reaches: `remote`, `privileged` or `contained`, as on the Plugin; null when not classifiable.

    - `const BetaPluginVersionReachContained BetaPluginVersionReach = "contained"`

    - `const BetaPluginVersionReachPrivileged BetaPluginVersionReach = "privileged"`

    - `const BetaPluginVersionReachRemote BetaPluginVersionReach = "remote"`

  - `ReleaseNotes string`

    As supplied with the upload; null when none were supplied.

#### Example

```go
package main

import (
	"bytes"
	"context"
	"fmt"
	"io"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaPluginVersion, err := client.Beta.Organization.Plugins.Versions.New(
		context.TODO(),
		"plugin_id",
		anthropic.BetaOrganizationPluginVersionNewParams{
			Files: []io.Reader{io.Reader(bytes.NewBuffer([]byte("Example data")))},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaPluginVersion.ID)
}
```

##### Response (200)

```json
{
  "id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "manifest_version": "1.2.0",
  "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "reach": "contained",
  "release_notes": "Adds a review checklist for database migrations.",
  "type": "plugin_version"
}
```

### List Plugin Versions

`client.Beta.Organization.Plugins.Versions.List(ctx, pluginID, params) (*PageCursor[BetaPluginVersion], error)`

**GET** `/v1/organizations/plugins/{plugin_id}/versions`

List a Plugin's versions, newest first.

The first item of the first page is the version the Plugin's `latest_version_id`
refers to.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `pluginID string`

  ID of the Plugin (prefixed `plugin_`).

- `params BetaOrganizationPluginVersionListParams`

  - `Limit param.Field[int64] Optional`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    minimum: 1, maximum: 1000

  - `OrganizationID param.Field[string] Optional`

    Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

  - `Page param.Field[string] Optional`

    Query param: Optionally set to the `next_page` token from the previous response.

    maxLength: 2048

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPluginVersion`

  - `Type PluginVersion`

    Always `plugin_version`.

    default: plugin_version

  - `ID string`

    The version's ID.

  - `Components []BetaPluginComponent`

    What the version contains; null when not enumerated.

    - `Type BetaPluginComponentType`

      The kind of component.

      - `const BetaPluginComponentTypeAgent BetaPluginComponentType = "agent"`

      - `const BetaPluginComponentTypeCli BetaPluginComponentType = "cli"`

      - `const BetaPluginComponentTypeCommand BetaPluginComponentType = "command"`

      - `const BetaPluginComponentTypeHook BetaPluginComponentType = "hook"`

      - `const BetaPluginComponentTypeMCPServer BetaPluginComponentType = "mcp_server"`

      - `const BetaPluginComponentTypeSkill BetaPluginComponentType = "skill"`

    - `Description string`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `Name string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `ContentScan BetaPluginContentScan`

    This version's content scan; null when it has not been scanned.

    - `Assessment BetaPluginContentScanAssessment`

      The scan's verdict; set only when `status` is `completed`.

      - `const BetaPluginContentScanAssessmentFail BetaPluginContentScanAssessment = "fail"`

      - `const BetaPluginContentScanAssessmentPass BetaPluginContentScanAssessment = "pass"`

      - `const BetaPluginContentScanAssessmentUnknown BetaPluginContentScanAssessment = "unknown"`

      - `const BetaPluginContentScanAssessmentWarn BetaPluginContentScanAssessment = "warn"`

    - `Reason string`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `Status BetaPluginContentScanStatus`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `const BetaPluginContentScanStatusCompleted BetaPluginContentScanStatus = "completed"`

      - `const BetaPluginContentScanStatusErrored BetaPluginContentScanStatus = "errored"`

      - `const BetaPluginContentScanStatusProcessing BetaPluginContentScanStatus = "processing"`

  - `CreatedAt Time`

    RFC 3339.

    format: date-time

  - `CreatedBy BetaPluginVersionCreatedByUnion`

    Who uploaded this version; null when not recorded.

    - `type BetaPluginUserActor`

      - `Type UserActor`

        A member of the organization.

        default: user_actor

      - `EmailAddress string`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `UserID string`

        The member's User ID.

    - `type BetaPluginAPIActor`

      - `Type APIActor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `APIKeyID string`

        The key's ID.

  - `Description string`

    The manifest's description; null when it declares none.

  - `DisplayName string`

    The manifest's display name; null when it declares none.

  - `ManifestVersion string`

    The version string the manifest declares; null when it declares none.

  - `PluginID string`

    The Plugin's ID.

  - `Reach BetaPluginVersionReach`

    How far the version reaches: `remote`, `privileged` or `contained`, as on the Plugin; null when not classifiable.

    - `const BetaPluginVersionReachContained BetaPluginVersionReach = "contained"`

    - `const BetaPluginVersionReachPrivileged BetaPluginVersionReach = "privileged"`

    - `const BetaPluginVersionReachRemote BetaPluginVersionReach = "remote"`

  - `ReleaseNotes string`

    As supplied with the upload; null when none were supplied.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Plugins.Versions.List(
		context.TODO(),
		"plugin_id",
		anthropic.BetaOrganizationPluginVersionListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
      "components": [
        {
          "description": "description",
          "name": "review-pr",
          "type": "skill"
        }
      ],
      "content_scan": {
        "assessment": "warn",
        "reason": "credential-exposure",
        "status": "completed"
      },
      "created_at": "2026-03-14T09:26:53.589793Z",
      "created_by": {
        "email_address": "user@example.com",
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "description": "Reviews pull requests against your team's conventions.",
      "display_name": "Code Review Helper",
      "manifest_version": "1.2.0",
      "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "reach": "contained",
      "release_notes": "Adds a review checklist for database migrations.",
      "type": "plugin_version"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

### Get Plugin Version

`client.Beta.Organization.Plugins.Versions.Get(ctx, version, params) (*BetaPluginVersion, error)`

**GET** `/v1/organizations/plugins/{plugin_id}/versions/{version}`

Retrieve one version of a Plugin by its ID, or the Plugin's newest version.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `version string`

  ID of the Plugin Version (prefixed `pluginver_`), or `latest` for the newest one.

- `params BetaOrganizationPluginVersionGetParams`

  - `PluginID param.Field[string]`

    Path param: ID of the Plugin (prefixed `plugin_`).

  - `OrganizationID param.Field[string] Optional`

    Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPluginVersion`

  - `Type PluginVersion`

    Always `plugin_version`.

    default: plugin_version

  - `ID string`

    The version's ID.

  - `Components []BetaPluginComponent`

    What the version contains; null when not enumerated.

    - `Type BetaPluginComponentType`

      The kind of component.

      - `const BetaPluginComponentTypeAgent BetaPluginComponentType = "agent"`

      - `const BetaPluginComponentTypeCli BetaPluginComponentType = "cli"`

      - `const BetaPluginComponentTypeCommand BetaPluginComponentType = "command"`

      - `const BetaPluginComponentTypeHook BetaPluginComponentType = "hook"`

      - `const BetaPluginComponentTypeMCPServer BetaPluginComponentType = "mcp_server"`

      - `const BetaPluginComponentTypeSkill BetaPluginComponentType = "skill"`

    - `Description string`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `Name string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `ContentScan BetaPluginContentScan`

    This version's content scan; null when it has not been scanned.

    - `Assessment BetaPluginContentScanAssessment`

      The scan's verdict; set only when `status` is `completed`.

      - `const BetaPluginContentScanAssessmentFail BetaPluginContentScanAssessment = "fail"`

      - `const BetaPluginContentScanAssessmentPass BetaPluginContentScanAssessment = "pass"`

      - `const BetaPluginContentScanAssessmentUnknown BetaPluginContentScanAssessment = "unknown"`

      - `const BetaPluginContentScanAssessmentWarn BetaPluginContentScanAssessment = "warn"`

    - `Reason string`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `Status BetaPluginContentScanStatus`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `const BetaPluginContentScanStatusCompleted BetaPluginContentScanStatus = "completed"`

      - `const BetaPluginContentScanStatusErrored BetaPluginContentScanStatus = "errored"`

      - `const BetaPluginContentScanStatusProcessing BetaPluginContentScanStatus = "processing"`

  - `CreatedAt Time`

    RFC 3339.

    format: date-time

  - `CreatedBy BetaPluginVersionCreatedByUnion`

    Who uploaded this version; null when not recorded.

    - `type BetaPluginUserActor`

      - `Type UserActor`

        A member of the organization.

        default: user_actor

      - `EmailAddress string`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `UserID string`

        The member's User ID.

    - `type BetaPluginAPIActor`

      - `Type APIActor`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

        default: api_actor

      - `APIKeyID string`

        The key's ID.

  - `Description string`

    The manifest's description; null when it declares none.

  - `DisplayName string`

    The manifest's display name; null when it declares none.

  - `ManifestVersion string`

    The version string the manifest declares; null when it declares none.

  - `PluginID string`

    The Plugin's ID.

  - `Reach BetaPluginVersionReach`

    How far the version reaches: `remote`, `privileged` or `contained`, as on the Plugin; null when not classifiable.

    - `const BetaPluginVersionReachContained BetaPluginVersionReach = "contained"`

    - `const BetaPluginVersionReachPrivileged BetaPluginVersionReach = "privileged"`

    - `const BetaPluginVersionReachRemote BetaPluginVersionReach = "remote"`

  - `ReleaseNotes string`

    As supplied with the upload; null when none were supplied.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaPluginVersion, err := client.Beta.Organization.Plugins.Versions.Get(
		context.TODO(),
		"version",
		anthropic.BetaOrganizationPluginVersionGetParams{
			PluginID: "plugin_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaPluginVersion.ID)
}
```

##### Response (200)

```json
{
  "id": "pluginver_01KaZmQpRsTuVwXyZ2b4c6d8",
  "components": [
    {
      "description": "description",
      "name": "review-pr",
      "type": "skill"
    }
  ],
  "content_scan": {
    "assessment": "warn",
    "reason": "credential-exposure",
    "status": "completed"
  },
  "created_at": "2026-03-14T09:26:53.589793Z",
  "created_by": {
    "email_address": "user@example.com",
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "description": "Reviews pull requests against your team's conventions.",
  "display_name": "Code Review Helper",
  "manifest_version": "1.2.0",
  "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "reach": "contained",
  "release_notes": "Adds a review checklist for database migrations.",
  "type": "plugin_version"
}
```

### Download Plugin Version Archive

`client.Beta.Organization.Plugins.Versions.Download(ctx, version, params) (*Response, error)`

**GET** `/v1/organizations/plugins/{plugin_id}/versions/{version}/content`

Download one version's `.zip` archive, exactly as stored. Each download of a
Plugin from a member's personal plugin marketplace is recorded on the Compliance API
activity feed.

The response body is the archive (`Content-Type: application/zip`), sent as an
attachment whose filename is derived from the Plugin's name; name saved files from
the IDs in the request path, since that filename is not unique.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every read scope above (`read:plugins`, `read:org_audit`, and
`read:compliance_org_data`) can download the files of plugins in members' personal
marketplaces, including files that claude.ai's admin settings do not show, and a
`read:org_audit` or `read:compliance_org_data` key created for all of your parent
organization's linked organizations can do this in any organization under it that has
access to this API, by passing `organization_id`. Each such download records a
`claude_plugin_archive_accessed` event on the Compliance API activity feed,
identifying the key, the plugin, the version, and the member. Downloads of
organization-owned plugins are not recorded.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `version string`

  ID of the Plugin Version (prefixed `pluginver_`). `latest` is not accepted here.

- `params BetaOrganizationPluginVersionDownloadParams`

  - `PluginID param.Field[string]`

    Path param: ID of the Plugin (prefixed `plugin_`).

  - `OrganizationID param.Field[string] Optional`

    Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaOrganizationPluginVersionDownloadResponse interface{…}`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	response, err := client.Beta.Organization.Plugins.Versions.Download(
		context.TODO(),
		"version",
		anthropic.BetaOrganizationPluginVersionDownloadParams{
			PluginID: "plugin_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", response)
}
```

## Beta › Organization › Plugins › Installation Settings

### List Plugin Installation Settings

`client.Beta.Organization.Plugins.InstallationSettings.List(ctx, pluginID, params) (*PageCursor[BetaPluginInstallationSetting], error)`

**GET** `/v1/organizations/plugins/{plugin_id}/installation_settings`

List an organization-owned Plugin's installation settings, which say which
members it is for, most recently created first.

The list holds the Plugin's own organization-wide setting (absent while the Plugin
inherits its marketplace's default) and each RBAC Group's own setting. A
member-owned Plugin has shares instead, so this path returns 404 for one.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `pluginID string`

  ID of the Plugin (prefixed `plugin_`).

- `params BetaOrganizationPluginInstallationSettingListParams`

  - `Limit param.Field[int64] Optional`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `100`.

    minimum: 1, maximum: 100

  - `OrganizationID param.Field[string] Optional`

    Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

  - `Page param.Field[string] Optional`

    Query param: Optionally set to the `next_page` token from the previous response.

    maxLength: 2048

  - `TargetType param.Field[BetaOrganizationPluginInstallationSettingListParamsTargetType] Optional`

    Query param: Only settings for this kind of target: `organization` (the organization-wide setting) or `rbac_group` (an RBAC Group's).

    - `const BetaOrganizationPluginInstallationSettingListParamsTargetTypeOrganization BetaOrganizationPluginInstallationSettingListParamsTargetType = "organization"`

    - `const BetaOrganizationPluginInstallationSettingListParamsTargetTypeRBACGroup BetaOrganizationPluginInstallationSettingListParamsTargetType = "rbac_group"`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPluginInstallationSetting`

  The installation setting an organization-owned Plugin holds for one
  target. It has no ID of its own: it is addressed by the Plugin's ID and the
  target.

  - `Type PluginInstallationSetting`

    Always `plugin_installation_setting`.

    default: plugin_installation_setting

  - `CreatedAt Time`

    When the target was first given a setting for this Plugin.

    format: date-time

  - `InstallationPreference BetaPluginInstallationSettingInstallationPreference`

    The setting the target holds for this Plugin. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `const BetaPluginInstallationSettingInstallationPreferenceAutoInstall BetaPluginInstallationSettingInstallationPreference = "auto_install"`

    - `const BetaPluginInstallationSettingInstallationPreferenceAvailable BetaPluginInstallationSettingInstallationPreference = "available"`

    - `const BetaPluginInstallationSettingInstallationPreferenceNotAvailable BetaPluginInstallationSettingInstallationPreference = "not_available"`

    - `const BetaPluginInstallationSettingInstallationPreferenceRequired BetaPluginInstallationSettingInstallationPreference = "required"`

  - `PluginID string`

    The Plugin's ID.

  - `Target BetaPluginInstallationSettingTargetUnion`

    Whose setting this is: `organization` (the Plugin's own organization-wide setting) or `rbac_group` (one RBAC Group's own setting); `organization_member` does not occur here.

    - `type BetaPluginTargetOrganization`

      - `Type Organization`

        Every member of the organization.

        default: organization

    - `type BetaPluginTargetRBACGroup`

      - `Type RBACGroup`

        An RBAC Group.

        default: rbac_group

      - `RBACGroupID string`

        The RBAC Group's ID.

    - `type BetaPluginTargetOrganizationMember`

      - `Type OrganizationMember`

        One member of the organization.

        default: organization_member

      - `UserID string`

        The member's User ID.

  - `UpdatedAt Time`

    When its setting last changed.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Plugins.InstallationSettings.List(
		context.TODO(),
		"plugin_id",
		anthropic.BetaOrganizationPluginInstallationSettingListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2026-03-14T09:26:53.589793Z",
      "installation_preference": "required",
      "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "target": {
        "type": "organization"
      },
      "type": "plugin_installation_setting",
      "updated_at": "2026-03-14T09:26:53.589793Z"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

### Set Plugin Installation Setting

`client.Beta.Organization.Plugins.InstallationSettings.Set(ctx, target, params) (*BetaPluginInstallationSetting, error)`

**POST** `/v1/organizations/plugins/{plugin_id}/installation_settings/{target}`

Set or change an organization-owned Plugin's installation setting for the whole
organization or for one RBAC Group.

Writing the value a target already holds of its own changes nothing.

A member-owned Plugin has shares instead of installation settings, so this path
returns 404 for one.

Send a Plugin's installation-setting writes one at a time. If several writes for the
same Plugin arrive at the same time, the server handles them one after another and
can answer some of them with `503` instead of applying them. That `503` carries
`x-should-retry: true`, and the write is safe to repeat: wait a second or two, then
send it again.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `target string`

  The target whose setting is written: the literal `organization` for the Plugin's organization-wide setting, or an RBAC Group's ID (prefixed `rbac_group_`) for that group's own setting. Writing the `organization` target stops the Plugin from inheriting its marketplace's default, even when the value written equals that default.

- `params BetaOrganizationPluginInstallationSettingSetParams`

  - `PluginID param.Field[string]`

    Path param: ID of the Plugin (prefixed `plugin_`).

  - `InstallationPreference param.Field[BetaOrganizationPluginInstallationSettingSetParamsInstallationPreference]`

    Body param: The installation setting the target is to hold for this Plugin: one of `required`, `auto_install`, `available`, `not_available`.

    - `const BetaOrganizationPluginInstallationSettingSetParamsInstallationPreferenceAutoInstall BetaOrganizationPluginInstallationSettingSetParamsInstallationPreference = "auto_install"`

    - `const BetaOrganizationPluginInstallationSettingSetParamsInstallationPreferenceAvailable BetaOrganizationPluginInstallationSettingSetParamsInstallationPreference = "available"`

    - `const BetaOrganizationPluginInstallationSettingSetParamsInstallationPreferenceNotAvailable BetaOrganizationPluginInstallationSettingSetParamsInstallationPreference = "not_available"`

    - `const BetaOrganizationPluginInstallationSettingSetParamsInstallationPreferenceRequired BetaOrganizationPluginInstallationSettingSetParamsInstallationPreference = "required"`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPluginInstallationSetting`

  The installation setting an organization-owned Plugin holds for one
  target. It has no ID of its own: it is addressed by the Plugin's ID and the
  target.

  - `Type PluginInstallationSetting`

    Always `plugin_installation_setting`.

    default: plugin_installation_setting

  - `CreatedAt Time`

    When the target was first given a setting for this Plugin.

    format: date-time

  - `InstallationPreference BetaPluginInstallationSettingInstallationPreference`

    The setting the target holds for this Plugin. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `const BetaPluginInstallationSettingInstallationPreferenceAutoInstall BetaPluginInstallationSettingInstallationPreference = "auto_install"`

    - `const BetaPluginInstallationSettingInstallationPreferenceAvailable BetaPluginInstallationSettingInstallationPreference = "available"`

    - `const BetaPluginInstallationSettingInstallationPreferenceNotAvailable BetaPluginInstallationSettingInstallationPreference = "not_available"`

    - `const BetaPluginInstallationSettingInstallationPreferenceRequired BetaPluginInstallationSettingInstallationPreference = "required"`

  - `PluginID string`

    The Plugin's ID.

  - `Target BetaPluginInstallationSettingTargetUnion`

    Whose setting this is: `organization` (the Plugin's own organization-wide setting) or `rbac_group` (one RBAC Group's own setting); `organization_member` does not occur here.

    - `type BetaPluginTargetOrganization`

      - `Type Organization`

        Every member of the organization.

        default: organization

    - `type BetaPluginTargetRBACGroup`

      - `Type RBACGroup`

        An RBAC Group.

        default: rbac_group

      - `RBACGroupID string`

        The RBAC Group's ID.

    - `type BetaPluginTargetOrganizationMember`

      - `Type OrganizationMember`

        One member of the organization.

        default: organization_member

      - `UserID string`

        The member's User ID.

  - `UpdatedAt Time`

    When its setting last changed.

    format: date-time

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaPluginInstallationSetting, err := client.Beta.Organization.Plugins.InstallationSettings.Set(
		context.TODO(),
		"target",
		anthropic.BetaOrganizationPluginInstallationSettingSetParams{
			PluginID:               "plugin_id",
			InstallationPreference: anthropic.BetaOrganizationPluginInstallationSettingSetParamsInstallationPreferenceRequired,
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaPluginInstallationSetting.PluginID)
}
```

##### Response (200)

```json
{
  "created_at": "2026-03-14T09:26:53.589793Z",
  "installation_preference": "required",
  "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "target": {
    "type": "organization"
  },
  "type": "plugin_installation_setting",
  "updated_at": "2026-03-14T09:26:53.589793Z"
}
```

### Remove Plugin Installation Setting

`client.Beta.Organization.Plugins.InstallationSettings.Remove(ctx, target, params) (*BetaDeletedPluginInstallationSetting, error)`

**DELETE** `/v1/organizations/plugins/{plugin_id}/installation_settings/{target}`

Remove an organization-owned Plugin's own installation setting for the whole
organization or for one RBAC Group.

Removing the `organization` target returns the Plugin to its marketplace's default
installation setting and leaves the groups' settings in place. Removing a group's
setting makes the group's members fall back to the Plugin's organization-wide setting
or to the settings of their other groups.

A target that holds no setting of its own returns 404 (a Plugin that already inherits
its marketplace's default holds no `organization` setting), and so does a member-owned
Plugin.

A removal counts as one of the Plugin's installation-setting writes: send all of those
writes one at a time. If several arrive for the same Plugin at the same time, the server
handles them one after another and can answer some of them with `503` and
`x-should-retry: true` instead of applying them; wait a second or two and send the
removal again. A `404` on the repeat means the setting is already gone.

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `target string`

  The target whose own setting is removed: the literal `organization` for the Plugin's organization-wide setting, or an RBAC Group's ID (prefixed `rbac_group_`) for that group's own setting. Removing the `organization` setting returns the Plugin to its marketplace's default.

- `params BetaOrganizationPluginInstallationSettingRemoveParams`

  - `PluginID param.Field[string]`

    Path param: ID of the Plugin (prefixed `plugin_`).

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaDeletedPluginInstallationSetting`

  Confirmation that one target's installation setting was removed, naming
  the Plugin and the target in place of an ID.

  - `Type PluginInstallationSettingDeleted`

    Always `plugin_installation_setting_deleted`.

    default: plugin_installation_setting_deleted

  - `PluginID string`

    The Plugin's ID.

  - `Target BetaDeletedPluginInstallationSettingTargetUnion`

    Whose setting was removed.

    - `type BetaPluginTargetOrganization`

      - `Type Organization`

        Every member of the organization.

        default: organization

    - `type BetaPluginTargetRBACGroup`

      - `Type RBACGroup`

        An RBAC Group.

        default: rbac_group

      - `RBACGroupID string`

        The RBAC Group's ID.

    - `type BetaPluginTargetOrganizationMember`

      - `Type OrganizationMember`

        One member of the organization.

        default: organization_member

      - `UserID string`

        The member's User ID.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaDeletedPluginInstallationSetting, err := client.Beta.Organization.Plugins.InstallationSettings.Remove(
		context.TODO(),
		"target",
		anthropic.BetaOrganizationPluginInstallationSettingRemoveParams{
			PluginID: "plugin_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaDeletedPluginInstallationSetting.PluginID)
}
```

##### Response (200)

```json
{
  "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
  "target": {
    "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
    "type": "rbac_group"
  },
  "type": "plugin_installation_setting_deleted"
}
```

## Beta › Organization › Plugins › Shares

### List Plugin Shares

`client.Beta.Organization.Plugins.Shares.List(ctx, pluginID, params) (*PageCursor[BetaPluginShare], error)`

**GET** `/v1/organizations/plugins/{plugin_id}/shares`

List the shares the owner of a member-owned Plugin has given — to every member of
the organization, to an RBAC Group, or to one member — most recently granted first.

Shares are read-only in this API: members give and withdraw them in claude.ai, and
who gave a share is recorded on the Compliance API activity feed rather than on the
share. An organization-owned Plugin has installation settings instead, so this path
returns 404 for one.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `pluginID string`

  ID of the Plugin (prefixed `plugin_`).

- `params BetaOrganizationPluginShareListParams`

  - `Limit param.Field[int64] Optional`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `100`.

    minimum: 1, maximum: 100

  - `OrganizationID param.Field[string] Optional`

    Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

  - `Page param.Field[string] Optional`

    Query param: Optionally set to the `next_page` token from the previous response.

    maxLength: 2048

  - `TargetType param.Field[BetaOrganizationPluginShareListParamsTargetType] Optional`

    Query param: Only shares with this kind of target: `organization` (every member), `rbac_group` (one RBAC Group), or `organization_member` (one member).

    - `const BetaOrganizationPluginShareListParamsTargetTypeOrganization BetaOrganizationPluginShareListParamsTargetType = "organization"`

    - `const BetaOrganizationPluginShareListParamsTargetTypeOrganizationMember BetaOrganizationPluginShareListParamsTargetType = "organization_member"`

    - `const BetaOrganizationPluginShareListParamsTargetTypeRBACGroup BetaOrganizationPluginShareListParamsTargetType = "rbac_group"`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPluginShare`

  One share the owner of a member-owned Plugin has given. Shares are
  read-only in this API and have no ID of their own; who gave a share is
  recorded on the Compliance API activity feed, not here.

  - `Type PluginShare`

    Always `plugin_share`.

    default: plugin_share

  - `GrantedAt Time`

    When the share was given; a share whose role is later changed in claude.ai is re-granted and carries the time of that change.

    format: date-time

  - `PluginID string`

    The Plugin's ID.

  - `Target BetaPluginShareTargetUnion`

    Who the Plugin is shared with: `organization` (every member), `rbac_group` (one RBAC Group), or `organization_member` (one member).

    - `type BetaPluginTargetOrganization`

      - `Type Organization`

        Every member of the organization.

        default: organization

    - `type BetaPluginTargetRBACGroup`

      - `Type RBACGroup`

        An RBAC Group.

        default: rbac_group

      - `RBACGroupID string`

        The RBAC Group's ID.

    - `type BetaPluginTargetOrganizationMember`

      - `Type OrganizationMember`

        One member of the organization.

        default: organization_member

      - `UserID string`

        The member's User ID.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.Plugins.Shares.List(
		context.TODO(),
		"plugin_id",
		anthropic.BetaOrganizationPluginShareListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "granted_at": "2026-03-14T09:26:53.589793Z",
      "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "target": {
        "type": "organization"
      },
      "type": "plugin_share"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

## Beta › Organization › Plugin Marketplaces

### List Plugin Marketplaces

`client.Beta.Organization.PluginMarketplaces.List(ctx, params) (*PageCursor[BetaPluginMarketplace], error)`

**GET** `/v1/organizations/plugin_marketplaces`

List the plugin marketplaces Plugins live in, newest first: the organization's own
and its members' personal ones.

Plugin marketplaces are created, connected to a repository and deleted in
claude.ai, not through this API. The organization's library marketplace, the
organization-owned `manual` marketplace that uploads go to when no marketplace is
named, is created the first time something is put in it and is listed from then on.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `params BetaOrganizationPluginMarketplaceListParams`

  - `Limit param.Field[int64] Optional`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    minimum: 1, maximum: 1000

  - `OrganizationID param.Field[string] Optional`

    Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

  - `OwnerType param.Field[BetaOrganizationPluginMarketplaceListParamsOwnerType] Optional`

    Query param: `organization` for the organization's plugin marketplaces, `user` for members' personal plugin marketplaces.

    - `const BetaOrganizationPluginMarketplaceListParamsOwnerTypeOrganization BetaOrganizationPluginMarketplaceListParamsOwnerType = "organization"`

    - `const BetaOrganizationPluginMarketplaceListParamsOwnerTypeUser BetaOrganizationPluginMarketplaceListParamsOwnerType = "user"`

  - `Page param.Field[string] Optional`

    Query param: Optionally set to the `next_page` token from the previous response.

    maxLength: 2048

  - `Source param.Field[BetaOrganizationPluginMarketplaceListParamsSource] Optional`

    Query param: Only plugin marketplaces with this `source`: `manual` for those whose Plugins are uploaded; `github`, `gitlab` or `public_git` for those synchronized from a Git repository. `directory` (Anthropic's catalog) is never listed here.

    - `const BetaOrganizationPluginMarketplaceListParamsSourceDirectory BetaOrganizationPluginMarketplaceListParamsSource = "directory"`

    - `const BetaOrganizationPluginMarketplaceListParamsSourceGitHub BetaOrganizationPluginMarketplaceListParamsSource = "github"`

    - `const BetaOrganizationPluginMarketplaceListParamsSourceGitlab BetaOrganizationPluginMarketplaceListParamsSource = "gitlab"`

    - `const BetaOrganizationPluginMarketplaceListParamsSourceManual BetaOrganizationPluginMarketplaceListParamsSource = "manual"`

    - `const BetaOrganizationPluginMarketplaceListParamsSourcePublicGit BetaOrganizationPluginMarketplaceListParamsSource = "public_git"`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPluginMarketplace`

  - `Type PluginMarketplace`

    Always `plugin_marketplace`.

    default: plugin_marketplace

  - `ID string`

    The plugin marketplace's ID, prefixed `marketplace_`.

  - `CreatedAt Time`

    RFC 3339.

    format: date-time

  - `DefaultInstallationPreference BetaPluginMarketplaceDefaultInstallationPreference`

    Organization plugin marketplace: the organization-wide setting every Plugin in it with no setting of its own gets. Null for a member's personal plugin marketplace. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `const BetaPluginMarketplaceDefaultInstallationPreferenceAutoInstall BetaPluginMarketplaceDefaultInstallationPreference = "auto_install"`

    - `const BetaPluginMarketplaceDefaultInstallationPreferenceAvailable BetaPluginMarketplaceDefaultInstallationPreference = "available"`

    - `const BetaPluginMarketplaceDefaultInstallationPreferenceNotAvailable BetaPluginMarketplaceDefaultInstallationPreference = "not_available"`

    - `const BetaPluginMarketplaceDefaultInstallationPreferenceRequired BetaPluginMarketplaceDefaultInstallationPreference = "required"`

  - `LastSyncEndedAt Time`

    RFC 3339. When the most recent synchronization attempt to finish did so, whatever its outcome; for a repository plugin marketplace no synchronization has run on yet, when it was created. Null for a plugin marketplace that is not synchronized from a repository.

    format: date-time

  - `LastSyncReadSha string`

    The commit the last synchronization attempt that reached the repository read, whether or not its content was then accepted (see `sync_status`); an attempt that ends `failed_auth` or `failed_transient` leaves it unchanged. Null until an attempt has first read the repository, and for a plugin marketplace that is not synchronized from a repository.

  - `Name string`

    Fixed for the plugin marketplace's lifetime.

  - `Owner BetaPluginMarketplaceOwnerUnion`

    The organization, or the member whose personal plugin marketplace it is.

    - `type BetaPluginOwnerOrganization`

      - `Type Organization`

        The Plugin lives in a plugin marketplace the organization owns.

        default: organization

    - `type BetaPluginOwnerUser`

      - `Type User`

        The Plugin lives in one member's personal plugin marketplace.

        default: user

      - `UserID string`

        The member's User ID.

  - `Source BetaPluginMarketplaceSource`

    Where the plugin marketplace's Plugins come from: `manual` when they are uploaded; `github`, `gitlab` or `public_git` when they are synchronized from the Git repository the owner connected, into which nothing can be uploaded; `directory` is Anthropic's own catalog, which this API does not list. A value this API does not yet name is returned as stored.

    - `const BetaPluginMarketplaceSourceDirectory BetaPluginMarketplaceSource = "directory"`

    - `const BetaPluginMarketplaceSourceGitHub BetaPluginMarketplaceSource = "github"`

    - `const BetaPluginMarketplaceSourceGitlab BetaPluginMarketplaceSource = "gitlab"`

    - `const BetaPluginMarketplaceSourceManual BetaPluginMarketplaceSource = "manual"`

    - `const BetaPluginMarketplaceSourcePublicGit BetaPluginMarketplaceSource = "public_git"`

  - `SyncStatus BetaPluginMarketplaceSyncStatus`

    Outcome of the plugin marketplace's most recent synchronization: one of `success`, `in_progress`, `failed_content`, `failed_transient`, `failed_auth`, `failed_limits`; a value this API does not yet name is returned as stored. Null until a synchronization is first attempted — so always for a `manual` plugin marketplace.

    - `const BetaPluginMarketplaceSyncStatusFailedAuth BetaPluginMarketplaceSyncStatus = "failed_auth"`

    - `const BetaPluginMarketplaceSyncStatusFailedContent BetaPluginMarketplaceSyncStatus = "failed_content"`

    - `const BetaPluginMarketplaceSyncStatusFailedLimits BetaPluginMarketplaceSyncStatus = "failed_limits"`

    - `const BetaPluginMarketplaceSyncStatusFailedTransient BetaPluginMarketplaceSyncStatus = "failed_transient"`

    - `const BetaPluginMarketplaceSyncStatusInProgress BetaPluginMarketplaceSyncStatus = "in_progress"`

    - `const BetaPluginMarketplaceSyncStatusSuccess BetaPluginMarketplaceSyncStatus = "success"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Organization.PluginMarketplaces.List(context.TODO(), anthropic.BetaOrganizationPluginMarketplaceListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
      "created_at": "2026-03-14T09:26:53.589793Z",
      "default_installation_preference": "available",
      "last_sync_ended_at": "2026-03-14T09:26:53.589793Z",
      "last_sync_read_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
      "name": "engineering-tools",
      "owner": {
        "type": "organization"
      },
      "source": "github",
      "sync_status": "success",
      "type": "plugin_marketplace"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

### Get Plugin Marketplace

`client.Beta.Organization.PluginMarketplaces.Get(ctx, marketplaceID, params) (*BetaPluginMarketplace, error)`

**GET** `/v1/organizations/plugin_marketplaces/{marketplace_id}`

Retrieve a plugin marketplace by ID.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `marketplaceID string`

  ID of the plugin marketplace (prefixed `marketplace_`).

- `params BetaOrganizationPluginMarketplaceGetParams`

  - `OrganizationID param.Field[string] Optional`

    Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPluginMarketplace`

  - `Type PluginMarketplace`

    Always `plugin_marketplace`.

    default: plugin_marketplace

  - `ID string`

    The plugin marketplace's ID, prefixed `marketplace_`.

  - `CreatedAt Time`

    RFC 3339.

    format: date-time

  - `DefaultInstallationPreference BetaPluginMarketplaceDefaultInstallationPreference`

    Organization plugin marketplace: the organization-wide setting every Plugin in it with no setting of its own gets. Null for a member's personal plugin marketplace. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `const BetaPluginMarketplaceDefaultInstallationPreferenceAutoInstall BetaPluginMarketplaceDefaultInstallationPreference = "auto_install"`

    - `const BetaPluginMarketplaceDefaultInstallationPreferenceAvailable BetaPluginMarketplaceDefaultInstallationPreference = "available"`

    - `const BetaPluginMarketplaceDefaultInstallationPreferenceNotAvailable BetaPluginMarketplaceDefaultInstallationPreference = "not_available"`

    - `const BetaPluginMarketplaceDefaultInstallationPreferenceRequired BetaPluginMarketplaceDefaultInstallationPreference = "required"`

  - `LastSyncEndedAt Time`

    RFC 3339. When the most recent synchronization attempt to finish did so, whatever its outcome; for a repository plugin marketplace no synchronization has run on yet, when it was created. Null for a plugin marketplace that is not synchronized from a repository.

    format: date-time

  - `LastSyncReadSha string`

    The commit the last synchronization attempt that reached the repository read, whether or not its content was then accepted (see `sync_status`); an attempt that ends `failed_auth` or `failed_transient` leaves it unchanged. Null until an attempt has first read the repository, and for a plugin marketplace that is not synchronized from a repository.

  - `Name string`

    Fixed for the plugin marketplace's lifetime.

  - `Owner BetaPluginMarketplaceOwnerUnion`

    The organization, or the member whose personal plugin marketplace it is.

    - `type BetaPluginOwnerOrganization`

      - `Type Organization`

        The Plugin lives in a plugin marketplace the organization owns.

        default: organization

    - `type BetaPluginOwnerUser`

      - `Type User`

        The Plugin lives in one member's personal plugin marketplace.

        default: user

      - `UserID string`

        The member's User ID.

  - `Source BetaPluginMarketplaceSource`

    Where the plugin marketplace's Plugins come from: `manual` when they are uploaded; `github`, `gitlab` or `public_git` when they are synchronized from the Git repository the owner connected, into which nothing can be uploaded; `directory` is Anthropic's own catalog, which this API does not list. A value this API does not yet name is returned as stored.

    - `const BetaPluginMarketplaceSourceDirectory BetaPluginMarketplaceSource = "directory"`

    - `const BetaPluginMarketplaceSourceGitHub BetaPluginMarketplaceSource = "github"`

    - `const BetaPluginMarketplaceSourceGitlab BetaPluginMarketplaceSource = "gitlab"`

    - `const BetaPluginMarketplaceSourceManual BetaPluginMarketplaceSource = "manual"`

    - `const BetaPluginMarketplaceSourcePublicGit BetaPluginMarketplaceSource = "public_git"`

  - `SyncStatus BetaPluginMarketplaceSyncStatus`

    Outcome of the plugin marketplace's most recent synchronization: one of `success`, `in_progress`, `failed_content`, `failed_transient`, `failed_auth`, `failed_limits`; a value this API does not yet name is returned as stored. Null until a synchronization is first attempted — so always for a `manual` plugin marketplace.

    - `const BetaPluginMarketplaceSyncStatusFailedAuth BetaPluginMarketplaceSyncStatus = "failed_auth"`

    - `const BetaPluginMarketplaceSyncStatusFailedContent BetaPluginMarketplaceSyncStatus = "failed_content"`

    - `const BetaPluginMarketplaceSyncStatusFailedLimits BetaPluginMarketplaceSyncStatus = "failed_limits"`

    - `const BetaPluginMarketplaceSyncStatusFailedTransient BetaPluginMarketplaceSyncStatus = "failed_transient"`

    - `const BetaPluginMarketplaceSyncStatusInProgress BetaPluginMarketplaceSyncStatus = "in_progress"`

    - `const BetaPluginMarketplaceSyncStatusSuccess BetaPluginMarketplaceSyncStatus = "success"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaPluginMarketplace, err := client.Beta.Organization.PluginMarketplaces.Get(
		context.TODO(),
		"marketplace_id",
		anthropic.BetaOrganizationPluginMarketplaceGetParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaPluginMarketplace.ID)
}
```

##### Response (200)

```json
{
  "id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "created_at": "2026-03-14T09:26:53.589793Z",
  "default_installation_preference": "available",
  "last_sync_ended_at": "2026-03-14T09:26:53.589793Z",
  "last_sync_read_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
  "name": "engineering-tools",
  "owner": {
    "type": "organization"
  },
  "source": "github",
  "sync_status": "success",
  "type": "plugin_marketplace"
}
```

### Update Plugin Marketplace

`client.Beta.Organization.PluginMarketplaces.Update(ctx, marketplaceID, params) (*BetaPluginMarketplace, error)`

**POST** `/v1/organizations/plugin_marketplaces/{marketplace_id}`

Set the default installation setting of one of the organization's own plugin
marketplaces. Every Plugin in it without a setting of its own gets this default as
its organization-wide setting, including Plugins added later.

Pass it as `default_installation_preference`. A member's personal marketplace
cannot be updated here (403).

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `marketplaceID string`

  ID of the plugin marketplace (prefixed `marketplace_`).

- `params BetaOrganizationPluginMarketplaceUpdateParams`

  - `DefaultInstallationPreference param.Field[BetaOrganizationPluginMarketplaceUpdateParamsDefaultInstallationPreference]`

    Body param: The organization-wide installation setting every Plugin in the marketplace without one of its own gets: one of `required`, `auto_install`, `available`, `not_available`. Once set it can be changed but not removed.

    - `const BetaOrganizationPluginMarketplaceUpdateParamsDefaultInstallationPreferenceAutoInstall BetaOrganizationPluginMarketplaceUpdateParamsDefaultInstallationPreference = "auto_install"`

    - `const BetaOrganizationPluginMarketplaceUpdateParamsDefaultInstallationPreferenceAvailable BetaOrganizationPluginMarketplaceUpdateParamsDefaultInstallationPreference = "available"`

    - `const BetaOrganizationPluginMarketplaceUpdateParamsDefaultInstallationPreferenceNotAvailable BetaOrganizationPluginMarketplaceUpdateParamsDefaultInstallationPreference = "not_available"`

    - `const BetaOrganizationPluginMarketplaceUpdateParamsDefaultInstallationPreferenceRequired BetaOrganizationPluginMarketplaceUpdateParamsDefaultInstallationPreference = "required"`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPluginMarketplace`

  - `Type PluginMarketplace`

    Always `plugin_marketplace`.

    default: plugin_marketplace

  - `ID string`

    The plugin marketplace's ID, prefixed `marketplace_`.

  - `CreatedAt Time`

    RFC 3339.

    format: date-time

  - `DefaultInstallationPreference BetaPluginMarketplaceDefaultInstallationPreference`

    Organization plugin marketplace: the organization-wide setting every Plugin in it with no setting of its own gets. Null for a member's personal plugin marketplace. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `const BetaPluginMarketplaceDefaultInstallationPreferenceAutoInstall BetaPluginMarketplaceDefaultInstallationPreference = "auto_install"`

    - `const BetaPluginMarketplaceDefaultInstallationPreferenceAvailable BetaPluginMarketplaceDefaultInstallationPreference = "available"`

    - `const BetaPluginMarketplaceDefaultInstallationPreferenceNotAvailable BetaPluginMarketplaceDefaultInstallationPreference = "not_available"`

    - `const BetaPluginMarketplaceDefaultInstallationPreferenceRequired BetaPluginMarketplaceDefaultInstallationPreference = "required"`

  - `LastSyncEndedAt Time`

    RFC 3339. When the most recent synchronization attempt to finish did so, whatever its outcome; for a repository plugin marketplace no synchronization has run on yet, when it was created. Null for a plugin marketplace that is not synchronized from a repository.

    format: date-time

  - `LastSyncReadSha string`

    The commit the last synchronization attempt that reached the repository read, whether or not its content was then accepted (see `sync_status`); an attempt that ends `failed_auth` or `failed_transient` leaves it unchanged. Null until an attempt has first read the repository, and for a plugin marketplace that is not synchronized from a repository.

  - `Name string`

    Fixed for the plugin marketplace's lifetime.

  - `Owner BetaPluginMarketplaceOwnerUnion`

    The organization, or the member whose personal plugin marketplace it is.

    - `type BetaPluginOwnerOrganization`

      - `Type Organization`

        The Plugin lives in a plugin marketplace the organization owns.

        default: organization

    - `type BetaPluginOwnerUser`

      - `Type User`

        The Plugin lives in one member's personal plugin marketplace.

        default: user

      - `UserID string`

        The member's User ID.

  - `Source BetaPluginMarketplaceSource`

    Where the plugin marketplace's Plugins come from: `manual` when they are uploaded; `github`, `gitlab` or `public_git` when they are synchronized from the Git repository the owner connected, into which nothing can be uploaded; `directory` is Anthropic's own catalog, which this API does not list. A value this API does not yet name is returned as stored.

    - `const BetaPluginMarketplaceSourceDirectory BetaPluginMarketplaceSource = "directory"`

    - `const BetaPluginMarketplaceSourceGitHub BetaPluginMarketplaceSource = "github"`

    - `const BetaPluginMarketplaceSourceGitlab BetaPluginMarketplaceSource = "gitlab"`

    - `const BetaPluginMarketplaceSourceManual BetaPluginMarketplaceSource = "manual"`

    - `const BetaPluginMarketplaceSourcePublicGit BetaPluginMarketplaceSource = "public_git"`

  - `SyncStatus BetaPluginMarketplaceSyncStatus`

    Outcome of the plugin marketplace's most recent synchronization: one of `success`, `in_progress`, `failed_content`, `failed_transient`, `failed_auth`, `failed_limits`; a value this API does not yet name is returned as stored. Null until a synchronization is first attempted — so always for a `manual` plugin marketplace.

    - `const BetaPluginMarketplaceSyncStatusFailedAuth BetaPluginMarketplaceSyncStatus = "failed_auth"`

    - `const BetaPluginMarketplaceSyncStatusFailedContent BetaPluginMarketplaceSyncStatus = "failed_content"`

    - `const BetaPluginMarketplaceSyncStatusFailedLimits BetaPluginMarketplaceSyncStatus = "failed_limits"`

    - `const BetaPluginMarketplaceSyncStatusFailedTransient BetaPluginMarketplaceSyncStatus = "failed_transient"`

    - `const BetaPluginMarketplaceSyncStatusInProgress BetaPluginMarketplaceSyncStatus = "in_progress"`

    - `const BetaPluginMarketplaceSyncStatusSuccess BetaPluginMarketplaceSyncStatus = "success"`

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaPluginMarketplace, err := client.Beta.Organization.PluginMarketplaces.Update(
		context.TODO(),
		"marketplace_id",
		anthropic.BetaOrganizationPluginMarketplaceUpdateParams{
			DefaultInstallationPreference: anthropic.BetaOrganizationPluginMarketplaceUpdateParamsDefaultInstallationPreferenceAvailable,
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaPluginMarketplace.ID)
}
```

##### Response (200)

```json
{
  "id": "marketplace_01HxQ3v9KpZ2mTn8RwLc4Ys7",
  "created_at": "2026-03-14T09:26:53.589793Z",
  "default_installation_preference": "available",
  "last_sync_ended_at": "2026-03-14T09:26:53.589793Z",
  "last_sync_read_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
  "name": "engineering-tools",
  "owner": {
    "type": "organization"
  },
  "source": "github",
  "sync_status": "success",
  "type": "plugin_marketplace"
}
```

### Validate Plugin Marketplace Repository

`client.Beta.Organization.PluginMarketplaces.ValidateRepository(ctx, params) (*BetaPluginMarketplaceValidationReport, error)`

**POST** `/v1/organizations/plugin_marketplaces/validate_repository`

Check whether a plugin marketplace held in a public GitHub repository would
synchronize into claude.ai, without connecting or storing it.

To check a `.zip` of the marketplace directory instead, use Validate Plugin Marketplace Archive.

The report says whether `marketplace.json` is well-formed, which plugins a
synchronization would skip and why, and which plugins would synchronize only in
part, with some files left out. A repository that is missing, private, or has no such branch or commit is reported, not refused: the response is a report with `valid: false`. Plugin sources outside the marketplace
are fetched anonymously from GitHub, so a private one is reported as not found; a
source on any other host is not fetched here, and the report notes that it will be
checked when the marketplace actually synchronizes.

Nothing is recorded on the Compliance API activity feed.

For a worked example, see [Validate marketplace content](https://platform.claude.com/docs/en/manage-claude/plugins-api#validate-marketplace-content)
in the Plugins API guide.

**Accepted credentials:** an Admin API key with the `read:plugins` or `write:plugins` scope; `read:org_audit` and `read:compliance_org_data` do not grant it.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `params BetaOrganizationPluginMarketplaceValidateRepositoryParams`

  - `RepositoryURL param.Field[string]`

    Body param: The `https://` URL of a public repository on github.com that holds the marketplace. Any other host, a URL with credentials in it, or one that does not name a repository is a 400.

    minLength: 1

  - `Ref param.Field[string] Optional`

    Body param: The branch to validate the tip of, or the full 40-character SHA of the commit to validate. When omitted, the branch a synchronization would read (usually the repository's default branch); if that is not the default branch, the report's `ref` says which branch was read. An empty string, or a value that is neither a branch name nor a 40-character SHA, is a 400.

    minLength: 1

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPluginMarketplaceValidationReport`

  The outcome of validating plugin marketplace content: a report, not a
  stored object, so nothing in it can be retrieved afterwards.

  - `Type PluginMarketplaceValidationReport`

    Always `plugin_marketplace_validation_report`.

    default: plugin_marketplace_validation_report

  - `CommitSha string`

    The full SHA of the commit that was validated: for a repository, the commit that was read; for an uploaded archive, the commit recorded in the archive's comment (as a Git host's download writes it; not verified), else null.

  - `ManifestError string`

    Set when nothing could be validated: the repository or archive could not be read, or marketplace.json is missing, malformed or over a limit. Null otherwise.

  - `ManifestErrorCode string`

    A stable identifier for `manifest_error`; null when that is.

  - `PluginErrors []BetaPluginMarketplaceValidationPluginError`

    One entry per plugin a synchronization would skip entirely, keyed by the plugin's name in marketplace.json.

    - `Error string`

      Why the plugin would be skipped by a synchronization.

    - `ErrorCode string`

      A stable identifier for the reason — the value to branch on.

    - `Name string`

      The plugin's name, as its entry in marketplace.json declares it.

  - `PluginWarnings []BetaPluginMarketplaceValidationPluginWarnings`

    One entry per plugin that would synchronize with some of its contents left out, keyed by the plugin's name in marketplace.json.

    - `Name string`

      The plugin's name, as its entry in marketplace.json declares it.

    - `Warnings []BetaPluginMarketplaceValidationPluginWarning`

      The parts of the plugin a synchronization would leave out.

      - `ErrorCode string`

        A stable identifier for the kind of warning.

      - `Message string`

        What would be left out, and why.

  - `Ref string`

    For a repository, the branch that was read by name: the one requested, or else the branch a synchronization of this repository is set to read. Null when no branch is named or set and the repository's default branch was read, for a request by commit SHA, and for an uploaded archive.

  - `TotalPluginCount int64`

    How many plugins marketplace.json declares; 0 when it could not be read.

  - `Valid bool`

    True when marketplace.json is well-formed and no plugin would be skipped; warnings never make it false.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaPluginMarketplaceValidationReport, err := client.Beta.Organization.PluginMarketplaces.ValidateRepository(context.TODO(), anthropic.BetaOrganizationPluginMarketplaceValidateRepositoryParams{
		RepositoryURL: "https://github.com/example-org/example-marketplace",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaPluginMarketplaceValidationReport.Valid)
}
```

##### Response (200)

```json
{
  "commit_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
  "manifest_error": "manifest_error",
  "manifest_error_code": "marketplace_sync_manifest_not_found",
  "plugin_errors": [
    {
      "error": "error",
      "error_code": "marketplace_sync_plugin_missing_manifest",
      "name": "name"
    }
  ],
  "plugin_warnings": [
    {
      "name": "name",
      "warnings": [
        {
          "error_code": "marketplace_sync_zipball_symlink_dangling",
          "message": "message"
        }
      ]
    }
  ],
  "ref": "main",
  "total_plugin_count": 0,
  "type": "plugin_marketplace_validation_report",
  "valid": false
}
```

### Validate Plugin Marketplace Archive

`client.Beta.Organization.PluginMarketplaces.ValidateArchive(ctx, params) (*BetaPluginMarketplaceValidationReport, error)`

**POST** `/v1/organizations/plugin_marketplaces/validate_archive`

Check whether a plugin marketplace, uploaded as a `.zip` of the marketplace
directory, would synchronize into claude.ai, without connecting or storing it.

To check a public GitHub repository instead, use Validate Plugin Marketplace Repository.

The report says whether `marketplace.json` is well-formed, which plugins a
synchronization would skip and why, and which plugins would synchronize only in
part, with some files left out. An archive that cannot be read as a marketplace is reported, not refused: the response is a report with `valid: false`. Plugin sources outside the marketplace
are fetched anonymously from GitHub, so a private one is reported as not found; a
source on any other host is not fetched here, and the report notes that it will be
checked when the marketplace actually synchronizes.

Nothing is recorded on the Compliance API activity feed.

For a worked example, see [Validate marketplace content](https://platform.claude.com/docs/en/manage-claude/plugins-api#validate-marketplace-content)
in the Plugins API guide.

**Accepted credentials:** an Admin API key with the `read:plugins` or `write:plugins` scope; `read:org_audit` and `read:compliance_org_data` do not grant it.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `params BetaOrganizationPluginMarketplaceValidateArchiveParams`

  - `Archive param.Field[Reader]`

    Body param: A .zip of the marketplace directory (its contents at the root, or wrapped in one folder as a Git host's download produces), sent as a file part with a filename; DEFLATE- or STORE-compressed, at most 32 MB. A part sent without a filename, a second archive part, or any other form field is a 400; a larger archive is a 413.

    format: binary

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

    - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

    - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

    - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

    - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

    - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

    - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

    - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

    - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

    - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

    - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

    - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

    - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

    - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

    - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

    - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

    - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

    - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

    - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

    - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

    - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

    - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

    - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

    - `const AnthropicBetaUserProfiles2026_09_04 AnthropicBeta = "user-profiles-2026-09-04"`

    - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

    - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

    - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

    - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

    - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

    - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

    - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

    - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

    - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

    - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

    - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

    - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

    - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

    - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

    - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

    - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

    - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

    - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

    - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

    - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

    - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

    - `const AnthropicBetaCompact2026_09_04 AnthropicBeta = "compact-2026-09-04"`

    - `const AnthropicBetaInlineTools2026_09_15 AnthropicBeta = "inline-tools-2026-09-15"`

    - `const AnthropicBetaMCPClient2026_09_15 AnthropicBeta = "mcp-client-2026-09-15"`

    - `const AnthropicBetaCEPlugins2026_09_01 AnthropicBeta = "ce-plugins-2026-09-01"`

    - `const AnthropicBetaSpendLimitReads2026_09_26 AnthropicBeta = "spend-limit-reads-2026-09-26"`

#### Returns

- `type BetaPluginMarketplaceValidationReport`

  The outcome of validating plugin marketplace content: a report, not a
  stored object, so nothing in it can be retrieved afterwards.

  - `Type PluginMarketplaceValidationReport`

    Always `plugin_marketplace_validation_report`.

    default: plugin_marketplace_validation_report

  - `CommitSha string`

    The full SHA of the commit that was validated: for a repository, the commit that was read; for an uploaded archive, the commit recorded in the archive's comment (as a Git host's download writes it; not verified), else null.

  - `ManifestError string`

    Set when nothing could be validated: the repository or archive could not be read, or marketplace.json is missing, malformed or over a limit. Null otherwise.

  - `ManifestErrorCode string`

    A stable identifier for `manifest_error`; null when that is.

  - `PluginErrors []BetaPluginMarketplaceValidationPluginError`

    One entry per plugin a synchronization would skip entirely, keyed by the plugin's name in marketplace.json.

    - `Error string`

      Why the plugin would be skipped by a synchronization.

    - `ErrorCode string`

      A stable identifier for the reason — the value to branch on.

    - `Name string`

      The plugin's name, as its entry in marketplace.json declares it.

  - `PluginWarnings []BetaPluginMarketplaceValidationPluginWarnings`

    One entry per plugin that would synchronize with some of its contents left out, keyed by the plugin's name in marketplace.json.

    - `Name string`

      The plugin's name, as its entry in marketplace.json declares it.

    - `Warnings []BetaPluginMarketplaceValidationPluginWarning`

      The parts of the plugin a synchronization would leave out.

      - `ErrorCode string`

        A stable identifier for the kind of warning.

      - `Message string`

        What would be left out, and why.

  - `Ref string`

    For a repository, the branch that was read by name: the one requested, or else the branch a synchronization of this repository is set to read. Null when no branch is named or set and the repository's default branch was read, for a request by commit SHA, and for an uploaded archive.

  - `TotalPluginCount int64`

    How many plugins marketplace.json declares; 0 when it could not be read.

  - `Valid bool`

    True when marketplace.json is well-formed and no plugin would be skipped; warnings never make it false.

#### Example

```go
package main

import (
	"bytes"
	"context"
	"fmt"
	"io"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaPluginMarketplaceValidationReport, err := client.Beta.Organization.PluginMarketplaces.ValidateArchive(context.TODO(), anthropic.BetaOrganizationPluginMarketplaceValidateArchiveParams{
		Archive: io.Reader(bytes.NewBuffer([]byte("Example data"))),
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaPluginMarketplaceValidationReport.Valid)
}
```

##### Response (200)

```json
{
  "commit_sha": "9fceb02d0ae598e95dc970b74767f19372d61af8",
  "manifest_error": "manifest_error",
  "manifest_error_code": "marketplace_sync_manifest_not_found",
  "plugin_errors": [
    {
      "error": "error",
      "error_code": "marketplace_sync_plugin_missing_manifest",
      "name": "name"
    }
  ],
  "plugin_warnings": [
    {
      "name": "name",
      "warnings": [
        {
          "error_code": "marketplace_sync_zipball_symlink_dangling",
          "message": "message"
        }
      ]
    }
  ],
  "ref": "main",
  "total_plugin_count": 0,
  "type": "plugin_marketplace_validation_report",
  "valid": false
}
```
