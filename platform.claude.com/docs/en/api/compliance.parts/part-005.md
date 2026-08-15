<!-- source: https://platform.claude.com/docs/en/api/compliance -->
<!-- part of: https://platform.claude.com/docs/en/api/compliance -->

<!-- chunk-start -->

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `previous_value: optional boolean or null`

      Override state immediately before this change

    - `type: optional "platform_workspace_inference_data_retention_enabled"`

      - `"platform_workspace_inference_data_retention_enabled"`

  - `PlatformWorkspaceMemberAdded object { actor, user_id, workspace_id, 5 more }`

    A member was added to a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, service_account_id, user_agent, type }  or object { provider, ip_address, subject, 2 more }`

      An external identity asserted by a trusted provider — a cloud-provider
      gateway or a customer-registered federation issuer — acting without an
      Anthropic-provisioned account or service account.

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

    - `user_id: string`

      Tagged ID of the added member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_workspace_member_added"`

      - `"platform_workspace_member_added"`

  - `PlatformWorkspaceMemberRemoved object { actor, user_id, workspace_id, 5 more }`

    A member was removed from a workspace.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, service_account_id, user_agent, type }  or object { provider, ip_address, subject, 2 more }`

      An external identity asserted by a trusted provider — a cloud-provider
      gateway or a customer-registered federation issuer — acting without an
      Anthropic-provisioned account or service account.

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

    - `user_id: string`

      Tagged ID of the removed member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_workspace_member_removed"`

      - `"platform_workspace_member_removed"`

  - `PlatformWorkspaceMemberUpdated object { actor, updates, user_id, 6 more }`

    A workspace member was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, service_account_id, user_agent, type }  or object { provider, ip_address, subject, 2 more }`

      An external identity asserted by a trusted provider — a cloud-provider
      gateway or a customer-registered federation issuer — acting without an
      Anthropic-provisioned account or service account.

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "workspace_role"`

        - `"workspace_role"`

    - `user_id: string`

      Tagged ID of the updated member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_workspace_member_updated"`

      - `"platform_workspace_member_updated"`

  - `PlatformWorkspaceMemberViewed object { actor, user_id, workspace_id, 5 more }`

    A workspace member was viewed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, service_account_id, user_agent, type }  or object { provider, ip_address, subject, 2 more }`

      An external identity asserted by a trusted provider — a cloud-provider
      gateway or a customer-registered federation issuer — acting without an
      Anthropic-provisioned account or service account.

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

    - `user_id: string`

      Tagged ID of the viewed member

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_workspace_member_viewed"`

      - `"platform_workspace_member_viewed"`

  - `PlatformWorkspaceMembersListed object { actor, workspace_id, id, 4 more }`

    Workspace members were listed.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, service_account_id, user_agent, type }  or object { provider, ip_address, subject, 2 more }`

      An external identity asserted by a trusted provider — a cloud-provider
      gateway or a customer-registered federation issuer — acting without an
      Anthropic-provisioned account or service account.

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

    - `workspace_id: string`

      Tagged ID of the workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_workspace_members_listed"`

      - `"platform_workspace_members_listed"`

  - `PlatformWorkspaceRateLimitDeleted object { actor, limiter_type, model_group, 6 more }`

    A workspace rate limit was deleted.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, service_account_id, user_agent, type }  or object { provider, ip_address, subject, 2 more }`

      An external identity asserted by a trusted provider — a cloud-provider
      gateway or a customer-registered federation issuer — acting without an
      Anthropic-provisioned account or service account.

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

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

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_workspace_rate_limit_deleted"`

      - `"platform_workspace_rate_limit_deleted"`

  - `PlatformWorkspaceRateLimitUpdated object { actor, limiter_type, model_group, 7 more }`

    A workspace rate limit was created or updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, service_account_id, user_agent, type }  or object { provider, ip_address, subject, 2 more }`

      An external identity asserted by a trusted provider — a cloud-provider
      gateway or a customer-registered federation issuer — acting without an
      Anthropic-provisioned account or service account.

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

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

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_workspace_rate_limit_updated"`

      - `"platform_workspace_rate_limit_updated"`

  - `PlatformWorkspaceUpdated object { actor, updates, workspace_id, 5 more }`

    A workspace was updated.

    - `actor: object { admin_api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, service_account_id, user_agent, type }  or object { provider, ip_address, subject, 2 more }`

      An external identity asserted by a trusted provider — a cloud-provider
      gateway or a customer-registered federation issuer — acting without an
      Anthropic-provisioned account or service account.

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "allowed_inference_geos" or "default_inference_geo" or "display_color" or 3 more`

        The workspace property that was changed

        - `"allowed_inference_geos"`

        - `"default_inference_geo"`

        - `"display_color"`

        - `"external_key_config_id"`

        - `"inference_data_retention"`

        - `"name"`

    - `workspace_id: string`

      Tagged ID of the updated workspace

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "platform_workspace_updated"`

      - `"platform_workspace_updated"`

  - `ClaudePluginCreated object { actor, id, created_at, 5 more }`

    Plugin was created.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `plugin_id: optional string or null`

    - `plugin_name: optional string or null`

    - `type: optional "claude_plugin_created"`

      - `"claude_plugin_created"`

  - `ClaudePluginDeleted object { actor, id, created_at, 5 more }`

    Plugin was deleted.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `plugin_id: optional string or null`

    - `plugin_name: optional string or null`

    - `type: optional "claude_plugin_deleted"`

      - `"claude_plugin_deleted"`

  - `ClaudePluginDisabled object { actor, id, created_at, 6 more }`

    User disabled a plugin for their account.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

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

      - `"claude_plugin_disabled"`

  - `ClaudePluginEnabled object { actor, id, created_at, 6 more }`

    User enabled a plugin for their account.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

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

      - `"claude_plugin_enabled"`

  - `PluginInstallationPreferenceUpdated object { actor, marketplace_id, plugin_name, 9 more }`

    An org admin changed the installation preference for a plugin.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

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

      - `"plugin_installation_preference_updated"`

  - `ClaudePluginReplaced object { actor, id, created_at, 5 more }`

    Plugin was replaced.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `plugin_id: optional string or null`

    - `plugin_name: optional string or null`

    - `type: optional "claude_plugin_replaced"`

      - `"claude_plugin_replaced"`

  - `ClaudePluginUpdated object { actor, id, created_at, 5 more }`

    Plugin was updated.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `plugin_id: optional string or null`

    - `plugin_name: optional string or null`

    - `type: optional "claude_plugin_updated"`

      - `"claude_plugin_updated"`

  - `PrepaidAutoRechargeDisabled object { actor, id, created_at, 3 more }`

    Auto-recharge was disabled for API prepaid org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "prepaid_auto_recharge_disabled"`

      - `"prepaid_auto_recharge_disabled"`

  - `PrepaidAutoRechargeUpdated object { actor, id, created_at, 5 more }`

    Auto-recharge settings were updated for API prepaid org.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `target_amount: optional number or null`

      Target recharge amount in minor units.

    - `threshold_amount: optional number or null`

      Threshold amount to trigger recharge in minor units.

    - `type: optional "prepaid_auto_recharge_updated"`

      - `"prepaid_auto_recharge_updated"`

  - `PrepaidExtraUsageAutoReloadDisabled object { actor, id, created_at, 3 more }`

    Prepaid usage credit auto-reload was disabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "prepaid_extra_usage_auto_reload_disabled"`

      - `"prepaid_extra_usage_auto_reload_disabled"`

  - `PrepaidExtraUsageAutoReloadEnabled object { actor, id, created_at, 3 more }`

    Prepaid usage credit auto-reload was enabled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "prepaid_extra_usage_auto_reload_enabled"`

      - `"prepaid_extra_usage_auto_reload_enabled"`

  - `PrepaidExtraUsageAutoReloadSettingsUpdated object { actor, id, created_at, 3 more }`

    Prepaid usage credit auto-reload settings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "prepaid_extra_usage_auto_reload_settings_updated"`

      - `"prepaid_extra_usage_auto_reload_settings_updated"`

  - `PrimaryOwnerTransferred object { actor, new_owner_id, previous_owner_id, 5 more }`

    Primary owner role was transferred to another org member.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `new_owner_id: string`

    - `previous_owner_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "primary_owner_transferred"`

      - `"primary_owner_transferred"`

  - `ClaudeProjectArchived object { actor, claude_project_id, id, 4 more }`

    A Claude project was archived.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_archived"`

      - `"claude_project_archived"`

  - `ClaudeProjectCreated object { actor, claude_project_id, id, 4 more }`

    A Claude project was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_created"`

      - `"claude_project_created"`

  - `ClaudeProjectDeleted object { actor, claude_project_id, id, 4 more }`

    A Claude project was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_deleted"`

      - `"claude_project_deleted"`

  - `ClaudeProjectDocumentAccessFailed object { actor, claude_project_document_id, claude_project_id, 6 more }`

    An attempt to access a document in a Claude project failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

    - `claude_project_document_id: string or null`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_document_access_failed"`

      - `"claude_project_document_access_failed"`

  - `ClaudeProjectDocumentBulkDeletionAuditTruncated object { actor, audited_count, claude_project_id, 6 more }`

    A bulk request to delete documents from a Claude project failed with more documents requested than were individually recorded in the audit log.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

    - `audited_count: number`

      Number of documents that received an individual audit record.

    - `claude_project_id: string`

    - `requested_count: number`

      Total number of documents the request asked to delete.

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_document_bulk_deletion_audit_truncated"`

      - `"claude_project_document_bulk_deletion_audit_truncated"`

  - `ClaudeProjectDocumentDeleted object { actor, claude_project_document_id, claude_project_id, 6 more }`

    A document was deleted from a Claude project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_document_deleted"`

      - `"claude_project_document_deleted"`

  - `ClaudeProjectDocumentDeletionFailed object { actor, claude_project_document_id, claude_project_id, 6 more }`

    A request to delete a document from a Claude project failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

    - `claude_project_document_id: string or null`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_document_deletion_failed"`

      - `"claude_project_document_deletion_failed"`

  - `ClaudeProjectDocumentUpdated object { actor, claude_project_document_id, claude_project_id, 6 more }`

    The content of a document in a Claude project was replaced in place.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_document_updated"`

      - `"claude_project_document_updated"`

  - `ClaudeProjectDocumentUploaded object { actor, claude_project_document_id, claude_project_id, 6 more }`

    A document was uploaded to a Claude project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_document_uploaded"`

      - `"claude_project_document_uploaded"`

  - `ClaudeProjectDocumentViewed object { actor, claude_project_document_id, claude_project_id, 6 more }`

    A document in a Claude project was viewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_document_id: string`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_document_viewed"`

      - `"claude_project_document_viewed"`

  - `ClaudeProjectFileAccessFailed object { actor, claude_file_id, claude_project_id, 5 more }`

    An attempt to access a file in a Claude project failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_file_access_failed"`

      - `"claude_project_file_access_failed"`

  - `ClaudeProjectFileBulkDeletionAuditTruncated object { actor, audited_count, claude_project_id, 6 more }`

    A bulk request to delete files from a Claude project failed with more files requested than were individually recorded in the audit log.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

    - `audited_count: number`

      Number of files that received an individual audit record.

    - `claude_project_id: string`

    - `requested_count: number`

      Total number of files the request asked to delete.

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_file_bulk_deletion_audit_truncated"`

      - `"claude_project_file_bulk_deletion_audit_truncated"`

  - `ClaudeProjectFileDeleted object { actor, claude_file_id, claude_project_id, 5 more }`

    A file was deleted from a Claude project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_file_deleted"`

      - `"claude_project_file_deleted"`

  - `ClaudeProjectFileDeletionFailed object { actor, claude_file_id, claude_project_id, 5 more }`

    A request to delete a file from a Claude project failed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

    - `claude_file_id: string or null`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_file_deletion_failed"`

      - `"claude_project_file_deletion_failed"`

  - `ClaudeProjectFileUploaded object { actor, claude_file_id, claude_project_id, 6 more }`

    A file was uploaded to a Claude project.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

    - `claude_file_id: string`

    - `claude_project_id: string`

    - `filename: string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_file_uploaded"`

      - `"claude_project_file_uploaded"`

  - `ClaudeProjectReported object { actor, claude_project_id, id, 4 more }`

    A Claude project was reported.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_reported"`

      - `"claude_project_reported"`

  - `ClaudeProjectSharingUpdated object { actor, audience, claude_project_id, 5 more }`

    A Claude project's sharing settings were updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `audience: array of object { type }  or object { type }`

      Sharing audience for the project. If empty, this it's only visible to the creating user.

      - `ProjectSharingAudiencePublic object { type }`

        - `type: optional "public"`

          - `"public"`

      - `ProjectSharingAudienceOrganization object { type }`

        - `type: optional "organization"`

          - `"organization"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_project_sharing_updated"`

      - `"claude_project_sharing_updated"`

  - `ClaudeProjectViewed object { actor, claude_project_id, id, 5 more }`

    A Claude project was viewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `claude_project_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `preview_only: optional boolean`

    - `type: optional "claude_project_viewed"`

      - `"claude_project_viewed"`

  - `ClaudePubsecIdentityConfigured object { actor, idp_saml_config_updated, magic_link_toggled, 6 more }`

    SAML IdP configuration updated for a public sector organization.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `idp_saml_config_updated: boolean`

    - `magic_link_toggled: boolean`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `magic_link_enabled: optional boolean or null`

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_pubsec_identity_configured"`

      - `"claude_pubsec_identity_configured"`

  - `RbacRoleAssigned object { actor, principal_id, principal_type, 6 more }`

    Admin assigned an RBAC custom role to a principal.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `principal_id: string`

      Tagged ID of the principal

    - `principal_type: string`

      Type of principal: account or group

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "rbac_role_assigned"`

      - `"rbac_role_assigned"`

  - `RbacRoleCreated object { actor, role_id, role_name, 5 more }`

    Admin created an RBAC custom role.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `role_id: string`

      Tagged ID of the created role

    - `role_name: string`

      Name of the created role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "rbac_role_created"`

      - `"rbac_role_created"`

  - `RbacRoleDeleted object { actor, role_id, id, 4 more }`

    Admin deleted an RBAC custom role.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `role_id: string`

      Tagged ID of the deleted role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "rbac_role_deleted"`

      - `"rbac_role_deleted"`

  - `RbacRolePermissionAdded object { action, actor, resource_id, 7 more }`

    Admin added a permission to an RBAC custom role.

    Emitted once per requested permission, including permissions the role
    already had, so a retried request still produces a complete audit record.

    - `action: string`

      Action permitted on the resource

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

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

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "rbac_role_permission_added"`

      - `"rbac_role_permission_added"`

  - `RbacRolePermissionRemoved object { action, actor, resource_id, 7 more }`

    Admin removed a permission from an RBAC custom role.

    Emitted once per requested permission, including permissions the role
    already lacked, so a retried request still produces a complete audit
    record.

    - `action: string`

      Action that was permitted on the resource

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

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

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "rbac_role_permission_removed"`

      - `"rbac_role_permission_removed"`

  - `RbacRoleUnassigned object { actor, principal_id, principal_type, 6 more }`

    Admin unassigned an RBAC custom role from a principal.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `principal_id: string`

      Tagged ID of the principal

    - `principal_type: string`

      Type of principal: account or group

    - `role_id: string`

      Tagged ID of the role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "rbac_role_unassigned"`

      - `"rbac_role_unassigned"`

  - `RbacRoleUpdated object { actor, role_id, id, 4 more }`

    Admin updated an RBAC custom role.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `role_id: string`

      Tagged ID of the updated role

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "rbac_role_updated"`

      - `"rbac_role_updated"`

  - `RoleAssignmentGranted object { actor, id, created_at, 8 more }`

    Role assignment was granted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `resource_id: optional string or null`

    - `resource_type: optional string or null`

    - `role: optional string or null`

    - `target_id: optional string or null`

    - `target_type: optional string or null`

    - `type: optional "role_assignment_granted"`

      - `"role_assignment_granted"`

  - `RoleAssignmentRevoked object { actor, id, created_at, 8 more }`

    Role assignment was revoked.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { email_address, type }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `resource_id: optional string or null`

    - `resource_type: optional string or null`

    - `role: optional string or null`

    - `target_id: optional string or null`

    - `target_type: optional string or null`

    - `type: optional "role_assignment_revoked"`

      - `"role_assignment_revoked"`

  - `SSOLoginFailed object { actor, id, created_at, 3 more }`

    An SSO sign-in attempt failed.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "sso_login_failed"`

      - `"sso_login_failed"`

  - `SSOLoginInitiated object { actor, id, created_at, 3 more }`

    A user started an SSO sign-in flow.

    - `actor: object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `ip_address: string`

      - `user_agent: string`

      - `type: optional "unauthenticated_user_actor"`

        - `"unauthenticated_user_actor"`

      - `unauthenticated_email_address: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "sso_login_initiated"`

      - `"sso_login_initiated"`

  - `SSOLoginSucceeded object { actor, id, auth_method, 5 more }`

    A user successfully signed in with SSO.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `auth_method: optional "sso"`

      The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

      - `"sso"`

    - `created_at: optional string`

      When this activity occurred.

    - `mfa_method: optional "not_used" or null`

      The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multistep login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

      - `"not_used"`

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "sso_login_succeeded"`

      - `"sso_login_succeeded"`

  - `SSOSecondFactorMagicLink object { actor, id, created_at, 3 more }`

    SSO second factor magic link was used.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "sso_second_factor_magic_link"`

      - `"sso_second_factor_magic_link"`

  - `ScimUserCreated object { actor, user_id, id, 4 more }`

    A SCIM user was provisioned.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `user_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "scim_user_created"`

      - `"scim_user_created"`

  - `ScimUserDeleted object { actor, user_id, id, 4 more }`

    A SCIM user was deleted.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `user_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "scim_user_deleted"`

      - `"scim_user_deleted"`

  - `ScimUserUpdated object { actor, user_id, id, 4 more }`

    A SCIM user was updated.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `user_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "scim_user_updated"`

      - `"scim_user_updated"`

  - `ScopedAPIKeyDeleted object { actor, api_key_id, api_key_name, 6 more }`

    A scoped API key was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

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

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "scoped_api_key_deleted"`

      - `"scoped_api_key_deleted"`

  - `ScopedAPIKeyUpdated object { actor, api_key_id, updates, 5 more }`

    A scoped API key was renamed or its activation state changed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `api_key_id: string`

      Tagged ID of the updated scoped API key

    - `updates: array of object { current_value, previous_value, type }`

      - `current_value: string`

      - `previous_value: string`

      - `type: "activation_state" or "name"`

        - `"activation_state"`

        - `"name"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "scoped_api_key_updated"`

      - `"scoped_api_key_updated"`

  - `SeatTierChangesCancelled object { actor, id, created_at, 3 more }`

    Scheduled seat tier downgrades were cancelled.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "seat_tier_changes_cancelled"`

      - `"seat_tier_changes_cancelled"`

  - `SeatTiersPurchased object { actor, id, created_at, 4 more }`

    Seat tiers were purchased or upgraded on a subscription.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `item_allocations: optional map[number] or null`

      Desired seat tier allocations (item type to quantity).

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "seat_tiers_purchased"`

      - `"seat_tiers_purchased"`

  - `ServiceCreated object { actor, service_name, id, 4 more }`

    Activity logged when an org service is explicitly created.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `service_name: string`

      The org service name (e.g., 'external:my-service')

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "service_created"`

      - `"service_created"`

  - `ServiceDeleted object { actor, service_name, id, 4 more }`

    Activity logged when an org service is deleted.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `service_name: string`

      The org service name (e.g., 'external:my-service')

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "service_deleted"`

      - `"service_deleted"`

  - `ServiceKeyCreated object { actor, is_service_created, key_name, 8 more }`

    Activity logged when a new org service key is created.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

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

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `scopes: optional array of string`

      The scopes granted to this service key

    - `service_key_id: optional string or null`

      The ID of the created service key

    - `type: optional "service_key_created"`

      - `"service_key_created"`

  - `ServiceKeyRevoked object { actor, service_key_id, service_name, 5 more }`

    Activity logged when an org service key is revoked.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `service_key_id: string`

      The tagged ID of the revoked service key

    - `service_name: string`

      The service name this key belongs to

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "service_key_revoked"`

      - `"service_key_revoked"`

  - `SessionRevoked object { actor, id, created_at, 3 more }`

    User revoked a specific session.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "session_revoked"`

      - `"session_revoked"`

  - `SessionShareAccessed object { actor, id, created_at, 4 more }`

    Session share was accessed.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `share_id: optional string or null`

    - `type: optional "session_share_accessed"`

      - `"session_share_accessed"`

  - `SessionShareCreated object { actor, id, access_level, 5 more }`

    Session share was created.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `access_level: optional string or null`

      Access level granted for the share.

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `share_id: optional string or null`

    - `type: optional "session_share_created"`

      - `"session_share_created"`

  - `SessionShareRevoked object { actor, id, created_at, 5 more }`

    Session share was revoked.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `reason: optional string or null`

      Why the share was revoked.

    - `share_id: optional string or null`

    - `type: optional "session_share_revoked"`

      - `"session_share_revoked"`

  - `ClaudeSkillCreated object { actor, id, created_at, 5 more }`

    Skill was created.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `skill_id: optional string or null`

    - `skill_name: optional string or null`

    - `type: optional "claude_skill_created"`

      - `"claude_skill_created"`

  - `ClaudeSkillDeleted object { actor, id, created_at, 5 more }`

    Skill was deleted.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `skill_id: optional string or null`

    - `skill_name: optional string or null`

    - `type: optional "claude_skill_deleted"`

      - `"claude_skill_deleted"`

  - `ClaudeSkillDisabled object { actor, id, created_at, 5 more }`

    User disabled a skill for their account.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `skill_id: optional string or null`

    - `skill_name: optional string or null`

    - `type: optional "claude_skill_disabled"`

      - `"claude_skill_disabled"`

  - `ClaudeSkillEnabled object { actor, id, created_at, 5 more }`

    User enabled a skill for their account.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `skill_id: optional string or null`

    - `skill_name: optional string or null`

    - `type: optional "claude_skill_enabled"`

      - `"claude_skill_enabled"`

  - `ClaudeSkillReplaced object { actor, id, created_at, 5 more }`

    Skill was replaced.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `skill_id: optional string or null`

    - `skill_name: optional string or null`

    - `type: optional "claude_skill_replaced"`

      - `"claude_skill_replaced"`

  - `SlackWorkspaceClaimRevoked object { actor, slack_team_id, id, 5 more }`

    A Slack workspace or Enterprise Grid organization was disconnected
    from the organization for Claude in Slack.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `slack_team_id: string`

      Claim subject: a Slack team id for scope 'workspace', or an Enterprise Grid org id for scope 'enterprise_grid'. Use the scope field to tell which — never the value's prefix (legacy workspaces exist with E-prefixed team ids)

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `scope: optional string`

      Blast radius of the revocation: 'workspace' for one Slack workspace, 'enterprise_grid' for every workspace in a Slack Enterprise Grid organization

    - `type: optional "slack_workspace_claim_revoked"`

      - `"slack_workspace_claim_revoked"`

  - `SlackWorkspaceClaimed object { actor, slack_team_id, id, 5 more }`

    A Slack workspace or Enterprise Grid organization was connected to
    the organization for Claude in Slack.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `slack_team_id: string`

      Claim subject: a Slack team id for scope 'workspace', or an Enterprise Grid org id for scope 'enterprise_grid'. Use the scope field to tell which — never the value's prefix (legacy workspaces exist with E-prefixed team ids)

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `scope: optional string`

      Blast radius of the claim: 'workspace' for one Slack workspace, 'enterprise_grid' for every workspace in a Slack Enterprise Grid organization

    - `type: optional "slack_workspace_claimed"`

      - `"slack_workspace_claimed"`

  - `SocialLoginSucceeded object { actor, provider, id, 6 more }`

    A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `provider: "apple" or "google" or "microsoft"`

      - `"apple"`

      - `"google"`

      - `"microsoft"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `auth_method: optional "social"`

      The method the user used to authenticate. May be absent on activities recorded before this field was introduced.

      - `"social"`

    - `created_at: optional string`

      When this activity occurred.

    - `mfa_method: optional "not_used" or null`

      The second authentication factor performed during this login, if any. `null` when the second-factor status is not recorded on this event — for example, when authentication was delegated to an external identity provider and any second factor is not visible to Anthropic, or when this event is one step of a multistep login whose MFA is reported on another activity. May be absent on activities recorded before this field was introduced.

      - `"not_used"`

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "social_login_succeeded"`

      - `"social_login_succeeded"`

  - `StepUpAuthenticationFailed object { actor, method, reason, 6 more }`

    An additional identity check failed.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

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

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `trusted_device_id: optional string or null`

      Identifier of the trusted device the attempt referenced, e.g. "tdev_...". Present only for the device key method.

    - `type: optional "step_up_authentication_failed"`

      - `"step_up_authentication_failed"`

  - `StepUpAuthenticationSucceeded object { actor, method, id, 5 more }`

    The user completed an additional identity check to confirm a sensitive action.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

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

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `trusted_device_id: optional string or null`

      Identifier of the trusted device used, e.g. "tdev_...". Present only for the device key method.

    - `type: optional "step_up_authentication_succeeded"`

      - `"step_up_authentication_succeeded"`

  - `StepUpCredentialEnrolled object { actor, credential_id, id, 4 more }`

    A user enrolled a passkey for confirming sensitive actions on their account.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `credential_id: string`

      Identifier of the enrolled credential, e.g. "sucr_...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "step_up_credential_enrolled"`

      - `"step_up_credential_enrolled"`

  - `SubscriptionCancellationScheduled object { actor, id, created_at, 3 more }`

    Subscription cancellation was scheduled at end of billing period.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "subscription_cancellation_scheduled"`

      - `"subscription_cancellation_scheduled"`

  - `SubscriptionQuantityUpdated object { actor, added_seats, new_quantity, 6 more }`

    Contracted subscription seat quantity was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `added_seats: number`

    - `new_quantity: number`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `previous_quantity: optional number or null`

    - `type: optional "subscription_quantity_updated"`

      - `"subscription_quantity_updated"`

  - `SubscriptionRenewed object { actor, id, billing_interval, 5 more }`

    A cancelled subscription was renewed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `billing_interval: optional string or null`

      Billing interval (e.g. monthly, annual).

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `plan_type: optional string or null`

      Plan type being renewed into (e.g. team).

    - `type: optional "subscription_renewed"`

      - `"subscription_renewed"`

  - `SubscriptionResumed object { actor, id, created_at, 3 more }`

    A scheduled subscription cancellation was reversed.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "subscription_resumed"`

      - `"subscription_resumed"`

  - `SubscriptionStarted object { actor, id, billing_interval, 6 more }`

    A new subscription was created (Team or Enterprise).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `billing_interval: optional string or null`

      Billing interval (e.g. monthly, annual).

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `plan_type: optional string or null`

      Type of subscription started (e.g. team, enterprise).

    - `seat_count: optional number or null`

      Number of seats purchased.

    - `type: optional "subscription_started"`

      - `"subscription_started"`

  - `SubscriptionUpgraded object { actor, id, created_at, 5 more }`

    Subscription plan was upgraded (e.g. Team to Enterprise).

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `new_plan: optional string or null`

      New plan type after upgrade.

    - `old_plan: optional string or null`

      Previous plan type.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "subscription_upgraded"`

      - `"subscription_upgraded"`

  - `TrustedDeviceCredentialRotated object { actor, trusted_device_id, id, 4 more }`

    The identity-verification credential of a trusted device was rotated to a new key.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `trusted_device_id: string`

      Identifier of the device whose credential was rotated, e.g. "tdev_...".

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "trusted_device_credential_rotated"`

      - `"trusted_device_credential_rotated"`

  - `TrustedDeviceEnrolled object { actor, enrollment_method, platform, 6 more }`

    A device was enrolled as a trusted device for the user's account. Trusted devices can be used to confirm the user's identity for sensitive actions.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

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

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "trusted_device_enrolled"`

      - `"trusted_device_enrolled"`

  - `TrustedDeviceRevoked object { actor, reason, id, 6 more }`

    A trusted device was removed from the user's account.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

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

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `revoked_count: optional number or null`

      Number of devices removed. Set when a security action removed all of the user's trusted devices at once; absent when a single device was removed (see trusted_device_id).

    - `trusted_device_id: optional string or null`

      Identifier of the device that was removed, e.g. "tdev_...". Set when a single device was removed; absent when several devices were removed at once (see revoked_count).

    - `type: optional "trusted_device_revoked"`

      - `"trusted_device_revoked"`

  - `TunnelArchived object { actor, tunnel_id, id, 4 more }`

    An MCP tunnel was archived.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `tunnel_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "tunnel_archived"`

      - `"tunnel_archived"`

  - `TunnelCertificateAdded object { actor, certificate_id, tunnel_id, 6 more }`

    An inner-TLS CA certificate was added to a tunnel.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `certificate_id: string`

    - `tunnel_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `certificate_fingerprint: optional string or null`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "tunnel_certificate_added"`

      - `"tunnel_certificate_added"`

  - `TunnelCertificateRevoked object { actor, certificate_id, tunnel_id, 6 more }`

    An inner-TLS CA certificate was revoked from a tunnel.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `certificate_id: string`

    - `tunnel_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `certificate_fingerprint: optional string or null`

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "tunnel_certificate_revoked"`

      - `"tunnel_certificate_revoked"`

  - `TunnelCreated object { actor, tunnel_id, id, 4 more }`

    An MCP tunnel was created.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `tunnel_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "tunnel_created"`

      - `"tunnel_created"`

  - `TunnelTokenMinted object { actor, token_id, id, 5 more }`

    An OAuth bearer token for the tunnel management API was minted.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `token_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `token_name: optional string or null`

    - `type: optional "tunnel_token_minted"`

      - `"tunnel_token_minted"`

  - `TunnelTokenRevealed object { actor, tunnel_id, tunnel_token_id, 5 more }`

    The Cloudflare connector secret for a tunnel was revealed to the caller.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `tunnel_id: string`

    - `tunnel_token_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "tunnel_token_revealed"`

      - `"tunnel_token_revealed"`

  - `TunnelTokenRevoked object { actor, token_id, id, 5 more }`

    An OAuth bearer token for the tunnel management API was revoked.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `token_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `token_name: optional string or null`

      Name the administrator gave the token when it was created, if any

    - `type: optional "tunnel_token_revoked"`

      - `"tunnel_token_revoked"`

  - `TunnelTokenRotated object { actor, tunnel_id, tunnel_token_id, 6 more }`

    The Cloudflare connector secret for a tunnel was rotated.

    `tunnel_token_id` is the id of the *newly-issued* token. The previous
    token is invalidated by the rotation and its id is not recorded here.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `tunnel_id: string`

    - `tunnel_token_id: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `reason: optional string or null`

    - `type: optional "tunnel_token_rotated"`

      - `"tunnel_token_rotated"`

  - `UserConsentRecorded object { actor, consent_type, entity_id, 6 more }`

    User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `consent_type: string`

    - `entity_id: string`

    - `entity_type: string`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "user_consent_recorded"`

      - `"user_consent_recorded"`

  - `UserConsentRevoked object { actor, id, consent_id, 7 more }`

    User revoked a previously granted consent for a specific entity.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `consent_id: optional string or null`

    - `consent_type: optional string or null`

    - `created_at: optional string`

      When this activity occurred.

    - `entity_id: optional string or null`

    - `entity_type: optional string or null`

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "user_consent_revoked"`

      - `"user_consent_revoked"`

  - `ClaudeUserRoleUpdated object { actor, current_role, previous_role, 7 more }`

    A user's role within the organization was changed, or the user was added to or removed from the organization.

    - `actor: object { email_address, ip_address, user_agent, 2 more }  or object { admin_api_key_id, ip_address, user_agent, type }  or object { api_key_id, ip_address, user_agent, type }  or 3 more`

      An external identity asserted by a trusted provider — a cloud-provider
      gateway or a customer-registered federation issuer — acting without an
      Anthropic-provisioned account or service account.

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

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

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_user_role_updated"`

      - `"claude_user_role_updated"`

  - `ClaudeUserSettingsUpdated object { actor, updates, id, 4 more }`

    User updated their personal settings.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `updates: array of object { current_value, previous_value, type }  or object { current_value, previous_value, type }  or object { current_value, previous_value, type }  or 19 more`

      - `FullName object { current_value, previous_value, type }`

        - `current_value: string or null`

        - `previous_value: string or null`

        - `type: optional "full_name"`

          - `"full_name"`

      - `DisplayName object { current_value, previous_value, type }`

        - `current_value: string or null`

        - `previous_value: string or null`

        - `type: optional "display_name"`

          - `"display_name"`

      - `ArtifactsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "artifacts_enabled"`

          - `"artifacts_enabled"`

      - `LatexEnabled object { current_value, previous_value, type }`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "latex_enabled"`

          - `"latex_enabled"`

      - `AnalysisToolEnabled object { current_value, previous_value, type }`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "analysis_tool_enabled"`

          - `"analysis_tool_enabled"`

      - `ChatSuggestionsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "chat_suggestions_enabled"`

          - `"chat_suggestions_enabled"`

      - `MultimodalPdfsEnabled object { current_value, previous_value, type }`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "multimodal_pdfs_enabled"`

          - `"multimodal_pdfs_enabled"`

      - `GDriveEnabled object { current_value, previous_value, type }`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "gdrive_enabled"`

          - `"gdrive_enabled"`

      - `WebSearchEnabled object { current_value, previous_value, type }`

        The web search setting was changed.

        - `current_value: boolean or null`

          Setting value immediately after this change

        - `previous_value: boolean or null`

          Setting value immediately before this change

        - `type: optional "web_search_enabled"`

          - `"web_search_enabled"`

      - `GeolocationEnabled object { current_value, previous_value, type }`

        The geolocation setting was changed.

        - `current_value: boolean or null`

          Setting value immediately after this change

        - `previous_value: boolean or null`

          Setting value immediately before this change

        - `type: optional "geolocation_enabled"`

          - `"geolocation_enabled"`

      - `UserMemoryEnabledSetting object { current_value, previous_value, type }`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "enabled_saffron"`

          - `"enabled_saffron"`

      - `McpToolsEnabled object { current_value, previous_value, type }`

        - `current_value: map[boolean] or null`

        - `previous_value: map[boolean] or null`

        - `type: optional "mcp_tools_enabled"`

          - `"mcp_tools_enabled"`

      - `CliOpPermissionsEnabled object { current_value, previous_value, type }`

        - `current_value: map[string] or null`

        - `previous_value: map[string] or null`

        - `type: optional "cli_op_permissions_enabled"`

          - `"cli_op_permissions_enabled"`

      - `GoogleDriveSearchEnabled object { current_value, previous_value, type }`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "google_drive_search_enabled"`

          - `"google_drive_search_enabled"`

      - `GmailIntegrationEnabled object { current_value, previous_value, type }`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "gmail_integration_enabled"`

          - `"gmail_integration_enabled"`

      - `GoogleCalendarIntegrationEnabled object { current_value, previous_value, type }`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "google_calendar_integration_enabled"`

          - `"google_calendar_integration_enabled"`

      - `ThinkingModeEnabled object { current_value, previous_value, type }`

        - `current_value: "adaptive" or "extended" or "off" or null`

          - `"adaptive"`

          - `"extended"`

          - `"off"`

        - `previous_value: "adaptive" or "extended" or "off" or null`

          - `"adaptive"`

          - `"extended"`

          - `"off"`

        - `type: optional "thinking_mode_enabled"`

          - `"thinking_mode_enabled"`

      - `ResearchModeEnabled object { current_value, previous_value, type }`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "research_mode_enabled"`

          - `"research_mode_enabled"`

      - `ComputerUseEnabled object { current_value, previous_value, type }`

        - `current_value: boolean or null`

        - `previous_value: boolean or null`

        - `type: optional "computer_use_enabled"`

          - `"computer_use_enabled"`

      - `ClaudeAPIInArtifactsEnabled object { current_value, previous_value, type }`

        The Claude API in Artifacts setting was changed.

        - `current_value: boolean or null`

          Setting value immediately after this change

        - `previous_value: boolean or null`

          Setting value immediately before this change

        - `type: optional "claude_api_in_artifacts_enabled"`

          - `"claude_api_in_artifacts_enabled"`

      - `ConversationPreferences object { type }`

        The 'conversation_preferences' for the user were updated. Values omitted.

        - `type: optional "conversation_preferences"`

          - `"conversation_preferences"`

      - `CoworkGlobalInstructions object { type }`

        The Cowork global instructions were updated. Values omitted.

        - `type: optional "cowork_global_instructions"`

          - `"cowork_global_instructions"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "claude_user_settings_updated"`

      - `"claude_user_settings_updated"`

  - `VerificationEvidenceSubmitted object { actor, verification_id, verification_type, 5 more }`

    Verification evidence was submitted for an organization's verification.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `verification_id: string`

      Tagged ID of the verification the evidence was submitted for.

    - `verification_type: string`

      The type of verification the evidence was submitted for.

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "verification_evidence_submitted"`

      - `"verification_evidence_submitted"`

  - `VerificationProgramApplicationCreated object { actor, program_slug, id, 4 more }`

    An organization applied to a verification program.

    - `actor: object { api_key_id, ip_address, user_agent, type }  or object { email_address, ip_address, user_agent, 2 more }  or object { ip_address, user_agent, type, unauthenticated_email_address }  or 8 more`

      Automated background processing performed by Anthropic systems, acting
      without a user or customer credential.

      - `APIActor object { api_key_id, ip_address, user_agent, type }`

        - `api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "api_actor"`

          - `"api_actor"`

      - `UserActor object { email_address, ip_address, user_agent, 2 more }`

        - `email_address: string`

        - `ip_address: string`

        - `user_agent: string`

        - `user_id: string`

        - `type: optional "user_actor"`

          - `"user_actor"`

      - `UnauthenticatedUserActor object { ip_address, user_agent, type, unauthenticated_email_address }`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "unauthenticated_user_actor"`

          - `"unauthenticated_user_actor"`

        - `unauthenticated_email_address: optional string or null`

      - `AnthropicActor object { email_address, type }`

        - `email_address: optional string or null`

        - `type: optional "anthropic_actor"`

          - `"anthropic_actor"`

      - `SystemActor object { service, type }`

        Automated background processing performed by Anthropic systems, acting
        without a user or customer credential.

        - `service: optional string or null`

          Name of the automated process that performed the action, when known.

        - `type: optional "system_actor"`

          - `"system_actor"`

      - `AdminAPIKeyActor object { admin_api_key_id, ip_address, user_agent, type }`

        - `admin_api_key_id: string`

        - `ip_address: string`

        - `user_agent: string`

        - `type: optional "admin_api_key_actor"`

          - `"admin_api_key_actor"`

      - `ServiceAccountActor object { ip_address, service_account_id, user_agent, type }`

        - `ip_address: string`

        - `service_account_id: string`

        - `user_agent: string`

        - `type: optional "service_account_actor"`

          - `"service_account_actor"`

      - `ScimDirectorySyncActor object { directory_id, workos_event_id, idp_connection_type, type }`

        - `directory_id: string`

        - `workos_event_id: string`

        - `idp_connection_type: optional string or null`

        - `type: optional "scim_directory_sync_actor"`

          - `"scim_directory_sync_actor"`

      - `FederatedIdentityActor object { issuer, subject, audience, 3 more }`

        A federated external workload authenticated via a verified OIDC token.

        Carries the verified issuer, subject, and audience claims from the
        presented JWT.

        - `issuer: string`

        - `subject: string`

        - `audience: optional array of string`

        - `ip_address: optional string or null`

        - `type: optional "federated_identity_actor"`

          - `"federated_identity_actor"`

        - `user_agent: optional string or null`

      - `FederatedActor object { provider, ip_address, subject, 2 more }`

        An external identity asserted by a trusted provider — a cloud-provider
        gateway or a customer-registered federation issuer — acting without an
        Anthropic-provisioned account or service account.

        - `provider: object { account_id, signed_principal, type }  or object { subscription_id, type }  or object { project_number, type }  or object { issuer, type }`

          Asserting party: the AWS account the organization is bound to.

          - `FederatedActorAwsProvider object { account_id, signed_principal, type }`

            Asserting party: the AWS account the organization is bound to.

            - `account_id: string`

            - `signed_principal: string`

              The AWS-signed ARN of the IAM principal that requested the token.

            - `type: optional "aws"`

              - `"aws"`

          - `FederatedActorAzureProvider object { subscription_id, type }`

            Asserting party: the Azure subscription the organization is bound to.

            - `subscription_id: string`

            - `type: optional "azure"`

              - `"azure"`

          - `FederatedActorGcpProvider object { project_number, type }`

            Asserting party: the GCP project the organization is bound to.

            - `project_number: string`

            - `type: optional "gcp"`

              - `"gcp"`

          - `FederatedActorOidcProvider object { issuer, type }`

            Asserting party: a customer-registered OIDC federation issuer.

            - `issuer: optional string or null`

              The federation issuer's URL. Null when the presented credential failed verification.

            - `type: optional "oidc"`

              - `"oidc"`

        - `ip_address: optional string or null`

        - `subject: optional string or null`

          The provider's verified identifier for the caller; its form depends on the provider.

        - `type: optional "federated_actor"`

          - `"federated_actor"`

        - `user_agent: optional string or null`

      - `AttestedDeviceActor object { external_client_id, kid_hash, ip_address, 2 more }`

        An attested mobile device authenticated via Apple App Attest.

        - `external_client_id: string`

        - `kid_hash: string`

        - `ip_address: optional string or null`

        - `type: optional "attested_device_actor"`

          - `"attested_device_actor"`

        - `user_agent: optional string or null`

    - `program_slug: string`

      The verification program the organization applied to.

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "verification_program_application_created"`

      - `"verification_program_application_created"`

  - `WorkspaceMemberSpendLimitCreated object { actor, id, account_id, 7 more }`

    A per-member or workspace-default Claude Code spend limit was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `account_id: optional string or null`

      Tagged ID of the user (null for workspace-wide default).

    - `created_at: optional string`

      When this activity occurred.

    - `limit_action: optional string or null`

      The action taken when the limit is reached.

    - `limit_usd: optional number or null`

      The spend limit threshold in USD cents.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "workspace_member_spend_limit_created"`

      - `"workspace_member_spend_limit_created"`

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceMemberSpendLimitDeleted object { actor, id, account_id, 6 more }`

    A per-member or workspace-default Claude Code spend limit was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `account_id: optional string or null`

      Tagged ID of the user (null for workspace-wide default).

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `spend_limit_id: optional string or null`

      UUID of the deleted spend limit.

    - `type: optional "workspace_member_spend_limit_deleted"`

      - `"workspace_member_spend_limit_deleted"`

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceMemberSpendLimitUpdated object { actor, id, account_id, 7 more }`

    A per-member Claude Code spend limit amount was updated.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `account_id: optional string or null`

      Tagged ID of the user (null for workspace-wide default).

    - `created_at: optional string`

      When this activity occurred.

    - `new_limit_usd: optional number or null`

      The new spend limit threshold in USD cents.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `spend_limit_id: optional string or null`

      UUID of the spend limit.

    - `type: optional "workspace_member_spend_limit_updated"`

      - `"workspace_member_spend_limit_updated"`

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceSpendLimitAlertEmailsUpdated object { actor, id, alert_emails, 5 more }`

    Spend limit alert email recipients were updated for a workspace.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `alert_emails: optional array of string or null`

      Updated list of alert email addresses.

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "workspace_spend_limit_alert_emails_updated"`

      - `"workspace_spend_limit_alert_emails_updated"`

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceSpendLimitCreated object { actor, id, created_at, 6 more }`

    A workspace-level API spend limit was created.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `limit_action: optional string or null`

      The action taken when the limit is reached (notify_only or notify_and_pause).

    - `limit_usd: optional number or null`

      The spend limit threshold in USD cents.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `type: optional "workspace_spend_limit_created"`

      - `"workspace_spend_limit_created"`

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

  - `WorkspaceSpendLimitDeleted object { actor, id, created_at, 5 more }`

    A workspace-level API spend limit was deleted.

    - `actor: object { email_address, ip_address, user_agent, 2 more }`

      - `email_address: string`

      - `ip_address: string`

      - `user_agent: string`

      - `user_id: string`

      - `type: optional "user_actor"`

        - `"user_actor"`

    - `id: optional string`

      Unique identifier for the activity e.g. 'activity_abcd1234'

    - `created_at: optional string`

      When this activity occurred.

    - `organization_id: optional string or null`

      Organization ID this activity is associated with

    - `organization_uuid: optional string or null`

      Organization UUID where the activity occurred. Null when the activity is not tied to an organization (for example, login and logout events or calls to the Compliance API).

    - `spend_limit_id: optional string or null`

      UUID of the deleted spend limit.

    - `type: optional "workspace_spend_limit_deleted"`

      - `"workspace_spend_limit_deleted"`

    - `workspace_id: optional string or null`

      Tagged ID of the workspace.

