<!-- source: https://platform.claude.com/docs/en/api/ruby/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/ruby/beta -->

<!-- chunk-start -->

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccount`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: :service_account`

  - `id: String`

    Tagged ID of the service account.

  - `archived_at: Time`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: Time`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: String`

    Optional free-text description.

  - `name: String`

    Admin-chosen slug identifier.

  - `organization_role: :admin | :developer`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `:admin`

    - `:developer`

  - `updated_at: Time`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account = anthropic.beta.organization.service_accounts.create(name: "ci-deploy-bot")

puts(beta_service_account)
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

`beta.organization.service_accounts.list(**kwargs) -> PageCursor<BetaServiceAccount>`

**GET** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List service accounts in the caller's organization.

Results are ordered by creation time, newest first. Use `limit` and the
`next_page` cursor to paginate; set `include_archived=true` to include
archived service accounts.

#### Parameters

- `include_archived: bool`

  Include archived resources. Defaults to false.

- `limit: Integer`

  Number of results per page.

  maximum: 100, minimum: 1

- `page: String`

  Opaque cursor from a previous response's `next_page`.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 42 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccount`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: :service_account`

  - `id: String`

    Tagged ID of the service account.

  - `archived_at: Time`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: Time`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: String`

    Optional free-text description.

  - `name: String`

    Admin-chosen slug identifier.

  - `organization_role: :admin | :developer`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `:admin`

    - `:developer`

  - `updated_at: Time`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.service_accounts.list

puts(page)
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

`beta.organization.service_accounts.retrieve(service_account_id, **kwargs) -> BetaServiceAccount`

**GET** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a service account by its ID (`svac_...`).

#### Parameters

- `service_account_id: String`

  ID of the service account.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 42 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccount`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: :service_account`

  - `id: String`

    Tagged ID of the service account.

  - `archived_at: Time`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: Time`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: String`

    Optional free-text description.

  - `name: String`

    Admin-chosen slug identifier.

  - `organization_role: :admin | :developer`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `:admin`

    - `:developer`

  - `updated_at: Time`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account = anthropic.beta.organization.service_accounts.retrieve("service_account_id")

puts(beta_service_account)
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

`beta.organization.service_accounts.update(service_account_id, **kwargs) -> BetaServiceAccount`

**POST** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Update a service account.

Only `description` and `organization_role` are mutable; `name` cannot be
changed. Archived service accounts cannot be updated; this returns 400.
Setting `organization_role` to `admin` (even when unchanged) requires an
interactive credential (a user OAuth token or a Console session).

#### Parameters

- `service_account_id: String`

  ID of the service account to update.

- `description: String`

  Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

  maxLength: 2000

- `organization_role: :admin | :developer`

  Replaces the org-level role. Omit or send `null` to leave unchanged.

  - `:admin`

  - `:developer`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 42 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccount`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: :service_account`

  - `id: String`

    Tagged ID of the service account.

  - `archived_at: Time`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: Time`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: String`

    Optional free-text description.

  - `name: String`

    Admin-chosen slug identifier.

  - `organization_role: :admin | :developer`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `:admin`

    - `:developer`

  - `updated_at: Time`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account = anthropic.beta.organization.service_accounts.update("service_account_id")

puts(beta_service_account)
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

`beta.organization.service_accounts.archive(service_account_id, **kwargs) -> BetaServiceAccount`

**POST** `/v1/organizations/service_accounts/{service_account_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a service account.

Idempotent; re-archiving returns the service account with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still targets this service account, same as issuer archival; archive
those rules first or change their target to another service account.

#### Parameters

- `service_account_id: String`

  ID of the service account to archive.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 42 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccount`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `type: :service_account`

  - `id: String`

    Tagged ID of the service account.

  - `archived_at: Time`

    If set, this service account is archived.

    format: date-time

  - `archived_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `created_at: Time`

    When this service account was created.

    format: date-time

  - `created_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `description: String`

    Optional free-text description.

  - `name: String`

    Admin-chosen slug identifier.

  - `organization_role: :admin | :developer`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `:admin`

    - `:developer`

  - `updated_at: Time`

    When this service account was last updated.

    format: date-time

  - `updated_by_actor_id: String`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account = anthropic.beta.organization.service_accounts.archive("service_account_id")

