<!-- source: https://platform.claude.com/docs/en/api/http/compliance -->
<!-- part of: https://platform.claude.com/docs/en/api/http/compliance -->

<!-- chunk-start -->

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

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/activities \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

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

## Compliance API › Organizations

### List organizations

**GET** `/v1/compliance/organizations`

List organizations under the parent organization.

Returns organizations sorted by creation date in ascending order. Use
`limit` and `page` to paginate: each response includes `has_more` and a
`next_page` token to pass on the next request.

#### Query parameters

- `limit: optional number`

  Maximum results (default: 1000, max: 1000)

  default: 1000, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of organizations sorted by creation date, ascending

  - `created_at: string`

    Organization creation time (RFC 3339 format)

  - `name: string`

    Organization name

  - `uuid: string`

    Unique identifier for the organization (UUID format)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: optional string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2025-03-12T18:22:41.123456+00:00",
      "name": "Acme Corp",
      "uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Compliance API › Organizations › Users

### List organization users

**GET** `/v1/compliance/organizations/{org_uuid}/users`

List current user members of an organization.

#### Path parameters

- `org_uuid: string`

  The organization UUID

#### Query parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

  default: 500, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of current organization members sorted by organization join date ascending

  - `id: string`

    User identifier (tagged ID)

  - `created_at: string`

    User account creation timestamp

    format: date-time

  - `email: string`

    User's current email address

  - `full_name: string`

    User's current full name

  - `organization_role: "admin" or "billing" or "claude_code_user" or 8 more`

    User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"parent_org_admin"`

    - `"parent_org_owner"`

    - `"primary_owner"`

    - `"user"`

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/users \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "created_at": "2025-03-12T18:22:41.123456Z",
      "email": "jane.doe@example.com",
      "full_name": "Jane Doe",
      "organization_role": "admin"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Compliance API › Organizations › Roles

### List Compliance Roles

**GET** `/v1/compliance/organizations/{org_uuid}/roles`

List Compliance Roles

#### Path parameters

- `org_uuid: string`

  The organization UUID

#### Query parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

  default: 500, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of roles

  - `id: string`

    Role identifier (tagged ID)

  - `created_at: string or null`

    Role creation timestamp (RFC 3339)

    format: date-time

  - `description: string`

    Role description

  - `name: string`

    Role name

  - `updated_at: string or null`

    Role last-updated timestamp (RFC 3339)

    format: date-time

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
      "created_at": "2025-03-12T18:22:41.123456Z",
      "description": "Full administrative access to organization settings and members",
      "name": "Organization Admin",
      "updated_at": "2025-03-14T09:05:17.456789Z"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

### Get Compliance Role

**GET** `/v1/compliance/organizations/{org_uuid}/roles/{role_id}`

Get Compliance Role

#### Path parameters

- `org_uuid: string`

  The organization UUID

- `role_id: string`

  The role ID (tagged ID, e.g., rbac_role_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Role identifier (tagged ID)

- `created_at: string or null`

  Role creation timestamp (RFC 3339)

  format: date-time

- `description: string`

  Role description

- `name: string`

  Role name

- `updated_at: string or null`

  Role last-updated timestamp (RFC 3339)

  format: date-time

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "description": "Full administrative access to organization settings and members",
  "name": "Organization Admin",
  "updated_at": "2025-03-14T09:05:17.456789Z"
}
```

## Compliance API › Organizations › Roles › Permissions

### List Compliance Role Permissions

**GET** `/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions`

List Compliance Role Permissions

#### Path parameters

- `org_uuid: string`

  The organization UUID

- `role_id: string`

  The role ID (tagged ID, e.g., rbac_role_abc123)

#### Query parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

  default: 500, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of permissions

  - `action: string`

    Action permitted on the resource

  - `resource_id: string`

    Identifier of the resource the permission applies to

  - `resource_type: string`

    Type of resource the permission applies to

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID/permissions \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "action": "claude_code",
      "resource_id": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
      "resource_type": "organization"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Compliance API › Organizations › Settings

### Get effective organization settings

**GET** `/v1/compliance/organizations/{organization_id}/settings`

Retrieve the effective settings for an organization.

Returns the settings currently in force for the given organization — the
enforced state after all policies are applied, which may differ from what
is configured in the admin console. Settings an organization's
administrators cannot change (for example, ones controlled by Anthropic
policy or not available to the organization) are omitted from the list.
Settings that report a compliance arrangement with Anthropic are the
exception: the HIPAA and Access Transparency settings are always included;
the API zero data retention setting is reported for Claude Console
organizations, and the Claude Code zero data retention and customer-managed
encryption keys (CMEK) settings for Claude Enterprise organizations. Each
reports whether the arrangement is in place at the organization level; a
retention setting on an individual workspace is not reflected.

The organization must belong to the API key's organization hierarchy;
unknown organizations and organizations outside the hierarchy return 404.

#### Path parameters

- `organization_id: string`

  The organization's UUID

#### Headers

- `"x-api-key": optional string`

#### Returns

- `type: optional "effective_organization_settings"`

  default: effective_organization_settings

- `api_keys: array of object`

  Compliance API keys configured for the organization hierarchy, ordered by creation time ascending. Key secret values are never included.

  - `type: optional "compliance_api_key"`

    default: compliance_api_key

  - `id: string`

    Unique identifier for the API key.

  - `created_at: string`

    When the key was created.

    format: date-time

  - `created_by_id: string or null`

    Identifier of the user who created the key, or null when the key was created by automation or its creator's account no longer exists.

  - `is_active: boolean`

    Whether the key is currently active. A deactivated key is listed for audit visibility but cannot authenticate requests.

  - `name: string`

    The name given to the API key when it was created.

  - `scopes: array of string`

    The permission scopes granted to the key.

  - `expires_at: optional string or null`

    When the key will stop authenticating, or null when the key does not expire.

    format: date-time

- `organization_id: string`

