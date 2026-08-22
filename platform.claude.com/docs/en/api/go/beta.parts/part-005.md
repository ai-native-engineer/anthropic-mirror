<!-- source: https://platform.claude.com/docs/en/api/go/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/go/beta -->

<!-- chunk-start -->

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

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

### Returns

- `type BetaSkillVersionDeleteResponse struct{…}`

  - `ID string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `Type string`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

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
	version, err := client.Beta.Skills.Versions.Delete(
		context.TODO(),
		"version",
		anthropic.BetaSkillVersionDeleteParams{
			SkillID: "skill_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", version.ID)
}
```

#### Response

```json
{
  "id": "1759178010641129",
  "type": "type"
}
```

# User Profiles

## Create User Profile

`client.Beta.UserProfiles.New(ctx, params) (*BetaUserProfile, error)`

**post** `/v1/user_profiles`

Create User Profile

### Parameters

- `params BetaUserProfileNewParams`

  - `AccessType param.Field[BetaUserProfileNewParamsAccessType]`

    Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `const BetaUserProfileNewParamsAccessTypeApplication BetaUserProfileNewParamsAccessType = "application"`

    - `const BetaUserProfileNewParamsAccessTypePassthrough BetaUserProfileNewParamsAccessType = "passthrough"`

  - `ExternalID param.Field[string]`

    Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

  - `Metadata param.Field[map[string, string]]`

    Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

  - `Name param.Field[string]`

    Body param: Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a resold-to company (`relationship` `resold` / `access_type` `passthrough`), that company's name where known. Maximum 255 characters.

  - `Relationship param.Field[BetaUserProfileNewParamsRelationship]`

    Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileNewParamsRelationshipExternal BetaUserProfileNewParamsRelationship = "external"`

    - `const BetaUserProfileNewParamsRelationshipResold BetaUserProfileNewParamsRelationship = "resold"`

    - `const BetaUserProfileNewParamsRelationshipInternal BetaUserProfileNewParamsRelationship = "internal"`

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaUserProfile struct{…}`

  - `ID string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants map[string, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status BetaUserProfileTrustGrantStatus`

      Status of the trust grant.

      - `const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"`

      - `const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"`

      - `const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"`

  - `Type BetaUserProfileType`

    Object type. Always `user_profile`.

    - `const BetaUserProfileTypeUserProfile BetaUserProfileType = "user_profile"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `AccessType BetaUserProfileAccessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `const BetaUserProfileAccessTypeApplication BetaUserProfileAccessType = "application"`

    - `const BetaUserProfileAccessTypePassthrough BetaUserProfileAccessType = "passthrough"`

  - `ExternalID string`

    Platform's own identifier for this user. Not enforced unique.

  - `Name string`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Relationship BetaUserProfileRelationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileRelationshipExternal BetaUserProfileRelationship = "external"`

    - `const BetaUserProfileRelationshipResold BetaUserProfileRelationship = "resold"`

    - `const BetaUserProfileRelationshipInternal BetaUserProfileRelationship = "internal"`

### Example

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
	betaUserProfile, err := client.Beta.UserProfiles.New(context.TODO(), anthropic.BetaUserProfileNewParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaUserProfile.ID)
}
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "access_type": "application",
  "external_id": "user_12345",
  "name": "Example User",
  "relationship": "external"
}
```

## List User Profiles

`client.Beta.UserProfiles.List(ctx, params) (*PageCursor[BetaUserProfile], error)`

**get** `/v1/user_profiles`

List User Profiles

### Parameters