# Organizations

## List organizations

**get** `/v1/compliance/organizations`

List organizations under the parent organization.

Returns organizations sorted by creation date in ascending order. Use
`limit` and `page` to paginate: each response includes `has_more` and a
`next_page` token to pass on the next request.

### Query Parameters

- `limit: optional number`

  Maximum results (default: 1000, max: 1000)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { created_at, name, uuid }`

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

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Domain Types

### Organization List Response

- `OrganizationListResponse object { created_at, name, uuid }`

  Information about an organization.

  - `created_at: string`

    Organization creation time (RFC 3339 format)

  - `name: string`

    Organization name

  - `uuid: string`

    Unique identifier for the organization (UUID format)

# Users

## List organization users

**get** `/v1/compliance/organizations/{org_uuid}/users`

List current user members of an organization.

### Path Parameters

- `org_uuid: string`

  The organization UUID

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, email, 2 more }`

  List of current organization members sorted by organization join date ascending

  - `id: string`

    User identifier (tagged ID)

  - `created_at: string`

    User account creation timestamp

  - `email: string`

    User's current email address

  - `full_name: string`

    User's current full name

  - `organization_role: "admin" or "billing" or "claude_code_user" or 6 more`

    User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/users \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Domain Types

### User List Response

- `UserListResponse object { id, created_at, email, 2 more }`

  User member information for compliance responses.

  - `id: string`

    User identifier (tagged ID)

  - `created_at: string`

    User account creation timestamp

  - `email: string`

    User's current email address

  - `full_name: string`

    User's current full name

  - `organization_role: "admin" or "billing" or "claude_code_user" or 6 more`

    User's built-in role within the organization. This is distinct from any custom RBAC roles that may also be assigned.

    - `"admin"`

    - `"billing"`

    - `"claude_code_user"`

    - `"developer"`

    - `"managed"`

    - `"membership_admin"`

    - `"owner"`

    - `"primary_owner"`

    - `"user"`