- `settings: array of Boolean or Integer or String or 3 more`

  - `Boolean object`

    A setting whose enforced value is a single true/false flag.

    - `type: optional "boolean"`

      default: boolean

    - `name: "access_transparency_enabled" or "ai_powered_artifacts_enabled" or "api_workbench_feedback_collection_enabled" or 59 more`

      - `"access_transparency_enabled"`

      - `"ai_powered_artifacts_enabled"`

      - `"api_workbench_feedback_collection_enabled"`

      - `"api_zero_data_retention_enabled"`

      - `"artifact_connectors_enabled"`

      - `"ask_your_org_enabled"`

      - `"chat_enabled"`

      - `"claude_academy_inference_enabled"`

      - `"claude_ai_chat_sharing_enabled"`

      - `"claude_ai_feedback_collection_enabled"`

      - `"claude_ai_integration_sharing_enabled"`

      - `"claude_ai_skill_plugins_scanning_enabled"`

      - `"claude_code_desktop_bypass_permissions_enabled"`

      - `"claude_code_desktop_enabled"`

      - `"claude_code_fast_mode_enabled"`

      - `"claude_code_metrics_logging_enabled"`

      - `"claude_code_remote_control_enabled"`

      - `"claude_code_review_enabled"`

      - `"claude_code_routines_enabled"`

      - `"claude_code_security_enabled"`

      - `"claude_code_trusted_devices_required"`

      - `"claude_code_web_enabled"`

      - `"claude_code_workflows_enabled"`

      - `"claude_design_enabled"`

      - `"claude_enterprise_claude_code_zero_data_retention_enabled"`

      - `"claude_in_slack_enabled"`

      - `"claude_science_custom_connectors_enabled"`

      - `"claude_science_custom_skills_enabled"`

      - `"claude_science_enabled"`

      - `"claude_science_managed_network_allowlist_enabled"`

      - `"claude_science_memory_enabled"`

      - `"claude_science_modal_enabled"`

      - `"claude_science_scientific_model_endpoints_enabled"`

      - `"claude_science_ssh_hosts_enabled"`

      - `"cmek_enabled"`

      - `"code_execution_enabled"`

      - `"code_execution_network_egress_enabled"`

      - `"connector_tools_default_always_allow"`

      - `"content_redaction_enabled"`

      - `"cowork_trusted_devices_required"`

      - `"desktop_extension_allowlist_enabled"`

      - `"directory_sync_enabled"`

      - `"frontier_data_use_enabled"`

      - `"group_skill_sharing_enabled"`

      - `"hipaa_compliance_enabled"`

      - `"inline_visualizations_enabled"`

      - `"ip_allowlist_enabled"`

      - `"location_metadata_enabled"`

      - `"member_usage_dashboard_visible"`

      - `"memory_enabled"`

      - `"org_wide_skill_sharing_enabled"`

      - `"project_sharing_enabled"`

      - `"public_projects_enabled"`

      - `"skill_sharing_enabled"`

      - `"skills_enabled"`

      - `"sso_claude_ai_enforced"`

      - `"sso_console_enforced"`

      - `"sso_enabled"`

      - `"third_party_interactive_content_enabled"`

      - `"user_skill_creation_enabled"`

      - `"web_search_enabled"`

      - `"work_across_apps_enabled"`

    - `value: boolean`

  - `Integer object`

    A setting whose enforced value is a whole number; null means no limit
    is in force.

    - `type: optional "integer"`

      default: integer

    - `name: "account_session_duration_seconds"`

    - `value: number or null`

  - `String object`

    A setting whose enforced value is a single string; null means no value
    is configured.

    - `type: optional "string"`

      default: string

    - `name: "claude_code_default_worker_environment_id" or "claude_code_default_worker_pool_id"`

      - `"claude_code_default_worker_environment_id"`

      - `"claude_code_default_worker_pool_id"`

    - `value: string or null`

  - `StringList object`

    A setting whose enforced value is a list of strings.

    - `type: optional "string_list"`

      default: string_list

    - `name: "allowed_invite_domains" or "disabled_admin_request_types" or "ip_allowlist_ip_ranges"`

      - `"allowed_invite_domains"`

      - `"disabled_admin_request_types"`

      - `"ip_allowlist_ip_ranges"`

    - `value: array of string`

  - `ProvisioningMode object`

    How organization members are provisioned, resolved to the enforced mode.

    A configured mode is reported only while the mechanism that enforces it is
    active: just-in-time modes require single sign-on to be enabled, and SCIM
    modes require directory sync to be enabled. Otherwise `login_only` is
    reported, regardless of any stored configuration.

    - `type: optional "provisioning_mode"`

      default: provisioning_mode

    - `value: "jit_advanced" or "jit_permissive" or "login_only" or 2 more`

      How organization members are provisioned under SSO.

      - `"jit_advanced"`

      - `"jit_permissive"`

      - `"login_only"`

      - `"scim_advanced"`

      - `"scim_permissive"`

    - `name: optional "sso_provisioning_mode"`

      default: sso_provisioning_mode

  - `DataRetention object`

    The data retention periods in force, keyed by the type of data they
    apply to.

    A key of `all` covers every data type and is exclusive: when present it
    is the only key. A missing key means no organization-level
    administrator-configured retention period is in force for that data type;
    Anthropic's service defaults may still apply.

    - `type: optional "data_retention"`

      default: data_retention

    - `value: map[Fixed or Indefinite]`

      - `Fixed object`

        A fixed retention window measured from each item's last activity.

        - `type: optional "fixed"`

          default: fixed

        - `duration: number`

        - `timescale: "day" or "month"`

          - `"day"`

          - `"month"`

      - `Indefinite object`

        An indefinite retention period: data is kept with no time limit.

        - `type: optional "indefinite"`

          default: indefinite

    - `name: optional "data_retention_periods"`

      default: data_retention_periods

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/organizations/$ORGANIZATION_ID/settings \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "api_keys": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "created_by_id": "created_by_id",
      "is_active": true,
      "name": "name",
      "scopes": [
        "string"
      ],
      "expires_at": "2019-12-27T18:11:19.117Z",
      "type": "compliance_api_key"
    }
  ],
  "organization_id": "organization_id",
  "settings": [
    {
      "name": "access_transparency_enabled",
      "value": true,
      "type": "boolean"
    }
  ],
  "type": "effective_organization_settings"
}
```

## Compliance API › Groups

### List Compliance Groups

**GET** `/v1/compliance/groups`

List Compliance Groups

#### Query parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

  default: 500, minimum: 1, maximum: 1000

- `name_prefix: optional string`

  Filter groups by name prefix

  default: ""

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of groups

  - `id: string`

    Group identifier (tagged ID)

  - `created_at: string or null`

    Group creation timestamp (RFC 3339)

    format: date-time

  - `description: string`

    Group description

  - `name: string`

    Group name

  - `roles: array of string or null`

    Role IDs assigned to this group.

  - `source_type: string`

    How the group was created ('direct' or 'scim')

  - `updated_at: string or null`

    Group last-updated timestamp (RFC 3339)

    format: date-time

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/groups \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "created_at": "2025-03-12T18:22:41.123456Z",
      "description": "All members of the engineering organization",
      "name": "Engineering Team",
      "roles": [
        "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
        "rbac_role_01HtCd4mFoAseWS3RnzKcwE7"
      ],
      "source_type": "scim",
      "updated_at": "2025-03-14T09:05:17.456789Z"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

### Get Compliance Group

**GET** `/v1/compliance/groups/{group_id}`

Get Compliance Group

#### Path parameters

- `group_id: string`

  The group ID (tagged ID, e.g., rbac_group_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Group identifier (tagged ID)

- `created_at: string or null`

  Group creation timestamp (RFC 3339)

  format: date-time

- `description: string`

  Group description

- `name: string`

  Group name

- `roles: array of string or null`

  Role IDs assigned to this group.

- `source_type: string`

  How the group was created ('direct' or 'scim')

- `updated_at: string or null`

  Group last-updated timestamp (RFC 3339)

  format: date-time

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "description": "All members of the engineering organization",
  "name": "Engineering Team",
  "roles": [
    "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
    "rbac_role_01HtCd4mFoAseWS3RnzKcwE7"
  ],
  "source_type": "scim",
  "updated_at": "2025-03-14T09:05:17.456789Z"
}
```

## Compliance API › Groups › Members

### List Compliance Group Members

**GET** `/v1/compliance/groups/{group_id}/members`

List Compliance Group Members

#### Path parameters

- `group_id: string`

  The group ID (tagged ID, e.g., rbac_group_abc123)

#### Query parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

  default: 500, minimum: 1, maximum: 1000

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of group members

  - `created_at: string or null`

    Membership creation timestamp (RFC 3339)

    format: date-time

  - `email: string`

    Member email address

  - `updated_at: string or null`

    Membership last-updated timestamp (RFC 3339)

    format: date-time

  - `user_id: string`

    Member user identifier (tagged ID)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID/members \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2025-03-12T18:22:41.123456Z",
      "email": "jane.doe@example.com",
      "updated_at": "2025-03-14T09:05:17.456789Z",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Compliance API › Apps › Chats

### List chats

**GET** `/v1/compliance/apps/chats`

Lists chat metadata with filtering capabilities for targeted
compliance review. Results are sorted chronologically (time ascending)
by the `order_by` key, with ties broken by id.

Incremental polling with `order_by=updated_at` returns a chat again
after it receives a new message, is moved into or out of a project, or
is deleted in claude.ai. A chat is not guaranteed to be returned again
after other edits, such as a rename.

**Deprecation notice:** Combining `user_ids[]` with any `updated_at.*`
filter is deprecated and will be rejected with HTTP 400 after
2026-09-22. For incremental polling by update time, omit `user_ids[]`
and set `order_by=updated_at` with `after_id` cursor pagination —
this returns the same chats across the whole organization in a single
request stream. For per-user listing, use `created_at.*` filters (or
no time filter) with the default `order_by`. `user_ids[]` with
`order_by=updated_at` is already rejected.

#### Query parameters

- `after_id: optional string`

  Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `before_id: optional string`

  Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `created_at: optional object`

  - `gt: optional string`

    Filter chats created after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter chats created at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter chats created before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter chats created at or before this time (RFC 3339 format)

    format: date-time

- `limit: optional number`

  Maximum results (default: 100, max: 1000)

  default: 100, minimum: 1, maximum: 1000

- `order_by: optional "created_at" or "updated_at"`

  Sort key for results. `created_at` (default) sorts by chat creation time. `updated_at` sorts by last update time and is only supported for org-wide queries (omit user_ids[]). For org-wide queries, any time filter must match the sort key: `created_at.*` filters require `order_by=created_at`, and `updated_at.*` filters require `order_by=updated_at`.

  default: created_at

  - `"created_at"`

  - `"updated_at"`

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

- `project_ids: optional array of string`

  Filter by project IDs (accepts `claude_proj_...`). Enumerate IDs via `GET /v1/compliance/apps/projects`. Requires user_ids[]; not supported for org-wide queries.

- `updated_at: optional object`

  - `gt: optional string`

    Filter chats updated after this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

    format: date-time

  - `gte: optional string`

    Filter chats updated at or after this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

    format: date-time

  - `lt: optional string`

    Filter chats updated before this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

    format: date-time

  - `lte: optional string`

    Filter chats updated at or before this time (RFC 3339 format). Combining updated_at filters with `user_ids[]` is deprecated and will be rejected after 2026-09-22; for updated_at-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

    format: date-time

- `user_ids: optional array of string`

  Filter to chats created by specific users (max 10 per request). Omit for an org-wide query. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`. Deprecated combination: passing `user_ids[]` together with any `updated_at.*` filter is deprecated and will be rejected after 2026-09-22. For `updated_at`-windowed polling, omit `user_ids[]` and use `order_by=updated_at` with `after_id` pagination.

  maxItems: 10

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of chat metadata sorted chronologically by the request's `order_by` key (default `created_at`), tie break by id

  - `id: string`

    Chat ID

  - `created_at: string`

    Creation timestamp

    format: date-time

  - `deleted_at: string or null`

    Deletion timestamp if deleted

    format: date-time

  - `href: string`

    URL to view this chat in claude.ai

  - `model: string or null`

    Model selected for this chat (e.g. 'claude-opus-5'). May be null for legacy chats that never had a model recorded.

  - `name: string`

    Chat name/title

  - `organization_uuid: string`

    Organization UUID this chat belongs to

  - `project_id: string or null`

    Project ID this chat belongs to

  - `updated_at: string`

    Last update timestamp. Updated when the chat receives a new message, is moved into or out of a project, or is deleted in claude.ai. Other edits, such as renaming the chat, are not guaranteed to change it.

    format: date-time

  - `user: object or null`

    The user who created the chat. Null when the API key is restricted to one organization and the creator is no longer a member of it.

    - `id: string`

      User identifier

    - `email_address: string`

      User's email address

  - `organization_id: string`

    **Deprecated**

    Organization ID this chat belongs to

- `first_id: string or null`

  Opaque pagination cursor for the first chat in the current result set. Pass as `before_id` on the next request to page backwards. Backward pagination is only supported for per-user queries (`user_ids[]` set); org-wide queries do not accept `before_id`. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `last_id: string or null`

  Opaque pagination cursor for the last chat in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "claude_chat_abc123",
      "name": "Product Requirements Discussion",
      "created_at": "2025-06-07T08:09:10Z",
      "updated_at": "2025-06-07T09:10:11Z",
      "organization_id": "org_abc123",
      "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
      "project_id": "claude_proj_xyz789",
      "model": "claude-opus-5",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      },
      "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789"
    }
  ],
  "has_more": false,
  "first_id": "eyJrIjogImNyZWF0ZWRfYXQiLCAidCI6ICIyMDI1LTA2LTA3VDA4OjA5OjEwKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLTIzNDUtNjc4OS1hYmNkLWVmMDEyMzQ1Njc4OSJ9",
  "last_id": "eyJrIjogImNyZWF0ZWRfYXQiLCAidCI6ICIyMDI1LTA2LTA3VDA4OjA5OjEwKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLTIzNDUtNjc4OS1hYmNkLWVmMDEyMzQ1Njc4OSJ9"
}
```

