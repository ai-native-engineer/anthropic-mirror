<!-- source: https://platform.claude.com/cookbook/managed-agents-cma-operate-in-production -->

#  Operate: running Managed Agents in production

Most of the other Managed Agents cookbooks focus on the agent loop itself, getting an agent to do something useful against a fixture. This one is about the machinery around that loop, the pieces you need before you can put a Managed Agents app in front of real users:

1. **MCP toolsets** instead of custom tools, when your agent needs to talk to a SaaS API without round-tripping every call through your application.
2. **Vaults** to hold per-end-user credentials, so each user's GitHub / Linear / Slack tokens stay separate from everyone else's and your audit trail is clean.
3. **Webhooks** to drive human-in-the-loop work without holding a long-lived HTTP connection open the whole time.
4. **Resource lifecycle** verbs (list, retrieve, update, archive, delete) for managing what your workspace accumulates over time.
5. **Inference geography pinning** (`inference_geo`) when compliance requires model requests to run in a specific region.

We'll build one end-to-end flow that touches the first four, then close with the geography pin: create a vault for a fictional end user, attach a GitHub MCP credential to it, run an agent session that uses the credential server-side, show the webhook handler you'd register to drive the same session from a real production server, and walk through the management verbs you'd use to clean up afterwards.

This notebook needs `GITHUB_TOKEN` in your environment.



import os

from anthropic import Anthropic

from utilities import stream\_until\_end\_turn, wait\_for\_idle\_status

MODEL = os.environ.get("COOKBOOK\_MODEL", "claude-sonnet-4-6")

client = Anthropic()

GH\_TOKEN = os.environ.get("GITHUB\_TOKEN")

if not GH\_TOKEN:

raise SystemExit("Set GITHUB\_TOKEN to run this notebook.")

##  Concepts: MCP toolsets and vaults

