<!-- source: https://platform.claude.com/docs/en/api/compliance/activities -->
<!-- part of: https://platform.claude.com/docs/en/api/compliance/activities -->

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