### Delete chat

**DELETE** `/v1/compliance/apps/chats/{claude_chat_id}`

Permanently deletes a chat and all associated messages and
files. This is a destructive operation that cannot be undone.

#### Path parameters

- `claude_chat_id: string`

  The chat ID (tagged ID, e.g., claude_chat_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `type: optional "claude_chat_deleted"`

  Constant string confirming deletion

  default: claude_chat_deleted

- `id: string`

  The ID of the Claude chat that was deleted

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "claude_chat_abc123",
  "type": "claude_chat_deleted"
}
```

## Compliance API › Apps › Chats › Messages

### Get chat messages

**GET** `/v1/compliance/apps/chats/{claude_chat_id}/messages`

Retrieves message history and file metadata for a specific chat.

#### Path parameters

- `claude_chat_id: string`

  The chat ID (tagged ID, e.g., claude_chat_abc123)

#### Query parameters

- `after_id: optional string`

  Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `before_id: optional string`

  Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `created_at: optional object`

  - `gt: optional string`

    Filter messages created after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter messages created at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter messages created before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter messages created at or before this time (RFC 3339 format)

    format: date-time

- `limit: optional number`

  Maximum results (max: 1000). When omitted, the full result set is returned in one response.

  minimum: 1, maximum: 1000

- `order: optional "asc" or "desc"`

  Sort direction for messages within the response. `asc` (the default) returns oldest-first; `desc` returns newest-first.

  default: asc

  - `"asc"`

  - `"desc"`

- `tool_result_max_chars: optional number`

  Maximum characters returned per tool-result text item. Items longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

  default: 10000, minimum: -1

- `tool_use_input_max_chars: optional number`

  Maximum characters of JSON-encoded tool input returned per tool_use block. Inputs longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

  default: 10000, minimum: -1

- `updated_at: optional object`

  - `gt: optional string`

    Filter messages updated after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter messages updated at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter messages updated before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter messages updated at or before this time (RFC 3339 format)

    format: date-time

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Chat ID

- `chat_messages: array of object`

  Array of chat messages in order of created_at

  - `id: string`

    Unique identifier for the message e.g. 'claude_chat_msg_abcd1234'

  - `artifacts: array of object or null`

    Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.

    - `id: string`

      Artifact ID e.g. 'claude_artifact_abc123'

    - `artifact_type: string or null`

      MIME-like artifact type e.g. 'application/vnd.ant.code'

    - `title: string or null`

      Artifact title

    - `version_id: string`

      Artifact version ID e.g. 'claude_artifact_version_abc123'

  - `content: array of Text or ToolUse or ToolResult`

    Content blocks within the message

    - `Text object`

      Text content block.

      - `type: "text"`

        default: text

      - `text: string`

        Text content from human or assistant

      - `thinking_redacted: boolean`

        True when content enclosed in the assistant's internal-reasoning tags (or the tag markup itself) was removed from `text` during export. Removal never occurs with this field false. Always false on human messages, whose text is exported verbatim.

        default: false

      - `truncated: boolean`

        True when `text` was shortened by the server's fixed per-string bound (1 MiB). Always false on chat text blocks.

        default: false

    - `ToolUse object`

      Tool invocation requested by the assistant.

      - `type: "tool_use"`

        default: tool_use

      - `id: string or null`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

      - `integration_name: string or null`

        Name of the integration that provides this tool, when applicable

      - `mcp_server_url: string or null`

        Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass the endpoint's tool-use input max parameter as -1 to request full content, subject to any server-side maximum the endpoint enforces.

        default: false

    - `ToolResult object`

      Result returned by a tool invocation.

      - `type: "tool_result"`

        default: tool_result

      - `content: array of object`

        Text content returned by the tool. Generated files are surfaced via the message's `generated_files` list; other non-text item types (including images and links) are omitted.

        - `type: "text"`

          default: text

        - `text: string`

          Text returned by the tool

      - `integration_name: string or null`

        Name of the integration that provides this tool, when applicable

      - `is_error: boolean`

        True when the tool reported an error

      - `mcp_server_url: string or null`

        Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string or null`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened. Pass the endpoint's tool-result max parameter as -1 to request full content, subject to any server-side maximum the endpoint enforces.

        default: false

  - `created_at: string`

    Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

    format: date-time

  - `files: array of object or null`

    Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

    - `id: string`

      File ID

    - `created_at: string`

      File creation timestamp

      format: date-time

    - `filename: string`

      Display name of the file

    - `md5: string or null`

      Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available.

    - `mime_type: string or null`

      MIME type of the file's preferred downloadable variant (e.g. 'application/pdf')

    - `size_bytes: number or null`

      Size in bytes of the file's preferred downloadable variant, if known. Null for older files uploaded before size was recorded.

  - `generated_files: array of object or null`

    Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download an entry whose id starts with `claude_gen_file_` via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`, and one whose id starts with `claude_file_` via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

    - `id: string`

      Id of the file: either a generated-file id, e.g. 'claude_gen_file_abc123', or a file id, e.g. 'claude_file_abc123'; the prefix tells them apart. Download the first from the generated-files content endpoint and the second from the files content endpoint. Treat everything after the prefix as an opaque string; the encoding may change without notice.

    - `filename: string`

      Display name of the generated file

    - `md5: string or null`

      Lowercase hex MD5 of the generated file, when available. Null when no stored hash is available.

    - `mime_type: string or null`

      MIME type of the file, when known

    - `size_bytes: number or null`

      Size in bytes of the generated file, when available. Null when the file has expired or size is not recorded.

  - `role: "assistant" or "user"`

    Message sender (user or assistant)

    - `"assistant"`

    - `"user"`

- `created_at: string`

  Creation timestamp

  format: date-time

- `deleted_at: string or null`

  Deletion timestamp if deleted

  format: date-time

- `first_id: string or null`

  Opaque pagination cursor for the first message in the current result set. Pass as `before_id` on the next request to page backwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `has_more: boolean`

  Whether more chat messages exist beyond the current result set. Use `last_id` as `after_id` in a follow-up request to page forward.

  default: false

- `href: string`

  URL to view this chat in claude.ai

- `last_id: string or null`

  Opaque pagination cursor for the last message in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `model: string or null`

  Model selected for this chat (e.g. 'claude-opus-5'). May be null for legacy chats that never had a model recorded.

- `name: string`

  Chat name

- `organization_uuid: string`

  Organization UUID this chat belongs to

- `project_id: string or null`

  Project ID this chat belongs to

- `updated_at: string`

  Last update timestamp. Updated when the chat receives a new message, is moved into or out of a project, or is deleted in claude.ai. Other edits, such as renaming the chat, are not guaranteed to change it.

  format: date-time

- `user: object or null`

  The user who created the chat. Null when the API key is restricted to one organization and the creator is no longer a member of it.

  - `id: string`

    User identifier

  - `email_address: string`

    User's email address

- `organization_id: string`

  **Deprecated**

  Organization ID this chat belongs to

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID/messages \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "claude_chat_abc123",
  "name": "Product Requirements Discussion",
  "created_at": "2025-06-07T08:09:10Z",
  "updated_at": "2025-06-07T08:09:11Z",
  "organization_id": "org_abc123",
  "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
  "project_id": "claude_proj_xyz789",
  "model": "claude-opus-5",
  "user": {
    "id": "user_xyz456",
    "email_address": "user@example.com"
  },
  "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789",
  "chat_messages": [
    {
      "id": "claude_chat_msg_abc123",
      "role": "user",
      "created_at": "2025-06-07T08:09:10Z",
      "content": [
        {
          "type": "text",
          "text": "Can you help me draft requirements for our new dashboard feature?"
        }
      ],
      "files": [
        {
          "id": "claude_file_xyz789",
          "filename": "dashboard_mockup_v1.pdf",
          "mime_type": "application/pdf",
          "size_bytes": 12345,
          "md5": "5d41402abc4b2a76b9719d911017c592",
          "created_at": "2025-06-07T08:09:10Z"
        }
      ]
    },
    {
      "id": "claude_chat_msg_def456",
      "role": "assistant",
      "created_at": "2025-06-07T08:09:11Z",
      "content": [
        {
          "type": "text",
          "text": "I'd be happy to help you draft requirements for your dashboard feature..."
        }
      ],
      "artifacts": [
        {
          "id": "claude_artifact_abc123",
          "version_id": "claude_artifact_version_xyz789",
          "title": "Dashboard Requirements Draft",
          "artifact_type": "text/markdown"
        }
      ]
    }
  ],
  "has_more": false,
  "first_id": "eyJtc2dfdXVpZCI6ICIwZjcwYjA2Ni0uLi4ifQ==",
  "last_id": "eyJtc2dfdXVpZCI6ICJhNGUwYjE3Mi0uLi4ifQ=="
}
```

## Compliance API › Apps › Chats › Files

### Get file metadata

**GET** `/v1/compliance/apps/chats/files/{claude_file_id}`

Retrieves metadata for a file referenced in chat messages, without
downloading the file content. Use the sibling `/content` endpoint to
download the bytes.

#### Path parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  File ID

- `claude_chat_ids: array of string`

  Chats this file is attached to. A file can be referenced by messages across multiple chats.