**MCP toolsets** are the third extension pattern, after custom tools (the gate notebook) and `resources=` mounts (the orchestrate notebook). An MCP toolset points the agent at an external server that implements the [Model Context Protocol(opens in new tab)](https://modelcontextprotocol.io/). The agent calls tools on that server directly from inside the sandbox, with no round-trip through your application, Anthropic proxies the calls, the server responds, and the agent keeps going. The vast majority of public SaaS APIs (GitHub, Slack, Linear, Stripe, Notion, Salesforce, Asana...) either already have an MCP server or can be wrapped in one in an afternoon, and any of them are good MCP candidates.

Rule of thumb: if the service is reachable over the public internet with a bearer token, an MCP toolset will work. If it's only reachable from inside your own network, use a custom tool instead, which is what the gate notebook covers.

**Vaults** are the answer to the question "where do I put the tokens?" Hard-coding a single token at session creation time works for a one-tenant setup, but it falls apart the moment you have end users. Each user needs their own GitHub credential, and you need to keep them isolated from each other. A vault is a per-user container of credentials that you register once and then reference by ID on every session you create for that user. You don't run your own secret store, you don't pass tokens on every request, and the audit trail is tied to the vault so you always know which end user an agent was acting for.

##  1. Create a vault for an end user

A vault has a `display_name` that shows up in the Console and a `metadata` dict where you'd typically store your internal user ID, so you can map the vault back to a record in your own database.



vault = client.beta.vaults.create(

display\_name="Cookbook demo user",

metadata={"internal\_user\_id": "u\_demo\_001", "team": "engineering"},

)

print(f"vault: {vault.id}")

##  2. Attach an MCP credential

Credentials live under a vault. Each credential pairs an MCP server URL with a token the agent uses when calling that server. For the GitHub Copilot MCP server, a static bearer token (your GitHub PAT) is the simplest form. The API also supports a full OAuth flow with refresh for services that require it, both shapes are handled through `auth=`.



credential = client.beta.vaults.credentials.create(

vault\_id=vault.id,

display\_name="GitHub Copilot",

auth={

"type": "static\_bearer",

"mcp\_server\_url": "https://api.githubcopilot.com/mcp/",

"token": GH\_TOKEN,

},

)

print(f"credential: {credential.id}")

##  3. Reference the vault on a session

Pass `vault_ids=[vault.id]` on `sessions.create` and the API looks up the matching MCP server URL on every tool call. The agent never sees the token itself, and you don't have to pass it on the request. The agent definition just lists the MCP server as usual, the credential wiring happens at session creation time.



agent = client.beta.agents.create(

name="cookbook-operate",

model=MODEL,

system="You navigate GitHub repositories on behalf of the logged-in user.",

mcp\_servers=[

{

"type": "url",

"name": "github",

"url": "https://api.githubcopilot.com/mcp/",

}

],

tools=[

{

"type": "mcp\_toolset",

"mcp\_server\_name": "github",

"default\_config": {

"enabled": True,

"permission\_policy": {"type": "always\_allow"},

},

}

],

)

env = client.beta.environments.create(

name="cookbook-operate-env",

config={"type": "cloud", "networking": {"type": "unrestricted"}},

)

session = client.beta.sessions.create(

environment\_id=env.id,

agent={"type": "agent", "id": agent.id, "version": agent.version},

vault\_ids=[vault.id],

title="Operate demo",

)

print(f"session: {session.id}")

##  4. Run a turn as the end user

Everything the agent does against GitHub now flows through the vault's credential. Auditing in your own systems is straightforward: you know exactly which end user was acting because the vault is tied to them via the metadata you set in step 1.



client.beta.sessions.events.send(

session\_id=session.id,

events=[

{

"type": "user.message",

"content": [

{

"type": "text",

"text": "List the three most recently updated repos in the anthropics org.",

}

],

}

],

)

print("--- vault-backed MCP call ---")

stream\_until\_end\_turn(client, session.id)

##  5. Webhooks for production HITL

The streaming pattern in the gate notebook is convenient during development because everything happens in one process, but it holds an HTTP connection open while a human reviews, that doesn't scale, and it doesn't survive process restarts. The production pattern instead registers a webhook in the Console that fires on `session.status_idled`, which is the signal that the agent is either done OR waiting on a tool result.

When the webhook fires, your server inspects the events, puts any pending escalation in front of a reviewer, and POSTs the `user.custom_tool_result` back whenever the human finishes. The session simply sits idle until you respond, with no long-lived connection on your side.

If your sessions run with a `budget` (see [`CMA_cap_session_spend.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_cap_session_spend.ipynb)), also register for `session.budget_reached`. It fires once when a session's list cost reaches its cap, and it's the signal a supervisor process needs to decide, per session, whether to raise the cap or leave the work paused. It carries the session id, so the handler is the same shape as the idle one: look up the session, decide, act.

Webhook registration is a one-time Console step under **Settings → Webhooks**. You'll get a `whsec_...` signing secret that is shown only once at creation; store it in your secrets manager.

**The block below is a reference implementation, not a notebook cell.** Copy it into your own server, it depends on FastAPI, which the cookbook doesn't install, and it's not run as part of this notebook's flow. Paired with the agent definition from the gate notebook, it's enough to drive the gate workflow end-to-end from a production server.



import hmac

import hashlib

import json

from fastapi import FastAPI, Header, HTTPException, Request

app = FastAPI()

WEBHOOK\_SECRET = "whsec\_..." # from Console, load from your secrets manager

def verify(body: bytes, sig: str) -> bool:

expected = hmac.new(WEBHOOK\_SECRET.encode(), body, hashlib.sha256).hexdigest()

return hmac.compare\_digest(expected, sig)

@app.post("/webhooks/anthropic")

async def receive(req: Request, x\_anthropic\_signature: str = Header()):

body = await req.body()

if not verify(body, x\_anthropic\_signature):

raise HTTPException(401)

event = json.loads(body)

session\_id = event["resource\_id"]

if event["event\_type"] == "session.status\_idled":

# Agent went idle. Either it's done OR it called escalate()

# and is waiting on a user.custom\_tool\_result. Look at the

# latest events to decide.

events = client.beta.sessions.events.list(session\_id=session\_id)

pending = [

e for e in events.data

if e.type == "agent.custom\_tool\_use" and e.name == "escalate"

and not has\_result(events, e.id)

]

if pending:

for tu in pending:

enqueue\_for\_review(session\_id, tu.id, tu.input)

else:

finalize\_run(session\_id)

elif event["event\_type"] == "session.budget\_reached":

# Session paused at its spend cap with its work intact. Raise

# the budget to let it continue, or leave it paused and page

# an operator.

review\_budget(session\_id)

return {"ok": True}

# Called from your review UI once the human decides

def submit\_review(session\_id: str, custom\_tool\_use\_id: str, decision: str):

client.beta.sessions.events.send(

session\_id=session\_id,

events=[{

"type": "user.custom\_tool\_result",

"custom\_tool\_use\_id": custom\_tool\_use\_id,

"content": [{"type": "text",

"text": json.dumps({"human\_decision": decision})}],

}],

)

The code that responds to the agent is identical to the Part A loop in the gate notebook. The only thing that changes is how your server learns there's work to do: instead of a local loop pulling events, webhooks push notifications on your schedule.

##  6. Pin inference geography

When compliance requires model requests to be served from a specific geography, pin it on the agent rather than relying on the workspace default:



agent = client.beta.agents.create(

name="residency-pinned agent",

model={"id": MODEL, "inference\_geo": "us"},

...

)

Accepted values are `"global"` and `"us"`, bounded by the workspace's `allowed_inference_geos`. Unset, each request resolves to the workspace's `default_inference_geo` at serving time, so a later change to that default reaches sessions already running. Set, the pin is validated when the agent is saved, when a session is created, and on every turn: narrowing the workspace allowlist blocks new sessions from a now-disallowed agent and refuses the next turn of a running one, rather than grandfathering it. That strictness is what makes the pin usable as a residency control. `agent_with_overrides` on `sessions.create` moves a single session to another allowed geography without editing the shared agent. The full walkthrough, including the update semantics that clear the pin, is in [`CMA_pin_inference_geo.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_pin_inference_geo.ipynb).

##  7. Resource lifecycle: list, retrieve, update, archive

Every resource in the API, agents, environments, sessions, vaults, credentials, exposes the same five-verb pattern: `list`, `retrieve`, `update`, `archive`, and (for some) `delete`. We'll demonstrate the full set on agents, then list the verbs available on each other resource as a quick reference.

**archive vs delete:** `archive` keeps the record around for audit and retrieval but tears down any live container and stops the resource counting against your workspace quotas. `delete` removes the record entirely. For most workflows `archive` is the right call; reach for `delete` only when you specifically need the record gone (e.g. test cleanup).



listed = client.beta.agents.list(limit=5)

print(f"workspace has at least {len(listed.data)} agents")

retrieved = client.beta.agents.retrieve(agent.id)

print(f"retrieved agent: name={retrieved.name} version={retrieved.version}")

# Updating an agent produces a new version. Pass the current

# version to confirm you're updating from a known state, a

# concurrent update from another process will reject yours rather

# than silently overwriting.

updated = client.beta.agents.update(

agent.id,

version=agent.version,

system="You navigate GitHub repositories. Be terse.",

)

print(f"updated to version {updated.version}")

# Every historical version is queryable.

versions = client.beta.agents.versions.list(agent\_id=agent.id)

print(f"agent has {len(versions.data)} versions")

##  8. Cleanup

Credentials and vaults have their own archive endpoints. Archiving a vault does NOT automatically archive its credentials, so do the credentials first if you want a clean sweep.



wait\_for\_idle\_status(client, session.id)

client.beta.sessions.archive(session.id)

client.beta.environments.archive(env.id)

client.beta.agents.archive(agent.id)

client.beta.vaults.credentials.archive(credential.id, vault\_id=vault.id)

client.beta.vaults.archive(vault.id)

print("archived")

##  The other cookbooks

This notebook is the production-shaped bookend. The workflow notebooks it wraps around are worth running first if you haven't already:

* [`CMA_iterate_fix_failing_tests.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_iterate_fix_failing_tests.ipynb) — the entry-point notebook. Introduces agents, environments, sessions, file mounts, and the streaming event loop through a do-observe-fix loop on a failing test suite.
* [`CMA_orchestrate_issue_to_pr.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_orchestrate_issue_to_pr.ipynb) — multi-turn agent that drives an issue all the way to a merged PR through a mock gh CLI, with mid-chain recovery from a CI failure and a review comment.
* [`CMA_explore_unfamiliar_codebase.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_explore_unfamiliar_codebase.ipynb) — the grounding pattern, with a planted stale-doc trap. Also shows `sessions.resources.add` for pushing more context into a running session.
* [`CMA_gate_human_in_the_loop.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_gate_human_in_the_loop.ipynb) — custom-tool `decide()` and `escalate()` round-trip for human-in-the-loop workflows, paired with the webhook reference block above.
