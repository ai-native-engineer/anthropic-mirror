<!-- source: https://platform.claude.com/docs/en/api/compliance/activities/list -->
<!-- part of: https://platform.claude.com/docs/en/api/compliance/activities/list -->

<!-- chunk-start -->

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `resource_id: string`

      The resource that was removed, e.g. "resource_01HX...".

    - `session_id: string`

      The agent session the resource belonged to, e.g. "session_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_agent_session_resource_deleted"`

      default: platform_agent_session_resource_deleted

    - `workspace_id: optional string or null`

      Tagged workspace ID, e.g. "wrkspc_01HX...". Optional because org-scoped credentials may not resolve a workspace at request time.

  - `PlatformAgentSessionResourceUpdated object`

    A resource attached to an agent session was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `resource_id: string`

      The resource that was updated, e.g. "resource_01HX...".

    - `session_id: string`

      The agent session the resource belongs to, e.g. "session_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_agent_session_resource_updated"`

      default: platform_agent_session_resource_updated

    - `workspace_id: optional string or null`

      Tagged workspace ID, e.g. "wrkspc_01HX...". Optional because org-scoped credentials may not resolve a workspace at request time.

  - `PlatformAgentSessionThreadArchived object`

    A thread within an agent session was archived.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `session_id: string`

      The agent session the thread belongs to, e.g. "session_01HX...".

    - `thread_id: string`

      The thread that was archived, e.g. "thread_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_agent_session_thread_archived"`

      default: platform_agent_session_thread_archived

    - `workspace_id: optional string or null`

      Tagged workspace ID, e.g. "wrkspc_01HX...". Optional because org-scoped credentials may not resolve a workspace at request time.

  - `PlatformAgentSessionUpdated object`

    An agent session was updated on the API platform.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `session_id: string`

      The agent session that was updated, e.g. "session_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_agent_session_updated"`

      default: platform_agent_session_updated

    - `workspace_id: optional string or null`

      Tagged workspace ID, e.g. "wrkspc_01HX...". Optional because org-scoped credentials may not resolve a workspace at request time.

  - `PlatformAgentUpdated object`

    An agent was updated on the API platform.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `agent_id: string`

      The agent that was updated, e.g. "agent_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_agent_updated"`

      default: platform_agent_updated

    - `workspace_id: optional string or null`

      Tagged workspace ID, e.g. "wrkspc_01HX...". Optional because org-scoped credentials may not resolve a workspace at request time.

  - `PlatformAPIKeyCreated object`

    An API key was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `api_key_id: string`

      Tagged ID of the created API key

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_api_key_created"`

      default: platform_api_key_created

  - `PlatformAPIKeyUpdated object`

    An API key was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `api_key_id: string`

      Tagged ID of the updated API key

    - `updates: array of object`

      - `current_value: string`

      - `previous_value: string`

      - `type: "name" or "status" or "workspace"`

        - `"name"`

        - `"status"`

        - `"workspace"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_api_key_updated"`

      default: platform_api_key_updated

  - `PlatformAppAttestAuthentication object`

    An attested mobile device attempted to exchange an Apple App Attest assertion for Anthropic API credentials.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `event_data: optional object or null`

      A nested object within a compliance activity payload.

      - `external_client_id: optional string or null`

        The registered external client the device presented, e.g. "clid_01HXZ4J2N8K5P7R9T3V6W1Y4M0".

      - `kid_hash: optional string or null`

        A truncated hash of the device's attested key identifier.

      - `workspace_id: optional string or null`

        The tagged ID of the workspace the minted token is bound to.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `request_id: optional string or null`

      The Anthropic API request identifier for correlation.

    - `status: optional object or null`

      A nested object within a compliance activity payload.

      - `outcome: string`

        Whether the token exchange succeeded or was denied.

      - `reason: optional string or null`

        A short reason code when the exchange did not succeed.

    - `type: optional "platform_app_attest_authentication"`

      default: platform_app_attest_authentication

  - `PlatformBillingUpgradedToPrepaid object`

    The organization's API billing was upgraded to the prepaid plan.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `previous_billing_type: string`

      The organization's billing type before this upgrade, for example "api_evaluation".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_billing_upgraded_to_prepaid"`

      default: platform_billing_upgraded_to_prepaid

  - `PlatformClearanceWorkspaceProgramRequestCleared object`

    A workspace's clearance program assignment was removed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `program_slug: string`

      The clearance program's identifier

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

    - `type: optional "platform_clearance_workspace_program_request_cleared"`

      default: platform_clearance_workspace_program_request_cleared

  - `PlatformClearanceWorkspaceProgramRequestSet object`

    A workspace's clearance program assignment was created or updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `opt_decision: "opt_in" or "opt_out" or "unspecified"`

      Whether the workspace is opted in or out of the program

      - `"opt_in"`

      - `"opt_out"`

      - `"unspecified"`

    - `program_slug: string`

      The clearance program's identifier

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

    - `type: optional "platform_clearance_workspace_program_request_set"`

      default: platform_clearance_workspace_program_request_set

  - `PlatformCostReportViewed object`

    The cost report was viewed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_cost_report_viewed"`

      default: platform_cost_report_viewed

  - `PlatformDreamArchived object`

    A Dream (asynchronous memory-consolidation job) was archived.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `dream_id: string`

      Tagged dream ID, e.g. "drm_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_dream_archived"`

      default: platform_dream_archived

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the dream belongs to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace.

  - `PlatformDreamCancelled object`

    A Dream (asynchronous memory-consolidation job) was cancelled before it completed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `dream_id: string`

      Tagged dream ID, e.g. "drm_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_dream_cancelled"`

      default: platform_dream_cancelled

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the dream belongs to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace.

  - `PlatformDreamCreated object`

    A Dream (asynchronous memory-consolidation job) was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `dream_id: string`

      Tagged dream ID, e.g. "drm_01HX...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_dream_created"`

      default: platform_dream_created

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the dream belongs to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace.

  - `PlatformFederatedAuthentication object`

    A federated workload identity attempted to exchange an OIDC token for Anthropic API credentials.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `event_data: optional object or null`

      A nested object within a compliance activity payload.

      - `federation_rule_id: optional string or null`

        The federation rule that matched the request, e.g. "fdrl_01HXZ4J2N8K5P7R9T3V6W1Y4M0".

      - `issuer_id: optional string or null`

        The registered identity issuer for the request, e.g. "fdis_01HXZ4H5M3K8P1R7T9V2W6Y4N0".

      - `oidc_token: optional object or null`

        A nested object within a compliance activity payload.

        - `claims: optional map[unknown] or null`

          The verified claims from the presented OIDC token.

        - `jti: optional string or null`

          The presented token's unique identifier (its `jti` claim).

      - `requested_service_account_id: optional string or null`

        The service account the caller requested to authenticate as, e.g. "svac_01HXZ4...".

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `request_id: optional string or null`

      The Anthropic API request identifier for correlation, e.g. "req_01HXZ4K7M9P2QR5T8V6W3Y1N0B".

    - `resources: optional array of object`

      The resources involved in the exchange.

      - `id: string`

        The identifier of the resource involved in the exchange.

      - `type: string`

        The kind of resource involved in the exchange.

    - `status: optional object or null`

      A nested object within a compliance activity payload.

      - `outcome: string`

        Whether the token exchange succeeded or was denied.

      - `detail: optional string or null`

        A human-readable explanation when the exchange did not succeed. May contain values copied verbatim from the presented token's header (e.g. kid, alg) and error text; treat as caller-supplied free text.

      - `reason: optional string or null`

        A short reason code when the exchange did not succeed.

    - `type: optional "platform_federated_authentication"`

      default: platform_federated_authentication

  - `PlatformFederationIssuerArchived object`

    An OIDC federation issuer was archived.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `federation_issuer_id: string`

      Tagged ID of the archived issuer

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_federation_issuer_archived"`

      default: platform_federation_issuer_archived

  - `PlatformFederationIssuerUpdated object`

    An OIDC federation issuer was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `federation_issuer_id: string`

      Tagged ID of the updated issuer

    - `updates: array of object`

      - `current_value: string`

      - `previous_value: string`

      - `type: "ca_cert_pem_sha256" or "check_jti" or "discovery_base" or 7 more`

        - `"ca_cert_pem_sha256"`

        - `"check_jti"`

        - `"discovery_base"`

        - `"issuer_url"`

        - `"jwks_keys_sha256"`

        - `"jwks_polling_disabled_at"`

        - `"jwks_source"`

        - `"jwks_url"`

        - `"max_jwt_lifetime_seconds"`

        - `"name"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_federation_issuer_updated"`

      default: platform_federation_issuer_updated

  - `PlatformFederationRuleArchived object`

    An OIDC federation rule was archived.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `federation_rule_id: string`

      Tagged ID of the archived rule

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_federation_rule_archived"`

      default: platform_federation_rule_archived

  - `PlatformFederationRuleUpdated object`

    An OIDC federation rule was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `federation_rule_id: string`

      Tagged ID of the updated rule

    - `updates: array of object`

      - `current_value: string`

      - `previous_value: string`

      - `type: "applies_to_all_workspaces" or "attributes" or "description" or 11 more`

        - `"applies_to_all_workspaces"`

        - `"attributes"`

        - `"description"`

        - `"match_audience"`

        - `"match_claims"`

        - `"match_condition"`

        - `"match_subject_prefix"`

        - `"name"`

        - `"oauth_scope"`

        - `"target_id"`

        - `"target_lookup_attr"`

        - `"target_type"`

        - `"token_lifetime_seconds"`

        - `"workspace_id"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_federation_rule_updated"`

      default: platform_federation_rule_updated

  - `PlatformFederationRuleWorkspaceAdded object`

    A federation rule was enabled for a workspace.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `federation_rule_id: string`

      Tagged ID of the federation rule

    - `workspace_id: string`

      Tagged ID of the workspace the rule was enabled for

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_federation_rule_workspace_added"`

      default: platform_federation_rule_workspace_added

  - `PlatformFederationRuleWorkspaceRemoved object`

    A federation rule was disabled for a workspace.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `federation_rule_id: string`

      Tagged ID of the federation rule

    - `workspace_id: string`

      Tagged ID of the workspace the rule was disabled for

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_federation_rule_workspace_removed"`

      default: platform_federation_rule_workspace_removed

  - `PlatformFileContentDownloaded object`

    Activity logged when file content is downloaded via GET /v1/files/{file_id}/content.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `file_id: string`

      The tagged ID of the downloaded file

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_file_content_downloaded"`

      default: platform_file_content_downloaded

  - `PlatformFileDeleted object`

    Activity logged when a file is deleted via DELETE /v1/files/{file_id}.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `file_id: string`

      The tagged ID of the deleted file

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_file_deleted"`

      default: platform_file_deleted

  - `PlatformFileUploaded object`

    Activity logged when a file is uploaded via POST /v1/files.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `file_id: string`

      The tagged ID of the uploaded file

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `session_id: optional string or null`

      The tagged session ID (agent-api only)

    - `type: optional "platform_file_uploaded"`

      default: platform_file_uploaded

  - `PlatformMemoryCreated object`

    An agent memory document was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_memory_created"`

      default: platform_memory_created

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the request was scoped to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace. May differ from the workspace the store was created in when the store is account-scoped.

  - `PlatformMemoryDeleted object`

    An agent memory document was deleted.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

      Tagged ID of the memory version produced by this change — the deletion tombstone, e.g. "memver_01HX...". Links this event to the version history.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_memory_deleted"`

      default: platform_memory_deleted

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the request was scoped to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace. May differ from the workspace the store was created in when the store is account-scoped.

  - `PlatformMemoryStoreArchived object`

    An agent memory store was archived. Archived stores reject new memory writes and cannot be attached to new sessions; deletion and redaction remain permitted for privacy scrubbing.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_memory_store_archived"`

      default: platform_memory_store_archived

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the request was scoped to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace. May differ from the workspace the store was created in when the store is account-scoped.

  - `PlatformMemoryStoreCreated object`

    An agent memory store was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_memory_store_created"`

      default: platform_memory_store_created

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the request was scoped to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace. May differ from the workspace the store was created in when the store is account-scoped.

  - `PlatformMemoryStoreDeleted object`

    An agent memory store was deleted. Memory content removal may complete asynchronously for very large stores.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_memory_store_deleted"`

      default: platform_memory_store_deleted

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the request was scoped to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace. May differ from the workspace the store was created in when the store is account-scoped.

  - `PlatformMemoryStoreUpdated object`

    An agent memory store's name, description, or metadata was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_memory_store_updated"`

      default: platform_memory_store_updated

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the request was scoped to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace. May differ from the workspace the store was created in when the store is account-scoped.

  - `PlatformMemoryUpdated object`

    An agent memory document's content or path was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_memory_updated"`

      default: platform_memory_updated

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the request was scoped to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace. May differ from the workspace the store was created in when the store is account-scoped.

  - `PlatformMemoryVersionRedacted object`

    A historical version of an agent memory document was redacted. Redaction scrubs the stored content of a specific version while preserving the version's existence in the history.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_memory_version_redacted"`

      default: platform_memory_version_redacted

    - `workspace_id: optional string or null`

      Tagged ID of the workspace the request was scoped to, e.g. "wrkspc_01HX...". For organization-scoped credentials this is the organization's default workspace. May differ from the workspace the store was created in when the store is account-scoped.

  - `PlatformOAuthAppCreated object`

    An OAuth app was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_oauth_app_created"`

      default: platform_oauth_app_created

  - `PlatformOAuthAppRevoked object`

    An OAuth app was revoked.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_oauth_app_revoked"`

      default: platform_oauth_app_revoked

  - `PlatformOAuthAppUpdated object`

    An OAuth app was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `oauth_app_id: string`

      Tagged ID of the updated app

    - `updates: array of object`

      - `current_value: string`

      - `previous_value: string`

      - `type: "apple_ios_attestation_environment" or "apple_ios_bundles" or "name" or "status"`

        - `"apple_ios_attestation_environment"`

        - `"apple_ios_bundles"`

        - `"name"`

        - `"status"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_oauth_app_updated"`

      default: platform_oauth_app_updated

  - `PlatformPluginDirectorySubmissionCreated object`

    A plugin directory submission was created on the API platform. A plugin directory submission is a request to list a plugin in the public plugin directory.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_plugin_directory_submission_created"`

      default: platform_plugin_directory_submission_created

  - `PlatformPluginDirectorySubmissionDeleted object`

    A plugin directory submission was deleted on the API platform.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_plugin_directory_submission_deleted"`

      default: platform_plugin_directory_submission_deleted

  - `PlatformPluginDirectorySubmissionUpdated object`

    A plugin directory submission was updated on the API platform.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_plugin_directory_submission_updated"`

      default: platform_plugin_directory_submission_updated

  - `PlatformServiceAccountArchived object`

    A service account was archived.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_service_account_archived"`

      default: platform_service_account_archived

  - `PlatformServiceAccountUpdated object`

    A service account was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `service_account_id: string`

      Tagged ID of the updated service account

    - `updates: array of object`

      - `current_value: string`

      - `previous_value: string`

      - `type: "description" or "organization_role"`

        - `"description"`

        - `"organization_role"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_service_account_updated"`

      default: platform_service_account_updated

  - `PlatformServiceAccountWorkspaceMemberAdded object`

    A service account was added as a member of a workspace.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_service_account_workspace_member_added"`

      default: platform_service_account_workspace_member_added

  - `PlatformServiceAccountWorkspaceMemberRemoved object`

    A service account was removed from a workspace.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_service_account_workspace_member_removed"`

      default: platform_service_account_workspace_member_removed

  - `PlatformServiceAccountWorkspaceMemberUpdated object`

    A service account's workspace membership role was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `service_account_id: string`

      Tagged ID of the service account

    - `updates: array of object`

      - `current_value: string`

      - `previous_value: string`

      - `type: "workspace_role"`

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

    - `type: optional "platform_service_account_workspace_member_updated"`

      default: platform_service_account_workspace_member_updated

  - `PlatformSigningKeyCreated object`

    Activity logged when a new request-signing key is registered for the org.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_signing_key_created"`

      default: platform_signing_key_created

  - `PlatformSigningKeyDeleted object`

    Activity logged when a signing key is permanently deleted.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_signing_key_deleted"`

      default: platform_signing_key_deleted

  - `PlatformSigningKeyRotated object`

    Activity logged when an in-memory signing key is rotated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_signing_key_rotated"`

      default: platform_signing_key_rotated

  - `PlatformSkillVersionCreated object`

    Activity logged when a skill version is created via POST /v1/skills/{skill_id}/versions.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_skill_version_created"`

      default: platform_skill_version_created

  - `PlatformSkillVersionDeleted object`

    Activity logged when a skill version is deleted via DELETE /v1/skills/{skill_id}/versions/{version}.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_skill_version_deleted"`

      default: platform_skill_version_deleted

  - `PlatformSpendLimitAlertEmailsUpdated object`

    Spend limit alert email addresses and role targets were updated for an org.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_spend_limit_alert_emails_updated"`

      default: platform_spend_limit_alert_emails_updated

  - `PlatformSpendLimitCreated object`

    An org-level fixed-dollar spend limit was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_spend_limit_created"`

      default: platform_spend_limit_created

  - `PlatformSpendLimitDeleted object`

    An org-level spend limit was removed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_spend_limit_deleted"`

      default: platform_spend_limit_deleted

  - `PlatformSpendLimitUpdated object`

    An org-level spend limit snooze/ignore state was changed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_spend_limit_updated"`

      default: platform_spend_limit_updated

  - `PlatformUsageReportClaudeCodeViewed object`

    The Claude Code usage report was viewed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_usage_report_claude_code_viewed"`

      default: platform_usage_report_claude_code_viewed

  - `PlatformUsageReportMessagesViewed object`

    The messages usage report was viewed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_usage_report_messages_viewed"`

      default: platform_usage_report_messages_viewed

  - `PlatformWorkspaceArchived object`

    A workspace was archived.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_workspace_archived"`

      default: platform_workspace_archived

  - `PlatformWorkspaceCreated object`

    A workspace was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_workspace_created"`

      default: platform_workspace_created

  - `PlatformWorkspaceInferenceDataRetentionDisabled object`

    The zero data retention override was disabled for a workspace.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_workspace_inference_data_retention_disabled"`

      default: platform_workspace_inference_data_retention_disabled

  - `PlatformWorkspaceInferenceDataRetentionEnabled object`

    The zero data retention override was enabled for a workspace.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_workspace_inference_data_retention_enabled"`

      default: platform_workspace_inference_data_retention_enabled

  - `PlatformWorkspaceMemberAdded object`

    A member was added to a workspace.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_workspace_member_added"`

      default: platform_workspace_member_added

  - `PlatformWorkspaceMemberRemoved object`

    A member was removed from a workspace.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_workspace_member_removed"`

      default: platform_workspace_member_removed

  - `PlatformWorkspaceMemberUpdated object`

    A workspace member was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `updates: array of object`

      - `current_value: string`

      - `previous_value: string`

      - `type: "workspace_role"`

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

    - `type: optional "platform_workspace_member_updated"`

      default: platform_workspace_member_updated

  - `PlatformWorkspaceMemberViewed object`

    A workspace member was viewed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_workspace_member_viewed"`

      default: platform_workspace_member_viewed

  - `PlatformWorkspaceMembersListed object`

    Workspace members were listed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_workspace_members_listed"`

      default: platform_workspace_members_listed

  - `PlatformWorkspaceRateLimitDeleted object`

    A workspace rate limit was deleted.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_workspace_rate_limit_deleted"`

      default: platform_workspace_rate_limit_deleted

  - `PlatformWorkspaceRateLimitUpdated object`

    A workspace rate limit was created or updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_workspace_rate_limit_updated"`

      default: platform_workspace_rate_limit_updated

  - `PlatformWorkspaceUpdated object`

    A workspace was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "platform_workspace_updated"`

      default: platform_workspace_updated

    - `updates: optional array of object`

      The field-level changes applied in this update

      - `current_value: string`

        Field value immediately after this change

      - `previous_value: string`

        Field value immediately before this change

      - `type: "allowed_inference_geos" or "default_inference_geo" or "display_color" or 4 more`

        The workspace field that changed

        - `"allowed_inference_geos"`

        - `"default_inference_geo"`

        - `"display_color"`

        - `"external_key_config_id"`

        - `"inference_data_retention"`

        - `"name"`

        - `"unspecified"`

  - `ClaudePluginCreated object`

    Plugin was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "claude_plugin_created"`

      default: claude_plugin_created

  - `ClaudePluginDeleted object`

    Plugin was deleted.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "claude_plugin_deleted"`

      default: claude_plugin_deleted

  - `ClaudePluginDisabled object`

    User disabled a plugin for their account.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "claude_plugin_disabled"`

      default: claude_plugin_disabled

  - `ClaudePluginEnabled object`

    User enabled a plugin for their account.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "claude_plugin_enabled"`

      default: claude_plugin_enabled

  - `PluginInstallationPreferenceUpdated object`

    An org admin changed the installation preference for a plugin.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "plugin_installation_preference_updated"`

      default: plugin_installation_preference_updated

  - `ClaudePluginReplaced object`

    Plugin was replaced.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "claude_plugin_replaced"`

      default: claude_plugin_replaced

  - `ClaudePluginUpdated object`

    Plugin was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "claude_plugin_updated"`

      default: claude_plugin_updated

  - `PrepaidAutoRechargeDisabled object`

    Auto-recharge was disabled for API prepaid org.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "prepaid_auto_recharge_disabled"`

      default: prepaid_auto_recharge_disabled

  - `PrepaidAutoRechargeUpdated object`

    Auto-recharge settings were updated for API prepaid org.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "prepaid_auto_recharge_updated"`

      default: prepaid_auto_recharge_updated

  - `PrepaidExtraUsageAutoReloadDisabled object`

    Prepaid usage credit auto-reload was disabled.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "prepaid_extra_usage_auto_reload_disabled"`

      default: prepaid_extra_usage_auto_reload_disabled

  - `PrepaidExtraUsageAutoReloadEnabled object`

    Prepaid usage credit auto-reload was enabled.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "prepaid_extra_usage_auto_reload_enabled"`

      default: prepaid_extra_usage_auto_reload_enabled

  - `PrepaidExtraUsageAutoReloadSettingsUpdated object`

    Prepaid usage credit auto-reload settings were updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "prepaid_extra_usage_auto_reload_settings_updated"`

      default: prepaid_extra_usage_auto_reload_settings_updated

  - `PrimaryOwnerTransferred object`

    Primary owner role was transferred to another org member.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `new_owner_id: string`

    - `previous_owner_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "primary_owner_transferred"`

      default: primary_owner_transferred

  - `ClaudeProjectArchived object`

    A Claude project was archived.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_archived"`

      default: claude_project_archived

  - `ClaudeProjectCreated object`

    A Claude project was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_created"`

      default: claude_project_created

  - `ClaudeProjectDeleted object`

    A Claude project was deleted.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_deleted"`

      default: claude_project_deleted

  - `ClaudeProjectDocumentAccessFailed object`

    An attempt to access a document in a Claude project failed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_project_document_id: string or null`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_document_access_failed"`

      default: claude_project_document_access_failed

  - `ClaudeProjectDocumentBulkDeletionAuditTruncated object`

    A bulk request to delete documents from a Claude project failed with more documents requested than were individually recorded in the audit log.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `audited_count: number`

      Number of documents that received an individual audit record.

    - `claude_project_id: string`

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

    - `type: optional "claude_project_document_bulk_deletion_audit_truncated"`

      default: claude_project_document_bulk_deletion_audit_truncated

  - `ClaudeProjectDocumentDeleted object`

    A document was deleted from a Claude project.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_document_deleted"`

      default: claude_project_document_deleted

  - `ClaudeProjectDocumentDeletionFailed object`

    A request to delete a document from a Claude project failed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_project_document_id: string or null`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_document_deletion_failed"`

      default: claude_project_document_deletion_failed

  - `ClaudeProjectDocumentUpdated object`

    The content of a document in a Claude project was replaced in place.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_document_updated"`

      default: claude_project_document_updated

  - `ClaudeProjectDocumentUploaded object`

    A document was uploaded to a Claude project.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_document_uploaded"`

      default: claude_project_document_uploaded

  - `ClaudeProjectDocumentViewed object`

    A document in a Claude project was viewed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_document_viewed"`

      default: claude_project_document_viewed

  - `ClaudeProjectFileAccessFailed object`

    An attempt to access a file in a Claude project failed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_file_access_failed"`

      default: claude_project_file_access_failed

  - `ClaudeProjectFileBulkDeletionAuditTruncated object`

    A bulk request to delete files from a Claude project failed with more files requested than were individually recorded in the audit log.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `audited_count: number`

      Number of files that received an individual audit record.

    - `claude_project_id: string`

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

    - `type: optional "claude_project_file_bulk_deletion_audit_truncated"`

      default: claude_project_file_bulk_deletion_audit_truncated

  - `ClaudeProjectFileDeleted object`

    A file was deleted from a Claude project.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_file_deleted"`

      default: claude_project_file_deleted

  - `ClaudeProjectFileDeletionFailed object`

    A request to delete a file from a Claude project failed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_file_id: string or null`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_file_deletion_failed"`

      default: claude_project_file_deletion_failed

  - `ClaudeProjectFileUploaded object`

    A file was uploaded to a Claude project.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_file_uploaded"`

      default: claude_project_file_uploaded

  - `ClaudeProjectReported object`

    A Claude project was reported.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_reported"`

      default: claude_project_reported

  - `ClaudeProjectSharingUpdated object`

    A Claude project's sharing settings were updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `audience: array of object or object`

      Sharing audience for the project. If empty, it's only visible to the creating user.

      - `Public object`

        Sharing audience: the project is visible to anyone with the link.

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

    - `type: optional "claude_project_sharing_updated"`

      default: claude_project_sharing_updated

  - `ClaudeProjectViewed object`

    A Claude project was viewed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `preview_only: optional boolean`

      default: false

    - `type: optional "claude_project_viewed"`

      default: claude_project_viewed

  - `ClaudePubsecIdentityConfigured object`

    SAML IdP configuration updated for a public sector organization.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "claude_pubsec_identity_configured"`

      default: claude_pubsec_identity_configured

  - `RbacRoleAssigned object`

    Admin assigned an RBAC custom role to a principal.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "rbac_role_assigned"`

      default: rbac_role_assigned

  - `RbacRoleCreated object`

    Admin created an RBAC custom role.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "rbac_role_created"`

      default: rbac_role_created

  - `RbacRoleDeleted object`

    Admin deleted an RBAC custom role.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "rbac_role_deleted"`

      default: rbac_role_deleted

  - `RbacRolePermissionAdded object`

    Admin added a permission to an RBAC custom role.

    Emitted once per requested permission, including permissions the role
    already had, so a retried request still produces a complete audit record.

    - `action: string`

      Action permitted on the resource

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "rbac_role_permission_added"`

      default: rbac_role_permission_added

  - `RbacRolePermissionRemoved object`

    Admin removed a permission from an RBAC custom role.

    Emitted once per requested permission, including permissions the role
    already lacked, so a retried request still produces a complete audit
    record.

    - `action: string`

      Action that was permitted on the resource

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "rbac_role_permission_removed"`

      default: rbac_role_permission_removed

  - `RbacRoleUnassigned object`

    Admin unassigned an RBAC custom role from a principal.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "rbac_role_unassigned"`

      default: rbac_role_unassigned

  - `RbacRoleUpdated object`

    Admin updated an RBAC custom role.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "rbac_role_updated"`

      default: rbac_role_updated

  - `RoleAssignmentGranted object`

    Role assignment was granted.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `target_id: optional string or null`

      ID of the grantee: a user ID for a member, a group ID for a group, the organization ID for an organization-wide grant.

    - `target_type: optional string or null`

      What kind of grantee received the role, for example "organization_member", "group", or "organization".

    - `type: optional "role_assignment_granted"`

      default: role_assignment_granted

  - `RoleAssignmentRevoked object`

    Role assignment was revoked.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `target_id: optional string or null`

      ID of the grantee that held the role: a user ID for a member, a group ID for a group, the organization ID for an organization-wide grant.

    - `target_type: optional string or null`

      What kind of grantee held the role, for example "organization_member", "group", or "organization".

    - `type: optional "role_assignment_revoked"`

      default: role_assignment_revoked

  - `SSOLoginFailed object`

    An SSO sign-in attempt failed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "sso_login_failed"`

      default: sso_login_failed

  - `SSOLoginInitiated object`

    A user started an SSO sign-in flow.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "sso_login_initiated"`

      default: sso_login_initiated

  - `SSOLoginSucceeded object`

    A user successfully signed in with SSO.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `auth_method: optional "sso"`

      The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

      default: sso

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `mfa_method: optional "not_used" or null`

      The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multistep login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "sso_login_succeeded"`

      default: sso_login_succeeded

  - `SSOSecondFactorMagicLink object`

    SSO second factor magic link was used.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "sso_second_factor_magic_link"`

      default: sso_second_factor_magic_link

  - `ScimUserCreated object`

    A SCIM user was provisioned.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "scim_user_created"`

      default: scim_user_created

  - `ScimUserDeleted object`

    A SCIM user was deleted.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "scim_user_deleted"`

      default: scim_user_deleted

  - `ScimUserUpdated object`

    A SCIM user was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "scim_user_updated"`

      default: scim_user_updated

  - `ScopedAPIKeyDeleted object`

    A scoped API key was deleted.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `api_key_id: string`

      Tagged ID of the deleted scoped API key

    - `api_key_name: string`

      Name of the deleted scoped API key

    - `scopes: array of string`

      Scopes the deleted key had

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "scoped_api_key_deleted"`

      default: scoped_api_key_deleted

  - `ScopedAPIKeyUpdated object`

    A scoped API key was renamed or its activation state changed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `api_key_id: string`

      Tagged ID of the updated scoped API key

    - `updates: array of object`

      - `current_value: string`

      - `previous_value: string`

      - `type: "activation_state" or "name"`

        - `"activation_state"`

        - `"name"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "scoped_api_key_updated"`

      default: scoped_api_key_updated

  - `SeatTierChangesCancelled object`

    Scheduled seat tier downgrades were cancelled.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "seat_tier_changes_cancelled"`

      default: seat_tier_changes_cancelled

  - `SeatTiersPurchased object`

    Seat tiers were purchased or upgraded on a subscription.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "seat_tiers_purchased"`

      default: seat_tiers_purchased

  - `ServiceCreated object`

    Activity logged when an org service is explicitly created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "service_created"`

      default: service_created

  - `ServiceDeleted object`

    Activity logged when an org service is deleted.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "service_deleted"`

      default: service_deleted

  - `ServiceKeyCreated object`

    Activity logged when a new org service key is created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "service_key_created"`

      default: service_key_created

  - `ServiceKeyRevoked object`

    Activity logged when an org service key is revoked.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "service_key_revoked"`

      default: service_key_revoked

  - `SessionRevoked object`

    User revoked a specific session.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "session_revoked"`

      default: session_revoked

  - `SessionShareAccessed object`

    Session share was accessed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "session_share_accessed"`

      default: session_share_accessed

  - `SessionShareCreated object`

    Session share was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "session_share_created"`

      default: session_share_created

  - `SessionShareRevoked object`

    Session share was revoked.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "session_share_revoked"`

      default: session_share_revoked

  - `ClaudeSkillCreated object`

    Skill was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "claude_skill_created"`

      default: claude_skill_created

  - `ClaudeSkillDeleted object`

    Skill was deleted.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `skill_id: optional string or null`

    - `skill_name: optional string or null`

    - `type: optional "claude_skill_deleted"`

      default: claude_skill_deleted

    - `versions_deleted: optional number or null`

      Set when the deletion removed the skill's versions in the same request (the public API's cascading skill delete): one consolidated record of what went with the skill, reconcilable against earlier version-created records, rather than one version-deleted activity per row. versions_deleted is the exact count; deleted_version_ids lists at most the newest 1000 (truncated when versions_deleted exceeds its length).

  - `ClaudeSkillDisabled object`

    User disabled a skill for their account.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "claude_skill_disabled"`

      default: claude_skill_disabled

  - `ClaudeSkillEnabled object`

    User enabled a skill for their account.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "claude_skill_enabled"`

      default: claude_skill_enabled

  - `ClaudeSkillReplaced object`

    Skill was replaced.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "claude_skill_replaced"`

      default: claude_skill_replaced

  - `SlackWorkspaceClaimRevoked object`

    A Slack workspace or Enterprise Grid organization was disconnected
    from the organization for Claude in Slack.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `scope: optional string`

      Blast radius of the revocation: 'workspace' for one Slack workspace, 'enterprise_grid' for every workspace in a Slack Enterprise Grid organization

      default: workspace

    - `type: optional "slack_workspace_claim_revoked"`

      default: slack_workspace_claim_revoked

  - `SlackWorkspaceClaimed object`

    A Slack workspace or Enterprise Grid organization was connected to
    the organization for Claude in Slack.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `scope: optional string`

      Blast radius of the claim: 'workspace' for one Slack workspace, 'enterprise_grid' for every workspace in a Slack Enterprise Grid organization

      default: workspace

    - `type: optional "slack_workspace_claimed"`

      default: slack_workspace_claimed

  - `SocialLoginSucceeded object`

    A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `provider: "apple" or "google" or "microsoft"`

      - `"apple"`

      - `"google"`

      - `"microsoft"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `auth_method: optional "social"`

      The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

      default: social

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `mfa_method: optional "not_used" or null`

      The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multistep login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "social_login_succeeded"`

      default: social_login_succeeded

  - `StepUpAuthenticationFailed object`

    An additional identity check failed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "step_up_authentication_failed"`

      default: step_up_authentication_failed

  - `StepUpAuthenticationSucceeded object`

    The user completed an additional identity check to confirm a sensitive action.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "step_up_authentication_succeeded"`

      default: step_up_authentication_succeeded

  - `StepUpCredentialEnrolled object`

    A user enrolled a passkey for confirming sensitive actions on their account.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "step_up_credential_enrolled"`

      default: step_up_credential_enrolled

  - `SubscriptionCancellationScheduled object`

    Subscription cancellation was scheduled at end of billing period.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "subscription_cancellation_scheduled"`

      default: subscription_cancellation_scheduled

  - `SubscriptionQuantityUpdated object`

    Contracted subscription seat quantity was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `added_seats: number`

    - `new_quantity: number`

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

    - `type: optional "subscription_quantity_updated"`

      default: subscription_quantity_updated

  - `SubscriptionRenewed object`

    A cancelled subscription was renewed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "subscription_renewed"`

      default: subscription_renewed

  - `SubscriptionResumed object`

    A scheduled subscription cancellation was reversed.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "subscription_resumed"`

      default: subscription_resumed

  - `SubscriptionStarted object`

    A new subscription was created (Team or Enterprise).

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "subscription_started"`

      default: subscription_started

  - `SubscriptionUpgraded object`

    Subscription plan was upgraded (e.g. Team to Enterprise).

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "subscription_upgraded"`

      default: subscription_upgraded

  - `TrustedDeviceCredentialRotated object`

    The identity-verification credential of a trusted device was rotated to a new key.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "trusted_device_credential_rotated"`

      default: trusted_device_credential_rotated

  - `TrustedDeviceEnrolled object`

    A device was enrolled as a trusted device for the user's account. Trusted devices can be used to confirm the user's identity for sensitive actions.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "trusted_device_enrolled"`

      default: trusted_device_enrolled

  - `TrustedDeviceRevoked object`

    A trusted device was removed from the user's account.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "trusted_device_revoked"`

      default: trusted_device_revoked

  - `TunnelArchived object`

    An MCP tunnel was archived.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "tunnel_archived"`

      default: tunnel_archived

  - `TunnelCertificateAdded object`

    An inner-TLS CA certificate was added to a tunnel.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "tunnel_certificate_added"`

      default: tunnel_certificate_added

  - `TunnelCertificateRevoked object`

    An inner-TLS CA certificate was revoked from a tunnel.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "tunnel_certificate_revoked"`

      default: tunnel_certificate_revoked

  - `TunnelCreated object`

    An MCP tunnel was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "tunnel_created"`

      default: tunnel_created

  - `TunnelTokenMinted object`

    An OAuth bearer token for the tunnel management API was minted.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "tunnel_token_minted"`

      default: tunnel_token_minted

  - `TunnelTokenRevealed object`

    The Cloudflare connector secret for a tunnel was revealed to the caller.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "tunnel_token_revealed"`

      default: tunnel_token_revealed

  - `TunnelTokenRevoked object`

    An OAuth bearer token for the tunnel management API was revoked.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "tunnel_token_revoked"`

      default: tunnel_token_revoked

  - `TunnelTokenRotated object`

    The Cloudflare connector secret for a tunnel was rotated.

    `tunnel_token_id` is the id of the *newly-issued* token. The previous
    token is invalidated by the rotation and its id is not recorded here.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "tunnel_token_rotated"`

      default: tunnel_token_rotated

  - `UserConsentRecorded object`

    User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "user_consent_recorded"`

      default: user_consent_recorded

  - `UserConsentRevoked object`

    User revoked a previously granted consent for a specific entity.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "user_consent_revoked"`

      default: user_consent_revoked

  - `ClaudeUserRoleUpdated object`

    A user's role within the organization was changed, or the user was added to or removed from the organization.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `current_role: string or null`

      If null, then user was removed from the Organization

    - `previous_role: string or null`

      If null, then user was added to the Organization

    - `user_email: string`

      Email of the user whose role was changed

    - `user_id: string`

      ID of the user whose role was changed

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

      format: date-time

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_user_role_updated"`

      default: claude_user_role_updated

  - `ClaudeUserSettingsUpdated object`

    User updated their personal settings.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

        - `user_agent: optional string or null`

    - `updates: array of object or object or object or 19 more`

      - `FullName object`

        - `current_value: string or null`

        - `previous_value: string or null`

        - `type: optional "full_name"`

          default: full_name

      - `DisplayName object`

        - `current_value: string or null`

        - `previous_value: string or null`

        - `type: optional "display_name"`

          default: display_name

      - `ArtifactsEnabled object`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "artifacts_enabled"`

          default: artifacts_enabled

      - `LatexEnabled object`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "latex_enabled"`

          default: latex_enabled

      - `AnalysisToolEnabled object`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "analysis_tool_enabled"`

          default: analysis_tool_enabled

      - `ChatSuggestionsEnabled object`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "chat_suggestions_enabled"`

          default: chat_suggestions_enabled

      - `MultimodalPdfsEnabled object`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "multimodal_pdfs_enabled"`

          default: multimodal_pdfs_enabled

      - `GDriveEnabled object`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "gdrive_enabled"`

          default: gdrive_enabled

      - `WebSearchEnabled object`

        The web search setting was changed.

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

        - `type: optional "web_search_enabled"`

          default: web_search_enabled

      - `GeolocationEnabled object`

        The geolocation setting was changed.

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

        - `type: optional "geolocation_enabled"`

          default: geolocation_enabled

      - `UserMemoryEnabledSetting object`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "enabled_saffron"`

          default: enabled_saffron

      - `McpToolsEnabled object`

        - `current_value: map[boolean] or null`

        - `previous_value: map[boolean] or null`

        - `type: optional "mcp_tools_enabled"`

          default: mcp_tools_enabled

      - `CliOpPermissionsEnabled object`

        - `current_value: map[string] or null`

        - `previous_value: map[string] or null`

        - `type: optional "cli_op_permissions_enabled"`

          default: cli_op_permissions_enabled

      - `GoogleDriveSearchEnabled object`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "google_drive_search_enabled"`

          default: google_drive_search_enabled

      - `GmailIntegrationEnabled object`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "gmail_integration_enabled"`

          default: gmail_integration_enabled

      - `GoogleCalendarIntegrationEnabled object`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "google_calendar_integration_enabled"`

          default: google_calendar_integration_enabled

      - `ThinkingModeEnabled object`

        - `current_value: "adaptive" or "extended" or "off" or null`

          - `"adaptive"`

          - `"extended"`

          - `"off"`

        - `previous_value: "adaptive" or "extended" or "off" or null`

          - `"adaptive"`

          - `"extended"`

          - `"off"`

        - `type: optional "thinking_mode_enabled"`

          default: thinking_mode_enabled

      - `ResearchModeEnabled object`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "research_mode_enabled"`

          default: research_mode_enabled

      - `ComputerUseEnabled object`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "computer_use_enabled"`

          default: computer_use_enabled

      - `ClaudeAPIInArtifactsEnabled object`

        The Claude API in Artifacts setting was changed.

        - `current_value: optional boolean or null`

          Setting value immediately after this change

        - `previous_value: optional boolean or null`

          Setting value immediately before this change

        - `type: optional "claude_api_in_artifacts_enabled"`

          default: claude_api_in_artifacts_enabled

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

    - `type: optional "claude_user_settings_updated"`

      default: claude_user_settings_updated

  - `VerificationEvidenceSubmitted object`

    Verification evidence was submitted for an organization's verification.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "verification_evidence_submitted"`

      default: verification_evidence_submitted

  - `VerificationProgramApplicationCreated object`

    An organization applied to a verification program.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "verification_program_application_created"`

      default: verification_program_application_created

  - `WorkspaceMemberSpendLimitCreated object`

    A per-member or workspace-default Claude Code spend limit was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "workspace_member_spend_limit_created"`

      default: workspace_member_spend_limit_created

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceMemberSpendLimitDeleted object`

    A per-member or workspace-default Claude Code spend limit was deleted.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "workspace_member_spend_limit_deleted"`

      default: workspace_member_spend_limit_deleted

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceMemberSpendLimitUpdated object`

    A per-member Claude Code spend limit amount was updated.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "workspace_member_spend_limit_updated"`

      default: workspace_member_spend_limit_updated

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceSpendLimitAlertEmailsUpdated object`

    Spend limit alert email recipients were updated for a workspace.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "workspace_spend_limit_alert_emails_updated"`

      default: workspace_spend_limit_alert_emails_updated

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceSpendLimitCreated object`

    A workspace-level API spend limit was created.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "workspace_spend_limit_created"`

      default: workspace_spend_limit_created

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceSpendLimitDeleted object`

    A workspace-level API spend limit was deleted.

    - `actor: object or object or object or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          default: api_actor

      - `UserActor object`

        - `email_address: string`

          format: email

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          default: user_actor

      - `UnauthenticatedUserActor object`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          default: unauthenticated_user_actor

        - `unauthenticated_email_address: optional string or null`

          format: email

      - `AnthropicActor object`

        - `email_address: optional string or null`

          format: email

        - `type: optional "anthropic_actor"`

          default: anthropic_actor

      - `SystemActor object`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          default: system_actor

      - `AdminAPIKeyActor object`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          default: admin_api_key_actor

      - `ServiceAccountActor object`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          default: service_account_actor

      - `ScimDirectorySyncActor object`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          default: scim_directory_sync_actor

      - `FederatedIdentityActor object`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          default: federated_identity_actor

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object or object or object or object`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              default: aws

          - `FederatedActorAzureProvider object`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              default: azure

          - `FederatedActorGcpProvider object`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              default: gcp

          - `FederatedActorOidcProvider object`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              default: oidc

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          default: attested_device_actor

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

    - `type: optional "workspace_spend_limit_deleted"`

      default: workspace_spend_limit_deleted

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