puts(beta_service_account)
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

`beta.organization.service_accounts.workspaces.add(service_account_id, **kwargs) -> BetaServiceAccountWorkspaceMember`

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

- `service_account_id: String`

  ID of the service account.

- `workspace_id: String`

  Tagged workspace ID to add the service account to.

- `workspace_role: BetaNoBillingWorkspaceRole`

  Role to assign to the service account in this workspace.

  - `:workspace_admin`

  - `:workspace_developer`

  - `:workspace_restricted_developer`

  - `:workspace_user`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 42 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccountWorkspaceMember`

  - `type: :service_account_workspace_member`

  - `created_by_actor_id: String`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: String`

    Tagged service account ID (`svac_...`).

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account_workspace_member = anthropic.beta.organization.service_accounts.workspaces.add(
  "service_account_id",
  workspace_id: "workspace_id",
  workspace_role: :workspace_admin
)

puts(beta_service_account_workspace_member)
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

`beta.organization.service_accounts.workspaces.list(service_account_id, **kwargs) -> PageCursor<BetaServiceAccountWorkspaceMember>`

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

- `service_account_id: String`

  ID of the service account.

- `limit: Integer`

  Number of results per page.

  maximum: 100, minimum: 1

- `page: String`

  Opaque cursor from a previous response's `next_page`.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 42 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccountWorkspaceMember`

  - `type: :service_account_workspace_member`

  - `created_by_actor_id: String`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: String`

    Tagged service account ID (`svac_...`).

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.service_accounts.workspaces.list("service_account_id")

puts(page)
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

`beta.organization.service_accounts.workspaces.remove(workspace_id, **kwargs) -> WorkspaceRemoveResponse`

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

- `service_account_id: String`

  ID of the service account.

- `workspace_id: String`

  ID of the workspace.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 42 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class WorkspaceRemoveResponse`

  - `type: :service_account_workspace_member_deleted`

  - `service_account_id: String`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

workspace = anthropic.beta.organization.service_accounts.workspaces.remove(
  "workspace_id",
  service_account_id: "service_account_id"
)

puts(workspace)
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

`beta.organization.users.list(**kwargs) -> Page<BetaOrganizationUser>`

**GET** `/v1/organizations/users`

List the organization's members.

#### Parameters

- `after_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `email: String`

  Filter by user email.

  format: email

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

- `roles: Array[String]`

  Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

  Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

#### Returns

- `class BetaOrganizationUser`

  - `type: :user`

    Object type.

    For Users, this is always `"user"`.

  - `id: String`

    ID of the User.

  - `added_at: Time`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: String`

    Email of the User.

  - `name: String`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `:admin`

    - `:billing`

    - `:claude_code_user`

    - `:developer`

    - `:managed`

    - `:membership_admin`

    - `:owner`

    - `:primary_owner`

    - `:user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.users.list

puts(page)
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

`beta.organization.users.retrieve(user_id) -> BetaOrganizationUser`

**GET** `/v1/organizations/users/{user_id}`

Retrieve a member of the organization by user ID.

#### Parameters

- `user_id: String`

  ID of the User.

#### Returns

- `class BetaOrganizationUser`

  - `type: :user`

    Object type.

    For Users, this is always `"user"`.

  - `id: String`

    ID of the User.

  - `added_at: Time`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: String`

    Email of the User.

  - `name: String`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `:admin`

    - `:billing`

    - `:claude_code_user`

    - `:developer`

    - `:managed`

    - `:membership_admin`

    - `:owner`

    - `:primary_owner`

    - `:user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_organization_user = anthropic.beta.organization.users.retrieve("user_id")

puts(beta_organization_user)
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

`beta.organization.users.update(user_id, **kwargs) -> BetaOrganizationUser`

**POST** `/v1/organizations/users/{user_id}`

Update a member's organization role.

#### Parameters

- `user_id: String`

  ID of the User.

- `role: :billing | :claude_code_user | :developer | 2 more`

  New role for the User.

  The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

  - `:billing`

  - `:claude_code_user`

  - `:developer`

  - `:managed`

  - `:user`

#### Returns

- `class BetaOrganizationUser`

  - `type: :user`

    Object type.

    For Users, this is always `"user"`.

  - `id: String`

    ID of the User.

  - `added_at: Time`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `email: String`

    Email of the User.

  - `name: String`

    Name of the User.

  - `role: BetaOrganizationRole`

    Organization role of the User.

    - `:admin`

    - `:billing`

    - `:claude_code_user`

    - `:developer`

    - `:managed`

    - `:membership_admin`

    - `:owner`

    - `:primary_owner`

    - `:user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_organization_user = anthropic.beta.organization.users.update("user_id", role: :user)

