<!-- source: https://platform.claude.com/docs/en/api/python/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/python/beta -->

<!-- chunk-start -->

- `user_profile_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaUserProfile: …`

  - `id: str`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Dict[str, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: Literal["active", "pending", "rejected"]`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: Literal["user_profile"]`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `access_type: Optional[Literal["application", "passthrough"]]`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: Optional[Literal["external", "resold", "internal"]]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_user_profile = client.beta.user_profiles.retrieve(
    user_profile_id="uprof_011CZkZCu8hGbp5mYRQgUmz9",
)
print(beta_user_profile.id)
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

`beta.user_profiles.update(struser_profile_id, UserProfileUpdateParams**kwargs)  -> BetaUserProfile`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `user_profile_id: str`

- `access_type: Optional[Literal["application", "passthrough"]]`

  How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

  - `"application"`

  - `"passthrough"`

- `external_id: Optional[str]`

  If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

- `metadata: Optional[Dict[str, str]]`

  Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `name: Optional[str]`

  If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

- `relationship: Optional[Literal["external", "resold", "internal"]]`

  How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

  - `"external"`

  - `"resold"`

  - `"internal"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaUserProfile: …`

  - `id: str`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Dict[str, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: Literal["active", "pending", "rejected"]`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: Literal["user_profile"]`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `access_type: Optional[Literal["application", "passthrough"]]`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: Optional[Literal["external", "resold", "internal"]]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_user_profile = client.beta.user_profiles.update(
    user_profile_id="uprof_011CZkZCu8hGbp5mYRQgUmz9",
)
print(beta_user_profile.id)
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

`beta.user_profiles.create_enrollment_url(struser_profile_id, UserProfileCreateEnrollmentURLParams**kwargs)  -> BetaUserProfileEnrollmentURL`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `user_profile_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaUserProfileEnrollmentURL: …`

  - `expires_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["enrollment_url"]`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"`

  - `url: str`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_user_profile_enrollment_url = client.beta.user_profiles.create_enrollment_url(
    user_profile_id="uprof_011CZkZCu8hGbp5mYRQgUmz9",
)
print(beta_user_profile_enrollment_url.expires_at)
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

- `class BetaUserProfile: …`

  - `id: str`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `metadata: Dict[str, str]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `trust_grants: Dict[str, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: Literal["active", "pending", "rejected"]`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: Literal["user_profile"]`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

  - `access_type: Optional[Literal["application", "passthrough"]]`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `"application"`

    - `"passthrough"`

  - `external_id: Optional[str]`

    Platform's own identifier for this user. Not enforced unique.

  - `name: Optional[str]`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `relationship: Optional[Literal["external", "resold", "internal"]]`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

### Beta User Profile Enrollment URL

- `class BetaUserProfileEnrollmentURL: …`

  - `expires_at: datetime`

    A timestamp in RFC 3339 format

  - `type: Literal["enrollment_url"]`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"`

  - `url: str`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `class BetaUserProfileTrustGrant: …`

  - `status: Literal["active", "pending", "rejected"]`

    Status of the trust grant.

    - `"active"`

    - `"pending"`

    - `"rejected"`

# Dreams

## Create a Dream

`beta.dreams.create(DreamCreateParams**kwargs)  -> BetaDream`

**post** `/v1/dreams`

Create a Dream

### Parameters

- `inputs: Iterable[BetaDreamInputParam]`

  - `class BetaDreamMemoryStoreInput: …`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `class BetaDreamSessionsInput: …`

    Input session transcripts the dream reads.

    - `session_ids: List[str]`

    - `type: Literal["sessions"]`

      - `"sessions"`

- `model: Model`

  Model identifier and configuration applied to every pipeline stage.

  - `str`

  - `class BetaDreamModelConfigParam: …`

    Model identifier and configuration applied to every pipeline stage.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

- `instructions: Optional[str]`

- `output_behavior: Optional[BetaOutputBehaviorParam]`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `class BetaOutputBehaviorCreateNew: …`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type: Literal["create_new"]`

      - `"create_new"`

  - `class BetaOutputBehaviorUpdateExisting: …`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `memory_store_id: str`

    - `type: Literal["update_existing"]`

      - `"update_existing"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `ended_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `error: Optional[BetaDreamError]`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: str`

    - `type: str`

  - `inputs: List[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput: …`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: str`

      - `type: Literal["memory_store"]`

        - `"memory_store"`

    - `class BetaDreamSessionsInput: …`

      Input session transcripts the dream reads.

      - `session_ids: List[str]`

      - `type: Literal["sessions"]`

        - `"sessions"`

  - `instructions: Optional[str]`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew: …`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: Literal["create_new"]`

        - `"create_new"`

    - `class BetaOutputBehaviorUpdateExisting: …`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: str`

      - `type: Literal["update_existing"]`

        - `"update_existing"`

  - `outputs: List[BetaDreamOutput]`

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `session_id: Optional[str]`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: Literal["dream"]`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: int`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: int`

      Total tokens read from prompt cache.

    - `input_tokens: int`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: int`

      Total output tokens generated across every pipeline stage.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_dream = client.beta.dreams.create(
    inputs=[
        {
            "memory_store_id": "x",
            "type": "memory_store",
        }
    ],
    model="string",
)
print(beta_dream.id)
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

`beta.dreams.list(DreamListParams**kwargs)  -> SyncPageCursor[BetaDream]`

**get** `/v1/dreams`

List Dreams

### Parameters

- `created_at_gt: Optional[Union[str, datetime]]`

  Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

- `created_at_lt: Optional[Union[str, datetime]]`

  Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

- `include_archived: Optional[bool]`

  Query parameter for include_archived

- `limit: Optional[int]`

  Query parameter for limit

- `page: Optional[str]`

  Query parameter for page

- `statuses: Optional[List[BetaDreamStatus]]`

  Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

  - `"pending"`

  - `"running"`

  - `"completed"`

  - `"failed"`

  - `"canceled"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `ended_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `error: Optional[BetaDreamError]`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: str`

    - `type: str`

  - `inputs: List[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput: …`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: str`

      - `type: Literal["memory_store"]`

        - `"memory_store"`

    - `class BetaDreamSessionsInput: …`

      Input session transcripts the dream reads.

      - `session_ids: List[str]`

      - `type: Literal["sessions"]`

        - `"sessions"`

  - `instructions: Optional[str]`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew: …`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: Literal["create_new"]`

        - `"create_new"`

    - `class BetaOutputBehaviorUpdateExisting: …`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: str`

      - `type: Literal["update_existing"]`

        - `"update_existing"`

  - `outputs: List[BetaDreamOutput]`

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `session_id: Optional[str]`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: Literal["dream"]`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: int`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: int`

      Total tokens read from prompt cache.

    - `input_tokens: int`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: int`

      Total output tokens generated across every pipeline stage.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.dreams.list()
page = page.data[0]
print(page.id)
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

`beta.dreams.retrieve(strdream_id, DreamRetrieveParams**kwargs)  -> BetaDream`

**get** `/v1/dreams/{dream_id}`

Get a Dream

### Parameters

- `dream_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `ended_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `error: Optional[BetaDreamError]`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: str`

    - `type: str`

  - `inputs: List[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput: …`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: str`

      - `type: Literal["memory_store"]`

        - `"memory_store"`

    - `class BetaDreamSessionsInput: …`

      Input session transcripts the dream reads.

      - `session_ids: List[str]`

      - `type: Literal["sessions"]`

        - `"sessions"`

  - `instructions: Optional[str]`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew: …`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: Literal["create_new"]`

        - `"create_new"`

    - `class BetaOutputBehaviorUpdateExisting: …`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: str`

      - `type: Literal["update_existing"]`

        - `"update_existing"`

  - `outputs: List[BetaDreamOutput]`

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `session_id: Optional[str]`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: Literal["dream"]`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: int`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: int`

      Total tokens read from prompt cache.

    - `input_tokens: int`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: int`

      Total output tokens generated across every pipeline stage.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_dream = client.beta.dreams.retrieve(
    dream_id="dream_id",
)
print(beta_dream.id)
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

`beta.dreams.cancel(strdream_id, DreamCancelParams**kwargs)  -> BetaDream`

**post** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

### Parameters

- `dream_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `ended_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `error: Optional[BetaDreamError]`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: str`

    - `type: str`

  - `inputs: List[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput: …`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: str`

      - `type: Literal["memory_store"]`

        - `"memory_store"`

    - `class BetaDreamSessionsInput: …`

      Input session transcripts the dream reads.

      - `session_ids: List[str]`

      - `type: Literal["sessions"]`

        - `"sessions"`

  - `instructions: Optional[str]`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew: …`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: Literal["create_new"]`

        - `"create_new"`

    - `class BetaOutputBehaviorUpdateExisting: …`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: str`

      - `type: Literal["update_existing"]`

        - `"update_existing"`

  - `outputs: List[BetaDreamOutput]`

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `session_id: Optional[str]`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: Literal["dream"]`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: int`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: int`

      Total tokens read from prompt cache.

    - `input_tokens: int`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: int`

      Total output tokens generated across every pipeline stage.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_dream = client.beta.dreams.cancel(
    dream_id="dream_id",
)
print(beta_dream.id)
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

`beta.dreams.archive(strdream_id, DreamArchiveParams**kwargs)  -> BetaDream`

**post** `/v1/dreams/{dream_id}/archive`

Archive a Dream

### Parameters

- `dream_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `ended_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `error: Optional[BetaDreamError]`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: str`

    - `type: str`

  - `inputs: List[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput: …`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: str`

      - `type: Literal["memory_store"]`

        - `"memory_store"`

    - `class BetaDreamSessionsInput: …`

      Input session transcripts the dream reads.

      - `session_ids: List[str]`

      - `type: Literal["sessions"]`

        - `"sessions"`

  - `instructions: Optional[str]`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew: …`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: Literal["create_new"]`

        - `"create_new"`

    - `class BetaOutputBehaviorUpdateExisting: …`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: str`

      - `type: Literal["update_existing"]`

        - `"update_existing"`

  - `outputs: List[BetaDreamOutput]`

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `session_id: Optional[str]`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: Literal["dream"]`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: int`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: int`

      Total tokens read from prompt cache.

    - `input_tokens: int`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: int`

      Total output tokens generated across every pipeline stage.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_dream = client.beta.dreams.archive(
    dream_id="dream_id",
)
print(beta_dream.id)
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

- `class BetaDream: …`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `ended_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `error: Optional[BetaDreamError]`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: str`

    - `type: str`

  - `inputs: List[BetaDreamInput]`

    - `class BetaDreamMemoryStoreInput: …`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `memory_store_id: str`

      - `type: Literal["memory_store"]`

        - `"memory_store"`

    - `class BetaDreamSessionsInput: …`

      Input session transcripts the dream reads.

      - `session_ids: List[str]`

      - `type: Literal["sessions"]`

        - `"sessions"`

  - `instructions: Optional[str]`

  - `model: BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: str`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `output_behavior: BetaOutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew: …`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `type: Literal["create_new"]`

        - `"create_new"`

    - `class BetaOutputBehaviorUpdateExisting: …`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `memory_store_id: str`

      - `type: Literal["update_existing"]`

        - `"update_existing"`

  - `outputs: List[BetaDreamOutput]`

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `session_id: Optional[str]`

  - `status: BetaDreamStatus`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: Literal["dream"]`

    - `"dream"`

  - `usage: BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: int`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: int`

      Total tokens read from prompt cache.

    - `input_tokens: int`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: int`

      Total output tokens generated across every pipeline stage.

### Beta Dream Error

- `class BetaDreamError: …`

  Failure detail for a Dream whose `status` is `failed`.

  - `message: str`

  - `type: str`

### Beta Dream Input

- `BetaDreamInput`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `class BetaDreamMemoryStoreInput: …`

    An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

    - `memory_store_id: str`

    - `type: Literal["memory_store"]`

      - `"memory_store"`

  - `class BetaDreamSessionsInput: …`

    Input session transcripts the dream reads.

    - `session_ids: List[str]`

    - `type: Literal["sessions"]`

      - `"sessions"`

### Beta Dream Memory Store Input

- `class BetaDreamMemoryStoreInput: …`

  An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

  - `memory_store_id: str`

  - `type: Literal["memory_store"]`

    - `"memory_store"`

### Beta Dream Memory Store Output

- `class BetaDreamMemoryStoreOutput: …`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: str`

  - `type: Literal["memory_store"]`

    - `"memory_store"`

### Beta Dream Model Config

- `class BetaDreamModelConfig: …`

  Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

  - `id: str`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `speed: Optional[Literal["standard", "fast"]]`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Dream Model Config Param

- `class BetaDreamModelConfigParam: …`

  Model identifier and configuration applied to every pipeline stage.

  - `id: str`

    Model identifier, e.g. "claude-opus-5". 1-256 characters.

  - `speed: Optional[Literal["standard", "fast"]]`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Dream Output

- `class BetaDreamOutput: …`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: str`

  - `type: Literal["memory_store"]`

    - `"memory_store"`

### Beta Dream Sessions Input

- `class BetaDreamSessionsInput: …`

  Input session transcripts the dream reads.

  - `session_ids: List[str]`

  - `type: Literal["sessions"]`

    - `"sessions"`

### Beta Dream Status

- `Literal["pending", "running", "completed", 2 more]`

  Lifecycle status of a Dream.

  - `"pending"`

  - `"running"`

  - `"completed"`

  - `"failed"`

  - `"canceled"`

### Beta Dream Usage

- `class BetaDreamUsage: …`

  Cumulative token usage for the dream across every pipeline stage.

  - `cache_creation_input_tokens: int`

    Total tokens used to create prompt-cache entries (sum of all TTL tiers).

  - `cache_read_input_tokens: int`

    Total tokens read from prompt cache.

  - `input_tokens: int`

    Total uncached input tokens consumed across every pipeline stage.

  - `output_tokens: int`

    Total output tokens generated across every pipeline stage.

### Beta Output Behavior

- `BetaOutputBehavior`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `class BetaOutputBehaviorCreateNew: …`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `type: Literal["create_new"]`

      - `"create_new"`

  - `class BetaOutputBehaviorUpdateExisting: …`

    The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

    - `memory_store_id: str`

    - `type: Literal["update_existing"]`

      - `"update_existing"`

### Beta Output Behavior Create New

- `class BetaOutputBehaviorCreateNew: …`

  The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `type: Literal["create_new"]`

    - `"create_new"`

### Beta Output Behavior Update Existing

- `class BetaOutputBehaviorUpdateExisting: …`

  The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

  - `memory_store_id: str`

  - `type: Literal["update_existing"]`

    - `"update_existing"`

# Tunnels

## Create Tunnel

`beta.tunnels.create(TunnelCreateParams**kwargs)  -> BetaTunnel`

**post** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Parameters

- `display_name: Optional[str]`

  Optional human-readable name for the tunnel (1-255 characters).

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaTunnel: …`

  An MCP tunnel.

  - `id: str`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: Optional[str]`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: str`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: Literal["tunnel"]`

    - `"tunnel"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel = client.beta.tunnels.create()
print(beta_tunnel.id)
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

`beta.tunnels.retrieve(strtunnel_id, TunnelRetrieveParams**kwargs)  -> BetaTunnel`

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Parameters

- `tunnel_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaTunnel: …`

  An MCP tunnel.

  - `id: str`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: Optional[str]`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: str`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: Literal["tunnel"]`

    - `"tunnel"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel = client.beta.tunnels.retrieve(
    tunnel_id="tunnel_id",
)
print(beta_tunnel.id)
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

`beta.tunnels.list(TunnelListParams**kwargs)  -> SyncPageCursor[BetaTunnel]`

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Parameters

- `include_archived: Optional[bool]`

  Whether to include archived tunnels in the results. Defaults to false.

- `limit: Optional[int]`

  Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

- `page: Optional[str]`

  Opaque pagination cursor from a previous `list_tunnels` response.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaTunnel: …`

  An MCP tunnel.

  - `id: str`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: Optional[str]`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: str`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: Literal["tunnel"]`

    - `"tunnel"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.tunnels.list()
page = page.data[0]
print(page.id)
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

`beta.tunnels.archive(strtunnel_id, TunnelArchiveParams**kwargs)  -> BetaTunnel`

**post** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Parameters

- `tunnel_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaTunnel: …`

  An MCP tunnel.

  - `id: str`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: Optional[str]`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: str`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: Literal["tunnel"]`

    - `"tunnel"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel = client.beta.tunnels.archive(
    tunnel_id="tunnel_id",
)
print(beta_tunnel.id)
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

`beta.tunnels.reveal_token(strtunnel_id, TunnelRevealTokenParams**kwargs)  -> BetaTunnelToken`

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `tunnel_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaTunnelToken: …`

  A tunnel's connector token.

  - `id: str`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: str`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: Literal["tunnel_token"]`

    - `"tunnel_token"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel_token = client.beta.tunnels.reveal_token(
    tunnel_id="tunnel_id",
)
print(beta_tunnel_token.id)
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

`beta.tunnels.rotate_token(strtunnel_id, TunnelRotateTokenParams**kwargs)  -> BetaTunnelToken`

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `tunnel_id: str`

- `reason: Optional[str]`

  Optional free-text reason for the rotation, recorded for audit.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaTunnelToken: …`

  A tunnel's connector token.

  - `id: str`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: str`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: Literal["tunnel_token"]`

    - `"tunnel_token"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel_token = client.beta.tunnels.rotate_token(
    tunnel_id="tunnel_id",
)
print(beta_tunnel_token.id)
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

- `class BetaTunnel: …`

  An MCP tunnel.

  - `id: str`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `display_name: Optional[str]`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: str`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: Literal["tunnel"]`

    - `"tunnel"`

### Beta Tunnel Token

- `class BetaTunnelToken: …`

  A tunnel's connector token.

  - `id: str`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: str`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: Literal["tunnel_token"]`

    - `"tunnel_token"`

# Certificates

## Create Tunnel Certificate

`beta.tunnels.certificates.create(strtunnel_id, CertificateCreateParams**kwargs)  -> BetaTunnelCertificate`

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `tunnel_id: str`

- `ca_certificate_pem: str`

  PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaTunnelCertificate: …`

  A CA certificate attached to a tunnel.

  - `id: str`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `fingerprint: str`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: str`

    ID of the tunnel the certificate is registered against.

  - `type: Literal["tunnel_certificate"]`

    - `"tunnel_certificate"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel_certificate = client.beta.tunnels.certificates.create(
    tunnel_id="tunnel_id",
    ca_certificate_pem="ca_certificate_pem",
)
print(beta_tunnel_certificate.id)
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

`beta.tunnels.certificates.retrieve(strcertificate_id, CertificateRetrieveParams**kwargs)  -> BetaTunnelCertificate`

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `tunnel_id: str`

- `certificate_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaTunnelCertificate: …`

  A CA certificate attached to a tunnel.

  - `id: str`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `fingerprint: str`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: str`

    ID of the tunnel the certificate is registered against.

  - `type: Literal["tunnel_certificate"]`

    - `"tunnel_certificate"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel_certificate = client.beta.tunnels.certificates.retrieve(
    certificate_id="certificate_id",
    tunnel_id="tunnel_id",
)
print(beta_tunnel_certificate.id)
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

`beta.tunnels.certificates.list(strtunnel_id, CertificateListParams**kwargs)  -> SyncPageCursor[BetaTunnelCertificate]`

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `tunnel_id: str`

- `include_archived: Optional[bool]`

  Whether to include archived certificates in the results. Defaults to false.

- `limit: Optional[int]`

  Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

- `page: Optional[str]`

  Opaque pagination cursor from a previous `list_tunnel_certificates` response.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaTunnelCertificate: …`

  A CA certificate attached to a tunnel.

  - `id: str`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `fingerprint: str`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: str`

    ID of the tunnel the certificate is registered against.

  - `type: Literal["tunnel_certificate"]`

    - `"tunnel_certificate"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.tunnels.certificates.list(
    tunnel_id="tunnel_id",
)
page = page.data[0]
print(page.id)
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

`beta.tunnels.certificates.archive(strcertificate_id, CertificateArchiveParams**kwargs)  -> BetaTunnelCertificate`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `tunnel_id: str`

- `certificate_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 31 more]`

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

### Returns

- `class BetaTunnelCertificate: …`

  A CA certificate attached to a tunnel.

  - `id: str`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `fingerprint: str`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: str`

    ID of the tunnel the certificate is registered against.

  - `type: Literal["tunnel_certificate"]`

    - `"tunnel_certificate"`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_tunnel_certificate = client.beta.tunnels.certificates.archive(
    certificate_id="certificate_id",
    tunnel_id="tunnel_id",
)
print(beta_tunnel_certificate.id)
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

- `class BetaTunnelCertificate: …`

  A CA certificate attached to a tunnel.

  - `id: str`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `created_at: datetime`

    A timestamp in RFC 3339 format

  - `expires_at: Optional[datetime]`

    A timestamp in RFC 3339 format

  - `fingerprint: str`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: str`

    ID of the tunnel the certificate is registered against.

  - `type: Literal["tunnel_certificate"]`

    - `"tunnel_certificate"`

# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData: …`

  - `id: str`

    ID of the agent that triggered the event.

  - `organization_id: str`

  - `type: Literal["agent.archived"]`

    - `"agent.archived"`

  - `workspace_id: str`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData: …`

  - `id: str`

    ID of the agent that triggered the event.

  - `organization_id: str`

  - `type: Literal["agent.created"]`

    - `"agent.created"`

  - `workspace_id: str`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData: …`

  - `id: str`

    ID of the agent that triggered the event.

  - `organization_id: str`

  - `type: Literal["agent.deleted"]`

    - `"agent.deleted"`

  - `workspace_id: str`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData: …`

  - `id: str`

    ID of the agent that triggered the event.

  - `organization_id: str`

  - `type: Literal["agent.updated"]`

    - `"agent.updated"`

  - `workspace_id: str`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData: …`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment.archived"]`

    - `"deployment.archived"`

  - `workspace_id: str`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData: …`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment.created"]`

    - `"deployment.created"`

  - `workspace_id: str`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData: …`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment.deleted"]`

    - `"deployment.deleted"`

  - `workspace_id: str`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData: …`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment.paused"]`

    - `"deployment.paused"`

  - `workspace_id: str`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData: …`

  - `id: str`

    ID of the deployment run that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment_run.failed"]`

    - `"deployment_run.failed"`

  - `workspace_id: str`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData: …`

  - `id: str`

    ID of the deployment run that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment_run.started"]`

    - `"deployment_run.started"`

  - `workspace_id: str`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData: …`

  - `id: str`

    ID of the deployment run that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment_run.succeeded"]`

    - `"deployment_run.succeeded"`

  - `workspace_id: str`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData: …`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment.unpaused"]`

    - `"deployment.unpaused"`

  - `workspace_id: str`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData: …`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `type: Literal["deployment.updated"]`

    - `"deployment.updated"`

  - `workspace_id: str`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData: …`

  - `id: str`

    ID of the environment that triggered the event.

  - `organization_id: str`

  - `type: Literal["environment.archived"]`

    - `"environment.archived"`

  - `workspace_id: str`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData: …`

  - `id: str`

    ID of the environment that triggered the event.

  - `organization_id: str`

  - `type: Literal["environment.created"]`

    - `"environment.created"`

  - `workspace_id: str`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData: …`

  - `id: str`

    ID of the environment that triggered the event.

  - `organization_id: str`

  - `type: Literal["environment.deleted"]`

    - `"environment.deleted"`

  - `workspace_id: str`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData: …`

  - `id: str`

    ID of the environment that triggered the event.

  - `organization_id: str`

  - `type: Literal["environment.updated"]`

    - `"environment.updated"`

  - `workspace_id: str`

### Beta Webhook Event

- `class BetaWebhookEvent: …`

  - `id: str`

    Unique event identifier for idempotency.

  - `created_at: datetime`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.created"]`

        - `"session.created"`

      - `workspace_id: str`

    - `class BetaWebhookSessionPendingEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.pending"]`

        - `"session.pending"`

      - `workspace_id: str`

    - `class BetaWebhookSessionRunningEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.running"]`

        - `"session.running"`

      - `workspace_id: str`

    - `class BetaWebhookSessionIdledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.idled"]`

        - `"session.idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionRequiresActionEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.requires_action"]`

        - `"session.requires_action"`

      - `workspace_id: str`

    - `class BetaWebhookSessionArchivedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.archived"]`

        - `"session.archived"`

      - `workspace_id: str`

    - `class BetaWebhookSessionDeletedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.deleted"]`

        - `"session.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRescheduledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_rescheduled"]`

        - `"session.status_rescheduled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRunStartedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_run_started"]`

        - `"session.status_run_started"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusIdledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_idled"]`

        - `"session.status_idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusTerminatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_terminated"]`

        - `"session.status_terminated"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadCreatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `type: Literal["session.thread_created"]`

        - `"session.thread_created"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadIdledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `type: Literal["session.thread_idled"]`

        - `"session.thread_idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadTerminatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `type: Literal["session.thread_terminated"]`

        - `"session.thread_terminated"`

      - `workspace_id: str`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.outcome_evaluation_ended"]`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: str`

    - `class BetaWebhookVaultCreatedEventData: …`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.created"]`

        - `"vault.created"`

      - `workspace_id: str`

    - `class BetaWebhookVaultArchivedEventData: …`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.archived"]`

        - `"vault.archived"`

      - `workspace_id: str`

    - `class BetaWebhookVaultDeletedEventData: …`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.deleted"]`

        - `"vault.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialCreatedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.created"]`

        - `"vault_credential.created"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialArchivedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.archived"]`

        - `"vault_credential.archived"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialDeletedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.deleted"]`

        - `"vault_credential.deleted"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.refresh_failed"]`

        - `"vault_credential.refresh_failed"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookSessionUpdatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.updated"]`

        - `"session.updated"`

      - `workspace_id: str`

    - `class BetaWebhookAgentCreatedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.created"]`

        - `"agent.created"`

      - `workspace_id: str`

    - `class BetaWebhookAgentArchivedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.archived"]`

        - `"agent.archived"`

      - `workspace_id: str`

    - `class BetaWebhookAgentDeletedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.deleted"]`

        - `"agent.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentPausedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.paused"]`

        - `"deployment.paused"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunFailedEventData: …`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment_run.failed"]`

        - `"deployment_run.failed"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentCreatedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.created"]`

        - `"deployment.created"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentUpdatedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.updated"]`

        - `"deployment.updated"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentUnpausedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.unpaused"]`

        - `"deployment.unpaused"`

      - `workspace_id: str`

    - `class BetaWebhookAgentUpdatedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.updated"]`

        - `"agent.updated"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentArchivedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.archived"]`

        - `"deployment.archived"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunStartedEventData: …`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment_run.started"]`

        - `"deployment_run.started"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentDeletedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.deleted"]`

        - `"deployment.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunSucceededEventData: …`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment_run.succeeded"]`

        - `"deployment_run.succeeded"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentCreatedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.created"]`

        - `"environment.created"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentUpdatedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.updated"]`

        - `"environment.updated"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentArchivedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.archived"]`

        - `"environment.archived"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentDeletedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.deleted"]`

        - `"environment.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreCreatedEventData: …`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `type: Literal["memory_store.created"]`

        - `"memory_store.created"`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreArchivedEventData: …`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `type: Literal["memory_store.archived"]`

        - `"memory_store.archived"`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreDeletedEventData: …`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `type: Literal["memory_store.deleted"]`

        - `"memory_store.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookSessionBudgetReachedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.budget_reached"]`

        - `"session.budget_reached"`

      - `workspace_id: str`

  - `type: Literal["event"]`

    Object type. Always `event` for webhook payloads.

    - `"event"`

### Beta Webhook Event Data

- `BetaWebhookEventData`

  - `class BetaWebhookSessionCreatedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.created"]`

      - `"session.created"`

    - `workspace_id: str`

  - `class BetaWebhookSessionPendingEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.pending"]`

      - `"session.pending"`

    - `workspace_id: str`

  - `class BetaWebhookSessionRunningEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.running"]`

      - `"session.running"`

    - `workspace_id: str`

  - `class BetaWebhookSessionIdledEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.idled"]`

      - `"session.idled"`

    - `workspace_id: str`

  - `class BetaWebhookSessionRequiresActionEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.requires_action"]`

      - `"session.requires_action"`

    - `workspace_id: str`

  - `class BetaWebhookSessionArchivedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.archived"]`

      - `"session.archived"`

    - `workspace_id: str`

  - `class BetaWebhookSessionDeletedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.deleted"]`

      - `"session.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusRescheduledEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.status_rescheduled"]`

      - `"session.status_rescheduled"`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusRunStartedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.status_run_started"]`

      - `"session.status_run_started"`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusIdledEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.status_idled"]`

      - `"session.status_idled"`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusTerminatedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.status_terminated"]`

      - `"session.status_terminated"`

    - `workspace_id: str`

  - `class BetaWebhookSessionThreadCreatedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `session_thread_id: str`

      ID of the session thread this event refers to.

    - `type: Literal["session.thread_created"]`

      - `"session.thread_created"`

    - `workspace_id: str`

  - `class BetaWebhookSessionThreadIdledEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `session_thread_id: str`

      ID of the session thread this event refers to.

    - `type: Literal["session.thread_idled"]`

      - `"session.thread_idled"`

    - `workspace_id: str`

  - `class BetaWebhookSessionThreadTerminatedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `session_thread_id: str`

      ID of the session thread this event refers to.

    - `type: Literal["session.thread_terminated"]`

      - `"session.thread_terminated"`

    - `workspace_id: str`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.outcome_evaluation_ended"]`

      - `"session.outcome_evaluation_ended"`

    - `workspace_id: str`

  - `class BetaWebhookVaultCreatedEventData: …`

    - `id: str`

      ID of the vault that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault.created"]`

      - `"vault.created"`

    - `workspace_id: str`

  - `class BetaWebhookVaultArchivedEventData: …`

    - `id: str`

      ID of the vault that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault.archived"]`

      - `"vault.archived"`

    - `workspace_id: str`

  - `class BetaWebhookVaultDeletedEventData: …`

    - `id: str`

      ID of the vault that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault.deleted"]`

      - `"vault.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialCreatedEventData: …`

    - `id: str`

      ID of the vault credential that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault_credential.created"]`

      - `"vault_credential.created"`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialArchivedEventData: …`

    - `id: str`

      ID of the vault credential that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault_credential.archived"]`

      - `"vault_credential.archived"`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialDeletedEventData: …`

    - `id: str`

      ID of the vault credential that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault_credential.deleted"]`

      - `"vault_credential.deleted"`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

    - `id: str`

      ID of the vault credential that triggered the event.

    - `organization_id: str`

    - `type: Literal["vault_credential.refresh_failed"]`

      - `"vault_credential.refresh_failed"`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookSessionUpdatedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.updated"]`

      - `"session.updated"`

    - `workspace_id: str`

  - `class BetaWebhookAgentCreatedEventData: …`

    - `id: str`

      ID of the agent that triggered the event.

    - `organization_id: str`

    - `type: Literal["agent.created"]`

      - `"agent.created"`

    - `workspace_id: str`

  - `class BetaWebhookAgentArchivedEventData: …`

    - `id: str`

      ID of the agent that triggered the event.

    - `organization_id: str`

    - `type: Literal["agent.archived"]`

      - `"agent.archived"`

    - `workspace_id: str`

  - `class BetaWebhookAgentDeletedEventData: …`

    - `id: str`

      ID of the agent that triggered the event.

    - `organization_id: str`

    - `type: Literal["agent.deleted"]`

      - `"agent.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentPausedEventData: …`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment.paused"]`

      - `"deployment.paused"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentRunFailedEventData: …`

    - `id: str`

      ID of the deployment run that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment_run.failed"]`

      - `"deployment_run.failed"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentCreatedEventData: …`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment.created"]`

      - `"deployment.created"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentUpdatedEventData: …`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment.updated"]`

      - `"deployment.updated"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentUnpausedEventData: …`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment.unpaused"]`

      - `"deployment.unpaused"`

    - `workspace_id: str`

  - `class BetaWebhookAgentUpdatedEventData: …`

    - `id: str`

      ID of the agent that triggered the event.

    - `organization_id: str`

    - `type: Literal["agent.updated"]`

      - `"agent.updated"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentArchivedEventData: …`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment.archived"]`

      - `"deployment.archived"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentRunStartedEventData: …`

    - `id: str`

      ID of the deployment run that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment_run.started"]`

      - `"deployment_run.started"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentDeletedEventData: …`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment.deleted"]`

      - `"deployment.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentRunSucceededEventData: …`

    - `id: str`

      ID of the deployment run that triggered the event.

    - `organization_id: str`

    - `type: Literal["deployment_run.succeeded"]`

      - `"deployment_run.succeeded"`

    - `workspace_id: str`

  - `class BetaWebhookEnvironmentCreatedEventData: …`

    - `id: str`

      ID of the environment that triggered the event.

    - `organization_id: str`

    - `type: Literal["environment.created"]`

      - `"environment.created"`

    - `workspace_id: str`

  - `class BetaWebhookEnvironmentUpdatedEventData: …`

    - `id: str`

      ID of the environment that triggered the event.

    - `organization_id: str`

    - `type: Literal["environment.updated"]`

      - `"environment.updated"`

    - `workspace_id: str`

  - `class BetaWebhookEnvironmentArchivedEventData: …`

    - `id: str`

      ID of the environment that triggered the event.

    - `organization_id: str`

    - `type: Literal["environment.archived"]`

      - `"environment.archived"`

    - `workspace_id: str`

  - `class BetaWebhookEnvironmentDeletedEventData: …`

    - `id: str`

      ID of the environment that triggered the event.

    - `organization_id: str`

    - `type: Literal["environment.deleted"]`

      - `"environment.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookMemoryStoreCreatedEventData: …`

    - `id: str`

      ID of the memory store that triggered the event.

    - `organization_id: str`

    - `type: Literal["memory_store.created"]`

      - `"memory_store.created"`

    - `workspace_id: str`

  - `class BetaWebhookMemoryStoreArchivedEventData: …`

    - `id: str`

      ID of the memory store that triggered the event.

    - `organization_id: str`

    - `type: Literal["memory_store.archived"]`

      - `"memory_store.archived"`

    - `workspace_id: str`

  - `class BetaWebhookMemoryStoreDeletedEventData: …`

    - `id: str`

      ID of the memory store that triggered the event.

    - `organization_id: str`

    - `type: Literal["memory_store.deleted"]`

      - `"memory_store.deleted"`

    - `workspace_id: str`

  - `class BetaWebhookSessionBudgetReachedEventData: …`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `type: Literal["session.budget_reached"]`

      - `"session.budget_reached"`

    - `workspace_id: str`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData: …`

  - `id: str`

    ID of the memory store that triggered the event.

  - `organization_id: str`

  - `type: Literal["memory_store.archived"]`

    - `"memory_store.archived"`

  - `workspace_id: str`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData: …`

  - `id: str`

    ID of the memory store that triggered the event.

  - `organization_id: str`

  - `type: Literal["memory_store.created"]`

    - `"memory_store.created"`

  - `workspace_id: str`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData: …`

  - `id: str`

    ID of the memory store that triggered the event.

  - `organization_id: str`

  - `type: Literal["memory_store.deleted"]`

    - `"memory_store.deleted"`

  - `workspace_id: str`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.archived"]`

    - `"session.archived"`

  - `workspace_id: str`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.budget_reached"]`

    - `"session.budget_reached"`

  - `workspace_id: str`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.created"]`

    - `"session.created"`

  - `workspace_id: str`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.deleted"]`

    - `"session.deleted"`

  - `workspace_id: str`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.idled"]`

    - `"session.idled"`

  - `workspace_id: str`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.outcome_evaluation_ended"]`

    - `"session.outcome_evaluation_ended"`

  - `workspace_id: str`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.pending"]`

    - `"session.pending"`

  - `workspace_id: str`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.requires_action"]`

    - `"session.requires_action"`

  - `workspace_id: str`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.running"]`

    - `"session.running"`

  - `workspace_id: str`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.status_idled"]`

    - `"session.status_idled"`

  - `workspace_id: str`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.status_rescheduled"]`

    - `"session.status_rescheduled"`

  - `workspace_id: str`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.status_run_started"]`

    - `"session.status_run_started"`

  - `workspace_id: str`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.status_terminated"]`

    - `"session.status_terminated"`

  - `workspace_id: str`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `session_thread_id: str`

    ID of the session thread this event refers to.

  - `type: Literal["session.thread_created"]`

    - `"session.thread_created"`

  - `workspace_id: str`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `session_thread_id: str`

    ID of the session thread this event refers to.

  - `type: Literal["session.thread_idled"]`

    - `"session.thread_idled"`

  - `workspace_id: str`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `session_thread_id: str`

    ID of the session thread this event refers to.

  - `type: Literal["session.thread_terminated"]`

    - `"session.thread_terminated"`

  - `workspace_id: str`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData: …`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `type: Literal["session.updated"]`

    - `"session.updated"`

  - `workspace_id: str`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData: …`

  - `id: str`

    ID of the vault that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault.archived"]`

    - `"vault.archived"`

  - `workspace_id: str`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData: …`

  - `id: str`

    ID of the vault that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault.created"]`

    - `"vault.created"`

  - `workspace_id: str`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData: …`

  - `id: str`

    ID of the vault credential that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault_credential.archived"]`

    - `"vault_credential.archived"`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData: …`

  - `id: str`

    ID of the vault credential that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault_credential.created"]`

    - `"vault_credential.created"`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData: …`

  - `id: str`

    ID of the vault credential that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault_credential.deleted"]`

    - `"vault_credential.deleted"`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

  - `id: str`

    ID of the vault credential that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault_credential.refresh_failed"]`

    - `"vault_credential.refresh_failed"`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData: …`

  - `id: str`

    ID of the vault that triggered the event.

  - `organization_id: str`

  - `type: Literal["vault.deleted"]`

    - `"vault.deleted"`

  - `workspace_id: str`

### Unwrap Webhook Event

- `class UnwrapWebhookEvent: …`

  - `id: str`

    Unique event identifier for idempotency.

  - `created_at: datetime`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.created"]`

        - `"session.created"`

      - `workspace_id: str`

    - `class BetaWebhookSessionPendingEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.pending"]`

        - `"session.pending"`

      - `workspace_id: str`

    - `class BetaWebhookSessionRunningEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.running"]`

        - `"session.running"`

      - `workspace_id: str`

    - `class BetaWebhookSessionIdledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.idled"]`

        - `"session.idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionRequiresActionEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.requires_action"]`

        - `"session.requires_action"`

      - `workspace_id: str`

    - `class BetaWebhookSessionArchivedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.archived"]`

        - `"session.archived"`

      - `workspace_id: str`

    - `class BetaWebhookSessionDeletedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.deleted"]`

        - `"session.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRescheduledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_rescheduled"]`

        - `"session.status_rescheduled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRunStartedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_run_started"]`

        - `"session.status_run_started"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusIdledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_idled"]`

        - `"session.status_idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusTerminatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.status_terminated"]`

        - `"session.status_terminated"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadCreatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `type: Literal["session.thread_created"]`

        - `"session.thread_created"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadIdledEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `type: Literal["session.thread_idled"]`

        - `"session.thread_idled"`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadTerminatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `type: Literal["session.thread_terminated"]`

        - `"session.thread_terminated"`

      - `workspace_id: str`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.outcome_evaluation_ended"]`

        - `"session.outcome_evaluation_ended"`

      - `workspace_id: str`

    - `class BetaWebhookVaultCreatedEventData: …`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.created"]`

        - `"vault.created"`

      - `workspace_id: str`

    - `class BetaWebhookVaultArchivedEventData: …`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.archived"]`

        - `"vault.archived"`

      - `workspace_id: str`

    - `class BetaWebhookVaultDeletedEventData: …`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault.deleted"]`

        - `"vault.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialCreatedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.created"]`

        - `"vault_credential.created"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialArchivedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.archived"]`

        - `"vault_credential.archived"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialDeletedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.deleted"]`

        - `"vault_credential.deleted"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `type: Literal["vault_credential.refresh_failed"]`

        - `"vault_credential.refresh_failed"`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookSessionUpdatedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.updated"]`

        - `"session.updated"`

      - `workspace_id: str`

    - `class BetaWebhookAgentCreatedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.created"]`

        - `"agent.created"`

      - `workspace_id: str`

    - `class BetaWebhookAgentArchivedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.archived"]`

        - `"agent.archived"`

      - `workspace_id: str`

    - `class BetaWebhookAgentDeletedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.deleted"]`

        - `"agent.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentPausedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.paused"]`

        - `"deployment.paused"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunFailedEventData: …`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment_run.failed"]`

        - `"deployment_run.failed"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentCreatedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.created"]`

        - `"deployment.created"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentUpdatedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.updated"]`

        - `"deployment.updated"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentUnpausedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.unpaused"]`

        - `"deployment.unpaused"`

      - `workspace_id: str`

    - `class BetaWebhookAgentUpdatedEventData: …`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `type: Literal["agent.updated"]`

        - `"agent.updated"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentArchivedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.archived"]`

        - `"deployment.archived"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunStartedEventData: …`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment_run.started"]`

        - `"deployment_run.started"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentDeletedEventData: …`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment.deleted"]`

        - `"deployment.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunSucceededEventData: …`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `type: Literal["deployment_run.succeeded"]`

        - `"deployment_run.succeeded"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentCreatedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.created"]`

        - `"environment.created"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentUpdatedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.updated"]`

        - `"environment.updated"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentArchivedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.archived"]`

        - `"environment.archived"`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentDeletedEventData: …`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `type: Literal["environment.deleted"]`

        - `"environment.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreCreatedEventData: …`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `type: Literal["memory_store.created"]`

        - `"memory_store.created"`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreArchivedEventData: …`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `type: Literal["memory_store.archived"]`

        - `"memory_store.archived"`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreDeletedEventData: …`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `type: Literal["memory_store.deleted"]`

        - `"memory_store.deleted"`

      - `workspace_id: str`

    - `class BetaWebhookSessionBudgetReachedEventData: …`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `type: Literal["session.budget_reached"]`

        - `"session.budget_reached"`

      - `workspace_id: str`

  - `type: Literal["event"]`

    Object type. Always `event` for webhook payloads.

    - `"event"`
