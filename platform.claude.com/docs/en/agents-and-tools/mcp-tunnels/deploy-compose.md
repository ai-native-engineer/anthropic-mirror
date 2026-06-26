<!-- source: https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose -->

# Deploy MCP tunnels with Docker Compose
Install the MCP tunnel stack on a VM using Docker Compose.
MCP tunnels are in research preview. [Request access](https://claude.com/form/claude-managed-agents) to try them.
This guide deploys the [tunnel stack](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) as hardened containers on a single host. The same configuration can be replicated across multiple hosts for availability.
Before you begin
You need:
  * **A tunnel created in the Console.** Follow [Create a tunnel](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#create-a-tunnel) and record the tunnel ID (`tnl_...`).
  * **A way for the host to authenticate to the Tunnels API.**
    * **Programmatic access (recommended).** Turn on **Set up programmatic access** when creating the tunnel so the [setup component](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) can authenticate through Workload Identity Federation. Record the federation rule ID (`fdrl_...`) and your organization ID.
    * **Manual.** Skip programmatic access. You'll [get the tunnel token from the Console](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#get-the-connection-details), generate a CA and server certificate yourself, and [register the CA in the Console](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#add-a-ca-certificate).
  * **A host with Docker and Docker Compose** installed. The manual flow also requires `openssl` (1.1.1 or newer).
  * **Outbound network connectivity** from the host to `api.anthropic.com` (443 TCP) and the [tunnel edge](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) (7844 TCP and UDP). See the full [network requirements](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview#network-requirements).
  * **One or more MCP servers** running and reachable from the host on the addresses you'll configure under `routes`. If you don't have one yet, [use the sample server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#optional-use-a-sample-mcp-server).

Optional: Use a sample MCP server
If you don't have an MCP server available for testing, use this minimal one:

mkdir -p mcp-tunnel
cat > mcp-tunnel/hello_server.py <<'EOF'
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-server", host="0.0.0.0", port=9000)

@mcp.tool()
def hello(name: str = "world") -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
EOF

The following Install steps `cd` into `mcp-tunnel/` and note where to add the corresponding service and route.
Install
This guide provides one reference approach using Docker Compose. You are responsible for adapting it to meet your organization's security requirements.
With programmatic access
With programmatic access
Without programmatic access
Without programmatic access
This path requires the host to have an OIDC identity provider (such as a cloud VM metadata server or SPIFFE). If it doesn't, use the **Without programmatic access** tab instead.
The setup component uses Workload Identity Federation to fetch the tunnel token, generate a CA and server certificate, and register the CA with Anthropic.
  1. 1
Prepare the deployment directory

mkdir -p mcp-tunnel/{config,data}
cd mcp-tunnel
sudo chown 65532:65532 data

The containers run as the non-root UID `65532` and need write access to `data/`.
  2. 2
Write docker-compose.yaml
The compose file pins images by SHA-256 digest, runs every container as non-root with a read-only filesystem, drops all Linux capabilities, and disables privilege escalation.

cat > docker-compose.yaml <<'EOF'
services:
  setup:
    image: us-docker.pkg.dev/anthropic-public-registry/images/mcp-proxy@sha256:6b9adedbf2763143ec72f106ecaf0ce7fd3294e89b208f54a1db97a33d14c5ba
    entrypoint: ["/setup"]
    command:
      - init
      - --api-url=https://api.anthropic.com
      - --output=dir:/data
      - --token-version=1
    environment:
      - TUNNEL_ID
      - ANTHROPIC_FEDERATION_RULE_ID
      - ANTHROPIC_ORGANIZATION_ID
      - ANTHROPIC_WORKSPACE_ID
      - ANTHROPIC_IDENTITY_TOKEN
    volumes:
      - ./data:/data
    user: "65532:65532"
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    profiles: ["setup"]

  cloudflared:
    image: cloudflare/cloudflared@sha256:6b599ca3e974349ead3286d178da61d291961182ec3fe9c505e1dd02c8ac31b0
    command: tunnel --no-autoupdate run --url http://localhost:8080
    environment:
      - TUNNEL_TOKEN
    # Share the proxy's netns so localhost:8080 reaches it.
    network_mode: "service:mcp-proxy"
    restart: unless-stopped
    user: "65532:65532"
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    stop_grace_period: 30s
    logging:
      options:
        max-size: "10m"
        max-file: "3"

  mcp-proxy:
    image: us-docker.pkg.dev/anthropic-public-registry/images/mcp-proxy@sha256:6b9adedbf2763143ec72f106ecaf0ce7fd3294e89b208f54a1db97a33d14c5ba
    volumes:
      - ./config/mcp-proxy.yaml:/etc/mcp-gateway/config.yaml:ro
      - ./data:/data:ro
    restart: unless-stopped
    user: "65532:65532"
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    stop_grace_period: 30s
    logging:
      options:
        max-size: "10m"
        max-file: "3"
EOF

If you're using the [sample MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#optional-use-a-sample-mcp-server), append it as a service:

cat >> docker-compose.yaml <<'EOF'

  hello-mcp:
    image: python:3.13-slim
    working_dir: /app
    volumes:
      - ./hello_server.py:/app/hello_server.py:ro
    command: sh -c "pip install --quiet mcp && python hello_server.py"
    restart: unless-stopped
EOF

  3. 3
Provision the tunnel
Set the identifiers from the [Console create-tunnel flow](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#create-a-tunnel):

export TUNNEL_ID=tnl_...
export ANTHROPIC_FEDERATION_RULE_ID=fdrl_...
export ANTHROPIC_ORGANIZATION_ID=00000000-0000-0000-0000-000000000000

If your federation rule is scoped to a workspace other than your organization's default, also set `ANTHROPIC_WORKSPACE_ID=wrkspc_...`; the setup component uses the default workspace otherwise.
Set `ANTHROPIC_IDENTITY_TOKEN` to an OIDC JWT from this host's identity provider. Follow the [WIF guide for your provider](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#identity-providers) to register the issuer, set the rule's subject, and mint the token; the rule's audience must match the audience you request when minting.
Run the setup component:

docker compose run --rm setup

`setup init` is idempotent over `data/`: re-running it reuses the existing CA and skips registration. A new CA is generated and registered only when `data/` is empty or `TUNNEL_ID` has changed; in that case the cap of two active certificates applies, so revoke one in the Console first if both slots are filled.
See [Setup component authentication failures](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting#setup-component-authentication-failures) if it errors.
Retrieve your tunnel domain and export it for later steps:

export TUNNEL_DOMAIN=$(sudo cat data/tunnel-domain)
echo "$TUNNEL_DOMAIN"

Workload Identity Federation tokens are short-lived (one hour by default) and expire automatically; there is nothing to revoke after setup completes.
  4. 4
Write the proxy config
`tunnel_domain` is **required** : the [proxy](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) uses it to strip the domain suffix from incoming hostnames before looking up the subdomain in `routes`. `routes` is a flat map from subdomain to upstream URL, not a list.

cat > config/mcp-proxy.yaml <<EOF
listen_addr: ":8080"
log_level: info
shutdown_timeout: 30s
tunnel_domain: ${TUNNEL_DOMAIN}
tls:
  cert_file: /data/tls.crt
  key_file: /data/tls.key
routes:
  echo: http://hello-mcp:9000
EOF

The `echo:` route targets the [sample MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#optional-use-a-sample-mcp-server); replace it with (or add) your own routes. See the [proxy configuration](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/reference#proxy-configuration) reference for all available fields.
  5. 5
Start the deployment

export TUNNEL_TOKEN=$(sudo cat data/tunnel-token)
docker compose up -d

The compose file reads `TUNNEL_TOKEN` from the host environment with no default, so the export must be repeated in every fresh shell and after a reboot.
For a multi-VM deployment, copy the `mcp-tunnel/` directory to each host, set `TUNNEL_TOKEN`, and run `docker compose up -d`. In the programmatic flow `TUNNEL_TOKEN` is `$(sudo cat data/tunnel-token)`; in the manual flow it's the value you copied from the Console. The same tunnel token and certificates work across all replicas.
Verify the deployment
Verify end to end by calling an [upstream MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) from Anthropic's side: see [Use the tunneled MCP servers](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview#use-the-tunneled-mcp-servers). With the [sample MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#optional-use-a-sample-mcp-server), the routed URL is `https://echo.<your-tunnel-domain>/mcp`. If verification fails, see [Troubleshooting](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting).
Upgrades
Run the commands in this section from inside the `mcp-tunnel/` deployment directory.
### 
Rotate the tunnel token
With programmatic access, increment `--token-version` in the `setup` service command, set the Workload Identity Federation identifiers, mint a fresh OIDC JWT, and re-run the setup component:

# Edit docker-compose.yaml: increment the integer in the setup service's
# --token-version argument (for example, --token-version=1 to
# --token-version=2). The setup binary refuses to rotate when the value
# hasn't changed.

export TUNNEL_ID=tnl_...
export ANTHROPIC_FEDERATION_RULE_ID=fdrl_...
export ANTHROPIC_ORGANIZATION_ID=00000000-0000-0000-0000-000000000000
# export ANTHROPIC_WORKSPACE_ID=wrkspc_...   # if your rule is workspace-scoped
# Re-mint ANTHROPIC_IDENTITY_TOKEN per the WIF provider guide for your
# environment (it will have expired since install).
export ANTHROPIC_IDENTITY_TOKEN=...

docker compose run --rm setup

export TUNNEL_TOKEN=$(sudo cat data/tunnel-token)
docker compose up -d cloudflared

The `--token-version` argument is edited in `docker-compose.yaml` rather than passed on the command line so the new value persists for future runs of the setup component. The setup component authenticates with Workload Identity Federation; there is no API token to revoke.
Without programmatic access, click **Rotate token** on the tunnel detail page in the Console, then update the `TUNNEL_TOKEN` environment variable on each host and restart cloudflared (`docker compose up -d cloudflared`).

Clicking **Rotate token** invalidates the current token immediately. Between that moment and updating `TUNNEL_TOKEN` on every host and restarting cloudflared, any host whose cloudflared restarts (crash, host reboot) cannot reconnect. Update each host promptly after rotating.
### 
Certificate renewal
You're responsible for monitoring expiry and renewing the server certificate before it expires.
With programmatic access:

docker compose run --rm setup renew-cert --output=dir:/data

The CLI arguments replace the `setup` service's `command` (the `init` arguments) but keep its `entrypoint`, so this runs `/setup renew-cert --output=dir:/data`.

Pass `--renew-before=720h` to make the command a no-op when more than 30 days of validity remain. This makes it safe to run on a fixed schedule.
Without programmatic access, sign a new server certificate with your existing CA (the CA registered in the Console doesn't change) and replace `data/tls.crt`. Set `TUNNEL_DOMAIN` first if you're running this from a fresh shell.

export TUNNEL_DOMAIN=YOUR_TUNNEL_DOMAIN_HERE
openssl req -new -key data/tls.key -out /tmp/server.csr \
  -subj "/CN=${TUNNEL_DOMAIN}"
openssl x509 -req -in /tmp/server.csr \
  -CA data/ca.crt -CAkey data/ca.key -CAcreateserial \
  -out data/tls.crt -days 90 \
  -extfile data/tls.ext

In either flow the proxy polls `tls.cert_file` and reloads it automatically, so no restart is required.
Next steps
[  Use the tunneled MCP servers Attach an upstream MCP server to a Managed Agent or the Messages API. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview#use-the-tunneled-mcp-servers)[  Security Hardening guidance, credential rotation, and breach response. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/security)[  Troubleshooting Diagnose connectivity, TLS, and routing issues. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting)
  * [Before you begin](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#before-you-begin)
  * [Optional: Use a sample MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#optional-use-a-sample-mcp-server)
  * [Install](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#install)
  * [Verify the deployment](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#verify-the-deployment)
  * [Upgrades](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#upgrades)
  * [Rotate the tunnel token](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#rotate-the-tunnel-token)
  * [Certificate renewal](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#certificate-renewal)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#next-steps)

Messages/MCP tunnels
# Deploy MCP tunnels with Docker Compose
Install the MCP tunnel stack on a VM using Docker Compose.
MCP tunnels are in research preview. [Request access](https://claude.com/form/claude-managed-agents) to try them.
This guide deploys the [tunnel stack](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) as hardened containers on a single host. The same configuration can be replicated across multiple hosts for availability.
Before you begin
You need:
  * **A tunnel created in the Console.** Follow [Create a tunnel](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#create-a-tunnel) and record the tunnel ID (`tnl_...`).
  * **A way for the host to authenticate to the Tunnels API.**
    * **Programmatic access (recommended).** Turn on **Set up programmatic access** when creating the tunnel so the [setup component](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) can authenticate through Workload Identity Federation. Record the federation rule ID (`fdrl_...`) and your organization ID.
    * **Manual.** Skip programmatic access. You'll [get the tunnel token from the Console](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#get-the-connection-details), generate a CA and server certificate yourself, and [register the CA in the Console](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#add-a-ca-certificate).
  * **A host with Docker and Docker Compose** installed. The manual flow also requires `openssl` (1.1.1 or newer).
  * **Outbound network connectivity** from the host to `api.anthropic.com` (443 TCP) and the [tunnel edge](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) (7844 TCP and UDP). See the full [network requirements](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview#network-requirements).
  * **One or more MCP servers** running and reachable from the host on the addresses you'll configure under `routes`. If you don't have one yet, [use the sample server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#optional-use-a-sample-mcp-server).

Optional: Use a sample MCP server
If you don't have an MCP server available for testing, use this minimal one:

mkdir -p mcp-tunnel
cat > mcp-tunnel/hello_server.py <<'EOF'
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hello-server", host="0.0.0.0", port=9000)

@mcp.tool()
def hello(name: str = "world") -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
EOF

The following Install steps `cd` into `mcp-tunnel/` and note where to add the corresponding service and route.
Install
This guide provides one reference approach using Docker Compose. You are responsible for adapting it to meet your organization's security requirements.
With programmatic access
With programmatic access
Without programmatic access
Without programmatic access
This path requires the host to have an OIDC identity provider (such as a cloud VM metadata server or SPIFFE). If it doesn't, use the **Without programmatic access** tab instead.
The setup component uses Workload Identity Federation to fetch the tunnel token, generate a CA and server certificate, and register the CA with Anthropic.
  1. 1
Prepare the deployment directory

mkdir -p mcp-tunnel/{config,data}
cd mcp-tunnel
sudo chown 65532:65532 data

The containers run as the non-root UID `65532` and need write access to `data/`.
  2. 2
Write docker-compose.yaml
The compose file pins images by SHA-256 digest, runs every container as non-root with a read-only filesystem, drops all Linux capabilities, and disables privilege escalation.

cat > docker-compose.yaml <<'EOF'
services:
  setup:
    image: us-docker.pkg.dev/anthropic-public-registry/images/mcp-proxy@sha256:6b9adedbf2763143ec72f106ecaf0ce7fd3294e89b208f54a1db97a33d14c5ba
    entrypoint: ["/setup"]
    command:
      - init
      - --api-url=https://api.anthropic.com
      - --output=dir:/data
      - --token-version=1
    environment:
      - TUNNEL_ID
      - ANTHROPIC_FEDERATION_RULE_ID
      - ANTHROPIC_ORGANIZATION_ID
      - ANTHROPIC_WORKSPACE_ID
      - ANTHROPIC_IDENTITY_TOKEN
    volumes:
      - ./data:/data
    user: "65532:65532"
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    profiles: ["setup"]

  cloudflared:
    image: cloudflare/cloudflared@sha256:6b599ca3e974349ead3286d178da61d291961182ec3fe9c505e1dd02c8ac31b0
    command: tunnel --no-autoupdate run --url http://localhost:8080
    environment:
      - TUNNEL_TOKEN
    # Share the proxy's netns so localhost:8080 reaches it.
    network_mode: "service:mcp-proxy"
    restart: unless-stopped
    user: "65532:65532"
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    stop_grace_period: 30s
    logging:
      options:
        max-size: "10m"
        max-file: "3"

  mcp-proxy:
    image: us-docker.pkg.dev/anthropic-public-registry/images/mcp-proxy@sha256:6b9adedbf2763143ec72f106ecaf0ce7fd3294e89b208f54a1db97a33d14c5ba
    volumes:
      - ./config/mcp-proxy.yaml:/etc/mcp-gateway/config.yaml:ro
      - ./data:/data:ro
    restart: unless-stopped
    user: "65532:65532"
    read_only: true
    security_opt:
      - no-new-privileges:true
    cap_drop:
      - ALL
    stop_grace_period: 30s
    logging:
      options:
        max-size: "10m"
        max-file: "3"
EOF

If you're using the [sample MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#optional-use-a-sample-mcp-server), append it as a service:

cat >> docker-compose.yaml <<'EOF'

  hello-mcp:
    image: python:3.13-slim
    working_dir: /app
    volumes:
      - ./hello_server.py:/app/hello_server.py:ro
    command: sh -c "pip install --quiet mcp && python hello_server.py"
    restart: unless-stopped
EOF

  3. 3
Provision the tunnel
Set the identifiers from the [Console create-tunnel flow](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/console#create-a-tunnel):

export TUNNEL_ID=tnl_...
export ANTHROPIC_FEDERATION_RULE_ID=fdrl_...
export ANTHROPIC_ORGANIZATION_ID=00000000-0000-0000-0000-000000000000

If your federation rule is scoped to a workspace other than your organization's default, also set `ANTHROPIC_WORKSPACE_ID=wrkspc_...`; the setup component uses the default workspace otherwise.
Set `ANTHROPIC_IDENTITY_TOKEN` to an OIDC JWT from this host's identity provider. Follow the [WIF guide for your provider](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#identity-providers) to register the issuer, set the rule's subject, and mint the token; the rule's audience must match the audience you request when minting.
Run the setup component:

docker compose run --rm setup

`setup init` is idempotent over `data/`: re-running it reuses the existing CA and skips registration. A new CA is generated and registered only when `data/` is empty or `TUNNEL_ID` has changed; in that case the cap of two active certificates applies, so revoke one in the Console first if both slots are filled.
See [Setup component authentication failures](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting#setup-component-authentication-failures) if it errors.
Retrieve your tunnel domain and export it for later steps:

export TUNNEL_DOMAIN=$(sudo cat data/tunnel-domain)
echo "$TUNNEL_DOMAIN"

Workload Identity Federation tokens are short-lived (one hour by default) and expire automatically; there is nothing to revoke after setup completes.
  4. 4
Write the proxy config
`tunnel_domain` is **required** : the [proxy](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) uses it to strip the domain suffix from incoming hostnames before looking up the subdomain in `routes`. `routes` is a flat map from subdomain to upstream URL, not a list.

cat > config/mcp-proxy.yaml <<EOF
listen_addr: ":8080"
log_level: info
shutdown_timeout: 30s
tunnel_domain: ${TUNNEL_DOMAIN}
tls:
  cert_file: /data/tls.crt
  key_file: /data/tls.key
routes:
  echo: http://hello-mcp:9000
EOF

The `echo:` route targets the [sample MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#optional-use-a-sample-mcp-server); replace it with (or add) your own routes. See the [proxy configuration](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/reference#proxy-configuration) reference for all available fields.
  5. 5
Start the deployment

export TUNNEL_TOKEN=$(sudo cat data/tunnel-token)
docker compose up -d

The compose file reads `TUNNEL_TOKEN` from the host environment with no default, so the export must be repeated in every fresh shell and after a reboot.
For a multi-VM deployment, copy the `mcp-tunnel/` directory to each host, set `TUNNEL_TOKEN`, and run `docker compose up -d`. In the programmatic flow `TUNNEL_TOKEN` is `$(sudo cat data/tunnel-token)`; in the manual flow it's the value you copied from the Console. The same tunnel token and certificates work across all replicas.
Verify the deployment
Verify end to end by calling an [upstream MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/concepts#components) from Anthropic's side: see [Use the tunneled MCP servers](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview#use-the-tunneled-mcp-servers). With the [sample MCP server](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose#optional-use-a-sample-mcp-server), the routed URL is `https://echo.<your-tunnel-domain>/mcp`. If verification fails, see [Troubleshooting](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting).
Upgrades
Run the commands in this section from inside the `mcp-tunnel/` deployment directory.
### 
Rotate the tunnel token
With programmatic access, increment `--token-version` in the `setup` service command, set the Workload Identity Federation identifiers, mint a fresh OIDC JWT, and re-run the setup component:

# Edit docker-compose.yaml: increment the integer in the setup service's
# --token-version argument (for example, --token-version=1 to
# --token-version=2). The setup binary refuses to rotate when the value
# hasn't changed.

export TUNNEL_ID=tnl_...
export ANTHROPIC_FEDERATION_RULE_ID=fdrl_...
export ANTHROPIC_ORGANIZATION_ID=00000000-0000-0000-0000-000000000000
# export ANTHROPIC_WORKSPACE_ID=wrkspc_...   # if your rule is workspace-scoped
# Re-mint ANTHROPIC_IDENTITY_TOKEN per the WIF provider guide for your
# environment (it will have expired since install).
export ANTHROPIC_IDENTITY_TOKEN=...

docker compose run --rm setup

export TUNNEL_TOKEN=$(sudo cat data/tunnel-token)
docker compose up -d cloudflared

The `--token-version` argument is edited in `docker-compose.yaml` rather than passed on the command line so the new value persists for future runs of the setup component. The setup component authenticates with Workload Identity Federation; there is no API token to revoke.
Without programmatic access, click **Rotate token** on the tunnel detail page in the Console, then update the `TUNNEL_TOKEN` environment variable on each host and restart cloudflared (`docker compose up -d cloudflared`).

Clicking **Rotate token** invalidates the current token immediately. Between that moment and updating `TUNNEL_TOKEN` on every host and restarting cloudflared, any host whose cloudflared restarts (crash, host reboot) cannot reconnect. Update each host promptly after rotating.
### 
Certificate renewal
You're responsible for monitoring expiry and renewing the server certificate before it expires.
With programmatic access:

docker compose run --rm setup renew-cert --output=dir:/data

The CLI arguments replace the `setup` service's `command` (the `init` arguments) but keep its `entrypoint`, so this runs `/setup renew-cert --output=dir:/data`.

Pass `--renew-before=720h` to make the command a no-op when more than 30 days of validity remain. This makes it safe to run on a fixed schedule.
Without programmatic access, sign a new server certificate with your existing CA (the CA registered in the Console doesn't change) and replace `data/tls.crt`. Set `TUNNEL_DOMAIN` first if you're running this from a fresh shell.

export TUNNEL_DOMAIN=YOUR_TUNNEL_DOMAIN_HERE
openssl req -new -key data/tls.key -out /tmp/server.csr \
  -subj "/CN=${TUNNEL_DOMAIN}"
openssl x509 -req -in /tmp/server.csr \
  -CA data/ca.crt -CAkey data/ca.key -CAcreateserial \
  -out data/tls.crt -days 90 \
  -extfile data/tls.ext

In either flow the proxy polls `tls.cert_file` and reloads it automatically, so no restart is required.
Next steps
[  Use the tunneled MCP servers Attach an upstream MCP server to a Managed Agent or the Messages API. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview#use-the-tunneled-mcp-servers)[  Security Hardening guidance, credential rotation, and breach response. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/security)[  Troubleshooting Diagnose connectivity, TLS, and routing issues. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/troubleshooting)