puts(beta_organization_user)
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

`beta.organization.users.remove(user_id) -> UserRemoveResponse`

**DELETE** `/v1/organizations/users/{user_id}`

Remove a member from the organization.

#### Parameters

- `user_id: String`

  ID of the User.

#### Returns

- `class UserRemoveResponse`

  - `type: :user_deleted`

    Deleted object type.

    For Users, this is always `"user_deleted"`.

  - `id: String`

    ID of the User.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

user = anthropic.beta.organization.users.remove("user_id")

puts(user)
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

`beta.organization.workspaces.list(**kwargs) -> Page<BetaWorkspace>`

**GET** `/v1/organizations/workspaces`

List Workspaces

#### Parameters

- `after_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `include_archived: bool`

  Whether to include Workspaces that have been archived in the response

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

#### Returns

- `class BetaWorkspace`

  - `type: :workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `id: String`

    ID of the Workspace.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: String`

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

  - `created_at: Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Array[String] | :unrestricted`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = Array[String]`

      - `AllowedInferenceGeos = :unrestricted`

    - `default_inference_geo: String`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: String`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: String`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: String`

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

  - `name: String`

    Name of the Workspace.

  - `tags: Hash[Symbol, String]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.workspaces.list

puts(page)
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

`beta.organization.workspaces.create(**kwargs) -> BetaWorkspace`

**POST** `/v1/organizations/workspaces`

Create Workspace

#### Parameters

- `name: String`

  Name of the Workspace.

  maxLength: 40, minLength: 1

- `data_residency: BetaDataResidencyCreateConfig`

  Data residency configuration for the workspace. If omitted, defaults to `workspace_geo: "us"`, `allowed_inference_geos: "unrestricted"`, and `default_inference_geo: "global"`.

  - `allowed_inference_geos: Array[BetaAllowedInferenceGeo] | :unrestricted`

    Permitted inference geo values. Defaults to 'unrestricted' if omitted, which allows all geos. Use the string 'unrestricted' to allow all geos, or a list of specific geos.

    - `Geos = Array[BetaAllowedInferenceGeo]`

      - `:global`

      - `:us`

    - `AllowedInferenceGeos = :unrestricted`

  - `default_inference_geo: :global | :us`

    Default inference geo applied when requests omit the parameter. Defaults to 'global' if omitted. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

    - `:global`

    - `:us`

  - `workspace_geo: :us`

    Geographic region for workspace data storage. Immutable after creation. Defaults to 'us' if omitted.

- `display_color: String`

  Hex color code representing the Workspace in the Anthropic Console.

  maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

- `external_key_id: String`

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

- `tags: Hash[Symbol, String]`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 42 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaWorkspace`

  - `type: :workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `id: String`

    ID of the Workspace.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: String`

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

  - `created_at: Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Array[String] | :unrestricted`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = Array[String]`

      - `AllowedInferenceGeos = :unrestricted`

    - `default_inference_geo: String`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: String`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: String`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: String`

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

  - `name: String`

    Name of the Workspace.

  - `tags: Hash[Symbol, String]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace = anthropic.beta.organization.workspaces.create(name: "x")