- `created_at: string`

  File creation timestamp

  format: date-time

- `filename: string or null`

  Display name of the file, if set

- `md5: string or null`

  Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes; when the two disagree, the header is authoritative.

- `message_ids: array of string`

  Chat message IDs this file is attached to. A file can be referenced by multiple messages.

- `mime_type: string or null`

  MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

- `size_bytes: number or null`

  Size in bytes of the file's preferred downloadable variant, if known

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "claude_file_xyz789",
  "filename": "quarterly_report.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1048576,
  "md5": "5d41402abc4b2a76b9719d911017c592",
  "created_at": "2024-01-15T10:30:00Z",
  "message_ids": [
    "claude_chat_msg_abc123"
  ],
  "claude_chat_ids": [
    "claude_chat_def456"
  ]
}
```

### Delete file

**DELETE** `/v1/compliance/apps/chats/files/{claude_file_id}`

Permanently deletes a specific file. This is a destructive
operation that cannot be undone.

#### Path parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `type: optional "claude_file_deleted"`

  Constant string confirming deletion

  default: claude_file_deleted

- `id: string`

  The ID of the file that was deleted

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "claude_file_xyz789",
  "type": "claude_file_deleted"
}
```

### Download file content

**GET** `/v1/compliance/apps/chats/files/{claude_file_id}/content`

Downloads the binary content of a file referenced in chat messages.

#### Path parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

#### Headers

- `"x-api-key": optional string`

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID/content \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Compliance API › Apps › Chats › Generated Files

### Get Claude-generated file metadata

**GET** `/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}`

Returns metadata for a file the assistant created via tool use.

Use the sibling `/content` endpoint to download the bytes.

#### Path parameters

- `claude_gen_file_id: string`

  The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Opaque generated-file id, e.g. 'claude_gen_file_abc123'.

- `claude_chat_id: string`

  The chat this generated file belongs to

- `created_at: string or null`

  File creation timestamp, when available

  format: date-time

- `filename: string`

  Display name of the generated file

- `md5: string or null`

  Lowercase hex MD5 of the stored file. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

- `mime_type: string or null`

  MIME type of the stored file, when available

- `size_bytes: number or null`

  Size in bytes of the stored file, when available

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "mime_type",
  "size_bytes": 0
}
```

### Download a Claude-generated file

**GET** `/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`

Downloads the binary content of a file the assistant created via tool use.

#### Path parameters

- `claude_gen_file_id: string`

  The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.

#### Headers

- `"x-api-key": optional string`

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID/content \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Compliance API › Apps › Projects

### List projects

**GET** `/v1/compliance/apps/projects`

Lists project metadata with filtering capabilities. Results
are sorted chronologically (time ascending) by created_at.

#### Query parameters

- `created_at: optional object`

  - `gt: optional string`

    Filter projects created after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter projects created at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter projects created before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter projects created at or before this time (RFC 3339 format)

    format: date-time

- `limit: optional number`

  Maximum results (default: 20, max: 100)

  default: 20, minimum: 1, maximum: 100

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `updated_at: optional object`

  - `gt: optional string`

    Filter projects updated after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter projects updated at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter projects updated before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter projects updated at or before this time (RFC 3339 format)

    format: date-time

- `user_ids: optional array of string`

  Filter by user IDs. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  List of projects sorted by creation date ascending

  - `id: string`

    Project identifier (tagged ID)

  - `created_at: string`

    Project creation timestamp

    format: date-time

  - `deleted_at: string or null`

    Timestamp when the project was deleted by an end user, or null otherwise

    format: date-time

  - `is_private: boolean`

    If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

  - `name: string`

    Project name

  - `organization_uuid: string`

    Organization UUID this project belongs to

  - `updated_at: string`

    Project last update timestamp

    format: date-time

  - `user: object or null`

    Project creator information, or null if the creator's account has been deleted or the creator is no longer a member of an organization the key may read

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

  - `organization_id: string`

    **Deprecated**

    Organization identifier (tagged ID)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "claude_proj_abc123",
      "name": "Q4 Product Planning",
      "created_at": "2025-06-01T10:00:00Z",
      "updated_at": "2025-06-15T14:30:00Z",
      "is_private": true,
      "organization_id": "org_abc123",
      "organization_uuid": "abc12345-6789-0abc-def0-123456789abc",
      "user": {
        "id": "user_xyz456",
        "email_address": "user@example.com"
      }
    }
  ],
  "has_more": true,
  "next_page": "page_eyJjcmVhdGVkX2F0IjoiMjAyNS0wNi0wMVQxMDowMDowMFoiLCJ1dWlkIjoiYWJjMTIzIn0="
}
```

### Get project details

**GET** `/v1/compliance/apps/projects/{project_id}`

Get detailed information for a specific project.

#### Path parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Project identifier (tagged ID)

- `attachments_count: number`

  Number of attachments contained within this project

- `chats_count: number`

  Number of chats contained within this project

- `created_at: string`

  Project creation timestamp

  format: date-time

- `deleted_at: string or null`

  Timestamp when the project was deleted by an end user, or null otherwise

  format: date-time

- `description: string`

  Project description

- `instructions: string`

  Project's custom instructions / prompt

- `is_private: boolean`

  If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

- `name: string`

  Project name

- `organization_uuid: string`

  Organization UUID this project belongs to

- `updated_at: string`

  Project last update timestamp

  format: date-time

- `user: object or null`

  Project creator information, or null if the creator's account has been deleted or the creator is no longer a member of an organization the key may read

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

- `organization_id: string`

  **Deprecated**

  Organization identifier (tagged ID)

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "claude_proj_01Nm7PqRsTuVwXyZaBcDeFgH",
  "attachments_count": 3,
  "chats_count": 14,
  "created_at": "2025-03-12T18:22:41.123456Z",
  "deleted_at": "2019-12-27T18:11:19.117Z",
  "description": "Planning and research for the Q3 launch",
  "instructions": "Focus on concise, actionable answers.",
  "is_private": true,
  "name": "Q3 Product Launch",
  "organization_id": "org_015eofRkKpogX7uDKUyvBTph",
  "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
  "updated_at": "2025-03-14T09:05:17.456789Z",
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
  }
}
```

### Delete project

**DELETE** `/v1/compliance/apps/projects/{project_id}`

Delete a project for compliance purposes.

Hard-deletes the project and all its associated data including:

- All project documents and files
- All role assignments
- Knowledge base (if RAG is enabled)
- Sync sources

Project must have no attached chats - returns 409 if chats exist.

#### Path parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `type: optional "claude_project_deleted"`

  Constant string confirming deletion.

  default: claude_project_deleted

- `id: string`

  The ID of the Claude project that was deleted

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "type": "claude_project_deleted"
}
```

## Compliance API › Apps › Projects › Attachments

### List project attachments

**GET** `/v1/compliance/apps/projects/{project_id}/attachments`

List files and documents attached to a project.

List files and project documents attached to the project referenced by project_id.
This includes the IDs of attached files, and attached project documents.

The raw binary content of attached files can be downloaded using the
GET /v1/compliance/apps/chats/files/{claude_file_id}/content endpoint.

The text content of attached project documents can be fetched using the
GET /v1/compliance/apps/projects/documents/{claude_proj_doc_id} endpoint.

#### Path parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

#### Query parameters

- `limit: optional number`

  Maximum results (default: 20, max: 100)

  default: 20, minimum: 1, maximum: 100

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of ComplianceProjectFileReference or ComplianceProjectDocReference`

  List of attachments sorted chronologically by created_at, tie break by id

  - `ComplianceProjectFileReference object`

    File attachment reference for compliance responses.

    - `type: "project_file"`

      Discriminator marking this as a binary file

      default: project_file

    - `id: string`

      File identifier (e.g., 'claude_file_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

      format: date-time

    - `filename: string`

      Display name of the file (e.g., 'document.pdf')

    - `md5: string or null`

      Lowercase hex MD5 of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

    - `mime_type: string`

      MIME type of the file's preferred downloadable variant when one is recorded, else 'application/octet-stream'. Use the per-file `/metadata` endpoint for the authoritative value.

    - `size_bytes: number or null`

      Size in bytes of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

  - `ComplianceProjectDocReference object`

    Project document attachment reference for compliance responses.

    - `type: "project_doc"`

      Discriminator marking this as a plain text document

      default: project_doc

    - `id: string`

      Project document identifier (e.g., 'claude_proj_doc_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

      format: date-time

    - `filename: string`

      Display name of the document (e.g., 'document.txt')

    - `mime_type: "text/plain"`

      MIME type of the project document, always set to plain text

      default: text/plain

    - `updated_at: string or null`

      Last-modified timestamp of the document. Reserved for future use — currently always null.

      format: date-time

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  To get the next page, use the 'next_page' from the current response as the 'page' in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/attachments \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "filename": "filename",
      "md5": "md5",
      "mime_type": "mime_type",
      "size_bytes": 0,
      "type": "project_file"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

## Compliance API › Apps › Projects › Collaborators

### List project collaborators

**GET** `/v1/compliance/apps/projects/{project_id}/collaborators`

List the users, groups, and organization-wide grants on a project.

Each entry represents one active role assignment on the project. Principals
are returned as a discriminated union on `type` — an individual user, an
RBAC group, the whole organization, or all holders of an organization-level
role.

#### Path parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

#### Query parameters

- `limit: optional number`

  Maximum results (default: 20, max: 100)

  default: 20, minimum: 1, maximum: 100

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of ComplianceProjectUserCollaborator or ComplianceProjectGroupCollaborator or ComplianceProjectOrganizationCollaborator or ComplianceProjectOrganizationRoleCollaborator`

  List of collaborators sorted chronologically by granted_at, tie break by the underlying role-assignment UUID

  - `ComplianceProjectUserCollaborator object`

    An individual user granted a role on a project.

    - `type: "user"`

      Discriminator marking this as an individual user collaborator

      default: user

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

      format: date-time

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `user_id: string or null`

      Identifier of the user granted access (tagged ID), or null if their account has since been deleted

  - `ComplianceProjectGroupCollaborator object`

    An RBAC group granted a role on a project.

    - `type: "group"`

      Discriminator marking this as a group collaborator

      default: group

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

      format: date-time

    - `group_id: string`

      Identifier of the group granted access (tagged ID)

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

  - `ComplianceProjectOrganizationCollaborator object`

    An entire organization granted a role on a project.

    - `type: "organization"`

      Discriminator marking this as an organization-wide grant

      default: organization

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

      format: date-time

    - `organization_uuid: string`

      UUID of the organization granted access

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

  - `ComplianceProjectOrganizationRoleCollaborator object`

    All holders of an organization-level role granted a role on a project.

    - `type: "organization_role"`

      Discriminator marking this as a grant to all organization members holding a specific org-level role

      default: organization_role

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

      format: date-time

    - `organization_role: string`

      The organization-level role whose holders are granted access

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  To get the next page, use the 'next_page' from the current response as the 'page' in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/collaborators \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "granted_at": "2019-12-27T18:11:19.117Z",
      "role": "admin",
      "type": "user",
      "user_id": "user_id"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