# Roles

## List Compliance Roles

**get** `/v1/compliance/organizations/{org_uuid}/roles`

List Compliance Roles

### Path Parameters

- `org_uuid: string`

  The organization UUID

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, description, 2 more }`

  List of roles

  - `id: string`

    Role identifier (tagged ID)

  - `created_at: string or null`

    Role creation timestamp (ISO 8601)

  - `description: string`

    Role description

  - `name: string`

    Role name

  - `updated_at: string or null`

    Role last-updated timestamp (ISO 8601)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
      "created_at": "2025-03-12T18:22:41.123456",
      "description": "Full administrative access to organization settings and members",
      "name": "Organization Admin",
      "updated_at": "2025-03-14T09:05:17.456789"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Get Compliance Role

**get** `/v1/compliance/organizations/{org_uuid}/roles/{role_id}`

Get Compliance Role

### Path Parameters

- `org_uuid: string`

  The organization UUID

- `role_id: string`

  The role ID (tagged ID, e.g., rbac_role_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Role identifier (tagged ID)

- `created_at: string or null`

  Role creation timestamp (ISO 8601)

- `description: string`

  Role description

- `name: string`

  Role name

- `updated_at: string or null`

  Role last-updated timestamp (ISO 8601)

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
  "created_at": "2025-03-12T18:22:41.123456",
  "description": "Full administrative access to organization settings and members",
  "name": "Organization Admin",
  "updated_at": "2025-03-14T09:05:17.456789"
}
```

## Domain Types

### Role List Response

- `RoleListResponse object { id, created_at, description, 2 more }`

  Role information for compliance responses.

  - `id: string`

    Role identifier (tagged ID)

  - `created_at: string or null`

    Role creation timestamp (ISO 8601)

  - `description: string`

    Role description

  - `name: string`

    Role name

  - `updated_at: string or null`

    Role last-updated timestamp (ISO 8601)

### Role Retrieve Response

- `RoleRetrieveResponse object { id, created_at, description, 2 more }`

  Role information for compliance responses.

  - `id: string`

    Role identifier (tagged ID)

  - `created_at: string or null`

    Role creation timestamp (ISO 8601)

  - `description: string`

    Role description

  - `name: string`

    Role name

  - `updated_at: string or null`

    Role last-updated timestamp (ISO 8601)

# Permissions

## List Compliance Role Permissions

**get** `/v1/compliance/organizations/{org_uuid}/roles/{role_id}/permissions`

List Compliance Role Permissions

### Path Parameters

- `org_uuid: string`

  The organization UUID

