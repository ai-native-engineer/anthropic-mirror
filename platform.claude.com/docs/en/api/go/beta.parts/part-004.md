<!-- source: https://platform.claude.com/docs/en/api/go/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/go/beta -->

<!-- chunk-start -->

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

    - `string`

    - `type AnthropicBeta string`

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

- `workspaceID string`

  ID of the workspace.

- `params BetaOrganizationWorkspaceServiceAccountAddParams`

  - `ServiceAccountID param.Field[string]`

    Body param: Tagged service account ID to add.

  - `WorkspaceRole param.Field[BetaNoBillingWorkspaceRole]`

    Body param: Role to assign to the service account in this workspace.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

    - `string`

    - `type AnthropicBeta string`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

    - `string`

    - `type AnthropicBeta string`

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

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

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

    - `string`

    - `type AnthropicBeta string`

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
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

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
