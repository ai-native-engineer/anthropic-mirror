<!-- source: https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve -->

# Get Service Account
GET/v1/organizations/service_accounts/{service_account_id}
Retrieve a service account by its ID (`svac_...`).
##### Path ParametersExpand Collapse 
service_account_id: string
ID of the service account.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#retrieve.service_account_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of string
Optional header to specify the beta version(s) you want to use.
To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#retrieve.anthropic-beta)
ServiceAccount object { id, archived_at, archived_by_actor_id, 8 more } 
Named non-human identity within the caller's organization.
A service account is a pure identity: name + org. Authorization lives on whatever references it (federation rules).
Tagged ID of the service account.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account.id)
archived_at: string
If set, this service account is archived.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account.archived_at)
archived_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that archived this service account.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account.archived_by_actor_id)
created_at: string
When this service account was created.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account.created_at)
created_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that created this service account.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account.created_by_actor_id)
description: string
Optional free-text description.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account.description)
name: string
Admin-chosen slug identifier.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account.name)
organization_role: "developer" or "admin"
Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.
"developer"
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account.organization_role%5B0%5D)
"admin"
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account.organization_role%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account.organization_role)
type: "service_account"
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account.type)
updated_at: string
When this service account was last updated.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account.updated_at)
updated_by_actor_id: string
Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account.updated_by_actor_id)
[](https://platform.claude.com/docs/en/api/admin/service_accounts/retrieve#service_account)
Get Service Account

curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "developer",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"

  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "developer",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
