<!-- source: https://platform.claude.com/docs/en/manage-claude/wif-providers/github-actions -->

# Use WIF with GitHub Actions
Authenticate GitHub Actions workflows to the Claude API with short-lived identity tokens instead of long-lived API keys.
Every GitHub Actions workflow run can request a signed identity token from GitHub's hosted issuer at `https://token.actions.githubusercontent.com`. With Workload Identity Federation, your workflow exchanges that token for a short-lived Anthropic access token, so your CI jobs can call the Claude API without an `ANTHROPIC_API_KEY` secret stored in your repository.
The token's `sub` claim encodes the repository and trigger context. For a push to a branch it has the form `repo:<owner>/<repo>:ref:refs/heads/<branch>`. Pull-request runs use `repo:<owner>/<repo>:pull_request`, and environment-gated deployments use `repo:<owner>/<repo>:environment:<name>`. Your federation rule matches against this claim (and others, such as `repository_owner` and `ref`) to decide which workflow runs are allowed to authenticate.
Prerequisites
  * Familiarity with [WIF concepts](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#concepts): service accounts, federation issuers, and federation rules.
  * A GitHub repository where you can edit workflow files and grant the `id-token: write` permission.
  * Permission to create service accounts, federation issuers, and federation rules in the Claude Console for your Anthropic organization.
  * Your Anthropic organization ID. You can find it in the Claude Console under **Settings → Organization**.

Configure your workflow
GitHub only issues an identity token to jobs that explicitly request it. Add the `id-token: write` permission at the workflow or job level:

permissions:
  id-token: write
  contents: read

Inside the job, the runner exposes two environment variables: `ACTIONS_ID_TOKEN_REQUEST_URL` and `ACTIONS_ID_TOKEN_REQUEST_TOKEN`. Call the request URL with the request token as a bearer credential and your chosen audience as a query parameter, then write the returned JSON Web Token (JWT) to a file:

- name: Fetch GitHub OIDC token
  run: |
    curl -sS -H "Authorization: Bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" \
      "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=https://api.anthropic.com" \
      | jq -r .value > /tmp/gha-jwt

If you prefer JavaScript, `actions/github-script` exposes the same capability through `core.getIDToken(audience)`:

- name: Fetch GitHub OIDC token
  uses: actions/github-script@v8
  with:
    script: |
      const fs = require('fs');
      const token = await core.getIDToken('https://api.anthropic.com');
      fs.writeFileSync('/tmp/gha-jwt', token);

The decoded token carries claims that describe the workflow run. Your federation rule matches against these:

  "iss": "https://token.actions.githubusercontent.com",
  "sub": "repo:your-org/your-repo:ref:refs/heads/main",
  "aud": "https://api.anthropic.com",
  "repository": "your-org/your-repo",
  "repository_owner": "your-org",
  "ref": "refs/heads/main",
  "sha": "abc123...",
  "workflow": "CI",
  "actor": "octocat",
  "event_name": "push"

See [GitHub's OIDC subject claim reference](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-subject-claims) for the full list of `sub` formats.
Configure Anthropic
In the Claude Console, open **Settings → Workload identity** , click **Connect workload** , and select the **GitHub Actions** tile. The wizard walks you through registering the issuer, creating a service account, and creating a federation rule.
The wizard creates these resources for you. Use the following values whether you enter them in the wizard or send them to the [Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api):
**Federation issuer:** GitHub publishes its OIDC discovery document and JWKS publicly, so use discovery mode. Anthropic refreshes the keys automatically when GitHub rotates them.

  "name": "github-actions",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": { "type": "discovery" }

**Federation rule:** Match only the workflow runs you intend to trust. See [Restrict which workflows can authenticate](https://platform.claude.com/docs/en/manage-claude/wif-providers/github-actions#restrict-which-workflows-can-authenticate) for how to scope these claims safely.

  "name": "gha-main",
  "issuer_id": "fdis_...",
  "match": {
    "subject_prefix": "repo:your-org/your-repo:ref:refs/heads/main",
    "audience": "https://api.anthropic.com",
    "claims": {
      "repository_owner": "your-org"
  "target": {
    "type": "service_account",
    "service_account_id": "svac_..."
  "workspace_id": "wrkspc_...",
  "oauth_scope": "workspace:developer",
  "token_lifetime_seconds": 600

Be as specific as the workload allows. Loosen `subject_prefix` to `repo:your-org/your-repo:*` (paired with a `claims.ref` constraint) only if the rule must match multiple event types from the same repository, because the trailing segment of `sub` varies between `ref:...`, `environment:...`, and `pull_request` events.
Acquire and use a token
Set the federation environment variables on the job and call the SDK normally. `Anthropic()` reads `ANTHROPIC_IDENTITY_TOKEN_FILE`, exchanges the JWT on the first request, and refreshes the access token automatically before it expires.
WorkflowcURLPythonTypeScriptGoJavaC#CLIPHPRuby

import anthropic

# Reads ANTHROPIC_FEDERATION_RULE_ID, ANTHROPIC_ORGANIZATION_ID,
# ANTHROPIC_SERVICE_ACCOUNT_ID, ANTHROPIC_WORKSPACE_ID, and ANTHROPIC_IDENTITY_TOKEN_FILE
# from the job environment.
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message.content[0].text)

Each GitHub-issued identity token expires roughly five minutes after issuance. The token-request endpoint (`ACTIONS_ID_TOKEN_REQUEST_URL`) stays valid for the entire job, so you can fetch a fresh token at any point. The SDK exchanges the token on first use and caches the resulting Anthropic access token. For jobs that run longer than the Anthropic token's lifetime, the SDK re-reads `ANTHROPIC_IDENTITY_TOKEN_FILE` on each refresh, so re-run the fetch step periodically (or wrap it in a background loop) to keep the file current. Alternatively, pass a token-provider callback to the SDK that calls `ACTIONS_ID_TOKEN_REQUEST_URL` directly instead of using the file path.
Verify the setup
A successful exchange returns an `access_token` beginning with `sk-ant-oat01-` and an `expires_in` value in seconds. On `400 invalid_grant`, see [Troubleshoot a failed exchange](https://platform.claude.com/docs/en/manage-claude/wif-reference#troubleshoot-a-failed-exchange); the most common GitHub Actions-side cause is the `sub` claim format not matching (its trailing segment varies between `ref:...`, `environment:...`, and `pull_request` events).
Restrict which workflows can authenticate

A `subject_prefix` of `repo:your-org/*` alone matches every repository in your organization, and without a `ref` constraint it also matches `pull_request` runs triggered from forks. Anyone who can open a pull request against a matching repository could obtain a federated Anthropic token.
Lock the rule's `match` block to the narrowest scope that fits your use case:
  * **Pin to a single repository:** Use `subject_prefix: "repo:your-org/your-repo:*"` so other repositories in the organization do not match.
  * **Pin to a protected branch:** Add `"ref": "refs/heads/main"` (or your release branch) under `claims` so pull-request runs and feature branches do not match.
  * **Pin the owner explicitly:** Add `"repository_owner": "your-org"` under `claims` as a defense-in-depth check against `sub` parsing edge cases.
  * **Pin to a deployment environment:** For deploy jobs, match `subject_prefix: "repo:your-org/your-repo:environment:production"` and gate that environment with required reviewers in GitHub.

Next steps
  * [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation): full setup walkthrough, environment variables, and credential precedence.
  * [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication): how federation compares to API keys.

  * [Prerequisites](https://platform.claude.com/docs/en/manage-claude/wif-providers/github-actions#prerequisites)
  * [Configure your workflow](https://platform.claude.com/docs/en/manage-claude/wif-providers/github-actions#configure-your-workflow)
  * [Configure Anthropic](https://platform.claude.com/docs/en/manage-claude/wif-providers/github-actions#configure-anthropic)
  * [Acquire and use a token](https://platform.claude.com/docs/en/manage-claude/wif-providers/github-actions#acquire-and-use-a-token)
  * [Verify the setup](https://platform.claude.com/docs/en/manage-claude/wif-providers/github-actions#verify-the-setup)
  * [Restrict which workflows can authenticate](https://platform.claude.com/docs/en/manage-claude/wif-providers/github-actions#restrict-which-workflows-can-authenticate)
  * [Next steps](https://platform.claude.com/docs/en/manage-claude/wif-providers/github-actions#next-steps)

Admin/Identity providers
# Use WIF with GitHub Actions
Authenticate GitHub Actions workflows to the Claude API with short-lived identity tokens instead of long-lived API keys.
Every GitHub Actions workflow run can request a signed identity token from GitHub's hosted issuer at `https://token.actions.githubusercontent.com`. With Workload Identity Federation, your workflow exchanges that token for a short-lived Anthropic access token, so your CI jobs can call the Claude API without an `ANTHROPIC_API_KEY` secret stored in your repository.
The token's `sub` claim encodes the repository and trigger context. For a push to a branch it has the form `repo:<owner>/<repo>:ref:refs/heads/<branch>`. Pull-request runs use `repo:<owner>/<repo>:pull_request`, and environment-gated deployments use `repo:<owner>/<repo>:environment:<name>`. Your federation rule matches against this claim (and others, such as `repository_owner` and `ref`) to decide which workflow runs are allowed to authenticate.
Prerequisites
  * Familiarity with [WIF concepts](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation#concepts): service accounts, federation issuers, and federation rules.
  * A GitHub repository where you can edit workflow files and grant the `id-token: write` permission.
  * Permission to create service accounts, federation issuers, and federation rules in the Claude Console for your Anthropic organization.
  * Your Anthropic organization ID. You can find it in the Claude Console under **Settings → Organization**.

Configure your workflow
GitHub only issues an identity token to jobs that explicitly request it. Add the `id-token: write` permission at the workflow or job level:

permissions:
  id-token: write
  contents: read

Inside the job, the runner exposes two environment variables: `ACTIONS_ID_TOKEN_REQUEST_URL` and `ACTIONS_ID_TOKEN_REQUEST_TOKEN`. Call the request URL with the request token as a bearer credential and your chosen audience as a query parameter, then write the returned JSON Web Token (JWT) to a file:

- name: Fetch GitHub OIDC token
  run: |
    curl -sS -H "Authorization: Bearer $ACTIONS_ID_TOKEN_REQUEST_TOKEN" \
      "$ACTIONS_ID_TOKEN_REQUEST_URL&audience=https://api.anthropic.com" \
      | jq -r .value > /tmp/gha-jwt

If you prefer JavaScript, `actions/github-script` exposes the same capability through `core.getIDToken(audience)`:

- name: Fetch GitHub OIDC token
  uses: actions/github-script@v8
  with:
    script: |
      const fs = require('fs');
      const token = await core.getIDToken('https://api.anthropic.com');
      fs.writeFileSync('/tmp/gha-jwt', token);

The decoded token carries claims that describe the workflow run. Your federation rule matches against these:

  "iss": "https://token.actions.githubusercontent.com",
  "sub": "repo:your-org/your-repo:ref:refs/heads/main",
  "aud": "https://api.anthropic.com",
  "repository": "your-org/your-repo",
  "repository_owner": "your-org",
  "ref": "refs/heads/main",
  "sha": "abc123...",
  "workflow": "CI",
  "actor": "octocat",
  "event_name": "push"

See [GitHub's OIDC subject claim reference](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect#example-subject-claims) for the full list of `sub` formats.
Configure Anthropic
In the Claude Console, open **Settings → Workload identity** , click **Connect workload** , and select the **GitHub Actions** tile. The wizard walks you through registering the issuer, creating a service account, and creating a federation rule.
The wizard creates these resources for you. Use the following values whether you enter them in the wizard or send them to the [Admin API](https://platform.claude.com/docs/en/manage-claude/wif-admin-api):
**Federation issuer:** GitHub publishes its OIDC discovery document and JWKS publicly, so use discovery mode. Anthropic refreshes the keys automatically when GitHub rotates them.

  "name": "github-actions",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": { "type": "discovery" }

**Federation rule:** Match only the workflow runs you intend to trust. See [Restrict which workflows can authenticate](https://platform.claude.com/docs/en/manage-claude/wif-providers/github-actions#restrict-which-workflows-can-authenticate) for how to scope these claims safely.

  "name": "gha-main",
  "issuer_id": "fdis_...",
  "match": {
    "subject_prefix": "repo:your-org/your-repo:ref:refs/heads/main",
    "audience": "https://api.anthropic.com",
    "claims": {
      "repository_owner": "your-org"
  "target": {
    "type": "service_account",
    "service_account_id": "svac_..."
  "workspace_id": "wrkspc_...",
  "oauth_scope": "workspace:developer",
  "token_lifetime_seconds": 600

Be as specific as the workload allows. Loosen `subject_prefix` to `repo:your-org/your-repo:*` (paired with a `claims.ref` constraint) only if the rule must match multiple event types from the same repository, because the trailing segment of `sub` varies between `ref:...`, `environment:...`, and `pull_request` events.
Acquire and use a token
Set the federation environment variables on the job and call the SDK normally. `Anthropic()` reads `ANTHROPIC_IDENTITY_TOKEN_FILE`, exchanges the JWT on the first request, and refreshes the access token automatically before it expires.
WorkflowcURLPythonTypeScriptGoJavaC#CLIPHPRuby

import anthropic

# Reads ANTHROPIC_FEDERATION_RULE_ID, ANTHROPIC_ORGANIZATION_ID,
# ANTHROPIC_SERVICE_ACCOUNT_ID, ANTHROPIC_WORKSPACE_ID, and ANTHROPIC_IDENTITY_TOKEN_FILE
# from the job environment.
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message.content[0].text)

Each GitHub-issued identity token expires roughly five minutes after issuance. The token-request endpoint (`ACTIONS_ID_TOKEN_REQUEST_URL`) stays valid for the entire job, so you can fetch a fresh token at any point. The SDK exchanges the token on first use and caches the resulting Anthropic access token. For jobs that run longer than the Anthropic token's lifetime, the SDK re-reads `ANTHROPIC_IDENTITY_TOKEN_FILE` on each refresh, so re-run the fetch step periodically (or wrap it in a background loop) to keep the file current. Alternatively, pass a token-provider callback to the SDK that calls `ACTIONS_ID_TOKEN_REQUEST_URL` directly instead of using the file path.
Verify the setup
A successful exchange returns an `access_token` beginning with `sk-ant-oat01-` and an `expires_in` value in seconds. On `400 invalid_grant`, see [Troubleshoot a failed exchange](https://platform.claude.com/docs/en/manage-claude/wif-reference#troubleshoot-a-failed-exchange); the most common GitHub Actions-side cause is the `sub` claim format not matching (its trailing segment varies between `ref:...`, `environment:...`, and `pull_request` events).
Restrict which workflows can authenticate

A `subject_prefix` of `repo:your-org/*` alone matches every repository in your organization, and without a `ref` constraint it also matches `pull_request` runs triggered from forks. Anyone who can open a pull request against a matching repository could obtain a federated Anthropic token.
Lock the rule's `match` block to the narrowest scope that fits your use case:
  * **Pin to a single repository:** Use `subject_prefix: "repo:your-org/your-repo:*"` so other repositories in the organization do not match.
  * **Pin to a protected branch:** Add `"ref": "refs/heads/main"` (or your release branch) under `claims` so pull-request runs and feature branches do not match.
  * **Pin the owner explicitly:** Add `"repository_owner": "your-org"` under `claims` as a defense-in-depth check against `sub` parsing edge cases.
  * **Pin to a deployment environment:** For deploy jobs, match `subject_prefix: "repo:your-org/your-repo:environment:production"` and gate that environment with required reviewers in GitHub.

Next steps
  * [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation): full setup walkthrough, environment variables, and credential precedence.
  * [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication): how federation compares to API keys.