- `role_id: string`

  The role ID (tagged ID, e.g., rbac_role_abc123)

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { action, resource_id, resource_type }`

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

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID/permissions \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Domain Types

### Permission List Response

- `PermissionListResponse object { action, resource_id, resource_type }`

  Permission granted by a role.

  - `action: string`

    Action permitted on the resource

  - `resource_id: string`

    Identifier of the resource the permission applies to

  - `resource_type: string`

    Type of resource the permission applies to

# Settings

## Get effective organization settings

**get** `/v1/compliance/organizations/{organization_id}/settings`

Retrieve the effective settings for an organization.

Returns the settings currently in force for the given organization — the
enforced state after all policies are applied, which may differ from what
is configured in the admin console. Settings an organization's
administrators cannot change (for example, ones controlled by Anthropic
policy or not available to the organization) are omitted from the list.

The organization must belong to the API key's organization hierarchy;
unknown organizations and organizations outside the hierarchy return 404.

### Path Parameters

- `organization_id: string`

  The organization's UUID

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `api_keys: array of object { id, created_at, created_by_id, 5 more }`

  Compliance API keys configured for the organization hierarchy, ordered by creation time ascending. Key secret values are never included.

  - `id: string`

    Unique identifier for the API key.

  - `created_at: string`

    When the key was created.

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

  - `type: optional "compliance_api_key"`

    - `"compliance_api_key"`

- `organization_id: string`

- `settings: array of object { name, value, type }  or object { name, value, type }  or object { name, value, type }  or 3 more`

  - `Boolean object { name, value, type }`

    A setting whose enforced value is a single true/false flag.

    - `name: "ai_powered_artifacts_enabled" or "api_workbench_feedback_collection_enabled" or "artifact_connectors_enabled" or 43 more`

      - `"ai_powered_artifacts_enabled"`

      - `"api_workbench_feedback_collection_enabled"`

      - `"artifact_connectors_enabled"`

      - `"ask_your_org_enabled"`

      - `"chat_enabled"`

      - `"claude_ai_chat_sharing_enabled"`

      - `"claude_ai_feedback_collection_enabled"`

      - `"claude_ai_integration_sharing_enabled"`

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

      - `"claude_in_slack_enabled"`

      - `"code_execution_enabled"`

      - `"code_execution_network_egress_enabled"`

      - `"connector_tools_default_always_allow"`

      - `"content_redaction_enabled"`

      - `"cowork_trusted_devices_required"`

      - `"desktop_extension_allowlist_enabled"`

      - `"directory_sync_enabled"`

      - `"frontier_data_use_enabled"`

      - `"hipaa_compliance_enabled"`

      - `"inline_visualizations_enabled"`

      - `"ip_allowlist_enabled"`

      - `"location_metadata_enabled"`

      - `"member_usage_dashboard_visible"`

      - `"memory_enabled"`

      - `"org_wide_skill_sharing_enabled"`

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

    - `type: optional "boolean"`

      - `"boolean"`

  - `Integer object { name, value, type }`

    A setting whose enforced value is a whole number; null means no limit
    is in force.

    - `name: "account_session_duration_seconds"`

      - `"account_session_duration_seconds"`

    - `value: number or null`

    - `type: optional "integer"`

      - `"integer"`

  - `String object { name, value, type }`

    A setting whose enforced value is a single string; null means no value
    is configured.

    - `name: "claude_code_default_worker_environment_id" or "claude_code_default_worker_pool_id"`

      - `"claude_code_default_worker_environment_id"`

      - `"claude_code_default_worker_pool_id"`

    - `value: string or null`

    - `type: optional "string"`

      - `"string"`

  - `StringList object { name, value, type }`

    A setting whose enforced value is a list of strings.

    - `name: "allowed_invite_domains" or "disabled_admin_request_types" or "ip_allowlist_ip_ranges"`

      - `"allowed_invite_domains"`

      - `"disabled_admin_request_types"`

      - `"ip_allowlist_ip_ranges"`

    - `value: array of string`

    - `type: optional "string_list"`

      - `"string_list"`

  - `ProvisioningMode object { value, name, type }`

    How organization members are provisioned, resolved to the enforced mode.

    A configured mode is reported only while the mechanism that enforces it is
    active: just-in-time modes require single sign-on to be enabled, and SCIM
    modes require directory sync to be enabled. Otherwise `login_only` is
    reported, regardless of any stored configuration.

    - `value: "jit_advanced" or "jit_permissive" or "login_only" or 2 more`

      How organization members are provisioned under SSO.

      - `"jit_advanced"`

      - `"jit_permissive"`

      - `"login_only"`

      - `"scim_advanced"`

      - `"scim_permissive"`

    - `name: optional "sso_provisioning_mode"`

      - `"sso_provisioning_mode"`

    - `type: optional "provisioning_mode"`

      - `"provisioning_mode"`

  - `DataRetention object { value, name, type }`

    The data retention periods in force, keyed by the type of data they
    apply to.

    A key of `all` covers every data type and is exclusive: when present it
    is the only key. A missing key means no organization-level
    administrator-configured retention period is in force for that data type;
    Anthropic's service defaults may still apply.

    - `value: map[object { duration, timescale, type }  or object { type } ]`

      - `Fixed object { duration, timescale, type }`

        A fixed retention window measured from each item's last activity.

        - `duration: number`

        - `timescale: "day" or "month"`

          - `"day"`

          - `"month"`

        - `type: optional "fixed"`

          - `"fixed"`

      - `Indefinite object { type }`

        An indefinite retention period: data is kept with no time limit.

        - `type: optional "indefinite"`

          - `"indefinite"`

    - `name: optional "data_retention_periods"`

      - `"data_retention_periods"`

    - `type: optional "data_retention"`

      - `"data_retention"`

- `type: optional "effective_organization_settings"`

  - `"effective_organization_settings"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/organizations/$ORGANIZATION_ID/settings \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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
      "name": "ai_powered_artifacts_enabled",
      "value": true,
      "type": "boolean"
    }
  ],
  "type": "effective_organization_settings"
}
```

## Domain Types

### Setting Retrieve Response

- `SettingRetrieveResponse object { api_keys, organization_id, settings, type }`

  The resolved settings in force for one organization at read time.

  Settings appear at most once each, in a fixed relative order, and values
  reflect the enforced state. A setting the organization's administrators
  cannot change — for example, one controlled by Anthropic policy or not
  available to the organization — is omitted from the list.

  - `api_keys: array of object { id, created_at, created_by_id, 5 more }`

    Compliance API keys configured for the organization hierarchy, ordered by creation time ascending. Key secret values are never included.

    - `id: string`

      Unique identifier for the API key.

    - `created_at: string`

      When the key was created.

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

    - `type: optional "compliance_api_key"`

      - `"compliance_api_key"`

  - `organization_id: string`

  - `settings: array of object { name, value, type }  or object { name, value, type }  or object { name, value, type }  or 3 more`

    - `Boolean object { name, value, type }`

      A setting whose enforced value is a single true/false flag.

      - `name: "ai_powered_artifacts_enabled" or "api_workbench_feedback_collection_enabled" or "artifact_connectors_enabled" or 43 more`

        - `"ai_powered_artifacts_enabled"`

        - `"api_workbench_feedback_collection_enabled"`

        - `"artifact_connectors_enabled"`

        - `"ask_your_org_enabled"`

        - `"chat_enabled"`

        - `"claude_ai_chat_sharing_enabled"`

        - `"claude_ai_feedback_collection_enabled"`

        - `"claude_ai_integration_sharing_enabled"`

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

        - `"claude_in_slack_enabled"`

        - `"code_execution_enabled"`

        - `"code_execution_network_egress_enabled"`

        - `"connector_tools_default_always_allow"`

        - `"content_redaction_enabled"`

        - `"cowork_trusted_devices_required"`

        - `"desktop_extension_allowlist_enabled"`

        - `"directory_sync_enabled"`

        - `"frontier_data_use_enabled"`

        - `"hipaa_compliance_enabled"`

        - `"inline_visualizations_enabled"`

        - `"ip_allowlist_enabled"`

        - `"location_metadata_enabled"`

        - `"member_usage_dashboard_visible"`

        - `"memory_enabled"`

        - `"org_wide_skill_sharing_enabled"`

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

      - `type: optional "boolean"`

        - `"boolean"`

    - `Integer object { name, value, type }`

      A setting whose enforced value is a whole number; null means no limit
      is in force.

      - `name: "account_session_duration_seconds"`

        - `"account_session_duration_seconds"`

      - `value: number or null`

      - `type: optional "integer"`

        - `"integer"`

    - `String object { name, value, type }`

      A setting whose enforced value is a single string; null means no value
      is configured.

      - `name: "claude_code_default_worker_environment_id" or "claude_code_default_worker_pool_id"`

        - `"claude_code_default_worker_environment_id"`

        - `"claude_code_default_worker_pool_id"`

      - `value: string or null`

      - `type: optional "string"`

        - `"string"`

    - `StringList object { name, value, type }`

      A setting whose enforced value is a list of strings.

      - `name: "allowed_invite_domains" or "disabled_admin_request_types" or "ip_allowlist_ip_ranges"`

        - `"allowed_invite_domains"`

        - `"disabled_admin_request_types"`

        - `"ip_allowlist_ip_ranges"`

      - `value: array of string`

      - `type: optional "string_list"`

        - `"string_list"`

    - `ProvisioningMode object { value, name, type }`

      How organization members are provisioned, resolved to the enforced mode.

      A configured mode is reported only while the mechanism that enforces it is
      active: just-in-time modes require single sign-on to be enabled, and SCIM
      modes require directory sync to be enabled. Otherwise `login_only` is
      reported, regardless of any stored configuration.

      - `value: "jit_advanced" or "jit_permissive" or "login_only" or 2 more`

        How organization members are provisioned under SSO.

        - `"jit_advanced"`

        - `"jit_permissive"`

        - `"login_only"`

        - `"scim_advanced"`

        - `"scim_permissive"`

      - `name: optional "sso_provisioning_mode"`

        - `"sso_provisioning_mode"`

      - `type: optional "provisioning_mode"`

        - `"provisioning_mode"`

    - `DataRetention object { value, name, type }`

      The data retention periods in force, keyed by the type of data they
      apply to.

      A key of `all` covers every data type and is exclusive: when present it
      is the only key. A missing key means no organization-level
      administrator-configured retention period is in force for that data type;
      Anthropic's service defaults may still apply.

      - `value: map[object { duration, timescale, type }  or object { type } ]`

        - `Fixed object { duration, timescale, type }`

          A fixed retention window measured from each item's last activity.

          - `duration: number`

          - `timescale: "day" or "month"`

            - `"day"`

            - `"month"`

          - `type: optional "fixed"`

            - `"fixed"`

        - `Indefinite object { type }`

          An indefinite retention period: data is kept with no time limit.

          - `type: optional "indefinite"`

            - `"indefinite"`

      - `name: optional "data_retention_periods"`

        - `"data_retention_periods"`

      - `type: optional "data_retention"`

        - `"data_retention"`

  - `type: optional "effective_organization_settings"`

    - `"effective_organization_settings"`

# Groups

## List Compliance Groups

**get** `/v1/compliance/groups`

List Compliance Groups

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `name_prefix: optional string`

  Filter groups by name prefix

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, description, 4 more }`

  List of groups

  - `id: string`

    Group identifier (tagged ID)

  - `created_at: string or null`

    Group creation timestamp (ISO 8601)

  - `description: string`

    Group description

  - `name: string`

    Group name

  - `roles: array of string or null`

    Role IDs assigned to this group.

  - `source_type: string`

    How the group was created ('direct' or 'scim')

  - `updated_at: string or null`

    Group last-updated timestamp (ISO 8601)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/groups \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "created_at": "2025-03-12T18:22:41.123456",
      "description": "All members of the engineering organization",
      "name": "Engineering Team",
      "roles": [
        "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
        "rbac_role_01HtCd4mFoAseWS3RnzKcwE7"
      ],
      "source_type": "scim",
      "updated_at": "2025-03-14T09:05:17.456789"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Get Compliance Group

**get** `/v1/compliance/groups/{group_id}`

Get Compliance Group

### Path Parameters

- `group_id: string`

  The group ID (tagged ID, e.g., rbac_group_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Group identifier (tagged ID)

- `created_at: string or null`

  Group creation timestamp (ISO 8601)

- `description: string`

  Group description

- `name: string`

  Group name

- `roles: array of string or null`

  Role IDs assigned to this group.

- `source_type: string`

  How the group was created ('direct' or 'scim')

- `updated_at: string or null`

  Group last-updated timestamp (ISO 8601)

### Example

```http
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2025-03-12T18:22:41.123456",
  "description": "All members of the engineering organization",
  "name": "Engineering Team",
  "roles": [
    "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
    "rbac_role_01HtCd4mFoAseWS3RnzKcwE7"
  ],
  "source_type": "scim",
  "updated_at": "2025-03-14T09:05:17.456789"
}
```

## Domain Types

### Group List Response

- `GroupListResponse object { id, created_at, description, 4 more }`

  Group information for compliance responses.

  - `id: string`

    Group identifier (tagged ID)

  - `created_at: string or null`

    Group creation timestamp (ISO 8601)

  - `description: string`

    Group description

  - `name: string`

    Group name

  - `roles: array of string or null`

    Role IDs assigned to this group.

  - `source_type: string`

    How the group was created ('direct' or 'scim')

  - `updated_at: string or null`

    Group last-updated timestamp (ISO 8601)

### Group Retrieve Response

- `GroupRetrieveResponse object { id, created_at, description, 4 more }`

  Group information for compliance responses.

  - `id: string`

    Group identifier (tagged ID)

  - `created_at: string or null`

    Group creation timestamp (ISO 8601)

  - `description: string`

    Group description

  - `name: string`

    Group name

  - `roles: array of string or null`

    Role IDs assigned to this group.

  - `source_type: string`

    How the group was created ('direct' or 'scim')

  - `updated_at: string or null`

    Group last-updated timestamp (ISO 8601)

# Members

## List Compliance Group Members

**get** `/v1/compliance/groups/{group_id}/members`

List Compliance Group Members

### Path Parameters

- `group_id: string`

  The group ID (tagged ID, e.g., rbac_group_abc123)

### Query Parameters

- `limit: optional number`

  Maximum results (default: 500, max: 1000)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { created_at, email, updated_at, user_id }`

  List of group members

  - `created_at: string or null`

    Membership creation timestamp (ISO 8601)

  - `email: string`

    Member email address

  - `updated_at: string or null`

    Membership last-updated timestamp (ISO 8601)

  - `user_id: string`

    Member user identifier (tagged ID)

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID/members \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "created_at": "2025-03-12T18:22:41.123456",
      "email": "jane.doe@example.com",
      "updated_at": "2025-03-14T09:05:17.456789",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
    }
  ],
  "has_more": true,
  "next_page": "cGFnZV90b2tlbl9leGFtcGxlXzE3MzQ1Njc4OTA="
}
```

## Domain Types

### Member List Response

- `MemberListResponse object { created_at, email, updated_at, user_id }`

  Group member for compliance responses.

  - `created_at: string or null`

    Membership creation timestamp (ISO 8601)

  - `email: string`

    Member email address

  - `updated_at: string or null`

    Membership last-updated timestamp (ISO 8601)

  - `user_id: string`

    Member user identifier (tagged ID)

# Apps

# Chats

## List chats

**get** `/v1/compliance/apps/chats`

Lists chat metadata with filtering capabilities for targeted
compliance review. Results are sorted chronologically (time ascending)
by the `order_by` key, with ties broken by id.

### Query Parameters

- `after_id: optional string`

  Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `before_id: optional string`

  Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `created_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter chats created after this time (RFC 3339 format)

  - `gte: optional string`

    Filter chats created at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter chats created before this time (RFC 3339 format)

  - `lte: optional string`

    Filter chats created at or before this time (RFC 3339 format)

- `limit: optional number`

  Maximum results (default: 100, max: 1000)

- `order_by: optional "created_at" or "updated_at"`

  Sort key for results. `created_at` (default) sorts by chat creation time. `updated_at` sorts by last update time and is only supported for org-wide queries (omit user_ids[]). For org-wide queries, any time filter must match the sort key: `created_at.*` filters require `order_by=created_at`, and `updated_at.*` filters require `order_by=updated_at`.

  - `"created_at"`

  - `"updated_at"`

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

- `project_ids: optional array of string`

  Filter by project IDs (accepts `claude_proj_...`). Enumerate IDs via `GET /v1/compliance/apps/projects`. Requires user_ids[]; not supported for org-wide queries.

- `updated_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter chats updated after this time (RFC 3339 format)

  - `gte: optional string`

    Filter chats updated at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter chats updated before this time (RFC 3339 format)

  - `lte: optional string`

    Filter chats updated at or before this time (RFC 3339 format)

- `user_ids: optional array of string`

  Filter to chats created by specific users (max 10 per request). Omit for an org-wide query. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, deleted_at, 8 more }`

  List of chat metadata sorted chronologically by the request's `order_by` key (default `created_at`), tie break by id

  - `id: string`

    Chat ID

  - `created_at: string`

    Creation timestamp

  - `deleted_at: string or null`

    Deletion timestamp if deleted

  - `href: string`

    URL to view this chat in claude.ai

  - `model: string or null`

    Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

  - `name: string`

    Chat name/title

  - `organization_id: string`

    Organization ID this chat belongs to

  - `organization_uuid: string`

    Organization UUID this chat belongs to

  - `project_id: string or null`

    Project ID this chat belongs to

  - `updated_at: string`

    Last update timestamp

  - `user: object { id, email_address }  or null`

    User information for compliance responses.

    - `id: string`

      User identifier

    - `email_address: string`

      User's email address

- `first_id: string or null`

  Opaque pagination cursor for the first chat in the current result set. Pass as `before_id` on the next request to page backwards. Backward pagination is only supported for per-user queries (`user_ids[]` set); org-wide queries do not accept `before_id`. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `last_id: string or null`

  Opaque pagination cursor for the last chat in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "id": "claude_chat_abc123",
      "name": "Product Requirements Discussion",
      "created_at": "2025-06-07T08:09:10Z",
      "updated_at": "2025-06-07T09:10:11Z",
      "organization_id": "org_abc123",
      "organization_uuid": "abcdef0123-4567-89ab-cdef-0123456789ab",
      "project_id": "claude_proj_xyz789",
      "model": "claude-opus-4-7",
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

## Delete chat

**delete** `/v1/compliance/apps/chats/{claude_chat_id}`

Permanently deletes a chat and all associated messages and
files. This is a destructive operation that cannot be undone.

### Path Parameters

- `claude_chat_id: string`

  The chat ID (tagged ID, e.g., claude_chat_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the Claude chat that was deleted

- `type: optional "claude_chat_deleted"`

  Constant string confirming deletion

  - `"claude_chat_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "claude_chat_abc123",
  "type": "claude_chat_deleted"
}
```

## Domain Types

### Chat List Response

- `ChatListResponse object { id, created_at, deleted_at, 8 more }`

  Chat metadata for listing chats (without messages).

  - `id: string`

    Chat ID

  - `created_at: string`

    Creation timestamp

  - `deleted_at: string or null`

    Deletion timestamp if deleted

  - `href: string`

    URL to view this chat in claude.ai

  - `model: string or null`

    Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

  - `name: string`

    Chat name/title

  - `organization_id: string`

    Organization ID this chat belongs to

  - `organization_uuid: string`

    Organization UUID this chat belongs to

  - `project_id: string or null`

    Project ID this chat belongs to

  - `updated_at: string`

    Last update timestamp

  - `user: object { id, email_address }  or null`

    User information for compliance responses.

    - `id: string`

      User identifier

    - `email_address: string`

      User's email address

### Chat Delete Response

- `ChatDeleteResponse object { id, type }`

  Response for deleting a Claude chat.

  - `id: string`

    The ID of the Claude chat that was deleted

  - `type: optional "claude_chat_deleted"`

    Constant string confirming deletion

    - `"claude_chat_deleted"`

# Messages

## Get chat messages

**get** `/v1/compliance/apps/chats/{claude_chat_id}/messages`

Retrieves message history and file metadata for a specific chat.

### Path Parameters

- `claude_chat_id: string`

  The chat ID (tagged ID, e.g., claude_chat_abc123)

### Query Parameters

- `after_id: optional string`

  Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `before_id: optional string`

  Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `created_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter messages created after this time (RFC 3339 format)

  - `gte: optional string`

    Filter messages created at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter messages created before this time (RFC 3339 format)

  - `lte: optional string`

    Filter messages created at or before this time (RFC 3339 format)

