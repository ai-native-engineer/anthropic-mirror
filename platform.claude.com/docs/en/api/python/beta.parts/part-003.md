<!-- source: https://platform.claude.com/docs/en/api/python/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/python/beta -->

<!-- chunk-start -->

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `type: Literal["service_account_workspace_member_deleted"]`

    default: service_account_workspace_member_deleted

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

  - `type: Literal["rate_limit"]`

    Object type. Always `rate_limit` for organization rate-limit entries.

    default: rate_limit

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
