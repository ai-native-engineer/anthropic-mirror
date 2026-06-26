<!-- source: https://support.claude.com/en/articles/13015708-access-the-compliance-api -->

# Access the Compliance API

Updated over 2 weeks ago

The Compliance API is generally available to Claude Enterprise plans, excluding Public Sector organizations, and Claude Platform customers.

## Claude Enterprise plan customers

Enterprise plan Primary Owners can enable the Compliance API by navigating to **[Organization settings > API](https://claude.ai/admin-settings/api-access)** and clicking "Enable" under **Compliance API**.

Once the Compliance API is enabled, create new compliance access keys by clicking "+ Create key":

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1867701300/8a148e524f7ac2b1295d87005656/bd069690-3edf-4c51-ab66-09c73db81328?expires=1782459900&signature=4249fe23bd6242de3c1f7054716ad89295196986a75fb4a5ce14cb1f730ba8d6&req=dSghEc5%2BnIJfWfMW1HO4zdjcO0o43MQaLb9AVN3cSSGVLFiizq59%2BtDsi2oH%0AGKr%2FQJ8HV1q1IKRMauQ%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1867701300/8a148e524f7ac2b1295d87005656/bd069690-3edf-4c51-ab66-09c73db81328?expires=1782459900&signature=4249fe23bd6242de3c1f7054716ad89295196986a75fb4a5ce14cb1f730ba8d6&req=dSghEc5%2BnIJfWfMW1HO4zdjcO0o43MQaLb9AVN3cSSGVLFiizq59%2BtDsi2oH%0AGKr%2FQJ8HV1q1IKRMauQ%3D%0A)

Creating a compliance access key will allow you to start pulling activity feed events, chat data, and file content programmatically.

## Claude Platform customers

Claude Platform admins can enable the Compliance API from the Claude Platform. For setup instructions, see **[Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api)** in the Claude API Docs.

## Audit log events in the Compliance API

The Compliance API now includes audit log events, giving you a full view across all your Claude deployments. To see which events are recorded via audit logs, refer to **[How to access audit logs](https://support.claude.com/en/articles/9970975-how-to-access-audit-logs#h_41cdad187a)**.

## Compliance API security integrations

Security and compliance platforms have built integrations on top of the Claude Compliance API, so your team can monitor Claude activity within the tools you already use. Learn more about **[Compliance API integrations](https://support.claude.com/en/articles/15167101-get-started-with-claude-compliance-api-integrations)**.

## Compliance API technical documentation

For setup instructions and endpoint details, see the **[Compliance API guide](https://platform.claude.com/docs/en/manage-claude/compliance-api)** and the **[Compliance API reference](https://platform.claude.com/docs/en/api/compliance)** on Claude API Docs.

[Enforce network-level access control with Tenant Restrictions](https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions)[Monitor Claude Cowork activity with OpenTelemetry](https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry)[Claude Cowork desktop architecture overview](https://support.claude.com/en/articles/14479288-claude-cowork-desktop-architecture-overview)[Get started with Claude Compliance API integrations](https://support.claude.com/en/articles/15167101-get-started-with-claude-compliance-api-integrations)[What are customer-managed encryption keys (CMEK)?](https://support.claude.com/en/articles/15505325-what-are-customer-managed-encryption-keys-cmek)