puts(beta_workspace)
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

`beta.organization.workspaces.retrieve(workspace_id) -> BetaWorkspace`

**GET** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

#### Parameters

- `workspace_id: String`

  ID of the Workspace.

#### Returns

- `class BetaWorkspace`

  - `type: :workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `id: String`

    ID of the Workspace.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: String`

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

  - `created_at: Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Array[String] | :unrestricted`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = Array[String]`

      - `AllowedInferenceGeos = :unrestricted`

    - `default_inference_geo: String`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: String`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: String`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: String`

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

  - `name: String`

    Name of the Workspace.

  - `tags: Hash[Symbol, String]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace = anthropic.beta.organization.workspaces.retrieve("workspace_id")

puts(beta_workspace)
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

`beta.organization.workspaces.update(workspace_id, **kwargs) -> BetaWorkspace`

**POST** `/v1/organizations/workspaces/{workspace_id}`

Update Workspace

#### Parameters

- `workspace_id: String`

- `data_residency: BetaDataResidencyUpdateConfig`

  Data residency configuration for the workspace.

  - `allowed_inference_geos: Array[BetaAllowedInferenceGeo] | :unrestricted`

    Permitted inference geo values. Use 'unrestricted' to allow all geos, or a list of specific geos.

    - `Geos = Array[BetaAllowedInferenceGeo]`

      - `:global`

      - `:us`

    - `AllowedInferenceGeos = :unrestricted`

  - `default_inference_geo: :global | :us`

    Default inference geo applied when requests omit the parameter. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

    - `:global`

    - `:us`

- `display_color: String`

  Hex color code representing the Workspace in the Anthropic Console.

  maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

- `external_key_id: String`

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

- `name: String`

  Name of the Workspace.

  maxLength: 40, minLength: 1

- `tags: Hash[Symbol, String]`

  User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Returns

- `class BetaWorkspace`

  - `type: :workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `id: String`

    ID of the Workspace.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: String`

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

  - `created_at: Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Array[String] | :unrestricted`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = Array[String]`

      - `AllowedInferenceGeos = :unrestricted`

    - `default_inference_geo: String`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: String`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: String`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: String`

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

  - `name: String`

    Name of the Workspace.

  - `tags: Hash[Symbol, String]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace = anthropic.beta.organization.workspaces.update("workspace_id")

puts(beta_workspace)
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

`beta.organization.workspaces.archive(workspace_id) -> BetaWorkspace`

**POST** `/v1/organizations/workspaces/{workspace_id}/archive`

Archive Workspace

#### Parameters

- `workspace_id: String`

#### Returns

- `class BetaWorkspace`

  - `type: :workspace`

    Object type.

    For Workspaces, this is always `"workspace"`.

  - `id: String`

    ID of the Workspace.

  - `archived_at: Time`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `compartment_id: String`

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

  - `created_at: Time`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `data_residency: BetaDataResidency`

    Data residency configuration.

    - `allowed_inference_geos: Array[String] | :unrestricted`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `Geos = Array[String]`

      - `AllowedInferenceGeos = :unrestricted`

    - `default_inference_geo: String`

      Default inference geo applied when requests omit the parameter.

    - `workspace_geo: String`

      Geographic region for workspace data storage. Immutable after creation.

  - `display_color: String`

    Hex color code representing the Workspace in the Anthropic Console.

  - `external_key_id: String`

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

  - `name: String`

    Name of the Workspace.

  - `tags: Hash[Symbol, String]`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace = anthropic.beta.organization.workspaces.archive("workspace_id")

puts(beta_workspace)
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

`beta.organization.workspaces.rate_limits.list(workspace_id, **kwargs) -> PageCursor<BetaWorkspaceRateLimit>`

**GET** `/v1/organizations/workspaces/{workspace_id}/rate_limits`

List rate-limit overrides configured for a workspace.

Returns only the groups and limiter types that have a workspace-level
override. Groups without overrides inherit the organization limits and
are not listed; use `GET /v1/organizations/rate_limits` to see those.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `workspace_id: String`

  The ID of the workspace.

