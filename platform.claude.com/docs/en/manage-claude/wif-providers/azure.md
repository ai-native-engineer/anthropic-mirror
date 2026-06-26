<!-- source: https://platform.claude.com/docs/en/manage-claude/wif-providers/azure -->

# Use WIF with Microsoft Entra ID
Federate Azure managed identities and Entra Workload Identity with the Claude API so your Azure workloads can call Claude without static API keys.
Azure workloads authenticate to the Claude API by presenting a JSON Web Token (JWT) issued by Microsoft Entra ID, then exchanging it for a short-lived Anthropic access token. There are two common ways to obtain the Entra-issued token:
  * **Managed identity (VMs, App Service, Functions, Container Apps):** The workload calls the Azure Instance Metadata Service (IMDS) at `http://169.254.169.254/metadata/identity/oauth2/token` and receives a JWT for its assigned identity.
  * **Entra Workload Identity (AKS pods):** Kubernetes projects a service account token (signed by the AKS cluster's OIDC issuer) into the pod at the path in `AZURE_FEDERATED_TOKEN_FILE`. The workload exchanges that token at Entra for an Entra-issued access token.

In both cases the Entra-issued token you present to Anthropic carries a tenant-specific Entra issuer (the [Configure Anthropic](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure#configure-anthropic) step shows the exact URL to register) and the managed identity's object ID in the `sub` and `oid` claims. You register that issuer with Anthropic once, write a federation rule that matches the expected claims, and your workload exchanges its Entra token for an `sk-ant-oat01-...` access token at runtime.

AKS pods can alternatively skip the Entra exchange and present the Kubernetes-projected service account token to Anthropic directly. That path registers your AKS cluster's OIDC issuer with Anthropic instead of your Entra tenant. See [Kubernetes](https://platform.claude.com/docs/en/manage-claude/wif-providers/kubernetes) for that flow.
Prerequisites
  * Familiarity with [WIF concepts](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#concepts): service accounts, federation issuers, and federation rules.
  * An Azure subscription with permission to assign managed identities (or configure Entra Workload Identity on AKS).
  * Your Microsoft Entra tenant ID. Find it in the Azure portal under **Microsoft Entra ID → Overview → Tenant ID**.
  * Permission to create service accounts, federation issuers, and federation rules in the Claude Console for your Anthropic organization.

Configure Azure
Set up the identity that Microsoft Entra ID will issue tokens for. Choose the path that matches where your workload runs.
VM, App Service, Functions, Container Apps
VM, App Service, Functions, Container Apps
Entra Workload Identity (AKS)
Entra Workload Identity (AKS)
Enable a system-assigned or user-assigned managed identity on your Azure resource. In the Azure portal, open the resource, go to **Identity** , and turn on **System assigned** (or attach a user-assigned identity).
After the identity is created, note its **Object (principal) ID**. This GUID appears as both the `sub` and `oid` claims in the issued token, and your Anthropic federation rule will match on it. You can find it on the resource's **Identity** page, or under **Microsoft Entra ID → Enterprise applications** for user-assigned identities.
No further Azure-side configuration is required. The Azure Instance Metadata Service is reachable at `169.254.169.254` from inside the resource once the identity is attached.
### 
Token claims
An Entra-issued token for a managed identity carries these claims (v2 token shown; see the Note under [Configure Anthropic](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure#configure-anthropic) for how `iss` and `aud` differ in v1 tokens):

  "iss": "https://login.microsoftonline.com/<TENANT_ID>/v2.0",
  "sub": "9f8e7d6c-1a2b-3c4d-5e6f-...",
  "aud": "00000000-0000-0000-0000-000000000000",
  "oid": "9f8e7d6c-1a2b-3c4d-5e6f-...",
  "tid": "<TENANT_ID>",
  "azp": "<CLIENT_ID>",
  "exp": 1775527120

`sub` and `oid` are identical (the managed identity's object ID). `azp` is the application or client ID. The `aud` claim depends on the token version: v2 tokens carry your Entra application's client ID (a GUID); v1 tokens carry the requested resource identifier, which is whatever value you passed as `resource` when fetching the token (for example, `https://api.anthropic.com`). Match on `oid` to authorize one specific identity, or on `azp` to authorize any identity associated with an application registration. The `tid` claim repeats your tenant ID; matching on it is defense in depth, because the issuer URL already pins the tenant.
Configure Anthropic
In the Claude Console, open **Settings → Workload identity** , click **Connect workload** , and select the **Microsoft Entra ID** tile. The wizard walks you through registering the issuer, creating a service account, and creating a federation rule.
The wizard creates these resources for you. Use the following values whether you enter them in the wizard or send them to the [Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api):
**Federation issuer:** Entra publishes an OIDC discovery document at the per-tenant issuer URL, so use discovery mode. Each Microsoft Entra tenant you federate needs its own issuer record.

  "name": "azure-prod-tenant",
  "issuer_url": "https://login.microsoftonline.com/<TENANT_ID>/v2.0",
  "jwks": { "type": "discovery" }

The access-token `iss` might be `https://sts.windows.net/<TENANT_ID>/` (v1.0) instead, and the `aud` claim might carry the requested resource URL (`https://api.anthropic.com`) rather than a GUID. Which form a workload gets is set by the **resource** app registration's `api.requestedAccessTokenVersion`: the default (`null`) emits v1.0 tokens, so managed-identity tokens for a custom audience are v1.0 unless that registration sets `requestedAccessTokenVersion: 2`. Decode your managed-identity token (the Verify section later in this guide shows how), register whichever `iss` value it contains, and set the federation rule's `audience` to whichever `aud` value it contains. The two issuer URLs share the same JWKS, so discovery mode works for either.
**Federation rule:** Match on the managed identity's object ID and your tenant ID. For v2 tokens the `audience` value is your Entra application's client ID (a GUID); use the exact `aud` value from your decoded token.

  "name": "azure-inference-worker",
  "issuer_id": "fdis_...",
  "match": {
    "audience": "00000000-0000-0000-0000-000000000000",
    "claims": {
      "oid": "9f8e7d6c-1a2b-3c4d-5e6f-...",
      "tid": "<TENANT_ID>"
  "target": {
    "type": "service_account",
    "service_account_id": "svac_..."
  "workspace_id": "wrkspc_...",
  "oauth_scope": "workspace:developer",
  "token_lifetime_seconds": 600

Acquire and use the token
At runtime your workload fetches its Entra token, exchanges it at `POST /v1/oauth/token`, and uses the returned bearer token to call Claude. Each Anthropic SDK handles the exchange and refresh loop when you supply a token-provider callable, as shown in the following examples. The cURL tab shows the raw flow.
cURLPythonTypeScriptGoJavaC#PHPRubyCLI

import os

import anthropic
import requests
from anthropic import WorkloadIdentityCredentials

IMDS_URL = "http://169.254.169.254/metadata/identity/oauth2/token"

def fetch_entra_token() -> str:
    """Fetch a managed identity token from Azure IMDS."""
    response = requests.get(
        IMDS_URL,
        headers={"Metadata": "true"},
        params={"api-version": "2018-02-01", "resource": "https://api.anthropic.com"},
        timeout=5,
    )
    response.raise_for_status()
    return response.json()["access_token"]

client = anthropic.Anthropic(
    credentials=WorkloadIdentityCredentials(
        identity_token_provider=fetch_entra_token,
        federation_rule_id=os.environ["ANTHROPIC_FEDERATION_RULE_ID"],
        organization_id=os.environ["ANTHROPIC_ORGANIZATION_ID"],
        service_account_id=os.environ["ANTHROPIC_SERVICE_ACCOUNT_ID"],
        workspace_id=os.environ.get("ANTHROPIC_WORKSPACE_ID"),
    ),
)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello from Azure"}],
)
print(message.content[0].text)

### 
On AKS with Entra Workload Identity
On AKS, the file at `AZURE_FEDERATED_TOKEN_FILE` is a Kubernetes-projected service account token signed by your cluster's OIDC issuer, not an Entra-issued token. To stay on the Entra-mediated path described on this page, exchange that token at `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token` (federated `client_credentials` grant) first, then pass the resulting Entra access token to the Anthropic SDK as the identity token.
cURLPythonTypeScriptGoJavaC#PHPRubyCLI

import os
from pathlib import Path
import httpx
import anthropic
from anthropic import WorkloadIdentityCredentials

def fetch_entra_token_via_federation() -> str:
    federated_token = Path(os.environ["AZURE_FEDERATED_TOKEN_FILE"]).read_text()
    response = httpx.post(
        f"https://login.microsoftonline.com/{os.environ['AZURE_TENANT_ID']}/oauth2/v2.0/token",
        data={
            "client_id": os.environ["AZURE_CLIENT_ID"],
            "grant_type": "client_credentials",
            "scope": "https://api.anthropic.com/.default",
            "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            "client_assertion": federated_token,
    )
    response.raise_for_status()
    return response.json()["access_token"]

client = anthropic.Anthropic(
    credentials=WorkloadIdentityCredentials(
        identity_token_provider=fetch_entra_token_via_federation,
        federation_rule_id=os.environ["ANTHROPIC_FEDERATION_RULE_ID"],
        organization_id=os.environ["ANTHROPIC_ORGANIZATION_ID"],
        service_account_id=os.environ["ANTHROPIC_SERVICE_ACCOUNT_ID"],
        workspace_id=os.environ.get("ANTHROPIC_WORKSPACE_ID"),
    ),
)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello from Azure"}],
)
print(message.content[0].text)

Alternatively, register your AKS cluster's OIDC issuer with Anthropic directly and skip the Entra hop. See [Kubernetes](https://platform.claude.com/docs/en/manage-claude/wif-providers/kubernetes) for that pattern.
Verify the setup
From your Azure resource, run the cURL exchange shown earlier and confirm that `POST /v1/oauth/token` returns a `200` with an `access_token` beginning with `sk-ant-oat01-` and an `expires_in` value in seconds. On `400 invalid_grant`, see [Troubleshoot a failed exchange](https://platform.claude.com/docs/en/manage-claude/wif-reference#troubleshoot-a-failed-exchange); the most common Azure-side cause is a mismatch between the `issuer_url` you registered and the `iss` claim in your decoded token. They must match exactly. For managed-identity tokens the `iss` value is either `https://login.microsoftonline.com/<TENANT_ID>/v2.0` or `https://sts.windows.net/<TENANT_ID>/`.
Scope your rule

The `oid` claim is a managed identity's GUID and has no stable prefix. A `subject_prefix` with `*` matches arbitrary identities in the tenant, so any workload that holds a managed identity could obtain a federated Anthropic token.
Lock the rule's `match` block to the narrowest scope that fits your use case:
  * **Match`oid` as an exact value:** Set `claims.oid` to the managed identity's full object ID and never use `subject_prefix` for Entra tokens.
  * **Pin`tid` as defense in depth:** The issuer URL already pins your tenant, but adding `claims.tid` guards against configuration drift if the issuer record is later edited.
  * **Pin the audience:** Set `audience` to the exact `aud` value from your decoded token so tokens minted for other applications are rejected.
  * **Use a separate rule per managed identity:** Create one rule per identity rather than one rule that authorizes several, so you can revoke a single workload's access without affecting others.

Next steps
  * Review the full configuration model in [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation).
  * See the [provider guides](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#identity-providers) for AWS, Google Cloud, GitHub Actions, and Kubernetes.
  * For environment variables, profile files, and credential precedence, see the [WIF reference](https://platform.claude.com/docs/en/manage-claude/wif-reference).

  * [Prerequisites](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure#prerequisites)
  * [Configure Azure](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure#configure-azure)
  * [Token claims](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure#token-claims)
  * [Configure Anthropic](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure#configure-anthropic)
  * [Acquire and use the token](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure#acquire-and-use-the-token)
  * [On AKS with Entra Workload Identity](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure#on-aks-with-entra-workload-identity)
  * [Verify the setup](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure#verify-the-setup)
  * [Scope your rule](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure#scope-your-rule)
  * [Next steps](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure#next-steps)

Admin/Identity providers
# Use WIF with Microsoft Entra ID
Federate Azure managed identities and Entra Workload Identity with the Claude API so your Azure workloads can call Claude without static API keys.
Azure workloads authenticate to the Claude API by presenting a JSON Web Token (JWT) issued by Microsoft Entra ID, then exchanging it for a short-lived Anthropic access token. There are two common ways to obtain the Entra-issued token:
  * **Managed identity (VMs, App Service, Functions, Container Apps):** The workload calls the Azure Instance Metadata Service (IMDS) at `http://169.254.169.254/metadata/identity/oauth2/token` and receives a JWT for its assigned identity.
  * **Entra Workload Identity (AKS pods):** Kubernetes projects a service account token (signed by the AKS cluster's OIDC issuer) into the pod at the path in `AZURE_FEDERATED_TOKEN_FILE`. The workload exchanges that token at Entra for an Entra-issued access token.

In both cases the Entra-issued token you present to Anthropic carries a tenant-specific Entra issuer (the [Configure Anthropic](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure#configure-anthropic) step shows the exact URL to register) and the managed identity's object ID in the `sub` and `oid` claims. You register that issuer with Anthropic once, write a federation rule that matches the expected claims, and your workload exchanges its Entra token for an `sk-ant-oat01-...` access token at runtime.

AKS pods can alternatively skip the Entra exchange and present the Kubernetes-projected service account token to Anthropic directly. That path registers your AKS cluster's OIDC issuer with Anthropic instead of your Entra tenant. See [Kubernetes](https://platform.claude.com/docs/en/manage-claude/wif-providers/kubernetes) for that flow.
Prerequisites
  * Familiarity with [WIF concepts](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#concepts): service accounts, federation issuers, and federation rules.
  * An Azure subscription with permission to assign managed identities (or configure Entra Workload Identity on AKS).
  * Your Microsoft Entra tenant ID. Find it in the Azure portal under **Microsoft Entra ID → Overview → Tenant ID**.
  * Permission to create service accounts, federation issuers, and federation rules in the Claude Console for your Anthropic organization.

Configure Azure
Set up the identity that Microsoft Entra ID will issue tokens for. Choose the path that matches where your workload runs.
VM, App Service, Functions, Container Apps
VM, App Service, Functions, Container Apps
Entra Workload Identity (AKS)
Entra Workload Identity (AKS)
Enable a system-assigned or user-assigned managed identity on your Azure resource. In the Azure portal, open the resource, go to **Identity** , and turn on **System assigned** (or attach a user-assigned identity).
After the identity is created, note its **Object (principal) ID**. This GUID appears as both the `sub` and `oid` claims in the issued token, and your Anthropic federation rule will match on it. You can find it on the resource's **Identity** page, or under **Microsoft Entra ID → Enterprise applications** for user-assigned identities.
No further Azure-side configuration is required. The Azure Instance Metadata Service is reachable at `169.254.169.254` from inside the resource once the identity is attached.
### 
Token claims
An Entra-issued token for a managed identity carries these claims (v2 token shown; see the Note under [Configure Anthropic](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure#configure-anthropic) for how `iss` and `aud` differ in v1 tokens):

  "iss": "https://login.microsoftonline.com/<TENANT_ID>/v2.0",
  "sub": "9f8e7d6c-1a2b-3c4d-5e6f-...",
  "aud": "00000000-0000-0000-0000-000000000000",
  "oid": "9f8e7d6c-1a2b-3c4d-5e6f-...",
  "tid": "<TENANT_ID>",
  "azp": "<CLIENT_ID>",
  "exp": 1775527120

`sub` and `oid` are identical (the managed identity's object ID). `azp` is the application or client ID. The `aud` claim depends on the token version: v2 tokens carry your Entra application's client ID (a GUID); v1 tokens carry the requested resource identifier, which is whatever value you passed as `resource` when fetching the token (for example, `https://api.anthropic.com`). Match on `oid` to authorize one specific identity, or on `azp` to authorize any identity associated with an application registration. The `tid` claim repeats your tenant ID; matching on it is defense in depth, because the issuer URL already pins the tenant.
Configure Anthropic
In the Claude Console, open **Settings → Workload identity** , click **Connect workload** , and select the **Microsoft Entra ID** tile. The wizard walks you through registering the issuer, creating a service account, and creating a federation rule.
The wizard creates these resources for you. Use the following values whether you enter them in the wizard or send them to the [Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api):
**Federation issuer:** Entra publishes an OIDC discovery document at the per-tenant issuer URL, so use discovery mode. Each Microsoft Entra tenant you federate needs its own issuer record.

  "name": "azure-prod-tenant",
  "issuer_url": "https://login.microsoftonline.com/<TENANT_ID>/v2.0",
  "jwks": { "type": "discovery" }

The access-token `iss` might be `https://sts.windows.net/<TENANT_ID>/` (v1.0) instead, and the `aud` claim might carry the requested resource URL (`https://api.anthropic.com`) rather than a GUID. Which form a workload gets is set by the **resource** app registration's `api.requestedAccessTokenVersion`: the default (`null`) emits v1.0 tokens, so managed-identity tokens for a custom audience are v1.0 unless that registration sets `requestedAccessTokenVersion: 2`. Decode your managed-identity token (the Verify section later in this guide shows how), register whichever `iss` value it contains, and set the federation rule's `audience` to whichever `aud` value it contains. The two issuer URLs share the same JWKS, so discovery mode works for either.
**Federation rule:** Match on the managed identity's object ID and your tenant ID. For v2 tokens the `audience` value is your Entra application's client ID (a GUID); use the exact `aud` value from your decoded token.

  "name": "azure-inference-worker",
  "issuer_id": "fdis_...",
  "match": {
    "audience": "00000000-0000-0000-0000-000000000000",
    "claims": {
      "oid": "9f8e7d6c-1a2b-3c4d-5e6f-...",
      "tid": "<TENANT_ID>"
  "target": {
    "type": "service_account",
    "service_account_id": "svac_..."
  "workspace_id": "wrkspc_...",
  "oauth_scope": "workspace:developer",
  "token_lifetime_seconds": 600

Acquire and use the token
At runtime your workload fetches its Entra token, exchanges it at `POST /v1/oauth/token`, and uses the returned bearer token to call Claude. Each Anthropic SDK handles the exchange and refresh loop when you supply a token-provider callable, as shown in the following examples. The cURL tab shows the raw flow.
cURLPythonTypeScriptGoJavaC#PHPRubyCLI

import os

import anthropic
import requests
from anthropic import WorkloadIdentityCredentials

IMDS_URL = "http://169.254.169.254/metadata/identity/oauth2/token"

def fetch_entra_token() -> str:
    """Fetch a managed identity token from Azure IMDS."""
    response = requests.get(
        IMDS_URL,
        headers={"Metadata": "true"},
        params={"api-version": "2018-02-01", "resource": "https://api.anthropic.com"},
        timeout=5,
    )
    response.raise_for_status()
    return response.json()["access_token"]

client = anthropic.Anthropic(
    credentials=WorkloadIdentityCredentials(
        identity_token_provider=fetch_entra_token,
        federation_rule_id=os.environ["ANTHROPIC_FEDERATION_RULE_ID"],
        organization_id=os.environ["ANTHROPIC_ORGANIZATION_ID"],
        service_account_id=os.environ["ANTHROPIC_SERVICE_ACCOUNT_ID"],
        workspace_id=os.environ.get("ANTHROPIC_WORKSPACE_ID"),
    ),
)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello from Azure"}],
)
print(message.content[0].text)

### 
On AKS with Entra Workload Identity
On AKS, the file at `AZURE_FEDERATED_TOKEN_FILE` is a Kubernetes-projected service account token signed by your cluster's OIDC issuer, not an Entra-issued token. To stay on the Entra-mediated path described on this page, exchange that token at `https://login.microsoftonline.com/<TENANT_ID>/oauth2/v2.0/token` (federated `client_credentials` grant) first, then pass the resulting Entra access token to the Anthropic SDK as the identity token.
cURLPythonTypeScriptGoJavaC#PHPRubyCLI

import os
from pathlib import Path
import httpx
import anthropic
from anthropic import WorkloadIdentityCredentials

def fetch_entra_token_via_federation() -> str:
    federated_token = Path(os.environ["AZURE_FEDERATED_TOKEN_FILE"]).read_text()
    response = httpx.post(
        f"https://login.microsoftonline.com/{os.environ['AZURE_TENANT_ID']}/oauth2/v2.0/token",
        data={
            "client_id": os.environ["AZURE_CLIENT_ID"],
            "grant_type": "client_credentials",
            "scope": "https://api.anthropic.com/.default",
            "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            "client_assertion": federated_token,
    )
    response.raise_for_status()
    return response.json()["access_token"]

client = anthropic.Anthropic(
    credentials=WorkloadIdentityCredentials(
        identity_token_provider=fetch_entra_token_via_federation,
        federation_rule_id=os.environ["ANTHROPIC_FEDERATION_RULE_ID"],
        organization_id=os.environ["ANTHROPIC_ORGANIZATION_ID"],
        service_account_id=os.environ["ANTHROPIC_SERVICE_ACCOUNT_ID"],
        workspace_id=os.environ.get("ANTHROPIC_WORKSPACE_ID"),
    ),
)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello from Azure"}],
)
print(message.content[0].text)

Alternatively, register your AKS cluster's OIDC issuer with Anthropic directly and skip the Entra hop. See [Kubernetes](https://platform.claude.com/docs/en/manage-claude/wif-providers/kubernetes) for that pattern.
Verify the setup
From your Azure resource, run the cURL exchange shown earlier and confirm that `POST /v1/oauth/token` returns a `200` with an `access_token` beginning with `sk-ant-oat01-` and an `expires_in` value in seconds. On `400 invalid_grant`, see [Troubleshoot a failed exchange](https://platform.claude.com/docs/en/manage-claude/wif-reference#troubleshoot-a-failed-exchange); the most common Azure-side cause is a mismatch between the `issuer_url` you registered and the `iss` claim in your decoded token. They must match exactly. For managed-identity tokens the `iss` value is either `https://login.microsoftonline.com/<TENANT_ID>/v2.0` or `https://sts.windows.net/<TENANT_ID>/`.
Scope your rule

The `oid` claim is a managed identity's GUID and has no stable prefix. A `subject_prefix` with `*` matches arbitrary identities in the tenant, so any workload that holds a managed identity could obtain a federated Anthropic token.
Lock the rule's `match` block to the narrowest scope that fits your use case:
  * **Match`oid` as an exact value:** Set `claims.oid` to the managed identity's full object ID and never use `subject_prefix` for Entra tokens.
  * **Pin`tid` as defense in depth:** The issuer URL already pins your tenant, but adding `claims.tid` guards against configuration drift if the issuer record is later edited.
  * **Pin the audience:** Set `audience` to the exact `aud` value from your decoded token so tokens minted for other applications are rejected.
  * **Use a separate rule per managed identity:** Create one rule per identity rather than one rule that authorizes several, so you can revoke a single workload's access without affecting others.

Next steps
  * Review the full configuration model in [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation).
  * See the [provider guides](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#identity-providers) for AWS, Google Cloud, GitHub Actions, and Kubernetes.
  * For environment variables, profile files, and credential precedence, see the [WIF reference](https://platform.claude.com/docs/en/manage-claude/wif-reference).
