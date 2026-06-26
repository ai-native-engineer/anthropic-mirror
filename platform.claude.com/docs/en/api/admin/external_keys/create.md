<!-- source: https://platform.claude.com/docs/en/api/admin/external_keys/create -->

# Create External Key
POST/v1/organizations/external_keys
Create an external key config owned by the caller's organization.
#####  Body ParametersJSONExpand Collapse 
display_name: string
Human-friendly display name.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.display_name)
provider_config: object { kms_arn, role_arn, type, region }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more } 
KMS provider identity and auth coordinates.
Aws object { kms_arn, role_arn, type, region } 
kms_arn: string
Full ARN of the AWS KMS key.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B0%5D.kms_arn)
role_arn: string
IAM role ARN that Anthropic assumes to access the KMS key.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B0%5D.role_arn)
type: "aws"
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B0%5D.type)
region: optional string
AWS region. Derived from kms_arn if omitted.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B0%5D.region)
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B0%5D)
Gcp object { key_name, type } 
key_name: string
Full resource name of the Cloud KMS key.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B1%5D.key_name)
type: "gcp"
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B1%5D)
Azure object { key_name, tenant_id, type, 2 more } 
key_name: string
Name of the key within the vault.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B2%5D.key_name)
tenant_id: string
Azure AD tenant ID.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B2%5D.tenant_id)
type: "azure"
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B2%5D.type)
vault_uri: string
Key Vault URI.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B2%5D.vault_uri)
client_id: optional string
Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B2%5D.client_id)
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.provider_config)
geo: optional "us"
Data residency geo. Only `us` is supported.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#create.geo)
Tagged ID of the external key config.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.id)
created_at: string
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.created_at)
display_name: string
Human-friendly display name.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.display_name)
geo: string
Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.geo)
provider_config: object { kms_arn, role_arn, type, region }  or object { key_name, type }  or object { key_name, tenant_id, type, 2 more } 
KMS provider identity and auth coordinates.
Aws object { kms_arn, role_arn, type, region } 
kms_arn: string
Full ARN of the AWS KMS key.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B0%5D.kms_arn)
role_arn: string
IAM role ARN that Anthropic assumes to access the KMS key.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B0%5D.role_arn)
type: "aws"
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B0%5D.type)
region: optional string
AWS region. Derived from kms_arn if omitted.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B0%5D.region)
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B0%5D)
Gcp object { key_name, type } 
key_name: string
Full resource name of the Cloud KMS key.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B1%5D.key_name)
type: "gcp"
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B1%5D.type)
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B1%5D)
Azure object { key_name, tenant_id, type, 2 more } 
key_name: string
Name of the key within the vault.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B2%5D.key_name)
tenant_id: string
Azure AD tenant ID.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B2%5D.tenant_id)
type: "azure"
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B2%5D.type)
vault_uri: string
Key Vault URI.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B2%5D.vault_uri)
client_id: optional string
Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B2%5D.client_id)
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config%5B2%5D)
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.provider_config)
type: "external_key"
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.type)
updated_at: string
[](https://platform.claude.com/docs/en/api/admin/external_keys/create#external_key_create_response.updated_at)
Create External Key

curl https://api.anthropic.com/v1/organizations/external_keys \
    -H 'Content-Type: application/json' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "display_name": "x",
          "provider_config": {
            "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
            "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek",
            "type": "aws"
        }'

  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek",
    "type": "aws",
    "region": "us-east-1"
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"

  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek",
    "type": "aws",
    "region": "us-east-1"
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
