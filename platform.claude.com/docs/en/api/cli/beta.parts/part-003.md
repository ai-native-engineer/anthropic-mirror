<!-- source: https://platform.claude.com/docs/en/api/cli/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/cli/beta -->

<!-- chunk-start -->
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

`$ ant beta:organization:rbac-groups create`

**POST** `/v1/organizations/rbac_groups`

Create an RBAC Group in the Claude Enterprise tenant. Groups created via the API have source type `"direct"`.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `--name: string`

  Name of the RBAC Group. Not uniqueness-enforced.

  minLength: 1, maxLength: 255

#### Returns

- `beta_rbac_group: object`

  - `type: "rbac_group"`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

  - `id: string`

    ID of the RBAC Group.

  - `created_at: string`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `name: string`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `role_ids: array of string`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `source_type: "direct" or "scim"`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `"direct"`

    - `"scim"`

  - `updated_at: string`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```bash
ant beta:organization:rbac-groups create \
  --api-key my-anthropic-api-key \
  --name Engineering
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

`$ ant beta:organization:rbac-groups list`

**GET** `/v1/organizations/rbac_groups`

List RBAC Groups in the Claude Enterprise tenant.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `--limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `--page: optional string`

  Optionally set to the `next_page` token from the previous response.

#### Returns

- `BetaRbacGroupList: object`

  - `data: array of BetaRBACGroup`

    - `type: "rbac_group"`

      Object type.

      For RBAC Groups, this is always `"rbac_group"`.

    - `id: string`

      ID of the RBAC Group.

    - `created_at: string`

      RFC 3339 timestamp of when the RBAC Group was created.

      format: date-time

    - `name: string`

      Name of the RBAC Group. Not uniqueness-enforced.

    - `role_ids: array of string`

      RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

    - `source_type: "direct" or "scim"`

      How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

      - `"direct"`

      - `"scim"`

    - `updated_at: string`

      RFC 3339 timestamp of when the RBAC Group was last updated.

      format: date-time

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### Example

```bash
ant beta:organization:rbac-groups list \
  --api-key my-anthropic-api-key
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

`$ ant beta:organization:rbac-groups retrieve`

**GET** `/v1/organizations/rbac_groups/{rbac_group_id}`

Retrieve an RBAC Group by ID.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `--rbac-group-id: string`

  ID of the RBAC Group.

#### Returns

- `beta_rbac_group: object`

  - `type: "rbac_group"`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

  - `id: string`

    ID of the RBAC Group.

  - `created_at: string`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `name: string`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `role_ids: array of string`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `source_type: "direct" or "scim"`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `"direct"`

    - `"scim"`

  - `updated_at: string`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```bash
ant beta:organization:rbac-groups retrieve \
  --api-key my-anthropic-api-key \
  --rbac-group-id rbac_group_id
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

`$ ant beta:organization:rbac-groups update`

**POST** `/v1/organizations/rbac_groups/{rbac_group_id}`

Update an RBAC Group's name. Groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `--rbac-group-id: string`

  ID of the RBAC Group.

- `--name: optional string`

  Name of the RBAC Group. Not uniqueness-enforced.

  minLength: 1, maxLength: 255

#### Returns

