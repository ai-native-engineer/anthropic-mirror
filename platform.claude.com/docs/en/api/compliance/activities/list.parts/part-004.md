<!-- source: https://platform.claude.com/docs/en/api/compliance/activities/list -->
<!-- part of: https://platform.claude.com/docs/en/api/compliance/activities/list -->

<!-- chunk-start -->

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

        - `email_address: optional string or null`

          format: email

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `type: optional "system_actor"`

          default: system_actor

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

      - `AdminAPIKeyActor object`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `ServiceAccountActor object`

        - `type: optional "service_account_actor"`

          default: service_account_actor

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

      - `ScimDirectorySyncActor object`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `type: optional "aws"`

              default: aws

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `type: optional "azure"`

              default: azure

            - `subscription_id: string`

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `type: optional "gcp"`

              default: gcp

            - `project_number: string`

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `type: optional "oidc"`

              default: oidc

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

    - `verification_id: string`

      Tagged ID of the verification the evidence was submitted for.

    - `verification_type: string`

      The type of verification the evidence was submitted for.

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `VerificationProgramApplicationCreated object`

    An organization applied to a verification program.

    - `type: optional "verification_program_application_created"`

      default: verification_program_application_created

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `type: optional "api_actor"`

          default: api_actor

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `UserActor object`

        - `type: optional "user_actor"`

          default: user_actor

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

      - `UnauthenticatedUserActor object`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `ip_address: string`

        - `user_agent: string`

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

        - `email_address: optional string or null`

          format: email

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `type: optional "system_actor"`

          default: system_actor

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

      - `AdminAPIKeyActor object`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `ServiceAccountActor object`

        - `type: optional "service_account_actor"`

          default: service_account_actor

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

      - `ScimDirectorySyncActor object`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `type: optional "aws"`

              default: aws

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `type: optional "azure"`

              default: azure

            - `subscription_id: string`

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `type: optional "gcp"`

              default: gcp

            - `project_number: string`

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `type: optional "oidc"`

              default: oidc

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

    - `program_slug: string`

      The verification program the organization applied to.

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `WorkspaceMemberSpendLimitCreated object`

    A per-member or workspace-default Claude Code spend limit was created.

    - `type: optional "workspace_member_spend_limit_created"`

      default: workspace_member_spend_limit_created

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `type: optional "api_actor"`

          default: api_actor

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `UserActor object`

        - `type: optional "user_actor"`

          default: user_actor

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

      - `UnauthenticatedUserActor object`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `ip_address: string`

        - `user_agent: string`

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

        - `email_address: optional string or null`

          format: email

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `type: optional "system_actor"`

          default: system_actor

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

      - `AdminAPIKeyActor object`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `ServiceAccountActor object`

        - `type: optional "service_account_actor"`

          default: service_account_actor

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

      - `ScimDirectorySyncActor object`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `type: optional "aws"`

              default: aws

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `type: optional "azure"`

              default: azure

            - `subscription_id: string`

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `type: optional "gcp"`

              default: gcp

            - `project_number: string`

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `type: optional "oidc"`

              default: oidc

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `account_id: optional string or null`

      Tagged ID of the user (null for workspace-wide default).

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `limit_action: optional string or null`

      The action taken when the limit is reached.

    - `limit_usd: optional number or null`

      The spend limit threshold in USD cents.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceMemberSpendLimitDeleted object`

    A per-member or workspace-default Claude Code spend limit was deleted.

    - `type: optional "workspace_member_spend_limit_deleted"`

      default: workspace_member_spend_limit_deleted

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `type: optional "api_actor"`

          default: api_actor

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `UserActor object`

        - `type: optional "user_actor"`

          default: user_actor

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

      - `UnauthenticatedUserActor object`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `ip_address: string`

        - `user_agent: string`

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

        - `email_address: optional string or null`

          format: email

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `type: optional "system_actor"`

          default: system_actor

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

      - `AdminAPIKeyActor object`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `ServiceAccountActor object`

        - `type: optional "service_account_actor"`

          default: service_account_actor

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

      - `ScimDirectorySyncActor object`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `type: optional "aws"`

              default: aws

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `type: optional "azure"`

              default: azure

            - `subscription_id: string`

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `type: optional "gcp"`

              default: gcp

            - `project_number: string`

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `type: optional "oidc"`

              default: oidc

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `account_id: optional string or null`

      Tagged ID of the user (null for workspace-wide default).

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `spend_limit_id: optional string or null`

      UUID of the deleted spend limit.

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceMemberSpendLimitUpdated object`

    A per-member Claude Code spend limit amount was updated.

    - `type: optional "workspace_member_spend_limit_updated"`

      default: workspace_member_spend_limit_updated

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `type: optional "api_actor"`

          default: api_actor

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `UserActor object`

        - `type: optional "user_actor"`

          default: user_actor

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

      - `UnauthenticatedUserActor object`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `ip_address: string`

        - `user_agent: string`

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

        - `email_address: optional string or null`

          format: email

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `type: optional "system_actor"`

          default: system_actor

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

      - `AdminAPIKeyActor object`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `ServiceAccountActor object`

        - `type: optional "service_account_actor"`

          default: service_account_actor

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

      - `ScimDirectorySyncActor object`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `type: optional "aws"`

              default: aws

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `type: optional "azure"`

              default: azure

            - `subscription_id: string`

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `type: optional "gcp"`

              default: gcp

            - `project_number: string`

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `type: optional "oidc"`

              default: oidc

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `account_id: optional string or null`

      Tagged ID of the user (null for workspace-wide default).

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `new_limit_usd: optional number or null`

      The new spend limit threshold in USD cents.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `spend_limit_id: optional string or null`

      UUID of the spend limit.

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceSpendLimitAlertEmailsUpdated object`

    Spend limit alert email recipients were updated for a workspace.

    - `type: optional "workspace_spend_limit_alert_emails_updated"`

      default: workspace_spend_limit_alert_emails_updated

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `type: optional "api_actor"`

          default: api_actor

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `UserActor object`

        - `type: optional "user_actor"`

          default: user_actor

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

      - `UnauthenticatedUserActor object`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `ip_address: string`

        - `user_agent: string`

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

        - `email_address: optional string or null`

          format: email

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `type: optional "system_actor"`

          default: system_actor

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

      - `AdminAPIKeyActor object`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `ServiceAccountActor object`

        - `type: optional "service_account_actor"`

          default: service_account_actor

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

      - `ScimDirectorySyncActor object`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `type: optional "aws"`

              default: aws

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `type: optional "azure"`

              default: azure

            - `subscription_id: string`

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `type: optional "gcp"`

              default: gcp

            - `project_number: string`

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `type: optional "oidc"`

              default: oidc

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `alert_emails: optional array of string or null`

      Updated list of alert email addresses.

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceSpendLimitCreated object`

    A workspace-level API spend limit was created.

    - `type: optional "workspace_spend_limit_created"`

      default: workspace_spend_limit_created

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `type: optional "api_actor"`

          default: api_actor

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `UserActor object`

        - `type: optional "user_actor"`

          default: user_actor

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

      - `UnauthenticatedUserActor object`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `ip_address: string`

        - `user_agent: string`

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

        - `email_address: optional string or null`

          format: email

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `type: optional "system_actor"`

          default: system_actor

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

      - `AdminAPIKeyActor object`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `ServiceAccountActor object`

        - `type: optional "service_account_actor"`

          default: service_account_actor

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

      - `ScimDirectorySyncActor object`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `type: optional "aws"`

              default: aws

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `type: optional "azure"`

              default: azure

            - `subscription_id: string`

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `type: optional "gcp"`

              default: gcp

            - `project_number: string`

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `type: optional "oidc"`

              default: oidc

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `limit_action: optional string or null`

      The action taken when the limit is reached (notify_only or notify_and_pause).

    - `limit_usd: optional number or null`

      The spend limit threshold in USD cents.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceSpendLimitDeleted object`

    A workspace-level API spend limit was deleted.

    - `type: optional "workspace_spend_limit_deleted"`

      default: workspace_spend_limit_deleted

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `type: optional "api_actor"`

          default: api_actor

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `UserActor object`

        - `type: optional "user_actor"`

          default: user_actor

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

      - `UnauthenticatedUserActor object`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `ip_address: string`

        - `user_agent: string`

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

        - `email_address: optional string or null`

          format: email

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `type: optional "system_actor"`

          default: system_actor

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

      - `AdminAPIKeyActor object`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

      - `ServiceAccountActor object`

        - `type: optional "service_account_actor"`

          default: service_account_actor

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

      - `ScimDirectorySyncActor object`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `type: optional "aws"`

              default: aws

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `type: optional "azure"`

              default: azure

            - `subscription_id: string`

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `type: optional "gcp"`

              default: gcp

            - `project_number: string`

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `type: optional "oidc"`

              default: oidc

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `spend_limit_id: optional string or null`

      UUID of the deleted spend limit.

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

- `first_id: optional string or null`

- `has_more: optional boolean`

  default: false

- `last_id: optional string or null`

## Example

```bash
curl https://api.anthropic.com/v1/compliance/activities \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Response (200)

```json
{
  "data": [
    {
      "actor": {
        "api_key_id": "api_key_id",
        "ip_address": "ip_address",
        "user_agent": "user_agent",
        "type": "api_actor"
      },
      "decision": "blocked",
      "id": "id",
      "abuse_session_id": "abuse_session_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "organization_id": "organization_id",
      "organization_uuid": "organization_uuid",
      "type": "abuse_decision_received"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```