- `group_type: :batch | :files | :model_group | 3 more`

  Filter by group type.

  - `:batch`

  - `:files`

  - `:model_group`

  - `:skills`

  - `:token_count`

  - `:web_search`

- `limit: Integer`

  Maximum number of items to return per page. Ranges from `1` to `1000`.

  When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

  maximum: 1000, minimum: 1

- `page: String`

  Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaWorkspaceRateLimit`

  - `type: :workspace_rate_limit`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

  - `group_type: :batch | :files | :model_group | 3 more`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `:batch`

    - `:files`

    - `:model_group`

    - `:skills`

    - `:token_count`

    - `:web_search`

  - `limits: Array[BetaWorkspaceRateLimitValue]`

    The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

    - `type: String`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `org_limit: Integer`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `value: Integer`

      The workspace-level override value for this limiter type.

  - `models: Array[String]`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `rate_limit_id: String`

    The `id` of the RateLimit group this override applies to.

  - `workspace_id: String`

    ID of the Workspace this override applies to.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.workspaces.rate_limits.list("workspace_id")

puts(page)
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

`beta.organization.workspaces.members.list(workspace_id, **kwargs) -> Page<BetaWorkspaceMember>`

**GET** `/v1/organizations/workspaces/{workspace_id}/members`

List Workspace Members

#### Parameters

- `workspace_id: String`

  ID of the Workspace.

- `after_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `before_id: String`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit: Integer`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

#### Returns

- `class BetaWorkspaceMember`

  - `type: :workspace_member`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `user_id: String`

    ID of the User.

  - `workspace_id: String`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.workspaces.members.list("workspace_id")

puts(page)
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

`beta.organization.workspaces.members.add(workspace_id, **kwargs) -> BetaWorkspaceMember`

**POST** `/v1/organizations/workspaces/{workspace_id}/members`

Create Workspace Member

#### Parameters

- `workspace_id: String`

  ID of the Workspace.

- `user_id: String`

  ID of the User.

- `workspace_role: BetaNoBillingWorkspaceRole`

  Role of the new Workspace Member. Cannot be `workspace_billing`.

  - `:workspace_admin`

  - `:workspace_developer`

  - `:workspace_restricted_developer`

  - `:workspace_user`

#### Returns

- `class BetaWorkspaceMember`

  - `type: :workspace_member`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `user_id: String`

    ID of the User.

  - `workspace_id: String`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace_member = anthropic.beta.organization.workspaces.members.add(
  "workspace_id",
  user_id: "user_01WCz1FkmYMm4gnmykNKUu3Q",
  workspace_role: :workspace_admin
)

puts(beta_workspace_member)
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

`beta.organization.workspaces.members.retrieve(user_id, **kwargs) -> BetaWorkspaceMember`

**GET** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Get Workspace Member

#### Parameters

- `workspace_id: String`

  ID of the Workspace.

- `user_id: String`

  ID of the User.

#### Returns

- `class BetaWorkspaceMember`

  - `type: :workspace_member`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `user_id: String`

    ID of the User.

  - `workspace_id: String`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace_member = anthropic.beta.organization.workspaces.members.retrieve("user_id", workspace_id: "workspace_id")

puts(beta_workspace_member)
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

`beta.organization.workspaces.members.update(user_id, **kwargs) -> BetaWorkspaceMember`

**POST** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Update Workspace Member

#### Parameters

- `workspace_id: String`

  ID of the Workspace.

- `user_id: String`

  ID of the User.

- `workspace_role: BetaWorkspaceRole`

  New workspace role for the User.

  - `:workspace_admin`

  - `:workspace_billing`

  - `:workspace_developer`

  - `:workspace_restricted_developer`

  - `:workspace_user`

#### Returns

- `class BetaWorkspaceMember`

  - `type: :workspace_member`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `user_id: String`

    ID of the User.

  - `workspace_id: String`

    ID of the Workspace.

  - `workspace_role: BetaWorkspaceRole`

    Role of the Workspace Member.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_workspace_member = anthropic.beta.organization.workspaces.members.update(
  "user_id",
  workspace_id: "workspace_id",
  workspace_role: :workspace_admin
)

puts(beta_workspace_member)
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

`beta.organization.workspaces.members.remove(user_id, **kwargs) -> MemberRemoveResponse`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Delete Workspace Member

#### Parameters

- `workspace_id: String`

  ID of the Workspace.

- `user_id: String`

  ID of the User.

#### Returns

- `class MemberRemoveResponse`

  - `type: :workspace_member_deleted`

    Deleted object type.

    For Workspace Members, this is always `"workspace_member_deleted"`.

  - `user_id: String`

    ID of the User.

  - `workspace_id: String`

    ID of the Workspace.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

member = anthropic.beta.organization.workspaces.members.remove("user_id", workspace_id: "workspace_id")

puts(member)
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

`beta.organization.workspaces.service_accounts.list(workspace_id, **kwargs) -> PageCursor<BetaServiceAccountWorkspaceMember>`

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

- `workspace_id: String`

  ID of the workspace.

- `limit: Integer`

  Number of results per page.

  maximum: 100, minimum: 1

- `page: String`

  Opaque cursor from a previous response's `next_page`.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 42 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccountWorkspaceMember`

  - `type: :service_account_workspace_member`

  - `created_by_actor_id: String`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: String`

    Tagged service account ID (`svac_...`).

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.workspaces.service_accounts.list("workspace_id")

puts(page)
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

`beta.organization.workspaces.service_accounts.add(workspace_id, **kwargs) -> BetaServiceAccountWorkspaceMember`

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

- `workspace_id: String`

  ID of the workspace.

- `service_account_id: String`

  Tagged service account ID to add.

- `workspace_role: BetaNoBillingWorkspaceRole`

  Role to assign to the service account in this workspace.

  - `:workspace_admin`

  - `:workspace_developer`

  - `:workspace_restricted_developer`

  - `:workspace_user`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 42 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccountWorkspaceMember`

  - `type: :service_account_workspace_member`

  - `created_by_actor_id: String`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: String`

    Tagged service account ID (`svac_...`).

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account_workspace_member = anthropic.beta.organization.workspaces.service_accounts.add(
  "workspace_id",
  service_account_id: "service_account_id",
  workspace_role: :workspace_admin
)

puts(beta_service_account_workspace_member)
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

`beta.organization.workspaces.service_accounts.retrieve(service_account_id, **kwargs) -> BetaServiceAccountWorkspaceMember`

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

- `workspace_id: String`

  ID of the workspace.

- `service_account_id: String`

  ID of the service account.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 42 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccountWorkspaceMember`

  - `type: :service_account_workspace_member`

  - `created_by_actor_id: String`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: String`

    Tagged service account ID (`svac_...`).

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account_workspace_member = anthropic.beta.organization.workspaces.service_accounts.retrieve(
  "service_account_id",
  workspace_id: "workspace_id"
)

puts(beta_service_account_workspace_member)
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

`beta.organization.workspaces.service_accounts.update(service_account_id, **kwargs) -> BetaServiceAccountWorkspaceMember`

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

- `workspace_id: String`

  ID of the workspace.

- `service_account_id: String`

  ID of the service account.

- `workspace_role: BetaNoBillingWorkspaceRole`

  New role for the service account in this workspace.

  - `:workspace_admin`

  - `:workspace_developer`

  - `:workspace_restricted_developer`

  - `:workspace_user`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 42 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class BetaServiceAccountWorkspaceMember`

  - `type: :service_account_workspace_member`

  - `created_by_actor_id: String`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `implicit: bool`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `service_account_id: String`

    Tagged service account ID (`svac_...`).

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`).

  - `workspace_role: BetaWorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `:workspace_admin`

    - `:workspace_billing`

    - `:workspace_developer`

    - `:workspace_restricted_developer`

    - `:workspace_user`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_service_account_workspace_member = anthropic.beta.organization.workspaces.service_accounts.update(
  "service_account_id",
  workspace_id: "workspace_id",
  workspace_role: :workspace_admin
)

