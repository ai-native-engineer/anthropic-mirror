<!-- source: https://support.claude.com/en/articles/15505325-what-are-customer-managed-encryption-keys-cmek -->

# What are customer-managed encryption keys (CMEK)?

Updated over a week ago

Customer-managed encryption keys are available to eligible organizations on Enterprise plans and the Claude Platform.

A customer-managed encryption key (CMEK) lets your organization provision an encryption key in your own AWS KMS, Google Cloud KMS, or Azure Key Vault and have Anthropic use it to encrypt certain data in Claude, such as your team's chats, projects, and files. You keep full control of the key, and every operation Anthropic performs with your key is recorded in your cloud provider's audit logs. CMEK is optional, and your organization can choose to enable it in place of the default encryption Anthropic provides.

For complete details, including what's encrypted, what's disabled or changed, limitations, and setup guides for each cloud provider, see **[Customer-managed encryption keys on Claude API Docs](https://platform.claude.com/docs/en/manage-claude/cmek)**.

[I use Claude in Amazon Bedrock. Who do I contact for customer support inquiries?](https://support.claude.com/en/articles/7996921-i-use-claude-in-amazon-bedrock-who-do-i-contact-for-customer-support-inquiries)[API Key Best Practices: Keeping Your Keys Safe and Secure](https://support.claude.com/en/articles/9767949-api-key-best-practices-keeping-your-keys-safe-and-secure)[What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)[Use Claude for Microsoft 365 with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-microsoft-365-with-third-party-platforms)[Data retention practices for Mythos-class models](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)