- `limit: optional number`

  Maximum results (max: 1000). When omitted, the full result set is returned in one response.

- `order: optional "asc" or "desc"`

  Sort direction for messages within the response. `asc` (the default) returns oldest-first; `desc` returns newest-first.

  - `"asc"`

  - `"desc"`

- `tool_result_max_chars: optional number`

  Maximum characters returned per tool-result text item. Items longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

- `tool_use_input_max_chars: optional number`

  Maximum characters of JSON-encoded tool input returned per tool_use block. Inputs longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

- `updated_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter messages updated after this time (RFC 3339 format)

  - `gte: optional string`

    Filter messages updated at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter messages updated before this time (RFC 3339 format)

  - `lte: optional string`

    Filter messages updated at or before this time (RFC 3339 format)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Chat ID

- `chat_messages: array of object { id, artifacts, content, 4 more }`

  Array of chat messages in order of created_at

  - `id: string`

    Unique identifier for the message e.g. 'claude_chat_msg_abcd1234'

  - `artifacts: array of object { id, artifact_type, title, version_id }  or null`

    Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.

    - `id: string`

      Artifact ID e.g. 'claude_artifact_abc123'

    - `artifact_type: string or null`

      MIME-like artifact type e.g. 'application/vnd.ant.code'

    - `title: string or null`

      Artifact title

    - `version_id: string`

      Artifact version ID e.g. 'claude_artifact_version_abc123'

  - `content: array of object { text, thinking_redacted, truncated, type }  or object { id, input, integration_name, 4 more }  or object { content, integration_name, is_error, 5 more }`

    Content blocks within the message

    - `Text object { text, thinking_redacted, truncated, type }`

      Text content block.

      - `text: string`

        Text content from human or assistant

      - `thinking_redacted: boolean`

        True when content enclosed in the assistant's internal-reasoning tags (or the tag markup itself) was removed from `text` during export. Removal never occurs with this field false. Always false on human messages, whose text is exported verbatim.

      - `truncated: boolean`

        True when `text` was shortened by the server's fixed per-string bound (1 MiB). Always false on chat text blocks.

      - `type: "text"`

        - `"text"`

    - `ToolUse object { id, input, integration_name, 4 more }`

      Tool invocation requested by the assistant.

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

      - `type: "tool_use"`

        - `"tool_use"`

    - `ToolResult object { content, integration_name, is_error, 5 more }`

      Result returned by a tool invocation.

      - `content: array of object { text, type }`

        Text content returned by the tool. Generated files are surfaced via the message's `generated_files` list; other non-text item types (including images and links) are omitted.

        - `text: string`

          Text returned by the tool

        - `type: "text"`

          - `"text"`

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

      - `type: "tool_result"`

        - `"tool_result"`

  - `created_at: string`

    Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

  - `files: array of object { id, created_at, filename, 3 more }  or null`

    Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

    - `id: string`

      File ID

    - `created_at: string`

      File creation timestamp

    - `filename: string`

      Display name of the file

    - `md5: string or null`

      Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available.

    - `mime_type: string or null`

      MIME type of the file's preferred downloadable variant (e.g. 'application/pdf')

    - `size_bytes: number or null`

      Size in bytes of the file's preferred downloadable variant, if known. Null for older files uploaded before size was recorded.

  - `generated_files: array of object { id, filename, md5, 2 more }  or null`

    Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`.

    - `id: string`

      Opaque generated-file id, e.g. 'claude_gen_file_abc123'. Treat as an opaque string; the encoding may change without notice.

    - `filename: string`

      Display name of the generated file

    - `md5: string or null`

      Lowercase hex MD5 of the generated file, when available. Null when no stored hash is available.

    - `mime_type: string or null`

      MIME type reported by the tool that produced the file

    - `size_bytes: number or null`

      Size in bytes of the generated file, when available. Null when the file has expired or size is not recorded.

  - `role: "assistant" or "user"`

    Message sender (user or assistant)

    - `"assistant"`

    - `"user"`

- `created_at: string`

  Creation timestamp

- `deleted_at: string or null`

  Deletion timestamp if deleted

- `first_id: string or null`

  Opaque pagination cursor for the first message in the current result set. Pass as `before_id` on the next request to page backwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `has_more: boolean`

  Whether more chat messages exist beyond the current result set. Use `last_id` as `after_id` in a follow-up request to page forward.

- `href: string`

  URL to view this chat in claude.ai

- `last_id: string or null`

  Opaque pagination cursor for the last message in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `model: string or null`

  Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

- `name: string`

  Chat name

- `organization_id: string`

  Organization ID this chat belongs to

- `organization_uuid: string`

  Organization UUID this chat belongs to

- `project_id: string or null`

  Project ID this chat belongs to

- `updated_at: string`

  Last update timestamp

- `user: object { id, email_address }  or null`

  User information for compliance responses.

  - `id: string`

    User identifier

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID/messages \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "claude_chat_abc123",
  "name": "Product Requirements Discussion",
  "created_at": "2025-06-07T08:09:10Z",
  "updated_at": "2025-06-07T08:09:11Z",
  "organization_id": "org_abc123",
  "organization_uuid": "abcdef0123-4567-89ab-cdef-0123456789ab",
  "project_id": "claude_proj_xyz789",
  "model": "claude-opus-4-7",
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

## Domain Types

### Message List Response

- `MessageListResponse object { id, artifacts, content, 4 more }`

  A single message in a chat conversation.

  - `id: string`

    Unique identifier for the message e.g. 'claude_chat_msg_abcd1234'

  - `artifacts: array of object { id, artifact_type, title, version_id }  or null`

    Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.

    - `id: string`

      Artifact ID e.g. 'claude_artifact_abc123'

    - `artifact_type: string or null`

      MIME-like artifact type e.g. 'application/vnd.ant.code'

    - `title: string or null`

      Artifact title

    - `version_id: string`

      Artifact version ID e.g. 'claude_artifact_version_abc123'

  - `content: array of object { text, thinking_redacted, truncated, type }  or object { id, input, integration_name, 4 more }  or object { content, integration_name, is_error, 5 more }`

    Content blocks within the message

    - `Text object { text, thinking_redacted, truncated, type }`

      Text content block.

      - `text: string`

        Text content from human or assistant

      - `thinking_redacted: boolean`

        True when content enclosed in the assistant's internal-reasoning tags (or the tag markup itself) was removed from `text` during export. Removal never occurs with this field false. Always false on human messages, whose text is exported verbatim.

      - `truncated: boolean`

        True when `text` was shortened by the server's fixed per-string bound (1 MiB). Always false on chat text blocks.

      - `type: "text"`

        - `"text"`

    - `ToolUse object { id, input, integration_name, 4 more }`

      Tool invocation requested by the assistant.

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

      - `type: "tool_use"`

        - `"tool_use"`

    - `ToolResult object { content, integration_name, is_error, 5 more }`

      Result returned by a tool invocation.

      - `content: array of object { text, type }`

        Text content returned by the tool. Generated files are surfaced via the message's `generated_files` list; other non-text item types (including images and links) are omitted.

        - `text: string`

          Text returned by the tool

        - `type: "text"`

          - `"text"`

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

      - `type: "tool_result"`

        - `"tool_result"`

  - `created_at: string`

    Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

  - `files: array of object { id, created_at, filename, 3 more }  or null`

    Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

    - `id: string`

      File ID

    - `created_at: string`

      File creation timestamp

    - `filename: string`

      Display name of the file

    - `md5: string or null`

      Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available.

    - `mime_type: string or null`

      MIME type of the file's preferred downloadable variant (e.g. 'application/pdf')

    - `size_bytes: number or null`

      Size in bytes of the file's preferred downloadable variant, if known. Null for older files uploaded before size was recorded.

  - `generated_files: array of object { id, filename, md5, 2 more }  or null`

    Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`.

    - `id: string`

      Opaque generated-file id, e.g. 'claude_gen_file_abc123'. Treat as an opaque string; the encoding may change without notice.

    - `filename: string`

      Display name of the generated file

    - `md5: string or null`

      Lowercase hex MD5 of the generated file, when available. Null when no stored hash is available.

    - `mime_type: string or null`

      MIME type reported by the tool that produced the file

    - `size_bytes: number or null`

      Size in bytes of the generated file, when available. Null when the file has expired or size is not recorded.

  - `role: "assistant" or "user"`

    Message sender (user or assistant)

    - `"assistant"`

    - `"user"`

# Files

## Get file metadata

**get** `/v1/compliance/apps/chats/files/{claude_file_id}`

Retrieves metadata for a file referenced in chat messages, without
downloading the file content. Use the sibling `/content` endpoint to
download the bytes.

### Path Parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  File ID

- `claude_chat_ids: array of string`

  Chats this file is attached to. A file can be referenced by messages across multiple chats.

- `created_at: string`

  File creation timestamp

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

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Delete file

**delete** `/v1/compliance/apps/chats/files/{claude_file_id}`

Permanently deletes a specific file. This is a destructive
operation that cannot be undone.

### Path Parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the file that was deleted

- `type: optional "claude_file_deleted"`

  Constant string confirming deletion

  - `"claude_file_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "claude_file_xyz789",
  "type": "claude_file_deleted"
}
```

## Download file content

**get** `/v1/compliance/apps/chats/files/{claude_file_id}/content`

Downloads the binary content of a file referenced in chat messages.

### Path Parameters

- `claude_file_id: string`

  The file ID (tagged ID, e.g., claude_file_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### File Retrieve Response

- `FileRetrieveResponse object { id, claude_chat_ids, created_at, 5 more }`

  File metadata for GET /v1/compliance/apps/chats/files/{claude_file_id}.

  Returns metadata only. Use the sibling `/content` endpoint to download
  the file bytes.

  - `id: string`

    File ID

  - `claude_chat_ids: array of string`

    Chats this file is attached to. A file can be referenced by messages across multiple chats.

  - `created_at: string`

    File creation timestamp

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

### File Delete Response

- `FileDeleteResponse object { id, type }`

  Response for deleting a compliance file.

  - `id: string`

    The ID of the file that was deleted

  - `type: optional "claude_file_deleted"`

    Constant string confirming deletion

    - `"claude_file_deleted"`

# Generated Files

## Get Claude-generated file metadata

**get** `/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}`

Returns metadata for a file the assistant created via tool use.

Use the sibling `/content` endpoint to download the bytes.

### Path Parameters

- `claude_gen_file_id: string`

  The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Opaque generated-file id, e.g. 'claude_gen_file_abc123'.

- `claude_chat_id: string`

  The chat this generated file belongs to

- `created_at: string or null`

  File creation timestamp, when available

- `filename: string`

  Display name of the generated file

- `md5: string or null`

  Lowercase hex MD5 of the stored file. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

- `mime_type: string or null`

  MIME type of the stored file, when available

- `size_bytes: number or null`

  Size in bytes of the stored file, when available

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Download a Claude-generated file

**get** `/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`

Downloads the binary content of a file the assistant created via tool use.

### Path Parameters

- `claude_gen_file_id: string`

  The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from GET /apps/chats/{claude_chat_id}/messages.

### Header Parameters

- `"x-api-key": optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Generated File Retrieve Response

- `GeneratedFileRetrieveResponse object { id, claude_chat_id, created_at, 4 more }`

  Metadata for GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}.

  Returns metadata only. Use the sibling `/content` endpoint to download
  the bytes. The owning chat is included since the id is opaque; to find the
  specific message that produced the file, fetch
  `/v1/compliance/apps/chats/{claude_chat_id}/messages` and match on
  `generated_files[].id`.

  - `id: string`

    Opaque generated-file id, e.g. 'claude_gen_file_abc123'.

  - `claude_chat_id: string`

    The chat this generated file belongs to

  - `created_at: string or null`

    File creation timestamp, when available

  - `filename: string`

    Display name of the generated file

  - `md5: string or null`

    Lowercase hex MD5 of the stored file. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

  - `mime_type: string or null`

    MIME type of the stored file, when available

  - `size_bytes: number or null`

    Size in bytes of the stored file, when available

# Projects

## List projects

**get** `/v1/compliance/apps/projects`

Lists project metadata with filtering capabilities. Results
are sorted chronologically (time ascending) by created_at.

### Query Parameters

- `created_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter projects created after this time (RFC 3339 format)

  - `gte: optional string`

    Filter projects created at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter projects created before this time (RFC 3339 format)

  - `lte: optional string`

    Filter projects created at or before this time (RFC 3339 format)

- `limit: optional number`

  Maximum results (default: 20, max: 100)

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `updated_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter projects updated after this time (RFC 3339 format)

  - `gte: optional string`

    Filter projects updated at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter projects updated before this time (RFC 3339 format)

  - `lte: optional string`

    Filter projects updated at or before this time (RFC 3339 format)