puts(beta_service_account_workspace_member)
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

`beta.organization.workspaces.service_accounts.remove(service_account_id, **kwargs) -> ServiceAccountRemoveResponse`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Removal is idempotent (returns 200 even if the membership was already
removed). A DELETE against the implicit default-workspace membership
returns 200 but is a no-op and the membership persists; deleting an
explicit default-workspace row reverts to the implicit `workspace_user`
membership. Archived workspaces return 400.

#### Parameters

- `workspace_id: String`

  ID of the workspace.

- `service_account_id: String`

  ID of the service account.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 42 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"user-profiles-2026-09-04"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

    - `:"mid-conversation-output-config-2026-07-01"`

    - `:"thinking-binding-controls-2026-08-01"`

    - `:"mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `class ServiceAccountRemoveResponse`

  - `type: :service_account_workspace_member_deleted`

  - `service_account_id: String`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `workspace_id: String`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

service_account = anthropic.beta.organization.workspaces.service_accounts.remove(
  "service_account_id",
  workspace_id: "workspace_id"
)

puts(service_account)
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

`beta.organization.rate_limits.list(**kwargs) -> PageCursor<BetaOrganizationRateLimit>`

**GET** `/v1/organizations/rate_limits`

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `group_type: :batch | :files | :model_group | 3 more`

  Filter by group type.

  - `:batch`

  - `:files`

  - `:model_group`

  - `:skills`

  - `:token_count`

  - `:web_search`

- `limit: Integer`

  Maximum number of items to return per page. Ranges from `1` to `1000`.

  When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

  maximum: 1000, minimum: 1

- `model: String`

  Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

- `page: String`

  Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaOrganizationRateLimit`

  - `type: :rate_limit`

    Object type. Always `rate_limit` for organization rate-limit entries.

  - `id: String`

    Stable identifier for this rate-limit group within the organization.

  - `group_type: :batch | :files | :model_group | 3 more`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `:batch`

    - `:files`

    - `:model_group`

    - `:skills`

    - `:token_count`

    - `:web_search`

  - `limits: Array[BetaOrganizationRateLimitValue]`

    The limiter values that apply to this group.

    - `type: String`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `value: Integer`

      The configured limit value for this limiter type.

  - `models: Array[String]`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.organization.rate_limits.list