## Compliance API › Apps › Projects › Documents

### Get project document content

**GET** `/v1/compliance/apps/projects/documents/{document_id}`

Get detailed information for a specific project document.

#### Path parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Project document identifier (tagged ID)

- `content: string`

  Document text content

- `created_at: string`

  Document creation timestamp

  format: date-time

- `filename: string`

  Document filename

- `user: object or null`

  Document creator information, or null if the creator's account has been deleted or the creator is no longer a member of an organization the key may read

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "claude_proj_doc_01Qr8StUvWxYzAbCdEfGhJjK",
  "content": "# Design notes\n\n- Item one\n- Item two\n",
  "created_at": "2025-03-12T18:22:41.123456Z",
  "filename": "design-notes.txt",
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
  }
}
```

### Get project document metadata

**GET** `/v1/compliance/apps/projects/documents/{document_id}/metadata`

Returns metadata for a project document, without the content body.

Use the sibling `GET /v1/compliance/apps/projects/documents/{document_id}`
endpoint to fetch the document text. The `md5` and `size_bytes`
fields here are computed over the UTF-8 encoding of that text, so a DLP
consumer can dedupe or match hashes without downloading every document.

#### Path parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Project document identifier (tagged ID)

- `claude_project_id: string`

  The project this document belongs to

- `created_at: string`

  Document creation timestamp

  format: date-time

- `filename: string`

  Document filename

- `md5: string`

  Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.

- `mime_type: "text/plain"`

  MIME type of the document content, always plain text

  default: text/plain

- `size_bytes: number`

  Size in bytes of the document content (UTF-8 encoded)

- `user: object or null`

  Document creator information, or null if the creator's account has been deleted or the creator is no longer a member of an organization the key may read

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID/metadata \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "claude_project_id": "claude_project_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "filename": "filename",
  "md5": "md5",
  "mime_type": "text/plain",
  "size_bytes": 0,
  "user": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "email_address": "jane.doe@example.com"
  }
}
```

### Delete project document

**DELETE** `/v1/compliance/apps/projects/documents/{document_id}`

Delete a project document for compliance purposes.

Hard-deletes the project document permanently.

#### Path parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `type: "claude_project_document_deleted"`

  Constant string confirming deletion.

  default: claude_project_document_deleted

- `id: string`

  The ID of the project document that was deleted

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "type": "claude_project_document_deleted"
}
```

## Compliance API › Apps › Artifacts

### Get artifact metadata

**GET** `/v1/compliance/apps/artifacts/{artifact_version_id}`

Returns metadata for an artifact version, without the content body.

Use the sibling `/content` endpoint to fetch the artifact text. The
`md5` and `size_bytes` fields here are computed over the UTF-8
encoding of that text, so a DLP consumer can dedupe or match hashes
without downloading every artifact.

#### Path parameters

- `artifact_version_id: string`

  The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `id: string`

  Artifact ID e.g. 'claude_artifact_abc123'

- `artifact_type: string or null`

  MIME-like artifact type e.g. 'application/vnd.ant.code'

- `claude_chat_id: string`

  The chat this artifact belongs to

- `created_at: string`

  Artifact version creation timestamp

  format: date-time

- `md5: string`

  Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

- `size_bytes: number`

  Size in bytes of the artifact content (UTF-8 encoded)

- `title: string or null`

  Artifact title

- `version_id: string`

  Artifact version ID e.g. 'claude_artifact_version_abc123'

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "artifact_type": "artifact_type",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "md5": "md5",
  "size_bytes": 0,
  "title": "title",
  "version_id": "version_id"
}
```

### Download artifact content

**GET** `/v1/compliance/apps/artifacts/{artifact_version_id}/content`

Download the content of an artifact version for compliance purposes.

Returns the full text content of the artifact version.

#### Path parameters

- `artifact_version_id: string`

  The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

#### Headers

- `"x-api-key": optional string`

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID/content \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Compliance API › Apps › Sessions › Local

### List local sessions

**GET** `/v1/compliance/apps/sessions/local`

List local sessions across the organizations the key may read.

Results are ordered by `created_at` descending. Pagination is
forward-only via `next_page`; there is no reverse cursor.

#### Query parameters

- `created_at: optional object`

  - `gte: optional string`

    Only return sessions whose first inference call is at or after this time (RFC 3339; a UTC offset is required).

    format: date-time

  - `lt: optional string`

    Only return sessions whose first inference call is strictly before this time (RFC 3339; a UTC offset is required).

    format: date-time

- `limit: optional number`

  Maximum results (default: 100, max: 500)

  default: 100, minimum: 1, maximum: 500

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `updated_at: optional object`

  - `gte: optional string`

    Only return sessions whose last inference call is at or after this time (RFC 3339; a UTC offset is required). Combines with `created_at.gte` / `created_at.lt`; the ordering and pagination are unchanged. Use it to poll for sessions that have been active since a previous pass — a session that becomes active later can only enter the result, never leave it.

    format: date-time

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  Page of local sessions, ordered by `created_at` descending; ties are broken by a fixed server-side order. `updated_at` never participates in the ordering; the `updated_at.gte` query parameter filters on it without changing the order or the pagination cursor.

  - `type: "compliance_local_session"`

    default: compliance_local_session

  - `id: string`

    Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

  - `created_at: string`

    Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

    format: date-time

  - `organization_uuid: string`

    UUID of the child organization the session belongs to

  - `product_surface: string or null`

    The product the session ran in: `cowork` (Cowork in Claude Desktop on the user's machine), `claude_code` (Claude Code), `claude_science` (Claude Science), `claude_in_chrome` (the Claude in Chrome browser extension's built-in chat), or one of `office_agents/excel`, `office_agents/powerpoint`, `office_agents/word`, and `office_agents/outlook` (Claude for Microsoft 365, by app; `office_agents` alone when the app is not identified). New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

  - `truncated: boolean`

    True when the session has more inference calls than the service can return for one session (100,000). The messages endpoint then returns only the session's earliest calls, up to that many, and ends before the session does; `updated_at` is a lower bound on the latest call and can differ between the list and retrieve endpoints. False for every session within that bound.

    default: false

  - `updated_at: string`

    Timestamp of the session's last retained inference call (RFC 3339, UTC). Always at or after `created_at`. When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected — but because retention removes only the oldest calls, this value (unlike `created_at`) is unaffected until the entire session has aged out. On the list endpoint this value is a lower bound: for a session still active at a page or `created_at.lt` window boundary it can momentarily lag the session's true last activity. Retrieving the session, or its messages, always reflects the exact latest retained call.

    format: date-time

  - `user: object`

    The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

    - `id: string`

      User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

    - `email_address: string or null`

      User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

  - `workspace_id: string or null`

    Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

- `next_page: string or null`

  Opaque pagination cursor (prefixed `page_`) for the next page. Null when there is no further page. Treat as an opaque string; the format may change without notice.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/sessions/local \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "type": "compliance_local_session",
      "id": "clls_eyJ2IjoxLCJvIjoiOWEx…",
      "organization_uuid": "9a1e0000-0000-0000-0000-000000000000",
      "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR",
      "user": {
        "id": "user_01GpKpLmNoPqRsTuVwXyZaBc",
        "email_address": "engineer@example.com"
      },
      "product_surface": "cowork",
      "created_at": "2026-07-09T14:02:11Z",
      "updated_at": "2026-07-09T15:47:33Z"
    }
  ]
}
```

### Retrieve a local session

**GET** `/v1/compliance/apps/sessions/local/{local_session_id}`

Retrieve one local session.

The response is the same session object the list endpoint returns,
with `user.email_address` resolved the same way. Retention is
enforced when the response is served: a session whose every
inference call has aged out returns 404.

#### Path parameters

- `local_session_id: string`

#### Headers

- `"x-api-key": optional string`

#### Returns

- `type: "compliance_local_session"`

  default: compliance_local_session

- `id: string`

  Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

- `created_at: string`

  Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

  format: date-time

- `organization_uuid: string`

  UUID of the child organization the session belongs to

- `product_surface: string or null`

  The product the session ran in: `cowork` (Cowork in Claude Desktop on the user's machine), `claude_code` (Claude Code), `claude_science` (Claude Science), `claude_in_chrome` (the Claude in Chrome browser extension's built-in chat), or one of `office_agents/excel`, `office_agents/powerpoint`, `office_agents/word`, and `office_agents/outlook` (Claude for Microsoft 365, by app; `office_agents` alone when the app is not identified). New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

- `truncated: boolean`

  True when the session has more inference calls than the service can return for one session (100,000). The messages endpoint then returns only the session's earliest calls, up to that many, and ends before the session does; `updated_at` is a lower bound on the latest call and can differ between the list and retrieve endpoints. False for every session within that bound.

  default: false

- `updated_at: string`

  Timestamp of the session's last retained inference call (RFC 3339, UTC). Always at or after `created_at`. When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected — but because retention removes only the oldest calls, this value (unlike `created_at`) is unaffected until the entire session has aged out. On the list endpoint this value is a lower bound: for a session still active at a page or `created_at.lt` window boundary it can momentarily lag the session's true last activity. Retrieving the session, or its messages, always reflects the exact latest retained call.

  format: date-time

- `user: object`

  The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

  - `id: string`

    User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

  - `email_address: string or null`

    User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

- `workspace_id: string or null`

  Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/sessions/local/$LOCAL_SESSION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "type": "compliance_local_session",
  "id": "clls_eyJ2IjoxLCJvIjoiOWEx…",
  "organization_uuid": "9a1e0000-0000-0000-0000-000000000000",
  "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR",
  "user": {
    "id": "user_01GpKpLmNoPqRsTuVwXyZaBc",
    "email_address": "engineer@example.com"
  },
  "product_surface": "cowork",
  "created_at": "2026-07-09T14:02:11Z",
  "updated_at": "2026-07-09T15:47:33Z"
}
```

