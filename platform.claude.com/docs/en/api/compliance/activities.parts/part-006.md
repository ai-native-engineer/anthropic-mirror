<!-- source: https://platform.claude.com/docs/en/api/compliance/activities -->
<!-- part of: https://platform.claude.com/docs/en/api/compliance/activities -->

<!-- chunk-start -->

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the request was scoped to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace. May differ from the workspace the store was created in when the store is account-scoped.

  - `PlatformMemoryStoreDeleted object`

    An agent memory store was deleted. Memory content removal may complete asynchronously for very large stores.

    - `type: optional "platform_memory_store_deleted"`

      default: platform_memory_store_deleted

    - `actor: object or object or object or 8 more`

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

    - `memory_store_id: string`

      Tagged memory store ID, e.g. "memstore_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the request was scoped to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace. May differ from the workspace the store was created in when the store is account-scoped.

  - `PlatformMemoryStoreUpdated object`

    An agent memory store's name, description, or metadata was updated.

    - `type: optional "platform_memory_store_updated"`

      default: platform_memory_store_updated

    - `actor: object or object or object or 8 more`

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

    - `memory_store_id: string`

      Tagged memory store ID, e.g. "memstore_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the request was scoped to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace. May differ from the workspace the store was created in when the store is account-scoped.

  - `PlatformMemoryUpdated object`

    An agent memory document's content or path was updated.

    - `type: optional "platform_memory_updated"`

      default: platform_memory_updated

    - `actor: object or object or object or 8 more`

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

    - `memory_id: string`

      Tagged memory ID, e.g. "mem_01HX...".

    - `memory_store_id: string`

      Tagged ID of the memory store the memory belongs to, e.g. "memstore_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `memory_version_id: optional string or null`

      Tagged ID of the memory version produced by this change, e.g. "memver_01HX...". Links this event to the version history.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the request was scoped to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace. May differ from the workspace the store was created in when the store is account-scoped.

  - `PlatformMemoryVersionRedacted object`

    A historical version of an agent memory document was redacted. Redaction scrubs the stored content of a specific version while preserving the version's existence in the history.

    - `type: optional "platform_memory_version_redacted"`

      default: platform_memory_version_redacted

    - `actor: object or object or object or 8 more`

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

    - `memory_id: string`

      Tagged ID of the memory the version belongs to, e.g. "mem_01HX...".

    - `memory_store_id: string`

      Tagged ID of the memory store the memory belongs to, e.g. "memstore_01HX...".

    - `memory_version_id: string`

      Tagged memory version ID, e.g. "memver_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the request was scoped to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace. May differ from the workspace the store was created in when the store is account-scoped.

  - `PlatformOAuthAppCreated object`

    An OAuth app was created.

    - `type: optional "platform_oauth_app_created"`

      default: platform_oauth_app_created

    - `actor: object or object or object or 8 more`

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

    - `oauth_app_id: string`

      Tagged ID of the created app

    - `workspace_id: string`

      Tagged ID of the workspace the app is scoped to

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformOAuthAppRevoked object`

    An OAuth app was revoked.

    - `type: optional "platform_oauth_app_revoked"`

      default: platform_oauth_app_revoked

    - `actor: object or object or object or 8 more`

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

    - `oauth_app_id: string`

      Tagged ID of the revoked app

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformOAuthAppUpdated object`

    An OAuth app was updated.

    - `type: optional "platform_oauth_app_updated"`

      default: platform_oauth_app_updated

    - `actor: object or object or object or 8 more`

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

    - `oauth_app_id: string`

      Tagged ID of the updated app

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `updates: optional array of object`

      The field-level changes applied in this update

      - `type: "apple_ios_attestation_environment" or "apple_ios_bundles" or "name" or 2 more`

        The OAuth app field that changed

        - `"apple_ios_attestation_environment"`

        - `"apple_ios_bundles"`

        - `"name"`

        - `"status"`

        - `"unspecified"`

      - `current_value: string`

        Field value immediately after this change

      - `previous_value: string`

        Field value immediately before this change

  - `PlatformPluginDirectorySubmissionCreated object`

    A plugin directory submission was created on the API platform. A plugin directory submission is a request to list a plugin in the public plugin directory.

    - `type: optional "platform_plugin_directory_submission_created"`

      default: platform_plugin_directory_submission_created

    - `actor: object or object or object or 8 more`

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

    - `plugin_name: string`

      The name of the plugin being submitted.

    - `submission_id: string`

      The submission that was created, e.g. "psub_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformPluginDirectorySubmissionDeleted object`

    A plugin directory submission was deleted on the API platform.

    - `type: optional "platform_plugin_directory_submission_deleted"`

      default: platform_plugin_directory_submission_deleted

    - `actor: object or object or object or 8 more`

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

    - `submission_id: string`

      The submission that was deleted, e.g. "psub_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformPluginDirectorySubmissionUpdated object`

    A plugin directory submission was updated on the API platform.

    - `type: optional "platform_plugin_directory_submission_updated"`

      default: platform_plugin_directory_submission_updated

    - `actor: object or object or object or 8 more`

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

    - `status: string`

      The submission's status after the update.

    - `submission_id: string`

      The submission that was updated, e.g. "psub_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformServiceAccountArchived object`

    A service account was archived.

    - `type: optional "platform_service_account_archived"`

      default: platform_service_account_archived

    - `actor: object or object or object or 8 more`

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

    - `service_account_id: string`

      Tagged ID of the archived service account

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformServiceAccountUpdated object`

    A service account was updated.

    - `type: optional "platform_service_account_updated"`

      default: platform_service_account_updated

    - `actor: object or object or object or 8 more`

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

    - `service_account_id: string`

      Tagged ID of the updated service account

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `updates: optional array of object`

      The field-level changes applied in this update

      - `type: "description" or "organization_role" or "unspecified"`

        The service account field that changed

        - `"description"`

        - `"organization_role"`

        - `"unspecified"`

      - `current_value: string`

        Field value immediately after this change

      - `previous_value: string`

        Field value immediately before this change

  - `PlatformServiceAccountWorkspaceMemberAdded object`

    A service account was added as a member of a workspace.

    - `type: optional "platform_service_account_workspace_member_added"`

      default: platform_service_account_workspace_member_added

    - `actor: object or object or object or 8 more`

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

    - `service_account_id: string`

      Tagged ID of the service account

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `workspace_role: optional string or null`

      Role the service account was given in the workspace, for example workspace_developer.

  - `PlatformServiceAccountWorkspaceMemberRemoved object`

    A service account was removed from a workspace.

    - `type: optional "platform_service_account_workspace_member_removed"`

      default: platform_service_account_workspace_member_removed

    - `actor: object or object or object or 8 more`

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

    - `service_account_id: string`

      Tagged ID of the service account

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformServiceAccountWorkspaceMemberUpdated object`

    A service account's workspace membership role was updated.

    - `type: optional "platform_service_account_workspace_member_updated"`

      default: platform_service_account_workspace_member_updated

    - `actor: object or object or object or 8 more`

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

    - `service_account_id: string`

      Tagged ID of the service account

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `updates: optional array of object`

      The field-level changes applied in this update

      - `type: "unspecified" or "workspace_role"`

        The service account's workspace membership field that changed

        - `"unspecified"`

        - `"workspace_role"`

      - `current_value: string`

        Field value immediately after this change

      - `previous_value: string`

        Field value immediately before this change

  - `PlatformSigningKeyCreated object`

    Activity logged when a new request-signing key is registered for the org.

    - `type: optional "platform_signing_key_created"`

      default: platform_signing_key_created

    - `actor: object or object or object or 8 more`

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

    - `algorithm: string`

      The signing algorithm (e.g. ecdsa-p256-sha256)

    - `key_backing_type: string`

      The backing type of the key (IN_MEMORY or CLOUD_KMS)

    - `signing_key_id: string`

      The tagged ID of the created signing key

    - `status: string`

      The initial status of the key (ACTIVE or PENDING)

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformSigningKeyDeleted object`

    Activity logged when a signing key is permanently deleted.

    - `type: optional "platform_signing_key_deleted"`

      default: platform_signing_key_deleted

    - `actor: object or object or object or 8 more`

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

    - `algorithm: string`

      The algorithm of the deleted key

    - `key_backing_type: string`

      The backing type of the deleted key (IN_MEMORY or CLOUD_KMS)

    - `key_name: string`

      The name of the deleted key

    - `signing_key_id: string`

      The tagged ID of the deleted signing key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformSigningKeyRotated object`

    Activity logged when an in-memory signing key is rotated.

    - `type: optional "platform_signing_key_rotated"`

      default: platform_signing_key_rotated

    - `actor: object or object or object or 8 more`

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

    - `algorithm: string`

      The algorithm of the new key

    - `key_group_identifier: string`

      The key group identifier linking old and new keys

    - `new_signing_key_id: string`

      The tagged ID of the newly created key

    - `old_signing_key_id: string`

      The tagged ID of the expired old key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformSkillVersionContentDownloaded object`

    The content of a skill version was downloaded through the Skills API.

    - `type: optional "platform_skill_version_content_downloaded"`

      default: platform_skill_version_content_downloaded

    - `actor: object or object or object or 8 more`

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

    - `skill_id: string`

      The tagged ID of the skill

    - `version: string`

      The version of the skill whose content was downloaded

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformSkillVersionCreated object`

    Activity logged when a skill version is created via POST /v1/skills/{skill_id}/versions.

    - `type: optional "platform_skill_version_created"`

      default: platform_skill_version_created

    - `actor: object or object or object or 8 more`

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

    - `skill_id: string`

      The tagged ID of the skill

    - `version: string`

      The version number of the created version

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformSkillVersionDeleted object`

    Activity logged when a skill version is deleted via DELETE /v1/skills/{skill_id}/versions/{version}.

    - `type: optional "platform_skill_version_deleted"`

      default: platform_skill_version_deleted

    - `actor: object or object or object or 8 more`

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

    - `skill_id: string`

      The tagged ID of the skill

    - `version: string`

      The version number of the deleted version

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformSpendLimitAlertEmailsUpdated object`

    Spend limit alert email addresses and role targets were updated for an org.

    - `type: optional "platform_spend_limit_alert_emails_updated"`

      default: platform_spend_limit_alert_emails_updated

    - `actor: object or object or object or 8 more`

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

    - `alerted_roles: optional array of string or null`

      Updated list of alerted roles.

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformSpendLimitCreated object`

    An org-level fixed-dollar spend limit was created.

    - `type: optional "platform_spend_limit_created"`

      default: platform_spend_limit_created

    - `actor: object or object or object or 8 more`

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

  - `PlatformSpendLimitDeleted object`

    An org-level spend limit was removed.

    - `type: optional "platform_spend_limit_deleted"`

      default: platform_spend_limit_deleted

    - `actor: object or object or object or 8 more`

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

  - `PlatformSpendLimitUpdated object`

    An org-level spend limit snooze/ignore state was changed.

    - `type: optional "platform_spend_limit_updated"`

      default: platform_spend_limit_updated

    - `actor: object or object or object or 8 more`

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

    - `ignore: optional boolean or null`

      Whether the limit is being snoozed (ignored).

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `spend_limit_id: optional string or null`

      UUID of the spend limit.

  - `PlatformUsageReportClaudeCodeViewed object`

    The Claude Code usage report was viewed.

    - `type: optional "platform_usage_report_claude_code_viewed"`

      default: platform_usage_report_claude_code_viewed

    - `actor: object or object or object or 8 more`

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

  - `PlatformUsageReportMessagesViewed object`

    The messages usage report was viewed.

    - `type: optional "platform_usage_report_messages_viewed"`

      default: platform_usage_report_messages_viewed

    - `actor: object or object or object or 8 more`

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

  - `PlatformWorkspaceArchived object`

    A workspace was archived.

    - `type: optional "platform_workspace_archived"`

      default: platform_workspace_archived

    - `actor: object or object or object or 8 more`

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

    - `workspace_id: string`

      Tagged ID of the archived workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformWorkspaceCreated object`

    A workspace was created.

    - `type: optional "platform_workspace_created"`

      default: platform_workspace_created

    - `actor: object or object or object or 8 more`

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

    - `workspace_id: string`

      Tagged ID of the created workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformWorkspaceInferenceDataRetentionDisabled object`

    The zero data retention override was disabled for a workspace.

    - `type: optional "platform_workspace_inference_data_retention_disabled"`

      default: platform_workspace_inference_data_retention_disabled

    - `actor: object or object or object or 8 more`

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

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `previous_value: optional boolean or null`

      Override state immediately before this change

  - `PlatformWorkspaceInferenceDataRetentionEnabled object`

    The zero data retention override was enabled for a workspace.

    - `type: optional "platform_workspace_inference_data_retention_enabled"`

      default: platform_workspace_inference_data_retention_enabled

    - `actor: object or object or object or 8 more`

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

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `previous_value: optional boolean or null`

      Override state immediately before this change

  - `PlatformWorkspaceMemberAdded object`

    A member was added to a workspace.

    - `type: optional "platform_workspace_member_added"`

      default: platform_workspace_member_added

    - `actor: object or object or object or 8 more`

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

    - `user_id: string`

      Tagged ID of the added member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformWorkspaceMemberRemoved object`

    A member was removed from a workspace.

    - `type: optional "platform_workspace_member_removed"`

      default: platform_workspace_member_removed

    - `actor: object or object or object or 8 more`

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

    - `user_id: string`

      Tagged ID of the removed member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformWorkspaceMemberUpdated object`

    A workspace member was updated.

    - `type: optional "platform_workspace_member_updated"`

      default: platform_workspace_member_updated

    - `actor: object or object or object or 8 more`

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

    - `user_id: string`

      Tagged ID of the updated member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `updates: optional array of object`

      The field-level changes applied in this update

      - `type: "unspecified" or "workspace_role"`

        The workspace member field that changed

        - `"unspecified"`

        - `"workspace_role"`

      - `current_value: string`

        Field value immediately after this change

      - `previous_value: string`

        Field value immediately before this change

  - `PlatformWorkspaceMemberViewed object`

    A workspace member was viewed.

    - `type: optional "platform_workspace_member_viewed"`

      default: platform_workspace_member_viewed

    - `actor: object or object or object or 8 more`

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

    - `user_id: string`

      Tagged ID of the viewed member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformWorkspaceMembersListed object`

    Workspace members were listed.

    - `type: optional "platform_workspace_members_listed"`

      default: platform_workspace_members_listed

    - `actor: object or object or object or 8 more`

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

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformWorkspaceRateLimitDeleted object`

    A workspace rate limit was deleted.

    - `type: optional "platform_workspace_rate_limit_deleted"`

      default: platform_workspace_rate_limit_deleted

    - `actor: object or object or object or 8 more`

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

    - `limiter_type: string`

      Type of rate limiter

    - `model_group: string`

      Model group the rate limit applied to

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformWorkspaceRateLimitUpdated object`

    A workspace rate limit was created or updated.

    - `type: optional "platform_workspace_rate_limit_updated"`

      default: platform_workspace_rate_limit_updated

    - `actor: object or object or object or 8 more`

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

    - `limiter_type: string`

      Type of rate limiter

    - `model_group: string`

      Model group the rate limit applies to

    - `value: number`

      New rate limit value

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `PlatformWorkspaceUpdated object`

    A workspace was updated.

    - `type: optional "platform_workspace_updated"`

      default: platform_workspace_updated

    - `actor: object or object or object or 8 more`

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

    - `workspace_id: string`

      Tagged ID of the updated workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `updates: optional array of object`

      The field-level changes applied in this update

      - `type: "allowed_inference_geos" or "default_inference_geo" or "display_color" or 4 more`

        The workspace field that changed

        - `"allowed_inference_geos"`

        - `"default_inference_geo"`

        - `"display_color"`

        - `"external_key_config_id"`

        - `"inference_data_retention"`

        - `"name"`

        - `"unspecified"`

      - `current_value: string`

        Field value immediately after this change

      - `previous_value: string`

        Field value immediately before this change

  - `ClaudePluginCreated object`

    Plugin was created.

    - `type: optional "claude_plugin_created"`

      default: claude_plugin_created

    - `actor: object or object or object or 8 more`

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

    - `plugin_id: optional string or null`

    - `plugin_name: optional string or null`

  - `ClaudePluginDeleted object`

    Plugin was deleted.

    - `type: optional "claude_plugin_deleted"`

      default: claude_plugin_deleted

    - `actor: object or object or object or 8 more`

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

    - `plugin_id: optional string or null`

    - `plugin_name: optional string or null`

  - `ClaudePluginDisabled object`

    User disabled a plugin for their account.

    - `type: optional "claude_plugin_disabled"`

      default: claude_plugin_disabled

    - `actor: object or object or object or 8 more`

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

    - `marketplace_id: optional string or null`

      Identifier of the marketplace the plugin was installed from.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `plugin_id: optional string or null`

      Identifier of the plugin that was disabled.

    - `plugin_name: optional string or null`

      Name of the plugin that was disabled.

  - `ClaudePluginEnabled object`

    User enabled a plugin for their account.

    - `type: optional "claude_plugin_enabled"`

      default: claude_plugin_enabled

    - `actor: object or object or object or 8 more`

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

    - `marketplace_id: optional string or null`

      Identifier of the marketplace the plugin was installed from.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `plugin_id: optional string or null`

      Identifier of the plugin that was enabled.

    - `plugin_name: optional string or null`

      Name of the plugin that was enabled.

  - `PluginInstallationPreferenceUpdated object`

    An org admin changed the installation preference for a plugin.

    - `type: optional "plugin_installation_preference_updated"`

      default: plugin_installation_preference_updated

    - `actor: object or object or object or 8 more`

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

    - `marketplace_id: string`

      Marketplace ID

    - `plugin_name: string`

      Plugin name

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `action: optional string or null`

      Action taken (e.g. 'deleted' for clearing an override)

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `group_id: optional string or null`

      Tagged group ID for group-level overrides (null for org-level)

    - `group_name: optional string or null`

      Group name for group-level overrides

    - `installation_preference: optional string or null`

      New installation preference value (set only when action is an update; null for delete actions)

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `previous_installation_preference: optional string or null`

      Installation preference value before this change, at the same level (organization or group); absent when none was set before

  - `ClaudePluginReplaced object`

    Plugin was replaced.

    - `type: optional "claude_plugin_replaced"`

      default: claude_plugin_replaced

    - `actor: object or object or object or 8 more`

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

    - `plugin_id: optional string or null`

    - `plugin_name: optional string or null`

  - `ClaudePluginSecurityScanCompleted object`

    A security scan of a plugin completed and produced a verdict.

    - `type: optional "claude_plugin_security_scan_completed"`

      default: claude_plugin_security_scan_completed

    - `actor: object or object or object or 8 more`

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

    - `scan_id: string`

      Identifier of the security scan.

    - `verdict: "fail" or "pass" or "unknown" or 2 more`

      Verdict the scan produced.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"unspecified"`

      - `"warn"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `plugin_id: optional string or null`

      Identifier of the plugin that was scanned.

    - `plugin_name: optional string or null`

      Name of the plugin that was scanned.

    - `plugin_version: optional string or null`

      Version of the plugin that was scanned.

  - `ClaudePluginUpdated object`

    Plugin was updated.

    - `type: optional "claude_plugin_updated"`

      default: claude_plugin_updated

    - `actor: object or object or object or 8 more`

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

    - `plugin_id: optional string or null`

    - `plugin_name: optional string or null`

  - `PrepaidAutoRechargeDisabled object`

    Auto-recharge was disabled for API prepaid org.

    - `type: optional "prepaid_auto_recharge_disabled"`

      default: prepaid_auto_recharge_disabled

    - `actor: object or object or object or 8 more`

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

  - `PrepaidAutoRechargeUpdated object`

    Auto-recharge settings were updated for API prepaid org.

    - `type: optional "prepaid_auto_recharge_updated"`

      default: prepaid_auto_recharge_updated

    - `actor: object or object or object or 8 more`

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

    - `target_amount: optional number or null`

      Target recharge amount in minor units.

    - `threshold_amount: optional number or null`

      Threshold amount to trigger recharge in minor units.

  - `PrepaidExtraUsageAutoReloadDisabled object`

    Prepaid usage credit auto-reload was disabled.

    - `type: optional "prepaid_extra_usage_auto_reload_disabled"`

      default: prepaid_extra_usage_auto_reload_disabled

    - `actor: object or object or object or 8 more`

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

  - `PrepaidExtraUsageAutoReloadEnabled object`

    Prepaid usage credit auto-reload was enabled.

    - `type: optional "prepaid_extra_usage_auto_reload_enabled"`

      default: prepaid_extra_usage_auto_reload_enabled

    - `actor: object or object or object or 8 more`

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

  - `PrepaidExtraUsageAutoReloadSettingsUpdated object`

    Prepaid usage credit auto-reload settings were updated.

    - `type: optional "prepaid_extra_usage_auto_reload_settings_updated"`

      default: prepaid_extra_usage_auto_reload_settings_updated

    - `actor: object or object or object or 8 more`

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

  - `PrimaryOwnerTransferred object`

    Primary owner role was transferred to another org member.

    - `type: optional "primary_owner_transferred"`

      default: primary_owner_transferred

    - `actor: object or object or object or 8 more`

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

    - `new_owner_id: string`

      Tagged ID of the member who became the primary owner.

    - `previous_owner_id: string`

      Tagged ID of the member who was the primary owner before the transfer.

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectArchived object`

    A Claude project was archived.

    - `type: optional "claude_project_archived"`

      default: claude_project_archived

    - `actor: object or object or object or 8 more`

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

    - `claude_project_id: string`

      Tagged ID of the project that was archived, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectCreated object`

    A Claude project was created.

    - `type: optional "claude_project_created"`

      default: claude_project_created

    - `actor: object or object or object or 8 more`

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

    - `claude_project_id: string`

      Tagged ID of the project that was created, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectDeleted object`

    A Claude project was deleted.

    - `type: optional "claude_project_deleted"`

      default: claude_project_deleted

    - `actor: object or object or object or 8 more`

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

    - `claude_project_id: string`

      Tagged ID of the project that was deleted, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectDocumentAccessFailed object`

    An attempt to access a document in a Claude project failed.

    - `type: optional "claude_project_document_access_failed"`

      default: claude_project_document_access_failed

    - `actor: object or object or object or 8 more`

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

    - `claude_project_id: string`

      Tagged ID of the project the request targeted, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_project_document_id: optional string or null`

      Tagged ID of the document the request tried to access, e.g. "claude_proj_doc_01HX...". Absent when the request did not carry a well-formed document identifier.

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `filename: optional string or null`

      Name of the document, when known.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectDocumentBulkDeletionAuditTruncated object`

    A bulk request to delete documents from a Claude project failed with more documents requested than were individually recorded in the audit log.

    - `type: optional "claude_project_document_bulk_deletion_audit_truncated"`

      default: claude_project_document_bulk_deletion_audit_truncated

    - `actor: object or object or object or 8 more`

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

    - `audited_count: number`

      Number of documents that received an individual audit record.

    - `claude_project_id: string`

      Tagged ID of the project the bulk deletion targeted, e.g. "claude_proj_01HX...".

    - `requested_count: number`

      Total number of documents the request asked to delete.

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectDocumentDeleted object`

    A document was deleted from a Claude project.

    - `type: optional "claude_project_document_deleted"`

      default: claude_project_document_deleted

    - `actor: object or object or object or 8 more`

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

    - `claude_project_document_id: string`

      Tagged ID of the document that was deleted, e.g. "claude_proj_doc_01HX...".

    - `claude_project_id: string`

      Tagged ID of the project the document was deleted from, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `filename: optional string or null`

      Name of the deleted document, when known.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectDocumentDeletionFailed object`

    A request to delete a document from a Claude project failed.

    - `type: optional "claude_project_document_deletion_failed"`

      default: claude_project_document_deletion_failed

    - `actor: object or object or object or 8 more`

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

    - `claude_project_id: string`

      Tagged ID of the project the deletion targeted, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_project_document_id: optional string or null`

      Tagged ID of the document the deletion targeted, e.g. "claude_proj_doc_01HX...".

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `filename: optional string or null`

      Name of the document, when known.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectDocumentUpdated object`

    The content of a document in a Claude project was replaced in place.

    - `type: optional "claude_project_document_updated"`

      default: claude_project_document_updated

    - `actor: object or object or object or 8 more`

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

    - `claude_project_document_id: string`

      Tagged ID of the document whose content was replaced, e.g. "claude_proj_doc_01HX...".

    - `claude_project_id: string`

      Tagged ID of the project containing the document, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `filename: optional string or null`

      Name of the updated document.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectDocumentUploaded object`

    A document was uploaded to a Claude project.

    - `type: optional "claude_project_document_uploaded"`

      default: claude_project_document_uploaded

    - `actor: object or object or object or 8 more`

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

    - `claude_project_document_id: string`

      Tagged ID of the document that was uploaded, e.g. "claude_proj_doc_01HX...".

    - `claude_project_id: string`

      Tagged ID of the project the document was uploaded to, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `filename: optional string or null`

      Name of the uploaded document.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectDocumentViewed object`

    A document in a Claude project was viewed.

    - `type: optional "claude_project_document_viewed"`

      default: claude_project_document_viewed

    - `actor: object or object or object or 8 more`

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

    - `claude_project_document_id: string`

      Tagged ID of the document that was viewed, e.g. "claude_proj_doc_01HX...".

    - `claude_project_id: string`

      Tagged ID of the project containing the document, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `filename: optional string or null`

      Name of the viewed document.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectFileAccessFailed object`

    An attempt to access a file in a Claude project failed.

    - `type: optional "claude_project_file_access_failed"`

      default: claude_project_file_access_failed

    - `actor: object or object or object or 8 more`

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

    - `claude_file_id: string`

      Tagged ID of the file the request tried to access, e.g. "claude_file_01HX...".

    - `claude_project_id: string`

      Tagged ID of the project the request targeted, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectFileBulkDeletionAuditTruncated object`

    A bulk request to delete files from a Claude project failed with more files requested than were individually recorded in the audit log.

    - `type: optional "claude_project_file_bulk_deletion_audit_truncated"`

      default: claude_project_file_bulk_deletion_audit_truncated

    - `actor: object or object or object or 8 more`

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

    - `audited_count: number`

      Number of files that received an individual audit record.

    - `claude_project_id: string`

      Tagged ID of the project the bulk deletion targeted, e.g. "claude_proj_01HX...".

    - `requested_count: number`

      Total number of files the request asked to delete.

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectFileDeleted object`

    A file was deleted from a Claude project.

    - `type: optional "claude_project_file_deleted"`

      default: claude_project_file_deleted

    - `actor: object or object or object or 8 more`

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

    - `claude_file_id: string`

      Tagged ID of the file that was deleted, e.g. "claude_file_01HX...".

    - `claude_project_id: string`

      Tagged ID of the project the file was deleted from, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectFileDeletionFailed object`

    A request to delete a file from a Claude project failed.

    - `type: optional "claude_project_file_deletion_failed"`

      default: claude_project_file_deletion_failed

    - `actor: object or object or object or 8 more`

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

    - `claude_project_id: string`

      Tagged ID of the project the deletion targeted, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `claude_file_id: optional string or null`

      Tagged ID of the file that was not deleted, e.g. "claude_file_01HX...".

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectFileUploaded object`

    A file was uploaded to a Claude project.

    - `type: optional "claude_project_file_uploaded"`

      default: claude_project_file_uploaded

    - `actor: object or object or object or 8 more`

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

    - `claude_file_id: string`

      Tagged ID of the file that was uploaded, e.g. "claude_file_01HX...".

    - `claude_project_id: string`

      Tagged ID of the project the file was uploaded to, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `filename: optional string or null`

      Name of the uploaded file.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectReported object`

    A Claude project was reported.

    - `type: optional "claude_project_reported"`

      default: claude_project_reported

    - `actor: object or object or object or 8 more`

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

    - `claude_project_id: string`

      Tagged ID of the project that was reported, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectSharingUpdated object`

    A Claude project's sharing settings were updated.

    - `type: optional "claude_project_sharing_updated"`

      default: claude_project_sharing_updated

    - `actor: object or object or object or 8 more`

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

    - `audience: array of object or object`

      Sharing audience for the project. If empty, it's only visible to the creating user.

      - `Public object`

        Sharing audience: public.

        - `type: optional "public"`

          default: public

      - `Organization object`

        Sharing audience: the project is visible to members of the owning organization.

        - `type: optional "organization"`

          default: organization

    - `claude_project_id: string`

      The project's identifier, e.g. "claude_proj_01Ab...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeProjectViewed object`

    A Claude project was viewed.

    - `type: optional "claude_project_viewed"`

      default: claude_project_viewed

    - `actor: object or object or object or 8 more`

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

    - `claude_project_id: string`

      Tagged ID of the project that was viewed, e.g. "claude_proj_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `preview_only: optional boolean or null`

      Whether only the project's summary metadata was viewed rather than the full project.

  - `ClaudePubsecIdentityConfigured object`

    SAML IdP configuration updated for a public sector organization.

    - `type: optional "claude_pubsec_identity_configured"`

      default: claude_pubsec_identity_configured

    - `actor: object or object or object or 8 more`

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

    - `idp_saml_config_updated: boolean`

    - `magic_link_toggled: boolean`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `magic_link_enabled: optional boolean or null`

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `RbacRoleAssigned object`

    Admin assigned an RBAC custom role to a principal.

    - `type: optional "rbac_role_assigned"`

      default: rbac_role_assigned

    - `actor: object or object or object or 8 more`

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

    - `principal_id: string`

      Tagged ID of the principal

    - `principal_type: string`

      Type of principal: account, group, or service_account

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `RbacRoleCreated object`

    Admin created an RBAC custom role.

    - `type: optional "rbac_role_created"`

      default: rbac_role_created

    - `actor: object or object or object or 8 more`

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

    - `role_id: string`

      Tagged ID of the created role

    - `role_name: string`

      Name of the created role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `RbacRoleDeleted object`

    Admin deleted an RBAC custom role.

    - `type: optional "rbac_role_deleted"`

      default: rbac_role_deleted

    - `actor: object or object or object or 8 more`

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

    - `role_id: string`

      Tagged ID of the deleted role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `RbacRoleGrantUpdated object`

    Admin requested a capability grant for an RBAC custom role, or removed it.

    Records the admin's change to the role. Whether the grant is currently in
    effect on the role is reported separately.

    - `type: optional "rbac_role_grant_updated"`

      default: rbac_role_grant_updated

    - `action: "removed" or "requested" or "unspecified"`

      Whether the grant was requested for the role or removed from it

      - `"removed"`

      - `"requested"`

      - `"unspecified"`

    - `actor: object or object or object or 8 more`

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

    - `grant_type: string`

      The type of capability grant

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `RbacRolePermissionAdded object`

    Admin added a permission to an RBAC custom role.

    Emitted once per requested permission, including permissions the role
    already had, so a retried request still produces a complete audit record.

    - `type: optional "rbac_role_permission_added"`

      default: rbac_role_permission_added

    - `action: string`

      Action permitted on the resource

    - `actor: object or object or object or 8 more`

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

    - `resource_id: string`

      ID of the resource

    - `resource_type: string`

      Type of resource the permission applies to

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `RbacRolePermissionRemoved object`

    Admin removed a permission from an RBAC custom role.

    Emitted once per requested permission, including permissions the role
    already lacked, so a retried request still produces a complete audit
    record.

    - `type: optional "rbac_role_permission_removed"`

      default: rbac_role_permission_removed

    - `action: string`

      Action that was permitted on the resource

    - `actor: object or object or object or 8 more`

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

    - `resource_id: string`

      ID of the resource

    - `resource_type: string`

      Type of resource the permission applied to

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `RbacRoleUnassigned object`

    Admin unassigned an RBAC custom role from a principal.

    - `type: optional "rbac_role_unassigned"`

      default: rbac_role_unassigned

    - `actor: object or object or object or 8 more`

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

    - `principal_id: string`

      Tagged ID of the principal

    - `principal_type: string`

      Type of principal: account, group, or service_account

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `RbacRoleUpdated object`

    Admin updated an RBAC custom role.

    - `type: optional "rbac_role_updated"`

      default: rbac_role_updated

    - `actor: object or object or object or 8 more`

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

    - `role_id: string`

      Tagged ID of the updated role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `RoleAssignmentGranted object`

    Role assignment was granted.

    - `type: optional "role_assignment_granted"`

      default: role_assignment_granted

    - `actor: object or object or object or 8 more`

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

    - `resource_id: optional string or null`

      ID of the resource the role is on.

    - `resource_type: optional string or null`

      What kind of resource the role is on, for example "chat_project", "skill", or "plugin".

    - `role: optional string or null`

      The role that was granted, for example "skill:viewer" or "plugin:viewer".

    - `target_email: optional string or null`

      Email address of the person who received the role when they are an invitee identified by email address or an account outside the organization; absent or null for members and groups.

    - `target_id: optional string or null`

      ID of the grantee: a user ID for a member or for an account outside the organization, a group ID for a group, the organization ID for an organization-wide grant, or an opaque "email:" key for an invitee identified only by email address.

    - `target_type: optional string or null`

      What kind of grantee received the role, for example "organization_member", "group", "organization", "account" (an account outside the organization), or "email" (an invitee identified by email address).

  - `RoleAssignmentRevoked object`

    Role assignment was revoked.

    - `type: optional "role_assignment_revoked"`

      default: role_assignment_revoked

    - `actor: object or object or object or 8 more`

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

    - `resource_id: optional string or null`

      ID of the resource the role was on.

    - `resource_type: optional string or null`

      What kind of resource the role was on, for example "chat_project", "skill", or "plugin".

    - `role: optional string or null`

      The role that was revoked, for example "skill:viewer" or "plugin:viewer".

    - `target_email: optional string or null`

      Email address of the person who held the role when they are an invitee identified by email address or an account outside the organization; absent or null for members and groups.

    - `target_id: optional string or null`

      ID of the grantee that held the role: a user ID for a member or for an account outside the organization, a group ID for a group, the organization ID for an organization-wide grant, or an opaque "email:" key for an invitee identified only by email address.

    - `target_type: optional string or null`

      What kind of grantee held the role, for example "organization_member", "group", "organization", "account" (an account outside the organization), or "email" (an invitee identified by email address).

  - `SSOLoginFailed object`

    An SSO sign-in attempt failed.

    - `type: optional "sso_login_failed"`

      default: sso_login_failed

    - `actor: object or object or object or 8 more`

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

  - `SSOLoginInitiated object`

    A user started an SSO sign-in flow.

    - `type: optional "sso_login_initiated"`

      default: sso_login_initiated

    - `actor: object or object or object or 8 more`

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

  - `SSOLoginSucceeded object`

    A user successfully signed in with SSO.

    - `type: optional "sso_login_succeeded"`

      default: sso_login_succeeded

    - `actor: object or object or object or 8 more`

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

    - `auth_method: optional "sso" or "unspecified" or null`

      The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

      - `"sso"`

      - `"unspecified"`

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `mfa_method: optional "not_used" or "unspecified" or null`

      The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multistep login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

      - `"not_used"`

      - `"unspecified"`

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `SSOSecondFactorMagicLink object`

    SSO second factor magic link was used.

    - `type: optional "sso_second_factor_magic_link"`

      default: sso_second_factor_magic_link

    - `actor: object or object or object or 8 more`

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

  - `ScimUserCreated object`

    A SCIM user was provisioned.

    - `type: optional "scim_user_created"`

      default: scim_user_created

    - `actor: object or object or object or 8 more`

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

    - `user_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ScimUserDeleted object`

    A SCIM user was deleted.

    - `type: optional "scim_user_deleted"`

      default: scim_user_deleted

    - `actor: object or object or object or 8 more`

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

    - `user_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ScimUserUpdated object`

    A SCIM user was updated.

    - `type: optional "scim_user_updated"`

      default: scim_user_updated

    - `actor: object or object or object or 8 more`

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

    - `user_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ScopedAPIKeyDeleted object`

    A scoped API key was deleted.

    - `type: optional "scoped_api_key_deleted"`

      default: scoped_api_key_deleted

    - `actor: object or object or object or 8 more`

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

    - `api_key_id: string`

      Tagged ID of the deleted scoped API key

    - `api_key_name: string`

      Name of the deleted scoped API key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `scopes: optional array of string`

      Scopes the deleted key had

  - `ScopedAPIKeyUpdated object`

    A scoped API key was renamed or its activation state changed.

    - `type: optional "scoped_api_key_updated"`

      default: scoped_api_key_updated

    - `actor: object or object or object or 8 more`

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

    - `api_key_id: string`

      Tagged ID of the updated scoped API key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `updates: optional array of object`

      The field-level changes applied in this update

      - `type: "activation_state" or "name" or "unspecified"`

        The scoped API key field that changed

        - `"activation_state"`

        - `"name"`

        - `"unspecified"`

      - `current_value: string`

        Field value immediately after this change

      - `previous_value: string`

        Field value immediately before this change

  - `SeatTierChangesCancelled object`

    Scheduled seat tier downgrades were cancelled.

    - `type: optional "seat_tier_changes_cancelled"`

      default: seat_tier_changes_cancelled

    - `actor: object or object or object or 8 more`

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

  - `SeatTiersPurchased object`

    Seat tiers were purchased or upgraded on a subscription.

    - `type: optional "seat_tiers_purchased"`

      default: seat_tiers_purchased

    - `actor: object or object or object or 8 more`

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

    - `item_allocations: optional map[number] or null`

      Desired seat tier allocations (item type to quantity).

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ServiceCreated object`

    Activity logged when an org service is explicitly created.

    - `type: optional "service_created"`

      default: service_created

    - `actor: object or object or object or 8 more`

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

    - `service_name: string`

      The org service name (e.g., 'external:my-service')

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ServiceDeleted object`

    Activity logged when an org service is deleted.

    - `type: optional "service_deleted"`

      default: service_deleted

    - `actor: object or object or object or 8 more`

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

    - `service_name: string`

      The org service name (e.g., 'external:my-service')

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ServiceKeyCreated object`

    Activity logged when a new org service key is created.

    - `type: optional "service_key_created"`

      default: service_key_created

    - `actor: object or object or object or 8 more`

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

    - `is_service_created: boolean`

      Whether the org service was implicitly created in this request

    - `key_name: string`

      The human-readable name of the key

    - `service_name: string`

      The service name this key belongs to

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `scopes: optional array of string`

      The scopes granted to this service key

    - `service_key_id: optional string or null`

      The ID of the created service key

  - `ServiceKeyRevoked object`

    Activity logged when an org service key is revoked.

    - `type: optional "service_key_revoked"`

      default: service_key_revoked

    - `actor: object or object or object or 8 more`

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

    - `service_key_id: string`

      The tagged ID of the revoked service key

    - `service_name: string`

      The service name this key belongs to

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `SessionRevoked object`

    User revoked a specific session.

    - `type: optional "session_revoked"`

      default: session_revoked

    - `actor: object or object or object or 8 more`

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

  - `SessionShareAccessed object`

    Session share was accessed.

    - `type: optional "session_share_accessed"`

      default: session_share_accessed

    - `actor: object or object or object or 8 more`

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

    - `share_id: optional string or null`

  - `SessionShareCreated object`

    Session share was created.

    - `type: optional "session_share_created"`

      default: session_share_created

    - `actor: object or object or object or 8 more`

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

    - `access_level: optional string or null`

      Access level granted for the share.

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `share_id: optional string or null`

  - `SessionShareRevoked object`

    Session share was revoked.

    - `type: optional "session_share_revoked"`

      default: session_share_revoked

    - `actor: object or object or object or 8 more`

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

    - `reason: optional string or null`

      Why the share was revoked.

    - `share_id: optional string or null`

  - `ClaudeSkillCreated object`

    Skill was created.

    - `type: optional "claude_skill_created"`

      default: claude_skill_created

    - `actor: object or object or object or 8 more`

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

    - `owner_user_id: optional string or null`

      The member who owns the skill; unset for an organization-owned skill.

    - `scope: optional "organization" or "personal" or "unspecified" or null`

      Whether the skill is the member's own or the organization's.

      - `"organization"`

      - `"personal"`

      - `"unspecified"`

    - `skill_id: optional string or null`

    - `skill_name: optional string or null`

    - `skill_version: optional string or null`

      Version of the skill that was created.

  - `ClaudeSkillDeleted object`

    Skill was deleted.

    - `type: optional "claude_skill_deleted"`

      default: claude_skill_deleted

    - `actor: object or object or object or 8 more`

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

    - `deleted_version_ids: optional array of string`

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `owner_user_id: optional string or null`

      The member who owns the skill; unset for an organization-owned skill.

    - `scope: optional "organization" or "personal" or "unspecified" or null`

      Whether the skill is the member's own or the organization's.

      - `"organization"`

      - `"personal"`

      - `"unspecified"`

    - `skill_id: optional string or null`

    - `skill_name: optional string or null`

    - `skill_version: optional string or null`

      Latest version of the skill when it was deleted.

    - `versions_deleted: optional number or null`

      Set when the deletion removed the skill's versions in the same request (the public API's cascading skill delete): one consolidated record of what went with the skill, reconcilable against earlier version-created records, rather than one version-deleted activity per row. versions_deleted is the exact count; deleted_version_ids lists at most the newest 1000 (truncated when versions_deleted exceeds its length).

  - `ClaudeSkillDisabled object`

    User disabled a skill for their account.

    - `type: optional "claude_skill_disabled"`

      default: claude_skill_disabled

    - `actor: object or object or object or 8 more`

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

    - `skill_id: optional string or null`

    - `skill_name: optional string or null`

  - `ClaudeSkillEnabled object`

    User enabled a skill for their account.

    - `type: optional "claude_skill_enabled"`

      default: claude_skill_enabled

    - `actor: object or object or object or 8 more`

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

    - `skill_id: optional string or null`

    - `skill_name: optional string or null`

  - `ClaudeSkillReplaced object`

    Skill was replaced.

    - `type: optional "claude_skill_replaced"`

      default: claude_skill_replaced

    - `actor: object or object or object or 8 more`

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

    - `owner_user_id: optional string or null`

      The member who owns the skill; unset for an organization-owned skill.

    - `scope: optional "organization" or "personal" or "unspecified" or null`

      Whether the skill is the member's own or the organization's.

      - `"organization"`

      - `"personal"`

      - `"unspecified"`

    - `skill_id: optional string or null`

    - `skill_name: optional string or null`

    - `skill_version: optional string or null`

      Version of the skill after it was replaced.

  - `ClaudeSkillSecurityScanCompleted object`

    A security scan of a skill completed and produced a verdict.

    - `type: optional "claude_skill_security_scan_completed"`

      default: claude_skill_security_scan_completed

    - `actor: object or object or object or 8 more`

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

    - `scan_id: string`

      Identifier of the security scan.

    - `verdict: "fail" or "pass" or "unknown" or 2 more`

      Verdict the scan produced.

      - `"fail"`

      - `"pass"`

      - `"unknown"`

      - `"unspecified"`

      - `"warn"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `skill_id: optional string or null`

      Identifier of the skill that was scanned.

    - `skill_name: optional string or null`

      Name of the skill that was scanned.

    - `skill_version: optional string or null`

      Version of the skill that was scanned.

  - `SlackWorkspaceClaimRevoked object`

    A Slack workspace or Enterprise Grid organization was disconnected from the organization for Claude in Slack.

    - `type: optional "slack_workspace_claim_revoked"`

      default: slack_workspace_claim_revoked

    - `actor: object or object or object or 8 more`

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

    - `slack_team_id: string`

      Claim subject: a Slack team id for scope 'workspace', or an Enterprise Grid org id for scope 'enterprise_grid'. Use the scope field to tell which — never the value's prefix (legacy workspaces exist with E-prefixed team ids)

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `scope: optional string or null`

      Blast radius of the revocation: 'workspace' for one Slack workspace, 'enterprise_grid' for every workspace in a Slack Enterprise Grid organization

  - `SlackWorkspaceClaimed object`

    A Slack workspace or Enterprise Grid organization was connected to the organization for Claude in Slack.

    - `type: optional "slack_workspace_claimed"`

      default: slack_workspace_claimed

    - `actor: object or object or object or 8 more`

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

    - `slack_team_id: string`

      Claim subject: a Slack team id for scope 'workspace', or an Enterprise Grid org id for scope 'enterprise_grid'. Use the scope field to tell which — never the value's prefix (legacy workspaces exist with E-prefixed team ids)

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `scope: optional string or null`

      Blast radius of the claim: 'workspace' for one Slack workspace, 'enterprise_grid' for every workspace in a Slack Enterprise Grid organization

  - `SocialLoginSucceeded object`

    A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).

    - `type: optional "social_login_succeeded"`

      default: social_login_succeeded

    - `actor: object or object or object or 8 more`

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

    - `provider: "apple" or "google" or "microsoft" or "unspecified"`

      The social identity provider the user signed in with: "google", "apple", or "microsoft".

      - `"apple"`

      - `"google"`

      - `"microsoft"`

      - `"unspecified"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `auth_method: optional "social" or "unspecified" or null`

      The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

      - `"social"`

      - `"unspecified"`

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `mfa_method: optional "not_used" or "unspecified" or null`

      The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multistep login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

      - `"not_used"`

      - `"unspecified"`

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `StepUpAuthenticationFailed object`

    An additional identity check failed.

    - `type: optional "step_up_authentication_failed"`

      default: step_up_authentication_failed

    - `actor: object or object or object or 8 more`

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

    - `method: "device_key" or "unspecified" or "webauthn"`

      The verification method the user attempted.

      - `"device_key"`

      - `"unspecified"`

      - `"webauthn"`

    - `reason: "challenge_rejected" or "unspecified" or "verification_failed"`

      Why the attempt failed.

      - `"challenge_rejected"`

      - `"unspecified"`

      - `"verification_failed"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `trusted_device_id: optional string or null`

      Identifier of the trusted device the attempt referenced, e.g. "tdev_...". Present only for the device key method.

  - `StepUpAuthenticationSucceeded object`

    The user completed an additional identity check to confirm a sensitive action.

    - `type: optional "step_up_authentication_succeeded"`

      default: step_up_authentication_succeeded

    - `actor: object or object or object or 8 more`

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

    - `method: "device_key" or "unspecified" or "webauthn"`

      The verification method the user completed.

      - `"device_key"`

      - `"unspecified"`

      - `"webauthn"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `trusted_device_id: optional string or null`

      Identifier of the trusted device used, e.g. "tdev_...". Present only for the device key method.

  - `StepUpCredentialEnrolled object`

    A user enrolled a passkey for confirming sensitive actions on their account.

    - `type: optional "step_up_credential_enrolled"`

      default: step_up_credential_enrolled

    - `actor: object or object or object or 8 more`

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

    - `credential_id: string`

      Identifier of the enrolled credential, e.g. "sucr_...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `SubscriptionCancellationScheduled object`

    Subscription cancellation was scheduled at end of billing period.

    - `type: optional "subscription_cancellation_scheduled"`

      default: subscription_cancellation_scheduled

    - `actor: object or object or object or 8 more`

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

  - `SubscriptionQuantityUpdated object`

    Contracted subscription seat quantity was updated.

    - `type: optional "subscription_quantity_updated"`

      default: subscription_quantity_updated

    - `actor: object or object or object or 8 more`

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

    - `added_seats: number`

      The number of seats added by this change.

    - `new_quantity: number`

      The contracted seat quantity after this change.

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `previous_quantity: optional number or null`

      The contracted seat quantity before this change.

  - `SubscriptionRenewed object`

    A cancelled subscription was renewed.

    - `type: optional "subscription_renewed"`

      default: subscription_renewed

    - `actor: object or object or object or 8 more`

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

    - `billing_interval: optional string or null`

      Billing interval (e.g. monthly, annual).

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `plan_type: optional string or null`

      Plan type being renewed into (e.g. team).

  - `SubscriptionResumed object`

    A scheduled subscription cancellation was reversed.

    - `type: optional "subscription_resumed"`

      default: subscription_resumed

    - `actor: object or object or object or 8 more`

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

  - `SubscriptionStarted object`

    A new subscription was created (Team or Enterprise).

    - `type: optional "subscription_started"`

      default: subscription_started

    - `actor: object or object or object or 8 more`

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

    - `billing_interval: optional string or null`

      Billing interval (e.g. monthly, annual).

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `plan_type: optional string or null`

      Type of subscription started (e.g. team, enterprise).

    - `seat_count: optional number or null`

      Number of seats purchased.

  - `SubscriptionUpgraded object`

    Subscription plan was upgraded (e.g. Team to Enterprise).

    - `type: optional "subscription_upgraded"`

      default: subscription_upgraded

    - `actor: object or object or object or 8 more`

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

    - `new_plan: optional string or null`

      New plan type after upgrade.

    - `old_plan: optional string or null`

      Previous plan type.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `TrustedDeviceCredentialRotated object`

    The identity-verification credential of a trusted device was rotated to a new key.

    - `type: optional "trusted_device_credential_rotated"`

      default: trusted_device_credential_rotated

    - `actor: object or object or object or 8 more`

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

    - `trusted_device_id: string`

      Identifier of the device whose credential was rotated, e.g. "tdev_...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `TrustedDeviceEnrolled object`

    A device was enrolled as a trusted device for the user's account. Trusted devices can be used to confirm the user's identity for sensitive actions.

    - `type: optional "trusted_device_enrolled"`

      default: trusted_device_enrolled

    - `actor: object or object or object or 8 more`

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

    - `enrollment_method: "oauth" or "session" or "unspecified"`

      How the user confirmed their identity when enrolling the device.

      - `"oauth"`

      - `"session"`

      - `"unspecified"`

    - `platform: "android" or "claude_in_slack" or "desktop_app" or 4 more`

      The kind of client the enrollment request came from.

      - `"android"`

      - `"claude_in_slack"`

      - `"desktop_app"`

      - `"ios"`

      - `"unspecified"`

      - `"web_claude_ai"`

      - `"web_console"`

    - `trusted_device_id: string`

      Identifier of the device that was enrolled, e.g. "tdev_...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `TrustedDeviceRevoked object`

    A trusted device was removed from the user's account.

    - `type: optional "trusted_device_revoked"`

      default: trusted_device_revoked

    - `actor: object or object or object or 8 more`

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

    - `reason: "org_member_removed" or "superseded" or "unspecified" or "user_revoked"`

      Why the device trust was removed.

      - `"org_member_removed"`

      - `"superseded"`

      - `"unspecified"`

      - `"user_revoked"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `revoked_count: optional number or null`

      Number of devices removed. Set when a security action removed all of the user's trusted devices at once; absent when a single device was removed (see trusted_device_id).

    - `trusted_device_id: optional string or null`

      Identifier of the device that was removed, e.g. "tdev_...". Set when a single device was removed; absent when several devices were removed at once (see revoked_count).

  - `TunnelArchived object`

    An MCP tunnel was archived.

    - `type: optional "tunnel_archived"`

      default: tunnel_archived

    - `actor: object or object or object or 8 more`

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

    - `tunnel_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `TunnelCertificateAdded object`

    An inner-TLS CA certificate was added to a tunnel.

    - `type: optional "tunnel_certificate_added"`

      default: tunnel_certificate_added

    - `actor: object or object or object or 8 more`

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

    - `certificate_id: string`

    - `tunnel_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `certificate_fingerprint: optional string or null`

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `TunnelCertificateRevoked object`

    An inner-TLS CA certificate was revoked from a tunnel.

    - `type: optional "tunnel_certificate_revoked"`

      default: tunnel_certificate_revoked

    - `actor: object or object or object or 8 more`

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

    - `certificate_id: string`

    - `tunnel_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `certificate_fingerprint: optional string or null`

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `TunnelCreated object`

    An MCP tunnel was created.

    - `type: optional "tunnel_created"`

      default: tunnel_created

    - `actor: object or object or object or 8 more`

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

    - `tunnel_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `TunnelTokenMinted object`

    An OAuth bearer token for the tunnel management API was minted.

    - `type: optional "tunnel_token_minted"`

      default: tunnel_token_minted

    - `actor: object or object or object or 8 more`

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

    - `token_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `token_name: optional string or null`

  - `TunnelTokenRevealed object`

    The Cloudflare connector secret for a tunnel was revealed to the caller.

    - `type: optional "tunnel_token_revealed"`

      default: tunnel_token_revealed

    - `actor: object or object or object or 8 more`

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

    - `tunnel_id: string`

    - `tunnel_token_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `TunnelTokenRevoked object`

    An OAuth bearer token for the tunnel management API was revoked.

    - `type: optional "tunnel_token_revoked"`

      default: tunnel_token_revoked

    - `actor: object or object or object or 8 more`

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

    - `token_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `token_name: optional string or null`

      Name the administrator gave the token when it was created, if any

  - `TunnelTokenRotated object`

    The Cloudflare connector secret for a tunnel was rotated.

    `tunnel_token_id` is the id of the *newly-issued* token. The previous
    token is invalidated by the rotation and its id is not recorded here.

    - `type: optional "tunnel_token_rotated"`

      default: tunnel_token_rotated

    - `actor: object or object or object or 8 more`

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

    - `tunnel_id: string`

    - `tunnel_token_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `reason: optional string or null`

  - `UserConsentRecorded object`

    User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).

    - `type: optional "user_consent_recorded"`

      default: user_consent_recorded

    - `actor: object or object or object or 8 more`

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

    - `consent_type: string`

    - `entity_id: string`

    - `entity_type: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `UserConsentRevoked object`

    User revoked a previously granted consent for a specific entity.

    - `type: optional "user_consent_revoked"`

      default: user_consent_revoked

    - `actor: object or object or object or 8 more`

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

    - `consent_id: optional string or null`

    - `consent_type: optional string or null`

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `entity_id: optional string or null`

    - `entity_type: optional string or null`

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `ClaudeUserRoleUpdated object`

    A user's role within the organization was changed, or the user was added to or removed from the organization.

    - `type: optional "claude_user_role_updated"`

      default: claude_user_role_updated

    - `actor: object or object or object or 8 more`

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

    - `user_email: string`

      Email of the user whose role was changed

    - `user_id: string`

      ID of the user whose role was changed

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `current_role: optional string or null`

      If null, then user was removed from the Organization

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `previous_role: optional string or null`

      If null, then user was added to the Organization

  - `ClaudeUserSettingsUpdated object`

    User updated their personal settings.

    - `type: optional "claude_user_settings_updated"`

      default: claude_user_settings_updated

    - `actor: object or object or object or 8 more`

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

    - `updates: array of object or object or object or 19 more`

      - `FullName object`

        The full name setting was changed.

        - `type: optional "full_name"`

          default: full_name

        - `current_value: optional string or null`

          Setting value immediately after this change

        - `previous_value: optional string or null`

          Setting value immediately before this change

      - `DisplayName object`

        The display name setting was changed.

        - `type: optional "display_name"`

          default: display_name

        - `current_value: optional string or null`

          Setting value immediately after this change

        - `previous_value: optional string or null`

          Setting value immediately before this change

      - `ArtifactsEnabled object`

        The artifacts setting was changed.

        - `type: optional "artifacts_enabled"`

          default: artifacts_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `LatexEnabled object`

        The LaTeX setting was changed.

        - `type: optional "latex_enabled"`

          default: latex_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `AnalysisToolEnabled object`

        The analysis tool setting was changed.

        - `type: optional "analysis_tool_enabled"`

          default: analysis_tool_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `ChatSuggestionsEnabled object`

        The chat suggestions setting was changed.

        - `type: optional "chat_suggestions_enabled"`

          default: chat_suggestions_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `MultimodalPdfsEnabled object`

        The multimodal PDFs setting was changed.

        - `type: optional "multimodal_pdfs_enabled"`

          default: multimodal_pdfs_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `GdriveEnabled object`

        The Google Drive setting was changed.

        - `type: optional "gdrive_enabled"`

          default: gdrive_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `WebSearchEnabled object`

        The web search setting was changed.

        - `type: optional "web_search_enabled"`

          default: web_search_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `GeolocationEnabled object`

        The geolocation setting was changed.

        - `type: optional "geolocation_enabled"`

          default: geolocation_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `EnabledSaffron object`

        The memory setting was changed for the user.

        - `type: optional "enabled_saffron"`

          default: enabled_saffron

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `McpToolsEnabled object`

        The MCP tools setting was changed.

        - `type: optional "mcp_tools_enabled"`

          default: mcp_tools_enabled

        - `current_value: optional map[boolean] or null`

          Setting value immediately after this change

        - `previous_value: optional map[boolean] or null`

          Setting value immediately before this change

      - `CliOpPermissionsEnabled object`

        The CLI operation permissions setting was changed.

        - `type: optional "cli_op_permissions_enabled"`

          default: cli_op_permissions_enabled

        - `current_value: optional map[string] or null`

          Setting value immediately after this change

        - `previous_value: optional map[string] or null`

          Setting value immediately before this change

      - `GoogleDriveSearchEnabled object`

        The Google Drive search setting was changed.

        - `type: optional "google_drive_search_enabled"`

          default: google_drive_search_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `GmailIntegrationEnabled object`

        The Gmail integration setting was changed.

        - `type: optional "gmail_integration_enabled"`

          default: gmail_integration_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `GoogleCalendarIntegrationEnabled object`

        The Google Calendar integration setting was changed.

        - `type: optional "google_calendar_integration_enabled"`

          default: google_calendar_integration_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `ThinkingModeEnabled object`

        The thinking mode setting was changed.

        - `type: optional "thinking_mode_enabled"`

          default: thinking_mode_enabled

        - `current_value: optional "adaptive" or "extended" or "off" or "unspecified" or null`

          Setting value immediately after this change

          - `"adaptive"`

          - `"extended"`

          - `"off"`

          - `"unspecified"`

        - `previous_value: optional "adaptive" or "extended" or "off" or "unspecified" or null`

          Setting value immediately before this change

          - `"adaptive"`

          - `"extended"`

          - `"off"`

          - `"unspecified"`

      - `ResearchModeEnabled object`

        The research mode setting was changed.

        - `type: optional "research_mode_enabled"`

          default: research_mode_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `ComputerUseEnabled object`

        The computer use setting was changed.

        - `type: optional "computer_use_enabled"`

          default: computer_use_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `ClaudeAPIInArtifactsEnabled object`

        The Claude API in Artifacts setting was changed.

        - `type: optional "claude_api_in_artifacts_enabled"`

          default: claude_api_in_artifacts_enabled

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

      - `ConversationPreferences object`

        The 'conversation_preferences' for the user were updated. Values omitted.

        - `type: optional "conversation_preferences"`

          default: conversation_preferences

      - `CoworkGlobalInstructions object`

        The Cowork global instructions were updated. Values omitted.

        - `type: optional "cowork_global_instructions"`

          default: cowork_global_instructions

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

  - `VerificationEvidenceSubmitted object`

    Verification evidence was submitted for an organization's verification.

    - `type: optional "verification_evidence_submitted"`

      default: verification_evidence_submitted

    - `actor: object or object or object or 8 more`

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
