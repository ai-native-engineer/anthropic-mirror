<!-- source: https://platform.claude.com/cookbook/misc-admin-api -->

#  Manage your organization with the Admin API

Onboarding a team onto the Claude API means the same Console clicks every time: invite each person, create a workspace, add members, check which API keys exist, and set up an identity for CI. Doing that by hand leaves no record and doesn't scale past a few teams.

The Admin API exposes those controls as REST endpoints under `/v1/organizations`, and the Python SDK wraps them as `client.beta.organization`. This notebook onboards a team end to end, audits the organization's API keys along the way, and then removes everything it created.

**By the end of this notebook, you'll be able to:**

* Authenticate as an organization admin with an OAuth login or a Console Admin API key
* Invite users, set organization roles, and create a workspace with members
* Audit the organization's API keys and read its rate limits
* Create a service account for automation and grant it workspace access

The same calls work unchanged in a provisioning script or a scheduled audit job.

##  Prerequisites

* Python fundamentals, and familiarity with Claude Console organizations, workspaces, and API keys
* Python 3.11+ and `anthropic>=1.1.0`, the first release with `client.beta.organization`
* A Claude Console **organization** where you hold the `admin`, `owner`, or `primary_owner` role. The Admin API isn't available for individual accounts.
* Optional: the [`ant` CLI(opens in new tab)](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication) for the OAuth login path

##  Authenticate as an admin

API keys scoped to a single workspace can't call the Admin API. It accepts three credentials: an `org:admin` OAuth token, an Admin API key, and a personal or service account key that isn't scoped to one workspace. This notebook uses the first two, and only organization admins can create either:

| Credential | How to get it | Coverage |
| --- | --- | --- |
| OAuth token with the `org:admin` scope | `ant auth login --profile admin --scope org:admin` | Every endpoint in this notebook |
| Admin API key (`sk-ant-admin01-...`) | Claude Console → Settings → [Admin keys(opens in new tab)](https://platform.claude.com/settings/admin-keys) | Everything except service accounts and workload identity federation |

The OAuth login opens a browser, asks you to pick the organization, and stores a refreshable token under `~/.config/anthropic/`. The SDK loads it when you construct the client with `profile="admin"`.

To use an Admin API key instead, add `ANTHROPIC_ADMIN_API_KEY=sk-ant-admin01-...` to a `.env` file next to this notebook. The setup cell uses the key if it's set and falls back to the OAuth profile otherwise.

%%capture

%pip install -U "anthropic>=1.1.0" python-dotenv

import os

import time

from datetime import UTC, datetime

from itertools import islice

import anthropic

from dotenv import load\_dotenv

load\_dotenv()

ADMIN\_KEY = os.getenv("ANTHROPIC\_ADMIN\_API\_KEY")

# The profile name you passed to `ant auth login --profile`.

PROFILE = os.getenv("ANTHROPIC\_PROFILE", "admin")

# Only used to pick which rate limit group to print.

MODEL = "claude-sonnet-5"

if ADMIN\_KEY:

client = anthropic.Anthropic(api\_key=ADMIN\_KEY)

else:

client = anthropic.Anthropic(profile=PROFILE)

org = client.beta.organization.retrieve()

auth = "an Admin API key" if ADMIN\_KEY else f"OAuth profile {PROFILE!r}"

print(f"Connected to {org.name} ({org.id}) with {auth}")

```
Connected to Example Org (1f6e8a52-93c4-4d7b-a1e0-5b2c9d8e4f37) with OAuth profile 'admin'
```

`organization.retrieve()` calls `GET /v1/organizations/me`. Check the name before going further: an admin credential is bound to one organization, and every call that follows reads or writes it.

The rest of the notebook names what it creates after one team, so you can spot it in the Console.

RUN\_ID = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")

TEAM = f"research-{RUN\_ID}"

print(TEAM)

```
research-20260826-180659
```

##  Invite teammates and set roles

An invite emails the recipient a sign-up link and records the role they get when they accept. For Console organizations the API accepts `user`, `developer`, `billing`, and `claude_code_user`. The `admin` role can only be granted in the Console.

Start new members as `user`, which grants Console and playground access without API keys, and promote them when they need more.

An invite sends a real email. Some organizations accept invites only to their own email domain, and an invite to any other domain returns a `400`. The next cell defaults to a placeholder address on an existing admin's domain so it runs in any organization. Set `INVITE_EMAIL` to a teammate's address to try the full flow.

INVITE\_EMAIL = os.getenv("INVITE\_EMAIL")

if not INVITE\_EMAIL:

# Invites to other domains return a 400 in organizations that restrict invite domains.

users = client.beta.organization.users.list(limit=100)

admin = next((u for u in users if u.role in {"admin", "owner", "primary\_owner"}), None)

if admin is None:

raise RuntimeError("No admin user to borrow an email domain from. Set INVITE\_EMAIL.")

INVITE\_EMAIL = f"new.teammate+{RUN\_ID}@{admin.email.split('@', 1)[1]}"

invite = client.beta.organization.invites.create(email=INVITE\_EMAIL, role="user")

print(f"{invite.id} {invite.email} role={invite.role} status={invite.status}")

print(f"expires {invite.expires\_at:%Y-%m-%d}")

```
invite_015gWxHNr6h6TdRPZTmuCGnn  new.teammate+20260826-180659@example.com  role=user  status=pending
expires 2026-09-16
```

Invites expire after 21 days. `invites.list()` returns every invite in the organization with its status, and `invites.delete()` revokes a pending one.

for inv in client.beta.organization.invites.list(limit=100):

print(f"{inv.email:<45} {inv.role:<16} {inv.status:<9} sent {inv.invited\_at:%Y-%m-%d}")

```
new.teammate+20260826-180659@example.com                 user             pending   sent 2026-08-26
```

Once someone accepts, they show up in `users.list()`. The next cell prints the first 10. Filter by `email` to find one person, then change their role with `users.update()` or offboard them with `users.remove()`. Admins can't be removed through the API.

While the invite is pending, the next cell finds no user and skips the promotion, and the membership cell later skips the add. Both run once the invite is accepted.

# Iterating a list call fetches every page, so cap what gets printed.

for user in islice(client.beta.organization.users.list(limit=100), 10):

print(f"{user.email:<45} {user.role:<16} joined {user.added\_at:%Y-%m-%d}")

teammate = next(iter(client.beta.organization.users.list(email=INVITE\_EMAIL)), None)

if teammate is None:

print(f"\n{INVITE\_EMAIL} hasn't accepted yet, nothing to promote")

else:

teammate = client.beta.organization.users.update(teammate.id, role="developer")

print(f"\n{teammate.email} is now {teammate.role}")

```
ada@example.com                              admin            joined 2026-06-01

new.teammate+20260826-180659@example.com hasn't accepted yet, nothing to promote
```

##  Create a workspace for the team

Workspaces partition API keys, spend limits, rate limits, and usage reporting inside one organization. One workspace per team or per environment is the usual layout. `tags` carry your own metadata, such as a cost center, and come back on every read.

workspace = client.beta.organization.workspaces.create(

name=TEAM,

tags={"team": "research", "cost-center": "4711"},

)

print(workspace.id, workspace.name, workspace.tags)

```
wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ research-20260826-180659 {'team': 'research', 'cost-center': '4711'}
```

`workspaces.update()` changes the name, display color, or tags. Tags merge with what's already there, and setting a tag to `None` removes it.

workspace = client.beta.organization.workspaces.update(

workspace.id, tags={"env": "sandbox", "cost-center": None}

)

print(workspace.tags)

```
{'env': 'sandbox', 'team': 'research'}
```

Organization admins and billing users are implicit members of every workspace and don't appear in `members.list()`. Everyone else needs an explicit workspace role, such as `workspace_user`, `workspace_developer`, or `workspace_admin`.

`members.update()` changes a role and `members.remove()` drops someone from the workspace without touching their organization membership.

if teammate:

client.beta.organization.workspaces.members.add(

workspace.id, user\_id=teammate.id, workspace\_role="workspace\_developer"

)

members = list(client.beta.organization.workspaces.members.list(workspace.id))

print(f"{workspace.name}: {len(members)} explicit member(s)")

for m in members:

print(f" {m.user\_id} {m.workspace\_role}")

```
research-20260826-180659: 0 explicit member(s)
```

##  Audit API keys

The Admin API lists, renames, deactivates, and archives API keys, but it can't create them: new keys come from the Console only. Use it for a scheduled audit, not for provisioning.

The next cell walks every active key in the organization and flags keys older than `MAX_KEY_AGE_DAYS` and keys with no expiry.

MAX\_KEY\_AGE\_DAYS = 90

now = datetime.now(UTC)

# The default workspace isn't returned by workspaces.list(), so any ID missing here is it.

workspace\_names = {w.id: w.name for w in client.beta.organization.workspaces.list(limit=1000)}

flagged = []

for key in client.beta.organization.api\_keys.list(status="active", limit=1000):

if key.scope.type == "workspace":

where = workspace\_names.get(key.scope.workspace\_id, "Default")

else:

where = "(organization)"

age = (now - key.created\_at).days

expires = f"{key.expires\_at:%Y-%m-%d}" if key.expires\_at else "never"

flags = []

if age > MAX\_KEY\_AGE\_DAYS:

flags.append("old")

if key.expires\_at is None:

flags.append("no-expiry")

if flags:

flagged.append(key)

hint = key.partial\_key\_hint or "-"

print(f"{key.name:<28} {where:<18} {hint:<24}", end=" ")

print(f"{age:>4}d expires {expires:<10} {' '.join(flags)}")

print(f"\n{len(flagged)} key(s) flagged")

```
backend-prod                 production         sk-ant-api03-R2D...igAA    14d  expires 2027-08-12
ci-deploy                    production         sk-ant-api03-9xQ...0mAA    14d  expires 2026-12-09

0 key(s) flagged
```

Deactivating a key is reversible (`status="active"` turns it back on). Archiving is not. Leave `APPLY = False` for a dry run, or set it to `True` to deactivate the flagged keys.

Read the flagged list first. A key with no expiry is flagged even if it serves production traffic, and a deactivated key starts failing requests immediately.

APPLY = False

if not flagged:

print("no flagged keys, nothing to do")

for key in flagged:

if APPLY:

key = client.beta.organization.api\_keys.update(key.id, status="inactive")

print(f"{key.name:<28} -> {key.status}{'' if APPLY else ' (dry run, unchanged)'}")

```
no flagged keys, nothing to do
```

##  Create a service account for automation

A service account is a non-human member of the organization for CI jobs and backend services. It holds an organization role and workspace roles like a person does, so credentials issued to it don't depend on an employee's account. The service account endpoints accept only the `org:admin` OAuth credential. An Admin API key is rejected here.

`name` is a slug of lowercase letters, digits, and hyphens, and it must be unique in the organization. The service account endpoints can lag behind creation. An object created a few seconds ago can briefly return `404` from these endpoints, or be missing from a list. Retry on `404` when a call references something you just created, which is what the helper in the next cell does.

# New objects can briefly 404 on the service account endpoints.

def retry\_on\_not\_found(call, attempts: int = 6, delay: float = 5.0):

for attempt in range(attempts):

try:

return call()

except anthropic.NotFoundError:

if attempt == attempts - 1:

raise

time.sleep(delay)

service\_account = None

if ADMIN\_KEY:

print("Skipped: service account endpoints need the org:admin OAuth credential")

else:

service\_account = client.beta.organization.service\_accounts.create(

name=f"ci-{TEAM}",

description="Deploy pipeline for the research team",

)

print(service\_account.id, service\_account.name, service\_account.organization\_role)

```
svac_01ABCDEFabcdef0123456789XY ci-research-20260826-180659 developer
```

Grant it a role in the team workspace, then list its memberships. Every service account is also an implicit `workspace_user` in the default workspace, and a grant made seconds ago can take a moment to appear in the list.

if service\_account:

grant = retry\_on\_not\_found(

lambda: client.beta.organization.service\_accounts.workspaces.add(

service\_account.id, workspace\_id=workspace.id, workspace\_role="workspace\_developer"

)

)

print(f"granted {grant.workspace\_role} in {workspace.name}\n")

for m in client.beta.organization.service\_accounts.workspaces.list(service\_account.id):

name = workspace.name if m.workspace\_id == workspace.id else "Default"

print(f"{name:<28} {m.workspace\_role:<22} {'implicit' if m.implicit else 'explicit'}")

```
granted workspace_developer in research-20260826-180659

Default                      workspace_user         implicit
research-20260826-180659     workspace_developer    explicit
```

To let a pipeline authenticate as this service account without storing a secret, register your CI provider as a federation issuer and add a rule that maps its OIDC tokens to the account. [Workload identity federation(opens in new tab)](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) covers that setup.

##  Check rate limits

Rate limits are set per organization. Each group covers a model family or another part of the API, such as `batch`, `files`, or `web_search`. `rate_limits.list()` returns every group. The next cell prints the group that covers `MODEL`, which the setup cell defines, plus the groups that aren't tied to a model.

for rl in client.beta.organization.rate\_limits.list():

if rl.group\_type == "model\_group" and MODEL not in (rl.models or []):

continue

label = MODEL if rl.group\_type == "model\_group" else rl.group\_type

limits = ", ".join(f"{limit.type}={limit.value:,}" for limit in rl.limits)

print(f"{label:<18} {limits}")

```
batch              enqueued_batch_requests=500,000, requests_per_minute=4,000
claude-sonnet-5    input_tokens_per_minute=10,000,000, output_tokens_per_minute=2,000,000, requests_per_minute=10,000
```

Workspaces inherit those values. An admin can cap a workspace lower in the Console, and `workspaces.rate_limits.list()` returns only the values that were overridden.

overrides = list(client.beta.organization.workspaces.rate\_limits.list(workspace.id))

if not overrides:

print(f"{workspace.name} has no overrides and inherits the organization limits")

for rl in overrides:

print(rl.group\_type, rl.models, [(limit.type, limit.value) for limit in rl.limits])

```
research-20260826-180659 has no overrides and inherits the organization limits
```

##  Clean up

Remove what this notebook created. **Archiving a workspace is permanent and revokes every API key in it**, so double-check `workspace.name` before running this against a real organization. Archived workspaces don't count toward the 100-workspace limit.

If an earlier cell raised, run this cell by hand. It needs `workspace`, `service_account`, and `invite` from the kernel.

archived = client.beta.organization.workspaces.archive(workspace.id)

print(f"archived workspace {archived.name} at {archived.archived\_at:%Y-%m-%d %H:%M}")

if service\_account:

retry\_on\_not\_found(

lambda: client.beta.organization.service\_accounts.archive(service\_account.id)

)

print(f"archived service account {service\_account.name}")

# Deleting an accepted invite returns a 400, because that person is a member now.

if client.beta.organization.invites.retrieve(invite.id).status == "pending":

client.beta.organization.invites.delete(invite.id)

print(f"deleted invite for {invite.email}")

else:

print(f"{invite.email} joined the organization, offboard them with users.remove()")

```
archived workspace research-20260826-180659 at 2026-08-26 18:07
archived service account ci-research-20260826-180659
deleted invite for new.teammate+20260826-180659@example.com
```

##  Next steps

You authenticated as an admin, invited a user, created a workspace, gave a service account access to it, audited the organization's API keys, and read its rate limits, all through `client.beta.organization`.

Related admin surfaces that aren't covered here:

* [Usage and cost cookbook(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/misc/../observability/usage_cost_api.ipynb) and the [Usage and Cost API(opens in new tab)](https://platform.claude.com/docs/en/manage-claude/usage-cost-api): token and dollar reporting by workspace, key, and model
* [Claude Code Analytics API(opens in new tab)](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api): per-user Claude Code activity for the organization
* [Workload identity federation(opens in new tab)](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation): keyless authentication for the service account you created, via `client.beta.organization.federation`
* [Admin API reference(opens in new tab)](https://platform.claude.com/docs/en/api/admin): every endpoint, including the ones the SDK exposes under `external_keys` and `federation`