puts(page)
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

`beta.organization.compliance_settings.retrieve() -> BetaComplianceSettings`

**GET** `/v1/organizations/compliance_settings`

Retrieve your organization's Compliance Settings.

Compliance Settings is a singleton resource: there is exactly one per
organization, addressed without an identifier. The `state` field reflects
whether the Compliance API is enabled. An organization with a parent
organization reads the state inherited from the parent's configuration.

#### Returns

- `class BetaComplianceSettings`

  - `type: :compliance_settings`

  - `state: BetaComplianceSettingsState`

    Whether the Compliance API is enabled for this organization.

    - `class BetaComplianceSettingsStateEnabled`

      - `type: :enabled`

    - `class BetaComplianceSettingsStateDisabled`

      - `type: :disabled`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_compliance_settings = anthropic.beta.organization.compliance_settings.retrieve

puts(beta_compliance_settings)
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

`beta.organization.compliance_settings.update(**kwargs) -> BetaComplianceSettings`

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

  - `class BetaComplianceSettingsStateEnabledParam`

    - `type: :enabled`

  - `class BetaComplianceSettingsStateDisabledParam`

    - `type: :disabled`

#### Returns

- `class BetaComplianceSettings`

  - `type: :compliance_settings`

  - `state: BetaComplianceSettingsState`

    Whether the Compliance API is enabled for this organization.

    - `class BetaComplianceSettingsStateEnabled`

      - `type: :enabled`

    - `class BetaComplianceSettingsStateDisabled`

      - `type: :disabled`

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_compliance_settings = anthropic.beta.organization.compliance_settings.update(state: {type: :enabled})

puts(beta_compliance_settings)
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