- `user_ids: optional array of string`

  Filter by user IDs. Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, deleted_at, 6 more }`

  List of projects sorted by creation date ascending

  - `id: string`

    Project identifier (tagged ID)

  - `created_at: string`

    Project creation timestamp

  - `deleted_at: string or null`

    Timestamp when the project was deleted by an end user, or null otherwise

  - `is_private: boolean`

    If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

  - `name: string`

    Project name

  - `organization_id: string`

    Organization identifier (tagged ID)

  - `organization_uuid: string`

    Organization UUID this project belongs to

  - `updated_at: string`

    Project last update timestamp

  - `user: object { id, email_address }  or null`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of an organization the
    key may read.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Get project details

**get** `/v1/compliance/apps/projects/{project_id}`

Get detailed information for a specific project.

### Path Parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Project identifier (tagged ID)

- `attachments_count: number`

  Number of attachments contained within this project

- `chats_count: number`

  Number of chats contained within this project

- `created_at: string`

  Project creation timestamp

- `deleted_at: string or null`

  Timestamp when the project was deleted by an end user, or null otherwise

- `description: string`

  Project description

- `instructions: string`

  Project's custom instructions / prompt

- `is_private: boolean`

  If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

- `name: string`

  Project name

- `organization_id: string`

  Organization identifier (tagged ID)

- `organization_uuid: string`

  Organization UUID this project belongs to

- `updated_at: string`

  Project last update timestamp

- `user: object { id, email_address }  or null`

  The user who created a project or project document.

  Fields that reference this type are null when the creator's account has
  been deleted or the creator is no longer a member of an organization the
  key may read.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Delete project

**delete** `/v1/compliance/apps/projects/{project_id}`

Delete a project for compliance purposes.

Hard-deletes the project and all its associated data including:

- All project documents and files
- All role assignments
- Knowledge base (if RAG is enabled)
- Sync sources

Project must have no attached chats - returns 409 if chats exist.

### Path Parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the Claude project that was deleted

- `type: optional "claude_project_deleted"`

  Constant string confirming deletion.

  - `"claude_project_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "id",
  "type": "claude_project_deleted"
}
```

## Domain Types

### Project List Response

- `ProjectListResponse object { id, created_at, deleted_at, 6 more }`

  Project information for compliance responses.

  - `id: string`

    Project identifier (tagged ID)

  - `created_at: string`

    Project creation timestamp

  - `deleted_at: string or null`

    Timestamp when the project was deleted by an end user, or null otherwise

  - `is_private: boolean`

    If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

  - `name: string`

    Project name

  - `organization_id: string`

    Organization identifier (tagged ID)

  - `organization_uuid: string`

    Organization UUID this project belongs to

  - `updated_at: string`

    Project last update timestamp

  - `user: object { id, email_address }  or null`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of an organization the
    key may read.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

### Project Retrieve Response

- `ProjectRetrieveResponse object { id, attachments_count, chats_count, 10 more }`

  Detailed project information for compliance responses.

  - `id: string`

    Project identifier (tagged ID)

  - `attachments_count: number`

    Number of attachments contained within this project

  - `chats_count: number`

    Number of chats contained within this project

  - `created_at: string`

    Project creation timestamp

  - `deleted_at: string or null`

    Timestamp when the project was deleted by an end user, or null otherwise

  - `description: string`

    Project description

  - `instructions: string`

    Project's custom instructions / prompt

  - `is_private: boolean`

    If false, the project is visible to all organization members; if true the project is accessible only to the creator and specified collaborators

  - `name: string`

    Project name

  - `organization_id: string`

    Organization identifier (tagged ID)

  - `organization_uuid: string`

    Organization UUID this project belongs to

  - `updated_at: string`

    Project last update timestamp

  - `user: object { id, email_address }  or null`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of an organization the
    key may read.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

### Project Delete Response

- `ProjectDeleteResponse object { id, type }`

  Response for deleting a Claude project.

  - `id: string`

    The ID of the Claude project that was deleted

  - `type: optional "claude_project_deleted"`

    Constant string confirming deletion.

    - `"claude_project_deleted"`

# Attachments

## List project attachments

**get** `/v1/compliance/apps/projects/{project_id}/attachments`

List files and documents attached to a project.

List files and project documents attached to the project referenced by project_id.
This includes the IDs of attached files, and attached project documents.

The raw binary content of attached files can be downloaded using the
GET /v1/compliance/apps/chats/files/{claude_file_id}/content endpoint.

The text content of attached project documents can be fetched using the
GET /v1/compliance/apps/projects/documents/{claude_proj_doc_id} endpoint.

### Path Parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

### Query Parameters

- `limit: optional number`

  Maximum results (default: 20, max: 100)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, filename, 4 more }  or object { id, created_at, filename, 3 more }`

  List of attachments sorted chronologically by created_at, tie break by id

  - `ComplianceProjectFileReference object { id, created_at, filename, 4 more }`

    File attachment reference for compliance responses.

    - `id: string`

      File identifier (e.g., 'claude_file_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

    - `filename: string`

      Display name of the file (e.g., 'document.pdf')

    - `md5: string or null`

      Lowercase hex MD5 of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

    - `mime_type: string`

      MIME type of the file's preferred downloadable variant when one is recorded, else 'application/octet-stream'. Use the per-file `/metadata` endpoint for the authoritative value.

    - `size_bytes: number or null`

      Size in bytes of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

    - `type: "project_file"`

      Discriminator marking this as a binary file

      - `"project_file"`

  - `ComplianceProjectDocReference object { id, created_at, filename, 3 more }`

    Project document attachment reference for compliance responses.

    - `id: string`

      Project document identifier (e.g., 'claude_proj_doc_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

    - `filename: string`

      Display name of the document (e.g., 'document.txt')

    - `mime_type: "text/plain"`

      MIME type of the project document, always set to plain text

      - `"text/plain"`

    - `type: "project_doc"`

      Discriminator marking this as a plain text document

      - `"project_doc"`

    - `updated_at: string or null`

      Last-modified timestamp of the document. Reserved for future use — currently always null.

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  To get the next page, use the 'next_page' from the current response as the 'page' in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/attachments \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Domain Types

### Attachment List Response

- `AttachmentListResponse = object { id, created_at, filename, 4 more }  or object { id, created_at, filename, 3 more }`

  File attachment reference for compliance responses.

  - `ComplianceProjectFileReference object { id, created_at, filename, 4 more }`

    File attachment reference for compliance responses.

    - `id: string`

      File identifier (e.g., 'claude_file_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

    - `filename: string`

      Display name of the file (e.g., 'document.pdf')

    - `md5: string or null`

      Lowercase hex MD5 of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

    - `mime_type: string`

      MIME type of the file's preferred downloadable variant when one is recorded, else 'application/octet-stream'. Use the per-file `/metadata` endpoint for the authoritative value.

    - `size_bytes: number or null`

      Size in bytes of the file's preferred downloadable variant, when recorded. Null otherwise. Use the per-file `/metadata` endpoint for the authoritative value.

    - `type: "project_file"`

      Discriminator marking this as a binary file

      - `"project_file"`

  - `ComplianceProjectDocReference object { id, created_at, filename, 3 more }`

    Project document attachment reference for compliance responses.

    - `id: string`

      Project document identifier (e.g., 'claude_proj_doc_abcd')

    - `created_at: string`

      Creation timestamp (RFC 3339 format)

    - `filename: string`

      Display name of the document (e.g., 'document.txt')

    - `mime_type: "text/plain"`

      MIME type of the project document, always set to plain text

      - `"text/plain"`

    - `type: "project_doc"`

      Discriminator marking this as a plain text document

      - `"project_doc"`

    - `updated_at: string or null`

      Last-modified timestamp of the document. Reserved for future use — currently always null.

# Collaborators

## List project collaborators

**get** `/v1/compliance/apps/projects/{project_id}/collaborators`

List the users, groups, and organization-wide grants on a project.

Each entry represents one active role assignment on the project. Principals
are returned as a discriminated union on `type` — an individual user, an
RBAC group, the whole organization, or all holders of an organization-level
role.

### Path Parameters

- `project_id: string`

  The project ID (tagged ID, e.g., claude_proj_abc123)

### Query Parameters

- `limit: optional number`

  Maximum results (default: 20, max: 100)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { granted_at, role, type, user_id }  or object { granted_at, group_id, role, type }  or object { granted_at, organization_uuid, role, type }  or object { granted_at, organization_role, role, type }`

  List of collaborators sorted chronologically by granted_at, tie break by the underlying role-assignment UUID

  - `ComplianceProjectUserCollaborator object { granted_at, role, type, user_id }`

    An individual user granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "user"`

      Discriminator marking this as an individual user collaborator

      - `"user"`

    - `user_id: string or null`

      Identifier of the user granted access (tagged ID), or null if their account has since been deleted

  - `ComplianceProjectGroupCollaborator object { granted_at, group_id, role, type }`

    An RBAC group granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

    - `group_id: string`

      Identifier of the group granted access (tagged ID)

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "group"`

      Discriminator marking this as a group collaborator

      - `"group"`

  - `ComplianceProjectOrganizationCollaborator object { granted_at, organization_uuid, role, type }`

    An entire organization granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

    - `organization_uuid: string`

      UUID of the organization granted access

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "organization"`

      Discriminator marking this as an organization-wide grant

      - `"organization"`

  - `ComplianceProjectOrganizationRoleCollaborator object { granted_at, organization_role, role, type }`

    All holders of an organization-level role granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

    - `organization_role: string`

      The organization-level role whose holders are granted access

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "organization_role"`

      Discriminator marking this as a grant to all organization members holding a specific org-level role

      - `"organization_role"`

- `has_more: boolean`

  Whether more records exist beyond the current result set

- `next_page: string or null`

  To get the next page, use the 'next_page' from the current response as the 'page' in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/collaborators \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Domain Types

### Collaborator List Response

- `CollaboratorListResponse = object { granted_at, role, type, user_id }  or object { granted_at, group_id, role, type }  or object { granted_at, organization_uuid, role, type }  or object { granted_at, organization_role, role, type }`

  An individual user granted a role on a project.

  - `ComplianceProjectUserCollaborator object { granted_at, role, type, user_id }`

    An individual user granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "user"`

      Discriminator marking this as an individual user collaborator

      - `"user"`

    - `user_id: string or null`

      Identifier of the user granted access (tagged ID), or null if their account has since been deleted

  - `ComplianceProjectGroupCollaborator object { granted_at, group_id, role, type }`

    An RBAC group granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

    - `group_id: string`

      Identifier of the group granted access (tagged ID)

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "group"`

      Discriminator marking this as a group collaborator

      - `"group"`

  - `ComplianceProjectOrganizationCollaborator object { granted_at, organization_uuid, role, type }`

    An entire organization granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

    - `organization_uuid: string`

      UUID of the organization granted access

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "organization"`

      Discriminator marking this as an organization-wide grant

      - `"organization"`

  - `ComplianceProjectOrganizationRoleCollaborator object { granted_at, organization_role, role, type }`

    All holders of an organization-level role granted a role on a project.

    - `granted_at: string`

      When this collaborator was granted access (RFC 3339 format)

    - `organization_role: string`

      The organization-level role whose holders are granted access

    - `role: "admin" or "editor" or "owner" or "viewer"`

      Role granted on the project

      - `"admin"`

      - `"editor"`

      - `"owner"`

      - `"viewer"`

    - `type: "organization_role"`

      Discriminator marking this as a grant to all organization members holding a specific org-level role

      - `"organization_role"`

# Documents

## Get project document content

**get** `/v1/compliance/apps/projects/documents/{document_id}`

Get detailed information for a specific project document.

### Path Parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Project document identifier (tagged ID)

- `content: string`

  Document text content

- `created_at: string`

  Document creation timestamp

- `filename: string`

  Document filename

- `user: object { id, email_address }  or null`

  The user who created a project or project document.

  Fields that reference this type are null when the creator's account has
  been deleted or the creator is no longer a member of an organization the
  key may read.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Get project document metadata

**get** `/v1/compliance/apps/projects/documents/{document_id}/metadata`

Returns metadata for a project document, without the content body.

Use the sibling `GET /v1/compliance/apps/projects/documents/{document_id}`
endpoint to fetch the document text. The `md5` and `size_bytes`
fields here are computed over the UTF-8 encoding of that text, so a DLP
consumer can dedupe or match hashes without downloading every document.

### Path Parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Project document identifier (tagged ID)

- `claude_project_id: string`

  The project this document belongs to

- `created_at: string`

  Document creation timestamp

- `filename: string`

  Document filename

- `md5: string`

  Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.

- `mime_type: "text/plain"`

  MIME type of the document content, always plain text

  - `"text/plain"`

- `size_bytes: number`

  Size in bytes of the document content (UTF-8 encoded)

- `user: object { id, email_address }  or null`

  The user who created a project or project document.

  Fields that reference this type are null when the creator's account has
  been deleted or the creator is no longer a member of an organization the
  key may read.

  - `id: string`

    User identifier (tagged ID)

  - `email_address: string`

    User's email address

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID/metadata \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Delete project document

**delete** `/v1/compliance/apps/projects/documents/{document_id}`

Delete a project document for compliance purposes.

Hard-deletes the project document permanently.

### Path Parameters

- `document_id: string`

  The document ID (tagged ID, e.g., claude_proj_doc_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the project document that was deleted

- `type: "claude_project_document_deleted"`

  Constant string confirming deletion.

  - `"claude_project_document_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/projects/documents/$DOCUMENT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "id",
  "type": "claude_project_document_deleted"
}
```

## Domain Types

### Document Retrieve Response

- `DocumentRetrieveResponse object { id, content, created_at, 2 more }`

  Project document information for compliance responses.

  - `id: string`

    Project document identifier (tagged ID)

  - `content: string`

    Document text content

  - `created_at: string`

    Document creation timestamp

  - `filename: string`

    Document filename

  - `user: object { id, email_address }  or null`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of an organization the
    key may read.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

### Document Metadata Response

- `DocumentMetadataResponse object { id, claude_project_id, created_at, 5 more }`

  Project document metadata for GET /v1/compliance/apps/projects/documents/{document_id}/metadata.

  Returns metadata only. Use the sibling endpoint (without `/metadata`)
  to fetch the document text content.

  - `id: string`

    Project document identifier (tagged ID)

  - `claude_project_id: string`

    The project this document belongs to

  - `created_at: string`

    Document creation timestamp

  - `filename: string`

    Document filename

  - `md5: string`

    Lowercase hex MD5 of the document content (UTF-8 encoded). Matches the `content` field returned by the sibling content endpoint.

  - `mime_type: "text/plain"`

    MIME type of the document content, always plain text

    - `"text/plain"`

  - `size_bytes: number`

    Size in bytes of the document content (UTF-8 encoded)

  - `user: object { id, email_address }  or null`

    The user who created a project or project document.

    Fields that reference this type are null when the creator's account has
    been deleted or the creator is no longer a member of an organization the
    key may read.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

### Document Delete Response

- `DocumentDeleteResponse object { id, type }`

  Response for deleting a project document.

  - `id: string`

    The ID of the project document that was deleted

  - `type: "claude_project_document_deleted"`

    Constant string confirming deletion.

    - `"claude_project_document_deleted"`

# Artifacts

## Get artifact metadata

**get** `/v1/compliance/apps/artifacts/{artifact_version_id}`

Returns metadata for an artifact version, without the content body.

Use the sibling `/content` endpoint to fetch the artifact text. The
`md5` and `size_bytes` fields here are computed over the UTF-8
encoding of that text, so a DLP consumer can dedupe or match hashes
without downloading every artifact.

### Path Parameters

- `artifact_version_id: string`

  The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Artifact ID e.g. 'claude_artifact_abc123'

- `artifact_type: string or null`

  MIME-like artifact type e.g. 'application/vnd.ant.code'

- `claude_chat_id: string`

  The chat this artifact belongs to

- `created_at: string`

  Artifact version creation timestamp

- `md5: string`

  Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

- `size_bytes: number`

  Size in bytes of the artifact content (UTF-8 encoded)

- `title: string or null`

  Artifact title

- `version_id: string`

  Artifact version ID e.g. 'claude_artifact_version_abc123'

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Download artifact content

**get** `/v1/compliance/apps/artifacts/{artifact_version_id}/content`

Download the content of an artifact version for compliance purposes.

Returns the full text content of the artifact version.

### Path Parameters

- `artifact_version_id: string`

  The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID/content \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Domain Types

### Artifact Retrieve Response

- `ArtifactRetrieveResponse object { id, artifact_type, claude_chat_id, 5 more }`

  Artifact version metadata for GET /v1/compliance/apps/artifacts/{artifact_version_id}.

  Returns metadata only. Use the sibling `/content` endpoint to fetch the
  artifact body.

  - `id: string`

    Artifact ID e.g. 'claude_artifact_abc123'

  - `artifact_type: string or null`

    MIME-like artifact type e.g. 'application/vnd.ant.code'

  - `claude_chat_id: string`

    The chat this artifact belongs to

  - `created_at: string`

    Artifact version creation timestamp

  - `md5: string`

    Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

  - `size_bytes: number`

    Size in bytes of the artifact content (UTF-8 encoded)

  - `title: string or null`

    Artifact title

  - `version_id: string`

    Artifact version ID e.g. 'claude_artifact_version_abc123'

# Sessions

# Local

## List local sessions

**get** `/v1/compliance/apps/sessions/local`

List local sessions across the organizations the key may read.

Results are ordered by `created_at` descending. Pagination is
forward-only via `next_page`; there is no reverse cursor.

### Query Parameters

- `created_at: optional object { gte, lt }`

  - `gte: optional string`

    Only return sessions whose first inference call is at or after this time (RFC 3339; a UTC offset is required).

  - `lt: optional string`

    Only return sessions whose first inference call is strictly before this time (RFC 3339; a UTC offset is required).

- `limit: optional number`

  Maximum results (default: 100, max: 500)

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, created_at, organization_uuid, 4 more }`

  Page of local sessions, ordered by `created_at` descending; ties are broken by a fixed server-side order.

  - `id: string`

    Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

  - `created_at: string`

    Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

  - `organization_uuid: string`

    UUID of the child organization the session belongs to

  - `product_surface: string or null`

    The product the session ran in: `cowork` for Cowork sessions in Claude Desktop, or `claude_code` for Claude Code sessions. New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

  - `type: "compliance_local_session"`

    - `"compliance_local_session"`

  - `user: object { id, email_address }`

    The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

    - `id: string`

      User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

    - `email_address: string or null`

      User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

  - `workspace_id: string or null`

    Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

- `next_page: string or null`

  Opaque pagination cursor (prefixed `page_`) for the next page. Null when there is no further page. Treat as an opaque string; the format may change without notice.

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/sessions/local \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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
      "created_at": "2026-07-09T14:02:11Z"
    }
  ]
}
```

## Retrieve a local session

**get** `/v1/compliance/apps/sessions/local/{local_session_id}`

Retrieve one local session.

The response is the same session object the list endpoint returns,
with `user.email_address` resolved the same way. Retention is
enforced when the response is served: a session whose every
inference call has aged out returns 404.

### Path Parameters

- `local_session_id: string`

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

- `created_at: string`

  Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

- `organization_uuid: string`

  UUID of the child organization the session belongs to

- `product_surface: string or null`

  The product the session ran in: `cowork` for Cowork sessions in Claude Desktop, or `claude_code` for Claude Code sessions. New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

- `type: "compliance_local_session"`

  - `"compliance_local_session"`

- `user: object { id, email_address }`

  The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

  - `id: string`

    User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

  - `email_address: string or null`

    User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

- `workspace_id: string or null`

  Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/sessions/local/$LOCAL_SESSION_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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
  "created_at": "2026-07-09T14:02:11Z"
}
```

## Domain Types

### Local List Response

- `LocalListResponse object { id, created_at, organization_uuid, 4 more }`

  A Cowork or Claude Code session that a user ran on their own computer
  while signed in with their organization account.

  - `id: string`

    Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

  - `created_at: string`

    Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

  - `organization_uuid: string`

    UUID of the child organization the session belongs to

  - `product_surface: string or null`

    The product the session ran in: `cowork` for Cowork sessions in Claude Desktop, or `claude_code` for Claude Code sessions. New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

  - `type: "compliance_local_session"`

    - `"compliance_local_session"`

  - `user: object { id, email_address }`

    The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

    - `id: string`

      User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

    - `email_address: string or null`

      User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

  - `workspace_id: string or null`

    Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

### Local Retrieve Response

- `LocalRetrieveResponse object { id, created_at, organization_uuid, 4 more }`

  A Cowork or Claude Code session that a user ran on their own computer
  while signed in with their organization account.

  - `id: string`

    Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

  - `created_at: string`

    Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

  - `organization_uuid: string`

    UUID of the child organization the session belongs to

  - `product_surface: string or null`

    The product the session ran in: `cowork` for Cowork sessions in Claude Desktop, or `claude_code` for Claude Code sessions. New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

  - `type: "compliance_local_session"`

    - `"compliance_local_session"`

  - `user: object { id, email_address }`

    The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

    - `id: string`

      User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

    - `email_address: string or null`

      User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

  - `workspace_id: string or null`

    Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

# Messages

## Retrieve local session messages

**get** `/v1/compliance/apps/sessions/local/{local_session_id}/messages`

Read one local session's transcript, oldest-first by default.

Retention is enforced read-side: turns at or before the child
organization's retention boundary are never returned; a session
that straddles the boundary carries one leading
`content_unavailable` placeholder (`reason: "retention_elapsed"`)
in their place. The boundary is pinned on the walk's first page and
honored for 24 hours: a cursor older than that is rejected with an
explicit 400; restart the walk to read under the current boundary.

### Path Parameters

- `local_session_id: string`

### Query Parameters

- `limit: optional number`

  Maximum results (default: 100, max: 1000)

- `order: optional "asc" or "desc"`

  Sort direction. `asc` (oldest-first, default) or `desc`.

  - `"asc"`

  - `"desc"`

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `tool_result_max_bytes: optional number`

  Truncate each text item inside a tool result to at most this many bytes (cut on a code-point boundary). Pass `-1` to request the server maximum (approximately 1 MiB); larger values are clamped to it. `0` is not a valid value.

- `tool_use_input_max_bytes: optional number`

  Truncate each tool-use input to at most this many bytes (cut on a code-point boundary so the result is valid UTF-8). Pass `-1` to request the server maximum (approximately 1 MiB); larger values are clamped to it. `0` is not a valid value.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, content, created_at, 3 more }`

  Transcript turns for this page, ordered by `created_at` in the direction selected by the `order` parameter (ascending by default). Turns sharing a `created_at` (all messages of one inference call carry the call's timestamp) are returned in transcript order.

  - `id: string`

    Message identifier, prefixed `clsm_`. Stable for as long as the message's turn is retained: identifiers of retained turns do not change as older turns age out of the organization's retention period. The `retention_elapsed` placeholder's identifier is distinct from every retained turn's and changes only when further turns age out.

  - `content: array of object { text, truncated, type }  or object { id, input, name, 2 more }  or object { content, is_error, name, 3 more }`

    Content blocks within the message, discriminated on `type` (`text` / `tool_use` / `tool_result`: the same discriminator values as the claude.ai chat-messages endpoint; the tool variants omit `integration_name` and `mcp_server_url`, and `text` carries `truncated`). Extended-thinking content is never included. The request's `system` field is never included; a presence-only marker message is emitted when it was set. The request's `tools[]` definitions are never included as transcript messages. Project-level instructions (such as CLAUDE.md files) appear in the message stream as a user-role context block and are included. Empty when `provenance.type` is `content_unavailable`.

    - `Text object { text, truncated, type }`

      Text content block.

      - `text: string`

        Text content from the user or the assistant

      - `truncated: boolean`

        True when `text` was shortened by the server's fixed per-string bound (approximately 1 MiB), or when ancillary content the block carried (such as citations) was omitted, or when this block stands in for a non-text block whose content is not shown, or when it is an explanatory marker the server inserted (its text enclosed in square brackets, e.g. prefacing client-asserted history). There is no request parameter that raises the per-string bound.

      - `type: "text"`

        - `"text"`

    - `ToolUse object { id, input, name, 2 more }`

      Tool invocation requested by the assistant.

      - `id: string or null`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened (see the `truncated` field); a truncated value is cut mid-document and is not valid JSON.

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request the server maximum.

      - `type: "tool_use"`

        - `"tool_use"`

    - `ToolResult object { content, is_error, name, 3 more }`

      Result returned by a tool invocation.

      - `content: array of object { text, type }`

        Text content returned by the tool. Non-text item types are omitted and signalled via `truncated` with an in-band item-count marker.

        - `text: string`

          Text returned by the tool

        - `type: "text"`

          - `"text"`

      - `is_error: boolean`

        True when the tool reported an error

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string or null`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened or non-text items were omitted. Pass `tool_result_max_bytes=-1` to request the server maximum.

      - `type: "tool_result"`

        - `"tool_result"`

  - `created_at: string`

    When the message was recorded (RFC 3339, UTC)

  - `provenance: object { reason, type }  or object { type }  or object { type }  or null`

    Where this turn's content came from, discriminated on `type`. Null (the common case) means verified content: on an assistant message, content Claude produced during this session; on a user message, content the user sent. `content_unavailable`: the turn's content cannot be returned and `content` is empty; `reason` says why. `client_asserted`: assistant content the client supplied as conversation history; `content` shows what the model received but its authorship is not verified; never on user-role messages. `synthetic_marker`: a transcript marker the endpoint generated rather than content either party sent during the session. Both `client_asserted` and `synthetic_marker` can result from normal request or client processing, not only client modification. Callers should tolerate unrecognized `type` values.

    - `ContentUnavailable object { reason, type }`

      The turn's content cannot be returned; `content` is empty.

      - `reason: string`

        Why this turn's content cannot be returned, e.g. `not_captured` (the content was not captured for compliance retrieval), `cmek_key_revoked` (the content is encrypted under the organization's customer-managed key and that key is unavailable), `retention_elapsed` (the content lies past the organization's retention boundary; on the placeholder standing in for every pre-boundary turn), or `oversize` (the message exceeds the server's per-message size bound even after per-block truncation). Callers should tolerate unrecognized values. `not_captured` is not proof that no record was stored: content withheld by the storage layer's fail-closed access policies carries the same reason and is deliberately indistinguishable from content that was never captured.

      - `type: "content_unavailable"`

        - `"content_unavailable"`

    - `ClientAsserted object { type }`

      Assistant content the client supplied as conversation history
      rather than produced by Claude during this session. `content` shows
      what the model received but its authorship is not verified; this can
      result from normal request or client processing, not only client
      modification. Never on user-role messages.

      - `type: "client_asserted"`

        - `"client_asserted"`

    - `SyntheticMarker object { type }`

      A transcript marker generated by the endpoint rather than sent by
      either party during the session. Marker messages indicate that the
      prompt history diverged from what was captured, that the request's
      `system` field was present but is not shown, or that
      prompt-carried history was suppressed because the session spans the
      child organization's retention boundary and those turns cannot be
      placed against it (the marker's text names the cause). Markers that
      report a mismatch with captured history can result from normal request
      or client processing, not only client modification.

      - `type: "synthetic_marker"`

        - `"synthetic_marker"`

  - `role: "assistant" or "user"`

    Message sender (`user` or `assistant`)

    - `"assistant"`

    - `"user"`

  - `type: "compliance_local_session_message"`

    - `"compliance_local_session_message"`

- `next_page: string or null`

  Opaque pagination cursor (prefixed `page_`) for the next page. Null when there is no further page. Treat as an opaque string; the format may change without notice.

- `session: object { id, created_at, organization_uuid, 4 more }`

  The local session the messages belong to. `user.email_address` is always null on this endpoint; the messages endpoint does not resolve email addresses.

  - `id: string`

    Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.

  - `created_at: string`

    Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

  - `organization_uuid: string`

    UUID of the child organization the session belongs to

  - `product_surface: string or null`

    The product the session ran in: `cowork` for Cowork sessions in Claude Desktop, or `claude_code` for Claude Code sessions. New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.

  - `type: "compliance_local_session"`

    - `"compliance_local_session"`

  - `user: object { id, email_address }`

    The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

    - `id: string`

      User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

    - `email_address: string or null`

      User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

  - `workspace_id: string or null`

    Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/sessions/local/$LOCAL_SESSION_ID/messages \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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
    "type": "compliance_local_session",
    "user": {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "email_address": "jane.doe@example.com"
    },
    "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR"
  }
}
```

## Domain Types

### Message List Response

- `MessageListResponse object { id, content, created_at, 3 more }`

  A single user or assistant turn in a local session transcript.

  - `id: string`

    Message identifier, prefixed `clsm_`. Stable for as long as the message's turn is retained: identifiers of retained turns do not change as older turns age out of the organization's retention period. The `retention_elapsed` placeholder's identifier is distinct from every retained turn's and changes only when further turns age out.

  - `content: array of object { text, truncated, type }  or object { id, input, name, 2 more }  or object { content, is_error, name, 3 more }`

    Content blocks within the message, discriminated on `type` (`text` / `tool_use` / `tool_result`: the same discriminator values as the claude.ai chat-messages endpoint; the tool variants omit `integration_name` and `mcp_server_url`, and `text` carries `truncated`). Extended-thinking content is never included. The request's `system` field is never included; a presence-only marker message is emitted when it was set. The request's `tools[]` definitions are never included as transcript messages. Project-level instructions (such as CLAUDE.md files) appear in the message stream as a user-role context block and are included. Empty when `provenance.type` is `content_unavailable`.

    - `Text object { text, truncated, type }`

      Text content block.

      - `text: string`

        Text content from the user or the assistant

      - `truncated: boolean`

        True when `text` was shortened by the server's fixed per-string bound (approximately 1 MiB), or when ancillary content the block carried (such as citations) was omitted, or when this block stands in for a non-text block whose content is not shown, or when it is an explanatory marker the server inserted (its text enclosed in square brackets, e.g. prefacing client-asserted history). There is no request parameter that raises the per-string bound.

      - `type: "text"`

        - `"text"`

    - `ToolUse object { id, input, name, 2 more }`

      Tool invocation requested by the assistant.

      - `id: string or null`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened (see the `truncated` field); a truncated value is cut mid-document and is not valid JSON.

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request the server maximum.

      - `type: "tool_use"`

        - `"tool_use"`

    - `ToolResult object { content, is_error, name, 3 more }`

      Result returned by a tool invocation.

      - `content: array of object { text, type }`

        Text content returned by the tool. Non-text item types are omitted and signalled via `truncated` with an in-band item-count marker.

        - `text: string`

          Text returned by the tool

        - `type: "text"`

          - `"text"`

      - `is_error: boolean`

        True when the tool reported an error

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string or null`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened or non-text items were omitted. Pass `tool_result_max_bytes=-1` to request the server maximum.

      - `type: "tool_result"`

        - `"tool_result"`

  - `created_at: string`

    When the message was recorded (RFC 3339, UTC)

  - `provenance: object { reason, type }  or object { type }  or object { type }  or null`

    Where this turn's content came from, discriminated on `type`. Null (the common case) means verified content: on an assistant message, content Claude produced during this session; on a user message, content the user sent. `content_unavailable`: the turn's content cannot be returned and `content` is empty; `reason` says why. `client_asserted`: assistant content the client supplied as conversation history; `content` shows what the model received but its authorship is not verified; never on user-role messages. `synthetic_marker`: a transcript marker the endpoint generated rather than content either party sent during the session. Both `client_asserted` and `synthetic_marker` can result from normal request or client processing, not only client modification. Callers should tolerate unrecognized `type` values.

    - `ContentUnavailable object { reason, type }`

      The turn's content cannot be returned; `content` is empty.

      - `reason: string`

        Why this turn's content cannot be returned, e.g. `not_captured` (the content was not captured for compliance retrieval), `cmek_key_revoked` (the content is encrypted under the organization's customer-managed key and that key is unavailable), `retention_elapsed` (the content lies past the organization's retention boundary; on the placeholder standing in for every pre-boundary turn), or `oversize` (the message exceeds the server's per-message size bound even after per-block truncation). Callers should tolerate unrecognized values. `not_captured` is not proof that no record was stored: content withheld by the storage layer's fail-closed access policies carries the same reason and is deliberately indistinguishable from content that was never captured.

      - `type: "content_unavailable"`

        - `"content_unavailable"`

    - `ClientAsserted object { type }`

      Assistant content the client supplied as conversation history
      rather than produced by Claude during this session. `content` shows
      what the model received but its authorship is not verified; this can
      result from normal request or client processing, not only client
      modification. Never on user-role messages.

      - `type: "client_asserted"`

        - `"client_asserted"`

    - `SyntheticMarker object { type }`

      A transcript marker generated by the endpoint rather than sent by
      either party during the session. Marker messages indicate that the
      prompt history diverged from what was captured, that the request's
      `system` field was present but is not shown, or that
      prompt-carried history was suppressed because the session spans the
      child organization's retention boundary and those turns cannot be
      placed against it (the marker's text names the cause). Markers that
      report a mismatch with captured history can result from normal request
      or client processing, not only client modification.

      - `type: "synthetic_marker"`

        - `"synthetic_marker"`

  - `role: "assistant" or "user"`

    Message sender (`user` or `assistant`)

    - `"assistant"`

    - `"user"`

  - `type: "compliance_local_session_message"`

    - `"compliance_local_session_message"`

# Remote

## List remote sessions

**get** `/v1/compliance/apps/sessions/remote`

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

### Query Parameters

- `created_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Filter remote sessions created after this time (RFC 3339 format)

  - `gte: optional string`

    Filter remote sessions created at or after this time (RFC 3339 format)

  - `lt: optional string`

    Filter remote sessions created before this time (RFC 3339 format)

  - `lte: optional string`

    Filter remote sessions created at or before this time (RFC 3339 format)

- `limit: optional number`

  Maximum results (default: 100, max: 500)

- `organization_ids: optional array of string`

  Filter to specific child organization identifiers. Omit to enumerate every child organization the key may read.

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `user_ids: optional array of string`

  Filter to sessions owned by specific users (max 10 per request). Agent-owned sessions are excluded when this filter is set.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, agent_id, claude_project_id, 7 more }`

  - `id: string`

    Remote session identifier

  - `agent_id: string or null`

    Identifier of the automated agent that owns the session. Null for user-owned sessions. At most one of `user` and `agent_id` is set.

  - `claude_project_id: string or null`

    ID of the project the session is bound to. Null when the session has no project binding.

  - `created_at: string`

    When the session was created (RFC 3339, UTC)

  - `organization_uuid: string`

    UUID of the organization the session belongs to

  - `product_surface: string or null`

    The Claude product the session was created from. Currently `cowork_remote`, for Cowork sessions started on claude.ai web or mobile. More values will appear as other surfaces launch, so treat any unrecognized value as an unclassified surface rather than an error. Null for sessions created before this field was recorded, for surfaces that do not stamp it, and for unrecognized tag values.

  - `started_by_user: object { id, email_address }  or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

  - `status: string`

    Session lifecycle state. One of `active`, `paused`, `archived`, or `failed` — the lifecycle states the owning product surface exposes — plus `pending`, a brief transient state that resolves before any transcript content exists. The list endpoint includes `pending`; the messages endpoint returns 404 for it. Deleted sessions are not returned on either endpoint. Treat unrecognized values as an unknown state rather than an error.

  - `updated_at: string`

    When the session was last modified (RFC 3339, UTC)

  - `user: object { id, email_address }  or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

- `next_page: string or null`

  Opaque page token; pass as `page` to retrieve the next page. Null when no rows exist after this page. Treat this value as opaque; do not parse or store it long-term, as the format may change without notice.

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/sessions/remote \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Domain Types

### Remote List Response

- `RemoteListResponse object { id, agent_id, claude_project_id, 7 more }`

  Metadata for one remote session, as returned in the list response
  and in the messages response's `session` field.

  Carries session attributes only, not transcript content. Use the
  messages endpoint to retrieve a session's transcript.

  - `id: string`

    Remote session identifier

  - `agent_id: string or null`

    Identifier of the automated agent that owns the session. Null for user-owned sessions. At most one of `user` and `agent_id` is set.

  - `claude_project_id: string or null`

    ID of the project the session is bound to. Null when the session has no project binding.

  - `created_at: string`

    When the session was created (RFC 3339, UTC)

  - `organization_uuid: string`

    UUID of the organization the session belongs to

  - `product_surface: string or null`

    The Claude product the session was created from. Currently `cowork_remote`, for Cowork sessions started on claude.ai web or mobile. More values will appear as other surfaces launch, so treat any unrecognized value as an unclassified surface rather than an error. Null for sessions created before this field was recorded, for surfaces that do not stamp it, and for unrecognized tag values.

  - `started_by_user: object { id, email_address }  or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

  - `status: string`

    Session lifecycle state. One of `active`, `paused`, `archived`, or `failed` — the lifecycle states the owning product surface exposes — plus `pending`, a brief transient state that resolves before any transcript content exists. The list endpoint includes `pending`; the messages endpoint returns 404 for it. Deleted sessions are not returned on either endpoint. Treat unrecognized values as an unknown state rather than an error.

  - `updated_at: string`

    When the session was last modified (RFC 3339, UTC)

  - `user: object { id, email_address }  or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

# Messages

## Retrieve remote session messages

**get** `/v1/compliance/apps/sessions/remote/{claude_remote_session_id}/messages`

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

### Path Parameters

- `claude_remote_session_id: string`

  The remote session identifier (`cse_...`) to retrieve

### Query Parameters

- `limit: optional number`

  Maximum results (default: 100, max: 1000)

- `order: optional "asc" or "desc"`

  Sort direction. `asc` (oldest-first) or `desc`.

  - `"asc"`

  - `"desc"`

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `tool_result_max_bytes: optional number`

  Truncate each text item inside a tool result to at most this many bytes (cut on a code-point boundary). Pass `-1` to request the server maximum. `0` is not a valid value.

- `tool_use_input_max_bytes: optional number`

  Truncate each tool-use input to at most this many bytes (cut on a code-point boundary so the result is valid UTF-8). Pass `-1` to request the server maximum. `0` is not a valid value.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, content, content_unavailable, 3 more }`

  Transcript turns for this page, ordered by transcript position. `created_at` is a commit timestamp and may tie or invert under concurrent writes; do not re-sort by it.

  - `id: string`

    Unique identifier for the message, e.g. `csev_abc123`

  - `content: array of object { text, truncated, type }  or object { id, input, name, 2 more }  or object { content, is_error, name, 3 more }`

    Content blocks within the message

    - `Text object { text, truncated, type }`

      Text content block.

      - `text: string`

        Text content from the user or the assistant

      - `truncated: boolean`

        True when `text` exceeded the server-defined maximum (approximately 1 MiB) and was shortened.

      - `type: "text"`

        - `"text"`

    - `ToolUse object { id, input, name, 2 more }`

      Tool invocation requested by the assistant.

      - `id: string or null`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request full content, subject to the server-side maximum.

      - `type: "tool_use"`

        - `"tool_use"`

    - `ToolResult object { content, is_error, name, 3 more }`

      Result returned by a tool invocation.

      - `content: array of object { text, type }`

        Text content returned by the tool. Non-text item types are omitted.

        - `text: string`

          Text returned by the tool

        - `type: "text"`

          - `"text"`

      - `is_error: boolean`

        True when the tool reported an error

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string or null`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened. Pass `tool_result_max_bytes=-1` to request full content, subject to the server-side maximum.

      - `type: "tool_result"`

        - `"tool_result"`

  - `content_unavailable: boolean`

    True when the stored content could not be returned — it could not be decrypted, or it exceeded the server's per-event size bound. `content` is empty in that case; this distinguishes 'no content' from 'content withheld'.

  - `created_at: string`

    When the message was recorded (RFC 3339, UTC)

  - `role: "assistant" or "user"`

    Message sender (`user` or `assistant`)

    - `"assistant"`

    - `"user"`

  - `sent_by_user_id: string or null`

    Identifier of the human account that sent this turn on an agent-owned session. Null on user-owned sessions, where every user-role turn was sent by the session's `user`.

- `next_page: string or null`

  Opaque page token; pass as `page` to retrieve the next page. Null when no rows exist after this page. Treat this value as opaque; do not parse or store it long-term, as the format may change without notice.

- `session: object { id, agent_id, claude_project_id, 7 more }`

  Session metadata. `started_by_user`, `user.email_address`, and `claude_project_id` are always null on this endpoint; the messages endpoint resolves neither email addresses nor project bindings.

  - `id: string`

    Remote session identifier

  - `agent_id: string or null`

    Identifier of the automated agent that owns the session. Null for user-owned sessions. At most one of `user` and `agent_id` is set.

  - `claude_project_id: string or null`

    ID of the project the session is bound to. Null when the session has no project binding.

  - `created_at: string`

    When the session was created (RFC 3339, UTC)

  - `organization_uuid: string`

    UUID of the organization the session belongs to

  - `product_surface: string or null`

    The Claude product the session was created from. Currently `cowork_remote`, for Cowork sessions started on claude.ai web or mobile. More values will appear as other surfaces launch, so treat any unrecognized value as an unclassified surface rather than an error. Null for sessions created before this field was recorded, for surfaces that do not stamp it, and for unrecognized tag values.

  - `started_by_user: object { id, email_address }  or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

  - `status: string`

    Session lifecycle state. One of `active`, `paused`, `archived`, or `failed` — the lifecycle states the owning product surface exposes — plus `pending`, a brief transient state that resolves before any transcript content exists. The list endpoint includes `pending`; the messages endpoint returns 404 for it. Deleted sessions are not returned on either endpoint. Treat unrecognized values as an unknown state rather than an error.

  - `updated_at: string`

    When the session was last modified (RFC 3339, UTC)

  - `user: object { id, email_address }  or null`

    A user associated with a remote session.

    - `id: string`

      User identifier

    - `email_address: string or null`

      User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/sessions/remote/$CLAUDE_REMOTE_SESSION_ID/messages \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

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

## Domain Types

### Message List Response

- `MessageListResponse object { id, content, content_unavailable, 3 more }`

  A single user or assistant turn in a remote session transcript.

  `content` is a discriminated union of `text`, `tool_use`, and
  `tool_result` blocks.

  - `id: string`

    Unique identifier for the message, e.g. `csev_abc123`

  - `content: array of object { text, truncated, type }  or object { id, input, name, 2 more }  or object { content, is_error, name, 3 more }`

    Content blocks within the message

    - `Text object { text, truncated, type }`

      Text content block.

      - `text: string`

        Text content from the user or the assistant

      - `truncated: boolean`

        True when `text` exceeded the server-defined maximum (approximately 1 MiB) and was shortened.

      - `type: "text"`

        - `"text"`

    - `ToolUse object { id, input, name, 2 more }`

      Tool invocation requested by the assistant.

      - `id: string or null`

        Tool-use ID, e.g. 'toolu_01AbC...'

      - `input: string`

        Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

      - `name: string`

        Name of the tool invoked

      - `truncated: boolean`

        True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request full content, subject to the server-side maximum.

      - `type: "tool_use"`

        - `"tool_use"`

    - `ToolResult object { content, is_error, name, 3 more }`

      Result returned by a tool invocation.

      - `content: array of object { text, type }`

        Text content returned by the tool. Non-text item types are omitted.

        - `text: string`

          Text returned by the tool

        - `type: "text"`

          - `"text"`

      - `is_error: boolean`

        True when the tool reported an error

      - `name: string`

        Name of the tool that produced this result

      - `tool_use_id: string or null`

        ID of the tool_use block this result responds to

      - `truncated: boolean`

        True when one or more text items in `content` were shortened. Pass `tool_result_max_bytes=-1` to request full content, subject to the server-side maximum.

      - `type: "tool_result"`

        - `"tool_result"`

  - `content_unavailable: boolean`

    True when the stored content could not be returned — it could not be decrypted, or it exceeded the server's per-event size bound. `content` is empty in that case; this distinguishes 'no content' from 'content withheld'.

  - `created_at: string`

    When the message was recorded (RFC 3339, UTC)

  - `role: "assistant" or "user"`

    Message sender (`user` or `assistant`)

    - `"assistant"`

    - `"user"`

  - `sent_by_user_id: string or null`

    Identifier of the human account that sent this turn on an agent-owned session. Null on user-owned sessions, where every user-role turn was sent by the session's `user`.

# Code

# Artifacts

## List Code Artifacts

**get** `/v1/compliance/apps/code/artifacts`

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

### Query Parameters

- `limit: optional number`

  Maximum results (default: 20, max: 100)

- `organization_ids: optional array of string`

  Filter by organization IDs (accepts `org_...` or organization UUID, up to 500). Enumerate IDs via `GET /v1/compliance/organizations`.

- `page: optional string`

  Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

- `updated_at: optional object { gt, gte, lt, lte }`

  - `gt: optional string`

    Return only Artifacts updated after this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.

  - `gte: optional string`

    Return only Artifacts updated at or after this time (RFC 3339 format). Time filters match an eventually-consistent index and Artifacts published before this field was recorded never match — omit the time filter for compliance-complete enumeration. For incremental export, apply a generous overlap margin between windows and dedupe by `id`: adjacent tiling silently misses items whose index update lagged their publish.

  - `lt: optional string`

    Return only Artifacts updated before this time (RFC 3339 format). Multiple time operators are AND-ed to the tightest bound. See `updated_at.gte` for the completeness caveat.

  - `lte: optional string`

    Return only Artifacts updated at or before this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.

- `user_ids: optional array of string`

  Filter by owner user IDs (up to 200). Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `data: array of object { id, organization_uuid, owner_user_id, 5 more }`

  Page of Artifacts

  - `id: string`

    Artifact identifier (tagged ID)

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

  - `user: object { id, email_address }  or null`

    The user who owns a Code Artifact.

    Fields that reference this type are null when the Artifact was
    published by an agent session rather than a user account, when the
    owner's account has been deleted, or when the owner is no longer a
    member of an organization the key may read.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

  - `versions: array of object { id, created_at, name }`

    Up to roughly 20 most-recently-published versions of this Artifact (older versions are not retained). Metadata only — use `GET /v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}` to download a version's content.

    - `id: string`

      Opaque version identifier

    - `created_at: string or null`

      When this version was published

    - `name: string`

      Artifact title at this version. Falls back to the version identifier when the title for an older version is no longer retained.

- `has_more: boolean`

  Whether `next_page` is set. May be true for a page whose next page is empty — continue until `next_page` is absent.

- `next_page: string or null`

  Token to retrieve the next page. Use this as the 'page' parameter in your next request

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "data": [
    {
      "id": "cart_01Tu9VwXyZaBcDeFgHiJkLmN",
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

## Download Code Artifact Version Content

**get** `/v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}`

Streams the content of one version of a Claude Code Artifact as the
response body.

Returns 404 for Artifacts that don't exist or belong to another parent
organization. A listed version id can start returning 404 if subsequent
publishes rotated it out of retained history — re-list on 404. Returns
503 while the version's content upload is
still in flight or was abandoned — retry with backoff. Oversized
encoded content aborts mid-stream: headers and initial bytes arrive
but the body terminates early — an aborted chunked transfer is the
only truncation signal for encoded content. `Content-MD5` is emitted
only for identity-stored content; validate against it when present.

### Path Parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

- `version_id: string`

  Opaque version identifier from the Artifact's `versions` list

### Header Parameters

- `"x-api-key": optional string`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID/versions/$VERSION_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

## Delete Code Artifact

**delete** `/v1/compliance/apps/code/artifacts/{artifact_id}`

Permanently deletes a Code Artifact and all its versions. This is a
destructive operation that cannot be undone. A 200 response means the
deletion is initiated and the Artifact is claimed; content removal
completes asynchronously.

Returns 404 for Artifacts that don't exist or belong to another parent
organization. Returns 404 on a repeated delete of an already-deleted
Artifact.

### Path Parameters

- `artifact_id: string`

  The Artifact ID (tagged ID, e.g., cart_abc123)

### Header Parameters

- `"x-api-key": optional string`

### Returns

- `id: string`

  The ID of the Artifact that was deleted

- `type: "code_artifact_deleted"`

  Constant string confirming deletion

  - `"code_artifact_deleted"`

### Example

```http
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID \
    -X DELETE \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

#### Response

```json
{
  "id": "cart_xyz789",
  "type": "code_artifact_deleted"
}
```

## Domain Types

### Artifact List Response

- `ArtifactListResponse object { id, organization_uuid, owner_user_id, 5 more }`

  A hosted site published via Claude Code.

  - `id: string`

    Artifact identifier (tagged ID)

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

  - `user: object { id, email_address }  or null`

    The user who owns a Code Artifact.

    Fields that reference this type are null when the Artifact was
    published by an agent session rather than a user account, when the
    owner's account has been deleted, or when the owner is no longer a
    member of an organization the key may read.

    - `id: string`

      User identifier (tagged ID)

    - `email_address: string`

      User's email address

  - `versions: array of object { id, created_at, name }`

    Up to roughly 20 most-recently-published versions of this Artifact (older versions are not retained). Metadata only — use `GET /v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}` to download a version's content.

    - `id: string`

      Opaque version identifier

    - `created_at: string or null`

      When this version was published

    - `name: string`

      Artifact title at this version. Falls back to the version identifier when the title for an older version is no longer retained.

### Artifact Delete Response

- `ArtifactDeleteResponse object { id, type }`

  Response for deleting a Code Artifact.

  - `id: string`

    The ID of the Artifact that was deleted

  - `type: "code_artifact_deleted"`

    Constant string confirming deletion

    - `"code_artifact_deleted"`