## Compliance API › Apps › Sessions › Local › Messages

### Retrieve local session messages

**GET** `/v1/compliance/apps/sessions/local/{local_session_id}/messages`

Read one local session's transcript, oldest-first by default.

Retention is enforced read-side: turns at or before the child
organization's retention boundary are never returned; a session
that straddles the boundary carries one leading
`content_unavailable` placeholder (`reason: "retention_elapsed"`)
in their place. The boundary is pinned on the walk's first page and
honored for 24 hours: a cursor older than that is rejected with an
explicit 400; restart the walk to read under the current boundary.

On a very large session, some pages are too large to read and return a
400; retrying does not help. If the request used `order=desc`, read the
session oldest first from its first page instead (omit `order` and
`page`, then follow `next_page`). Rarely, an oldest-first page returns
this 400 too; contact Anthropic support and quote the `request-id`
response header.

#### Path parameters

- `local_session_id: string`

#### Query parameters

- `limit: optional number`

  Maximum results (default: 100, max: 1000)

  default: 100, minimum: 1, maximum: 1000

- `order: optional "asc" or "desc"`

  Sort direction. `asc` (oldest-first, default) or `desc`. On very large sessions some pages are too large to read and return a 400, far more often with `desc`; read those sessions with `asc`, starting again from the first page.

  default: asc

  - `"asc"`

  - `"desc"`

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `tool_result_max_bytes: optional number`

  Truncate each text item inside a tool result to at most this many bytes (cut on a code-point boundary). Pass `-1` to request the server maximum (approximately 1 MiB); larger values are clamped to it. `0` is not a valid value.

  default: 10000, minimum: -1, maximum: 2147483647

- `tool_use_input_max_bytes: optional number`

  Truncate each tool-use input to at most this many bytes (cut on a code-point boundary so the result is valid UTF-8). Pass `-1` to request the server maximum (approximately 1 MiB); larger values are clamped to it. `0` is not a valid value.

  default: 10000, minimum: -1, maximum: 2147483647

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  Transcript turns for this page, in call order: oldest call first by default, newest call first with `order=desc`. The messages of one call carry the call's timestamp and follow each other in transcript order; a page boundary can fall between them.

  - `type: "compliance_local_session_message"`

    default: compliance_local_session_message

  - `id: string`

    Message identifier, prefixed `clsm_`. Stable for as long as the message's turn is retained: identifiers of retained turns do not change as older turns age out of the organization's retention period. The `retention_elapsed` placeholder's identifier is distinct from every retained turn's and changes only when further turns age out.

  - `content: array of Text or ToolUse or ToolResult`

    Content blocks within the message, discriminated on `type` (`text` / `tool_use` / `tool_result`: the same discriminator values as the claude.ai chat-messages endpoint; the tool variants omit `integration_name` and `mcp_server_url`, and `text` carries `truncated`). Extended-thinking content is never included. The request's `system` field is never included; a presence-only marker message is emitted when it was set. The request's `tools[]` definitions are never included as transcript messages. Project-level instructions (such as CLAUDE.md files) appear in the message stream as a user-role context block and are included. Empty when `provenance.type` is `content_unavailable`.

    - `Text object`

      Text content block.

      - `type: "text"`

        default: text

      - `text: string`

        Text content from the user or the assistant

      - `truncated: boolean`

        True when `text` was shortened by the server's fixed per-string bound (approximately 1 MiB), or when ancillary content the block carried (such as citations) was omitted, or when this block stands in for a non-text block whose content is not shown, or when it is an explanatory marker the server inserted (its text enclosed in square brackets, e.g. prefacing client-asserted history). There is no request parameter that raises the per-string bound.

        default: false

    - `ToolUse object`

      Tool invocation requested by the assistant.

      - `type: "tool_use"`

        default: tool_use

      - `id: string or null`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened (see the `truncated` field); a truncated value is cut mid-document and is not valid JSON.

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request the server maximum.

        default: false

    - `ToolResult object`

      Result returned by a tool invocation.

      - `type: "tool_result"`

        default: tool_result

      - `content: array of object`

        Text content returned by the tool. Non-text item types are omitted and signalled via `truncated` with an in-band item-count marker.

        - `type: "text"`

          default: text

        - `text: string`

          Text returned by the tool

      - `is_error: boolean`

        True when the tool reported an error

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string or null`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened or non-text items were omitted. Pass `tool_result_max_bytes=-1` to request the server maximum.

        default: false

  - `created_at: string`

    When the message was recorded (RFC 3339, UTC)

    format: date-time

  - `model: string or null`

    The model that served this assistant turn, as reported in the `model` field of the underlying Messages API response. Null on user messages and on any assistant message whose `provenance` is set: client-asserted history and synthetic markers were not produced by a model during this session, and for unavailable content the serving model is not known.

  - `provenance: ContentUnavailable or ClientAsserted or SyntheticMarker or null`

    Where this turn's content came from, discriminated on `type`. Null (the common case) means verified content: on an assistant message, content Claude produced during this session; on a user message, content the user sent. `content_unavailable`: the turn's content cannot be returned and `content` is empty; `reason` says why. `client_asserted`: assistant content the client supplied as conversation history; `content` shows what the model received but its authorship is not verified; never on user-role messages. `synthetic_marker`: a transcript marker the endpoint generated rather than content either party sent during the session. Both `client_asserted` and `synthetic_marker` can result from normal request or client processing, not only client modification. Callers should tolerate unrecognized `type` values.

    - `ContentUnavailable object`

      The turn's content cannot be returned; `content` is empty.

      - `type: "content_unavailable"`

        default: content_unavailable

      - `reason: string`

        Why this turn's content cannot be returned, e.g. `not_captured` (the content was not captured for compliance retrieval), `client_aborted` (the client closed the connection or cancelled the request before the response completed, so the response was not captured for this turn; any partial output already streamed to the client is not included; assistant-role turns only), `cmek_key_revoked` (the content is encrypted under the organization's customer-managed key and that key is unavailable), `retention_elapsed` (the content lies past the organization's retention boundary; on the placeholder standing in for every pre-boundary turn), or `oversize` (the message exceeds the server's per-message size bound even after per-block truncation). Callers should tolerate unrecognized values. `not_captured` is not proof that no record was stored: content withheld by the storage layer's fail-closed access policies carries the same reason and is deliberately indistinguishable from content that was never captured.

    - `ClientAsserted object`

      Assistant content the client supplied as conversation history
      rather than produced by Claude during this session. `content` shows
      what the model received but its authorship is not verified; this can
      result from normal request or client processing, not only client
      modification. Never on user-role messages.

      - `type: "client_asserted"`

        default: client_asserted

    - `SyntheticMarker object`

      A transcript marker generated by the endpoint rather than sent by
      either party during the session. Marker messages indicate that the
      prompt history diverged from what was captured, that the request's
      `system` field was present but is not shown, or that earlier turns
      that a request re-sent as history were withheld because they cannot
      be dated against the child organization's data-retention period
      (only for organizations with a finite retention period; the request's
      new user input after its last assistant turn is not affected). The
      marker's text names the cause. Markers that report a mismatch with
      captured history can result from normal request or client processing,
      not only client modification.

      - `type: "synthetic_marker"`

        default: synthetic_marker

  - `role: "assistant" or "user"`

    Message sender (`user` or `assistant`)

    - `"assistant"`

    - `"user"`

- `next_page: string or null`

  Opaque pagination cursor (prefixed `page_`) for the next page. Null when there is no further page. Treat as an opaque string; the format may change without notice.

- `session: object`

  The local session the messages belong to. `user.email_address` is always null on this endpoint; the messages endpoint does not resolve email addresses.

  - `type: "compliance_local_session"`

    default: compliance_local_session

  - `id: string`

    Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

  - `created_at: string`

    Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

    format: date-time

  - `organization_uuid: string`

    UUID of the child organization the session belongs to

  - `product_surface: string or null`

    The product the session ran in: `cowork` (Cowork in Claude Desktop on the user's machine), `claude_code` (Claude Code), `claude_science` (Claude Science), `claude_in_chrome` (the Claude in Chrome browser extension's built-in chat), or one of `office_agents/excel`, `office_agents/powerpoint`, `office_agents/word`, and `office_agents/outlook` (Claude for Microsoft 365, by app; `office_agents` alone when the app is not identified). New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

  - `truncated: boolean`

    True when the session has more inference calls than the service can return for one session (100,000). The messages endpoint then returns only the session's earliest calls, up to that many, and ends before the session does; `updated_at` is a lower bound on the latest call and can differ between the list and retrieve endpoints. False for every session within that bound.

    default: false

  - `updated_at: string`

    Timestamp of the session's last retained inference call (RFC 3339, UTC). Always at or after `created_at`. When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected — but because retention removes only the oldest calls, this value (unlike `created_at`) is unaffected until the entire session has aged out. On the list endpoint this value is a lower bound: for a session still active at a page or `created_at.lt` window boundary it can momentarily lag the session's true last activity. Retrieving the session, or its messages, always reflects the exact latest retained call.

    format: date-time

  - `user: object`

    The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

    - `id: string`

      User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

    - `email_address: string or null`

      User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

  - `workspace_id: string or null`

    Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/sessions/local/$LOCAL_SESSION_ID/messages \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "clsm_eyJ2IjoxLCJsIjoi…",
      "content": [
        {
          "text": "text",
          "truncated": true,
          "type": "text"
        }
      ],
      "created_at": "2025-03-12T18:22:41.123456Z",
      "model": "claude-opus-5",
      "provenance": {
        "reason": "not_captured",
        "type": "content_unavailable"
      },
      "role": "assistant",
      "type": "compliance_local_session_message"
    }
  ],
  "next_page": "page_eyJ2IjoxLCJmIjoibSIs…",
  "session": {
    "id": "clls_eyJ2IjoxLCJvIjoiOWEx…",
    "created_at": "2025-03-12T18:22:41.123456Z",
    "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
    "product_surface": "cowork",
    "truncated": true,
    "type": "compliance_local_session",
    "updated_at": "2025-03-12T18:22:41.123456Z",
    "user": {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "email_address": "jane.doe@example.com"
    },
    "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR"
  }
}
```

