<!-- source: https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm -->

# Deploy MCP tunnels with Helm
Install the tunnel stack on a Kubernetes cluster using the Anthropic Helm chart.
MCP tunnels are in research preview. [Request access](https://claude.com/form/claude-managed-agents) to try them.
The Anthropic Helm chart installs the [tunnel stack](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) as a single Deployment and attaches it to the tunnel you created in the [Console](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#create-a-tunnel).
Before you begin
You need:
  * **A tunnel created in the Console.** Complete [Create a tunnel](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#create-a-tunnel) first and record the tunnel ID (`tnl_...`). For manual provisioning you also need the tunnel token and tunnel domain from that step.
  * **A way for the chart to authenticate to the Tunnels API.**
    * **[Programmatic access](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#credential-provisioning) (recommended).** The [setup component](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) authenticates through Workload Identity Federation, fetches the tunnel token, generates a CA, registers it with Anthropic, and stores everything in a Secret. You'll need a federation rule scoped to `org:manage_tunnels`.
    * **[Manual](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#credential-provisioning).** Skip programmatic access. You'll [get the tunnel token from the Console](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#get-the-connection-details), generate a CA and server certificate yourself, [register the CA in the Console](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#add-a-ca-certificate), and supply the credentials to the cluster as Secrets.
  * **A Kubernetes cluster** you can deploy to with `helm` and `kubectl`. The **Without programmatic access** tab also uses `openssl` (1.1.1 or later).
  * **Outbound network connectivity** from the cluster to `api.anthropic.com` (443 TCP) and the [tunnel edge](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) (7844 TCP and UDP). See the full [network requirements](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview#network-requirements).
  * **One or more MCP servers** running and reachable from the cluster on the addresses you'll configure under `gateway.config.routes`. If you don't have one yet, [use the sample server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#optional-use-a-sample-mcp-server).

Optional: Use a sample MCP server
If you don't have an MCP server available for testing, use this minimal one:

kubectl create namespace mcp-tunnel --dry-run=client -o yaml | kubectl apply -f -
kubectl -n mcp-tunnel apply -f - <<'EOF'
apiVersion: v1
kind: ConfigMap
metadata:
  name: hello-mcp-src
data:
  hello_server.py: |
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("hello-server", host="0.0.0.0", port=9000)

    @mcp.tool()
    def hello(name: str = "world") -> str:
        """Say hello to someone."""
        return f"Hello, {name}!"

    if __name__ == "__main__":
        mcp.run(transport="streamable-http")
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-mcp
spec:
  replicas: 1
  selector:
    matchLabels: { app: hello-mcp }
  template:
    metadata:
      labels: { app: hello-mcp }
    spec:
      containers:
        - name: hello-mcp
          image: python:3.13-slim
          command: ["sh", "-c", "pip install --quiet mcp && python /app/hello_server.py"]
          volumeMounts:
            - { name: src, mountPath: /app }
          ports:
            - { containerPort: 9000 }
      volumes:
        - name: src
          configMap: { name: hello-mcp-src }
---
apiVersion: v1
kind: Service
metadata:
  name: hello-mcp
spec:
  selector: { app: hello-mcp }
  ports:
    - { port: 9000, targetPort: 9000 }
EOF

The Install steps that follow note where to add the corresponding route.
Install
With programmatic access
With programmatic access
Without programmatic access
Without programmatic access
The setup component exchanges the cluster's projected ServiceAccount token through your federation rule, fetches the tunnel token, generates a CA and server certificate, and registers the CA with Anthropic. A daily CronJob renews the server certificate as needed, so you don't handle any secrets by hand.
  1. 1
Set up Workload Identity Federation for the cluster
Follow [Use WIF with Kubernetes](https://platform.claude.com/docs/en/manage-claude/wif-providers/kubernetes) to register your cluster's OIDC issuer and create a federation rule. The setup component runs under its own ServiceAccount in the release namespace; the exact name follows Helm's `fullname` convention, so for any release name other than `mcp-tunnel`, run `helm template <release> ... | grep -A2 'kind: ServiceAccount'` to confirm it before creating the rule. The rest of this guide assumes release name `mcp-tunnel` in namespace `mcp-tunnel`, where the ServiceAccount is `mcp-tunnel-setup`.  
| Field  | Value  |  
| --- | --- |  
| Subject  | `system:serviceaccount:mcp-tunnel:mcp-tunnel-setup`  |  
| Audience  |  `api.anthropic.com` (the chart's default; no scheme)  |  
| Scope  | `org:manage_tunnels`  |  
The chart's default audience is `api.anthropic.com` with no scheme, but the Console's federation-rule form suggests `https://api.anthropic.com`. The two must match byte-for-byte or authentication fails. Either set the rule's audience to `api.anthropic.com`, or set `api.wif.audience` in `values.yaml` to `https://api.anthropic.com`.
If the tunnel is in a workspace other than the organization's default, also add the rule's service account as a member of that workspace under **Settings > Workspaces** (the Tunnels API authorizes against the service account's workspace memberships).
Note the rule's ID (`fdrl_...`); you'll set it as `api.wif.federationRuleId`.
The daily certificate-renewal CronJob uses a separate ServiceAccount (also derived from the Helm `fullname`) but does not call the Tunnels API; it renews the certificate locally and only needs Kubernetes RBAC, which the chart grants. The federation rule does not need to cover it.
  2. 2
Fetch the default values

helm show values \
  oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
  --version 1.0.0 > values.yaml

  3. 3
Configure tunnel attachment and routes
Edit `values.yaml` and set the `api.wif.*` keys with the tunnel ID, federation rule ID, and organization ID, plus a `routes` entry for each [upstream MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components):
values.yaml

api:
  wif:
    tunnelId: "tnl_..."
    federationRuleId: "fdrl_..."
    organizationId: "00000000-0000-0000-0000-000000000000"
    # Set when the tunnel is in a non-default workspace and the
    # rule's service account is a member of that workspace.
    # workspaceId: "wrkspc_..."

tunnel:
  # Increment to rotate the tunnel token on the next upgrade.
  # See the "Rotate the tunnel token" section.
  tokenVersion: "1"

gateway:
  config:
    routes:
      docs: http://docs-mcp.internal:8080
      search: http://search-mcp.internal:8080

With these routes, Claude reaches the servers at `docs.<your-tunnel-domain>` and `search.<your-tunnel-domain>`. Some managed Kubernetes distributions allocate the Service CIDR outside the standard private ranges; if your routes target in-cluster Services, add `gateway.config.upstream.allowed_ips` here per [Upstream IP validation](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting#upstream-ip-validation).
If you're using the [sample MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#optional-use-a-sample-mcp-server), set `routes` to `echo: http://hello-mcp:9000` instead.
  4. 4
Review the rendered manifests
Render the chart and review the output according to your organization's vetting practices:

helm template mcp-tunnel \
  oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
  --version 1.0.0 \
  -n mcp-tunnel \
  -f values.yaml > rendered.yaml

  5. 5
Install

helm install mcp-tunnel \
  oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
  --version 1.0.0 \
  --namespace mcp-tunnel --create-namespace \
  -f values.yaml

The setup component runs as a Helm pre-install hook Job, so `helm install` blocks until it completes. On success Helm deletes the Job automatically. If `helm install` fails with a hook error, see [Setup component authentication failures](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting#setup-component-authentication-failures).

The `api.wif.*` values are identifiers, not secrets, so storing them in Helm release-history Secrets is not a risk. The sensitive data at rest is the `mcp-tunnel` Secret the setup component creates, which holds the tunnel token and TLS private keys. Apply your organization's standard practices for protecting Kubernetes Secrets to this namespace.

Verify the deployment
Verify end to end from Anthropic's side: use `https://<route>.<your-tunnel-domain>/<path>` in a Managed Agent session or a Messages API request, where `<route>` is a key from `gateway.config.routes` and `<path>` is whatever the upstream MCP server serves at. With the [sample MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#optional-use-a-sample-mcp-server), that's `https://echo.<your-tunnel-domain>/mcp`. See [Use the tunneled MCP servers](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview#use-the-tunneled-mcp-servers) for the request shapes.
If that fails, check the pod logs (`kubectl -n mcp-tunnel logs deploy/mcp-tunnel -c mcp-proxy` and `-c cloudflared`) and consult [Troubleshooting](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting).
Optional configuration
### 
Restrict egress with NetworkPolicy
Ingress to the proxy pod is denied by default (`networkPolicy.ingress.enabled: true`). To additionally restrict pod egress, set `networkPolicy.egress.enabled: true` and populate `networkPolicy.egress.mcpServers` with pod label selectors or CIDR ranges that cover your upstream MCP servers. Egress from cloudflared to the tunnel edge is allowed separately through `networkPolicy.egress.cloudflaredEgressCIDRs`.
### 
Tune the proxy
Fields under `gateway.config.*` pass through to the proxy configuration file. Common adjustments include `upstream.allowed_ips`, `log_level`, and `upstream.tls`. See the [proxy configuration](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/reference#proxy-configuration) reference for the full field list. The chart always sets `listen_addr`, `tls.cert_file`, and `tls.key_file`; setting them in `gateway.config` has no effect.
### 
Supply your own OIDC token
By default the chart projects a Kubernetes ServiceAccount token for the setup component. To use a token from a different identity provider (such as [SPIFFE](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe), Vault, or a cloud-SDK sidecar), mount it with `setup.extraVolumes` and `setup.extraVolumeMounts`. Then point `api.wif.tokenFile` at the mount path. The chart sets `ANTHROPIC_IDENTITY_TOKEN_FILE` to that path, and the setup component reads the token from there.
Upgrades
Always pass `--version` to `helm upgrade` so you don't pull a newer chart unexpectedly.
### 
Change configuration
For routine changes such as routes, replica count, or NetworkPolicy:

helm upgrade mcp-tunnel \
  oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
  --version 1.0.0 \
  -n mcp-tunnel \
  -f values.yaml


Maintain a complete `values.yaml` rather than relying on `--reuse-values`. Helm's deep-merge behavior can silently fail to remove deleted routes.
### 
Rotate the tunnel token
With programmatic access, increment `tunnel.tokenVersion` in `values.yaml` and upgrade with `--set setup.force=true`. The setup component only re-runs on upgrades when forced:

helm upgrade mcp-tunnel \
  oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
  --version 1.0.0 \
  -n mcp-tunnel \
  -f values.yaml \
  --set setup.force=true

The setup component authenticates with Workload Identity Federation; there is no API token to revoke.
Without programmatic access, click **Rotate token** on the tunnel detail page in the Console, then update the `mcp-tunnel-token` Secret:

kubectl -n mcp-tunnel create secret generic mcp-tunnel-token \
  --from-literal=tunnel-token='eyJ...' --dry-run=client -o yaml | kubectl apply -f -
kubectl -n mcp-tunnel rollout restart deploy/mcp-tunnel


Clicking **Rotate token** invalidates the current token immediately. Until the Secret is updated and the rollout completes, any pod that restarts with the old token (eviction, node drain, OOM) cannot reconnect. Update the Secret promptly after rotating; for stricter availability requirements, use programmatic access so the chart handles the rotation atomically.
### 
Certificate renewal
The chart provides automation, but you remain responsible for monitoring expiry and confirming renewal completes.
With programmatic access, certificate renewal is automatic. The chart deploys a CronJob (named after the Helm `fullname`, suffixed `-cert-renew`) that runs `setup renew-cert` daily (at `serverCert.cronSchedule`, default `0 0 * * *` UTC). The job is a no-op unless the certificate is within `serverCert.renewBefore` of expiry (default 30 days). Renewal is local: the job signs a fresh certificate with the CA already stored in the Secret, makes no API calls, and only needs the Kubernetes RBAC the chart grants. The proxy hot-reloads the certificate from the Secret mount, so no Deployment restart is needed.
Without programmatic access there is no CronJob. From inside the `mcp-tunnel/` directory you kept after install, sign a fresh server certificate with the existing CA (do not regenerate the CA):

export TUNNEL_DOMAIN=YOUR_TUNNEL_DOMAIN_HERE
openssl req -new -key data/tls.key -out /tmp/server.csr \
  -subj "/CN=${TUNNEL_DOMAIN}"
openssl x509 -req -in /tmp/server.csr \
  -CA data/ca.crt -CAkey data/ca.key -CAcreateserial \
  -out data/tls.crt -days 90 -extfile data/tls.ext

kubectl -n mcp-tunnel create secret generic mcp-tunnel-cert \
  --from-file=tls.crt=data/tls.crt --from-file=tls.key=data/tls.key \
  --dry-run=client -o yaml | kubectl apply -f -

The proxy hot-reloads the certificate from the Secret mount.
Next steps
[  Use the tunneled MCP servers Attach an upstream MCP server to a Managed Agent or the Messages API. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview#use-the-tunneled-mcp-servers)[  Security Hardening guidance, credential rotation, and breach response. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/security)[  Troubleshooting Diagnose connectivity, TLS, and routing issues. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting)
  * [Before you begin](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#before-you-begin)
  * [Optional: Use a sample MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#optional-use-a-sample-mcp-server)
  * [Install](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#install)
  * [Verify the deployment](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#verify-the-deployment)
  * [Optional configuration](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#optional-configuration)
  * [Restrict egress with NetworkPolicy](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#restrict-egress-with-network-policy)
  * [Tune the proxy](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#tune-the-proxy)
  * [Supply your own OIDC token](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#supply-your-own-oidc-token)
  * [Upgrades](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#upgrades)
  * [Change configuration](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#change-configuration)
  * [Rotate the tunnel token](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#rotate-the-tunnel-token)
  * [Certificate renewal](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#certificate-renewal)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#next-steps)

Messages/MCP tunnels
# Deploy MCP tunnels with Helm
Install the tunnel stack on a Kubernetes cluster using the Anthropic Helm chart.
MCP tunnels are in research preview. [Request access](https://claude.com/form/claude-managed-agents) to try them.
The Anthropic Helm chart installs the [tunnel stack](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) as a single Deployment and attaches it to the tunnel you created in the [Console](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#create-a-tunnel).
Before you begin
You need:
  * **A tunnel created in the Console.** Complete [Create a tunnel](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#create-a-tunnel) first and record the tunnel ID (`tnl_...`). For manual provisioning you also need the tunnel token and tunnel domain from that step.
  * **A way for the chart to authenticate to the Tunnels API.**
    * **[Programmatic access](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#credential-provisioning) (recommended).** The [setup component](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) authenticates through Workload Identity Federation, fetches the tunnel token, generates a CA, registers it with Anthropic, and stores everything in a Secret. You'll need a federation rule scoped to `org:manage_tunnels`.
    * **[Manual](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#credential-provisioning).** Skip programmatic access. You'll [get the tunnel token from the Console](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#get-the-connection-details), generate a CA and server certificate yourself, [register the CA in the Console](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#add-a-ca-certificate), and supply the credentials to the cluster as Secrets.
  * **A Kubernetes cluster** you can deploy to with `helm` and `kubectl`. The **Without programmatic access** tab also uses `openssl` (1.1.1 or later).
  * **Outbound network connectivity** from the cluster to `api.anthropic.com` (443 TCP) and the [tunnel edge](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) (7844 TCP and UDP). See the full [network requirements](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview#network-requirements).
  * **One or more MCP servers** running and reachable from the cluster on the addresses you'll configure under `gateway.config.routes`. If you don't have one yet, [use the sample server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#optional-use-a-sample-mcp-server).

Optional: Use a sample MCP server
If you don't have an MCP server available for testing, use this minimal one:

kubectl create namespace mcp-tunnel --dry-run=client -o yaml | kubectl apply -f -
kubectl -n mcp-tunnel apply -f - <<'EOF'
apiVersion: v1
kind: ConfigMap
metadata:
  name: hello-mcp-src
data:
  hello_server.py: |
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("hello-server", host="0.0.0.0", port=9000)

    @mcp.tool()
    def hello(name: str = "world") -> str:
        """Say hello to someone."""
        return f"Hello, {name}!"

    if __name__ == "__main__":
        mcp.run(transport="streamable-http")
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-mcp
spec:
  replicas: 1
  selector:
    matchLabels: { app: hello-mcp }
  template:
    metadata:
      labels: { app: hello-mcp }
    spec:
      containers:
        - name: hello-mcp
          image: python:3.13-slim
          command: ["sh", "-c", "pip install --quiet mcp && python /app/hello_server.py"]
          volumeMounts:
            - { name: src, mountPath: /app }
          ports:
            - { containerPort: 9000 }
      volumes:
        - name: src
          configMap: { name: hello-mcp-src }
---
apiVersion: v1
kind: Service
metadata:
  name: hello-mcp
spec:
  selector: { app: hello-mcp }
  ports:
    - { port: 9000, targetPort: 9000 }
EOF

The Install steps that follow note where to add the corresponding route.
Install
With programmatic access
With programmatic access
Without programmatic access
Without programmatic access
The setup component exchanges the cluster's projected ServiceAccount token through your federation rule, fetches the tunnel token, generates a CA and server certificate, and registers the CA with Anthropic. A daily CronJob renews the server certificate as needed, so you don't handle any secrets by hand.
  1. 1
Set up Workload Identity Federation for the cluster
Follow [Use WIF with Kubernetes](https://platform.claude.com/docs/en/manage-claude/wif-providers/kubernetes) to register your cluster's OIDC issuer and create a federation rule. The setup component runs under its own ServiceAccount in the release namespace; the exact name follows Helm's `fullname` convention, so for any release name other than `mcp-tunnel`, run `helm template <release> ... | grep -A2 'kind: ServiceAccount'` to confirm it before creating the rule. The rest of this guide assumes release name `mcp-tunnel` in namespace `mcp-tunnel`, where the ServiceAccount is `mcp-tunnel-setup`.  
| Field  | Value  |  
| --- | --- |  
| Subject  | `system:serviceaccount:mcp-tunnel:mcp-tunnel-setup`  |  
| Audience  |  `api.anthropic.com` (the chart's default; no scheme)  |  
| Scope  | `org:manage_tunnels`  |  
The chart's default audience is `api.anthropic.com` with no scheme, but the Console's federation-rule form suggests `https://api.anthropic.com`. The two must match byte-for-byte or authentication fails. Either set the rule's audience to `api.anthropic.com`, or set `api.wif.audience` in `values.yaml` to `https://api.anthropic.com`.
If the tunnel is in a workspace other than the organization's default, also add the rule's service account as a member of that workspace under **Settings > Workspaces** (the Tunnels API authorizes against the service account's workspace memberships).
Note the rule's ID (`fdrl_...`); you'll set it as `api.wif.federationRuleId`.
The daily certificate-renewal CronJob uses a separate ServiceAccount (also derived from the Helm `fullname`) but does not call the Tunnels API; it renews the certificate locally and only needs Kubernetes RBAC, which the chart grants. The federation rule does not need to cover it.
  2. 2
Fetch the default values

helm show values \
  oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
  --version 1.0.0 > values.yaml

  3. 3
Configure tunnel attachment and routes
Edit `values.yaml` and set the `api.wif.*` keys with the tunnel ID, federation rule ID, and organization ID, plus a `routes` entry for each [upstream MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components):
values.yaml

api:
  wif:
    tunnelId: "tnl_..."
    federationRuleId: "fdrl_..."
    organizationId: "00000000-0000-0000-0000-000000000000"
    # Set when the tunnel is in a non-default workspace and the
    # rule's service account is a member of that workspace.
    # workspaceId: "wrkspc_..."

tunnel:
  # Increment to rotate the tunnel token on the next upgrade.
  # See the "Rotate the tunnel token" section.
  tokenVersion: "1"

gateway:
  config:
    routes:
      docs: http://docs-mcp.internal:8080
      search: http://search-mcp.internal:8080

With these routes, Claude reaches the servers at `docs.<your-tunnel-domain>` and `search.<your-tunnel-domain>`. Some managed Kubernetes distributions allocate the Service CIDR outside the standard private ranges; if your routes target in-cluster Services, add `gateway.config.upstream.allowed_ips` here per [Upstream IP validation](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting#upstream-ip-validation).
If you're using the [sample MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#optional-use-a-sample-mcp-server), set `routes` to `echo: http://hello-mcp:9000` instead.
  4. 4
Review the rendered manifests
Render the chart and review the output according to your organization's vetting practices:

helm template mcp-tunnel \
  oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
  --version 1.0.0 \
  -n mcp-tunnel \
  -f values.yaml > rendered.yaml

  5. 5
Install

helm install mcp-tunnel \
  oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
  --version 1.0.0 \
  --namespace mcp-tunnel --create-namespace \
  -f values.yaml

The setup component runs as a Helm pre-install hook Job, so `helm install` blocks until it completes. On success Helm deletes the Job automatically. If `helm install` fails with a hook error, see [Setup component authentication failures](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting#setup-component-authentication-failures).

The `api.wif.*` values are identifiers, not secrets, so storing them in Helm release-history Secrets is not a risk. The sensitive data at rest is the `mcp-tunnel` Secret the setup component creates, which holds the tunnel token and TLS private keys. Apply your organization's standard practices for protecting Kubernetes Secrets to this namespace.

Verify the deployment
Verify end to end from Anthropic's side: use `https://<route>.<your-tunnel-domain>/<path>` in a Managed Agent session or a Messages API request, where `<route>` is a key from `gateway.config.routes` and `<path>` is whatever the upstream MCP server serves at. With the [sample MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm#optional-use-a-sample-mcp-server), that's `https://echo.<your-tunnel-domain>/mcp`. See [Use the tunneled MCP servers](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview#use-the-tunneled-mcp-servers) for the request shapes.
If that fails, check the pod logs (`kubectl -n mcp-tunnel logs deploy/mcp-tunnel -c mcp-proxy` and `-c cloudflared`) and consult [Troubleshooting](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting).
Optional configuration
### 
Restrict egress with NetworkPolicy
Ingress to the proxy pod is denied by default (`networkPolicy.ingress.enabled: true`). To additionally restrict pod egress, set `networkPolicy.egress.enabled: true` and populate `networkPolicy.egress.mcpServers` with pod label selectors or CIDR ranges that cover your upstream MCP servers. Egress from cloudflared to the tunnel edge is allowed separately through `networkPolicy.egress.cloudflaredEgressCIDRs`.
### 
Tune the proxy
Fields under `gateway.config.*` pass through to the proxy configuration file. Common adjustments include `upstream.allowed_ips`, `log_level`, and `upstream.tls`. See the [proxy configuration](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/reference#proxy-configuration) reference for the full field list. The chart always sets `listen_addr`, `tls.cert_file`, and `tls.key_file`; setting them in `gateway.config` has no effect.
### 
Supply your own OIDC token
By default the chart projects a Kubernetes ServiceAccount token for the setup component. To use a token from a different identity provider (such as [SPIFFE](https://platform.claude.com/docs/en/manage-claude/wif-providers/spiffe), Vault, or a cloud-SDK sidecar), mount it with `setup.extraVolumes` and `setup.extraVolumeMounts`. Then point `api.wif.tokenFile` at the mount path. The chart sets `ANTHROPIC_IDENTITY_TOKEN_FILE` to that path, and the setup component reads the token from there.
Upgrades
Always pass `--version` to `helm upgrade` so you don't pull a newer chart unexpectedly.
### 
Change configuration
For routine changes such as routes, replica count, or NetworkPolicy:

helm upgrade mcp-tunnel \
  oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
  --version 1.0.0 \
  -n mcp-tunnel \
  -f values.yaml


Maintain a complete `values.yaml` rather than relying on `--reuse-values`. Helm's deep-merge behavior can silently fail to remove deleted routes.
### 
Rotate the tunnel token
With programmatic access, increment `tunnel.tokenVersion` in `values.yaml` and upgrade with `--set setup.force=true`. The setup component only re-runs on upgrades when forced:

helm upgrade mcp-tunnel \
  oci://us-docker.pkg.dev/anthropic-public-registry/charts/mcp-tunnel \
  --version 1.0.0 \
  -n mcp-tunnel \
  -f values.yaml \
  --set setup.force=true

The setup component authenticates with Workload Identity Federation; there is no API token to revoke.
Without programmatic access, click **Rotate token** on the tunnel detail page in the Console, then update the `mcp-tunnel-token` Secret:

kubectl -n mcp-tunnel create secret generic mcp-tunnel-token \
  --from-literal=tunnel-token='eyJ...' --dry-run=client -o yaml | kubectl apply -f -
kubectl -n mcp-tunnel rollout restart deploy/mcp-tunnel


Clicking **Rotate token** invalidates the current token immediately. Until the Secret is updated and the rollout completes, any pod that restarts with the old token (eviction, node drain, OOM) cannot reconnect. Update the Secret promptly after rotating; for stricter availability requirements, use programmatic access so the chart handles the rotation atomically.
### 
Certificate renewal
The chart provides automation, but you remain responsible for monitoring expiry and confirming renewal completes.
With programmatic access, certificate renewal is automatic. The chart deploys a CronJob (named after the Helm `fullname`, suffixed `-cert-renew`) that runs `setup renew-cert` daily (at `serverCert.cronSchedule`, default `0 0 * * *` UTC). The job is a no-op unless the certificate is within `serverCert.renewBefore` of expiry (default 30 days). Renewal is local: the job signs a fresh certificate with the CA already stored in the Secret, makes no API calls, and only needs the Kubernetes RBAC the chart grants. The proxy hot-reloads the certificate from the Secret mount, so no Deployment restart is needed.
Without programmatic access there is no CronJob. From inside the `mcp-tunnel/` directory you kept after install, sign a fresh server certificate with the existing CA (do not regenerate the CA):

export TUNNEL_DOMAIN=YOUR_TUNNEL_DOMAIN_HERE
openssl req -new -key data/tls.key -out /tmp/server.csr \
  -subj "/CN=${TUNNEL_DOMAIN}"
openssl x509 -req -in /tmp/server.csr \
  -CA data/ca.crt -CAkey data/ca.key -CAcreateserial \
  -out data/tls.crt -days 90 -extfile data/tls.ext

kubectl -n mcp-tunnel create secret generic mcp-tunnel-cert \
  --from-file=tls.crt=data/tls.crt --from-file=tls.key=data/tls.key \
  --dry-run=client -o yaml | kubectl apply -f -

The proxy hot-reloads the certificate from the Secret mount.
Next steps
[  Use the tunneled MCP servers Attach an upstream MCP server to a Managed Agent or the Messages API. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview#use-the-tunneled-mcp-servers)[  Security Hardening guidance, credential rotation, and breach response. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/security)[  Troubleshooting Diagnose connectivity, TLS, and routing issues. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting)
