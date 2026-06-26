<!-- source: https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe -->

# Use WIF with SPIFFE
Authenticate SPIFFE workloads to the Claude API using JWT-SVIDs from SPIRE or any other SPIFFE-conformant issuer.
[SPIFFE](https://spiffe.io/) is the CNCF standard for issuing identity to workloads. [SPIRE](https://spiffe.io/docs/latest/spire-about/) is its open-source reference implementation, and several commercial products also issue SPIFFE-conformant identities. Anthropic federates with any SPIFFE implementation that emits OIDC-compatible JWT-SVIDs. Federation works either through an OIDC discovery document at a public HTTPS URL (`discovery` mode; see the [URL constraints](https://platform.claude.com/docs/en/manage-claude/wif-reference#url-fields)) or by registering the JWKS directly (`inline` mode). The JWT-SVID spec defines `sub` as the workload's SPIFFE ID, and the SPIFFE Workload API requires the caller to supply `aud` at fetch time, so those claims are the same across implementations. Anthropic additionally requires `iss` and `iat`, neither of which the JWT-SVID spec mandates, so configure your implementation to populate both (in SPIRE, `iss` is the `jwt_issuer` server setting and `iat` is set automatically). With those in place, the [Configure Anthropic](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#configure-anthropic), [Acquire and use the token](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#acquire-and-use-the-token), and [Scope your rule](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#scope-your-rule) sections of this guide apply to any SPIFFE implementation. For a current list, see [Commercial software that implements SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/#commercial-software-that-implements-spiffe) on the SPIFFE project site.
SPIFFE assigns every workload a stable identity URI of the form `spiffe://<trust-domain>/<path>`, and SPIRE issues that identity as a JWT-SVID on demand through the Workload API. A JWT-SVID is an ordinary signed JWT whose `sub` claim is the workload's SPIFFE ID and whose `aud` claim is supplied by the workload at fetch time.
The bridge from a SPIRE trust domain to standard OIDC is the [SPIRE OIDC Discovery Provider](https://github.com/spiffe/spire/blob/main/support/oidc-discovery-provider/README.md), a standalone helper that publishes `/.well-known/openid-configuration` and a JWKS endpoint for the trust domain's JWT signing keys. With the discovery provider running, a JWT-SVID validates like any other OIDC token: register the discovery URL as a federation issuer, write a federation rule that matches the workload's SPIFFE ID, and have the workload present its JWT-SVID to Anthropic's token-exchange endpoint.
This page's examples use SPIRE and apply anywhere SPIRE Agent runs: Kubernetes pods, virtual machines, and bare-metal hosts.
If your Kubernetes cluster does not run SPIRE and you want to authenticate with the cluster's native projected service-account tokens instead, see [Use WIF with Kubernetes](https://platform.claude.com/docs/en/manage-claude/wif-providers/kubernetes).
Prerequisites
  * Familiarity with [WIF concepts](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#concepts): service accounts, federation issuers, and federation rules.
  * A SPIFFE deployment with workload identities issued (the examples on this page use SPIRE Server and Agent), and registration entries for the workloads that need to call the Claude API.
  * An OIDC discovery endpoint for the trust domain (in SPIRE, the [OIDC Discovery Provider](https://github.com/spiffe/spire/blob/main/support/oidc-discovery-provider/README.md)) running with a publicly reachable HTTPS endpoint, or the JWKS exported for `inline` registration.
  * Your SPIFFE issuer configured to set the `iss` claim on JWT-SVIDs to the value you will register as the federation issuer's `issuer_url`. For `discovery` mode, this is the discovery endpoint's public URL (in SPIRE, the `jwt_issuer` server setting).
  * JWT-SVIDs available to your workloads. WIF accepts JWT-SVIDs only; X.509-SVIDs are not used.
  * Permission to create service accounts, federation issuers, and federation rules in the Claude Console for your Anthropic organization.

The audience value to request when fetching a JWT-SVID is always `https://api.anthropic.com`. Use this value in spiffe-helper's `jwt_audience`, the Workload API `FetchJWTSVID` call, and the federation rule's `audience` matcher.
Configure SPIRE
The instructions in this section are SPIRE-specific. If you use a different SPIFFE issuer, configure its OIDC discovery endpoint and JWT-SVID retrieval according to its own documentation, then continue at [Configure Anthropic](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#configure-anthropic).
If you already run SPIRE with the OIDC Discovery Provider, federating with Anthropic requires three things on the SPIRE side: a `jwt_issuer` that matches the discovery URL, a registration entry for the workload that will call the Claude API, and a way for that workload to fetch a JWT-SVID with the Anthropic audience. The following subsections walk through each. The configuration snippets show only the settings relevant to Anthropic federation; they are not complete SPIRE deployment configs.

Setting up SPIRE for the first time? Deploy SPIRE Server and Agent following the [SPIRE quickstart](https://spiffe.io/docs/latest/try/), then add the [OIDC Discovery Provider](https://github.com/spiffe/spire/blob/main/support/oidc-discovery-provider/README.md) as a separate service alongside SPIRE Server. Discovery-mode federation depends on the provider being deployed and publicly reachable; it is not part of a default SPIRE install.
### 
Verify the JWT issuer
Anthropic validates a JWT-SVID by matching its `iss` claim against a registered federation issuer and fetching the JWKS from that issuer's discovery document. Two SPIRE settings must agree on the same URL: SPIRE Server's `jwt_issuer` (which becomes the `iss` claim in every minted JWT-SVID) and the OIDC Discovery Provider's `domains` list (which determines the host the discovery document and JWKS are served from). That shared URL is what you register with Anthropic.
The trust domain and the issuer URL are independent. The trust domain (`spiffe://prod.example.com`) scopes the `sub` claim; the issuer URL (`https://oidc-discovery.prod.example.com`) is where Anthropic fetches signing keys. They do not need to share a hostname.
Confirm `jwt_issuer` is set in SPIRE Server's configuration and points at the discovery provider's public URL. The following example also shows a default JWT-SVID lifetime; SPIRE's built-in default is 5 minutes, which is short enough that continuous rotation is required (see [Run spiffe-helper](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#run-spiffe-helper)). Anthropic's token-exchange endpoint rejects any identity token whose lifetime exceeds the federation issuer's configured maximum (1 hour by default; see [Validation rules](https://platform.claude.com/docs/en/manage-claude/wif-reference#validation-rules)). This check applies to every SPIFFE implementation, not just SPIRE, so keep `default_jwt_svid_ttl` (or any per-entry override) at or below that maximum.
server.conf

server {
    trust_domain         = "prod.example.com"
    jwt_issuer           = "https://oidc-discovery.prod.example.com"
    default_jwt_svid_ttl = "5m"
    # ...

In the OIDC Discovery Provider's configuration, the same hostname must appear under `domains`, and the provider must be able to reach SPIRE Server's API socket. The provider serves the discovery document and JWKS over HTTPS; terminate TLS with its built-in ACME support or front it with a load balancer that does.
oidc-discovery-provider.conf

domains = ["oidc-discovery.prod.example.com"]

server_api {
    address = "unix:///run/spire/sockets/private/api.sock"

acme {
    email        = "platform@example.com"
    tos_accepted = true

The example uses `server_api`, which connects the discovery provider to SPIRE Server's privileged API socket. The provider also accepts a `workload_api` block (with `socket_path` and `trust_domain`) that obtains the bundle through a SPIRE Agent's Workload API instead; use it when the discovery provider should not have access to the Server API or runs on a node that cannot reach the Server. On Windows, the `address` field is Unix-only; supply the Server API pipe name by using `server_api { experimental { named_pipe_name = "\\spire-server\\private\\api" } }` instead.
### 
Register the workload
Each workload that calls the Claude API needs a SPIRE registration entry that maps its runtime selectors to a SPIFFE ID. If the workload is already registered, note its SPIFFE ID; you use it in the federation rule's `subject_prefix`. If not, register it. For a Kubernetes pod, the selectors are typically the namespace and Kubernetes service account:
CLI

spire-server entry create \
    -spiffeID spiffe://prod.example.com/ns/inference/sa/worker \
    -parentID spiffe://prod.example.com/spire/agent/k8s_psat/prod-cluster/NODE_UID \
    -selector k8s:ns:inference \
    -selector k8s:sa:worker

The `parentID` shown is a single node's auto-generated agent ID. For cluster-wide registration, parent the entry to a [node alias](https://spiffe.io/docs/latest/deploying/registering/#mapping-workloads-to-multiple-nodes) so it matches workloads on every node, as the [SPIRE Kubernetes quickstart](https://spiffe.io/docs/latest/try/getting-started-k8s/) does.
Workloads outside Kubernetes use host-level selectors such as `unix:uid:1000` (`unix:path` is also available but requires `discover_workload_path = true` in the agent's unix workload attestor configuration). Clusters running [spire-controller-manager](https://github.com/spiffe/spire-controller-manager) can declare entries with the `ClusterSPIFFEID` custom resource instead of calling `spire-server entry create` directly.
### 
Run spiffe-helper
[spiffe-helper](https://github.com/spiffe/spiffe-helper) is a sidecar utility that connects to the SPIRE Agent socket, fetches a JWT-SVID for a given audience, writes it to a file, and re-fetches it before expiry. The helper runs in daemon mode by default; the following example sets `daemon_mode = true` explicitly.
helper.conf

agent_address = "/run/spire/sockets/agent.sock"
cert_dir      = "/var/run/secrets/anthropic.com"
daemon_mode   = true

jwt_svids = [{
    jwt_audience       = "https://api.anthropic.com"
    jwt_svid_file_name = "token"
}]

In Kubernetes, run spiffe-helper as a sidecar container that shares a memory-backed `emptyDir` volume (`medium: Memory`) with your application container so the bearer SVID never lands on the node's disk. Mount the SPIRE Agent socket from the host into the sidecar, mount the shared volume at `/var/run/secrets/anthropic.com` in both containers, and set `ANTHROPIC_IDENTITY_TOKEN_FILE=/var/run/secrets/anthropic.com/token` on the application container. On VMs and bare metal, run spiffe-helper as a system service alongside the workload and point both at a shared directory.
Configure Anthropic
In the Claude Console, open **Settings → Workload identity** , click **Connect workload** , and select **Custom OIDC**. The wizard walks you through registering the issuer, creating a service account, and creating a federation rule.
The wizard creates these resources for you. Use the following values whether you enter them in the wizard or send them to the [Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api):
**Federation issuer:** Register the OIDC Discovery Provider's public URL in `discovery` mode. Anthropic fetches `/.well-known/openid-configuration` from this URL and follows the returned `jwks_uri` to retrieve the trust domain's signing keys.

  "name": "spire-prod",
  "issuer_url": "https://oidc-discovery.prod.example.com",
  "jwks": { "type": "discovery" }

If the discovery provider is not reachable from the public internet, fetch the JWKS yourself (`curl https://oidc-discovery.prod.example.com/keys`) and register the issuer with `"jwks": {"type": "inline", "keys": [...]}` using the contents of the returned `keys` array. In `inline` mode the `issuer_url` is only compared against the JWT-SVID's `iss` claim; Anthropic never attempts to reach it.

SPIRE rotates JWT signing keys frequently, by default on the same cadence as the CA (`ca_ttl`, 24 hours). If you register the issuer with an inline JWKS instead of a discovery URL, you must update the JWKS every time SPIRE rotates: add the new key before workloads start presenting it, and **remove superseded keys** once tokens signed with them have expired. Stale keys left in an inline JWKS remain trusted indefinitely.
To automate JWKS updates without exposing a public discovery endpoint, configure a SPIRE Server [BundlePublisher](https://spiffe.io/docs/latest/deploying/spire_server/#built-in-plugins) plugin (`aws_s3`, `gcp_cloudstorage`, or `k8s_configmap`) with `format = "jwks"` to push the JWT signing keys to external storage on every rotation, then sync that into the issuer's inline keys.
**Federation rule:** Match the JWT-SVID's `sub` (the SPIFFE ID) and the `aud` you configured spiffe-helper to request. SPIFFE IDs are URI strings and `subject_prefix` matches them as opaque text, so an exact value or a trailing-`*` prefix match both work against them. For more complex patterns, use a CEL `condition`.

  "name": "spire-inference-worker",
  "issuer_id": "fdis_...",
  "match": {
    "subject_prefix": "spiffe://prod.example.com/ns/inference/sa/worker",
    "audience": "https://api.anthropic.com"
  "target": {
    "type": "service_account",
    "service_account_id": "svac_..."
  "workspace_id": "wrkspc_...",
  "oauth_scope": "workspace:developer",
  "token_lifetime_seconds": 600

Be as specific as the workload allows. Loosen `subject_prefix` to `spiffe://prod.example.com/ns/inference/*` only if every workload registered under that path should map to the same Anthropic service account. Add the rule's `fdrl_...` ID to the workload's `ANTHROPIC_FEDERATION_RULE_ID` environment variable.
Acquire and use the token
The Anthropic SDKs can either read the JWT-SVID from the file that spiffe-helper maintains or call the SPIFFE Workload API directly through a token-provider callable. The file path is the simplest integration and works in every SDK language; the callable path removes the sidecar but requires a SPIFFE Workload API client in your application's language.
File-based with spiffe-helper
File-based with spiffe-helper
Callable through the SPIFFE Workload API
Callable through the SPIFFE Workload API
With spiffe-helper writing a fresh JWT-SVID to `/var/run/secrets/anthropic.com/token`, set `ANTHROPIC_IDENTITY_TOKEN_FILE` to that path along with `ANTHROPIC_FEDERATION_RULE_ID`, `ANTHROPIC_ORGANIZATION_ID`, `ANTHROPIC_SERVICE_ACCOUNT_ID`, and `ANTHROPIC_WORKSPACE_ID`. The SDK reads the file on every token exchange, so it always picks up the most recently rotated SVID, and refreshes the Anthropic access token automatically before it expires.
cURLPythonTypeScriptGoJavaC#CLIPHPRuby

import anthropic

# Reads the JWT-SVID that spiffe-helper writes to
# ANTHROPIC_IDENTITY_TOKEN_FILE, plus ANTHROPIC_FEDERATION_RULE_ID,
# ANTHROPIC_ORGANIZATION_ID, ANTHROPIC_SERVICE_ACCOUNT_ID, and ANTHROPIC_WORKSPACE_ID.
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message.content[0].text)

Verify the setup
Before wiring the SDK in, fetch a JWT-SVID directly from SPIRE Agent and confirm the claims match what your federation rule expects. If you use a different SPIFFE implementation, fetch a JWT-SVID with its CLI or Workload API client and decode the payload the same way.
The Workload API attests the calling process. For a Kubernetes registration entry, run this command inside a pod that satisfies the entry's selectors and has the agent socket mounted (for example, by using `kubectl exec`). On VMs and bare metal, run it as the user or process that matches the entry's `unix:` selectors. Running from an unattested host shell returns `no identity issued`, which is the most common verify-step failure.
CLI

spire-agent api fetch jwt \
    -audience https://api.anthropic.com \
    -socketPath /run/spire/sockets/agent.sock \
    -output json \
  | jq -r '.[0].svids[0].svid' \
  | jq -rR 'split(".")[1] | gsub("-";"+") | gsub("_";"/") | @base64d | fromjson'

The `-output json` flag returns the SVID response and bundle response as a two-element JSON array, so `jq -r '.[0].svids[0].svid'` extracts the bare token. On older SPIRE versions without `-output`, the command prints a labeled block instead; in that case pipe the default output through `awk '/^[[:space:]]*eyJ/{print $1; exit}'` to extract the token line. Check that `iss` is the OIDC Discovery Provider URL you registered, `sub` is the workload's SPIFFE ID, and `aud` contains `https://api.anthropic.com`. Then run the cURL example from [Acquire and use the token](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#acquire-and-use-the-token); a successful exchange returns an `access_token` beginning with `sk-ant-oat01-`. On `400 invalid_grant`, see [Troubleshoot a failed exchange](https://platform.claude.com/docs/en/manage-claude/wif-reference#troubleshoot-a-failed-exchange); the most common SPIRE-side cause is a mismatch between SPIRE Server's `jwt_issuer` and the URL registered as the federation issuer.
Scope your rule
SPIFFE ID path conventions are operator-defined, so the federation rule's `subject_prefix` matcher should reflect the path scheme your registration entries use. Common schemes include `spiffe://<trust-domain>/ns/<namespace>/sa/<service-account>` (the default emitted by the `ClusterSPIFFEID` resource in spire-controller-manager) and `spiffe://<trust-domain>/host/<hostname>/<service>` for VM and bare-metal workloads.

A `subject_prefix` of `spiffe://prod.example.com/*` matches every workload in the trust domain. Without an `audience` matcher, the rule also accepts JWT-SVIDs minted for any audience, including ones the workload requested for unrelated relying parties.
Lock the rule's `match` block to the narrowest scope that fits your use case:
  * **Pin to one workload:** Set `subject_prefix` to the full SPIFFE ID with no trailing `*`.
  * **Always set an audience:** Require `audience` on the rule and configure spiffe-helper (or the Workload API call) with the same value so SVIDs minted for other relying parties are rejected.
  * **Scope by path segment:** Use `spiffe://prod.example.com/ns/inference/*` to grant every workload registered under a namespace, and create a separate rule and Anthropic service account per namespace rather than widening one rule.
  * **One issuer per trust domain:** Each SPIRE trust domain has its own signing keys and OIDC Discovery Provider. Register each as a separate federation issuer and bind rules to the issuer that owns the SPIFFE IDs they match.

Next steps
  * [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation): concepts, the token-exchange flow, and SDK configuration options.
  * [WIF reference](https://platform.claude.com/docs/en/manage-claude/wif-reference): environment variables, JWKS source modes, and rule match modes.
  * [Use WIF with Kubernetes](https://platform.claude.com/docs/en/manage-claude/wif-providers/kubernetes): for clusters that use native projected service-account tokens instead of SPIRE.

  * [Prerequisites](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#prerequisites)
  * [Configure SPIRE](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#configure-spire)
  * [Verify the JWT issuer](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#verify-the-jwt-issuer)
  * [Register the workload](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#register-the-workload)
  * [Run spiffe-helper](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#run-spiffe-helper)
  * [Configure Anthropic](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#configure-anthropic)
  * [Acquire and use the token](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#acquire-and-use-the-token)
  * [Verify the setup](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#verify-the-setup)
  * [Scope your rule](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#scope-your-rule)
  * [Next steps](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#next-steps)

Admin/Identity providers
# Use WIF with SPIFFE
Authenticate SPIFFE workloads to the Claude API using JWT-SVIDs from SPIRE or any other SPIFFE-conformant issuer.
[SPIFFE](https://spiffe.io/) is the CNCF standard for issuing identity to workloads. [SPIRE](https://spiffe.io/docs/latest/spire-about/) is its open-source reference implementation, and several commercial products also issue SPIFFE-conformant identities. Anthropic federates with any SPIFFE implementation that emits OIDC-compatible JWT-SVIDs. Federation works either through an OIDC discovery document at a public HTTPS URL (`discovery` mode; see the [URL constraints](https://platform.claude.com/docs/en/manage-claude/wif-reference#url-fields)) or by registering the JWKS directly (`inline` mode). The JWT-SVID spec defines `sub` as the workload's SPIFFE ID, and the SPIFFE Workload API requires the caller to supply `aud` at fetch time, so those claims are the same across implementations. Anthropic additionally requires `iss` and `iat`, neither of which the JWT-SVID spec mandates, so configure your implementation to populate both (in SPIRE, `iss` is the `jwt_issuer` server setting and `iat` is set automatically). With those in place, the [Configure Anthropic](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#configure-anthropic), [Acquire and use the token](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#acquire-and-use-the-token), and [Scope your rule](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#scope-your-rule) sections of this guide apply to any SPIFFE implementation. For a current list, see [Commercial software that implements SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/#commercial-software-that-implements-spiffe) on the SPIFFE project site.
SPIFFE assigns every workload a stable identity URI of the form `spiffe://<trust-domain>/<path>`, and SPIRE issues that identity as a JWT-SVID on demand through the Workload API. A JWT-SVID is an ordinary signed JWT whose `sub` claim is the workload's SPIFFE ID and whose `aud` claim is supplied by the workload at fetch time.
The bridge from a SPIRE trust domain to standard OIDC is the [SPIRE OIDC Discovery Provider](https://github.com/spiffe/spire/blob/main/support/oidc-discovery-provider/README.md), a standalone helper that publishes `/.well-known/openid-configuration` and a JWKS endpoint for the trust domain's JWT signing keys. With the discovery provider running, a JWT-SVID validates like any other OIDC token: register the discovery URL as a federation issuer, write a federation rule that matches the workload's SPIFFE ID, and have the workload present its JWT-SVID to Anthropic's token-exchange endpoint.
This page's examples use SPIRE and apply anywhere SPIRE Agent runs: Kubernetes pods, virtual machines, and bare-metal hosts.
If your Kubernetes cluster does not run SPIRE and you want to authenticate with the cluster's native projected service-account tokens instead, see [Use WIF with Kubernetes](https://platform.claude.com/docs/en/manage-claude/wif-providers/kubernetes).
Prerequisites
  * Familiarity with [WIF concepts](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#concepts): service accounts, federation issuers, and federation rules.
  * A SPIFFE deployment with workload identities issued (the examples on this page use SPIRE Server and Agent), and registration entries for the workloads that need to call the Claude API.
  * An OIDC discovery endpoint for the trust domain (in SPIRE, the [OIDC Discovery Provider](https://github.com/spiffe/spire/blob/main/support/oidc-discovery-provider/README.md)) running with a publicly reachable HTTPS endpoint, or the JWKS exported for `inline` registration.
  * Your SPIFFE issuer configured to set the `iss` claim on JWT-SVIDs to the value you will register as the federation issuer's `issuer_url`. For `discovery` mode, this is the discovery endpoint's public URL (in SPIRE, the `jwt_issuer` server setting).
  * JWT-SVIDs available to your workloads. WIF accepts JWT-SVIDs only; X.509-SVIDs are not used.
  * Permission to create service accounts, federation issuers, and federation rules in the Claude Console for your Anthropic organization.

The audience value to request when fetching a JWT-SVID is always `https://api.anthropic.com`. Use this value in spiffe-helper's `jwt_audience`, the Workload API `FetchJWTSVID` call, and the federation rule's `audience` matcher.
Configure SPIRE
The instructions in this section are SPIRE-specific. If you use a different SPIFFE issuer, configure its OIDC discovery endpoint and JWT-SVID retrieval according to its own documentation, then continue at [Configure Anthropic](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#configure-anthropic).
If you already run SPIRE with the OIDC Discovery Provider, federating with Anthropic requires three things on the SPIRE side: a `jwt_issuer` that matches the discovery URL, a registration entry for the workload that will call the Claude API, and a way for that workload to fetch a JWT-SVID with the Anthropic audience. The following subsections walk through each. The configuration snippets show only the settings relevant to Anthropic federation; they are not complete SPIRE deployment configs.

Setting up SPIRE for the first time? Deploy SPIRE Server and Agent following the [SPIRE quickstart](https://spiffe.io/docs/latest/try/), then add the [OIDC Discovery Provider](https://github.com/spiffe/spire/blob/main/support/oidc-discovery-provider/README.md) as a separate service alongside SPIRE Server. Discovery-mode federation depends on the provider being deployed and publicly reachable; it is not part of a default SPIRE install.
### 
Verify the JWT issuer
Anthropic validates a JWT-SVID by matching its `iss` claim against a registered federation issuer and fetching the JWKS from that issuer's discovery document. Two SPIRE settings must agree on the same URL: SPIRE Server's `jwt_issuer` (which becomes the `iss` claim in every minted JWT-SVID) and the OIDC Discovery Provider's `domains` list (which determines the host the discovery document and JWKS are served from). That shared URL is what you register with Anthropic.
The trust domain and the issuer URL are independent. The trust domain (`spiffe://prod.example.com`) scopes the `sub` claim; the issuer URL (`https://oidc-discovery.prod.example.com`) is where Anthropic fetches signing keys. They do not need to share a hostname.
Confirm `jwt_issuer` is set in SPIRE Server's configuration and points at the discovery provider's public URL. The following example also shows a default JWT-SVID lifetime; SPIRE's built-in default is 5 minutes, which is short enough that continuous rotation is required (see [Run spiffe-helper](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#run-spiffe-helper)). Anthropic's token-exchange endpoint rejects any identity token whose lifetime exceeds the federation issuer's configured maximum (1 hour by default; see [Validation rules](https://platform.claude.com/docs/en/manage-claude/wif-reference#validation-rules)). This check applies to every SPIFFE implementation, not just SPIRE, so keep `default_jwt_svid_ttl` (or any per-entry override) at or below that maximum.
server.conf

server {
    trust_domain         = "prod.example.com"
    jwt_issuer           = "https://oidc-discovery.prod.example.com"
    default_jwt_svid_ttl = "5m"
    # ...

In the OIDC Discovery Provider's configuration, the same hostname must appear under `domains`, and the provider must be able to reach SPIRE Server's API socket. The provider serves the discovery document and JWKS over HTTPS; terminate TLS with its built-in ACME support or front it with a load balancer that does.
oidc-discovery-provider.conf

domains = ["oidc-discovery.prod.example.com"]

server_api {
    address = "unix:///run/spire/sockets/private/api.sock"

acme {
    email        = "platform@example.com"
    tos_accepted = true

The example uses `server_api`, which connects the discovery provider to SPIRE Server's privileged API socket. The provider also accepts a `workload_api` block (with `socket_path` and `trust_domain`) that obtains the bundle through a SPIRE Agent's Workload API instead; use it when the discovery provider should not have access to the Server API or runs on a node that cannot reach the Server. On Windows, the `address` field is Unix-only; supply the Server API pipe name by using `server_api { experimental { named_pipe_name = "\\spire-server\\private\\api" } }` instead.
### 
Register the workload
Each workload that calls the Claude API needs a SPIRE registration entry that maps its runtime selectors to a SPIFFE ID. If the workload is already registered, note its SPIFFE ID; you use it in the federation rule's `subject_prefix`. If not, register it. For a Kubernetes pod, the selectors are typically the namespace and Kubernetes service account:
CLI

spire-server entry create \
    -spiffeID spiffe://prod.example.com/ns/inference/sa/worker \
    -parentID spiffe://prod.example.com/spire/agent/k8s_psat/prod-cluster/NODE_UID \
    -selector k8s:ns:inference \
    -selector k8s:sa:worker

The `parentID` shown is a single node's auto-generated agent ID. For cluster-wide registration, parent the entry to a [node alias](https://spiffe.io/docs/latest/deploying/registering/#mapping-workloads-to-multiple-nodes) so it matches workloads on every node, as the [SPIRE Kubernetes quickstart](https://spiffe.io/docs/latest/try/getting-started-k8s/) does.
Workloads outside Kubernetes use host-level selectors such as `unix:uid:1000` (`unix:path` is also available but requires `discover_workload_path = true` in the agent's unix workload attestor configuration). Clusters running [spire-controller-manager](https://github.com/spiffe/spire-controller-manager) can declare entries with the `ClusterSPIFFEID` custom resource instead of calling `spire-server entry create` directly.
### 
Run spiffe-helper
[spiffe-helper](https://github.com/spiffe/spiffe-helper) is a sidecar utility that connects to the SPIRE Agent socket, fetches a JWT-SVID for a given audience, writes it to a file, and re-fetches it before expiry. The helper runs in daemon mode by default; the following example sets `daemon_mode = true` explicitly.
helper.conf

agent_address = "/run/spire/sockets/agent.sock"
cert_dir      = "/var/run/secrets/anthropic.com"
daemon_mode   = true

jwt_svids = [{
    jwt_audience       = "https://api.anthropic.com"
    jwt_svid_file_name = "token"
}]

In Kubernetes, run spiffe-helper as a sidecar container that shares a memory-backed `emptyDir` volume (`medium: Memory`) with your application container so the bearer SVID never lands on the node's disk. Mount the SPIRE Agent socket from the host into the sidecar, mount the shared volume at `/var/run/secrets/anthropic.com` in both containers, and set `ANTHROPIC_IDENTITY_TOKEN_FILE=/var/run/secrets/anthropic.com/token` on the application container. On VMs and bare metal, run spiffe-helper as a system service alongside the workload and point both at a shared directory.
Configure Anthropic
In the Claude Console, open **Settings → Workload identity** , click **Connect workload** , and select **Custom OIDC**. The wizard walks you through registering the issuer, creating a service account, and creating a federation rule.
The wizard creates these resources for you. Use the following values whether you enter them in the wizard or send them to the [Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api):
**Federation issuer:** Register the OIDC Discovery Provider's public URL in `discovery` mode. Anthropic fetches `/.well-known/openid-configuration` from this URL and follows the returned `jwks_uri` to retrieve the trust domain's signing keys.

  "name": "spire-prod",
  "issuer_url": "https://oidc-discovery.prod.example.com",
  "jwks": { "type": "discovery" }

If the discovery provider is not reachable from the public internet, fetch the JWKS yourself (`curl https://oidc-discovery.prod.example.com/keys`) and register the issuer with `"jwks": {"type": "inline", "keys": [...]}` using the contents of the returned `keys` array. In `inline` mode the `issuer_url` is only compared against the JWT-SVID's `iss` claim; Anthropic never attempts to reach it.

SPIRE rotates JWT signing keys frequently, by default on the same cadence as the CA (`ca_ttl`, 24 hours). If you register the issuer with an inline JWKS instead of a discovery URL, you must update the JWKS every time SPIRE rotates: add the new key before workloads start presenting it, and **remove superseded keys** once tokens signed with them have expired. Stale keys left in an inline JWKS remain trusted indefinitely.
To automate JWKS updates without exposing a public discovery endpoint, configure a SPIRE Server [BundlePublisher](https://spiffe.io/docs/latest/deploying/spire_server/#built-in-plugins) plugin (`aws_s3`, `gcp_cloudstorage`, or `k8s_configmap`) with `format = "jwks"` to push the JWT signing keys to external storage on every rotation, then sync that into the issuer's inline keys.
**Federation rule:** Match the JWT-SVID's `sub` (the SPIFFE ID) and the `aud` you configured spiffe-helper to request. SPIFFE IDs are URI strings and `subject_prefix` matches them as opaque text, so an exact value or a trailing-`*` prefix match both work against them. For more complex patterns, use a CEL `condition`.

  "name": "spire-inference-worker",
  "issuer_id": "fdis_...",
  "match": {
    "subject_prefix": "spiffe://prod.example.com/ns/inference/sa/worker",
    "audience": "https://api.anthropic.com"
  "target": {
    "type": "service_account",
    "service_account_id": "svac_..."
  "workspace_id": "wrkspc_...",
  "oauth_scope": "workspace:developer",
  "token_lifetime_seconds": 600

Be as specific as the workload allows. Loosen `subject_prefix` to `spiffe://prod.example.com/ns/inference/*` only if every workload registered under that path should map to the same Anthropic service account. Add the rule's `fdrl_...` ID to the workload's `ANTHROPIC_FEDERATION_RULE_ID` environment variable.
Acquire and use the token
The Anthropic SDKs can either read the JWT-SVID from the file that spiffe-helper maintains or call the SPIFFE Workload API directly through a token-provider callable. The file path is the simplest integration and works in every SDK language; the callable path removes the sidecar but requires a SPIFFE Workload API client in your application's language.
File-based with spiffe-helper
File-based with spiffe-helper
Callable through the SPIFFE Workload API
Callable through the SPIFFE Workload API
With spiffe-helper writing a fresh JWT-SVID to `/var/run/secrets/anthropic.com/token`, set `ANTHROPIC_IDENTITY_TOKEN_FILE` to that path along with `ANTHROPIC_FEDERATION_RULE_ID`, `ANTHROPIC_ORGANIZATION_ID`, `ANTHROPIC_SERVICE_ACCOUNT_ID`, and `ANTHROPIC_WORKSPACE_ID`. The SDK reads the file on every token exchange, so it always picks up the most recently rotated SVID, and refreshes the Anthropic access token automatically before it expires.
cURLPythonTypeScriptGoJavaC#CLIPHPRuby

import anthropic

# Reads the JWT-SVID that spiffe-helper writes to
# ANTHROPIC_IDENTITY_TOKEN_FILE, plus ANTHROPIC_FEDERATION_RULE_ID,
# ANTHROPIC_ORGANIZATION_ID, ANTHROPIC_SERVICE_ACCOUNT_ID, and ANTHROPIC_WORKSPACE_ID.
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message.content[0].text)

Verify the setup
Before wiring the SDK in, fetch a JWT-SVID directly from SPIRE Agent and confirm the claims match what your federation rule expects. If you use a different SPIFFE implementation, fetch a JWT-SVID with its CLI or Workload API client and decode the payload the same way.
The Workload API attests the calling process. For a Kubernetes registration entry, run this command inside a pod that satisfies the entry's selectors and has the agent socket mounted (for example, by using `kubectl exec`). On VMs and bare metal, run it as the user or process that matches the entry's `unix:` selectors. Running from an unattested host shell returns `no identity issued`, which is the most common verify-step failure.
CLI

spire-agent api fetch jwt \
    -audience https://api.anthropic.com \
    -socketPath /run/spire/sockets/agent.sock \
    -output json \
  | jq -r '.[0].svids[0].svid' \
  | jq -rR 'split(".")[1] | gsub("-";"+") | gsub("_";"/") | @base64d | fromjson'

The `-output json` flag returns the SVID response and bundle response as a two-element JSON array, so `jq -r '.[0].svids[0].svid'` extracts the bare token. On older SPIRE versions without `-output`, the command prints a labeled block instead; in that case pipe the default output through `awk '/^[[:space:]]*eyJ/{print $1; exit}'` to extract the token line. Check that `iss` is the OIDC Discovery Provider URL you registered, `sub` is the workload's SPIFFE ID, and `aud` contains `https://api.anthropic.com`. Then run the cURL example from [Acquire and use the token](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe#acquire-and-use-the-token); a successful exchange returns an `access_token` beginning with `sk-ant-oat01-`. On `400 invalid_grant`, see [Troubleshoot a failed exchange](https://platform.claude.com/docs/en/manage-claude/wif-reference#troubleshoot-a-failed-exchange); the most common SPIRE-side cause is a mismatch between SPIRE Server's `jwt_issuer` and the URL registered as the federation issuer.
Scope your rule
SPIFFE ID path conventions are operator-defined, so the federation rule's `subject_prefix` matcher should reflect the path scheme your registration entries use. Common schemes include `spiffe://<trust-domain>/ns/<namespace>/sa/<service-account>` (the default emitted by the `ClusterSPIFFEID` resource in spire-controller-manager) and `spiffe://<trust-domain>/host/<hostname>/<service>` for VM and bare-metal workloads.

A `subject_prefix` of `spiffe://prod.example.com/*` matches every workload in the trust domain. Without an `audience` matcher, the rule also accepts JWT-SVIDs minted for any audience, including ones the workload requested for unrelated relying parties.
Lock the rule's `match` block to the narrowest scope that fits your use case:
  * **Pin to one workload:** Set `subject_prefix` to the full SPIFFE ID with no trailing `*`.
  * **Always set an audience:** Require `audience` on the rule and configure spiffe-helper (or the Workload API call) with the same value so SVIDs minted for other relying parties are rejected.
  * **Scope by path segment:** Use `spiffe://prod.example.com/ns/inference/*` to grant every workload registered under a namespace, and create a separate rule and Anthropic service account per namespace rather than widening one rule.
  * **One issuer per trust domain:** Each SPIRE trust domain has its own signing keys and OIDC Discovery Provider. Register each as a separate federation issuer and bind rules to the issuer that owns the SPIFFE IDs they match.

Next steps
  * [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation): concepts, the token-exchange flow, and SDK configuration options.
  * [WIF reference](https://platform.claude.com/docs/en/manage-claude/wif-reference): environment variables, JWKS source modes, and rule match modes.
  * [Use WIF with Kubernetes](https://platform.claude.com/docs/en/manage-claude/wif-providers/kubernetes): for clusters that use native projected service-account tokens instead of SPIRE.