## Compliance API › Apps › Sessions › Remote

### List remote sessions

**GET** `/v1/compliance/apps/sessions/remote`

List remote sessions (Cowork sessions that run in Anthropic-managed
cloud environments) across the organizations the key may read.

Each entry carries session metadata only; retrieve a session's
transcript from the messages endpoint. By default the list spans every
such organization; pass up to 500 `organization_ids[]` values to
narrow it. Pass 1 to 10 `user_ids[]` values to scope the
list to specific users: that filter matches the session's owning user,
so agent-owned sessions are excluded whenever it is set. Bound results
in time with the `created_at` range parameters (`created_at.gte`,
`created_at.gt`, `created_at.lt`, `created_at.lte`; RFC 3339). There
is no `updated_at` filter.

Results are sorted newest first by `created_at`, with at most `limit`
sessions per page (default 100, maximum 500). Pagination is
forward-only: pass the response's `next_page` value back as `page` to
retrieve the next page, and stop when `next_page` is null.

#### Query parameters

- `created_at: optional object`

  - `gt: optional string`

    Filter remote sessions created after this time (RFC 3339 format)

    format: date-time

  - `gte: optional string`

    Filter remote sessions created at or after this time (RFC 3339 format)

    format: date-time

  - `lt: optional string`

    Filter remote sessions created before this time (RFC 3339 format)

    format: date-time

  - `lte: optional string`

    Filter remote sessions created at or before this time (RFC 3339 format)

    format: date-time

- `limit: optional number`

  Maximum results (default: 100, max: 500)

  default: 100, minimum: 1, maximum: 500

- `organization_ids: optional array of string`

  Filter to specific child organization identifiers. Omit to enumerate every child organization the key may read.

  maxItems: 500

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `user_ids: optional array of string`

  Filter to sessions owned by specific users (max 10 per request). Agent-owned sessions are excluded when this filter is set.

  maxItems: 10

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  - `id: string`

    Remote session identifier

  - `agent_id: string or null`

    Identifier of the automated agent that owns the session. Null for user-owned sessions. At most one of `user` and `agent_id` is set.

  - `claude_project_id: string or null`

    ID of the project the session is bound to. Null when the session has no project binding.

  - `created_at: string`

    When the session was created (RFC 3339, UTC)

    format: date-time

  - `organization_uuid: string`

    UUID of the organization the session belongs to

  - `product_surface: string or null`

    The Claude product the session was created from. Currently `cowork_remote`, for Cowork sessions started on claude.ai web or mobile. More values will appear as other surfaces launch, so treat any unrecognized value as an unclassified surface rather than an error. Null for sessions created before this field was recorded, for surfaces that do not stamp it, and for unrecognized tag values.

  - `started_by_user: object or null`

    The user who initiated an agent-owned session (for example, by mentioning Claude in Slack or via a scheduled trigger). Null for user-owned sessions — where the session's `user` started it — and for agent sessions with no human initiator. For initiators no longer a member of an organization the key may read, the object is populated with `email_address` null.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

  - `status: string`

    Session lifecycle state. One of `active`, `paused`, `archived`, or `failed` — the lifecycle states the owning product surface exposes — plus `pending`, a brief transient state that resolves before any transcript content exists. The list endpoint includes `pending`; the messages endpoint returns 404 for it. Deleted sessions are not returned on either endpoint. Treat unrecognized values as an unknown state rather than an error.

  - `updated_at: string`

    When the session was last modified (RFC 3339, UTC)

    format: date-time

  - `user: object or null`

    The user who owns the session. Null for sessions owned by an automated agent rather than a user. At most one of `user` and `agent_id` is set. For users no longer a member of an organization the key may read, the object is populated with `email_address` null.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

- `next_page: string or null`

  Opaque page token; pass as `page` to retrieve the next page. Null when no rows exist after this page. Treat this value as opaque; do not parse or store it long-term, as the format may change without notice.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/sessions/remote \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "cse_01A0000000000000000000000",
      "organization_uuid": "00000000-0000-0000-0000-000000000000",
      "user": {
        "id": "user_01A0000000000000000000000",
        "email_address": "user@example.com"
      },
      "status": "active",
      "created_at": "2026-01-02T03:04:05.000000Z",
      "updated_at": "2026-01-02T03:04:05.000000Z",
      "product_surface": "cowork_remote",
      "claude_project_id": "claude_proj_01Nm7PqRsTuVwXyZaBcDeFgH"
    }
  ],
  "next_page": "page_AAE..."
}
```

## Compliance API › Apps › Sessions › Remote › Messages

### Retrieve remote session messages

**GET** `/v1/compliance/apps/sessions/remote/{claude_remote_session_id}/messages`

Retrieve one remote session's transcript: user prompts, assistant
responses, and tool calls and results. Thinking blocks and images are
not included.

Messages are returned oldest first by default; pass `order=desc` to
reverse. Pagination uses the same `page`/`next_page` scheme as the
list endpoint, with at most `limit` messages per page (default 100,
maximum 1000); keep paginating until `next_page` is null.
`tool_use_input_max_bytes` and `tool_result_max_bytes` cap how many
bytes of each tool-use input and each tool-result text item are
returned; a block shortened by either cap carries `truncated: true`.

The response embeds the session's metadata under `session` alongside
the paginated `data` array. On this endpoint `session.user.email_address`
and `session.started_by_user` are always null; read them from the list
endpoint instead.

Returns 404 while the session is still `pending`, for deleted sessions,
and for sessions outside the organizations the key may read. A
malformed session identifier returns 400.

#### Path parameters

- `claude_remote_session_id: string`

  The remote session identifier (`cse_...`) to retrieve

#### Query parameters

- `limit: optional number`

  Maximum results (default: 100, max: 1000)

  default: 100, minimum: 1, maximum: 1000

- `order: optional "asc" or "desc"`

  Sort direction. `asc` (oldest-first) or `desc`.

  default: asc

  - `"asc"`

  - `"desc"`

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `tool_result_max_bytes: optional number`

  Truncate each text item inside a tool result to at most this many bytes (cut on a code-point boundary). Pass `-1` to request the server maximum. `0` is not a valid value.

  default: 10000, minimum: -1, maximum: 2147483647

- `tool_use_input_max_bytes: optional number`

  Truncate each tool-use input to at most this many bytes (cut on a code-point boundary so the result is valid UTF-8). Pass `-1` to request the server maximum. `0` is not a valid value.

  default: 10000, minimum: -1, maximum: 2147483647

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  Transcript turns for this page, ordered by transcript position. `created_at` is a commit timestamp and may tie or invert under concurrent writes; do not re-sort by it.

  - `id: string`

    Unique identifier for the message, e.g. `csev_abc123`

  - `content: array of Text or ToolUse or ToolResult`

    Content blocks within the message

    - `Text object`

      Text content block.

      - `type: "text"`

        default: text

      - `text: string`

        Text content from the user or the assistant

      - `truncated: boolean`

        True when `text` exceeded the server-defined maximum (approximately 1 MiB) and was shortened.

        default: false

    - `ToolUse object`

      Tool invocation requested by the assistant.

      - `type: "tool_use"`

        default: tool_use

      - `id: string or null`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request full content, subject to the server-side maximum.

        default: false

    - `ToolResult object`

      Result returned by a tool invocation.

      - `type: "tool_result"`

        default: tool_result

      - `content: array of object`

        Text content returned by the tool. Non-text item types are omitted.

        - `type: "text"`

          default: text

        - `text: string`

          Text returned by the tool

      - `is_error: boolean`

        True when the tool reported an error

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string or null`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened. Pass `tool_result_max_bytes=-1` to request full content, subject to the server-side maximum.

        default: false

  - `content_unavailable: boolean`

    True when the stored content could not be returned — it could not be decrypted, or it exceeded the server's per-event size bound. `content` is empty in that case; this distinguishes 'no content' from 'content withheld'.

    default: false

  - `created_at: string`

    When the message was recorded (RFC 3339, UTC)

    format: date-time

  - `role: "assistant" or "user"`

    Message sender (`user` or `assistant`)

    - `"assistant"`

    - `"user"`

  - `sent_by_user_id: string or null`

    Identifier of the human account that sent this turn on an agent-owned session. Null on user-owned sessions, where every user-role turn was sent by the session's `user`.

