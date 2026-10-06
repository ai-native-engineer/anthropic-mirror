<!-- source: https://platform.claude.com/docs/en/api/compliance/activities/list -->
<!-- part of: https://platform.claude.com/docs/en/api/compliance/activities/list -->

<!-- chunk-start -->

        - `ip_address: optional string or null`

        - `user_agent: optional string or null`

      - `FederatedActor object`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `type: optional "federated_actor"`

          default: federated_actor

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `tunnel_token_id: optional string or null`

      Id of the tunnel token issued with the tunnel and returned once in the create response; set only when creating the tunnel also issued its token, and absent for a tunnel whose token is revealed separately

  - `TunnelTokenMinted object`

    An OAuth bearer token for the tunnel management API was minted.

    - `type: optional "tunnel_token_minted"`

      default: tunnel_token_minted

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `updates: array of FullName or DisplayName or ArtifactsEnabled or 19 more`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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

    - `actor: APIActor or UserActor or UnauthenticatedUserActor or 8 more`

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

        - `provider: FederatedActorAwsProvider or FederatedActorAzureProvider or FederatedActorGcpProvider or FederatedActorOidcProvider`

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
    -H 'anthropic-version: 2023-06-01' \
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