- `beta_rbac_group: object`

  - `type: "rbac_group"`

    Object type.

    For RBAC Groups, this is always `"rbac_group"`.

  - `id: string`

    ID of the RBAC Group.

  - `created_at: string`

    RFC 3339 timestamp of when the RBAC Group was created.

    format: date-time

  - `name: string`

    Name of the RBAC Group. Not uniqueness-enforced.

  - `role_ids: array of string`

    RBAC Role IDs attached to this RBAC Group. Role attachment is managed in the admin settings and is read-only on this API. `null` means role data was temporarily unavailable — retry to distinguish from an empty list.

  - `source_type: "direct" or "scim"`

    How the RBAC Group was created: `"direct"` for groups created directly (for example, in the organization's admin settings), `"scim"` for groups provisioned by the identity provider.

    - `"direct"`

    - `"scim"`

  - `updated_at: string`

    RFC 3339 timestamp of when the RBAC Group was last updated.

    format: date-time

#### Example

```bash
ant beta:organization:rbac-groups update \
  --api-key my-anthropic-api-key \
  --rbac-group-id rbac_group_id
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

`$ ant beta:organization:rbac-groups delete`

**DELETE** `/v1/organizations/rbac_groups/{rbac_group_id}`

Delete an RBAC Group. Groups provisioned by an identity provider (source type `"scim"`) cannot be deleted via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `--rbac-group-id: string`

  ID of the RBAC Group.

#### Returns

- `BetaOrganizationRBACGroupDeleteResponse: object`

  - `type: "rbac_group_deleted"`

    Deleted object type.

    For RBAC Groups, this is always `"rbac_group_deleted"`.

  - `id: string`

    ID of the RBAC Group.

#### Example

```bash
ant beta:organization:rbac-groups delete \
  --api-key my-anthropic-api-key \
  --rbac-group-id rbac_group_id
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

`$ ant beta:organization:rbac-groups:members list`

**GET** `/v1/organizations/rbac_groups/{rbac_group_id}/members`

List members of an RBAC Group.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `--rbac-group-id: string`

  ID of the RBAC Group.

- `--limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `--page: optional string`

  Optionally set to the `next_page` token from the previous response.

#### Returns

- `BetaRbacGroupMemberList: object`

  - `data: array of BetaRBACGroupMember`

    - `type: "rbac_group_member"`

      Object type.

      For RBAC Group Members, this is always `"rbac_group_member"`.

    - `created_at: string`

      RFC 3339 timestamp of when the User was added to the RBAC Group.

      format: date-time

    - `email: string`

      Email of the User.

    - `rbac_group_id: string`

      ID of the RBAC Group.

    - `user_id: string`

      ID of the User.

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### Example

```bash
ant beta:organization:rbac-groups:members list \
  --api-key my-anthropic-api-key \
  --rbac-group-id rbac_group_id
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

`$ ant beta:organization:rbac-groups:members add`

**POST** `/v1/organizations/rbac_groups/{rbac_group_id}/members`

Add a User to an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `--rbac-group-id: string`

  ID of the RBAC Group.

- `--user-id: string`

  ID of the User.

#### Returns

- `beta_rbac_group_member: object`

  - `type: "rbac_group_member"`

    Object type.

    For RBAC Group Members, this is always `"rbac_group_member"`.

  - `created_at: string`

    RFC 3339 timestamp of when the User was added to the RBAC Group.

    format: date-time

  - `email: string`

    Email of the User.

  - `rbac_group_id: string`

    ID of the RBAC Group.

  - `user_id: string`

    ID of the User.

#### Example

```bash
ant beta:organization:rbac-groups:members add \
  --api-key my-anthropic-api-key \
  --rbac-group-id rbac_group_id \
  --user-id user_01WCz1FkmYMm4gnmykNKUu3Q
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

`$ ant beta:organization:rbac-groups:members remove`

**DELETE** `/v1/organizations/rbac_groups/{rbac_group_id}/members/{user_id}`

Remove a User from an RBAC Group. Membership of groups provisioned by an identity provider (source type `"scim"`) cannot be modified via the API while an organization in the tenant uses SCIM provisioning.

The RBAC Groups API is available to Claude Enterprise organizations only.

#### Parameters

- `--rbac-group-id: string`

  ID of the RBAC Group.

- `--user-id: string`

  ID of the User.

#### Returns

- `BetaOrganizationRBACGroupMemberRemoveResponse: object`

  - `type: "rbac_group_member_deleted"`

    Deleted object type. For RBAC Group Members, this is always `"rbac_group_member_deleted"`.

  - `rbac_group_id: string`

    ID of the RBAC Group.

  - `user_id: string`

    ID of the User.

#### Example

```bash
ant beta:organization:rbac-groups:members remove \
  --api-key my-anthropic-api-key \
  --rbac-group-id rbac_group_id \
  --user-id user_id
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

`$ ant beta:organization:rbac-roles list`

**GET** `/v1/organizations/rbac_roles`

List RBAC Roles in the organization.

The RBAC Roles API is available to Claude Enterprise organizations only.

#### Parameters

- `--limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `--page: optional string`

  Optionally set to the `next_page` token from the previous response.

#### Returns

- `BetaRbacRoleList: object`

  - `data: array of BetaRBACRole`

    - `type: "rbac_role"`

      Object type.

      For RBAC Roles, this is always `"rbac_role"`.

    - `id: string`

      ID of the RBAC Role.

    - `created_at: string`

      RFC 3339 datetime string indicating when the RBAC Role was created.

      format: date-time

    - `display_name: string`

      Name of the RBAC Role. For a role created by Anthropic, this name can differ from the label claude.ai shows, and Anthropic may change the name. To keep a lasting reference to a role, store its `id`.

    - `updated_at: string`

      RFC 3339 datetime string indicating when the RBAC Role was last updated.

      format: date-time

    - `name: string`

      **Deprecated**: Use `display_name` instead; `name` always has the same value.

      Deprecated: use `display_name` instead. Name of the RBAC Role; always the same value as `display_name`.

  - `has_more: boolean`

    Indicates whether there are more results beyond this page.

  - `next_page: string`

    Opaque cursor for the next page. Pass as the `page` parameter on the next
    request.

#### Example

```bash
ant beta:organization:rbac-roles list \
  --api-key my-anthropic-api-key
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

`$ ant beta:organization:rbac-roles retrieve`

**GET** `/v1/organizations/rbac_roles/{rbac_role_id}`

Retrieve an RBAC Role by ID.

The RBAC Roles API is available to Claude Enterprise organizations only.

#### Parameters

- `--rbac-role-id: string`

  ID of the RBAC Role.

#### Returns

- `beta_rbac_role: object`

  - `type: "rbac_role"`

    Object type.

    For RBAC Roles, this is always `"rbac_role"`.

  - `id: string`

    ID of the RBAC Role.

  - `created_at: string`

    RFC 3339 datetime string indicating when the RBAC Role was created.

    format: date-time

  - `display_name: string`

    Name of the RBAC Role. For a role created by Anthropic, this name can differ from the label claude.ai shows, and Anthropic may change the name. To keep a lasting reference to a role, store its `id`.

  - `updated_at: string`

    RFC 3339 datetime string indicating when the RBAC Role was last updated.

    format: date-time

  - `name: string`

    **Deprecated**: Use `display_name` instead; `name` always has the same value.

    Deprecated: use `display_name` instead. Name of the RBAC Role; always the same value as `display_name`.

#### Example

```bash
ant beta:organization:rbac-roles retrieve \
  --api-key my-anthropic-api-key \
  --rbac-role-id rbac_role_id
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

`$ ant beta:organization:rbac-roles:permissions list`

**GET** `/v1/organizations/rbac_roles/{rbac_role_id}/permissions`

List the permissions an RBAC Role grants.

The RBAC Roles API is available to Claude Enterprise organizations only.

#### Parameters

- `--rbac-role-id: string`

  ID of the RBAC Role.

- `--limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `--page: optional string`

  Optionally set to the `next_page` token from the previous response.

#### Returns

- `BetaRbacRolePermissionList: object`

  - `data: array of BetaRBACRolePermission`

    - `type: "rbac_role_permission"`

      Object type.

      For RBAC Role Permissions, this is always `"rbac_role_permission"`.

    - `action: string`

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

    - `resource: BetaRBACOrganizationPermissionResource or BetaRBACConnectorToolPermissionResource or BetaRBACConnectorScopePermissionResource or 2 more`

      What the permission applies to.

      A tagged union: `type` names the kind of resource and determines which
      identifier fields are present.

      - `beta_rbac_organization_permission_resource: object`

        - `type: "organization"`

          Kind of resource the permission applies to.

        - `organization_id: string`

          UUID of the organization the permission applies to.

      - `beta_rbac_connector_tool_permission_resource: object`

        - `type: "connector_tool"`

          Kind of resource the permission applies to.

        - `connector_id: string`

          ID of the connector the permission applies to.

        - `tool_name: string`

          Published name of the connector tool the permission applies to.

          When the published name contains characters outside `[a-zA-Z0-9_-]` (or
          collides with a reserved form), it is server-encoded into a stable
          `{prefix}_{32-hex}` form — a shortened readable prefix of the name plus
          a hash — from which the published name is not recoverable.

      - `beta_rbac_connector_scope_permission_resource: object`

        - `type: "connector_scope"`

          Kind of resource the permission applies to.

        - `connector_id: string`

          ID of the connector the permission applies to.

        - `scope: string`

          OAuth scope the permission names — the role may receive this scope when
          tokens are minted for the connector.

          Subject to the same encoding rule as `tool_name`: a scope containing
          characters outside `[a-zA-Z0-9_-]` (or colliding with a reserved form)
          appears server-encoded in a stable `{prefix}_{32-hex}` form. OAuth
          scopes routinely contain `:` and `/`, so most appear encoded.

      - `beta_rbac_connector_permission_resource: object`

        - `type: "connector"`

          Kind of resource the permission applies to.

        - `connector_id: string`

          ID of the connector the permission applies to.

      - `beta_rbac_all_connectors_permission_resource: object`

        - `type: "all_connectors"`

          Kind of resource the permission applies to.

  - `has_more: boolean`

    Indicates whether there are more results beyond this page.

  - `next_page: string`

    Opaque cursor for the next page. Pass as the `page` parameter on the next
    request.

#### Example

```bash
ant beta:organization:rbac-roles:permissions list \
  --api-key my-anthropic-api-key \
  --rbac-role-id rbac_role_id
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

`$ ant beta:organization:plugins create`

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

- `--file: array of string`

  Body param: The version's files: one part per file, the part's filename being the file's path within the Plugin (for example `skills/review-pr/SKILL.md`), or a single `.zip` or `.plugin` archive holding them all. On the wire each part is named `files[]`, and a part named plain `files` is not read; with cURL, `-F 'files[]=@SKILL.md;filename=skills/review-pr/SKILL.md'`. The files must include the manifest, `.claude-plugin/plugin.json`.

- `--marketplace-id: optional string`

  Body param: ID of the organization-owned plugin marketplace to create the Plugin in (prefixed `marketplace_`). It must be a `manual` marketplace, one whose Plugins are uploaded rather than synchronized from a repository. When omitted, the Plugin is created in the organization's library marketplace, an organization-owned `manual` marketplace created on first use.

- `--release-notes: optional string`

  Body param: Release notes stored with the version and shown in its version history in claude.ai; up to 5,000 characters.

  maxLength: 5000

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `beta_plugin: object`

  - `type: "plugin"`

    Always `plugin`.

  - `id: string`

    The Plugin's ID.

  - `components: array of BetaPluginComponent`

    What the served version contains; null when not enumerated.

    - `type: "agent" or "cli" or "command" or 3 more`

      The kind of component.

      - `"agent"`

      - `"cli"`

      - `"command"`

      - `"hook"`

      - `"mcp_server"`

      - `"skill"`

    - `description: string`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: object`

    The served version's content scan; null when it has not been scanned.

    - `assessment: "fail" or "pass" or "unknown" or "warn"`

      The scan's verdict; set only when `status` is `completed`.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `"completed"`

      - `"errored"`

      - `"processing"`

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor or BetaPluginAPIActor`

    Who created the Plugin; null when no creator is recorded.

    - `beta_plugin_user_actor: object`

      - `type: "user_actor"`

        A member of the organization.

      - `email_address: string`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: string`

        The member's User ID.

    - `beta_plugin_api_actor: object`

      - `type: "api_actor"`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

      - `api_key_id: string`

        The key's ID.

  - `description: string`

    The served version's description.

  - `display_name: string`

    The served version's display name.

  - `latest_version_id: string`

    The newest version.

  - `manifest_version: string`

    The version string the served version's manifest declares.

  - `marketplace_id: string`

    The ID of the plugin marketplace the Plugin lives in.

  - `name: string`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `organization_installation_preference: "auto_install" or "available" or "not_available" or "required"`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `"auto_install"`

    - `"available"`

    - `"not_available"`

    - `"required"`

  - `organization_installation_preference_inherited: boolean`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `owner: BetaPluginOwnerOrganization or BetaPluginOwnerUser`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `beta_plugin_owner_organization: object`

      - `type: "organization"`

        The Plugin lives in a plugin marketplace the organization owns.

    - `beta_plugin_owner_user: object`

      - `type: "user"`

        The Plugin lives in one member's personal plugin marketplace.

      - `user_id: string`

        The member's User ID.

  - `reach: "contained" or "privileged" or "remote"`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `served_version_id: string`

    The version claude.ai serves to members.

  - `served_version_pinned: boolean`

    False while the served version follows each new version; true once it has been pinned to one.

  - `updated_at: string`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

#### Example

```bash
ant beta:organization:plugins create \
  --api-key my-anthropic-api-key \
  --file 'Example data'
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

`$ ant beta:organization:plugins retrieve`

**GET** `/v1/organizations/plugins/{plugin_id}`

Retrieve a Plugin by ID.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `--plugin-id: string`

  Path param: ID of the Plugin (prefixed `plugin_`).

- `--organization-id: optional string`

  Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `beta_plugin: object`

  - `type: "plugin"`

    Always `plugin`.

  - `id: string`

    The Plugin's ID.

  - `components: array of BetaPluginComponent`

    What the served version contains; null when not enumerated.

    - `type: "agent" or "cli" or "command" or 3 more`

      The kind of component.

      - `"agent"`

      - `"cli"`

      - `"command"`

      - `"hook"`

      - `"mcp_server"`

      - `"skill"`

    - `description: string`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: object`

    The served version's content scan; null when it has not been scanned.

    - `assessment: "fail" or "pass" or "unknown" or "warn"`

      The scan's verdict; set only when `status` is `completed`.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `"completed"`

      - `"errored"`

      - `"processing"`

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor or BetaPluginAPIActor`

    Who created the Plugin; null when no creator is recorded.

    - `beta_plugin_user_actor: object`

      - `type: "user_actor"`

        A member of the organization.

      - `email_address: string`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: string`

        The member's User ID.

    - `beta_plugin_api_actor: object`

      - `type: "api_actor"`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

      - `api_key_id: string`

        The key's ID.

  - `description: string`

    The served version's description.

  - `display_name: string`

    The served version's display name.

  - `latest_version_id: string`

    The newest version.

  - `manifest_version: string`

    The version string the served version's manifest declares.

  - `marketplace_id: string`

    The ID of the plugin marketplace the Plugin lives in.

  - `name: string`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `organization_installation_preference: "auto_install" or "available" or "not_available" or "required"`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `"auto_install"`

    - `"available"`

    - `"not_available"`

    - `"required"`

  - `organization_installation_preference_inherited: boolean`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `owner: BetaPluginOwnerOrganization or BetaPluginOwnerUser`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `beta_plugin_owner_organization: object`

      - `type: "organization"`

        The Plugin lives in a plugin marketplace the organization owns.

    - `beta_plugin_owner_user: object`

      - `type: "user"`

        The Plugin lives in one member's personal plugin marketplace.

      - `user_id: string`

        The member's User ID.

  - `reach: "contained" or "privileged" or "remote"`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `served_version_id: string`

    The version claude.ai serves to members.

  - `served_version_pinned: boolean`

    False while the served version follows each new version; true once it has been pinned to one.

  - `updated_at: string`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

#### Example

```bash
ant beta:organization:plugins retrieve \
  --api-key my-anthropic-api-key \
  --plugin-id plugin_id
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

`$ ant beta:organization:plugins update`

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

- `--plugin-id: string`

  Path param: ID of the Plugin (prefixed `plugin_`).

- `--served-version-id: string`

  Body param: Serve this version of the Plugin (prefixed `pluginver_`) and pin the served version to it; `latest` is not accepted.

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `beta_plugin: object`

  - `type: "plugin"`

    Always `plugin`.

  - `id: string`

    The Plugin's ID.

  - `components: array of BetaPluginComponent`

    What the served version contains; null when not enumerated.

    - `type: "agent" or "cli" or "command" or 3 more`

      The kind of component.

      - `"agent"`

      - `"cli"`

      - `"command"`

      - `"hook"`

      - `"mcp_server"`

      - `"skill"`

    - `description: string`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: object`

    The served version's content scan; null when it has not been scanned.

    - `assessment: "fail" or "pass" or "unknown" or "warn"`

      The scan's verdict; set only when `status` is `completed`.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `"completed"`

      - `"errored"`

      - `"processing"`

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor or BetaPluginAPIActor`

    Who created the Plugin; null when no creator is recorded.

    - `beta_plugin_user_actor: object`

      - `type: "user_actor"`

        A member of the organization.

      - `email_address: string`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: string`

        The member's User ID.

    - `beta_plugin_api_actor: object`

      - `type: "api_actor"`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

      - `api_key_id: string`

        The key's ID.

  - `description: string`

    The served version's description.

  - `display_name: string`

    The served version's display name.

  - `latest_version_id: string`

    The newest version.

  - `manifest_version: string`

    The version string the served version's manifest declares.

  - `marketplace_id: string`

    The ID of the plugin marketplace the Plugin lives in.

  - `name: string`

    Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

  - `organization_installation_preference: "auto_install" or "available" or "not_available" or "required"`

    Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `"auto_install"`

    - `"available"`

    - `"not_available"`

    - `"required"`

  - `organization_installation_preference_inherited: boolean`

    Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

  - `owner: BetaPluginOwnerOrganization or BetaPluginOwnerUser`

    Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

    - `beta_plugin_owner_organization: object`

      - `type: "organization"`

        The Plugin lives in a plugin marketplace the organization owns.

    - `beta_plugin_owner_user: object`

      - `type: "user"`

        The Plugin lives in one member's personal plugin marketplace.

      - `user_id: string`

        The member's User ID.

  - `reach: "contained" or "privileged" or "remote"`

    How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `served_version_id: string`

    The version claude.ai serves to members.

  - `served_version_pinned: boolean`

    False while the served version follows each new version; true once it has been pinned to one.

  - `updated_at: string`

    RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

    format: date-time

#### Example

```bash
ant beta:organization:plugins update \
  --api-key my-anthropic-api-key \
  --plugin-id plugin_id \
  --served-version-id pluginver_01KaZmQpRsTuVwXyZ2b4c6d8
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

`$ ant beta:organization:plugins list`

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

- `--created-at-gt: optional string`

  Query param: RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

  format: date-time

- `--created-at-gte: optional string`

  Query param: RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

  format: date-time

- `--created-at-lt: optional string`

  Query param: RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

  format: date-time

- `--created-at-lte: optional string`

  Query param: RFC 3339 timestamp bound; combine [gte], [gt], [lte], [lt].

  format: date-time

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `100`.

  minimum: 1, maximum: 100

- `--marketplace-id: optional string`

  Query param: Only Plugins in this plugin marketplace (prefixed `marketplace_`).

- `--organization-id: optional string`

  Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `--owner-type: optional "organization" or "user"`

  Query param: `organization` for Plugins in the organization's plugin marketplaces, `user` for Plugins in members' personal plugin marketplaces.

- `--owner-user-id: optional string`

  Query param: Only Plugins in this member's personal plugin marketplaces (prefixed `user_`); a removed member's ID is accepted.

- `--page: optional string`

  Query param: Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `BetaPluginList: object`

  - `data: array of BetaPlugin`

    - `type: "plugin"`

      Always `plugin`.

    - `id: string`

      The Plugin's ID.

    - `components: array of BetaPluginComponent`

      What the served version contains; null when not enumerated.

      - `type: "agent" or "cli" or "command" or 3 more`

        The kind of component.

        - `"agent"`

        - `"cli"`

        - `"command"`

        - `"hook"`

        - `"mcp_server"`

        - `"skill"`

      - `description: string`

        What the component declares about itself; always null for MCP servers, hooks, and CLIs.

      - `name: string`

        The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

    - `content_scan: object`

      The served version's content scan; null when it has not been scanned.

      - `assessment: "fail" or "pass" or "unknown" or "warn"`

        The scan's verdict; set only when `status` is `completed`.

        - `"fail"`

        - `"pass"`

        - `"unknown"`

        - `"warn"`

      - `reason: string`

        The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

      - `status: "completed" or "errored" or "processing"`

        `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

        - `"completed"`

        - `"errored"`

        - `"processing"`

    - `created_at: string`

      RFC 3339.

      format: date-time

    - `created_by: BetaPluginUserActor or BetaPluginAPIActor`

      Who created the Plugin; null when no creator is recorded.

      - `beta_plugin_user_actor: object`

        - `type: "user_actor"`

          A member of the organization.

        - `email_address: string`

          The member's email address; may be null, for example when they are no longer a member of the organization.

        - `user_id: string`

          The member's User ID.

      - `beta_plugin_api_actor: object`

        - `type: "api_actor"`

          An Admin API key, in the same form the Compliance API activity feed uses for it.

        - `api_key_id: string`

          The key's ID.

    - `description: string`

      The served version's description.

    - `display_name: string`

      The served version's display name.

    - `latest_version_id: string`

      The newest version.

    - `manifest_version: string`

      The version string the served version's manifest declares.

    - `marketplace_id: string`

      The ID of the plugin marketplace the Plugin lives in.

    - `name: string`

      Lowercase identifier, unique within its plugin marketplace. Fixed for an organization-owned Plugin's lifetime; a member-owned Plugin's changes when its owner renames it in claude.ai, while its `id` stays the same.

    - `organization_installation_preference: "auto_install" or "available" or "not_available" or "required"`

      Organization-owned Plugin: the organization-wide installation setting every member gets unless an RBAC Group they belong to holds its own — the Plugin's own setting, or its plugin marketplace's default. Null for a member-owned Plugin, which has shares instead. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

      - `"auto_install"`

      - `"available"`

      - `"not_available"`

      - `"required"`

    - `organization_installation_preference_inherited: boolean`

      Organization-owned Plugin: true while it has no organization-wide setting of its own and `organization_installation_preference` is its plugin marketplace's default. Null for a member-owned Plugin.

    - `owner: BetaPluginOwnerOrganization or BetaPluginOwnerUser`

      Who owns the Plugin: the organization, or the member whose personal plugin marketplace it lives in.

      - `beta_plugin_owner_organization: object`

        - `type: "organization"`

          The Plugin lives in a plugin marketplace the organization owns.

      - `beta_plugin_owner_user: object`

        - `type: "user"`

          The Plugin lives in one member's personal plugin marketplace.

        - `user_id: string`

          The member's User ID.

    - `reach: "contained" or "privileged" or "remote"`

      How far the served version reaches: `remote` when it declares an MCP server or a CLI, `privileged` when it declares a hook, monitor, language server or settings but nothing remote, `contained` otherwise; null when not classifiable.

      - `"contained"`

      - `"privileged"`

      - `"remote"`

    - `served_version_id: string`

      The version claude.ai serves to members.

    - `served_version_pinned: boolean`

      False while the served version follows each new version; true once it has been pinned to one.

    - `updated_at: string`

      RFC 3339. Moves on a new version and on a served-version change; a change to the Plugin's installation settings or shares does not move it.

      format: date-time

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data. A page may hold fewer than `limit` Plugins, even none, while this is set; keep following it until it is null.

#### Example

```bash
ant beta:organization:plugins list \
  --api-key my-anthropic-api-key
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

`$ ant beta:organization:plugins delete`

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

- `--plugin-id: string`

  ID of the Plugin (prefixed `plugin_`).

- `--beta: optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `beta_deleted_plugin: object`

  - `type: "plugin_deleted"`

    Always `plugin_deleted`.

  - `id: string`

    The deleted Plugin's ID.

#### Example

```bash
ant beta:organization:plugins delete \
  --api-key my-anthropic-api-key \
  --plugin-id plugin_id
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

`$ ant beta:organization:plugins:versions create`

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

- `--plugin-id: string`

  Path param: ID of the Plugin (prefixed `plugin_`).

- `--file: array of string`

  Body param: The version's files: one part per file, the part's filename being the file's path within the Plugin (for example `skills/review-pr/SKILL.md`), or a single `.zip` or `.plugin` archive holding them all. On the wire each part is named `files[]`, and a part named plain `files` is not read; with cURL, `-F 'files[]=@SKILL.md;filename=skills/review-pr/SKILL.md'`. The files must include the manifest, `.claude-plugin/plugin.json`.

- `--release-notes: optional string`

  Body param: Release notes stored with the version and shown in its version history in claude.ai; up to 5,000 characters.

  maxLength: 5000

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `beta_plugin_version: object`

  - `type: "plugin_version"`

    Always `plugin_version`.

  - `id: string`

    The version's ID.

  - `components: array of BetaPluginComponent`

    What the version contains; null when not enumerated.

    - `type: "agent" or "cli" or "command" or 3 more`

      The kind of component.

      - `"agent"`

      - `"cli"`

      - `"command"`

      - `"hook"`

      - `"mcp_server"`

      - `"skill"`

    - `description: string`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: object`

    This version's content scan; null when it has not been scanned.

    - `assessment: "fail" or "pass" or "unknown" or "warn"`

      The scan's verdict; set only when `status` is `completed`.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `"completed"`

      - `"errored"`

      - `"processing"`

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor or BetaPluginAPIActor`

    Who uploaded this version; null when not recorded.

    - `beta_plugin_user_actor: object`

      - `type: "user_actor"`

        A member of the organization.

      - `email_address: string`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: string`

        The member's User ID.

    - `beta_plugin_api_actor: object`

      - `type: "api_actor"`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

      - `api_key_id: string`

        The key's ID.

  - `description: string`

    The manifest's description; null when it declares none.

  - `display_name: string`

    The manifest's display name; null when it declares none.

  - `manifest_version: string`

    The version string the manifest declares; null when it declares none.

  - `plugin_id: string`

    The Plugin's ID.

  - `reach: "contained" or "privileged" or "remote"`

    How far the version reaches: `remote`, `privileged` or `contained`, as on the Plugin; null when not classifiable.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `release_notes: string`

    As supplied with the upload; null when none were supplied.

#### Example

```bash
ant beta:organization:plugins:versions create \
  --api-key my-anthropic-api-key \
  --plugin-id plugin_id \
  --file 'Example data'
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

`$ ant beta:organization:plugins:versions list`

**GET** `/v1/organizations/plugins/{plugin_id}/versions`

List a Plugin's versions, newest first.

The first item of the first page is the version the Plugin's `latest_version_id`
refers to.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `--plugin-id: string`

  Path param: ID of the Plugin (prefixed `plugin_`).

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `--organization-id: optional string`

  Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `--page: optional string`

  Query param: Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `BetaPluginVersionList: object`

  - `data: array of BetaPluginVersion`

    - `type: "plugin_version"`

      Always `plugin_version`.

    - `id: string`

      The version's ID.

    - `components: array of BetaPluginComponent`

      What the version contains; null when not enumerated.

      - `type: "agent" or "cli" or "command" or 3 more`

        The kind of component.

        - `"agent"`

        - `"cli"`

        - `"command"`

        - `"hook"`

        - `"mcp_server"`

        - `"skill"`

      - `description: string`

        What the component declares about itself; always null for MCP servers, hooks, and CLIs.

      - `name: string`

        The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

    - `content_scan: object`

      This version's content scan; null when it has not been scanned.

      - `assessment: "fail" or "pass" or "unknown" or "warn"`

        The scan's verdict; set only when `status` is `completed`.

        - `"fail"`

        - `"pass"`

        - `"unknown"`

        - `"warn"`

      - `reason: string`

        The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

      - `status: "completed" or "errored" or "processing"`

        `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

        - `"completed"`

        - `"errored"`

        - `"processing"`

    - `created_at: string`

      RFC 3339.

      format: date-time

    - `created_by: BetaPluginUserActor or BetaPluginAPIActor`

      Who uploaded this version; null when not recorded.

      - `beta_plugin_user_actor: object`

        - `type: "user_actor"`

          A member of the organization.

        - `email_address: string`

          The member's email address; may be null, for example when they are no longer a member of the organization.

        - `user_id: string`

          The member's User ID.

      - `beta_plugin_api_actor: object`

        - `type: "api_actor"`

          An Admin API key, in the same form the Compliance API activity feed uses for it.

        - `api_key_id: string`

          The key's ID.

    - `description: string`

      The manifest's description; null when it declares none.

    - `display_name: string`

      The manifest's display name; null when it declares none.

    - `manifest_version: string`

      The version string the manifest declares; null when it declares none.

    - `plugin_id: string`

      The Plugin's ID.

    - `reach: "contained" or "privileged" or "remote"`

      How far the version reaches: `remote`, `privileged` or `contained`, as on the Plugin; null when not classifiable.

      - `"contained"`

      - `"privileged"`

      - `"remote"`

    - `release_notes: string`

      As supplied with the upload; null when none were supplied.

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### Example

```bash
ant beta:organization:plugins:versions list \
  --api-key my-anthropic-api-key \
  --plugin-id plugin_id
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

`$ ant beta:organization:plugins:versions retrieve`

**GET** `/v1/organizations/plugins/{plugin_id}/versions/{version}`

Retrieve one version of a Plugin by its ID, or the Plugin's newest version.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `--plugin-id: string`

  Path param: ID of the Plugin (prefixed `plugin_`).

- `--version: string`

  Path param: ID of the Plugin Version (prefixed `pluginver_`), or `latest` for the newest one.

- `--organization-id: optional string`

  Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `beta_plugin_version: object`

  - `type: "plugin_version"`

    Always `plugin_version`.

  - `id: string`

    The version's ID.

  - `components: array of BetaPluginComponent`

    What the version contains; null when not enumerated.

    - `type: "agent" or "cli" or "command" or 3 more`

      The kind of component.

      - `"agent"`

      - `"cli"`

      - `"command"`

      - `"hook"`

      - `"mcp_server"`

      - `"skill"`

    - `description: string`

      What the component declares about itself; always null for MCP servers, hooks, and CLIs.

    - `name: string`

      The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.

  - `content_scan: object`

    This version's content scan; null when it has not been scanned.

    - `assessment: "fail" or "pass" or "unknown" or "warn"`

      The scan's verdict; set only when `status` is `completed`.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"warn"`

    - `reason: string`

      The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Null on a `pass`, whenever `assessment` is null, and when no mechanism is reported for the verdict.

    - `status: "completed" or "errored" or "processing"`

      `processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run or its outcome cannot be read.

      - `"completed"`

      - `"errored"`

      - `"processing"`

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `created_by: BetaPluginUserActor or BetaPluginAPIActor`

    Who uploaded this version; null when not recorded.

    - `beta_plugin_user_actor: object`

      - `type: "user_actor"`

        A member of the organization.

      - `email_address: string`

        The member's email address; may be null, for example when they are no longer a member of the organization.

      - `user_id: string`

        The member's User ID.

    - `beta_plugin_api_actor: object`

      - `type: "api_actor"`

        An Admin API key, in the same form the Compliance API activity feed uses for it.

      - `api_key_id: string`

        The key's ID.

  - `description: string`

    The manifest's description; null when it declares none.

  - `display_name: string`

    The manifest's display name; null when it declares none.

  - `manifest_version: string`

    The version string the manifest declares; null when it declares none.

  - `plugin_id: string`

    The Plugin's ID.

  - `reach: "contained" or "privileged" or "remote"`

    How far the version reaches: `remote`, `privileged` or `contained`, as on the Plugin; null when not classifiable.

    - `"contained"`

    - `"privileged"`

    - `"remote"`

  - `release_notes: string`

    As supplied with the upload; null when none were supplied.

#### Example

```bash
ant beta:organization:plugins:versions retrieve \
  --api-key my-anthropic-api-key \
  --plugin-id plugin_id \
  --version version
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

`$ ant beta:organization:plugins:versions download`

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

- `--plugin-id: string`

  Path param: ID of the Plugin (prefixed `plugin_`).

- `--version: string`

  Path param: ID of the Plugin Version (prefixed `pluginver_`). `latest` is not accepted here.

- `--organization-id: optional string`

  Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `unnamed_schema_3: file path`

#### Example

```bash
ant beta:organization:plugins:versions download \
  --api-key my-anthropic-api-key \
  --plugin-id plugin_id \
  --version version
```

## Beta › Organization › Plugins › Installation Settings

### List Plugin Installation Settings

`$ ant beta:organization:plugins:installation-settings list`

**GET** `/v1/organizations/plugins/{plugin_id}/installation_settings`

List an organization-owned Plugin's installation settings, which say which
members it is for, most recently created first.

The list holds the Plugin's own organization-wide setting (absent while the Plugin
inherits its marketplace's default) and each RBAC Group's own setting. A
member-owned Plugin has shares instead, so this path returns 404 for one.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `--plugin-id: string`

  Path param: ID of the Plugin (prefixed `plugin_`).

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `100`.

  minimum: 1, maximum: 100

- `--organization-id: optional string`

  Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `--page: optional string`

  Query param: Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

- `--target-type: optional "organization" or "rbac_group"`

  Query param: Only settings for this kind of target: `organization` (the organization-wide setting) or `rbac_group` (an RBAC Group's).

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `BetaPluginInstallationSettingList: object`

  - `data: array of BetaPluginInstallationSetting`

    - `type: "plugin_installation_setting"`

      Always `plugin_installation_setting`.

    - `created_at: string`

      When the target was first given a setting for this Plugin.

      format: date-time

    - `installation_preference: "auto_install" or "available" or "not_available" or "required"`

      The setting the target holds for this Plugin. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

      - `"auto_install"`

      - `"available"`

      - `"not_available"`

      - `"required"`

    - `plugin_id: string`

      The Plugin's ID.

    - `target: BetaPluginTargetOrganization or BetaPluginTargetRBACGroup or BetaPluginTargetOrganizationMember`

      Whose setting this is: `organization` (the Plugin's own organization-wide setting) or `rbac_group` (one RBAC Group's own setting); `organization_member` does not occur here.

      - `beta_plugin_target_organization: object`

        - `type: "organization"`

          Every member of the organization.

      - `beta_plugin_target_rbac_group: object`

        - `type: "rbac_group"`

          An RBAC Group.

        - `rbac_group_id: string`

          The RBAC Group's ID.

      - `beta_plugin_target_organization_member: object`

        - `type: "organization_member"`

          One member of the organization.

        - `user_id: string`

          The member's User ID.

    - `updated_at: string`

      When its setting last changed.

      format: date-time

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### Example

```bash
ant beta:organization:plugins:installation-settings list \
  --api-key my-anthropic-api-key \
  --plugin-id plugin_id
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

`$ ant beta:organization:plugins:installation-settings set`

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

- `--plugin-id: string`

  Path param: ID of the Plugin (prefixed `plugin_`).

- `--target: string`

  Path param: The target whose setting is written: the literal `organization` for the Plugin's organization-wide setting, or an RBAC Group's ID (prefixed `rbac_group_`) for that group's own setting. Writing the `organization` target stops the Plugin from inheriting its marketplace's default, even when the value written equals that default.

- `--installation-preference: "auto_install" or "available" or "not_available" or "required"`

  Body param: The installation setting the target is to hold for this Plugin: one of `required`, `auto_install`, `available`, `not_available`.

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `beta_plugin_installation_setting: object`

  The installation setting an organization-owned Plugin holds for one
  target. It has no ID of its own: it is addressed by the Plugin's ID and the
  target.

  - `type: "plugin_installation_setting"`

    Always `plugin_installation_setting`.

  - `created_at: string`

    When the target was first given a setting for this Plugin.

    format: date-time

  - `installation_preference: "auto_install" or "available" or "not_available" or "required"`

    The setting the target holds for this Plugin. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `"auto_install"`

    - `"available"`

    - `"not_available"`

    - `"required"`

  - `plugin_id: string`

    The Plugin's ID.

  - `target: BetaPluginTargetOrganization or BetaPluginTargetRBACGroup or BetaPluginTargetOrganizationMember`

    Whose setting this is: `organization` (the Plugin's own organization-wide setting) or `rbac_group` (one RBAC Group's own setting); `organization_member` does not occur here.

    - `beta_plugin_target_organization: object`

      - `type: "organization"`

        Every member of the organization.

    - `beta_plugin_target_rbac_group: object`

      - `type: "rbac_group"`

        An RBAC Group.

      - `rbac_group_id: string`

        The RBAC Group's ID.

    - `beta_plugin_target_organization_member: object`

      - `type: "organization_member"`

        One member of the organization.

      - `user_id: string`

        The member's User ID.

  - `updated_at: string`

    When its setting last changed.

    format: date-time

#### Example

```bash
ant beta:organization:plugins:installation-settings set \
  --api-key my-anthropic-api-key \
  --plugin-id plugin_id \
  --target target \
  --installation-preference required
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

`$ ant beta:organization:plugins:installation-settings remove`

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

- `--plugin-id: string`

  Path param: ID of the Plugin (prefixed `plugin_`).

- `--target: string`

  Path param: The target whose own setting is removed: the literal `organization` for the Plugin's organization-wide setting, or an RBAC Group's ID (prefixed `rbac_group_`) for that group's own setting. Removing the `organization` setting returns the Plugin to its marketplace's default.

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `beta_deleted_plugin_installation_setting: object`

  Confirmation that one target's installation setting was removed, naming
  the Plugin and the target in place of an ID.

  - `type: "plugin_installation_setting_deleted"`

    Always `plugin_installation_setting_deleted`.

  - `plugin_id: string`

    The Plugin's ID.

  - `target: BetaPluginTargetOrganization or BetaPluginTargetRBACGroup or BetaPluginTargetOrganizationMember`

    Whose setting was removed.

    - `beta_plugin_target_organization: object`

      - `type: "organization"`

        Every member of the organization.

    - `beta_plugin_target_rbac_group: object`

      - `type: "rbac_group"`

        An RBAC Group.

      - `rbac_group_id: string`

        The RBAC Group's ID.

    - `beta_plugin_target_organization_member: object`

      - `type: "organization_member"`

        One member of the organization.

      - `user_id: string`

        The member's User ID.

#### Example

```bash
ant beta:organization:plugins:installation-settings remove \
  --api-key my-anthropic-api-key \
  --plugin-id plugin_id \
  --target target
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

`$ ant beta:organization:plugins:shares list`

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

- `--plugin-id: string`

  Path param: ID of the Plugin (prefixed `plugin_`).

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `100`.

  minimum: 1, maximum: 100

- `--organization-id: optional string`

  Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `--page: optional string`

  Query param: Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

- `--target-type: optional "organization" or "organization_member" or "rbac_group"`

  Query param: Only shares with this kind of target: `organization` (every member), `rbac_group` (one RBAC Group), or `organization_member` (one member).

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `BetaPluginShareList: object`

  - `data: array of BetaPluginShare`

    - `type: "plugin_share"`

      Always `plugin_share`.

    - `granted_at: string`

      When the share was given; a share whose role is later changed in claude.ai is re-granted and carries the time of that change.

      format: date-time

    - `plugin_id: string`

      The Plugin's ID.

    - `target: BetaPluginTargetOrganization or BetaPluginTargetRBACGroup or BetaPluginTargetOrganizationMember`

      Who the Plugin is shared with: `organization` (every member), `rbac_group` (one RBAC Group), or `organization_member` (one member).

      - `beta_plugin_target_organization: object`

        - `type: "organization"`

          Every member of the organization.

      - `beta_plugin_target_rbac_group: object`

        - `type: "rbac_group"`

          An RBAC Group.

        - `rbac_group_id: string`

          The RBAC Group's ID.

      - `beta_plugin_target_organization_member: object`

        - `type: "organization_member"`

          One member of the organization.

        - `user_id: string`

          The member's User ID.

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### Example

```bash
ant beta:organization:plugins:shares list \
  --api-key my-anthropic-api-key \
  --plugin-id plugin_id
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

`$ ant beta:organization:plugin-marketplaces list`

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

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  minimum: 1, maximum: 1000

- `--organization-id: optional string`

  Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `--owner-type: optional "organization" or "user"`

  Query param: `organization` for the organization's plugin marketplaces, `user` for members' personal plugin marketplaces.

- `--page: optional string`

  Query param: Optionally set to the `next_page` token from the previous response.

  maxLength: 2048

- `--source: optional "directory" or "github" or "gitlab" or 2 more`

  Query param: Only plugin marketplaces with this `source`: `manual` for those whose Plugins are uploaded; `github`, `gitlab` or `public_git` for those synchronized from a Git repository. `directory` (Anthropic's catalog) is never listed here.

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `BetaPluginMarketplaceList: object`

  - `data: array of BetaPluginMarketplace`

    - `type: "plugin_marketplace"`

      Always `plugin_marketplace`.

    - `id: string`

      The plugin marketplace's ID, prefixed `marketplace_`.

    - `created_at: string`

      RFC 3339.

      format: date-time

    - `default_installation_preference: "auto_install" or "available" or "not_available" or "required"`

      Organization plugin marketplace: the organization-wide setting every Plugin in it with no setting of its own gets. Null for a member's personal plugin marketplace. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

      - `"auto_install"`

      - `"available"`

      - `"not_available"`

      - `"required"`

    - `last_sync_ended_at: string`

      RFC 3339. When the most recent synchronization attempt to finish did so, whatever its outcome; for a repository plugin marketplace no synchronization has run on yet, when it was created. Null for a plugin marketplace that is not synchronized from a repository.

      format: date-time

    - `last_sync_read_sha: string`

      The commit the last synchronization attempt that reached the repository read, whether or not its content was then accepted (see `sync_status`); an attempt that ends `failed_auth` or `failed_transient` leaves it unchanged. Null until an attempt has first read the repository, and for a plugin marketplace that is not synchronized from a repository.

    - `name: string`

      Fixed for the plugin marketplace's lifetime.

    - `owner: BetaPluginOwnerOrganization or BetaPluginOwnerUser`

      The organization, or the member whose personal plugin marketplace it is.

      - `beta_plugin_owner_organization: object`

        - `type: "organization"`

          The Plugin lives in a plugin marketplace the organization owns.

      - `beta_plugin_owner_user: object`

        - `type: "user"`

          The Plugin lives in one member's personal plugin marketplace.

        - `user_id: string`

          The member's User ID.

    - `source: "directory" or "github" or "gitlab" or 2 more`

      Where the plugin marketplace's Plugins come from: `manual` when they are uploaded; `github`, `gitlab` or `public_git` when they are synchronized from the Git repository the owner connected, into which nothing can be uploaded; `directory` is Anthropic's own catalog, which this API does not list. A value this API does not yet name is returned as stored.

      - `"directory"`

      - `"github"`

      - `"gitlab"`

      - `"manual"`

      - `"public_git"`

    - `sync_status: "failed_auth" or "failed_content" or "failed_limits" or 3 more`

      Outcome of the plugin marketplace's most recent synchronization: one of `success`, `in_progress`, `failed_content`, `failed_transient`, `failed_auth`, `failed_limits`; a value this API does not yet name is returned as stored. Null until a synchronization is first attempted — so always for a `manual` plugin marketplace.

      - `"failed_auth"`

      - `"failed_content"`

      - `"failed_limits"`

      - `"failed_transient"`

      - `"in_progress"`

      - `"success"`

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### Example

```bash
ant beta:organization:plugin-marketplaces list \
  --api-key my-anthropic-api-key
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

`$ ant beta:organization:plugin-marketplaces retrieve`

**GET** `/v1/organizations/plugin_marketplaces/{marketplace_id}`

Retrieve a plugin marketplace by ID.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `--marketplace-id: string`

  Path param: ID of the plugin marketplace (prefixed `marketplace_`).

- `--organization-id: optional string`

  Query param: For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `beta_plugin_marketplace: object`

  - `type: "plugin_marketplace"`

    Always `plugin_marketplace`.

  - `id: string`

    The plugin marketplace's ID, prefixed `marketplace_`.

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `default_installation_preference: "auto_install" or "available" or "not_available" or "required"`

    Organization plugin marketplace: the organization-wide setting every Plugin in it with no setting of its own gets. Null for a member's personal plugin marketplace. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `"auto_install"`

    - `"available"`

    - `"not_available"`

    - `"required"`

  - `last_sync_ended_at: string`

    RFC 3339. When the most recent synchronization attempt to finish did so, whatever its outcome; for a repository plugin marketplace no synchronization has run on yet, when it was created. Null for a plugin marketplace that is not synchronized from a repository.

    format: date-time

  - `last_sync_read_sha: string`

    The commit the last synchronization attempt that reached the repository read, whether or not its content was then accepted (see `sync_status`); an attempt that ends `failed_auth` or `failed_transient` leaves it unchanged. Null until an attempt has first read the repository, and for a plugin marketplace that is not synchronized from a repository.

  - `name: string`

    Fixed for the plugin marketplace's lifetime.

  - `owner: BetaPluginOwnerOrganization or BetaPluginOwnerUser`

    The organization, or the member whose personal plugin marketplace it is.

    - `beta_plugin_owner_organization: object`

      - `type: "organization"`

        The Plugin lives in a plugin marketplace the organization owns.

    - `beta_plugin_owner_user: object`

      - `type: "user"`

        The Plugin lives in one member's personal plugin marketplace.

      - `user_id: string`

        The member's User ID.

  - `source: "directory" or "github" or "gitlab" or 2 more`

    Where the plugin marketplace's Plugins come from: `manual` when they are uploaded; `github`, `gitlab` or `public_git` when they are synchronized from the Git repository the owner connected, into which nothing can be uploaded; `directory` is Anthropic's own catalog, which this API does not list. A value this API does not yet name is returned as stored.

    - `"directory"`

    - `"github"`

    - `"gitlab"`

    - `"manual"`

    - `"public_git"`

  - `sync_status: "failed_auth" or "failed_content" or "failed_limits" or 3 more`

    Outcome of the plugin marketplace's most recent synchronization: one of `success`, `in_progress`, `failed_content`, `failed_transient`, `failed_auth`, `failed_limits`; a value this API does not yet name is returned as stored. Null until a synchronization is first attempted — so always for a `manual` plugin marketplace.

    - `"failed_auth"`

    - `"failed_content"`

    - `"failed_limits"`

    - `"failed_transient"`

    - `"in_progress"`

    - `"success"`

#### Example

```bash
ant beta:organization:plugin-marketplaces retrieve \
  --api-key my-anthropic-api-key \
  --marketplace-id marketplace_id
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

`$ ant beta:organization:plugin-marketplaces update`

**POST** `/v1/organizations/plugin_marketplaces/{marketplace_id}`

Set the default installation setting of one of the organization's own plugin
marketplaces. Every Plugin in it without a setting of its own gets this default as
its organization-wide setting, including Plugins added later.

Pass it as `default_installation_preference`. A member's personal marketplace
cannot be updated here (403).

**Accepted credentials:** an Admin API key with the `write:plugins` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

#### Parameters

- `--marketplace-id: string`

  Path param: ID of the plugin marketplace (prefixed `marketplace_`).

- `--default-installation-preference: "auto_install" or "available" or "not_available" or "required"`

  Body param: The organization-wide installation setting every Plugin in the marketplace without one of its own gets: one of `required`, `auto_install`, `available`, `not_available`. Once set it can be changed but not removed.

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `beta_plugin_marketplace: object`

  - `type: "plugin_marketplace"`

    Always `plugin_marketplace`.

  - `id: string`

    The plugin marketplace's ID, prefixed `marketplace_`.

  - `created_at: string`

    RFC 3339.

    format: date-time

  - `default_installation_preference: "auto_install" or "available" or "not_available" or "required"`

    Organization plugin marketplace: the organization-wide setting every Plugin in it with no setting of its own gets. Null for a member's personal plugin marketplace. One of `required`, `auto_install`, `available`, `not_available`; a value this API does not yet name is returned as stored.

    - `"auto_install"`

    - `"available"`

    - `"not_available"`

    - `"required"`

  - `last_sync_ended_at: string`

    RFC 3339. When the most recent synchronization attempt to finish did so, whatever its outcome; for a repository plugin marketplace no synchronization has run on yet, when it was created. Null for a plugin marketplace that is not synchronized from a repository.

    format: date-time

  - `last_sync_read_sha: string`

    The commit the last synchronization attempt that reached the repository read, whether or not its content was then accepted (see `sync_status`); an attempt that ends `failed_auth` or `failed_transient` leaves it unchanged. Null until an attempt has first read the repository, and for a plugin marketplace that is not synchronized from a repository.

  - `name: string`

    Fixed for the plugin marketplace's lifetime.

  - `owner: BetaPluginOwnerOrganization or BetaPluginOwnerUser`

    The organization, or the member whose personal plugin marketplace it is.

    - `beta_plugin_owner_organization: object`

      - `type: "organization"`

        The Plugin lives in a plugin marketplace the organization owns.

    - `beta_plugin_owner_user: object`

      - `type: "user"`

        The Plugin lives in one member's personal plugin marketplace.

      - `user_id: string`

        The member's User ID.

  - `source: "directory" or "github" or "gitlab" or 2 more`

    Where the plugin marketplace's Plugins come from: `manual` when they are uploaded; `github`, `gitlab` or `public_git` when they are synchronized from the Git repository the owner connected, into which nothing can be uploaded; `directory` is Anthropic's own catalog, which this API does not list. A value this API does not yet name is returned as stored.

    - `"directory"`

    - `"github"`

    - `"gitlab"`

    - `"manual"`

    - `"public_git"`

  - `sync_status: "failed_auth" or "failed_content" or "failed_limits" or 3 more`

    Outcome of the plugin marketplace's most recent synchronization: one of `success`, `in_progress`, `failed_content`, `failed_transient`, `failed_auth`, `failed_limits`; a value this API does not yet name is returned as stored. Null until a synchronization is first attempted — so always for a `manual` plugin marketplace.

    - `"failed_auth"`

    - `"failed_content"`

    - `"failed_limits"`

    - `"failed_transient"`

    - `"in_progress"`

    - `"success"`

#### Example

```bash
ant beta:organization:plugin-marketplaces update \
  --api-key my-anthropic-api-key \
  --marketplace-id marketplace_id \
  --default-installation-preference available
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

`$ ant beta:organization:plugin-marketplaces validate-repository`

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

- `--repository-url: string`

  Body param: The `https://` URL of a public repository on github.com that holds the marketplace. Any other host, a URL with credentials in it, or one that does not name a repository is a 400.

  minLength: 1

- `--ref: optional string`

  Body param: The branch to validate the tip of, or the full 40-character SHA of the commit to validate. When omitted, the branch a synchronization would read (usually the repository's default branch); if that is not the default branch, the report's `ref` says which branch was read. An empty string, or a value that is neither a branch name nor a 40-character SHA, is a 400.

  minLength: 1

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `beta_plugin_marketplace_validation_report: object`

  The outcome of validating plugin marketplace content: a report, not a
  stored object, so nothing in it can be retrieved afterwards.

  - `type: "plugin_marketplace_validation_report"`

    Always `plugin_marketplace_validation_report`.

  - `commit_sha: string`

    The full SHA of the commit that was validated: for a repository, the commit that was read; for an uploaded archive, the commit recorded in the archive's comment (as a Git host's download writes it; not verified), else null.

  - `manifest_error: string`

    Set when nothing could be validated: the repository or archive could not be read, or marketplace.json is missing, malformed or over a limit. Null otherwise.

  - `manifest_error_code: string`

    A stable identifier for `manifest_error`; null when that is.

  - `plugin_errors: array of BetaPluginMarketplaceValidationPluginError`

    One entry per plugin a synchronization would skip entirely, keyed by the plugin's name in marketplace.json.

    - `error: string`

      Why the plugin would be skipped by a synchronization.

    - `error_code: string`

      A stable identifier for the reason — the value to branch on.

    - `name: string`

      The plugin's name, as its entry in marketplace.json declares it.

  - `plugin_warnings: array of BetaPluginMarketplaceValidationPluginWarnings`

    One entry per plugin that would synchronize with some of its contents left out, keyed by the plugin's name in marketplace.json.

    - `name: string`

      The plugin's name, as its entry in marketplace.json declares it.

    - `warnings: array of BetaPluginMarketplaceValidationPluginWarning`

      The parts of the plugin a synchronization would leave out.

      - `error_code: string`

        A stable identifier for the kind of warning.

      - `message: string`

        What would be left out, and why.

  - `ref: string`

    For a repository, the branch that was read by name: the one requested, or else the branch a synchronization of this repository is set to read. Null when no branch is named or set and the repository's default branch was read, for a request by commit SHA, and for an uploaded archive.

  - `total_plugin_count: number`

    How many plugins marketplace.json declares; 0 when it could not be read.

  - `valid: boolean`

    True when marketplace.json is well-formed and no plugin would be skipped; warnings never make it false.

#### Example

```bash
ant beta:organization:plugin-marketplaces validate-repository \
  --api-key my-anthropic-api-key \
  --repository-url https://github.com/example-org/example-marketplace
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

`$ ant beta:organization:plugin-marketplaces validate-archive`

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

- `--archive: string`

  Body param: A .zip of the marketplace directory (its contents at the root, or wrapped in one folder as a Git host's download produces), sent as a file part with a filename; DEFLATE- or STORE-compressed, at most 32 MB. A part sent without a filename, a second archive part, or any other form field is a 400; a larger archive is a 413.

  format: binary

- `--beta: optional array of AnthropicBeta`

  Header param: This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

#### Returns

- `beta_plugin_marketplace_validation_report: object`

  The outcome of validating plugin marketplace content: a report, not a
  stored object, so nothing in it can be retrieved afterwards.

  - `type: "plugin_marketplace_validation_report"`

    Always `plugin_marketplace_validation_report`.

  - `commit_sha: string`

    The full SHA of the commit that was validated: for a repository, the commit that was read; for an uploaded archive, the commit recorded in the archive's comment (as a Git host's download writes it; not verified), else null.

  - `manifest_error: string`

    Set when nothing could be validated: the repository or archive could not be read, or marketplace.json is missing, malformed or over a limit. Null otherwise.

  - `manifest_error_code: string`

    A stable identifier for `manifest_error`; null when that is.

  - `plugin_errors: array of BetaPluginMarketplaceValidationPluginError`

    One entry per plugin a synchronization would skip entirely, keyed by the plugin's name in marketplace.json.

    - `error: string`

      Why the plugin would be skipped by a synchronization.

    - `error_code: string`

      A stable identifier for the reason — the value to branch on.

    - `name: string`

      The plugin's name, as its entry in marketplace.json declares it.

  - `plugin_warnings: array of BetaPluginMarketplaceValidationPluginWarnings`

    One entry per plugin that would synchronize with some of its contents left out, keyed by the plugin's name in marketplace.json.

    - `name: string`

      The plugin's name, as its entry in marketplace.json declares it.

    - `warnings: array of BetaPluginMarketplaceValidationPluginWarning`

      The parts of the plugin a synchronization would leave out.

      - `error_code: string`

        A stable identifier for the kind of warning.

      - `message: string`

        What would be left out, and why.

  - `ref: string`

    For a repository, the branch that was read by name: the one requested, or else the branch a synchronization of this repository is set to read. Null when no branch is named or set and the repository's default branch was read, for a request by commit SHA, and for an uploaded archive.

  - `total_plugin_count: number`

    How many plugins marketplace.json declares; 0 when it could not be read.

  - `valid: boolean`

    True when marketplace.json is well-formed and no plugin would be skipped; warnings never make it false.

#### Example

```bash
ant beta:organization:plugin-marketplaces validate-archive \
  --api-key my-anthropic-api-key \
  --archive 'Example data'
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