- `next_page: string or null`

  Opaque page token; pass as `page` to retrieve the next page. Null when no rows exist after this page. Treat this value as opaque; do not parse or store it long-term, as the format may change without notice.

- `session: object`

  Session metadata. `started_by_user`, `user.email_address`, and `claude_project_id` are always null on this endpoint; the messages endpoint resolves neither email addresses nor project bindings.

  - `id: string`

    Remote session identifier

  - `agent_id: string or null`

    Identifier of the automated agent that owns the session. Null for user-owned sessions. At most one of `user` and `agent_id` is set.

  - `claude_project_id: string or null`

    ID of the project the session is bound to. Null when the session has no project binding.

  - `created_at: string`

    When the session was created (RFC 3339, UTC)

    format: date-time

  - `organization_uuid: string`

    UUID of the organization the session belongs to

  - `product_surface: string or null`

    The Claude product the session was created from. Currently `cowork_remote`, for Cowork sessions started on claude.ai web or mobile. More values will appear as other surfaces launch, so treat any unrecognized value as an unclassified surface rather than an error. Null for sessions created before this field was recorded, for surfaces that do not stamp it, and for unrecognized tag values.

  - `started_by_user: object or null`

    The user who initiated an agent-owned session (for example, by mentioning Claude in Slack or via a scheduled trigger). Null for user-owned sessions — where the session's `user` started it — and for agent sessions with no human initiator. For initiators no longer a member of an organization the key may read, the object is populated with `email_address` null.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

  - `status: string`

    Session lifecycle state. One of `active`, `paused`, `archived`, or `failed` — the lifecycle states the owning product surface exposes — plus `pending`, a brief transient state that resolves before any transcript content exists. The list endpoint includes `pending`; the messages endpoint returns 404 for it. Deleted sessions are not returned on either endpoint. Treat unrecognized values as an unknown state rather than an error.

  - `updated_at: string`

    When the session was last modified (RFC 3339, UTC)

    format: date-time

  - `user: object or null`

    The user who owns the session. Null for sessions owned by an automated agent rather than a user. At most one of `user` and `agent_id` is set. For users no longer a member of an organization the key may read, the object is populated with `email_address` null.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/sessions/remote/$CLAUDE_REMOTE_SESSION_ID/messages \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "content": [
        {
          "text": "text",
          "truncated": true,
          "type": "text"
        }
      ],
      "content_unavailable": true,
      "created_at": "2019-12-27T18:11:19.117Z",
      "role": "assistant",
      "sent_by_user_id": "sent_by_user_id"
    }
  ],
  "next_page": "next_page",
  "session": {
    "id": "id",
    "agent_id": "agent_id",
    "claude_project_id": "claude_project_id",
    "created_at": "2019-12-27T18:11:19.117Z",
    "organization_uuid": "organization_uuid",
    "product_surface": "product_surface",
    "started_by_user": {
      "id": "id",
      "email_address": "email_address"
    },
    "status": "status",
    "updated_at": "2019-12-27T18:11:19.117Z",
    "user": {
      "id": "id",
      "email_address": "email_address"
    }
  }
}
```

## Compliance API › Code › Artifacts

### List Code Artifacts

**GET** `/v1/compliance/apps/code/artifacts`

List Claude Code Artifacts owned by organizations under the parent
organization.

Results are sorted by Artifact identifier. Pages may be short or empty
while `next_page` is still set — continue until `next_page` is absent.
Artifacts are sorted by identifier (not creation time): an Artifact
published during an export may land before the cursor and be omitted, so
for a point-in-time-complete export re-enumerate after publishing
quiesces.

Artifacts owned by a since-deleted child organization are not
returned.

#### Query parameters

- `limit: optional number`

  Maximum results (default: 20, max: 100)

  default: 20, minimum: 1, maximum: 100

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID, up to 500). Enumerate IDs via `GET /v1/compliance/organizations`.

  maxItems: 500

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `updated_at: optional object`

  - `gt: optional string`

    Return only Artifacts updated after this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.

    format: date-time

  - `gte: optional string`

    Return only Artifacts updated at or after this time (RFC 3339 format). Time filters match an eventually-consistent index and Artifacts published before this field was recorded never match — omit the time filter for compliance-complete enumeration. For incremental export, apply a generous overlap margin between windows and dedupe by `id`: adjacent tiling silently misses items whose index update lagged their publish.

    format: date-time

  - `lt: optional string`

    Return only Artifacts updated before this time (RFC 3339 format). Multiple time operators are AND-ed to the tightest bound. See `updated_at.gte` for the completeness caveat.

    format: date-time

  - `lte: optional string`

    Return only Artifacts updated at or before this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.

    format: date-time

- `user_ids: optional array of string`

  Filter by owner user IDs (up to 200). Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

  maxItems: 200

#### Headers

- `"x-api-key": optional string`

#### Returns

- `data: array of object`

  Page of Artifacts

  - `id: string`

    Artifact identifier (tagged ID)

  - `artifact_type: "claude_design" or "claude_design_systems" or "claude_docs" or 3 more`

    Which kind of Artifact this is: `code` for a site published from Claude Code, or the built-in Artifact type it was made from — `claude_docs` (Claude Docs), `claude_slides` (Slides), `claude_design` (Design) or `claude_design_systems` (a design system). `other` is an Artifact made from a built-in type this list does not name yet.

    - `"claude_design"`

    - `"claude_design_systems"`

    - `"claude_docs"`

    - `"claude_slides"`

    - `"code"`

    - `"other"`

  - `organization_uuid: string`

    Organization UUID this Artifact belongs to

  - `owner_user_id: string or null`

    Artifact owner's user identifier (tagged ID), or null for Artifacts published by an agent session rather than a user account. When set, it survives after the owner's account is deleted or the owner leaves every organization under the parent.

  - `published_version_id: string or null`

    Identifier of the version a non-owner viewer would render when `read_mode` permits them — the version the owner has pinned for non-owner readers if one is pinned, otherwise the owner's latest. When `read_mode` is `owner` no non-owner renders any version; the field still reports which version would be served were read_mode widened.

  - `read_mode: "org" or "owner" or "public" or "users"`

    Who can view this Artifact: only its owner, a named set of users, every member of its organization, or anyone on the internet (`public`)

    - `"org"`

    - `"owner"`

    - `"public"`

    - `"users"`

  - `updated_at: string or null`

    Artifact last update timestamp, or null for Artifacts published before this field was recorded

    format: date-time

  - `user: object or null`

    Artifact owner with email, or null if the Artifact was published by an agent session, the owner's account has been deleted, or the owner is no longer a member of an organization the key may read

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

  - `versions: array of object`

    Up to roughly 20 most-recently-published versions of this Artifact (older versions are not retained). Metadata only — use `GET /v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}` to download a version's content.

    - `id: string`

      Opaque version identifier

    - `created_at: string or null`

      When this version was published

      format: date-time

    - `name: string`

      Artifact title at this version. Falls back to the version identifier when the title for an older version is no longer retained.

- `has_more: boolean`

  Whether `next_page` is set. May be true for a page whose next page is empty — continue until `next_page` is absent.

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "cart_01Tu9VwXyZaBcDeFgHiJkLmN",
      "artifact_type": "claude_docs",
      "organization_uuid": "a1b2c3d4-e5f6-4789-a012-3456789abcde",
      "owner_user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "published_version_id": "1741803761-9f3a",
      "read_mode": "org",
      "updated_at": "2025-03-14T09:05:17.456789Z",
      "user": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "email_address": "jane.doe@example.com"
      },
      "versions": [
        {
          "id": "1741803761-9f3a",
          "created_at": "2025-03-12T18:22:41.123456Z",
          "name": "Team dashboard"
        }
      ]
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

### Download Code Artifact Version Content

**GET** `/v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}`

Streams the content of one version of a Claude Code Artifact as the
response body.

Returns 404 for Artifacts that don't exist or belong to another parent
organization. A listed version id can start returning 404 if subsequent
publishes rotated it out of retained history — re-list on 404. Returns
503 while the version's content upload is still in flight or was
abandoned — retry with backoff. Returns 422 for a version that has more
than one file, because the Compliance API returns only single-file
versions. Do not retry a 422. The 422's `error.details.error_code` is
`multi_file_unavailable`. Oversized
encoded content aborts mid-stream: headers and initial bytes arrive
but the body terminates early — an aborted chunked transfer is the
only truncation signal for encoded content. `Content-MD5` is emitted
only for identity-stored content; validate against it when present.

#### Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

- `version_id: string`

  Opaque version identifier from the Artifact's `versions` list

#### Headers

- `"x-api-key": optional string`

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/versions/$VERSION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

### Delete Code Artifact

**DELETE** `/v1/compliance/apps/code/artifacts/{artifact_id}`

Permanently deletes a Code Artifact and all its versions. This is a
destructive operation that cannot be undone. A 200 response means the
deletion is initiated and the Artifact is claimed; content removal
completes asynchronously.

Returns 404 for Artifacts that don't exist or belong to another parent
organization. Returns 404 on a repeated delete of an already-deleted
Artifact.

#### Path parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

#### Headers

- `"x-api-key": optional string`

#### Returns

- `type: "code_artifact_deleted"`

  Constant string confirming deletion

  default: code_artifact_deleted

- `id: string`

  The ID of the Artifact that was deleted

#### Example

```bash
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

##### Response (200)

```json
{
  "id": "cart_xyz789",
  "type": "code_artifact_deleted"
}
```
