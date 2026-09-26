<!-- source: https://claude.com/form/org-uuid-intake -->

# Org UUID Intake

Please provide the Org UUIDs to be associated to your contract.

## How to identify your account IDs

Provided for reference.

* **Anthropic:**
  + Claude.ai: if you have a pre-existing account to upgrade, log in to your Anthropic account, go to Account Settings, and copy the Organization ID.
  + API: if you intend to use Anthropic’s API, you must provide at least one ID. Log into your Anthropic Console account, navigate to Organization Settings, and copy the Organization ID. New accounts may be created at [platform.claude.com](http://platform.claude.com).
* **AWS:** Provide the 12-digit AWS Account ID(s) 0000-0000-0000:
  + Claude for Enterprise on AWS: AWS Marketplace ID
  + Claude Platform on AWS: AWS Marketplace ID
  + Bedrock API: AWS Bedrock ID
  + If you have multiple AWS accounts, provide all of them — each receives its own offers, and separate offers are currently required for each Claude model. For multiple AWS IDs, AWS’s Manage Entitlements feature is recommended: provide an overarching parent / “Payer ID” (same 12-digit structure); the parent account accepts the offer and then distributes grants to linked accounts so they inherit the discount. See [AWS Manage Entitlements FAQ](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-faq.html).
* **GCP:** Provide the 18-digit alphanumeric Vertex Billing Account ID 9000A00-000B0C-000D00); if purchasing Provisioned Throughput, also the Project Number and Region. If you have multiple GCP Billing Accounts, provide all of them — one offer covers multiple Claude models, and each account receives its own offer.
* **Azure:** provide the Billing Account ID; for help locating these, follow Microsoft’s instructions: [how to find your billing account ID](https://learn.microsoft.com/en-us/marketplace/private-offers-pre-check#locate-your-billing-account-id). ID formats — EA: 8 numeric digits; MCA: aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb:aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb\_2019-05-31.
