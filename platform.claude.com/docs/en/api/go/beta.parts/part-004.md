<!-- source: https://platform.claude.com/docs/en/api/go/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/go/beta -->

<!-- chunk-start -->

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