- `params BetaUserProfileListParams`

  - `Limit param.Field[int64]`

    Query param: Query parameter for limit

  - `Order param.Field[BetaUserProfileListParamsOrder]`

    Query param: Query parameter for order

    - `const BetaUserProfileListParamsOrderAsc BetaUserProfileListParamsOrder = "asc"`

    - `const BetaUserProfileListParamsOrderDesc BetaUserProfileListParamsOrder = "desc"`

  - `Page param.Field[string]`

    Query param: Query parameter for page

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaUserProfile struct{…}`

  - `ID string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants map[string, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status BetaUserProfileTrustGrantStatus`

      Status of the trust grant.

      - `const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"`

      - `const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"`

      - `const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"`

  - `Type BetaUserProfileType`

    Object type. Always `user_profile`.

    - `const BetaUserProfileTypeUserProfile BetaUserProfileType = "user_profile"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `AccessType BetaUserProfileAccessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `const BetaUserProfileAccessTypeApplication BetaUserProfileAccessType = "application"`

    - `const BetaUserProfileAccessTypePassthrough BetaUserProfileAccessType = "passthrough"`

  - `ExternalID string`

    Platform's own identifier for this user. Not enforced unique.

  - `Name string`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Relationship BetaUserProfileRelationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileRelationshipExternal BetaUserProfileRelationship = "external"`

    - `const BetaUserProfileRelationshipResold BetaUserProfileRelationship = "resold"`

    - `const BetaUserProfileRelationshipInternal BetaUserProfileRelationship = "internal"`

### Example

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
	page, err := client.Beta.UserProfiles.List(context.TODO(), anthropic.BetaUserProfileListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
    {
      "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {},
      "trust_grants": {
        "cyber": {
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z",
      "access_type": "application",
      "external_id": "user_12345",
      "name": "Example User",
      "relationship": "external"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get User Profile

`client.Beta.UserProfiles.Get(ctx, userProfileID, query) (*BetaUserProfile, error)`

**get** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `userProfileID string`

- `query BetaUserProfileGetParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaUserProfile struct{…}`

  - `ID string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants map[string, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status BetaUserProfileTrustGrantStatus`

      Status of the trust grant.

      - `const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"`

      - `const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"`

      - `const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"`

  - `Type BetaUserProfileType`

    Object type. Always `user_profile`.

    - `const BetaUserProfileTypeUserProfile BetaUserProfileType = "user_profile"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `AccessType BetaUserProfileAccessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `const BetaUserProfileAccessTypeApplication BetaUserProfileAccessType = "application"`

    - `const BetaUserProfileAccessTypePassthrough BetaUserProfileAccessType = "passthrough"`

  - `ExternalID string`

    Platform's own identifier for this user. Not enforced unique.

  - `Name string`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Relationship BetaUserProfileRelationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileRelationshipExternal BetaUserProfileRelationship = "external"`

    - `const BetaUserProfileRelationshipResold BetaUserProfileRelationship = "resold"`

    - `const BetaUserProfileRelationshipInternal BetaUserProfileRelationship = "internal"`

### Example

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
	betaUserProfile, err := client.Beta.UserProfiles.Get(
		context.TODO(),
		"uprof_011CZkZCu8hGbp5mYRQgUmz9",
		anthropic.BetaUserProfileGetParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaUserProfile.ID)
}
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "access_type": "application",
  "external_id": "user_12345",
  "name": "Example User",
  "relationship": "external"
}
```

## Update User Profile

`client.Beta.UserProfiles.Update(ctx, userProfileID, params) (*BetaUserProfile, error)`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `userProfileID string`

- `params BetaUserProfileUpdateParams`

  - `AccessType param.Field[BetaUserProfileUpdateParamsAccessType]`

    Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `const BetaUserProfileUpdateParamsAccessTypeApplication BetaUserProfileUpdateParamsAccessType = "application"`

    - `const BetaUserProfileUpdateParamsAccessTypePassthrough BetaUserProfileUpdateParamsAccessType = "passthrough"`

  - `ExternalID param.Field[string]`

    Body param: If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

  - `Metadata param.Field[map[string, string]]`

    Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

  - `Name param.Field[string]`

    Body param: If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

  - `Relationship param.Field[BetaUserProfileUpdateParamsRelationship]`

    Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileUpdateParamsRelationshipExternal BetaUserProfileUpdateParamsRelationship = "external"`

    - `const BetaUserProfileUpdateParamsRelationshipResold BetaUserProfileUpdateParamsRelationship = "resold"`

    - `const BetaUserProfileUpdateParamsRelationshipInternal BetaUserProfileUpdateParamsRelationship = "internal"`

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaUserProfile struct{…}`

  - `ID string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants map[string, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status BetaUserProfileTrustGrantStatus`

      Status of the trust grant.

      - `const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"`

      - `const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"`

      - `const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"`

  - `Type BetaUserProfileType`

    Object type. Always `user_profile`.

    - `const BetaUserProfileTypeUserProfile BetaUserProfileType = "user_profile"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `AccessType BetaUserProfileAccessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `const BetaUserProfileAccessTypeApplication BetaUserProfileAccessType = "application"`

    - `const BetaUserProfileAccessTypePassthrough BetaUserProfileAccessType = "passthrough"`

  - `ExternalID string`

    Platform's own identifier for this user. Not enforced unique.

  - `Name string`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Relationship BetaUserProfileRelationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileRelationshipExternal BetaUserProfileRelationship = "external"`

    - `const BetaUserProfileRelationshipResold BetaUserProfileRelationship = "resold"`

    - `const BetaUserProfileRelationshipInternal BetaUserProfileRelationship = "internal"`

### Example

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
	betaUserProfile, err := client.Beta.UserProfiles.Update(
		context.TODO(),
		"uprof_011CZkZCu8hGbp5mYRQgUmz9",
		anthropic.BetaUserProfileUpdateParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaUserProfile.ID)
}
```

#### Response

```json
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "access_type": "application",
  "external_id": "user_12345",
  "name": "Example User",
  "relationship": "external"
}
```

## Create Enrollment URL

`client.Beta.UserProfiles.NewEnrollmentURL(ctx, userProfileID, body) (*BetaUserProfileEnrollmentURL, error)`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `userProfileID string`

- `body BetaUserProfileNewEnrollmentURLParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaUserProfileEnrollmentURL struct{…}`

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Type BetaUserProfileEnrollmentURLType`

    Object type. Always `enrollment_url`.

    - `const BetaUserProfileEnrollmentURLTypeEnrollmentURL BetaUserProfileEnrollmentURLType = "enrollment_url"`

  - `URL string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

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
	betaUserProfileEnrollmentURL, err := client.Beta.UserProfiles.NewEnrollmentURL(
		context.TODO(),
		"uprof_011CZkZCu8hGbp5mYRQgUmz9",
		anthropic.BetaUserProfileNewEnrollmentURLParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaUserProfileEnrollmentURL.ExpiresAt)
}
```

#### Response

```json
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

## Domain Types

### Beta User Profile

- `type BetaUserProfile struct{…}`

  - `ID string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `TrustGrants map[string, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status BetaUserProfileTrustGrantStatus`

      Status of the trust grant.

      - `const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"`

      - `const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"`

      - `const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"`

  - `Type BetaUserProfileType`

    Object type. Always `user_profile`.

    - `const BetaUserProfileTypeUserProfile BetaUserProfileType = "user_profile"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `AccessType BetaUserProfileAccessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `const BetaUserProfileAccessTypeApplication BetaUserProfileAccessType = "application"`

    - `const BetaUserProfileAccessTypePassthrough BetaUserProfileAccessType = "passthrough"`

  - `ExternalID string`

    Platform's own identifier for this user. Not enforced unique.

  - `Name string`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Relationship BetaUserProfileRelationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileRelationshipExternal BetaUserProfileRelationship = "external"`

    - `const BetaUserProfileRelationshipResold BetaUserProfileRelationship = "resold"`

    - `const BetaUserProfileRelationshipInternal BetaUserProfileRelationship = "internal"`

### Beta User Profile Enrollment URL

- `type BetaUserProfileEnrollmentURL struct{…}`

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Type BetaUserProfileEnrollmentURLType`

    Object type. Always `enrollment_url`.

    - `const BetaUserProfileEnrollmentURLTypeEnrollmentURL BetaUserProfileEnrollmentURLType = "enrollment_url"`

  - `URL string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `type BetaUserProfileTrustGrant struct{…}`

  - `Status BetaUserProfileTrustGrantStatus`

    Status of the trust grant.

    - `const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"`

    - `const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"`

    - `const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"`

# Dreams

## Create a Dream

`client.Beta.Dreams.New(ctx, params) (*BetaDream, error)`

**post** `/v1/dreams`

Create a Dream

### Parameters

- `params BetaDreamNewParams`

  - `Inputs param.Field[[]BetaDreamInputUnion]`

    Body param

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Model param.Field[BetaDreamNewParamsModelUnion]`

    Body param: Model identifier and configuration applied to every pipeline stage.

    - `string`

    - `type BetaDreamModelConfigParamResp struct{…}`

      Model identifier and configuration applied to every pipeline stage.

      - `ID string`

        Model identifier, e.g. "claude-opus-5". 1-256 characters.

      - `Speed BetaDreamModelConfigParamSpeed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaDreamModelConfigParamSpeedStandard BetaDreamModelConfigParamSpeed = "standard"`

        - `const BetaDreamModelConfigParamSpeedFast BetaDreamModelConfigParamSpeed = "fast"`

  - `Instructions param.Field[string]`

    Body param

  - `OutputBehavior param.Field[BetaOutputBehaviorUnion]`

    Body param: The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaDream struct{…}`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EndedAt Time`

    A timestamp in RFC 3339 format

  - `Error BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `Message string`

    - `Type string`

  - `Inputs []BetaDreamInputUnion`

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Instructions string`

  - `Model BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `ID string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed BetaDreamModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

      - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

  - `OutputBehavior BetaOutputBehaviorUnion`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type BetaOutputBehaviorCreateNew struct{…}`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type BetaOutputBehaviorCreateNewType`

        - `const BetaOutputBehaviorCreateNewTypeCreateNew BetaOutputBehaviorCreateNewType = "create_new"`

    - `type BetaOutputBehaviorUpdateExisting struct{…}`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `MemoryStoreID string`

      - `Type BetaOutputBehaviorUpdateExistingType`

        - `const BetaOutputBehaviorUpdateExistingTypeUpdateExisting BetaOutputBehaviorUpdateExistingType = "update_existing"`

  - `Outputs []BetaDreamOutput`

    - `MemoryStoreID string`

    - `Type BetaDreamOutputType`

      - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

  - `SessionID string`

  - `Status BetaDreamStatus`

    Lifecycle status of a Dream.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Type BetaDreamType`

    - `const BetaDreamTypeDream BetaDreamType = "dream"`

  - `Usage BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `CacheCreationInputTokens int64`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total uncached input tokens consumed across every pipeline stage.

    - `OutputTokens int64`

      Total output tokens generated across every pipeline stage.

### Example

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
	betaDream, err := client.Beta.Dreams.New(context.TODO(), anthropic.BetaDreamNewParams{
		Inputs: []anthropic.BetaDreamInputUnionParam{anthropic.BetaDreamInputUnionParam{
			OfMemoryStore: &anthropic.BetaDreamMemoryStoreInputParam{
				MemoryStoreID: "x",
				Type:          anthropic.BetaDreamMemoryStoreInputTypeMemoryStore,
			},
		}},
		Model: anthropic.BetaDreamNewParamsModelUnion{
			OfString: anthropic.String("string"),
		},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaDream.ID)
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## List Dreams

`client.Beta.Dreams.List(ctx, params) (*PageCursor[BetaDream], error)`

**get** `/v1/dreams`

List Dreams

### Parameters

- `params BetaDreamListParams`

  - `CreatedAtGt param.Field[Time]`

    Query param: Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

  - `CreatedAtLt param.Field[Time]`

    Query param: Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

  - `IncludeArchived param.Field[bool]`

    Query param: Query parameter for include_archived

  - `Limit param.Field[int64]`

    Query param: Query parameter for limit

  - `Page param.Field[string]`

    Query param: Query parameter for page

  - `Statuses param.Field[[]BetaDreamStatus]`

    Query param: Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaDream struct{…}`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EndedAt Time`

    A timestamp in RFC 3339 format

  - `Error BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `Message string`

    - `Type string`

  - `Inputs []BetaDreamInputUnion`

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Instructions string`

  - `Model BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `ID string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed BetaDreamModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

      - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

  - `OutputBehavior BetaOutputBehaviorUnion`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type BetaOutputBehaviorCreateNew struct{…}`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type BetaOutputBehaviorCreateNewType`

        - `const BetaOutputBehaviorCreateNewTypeCreateNew BetaOutputBehaviorCreateNewType = "create_new"`

    - `type BetaOutputBehaviorUpdateExisting struct{…}`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `MemoryStoreID string`

      - `Type BetaOutputBehaviorUpdateExistingType`

        - `const BetaOutputBehaviorUpdateExistingTypeUpdateExisting BetaOutputBehaviorUpdateExistingType = "update_existing"`

  - `Outputs []BetaDreamOutput`

    - `MemoryStoreID string`

    - `Type BetaDreamOutputType`

      - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

  - `SessionID string`

  - `Status BetaDreamStatus`

    Lifecycle status of a Dream.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Type BetaDreamType`

    - `const BetaDreamTypeDream BetaDreamType = "dream"`

  - `Usage BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `CacheCreationInputTokens int64`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total uncached input tokens consumed across every pipeline stage.

    - `OutputTokens int64`

      Total output tokens generated across every pipeline stage.

### Example

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
	page, err := client.Beta.Dreams.List(context.TODO(), anthropic.BetaDreamListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "ended_at": "2019-12-27T18:11:19.117Z",
      "error": {
        "message": "message",
        "type": "type"
      },
      "inputs": [
        {
          "memory_store_id": "x",
          "type": "memory_store"
        }
      ],
      "instructions": "instructions",
      "model": {
        "id": "x",
        "speed": "standard"
      },
      "output_behavior": {
        "type": "create_new"
      },
      "outputs": [
        {
          "memory_store_id": "memory_store_id",
          "type": "memory_store"
        }
      ],
      "session_id": "session_id",
      "status": "pending",
      "type": "dream",
      "usage": {
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
      }
    }
  ],
  "next_page": "next_page"
}
```

## Get a Dream

`client.Beta.Dreams.Get(ctx, dreamID, query) (*BetaDream, error)`

**get** `/v1/dreams/{dream_id}`

Get a Dream

### Parameters

- `dreamID string`

- `query BetaDreamGetParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaDream struct{…}`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EndedAt Time`

    A timestamp in RFC 3339 format

  - `Error BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `Message string`

    - `Type string`

  - `Inputs []BetaDreamInputUnion`

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Instructions string`

  - `Model BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `ID string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed BetaDreamModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

      - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

  - `OutputBehavior BetaOutputBehaviorUnion`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type BetaOutputBehaviorCreateNew struct{…}`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type BetaOutputBehaviorCreateNewType`

        - `const BetaOutputBehaviorCreateNewTypeCreateNew BetaOutputBehaviorCreateNewType = "create_new"`

    - `type BetaOutputBehaviorUpdateExisting struct{…}`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `MemoryStoreID string`

      - `Type BetaOutputBehaviorUpdateExistingType`

        - `const BetaOutputBehaviorUpdateExistingTypeUpdateExisting BetaOutputBehaviorUpdateExistingType = "update_existing"`

  - `Outputs []BetaDreamOutput`

    - `MemoryStoreID string`

    - `Type BetaDreamOutputType`

      - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

  - `SessionID string`

  - `Status BetaDreamStatus`

    Lifecycle status of a Dream.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Type BetaDreamType`

    - `const BetaDreamTypeDream BetaDreamType = "dream"`

  - `Usage BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `CacheCreationInputTokens int64`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total uncached input tokens consumed across every pipeline stage.

    - `OutputTokens int64`

      Total output tokens generated across every pipeline stage.

### Example

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
	betaDream, err := client.Beta.Dreams.Get(
		context.TODO(),
		"dream_id",
		anthropic.BetaDreamGetParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaDream.ID)
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Cancel a Dream

`client.Beta.Dreams.Cancel(ctx, dreamID, body) (*BetaDream, error)`

**post** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

### Parameters

- `dreamID string`

- `body BetaDreamCancelParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaDream struct{…}`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EndedAt Time`

    A timestamp in RFC 3339 format

  - `Error BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `Message string`

    - `Type string`

  - `Inputs []BetaDreamInputUnion`

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Instructions string`

  - `Model BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `ID string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed BetaDreamModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

      - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

  - `OutputBehavior BetaOutputBehaviorUnion`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type BetaOutputBehaviorCreateNew struct{…}`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type BetaOutputBehaviorCreateNewType`

        - `const BetaOutputBehaviorCreateNewTypeCreateNew BetaOutputBehaviorCreateNewType = "create_new"`

    - `type BetaOutputBehaviorUpdateExisting struct{…}`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `MemoryStoreID string`

      - `Type BetaOutputBehaviorUpdateExistingType`

        - `const BetaOutputBehaviorUpdateExistingTypeUpdateExisting BetaOutputBehaviorUpdateExistingType = "update_existing"`

  - `Outputs []BetaDreamOutput`

    - `MemoryStoreID string`

    - `Type BetaDreamOutputType`

      - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

  - `SessionID string`

  - `Status BetaDreamStatus`

    Lifecycle status of a Dream.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Type BetaDreamType`

    - `const BetaDreamTypeDream BetaDreamType = "dream"`

  - `Usage BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `CacheCreationInputTokens int64`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total uncached input tokens consumed across every pipeline stage.

    - `OutputTokens int64`

      Total output tokens generated across every pipeline stage.

### Example

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
	betaDream, err := client.Beta.Dreams.Cancel(
		context.TODO(),
		"dream_id",
		anthropic.BetaDreamCancelParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaDream.ID)
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Archive a Dream

`client.Beta.Dreams.Archive(ctx, dreamID, body) (*BetaDream, error)`

**post** `/v1/dreams/{dream_id}/archive`

Archive a Dream

### Parameters

- `dreamID string`

- `body BetaDreamArchiveParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaDream struct{…}`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EndedAt Time`

    A timestamp in RFC 3339 format

  - `Error BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `Message string`

    - `Type string`

  - `Inputs []BetaDreamInputUnion`

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Instructions string`

  - `Model BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `ID string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed BetaDreamModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

      - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

  - `OutputBehavior BetaOutputBehaviorUnion`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type BetaOutputBehaviorCreateNew struct{…}`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type BetaOutputBehaviorCreateNewType`

        - `const BetaOutputBehaviorCreateNewTypeCreateNew BetaOutputBehaviorCreateNewType = "create_new"`

    - `type BetaOutputBehaviorUpdateExisting struct{…}`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `MemoryStoreID string`

      - `Type BetaOutputBehaviorUpdateExistingType`

        - `const BetaOutputBehaviorUpdateExistingTypeUpdateExisting BetaOutputBehaviorUpdateExistingType = "update_existing"`

  - `Outputs []BetaDreamOutput`

    - `MemoryStoreID string`

    - `Type BetaDreamOutputType`

      - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

  - `SessionID string`

  - `Status BetaDreamStatus`

    Lifecycle status of a Dream.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Type BetaDreamType`

    - `const BetaDreamTypeDream BetaDreamType = "dream"`

  - `Usage BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `CacheCreationInputTokens int64`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total uncached input tokens consumed across every pipeline stage.

    - `OutputTokens int64`

      Total output tokens generated across every pipeline stage.

### Example

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
	betaDream, err := client.Beta.Dreams.Archive(
		context.TODO(),
		"dream_id",
		anthropic.BetaDreamArchiveParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaDream.ID)
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "ended_at": "2019-12-27T18:11:19.117Z",
  "error": {
    "message": "message",
    "type": "type"
  },
  "inputs": [
    {
      "memory_store_id": "x",
      "type": "memory_store"
    }
  ],
  "instructions": "instructions",
  "model": {
    "id": "x",
    "speed": "standard"
  },
  "output_behavior": {
    "type": "create_new"
  },
  "outputs": [
    {
      "memory_store_id": "memory_store_id",
      "type": "memory_store"
    }
  ],
  "session_id": "session_id",
  "status": "pending",
  "type": "dream",
  "usage": {
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "output_tokens": 0
  }
}
```

## Domain Types

### Beta Dream

- `type BetaDream struct{…}`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EndedAt Time`

    A timestamp in RFC 3339 format

  - `Error BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `Message string`

    - `Type string`

  - `Inputs []BetaDreamInputUnion`

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Instructions string`

  - `Model BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `ID string`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `Speed BetaDreamModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

      - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

  - `OutputBehavior BetaOutputBehaviorUnion`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type BetaOutputBehaviorCreateNew struct{…}`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type BetaOutputBehaviorCreateNewType`

        - `const BetaOutputBehaviorCreateNewTypeCreateNew BetaOutputBehaviorCreateNewType = "create_new"`

    - `type BetaOutputBehaviorUpdateExisting struct{…}`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `MemoryStoreID string`

      - `Type BetaOutputBehaviorUpdateExistingType`

        - `const BetaOutputBehaviorUpdateExistingTypeUpdateExisting BetaOutputBehaviorUpdateExistingType = "update_existing"`

  - `Outputs []BetaDreamOutput`

    - `MemoryStoreID string`

    - `Type BetaDreamOutputType`

      - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

  - `SessionID string`

  - `Status BetaDreamStatus`

    Lifecycle status of a Dream.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Type BetaDreamType`

    - `const BetaDreamTypeDream BetaDreamType = "dream"`

  - `Usage BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `CacheCreationInputTokens int64`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total uncached input tokens consumed across every pipeline stage.

    - `OutputTokens int64`

      Total output tokens generated across every pipeline stage.

### Beta Dream Error

- `type BetaDreamError struct{…}`

  Failure detail for a Dream whose `status` is `failed`.

  - `Message string`

  - `Type string`

### Beta Dream Input

- `type BetaDreamInputUnion interface{…}`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `type BetaDreamMemoryStoreInput struct{…}`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `MemoryStoreID string`

    - `Type BetaDreamMemoryStoreInputType`

      - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

  - `type BetaDreamSessionsInput struct{…}`

    Input session transcripts the dream reads.

    - `SessionIDs []string`

    - `Type BetaDreamSessionsInputType`

      - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

### Beta Dream Memory Store Input

- `type BetaDreamMemoryStoreInput struct{…}`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `MemoryStoreID string`

  - `Type BetaDreamMemoryStoreInputType`

    - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

### Beta Dream Memory Store Output

- `type BetaDreamMemoryStoreOutput struct{…}`

  An output memory store the dream writes consolidated memories into.

  - `MemoryStoreID string`

  - `Type BetaDreamMemoryStoreOutputType`

    - `const BetaDreamMemoryStoreOutputTypeMemoryStore BetaDreamMemoryStoreOutputType = "memory_store"`

### Beta Dream Model Config

- `type BetaDreamModelConfig struct{…}`

  Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

  - `ID string`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `Speed BetaDreamModelConfigSpeed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

    - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

### Beta Dream Model Config Param

- `type BetaDreamModelConfigParamResp struct{…}`

  Model identifier and configuration applied to every pipeline stage.

  - `ID string`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `Speed BetaDreamModelConfigParamSpeed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `const BetaDreamModelConfigParamSpeedStandard BetaDreamModelConfigParamSpeed = "standard"`

    - `const BetaDreamModelConfigParamSpeedFast BetaDreamModelConfigParamSpeed = "fast"`

### Beta Dream Output

- `type BetaDreamOutput struct{…}`

  An output memory store the dream writes consolidated memories into.

  - `MemoryStoreID string`

  - `Type BetaDreamOutputType`

    - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

### Beta Dream Sessions Input

- `type BetaDreamSessionsInput struct{…}`

  Input session transcripts the dream reads.

  - `SessionIDs []string`

  - `Type BetaDreamSessionsInputType`

    - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

### Beta Dream Status

- `type BetaDreamStatus string`

  Lifecycle status of a Dream.

  - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

  - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

  - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

  - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

  - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

### Beta Dream Usage

- `type BetaDreamUsage struct{…}`

  Cumulative token usage for the dream across every pipeline stage.

  - `CacheCreationInputTokens int64`

    Total tokens used to create prompt-cache entries (sum of all TTL tiers).

  - `CacheReadInputTokens int64`

    Total tokens read from prompt cache.

  - `InputTokens int64`

    Total uncached input tokens consumed across every pipeline stage.

  - `OutputTokens int64`

    Total output tokens generated across every pipeline stage.

### Beta Output Behavior

- `type BetaOutputBehaviorUnion interface{…}`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `type BetaOutputBehaviorCreateNew struct{…}`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `Type BetaOutputBehaviorCreateNewType`

      - `const BetaOutputBehaviorCreateNewTypeCreateNew BetaOutputBehaviorCreateNewType = "create_new"`

  - `type BetaOutputBehaviorUpdateExisting struct{…}`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `MemoryStoreID string`

    - `Type BetaOutputBehaviorUpdateExistingType`

      - `const BetaOutputBehaviorUpdateExistingTypeUpdateExisting BetaOutputBehaviorUpdateExistingType = "update_existing"`

### Beta Output Behavior Create New

- `type BetaOutputBehaviorCreateNew struct{…}`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `Type BetaOutputBehaviorCreateNewType`

    - `const BetaOutputBehaviorCreateNewTypeCreateNew BetaOutputBehaviorCreateNewType = "create_new"`

### Beta Output Behavior Update Existing

- `type BetaOutputBehaviorUpdateExisting struct{…}`

  The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

  - `MemoryStoreID string`

  - `Type BetaOutputBehaviorUpdateExistingType`

    - `const BetaOutputBehaviorUpdateExistingTypeUpdateExisting BetaOutputBehaviorUpdateExistingType = "update_existing"`

# Tunnels

## Create Tunnel

`client.Beta.Tunnels.New(ctx, params) (*BetaTunnel, error)`

**post** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Parameters

- `params BetaTunnelNewParams`

  - `DisplayName param.Field[string]`

    Body param: Optional human-readable name for the tunnel (1-255 characters).

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaTunnel struct{…}`

  An MCP tunnel.

  - `ID string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `Domain string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `Type Tunnel`

    - `const TunnelTunnel Tunnel = "tunnel"`

### Example

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
	betaTunnel, err := client.Beta.Tunnels.New(context.TODO(), anthropic.BetaTunnelNewParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaTunnel.ID)
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

## Get Tunnel

`client.Beta.Tunnels.Get(ctx, tunnelID, query) (*BetaTunnel, error)`

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Parameters

- `tunnelID string`

- `query BetaTunnelGetParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaTunnel struct{…}`

  An MCP tunnel.

  - `ID string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `Domain string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `Type Tunnel`

    - `const TunnelTunnel Tunnel = "tunnel"`

### Example

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
	betaTunnel, err := client.Beta.Tunnels.Get(
		context.TODO(),
		"tunnel_id",
		anthropic.BetaTunnelGetParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaTunnel.ID)
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

## List Tunnels

`client.Beta.Tunnels.List(ctx, params) (*PageCursor[BetaTunnel], error)`

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Parameters

- `params BetaTunnelListParams`

  - `IncludeArchived param.Field[bool]`

    Query param: Whether to include archived tunnels in the results. Defaults to false.

  - `Limit param.Field[int64]`

    Query param: Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

  - `Page param.Field[string]`

    Query param: Opaque pagination cursor from a previous `list_tunnels` response.

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaTunnel struct{…}`

  An MCP tunnel.

  - `ID string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `Domain string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `Type Tunnel`

    - `const TunnelTunnel Tunnel = "tunnel"`

### Example

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
	page, err := client.Beta.Tunnels.List(context.TODO(), anthropic.BetaTunnelListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "display_name": "display_name",
      "domain": "domain",
      "type": "tunnel"
    }
  ],
  "next_page": "next_page"
}
```

## Archive Tunnel

`client.Beta.Tunnels.Archive(ctx, tunnelID, body) (*BetaTunnel, error)`

**post** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Parameters

- `tunnelID string`

- `body BetaTunnelArchiveParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaTunnel struct{…}`

  An MCP tunnel.

  - `ID string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `Domain string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `Type Tunnel`

    - `const TunnelTunnel Tunnel = "tunnel"`

### Example

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
	betaTunnel, err := client.Beta.Tunnels.Archive(
		context.TODO(),
		"tunnel_id",
		anthropic.BetaTunnelArchiveParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaTunnel.ID)
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

## Reveal Tunnel Token

`client.Beta.Tunnels.RevealToken(ctx, tunnelID, body) (*BetaTunnelToken, error)`

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `tunnelID string`

- `body BetaTunnelRevealTokenParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaTunnelToken struct{…}`

  A tunnel's connector token.

  - `ID string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `TunnelToken string`

    The connector token used to run the tunnel. Treat as a credential.

  - `Type TunnelToken`

    - `const TunnelTokenTunnelToken TunnelToken = "tunnel_token"`

### Example

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
	betaTunnelToken, err := client.Beta.Tunnels.RevealToken(
		context.TODO(),
		"tunnel_id",
		anthropic.BetaTunnelRevealTokenParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaTunnelToken.ID)
}
```

#### Response

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

## Rotate Tunnel Token

`client.Beta.Tunnels.RotateToken(ctx, tunnelID, params) (*BetaTunnelToken, error)`

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `tunnelID string`

- `params BetaTunnelRotateTokenParams`

  - `Reason param.Field[string]`

    Body param: Optional free-text reason for the rotation, recorded for audit.

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaTunnelToken struct{…}`

  A tunnel's connector token.

  - `ID string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `TunnelToken string`

    The connector token used to run the tunnel. Treat as a credential.

  - `Type TunnelToken`

    - `const TunnelTokenTunnelToken TunnelToken = "tunnel_token"`

### Example

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
	betaTunnelToken, err := client.Beta.Tunnels.RotateToken(
		context.TODO(),
		"tunnel_id",
		anthropic.BetaTunnelRotateTokenParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaTunnelToken.ID)
}
```

#### Response

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

## Domain Types

### Beta Tunnel

- `type BetaTunnel struct{…}`

  An MCP tunnel.

  - `ID string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `Domain string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `Type Tunnel`

    - `const TunnelTunnel Tunnel = "tunnel"`

### Beta Tunnel Token

- `type BetaTunnelToken struct{…}`

  A tunnel's connector token.

  - `ID string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `TunnelToken string`

    The connector token used to run the tunnel. Treat as a credential.

  - `Type TunnelToken`

    - `const TunnelTokenTunnelToken TunnelToken = "tunnel_token"`

# Certificates

## Create Tunnel Certificate

`client.Beta.Tunnels.Certificates.New(ctx, tunnelID, params) (*BetaTunnelCertificate, error)`

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `tunnelID string`

- `params BetaTunnelCertificateNewParams`

  - `CaCertificatePem param.Field[string]`

    Body param: PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaTunnelCertificate struct{…}`

  A CA certificate attached to a tunnel.

  - `ID string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Fingerprint string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `TunnelID string`

    ID of the tunnel the certificate is registered against.

  - `Type TunnelCertificate`

    - `const TunnelCertificateTunnelCertificate TunnelCertificate = "tunnel_certificate"`

### Example

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
	betaTunnelCertificate, err := client.Beta.Tunnels.Certificates.New(
		context.TODO(),
		"tunnel_id",
		anthropic.BetaTunnelCertificateNewParams{
			CaCertificatePem: "ca_certificate_pem",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaTunnelCertificate.ID)
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

## Get Tunnel Certificate

`client.Beta.Tunnels.Certificates.Get(ctx, certificateID, params) (*BetaTunnelCertificate, error)`

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `certificateID string`

- `params BetaTunnelCertificateGetParams`

  - `TunnelID param.Field[string]`

    Path param: Path parameter tunnel_id

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaTunnelCertificate struct{…}`

  A CA certificate attached to a tunnel.

  - `ID string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Fingerprint string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `TunnelID string`

    ID of the tunnel the certificate is registered against.

  - `Type TunnelCertificate`

    - `const TunnelCertificateTunnelCertificate TunnelCertificate = "tunnel_certificate"`

### Example

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
	betaTunnelCertificate, err := client.Beta.Tunnels.Certificates.Get(
		context.TODO(),
		"certificate_id",
		anthropic.BetaTunnelCertificateGetParams{
			TunnelID: "tunnel_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaTunnelCertificate.ID)
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

## List Tunnel Certificates

`client.Beta.Tunnels.Certificates.List(ctx, tunnelID, params) (*PageCursor[BetaTunnelCertificate], error)`

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `tunnelID string`

- `params BetaTunnelCertificateListParams`

  - `IncludeArchived param.Field[bool]`

    Query param: Whether to include archived certificates in the results. Defaults to false.

  - `Limit param.Field[int64]`

    Query param: Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

  - `Page param.Field[string]`

    Query param: Opaque pagination cursor from a previous `list_tunnel_certificates` response.

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaTunnelCertificate struct{…}`

  A CA certificate attached to a tunnel.

  - `ID string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Fingerprint string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `TunnelID string`

    ID of the tunnel the certificate is registered against.

  - `Type TunnelCertificate`

    - `const TunnelCertificateTunnelCertificate TunnelCertificate = "tunnel_certificate"`

### Example

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
	page, err := client.Beta.Tunnels.Certificates.List(
		context.TODO(),
		"tunnel_id",
		anthropic.BetaTunnelCertificateListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "expires_at": "2019-12-27T18:11:19.117Z",
      "fingerprint": "fingerprint",
      "tunnel_id": "tunnel_id",
      "type": "tunnel_certificate"
    }
  ],
  "next_page": "next_page"
}
```

## Archive Tunnel Certificate

`client.Beta.Tunnels.Certificates.Archive(ctx, certificateID, params) (*BetaTunnelCertificate, error)`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `certificateID string`

- `params BetaTunnelCertificateArchiveParams`

  - `TunnelID param.Field[string]`

    Path param: Path parameter tunnel_id

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaTunnelCertificate struct{…}`

  A CA certificate attached to a tunnel.

  - `ID string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Fingerprint string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `TunnelID string`

    ID of the tunnel the certificate is registered against.

  - `Type TunnelCertificate`

    - `const TunnelCertificateTunnelCertificate TunnelCertificate = "tunnel_certificate"`

### Example

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
	betaTunnelCertificate, err := client.Beta.Tunnels.Certificates.Archive(
		context.TODO(),
		"certificate_id",
		anthropic.BetaTunnelCertificateArchiveParams{
			TunnelID: "tunnel_id",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaTunnelCertificate.ID)
}
```

#### Response

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

## Domain Types

### Beta Tunnel Certificate

- `type BetaTunnelCertificate struct{…}`

  A CA certificate attached to a tunnel.

  - `ID string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Fingerprint string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `TunnelID string`

    ID of the tunnel the certificate is registered against.

  - `Type TunnelCertificate`

    - `const TunnelCertificateTunnelCertificate TunnelCertificate = "tunnel_certificate"`

# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `type BetaWebhookAgentArchivedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentArchived`

    - `const AgentArchivedAgentArchived AgentArchived = "agent.archived"`

  - `WorkspaceID string`

### Beta Webhook Agent Created Event Data

- `type BetaWebhookAgentCreatedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentCreated`

    - `const AgentCreatedAgentCreated AgentCreated = "agent.created"`

  - `WorkspaceID string`

### Beta Webhook Agent Deleted Event Data

- `type BetaWebhookAgentDeletedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentDeleted`

    - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

  - `WorkspaceID string`

### Beta Webhook Agent Updated Event Data

- `type BetaWebhookAgentUpdatedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentUpdated`

    - `const AgentUpdatedAgentUpdated AgentUpdated = "agent.updated"`

  - `WorkspaceID string`

### Beta Webhook Deployment Archived Event Data

- `type BetaWebhookDeploymentArchivedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentArchived`

    - `const DeploymentArchivedDeploymentArchived DeploymentArchived = "deployment.archived"`

  - `WorkspaceID string`

### Beta Webhook Deployment Created Event Data

- `type BetaWebhookDeploymentCreatedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentCreated`

    - `const DeploymentCreatedDeploymentCreated DeploymentCreated = "deployment.created"`

  - `WorkspaceID string`

### Beta Webhook Deployment Deleted Event Data

- `type BetaWebhookDeploymentDeletedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentDeleted`

    - `const DeploymentDeletedDeploymentDeleted DeploymentDeleted = "deployment.deleted"`

  - `WorkspaceID string`

### Beta Webhook Deployment Paused Event Data

- `type BetaWebhookDeploymentPausedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentPaused`

    - `const DeploymentPausedDeploymentPaused DeploymentPaused = "deployment.paused"`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Failed Event Data

- `type BetaWebhookDeploymentRunFailedEventData struct{…}`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentRunFailed`

    - `const DeploymentRunFailedDeploymentRunFailed DeploymentRunFailed = "deployment_run.failed"`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Started Event Data

- `type BetaWebhookDeploymentRunStartedEventData struct{…}`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentRunStarted`

    - `const DeploymentRunStartedDeploymentRunStarted DeploymentRunStarted = "deployment_run.started"`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Succeeded Event Data

- `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentRunSucceeded`

    - `const DeploymentRunSucceededDeploymentRunSucceeded DeploymentRunSucceeded = "deployment_run.succeeded"`

  - `WorkspaceID string`

### Beta Webhook Deployment Unpaused Event Data

- `type BetaWebhookDeploymentUnpausedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentUnpaused`

    - `const DeploymentUnpausedDeploymentUnpaused DeploymentUnpaused = "deployment.unpaused"`

  - `WorkspaceID string`

### Beta Webhook Deployment Updated Event Data

- `type BetaWebhookDeploymentUpdatedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentUpdated`

    - `const DeploymentUpdatedDeploymentUpdated DeploymentUpdated = "deployment.updated"`

  - `WorkspaceID string`

### Beta Webhook Environment Archived Event Data

- `type BetaWebhookEnvironmentArchivedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentArchived`

    - `const EnvironmentArchivedEnvironmentArchived EnvironmentArchived = "environment.archived"`

  - `WorkspaceID string`

### Beta Webhook Environment Created Event Data

- `type BetaWebhookEnvironmentCreatedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentCreated`

    - `const EnvironmentCreatedEnvironmentCreated EnvironmentCreated = "environment.created"`

  - `WorkspaceID string`

### Beta Webhook Environment Deleted Event Data

- `type BetaWebhookEnvironmentDeletedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentDeleted`

    - `const EnvironmentDeletedEnvironmentDeleted EnvironmentDeleted = "environment.deleted"`

  - `WorkspaceID string`

### Beta Webhook Environment Updated Event Data

- `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentUpdated`

    - `const EnvironmentUpdatedEnvironmentUpdated EnvironmentUpdated = "environment.updated"`

  - `WorkspaceID string`

### Beta Webhook Event

- `type BetaWebhookEvent struct{…}`

  - `ID string`

    Unique event identifier for idempotency.

  - `CreatedAt Time`

    RFC 3339 timestamp when the event occurred.

  - `Data BetaWebhookEventDataUnion`

    - `type BetaWebhookSessionCreatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionCreated`

        - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionPendingEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionPending`

        - `const SessionPendingSessionPending SessionPending = "session.pending"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRunningEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRunning`

        - `const SessionRunningSessionRunning SessionRunning = "session.running"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionIdled`

        - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRequiresActionEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRequiresAction`

        - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionArchivedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionArchived`

        - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionDeletedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionDeleted`

        - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRescheduled`

        - `const SessionStatusRescheduledSessionStatusRescheduled SessionStatusRescheduled = "session.status_rescheduled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRunStarted`

        - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusIdled`

        - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusTerminated`

        - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadCreated`

        - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadIdled`

        - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadTerminated`

        - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionOutcomeEvaluationEnded`

        - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCreatedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultCreated`

        - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultArchivedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultArchived`

        - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultDeletedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultDeleted`

        - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialCreated`

        - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialArchived`

        - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialDeleted`

        - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialRefreshFailed`

        - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookSessionUpdatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionUpdated`

        - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentCreatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentCreated`

        - `const AgentCreatedAgentCreated AgentCreated = "agent.created"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentArchivedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentArchived`

        - `const AgentArchivedAgentArchived AgentArchived = "agent.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentDeletedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentDeleted`

        - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentPausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentPaused`

        - `const DeploymentPausedDeploymentPaused DeploymentPaused = "deployment.paused"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunFailedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunFailed`

        - `const DeploymentRunFailedDeploymentRunFailed DeploymentRunFailed = "deployment_run.failed"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentCreatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentCreated`

        - `const DeploymentCreatedDeploymentCreated DeploymentCreated = "deployment.created"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUpdatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUpdated`

        - `const DeploymentUpdatedDeploymentUpdated DeploymentUpdated = "deployment.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUnpausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUnpaused`

        - `const DeploymentUnpausedDeploymentUnpaused DeploymentUnpaused = "deployment.unpaused"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentUpdatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentUpdated`

        - `const AgentUpdatedAgentUpdated AgentUpdated = "agent.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentArchivedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentArchived`

        - `const DeploymentArchivedDeploymentArchived DeploymentArchived = "deployment.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunStartedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunStarted`

        - `const DeploymentRunStartedDeploymentRunStarted DeploymentRunStarted = "deployment_run.started"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentDeletedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentDeleted`

        - `const DeploymentDeletedDeploymentDeleted DeploymentDeleted = "deployment.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunSucceeded`

        - `const DeploymentRunSucceededDeploymentRunSucceeded DeploymentRunSucceeded = "deployment_run.succeeded"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentCreatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentCreated`

        - `const EnvironmentCreatedEnvironmentCreated EnvironmentCreated = "environment.created"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentUpdated`

        - `const EnvironmentUpdatedEnvironmentUpdated EnvironmentUpdated = "environment.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentArchivedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentArchived`

        - `const EnvironmentArchivedEnvironmentArchived EnvironmentArchived = "environment.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentDeletedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentDeleted`

        - `const EnvironmentDeletedEnvironmentDeleted EnvironmentDeleted = "environment.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreCreated`

        - `const MemoryStoreCreatedMemoryStoreCreated MemoryStoreCreated = "memory_store.created"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreArchived`

        - `const MemoryStoreArchivedMemoryStoreArchived MemoryStoreArchived = "memory_store.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreDeleted`

        - `const MemoryStoreDeletedMemoryStoreDeleted MemoryStoreDeleted = "memory_store.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionBudgetReachedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionBudgetReached`

        - `const SessionBudgetReachedSessionBudgetReached SessionBudgetReached = "session.budget_reached"`

      - `WorkspaceID string`

  - `Type Event`

    Object type. Always `event` for webhook payloads.

    - `const EventEvent Event = "event"`

### Beta Webhook Event Data

- `type BetaWebhookEventDataUnion interface{…}`

  - `type BetaWebhookSessionCreatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionCreated`

      - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionPendingEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionPending`

      - `const SessionPendingSessionPending SessionPending = "session.pending"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRunningEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionRunning`

      - `const SessionRunningSessionRunning SessionRunning = "session.running"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionIdledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionIdled`

      - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRequiresActionEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionRequiresAction`

      - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionArchivedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionArchived`

      - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionDeletedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionDeleted`

      - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusRescheduled`

      - `const SessionStatusRescheduledSessionStatusRescheduled SessionStatusRescheduled = "session.status_rescheduled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusRunStarted`

      - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusIdledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusIdled`

      - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusTerminated`

      - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `Type SessionThreadCreated`

      - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadIdledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `Type SessionThreadIdled`

      - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `Type SessionThreadTerminated`

      - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionOutcomeEvaluationEnded`

      - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCreatedEventData struct{…}`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `Type VaultCreated`

      - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultArchivedEventData struct{…}`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `Type VaultArchived`

      - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultDeletedEventData struct{…}`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `Type VaultDeleted`

      - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialCreated`

      - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialArchived`

      - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialDeleted`

      - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialRefreshFailed`

      - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookSessionUpdatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionUpdated`

      - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

    - `WorkspaceID string`

  - `type BetaWebhookAgentCreatedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentCreated`

      - `const AgentCreatedAgentCreated AgentCreated = "agent.created"`

    - `WorkspaceID string`

  - `type BetaWebhookAgentArchivedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentArchived`

      - `const AgentArchivedAgentArchived AgentArchived = "agent.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookAgentDeletedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentDeleted`

      - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentPausedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentPaused`

      - `const DeploymentPausedDeploymentPaused DeploymentPaused = "deployment.paused"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunFailedEventData struct{…}`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentRunFailed`

      - `const DeploymentRunFailedDeploymentRunFailed DeploymentRunFailed = "deployment_run.failed"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentCreatedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentCreated`

      - `const DeploymentCreatedDeploymentCreated DeploymentCreated = "deployment.created"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentUpdatedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentUpdated`

      - `const DeploymentUpdatedDeploymentUpdated DeploymentUpdated = "deployment.updated"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentUnpausedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentUnpaused`

      - `const DeploymentUnpausedDeploymentUnpaused DeploymentUnpaused = "deployment.unpaused"`

    - `WorkspaceID string`

  - `type BetaWebhookAgentUpdatedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentUpdated`

      - `const AgentUpdatedAgentUpdated AgentUpdated = "agent.updated"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentArchivedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentArchived`

      - `const DeploymentArchivedDeploymentArchived DeploymentArchived = "deployment.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunStartedEventData struct{…}`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentRunStarted`

      - `const DeploymentRunStartedDeploymentRunStarted DeploymentRunStarted = "deployment_run.started"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentDeletedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentDeleted`

      - `const DeploymentDeletedDeploymentDeleted DeploymentDeleted = "deployment.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentRunSucceeded`

      - `const DeploymentRunSucceededDeploymentRunSucceeded DeploymentRunSucceeded = "deployment_run.succeeded"`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentCreatedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentCreated`

      - `const EnvironmentCreatedEnvironmentCreated EnvironmentCreated = "environment.created"`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentUpdated`

      - `const EnvironmentUpdatedEnvironmentUpdated EnvironmentUpdated = "environment.updated"`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentArchivedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentArchived`

      - `const EnvironmentArchivedEnvironmentArchived EnvironmentArchived = "environment.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentDeletedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentDeleted`

      - `const EnvironmentDeletedEnvironmentDeleted EnvironmentDeleted = "environment.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `Type MemoryStoreCreated`

      - `const MemoryStoreCreatedMemoryStoreCreated MemoryStoreCreated = "memory_store.created"`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `Type MemoryStoreArchived`

      - `const MemoryStoreArchivedMemoryStoreArchived MemoryStoreArchived = "memory_store.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `Type MemoryStoreDeleted`

      - `const MemoryStoreDeletedMemoryStoreDeleted MemoryStoreDeleted = "memory_store.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionBudgetReachedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionBudgetReached`

      - `const SessionBudgetReachedSessionBudgetReached SessionBudgetReached = "session.budget_reached"`

    - `WorkspaceID string`

### Beta Webhook Memory Store Archived Event Data

- `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `Type MemoryStoreArchived`

    - `const MemoryStoreArchivedMemoryStoreArchived MemoryStoreArchived = "memory_store.archived"`

  - `WorkspaceID string`

### Beta Webhook Memory Store Created Event Data

- `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `Type MemoryStoreCreated`

    - `const MemoryStoreCreatedMemoryStoreCreated MemoryStoreCreated = "memory_store.created"`

  - `WorkspaceID string`

### Beta Webhook Memory Store Deleted Event Data

- `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `Type MemoryStoreDeleted`

    - `const MemoryStoreDeletedMemoryStoreDeleted MemoryStoreDeleted = "memory_store.deleted"`

  - `WorkspaceID string`

### Beta Webhook Session Archived Event Data

- `type BetaWebhookSessionArchivedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionArchived`

    - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

  - `WorkspaceID string`

### Beta Webhook Session Budget Reached Event Data

- `type BetaWebhookSessionBudgetReachedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionBudgetReached`

    - `const SessionBudgetReachedSessionBudgetReached SessionBudgetReached = "session.budget_reached"`

  - `WorkspaceID string`

### Beta Webhook Session Created Event Data

- `type BetaWebhookSessionCreatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionCreated`

    - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

  - `WorkspaceID string`

### Beta Webhook Session Deleted Event Data

- `type BetaWebhookSessionDeletedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionDeleted`

    - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

  - `WorkspaceID string`

### Beta Webhook Session Idled Event Data

- `type BetaWebhookSessionIdledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionIdled`

    - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

  - `WorkspaceID string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionOutcomeEvaluationEnded`

    - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

  - `WorkspaceID string`

### Beta Webhook Session Pending Event Data

- `type BetaWebhookSessionPendingEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionPending`

    - `const SessionPendingSessionPending SessionPending = "session.pending"`

  - `WorkspaceID string`

### Beta Webhook Session Requires Action Event Data

- `type BetaWebhookSessionRequiresActionEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionRequiresAction`

    - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

  - `WorkspaceID string`

### Beta Webhook Session Running Event Data

- `type BetaWebhookSessionRunningEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionRunning`

    - `const SessionRunningSessionRunning SessionRunning = "session.running"`

  - `WorkspaceID string`

### Beta Webhook Session Status Idled Event Data

- `type BetaWebhookSessionStatusIdledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusIdled`

    - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

  - `WorkspaceID string`

### Beta Webhook Session Status Rescheduled Event Data

- `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusRescheduled`

    - `const SessionStatusRescheduledSessionStatusRescheduled SessionStatusRescheduled = "session.status_rescheduled"`

  - `WorkspaceID string`

### Beta Webhook Session Status Run Started Event Data

- `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusRunStarted`

    - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

  - `WorkspaceID string`

### Beta Webhook Session Status Terminated Event Data

- `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusTerminated`

    - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

  - `WorkspaceID string`

### Beta Webhook Session Thread Created Event Data

- `type BetaWebhookSessionThreadCreatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `Type SessionThreadCreated`

    - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

  - `WorkspaceID string`

### Beta Webhook Session Thread Idled Event Data

- `type BetaWebhookSessionThreadIdledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `Type SessionThreadIdled`

    - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

  - `WorkspaceID string`

### Beta Webhook Session Thread Terminated Event Data

- `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `Type SessionThreadTerminated`

    - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

  - `WorkspaceID string`

### Beta Webhook Session Updated Event Data

- `type BetaWebhookSessionUpdatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionUpdated`

    - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

  - `WorkspaceID string`

### Beta Webhook Vault Archived Event Data

- `type BetaWebhookVaultArchivedEventData struct{…}`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `Type VaultArchived`

    - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

  - `WorkspaceID string`

### Beta Webhook Vault Created Event Data

- `type BetaWebhookVaultCreatedEventData struct{…}`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `Type VaultCreated`

    - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

  - `WorkspaceID string`

### Beta Webhook Vault Credential Archived Event Data

- `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialArchived`

    - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Created Event Data

- `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialCreated`

    - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Deleted Event Data

- `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialDeleted`

    - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialRefreshFailed`

    - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Deleted Event Data

- `type BetaWebhookVaultDeletedEventData struct{…}`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `Type VaultDeleted`

    - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

  - `WorkspaceID string`

### Unwrap Webhook Event

- `type UnwrapWebhookEvent struct{…}`

  - `ID string`

    Unique event identifier for idempotency.

  - `CreatedAt Time`

    RFC 3339 timestamp when the event occurred.

  - `Data BetaWebhookEventDataUnion`

    - `type BetaWebhookSessionCreatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionCreated`

        - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionPendingEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionPending`

        - `const SessionPendingSessionPending SessionPending = "session.pending"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRunningEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRunning`

        - `const SessionRunningSessionRunning SessionRunning = "session.running"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionIdled`

        - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRequiresActionEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRequiresAction`

        - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionArchivedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionArchived`

        - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionDeletedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionDeleted`

        - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRescheduled`

        - `const SessionStatusRescheduledSessionStatusRescheduled SessionStatusRescheduled = "session.status_rescheduled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRunStarted`

        - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusIdled`

        - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusTerminated`

        - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadCreated`

        - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadIdled`

        - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadTerminated`

        - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionOutcomeEvaluationEnded`

        - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCreatedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultCreated`

        - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultArchivedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultArchived`

        - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultDeletedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultDeleted`

        - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialCreated`

        - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialArchived`

        - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialDeleted`

        - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialRefreshFailed`

        - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookSessionUpdatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionUpdated`

        - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentCreatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentCreated`

        - `const AgentCreatedAgentCreated AgentCreated = "agent.created"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentArchivedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentArchived`

        - `const AgentArchivedAgentArchived AgentArchived = "agent.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentDeletedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentDeleted`

        - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentPausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentPaused`

        - `const DeploymentPausedDeploymentPaused DeploymentPaused = "deployment.paused"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunFailedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunFailed`

        - `const DeploymentRunFailedDeploymentRunFailed DeploymentRunFailed = "deployment_run.failed"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentCreatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentCreated`

        - `const DeploymentCreatedDeploymentCreated DeploymentCreated = "deployment.created"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUpdatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUpdated`

        - `const DeploymentUpdatedDeploymentUpdated DeploymentUpdated = "deployment.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUnpausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUnpaused`

        - `const DeploymentUnpausedDeploymentUnpaused DeploymentUnpaused = "deployment.unpaused"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentUpdatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentUpdated`

        - `const AgentUpdatedAgentUpdated AgentUpdated = "agent.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentArchivedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentArchived`

        - `const DeploymentArchivedDeploymentArchived DeploymentArchived = "deployment.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunStartedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunStarted`

        - `const DeploymentRunStartedDeploymentRunStarted DeploymentRunStarted = "deployment_run.started"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentDeletedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentDeleted`

        - `const DeploymentDeletedDeploymentDeleted DeploymentDeleted = "deployment.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunSucceeded`

        - `const DeploymentRunSucceededDeploymentRunSucceeded DeploymentRunSucceeded = "deployment_run.succeeded"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentCreatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentCreated`

        - `const EnvironmentCreatedEnvironmentCreated EnvironmentCreated = "environment.created"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentUpdated`

        - `const EnvironmentUpdatedEnvironmentUpdated EnvironmentUpdated = "environment.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentArchivedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentArchived`

        - `const EnvironmentArchivedEnvironmentArchived EnvironmentArchived = "environment.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentDeletedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentDeleted`

        - `const EnvironmentDeletedEnvironmentDeleted EnvironmentDeleted = "environment.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreCreated`

        - `const MemoryStoreCreatedMemoryStoreCreated MemoryStoreCreated = "memory_store.created"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreArchived`

        - `const MemoryStoreArchivedMemoryStoreArchived MemoryStoreArchived = "memory_store.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreDeleted`

        - `const MemoryStoreDeletedMemoryStoreDeleted MemoryStoreDeleted = "memory_store.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionBudgetReachedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionBudgetReached`

        - `const SessionBudgetReachedSessionBudgetReached SessionBudgetReached = "session.budget_reached"`

      - `WorkspaceID string`

  - `Type Event`

    Object type. Always `event` for webhook payloads.

    - `const EventEvent Event = "event"`
