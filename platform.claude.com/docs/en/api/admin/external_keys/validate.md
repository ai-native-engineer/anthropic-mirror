<!-- source: https://platform.claude.com/docs/en/api/admin/external_keys/validate -->

# Validate External Key
POST/v1/organizations/external_keys/{external_key_id}/validate
Validate an external key config against the customer's KMS.
Anthropic performs an encrypt/decrypt roundtrip against the configured KMS key and waits up to 30 seconds for the result. The response status is `success` if the roundtrip succeeded, or `failure` with an error message if it failed or timed out.
##### Path ParametersExpand Collapse 
external_key_id: string
ID of the External Key to validate.
[](https://platform.claude.com/docs/en/api/admin/external_keys/validate#validate.external_key_id)
error: string
Error message when status is `failure`. Null otherwise.
[](https://platform.claude.com/docs/en/api/admin/external_keys/validate#external_key_validate_response.error)
status: "success" or "failure"
`success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.
"success"
[](https://platform.claude.com/docs/en/api/admin/external_keys/validate#external_key_validate_response.status%5B0%5D)
"failure"
[](https://platform.claude.com/docs/en/api/admin/external_keys/validate#external_key_validate_response.status%5B1%5D)
[](https://platform.claude.com/docs/en/api/admin/external_keys/validate#external_key_validate_response.status)
type: "external_key_validation"
[](https://platform.claude.com/docs/en/api/admin/external_keys/validate#external_key_validate_response.type)
Validate External Key

curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID/validate \
    -X POST \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"

  "error": null,
  "status": "success",
  "type": "external_key_validation"

  "error": null,
  "status": "success",
  "type": "external_key_validation"
