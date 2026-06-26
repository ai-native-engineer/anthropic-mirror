<!-- source: https://platform.claude.com/docs/en/api/admin/external_keys/delete -->

# Delete External Key
DELETE/v1/organizations/external_keys/{external_key_id}
Delete an external key config.
The request is rejected if any workspace still references this config.
##### Path ParametersExpand Collapse 
external_key_id: string
ID of the External Key to delete.
[](https://platform.claude.com/docs/en/api/admin/external_keys/delete#delete.external_key_id)
ID of the deleted External Key.
[](https://platform.claude.com/docs/en/api/admin/external_keys/delete#external_key_delete_response.id)
type: "external_key_deleted"
[](https://platform.claude.com/docs/en/api/admin/external_keys/delete#external_key_delete_response.type)
Delete External Key

curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"

  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"
